"""Downstream template rename behavior."""

from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def test_rename_keeps_heaven_style_source_neutral(tmp_path: Path) -> None:
    """The downstream rename changes product owners but not the shared skill."""

    script = tmp_path / "scripts" / "rename.bash"
    script.parent.mkdir()
    shutil.copy2(ROOT / "scripts" / "rename.bash", script)
    package = tmp_path / "src" / "blueprint"
    package.mkdir(parents=True)
    (package / "__init__.py").write_text("from blueprint.version import __version__\n", encoding="utf-8")
    (package / "config.py").write_text(
        'class ProjectConfig:\n    pass\n\nDEFAULT_CONFIG = ProjectIdentity(name="Blueprint")\n',
        encoding="utf-8",
    )
    (package / "version.py").write_text('__version__ = "1.0.0"\n', encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "blueprint"\n[project.scripts]\nbp = "blueprint.cli:main"\n'
        '[tool.setuptools.dynamic]\nversion = { attr = "blueprint.version.__version__" }\n',
        encoding="utf-8",
    )
    (tmp_path / "README.md").write_text("# Blueprint\n\nRun `uv run bp`.\n", encoding="utf-8")
    skill = tmp_path / ".agents" / "skills" / "heaven-style" / "SKILL.md"
    skill.parent.mkdir(parents=True)
    skill.write_text("Blueprint remains source-neutral.\n", encoding="utf-8")

    result = subprocess.run(
        [
            "bash",
            str(script),
            "--project-name",
            "Example Project",
            "--dist-name",
            "example-project",
            "--import-name",
            "example_project",
            "--cli-name",
            "example",
            "--yes",
        ],
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert not package.exists()
    assert (tmp_path / "src" / "example_project").is_dir()
    renamed_config = (tmp_path / "src" / "example_project" / "config.py").read_text(encoding="utf-8")
    assert "class ProjectConfig:" in renamed_config
    assert 'ProjectIdentity(name="Example Project")' in renamed_config
    assert 'name = "example-project"' in (tmp_path / "pyproject.toml").read_text(encoding="utf-8")
    assert 'example = "example_project.cli:main"' in (tmp_path / "pyproject.toml").read_text(encoding="utf-8")
    assert skill.read_text(encoding="utf-8") == "Blueprint remains source-neutral.\n"
