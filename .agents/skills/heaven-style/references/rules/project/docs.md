---
id: docs
title: Documentation and task lifecycle
enabled: true
blocking: true
order: 440
category: project
keywords: [README, user docs, engineering docs, authored docs, authority map, decision history, ADR, reference snapshot, YAML frontmatter, controlled technical English, ASD-STE100, task queue, dev log, scratch, generated docs, doc sync, cleanup, legacy docs, architecture status, translation]
description: Use when creating, restructuring, reviewing, or syncing authored documentation, or when work changes public behavior, architecture, task state, generated artifacts, examples, documentation authority, or temporary notes.
---

# Documentation and task lifecycle

## Core rule

Documentation is part of the maintained system, but prose is not automatically runtime truth. Each repository declares one concise authority map, one canonical surface for users, one engineering entry point, one active task queue, one development-log surface, and one temporary-note policy. Every durable fact has one normative home; other artifacts link to it.

Code, tests, generated artifacts, packaging, and release configuration describe shipped behavior. User and engineering docs describe intended and explained behavior. When they disagree, identify the owner and reconcile the mismatch; never present an accepted plan as shipped merely because it is well documented.

## Default four-surface model

Repository policy may choose different paths, but it must name equivalent owners:

| Surface | Default owner | Content | Lifecycle |
| --- | --- | --- | --- |
| User | Canonical English README or docs-site source | Installed behavior, setup, supported public APIs, examples, migration | Update in the same change that ships or removes the behavior; regenerate owned copies. |
| Engineering | `docs/README.md` and linked architecture/reference material | Current mental model, ownership, invariants, decisions, operational reference | Keep current and source-backed; label current, target, gap, and non-goal. |
| Development log | One rolling file or immutable dated entries behind one routing index | Concise change, verification, decision, blocker, handoff, next active task | Add one entry on substantial closeout or handoff; do not store durable truth, duplicate chronology, or a second queue. |
| Scratch | Expiring tracked notes plus an ignored local area | Rough requirements, brainstorms, comparisons, disposable discussion | Promote or delete by expiry. Local slop is never authoritative or committed. |

Keep user-facing explanation out of internal design notes, and keep internal task state, provider details, review evidence, and speculative plans out of user docs.

## Authority maps, decisions, and external evidence

Make the engineering entry point an authority map. It names the canonical user docs, engineering mental model, decision owner when the repository uses one, task queue, development log, scratch policy, generated surfaces, and deeper references. It links to those owners instead of copying volatile status, inventories, or chronology.

When a repository records architecture or project decisions, its policy owns the paths, states, metadata, and templates. Keep effective decisions navigable separately from pending, rejected, postponed, or superseded history when those states exist. Reserve prerequisite relationships for normative dependencies. Keep refinement, supersession, coordination, and historical evidence semantically distinct so a later clarification does not create a false build or approval order. Update a record and its routing index together when the repository declares that projection.

When an external repository, package, document, or mutable page materially guides a decision or review, record a stable locator, the exact consumed snapshot, its valid use, and its authority limit in repository-owned evidence. Use a commit, release, inspected URL and date, or content digest as appropriate. A reference checkout or mutable label such as `latest` does not prove a durable claim. The checkout itself must not become a build, test, or runtime dependency; product adoption uses a supported artifact or protocol through normal dependency policy.

## Authored-document standard

Apply this section to human-facing Markdown or MDX. The repository's `AGENTS.md`, parser, documentation platform, established page schema, and generated-file owner take precedence. This section does not replace format-specific contracts for an ADR, postmortem, changelog, API reference, generated catalog, task, plan, or development log.

Do not retrofit an existing corpus solely to make every file use one skeleton. Heaven Style does not define universal document kinds, package templates, fixed section names, locale paths, website manifests, translation sidecars, content hashes, word budgets, or CI commands. Add those only when the target repository owns and consumes them.

Discuss and obtain approval before introducing a repository-wide metadata schema, document taxonomy or template set, mass migration or hierarchy move, canonical-language or pair-layout change, mandatory same-pass translation policy, checksum/sidecar/CI regime, or broader API-doc, docstring, or inline-comment coverage. A focused page edit may follow an already approved owner without reopening that decision.

For a new or substantially reworked page:

- Identify the primary reader, their starting state, the outcome they need, the likely failure and recovery path, and the next useful level of detail.
- Follow the repository's YAML frontmatter schema. An authored bilingual page must have YAML frontmatter unless its format owner explicitly forbids it. When no schema exists, use a concise `description` that states what the page covers and when to read it; treat this as a page-level fallback, not a new corpus schema. Keep keys stable and do not copy volatile inventories into metadata.
- Give the subject a clear title and a brief entry paragraph. Add a linked contents section only when page length or lookup behavior justifies it.
- Progress from user outcome and shortest safe path to advanced operation and then concept-level developer detail. Explain ownership, lifecycle, failure, security, and performance only to the depth the target reader needs; link authoritative code, types, schemas, or generated catalogs for exact inventories.
- Open a dense section with a short orientation before tables, code, or lower-level headings. Keep one obvious next action and make success, limitations, and recovery discoverable.
- Keep current behavior, accepted target, known gap, migration guidance, history, and non-goal in their declared owners and label them accurately. Do not erase compatibility or migration facts merely to make prose read as current-state-only.

### Controlled technical English

Use a non-certified, ASD-STE100-inspired editorial pass for authored English prose. This is a clarity discipline; it does not claim standards compliance or impose a controlled dictionary.

