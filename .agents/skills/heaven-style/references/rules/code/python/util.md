---
id: util
title: Utility layer
enabled: true
blocking: true
order: 10
category: code-quality
keywords: [json, yaml, pickle, pathlib, os.path, subprocess, shutil, hashlib, logging, print, open, standard library, shared utility]
description: Use when Python code touches paths, files, serialization, shell commands, hashing, logging, temp files, IDs, or shared utility ownership.
---

# Utility layer

## Core rule

Use the utility layer that the target repository explicitly owns. If no coherent shared owner exists, use Python's standard library or an established dependency directly. Do not add HeavenBase, a platform package, or a project-local wrapper merely to satisfy heaven-style.

Create or promote a shared helper only when it owns real policy or multiple proven consumers need identical behavior. A thin wrapper that only renames `Path`, `json`, `subprocess`, `logging`, or another direct API adds indirection without ownership.

In a HeavenBase-lineage repository that explicitly adopts its infrastructure, `heavenbase.utils` is the declared owner for its covered paths, files, serialization, shell, logging, hashing, and ID concerns. That is a conditional repository profile, not a requirement for arbitrary Python packages.

## Apply when

- Code reads or writes files, paths, package resources, temp files, or user-state paths.
- Code serializes JSON/YAML/pickle/text/base64/hex payloads.
- Code runs shell commands, copies/deletes files, hashes values, logs, or creates IDs.
- A change proposes a generic helper module or a new dependency for utility behavior.

## Do

- Read `AGENTS.md`, nearby imports, and repository docs to identify an existing utility owner before adding another path.
- Use normal `pathlib`, `json`, `logging`, `hashlib`, `subprocess`, `shutil`, `tempfile`, `uuid`, and `importlib.resources` APIs when the repository has no contrary abstraction.
- Prefer a mature dependency when it supplies a substantial validated contract the standard library does not.
- Keep domain behavior in the owning package even when it delegates low-level work to a shared utility.
- Promote a helper only when reuse, validation, policy, observability, or error semantics justify a stable abstraction.
- Use the repository's logging policy instead of `print` in library code.

## Avoid

- Adding HeavenBase or another platform dependency solely for convenience helpers.
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

If several packages later need the same validation, resource lookup, logging, and error contract, promote that complete behavior to the repository's shared owner rather than wrapping each primitive separately.

## Ownership ladder

1. Use an existing repository/platform utility when it clearly owns the concern.
2. Otherwise use the standard library or an established dependency directly.
3. Keep one-off domain transforms local and explicit.
4. Introduce a shared helper only for repeated behavior with a stable policy boundary.

For a repository that explicitly adopts HeavenBase utilities, the same ladder starts with `heavenbase.utils`; verify the exact helper against that repository rather than assuming every utility exists.

## Related rules

Also apply [config.md](config.md) for config/resource ownership, [types.md](types.md) for annotation style, [clean.md](clean.md) for helper promotion decisions, and [files.md](files.md) for utility module placement.

Blueprint's skill-maintenance scanner is a repository self-compliance check, not a generic Python-package gate:

```bash
rtk uv run python .agents/skills/heaven-style/scripts/scan.py .agents/skills/heaven-style/scripts
```
