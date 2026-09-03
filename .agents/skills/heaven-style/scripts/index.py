#!/usr/bin/env python3
"""Validate heaven-style metadata and generate its compact routing index."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES = SKILL_ROOT / "references"
INDEX_PATH = REFERENCES / "index.yaml"
COLLECTIONS = ("rules", "examples", "design", "workflows", "tasks", "failures")
REQUIRED_FIELDS = {
    "rules": ("id", "title", "description"),
    "examples": ("id", "title", "description"),
    "design": ("id", "title", "description"),
    "workflows": ("id", "title", "description"),
    "tasks": ("id", "task_kind", "description"),
    "failures": ("id", "title", "description"),
}


class IndexValidationError(ValueError):
    """Aggregate deterministic skill-index diagnostics."""

    def __init__(self, errors: list[str]) -> None:
        super().__init__("\n".join(errors))
        self.errors = errors


class _IndentedDumper(yaml.SafeDumper):
    """Indent sequence items beneath their mapping owner."""

    def increase_indent(self, flow: bool = False, indentless: bool = False) -> None:
        return super().increase_indent(flow, False)


def _relative(path: Path, root: Path) -> str:
    """Return a stable skill-root-relative POSIX path."""
    return path.resolve().relative_to(root.resolve()).as_posix()


def _load_frontmatter(path: Path, root: Path, errors: list[str]) -> dict[str, object] | None:
    """Parse YAML frontmatter and fail closed on malformed input."""
    relative = _relative(path, root)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"READ_ERROR: {relative}: {exc}")
        return None
    match = FRONTMATTER_RE.match(text)
    if not match:
        errors.append(f"FRONTMATTER_MISSING: {relative}")
        return None
    try:
        metadata = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f"FRONTMATTER_INVALID: {relative}: {exc}")
        return None
    if not isinstance(metadata, dict):
        errors.append(f"FRONTMATTER_MAPPING: {relative}")
        return None
    return metadata


def _rule_category(path: Path, root: Path) -> str:
    """Infer the compact rule family from its path."""
    relative = _relative(path, root)
    if "/rules/code/python/" in f"/{relative}":
        return "python"
    if "/rules/code/typescript/" in f"/{relative}":
        return "typescript"
    if "/rules/code/rust/" in f"/{relative}":
        return "rust"
    if "/rules/project/" in f"/{relative}":
        return "project"
    return "overview"


def _markdown_links(path: Path) -> Iterable[str]:
    """Yield Markdown links outside fenced code blocks."""
    fenced = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        for match in LINK_RE.finditer(line):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            elif ' "' in target:
                target = target.split(' "', 1)[0]
            yield target


def _validate_links(root: Path, paths: Iterable[Path], errors: list[str]) -> None:
    """Reject broken local links in distributed skill Markdown."""
    for source in sorted(paths):
        for raw_target in _markdown_links(source):
            if raw_target.startswith(("#", "http://", "https://", "mailto:", "skill://")):
                continue
            target = unquote(raw_target.split("#", 1)[0])
            if not target:
                continue
            if Path(target).is_absolute():
                errors.append(f"LINK_ABSOLUTE: {_relative(source, root)} -> {raw_target}")
                continue
            resolved = (source.parent / target).resolve()
            if root.resolve() not in resolved.parents and resolved != root.resolve():
                errors.append(f"LINK_ESCAPE: {_relative(source, root)} -> {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"LINK_MISSING: {_relative(source, root)} -> {raw_target}")


def _reference_paths(root: Path, collection: str) -> list[Path]:
    """Return stable Markdown sources for one collection."""
    base = root / "references" / collection
    if not base.is_dir():
        return []
    return sorted(path for path in base.rglob("*.md") if not path.name.startswith("_"))


def _compact_entry(collection: str, path: Path, root: Path, metadata: dict[str, object]) -> tuple[str, dict[str, object]]:
    """Project canonical frontmatter into one compact route."""
    entry: dict[str, object] = {
        "path": _relative(path, root),
        "use": metadata["description"],
    }
    if collection == "rules":
        entry["family"] = metadata.get("category") or _rule_category(path, root)
        if metadata.get("blocking") is True:
            entry["blocking"] = True
    elif collection == "workflows" and metadata.get("audience"):
        entry["audience"] = metadata["audience"]
    elif collection == "tasks" and metadata.get("task_kind") != metadata.get("id"):
        entry["kind"] = metadata["task_kind"]
    if metadata.get("enabled") is False:
        entry["enabled"] = False
    if metadata.get("default_exposed") is False:
        entry["default"] = False
    return str(metadata["id"]), entry


def _collect_references(root: Path, errors: list[str]) -> tuple[dict[str, dict[str, dict[str, object]]], list[Path]]:
    """Validate reference metadata and return compact routes plus sources."""
    routes: dict[str, dict[str, dict[str, object]]] = {}
    sources: list[Path] = []
    identifiers: dict[str, str] = {}
    rules: set[str] = set()
    pending_relations: list[tuple[str, str, list[object]]] = []
    for collection in COLLECTIONS:
        records: list[tuple[int, str, dict[str, object]]] = []
        for path in _reference_paths(root, collection):
            sources.append(path)
            metadata = _load_frontmatter(path, root, errors)
            if metadata is None:
                continue
            relative = _relative(path, root)
            for field in REQUIRED_FIELDS[collection]:
                if field not in metadata or metadata[field] in (None, ""):
                    errors.append(f"FIELD_MISSING: {relative}: {field}")
                elif not isinstance(metadata[field], str):
                    errors.append(f"FIELD_TYPE: {relative}: {field} must be a string")
            identifier = metadata.get("id")
            if not isinstance(identifier, str) or not identifier.strip():
                errors.append(f"ID_INVALID: {relative}")
                continue
            if identifier in identifiers:
                errors.append(f"ID_DUPLICATE: {identifier}: {identifiers[identifier]} and {relative}")
                continue
            identifiers[identifier] = relative
            if collection == "rules":
                rules.add(identifier)
            if "enabled" in metadata and not isinstance(metadata["enabled"], bool):
                errors.append(f"ENABLED_INVALID: {relative}")
            for field in ("blocking", "default_exposed"):
                if field in metadata and not isinstance(metadata[field], bool):
                    errors.append(f"FIELD_TYPE: {relative}: {field} must be a boolean")
            if "order" in metadata and type(metadata["order"]) is not int:
                errors.append(f"FIELD_TYPE: {relative}: order must be an integer")
            for field in ("category", "audience", "status"):
                if field in metadata and not isinstance(metadata[field], str):
                    errors.append(f"FIELD_TYPE: {relative}: {field} must be a string")
            for field in ("keywords", "triggers"):
                value = metadata.get(field)
                if value is not None and (not isinstance(value, list) or not all(isinstance(item, str) for item in value)):
                    errors.append(f"FIELD_TYPE: {relative}: {field} must be a string list")
            related = metadata.get("related_rules")
            if related is not None:
                if not isinstance(related, list):
                    errors.append(f"RELATED_RULES_INVALID: {relative}")
                else:
                    pending_relations.append((identifier, relative, related))
            if any(field not in metadata or metadata[field] in (None, "") for field in REQUIRED_FIELDS[collection]):
                continue
            route_id, entry = _compact_entry(collection, path, root, metadata)
            order = metadata.get("order", 9999)
            records.append((order if isinstance(order, int) else 9999, route_id, entry))
        routes[collection] = {identifier: entry for _, identifier, entry in sorted(records)}
    for identifier, relative, related in pending_relations:
        for rule_id in related:
            if not isinstance(rule_id, str) or rule_id not in rules:
                errors.append(f"RELATED_RULE_MISSING: {identifier} in {relative} -> {rule_id}")
    return routes, sources


def _script_summary(path: Path) -> str:
    """Return the first line of a script module docstring."""
    text = path.read_text(encoding="utf-8")[:1000]
    match = re.search(r'^[^\n]*\n?\s*"""(.*?)"""', text, re.DOTALL)
    return match.group(1).strip().splitlines()[0] if match else ""


def _collect_scripts(root: Path) -> dict[str, dict[str, str]]:
    """Return compact maintenance-script routes."""
    scripts = root / "scripts"
    return {path.stem: {"path": _relative(path, root), "use": _script_summary(path)} for path in sorted(scripts.glob("*.py")) if not path.name.startswith("_")}


def _collect_assets(root: Path) -> list[str]:
    """Return stable direct asset paths without indexing reference-clone contents."""
    assets = root / "assets"
    if not assets.is_dir():
        return []
    output: list[str] = []
    for path in sorted(assets.iterdir()):
        if path.name.startswith(".") or path.name.endswith("-reference"):
            continue
        output.append(_relative(path, root))
        if path.name == "instance" and path.is_dir():
            output.extend(_relative(child, root) for child in sorted(path.iterdir()) if not child.name.startswith(".") and not child.name.endswith(".local.md"))
    return output


def _source_digest(root: Path, sources: Iterable[Path]) -> str:
    """Hash normalized source paths and bytes for traceable generation."""
    digest = hashlib.sha256()
    for path in sorted(set(sources)):
        digest.update(_relative(path, root).encode("utf-8"))
        digest.update(b"\0")
        if path.is_file():
            digest.update(path.read_bytes().replace(b"\r\n", b"\n"))
        elif path.is_dir():
            digest.update(b"<directory>")
        else:
            digest.update(b"<missing>")
        digest.update(b"\0")
    return f"sha256:{digest.hexdigest()}"


def build_index(root: Path = SKILL_ROOT) -> dict[str, object]:
    """Validate the skill graph and return its compact deterministic index."""
    root = root.resolve()
    errors: list[str] = []
    skill_path = root / "SKILL.md"
    skill = _load_frontmatter(skill_path, root, errors)
    routes, sources = _collect_references(root, errors)
    markdown_sources = [skill_path, *sources]
    _validate_links(root, markdown_sources, errors)
    if skill is None:
        skill = {}
    for field in ("name", "description", "metadata"):
        if field not in skill:
            errors.append(f"SKILL_FIELD_MISSING: {field}")
    for field in ("name", "description"):
        if field in skill and not isinstance(skill[field], str):
            errors.append(f"SKILL_FIELD_TYPE: {field} must be a string")
    metadata = skill.get("metadata")
    version = metadata.get("version") if isinstance(metadata, dict) else None
    if not isinstance(version, str) or not version:
        errors.append("SKILL_VERSION: metadata.version must be a non-empty string")
    if errors:
        raise IndexValidationError(sorted(set(errors)))
    scripts = _collect_scripts(root)
    assets = _collect_assets(root)
    projection_sources = [root / route["path"] for route in scripts.values()]
    projection_sources.extend(root / path for path in assets)
    counts = {collection: len(routes[collection]) for collection in COLLECTIONS}
    return {
        "schema": "heaven-style-index/v2",
        "skill": {
            "name": skill["name"],
            "version": version,
            "description": skill["description"],
            "source_digest": _source_digest(root, [*markdown_sources, *projection_sources]),
        },
        "entrypoints": {
            "default": "SKILL.md",
            "start": "references/workflows/start.md",
            "rules": "references/rules/overview.md",
            "architect": "references/workflows/architect.md",
            "editor": "references/workflows/editor.md",
        },
        "counts": counts,
        "routes": routes,
        "scripts": scripts,
        "assets": assets,
    }


def render_index(index: dict[str, object]) -> str:
    """Render canonical UTF-8 YAML bytes without volatile timestamps."""
    body = yaml.dump(index, Dumper=_IndentedDumper, sort_keys=False, allow_unicode=True, width=120)
    return "# Generated by scripts/index.py. Do not edit.\n" + body


def write_atomic(path: Path, content: str) -> None:
    """Stage and atomically publish one validated generated artifact."""
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="\n", dir=path.parent, prefix=f".{path.name}.", delete=False)
    staged = Path(handle.name)
    try:
        with handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(staged, path)
    finally:
        if staged.exists():
            staged.unlink()


def main() -> int:
    """Validate and regenerate the index, or check exact freshness."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate and exit 1 unless index.yaml is byte-current")
    parser.add_argument("--root", type=Path, default=SKILL_ROOT, help="Skill root for fixtures or embedded copies")
    args = parser.parse_args()
    try:
        rendered = render_index(build_index(args.root))
    except IndexValidationError as exc:
        for error in exc.errors:
            print(error, file=sys.stderr)
        return 1
    index_path = args.root.resolve() / "references" / "index.yaml"
    if args.check:
        current = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""
        if current != rendered:
            print(f"index.yaml is stale; run: python {_relative(Path(__file__), SKILL_ROOT)}", file=sys.stderr)
            return 1
        print("index.yaml is valid and up to date")
        return 0
    write_atomic(index_path, rendered)
    print(f"Wrote {_relative(index_path, args.root.resolve())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
