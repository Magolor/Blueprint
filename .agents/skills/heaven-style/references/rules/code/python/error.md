---
name: error
description: Handle Python validation, exceptions, logging, and contextual failures.
---

# Errors

## Summary

Raise with context. Catch only at defined boundaries such as CLI, HTTP handlers, workers, and integration adapters. Use project logging helpers. Gate verbose output on debug config.

## Principle

For unsupported choices, use the target repository's validated lookup/error helper when it exists; otherwise raise a focused standard or project exception with the invalid value and supported choices.

## Do

- Raise contextual exceptions at the point where invalid state is known.
- Use the repository's supported-value helper when it exists; otherwise validate directly and raise a focused exception.
- Catch exceptions only at boundary layers and preserve cause/context.
- Use logging helpers instead of `print`.
- Keep “not found” distinct from “could not observe”. Translate absence only from the repository's specific absence signal. Transport, permission, parse, and backend failures remain failures.
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
from acme.utils import loads_json


def parse_job(payload: bytes, mode: str) -> dict[str, object]:
    if mode not in MODES:
        choices = ", ".join(sorted(MODES))
        raise ValueError(f"unknown job mode {mode!r}; expected one of: {choices}")
    data = loads_json(payload)
    if not isinstance(data, dict):
        raise TypeError(f"job payload must decode to dict, got {type(data).__name__}")
    return data
```

Validate untrusted boundaries and domain invariants where the code has enough knowledge to produce a useful failure. Do not surround ordinary internal operations with speculative guards. Typed/internal preconditions may remain documented contracts when all callers are owned and verified.

## Guard errors; preserve logical indentation

Guard invalid states with early raise/throw or return before normal work. Indentation expresses logical dependence, not whether a line might throw. Parallel alternatives should stay parallel; do not bury one alternative under a catch solely because it can fail. Native exceptions can propagate. When translation/recovery is necessary, keep the try block to the smallest operation that needs it, then resume ordinary flow outside it.

**Anti-pattern:**

```python
if mode == "json":
    try:
        if not isinstance(payload, str):
            raise TypeError("JSON input must be text")
        entity = Entity.from_json(loads_json(payload))
    except Exception:
        raise ValueError("bad entity")
elif mode == "dict":
    entity = Entity.from_dict(payload)
```

**Recommended pattern:** illustrative package-owned loads_json validates text decoding; entity factories validate the representation.

```python
if mode not in {"json", "dict"}:
    raise ValueError(f"unknown entity format: {mode!r}")
if mode == "json" and not isinstance(payload, str):
    raise TypeError("JSON input must be text")

if mode == "json":
    entity = Entity.from_json(loads_json(payload))
else:
    entity = Entity.from_dict(payload)
```

The two construction alternatives have the same indentation. Validation guards do not swallow decoder, permission, or backend failures. If the boundary must translate a specific decode exception, catch only that exception around decoding, preserve its cause with `raise ... from cause`, and keep subsequent domain work outside the try.
