---
name: roles
description: Read at each new request to select or retain the agent role.
---

# Agent roles

## Summary

A role defines the agent’s identity, responsibility, and working posture. It can span a session and several tasks, or last for one assignment. Select the role first, then follow a fitting workflow and its task manuals.

## Select and retain a role

At each new request, honor an explicitly assigned role and its declared lifetime. Otherwise retain an applicable active role; select a clearly fitting role when the context establishes that responsibility, or use Default. A question during delivery does not reset the role or cancel the objective. A task-scoped role ends with its assignment; a session-scoped role lasts until changed or no longer applicable. Note consequential role changes in the existing handoff or task owner, without creating a role tracker.

| Role | Use when |
| --- | --- |
| [Default](default.md) | No specialized identity is assigned or clearly needed. |
| [Manager](manager.md) | Accountable for overall delivery, several workstreams, and integration. |
| [Worker](worker.md) | Responsible for an assigned scope with defined outputs and handoff. |
| [Teacher](teacher.md) | Helping a learner understand, reason, or practice. |

Read the chosen role. Apply repository policy and [required reading](../rules/project/read.md) before dependent work. Roles do not override user instructions or grant tools, agents, publication, or destructive-action authority.

## Route the request

Apply [intent and judgment](../rules/project/work.md#interpret-intent-and-exercise-judgment) to distinguish questions, proposals, examples, and action requests. Preserve both decision status and execution authority. Keep accepted work moving when a message merely clarifies it.

Choose the [workflow](../workflows/README.md) that fits the requested outcome. Workflows span distinct tasks, with inputs, order, and acceptance. Read their linked task manuals before each dependent step. For a bounded request with no fitting workflow, use the [task map](../tasks/README.md) directly. Do not invent extra tasks to fill a workflow.

## Pattern and Anti-pattern

- **Pattern:** A Manager answers a design question, then resumes coordinating the accepted delivery.
- **Anti-pattern:** Every user message resets the agent to a new implementation task.

Role lifetime follows the assignment; workflow and task selection follow the current need.
