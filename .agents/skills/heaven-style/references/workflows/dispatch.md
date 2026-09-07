---
id: workflow-dispatch
title: File-based handoff
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
  [component protocol](design/module.md#component-protocol).
- **Work:** short ordered actions, dependencies, non-goals, and stop conditions.
- **Acceptance:** observable results, focused checks, relevant aggregate gates,
  and required documentation updates.
- **Output:** the result file path, candidate revision, evidence, unresolved
  findings, and the next receiver.

Link canonical rules instead of copying them. Read linked sections by stable
headings, not stale line ranges. Pin the assignment to a revision. The receiver
must not silently follow a moving branch if its contracts change. The manager
coordinates the update and any required rebase.

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

For dependencies and integration ownership, use the [manager role](../tasks/manager.md).
For proposed and confirmed plans, use the [plan workflow](design/plan.md).
