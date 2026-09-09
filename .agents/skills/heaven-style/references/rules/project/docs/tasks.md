---
name: project-docs-tasks
description: Read before creating, resuming, handing off, or closing tasks.
---

# Task ownership

## Summary

Keep live work in one canonical queue with explicit ownership and observable completion or resumption conditions.

## One task authority

- The repository declares exactly one writable active task queue. A repository file, GitHub, or Linear may own it; snapshots and links are read-only mirrors.
- Read the queue before creating work. A direct request that will finish in one session may stay unqueued; resumable, multi-slice, blocked, or independently delegated work must enter the queue.
- Queue items own identity, priority, status, owner, acceptance, dependencies, and links. Detailed slice checklists belong in one subordinate plan when needed.
- Chat, plans, reports, goals, TODO files, the development log, PR descriptions, and subagent notes must not become parallel task lists.
- Claim work explicitly. A blocked task states the blocker and observable unblock condition. Delegated work remains under the parent task unless it needs independent resumption; a durable delegated task points to its parent instead of duplicating child lists.
- Closed or cancelled work leaves the live queue after acceptance evidence is recorded. Git history, the development log, the issue/PR, and a closed plan preserve history.

## States

Use the repository schema. Common live states are `draft` (needs review), `ready` (clear and unblocked), `active` (named owner), `blocked` (external blocker and observable unblock condition), and `postponed` (intentional deferral and resume condition). Queue items include stable ID, outcome, priority, state, acceptance, dependencies, and links. Select the highest-priority ready task whose dependencies are complete. Record completion or cancellation and its reason in closeout history, then remove the live row when policy requires it.

## Pattern and Anti-pattern

- **Pattern:** The plan links task status to the canonical queue.
- **Anti-pattern:** Chat, a plan, and a separate TODO each maintain a different status.

One writable owner prevents contradictory resume state.
