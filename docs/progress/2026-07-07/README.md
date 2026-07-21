# 2026-07-07 Progress

## Heaven-style GUI Design Reference

- Type: docs
- Links: `.agents/skills/heaven-style/references/design/gui-style.md`, `.agents/skills/heaven-style/SKILL.md`
- Summary: Initialized the Heaven-style `references/design/` surface with a framework-neutral GUI style guide for future frontend, desktop, dashboard, and app-shell work. The guide preserves the three-mode theme token contract and links only public visual references.
- Decisions: Keep detailed GUI rules out of `SKILL.md`; route future GUI work to `references/design/gui-style.md`. Treat "Materialism" as a local Heaven-style term for calm physical surfaces, not as Google Material Design.
- Verification: `rtk uv run python .agents/skills/heaven-style/scripts/install.py`; `rtk uv run python .agents/skills/heaven-style/scripts/index.py`; `rtk uv run python .agents/skills/heaven-style/scripts/index.py --check`; `rtk uv run python .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts`; `rtk uv run python -m py_compile .agents/skills/heaven-style/scripts/index.py .agents/skills/heaven-style/scripts/install.py .agents/skills/heaven-style/scripts/sync.py .agents/skills/heaven-style/scripts/scan.py`; `rtk bash scripts/flake.bash --ci --paths .agents/skills/heaven-style/scripts`; `rtk bash scripts/test.bash` (expected no tests found); `rtk git diff --check`.
- Next: Review and commit the Heaven-style `0.1.1.6` GUI design reference update.

## GUI Component Unity Follow-up

- Type: docs
- Links: `.agents/skills/heaven-style/references/design/gui-style.md`
- Summary: Added an explicit component-unity contract so buttons, dropdown lists, search bars, input boxes, tables, popovers, and third-party widgets inherit the same visual system instead of leaking browser or library defaults.
- Decisions: Preserve the theme sources as Light Mode = Ollama White and Dark Mode = GitHub Soft Dark.
- Verification: `rtk uv run python .agents/skills/heaven-style/scripts/install.py`; `rtk uv run python .agents/skills/heaven-style/scripts/index.py --check`; `rtk uv run python .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts`; `rtk uv run python -m py_compile .agents/skills/heaven-style/scripts/index.py .agents/skills/heaven-style/scripts/install.py .agents/skills/heaven-style/scripts/sync.py .agents/skills/heaven-style/scripts/scan.py`; `rtk bash scripts/flake.bash --ci --paths .agents/skills/heaven-style/scripts`; `rtk bash scripts/test.bash` (expected no tests found); `rtk git diff --check`.
- Next: Review and commit the Heaven-style `0.1.1.6` GUI design reference update.

## GUI Design Indexed-only Exposure

- Type: docs
- Links: `.agents/skills/heaven-style/references/design/gui-style.md`, `.agents/skills/heaven-style/references/index.yaml`
- Summary: Kept the GUI design guide indexed under `references.design` while removing it from `SKILL.md` and `references/rules/overview.md` default routing.
- Decisions: Mark the design guide frontmatter with `default_exposed: false` so future index readers can distinguish indexed optional references from fast-path rule surfaces.
- Verification: `rtk uv run python .agents/skills/heaven-style/scripts/index.py`; `rtk uv run python .agents/skills/heaven-style/scripts/install.py` failed in `sync.py` reference refresh; `rtk uv run python .agents/skills/heaven-style/scripts/install.py --skip-sync`; `rtk uv run python .agents/skills/heaven-style/scripts/index.py --check`; `rtk uv run python .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts`; `rtk uv run python -m py_compile .agents/skills/heaven-style/scripts/index.py .agents/skills/heaven-style/scripts/install.py .agents/skills/heaven-style/scripts/sync.py .agents/skills/heaven-style/scripts/scan.py`; `rtk bash scripts/flake.bash --ci --paths .agents/skills/heaven-style/scripts`; `rtk bash scripts/test.bash` (expected no tests found); `rtk git diff --check`.
- Next: Review and commit the Heaven-style `0.1.1.6` GUI design reference update.

## Heaven-style Version Preservation

- Type: docs
- Links: `.agents/skills/heaven-style/SKILL.md`, `.agents/skills/heaven-style/references/index.yaml`
- Summary: Preserved the Heaven-style skill version at `0.1.1.6` while keeping the GUI design reference indexed.
- Decisions: Do not bump the Heaven-style version for this reference-only addition.
- Verification: `rtk uv run python .agents/skills/heaven-style/scripts/index.py`; `rtk uv run python .agents/skills/heaven-style/scripts/install.py --skip-sync`; `rtk uv run python .agents/skills/heaven-style/scripts/index.py --check`; `rtk uv run python .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts`; `rtk uv run python -m py_compile .agents/skills/heaven-style/scripts/index.py .agents/skills/heaven-style/scripts/install.py .agents/skills/heaven-style/scripts/sync.py .agents/skills/heaven-style/scripts/scan.py`; `rtk bash scripts/flake.bash --ci --paths .agents/skills/heaven-style/scripts`; `rtk bash scripts/test.bash` (expected no tests found); `rtk git diff --check`.
- Next: Commit and push the GUI design reference update.
