# Docs Governance Plan

- Status: Done
- Created: 2026-06-27
- Scope: Make Blueprint's docs directory operationally maintainable for future agents by defining artifact locations, update triggers, and closeout rules.
- Links: `AGENTS.md`, `docs/README.md`, `docs/progress/README.md`

## Problem

Blueprint had a clean but underspecified docs split. Agents could see `goals/`, `resources/`, and `progress/`, but the repo did not clearly say when to create plans, how to keep progress append-only, or where durable review, refactor, and survey reports should live.

## Success Criteria

- [x] `docs/README.md` acts as a docs authority map and artifact router.
- [x] `AGENTS.md` tells future agents when to update plans, progress, resources, reports, and generated docs.
- [x] `docs/progress/` defines append-only daily note rules.
- [x] `docs/plans/` defines plan lifecycle and progress tracking.
- [x] `docs/reports/` defines review, refactor, and survey report locations.
- [x] README copies are synced from `README.en.md`.
- [x] Docs and skill edits pass lightweight verification.

## Non-Goals

- Do not create a full documentation site.
- Do not translate `README.zh.md` during this English docs governance update.
- Do not add project-specific roadmap content beyond the docs governance work itself.

## Slices

### Slice 1: Establish the Docs Taxonomy

- Goal: Define the durable artifact families and their update triggers.
- Touch: `AGENTS.md`, `docs/README.md`, folder-level docs READMEs.
- Acceptance: Future agents can choose where a plan, progress note, report, resource, or goal update belongs.
- Verification: Review changed markdown for conflicting path guidance.
- Docs: This plan and today's progress note.

### Slice 2: Align Generated and Agent-Facing Guidance

- Goal: Keep README copies and repo-local skill references consistent with the new taxonomy.
- Touch: `README.en.md`, generated README copies, `.agents/skills/heaven-style/`.
- Acceptance: Durable review guidance uses `docs/reports/reviews/` and README layout lists the new docs folders.
- Verification: `rtk bash scripts/sync-readme.bash --check`; heaven-style scan when available.
- Docs: Update this plan closeout and daily progress.

## Progress

- 2026-06-27: Inspected current docs layout, AGENTS guidance, README source, and heaven-style docs/review rules. Began taxonomy and lifecycle updates.
- 2026-06-27: Synced README copies, aligned repo-local heaven-style review guidance, refreshed the repo-local skill index, and ran verification.

## Closeout

- Verification:
  - `rtk bash scripts/sync-readme.bash`
  - `rtk bash scripts/sync-readme.bash --check`
  - `rtk uv run python .agents/skills/heaven-style/scripts/install.py --in-place --skip-sync`
  - `rtk uv run python .agents/skills/heaven-style/scripts/scan.py AGENTS.md docs README.en.md README.md src/blueprint/resources/README.md .agents/skills/heaven-style/SKILL.md .agents/skills/heaven-style/references/tasks/code-review.md .agents/skills/heaven-style/references/workflows/architect.md`
  - `rtk proxy git diff --check`
  - `rtk bash scripts/flake.bash --ci`
- Follow-up:
  - `README.zh.md` is stale relative to the English README docs-layout update and should be refreshed through the translation workflow.
  - Standard global skill install was retried later with `rtk uv run python .agents/skills/heaven-style/scripts/install.py` and completed successfully at `C:\Users\magol\.agents\skills\heaven-style`.
