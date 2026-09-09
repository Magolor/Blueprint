---
name: workflow-dispatch
description: Dispatch implementation and review through short plans and durable evidence files.
---

# File-based handoff

## Summary

Use files to transfer work between implementers, reviewers, and parallel
sessions. Keep the dispatch message short. The receiver reads one entry file
and follows its links. The canonical queue still owns task state.

## Prepare the assignment

Use an existing plan section when it owns the slice. Create a small linked
file when a separate assignment needs independent retrieval. Follow the
repository’s paths and metadata. Do not create a second planning hierarchy.

The entry file states:

- **Summary:** the user outcome and the receiver’s responsibility.
- **Input:** task and accepted design links, base revision, branch, worktree,
  owned paths, and verified setup already present.
- **Contract:** required attributes and methods, or a link to the
  [component protocol](../design/module.md#component-protocol).
- **Work:** short ordered actions, dependencies, non-goals, and stop conditions.
- **Acceptance:** observable results, focused checks, relevant aggregate gates,
  and required documentation updates.
- **Output:** the result file path, candidate revision, evidence, unresolved
  findings, and the next receiver.

Link canonical rules instead of copying them. Read linked sections by stable
headings, not stale line ranges. Pin the assignment to a revision. The receiver
must not silently follow a moving branch if its contracts change. The manager
coordinates the update and any required rebase.

## Expand a short request

Recover context from the accepted objective, current task, and verified repository state. Preserve requirement, question, proposal, example, and deferred status using [intent and judgment](../../rules/project/work.md#interpret-intent-and-exercise-judgment). Carry decision authority separately; uncertainty alone does not require another approval.

Use this order in the assignment file or existing plan section. Its opening Summary gives the project objective and current focus; the remaining fields can follow the repository’s format. Resolve routine placeholders before dispatch. Keep the project objective as context, not the receiver’s entire assignment.

```text
Skill: heaven-style, plus applicable repository instructions.
Role: [receiver’s actual role, responsibility, and assignment/session lifetime].

Project and objective: [one sentence describing the project and accepted outcome].
Current focus: [bounded result this receiver owns and why it matters].

Tasks:
1. [Action and expected output].
2. [Next action and expected output].

Emphasis:
- [Relevant constraints, behavior/content to preserve, and non-goals].
- [Owned paths, dependencies, and decisions reserved for another owner].

Done when: [observable acceptance and required checks].
Return: [result location, candidate revision, evidence, gaps, and receiver].
```

Use only relevant emphasis; do not paste every preference into each assignment. Translate “systematically” into the surfaces to inspect and “minimal” into the complexity to remove and behavior to preserve. Give Workers discretion over routine details. Assign the receiver’s actual role rather than copying the parent’s Manager identity; a review assignment specifies inspection and findings, not implementation.

For an open design choice, add a short clause: “Treat the proposed approach as a candidate. Preserve [goal and constraints], inspect relevant scenarios, and recommend the simplest sound choice. [Propose for review / decide and implement, as authorized].” Resolve the bracketed authority before dispatch. A detailed example must not become an extra feature requirement.

### Pattern and Anti-pattern

For “clean up the old interface”, first verify the accepted replacement and support policy.

- **Pattern:** “Project objective: one coherent SDK. Current focus: complete the accepted interface replacement in the export component. Update its owned callers, tests, examples, and docs; retire obsolete paths under the compatibility rule. Done when retained behavior works through the current entry and required checks pass. Return the candidate and evidence; the manager owns integration.”
- **Anti-pattern:** “Modernize the whole SDK, keep aliases just in case, and finish everything.”

The pattern bounds the assignment and preserves capability. It does not turn project context into unlimited scope or invent a support contract. A tiny assignment may use two sentences and a short list instead of every field.

## Dispatch and monitor

Send the entry path, revision, role, worktree, and output path. Require the
receiver to read the entry before editing. A long prompt is not a substitute
for the file. Use an available attachment or shared artifact if sessions do
not share a filesystem; do not send a path the receiver cannot access.

Keep setup state and corrections in the entry file. Notify the receiver of
the changed section and revision. Preserve one owner for each shared file.
Give an implementer a task-owned result path even when central plans, queue,
or development logs are manager-owned. A ban on central document edits must
not force the only evidence into chat.

## Return and review

For a side discussion, transfer the proposed or accepted decision, reason, preserved constraints, open question, canonical owner, and next authorized action. Update the existing decision or assignment before resuming dependent work. Do not promote a brainstorm to accepted design merely because it arrived in a handoff.

The result file starts with a short outcome summary. Record the exact candidate
commit, changed paths, acceptance results, commands and outcomes, relevant logs,
remaining gaps, and disposition questions. Link evidence rather than embedding
large transcripts. Keep secrets and raw private traces out of the artifact.

The reviewer reads that file and inspects the named revision. Record findings
and their resolution under the repository’s review procedure. Fixes update the
candidate revision and the handoff. Retire temporary detail through the normal
task lifecycle after integration.

## Acceptance

A new session can find the input, perform the assigned work, and verify the
result from files alone. No assignment depends on an unrecorded chat correction.
The reviewer can identify the exact code and evidence being accepted.

For dependencies and integration ownership, use the [manager role](../../roles/manager.md).
For proposed and confirmed plans, use the [planning manual](../design/plan.md).
