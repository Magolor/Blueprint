# Heaven-style Service Interface Rule Plan

- Status: Done
- Created: 2026-07-14
- Scope: Add a blocking cross-language heaven-style rule for service-package SDK, API, CLI, GUI, MCP, TUI, and desktop boundaries.
- Links: `.agents/skills/heaven-style/references/rules/project/interfaces.md`; `docs/DEVLOG.md`

## Problem

Heaven-style has public API, extension, Python file-layout, TypeScript architecture, and GUI design guidance, but no single rule that keeps a service package's core SDK, API orchestration, and user interfaces separated. Python CLI backend parity and minimal-versus-releasable GUI stack decisions are also not explicit.

## Success Criteria

- [x] Service packages expose core behavior through a small, preferably OOP Python SDK.
- [x] A real `api/` boundary owns orchestration, serializable contracts, REST/OpenAPI transport, and concurrent-request policy.
- [x] CLI, GUI, MCP, TUI, and future interfaces are thin API wrappers with inward dependency direction.
- [x] Python CLIs declare commands once and support Typer, Click, and argparse simultaneously, defaulting to Typer and sharing Rich presentation.
- [x] Minimal Python GUI and releasable React/TypeScript plus Tauri v2 desktop defaults are explicit.
- [x] Skill routing, generated index, global installation, progress notes, and repository verification are current.

## Non-Goals

- Do not scaffold interface packages in Blueprint.
- Do not prescribe empty folders for interfaces a service does not ship.
- Do not replace language-specific Python or TypeScript mechanics with one generic implementation rule.

## Slices

### Slice 1: Rule and routing

- Goal: Add the normative architecture and make it discoverable from ordinary coding, review, design, explanation, and skill-maintenance routes.
- Touch: `SKILL.md`, project rule map, language/design cross-links, task/workflow metadata.
- Acceptance: The generated index can discover `interfaces` from SDK/API/CLI/GUI/MCP/TUI/OpenAPI/Tauri terms.
- Verification: Index generation/check and relative-link validation.
- Docs: New rule and this plan.

### Slice 2: Install and closeout

- Goal: Refresh the canonical global skill and close the repository artifacts.
- Touch: generated `references/index.yaml`, global install, daily progress note, plan status.
- Acceptance: Skill checks and repository gates pass or carry explicit waivers.
- Verification: Skill install/index, scanner, compile, flake, tests, env/README drift, diff checks.
- Docs: `docs/DEVLOG.md` and plan closeout.

## Progress

- 2026-07-14: Reviewed the existing skill routes, Python file organization, TypeScript architecture/modules, GUI guidance, packaged HeavenBase `CLIRegistry`, the dashboard branch architecture, and current primary CLI/OpenAPI/Tauri documentation; added the rule and routing changes.

## Closeout

- Verification: `rtk uv run python .agents/skills/heaven-style/scripts/install.py`; `index.py --check`; `scan.py` (5 files, no banned imports); `python -m py_compile` for four maintenance scripts; relative Markdown target check (52 files, no missing targets); canonical/global `cmp` for `SKILL.md` and `interfaces.md`; targeted and full `scripts/flake.bash --ci`; `scripts/test.bash` (expected no-tests success); `scripts/sync-env.bash --check`; `scripts/sync-readme.bash --check`; `git diff --check`. All passed after regenerating the canonical index before the final install.
- Artifacts: `.agents/skills/heaven-style/references/rules/project/interfaces.md`; skill version `0.1.1.9`; generated `references/index.yaml`; daily progress note.
- Follow-up: Validate the rule against the next real service-package implementation and tighten only where repeated evidence warrants it.
