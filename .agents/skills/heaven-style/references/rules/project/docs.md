---
id: docs
title: Documentation and task lifecycle
blocking: true
description: Define documentation authority, lifecycle, synchronization, or validation.
---

# Documentation and task lifecycle

## Core rule

Documentation is part of the maintained system. Prose is not automatically runtime truth. Each repository declares one concise authority map, one canonical surface for users, one engineering entry point, one active task queue, one development-log surface, and one temporary-note policy. Every durable fact has one normative home. Other artifacts link to it.

Code, tests, generated artifacts, packaging, and release configuration describe shipped behavior. User and engineering docs describe intended and explained behavior. When they disagree, identify the owner. Reconcile the mismatch. Never present an accepted plan as shipped merely because it is well documented.

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

## Choose the affected surface

- Author a page: [writing](docs/write.md) and [controlled prose](docs/prose.md).
- Create, resume, or close work: [task ownership](docs/tasks.md).
- Change claims, projections, or stale pages: [sync and cleanup](docs/sync.md).
- Define or run documentation validation: [checks](docs/check.md).

Small internal edits need no ceremonial documents. Update existing claims when they become false.
