---
name: workflow-design-inspect
description: Read before architecture discovery in an unfamiliar repository.
---

# Architecture discovery

## Summary

Inspect repository-wide evidence before narrowing to the affected architectural boundary.

## Discovery procedure

Start from repository-wide evidence, then narrow to the affected surface. Prefer live connectors for linked external state; use local Git and docs when unavailable.

1. Read `AGENTS.md`, the authority map, canonical queue, development log, goals, and current mental model.
2. Inspect manifest/version, branch, compatibility/release policy, runtime pins, lockfile, command entry points, and public exports. Map layers rather than every file.
3. Inventory user, engineering, generated, sibling, and temporary docs. Classify current, target, gap, non-goal, stale, duplicate, orphan, and expiring scratch. Resolve one owner for each public claim.
4. Inspect variation boundaries: open registries/providers versus closed variants. Sample contract tests and examples; note compatibility exports, TODOs, and duplicated planners.
5. Read linked Linear milestones, issue evidence, blockers, status comments, and design threads; read linked GitHub PRs, failing checks, reviews, and recent merges. Trackers remain subordinate to the declared queue. Use the [failure routes](../README.md) only when blocked.

Produce a current-state brief of at most half a page: purpose, boundary map, queue/docs/goals/code mismatches, recorded constraints/non-goals, and decision-blocking questions. List mismatches before detailed design. Clarify unresolved scope without reopening settled decisions.
