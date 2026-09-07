---
id: compat
title: Compatibility shims
blocking: true
description: Change Python names, schemas, or compatibility promises.
---

# Compatibility shims

## Core rule

Prefer one live API version. Rename freely. Update call sites in the same change.

## Do

- Update call sites to the cleaner API in the same change.
- Keep one config schema. Update defaults/bootstrap when keys change.
- Put one-shot migrations under scripts or migrations.
- Document explicit compatibility waivers when the user requires a layer.

## Avoid

- Permanent `warnings.warn` shims.
- Parallel `v1` / `v2` modules.
- Old imports/dependencies that duplicate the new API.
- Permanent library branches for one-time migrations.

## Example

**Anti-pattern:**

```python
def old_api(value: str) -> str:
    warnings.warn("old_api is deprecated; use new_api", DeprecationWarning)
    return new_api(value)

def new_api(value: str) -> str:
    ...

def migrate_old_api_to_new_api():
    ...
```

**Recommended pattern:**

```python
def api(value: str) -> str:
    ...
```

Unless explicitly instructed, never consider migration from an older codebase or data source during coding, refactoring, or reviews. Keep only the cleanest, latest API. Do not even notify the user that the old API exists.

This rule applies while the package is under development. Waive it for a stable-version project or when the user explicitly requests compatibility.
