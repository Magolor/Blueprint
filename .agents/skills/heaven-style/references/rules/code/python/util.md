---
id: util
title: Utility layer
blocking: true
description: Choose Python utilities for resources, I/O, serialization, logging, and processes.
---

# Utility layer

## Core rule

Use the utility layer that the target repository explicitly owns. If no coherent shared owner exists, use Python's standard library or an established dependency directly. Do not add a platform package or project-local wrapper merely to satisfy heaven-style.

Create or promote a shared helper only when it owns real policy or multiple proven consumers need identical behavior. A thin wrapper that only renames `Path`, `json`, `subprocess`, `logging`, or another direct API adds indirection without ownership.

## Do

- Read `AGENTS.md`, nearby imports, and repository docs to identify an existing utility owner before adding another path.
- Use normal `pathlib`, `json`, `logging`, `hashlib`, `subprocess`, `shutil`, `tempfile`, `uuid`, and `importlib.resources` APIs when the repository has no contrary abstraction.
- Prefer a mature dependency when it supplies a substantial validated contract the standard library does not.
- Keep domain behavior in the owning package even when it delegates low-level work to a shared utility.
- Promote a helper only when reuse, validation, policy, observability, or error semantics justify a stable abstraction.
- Use the repository's logging policy instead of `print` in library code.

## Avoid

- Adding a platform dependency solely for convenience helpers.
- Project-local wrappers that only rename one standard-library or dependency call.
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

**Recommended pattern:**

```python
import json
from pathlib import Path


def load_items(root: Path, name: str) -> list[dict[str, object]]:
    path = root / "data" / f"{name}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("items", []))
```

If several packages later need the same validation, resource lookup, logging, and error contract, move that complete behavior to the repository's shared owner. Do not wrap each primitive separately in that case.

## Ownership ladder

1. Use an existing repository/platform utility when it clearly owns the concern.
2. Otherwise use the standard library or an established dependency directly.
3. Keep one-off domain transforms local and explicit.
4. Introduce a shared helper only for repeated behavior with a stable policy boundary.

The skill's standalone dependency scan is a maintenance check, not a generic Python-package gate:

```bash
rtk uv run python .agents/skills/heaven-style/scripts/scan.py --stdlib-only --allow-import yaml .agents/skills/heaven-style/scripts
```
