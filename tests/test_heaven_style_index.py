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
        _frontmatter(name="overview", description="Choose rules.", enabled=True, order=1),
    )
    _write(
        tmp_path / "references" / "rules" / "project" / "docs.md",
        _frontmatter(name="docs", description="Maintain docs.", enabled=True, category="project", order=2),
    )
    _write(
        tmp_path / "references" / "tasks" / "code.md",
        _frontmatter(
            name="code",
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
    assert "schema: heaven-style-index/v3" in first
    assert "version: 0.2.0-alpha.1" in first
    assert "start: references/roles/README.md" in first
    assert "workflow-work-types:" in first
    assert first == (skill_root / "references" / "index.yaml").read_text(encoding="utf-8")


def test_minimal_valid_skill_builds_compact_routes(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)

    result = indexer.build_index(root)

    assert result["skill"]["version"] == "0.1.2.0"
    assert result["counts"]["rules"] == 2
    assert result["routes"]["tasks"]["code"]["path"] == "references/tasks/code.md"


@pytest.mark.parametrize(
    ("path", "before", "after", "error"),
    [
        ("references/tasks/code.md", "- docs\n", "- missing\n", "RELATED_RULE_MISSING:"),
        ("references/rules/project/docs.md", "name: docs", "name: overview", "NAME_DUPLICATE:"),
        ("references/rules/project/docs.md", "name: docs\n", "", "NAME_INVALID:"),
        ("references/rules/project/docs.md", "# Body", "[Missing](missing.md)", "LINK_MISSING:"),
        ("references/rules/project/docs.md", "---", "", "FRONTMATTER_MISSING:"),
        ("references/rules/project/docs.md", "# Body", "[Outside](../../../../outside.md)", "LINK_ESCAPE:"),
        ("references/rules/project/docs.md", "order: 2", "order: wrong", "FIELD_TYPE:"),
    ],
)
def test_invalid_source_fails_closed(tmp_path: Path, path: str, before: str, after: str, error: str) -> None:
    root = _valid_skill(tmp_path)
    (tmp_path.parent / "outside.md").write_text("# Outside\n", encoding="utf-8")
    source = root / path
    source.write_text(source.read_text(encoding="utf-8").replace(before, after), encoding="utf-8")

    with pytest.raises(indexer.IndexValidationError) as caught:
        indexer.build_index(root)

    assert any(item.startswith(error) for item in caught.value.errors)


def test_source_digest_covers_indexed_scripts(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)
    first = indexer.build_index(root)["skill"]["source_digest"]
    (root / "scripts" / "check.py").write_text('#!/usr/bin/env python3\n"""Changed check."""\n', encoding="utf-8")

    second = indexer.build_index(root)["skill"]["source_digest"]

    assert second != first


def test_roles_and_nested_task_manuals_are_discoverable(tmp_path: Path) -> None:
    root = _valid_skill(tmp_path)
    _write(root / "references/roles/default.md", _frontmatter(name="role-default", description="Use by default."))
    _write(root / "references/tasks/code/slices.md", _frontmatter(name="code-slices", description="Read for ordered slices."))

    result = indexer.build_index(root)

    assert result["routes"]["roles"]["role-default"]["path"] == "references/roles/default.md"
    assert result["routes"]["tasks"]["code-slices"] == {
        "path": "references/tasks/code/slices.md",
        "use": "Read for ordered slices.",
    }

    _write(root / "references/roles/default.md", _frontmatter(name="role-default"))
    with pytest.raises(indexer.IndexValidationError, match="FIELD_MISSING: references/roles/default.md: description"):
        indexer.build_index(root)
