---
id: files
title: File organization
enabled: true
blocking: true
order: 290
category: code-quality
keywords: [file organization, module layout, package layout, folder, private module, internal file, utils.py, _utils.py, __init__, __init__.pyi, py.typed, pyi, __all__, __getattr__, lazy exports, exports, adapter files, provider files, feature folder, file naming]
description: Use when adding or reviewing Python files, package folders, public exports, lazy exports, local helper modules, internal helper modules, typing stubs, implementation families, adapters, providers, or feature-local module boundaries.
---

# File Organization

## Core rule

Organize files by ownership and feature locality. A reader should find the code for one feature or extension by opening one cohesive folder or distribution, not by chasing same-feature files across top-level buckets, export helpers, and generic registries. Folder placement owns code; it must not become discovery truth for an open extension family.

Prefer short one-word file and folder names. Use a two-word name only for an established domain phrase such as `user_auth`, `text_index`, or `jsonl`. Re-examine any file name with three or more words, any obscure abbreviation, and any file name that repeats parent-folder context.

## Apply when

- Code adds, renames, moves, or deletes Python files or package folders.
- Code adds an adapter, provider, handler, strategy, registry, or implementation family.
- A feature's implementation is spread across top-level modules and nested helper packages.
- A public import surface needs lazy exports or package-level re-exports.
- A package uses module-level `__getattr__` for known lazy public exports.
- A package needs local helper modules that are not broad enough for the repo's shared utility layer.

## Do

- Keep all code for the same feature under the owning folder.
- Keep each independently extensible implementation as a cohesive bundle containing its manifest/descriptor, implementation, configuration schema, assets, tests, docs, and migrations where practical. Bundled and external implementations use the same declared registration/selection contract; a durable registry is optional unless the product promises managed discovery or lifecycle.
- Group small internal implementations as sibling modules only when the family is not promised as an independently installable extension surface.
- Promote a feature to a subfolder when it has several real internal parts; keep those parts inside that folder.
- Use `base.py` for package-local base classes and contracts.
- Use `registry.py` for the family-owned catalog/resolver facade or durable registration and discovery behavior; concrete extension inventory belongs in extension descriptors, not in a privileged import list.
- Use `utils.py` for exposable local helper functions that belong to this package but are not broad shared-infrastructure utilities.
- Use `_utils.py` for internal helper functions shared inside one package. Whether a helper deserves to exist is governed by [clean.md](clean.md).
- Use a generic implementation filename such as `client.py`, `adapter.py`, or `handler.py` only when the folder name already provides the domain context.
- Put package public exports in the owning `__init__.py` with `__all__` and, when imports are expensive, `__getattr__` plus a local lazy export map.
- Add an adjacent `__init__.pyi` when `__init__.py` lazily exposes known public symbols through `__getattr__` and the package should work well with type checkers or IDE autocomplete.
- Ship `py.typed` at the distributed package root for packages that expose inline types or mixed `.py` plus `.pyi` type information.
- Delete or move the old files in the same change; do not leave compatibility packages, alias modules, or old-path shims unless explicitly waived.

## Avoid

- Top-level buckets such as `builtin.py`, `families.py`, `type_registry.py`, `helpers.py`, `common.py`, or `misc.py` when the code has a clearer owning module.
- Sidecar exposure files such as `exports.py`, `_exports.py`, `api.py`, `public.py`, or `facade.py` inside one package. Use `__init__.py`; if the exposure surface is large, add nested folders with their own `__init__.py`. A service package's `api/` boundary is different: it is valid when it owns real orchestration and transport contracts under the [service interface rule](../../project/interfaces.md), never when it only re-exports symbols.
- Public-looking internal helpers such as `config.py` when the module is only helper code; prefer `_utils.py`. Keep `config.py` for true config models, schemas, defaults, or resource loading.
- Broad `def __getattr__(name: str) -> Any: ...` stubs for a known finite public API. List the exact exports in `__init__.pyi` instead.
- `.pyi` files for ordinary eager exports when inline annotations plus `py.typed` already give type checkers a clear public interface.
- Standalone feature packages for code that only exists to serve one parent feature or strategy.
- File names that repeat parent context, such as `storage_type_registry.py` inside `storage/`.
- Obscure, inconsistent, or long names such as `tokidxrt.py`, `search_strategy_token_index_runtime_manager.py`, or mixed pairs like `token_index.py` plus `vectorStrategy.py`.
- Many tiny files that split one concept by function name rather than by ownership.
- Built-in-only folders, package scans, or `__init__.py` import lists that act as the discovery mechanism for an open extension family.
- Manifests, schemas, assets, and migrations scattered into central host-package buckets when one extension owns them.

## Standard Package Shape

Use this as a gold template for a package or substantial feature folder. Include only the files that the package actually needs.

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

## Example

### Keep a feature under its owner

**Anti-pattern:**

```text
src/acme/token_search.py
src/acme/search_token_runtime.py
src/acme/search_strategy_token_index.py
src/acme/indexing/token_strategy_registry.py
src/acme/providers/search_token_provider.py
```

