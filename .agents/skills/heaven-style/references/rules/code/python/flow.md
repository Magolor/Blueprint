---
id: py
title: Python shape
blocking: true
description: Simplify Python control flow and preserve fallback semantics.
---

# Python shape

## Core rule

Prefer comprehensions, guard clauses, unpacking, and direct returns when they keep behavior readable. Do not compress regex bodies, SQL, prompts, long error messages, or branching that needs operator context.

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
