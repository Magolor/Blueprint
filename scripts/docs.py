#!/usr/bin/env python3
"""Validate the repository documentation contract and inspect its task queue."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

import yaml

QUEUE_SCHEMA = "heaven.tasks/v1"
OPEN_STATUSES = {"ready", "active", "blocked"}
PRIORITIES = {"P0", "P1", "P2", "P3"}
REQUIRED_FILES = (
    "README.en.md",
    "docs/README.md",
    "docs/DEVLOG.md",
    "docs/tasks.yaml",
)
LEGACY_DOC_DIRS = ("docs/progress",)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
TASK_ID_RE = re.compile(r"^[A-Z][A-Z0-9]*-[0-9]{3,}$")
DEVLOG_ENTRY_RE = re.compile(r"^##\s+(\S+)(?:\s+.*)?$", re.MULTILINE)
DEVLOG_NEXT_RE = re.compile(r"^- Next:\s*(.+)$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _as_date(value: object, field: str, errors: list[str]) -> date | None:
    """Normalize a YAML date while collecting a stable diagnostic."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    errors.append(f"DATE_INVALID: {field} must be YYYY-MM-DD")
    return None


def _load_yaml(path: Path, errors: list[str]) -> object:
    """Load YAML without allowing parse failures to become nominal data."""
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"YAML_INVALID: {path}: {exc}")
        return None


def _markdown_links(path: Path) -> Iterable[str]:
    """Yield local-looking Markdown link targets outside fenced code blocks."""
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


def _validate_links(root: Path, errors: list[str]) -> None:
    """Reject broken repository-local Markdown links."""
    candidates = [root / name for name in ("README.en.md", "AGENTS.md", "CONTRIBUTING.md")]
    candidates.extend(sorted((root / "docs").rglob("*.md")))
    for source in candidates:
        if not source.is_file():
            continue
        for raw_target in _markdown_links(source):
            if raw_target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                continue
            target = unquote(raw_target.split("#", 1)[0])
            if not target:
                continue
            if target.startswith("/"):
                rel_source = source.relative_to(root).as_posix()
                errors.append(f"LINK_ABSOLUTE: {rel_source} -> {raw_target}")
                continue
            resolved = (source.parent / target).resolve()
            if root.resolve() not in resolved.parents and resolved != root.resolve():
                rel_source = source.relative_to(root).as_posix()
                errors.append(f"LINK_ESCAPE: {rel_source} -> {raw_target}")
                continue
            if not resolved.exists():
                rel_source = source.relative_to(root).as_posix()
                errors.append(f"LINK_MISSING: {rel_source} -> {raw_target}")


def _validate_structure(root: Path, errors: list[str]) -> None:
    """Validate the four documentation surfaces and retired paths."""
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"SURFACE_MISSING: {relative}")
    for relative in LEGACY_DOC_DIRS:
        if (root / relative).exists():
            errors.append(f"LEGACY_SURFACE: retire {relative} into docs/DEVLOG.md")
    temp_root = root / ".temp"
    if temp_root.exists():
        tracked = _git_files(root, ".temp")
        for path in tracked:
            errors.append(f"SCRATCH_TRACKED: {path} must remain disposable")


def _git_files(root: Path, prefix: str) -> list[str]:
    """Return tracked paths below a prefix without importing repository runtime code."""
    import subprocess

    result = subprocess.run(
        ["git", "ls-files", "--", prefix],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line]


