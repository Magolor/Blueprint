---
name: py-doc-example
description: Read when writing Python function or generator docstrings.
---

# Python docstring examples

## Summary

Use these forms to document ordinary functions, no-value operations, and generators.

## Examples

### Public function

**Recommended pattern:**

```python
def load_profile(path: str, *, strict: bool = True) -> Profile:
    """Load a profile from a JSON file.

    Args:
        path (str): Filesystem path to the profile JSON file.
        strict (bool): Whether to reject unknown fields.

    Returns:
        Profile: Loaded profile object.

    Raises:
        ProfileError: If the file cannot be decoded or validated.
    """
```

### No arguments and no return value

**Recommended pattern:**

```python
def reset_cache() -> None:
    """Clear cached registry state.

    Args:
        None.

    Returns:
        None: This function does not return a value.
    """
```

### Generator

**Recommended pattern:**

```python
from collections.abc import Iterator


def iter_rows(limit: int | None = None) -> Iterator[Row]:
    """Yield rows from the active result set.

    Args:
        limit (int | None): Maximum number of rows to yield.

    Yields:
        Row: Next row in query order.
    """
```
