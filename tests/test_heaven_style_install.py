"""Behavioral tests for transactional heaven-style installation and mirrors."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
INSTALL_SCRIPT = ROOT / ".agents" / "skills" / "heaven-style" / "scripts" / "install.py"
SPEC = importlib.util.spec_from_file_location("heaven_style_install", INSTALL_SCRIPT)
assert SPEC and SPEC.loader
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


def _valid_skill(path: Path) -> None:
    installer.copy_skill_tree(installer.SKILL_ROOT, path)


def test_mirror_prunes_stale_managed_files_and_preserves_local_content(tmp_path: Path) -> None:
    mirror = tmp_path / "heaven-style"
    _valid_skill(mirror)
    stale_script = mirror / "scripts" / "sync.py"
    stale_script.write_text("stale = True\n", encoding="utf-8")
    local_cache = mirror / "assets" / "project-reference" / "marker.txt"
    local_cache.parent.mkdir(parents=True)
    local_cache.write_text("keep\n", encoding="utf-8")
    local_note = mirror / "LOCAL.md"
    local_note.write_text("keep\n", encoding="utf-8")
    local_machine = mirror / "assets" / "instance" / "machine.local.md"
    local_machine.parent.mkdir(parents=True, exist_ok=True)
    local_machine.write_text("keep local machine facts\n", encoding="utf-8")

    installer.mirror_skill(str(mirror))

    assert not stale_script.exists()
    assert local_cache.read_text(encoding="utf-8") == "keep\n"
    assert local_note.read_text(encoding="utf-8") == "keep\n"
    assert local_machine.read_text(encoding="utf-8") == "keep local machine facts\n"
    index = (mirror / "references" / "index.yaml").read_text(encoding="utf-8")
    assert "  sync:" not in index


def test_failed_global_install_keeps_previous_verified_skill(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    agents_root = tmp_path / "agents"
    target = agents_root / installer.SKILL_NAME
    _valid_skill(target)
    sentinel = target / "previous-install.txt"
    sentinel.write_text("previous\n", encoding="utf-8")
    local_machine = target / "assets" / "instance" / "machine.local.md"
    local_machine.parent.mkdir(parents=True, exist_ok=True)
    local_machine.write_text("keep local machine facts\n", encoding="utf-8")
    monkeypatch.setenv("HEAVEN_STYLE_AGENTS_ROOT", str(agents_root))

    def fail_index(_skill_root: Path) -> None:
        raise RuntimeError("injected index failure")

    monkeypatch.setattr(installer, "index_skill", fail_index)

    with pytest.raises(RuntimeError, match="injected index failure"):
        installer.install_global()

    assert sentinel.read_text(encoding="utf-8") == "previous\n"
    assert local_machine.read_text(encoding="utf-8") == "keep local machine facts\n"
    assert installer.is_heaven_style_skill(target)
    assert not list(agents_root.glob(".heaven-style.stage-*"))


def test_global_install_replaces_previous_skill_after_staging(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    agents_root = tmp_path / "agents"
    target = agents_root / installer.SKILL_NAME
    _valid_skill(target)
    sentinel = target / "previous-install.txt"
    sentinel.write_text("previous\n", encoding="utf-8")
    local_machine = target / "assets" / "instance" / "machine.local.md"
    local_machine.parent.mkdir(parents=True, exist_ok=True)
    local_machine.write_text("keep local machine facts\n", encoding="utf-8")
    monkeypatch.setenv("HEAVEN_STYLE_AGENTS_ROOT", str(agents_root))

    installed = installer.install_global()

    assert installed == target
    assert installer.is_heaven_style_skill(target)
    assert installer.read_skill_version(target) == "0.1.2.15"
    assert not sentinel.exists()
    assert local_machine.read_text(encoding="utf-8") == "keep local machine facts\n"
    assert not list(agents_root.glob(".heaven-style.stage-*"))


def test_mirror_refuses_non_skill_content(tmp_path: Path) -> None:
    target = tmp_path / "not-a-skill"
    target.mkdir()
    (target / "important.txt").write_text("do not replace\n", encoding="utf-8")

    with pytest.raises(RuntimeError, match="not a verified heaven-style skill"):
        installer.mirror_skill(str(target))

    assert (target / "important.txt").read_text(encoding="utf-8") == "do not replace\n"
