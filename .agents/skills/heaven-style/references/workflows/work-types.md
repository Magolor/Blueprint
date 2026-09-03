---
id: workflow-work-types
title: Work type procedures
enabled: true
order: 2
audience: all
keywords: [feature, design, discussion, bug, documentation, refactor, experiment, tasks, hygiene, workflow, communication, report, pull request, review comment, parallel implementation, downstream project, test compression, survey, integration]
description: Use when a person or agent needs the complete start, resume, evidence, verification, communication, and closeout procedure for a common work type.
---

# Work Type Procedures

Use this page after you select a route in [Start or Resume a Workflow](start.md).

Repository policy has priority. Use its queue, decision records, commands, and release rules.

## Use the common lifecycle

1. Read repository policy and current task state.
2. State the outcome and the permitted action.
3. Name the authority for each fact that can change.
4. Define acceptance conditions before you edit files.
5. Create one task only when the work must persist.
6. Use one plan for ordered, multi-slice work.
7. Change the smallest authoritative surface.
8. Run focused checks, then the repository closeout gate.
9. Update durable documentation and task state.
10. Report the result, evidence, residual risk, and next action.

Use one of these action levels:

- `inspect`: Read evidence. Do not change local or external state.
- `discuss`: Compare options. Do not accept a decision or change files.
- `design`: Write a proposal or decision artifact. Do not implement it.
- `change`: Modify the authorized repository or local artifact.
- `publish`: Change external state. Examples include a push, release, deployment, or message.

Publication is not the same as a local commit. Get explicit authority before publication.

## Communicate the result

Use the same verified facts on each communication surface, but adapt the detail and form:

- **Session update:** state the new fact, blocker, or decision. Do not repeat the full plan or command transcript.
- **Session completion:** lead with the outcome. Name changed authorities, verification, residual risk or waiver, and the next action when one exists.
- **Durable report file:** record scope, status, comparison base, evidence, findings or decisions, verification gaps, and the next owner. Follow the repository report path and do not create a second task queue.
- **Commit or pull-request title:** follow repository convention and state one durable outcome. Avoid generic labels, file inventories, process narration, and agent attribution.
- **Pull-request description or top-level comment:** state the user reason, observable change, important scope or non-goals, verification, and material risk or waiver. Link to canonical owners instead of copying their full content.
- **Inline review comment:** state one actionable problem, precise evidence, impact, and fix direction. Keep the line range narrow and do not publish without authority.

## Use stable task states

- `draft`: The outcome or acceptance conditions need review.
- `ready`: The task is clear and has no unresolved dependency.
- `active`: One named owner is working on the task.
- `blocked`: An external condition prevents progress. Record the unblock condition.
- `postponed`: The task is valid but intentionally deferred. Record the resume condition.
- `canceled`: The outcome is no longer wanted. Record the reason, then close the task.

Record completed and canceled work in the repository's closeout surface. Remove closed rows when policy keeps only live tasks.

## Start or resume a feature

- Start: State the user outcome, acceptance conditions, non-goals, and compatibility policy.
- Record: Link one task to a plan only when the feature has multiple ordered slices.
- Resolve: Accept any uncertain public, persistent, security, or cross-module contract before implementation.
- Resume: Read the task, accepted design, current diff, last passing check, and first incomplete condition.
- Complete: Prove the user path, error path, owned tests, docs, package boundary, and release impact.

## Propose or resume a design

- Start: State one problem, decision scope, alternatives, evidence needs, and affected authorities.
- Record: Put normative decisions in the repository's decision owner. Keep surveys non-normative.
- Compare: Show tradeoffs, failure modes, migration cost, and explicit non-goals.
- Resume: Read annotations and unresolved decision gates. Do not repeat settled analysis.
- Complete: Record the accepted, rejected, or postponed result. List implementation dependencies and stop conditions.

## Start or resume a discussion

- Start: Ask one focused question. Name the decision or action that the answer can affect.
- Record: Keep exploratory discussion in chat unless durable review needs a design or issue artifact.
- Bound: Discussion permits no file change, decision acceptance, or publication by itself.
- Resume: Link the prior thread or summarize settled points and the remaining question.
- Complete: State the conclusion, disagreement, evidence gap, and next authorized action.

## Report, diagnose, or fix a bug

- Start: Give expected behavior, actual behavior, reproduction steps, environment, and relevant evidence.
- Classify: State whether the request permits a report, diagnosis, or fix.
- Record: Keep the smallest stable regression case that proves the defect.
- Resume: Reproduce at the recorded revision. Read the diagnosis, diff, and last failing or passing check.
- Complete: Explain the cause. For a fix, prove the regression, nearby behavior, docs, and release impact.

## Update or resume documentation

