# Engineering Guide

This is the single entry point for engineers, agents, and architects. It explains where each kind of truth lives, how work enters the repository, and when temporary or historical material must be removed.

## Four Documentation Surfaces

| Surface | Canonical home | Audience | Lifecycle |
| --- | --- | --- | --- |
| User documentation | `README.en.md` | Users and evaluators | Update when shipped behavior, setup, or supported usage changes. `README.md` and package copies are generated from it. |
| Engineering documentation | `docs/README.md` plus the durable folders below | Engineers, agents, and architects | Keep current and source-backed. Planned behavior must be labeled; stable conclusions have one normative home. |
| Development log | [`docs/DEVLOG.md`](DEVLOG.md) | Future maintainers and agents resuming work | Record concise change, verification, and handoff evidence. Keep at most 50 entries; Git preserves older detail. |
| Scratch | [`docs/scratch/`](scratch/README.md) and ignored `.temp/notes/` | Short-lived requirements, brainstorms, and rough analysis | Tracked notes expire within 45 days and must be promoted or deleted. Pure local slop stays under `.temp/notes/`. |

The canonical active task source is [`docs/tasks.yaml`](tasks.yaml). GitHub, Linear, plans, reports, chat, and the development log may link to tasks, but must not become parallel writable queues.

## Engineering Areas

| Area | Purpose |
| --- | --- |
| [Goals](goals/README.md) | Durable product or platform outcomes. Never store task state here. |
| [Plans](plans/README.md) | Detailed execution for a queued multi-slice task. A plan is subordinate to exactly one queue item while active. |
| [Resources](resources/README.md) | Stable architecture, specifications, inventories, and source-of-truth notes. |
| [Reports](reports/README.md) | Evidence snapshots for reviews, refactors, and surveys. Actionable follow-up becomes a queue task. |

## Authority Order

When sources disagree, resolve them in this order:

1. User instructions and repository policy.
2. Shipped code, tests, generated artifacts, packaging, and release configuration.
3. Canonical user documentation.
4. Stable engineering resources.
5. Current goals and accepted plans.
6. Reports, the development log, and scratch notes.

Architecture documents must distinguish **current**, **target**, **gap**, and **non-goal**. An accepted design is not shipped behavior until code and behavioral evidence prove it.

## Agent Work Loop

1. Run `rtk uv run python scripts/docs.py tasks --ready` and read the first relevant task before proposing new work.
2. If the user's request is meant for later, spans sessions, or needs delegation, add one queue item before implementation. A one-session direct request may stay out of the queue only if it is completed in that session.
3. Claim queued work by setting `status: active`, `owner`, and `updated`. A blocked task records both `blocker` and an observable `unblock_when`. Keep detailed slice checklists in one linked plan only when the plan trigger applies.
4. Delegate beneath the owning task; subagents do not create parallel task lists. Durable child work becomes another queue item with `parent` pointing to the owning task and `depends_on` describing execution order only when it must be resumed independently.
5. Update user docs for shipped user-visible behavior and engineering docs for durable architecture or workflow changes.
6. Close work by verifying acceptance criteria, appending one development-log entry, promoting durable conclusions, deleting or promoting scratch notes, and removing the completed task from the live queue.
7. Run `rtk uv run python scripts/docs.py check`. The queue and docs checks are also enforced by hooks and CI.

## Cleanup Rules

- Completed or cancelled work leaves `docs/tasks.yaml`; Git and the development log preserve the history.
- A finished plan becomes `Done` or `Superseded`. Do not leave silent `Planned` or `In progress` files.
- A report is an evidence snapshot. Promote accepted conclusions to resources, code, tests, or user docs; mark the report `Actioned` or `Superseded` when its action is complete.
- The newest development-log entry's `Next` names an active task ID or `none`; historical entries may retain IDs that have since left the live queue.
- Tracked scratch notes require `status`, `created`, `expires`, and `task` frontmatter. Expired notes fail validation.
- `.temp/notes/` is disposable, ignored, and never authoritative. `scripts/cleanup.bash` removes it.
- Delete stale navigation and contradictory legacy docs in the same change that promotes their surviving truth.

## Enforcement

```bash
rtk uv run python scripts/docs.py tasks --ready
rtk uv run python scripts/docs.py check
rtk bash scripts/test.bash tests/test_docs_contract.py -q
```

The checker validates the four surfaces, queue schema and dependencies, development-log ordering, scratch expiry, retired progress directories, task links, and repository-local Markdown links.
