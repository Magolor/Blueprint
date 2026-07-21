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
- Task: one active `docs/tasks.yaml` ID
- Links: issues, reports, or resources

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

## Checkpoints

- YYYY-MM-DD: short evidence checkpoint; keep queue state in `docs/tasks.yaml`.

## Closeout

- Verification:
- Follow-up:
```

## Update Rules

- Keep status and checkboxes current while work proceeds.
- Every `Planned`, `In progress`, or `Blocked` plan must be linked by exactly one active queue task.
- Append dated evidence checkpoints rather than replacing history.
- Add exact verification commands, preferably repo wrappers with `rtk`.
- Close with `Done` or `Superseded`, append the development log, and remove the task from the live queue. A blocked plan remains linked to one `blocked` task with an explicit unblock condition.