- Start: Name the reader, required outcome, canonical page, and evidence owner.
- Record: Distinguish authored sources, generated projections, translations, and temporary notes.
- Write: Use one stable term, direct verbs, short sentences, and explicit conditions.
- Resume: Read the canonical source and generation state. Do not edit a projection as authority.
- Complete: Check claims, links, navigation, examples, generated outputs, and stale competing text.

## Start or resume a refactor

- Start: State the behavior that must remain and the boundary that must improve.
- Record: Add a plan for cross-module, persistent, or public changes. Name the migration sweep.
- Bound: Do not mix an unrelated feature with the refactor.
- Resume: Read invariants, completed slices, current call sites, and the next safe deletion.
- Complete: Prove behavior parity, remove obsolete paths, update docs, and record any compatibility waiver.

## Launch or resume an experiment

- Start: State the hypothesis, metric, baseline, limit, end condition, and promotion rule.
- Isolate: Keep experimental state outside production authority and supported public contracts.
- Record: Save inputs, environment, method, result, and known sources of bias.
- Resume: Use the same baseline and measurement method, or record the change.
- Complete: Accept, reject, or leave the hypothesis unresolved. Remove temporary state or promote verified results.

## Manage tasks

- Start: Read the canonical queue before you create or update a task.
- Create: Give one stable ID, outcome-shaped title, priority, state, acceptance list, dependencies, and links.
- Claim: Set one owner and `active` before implementation when repository policy requires it.
- Resume: Select the highest-priority ready task whose dependencies are complete.
- Complete: Verify acceptance, update closeout evidence, close linked plans, and remove terminal queue rows when required.

## Maintain repository hygiene

- Start: Define the surface and state that product behavior must not change.
- Inspect: Check status, ignored files, generated files, stale docs, dead code, duplicate authorities, and dependency drift.
- Protect: Preserve unrelated work. Resolve exact targets before any deletion or history change.
- Resume: Recheck status and generated-file drift before continuing cleanup.
- Complete: Run the full repository gate and report removed material plus recovery limits.

## Edit or resume a workflow

- Start: Name the workflow owner, current behavior, desired behavior, and affected users or agents.
- Inspect: Read the complete skill or repository workflow before editing it.
- Record: Update one canonical rule. Regenerate indexes or mirrors from that owner.
- Resume: Check the workflow version, generated state, installations, and linked compatibility tests.
- Complete: Test positive and failure paths. Verify installs, mirrors, navigation, and version identity.

## Launch or resume large parallel implementation

- Start: Get explicit authority for parallel agents. Define one parent outcome and one integration owner.
- Partition: Freeze shared contracts first. Give each slice exclusive path ownership and acceptance conditions.
- Record: Put dependencies, merge order, shared fixtures, and stop conditions in one parent plan.
- Resume: Read each slice status and integrate only verified outputs. Resolve overlaps with their owners.
- Complete: Run assembled tests after merge. Close child tasks before the parent task.

## Start or resume a downstream project

- Start: Name the consumer, supported artifact, compatibility range, and required user outcome.
- Bound: Depend only on published or explicitly supported interfaces. Do not import private source paths.
- Record: Keep a minimal consumer fixture and the exact upstream version or revision.
- Resume: Reproduce the consumer against that artifact before changing either side.
- Complete: Pass the consumer fixture, document upgrade steps, and record upstream or downstream ownership.

## Compress or resume test compression

- Start: Inventory behavior contracts, test tiers, cost, flakiness, and duplicate coverage.
- Classify: Keep contract tests. Mark redundant or private-detail tests with evidence.
- Change: Merge or remove tests only after retained tests cover the same meaningful behavior.
- Resume: Read the keep/drop record and compare test counts, tiers, duration, and last full result.
- Complete: Run targeted and full gates. Report kept, merged, rewritten, reclassified, and removed tests.

## Start or resume a survey

- Start: State one research question, scope, source standard, date boundary, and consuming decision.
- Gather: Prefer primary and current sources. Separate observed fact, inference, and recommendation.
- Record: Store citations, versions, comparison criteria, gaps, and source-quality limits.
- Resume: Check source freshness and continue from the unanswered comparison item.
- Complete: Answer the question or state why evidence is insufficient. Keep the report non-normative until accepted.

## Start or resume an integration

- Start: Name both systems, public protocol, authority boundary, compatibility range, and teardown owner.
- Design: Define validation, identity, errors, cancellation, retries, ordering, and partial-failure behavior.
- Record: Keep contract fixtures at the boundary. Do not share private runtime state.
- Resume: Verify both versions, last contract result, outstanding ownership issue, and cleanup state.
- Complete: Pass both-side contract tests, failure tests, packed or deployed artifact checks, and teardown verification.

## Hand off unfinished work

Give the next owner these facts:

- stable task and plan references;
- current branch, revision, and working-tree state;
- completed acceptance conditions;
- next incomplete condition;
- last verification command and result;
- blocker or resume condition;
- changed authorities and remaining risk.

Do not use chat history as the only resume state.
