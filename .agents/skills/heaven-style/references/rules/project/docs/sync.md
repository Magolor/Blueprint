---
name: project-docs-sync
description: Read before synchronizing or retiring documentation.
---

# Synchronize and retire documentation

## Summary

Keep current documentation small, coherent, and useful to its reader. Promote durable facts into one owner and move useful execution evidence out of the main reading path.

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

For corrections, follow [whole-document integration](edit.md). Current guidance explains accepted behavior; the development log records the changed decision.

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

## Maintenance review

Review at the repository’s chosen cadence, release preparation, or signs of drift: repeated instructions, slow onboarding, a growing decision list, stale plans, or conflicting claims. No fixed word, file, or decision-count limit is required.

- Check each user-facing page and engineering entry for one audience, purpose, and level of detail. Replace duplicate claims with links. Split by reader need only when navigation improves; many tiny pages can increase reading cost.
- Keep decision records at the [declared high-level scope](../docs.md#authority-maps-decisions-and-external-evidence). Consolidate refinements under their owner without erasing rationale, accepted constraints, or stable references. A larger decision count is not evidence of progress.
- Move useful per-commit, slice, experiment, and review evidence to the existing development-log lane. As it grows, use year/month folders and dated entries behind one short index, or the repository’s equivalent chronological scheme. Keep full logs and annotations in linked evidence; discard unneeded chatter under retention policy. Do not copy each entry into the index.
- Retire finished plans and actioned reports after promoting surviving conclusions. Keep an audit trail only where needed, clearly historical. Preserve active requirements and unresolved risks.
- Pair this pass with the [quality review](../../../tasks/design/review.md): simplify code and compress redundant tests while preserving supported behavior and meaningful coverage.

Record a concise closeout in the existing log and put actionable follow-up in the canonical queue. Reuse an existing review owner; do not create a permanent report series for routine cleanup. Review success means readers can find current guidance with fewer competing claims, and checks still protect the supported contracts.
