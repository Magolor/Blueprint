---
name: project-docs-write
description: Read before writing or restructuring Markdown or MDX documentation.
---

# Write documentation

## Summary

Start every authored document with a short summary. Show the reader how to
use the subject before exposing developer-only detail. State success criteria
and link the authoritative references. Use controlled technical English.

## Authored-document standard

Apply this section to human-facing Markdown or MDX. The repository's `AGENTS.md`, parser, documentation platform, established page schema, and generated-file owner take precedence. This section does not replace format-specific contracts for an ADR, postmortem, changelog, API reference, generated catalog, task, plan, or development log.

Do not retrofit an existing corpus solely to make every file use one skeleton. Use Heaven Style’s [artifact templates](../../../../assets/templates/index.md) as the default structure for new artifacts, adapting them to existing repository formats. They do not impose a repository-wide taxonomy, locale paths, website manifests, translation sidecars, content hashes, hard word budgets, or CI commands.

Discuss and obtain approval before introducing a repository-wide metadata schema, document taxonomy or template set, mass migration or hierarchy move, canonical-language or pair-layout change, mandatory same-pass translation policy, checksum/sidecar/CI regime, or broader API-doc, docstring, or inline-comment coverage. A focused page edit may follow an already approved owner without reopening that decision.

For a new or substantially reworked page:

- Identify the primary reader, their starting state, the outcome they need, the likely failure and recovery path, and the next useful level of detail.
- Follow the repository's frontmatter schema. Otherwise recommend `name` and a scenario-focused `description`, using [searchable YAML](../../../tasks/docs/write.md#searchable-yaml). An authored bilingual page still requires YAML unless its format owner forbids it. Preserve stable IDs and consumed metadata.
- Start the body with an explicit `## Summary` after the header, title, and language switcher. Use the natural equivalent in other languages. Existing generated or parser-owned formats follow their owner. The summary and search description serve different purposes.
- Progress from user outcome and shortest safe path to advanced operation and then concept-level developer detail. Explain ownership, lifecycle, failure, security, and performance only to the depth the target reader needs; link authoritative code, types, schemas, or generated catalogs for exact inventories.
- Open a dense section with a short orientation before tables, code, or lower-level headings. Keep one obvious next action. Make success, limitations, and recovery discoverable.
- Keep current behavior, accepted target, known gap, migration guidance, history, and non-goal in their declared owners and label them accurately. Do not erase compatibility or migration facts merely to make prose read as current-state-only.

Use [controlled prose and claim verification](prose.md) for authored English. Preserve modality, exceptions, quantities, and uncertainty.

## Create the summary

Use [authoring](../../../tasks/docs/write.md#explain-the-readers-outcome) for the
summary's reader and voice; [the opening Summary rule](../../../tasks/docs/write.md#required-opening-summary) owns its section and soft length guidance. Keep capabilities and
consequential conditions visible. Move supporting implementation detail to its
owner without deleting facts or making mandatory reading optional. Review
accuracy before brevity; no summary or translation-length validator is required.

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

For corrections, follow [whole-document integration](edit.md). Keep the page centered on its reader’s task; put decision history in its historical owner.

## Make abstract rules concrete

For an abstract rule, recommend **one to four Pattern/Anti-pattern cases** that show its practical boundary. This is a soft range, not a quota. Use short pseudocode or concrete examples of prose, workflows, or interfaces. Label what to do and what to avoid; add one brief explanation of the decisive difference.

Compare the same task and conditions. Include an important exception when it prevents overapplication. Mark illustrative APIs as pseudocode, and avoid invented product claims. Reuse an existing example rather than repeat it across pages. Skip examples when the rule is already concrete or the case adds no clarity. No case-count validator is needed.

For example, when documenting an internal fix:

- **Pattern:** “Quoted spaces split one CLI argument into several. The argument parser now preserves quoted groups.”
- **Anti-pattern:** “Fixed `parseInput`.”

The pattern locates the failure and outcome before exposing an internal symbol.

## Acceptance and references

Every authored page states how the reader can recognize success. Use explicit
acceptance criteria for plans and assignments. A design explains the intended
outcome and architectural reasoning without becoming an execution checklist. For a guide, give an
observable result or check. For a descriptive reference, state the decision or
lookup it supports. Do not add an empty checklist to satisfy a template.

Link prerequisite material and the owners of important claims near their use.
Add a compact references section when it helps further work. Keep detailed
catalogs one link away instead of repeating them. A page is ready when a new
reader can identify its purpose, use path, success condition, and next source.

Use the [planning manual](../../../tasks/design/plan.md) for a short proposal
that expands after confirmation. These rules apply to new or revised pages;
they do not authorize an unrelated corpus-wide rewrite.
