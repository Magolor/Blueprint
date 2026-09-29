"""Verify machine reports preserve unknown facts and omit failed probe output."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents/skills/heaven-style/scripts/machine.py"
SPEC = importlib.util.spec_from_file_location("heaven_style_machine", SCRIPT)
assert SPEC and SPEC.loader
machine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(machine)


def test_failed_probe_does_not_publish_stdout_or_diagnostics() -> None:
    code, output = machine.run(
        (
            sys.executable,
            "-c",
            "import sys; print('untrusted value'); print('private diagnostic', file=sys.stderr); sys.exit(1)",
        )
    )

    assert code == 1
    assert output == ""


def test_successful_probe_keeps_stdout_only() -> None:
    code, output = machine.run(
        (
            sys.executable,
            "-c",
            "import sys; print('observed value'); print('private diagnostic', file=sys.stderr)",
        )
    )

    assert code == 0
    assert output == "observed value"


def test_missing_environment_does_not_invent_a_setup(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(machine, "run", lambda _args: (127, ""))
    monkeypatch.setattr(machine.shutil, "which", lambda _name: None)
    monkeypatch.setattr(machine.Path, "home", classmethod(lambda _cls: tmp_path))
    monkeypatch.delenv("SHELL", raising=False)

    report = machine.build_markdown()

    assert report.startswith("---\nname: asset-machine\n")
    assert report.index("## Summary") < report.index("## Identity")
    assert "Homebrew prefix: `unknown`" in report
    assert "Docker context: `unknown`" in report
    assert "Setup checkout: `not found; ask for the setup owner`" in report
    assert "`code`: `not on PATH`" in report
    assert "`python`: `not on PATH`" in report
    assert "/opt/homebrew" not in report
    assert "desktop-linux" not in report
    assert "miniforge3" not in report
    assert machine.DEFAULT_OUTPUT != machine.SKILL_ROOT / "assets/instance/machine.md"


def test_timeout_returns_unknown_without_diagnostics(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def timeout(args: list[str], **kwargs: object) -> None:
        assert kwargs["timeout"] == 15
        raise subprocess.TimeoutExpired(args, 15, output="private output")

    monkeypatch.setattr(machine.subprocess, "run", timeout)

    assert machine.run(("probe",)) == (127, "")
