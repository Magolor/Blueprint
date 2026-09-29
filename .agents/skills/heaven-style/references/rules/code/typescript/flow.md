---
name: ts-flow
description: Read before simplifying TypeScript flow or extracting helpers.
---

# TypeScript flow and helpers

## Summary

Keep control flow direct and preserve valid falsy values. Extract helpers only for meaningful boundaries.

## Compact logical shape

Prefer compact idiomatic code as the starting point: comprehensions/collection operations, ternaries, unpacking, direct returns, and guard clauses. Accept a small readability tradeoff for a materially shorter obvious operation, but do not compress complex branching, error context, SQL, regexes, or prompts into opaque expressions. Indentation should reflect logical dependence: parallel branches stay at the same level. Guard invalid cases first, then keep the ordinary branches parallel. See [errors](error.md) and [clean](clean.md).

## Language shape and helper cleanliness

- Prefer guard clauses and direct returns over deep nesting.
- Use `??` only when both `null` and `undefined` mean omission. Use `=== undefined` when `null` is meaningful. Do not use `||` when `0`, `false`, or `''` are valid caller values.
- Use optional chaining when absence is expected and stopping the access chain is the intended behavior.
- Use `map`, `filter`, `flatMap`, `some`, `every`, and `find` for one clear collection operation. Prefer a readable `for...of` loop when a long chain, `reduce`, mutation, early exit, async sequencing, or multiple branches would obscure intent.
- Keep specialized one-liners and small one-use blocks inline; do not turn them into module-local helpers. Reuse package-owned utilities first. Put a needed generic helper in package-wide or subgroup shared utils, even for its first consumer. Larger feature-specific boundaries may use focused private functions.
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
