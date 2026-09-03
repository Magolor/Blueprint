"""Contract tests for the standalone heaven-style maintenance scanner."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_SCRIPT = ROOT / ".agents" / "skills" / "heaven-style" / "scripts" / "scan.py"
SPEC = importlib.util.spec_from_file_location("heaven_style_scan", SCAN_SCRIPT)
assert SPEC and SPEC.loader
SCAN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCAN)


def test_scan_accepts_standard_library(tmp_path: Path) -> None:
    script = tmp_path / "ok.py"
    script.write_text("from pathlib import Path\nimport subprocess\n", encoding="utf-8")

    assert SCAN.scan_file(script, stdlib_only=True, allow_imports=set()) == []


def test_scan_rejects_project_dependency(tmp_path: Path) -> None:
    script = tmp_path / "coupled.py"
    script.write_text("import project_runtime.utils\n", encoding="utf-8")

    issues = SCAN.scan_file(script, stdlib_only=True, allow_imports=set())

    assert len(issues) == 1
    assert "project_runtime.utils is not standard library or explicitly allowed" in issues[0]


def test_scan_allows_declared_third_party_parser(tmp_path: Path) -> None:
    script = tmp_path / "index.py"
    script.write_text("import yaml\n", encoding="utf-8")

    assert SCAN.scan_file(script, stdlib_only=True, allow_imports={"yaml"}) == []


def test_scan_reports_syntax_error(tmp_path: Path) -> None:
    script = tmp_path / "broken.py"
    script.write_text("def broken(:\n", encoding="utf-8")

    issues = SCAN.scan_file(script, stdlib_only=False, allow_imports=set())

    assert len(issues) == 1
    assert "invalid syntax" in issues[0]
