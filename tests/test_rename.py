"""End-to-end coverage for instantiating the real Blueprint tree."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.10 compatibility
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[1]
RENAME_ARGS = (
    "--project-name",
    "Orbit Forge",
    "--dist-name",
    "orbit-forge",
    "--import-name",
    "orbit_forge",
    "--cli-name",
    "orbitctl",
    "--yes",
)


def _copy_real_tree(tmp_path: Path) -> Path:
    """Copy the working tree while avoiding generated environments and caches."""

    target = tmp_path / "project"

    def ignore(directory: str, names: list[str]) -> set[str]:
        root = Path(directory)
        ignored = {
            name
            for name in names
            if name
            in {
                ".venv",
                "dist",
                "build",
                ".temp",
                "cache",
                ".cache",
                "__pycache__",
                ".pytest_cache",
                ".mypy_cache",
                ".ruff_cache",
            }
            or name.endswith(".egg-info")
        }
        if root == ROOT and ".git" in names and (root / ".git").is_dir():
            ignored.add(".git")
        return ignored

    shutil.copytree(ROOT, target, ignore=ignore)
    if not (target / ".git").is_file():
        (target / ".git").write_text("gitdir: /tmp/blueprint-linked-worktree\n", encoding="utf-8")
    return target


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _run_rename(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["REPO_PYTHON_PREFERENCE"] = "venv-first"
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
    return subprocess.run(
        ["bash", "scripts/rename.bash", *args],
        cwd=root,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )


def test_real_tree_rename_preserves_boundaries_and_instantiates_project(tmp_path: Path) -> None:
    root = _copy_real_tree(tmp_path)
    git_before = (root / ".git").read_bytes()
    skill_before = (root / ".agents" / "skills" / "heaven-style" / "SKILL.md").read_bytes()
    protected = {
        ".venv/blueprint-bin/blueprint.txt": "Blueprint blueprint bp blueprint-gui\n",
        "dist/blueprint-artifacts/blueprint.txt": "Blueprint blueprint bp blueprint-gui\n",
        "build/blueprint-build/blueprint.txt": "Blueprint blueprint bp blueprint-gui\n",
        ".temp/blueprint-notes/blueprint.txt": "Blueprint blueprint bp blueprint-gui\n",
        "cache/blueprint-cache/blueprint.txt": "Blueprint blueprint bp blueprint-gui\n",
        ".pytest_cache/blueprint-cache/blueprint.txt": "Blueprint blueprint bp blueprint-gui\n",
        "src/blueprint.egg-info/blueprint.txt": "Blueprint blueprint bp blueprint-gui\n",
    }
    for relative, content in protected.items():
        _write(root / relative, content)
    _write(
        root / "docs" / "resources" / "marker-probe.md",
        "# Marker probe\n\nKeep before.\n\n"
        "<!-- blueprint-template-only:start -->\n"
        "Blueprint-only prose must leave the generated project.\n"
        "<!-- blueprint-template-only:end -->\n"
        "Keep after.\n",
    )
    _write(
        root / "docs" / "reports" / "reviews" / "2026-07-21-blueprint-probe.md",
        "# Blueprint report\n\n- Status: Superseded\n",
    )

    result = _run_rename(root, *RENAME_ARGS)

    assert result.returncode == 0, f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    assert (root / ".git").read_bytes() == git_before
    assert (root / ".agents" / "skills" / "heaven-style" / "SKILL.md").read_bytes() == skill_before
    for relative, content in protected.items():
        path = root / relative
        assert path.is_file(), relative
        assert path.read_text(encoding="utf-8") == content

    assert (root / "src" / "orbit_forge").is_dir()
    assert not (root / "src" / "blueprint").exists()
    assert not (root / ".blueprint-template.yaml").exists()
    assert not (root / "BLUEPRINT.md").exists()
    assert not (root / "README.zh.md").exists()
    assert not (root / "scripts" / "rename.bash").exists()
    assert not (root / "tests" / "test_rename.py").exists()
    assert not list((root / "docs" / "plans").glob("20??-??-??-*.md"))
    assert not list((root / "docs" / "reports").rglob("20??-??-??-*.md"))

    queue = yaml.safe_load((root / "docs" / "tasks.yaml").read_text(encoding="utf-8"))
    assert queue == {
        "schema": "heaven.tasks/v1",
        "project": "Orbit Forge",
        "updated": date.today().isoformat(),
        "tasks": [],
    }
    assert not (root / "docs" / "tasks.template.yaml").exists()

    devlog = (root / "docs" / "DEVLOG.md").read_text(encoding="utf-8")
    assert devlog.count("\n## ") == 1
    assert f"## {date.today().isoformat()} — Orbit Forge initialized" in devlog
    assert "Blueprint 0.1.2.0 release boundary" not in devlog
    assert "- Next: none" in devlog

    marker_probe = (root / "docs" / "resources" / "marker-probe.md").read_text(encoding="utf-8")
    assert marker_probe == "# Marker probe\n\nKeep before.\n\nKeep after.\n"

    project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
    assert project["project"]["name"] == "orbit-forge"
    assert "authors" not in project["project"]
    assert "urls" not in project["project"]
    assert project["project"]["scripts"] == {"orbitctl": "orbit_forge.cli:main"}
    assert project["project"]["gui-scripts"] == {"orbitctl-gui": "orbit_forge.gui:main"}
    assert project["tool"]["setuptools"]["package-data"] == {"orbit_forge": ["resources/**/*"]}
    assert project["tool"]["setuptools"]["dynamic"]["version"] == {"attr": "orbit_forge.version.__version__"}

    dockerfile = (root / "Dockerfile").read_text(encoding="utf-8")
    assert 'ENTRYPOINT ["orbitctl"]' in dockerfile
    readme = (root / "README.en.md").read_text(encoding="utf-8")
    assert "uv run orbitctl --help" in readme
    assert "uv run orbitctl-gui --help" in readme
    assert "docker build -t orbit-forge ." in readme
    assert "uv run bp --help" not in readme
    assert "docs/tasks.template.yaml" not in readme
    assert "| `docs/tasks.yaml` | Single writable task queue for active operational work. |" in readme
    assert (root / "README.md").read_bytes() == (root / "README.en.md").read_bytes()
    assert (root / "src" / "orbit_forge" / "resources" / "README.md").read_bytes() == (root / "README.en.md").read_bytes()

    cli_source = (root / "src" / "orbit_forge" / "cli.py").read_text(encoding="utf-8")
    config_source = (root / "src" / "orbit_forge" / "config.py").read_text(encoding="utf-8")
    gui_source = (root / "src" / "orbit_forge" / "gui.py").read_text(encoding="utf-8")
    assert 'PackageCLIContext(package="orbitctl"' in cli_source
    assert "CM_ORBIT_FORGE" in cli_source
    assert 'package="orbit_forge"' in config_source
    assert 'scope="orbit_forge"' in config_source
    assert 'prog="orbitctl-gui"' in gui_source

    workflow = (root / ".github" / "workflows" / "release.yml").read_text(encoding="utf-8")
    assert "src/orbit_forge/version.py" in workflow
    assert "import os, orbit_forge" in workflow
    assert "name: orbit-forge-dist" in workflow
    assert "orbitctl --version" in workflow
    assert "orbitctl-gui --help" in workflow
    assert "bp --version" not in workflow

    docs_check = subprocess.run(
        [sys.executable, "scripts/docs.py", "--root", str(root), "check"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    assert docs_check.returncode == 0, docs_check.stderr
    assert "Documentation contract is valid (0 active task(s))." in docs_check.stdout


def test_rename_rejects_python_keyword_before_mutation(tmp_path: Path) -> None:
    root = _copy_real_tree(tmp_path)
    git_before = (root / ".git").read_bytes()

    result = _run_rename(
        root,
        "--project-name",
        "Keyword Project",
        "--dist-name",
        "keyword-project",
        "--import-name",
        "class",
        "--cli-name",
        "keyword-tool",
        "--yes",
    )

    assert result.returncode != 0
    assert "must not be a Python keyword" in result.stderr
    assert (root / ".git").read_bytes() == git_before
    assert (root / ".blueprint-template.yaml").is_file()
    assert (root / "docs" / "tasks.template.yaml").is_file()
    assert not (root / "docs" / "tasks.yaml").exists()
    assert (root / "src" / "blueprint").is_dir()


def test_rename_rejects_dirty_task_starter_before_promotion(tmp_path: Path) -> None:
    root = _copy_real_tree(tmp_path)
    queue_path = root / "docs" / "tasks.template.yaml"
    queue = yaml.safe_load(queue_path.read_text(encoding="utf-8"))
    queue["tasks"] = [
        {
            "id": "TMP-001",
            "title": "Template work leaked into the starter",
            "status": "ready",
            "priority": "P1",
            "owner": None,
            "parent": None,
            "updated": date.today().isoformat(),
            "acceptance": ["Rename refuses the dirty starter."],
            "depends_on": [],
            "links": [],
        }
    ]
    queue_path.write_text(yaml.safe_dump(queue, sort_keys=False), encoding="utf-8")
    git_before = (root / ".git").read_bytes()

    result = _run_rename(root, *RENAME_ARGS)

    assert result.returncode != 0
    assert "TEMPLATE_QUEUE_NOT_INERT" in result.stderr
    assert (root / ".git").read_bytes() == git_before
    assert (root / ".blueprint-template.yaml").is_file()
    assert queue_path.is_file()
    assert not (root / "docs" / "tasks.yaml").exists()
    assert (root / "src" / "blueprint").is_dir()
