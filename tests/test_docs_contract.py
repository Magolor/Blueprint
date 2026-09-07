"""Behavioral tests for the repository documentation contract."""

from __future__ import annotations

import importlib.util
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("project_docs", ROOT / "scripts" / "docs.py")
assert SPEC and SPEC.loader
project_docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(project_docs)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _valid_repo(tmp_path: Path) -> Path:
    _write(tmp_path / "README.en.md", "# User guide\n\nSee [engineering](docs/README.md).\n")
    _write(tmp_path / "AGENTS.md", "# Agent guide\n\nRead [docs](docs/README.md).\n")
    _write(tmp_path / "CONTRIBUTING.md", "# Contributing\n")
    _write(tmp_path / "docs" / "README.md", "# Engineering Guide\n\nSee the [log](DEVLOG.md).\n")
    _write(
        tmp_path / "docs" / "DEVLOG.md",
        "# Development Log\n\n## 2026-07-21 — Contract added\n\n- Task: direct\n- Changed: Added the contract.\n- Verified: Focused tests.\n- Next: none\n",
    )
    queue = {
        "schema": "heaven.tasks/v1",
        "project": "Fixture",
        "updated": "2026-07-21",
        "tasks": [
            {
                "id": "FIX-001",
                "title": "Exercise the queue",
                "status": "ready",
                "priority": "P1",
                "owner": None,
                "parent": None,
                "updated": "2026-07-21",
                "acceptance": ["The fixture passes."],
                "depends_on": [],
                "links": ["docs/README.md"],
            }
        ],
    }
    _write(tmp_path / "docs" / "tasks.yaml", yaml.safe_dump(queue, sort_keys=False))
    return tmp_path


def test_valid_contract_passes(tmp_path: Path) -> None:
    root = _valid_repo(tmp_path)

    errors, tasks = project_docs.validate(root, today=date(2026, 7, 21))

    assert errors == []
    assert [task["id"] for task in tasks] == ["FIX-001"]


def test_invalid_queue_fails_closed(tmp_path: Path) -> None:
    root = _valid_repo(tmp_path)
    queue_path = root / "docs" / "tasks.yaml"
    queue = yaml.safe_load(queue_path.read_text(encoding="utf-8"))
    queue["tasks"].append(
        {
            "id": "FIX-002",
            "title": "Invalid blocked task",
            "status": "blocked",
            "priority": "P2",
            "updated": "2026-07-21",
            "parent": "MISSING-998",
            "acceptance": ["Never reached."],
            "depends_on": ["MISSING-999"],
            "links": [],
        }
    )
    queue_path.write_text(yaml.safe_dump(queue, sort_keys=False), encoding="utf-8")

    errors, _ = project_docs.validate(root, today=date(2026, 7, 21))

    assert "TASK_BLOCKER: blocked task FIX-002 needs a blocker" in errors
    assert "TASK_UNBLOCK: blocked task FIX-002 needs an observable unblock_when condition" in errors
    assert "TASK_DEPENDENCY_MISSING: FIX-002 -> MISSING-999" in errors
    assert "TASK_PARENT_MISSING: FIX-002 -> MISSING-998" in errors


def test_draft_and_postponed_tasks_are_valid(tmp_path: Path) -> None:
    """Live planning states remain in the canonical queue."""

    root = _valid_repo(tmp_path)
    queue_path = root / "docs" / "tasks.yaml"
    queue = yaml.safe_load(queue_path.read_text(encoding="utf-8"))
    queue["tasks"][0]["status"] = "draft"
    queue["tasks"].append(
        {
            "id": "FIX-002",
            "title": "Resume after release",
            "status": "postponed",
            "priority": "P3",
            "updated": "2026-07-21",
            "resume_when": "Version 2 ships.",
            "acceptance": ["Compatibility is verified."],
            "depends_on": [],
            "links": [],
        }
    )
    queue_path.write_text(yaml.safe_dump(queue, sort_keys=False), encoding="utf-8")

    errors, _ = project_docs.validate(root, today=date(2026, 7, 21))

    assert errors == []


