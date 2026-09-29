---
name: py-files-layout
description: Read when laying out a Python package or feature folder.
---

# Python package layout

## Summary

Start with the smallest owning package and add files only when their roles exist.

## Standard Package Shape

Use this as a reference template for a package or substantial feature folder. Include only the files that the package actually needs.

```text
src/acme/feature/
  __init__.py       # public exposure: __all__, imports, optional __getattr__
  __init__.pyi      # optional: static public exposure for lazy __getattr__
  py.typed          # optional: top-level package marker when distributing typed code
  base.py           # contracts, base classes, protocols (optional but usually present)
  registry.py       # registration/discovery when the feature has extensions (optional)
  manifest.py       # extension descriptor/schema when this is an extension bundle (optional)
  types.py          # type definitions (optional)
  utils.py          # exposable local helpers (optional)
  _utils.py         # internal shared helpers (optional)
  ...
  sub1/
    __init__.py
    adapter.py      # just an illustration file, not a rule
    ...
  sub2/
    __init__.py
    adapter.py      # keep subfolders as aligned as possible unless fundamentally different
    ...
```

Do not create every file by default. Start with `__init__.py` plus the smallest owning module; add `__init__.pyi`, top-level `py.typed`, `base.py`, `registry.py`, `utils.py`, `_utils.py`, or subfolders only when the code has that role.

For an open family, the same physical layout may appear inside the host repository, another installed distribution, or a registered local bundle. Consumers resolve the descriptor through the authoritative Registry; they do not infer origin or eligibility from the folder path.
