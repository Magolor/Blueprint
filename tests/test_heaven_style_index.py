"""Contract tests for the compact hermetic heaven-style index."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
INDEX_SCRIPT = ROOT / ".agents" / "skills" / "heaven-style" / "scripts" / "index.py"
SPEC = importlib.util.spec_from_file_location("heaven_style_index", INDEX_SCRIPT)
assert SPEC and SPEC.loader
indexer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(indexer)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _frontmatter(**fields: object) -> str:
    import yaml

    return f"---\n{yaml.safe_dump(fields, sort_keys=False)}---\n\n# Body\n"


def _valid_skill(tmp_path: Path) -> Path:
    _write(
        tmp_path / "SKILL.md",
        _frontmatter(name="fixture-style", description="Fixture skill.", metadata={"version": "0.1.2.0"}) + "\n[Rules](references/rules/overview.md)\n",
    )
    _write(
        tmp_path / "references" / "rules" / "overview.md",
        _frontmatter(id="overview", title="Overview", description="Choose rules.", enabled=True, blocking=True, order=1),
    )
    _write(
        tmp_path / "references" / "rules" / "project" / "docs.md",
        _frontmatter(id="docs", title="Docs", description="Maintain docs.", enabled=True, category="project", order=2),
    )
    _write(
        tmp_path / "references" / "tasks" / "code.md",
        _frontmatter(
            id="code",
            task_kind="code",
            description="Implement code.",
            enabled=True,
            order=1,
            related_rules=["overview", "docs"],
        ),
    )
    _write(tmp_path / "scripts" / "check.py", '#!/usr/bin/env python3\n"""Check the fixture."""\n')
    return tmp_path


def test_real_index_is_compact_deterministic_and_current() -> None:
    skill_root = INDEX_SCRIPT.parents[1]

    first = indexer.render_index(indexer.build_index(skill_root))
    second = indexer.render_index(indexer.build_index(skill_root))

    assert first == second
    assert "generated_at" not in first
    assert "schema: heaven-style-index/v2" in first
    assert "version: 0.1.2.15" in first
    assert "start: references/workflows/start.md" in first
    assert "workflow-work-types:" in first
    assert len(first.splitlines()) <= 600
    assert len(first.encode("utf-8")) <= 20_000
    assert first == (skill_root / "references" / "index.yaml").read_text(encoding="utf-8")


def test_minimal_valid_skill_builds_compact_routes(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)

    result = indexer.build_index(root)

    assert result["skill"]["version"] == "0.1.2.0"
    assert result["counts"]["rules"] == 2
    assert result["routes"]["tasks"]["code"]["path"] == "references/tasks/code.md"


def test_missing_related_rule_fails_closed(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)
    task = root / "references" / "tasks" / "code.md"
    task.write_text(task.read_text(encoding="utf-8").replace("- docs\n", "- missing\n"), encoding="utf-8")

    with pytest.raises(indexer.IndexValidationError) as caught:
        indexer.build_index(root)

    assert any(error.startswith("RELATED_RULE_MISSING:") for error in caught.value.errors)


def test_duplicate_id_fails_closed(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)
    _write(
        root / "references" / "rules" / "project" / "duplicate.md",
        _frontmatter(id="docs", title="Duplicate", description="Invalid duplicate.", enabled=True),
    )

    with pytest.raises(indexer.IndexValidationError) as caught:
        indexer.build_index(root)

    assert any(error.startswith("ID_DUPLICATE: docs:") for error in caught.value.errors)


def test_broken_link_fails_closed(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)
    rule = root / "references" / "rules" / "project" / "docs.md"
    rule.write_text(rule.read_text(encoding="utf-8") + "\n[Missing](missing.md)\n", encoding="utf-8")

    with pytest.raises(indexer.IndexValidationError) as caught:
        indexer.build_index(root)

    assert "LINK_MISSING: references/rules/project/docs.md -> missing.md" in caught.value.errors


def test_malformed_frontmatter_fails_closed(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)
    _write(root / "references" / "rules" / "project" / "bad.md", "# Missing frontmatter\n")

    with pytest.raises(indexer.IndexValidationError) as caught:
        indexer.build_index(root)

    assert "FRONTMATTER_MISSING: references/rules/project/bad.md" in caught.value.errors


def test_link_cannot_escape_skill_root(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)
    outside = tmp_path.parent / "outside.md"
    outside.write_text("# Outside\n", encoding="utf-8")
    rule = root / "references" / "rules" / "project" / "docs.md"
    rule.write_text(rule.read_text(encoding="utf-8") + "\n[Outside](../../../../outside.md)\n", encoding="utf-8")

    with pytest.raises(indexer.IndexValidationError) as caught:
        indexer.build_index(root)

    assert any(error.startswith("LINK_ESCAPE:") for error in caught.value.errors)


def test_invalid_metadata_type_fails_closed(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)
    rule = root / "references" / "rules" / "project" / "docs.md"
    rule.write_text(rule.read_text(encoding="utf-8").replace("order: 2", "order: wrong"), encoding="utf-8")

    with pytest.raises(indexer.IndexValidationError) as caught:
        indexer.build_index(root)

    assert "FIELD_TYPE: references/rules/project/docs.md: order must be an integer" in caught.value.errors


def test_source_digest_covers_indexed_scripts(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)
    first = indexer.build_index(root)["skill"]["source_digest"]
    (root / "scripts" / "check.py").write_text('#!/usr/bin/env python3\n"""Changed check."""\n', encoding="utf-8")

    second = indexer.build_index(root)["skill"]["source_digest"]

    assert second != first
