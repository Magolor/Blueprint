---
name: clean
description: Choose inline logic, private helpers, or shared Python utilities.
---

# Helper cleanliness

## Summary

Do not introduce small temporary helpers that only rename a one-line transform or hide a small local block. Every helper must justify its abstraction cost through ownership, repeated use, policy, validation, observability, or a meaningful transformation boundary.

## Do

- Use the target repository's existing shared utility first, including convenience contracts such as `pj`. Follow package style even when the standard library offers an equivalent operation.
- Otherwise prefer a direct standard-library or established dependency call over a speculative wrapper.
- Keep specialized one-liners inline where they are used.
- Use a private helper for a specialized larger block when its name, type contract, and short docstring clarify the boundary.
- When a needed small helper has a generic contract, add it to the package-wide utility owner or the narrowest subgroup shared by related modules. A second caller is not required; the current need and reusable contract justify placement.

## Avoid

- Helpers that only rename a comprehension, constructor, or function call.
- Local utility modules full of generic wrappers.
- Adding a platform dependency solely to obtain a convenience helper.
- Docstrings that merely restate trivial helper bodies.

Use this decision order:

1. Repository-owned shared behavior: use the declared owner.
2. Direct standard-library/dependency behavior: call it directly.
3. Specialized one-liner or small local block: keep it inline.
4. Specialized larger block: use one focused private helper.
5. Needed generic helper: add it directly to the package or subgroup shared utility owner, even for its first consumer. Do not park it in a single feature module.

## Example

**Anti-pattern:**

```python
def _convert_to_lists(rows: list[tuple[str, int]]) -> list[list[object]]:
    return [list(row) for row in rows]


def _flatten(rows: list[list[object]]) -> list[object]:
    return [item for row in rows for item in row]
```

**Recommended pattern:**

```python
from itertools import chain


payload = [list(row) for row in rows]
flattened_payload = list(chain.from_iterable(payload))
```

When the target repository already owns a shared flattening contract, use that contract instead. Do not add a platform dependency merely for this operation.
