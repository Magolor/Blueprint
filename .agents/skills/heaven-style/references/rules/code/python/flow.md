---
name: py
description: Simplify Python control flow and preserve fallback semantics.
---

# Python shape

## Summary

Prefer comprehensions, guard clauses, unpacking, and direct returns when they keep behavior readable. Do not compress regex bodies, SQL, prompts, long error messages, or branching that needs operator context.

## Compact logical shape

Prefer compact idiomatic code as the starting point: comprehensions/collection operations, ternaries, unpacking, direct returns, and guard clauses. Accept a small readability tradeoff for a materially shorter obvious operation, but do not compress complex branching, error context, SQL, regexes, or prompts into opaque expressions. Indentation should reflect logical dependence: parallel branches stay at the same level. Guard invalid cases first, then keep the ordinary branches parallel. See [errors](error.md) and [clean](clean.md).

## Principle

For tiny helper functions that only hide a one-line transform, also apply [clean](clean.md).

## Do

- Use comprehensions for simple filter/map operations.
- Use guard clauses for invalid or empty paths.
- Keep fallback semantics explicit.
- Prefer direct returns for simple expressions.

## Avoid

- Compressing multi-branch business logic into dense expressions.
- `or` defaults when falsy caller values are valid.
- Helpers that force readers to navigate elsewhere without providing real reuse.

## Example

**Anti-pattern:**

```python
out = []
for item in items:
    if item.get("active"):
        out.append(item["name"].lower())
```

**Recommended pattern:**

```python
out = [item["name"].lower() for item in items if item.get("active", False)]
```

Use explicit fallback semantics. Native `dict.get` takes the fallback positionally. Config helpers use `default=`.