def _validate_devlog(root: Path, task_ids: set[str], errors: list[str]) -> None:
    """Validate the rolling development log shape and ordering."""
    path = root / "docs" / "DEVLOG.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    if not text.startswith("# Development Log\n"):
        errors.append("DEVLOG_HEADER: docs/DEVLOG.md must start with '# Development Log'")
    headings = list(DEVLOG_ENTRY_RE.finditer(text))
    if not headings:
        errors.append("DEVLOG_EMPTY: docs/DEVLOG.md needs at least one dated entry")
        return
    dates: list[date] = []
    entries: list[tuple[str, list[str]]] = []
    for position, heading in enumerate(headings):
        label = heading.group(1)
        try:
            dates.append(date.fromisoformat(label))
        except ValueError:
            errors.append(f"DEVLOG_DATE: invalid entry date {label}")
        end = headings[position + 1].start() if position + 1 < len(headings) else len(text)
        next_values = DEVLOG_NEXT_RE.findall(text[heading.end() : end])
        entries.append((label, next_values))
        if len(next_values) != 1:
            errors.append(f"DEVLOG_NEXT: entry {label} needs exactly one '- Next:' line")
    if len(dates) == len(headings) and dates != sorted(dates, reverse=True):
        errors.append("DEVLOG_ORDER: dated entries must be newest first")
    if len(headings) > 50:
        errors.append("DEVLOG_TOO_LONG: keep at most 50 entries; Git preserves older detail")
    if len(entries[0][1]) != 1:
        return
    for value in entries[0][1]:
        normalized = value.strip().strip("`")
        if normalized.lower() == "none":
            continue
        references = set(re.findall(r"[A-Z][A-Z0-9]*-[0-9]{3,}", normalized))
        if not references:
            errors.append(f"DEVLOG_NEXT: '{value}' must reference an active task ID or none")
        for task_id in references - task_ids:
            errors.append(f"DEVLOG_TASK_MISSING: {task_id}")


def _validate_tasks(root: Path, errors: list[str]) -> list[dict[str, object]]:
    """Validate and return the canonical active task queue."""
    path = root / "docs" / "tasks.yaml"
    if not path.is_file():
        return []
    data = _load_yaml(path, errors)
    if not isinstance(data, dict):
        errors.append("QUEUE_ROOT: docs/tasks.yaml must contain a mapping")
        return []
    if data.get("schema") != QUEUE_SCHEMA:
        errors.append(f"QUEUE_SCHEMA: schema must be {QUEUE_SCHEMA}")
    if not isinstance(data.get("project"), str) or not str(data["project"]).strip():
        errors.append("QUEUE_PROJECT: project must be a non-empty string")
    tasks = data.get("tasks")
    if not isinstance(tasks, list):
        errors.append("QUEUE_TASKS: tasks must be a list")
        return []
    queue_updated = _as_date(data.get("updated"), "queue.updated", errors)
    seen: set[str] = set()
    normalized: list[dict[str, object]] = []
    for position, raw_task in enumerate(tasks):
        label = f"tasks[{position}]"
        if not isinstance(raw_task, dict):
            errors.append(f"TASK_MAPPING: {label} must be a mapping")
            continue
        task = dict(raw_task)
        task_id = task.get("id")
        if not isinstance(task_id, str) or not TASK_ID_RE.fullmatch(task_id):
            errors.append(f"TASK_ID: {label}.id must match {TASK_ID_RE.pattern}")
            continue
        if task_id in seen:
            errors.append(f"TASK_DUPLICATE: {task_id}")
            continue
        seen.add(task_id)
        normalized.append(task)
        if not isinstance(task.get("title"), str) or not str(task["title"]).strip():
            errors.append(f"TASK_TITLE: {task_id} needs a title")
        status = task.get("status")
        if status not in OPEN_STATUSES:
            errors.append(f"TASK_STATUS: {task_id} must use one of {sorted(OPEN_STATUSES)}; closed work leaves the queue")
        if task.get("priority") not in PRIORITIES:
            errors.append(f"TASK_PRIORITY: {task_id} must use P0, P1, P2, or P3")
        task_updated = _as_date(task.get("updated"), f"{task_id}.updated", errors)
        if queue_updated and task_updated and task_updated > queue_updated:
            errors.append(f"TASK_UPDATED: {task_id} is newer than queue.updated")
        if status == "active" and not str(task.get("owner") or "").strip():
            errors.append(f"TASK_OWNER: active task {task_id} needs an owner")
        if status == "blocked" and not str(task.get("blocker") or "").strip():
            errors.append(f"TASK_BLOCKER: blocked task {task_id} needs a blocker")
        if status == "blocked" and not str(task.get("unblock_when") or "").strip():
            errors.append(f"TASK_UNBLOCK: blocked task {task_id} needs an observable unblock_when condition")
        acceptance = task.get("acceptance")
        if not isinstance(acceptance, list) or not acceptance or not all(isinstance(item, str) and item.strip() for item in acceptance):
            errors.append(f"TASK_ACCEPTANCE: {task_id} needs a non-empty string list")
        for field in ("depends_on", "links"):
            value = task.get(field, [])
            if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
                errors.append(f"TASK_{field.upper()}: {task_id}.{field} must be a string list")
    by_id = {str(task["id"]): task for task in normalized}
    for task_id, task in by_id.items():
        parent = task.get("parent")
        if parent is not None and not isinstance(parent, str):
            errors.append(f"TASK_PARENT: {task_id}.parent must be a task ID or null")
        elif parent == task_id:
            errors.append(f"TASK_SELF_PARENT: {task_id}")
        elif isinstance(parent, str) and parent not in by_id:
            errors.append(f"TASK_PARENT_MISSING: {task_id} -> {parent}")
        dependencies = task.get("depends_on", [])
        if not isinstance(dependencies, list):
            continue
        for dependency in dependencies:
            if dependency == task_id:
                errors.append(f"TASK_SELF_DEPENDENCY: {task_id}")
            elif dependency not in by_id:
                errors.append(f"TASK_DEPENDENCY_MISSING: {task_id} -> {dependency}")
        links = task.get("links", [])
        if isinstance(links, list):
            for link in links:
                if link.startswith(("http://", "https://")):
                    continue
                target = (root / link).resolve()
                if root.resolve() not in target.parents and target != root.resolve():
                    errors.append(f"TASK_LINK_ESCAPE: {task_id} -> {link}")
                elif not target.exists():
                    errors.append(f"TASK_LINK_MISSING: {task_id} -> {link}")
    _validate_dependency_cycles(by_id, errors)
    _validate_parent_cycles(by_id, errors)
    return normalized


