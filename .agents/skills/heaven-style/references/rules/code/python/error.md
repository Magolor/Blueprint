---
id: error
title: Errors
enabled: true
blocking: true
order: 60
category: code-quality
keywords: [try except, logging, raise, print debug, raise_mismatch, unsupported value, swallowed error]
description: Use when validating supported values, handling exceptions, logging failures, catching broadly, or returning fallbacks.
---

# Errors

## Core rule

Raise with context. Catch only at defined boundaries such as CLI, HTTP handlers, workers, and integration adapters. Use project logging helpers; gate verbose output on debug config.

For unsupported choices, use the target repository's validated lookup/error helper when it exists; otherwise raise a focused standard or project exception with the invalid value and supported choices. `raise_mismatch` is a conditional HeavenBase-lineage helper, not a generic Python requirement.

## Apply when

- Code validates modes, providers, backend names, enum-like choices, or user input.
- Code catches exceptions, logs failures, returns fallbacks, or exits.
- Code handles decoded external payloads.

## Do

- Raise contextual exceptions at the point where invalid state is known.
- Use the repository's supported-value helper when it exists; otherwise validate directly and raise a focused exception.
- Catch exceptions only at boundary layers and preserve cause/context.
- Use logging helpers instead of `print`.
- Keep “not found” distinct from “could not observe.” Translate absence only from the repository's specific absence signal; transport, permission, parse, and backend failures remain failures.
- Stop an ordered mutation pipeline after the first failed phase. Preserve caller-visible mutation order unless the adapter proves failure atomicity for the entire reordered transaction.
- Roll back by ownership or compare-and-swap identity when concurrent work can replace the state. Cleanup from an older failed operation must not delete or overwrite a newer value.

## Avoid

- Bare `except:`.
- Broad `except Exception` around one-liners.
- `assert` for runtime validation.
- Swallowed errors and silent `{}`/`None` fallbacks.
- Broad fallback that turns observation failure into absence, unsupported, or unknown.
- Continuing later writes after an earlier write failed, or reordering writes around a lock without a full transactional guarantee.
- `print` in library code.

## Example

**Anti-pattern:**

```python
def parse_job(payload: bytes, mode: str) -> dict[str, object]:
    try:
        if mode not in MODES:
            raise ValueError(f"unknown mode: {mode}")
        return loads_json(payload)
    except Exception:
        print("bad job")
        return {}
```

**Recommended pattern:**

```python
import json


def parse_job(payload: bytes, mode: str) -> dict[str, object]:
    if mode not in MODES:
        choices = ", ".join(sorted(MODES))
        raise ValueError(f"unknown job mode {mode!r}; expected one of: {choices}")
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise TypeError(f"job payload must decode to dict, got {type(data).__name__}")
    return data
```

Validate untrusted boundaries and domain invariants where the code has enough knowledge to produce a useful failure. Do not surround ordinary internal operations with speculative guards; typed/internal preconditions may remain documented contracts when all callers are owned and verified.

## Related rules

Also apply [util.md](util.md) for logging/serialization helpers and [types.md](types.md) for decoded payload shape.
