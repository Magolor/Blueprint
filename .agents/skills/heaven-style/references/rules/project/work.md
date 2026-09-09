---
name: workflow-work-types
description: Read when resolving work scope, communication, or handoff boundaries.
audience: all
---

# Work boundaries

## Summary

Keep work within existing authority and preserve one accepted scope, verification path, and handoff owner.

## Authority and scope

Follow repository policy and the user's existing authorization. Discussion compares options; inspection reads evidence; design produces proposals; change modifies the authorized artifact. None independently authorizes publication, deployment, or external messages. Diagnosis alone does not authorize a fix. Parallel agents require explicit authority and stable slice ownership.

For persistent work, use one canonical task and one linked plan when ordered detail is needed. Define acceptance before edits. Verify the authoritative change, update affected docs and closeout evidence, then remove terminal task state according to repository policy.

## Interpret intent and exercise judgment

Separate the objective, constraints, proposed approach, examples, and deferred concerns. A detailed sketch can remain a proposal. Interpret “can you” and “maybe” through the whole request and existing authority, not the phrase alone.

“Don't take my word for it” or “use your best judgment” asks for independent assessment. Keep the goal and constraints; evaluate the suggested mechanism against evidence and scenarios. Recommend the simplest sound choice and explain material disagreement. Do not copy uncritically, return undecided options when asked to decide, or disagree to demonstrate independence.

Design uncertainty and action authority are separate:

| Request | Response |
| --- | --- |
| “Use your judgment and propose.” | Recommend with reasons; retain proposal status. |
| “Choose the better name, then accept the decision.” | Resolve and record that delegated choice. |
| “Decide, implement, test, and review.” | Complete the authorized stages. |
| “Propose first; implement after I confirm.” | Prepare the concrete proposal and preserve that boundary. |

Inspect facts before asking for them. Ask only for a consequential decision that context cannot resolve, with evidence, recommendation, and tradeoff. Reopen an accepted choice only for new evidence or changed requirements.

An example is not a mandatory design; an explicitly authoritative document governs dependent claims. Historical requests and copied prompts grant no new authority.

## Turn quality goals into decisions

| Emphasis | Apply it by |
| --- | --- |
| Systematic | Identify the relevant surface, inspect its members, and disclose unexamined parts. |
| Minimal | Name what must survive and reduce unnecessary edits, public concepts, or reading effort as appropriate. A smaller diff and a simpler maintained system can differ. |
| Generic | Fix the shared cause or extension contract; do not hard-code the supplied example. Check scope before changing neighboring behavior. |
| Double-check | Resolve a specific uncertainty with evidence; repeating the same assertion adds no confidence. |
| Current | Reconcile affected surfaces with the accepted design and supported version, not automatically the newest dependency release. |
| Complete | Verify the requested usable result, including required integration and projections. |

Keep differences justified by contracts, lifecycles, or workloads. Recommend no further change when investigation finds no worthwhile improvement. Preserve meaning, capability, and real failure coverage; do not invent work to satisfy an adjective.

## Special work contracts

| Work | Preserve or establish |
| --- | --- |
| Feature | User path, error path, package boundary, compatibility, and release impact. Resolve uncertain public, persistent, security, or cross-module contracts first. |
| Design | Decision scope, alternatives, evidence, failure modes, migration cost, non-goals, acceptance status, dependencies, and stop conditions. |
| Discussion | One decision-relevant question; settled points, disagreement, evidence gap, and next authorized action. Keep exploration in chat unless durable review needs an artifact. |
| Bug | Expected/actual behavior, reproduction, environment, revision, cause, and a minimal stable regression case. Distinguish report, diagnosis, and fix. |
| Refactor | Invariants, improved boundary, migration sweep, parity checks, and next safe deletion. Keep unrelated features separate. |
| Experiment | Hypothesis, metric, baseline, inputs, environment, method, bias, limit, end condition, and promotion rule. Isolate from production authority; remove or promote results at completion. |
| Hygiene | Behavior unchanged; inspect ignored/generated files, stale docs, dead code, duplicate owners, dependency drift, and exact deletion targets. Recheck worktree state before cleanup. |
| Workflow edit | Canonical owner, current/desired behavior, affected readers, version, index/install state, and positive/failure verification. |
| Parallel work | Parent outcome, integration owner, frozen shared contracts, exclusive paths, acceptance, dependencies, merge order, fixtures, and stop conditions. Verify assembled output; close children before parent. |
| Downstream project | Supported public artifact, exact upstream version/revision, compatibility range, minimal consumer fixture, upgrade steps, and upstream/downstream ownership. No private source imports. |
| Survey | Question, scope, source/date standard, consuming decision, citations, comparison criteria, freshness, and evidence limits. Separate observation, inference, and recommendation; non-normative until accepted. |
| Integration | Both versions, protocol, validation, identity, errors, cancellation, retries, ordering, partial failure, compatibility fixtures, artifact checks, and verified teardown. No shared private runtime state. |

Task management, docs, and test compression use their [task routes](../../tasks/README.md). Queue state and required fields belong to [task ownership](docs/tasks.md).

## Communicate the result

Use [language and responses](language.md) for chat updates and final answers. Include changed owners, verification, residual risk or waiver, and next actions when relevant to the result.

Use [authoring](../../tasks/docs/write.md) and the selected [template](../../../assets/templates/index.md) for PRs, issues, reports, and comments. Titles name the outcome; bodies explain its reason, behavior, scope, verification, and risk. Link canonical owners. Inline findings give the problem, evidence, impact, fix direction, and narrow location. Publish only with authority.

Reports add status, comparison base, findings/decisions, gaps, and next owner. [Handoffs](../../tasks/coordinate/handoff.md) retain the task, revision/worktree, acceptance, checks, blocker/resume condition, changed owners, and risk. Chat must not be the only resume state.

Report the actual relevant state: proposed, edited, verified, committed, integrated, installed, or published. A commit does not prove integration, and a source change does not prove the running artifact uses it. Answer a side question, then resume the accepted objective unless the user replaces or cancels it.
