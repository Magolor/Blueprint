---
id: workflow-design-plan
title: Refactor and execution plans
description: Read for refactor and execution plans.
---

# Refactor and execution plans

## Summary

Start with a short plan that a maintainer can judge. Expand confirmed scope
into execution steps that another engineer or agent can follow. Keep the
entry file short and link details by component or independently owned slice.

## Plan brief

Before a major design or implementation assignment, write or update one brief
at the repository’s plan owner. Use controlled technical English. Include:

1. A short summary of the user outcome and proposed change.
2. Scope, non-goals, and the important constraint or tradeoff.
3. Observable acceptance criteria and the verification approach.
4. Links to requirements, accepted contracts, evidence, and any
   [component protocol](module.md#component-protocol).
5. The decision needed and the next execution slice.

Keep proposed and confirmed work distinct. Existing user instructions or an
accepted decision can supply confirmation; do not add another approval round
for settled scope. Do not expand an unresolved design into an implementation
mandate. After confirmation, retain the brief as the entry and elaborate the
accepted parts. Record remaining decisions with their owners.

## Detail layout

Keep a small execution plan in the same file below the brief. If independent
slices make it hard to navigate, use one folder with a short index and numbered
component plans. Link each child by purpose and dependency. Do not create a
file for every minor step or copy the queue into the index.

Each child needs its own short summary, acceptance, references, inputs, work,
and handoff output. The parent links shared contracts instead of repeating
them in every child. Use [file-based handoff](../dispatch.md) for assignments.

## Refactor plan output

For cross-module refactors, produce a plan doc with:

1. **Trigger** — mismatch, tech debt, or goal that forces the change.
2. **Invariant checklist** — mental-model rules that must still hold after the refactor.
3. **Before / after map** — modules, public imports, registry ownership.
4. **Slice breakdown** — each slice is independently reviewable and verifiable:

```markdown
### Slice N: <short title>

**Goal:** one sentence.

**Touch:** paths/modules (bullet list).

**Steps:**
1. Concrete action an agent or human can execute.
2. ...

**Acceptance criteria:**
- [ ] Observable outcome.

**Verification:**
- `rtk <target-repo focused test command>`
- `rtk <target-repo static/format/type gate>`

**Docs:** files to update in the same slice or explicitly deferred.

**Non-goals:** what this slice must not do.
```

5. **Migration sweep** — ordered delete/rename steps for owned callers; policy-required external compatibility has a named consumer, test, owner, and removal condition.
6. **Rollback posture** — git revert boundaries per slice, not big-bang undeployable plans.

Hand implementation slices to [code](../../tasks/code.md) and rule-heavy execution to [developer](../developer.md).

## Step-by-step execution plan

The final architect artifact for major work is an **execution plan** that average engineers and LLM agents can follow. Requirements:

1. **Numbered steps** — each step is one clear action; no compound steps hiding multiple file edits.
2. **Preconditions** — branch, issue link, target-repo environment install/sync command from `AGENTS.md`, and docs read list.
3. **File paths** — absolute or repo-root-relative paths for every edit target.
4. **Code shape hints** — registry call, class skeleton, or config key — not full implementations unless the step is trivial.
5. **Verification after every slice** — exact `rtk` + wrapper commands from `AGENTS.md`.
6. **Stop conditions** — unresolved decisions, newly discovered scope, or waivers that exceed existing authority. An already accepted API or schema change does not require another approval merely because it is consequential.
7. **Handoff routes** — which task playbook continues after the plan (`code`, `code-review`, `doc-sync`, `manager`).

Store durable plans under a project-approved path:

- `docs/plans/<YYYY-MM-DD>-<topic>.md` for active multi-slice execution plans in repos that maintain plan artifacts.
- `docs/resources/architecture/<topic>.md` for architecture designs.
- `docs/goals/` updates for horizon changes.
- the declared scratch lane for time-bound unaccepted designs, with owner and expiry.
- Linear issue description or a single rolling design comment when the plan is issue-owned.

Do not bury the only copy in chat history.

## Acceptance

The brief is short enough to review as one decision. Confirmed slices name
their inputs, owned files, required checks, and output evidence. Another session
can execute one slice from its linked file without reconstructing chat history.
