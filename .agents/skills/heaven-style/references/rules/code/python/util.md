---
name: util
description: Choose Python utilities for resources, I/O, serialization, logging, and processes.
---

# Utility layer

## Summary

Use the utility layer that the target repository explicitly owns. If no coherent shared owner exists, use Python's standard library or an established dependency directly. Do not add a platform package or project-local wrapper merely to satisfy heaven-style.

## Helper and import ownership

Read [clean](clean.md) for inline code versus shared utility placement. Prefer the package's established utility re-exports as well as its wrapped operations, even for convenience symbols, rather than scattering equivalent imports. Do not add a foreign platform dependency or invent a giant facade merely to obtain them. Keep modern language types and the repository's runtime/import constraints.

## Principle

Prefer the package-owned utility contract whenever it supplies the operation, even when it delegates to the standard library. When a currently needed small helper is generic enough for reuse, place it directly in the package-wide utils or the narrowest subgroup shared utils. Do not require a second caller, create a small helper in a single feature module, or add wrappers for hypothetical needs.

## Do

- Read `AGENTS.md`, nearby imports, and repository docs to identify an existing utility owner before adding another path.
- Use normal `pathlib`, `json`, `logging`, `hashlib`, `subprocess`, `shutil`, `tempfile`, `uuid`, and `importlib.resources` APIs when the repository has no contrary abstraction.
- Prefer a mature dependency when it supplies a substantial validated contract the standard library does not.
- Keep domain behavior in the owning package even when it delegates low-level work to a shared utility.
- Add needed generic helpers to the shared owner; keep specialized one-use expressions inline. Larger private feature boundaries follow [clean](clean.md).
- Use the repository's logging policy instead of `print` in library code.

## Avoid

- Adding a platform dependency solely for convenience helpers.
- Small convenience wrappers confined to one feature module, or new wrappers duplicating an existing package utility.
- A catch-all `helpers.py`, `common.py`, or `utils.py` with no clear package owner.
- Manual encoding, unsafe shell strings, or ad-hoc serialization when a direct safe API already exists.
- Duplicating repository-owned path, resource, logging, serialization, or command policy.

## Example

**Anti-pattern:**

```python
def join_data_path(root: str, name: str) -> str:
    return str(Path(root) / "data" / f"{name}.json")


def read_json_file(path: str) -> dict[str, object]:
    return json.loads(Path(path).read_text(encoding="utf-8"))
```

These wrappers rename direct operations without adding policy.

**Recommended pattern:** when the package owns `pj` and `load_json`, reuse them. These imports illustrate an existing package utility surface, not a dependency to add.

```python
from acme.utils import load_json, pj


path = pj(root, "data", f"{name}.json")
data = load_json(path)
items = data.get("items", [])
```

Use standard-library `Path` and `json` directly only when the package has no suitable owner. Validate decoded values through the existing schema/boundary. A one-use transform remains inline; a needed generic helper belongs in shared utils from its introduction.

## Ownership ladder

1. Use an existing repository/platform utility when it clearly owns the concern.
2. Otherwise use the standard library or an established dependency directly.
3. Keep one-off domain transforms local and explicit.
4. Put a needed generic helper in package-wide or subgroup shared utils, with a clear contract; do not create a module-local miniature helper.

The skill's standalone dependency scan is a maintenance check, not a generic Python-package gate:

```bash
rtk uv run python .agents/skills/heaven-style/scripts/scan.py --stdlib-only --allow-import yaml .agents/skills/heaven-style/scripts
```
