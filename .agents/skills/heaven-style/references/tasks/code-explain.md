---
id: code-explain
task_kind: code-explain
status: active
enabled: true
order: 35
keywords: [explain code, explain module, architecture walkthrough, data flow, how does this work, compare changes]
triggers: [explain, walkthrough, how does, architecture, dataflow, compare code, module question]
description: Use when explaining TypeScript/Python repository architecture, modules, data flow, feature behavior, code changes, or project-specific systems.
related_rules: [overview, docs, ts-architecture, ts-api, ts-modules, model, oop, files, extension, interfaces, clean]
---

# Code Explain Task

## Goal

Answer code and architecture questions as if the reader is new to the repo. Make the mental model clear from both user and system perspectives, grounded in current source evidence.

## Scope Discovery

1. Identify the audience: user, developer, maintainer, reviewer, or mixed.
2. Identify the target: whole repo, architecture slice, module, feature, data flow, bug, diff, commit range, branch, or Linear issue.
3. Read `AGENTS.md`, relevant docs, nearby source, tests, generated artifacts, and examples in the relevant rules before explaining behavior.
4. For a TypeScript repository, inspect package entry points/exports, `tsconfig` coverage, composition roots, API types, async/resource owners, and package scripts before explaining lower-level modules. For Python, inspect the public facade, package boundaries, and declared runtime owners.
5. Prefer the repository's current mental model, concepts, data-flow, routing, and generated-capability documentation when present, then verify against source; for legacy names, see [compat.md](../rules/code/python/compat.md).
6. If the user wants a new design, architecture health review, periodic review, or refactor plan rather than an explanation, route to [arch-design.md](arch-design.md).

## Explanation Structure

Use the smallest structure that answers the question. For broad explanations, include:

- One-sentence answer.
- User perspective: what the user writes, sees, configures, and expects.
- System perspective: which objects/modules handle the request and where control/data move next.
- Data flow: inputs, normalization, planning/routing, handler/backend execution, result shaping, catalog/docs sync when relevant.
- Architecture map: key packages/classes/functions and why they exist.
- Illustration: Mermaid diagram, compact table, or step list when it reduces cognitive load.
- Code references: clickable file/line links when available.
- Code-change comparison: before/after behavior, API surface, migration impact, tests/docs implications, and risks.
- Summary: what to remember and what to read next.

## Style Criteria

- Start concrete, then generalize. Avoid dumping every class before the reader knows the use case.
- Keep the repository's public terms stable and distinguish public names from internal implementation labels.
- Separate facts from inference. Say when an explanation is inferred from tests or code shape.
- Prefer diagrams for multi-hop flows, but do not use diagrams as decoration.
- Use examples that can plausibly run in the current repo.
- If the question asks for a recommendation, include tradeoffs and a direct next step.

## Output Modes

- **Quick answer:** 1-3 paragraphs plus key files.
- **Walkthrough:** sections for user perspective, system perspective, data flow, key files, and summary.
- **Diff explanation:** what changed, why it matters, behavior impact, compatibility/migration, tests/docs.
- **Onboarding map:** architecture layers, common entrypoints, glossary, and first files to read.
