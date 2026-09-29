---
name: project-docs-prose
description: Read before checking technical prose or factual claims.
---

# Controlled technical prose

## Summary

Write controlled, natural technical prose while preserving conditions and evidence strength.

## Language

Use the shared [language and response rules](../language.md) for controlled technical prose. This page does not expand which code symbols or internal lines require documentation. TypeScript TSDoc/JSDoc, Python docstrings, and inline comments retain their own language and repository rules.

## Evidence for claims

Map each material claim to its strongest owner. Use public types and package metadata for interface facts, runtime code for behavior, tests for exercised paths, generated artifacts for exhaustive inventories, and accepted decisions for rationale.

Execute new or changed commands, configuration examples, and other operational paths exactly as documented when doing so is safe and the required environment is available. If exact execution is unavailable, state what remains unverified and name the evidence or owner needed to verify it. Verification depth is proportional to risk; do not turn every prose edit into an unrelated integration exercise.

## Pattern and Anti-pattern

- **Pattern:** “If the cache is stale, reload it before reading.”
- **Anti-pattern:** “Always reload the cache.” when the source condition is staleness.

Brevity must not remove a condition or strengthen a requirement.
