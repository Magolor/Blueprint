---
name: compat
description: Change Python names, schemas, or compatibility promises.
---

# Compatibility shims

## Summary

Keep one live API for owned or unreleased code. Preserve logical features while replacing obsolete interfaces and updating owned callers together. Stable packages and persisted formats follow the repository's declared support contract.

## One live version

Enforce one current owned API, configuration schema, and internal representation. Update owned callers together and delete obsolete paths; do not proactively preserve an old version. Supported canonical aliases belong to this same current API and share its implementation. They are not permission for parallel v1/v2 implementations.

Published support or an explicit user requirement can justify a bounded compatibility adapter at the external boundary, with a named consumer and removal condition. It does not create a second internal version or permit silent loss of persisted data.

## Do

- Update call sites, public exports, tests, examples, and current docs to the cleaner API in the same change.
- Keep one config schema. Update defaults/bootstrap when keys change.
- Put one-shot migrations under scripts or migrations.
- Document explicit compatibility waivers when the user requires a layer.
- Verify retained behavior through the current public entry. Remove tests that only preserve the retired interface; retain real behavioral regressions.
- Give a required temporary shim a named consumer, owner, test, and removal condition. Keep it at the supported boundary; internal callers use the canonical API.

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

Do not invent predecessor migrations or retain forwarding aliases merely because an old name existed. Under development, keep the accepted current API and migrate owned callers directly. Preserve required data and behavior; retiring code is not permission to discard stored data.

Current guides describe the supported interface. Keep relevant migration or decision history in its declared owner. Stable-version projects, supported persisted formats, and explicit user compatibility requests retain their real support obligations; resolve those obligations rather than silently deleting the old path or hiding a required migration.
