# 2026-07-06 Progress

## Heaven-style 0.1.1.6 Release Readiness

- Type: release
- Links: `.agents/skills/heaven-style/`, `src/blueprint/version.py`
- Summary: Prepared Blueprint `0.1.1.6` with the Heaven-style rule tree split into language-specific code rule folders, new Python `docstring`, `files`, and `solid` rules, macOS environment-maintenance assets, future Rust/TypeScript rule placeholders, and version alignment across Blueprint metadata.
- Decisions: Keep Rust and TypeScript support as inert `.gitkeep` scaffolding for this release. Treat global interactive Python as Miniforge `main`, while project work prefers repo wrappers and `uv run python`; the machine-note generator now preserves that distinction.
- Verification: `uv run python .agents/skills/heaven-style/scripts/machine.py`; machine-note temp regeneration diff; `uv run python .agents/skills/heaven-style/scripts/index.py`; `uv run python .agents/skills/heaven-style/scripts/index.py --check`; `uv run python .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts`; Markdown local-link check; `git diff --check`; `uv run python -m py_compile .agents/skills/heaven-style/scripts/index.py .agents/skills/heaven-style/scripts/install.py .agents/skills/heaven-style/scripts/sync.py .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts/machine.py`; `bash scripts/sync-env.bash --check`; `bash scripts/flake.bash --ci`; `bash scripts/test.bash`; `uv build`; `uv run --with twine twine check "dist/blueprint-0.1.1.6*"`; `uv run python .agents/skills/heaven-style/scripts/install.py --skip-sync`.
- Next: Commit and push the staged `0.1.1.6` release-prep set after final status review.
