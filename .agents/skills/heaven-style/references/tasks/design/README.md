---
name: arch-design
description: Read before architecture design or health review.
task_kind: arch-design
status: active
---

# Architecture design and review

## Summary

Design for verified change pressure and testable boundaries, then hand off the appropriate design, decision, or plan.

## Required reading

Use for new designs, refactor plans, targeted architecture reviews, or periodic health reviews before implementation. First complete [the architecture reading prerequisite](../../rules/project/read.md), including every design manual and code-design comparison. Read the repository mental model, current goals/tasks, public boundaries, tests, and actual reasons for change. Use [architecture outputs](guide.md) for the required artifact; code diffs use [review](../review.md).

## Decision checks

Design for verified change pressure. Requirements can change; each slice needs feedback through working software, tests, examples, review, or issue acceptance. Defer patterns and abstractions that solve imaginary variation. Diagrams clarify decisions but do not prove behavior.

| Smell | Evidence to find |
| --- | --- |
| Rigidity | One small requirement forces unrelated edits. |
| Fragility | Changes break surprising areas without a clear dependency. |
| Immobility | Useful behavior is trapped behind framework, storage, CLI, or provider details. |
| Viscosity | The wrong shortcut is easier than the supported change. |
| Needless complexity | Layers, flags, or patterns serve hypothetical futures. |
| Needless repetition | Business rules, defaults, schemas, or concepts have competing owners. |
| Opacity | Names, docs, and tests fail to explain the system. |

Use native [TypeScript SOLID](../../rules/code/typescript/solid.md) or [Python SOLID](../../rules/code/python/solid.md) for disputed boundaries. Name findings precisely: SRP (reason to change), OCP (open extension), LSP (substitution), ISP (capability separation), DIP (inward dependencies).

Core policy must not depend on drivers, file systems, provider SDKs, web/CLI adapters, or generated artifacts. Volatile details depend on stable abstractions. Cross-layer/package and initialization-order cycles are blockers; an intrinsic local cycle needs an owner and fitness test. Group code that changes together; release and document units reused together. ADP, REP, Common Closure/Reuse, Stable Dependencies, and Stable Abstractions are diagnostic tools, not reasons to add layers.

Register open families and exhaust closed variants. Independently extensible families share bundled/external registration, selection, and contract tests. Catalogs, acquisition, trust, and managed lifecycle require a product promise.

## Deliverables

Design: use the [design template](../../../assets/templates/design.md) for motivation, intuition, architecture, public mental model, tradeoffs, boundaries, and open questions. Link focused contracts when needed. A [decision](../../../assets/templates/decision.md) records disposition and rationale. An authorized implementation/refactor [plan](../../../assets/templates/plan.md) owns success criteria, migration, ordered slices, tests/CI feedback, docs impact, risks, and waivers.

Review: scope, trigger/cadence, comparison point, evidence, dependency map, severity/impact/fix findings, goal/docs/code alignment, and actions classified as now, next, defer, or waive. Name the next review trigger only when used by the project.

Before handoff, distinguish current behavior, accepted target, gap, and non-goal. Every recommendation needs a verification path. Keep slices small enough for focused PRs or agent sessions. Name required docs, goals, and issue changes. Report unapplied checks and waivers.
