#!/usr/bin/env python3
"""Check maintenance scripts for syntax and undeclared project dependencies."""

from __future__ import annotations

import argparse
import ast
from pathlib import Path
import sys


def _skip_file(path: Path) -> bool:
    """Return whether path is outside scanner scope."""
    parts = {part.lower() for part in path.parts}
    return bool(parts & {".venv", "__pycache__"}) or any(part.endswith("-reference") for part in parts)


def _imports(tree: ast.AST) -> list[tuple[int, str, str]]:
    """Return absolute imports from a parsed module."""
    imports: list[tuple[int, str, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend((node.lineno, alias.name.split(".")[0], alias.name) for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            imports.append((node.lineno, node.module.split(".")[0], node.module))
    return imports


def scan_file(path: str | Path, *, stdlib_only: bool, allow_imports: set[str]) -> list[str]:
    """Return syntax and dependency issues for one Python file."""
    resolved = Path(path).expanduser().resolve()
    issues: list[str] = []
    try:
        tree = ast.parse(resolved.read_text(encoding="utf-8"), filename=str(resolved))
    except (OSError, SyntaxError) as error:
        return [f"{resolved}: {error}"]
    if not stdlib_only:
        return issues
    for lineno, top, full in _imports(tree):
        if top in sys.stdlib_module_names or top in allow_imports:
            continue
        issues.append(f"{resolved}:{lineno}: import {full} is not standard library or explicitly allowed")
    return issues


def _scan_targets(paths: list[str]) -> list[Path]:
    """Expand input files and directories into Python files."""
    files: set[Path] = set()
    for raw in paths:
        path = Path(raw).expanduser().resolve()
        if path.is_file() and path.suffix == ".py":
            files.add(path)
        elif path.is_dir():
            files.update(candidate for candidate in path.rglob("*.py") if not _skip_file(candidate))
    return sorted(files, key=lambda item: str(item).lower())


def main() -> int:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Python files or directories to scan")
    parser.add_argument("--stdlib-only", action="store_true", help="Reject imports outside the standard library")
    parser.add_argument(
        "--allow-import",
        action="append",
        default=[],
        metavar="MODULE",
        help="Allow one top-level non-standard import under --stdlib-only; repeat as needed",
    )
    args = parser.parse_args()
    files = _scan_targets(args.paths)
    issues = [issue for file in files for issue in scan_file(file, stdlib_only=args.stdlib_only, allow_imports=set(args.allow_import))]
    if issues:
        print("\n".join(issues))
        return 1
    print(f"OK: {len(files)} file(s) - syntax and dependency policy pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
