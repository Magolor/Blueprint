---
id: code-explain
task_kind: code-explain
status: active
description: Explain existing architecture, modules, behavior, or changes.
---

# Code Explain Task

Before analysis or edits, complete [required code reading](../workflows/read.md), including the full applicable language and shared project trees.

## Goal

Answer code and architecture questions for a reader who is new to the repository. Explain the mental model from both user and system perspectives. Support the explanation with current source evidence.

## Scope Discovery

1. Identify the audience: user, developer, maintainer, reviewer, or mixed.
2. Identify the target: whole repo, architecture slice, module, feature, data flow, bug, diff, commit range, branch, or Linear issue.
3. Read `AGENTS.md`, relevant docs, nearby source, tests, generated artifacts, and examples in the relevant rules before explaining behavior.
4. For a TypeScript repository, inspect package entry points/exports, `tsconfig` coverage, composition roots, API types, async/resource owners, and package scripts before explaining lower-level modules. For Python, inspect the public facade, package boundaries, and declared runtime owners.
5. Prefer the repository's current mental model, concepts, data-flow, routing, and generated-capability documentation when present. Then verify it against source. For legacy names, see [compat](../rules/code/python/compat.md).
6. If the user wants a new design, architecture health review, periodic review, or refactor plan rather than an explanation, route to [design](design.md).

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
- Keep the repository's public terms stable. Distinguish public names from internal implementation labels.
- Separate facts from inference. Say when an explanation is inferred from tests or code shape.
- Prefer diagrams for multi-hop flows, but do not use diagrams as decoration.
- Use examples that can plausibly run in the current repo.
- If the question asks for a recommendation, include tradeoffs and a direct next step.

## Output Modes

- **Quick answer:** 1-3 paragraphs plus key files.
- **Walkthrough:** sections for user perspective, system perspective, data flow, key files, and summary.
- **Diff explanation:** what changed, why it matters, behavior impact, compatibility/migration, tests/docs.
- **Onboarding map:** architecture layers, common entrypoints, glossary, and first files to read.
