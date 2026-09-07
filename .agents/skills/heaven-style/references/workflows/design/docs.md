---
id: workflow-design-docs
title: Documentation design
description: Read for documentation design.
---

# Documentation design

## Doc organization and cleanup

When the task includes docs hygiene:

1. **Consolidate** — keep one canonical page per topic. Merge duplicates. Link to other owners instead of copying prose.
2. **Retire** — promote surviving truth. Then delete or clearly supersede stale pages. Git preserves execution history.
3. **Relabel** — separate **current**, **target**, **gap**, and **non-goal**; never describe planned behavior as current.
4. **Anchor** — ensure the engineering entry point names user docs, canonical tasks, the development log, scratch policy, durable references, and the mental model.
5. **Defer translation** — route line-aligned bilingual work to [translate](../../tasks/translate.md); architect output stays in the repository's canonical language unless the user requests translation.

Deliverable: a **docs change list** with file path, audience/surface, action (`keep`, `merge`, `rewrite`, `promote`, `retire`, `create`), owner task, expiry when temporary, and verification.
