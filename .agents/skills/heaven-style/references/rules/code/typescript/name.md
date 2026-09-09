---
name: ts-name
description: Read before naming TypeScript symbols.
---

# TypeScript names

## Summary

Use native TypeScript casing and short domain names with one term per concept.

## Names

- `camelCase` for variables, functions, and methods. Treat acronyms as words in owned names: `fromJson` / `toJson`. Preserve required runtime hooks through the aliases defined in [vocabulary](vocab/verbs.md).
- `PascalCase` for classes, interfaces, type aliases, and components.
- `SCREAMING_SNAKE_CASE` only for true process/module constants, not ordinary immutable locals.
- Predicates start with `is`, `has`, or `can`.
- Use one term per concept and short names whose context remains obvious; do not port Python `snake_case` symbol rules into TypeScript.
- Prefer domain vocabulary over suffixes such as `Impl`, `Manager`, `Helper`, `Utils`, or `Data` unless the suffix conveys a real role.

Method vocabulary, class-versus-function choice, collection protocols, fallback semantics, guard clauses, and helper extraction live in [TypeScript API design and vocabulary](api.md). Do not infer them from the Python naming or code-shape rules.

## Pattern and Anti-pattern

- **Pattern:** `isReady` names a predicate; `loadProfile` names a load operation.
- **Anti-pattern:** `profileDataManagerHelper` names an object without revealing its responsibility.

Names expose meaning with native casing.

## Brevity and vocabulary

Frequently used symbols should be terse. Re-examine names with three or more semantic words, just as Python reviews multi-part snake_case names; retain the longer name only when it conveys necessary meaning. Prefer `maxLen` over `maximumAllowedLength` when context is clear. Do not shorten into obscure initials.

Use the [vocabulary](vocab.md) for canonical nouns, paired verbs, and aliases. Keep pj for the package path utility; omit irrelevant KL/UKF lineage terminology and do not require CM_* for a future TypeScript config system.
