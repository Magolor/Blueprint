# Plans

Use this folder for active multi-slice work that needs ordered execution or handoff.

Do not create a plan for a one-pass edit. Each active plan belongs to exactly one live queue task.

## File name

Use this form:

```text
docs/plans/YYYY-MM-DD-<topic>.md
```

## Required shape

Use the [detailed plan template](../../.agents/skills/heaven-style/assets/templates/plan.md) with Blueprint's existing fields: Status, Created, Scope, Task, and Links. Keep one live task owner. Start with a summary, then state the problem, success criteria, non-goals, slices, checkpoints, and closeout evidence; the template's equivalent headings may group these facts. For an architectural idea, use the [design template](../../.agents/skills/heaven-style/assets/templates/design.md) and link it from the execution plan.

## Rules

Use `Planned`, `In progress`, `Blocked`, `Done`, or `Superseded` for Status.

- Keep status and acceptance checks current.
- Add exact verification commands.
- Link each active plan from one queue task.
- Keep blocked plans linked to a blocked task.
- Close the plan before you remove its queue task.
- Delete obsolete execution detail after you promote durable truth.
