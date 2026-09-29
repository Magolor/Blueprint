---
name: workflow-refactor
description: Use when simplifying structure while preserving supported behavior.
---

# Refactor

## Summary

Reduce the cost of understanding and changing the system while preserving the accepted invariants. Refactor by ownership and user benefit, not by line-count targets.

## Tasks

1. Use [design](../tasks/design/README.md) and its [plan manual](../tasks/design/plan.md) to identify change pressure, invariants, ownership, ordered slices, and verification. Keep documentation proportional to the scope.
2. [Implement](../tasks/code/README.md) each coherent slice and update owned callers together. Preserve logical features while retiring the obsolete interface: sweep callers, exports, defaults, tests, examples, and current docs under the matched [compatibility rule](../rules/overview.md). Keep one live path in owned/unreleased code; an old name alone does not justify a shim. [Compress tests](../tasks/tests.md) when duplication exists, preserving meaningful coverage.
3. [Review](../tasks/review.md), [triage](../tasks/triage.md), and [address](../tasks/address.md) material findings. Use [Extensive Review](review.md) for requested or substantial cross-boundary work.
4. Run [Document](document.md), verify the assembled candidate, and [sync](../tasks/sync/README.md) the accepted output and devlog evidence.

## Acceptance and stopping

Invariants and supported paths still hold, the intended ownership or complexity improvement is evident, and required checks pass. Pause dependent changes when a new behavior decision exceeds scope. Do not hide feature changes inside a structural refactor.

Verify the retained capability through its current entry point. Search the affected surface for obsolete imports, aliases, wrappers, fallback branches, and examples; remove them or identify their real support obligation. Keep useful decision history in its history owner. Do not preserve a superseded implementation merely to keep its tests green, or delete a supported feature to claim a smaller codebase.
