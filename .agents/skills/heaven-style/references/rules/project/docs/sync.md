---
id: project-docs-sync
title: Synchronize and retire documentation
description: Read for synchronize and retire documentation.
blocking: true
---

# Synchronize and retire documentation

## Update triggers

| Change | Required documentation action |
| --- | --- |
| Public behavior, install, configuration, CLI, API, or supported workflow | Update canonical user docs and executable examples; regenerate copies. |
| Architecture, ownership, dependency direction, persistence, lifecycle, extension seam, or compatibility | Update the engineering mental model/ADR and distinguish current implementation from accepted target and remaining gap. |
| Multi-session or delegated work | Create or update one queue task; add one linked plan only when ordered detail is needed. |
| Generated schema, inventory, capability, benchmark, API, or README | Run the owner generator and its `--check`/freshness gate. Unexpected probe errors must not silently become ordinary “unknown” values. |
| Substantial implementation, review, release, decision, blocker, or handoff | Append one concise development-log entry with task, change, verification, and next task or `none`. |
| Temporary requirement, brainstorm, comparison, or unaccepted design | Keep it in the declared scratch lane with owner and expiry, or in ignored local scratch when no handoff is required. |
| Canonical source changes while translations exist | Mark translation staleness and route translation separately; do not mix incidental translation into ordinary source sync. |

Small internal edits do not require ceremonial documents. They still update existing docs when their claims become false.

## Cleanup triggers

Clean documentation when any of these becomes true:

- a plan is done, superseded, or no longer owned;
- a review/report's recommendations were actioned or its status/path claims became historical;
- a current-only documentation set contains dated evidence that no longer describes current state;
- two pages state the same rule or one page contradicts the canonical owner;
- a temporary note expires or a discussion becomes an accepted decision;
- a generated artifact no longer has a generator or freshness check;
- a task closed but remains in a queue, goal, plan, log `Next`, or TODO list;
- navigation points to removed, renamed, or superseded content.

Cleanup means:

1. Promote the surviving current fact into its normative user/engineering/code/test owner.
2. Update task, plan, decision, report, and development-log state.
3. Remove closed queue rows and delete or clearly supersede contradictory legacy pages.
4. Delete expired scratch and orphan generated output.
5. Refresh navigation, local links, generated projections, and translations state.

Use Git history for old execution chatter. Keep historical reports only when the repository explicitly needs an audit trail; label status and staleness so they cannot masquerade as current truth.
