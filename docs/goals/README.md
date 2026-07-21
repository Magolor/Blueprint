# Goals

Use this folder for project goals that guide implementation.

Goals describe outcomes and ordering pressure. They are not plans, issue trackers, or daily status logs.

Recommended files after project initialization:

- `long-term.md`: product or platform destination.
- `mid-term.md`: milestone-level outcomes.
- `short-term.md`: current implementation slices.

Keep goals objective enough for agents to turn them into acceptance criteria. Link each active short-term goal to the owning plan, issue, or report when one exists.

## Update Rules

- Update goals when shipped behavior, roadmap priority, or a durable report changes what the project is trying to accomplish.
- Mark completed short-term goals with a completion date, then summarize the change in `docs/DEVLOG.md`.
- Keep speculative ideas out of goals unless they are explicit non-goals or accepted future direction.
- Do not duplicate plan checklists here; link to `docs/plans/` instead.
- Do not store task status here; active work belongs only in `docs/tasks.yaml`.
