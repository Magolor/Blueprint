---
id: docs
title: Documentation and task lifecycle
enabled: true
blocking: true
order: 120
category: project
keywords: [README, user docs, engineering docs, task queue, dev log, scratch, generated docs, doc sync, cleanup, legacy docs, architecture status, translation]
description: Use when work changes public behavior, architecture, active tasks, handoff state, generated artifacts, examples, documentation authority, or temporary notes.
---

# Documentation and task lifecycle

## Core rule

Documentation is part of the maintained system, but prose is not automatically runtime truth. Each repository declares one canonical surface for users, one engineering entry point, one development log, and one temporary-note policy. Each operational repository also declares exactly one active task authority. A repository whose product is a project template may carry an inert queue starter for generated projects, but the template source itself must not claim live project tasks. Every durable fact has one normative home; other artifacts link to it.

Code, tests, generated artifacts, packaging, and release configuration describe shipped behavior. User and engineering docs describe intended and explained behavior. When they disagree, identify the owner and reconcile the mismatch; never present an accepted plan as shipped merely because it is well documented.

## Default four-surface model

Repository policy may choose different paths, but it must name equivalent owners:

| Surface | Default owner | Content | Lifecycle |
| --- | --- | --- | --- |
| User | Canonical English README or docs-site source | Installed behavior, setup, supported public APIs, examples, migration | Update in the same change that ships or removes the behavior; regenerate owned copies. |
| Engineering | `docs/README.md` and linked architecture/reference material | Current mental model, ownership, invariants, decisions, operational reference | Keep current and source-backed; label current, target, gap, and non-goal. |
| Development log | One rolling repository log | Concise change, verification, decision, blocker, handoff, next active task | Append on substantial closeout or handoff; do not store durable truth or a second queue. |
| Scratch | Expiring tracked notes plus an ignored local area | Rough requirements, brainstorms, comparisons, disposable discussion | Promote or delete by expiry. Local slop is never authoritative or committed. |

Keep user-facing explanation out of internal design notes, and keep internal task state, provider details, review evidence, and speculative plans out of user docs.

## Task authority by repository role

- An operational repository declares exactly one writable active task authority. A repository file, GitHub, or Linear may own it; snapshots and links are read-only mirrors.
- A template-source repository declares that role explicitly, carries no live consumer tasks, and keeps any queue example or starter empty and visibly inert. Template maintenance may use direct requests or one declared external tracker without manufacturing a repository queue.
- Read the declared authority before creating operational work. A direct request that will finish in one session may stay unqueued; resumable, multi-slice, blocked, or independently delegated work must enter the operational repository's authority.
- Queue items own identity, priority, status, owner, acceptance, dependencies, and links. Detailed slice checklists belong in one subordinate plan when needed.
- Chat, plans, reports, goals, TODO files, the development log, PR descriptions, and subagent notes must not become parallel task lists.
- Claim work explicitly. A blocked task states the blocker and observable unblock condition. Delegated work remains under the parent task unless it needs independent resumption; a durable delegated task points to its parent instead of duplicating child lists.
- Closed or cancelled work leaves the live queue after acceptance evidence is recorded. Git history, the development log, the issue/PR, and a closed plan preserve history.

## Update triggers

| Change | Required documentation action |
| --- | --- |
| Public behavior, install, configuration, CLI, API, or supported workflow | Update canonical user docs and executable examples; regenerate copies. |
| Architecture, ownership, dependency direction, persistence, lifecycle, extension seam, or compatibility | Update the engineering mental model/ADR and distinguish current implementation from accepted target and remaining gap. |
| Multi-session or delegated operational work | Create or update one task in the declared authority; add one linked plan only when ordered detail is needed. Template-source maintenance uses its declared external authority or direct-request evidence instead of activating the consumer starter. |
| Generated schema, inventory, capability, benchmark, API, or README | Run the owner generator and its `--check`/freshness gate. Unexpected probe errors must not silently become ordinary “unknown” values. |
| Substantial implementation, review, release, decision, blocker, or handoff | Append one concise development-log entry with task, change, verification, and next task or `none`. |
| Temporary requirement, brainstorm, comparison, or unaccepted design | Keep it in the declared scratch lane with owner and expiry, or in ignored local scratch when no handoff is required. |
| English source changes while translations exist | Mark translation staleness and route translation separately; do not mix incidental translation into ordinary English sync. |