def _validate_dependency_cycles(tasks: dict[str, dict[str, object]], errors: list[str]) -> None:
    """Reject dependency cycles in the active queue."""
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(task_id: str, trail: list[str]) -> None:
        if task_id in visiting:
            start = trail.index(task_id)
            errors.append(f"TASK_DEPENDENCY_CYCLE: {' -> '.join(trail[start:] + [task_id])}")
            return
        if task_id in visited:
            return
        visiting.add(task_id)
        trail.append(task_id)
        dependencies = tasks[task_id].get("depends_on", [])
        if isinstance(dependencies, list):
            for dependency in dependencies:
                if isinstance(dependency, str) and dependency in tasks:
                    visit(dependency, trail)
        trail.pop()
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in sorted(tasks):
        visit(task_id, [])


def _validate_parent_cycles(tasks: dict[str, dict[str, object]], errors: list[str]) -> None:
    """Reject cycles in delegated parent relationships."""
    for task_id in sorted(tasks):
        trail: list[str] = []
        current = task_id
        while current in tasks:
            if current in trail:
                start = trail.index(current)
                errors.append(f"TASK_PARENT_CYCLE: {' -> '.join(trail[start:] + [current])}")
                break
            trail.append(current)
            parent = tasks[current].get("parent")
            if not isinstance(parent, str):
                break
            current = parent


def _validate_plan_coverage(root: Path, tasks: list[dict[str, object]], errors: list[str]) -> None:
    """Keep plans subordinate to exactly one active queue item."""
    links: dict[str, list[str]] = {}
    for task in tasks:
        task_id = str(task["id"])
        for link in task.get("links", []):
            if isinstance(link, str):
                links.setdefault(link, []).append(task_id)
    active_plans: dict[str, list[str]] = {}
    for path in sorted((root / "docs" / "plans").glob("*.md")):
        if path.name == "README.md":
            continue
        rel = path.relative_to(root).as_posix()
        match = re.search(r"^- Status:\s*(.+?)\s*$", path.read_text(encoding="utf-8"), re.MULTILINE)
        if not match:
            errors.append(f"PLAN_STATUS: {rel} needs '- Status:'")
            continue
        status = match.group(1)
        owners = links.get(rel, [])
        if status in {"Planned", "In progress", "Blocked"} and len(owners) != 1:
            errors.append(f"PLAN_QUEUE: {rel} with status {status} needs exactly one queue owner")
        elif status in {"Planned", "In progress", "Blocked"}:
            active_plans.setdefault(owners[0], []).append(rel)
        if status in {"Done", "Superseded"} and owners:
            errors.append(f"PLAN_CLOSED_QUEUED: {rel} -> {', '.join(owners)}")
        if status not in {"Planned", "In progress", "Blocked", "Done", "Superseded"}:
            errors.append(f"PLAN_STATUS_INVALID: {rel} -> {status}")
    for task_id, plans in sorted(active_plans.items()):
        if len(plans) > 1:
            errors.append(f"TASK_MULTIPLE_PLANS: {task_id} -> {', '.join(sorted(plans))}")


