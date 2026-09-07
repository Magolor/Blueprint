---
id: ts-name
title: TypeScript names
description: Read for TypeScript names.
blocking: true
---

# TypeScript names

## Names

- `camelCase` for variables, functions, and methods.
- `PascalCase` for classes, interfaces, type aliases, and components.
- `SCREAMING_SNAKE_CASE` only for true process/module constants, not ordinary immutable locals.
- Predicates start with `is`, `has`, or `can`.
- Use one term per concept and short names whose context remains obvious; do not port Python `snake_case` symbol rules into TypeScript.
- Prefer domain vocabulary over suffixes such as `Impl`, `Manager`, `Helper`, `Utils`, or `Data` unless the suffix conveys a real role.

Method vocabulary, class-versus-function choice, collection protocols, fallback semantics, guard clauses, and helper extraction live in [TypeScript API design and vocabulary](api.md). Do not infer them from the Python naming or code-shape rules.
