---
id: doc-trans
task_kind: doc-trans
status: active
enabled: true
order: 32
keywords: [translate docs, bilingual docs, YAML frontmatter, zh docs, chinese translation, batch translate, re-translate, doc translation, line-aligned translation]
triggers: [translate, translation, bilingual docs, zh doc, chinese docs, batch translate, re-translate, line-by-line translation, doc-trans]
description: Use when translating or re-translating Markdown or MDX into YAML-frontmatter, line-aligned English and Simplified Chinese pairs in the repository's declared layout.
related_rules: [overview, docs, test]
---

# Bilingual Documentation Translation Task

## Goal

Produce faithful, line-aligned English and Simplified Chinese Markdown/MDX pairs with YAML frontmatter. The repository owns the canonical-language policy, pairing layout, metadata schema, link rules, and documentation platform. Translation remains separate from [documentation writing and sync](doc-sync.md): canonical source changes happen there; counterparts refresh here when explicitly requested or when repository policy requires atomic pair updates.

## When to use

Load this task when the user asks to:

- translate docs or synchronize a declared Chinese counterpart tree;
- re-translate after canonical source pages changed; or
- replace legacy Chinese stubs with line-aligned translations.

Do **not** use this task during normal canonical-source sync. When a source changes and its counterpart is stale, report the affected paths and recommend a separate translation pass unless repository policy requires atomic pair updates.

## Sources

1. Read the target repository's `AGENTS.md`, documentation guide, navigation owner, pairing/layout contract, and source pages.
2. Load a documentation-platform skill only when that platform is present and the task needs its components or validation commands.
3. Resolve terminology from the first applicable repository glossary; use Heaven Style's fallback only for English–Chinese translation when the repository has no owner.
4. Read two or three nearby source pages and any existing pairs for voice, metadata, link, and navigation context.
5. Verify behavior facts against code and tests. Do not translate an unsupported claim into apparent authority.

## Hard constraints

These are non-negotiable for an authored bilingual pair unless its format owner declares a narrower exception:

1. **YAML frontmatter:** both pages start with parseable YAML. Follow the repository's field schema; when none exists, use only a concise `description` that states what the page covers and when to read it unless the user approves more fields. This page-level fallback is not a corpus schema. Keep delimiters, key order, and key names aligned. Localize only values the schema treats as prose.
2. **Total line parity:** both files have exactly the same number of physical lines.
3. **Section line parity:** line counts match within every heading-bounded section and subsection, not only at file level.
4. **One-to-one line map:** source line *N* maps to counterpart line *N*, including blank lines, frontmatter fields, component tags, code fences, table rows, list markers, and explicit break elements.
5. **Code parity:** every code fence keeps the same language tag, boundaries, and executable content byte-for-byte. Do not translate code comments inside a fence when doing so would violate executable-content parity.
6. **Structure parity:** preserve heading levels, component names, anchors, list/table shape, and navigation structure. Translate link text, but change a link target only through the repository's declared locale-mapping rule.
7. **Semantic parity:** each aligned prose line conveys the same proposition, modality, exception, number, timing, and uncertainty. Structural equality alone does not prove a faithful translation.

Do not add content hashes, checksums, pairing sidecars, or CI metadata unless the target repository already owns and consumes them.

## Voice and fidelity

Within the alignment constraints:

- Translate line by line in source order; do not rewrite the page as a summary.
- Write like a native technical writer: professional, friendly, and direct. Prefer natural Chinese over a literal calque when the meaning remains exact.
- Reorder phrases within an aligned line when the target language reads more naturally.
- Translate prose, table descriptions, callout bodies, and markup comments outside code fences. Preserve code, commands, flags, environment variables, identifiers, paths, URLs, data keys, and API literals.
- Keep frontmatter keys and machine-owned values such as IDs, slugs, and enum labels unchanged. Translate descriptive values only when the repository schema permits it.
- Report ambiguous or internally inconsistent source prose instead of silently choosing a stronger meaning.

## File policy

- Follow the repository's declared pairing layout, including sibling files such as `guide.md` and `guide.zh.md` or a mirrored locale tree. When no layout owner exists, mirror source paths under `zh/`.
- Preserve the repository's canonical-language model. Line alignment does not make both files independent sources of truth unless repository policy says so.
- When the user requests a batch re-translation, fully replace stale counterparts in that scope instead of patching them over outdated source structure.
- Update the repository's navigation owner only when the translation scope includes navigation labels or new counterpart pages.
- Do not move source pages unless the user explicitly requests a restructure.

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

Run only the documentation checks declared by the target repository. Pair verification is required; a new checksum, sidecar, or CI gate is not.

## Simplified Chinese conventions

Repository terminology and punctuation rules win. When no local convention exists:

- use corner brackets 「」 for quoted phrases in Chinese prose;
- on first mention, in headings, emphasis, or beside a code identifier, append the English original when it helps recognition, for example 入口 (Gateway); and
- use 智能体 or **Agent** consistently according to the product glossary.

## Translation terminology

Read and apply the first available glossary source:

1. the repository's documentation or localization glossary;
2. the repository's published glossary page; or
3. the [Heaven Style English–Chinese fallback](../../assets/default-glossary.md).

Keep identifiers in the spelling readers see in code. Report which glossary source you used.

## Handoff from doc-sync

When canonical pages change:

- doc-sync updates the canonical source and navigation owner, then reports stale counterpart paths;
- doc-trans re-translates affected pairs from the latest canonical source; and
- a source line-count change requires the counterpart to be realigned before the pair is current.
