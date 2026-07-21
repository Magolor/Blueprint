# Engineering Guide

This is the single entry point for engineers, agents, and architects. It explains where each kind of truth lives, how work enters the repository, and when temporary or historical material must be removed.

## Four Documentation Surfaces

| Surface | Canonical home | Audience | Lifecycle |
| --- | --- | --- | --- |
| User documentation | `README.en.md` | Users and evaluators | Update when shipped behavior, setup, or supported usage changes. `README.md` and package copies are generated from it. |
| Engineering documentation | `docs/README.md` plus the durable folders below | Engineers, agents, and architects | Keep current and source-backed. Planned behavior must be labeled; stable conclusions have one normative home. |
| Development log | [`docs/DEVLOG.md`](DEVLOG.md) | Future maintainers and agents resuming work | Record concise change, verification, and handoff evidence. Keep at most 50 entries; Git preserves older detail. |
| Scratch | [`docs/scratch/`](scratch/README.md) and ignored `.temp/notes/` | Short-lived requirements, brainstorms, and rough analysis | Tracked notes expire within 45 days and must be promoted or deleted. Pure local slop stays under `.temp/notes/`. |

Repository role is explicit.

<!-- blueprint-template-only:start -->
While `.blueprint-template.yaml` exists, `docs/tasks.template.yaml` is an inert, empty downstream starter and template maintenance stays attached to the direct request or an explicitly selected external issue. `scripts/rename.bash` removes template mode and promotes the starter.
<!-- blueprint-template-only:end -->

In operational mode, `docs/tasks.yaml` is the project's single writable task authority.

## Engineering Areas

| Area | Purpose |
| --- | --- |
| [Goals](goals/README.md) | Durable product or platform outcomes. Never store task state here. |
| [Plans](plans/README.md) | Detailed execution for multi-slice work, subordinate to the repository's declared operational task or template-maintenance reference. |
| [Resources](resources/README.md) | Stable architecture, specifications, inventories, and source-of-truth notes. |
| [Reports](reports/README.md) | Evidence snapshots for reviews, refactors, and surveys. Actionable follow-up enters the repository's declared authority. |

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

<!-- blueprint-template-only:start -->
In template mode, keep maintenance attached to the direct request or one explicitly selected GitHub/Linear issue and do not create `docs/tasks.yaml`. Close template work with `Next: none`, promote durable conclusions, and delete or promote scratch notes. To instantiate a concrete project, run `scripts/rename.bash`; it promotes the empty starter to that project's canonical queue.
<!-- blueprint-template-only:end -->

1. In an operational project, read and claim the existing task before creating another. A blocked task records both `blocker` and an observable `unblock_when`; one linked plan may hold ordered execution detail.
2. Delegate beneath the owning request or task; subagents do not create parallel task lists.
3. Update user docs for shipped user-visible behavior and engineering docs for durable architecture or workflow changes.
4. Close operational work by removing completed rows from the live queue after acceptance evidence, promoting durable conclusions, and deleting or promoting scratch notes.
5. Run `rtk uv run python scripts/docs.py check`. Hooks and CI enforce the role-aware docs contract.

## Cleanup Rules

<!-- blueprint-template-only:start -->
- Template mode never owns `docs/tasks.yaml`; its empty starter stays inert.
<!-- blueprint-template-only:end -->
- In operational mode, completed or cancelled work leaves the live task authority and Git plus the development log preserve history.
- A finished plan becomes `Done` or `Superseded`. Do not leave silent `Planned` or `In progress` files.
- A report is an evidence snapshot. Promote accepted conclusions to resources, code, tests, or user docs; mark the report `Actioned` or `Superseded` when its action is complete.
<!-- blueprint-template-only:start -->
- A template-mode development-log entry uses `Next: none`.
<!-- blueprint-template-only:end -->
- In operational mode, `Next` may name an active task ID or `none`; historical entries may retain IDs that have since closed.
- Tracked scratch notes require `status`, `created`, `expires`, and `task` frontmatter. Expired notes fail validation.
- `.temp/notes/` is disposable, ignored, and never authoritative. `scripts/cleanup.bash` removes it.
- Delete stale navigation and contradictory legacy docs in the same change that promotes their surviving truth.

## Enforcement

```bash
rtk uv run python scripts/docs.py check
rtk bash scripts/test.bash tests/test_docs_contract.py -q
```

<!-- blueprint-template-only:start -->
The checker rejects a live queue in template mode and validates the empty starter.
<!-- blueprint-template-only:end -->
In operational mode it requires the live queue and validates its schema, dependencies, development-log handoff, scratch expiry, retired paths, task links, and repository-local Markdown links.