def test_dependency_cycle_is_rejected(tmp_path: Path) -> None:
    root = _valid_repo(tmp_path)
    queue_path = root / "docs" / "tasks.yaml"
    queue = yaml.safe_load(queue_path.read_text(encoding="utf-8"))
    queue["tasks"][0]["depends_on"] = ["FIX-002"]
    queue["tasks"].append(
        {
            "id": "FIX-002",
            "title": "Second task",
            "status": "ready",
            "priority": "P2",
            "updated": "2026-07-21",
            "parent": None,
            "acceptance": ["The cycle is rejected."],
            "depends_on": ["FIX-001"],
            "links": [],
        }
    )
    queue_path.write_text(yaml.safe_dump(queue, sort_keys=False), encoding="utf-8")

    errors, _ = project_docs.validate(root, today=date(2026, 7, 21))

    assert any(error.startswith("TASK_DEPENDENCY_CYCLE:") for error in errors)


def test_expired_scratch_note_is_rejected(tmp_path: Path) -> None:
    root = _valid_repo(tmp_path)
    _write(
        root / "docs" / "scratch" / "old-idea.md",
        "---\nstatus: scratch\ncreated: 2026-06-01\nexpires: 2026-06-30\ntask: FIX-001\n---\n\n# Old idea\n",
    )

    errors, _ = project_docs.validate(root, today=date(2026, 7, 21))

    assert "SCRATCH_EXPIRED: docs/scratch/old-idea.md expired on 2026-06-30" in errors


def test_broken_markdown_link_is_rejected(tmp_path: Path) -> None:
    root = _valid_repo(tmp_path)
    _write(root / "docs" / "README.md", "# Engineering Guide\n\n[Missing](missing.md)\n")

    errors, _ = project_docs.validate(root, today=date(2026, 7, 21))

    assert "LINK_MISSING: docs/README.md -> missing.md" in errors


def test_task_link_cannot_escape_repository(tmp_path: Path) -> None:
    root = _valid_repo(tmp_path)
    queue_path = root / "docs" / "tasks.yaml"
    queue = yaml.safe_load(queue_path.read_text(encoding="utf-8"))
    queue["tasks"][0]["links"] = ["../outside.md"]
    queue_path.write_text(yaml.safe_dump(queue, sort_keys=False), encoding="utf-8")

    errors, _ = project_docs.validate(root, today=date(2026, 7, 21))

    assert "TASK_LINK_ESCAPE: FIX-001 -> ../outside.md" in errors


def test_historical_next_may_reference_a_closed_task(tmp_path: Path) -> None:
    """Only the newest handoff points into the live active-only queue."""
    root = _valid_repo(tmp_path)
    log = root / "docs" / "DEVLOG.md"
    log.write_text(
        log.read_text(encoding="utf-8") + "\n## 2026-07-20 — Closed work\n\n- Task: OLD-001\n- Changed: Closed.\n- Verified: Passed.\n- Next: `OLD-002`\n",
        encoding="utf-8",
    )

    errors, _ = project_docs.validate(root, today=date(2026, 7, 21))

    assert errors == []


def test_malformed_devlog_date_is_a_diagnostic(tmp_path: Path) -> None:
    root = _valid_repo(tmp_path)
    log = root / "docs" / "DEVLOG.md"
    log.write_text(log.read_text(encoding="utf-8").replace("2026-07-21", "2026-99-99", 1), encoding="utf-8")

    errors, _ = project_docs.validate(root, today=date(2026, 7, 21))

    assert "DEVLOG_DATE: invalid entry date 2026-99-99" in errors


def test_one_task_cannot_own_multiple_active_plans(tmp_path: Path) -> None:
    root = _valid_repo(tmp_path)
    queue_path = root / "docs" / "tasks.yaml"
    queue = yaml.safe_load(queue_path.read_text(encoding="utf-8"))
    queue["tasks"][0]["links"] = ["docs/plans/one.md", "docs/plans/two.md"]
    queue_path.write_text(yaml.safe_dump(queue, sort_keys=False), encoding="utf-8")
    _write(root / "docs" / "plans" / "one.md", "# One\n\n- Status: Planned\n")
    _write(root / "docs" / "plans" / "two.md", "# Two\n\n- Status: In progress\n")

    errors, _ = project_docs.validate(root, today=date(2026, 7, 21))

    assert "TASK_MULTIPLE_PLANS: FIX-001 -> docs/plans/one.md, docs/plans/two.md" in errors
