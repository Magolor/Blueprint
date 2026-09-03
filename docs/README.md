# Engineering Guide

This page is the engineering entry point for Blueprint.

## Documentation surfaces

| Surface | Owner | Lifecycle |
| --- | --- | --- |
| User guidance | `README.en.md` | Update it for shipped behavior. Regenerate `README.md`. |
| Engineering guidance | This page and linked folders | Keep it current and source-backed. |
| Development log | [`docs/DEVLOG.md`](DEVLOG.md) | Add concise closeout evidence. Put newest entries first. |
| Scratch | [`docs/scratch/`](scratch/README.md) | Promote or delete tracked notes within 45 days. |

[`docs/tasks.yaml`](tasks.yaml) is the only live task queue. Plans, reports, chat, issues, and the log can link to tasks. They do not replace the queue.

The queue supports these live states:

- `draft`: The task needs review.
- `ready`: The task can start.
- `active`: One named owner is working on it.
- `blocked`: An external condition prevents work.
- `postponed`: An explicit condition controls resumption.

Record completed and canceled work in the development log. Remove the terminal row in the same closeout change.

## Engineering areas

| Area | Purpose |
| --- | --- |
| [Goals](goals/README.md) | Durable outcomes and ordering pressure. |
| [Plans](plans/README.md) | Ordered execution for one live task. |
| [Resources](resources/README.md) | Stable architecture and specifications. |
| [Reports](reports/README.md) | Evidence, findings, and recommendations. |

## Authority order

1. Current user instructions and repository policy.
2. Shipped code, tests, artifacts, CI, and release configuration.
3. Canonical user guidance.
4. Stable engineering resources.
5. Current goals and accepted plans.
6. Reports, the development log, and scratch notes.

Label architecture claims as current, target, gap, or non-goal. A plan does not prove shipped behavior.

## Work loop

1. Run the repository task command.
2. Claim a matching task before you create one.
3. Add one plan only when the work needs ordered slices.
4. Change the authoritative code or document.
5. Run focused checks, then the complete gate.
6. Update canonical docs and closeout evidence.
7. Remove terminal queue rows and stale temporary material.

## Enforcement

Use the commands in `AGENTS.md`. The documentation checker validates surface presence, queue structure, plan ownership, log order, scratch expiry, and local links.
