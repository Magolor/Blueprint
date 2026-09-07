---
id: ts-flow
title: TypeScript flow and helpers
description: Read for TypeScript flow and helpers.
blocking: true
---

# TypeScript flow and helpers

## Language shape and helper cleanliness

- Prefer guard clauses and direct returns over deep nesting.
- Use `??` for missing-value defaults. Do not use `||` when `0`, `false`, or `''` are valid caller values.
- Use optional chaining when absence is expected and stopping the access chain is the intended behavior.
- Use `map`, `filter`, `flatMap`, `some`, `every`, and `find` for one clear collection operation. Prefer a readable `for...of` loop when a long chain, `reduce`, mutation, early exit, async sequencing, or multiple branches would obscure intent.
- Keep a specialized one-liner local. Extract a helper when its name and type contract clarify a meaningful transform, policy, validation, observability, or repeated use.
- Do not create wrapper classes/functions merely to rename a constructor, object spread, property access, or direct platform call.

**Anti-pattern:**

```ts
function getTimeout(options: RunOptions): number {
  return options.timeoutMs || 30_000
}
```

**Recommended pattern:**

```ts
const timeoutMs = options.timeoutMs ?? defaults.timeoutMs
```

If timeout resolution becomes a validated policy shared by several entry points, move that complete policy to the configuration owner. Do not retain the one-line wrapper in that case.
