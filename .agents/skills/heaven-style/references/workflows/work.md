---
id: workflow-work-types
title: Work type procedures
audience: all
description: Resolve work boundaries, special contracts, communication, and handoff.
---

# Work boundaries

Follow repository policy and the user's existing authorization. Discussion compares options; inspection reads evidence; design produces proposals; change modifies the authorized artifact. None independently authorizes publication, deployment, or external messages. Diagnosis alone does not authorize a fix. Parallel agents require explicit authority and stable slice ownership.

For persistent work, use one canonical task and one linked plan when ordered detail is needed. Define acceptance before edits. Verify the authoritative change, update affected docs and closeout evidence, then remove terminal task state according to repository policy.

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

Task management, docs, and test compression use their [task routes](start.md). Queue state and required fields belong to [task ownership](../rules/project/docs/tasks.md).

## Communicate the result

Lead updates with new evidence, decisions, or blockers. Final responses state outcome, changed owners, verification, residual risk or waiver, and any next action. Avoid command transcripts.

Commit/PR titles state one durable outcome under repository convention. PR descriptions explain the user reason, observable behavior, relevant scope, verification, and risk. Link canonical owners instead of duplicating them. Inline findings name one problem, evidence, impact, fix direction, and a narrow line range. Publish only with authority.

Durable reports add scope, status, comparison base, findings/decisions, gaps, and next owner. A handoff records task/plan, branch/revision/worktree, completed and next acceptance condition, last check/result, blocker or resume condition, changed owners, and risk. Chat must not be the only resume state.
