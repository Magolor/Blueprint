# 2026-06-27 Progress

## Docs Governance Operating Model

- Type: docs
- Links: `docs/plans/2026-06-27-docs-governance.md`
- Summary: Defined a stronger docs operating model for Blueprint so agents know when to update goals, plans, resources, reports, and append-only progress notes.
- Decisions: Use `docs/plans/` for multi-slice executable plans and `docs/reports/` for durable review, refactor, and survey reports. Keep `docs/progress/YYYY-MM-DD/README.md` as the dated append-only handoff surface.
- Verification: `rtk bash scripts/sync-readme.bash`; `rtk bash scripts/sync-readme.bash --check`; `rtk uv run python .agents/skills/heaven-style/scripts/install.py --in-place --skip-sync`; `rtk uv run python .agents/skills/heaven-style/scripts/scan.py AGENTS.md docs README.en.md README.md src/blueprint/resources/README.md .agents/skills/heaven-style/SKILL.md .agents/skills/heaven-style/references/tasks/code-review.md .agents/skills/heaven-style/references/workflows/architect.md`; `rtk proxy git diff --check`; `rtk bash scripts/flake.bash --ci`.
- Next: Refresh `README.zh.md` through the translation workflow if translated docs are in scope. The standard global skill install was retried later and completed successfully.

## 0.1.1.5 Version Alignment

- Type: release-prep
- Links: `src/blueprint/version.py`, `.agents/skills/heaven-style/SKILL.md`, `C:\Users\magol\.agents\skills\heaven-style`, `C:\Users\magol\.agents\heaven-style-claude-marketplace`
- Summary: Aligned Blueprint package metadata and the standard/Claude-plugin user installs of `heaven-style` to `0.1.1.5`, matching the HeavenBase release-prep train.
- Decisions: Kept Blueprint's `heavenbase>=0.1.1.1` runtime floor unchanged until HeavenBase `0.1.1.5` is actually published to PyPI; otherwise Blueprint lock/sync would require an unreleased dependency.
- Verification: `rtk bash scripts/sync-env.bash --check`; `rtk uv run python .agents/skills/heaven-style/scripts/index.py --check`; `rtk uv run python .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts`; `rtk uv run python -m py_compile .agents/skills/heaven-style/scripts/index.py .agents/skills/heaven-style/scripts/install.py .agents/skills/heaven-style/scripts/sync.py .agents/skills/heaven-style/scripts/scan.py`; `rtk bash scripts/flake.bash --ci`; `rtk bash scripts/test.bash`; `rtk uv build`; `rtk uv run --with twine twine check "dist/blueprint-0.1.1.5*"`.
- Next: Publish HeavenBase first, then revisit Blueprint's runtime dependency floor if the starter should require the newly published `0.1.1.5`.

## Test Compress Task

- Type: skill-docs
- Links: `.agents/skills/heaven-style/references/tasks/test-compress.md`, `.agents/skills/heaven-style/references/rules/project/test.md`, `AGENTS.md`, `pyproject.toml`, `scripts/test.bash`
- Summary: Added the `test-compress` task for pruning oddly specific, legacy, redundant, or non-contract pytest coverage while preserving modular behavior tests and marker-gated fast/full suites.
- Decisions: Registered `fast` and `full` pytest markers under strict markers, kept Blueprint and heaven-style versions at `0.1.1.5`, and completed the standard global `heaven-style` install after the earlier locked-copy blocker cleared.
- Verification: `rtk uv run python .agents/skills/heaven-style/scripts/index.py`; `rtk uv run python .agents/skills/heaven-style/scripts/index.py --check`; `rtk uv run python .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts`; `rtk bash scripts/test.bash`; `rtk bash -n scripts/test.bash`; `rtk proxy git diff --check`; `rtk bash scripts/flake.bash --ci`; `rtk uv run python .agents/skills/heaven-style/scripts/install.py --in-place --skip-sync`; `rtk bash scripts/sync-env.bash --check`; `rtk uv run python .agents/skills/heaven-style/scripts/install.py`.
- Next: Use `test-compress` for future large pytest cleanup passes.
