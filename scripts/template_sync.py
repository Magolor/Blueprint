#!/usr/bin/env python3
"""Detect and reconcile Blueprint template drift in a declared consumer."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

POLICY_SCHEMA = "heaven.template/v1"
MANIFEST_SCHEMA = "heaven.template-sync/v2"


class SyncError(ValueError):
    """Represent a deterministic template synchronization failure."""


def _git(root: Path, *args: str) -> str:
    """Run one read-only Git query."""
    result = subprocess.run(["git", *args], cwd=root, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise SyncError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout.strip()


def _load_mapping(path: Path) -> dict[str, object]:
    """Load one required YAML mapping."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise SyncError(f"cannot load {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SyncError(f"{path} must contain a mapping")
    return data


def load_policy(source: Path) -> dict[str, object]:
    """Load and validate the source classification policy."""
    policy = _load_mapping(source / ".blueprint-template.yaml")
    if policy.get("schema") != POLICY_SCHEMA:
        raise SyncError(f"policy schema must be {POLICY_SCHEMA}")
    for field in ("exact", "adapted", "excluded"):
        value = policy.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
            raise SyncError(f"policy.{field} must be a string list")
    source_policy = policy.get("source")
    if not isinstance(source_policy, dict) or not isinstance(source_policy.get("repository"), str):
        raise SyncError("policy.source.repository is required")
    consumer = policy.get("consumer")
    if not isinstance(consumer, dict):
        raise SyncError("policy.consumer must be a mapping")
    for field in ("repository", "ref", "manifest"):
        if not isinstance(consumer.get(field), str) or not str(consumer[field]).strip():
            raise SyncError(f"policy.consumer.{field} is required")
    return policy


def _matches(path: str, patterns: list[str]) -> bool:
    """Return whether a POSIX path matches any policy glob."""
    return any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)


