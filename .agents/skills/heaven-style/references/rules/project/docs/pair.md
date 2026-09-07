---
id: project-docs-pair
title: Bilingual file contract
description: Read for bilingual file contract.
---

# Bilingual file contract

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

## File policy

- Follow the repository's declared pairing layout, including sibling files such as `guide.md` and `guide.zh.md` or a mirrored locale tree. When no layout owner exists, mirror source paths under `zh/`.
- Preserve the repository's canonical-language model. Line alignment does not make both files independent sources of truth unless repository policy says so.
- When the user requests a batch re-translation, fully replace stale counterparts in that scope instead of patching them over outdated source structure.
- Update the repository's navigation owner only when the translation scope includes navigation labels or new counterpart pages.
- Do not move source pages unless the user explicitly requests a restructure.
