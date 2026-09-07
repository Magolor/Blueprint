---
id: project-docs-write
title: Write documentation
description: Write audience-focused Markdown or MDX under repository policy.
blocking: true
---

# Write documentation

## Summary

Start every authored document with a short summary. Show the reader how to
use the subject before exposing developer-only detail. State success criteria
and link the authoritative references. Use controlled technical English.

## Authored-document standard

Apply this section to human-facing Markdown or MDX. The repository's `AGENTS.md`, parser, documentation platform, established page schema, and generated-file owner take precedence. This section does not replace format-specific contracts for an ADR, postmortem, changelog, API reference, generated catalog, task, plan, or development log.

Do not retrofit an existing corpus solely to make every file use one skeleton. Heaven Style does not define universal document kinds, package templates, fixed section names, locale paths, website manifests, translation sidecars, content hashes, word budgets, or CI commands. Add those only when the target repository owns and consumes them.

Discuss and obtain approval before introducing a repository-wide metadata schema, document taxonomy or template set, mass migration or hierarchy move, canonical-language or pair-layout change, mandatory same-pass translation policy, checksum/sidecar/CI regime, or broader API-doc, docstring, or inline-comment coverage. A focused page edit may follow an already approved owner without reopening that decision.

For a new or substantially reworked page:

- Identify the primary reader, their starting state, the outcome they need, the likely failure and recovery path, and the next useful level of detail.
- Follow the repository's YAML frontmatter schema. An authored bilingual page must have YAML frontmatter unless its format owner explicitly forbids it. When no schema exists, use a concise `description` that states what the page covers and when to read it; treat this as a page-level fallback, not a new corpus schema. Keep keys stable and do not copy volatile inventories into metadata.
- After the title and any required metadata or language switcher, give a short summary in one paragraph. State what the reader can do, when to use it, and the main boundary. Use a Summary heading where the format permits. Tiny pages can use a plain opening paragraph; generated fragments and parser-owned formats follow their owner.
- Progress from user outcome and shortest safe path to advanced operation and then concept-level developer detail. Explain ownership, lifecycle, failure, security, and performance only to the depth the target reader needs; link authoritative code, types, schemas, or generated catalogs for exact inventories.
- Open a dense section with a short orientation before tables, code, or lower-level headings. Keep one obvious next action. Make success, limitations, and recovery discoverable.
- Keep current behavior, accepted target, known gap, migration guidance, history, and non-goal in their declared owners and label them accurately. Do not erase compatibility or migration facts merely to make prose read as current-state-only.

Use [controlled prose and claim verification](prose.md) for authored English. Preserve modality, exceptions, quantities, and uncertainty.

## User and developer paths

Assume the consumer path comes first. Show required inputs, the shortest safe
use, observable success, and likely recovery. Keep information needed for safe
use visible, including limits and failures.

Put exclusive developer material after that path, in a clearly named
`<details>` section when the renderer supports it, or in a linked reference.
Keep headings and links discoverable. Use folds for design concepts, ownership,
and data flow; link source for exact members and implementation details.

A developer guide, component protocol, or manager plan serves developers as
its primary users. Start with what that reader can do. Do not invent an
unrelated end-user section or hide their required instructions in a fold.

## Acceptance and references

Every authored page states how the reader can recognize success. Use explicit
acceptance criteria for plans, designs, and assignments. For a guide, give an
observable result or check. For a descriptive reference, state the decision or
lookup it supports. Do not add an empty checklist to satisfy a template.

Link prerequisite material and the owners of important claims near their use.
Add a compact references section when it helps further work. Keep detailed
catalogs one link away instead of repeating them. A page is ready when a new
reader can identify its purpose, use path, success condition, and next source.

Use the [plan workflow](../../../workflows/design/plan.md) for a short proposal
that expands after confirmation. These rules apply to new or revised pages;
they do not authorize an unrelated corpus-wide rewrite.