This makes token indexing look like a standalone package while part of the implementation actually belongs to search strategy execution.

**Recommended pattern:**

```text
src/acme/search/
  __init__.py
  base.py
  registry.py
  utils.py
  _utils.py
  strategies/
    __init__.py
    token/
      __init__.py
      index.py
      runtime.py
      registry.py
    vector/
      __init__.py
      index.py
      runtime.py
  providers/
    __init__.py
    openai.py
    local.py
  formats/
    __init__.py
    json.py
    jsonl.py
```

When token indexing is part of search strategies, its runtime and helper files live below `search/strategies/token/`. Provider and format implementations are separate sibling families, so a maintainer can inspect one hierarchy without decoding mixed file names.

### Put public exposure at the package front door

**Anti-pattern:**

```text
src/acme/storage/api.py
src/acme/storage/exports.py
src/acme/storage/public.py
src/acme/storage/sql_exports.py
```

**Recommended pattern:**

```text
src/acme/storage/__init__.py
src/acme/storage/sql/__init__.py
src/acme/storage/document/__init__.py
```

Package `__init__.py` owns the import surface for that package. Use `__all__` for explicit exports and optional `__getattr__` for lazy loading. Do not add exposure-only files at the same package level; introduce nested folders when the surface needs structure.

### Type lazy exports explicitly

**Anti-pattern:**

```text
src/acme/storage/__init__.py
```

```python
# src/acme/storage/__init__.py
from typing import Any

__all__ = ["SQLiteStore", "PostgresStore"]
_LAZY = {
    "SQLiteStore": (".sqlite", "SQLiteStore"),
    "PostgresStore": (".postgres", "PostgresStore"),
}

def __getattr__(name: str) -> Any:
    ...
```

Type checkers and IDEs cannot reliably infer this finite public API from the runtime lazy loader alone.

**Recommended pattern:**

```text
src/acme/storage/__init__.py
src/acme/storage/__init__.pyi
src/acme/storage/py.typed
```

```python
# src/acme/storage/__init__.pyi
from .sqlite import SQLiteStore as SQLiteStore
from .postgres import PostgresStore as PostgresStore

__all__ = ["SQLiteStore", "PostgresStore"]
```

Use an adjacent `__init__.pyi` to state known lazy exports exactly. Match runtime `__all__` and use explicit `X as X` re-exports in stubs. Use a broad stub-level `__getattr__` only for genuinely open-ended or intentionally incomplete dynamic modules.

### Name utility modules by exposure

**Anti-pattern:**

```text
src/acme/search/helpers.py
src/acme/search/common.py
src/acme/search/config.py
src/acme/search/_helpers.py
```

**Recommended pattern:**

```text
src/acme/search/utils.py
src/acme/search/_utils.py
src/acme/search/config.py
```

Use `utils.py` for helpers that are intentionally importable by package users or sibling modules. Use `_utils.py` for internal helpers. Keep `config.py` only when it truly owns configuration models, defaults, or resource loading.

### Prefer clear short names

**Anti-pattern:**

```text
src/acme/search/search_strategy_token_index_runtime_manager.py
src/acme/search/tokidxrt.py
src/acme/search/vectorStrategy.py
src/acme/search/providers/openai_provider_impl.py
```

**Recommended pattern:**

```text
src/acme/search/strategies/token/runtime.py
src/acme/search/strategies/token/index.py
src/acme/search/strategies/vector/runtime.py
src/acme/search/providers/openai.py
```

Short names are readable when the folder hierarchy carries context. Avoid abbreviations that only the author understands and long names that encode the whole path again.

### Keep implementation families together

**Anti-pattern:**

```text
src/acme/builtin.py
src/acme/type_registry.py
src/acme/families.py
src/acme/name_rules.py
```

**Recommended pattern:**

```text
src/acme/registry.py
src/acme/_utils.py
src/acme/storage/sqlite.py
src/acme/storage/postgres.py
src/acme/providers/openai.py
src/acme/formats/json.py
```

The package root owns registry behavior; implementation families own concrete implementations; private helper code stays visibly internal.

## Review checks

- Can a newcomer identify the owning feature from the path alone?
- Can the feature be changed, reviewed, or deleted by working mostly inside one folder?
- Does each folder expose public symbols through `__init__.py` instead of a sidecar exposure file?
- When `__init__.py` uses `__getattr__` for known lazy public exports, does an adjacent `__init__.pyi` describe those exports for type checkers?
- Are exposable local helpers in `utils.py` and internal shared helpers in `_utils.py`?
- Are file names short, contextual, and free of repeated parent-folder words?
- Can a bundled extension move to an external distribution without changing consumer imports, configuration, or runtime dispatch?
- Does folder locality keep one extension coherent without becoming a built-in-only discovery mechanism?

## Related rules

Also apply [name.md](name.md) for symbol and module naming, [clean.md](clean.md) for helper boundaries, [model.md](model.md) for public surface size, [extension.md](../../project/extension.md) for adapter/provider registration, [interfaces.md](../../project/interfaces.md) for service SDK/API/interface layers, and [compat.md](compat.md) for break-and-fix moves without shims.
