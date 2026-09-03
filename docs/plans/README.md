# Plans

Use this folder for active multi-slice work that needs ordered execution or handoff.

Do not create a plan for a one-pass edit. Each active plan belongs to exactly one live queue task.

## File name

Use this form:

```text
docs/plans/YYYY-MM-DD-<topic>.md
```

## Required shape

```markdown
# <Topic> Plan

- Status: Planned | In progress | Blocked | Done | Superseded
- Created: YYYY-MM-DD
- Scope: one or two sentences
- Task: one live task ID
- Links: relevant issues, reports, or resources

## Problem

## Success criteria

- [ ] Observable outcome.

## Non-goals

## Slices

### Slice 1: <short title>

- Goal:
- Touch:
- Acceptance:
- Verification:
- Docs:

## Checkpoints

## Closeout

- Verification:
- Follow-up:
```

## Rules

- Keep status and acceptance checks current.
- Add exact verification commands.
- Link each active plan from one queue task.
- Keep blocked plans linked to a blocked task.
- Close the plan before you remove its queue task.
- Delete obsolete execution detail after you promote durable truth.
