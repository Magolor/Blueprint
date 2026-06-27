# Plans

Use this folder for active or completed multi-slice plans that agents and maintainers may need to execute, resume, review, or audit.

Do not create a plan for a one-pass edit. Create one when work spans multiple sessions or PRs, changes public behavior or architecture, needs ordered acceptance criteria, or may be handed off to another agent.

## Naming

Use dated, slugged files:

```text
docs/plans/YYYY-MM-DD-<topic>.md
```

Use one plan per coherent outcome. If a plan becomes obsolete, mark it `Superseded` and link the replacement instead of deleting history.

## Required Shape

```markdown
# <Topic> Plan

- Status: Planned | In progress | Blocked | Done | Superseded
- Created: YYYY-MM-DD
- Scope: one or two sentences
- Links: issues, reports, resources, or progress notes

## Problem

## Success Criteria

- [ ] Observable outcome.

## Non-Goals

## Slices

### Slice 1: <short title>

- Goal:
- Touch:
- Acceptance:
- Verification:
- Docs:

## Progress

- YYYY-MM-DD: short checkpoint with links to daily progress.

## Closeout

- Verification:
- Follow-up:
```

## Update Rules

- Keep status and checkboxes current while work proceeds.
- Append dated progress checkpoints rather than replacing history.
- Link the daily progress note for each substantial work session.
- Add exact verification commands, preferably repo wrappers with `rtk`.
- Close with `Done`, `Superseded`, or `Blocked`; do not leave stale plans silently open.