Small internal edits do not require ceremonial documents. They still update existing docs when their claims become false.

## Cleanup triggers

Clean documentation when any of these becomes true:

- a plan is done, superseded, or no longer owned;
- a review/report's recommendations were actioned or its status/path claims became historical;
- a current-only documentation set contains dated evidence that no longer describes current state;
- two pages state the same rule or one page contradicts the canonical owner;
- a temporary note expires or a discussion becomes an accepted decision;
- a generated artifact no longer has a generator or freshness check;
- a task closed but remains in a queue, goal, plan, log `Next`, or TODO list;
- navigation points to removed, renamed, or superseded content.

Cleanup means:

1. Promote the surviving current fact into its normative user/engineering/code/test owner.
2. Update task, plan, decision, report, and development-log state.
3. Remove closed queue rows and delete or clearly supersede contradictory legacy pages.
4. Delete expired scratch and orphan generated output.
5. Refresh navigation, local links, generated projections, and translations state.

Use Git history for old execution chatter. Keep historical reports only when the repository explicitly needs an audit trail; label status and staleness so they cannot masquerade as current truth.

## Enforcement owners

Strong documentation promises need a named fitness function:

- Generated copies: deterministic generator plus exact `--check` comparison. Check mode is read-only, network-free, and does not initialize application/runtime state.
- Cross-repository or persisted projections: a source revision or content digest, explicit non-authoritative status, and a synchronization checkpoint.
- Operational task authority: schema, unique IDs, state-dependent fields, dependency-cycle, and link validation when repository-owned; equivalent integrity checks when externally owned.
- Template queue starter: deterministic empty content, an instantiation path, and a validator that rejects live template-source tasks.
- Development log: one declared path, newest-first ordering, and the newest `Next` reference to the active authority or `none`; a template source without live task authority requires `none`. Older entries preserve historical task IDs.
- Scratch: ignored local lane plus tracked-note owner/created/expiry validation.
- Local docs: relative-link and retired-path checks.
- Architecture “must” rules: a focused behavioral test, import/dependency check, generated inventory, or explicit human review owner.
- Current/target claims: source/test evidence and a status audit; a diagram alone is not proof.

Every new validator needs a valid fixture and an invalid fixture that proves the real top-level gate can fail. Prefer focused behavior checks over a large repository-shaped topology scanner.

## Completion gate

Before declaring docs-impacting work complete:

- [ ] The operational task authority is current and closed work is removed, or the template source has no live queue and its starter remains inert.
- [ ] User docs match shipped public behavior.
- [ ] Engineering docs distinguish current, target, gap, and non-goal.
- [ ] Stable conclusions were promoted from plans, reports, logs, and scratch.
- [ ] The development log records substantial closeout/handoff evidence.
- [ ] Scratch is unexpired or removed.
- [ ] Generated artifacts and README copies pass freshness checks.
- [ ] Local links, navigation, translation state, and repository docs validation pass.

## Avoid

- More workflow prose without an enforcement owner.
- A second task list hidden in goals, plans, progress notes, PR descriptions, or chat.
- Live product tasks stored in the source repository of a reusable project template.
- User docs that expose internal architecture churn instead of supported behavior.
- Architecture pages that describe planned behavior in present tense.
- Permanent dated progress trees when one rolling log and Git history are sufficient.
- Keeping stale reviews because deletion feels destructive; Git already preserves them.
- Hand-editing generated files.
- Mandatory docs artifacts for trivial one-pass work.

## Related rules

Also apply [test.md](test.md) when examples or architecture claims need executable evidence, [review.md](review.md) for completion reporting, [Python docstrings](../code/python/docstring.md) or [TypeScript API documentation](../code/typescript/docs.md) for API-comment surfaces, and [../../tasks/doc-sync.md](../../tasks/doc-sync.md) for user/docs-site synchronization.
