"""Exercise Blueprint template synchronization against temporary Git repositories."""

from __future__ import annotations

import importlib.util
import os
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "template_sync.py"
SPEC = importlib.util.spec_from_file_location("template_sync", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {SCRIPT}")
template_sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(template_sync)


def _run_git(root: Path, *args: str) -> None:
    """Run one fixture Git command."""
    env = dict(os.environ)
    for name in (
        "GIT_ALTERNATE_OBJECT_DIRECTORIES",
        "GIT_COMMON_DIR",
        "GIT_DIR",
        "GIT_GRAFT_FILE",
        "GIT_IMPLICIT_WORK_TREE",
        "GIT_INDEX_FILE",
        "GIT_NO_REPLACE_OBJECTS",
        "GIT_OBJECT_DIRECTORY",
        "GIT_PREFIX",
        "GIT_SHALLOW_FILE",
        "GIT_WORK_TREE",
    ):
        env.pop(name, None)
    subprocess.run(["git", *args], cwd=root, env=env, check=True, capture_output=True, text=True)


def _make_repositories(tmp_path: Path) -> tuple[Path, Path, dict[str, object]]:
    """Create one clean template source and matching consumer."""
    source = tmp_path / "source"
    consumer = tmp_path / "consumer"
    source.mkdir()
    consumer.mkdir()
    (source / ".blueprint-template.yaml").write_text(
        """\
schema: heaven.template/v1
source:
  repository: fixture/source
consumer:
  repository: fixture/consumer
  ref: main
  manifest: .blueprint-sync.yaml
exact:
  - template.txt
adapted:
  - "*.txt"
excluded:
  - .blueprint-template.yaml
  - .gitignore
""",
        encoding="utf-8",
    )
    (source / ".gitignore").write_text("ignored.bin\n", encoding="utf-8")
    (source / "template.txt").write_text("canonical\n", encoding="utf-8")
    (source / "notes.txt").write_text("consumer-owned adaptation\n", encoding="utf-8")
    (consumer / "template.txt").write_text("canonical\n", encoding="utf-8")
    for root, remote in ((source, "fixture/source"), (consumer, "fixture/consumer")):
        _run_git(root, "init", "--quiet")
        _run_git(root, "config", "user.name", "Template Sync Test")
        _run_git(root, "config", "user.email", "template-sync@example.invalid")
        _run_git(root, "config", "commit.gpgsign", "false")
        _run_git(root, "remote", "add", "origin", f"git@github.com:{remote}.git")
    _run_git(source, "add", ".")
    _run_git(source, "commit", "--quiet", "-m", "fixture")
    return source, consumer, template_sync.load_policy(source)


@pytest.mark.fast
@pytest.mark.integration
def test_record_and_check_accept_exact_override(tmp_path: Path) -> None:
    """Record and check a clean consumer when exact overlaps adapted."""
    source, consumer, policy = _make_repositories(tmp_path)

    classified = template_sync.classify(source, policy)
    manifest = template_sync.record_review(source, consumer, policy, "tester", "validated")

    assert classified["exact"] == ["template.txt"]
    assert classified["adapted"] == ["notes.txt"]
    assert manifest == consumer / ".blueprint-sync.yaml"
    assert template_sync.check_consumer(source, consumer, policy) == []


@pytest.mark.fast
@pytest.mark.integration
def test_check_reports_exact_drift(tmp_path: Path) -> None:
    """Report an exact consumer file whose bytes changed after review."""
    source, consumer, policy = _make_repositories(tmp_path)
    template_sync.record_review(source, consumer, policy, "tester", "validated")
    (consumer / "template.txt").write_text("drifted\n", encoding="utf-8")

    assert template_sync.check_consumer(source, consumer, policy) == ["EXACT_DRIFT: template.txt"]


@pytest.mark.fast
@pytest.mark.integration
def test_check_reports_adapted_drift_after_review(tmp_path: Path) -> None:
    """Fingerprint reviewed adapted counterparts without requiring byte equality."""
    source, consumer, policy = _make_repositories(tmp_path)
    template_sync.record_review(source, consumer, policy, "tester", "validated")
    (consumer / "notes.txt").write_text("later adaptation\n", encoding="utf-8")

    errors = template_sync.check_consumer(source, consumer, policy)

    assert "ADAPTED_DRIFT: notes.txt" in errors
    assert any(error.startswith("ADAPTED_DIGEST: expected sha256:") for error in errors)


@pytest.mark.fast
@pytest.mark.integration
def test_sync_removes_retired_exact_file_from_manifest_inventory(tmp_path: Path) -> None:
    """Remove a formerly exact file after policy deliberately makes it adapted."""
    source, consumer, policy = _make_repositories(tmp_path)
    template_sync.record_review(source, consumer, policy, "tester", "validated")
    policy["exact"] = []

    changed = template_sync.sync_exact(source, consumer, policy)

    assert changed == ["removed template.txt"]
    assert not (consumer / "template.txt").exists()


@pytest.mark.fast
@pytest.mark.integration
def test_sync_rejects_exact_target_symlink(tmp_path: Path) -> None:
    """Never follow a managed exact target symlink outside the consumer."""
    source, consumer, policy = _make_repositories(tmp_path)
    outside = tmp_path / "outside.txt"
    outside.write_text("untouched\n", encoding="utf-8")
    (consumer / "template.txt").unlink()
    (consumer / "template.txt").symlink_to(outside)

    with pytest.raises(template_sync.SyncError, match="MANAGED_SYMLINK: template.txt"):
        template_sync.sync_exact(source, consumer, policy)

    assert outside.read_text(encoding="utf-8") == "untouched\n"


@pytest.mark.fast
@pytest.mark.integration
def test_classify_rejects_untracked_non_ignored_paths_deterministically(tmp_path: Path) -> None:
    """Reject every new non-ignored source path in stable path order."""
    source, _, policy = _make_repositories(tmp_path)
    (source / "ignored.bin").write_text("ignored\n", encoding="utf-8")
    (source / "z-unclassified.bin").write_text("z\n", encoding="utf-8")
    (source / "a-unclassified.bin").write_text("a\n", encoding="utf-8")

    with pytest.raises(template_sync.SyncError) as error:
        template_sync.classify(source, policy)

    assert str(error.value) == "UNCLASSIFIED: a-unclassified.bin\nUNCLASSIFIED: z-unclassified.bin"
