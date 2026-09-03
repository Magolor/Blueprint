---
id: workflow-start
title: Start or resume a workflow
enabled: true
order: 1
audience: all
keywords: [start workflow, resume workflow, feature, design proposal, discussion, bug report, documentation, refactor, experiment, task management, hygiene, edit workflow, parallel implementation, downstream project, test compression, survey, integration]
description: Use when a user, developer, architect, or agent must select, start, hand off, or resume a Heaven Style workflow.
---

# Start or Resume a Workflow

Use this page to select one workflow. The target repository policy has priority over this page.

After you select a route, use [Work Type Procedures](work-types.md) for its full lifecycle and completion gate.

## Give the minimum context

Copy this request and replace each value:

```text
Use $heaven-style.
Repository: <repository or project>
Workflow: <work type>
Outcome: <observable result>
Allowed action: discuss | inspect | design | change | publish
Acceptance: <conditions that prove completion>
Constraints and non-goals: <limits>
Resume from: <task, issue, branch, commit, plan, or none>
Evidence: <error, reproduction, document, code, source, or none>
```

Use one stable term for each concept. Add details only when they change the work.

## Know your responsibility

- A user states the outcome, allowed action, acceptance conditions, and important limits.
- A developer identifies the affected contract, implementation slice, tests, and compatibility effect.
- An architect resolves boundaries, authority, non-goals, risks, and decision gates before implementation.
- An agent reads repository policy and task state. The agent announces the route, preserves unrelated work, and reports verification.

## Select the route

| Work type | Start action | Heaven Style route |
| --- | --- | --- |
| Feature | State the user outcome, acceptance conditions, and non-goals. Resolve an uncertain contract before code changes. | Use [Arch Design](../tasks/arch-design.md), then [Code](../tasks/code.md). Skip design when the contract is already clear. |
| Design proposal | State the problem, decision scope, alternatives, and required evidence. Do not implement the proposal. | Use [Arch Design](../tasks/arch-design.md). |
| Discussion | State one question and the decision that it can affect. Keep the discussion read-only unless the request permits changes. | Use chat first. Use [Arch Design](../tasks/arch-design.md) when the result must become a durable decision. |
| Bug report | Give the expected result, actual result, reproduction, environment, and evidence. State whether to diagnose or fix. | Use [Code](../tasks/code.md). A diagnosis request does not permit a fix. |
| Documentation update | Name the canonical page, reader, outcome, and evidence owner. | Use [Documentation Writing and Sync](../tasks/doc-sync.md). |
| Refactor | State the behavior that must not change. State the boundary that must improve. | Use [Code](../tasks/code.md). Use [Arch Design](../tasks/arch-design.md) first for public, persistent, or cross-module changes. |
| Experiment | State the hypothesis, measure, limit, end condition, and promotion rule. Keep experimental results outside production authority. | Use [Code](../tasks/code.md). Use [Arch Design](../tasks/arch-design.md) first when the experiment changes a contract or boundary. |
| Task management | Name the repository queue and the required status view or update. | Use [Manager](../tasks/manager.md). |
| Repository hygiene | Name the surface to clean. State that product behavior must not change. | Use [Manager](../tasks/manager.md) for coordination, [Code](../tasks/code.md) for code, or [Documentation Writing and Sync](../tasks/doc-sync.md) for docs. |
| Workflow edit | Name the workflow owner and the behavior to change. | Use [Skill Update](../tasks/skill-update.md) and [Editor Workflow](editor.md) for Heaven Style. Use the target repository's workflow owner for local policy. |
| Large parallel implementation | Define one parent outcome, stable shared contracts, independent slices, path ownership, dependencies, merge order, and one integration owner. Explicitly authorize parallel agents. | Use [Manager](../tasks/manager.md) with [Arch Design](../tasks/arch-design.md). Route each accepted slice through [Code](../tasks/code.md), review, and docs sync. |
| Downstream project | Name the consumer, supported public artifact, compatibility range, and integration test. Do not depend on a private path or source checkout. | Use [Arch Design](../tasks/arch-design.md), then [Code](../tasks/code.md). |
| Test compression | State the behavior contracts and test tiers that must remain. | Use [Test Compress](../tasks/test-compress.md). |
| Survey | State the question, scope, source requirements, and decision that will use the evidence. Keep observations separate from decisions. | Use [Arch Design](../tasks/arch-design.md). Label the output as evidence until an owner accepts a decision. |
| Integration | Name both systems, the public protocol, authority boundary, compatibility fixture, failure behavior, and teardown owner. | Use [Arch Design](../tasks/arch-design.md) when the boundary is open. Use [Code](../tasks/code.md) when the contract is accepted. |

## Start the work

1. Read the repository `AGENTS.md` file and its declared task queue.
2. Select one primary route from the table.
3. Announce the route and the allowed action.
4. Create or claim one queue task when the work must continue after the current session.
5. Define the acceptance conditions before you change files.
6. Read only the rules that apply to the selected route.
7. Preserve unrelated work in the repository.
8. Verify the result with the repository commands.
9. Update the canonical docs, development log, and task state when required.

## Resume the work

1. Give one stable resume reference.
2. Read the canonical queue before you create a task.
3. Read the current branch, diff, last verified evidence, and open acceptance item.
4. Confirm that the original allowed action still applies.
5. Continue from the first incomplete acceptance item.
6. Do not create a duplicate task or a second writable tracker.

Start a new task when the requested outcome changes. Reopen or replace a closed task only when repository policy permits it.

## Keep authority explicit

- A discussion does not permit a file change.
- A diagnosis does not permit a fix.
- A design does not permit implementation.
- A local change does not permit publication, deployment, or an external message.
- Parallel work requires an explicit request and stable slice ownership.

## Close or hand off the work

Report the outcome, changed owners, verification, remaining risk, and next action. Remove closed queue state when repository policy requires removal. Give the same stable reference when another person or agent must resume the work.
