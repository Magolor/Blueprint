---
id: arch-design
task_kind: arch-design
status: active
enabled: true
order: 38
keywords: [architecture design, architecture review, periodic architecture review, module design, refactor plan, dependency review, agile design, SOLID, SRP, OCP, LSP, ISP, DIP, design smells, design doc]
triggers: [arch-design, architecture design, design architecture, architecture review, design review, periodic architecture review, module design, refactor plan, ADR]
description: Use when designing or reviewing architecture, module boundaries, dependency direction, extension seams, refactor plans, or periodic architecture health using agile design principles before implementation.
related_rules: [overview, docs, review, model, oop, solid, types, docstring, files, clean, compat, ts-architecture, ts-types, ts-modules, ts-async, ts-docs, ts-environment, extension, interfaces, test, environment]
---

# Arch Design Task

## Goal

Design or review architecture as a continuous, evidence-backed activity that keeps the repo cheap to change.

## Route

1. Load [../workflows/architect.md](../workflows/architect.md) before producing the artifact.
2. Classify the mode: **new design**, **refactor plan**, **targeted architecture review**, or **periodic architecture review**.
3. Read `AGENTS.md`, the environment rule, docs authority map, current goals, latest progress, architecture docs, public exports, registry/extension points, tests, examples, and issue context when available.
4. Use this task for design and review before implementation. Route implementation to [code.md](code.md), diff-focused code review to [code-review.md](code-review.md), and newcomer explanation to [code-explain.md](code-explain.md).

## Agile Design Principles

Use agile design as a control loop, not a big upfront phase:

- Expect requirements to change. Tie the design to current user, goal, issue, and code evidence; defer speculative abstractions.
- Prefer working software evidence. Tests, examples, shipped behavior, and accepted issue criteria outrank diagrams or stale plans.
- Keep the design simple but refactorable. Avoid both needless abstraction and convenient shortcuts that make future change harder.
- Treat tests, CI, and refactoring as architectural fitness functions. A design is not agile if changes cannot be made safely.
- Use design patterns only to manage real variation, dependency, or collaboration pressure already visible in the evidence.
- Use [Python SOLID](../rules/code/python/solid.md) or [TypeScript architecture](../rules/code/typescript/architecture.md) for SRP, OCP, LSP, ISP, and DIP boundary checks according to the target language.
- Keep documentation light but durable. Use diagrams and tables when they clarify decisions; never let them substitute for tests or code truth.

## Architecture Review Checklist

Review the system for the design smells Robert C. Martin uses to define change resistance:

| Smell | Review question |
| --- | --- |
| Rigidity | Does one small requirement force unrelated module, storage, UI, or API edits? |
| Fragility | Do changes break surprising areas or tests with no obvious dependency path? |
| Immobility | Are useful modules trapped behind framework, database, CLI, or provider details? |
| Viscosity | Is the quick wrong change easier than the clean change path? |
| Needless complexity | Are patterns, layers, flags, or abstractions solving imaginary futures? |
| Needless repetition | Is the same business rule, default, schema, or concept duplicated across surfaces? |
| Opacity | Can a new maintainer reconstruct the architecture from names, docs, and tests? |

Then check dependency health:

- Core policy and domain behavior must not depend on low-level details such as database drivers, web/CLI adapters, file systems, provider SDKs, or generated artifacts.
- Stable packages should expose abstractions; volatile details should depend on those abstractions.
- Cross-layer/package cycles and initialization-order-dependent runtime cycles are blockers. A proven intrinsic local cycle needs explicit ownership and a fitness test; otherwise plan a break.
- Modules that change together should live together; modules reused together should be released and documented together.
- Open extension families should use registration APIs instead of concrete-name routing; closed protocols should use exhaustive variants rather than a mutable registry.
- An open family that promises independent extensions should make bundled and external implementations traverse the same persisted catalog, resolver, loader, validation, lifecycle, public surface, and contract suite. Origin is metadata, not a privileged path.
- SOLID findings should name the exact principle abbreviation: **SRP** for reason-to-change boundaries, **OCP** for extension without reopening stable planners, **LSP** for substitutable contracts, **ISP** for optional capability surfaces, and **DIP** for dependency direction.

## Output Modes

For a **new design** or **refactor plan**, produce:

1. Current-state brief grounded in code, docs, tests, and issues.
2. Problem, success criteria, non-goals, and change pressures.
3. Layer placement, dependency direction, public surface, API standard table, and extension seam.
4. Test/refactoring/CI gates for each slice.
5. Docs touch list, implementation slices, risks, waivers, and handoff route.

For a **targeted or periodic architecture review**, produce:

1. Scope, trigger or cadence, comparison point, and evidence inspected.
2. Dependency map or boundary table.
3. Smell/dependency findings with severity, impact, and fix direction.
4. Alignment check against current goals, docs, tests, and shipped behavior.
5. Prioritized actions: **now**, **next**, **defer**, or **waive**.
6. Next review trigger, such as release boundary, major refactor, repeated defect pattern, or dated cadence when the project uses one.

## Completion Gate

Do not mark architecture work ready until:

- The agile design principles and smell checklist have been applied or explicitly waived.
- The artifact distinguishes shipped facts from planned behavior.
- Each recommendation has a feedback or verification path, not just a diagram.
- Implementation work is sliced small enough for focused PRs or agent sessions.
- Docs, goals, and issue status updates are named when they must change.

## Output

Report scope, evidence, artifacts produced, review findings or design decisions, verification expectations, risks/waivers, and the recommended handoff.
