---
name: py-files-example
description: Read when comparing Python feature layouts and exports.
---

# Python layout examples

## Summary

Keep feature code under its owner and expose supported imports through the package front door.

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

The package root owns registry behavior. Implementation families own concrete implementations. Private helper code stays visibly internal.
