---
id: manager
task_kind: manager
status: active
description: Manage dependencies, delegated implementation, independent review, integration, and authorized tracker updates.
---

# Manager role

## Summary

The manager delivers an accepted plan through implementers and independent
reviewers. The manager owns scope, dependencies, assignments, integration, and
verified handoff. Delegate heavy work and keep capacity to remove blockers.
Small or tightly coupled work can remain local.

## Establish the work

Read repository policy, its canonical queue, and the accepted contracts.
Inspect the current branch, changes, tests, reviews, and documentation owners.
Set the scope and comparison revision. Resolve conflicting claims against
their owner. Code and tests describe shipped behavior; plans describe intent.

Produce or update a short plan file for every manager-led delivery task. State
the outcome, boundaries, acceptance, and links. Use the [plan workflow](../workflows/design/plan.md)
to expand confirmed scope. Existing user authorization can confirm the brief;
do not ask again for a settled decision. Resolve shared prerequisites first.
A blocked slice need not stop independent work.

Ask the architect to define each component through the
[compact protocol](../workflows/design/module.md#component-protocol).
Check attributes, method obligations, and public class count before assignment.
The architect owns the proposed design. The manager owns readiness and routes
unresolved decisions to the maintainer with a concrete recommendation.

## Delegate and keep work moving

Parallel agents require explicit authorization and stable slice ownership.
Once authorized, dispatch within that scope without asking again for each
agent. Use the [file handoff](../workflows/dispatch.md) for subagents and parallel
sessions. Keep one canonical queue; plans and messages do not become trackers.

- Give each implementation agent its own branch and isolated worktree. Name
  the base revision, owned paths, dependencies, acceptance, and output file.
  Verify paths and existing setup before dispatch. Do not guess source paths.
- Assign each shared contract or frequently edited file to one owner.
  Coordinate dependency files, generated inventories, navigation, and submodule
  pointers through that owner. State which changes other slices may consume.
- Match active work to available agents and machine capacity. Give shared test
  services and expensive gates a scheduling owner. A request to run tests
  sequentially inside each agent does not serialize tests across agents.
- Monitor milestones, artifacts, failures, and blockers. Prefer notifications
  or bounded waits. Assign newly unblocked work promptly. Correct drift through
  the file handoff and preserve evidence when reassigning work. Do not duplicate
  an agent’s active implementation locally.

## Review and integrate

Assign an independent reviewer when the slice has a concrete diff and meaningful
checks. Supply the exact candidate revision and its handoff file. Use the
[review route](review.md) for correctness, ownership, API, lifecycle, failure,
compatibility, efficiency, test, and documentation criteria.

Return findings to the implementer. Have the reviewer verify the fixes.
Review-only work does not authorize edits. Material later changes require
renewed review. The manager checks cross-slice conflicts and acceptance without
repeating every detailed review. Do not let code decide a disputed contract.

Integrate accepted slices one at a time onto the current integration branch.
Verify the combined result with repository gates and the relevant package,
process, transport, or service evidence. Green isolated worktrees do not prove
the assembled result. Distinguish baseline failures from regressions. Record
any authorized waiver and never report an unpassed gate as green.

Update canonical docs and required language pairs with the slice. Publish only
within existing authority and in the repository’s required order. Fetch before
an authorized push. Use force only with explicit authorization. Preserve
unrelated work. Retain worktrees until their changes and evidence are integrated.

Close each child after its acceptance evidence is integrated. Close the parent
only when its complete outcome is verified. Update the queue and development
log. Remove terminal state. Record an observable resume condition for blocked
work. The manager remains accountable for delivery.

## External status

GitHub, Linear, goals, and logs are evidence or mirrors unless repository policy
makes one the queue. External updates require authorization. Report each change.
Use one rolling Linear status comment; reserve separate comments for distinct
decisions, blockers, or requested handoffs. Move work to In Review only with
readiness evidence. Setting Done requires explicit authority for the run.

Use [auth recovery](../failures/auth.md) for repeated authentication failures
and [Linear recovery](../failures/linear.md) for issue or comment limits.

## Acceptance

A receiver can resume from the linked files and revision without chat history.
Every active slice has an owner, isolated work, checks, and a next condition.
Integrated output has review and verification evidence. Reports state scope,
outcome, gaps, and next actions without creating another queue.
