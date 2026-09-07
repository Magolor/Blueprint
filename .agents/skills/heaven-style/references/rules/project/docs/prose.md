---
id: project-docs-prose
title: Controlled technical prose
description: Read for controlled technical prose.
blocking: true
---

# Controlled technical prose

### Controlled technical English

Use a non-certified, ASD-STE100-inspired editorial pass for authored English prose. This is a clarity discipline; it does not claim standards compliance or impose a controlled dictionary.

- Name the actor and action when ambiguity can change behavior. Prefer active voice when the actor matters.
- Use one stable term for each concept. Prefer direct verbs over nominalizations, vague phrasal verbs, and rotating synonyms.
- Use logical quotation punctuation: place periods and commas outside closing quotation marks unless they are part of the quoted material, while otherwise following American English conventions.
- Put one instruction in each sentence. Use a list for several steps or conditions, split long clause chains, and keep each paragraph on one topic.
- Remove unsupported quality adjectives and stacked hedges. Preserve every `must`, `may`, `never`, condition, exception, number, timing constraint, and degree of uncertainty.
- Keep a longer sentence when splitting it would hide a relationship or reduce precision. Professional technical prose must remain natural, respectful, and exact. Do not shorten sentences mechanically.

This page-level prose standard does not expand which code symbols or internal lines require documentation. TypeScript TSDoc/JSDoc, Python docstrings, and inline comments retain their own language and repository rules.

Session responses, durable reports, commit and pull-request titles, pull-request descriptions, and review comments use [Communicate the result](../../../workflows/work.md#communicate-the-result). These communication surfaces do not become new documentation or task authorities.

### Evidence for claims

Map each material claim to its strongest owner. Use public types and package metadata for interface facts, runtime code for behavior, tests for exercised paths, generated artifacts for exhaustive inventories, and accepted decisions for rationale.

Execute new or changed commands, configuration examples, and other operational paths exactly as documented when doing so is safe and the required environment is available. If exact execution is unavailable, state what remains unverified and name the evidence or owner needed to verify it. Verification depth is proportional to risk; do not turn every prose edit into an unrelated integration exercise.
