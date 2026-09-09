---
name: doc-trans
description: Read before translating or synchronizing English–Chinese document pairs.
task_kind: doc-trans
status: active
---

# Bilingual Documentation Translation Task

## Summary

Translate authorized document pairs faithfully while preserving their declared line, code, and metadata alignment.

## Goal

Produce faithful, line-aligned English and Simplified Chinese Markdown/MDX pairs with YAML frontmatter. The repository owns the canonical-language policy, pairing layout, metadata schema, link rules, and documentation platform. Translation remains separate from [documentation writing and sync](docs/README.md). Canonical source changes happen there. Counterparts refresh here when explicitly requested or when repository policy requires atomic pair updates.

## When to use

Load this task when the user asks to:

- translate docs or synchronize a declared Chinese counterpart tree;
- re-translate after canonical source pages changed; or
- replace legacy Chinese stubs with line-aligned translations.

Do **not** use this task during normal canonical-source sync. When a source changes and its counterpart is stale, report the affected paths and recommend a separate translation pass unless repository policy requires atomic pair updates.

## Sources

1. Read the target repository's `AGENTS.md`, documentation guide, navigation owner, pairing/layout contract, and source pages.
2. Load a documentation-platform skill only when that platform is present and the task needs its components or validation commands.
3. Resolve terminology from the first applicable repository glossary. Use Heaven Style's fallback only for English–Chinese translation when the repository has no owner.
4. Read two or three nearby source pages and any existing pairs for voice, metadata, link, and navigation context.
5. Verify behavior facts against code and tests. Do not translate an unsupported claim into apparent authority.

## Voice and fidelity

Within the alignment constraints:

- Translate line by line in source order. Do not rewrite the page as a summary.
- Write like a native technical writer: professional, friendly, and direct. Prefer natural Chinese over a literal calque when the meaning remains exact.
- Reorder phrases within an aligned line when the target language reads more naturally.
- Translate prose, table descriptions, callout bodies, and markup comments outside code fences. Preserve code, commands, flags, environment variables, identifiers, paths, URLs, data keys, and API literals.
- Keep frontmatter keys and machine-owned values such as IDs, slugs, and enum labels unchanged. Translate descriptive values only when the repository schema permits it.
- Report ambiguous or internally inconsistent source prose instead of silently choosing a stronger meaning.

## Workflow

1. Identify the source page set and discover its counterpart mapping from repository policy.
2. Read each source end to end. Record frontmatter fields, sections, code blocks, components, links, and physical line boundaries.
3. Resolve terminology and note machine-owned tokens that must stay unchanged.
4. Translate line by line into the declared counterpart paths while preserving YAML and structure.
5. Verify metadata, total and section line counts, one-to-one structure, code bytes, links, and semantic fidelity.
6. Run the repository's documentation and link checks when available.
7. Report translated and replaced files, pair-verification evidence, terminology source, stale pages outside scope, and any source ambiguity.

## Verification

Verify every pair in scope with the repository's checker when one exists. Otherwise perform a local read-only comparison that proves all of these properties:

- both YAML headers parse and use the same delimiter positions, key order, and machine-owned values;
- total line count and each heading-bounded section line count match;
- headings, blank lines, list markers, tables, components, fences, and explicit breaks occur on corresponding lines;
- fenced code language tags and bodies are byte-identical;
- links preserve the repository's locale-mapping rule and still resolve; and
- a bilingual reviewer spot-checks meaning, terminology, modality, exceptions, and natural language.

Run only the documentation checks declared by the target repository. Pair verification is required. A new checksum, sidecar, or CI gate is not required.

## Handoff from doc-sync

When canonical pages change:

- doc-sync updates the canonical source and navigation owner, then reports stale counterpart paths;
- doc-trans re-translates affected pairs from the latest canonical source; and
- a source line-count change requires the counterpart to be realigned before the pair is current.
For Chinese punctuation, locale form, and glossary selection, read [Chinese conventions](../rules/project/docs/chinese.md).

Before editing a pair, apply the [bilingual file contract](../rules/project/docs/pair.md).
