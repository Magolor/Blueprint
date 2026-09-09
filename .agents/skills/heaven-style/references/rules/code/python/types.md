---
name: types
description: Annotate Python APIs and data shapes using supported language syntax.
---

# Type annotations

## Summary

Use current Python annotation style for new code unless the target repository pins an older runtime.

## Do

- Annotate public parameters and returns.
- Prefer built-in collection generics: `list`, `dict`, `tuple`, and `set`.
- Use `| None` on Python 3.10+.
- Use `TypedDict`, dataclasses, Pydantic models, or project `*Spec` objects when the shape matters.
- Use `Any` only at real integration boundaries.

## Avoid

- `Dict`, `List`, `Tuple`, and `Set` for Python 3.9+ code.
- Weak `dict[str, Any]` types for important internal schemas.
- Compatibility annotations unless the target repo requires them.

## Example

**Anti-pattern:**

```python
from typing import Dict, List, Optional

def rows_by_id(rows: List[Dict[str, str]], name: Optional[str] = None) -> Dict[str, str]:
    ...
```

**Recommended pattern:**

```python
def rows_by_id(rows: list[dict[str, str]], name: str | None = None) -> dict[str, str]:
    ...
```

Prefer built-in collection generics over `Dict`, `List`, `Tuple`, and `Set` in Python 3.9+. Use `|` instead of `Optional` or `Union` in Python 3.10+ for type hints.

## Python 3.9 compatibility

Temporarily keep `Union[...]` instead of `|` when the target project must support Python 3.9:

```python
from typing import Union

def label(value: Union[str, None]) -> str:
    ...
```

Still prefer built-in collections (`dict`, `list`, `tuple`, `set`) over `Dict`, `List`, `Tuple`, and `Set` in Python 3.9+.

## Rules

- Public functions and classes need parameter and return annotations.
- Prefer `Any` only at integration boundaries.
- Use `Self` when the supported Python version provides it. Otherwise, quote the class name.
- Do not add annotations that hide schema weakness. If the shape matters, define a `TypedDict`, dataclass, Pydantic model, or project `*Spec`.
