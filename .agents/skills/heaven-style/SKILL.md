---
name: heaven-style
description: Personal code, documentation, architecture, and GUI conventions for TypeScript and Python work.
metadata:
  version: 0.1.2.23
---

# Heaven Style

## Summary

Apply repository policy, runtime contracts, and compatibility promises first. Preserve the repository's language and toolchain. Default an undecided new project to TypeScript.

## Required reading before work

This entry is a summary, not a substitute for the full rules. Complete the [reading procedure](references/workflows/read.md) before implementation, diagnosis, review, explanation, tests, or code-bearing examples. Small changes have the same reading prerequisite.

- **Code:** Read every Markdown file recursively in the applicable [TypeScript](references/rules/code/typescript) or [Python](references/rules/code/python) rule tree, plus all [shared project rules](references/rules/project) and [design philosophy](references/design/philosophy.md). Include nested examples, formats, lifecycle, package, and configuration pages. Read both language trees for work involving both languages.
- **Architecture:** Complete code reading for the target language, then read [architecture checks](references/tasks/design.md), [the architect workflow](references/workflows/architect.md), every [design workflow](references/workflows/design), and all [code-design comparisons](references/examples/code). Also inspect the repository’s architecture and decision owners before proposing structure.
- **GUI:** Read every file in [GUI design](references/design/gui), including stack, interaction, review, and all six palette files. GUI code and architecture work also require the corresponding code and architecture reading.
- **Authored docs:** Start with a short summary and consumer use. Read the [documentation task](references/tasks/docs.md) and [documentation rules](references/rules/project/docs.md), including [nested pages](references/rules/project/docs). Code examples and architecture claims add their respective reading prerequisites.

Reading a rule does not require adding an irrelevant feature, framework, artifact, or test. Apply its conditions and repository exceptions after reading it. Reuse unchanged files already read in the current task; reread changed or unavailable context.

## Rule groups

These summaries name the contracts. Read their complete owners through the [paired language rule map](references/rules/overview.md).

- **SOLID:** Separate reasons to change; extend open families through stable contracts; preserve substitutable behavior; separate optional capabilities; depend inward on abstractions. Do not invent layers to claim compliance.
- **OOP / APIs / Name / Verbs:** Minimize public concepts and classes. Put domain operations on their owning object; prefer methods and classmethods over parallel helper APIs. Keep names short, precise, and native. Use one canonical verb per meaning; distinguish lookup, retrieval, query, search, loading, registration, and lifecycle. Keep stateless transforms as direct functions where idiomatic. Constructors must not hide I/O or activation.
- **Files:** Group by feature and ownership. Use short, intuitive names and cohesive subfolders. Keep one supported package entry; hide internal plumbing. Do not split one concept into many tiny files or use folder scans as extension discovery.
- **Clean:** Use existing infrastructure owners, then direct standard-library or established dependency APIs. Keep trivial local transforms inline. Extract meaningful private boundaries; share stable policy only for real consumers. Validate external input and make errors, async work, cancellation, and resource ownership explicit. TypeScript stays strict and accepts untrusted input as `unknown`.
- **Compat:** Keep one live internal API and update owned callers together. Published contracts follow repository policy. A temporary shim needs a real consumer, test, owner, and removal condition; do not build permanent parallel APIs or speculative migrations.
- **Docstring & Doc:** Document caller semantics with Python Google-style docstrings or TypeScript TSDoc; comments explain non-obvious constraints. Keep canonical docs, examples, and generated artifacts consistent. Preserve conditions and exceptions in controlled prose. Separate current behavior, target, gap, and non-goal.
- **Design / Philosophy:** Keep the user’s mental model small and OOP-centered while decoupling internal responsibilities. Maintain one authority per policy, explicit composition, independent extension contracts, and honest execution. Read [the full philosophy](references/design/philosophy.md).
- **Design / GUI:** Build a quiet, compact workbench with one dominant task, visible consequential state, stable interactions, consistent components, and purposeful motion. Read the complete [GUI rules](references/design/gui/style.md), including themes and stack.

Use the repository's verification commands. Prefix shell commands with `rtk` when available. Preserve unrelated work. Report the outcome, verification, and material gaps.

## Task and operational routes

Complete required reading, then use the requested workflow. These are responsibilities within a task; they do not require separate agents.

| Workflow / role | Responsibility and route |
| --- | --- |
| Design | Define compact component protocols and minimize public classes: [design](references/tasks/design.md), [architect](references/workflows/architect.md). |
| Code | Implement, fix, or refactor: [code](references/tasks/code.md). |
| Review | Inspect correctness, contracts, and regressions: [review](references/tasks/review.md). |
| Manager | Coordinate dependencies, delegated implementation, independent review, and integration through one queue: [manager](references/tasks/manager.md). |
| Doc + translate | Maintain canonical claims: [docs](references/tasks/docs.md); synchronize authorized language pairs: [translate](references/tasks/translate.md). |
| Test-compress | Reduce duplication while preserving behavioral coverage: [tests](references/tasks/tests.md). |
| Skill-edit | Preserve rules, validate, version, and synchronize: [editor](references/workflows/editor.md). |

The [task map](references/workflows/start.md) also routes explanation and environment work.

[Failure recovery](references/failures), [machine assets](assets/REFERENCE.md), and [skill maintenance](references/workflows/editor.md) remain conditional on their tasks. The [generated index](references/index.yaml) supports discovery; an index or directory listing alone does not count as reading the referenced files.