def _source_paths(source: Path) -> list[str]:
    """Return tracked and untracked non-ignored source paths."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=source,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SyncError(result.stderr.strip() or "git ls-files failed")
    return sorted({path for path in result.stdout.split("\0") if path})


def classify(source: Path, policy: dict[str, object]) -> dict[str, list[str]]:
    """Classify tracked and untracked non-ignored source paths."""
    classified = {"exact": [], "adapted": [], "excluded": []}
    errors: list[str] = []
    for path in _source_paths(source):
        exact = _matches(path, policy["exact"])
        adapted = _matches(path, policy["adapted"])
        excluded = _matches(path, policy["excluded"])
        categories: list[str] = []
        if exact:
            categories.append("exact")
        elif adapted:
            categories.append("adapted")
        if excluded:
            categories.append("excluded")
        if not categories:
            errors.append(f"UNCLASSIFIED: {path}")
            continue
        if len(categories) > 1:
            errors.append(f"MULTI_CLASSIFIED: {path} -> {', '.join(categories)}")
            continue
        category = categories[0]
        if category in {"exact", "adapted"}:
            try:
                managed = _managed_path(source, path)
                if not managed.is_file():
                    errors.append(f"MANAGED_SOURCE_MISSING: {path}")
                    continue
            except SyncError as exc:
                errors.append(str(exc))
                continue
        classified[category].append(path)
    if errors:
        raise SyncError("\n".join(sorted(errors)))
    return classified


def source_digest(source: Path, classified: dict[str, list[str]]) -> str:
    """Hash every exact or adapted source path and its normalized content."""
    digest = hashlib.sha256()
    paths = {".blueprint-template.yaml", *classified["exact"], *classified["adapted"]}
    for path in sorted(paths):
        target = _managed_path(source, path)
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(target.read_bytes().replace(b"\r\n", b"\n"))
        digest.update(b"\0")
    return f"sha256:{digest.hexdigest()}"


def _managed_path(root: Path, relative: str, *, allow_leaf_symlink: bool = False) -> Path:
    """Return one contained lexical path while rejecting symlink traversal."""
    candidate = Path(relative)
    if candidate.is_absolute() or not candidate.parts or any(part in {"", ".", ".."} for part in candidate.parts):
        raise SyncError(f"MANAGED_PATH_INVALID: {relative}")
    base = root.resolve()
    target = base.joinpath(*candidate.parts)
    current = base
    for position, part in enumerate(candidate.parts):
        current = current / part
        is_leaf = position == len(candidate.parts) - 1
        if current.is_symlink() and not (is_leaf and allow_leaf_symlink):
            raise SyncError(f"MANAGED_SYMLINK: {relative}")
    return target


def _repository_name(root: Path) -> str:
    """Return the normalized owner/repository identity for origin."""
    url = _git(root, "remote", "get-url", "origin")
    if ":" in url and not url.startswith(("http://", "https://", "ssh://")):
        path = url.split(":", 1)[1]
    else:
        path = urlparse(url).path
    normalized = path.strip("/")
    if normalized.endswith(".git"):
        normalized = normalized[:-4]
    parts = normalized.split("/")
    if len(parts) < 2:
        raise SyncError(f"REPOSITORY_IDENTITY_INVALID: {url}")
    return "/".join(parts[-2:])


def consumer_adapted_state(consumer: Path, classified: dict[str, list[str]]) -> dict[str, str]:
    """Fingerprint each reviewed consumer counterpart without following links."""
    state: dict[str, str] = {}
    for relative in sorted(classified["adapted"]):
        target = _managed_path(consumer, relative, allow_leaf_symlink=True)
        if target.is_symlink():
            state[relative] = f"symlink:{os.readlink(target)}"
        elif target.is_file():
            content = target.read_bytes().replace(b"\r\n", b"\n")
            state[relative] = f"sha256:{hashlib.sha256(content).hexdigest()}"
        elif target.exists():
            raise SyncError(f"ADAPTED_NOT_FILE: {relative}")
        else:
            state[relative] = "missing"
    return state


def consumer_adapted_digest(state: dict[str, str]) -> str:
    """Hash the stable per-path adapted review state."""
    digest = hashlib.sha256()
    for relative, fingerprint in sorted(state.items()):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(fingerprint.encode("utf-8"))
        digest.update(b"\0")
    return f"sha256:{digest.hexdigest()}"


def exact_drift(source: Path, consumer: Path, classified: dict[str, list[str]]) -> list[str]:
    """Return exact files whose consumer bytes differ."""
    drift: list[str] = []
    for relative in classified["exact"]:
        source_path = _managed_path(source, relative)
        target_path = _managed_path(consumer, relative)
        if not source_path.is_file() or not target_path.is_file() or source_path.read_bytes() != target_path.read_bytes():
            drift.append(relative)
    return drift


def _manifest_path(consumer: Path, policy: dict[str, object]) -> Path:
    """Return the declared consumer record path."""
    return _managed_path(consumer, policy["consumer"]["manifest"])


def check_consumer(source: Path, consumer: Path, policy: dict[str, object]) -> list[str]:
    """Return deterministic sync diagnostics without writes or network access."""
    classified = classify(source, policy)
    errors = [f"EXACT_DRIFT: {path}" for path in exact_drift(source, consumer, classified)]
    manifest_path = _manifest_path(consumer, policy)
    if not manifest_path.is_file():
        return [*errors, f"MANIFEST_MISSING: {manifest_path.name}"]
    try:
        manifest = _load_mapping(manifest_path)
    except SyncError as exc:
        return [*errors, f"MANIFEST_INVALID: {exc}"]
    if manifest.get("schema") != MANIFEST_SCHEMA:
        errors.append(f"MANIFEST_SCHEMA: expected {MANIFEST_SCHEMA}")
    source_repository = policy["source"]["repository"]
    consumer_repository = policy["consumer"]["repository"]
    consumer_ref = policy["consumer"]["ref"]
    if manifest.get("source_repository") != source_repository:
        errors.append(f"SOURCE_REPOSITORY: expected {source_repository}")
    if manifest.get("consumer_repository") != consumer_repository:
        errors.append(f"CONSUMER_REPOSITORY: expected {consumer_repository}")
    if manifest.get("consumer_ref") != consumer_ref:
        errors.append(f"CONSUMER_REF: expected {consumer_ref}")
    if _repository_name(source) != source_repository:
        errors.append(f"SOURCE_REMOTE: expected {source_repository}")
    if _repository_name(consumer) != consumer_repository:
        errors.append(f"CONSUMER_REMOTE: expected {consumer_repository}")
    expected_commit = _git(source, "rev-parse", "HEAD")
    expected_digest = source_digest(source, classified)
    if manifest.get("source_commit") != expected_commit:
        errors.append(f"SOURCE_COMMIT: expected {expected_commit}")
    if manifest.get("source_digest") != expected_digest:
        errors.append(f"SOURCE_DIGEST: expected {expected_digest}")
    expected_exact = sorted(classified["exact"])
    exact_paths = manifest.get("exact_paths")
    valid_exact_paths = isinstance(exact_paths, list) and all(isinstance(item, str) for item in exact_paths)
    if not valid_exact_paths or exact_paths != expected_exact:
        errors.append("EXACT_INVENTORY: manifest exact_paths do not match the source policy")
    if valid_exact_paths:
        for relative in sorted(set(exact_paths) - set(expected_exact)):
            if _managed_path(consumer, relative).exists():
                errors.append(f"STALE_EXACT: {relative}")
    adapted_state = consumer_adapted_state(consumer, classified)
    recorded_state = manifest.get("adapted_paths")
    if not isinstance(recorded_state, dict) or not all(isinstance(path, str) and isinstance(value, str) for path, value in recorded_state.items()):
        errors.append("ADAPTED_STATE: manifest adapted_paths must be a string mapping")
        recorded_state = {}
    for relative in sorted(set(recorded_state) | set(adapted_state)):
        if recorded_state.get(relative) != adapted_state.get(relative):
            errors.append(f"ADAPTED_DRIFT: {relative}")
    adapted_digest = consumer_adapted_digest(adapted_state)
    if manifest.get("consumer_adapted_digest") != adapted_digest:
        errors.append(f"ADAPTED_DIGEST: expected {adapted_digest}")
    return sorted(errors)


def _copy_atomic(source: Path, target: Path) -> None:
    """Copy one regular file through a same-directory atomic replacement."""
    target.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile("wb", dir=target.parent, prefix=f".{target.name}.", delete=False)
    staged = Path(handle.name)
    handle.close()
    try:
        shutil.copy2(source, staged)
        with staged.open("rb") as stream:
            os.fsync(stream.fileno())
        os.replace(staged, target)
    finally:
        if staged.exists():
            staged.unlink()


def sync_exact(source: Path, consumer: Path, policy: dict[str, object]) -> list[str]:
    """Copy exact template-owned files without accepting adapted surfaces."""
    classified = classify(source, policy)
    manifest_path = _manifest_path(consumer, policy)
    previous_exact: list[str] = []
    if manifest_path.is_file():
        previous = _load_mapping(manifest_path).get("exact_paths", [])
        if not isinstance(previous, list) or not all(isinstance(item, str) for item in previous):
            raise SyncError("manifest exact_paths must be a string list before synchronization")
        previous_exact = previous
    current_exact = sorted(classified["exact"])
    source_paths = {relative: _managed_path(source, relative) for relative in current_exact}
    target_paths = {relative: _managed_path(consumer, relative) for relative in current_exact}
    stale_paths = {relative: _managed_path(consumer, relative) for relative in sorted(set(previous_exact) - set(current_exact))}
    for relative, path in source_paths.items():
        if not path.is_file():
            raise SyncError(f"exact source is missing: {relative}")
    for relative, path in stale_paths.items():
        if path.exists() and not path.is_file():
            raise SyncError(f"stale exact target is not a regular file: {relative}")
    changed: list[str] = []
    for relative, target_path in stale_paths.items():
        if target_path.exists():
            target_path.unlink()
            changed.append(f"removed {relative}")
    for relative in current_exact:
        source_path = source_paths[relative]
        target_path = target_paths[relative]
        if target_path.is_file() and target_path.read_bytes() == source_path.read_bytes():
            continue
        _copy_atomic(source_path, target_path)
        changed.append(f"updated {relative}")
    return changed


def _write_yaml_atomic(path: Path, data: dict[str, object]) -> None:
    """Stage and atomically publish one manifest."""
    path.parent.mkdir(parents=True, exist_ok=True)
    content = yaml.safe_dump(data, sort_keys=False, allow_unicode=True)
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


def record_review(source: Path, consumer: Path, policy: dict[str, object], reviewer: str, note: str) -> Path:
    """Record human review after exact files match a clean source commit."""
    if _git(source, "status", "--porcelain"):
        raise SyncError("source must be clean before recording consumer review")
    if _repository_name(source) != policy["source"]["repository"]:
        raise SyncError(f"source origin must be {policy['source']['repository']}")
    if _repository_name(consumer) != policy["consumer"]["repository"]:
        raise SyncError(f"consumer origin must be {policy['consumer']['repository']}")
    classified = classify(source, policy)
    drift = exact_drift(source, consumer, classified)
    if drift:
        raise SyncError("exact drift remains:\n" + "\n".join(drift))
    manifest_path = _manifest_path(consumer, policy)
    adapted_state = consumer_adapted_state(consumer, classified)
    manifest = {
        "schema": MANIFEST_SCHEMA,
        "source_repository": policy["source"]["repository"],
        "source_commit": _git(source, "rev-parse", "HEAD"),
        "source_digest": source_digest(source, classified),
        "consumer_repository": policy["consumer"]["repository"],
        "consumer_ref": policy["consumer"]["ref"],
        "consumer_adapted_digest": consumer_adapted_digest(adapted_state),
        "adapted_paths": adapted_state,
        "exact_paths": sorted(classified["exact"]),
        "reviewed_at": date.today().isoformat(),
        "reviewed_by": reviewer,
        "note": note,
    }
    _write_yaml_atomic(manifest_path, manifest)
    return manifest_path


def main() -> int:
    """Validate source coverage, copy exact files, check drift, or record review."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("check-source", help="Validate that every tracked Blueprint file has one sync policy")
    for name in ("check", "sync-exact"):
        command = subparsers.add_parser(name)
        command.add_argument("--consumer", type=Path, required=True)
    record = subparsers.add_parser("record")
    record.add_argument("--consumer", type=Path, required=True)
    record.add_argument("--reviewed-by", required=True)
    record.add_argument("--note", required=True)
    args = parser.parse_args()
    try:
        source = args.source.resolve()
        policy = load_policy(source)
        classified = classify(source, policy)
        if args.command == "check-source":
            expected_repository = policy["source"]["repository"]
            if _repository_name(source) != expected_repository:
                raise SyncError(f"source origin must be {expected_repository}")
            print(
                f"Template policy covers {len(classified['exact'])} exact, "
                f"{len(classified['adapted'])} adapted, and {len(classified['excluded'])} excluded file(s)."
            )
            return 0
        consumer = args.consumer.resolve()
        if args.command == "sync-exact":
            changed = sync_exact(source, consumer, policy)
            print("Exact files already current." if not changed else "Synced exact files:\n" + "\n".join(changed))
            return 0
        if args.command == "record":
            path = record_review(source, consumer, policy, args.reviewed_by, args.note)
            print(f"Recorded review at {path}")
            return 0
        errors = check_consumer(source, consumer, policy)
        if errors:
            for error in errors:
                print(error, file=sys.stderr)
            return 1
        print("Consumer matches the recorded Blueprint template revision.")
        return 0
    except SyncError as exc:
        print(exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
