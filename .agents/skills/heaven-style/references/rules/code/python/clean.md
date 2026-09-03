---
id: clean
title: Helper cleanliness
enabled: true
blocking: true
order: 310
category: code-quality
keywords: [helper function, temporary helper, wrapper, small function, code cleanliness, abstraction]
description: Use when adding Python helper functions, wrappers, temporary transforms, adapters, or deciding inline logic versus shared utilities.
---

# Helper cleanliness

## Core rule

Do not introduce small temporary helpers that only rename a one-line transform or hide a tiny local block. Every helper must justify its abstraction cost through ownership, repeated use, policy, validation, observability, or a meaningful transformation boundary.

## Apply when

- Code adds private helpers, wrappers, adapter functions, one-line transforms, or local utility modules.
- Behavior could remain inline, use a direct standard-library/dependency API, or move to the repository's declared shared owner.

## Do

- Use the target repository's existing shared utility when it clearly owns the behavior.
- Otherwise prefer a direct standard-library or established dependency call over a speculative wrapper.
- Keep specialized one-liners inline where they are used.
- Use a private helper for a specialized larger block when a name, type contract, and short docstring clarify the boundary.
- Propose a shared utility only when multiple real consumers need the same stable policy.

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
5. Repeated stable policy across consumers: promote it to the shared owner.

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

## Related rules

Also apply [util.md](util.md) for shared-helper ownership, [name.md](name.md) for helper names, [files.md](files.md) for helper placement, and [py.md](py.md) for compact inline expressions.
