---
id: compat
title: Compatibility shims
enabled: true
blocking: true
order: 340
category: code-quality
keywords: [deprecated, shim, v1 v2, warnings.warn, backward compatibility, alias, migration]
description: Use when renaming APIs, changing config schemas, adding aliases, preserving old behavior, or proposing migration/deprecation shims.
---

# Compatibility shims

## Core rule

Prefer one live API version. Rename freely and update call sites in the same change.

## Apply when

- Code renames APIs, config keys, modules, imports, or public methods.
- A change proposes aliases, wrappers, deprecation warnings, v1/v2 modules, or migration branches.
- Predecessor project compatibility is being preserved or removed.

## Do

- Update call sites to the cleaner API in the same change.
- Keep one config schema and update defaults/bootstrap when keys change.
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

Unless explicitly instructed, never consider migration from an older codebase or data source in coding, refactoring, and reviews. Only keep the cleanest, latest api without even notifying the user of the existence of the old api.

This applies when the package is under development, waive for a stable version project or when user explicitly request for compatibility.

## Related rules

Also apply [model.md](model.md) for one clear API, [name.md](name.md) for renamed symbols, [config.md](config.md) for schema changes, and [docs](../../project/docs.md) for migration notes.