def _validate_scratch(root: Path, today: date, errors: list[str]) -> None:
    """Validate tracked scratch notes and force timely promotion or deletion."""
    scratch = root / "docs" / "scratch"
    if not scratch.is_dir():
        return
    for path in sorted(scratch.rglob("*.md")):
        if path.name == "README.md" or path.name.endswith(".local.md") or "local" in path.parts:
            continue
        match = FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
        rel = path.relative_to(root).as_posix()
        if not match:
            errors.append(f"SCRATCH_FRONTMATTER: {rel}")
            continue
        try:
            meta = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"SCRATCH_YAML: {rel}: {exc}")
            continue
        if not isinstance(meta, dict) or meta.get("status") != "scratch":
            errors.append(f"SCRATCH_STATUS: {rel} must declare status: scratch")
            continue
        created = _as_date(meta.get("created"), f"{rel}.created", errors)
        expires = _as_date(meta.get("expires"), f"{rel}.expires", errors)
        if created and expires:
            if expires <= today:
                errors.append(f"SCRATCH_EXPIRED: {rel} expired on {expires.isoformat()}")
            if expires > created + timedelta(days=45):
                errors.append(f"SCRATCH_TTL: {rel} may live for at most 45 days")
        if not str(meta.get("task") or "").strip():
            errors.append(f"SCRATCH_TASK: {rel} must name its owning task or direct request")


def validate(root: Path, *, today: date | None = None) -> tuple[list[str], list[dict[str, object]]]:
    """Return deterministic contract errors and normalized active tasks."""
    root = root.resolve()
    errors: list[str] = []
    _validate_structure(root, errors)
    tasks = _validate_tasks(root, errors)
    task_ids = {str(task["id"]) for task in tasks}
    _validate_devlog(root, task_ids, errors)
    _validate_plan_coverage(root, tasks, errors)
    _validate_scratch(root, today or date.today(), errors)
    _validate_links(root, errors)
    return sorted(set(errors)), tasks


def _print_tasks(tasks: list[dict[str, object]], *, ready_only: bool) -> None:
    """Print the queue in file order for humans and agents."""
    selected = [task for task in tasks if not ready_only or (task.get("status") == "ready" and not task.get("depends_on"))]
    if not selected:
        print("No actionable tasks." if ready_only else "Task queue is empty.")
        return
    for task in selected:
        owner = task.get("owner") or "unassigned"
        print(f"{task['id']} [{task['priority']} {task['status']}] {task['title']} — {owner}")


def main() -> int:
    """Run documentation validation or print the active queue."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    subparsers = parser.add_subparsers(dest="command", required=True)
    check = subparsers.add_parser("check", help="Validate documentation, links, scratch state, and the task queue")
    check.add_argument("--today", type=date.fromisoformat, default=None, help="Override today's date for deterministic tests")
    tasks = subparsers.add_parser("tasks", help="Print the canonical active task queue")
    tasks.add_argument("--ready", action="store_true", help="Show only dependency-free ready tasks")
    args = parser.parse_args()
    errors, queue = validate(args.root, today=getattr(args, "today", None))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    if args.command == "tasks":
        _print_tasks(queue, ready_only=args.ready)
    else:
        print(f"Documentation contract is valid ({len(queue)} active task(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
