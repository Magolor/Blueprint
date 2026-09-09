---
name: heaven-style
description: Use when coding, designing, reviewing, or writing documentation in TypeScript or Python projects.
metadata:
  version: 0.2.0-alpha.1
---

# Heaven Style

## Summary

Use shared code, design, GUI, and authoring conventions. Apply repository policy, runtime contracts, and compatibility promises first. Preserve the repository's language and toolchain. Default an undecided new project to TypeScript.

## Quick Read

At each new request, select or retain the [agent role](references/roles/README.md), using Default when none fits. Apply [intent and judgment](references/rules/project/work.md#interpret-intent-and-exercise-judgment): preserve the goal and explicit constraints, assess suggested approaches, and retain decision authority. Follow the role, then a fitting [workflow](references/workflows/README.md) and its [tasks](references/tasks/README.md). A role can span a session or one assignment; workflows sequence distinct tasks.

This entry is a summary, not a substitute for the full rules. Complete the [reading procedure](references/rules/project/read.md) before implementation, diagnosis, review, explanation, tests, or code-bearing examples. Small changes have the same reading prerequisite.

- **Code:** Read every Markdown file recursively in the applicable [TypeScript](references/rules/code/typescript) or [Python](references/rules/code/python) rule tree, plus all [shared project rules](references/rules/project) and [design philosophy](references/design/philosophy/README.md). Include nested examples, formats, lifecycle, package, and configuration pages. Read both language trees for work involving both languages.
- **Architecture:** Complete code reading for the target language, then read [architecture checks](references/tasks/design/README.md), [the design guide](references/tasks/design/guide.md), every [design manual](references/tasks/design), and all [code-design comparisons](references/examples/code). Also inspect the repository’s architecture and decision owners before proposing structure.
- **GUI:** Read every file in [GUI design](references/design/gui), including stack, interaction, review, and all six palette files. GUI code and architecture work also require the corresponding code and architecture reading.
- **Authoring:** Before creating or substantively editing PRs, issues, comments, docs, or reports, read [authoring](references/tasks/docs/write.md) for explicit Summary sections and searchable YAML, then the applicable [template](assets/templates/index.md). Standalone docs also require the [documentation task](references/tasks/docs/README.md) and all [documentation rules](references/rules/project/docs.md), including [nested pages](references/rules/project/docs). Code examples and architecture claims add their respective reading prerequisites. Load only applicable template details. Routine coding does not require the template catalog.

Reading a rule does not require adding an irrelevant feature, framework, artifact, or test. Apply its conditions and repository exceptions after reading it. Reuse unchanged files already read in the current task; reread changed or unavailable context.

For prose and chat responses, read [language and responses](references/rules/project/language.md). Lead with the answer or outcome, use direct language, and preserve material conditions and evidence.

### Core rules

These summaries name the contracts. Read their complete owners through the [paired language rule map](references/rules/overview.md).

- **SOLID:** Separate reasons to change; extend open families through stable contracts; preserve substitutable behavior; separate optional capabilities; depend inward on abstractions. Read the five dedicated principle pages for the applicable language, including their patterns and anti-patterns. Keep public object use simple while separating internal responsibilities.
- **OOP / APIs / Names / Vocabulary:** Minimize public concepts and classes. Put domain operations on their owning object; prefer methods and classmethods over parallel helper APIs. Keep names short, precise, and native. Use aligned conversion verbs (`fromJson`/`toJson` in TypeScript, with equivalent JSON hook aliases); use paired verbs, explicit domain nouns, and common aliases consistently across SDK and CLI; prefer single/multiple input on the same operation. Prefer member methods as much as possible, including pure domain construction/conversion; reserve direct functions for independent utilities and algorithms. Constructors must not hide I/O or activation.
- **Imports / Format:** Maximize stable dependency prefixes and show first-party relationships early. Preserve TypeScript import/runtime controls. Python must pass Black + Flake8 through repository commands; TypeScript retains its declared toolchain.
- **Files:** Group by feature and ownership. Use short, intuitive names and cohesive subfolders. Keep one supported package entry; hide internal plumbing. Do not split one concept into many tiny files or use folder scans as extension discovery.
- **Clean / Utils:** Read the dedicated clean and utility rules in each language catalog. Prefer package-owned utilities and their existing re-exports, then direct standard-library or established dependency APIs. Keep one-use transforms inline; put needed generic helpers in shared utils. Extract substantial private boundaries. Validate external input and make errors, async work, cancellation, and resource ownership explicit. TypeScript stays strict and accepts untrusted input as `unknown`.
- **Config / SQL:** Configs are KV dictionaries; externalize changeable defaults and resolve omission at the owning boundary. Prefer existing wrapped database operations, generic wrapped APIs, and ORM before packaged external SQL; keep values bound.
- **Compat:** Keep one live internal API and update owned callers together. Published contracts follow repository policy. A temporary shim needs a real consumer, test, owner, and removal condition; do not build permanent parallel APIs or speculative migrations.
- **Docstring & Doc:** Require Python Google-style short descriptions with full Args/Returns/Yields structure. Use short, structured TSDoc in TypeScript; comments explain non-obvious constraints. Keep canonical docs, examples, and generated artifacts consistent. Preserve conditions and exceptions in controlled prose. Separate current behavior, target, gap, and non-goal.
- **Design / Philosophy:** Keep the user’s mental model small and OOP-centered while decoupling internal responsibilities. Maintain one authority per policy, explicit composition, independent extension contracts, and honest execution. Read [the full philosophy](references/design/philosophy/README.md).
- **Design / GUI:** Build a quiet, compact workbench with one dominant task, visible consequential state, stable interactions, consistent components, and purposeful motion. Read the complete [GUI rules](references/design/gui/style.md), including themes and stack.

Use the repository's verification commands. Prefix shell commands with `rtk` when available. Preserve unrelated work. Report the outcome, verification, and material gaps.

## Roles, workflows, and tasks

- [Roles](references/roles/README.md): Default, Manager, Worker, and Teacher define the agent’s continuing responsibility.
- [Workflows](references/workflows/README.md): Feature, Bugfix, Enhancement, GUI, Document, Self-edit, Extensive Review, and Refactor sequence tasks with acceptance and stopping conditions.
- [Tasks](references/tasks/README.md): bounded procedures for code, design, review, triage, fixes, composing, proofreading, explanation, translation, test compression, synchronization, coordination, skill editing, and environment work. Detailed manuals live under their task.

Use the [reference guide](references/README.md) for folder purposes. A simple request can use a task directly when no workflow fits. Role selection changes neither required reading nor existing authority.

## Notes

- Missing or stale machine facts: follow the [setup owner and recovery guidance](assets/instance/README.md).
- Recurring operational blockers: use the relevant [failure record](references/failures); do not generalize a workaround beyond its conditions.

## References

[Failure recovery](references/failures), [machine assets](assets/REFERENCE.md), and [skill maintenance](references/tasks/edit/README.md) remain conditional on their tasks. The [generated index](references/index.yaml) supports discovery; an index or directory listing alone does not count as reading the referenced files.
