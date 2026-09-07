---
id: workflow-design-review
title: Periodic architecture review
description: Read for periodic architecture review.
---

# Periodic architecture review

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
