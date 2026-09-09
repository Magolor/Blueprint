---
name: doc-sync
description: Write, audit, or synchronize canonical documentation and projections.
task_kind: doc-sync
status: active
---

# Documentation

## Summary

Give readers a short summary, a usable path, and a clear success condition.
Keep consumer instructions first and link or fold exclusive developer detail.
Update the canonical claim before its projections.

## Procedure

For new artifacts, read [authoring rules](write.md) and the selected [template](../../../assets/templates/index.md).

Identify the reader, outcome, canonical source, and evidence owner before drafting. Read repository policy, its docs guide and glossary, the target page, and nearby navigation. Similar filenames do not establish a synchronization relationship.

Use [writing](../../rules/project/docs/write.md) for prose and page structure, and [documentation ownership](../../rules/project/docs.md) when authority or lifecycle changes. A dedicated installed docs-platform skill can supply platform-specific components and checks.

1. Map material claims to code, types, tests, artifacts, or accepted decisions. Label current behavior, target, gap, and non-goal accurately.
2. Write the canonical page in the repository's language; use English when no owner is declared. Start with a short summary. State acceptance or observable success and link references. Preserve native API/comment rules and supported package imports in examples.
3. Execute safe changed commands and examples exactly as documented when the environment permits. State unverified claims and their verification owner.
4. Regenerate declared copies and navigation through their owner. Remove or supersede conflicting pages and repair links in the same change.
5. Run relevant docs, link, snippet, schema, and build checks. Reread for factual completeness, then brevity and navigation.

Use [translation](../translate.md) only when requested or required by an existing atomic-pair policy. Otherwise report translation staleness and out-of-scope sibling projections. Source sync does not authorize deployment. Do not introduce a repository-wide metadata, template, or validation regime through an ordinary page edit.

Report canonical changes, generated outputs, stale projections, verification, and unresolved claims.
