---
name: code-explain
description: Read before explaining code, architecture, or changes.
task_kind: code-explain
status: active
---

# Code Explain Task

## Summary

Explain the user and system mental models with current source evidence for a reader new to the repository.

## Required reading

Before analysis or edits, complete [required code reading](../rules/project/read.md), including the full applicable language and shared project trees.

This prerequisite applies to repository code and architecture claims. A status question answerable from supplied verification facts can stay with the active role and [work boundaries](../rules/project/work.md); do not invent a source language or require a code walkthrough merely to explain why installation is incomplete.

## Goal

Answer code and architecture questions for a reader who is new to the repository. Explain the mental model from both user and system perspectives. Support the explanation with current source evidence.

## Scope Discovery

1. Identify the audience: user, developer, maintainer, reviewer, or mixed.
2. Identify the target: whole repo, architecture slice, module, feature, data flow, bug, diff, commit range, branch, or Linear issue.
3. Read `AGENTS.md`, relevant docs, nearby source, tests, generated artifacts, and examples in the relevant rules before explaining behavior.
4. For a TypeScript repository, inspect package entry points/exports, `tsconfig` coverage, composition roots, API types, async/resource owners, and package scripts before explaining lower-level modules. For Python, inspect the public facade, package boundaries, and declared runtime owners.
5. Prefer the repository's current mental model, concepts, data-flow, routing, and generated-capability documentation when present. Then verify it against source. For changed names, use the applicable [language compatibility rule](../rules/overview.md).
6. If the user wants a new design, architecture health review, periodic review, or refactor plan rather than an explanation, route to [design](design/README.md).

## Explanation Structure

Lead with the answer. For an unfamiliar concept, use purpose → concrete example → consequential boundary → minimal interface or command. Explain what the caller writes, sees, and expects before tracing internal implementation. Link current source evidence beside the claim.

Use the question to select the detail:

| Question | Show |
| --- | --- |
| “What is it; why separate it?” | Its responsibility, one use case, and why an existing owner cannot do that job as clearly. |
| “How does it differ?” | The relevant distinction: identifier vs object, definition vs live instance, building vs executing, closing vs deleting, or another actual contract. |
| “Is it ready/current?” | The inspected revision and whether it is proposed, implemented, verified, integrated, installed, or running. |
| “Why is this a problem?” | A concrete trigger, expected/actual result, and impact. |
| “Which should we choose?” | The recommendation and decisive tradeoff under [judgment](../rules/project/work.md#interpret-intent-and-exercise-judgment). |

For a broader walkthrough, follow the actual input-to-result path and name the objects that own each step. Use a compact table or diagram only when it reduces the explanation. Do not introduce every class, a glossary, or a second summary merely to fill an output shape.

## Style Criteria

- Start concrete, then generalize. Avoid dumping every class before the reader knows the use case.
- Keep the repository's public terms stable. Distinguish public names from internal implementation labels.
- Separate facts from inference. Say when an explanation is inferred from tests or code shape.
- Prefer diagrams for multi-hop flows, but do not use diagrams as decoration.
- Use examples that can plausibly run in the current repo.
- If the question asks for a recommendation, include tradeoffs and a direct next step.

## Output Modes

- **Quick answer:** 1-3 paragraphs plus key files.
- **Walkthrough:** follow the user and system flow; link the key owners. Use only the detail needed to answer the question.
- **Diff explanation:** what changed, why it matters, behavior impact, compatibility/migration, tests/docs.
- **Onboarding map:** introduce the main responsibilities, a common entry point, and the first useful files. Explain unfamiliar terms beside their use.
