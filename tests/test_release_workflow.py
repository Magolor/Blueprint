"""Exercise release-workflow Git invariants without network access."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "release.yml"
PYTHON_WORKFLOW = ROOT / ".github" / "workflows" / "python-test.yml"
PYPROJECT = ROOT / "pyproject.toml"


def _git_env() -> dict[str, str]:
    """Return an environment detached from a parent Git invocation."""
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
    return env


def _git(root: Path, *args: str) -> str:
    """Run one isolated Git command and return stdout."""
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        env=_git_env(),
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


@pytest.mark.fast
@pytest.mark.integration
def test_release_fetch_replaces_checkout_lightweight_tag(tmp_path: Path) -> None:
    """Fetch the remote annotated object over checkout's commit-typed tag ref."""
    source = tmp_path / "source"
    remote = tmp_path / "origin.git"
    checkout = tmp_path / "checkout"
    source.mkdir()
    checkout.mkdir()

    _git(source, "init", "--quiet", "--initial-branch=master")
    _git(source, "config", "user.name", "Release Test")
    _git(source, "config", "user.email", "release@example.invalid")
    _git(source, "config", "commit.gpgsign", "false")
    (source / "version.txt").write_text("0.1.2.0\n", encoding="utf-8")
    _git(source, "add", "version.txt")
    _git(source, "commit", "--quiet", "-m", "release fixture")
    _git(source, "tag", "-a", "v0.1.2.0", "-m", "v0.1.2.0")
    _git(tmp_path, "clone", "--quiet", "--bare", str(source), str(remote))

    _git(checkout, "init", "--quiet", "--initial-branch=master")
    _git(checkout, "remote", "add", "origin", str(remote))
    _git(
        checkout,
        "fetch",
        "--no-tags",
        "origin",
        "refs/heads/master:refs/remotes/origin/master",
    )
    _git(checkout, "checkout", "--quiet", "--detach", "refs/remotes/origin/master")
    _git(checkout, "tag", "v0.1.2.0")
    assert _git(checkout, "cat-file", "-t", "refs/tags/v0.1.2.0") == "commit"

    _git(
        checkout,
        "fetch",
        "--force",
        "--no-tags",
        "origin",
        "refs/heads/master:refs/remotes/origin/master",
        "refs/tags/v0.1.2.0:refs/tags/v0.1.2.0",
    )

    assert _git(checkout, "cat-file", "-t", "refs/tags/v0.1.2.0") == "tag"
    assert _git(checkout, "rev-parse", "refs/tags/v0.1.2.0^{commit}") == _git(checkout, "rev-parse", "refs/remotes/origin/master^{commit}")
    assert '"refs/tags/${GITHUB_REF_NAME}:refs/tags/${GITHUB_REF_NAME}"' in WORKFLOW.read_text(encoding="utf-8")


@pytest.mark.fast
def test_python_workflows_match_the_declared_runtime_floor() -> None:
    """Keep package metadata and uv-backed CI on the supported interpreters."""
    release = WORKFLOW.read_text(encoding="utf-8")
    python_tests = PYTHON_WORKFLOW.read_text(encoding="utf-8")
    pyproject = PYPROJECT.read_text(encoding="utf-8")

    assert 'requires-python = ">=3.12,<3.14"' in pyproject
    assert 'target-version = ["py312"]' in pyproject
    assert 'python-version: ["3.12", "3.13"]' in release
    assert 'python-version: ["3.12", "3.13"]' in python_tests
    for workflow in (release, python_tests):
        assert "UV_PYTHON: ${{ matrix.python-version }}" in workflow
        assert "actual == expected, (actual, expected)" in workflow
