---
name: workflow-design-review
description: Read before a periodic architecture or code-quality review.
---

# Periodic architecture review

## Summary

Review architecture, code, tests, and documentation together. Reduce the cost of understanding and changing the system while preserving supported contracts.

## Periodic architecture review

Use a periodic review when the project has a cadence, reaches a release boundary, accumulates repeated defects, expands a provider/backend family, or shows architecture drift in docs, tests, or implementation.

1. **Scope** - name the package, module family, feature slice, release train, or whole-repo boundary under review.
2. **Comparison point** - cite the last review, last release, baseline branch, roadmap item, or current state if no previous review exists.
3. **Evidence** - inspect architecture docs, current goals, canonical tasks, the development log, public exports, dependency entry points, open-registry or closed-variant seams, tests, examples, open issues, and recent PRs/commits when available.
4. **Change pressure** - list what actually changed: user requests, new backends/providers, schema/storage behavior, defects, onboarding pain, or repeated code-review findings.
5. **Smell matrix** - score rigidity, fragility, immobility, viscosity, needless complexity, needless repetition, and opacity with concrete file/doc/test evidence.
6. **Dependency matrix** - identify inward dependencies, cycles, unstable dependencies, detail leakage into policy, and extension seams that require central edits.
7. **Fitness checks** - name the tests, examples, CI checks, docs checks, or probes that prove the architecture remains changeable.
8. **Actions** - classify recommendations as **now**, **next**, **defer**, or **waive**. Avoid broad rewrites unless the evidence shows repeated change cost.
9. **Next trigger** - record the next review trigger or cadence only when the project actually uses one.

Deliverable: an **architecture review** with scope, evidence, findings, prioritized actions, verification expectations, and docs/task/issue updates. Store it only where repository policy keeps current engineering truth or auditable evidence; actionable follow-up becomes one canonical queue item.

## Code and test simplification

Inspect public concepts, modules, dependencies, compatibility paths, dead code, duplicate policy, and speculative abstractions. Remove unused behavior and merge boundaries that have no independent responsibility. Prefer a smaller supported codebase, but do not minimize line count by hiding intent, weakening validation, or joining responsibilities that change independently.

Use [test compression](../tests.md) for duplicated cases, brittle internal assertions, oversized fixtures, and slow setup. Map each removal or merge to retained behavior coverage; keep durable regressions and meaningful edge, failure, integration, and package paths. Fewer tests or lines alone is not success. Run affected checks and the repository’s required gate; report remaining coverage gaps.

Apply [documentation maintenance](../../rules/project/docs/sync.md#maintenance-review) in the same review. A small cleanup needs only concise evidence in the existing log; write a separate report when findings need independent review or follow-up.