- Name the actor and action when ambiguity can change behavior. Prefer active voice when the actor matters.
- Use one stable term for each concept. Prefer direct verbs over nominalizations, vague phrasal verbs, and rotating synonyms.
- Use logical quotation punctuation: place periods and commas outside closing quotation marks unless they are part of the quoted material, while otherwise following American English conventions.
- Put one instruction in each sentence. Use a list for several steps or conditions, split long clause chains, and keep each paragraph on one topic.
- Remove unsupported quality adjectives and stacked hedges. Preserve every `must`, `may`, `never`, condition, exception, number, timing constraint, and degree of uncertainty.
- Keep a longer sentence when splitting it would hide a relationship or reduce precision. Professional technical prose must remain natural, respectful, and exact rather than mechanically short.

This page-level prose standard does not expand which code symbols or internal lines require documentation. TypeScript TSDoc/JSDoc, Python docstrings, and inline comments retain their own language and repository rules.

Session responses, durable reports, commit and pull-request titles, pull-request descriptions, and review comments use [Communicate the result](../../workflows/work-types.md#communicate-the-result). These communication surfaces do not become new documentation or task authorities.

### Evidence for claims

Map each material claim to its strongest owner. Use public types and package metadata for interface facts, runtime code for behavior, tests for exercised paths, generated artifacts for exhaustive inventories, and accepted decisions for rationale.

Execute new or changed commands, configuration examples, and other operational paths exactly as documented when doing so is safe and the required environment is available. If exact execution is unavailable, state what remains unverified and name the evidence or owner needed to verify it. Verification depth is proportional to risk; do not turn every prose edit into an unrelated integration exercise.

## One task authority

- The repository declares exactly one writable active task queue. A repository file, GitHub, or Linear may own it; snapshots and links are read-only mirrors.
- Read the queue before creating work. A direct request that will finish in one session may stay unqueued; resumable, multi-slice, blocked, or independently delegated work must enter the queue.
- Queue items own identity, priority, status, owner, acceptance, dependencies, and links. Detailed slice checklists belong in one subordinate plan when needed.
- Chat, plans, reports, goals, TODO files, the development log, PR descriptions, and subagent notes must not become parallel task lists.
- Claim work explicitly. A blocked task states the blocker and observable unblock condition. Delegated work remains under the parent task unless it needs independent resumption; a durable delegated task points to its parent instead of duplicating child lists.
- Closed or cancelled work leaves the live queue after acceptance evidence is recorded. Git history, the development log, the issue/PR, and a closed plan preserve history.

## Update triggers

| Change | Required documentation action |
| --- | --- |
| Public behavior, install, configuration, CLI, API, or supported workflow | Update canonical user docs and executable examples; regenerate copies. |
| Architecture, ownership, dependency direction, persistence, lifecycle, extension seam, or compatibility | Update the engineering mental model/ADR and distinguish current implementation from accepted target and remaining gap. |
| Multi-session or delegated work | Create or update one queue task; add one linked plan only when ordered detail is needed. |
| Generated schema, inventory, capability, benchmark, API, or README | Run the owner generator and its `--check`/freshness gate. Unexpected probe errors must not silently become ordinary “unknown” values. |
| Substantial implementation, review, release, decision, blocker, or handoff | Append one concise development-log entry with task, change, verification, and next task or `none`. |
| Temporary requirement, brainstorm, comparison, or unaccepted design | Keep it in the declared scratch lane with owner and expiry, or in ignored local scratch when no handoff is required. |
| Canonical source changes while translations exist | Mark translation staleness and route translation separately; do not mix incidental translation into ordinary source sync. |

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
- Task queue: schema, unique IDs, state-dependent fields, dependency-cycle, and link validation.
- Development log: one declared surface and deterministic newest-entry rule. A rolling file keeps one explicit order. Separate immutable entries use stable chronological coordinates and one routing rule. If an index lists entries, it is authoritative or generated from them rather than a second manual chronology. When the repository records `Next`, its newest value refers to the active queue or `none`; older entries preserve historical task IDs.
- Scratch: ignored local lane plus tracked-note owner/created/expiry validation.
- Local docs: relative-link and retired-path checks.
- Architecture “must” rules: a focused behavioral test, import/dependency check, generated inventory, or explicit human review owner.
- Current/target claims: source/test evidence and a status audit; a diagram alone is not proof.

Every new validator needs a valid fixture and an invalid fixture that proves the real top-level gate can fail. Prefer focused behavior checks over a large repository-shaped topology scanner.

## Completion gate

Before declaring docs-impacting work complete:

- [ ] The canonical task source is current; closed work is removed.
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
- User docs that expose internal architecture churn instead of supported behavior.
- Architecture pages that describe planned behavior in present tense.
- Permanent dated progress trees without a declared log owner, stable ordering, routing rule, or retention reason; use a rolling file when separate entries add no value.
- Keeping stale reviews because deletion feels destructive; Git already preserves them.
- Hand-editing generated files.
- Mandatory docs artifacts for trivial one-pass work.

## Related rules

Also apply [test.md](test.md) when examples or architecture claims need executable evidence, [review.md](review.md) for completion reporting, [Python docstrings](../code/python/docstring.md) or [TypeScript API documentation](../code/typescript/docs.md) for API-comment surfaces, and [../../tasks/doc-sync.md](../../tasks/doc-sync.md) for user/docs-site synchronization.
