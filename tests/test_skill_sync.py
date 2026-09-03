"""Behavioral tests for configurable cross-branch skill synchronization."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SCRIPT = ROOT / "scripts" / "check-skill-sync.bash"


def _run(repository: Path, command: str, *arguments: str, environment: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(environment or {})
    return subprocess.run([command, *arguments], cwd=repository, env=env, check=False, capture_output=True, text=True)


def _git(repository: Path, *arguments: str) -> None:
    result = _run(repository, "git", *arguments)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)


def _fixture(tmp_path: Path) -> tuple[Path, Path]:
    repository = tmp_path / "repository"
    remote = tmp_path / "remote.git"
    skill = repository / ".agents" / "skills" / "heaven-style"
    scripts = repository / "scripts"
    skill.mkdir(parents=True)
    scripts.mkdir(parents=True)
    (skill / "SKILL.md").write_text("version: 1\n", encoding="utf-8")
    script = scripts / SOURCE_SCRIPT.name
    shutil.copy2(SOURCE_SCRIPT, script)
    _git(repository, "init", "--initial-branch=legacy")
    _git(repository, "config", "user.name", "Blueprint Test")
    _git(repository, "config", "user.email", "blueprint@example.invalid")
    _git(repository, "add", ".")
    _git(repository, "commit", "-m", "Initial skill")
    _git(repository, "branch", "next")
    _git(tmp_path, "init", "--bare", str(remote))
    _git(repository, "remote", "add", "origin", str(remote))
    _git(repository, "push", "origin", "legacy", "next")
    return repository, script


def test_skill_sync_accepts_configurable_local_branches(tmp_path: Path) -> None:
    repository, script = _fixture(tmp_path)

    result = _run(repository, "bash", str(script), "legacy,next")

    assert result.returncode == 0
    assert "byte-identical across 2 branches" in result.stdout
    assert "legacy=" in result.stdout
    assert "next=" in result.stdout


def test_skill_sync_fetches_remote_branches_and_rejects_divergence(tmp_path: Path) -> None:
    repository, script = _fixture(tmp_path)
    _git(repository, "switch", "next")
    (repository / ".agents" / "skills" / "heaven-style" / "SKILL.md").write_text("version: 2\n", encoding="utf-8")
    _git(repository, "add", ".agents/skills/heaven-style/SKILL.md")
    _git(repository, "commit", "-m", "Diverge skill")
    _git(repository, "push", "origin", "next")
    _git(repository, "switch", "legacy")
    _git(repository, "branch", "-D", "next")

    result = _run(
        repository,
        "bash",
        str(script),
        environment={
            "HEAVEN_STYLE_BRANCHES": "legacy,next",
            "HEAVEN_STYLE_CURRENT_BRANCH": "legacy",
            "HEAVEN_STYLE_FETCH_REMOTE": "origin",
        },
    )

    assert result.returncode == 1
    assert "differs across configured branches" in result.stderr
    assert "legacy=" in result.stderr
    assert "next=" in result.stderr


def test_skill_sync_rejects_uncommitted_current_skill(tmp_path: Path) -> None:
    repository, script = _fixture(tmp_path)
    (repository / ".agents" / "skills" / "heaven-style" / "SKILL.md").write_text("version: dirty\n", encoding="utf-8")

    result = _run(
        repository,
        "bash",
        str(script),
        "legacy",
        "next",
        environment={"HEAVEN_STYLE_CURRENT_BRANCH": "legacy"},
    )

    assert result.returncode == 1
    assert "has uncommitted changes on legacy" in result.stderr
