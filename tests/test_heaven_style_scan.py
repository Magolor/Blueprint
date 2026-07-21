"""Contract tests for the skill scanner's narrow hermetic-script exception."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_SCRIPT = ROOT / ".agents" / "skills" / "heaven-style" / "scripts" / "scan.py"
SPEC = importlib.util.spec_from_file_location("heaven_style_scan", SCAN_SCRIPT)
assert SPEC and SPEC.loader
scanner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scanner)


def test_banned_import_is_reported_without_exception(tmp_path: Path) -> None:
    path = tmp_path / "ordinary.py"
    path.write_text("from pathlib import Path\n", encoding="utf-8")

    issues = scanner.scan_file(str(path), allow_utils=False)

    assert len(issues) == 1
    assert "import pathlib -> use heavenbase.utils" in issues[0]


def test_standalone_control_plane_marker_allows_hermetic_imports(tmp_path: Path) -> None:
    path = tmp_path / "control.py"
    path.write_text(
        "#!/usr/bin/env python3\n# heaven-style-scan: standalone-control-plane\nfrom pathlib import Path\n",
        encoding="utf-8",
    )

    assert scanner.scan_file(str(path), allow_utils=False) == []
