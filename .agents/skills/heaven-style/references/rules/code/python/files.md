---
id: files
title: File organization
blocking: true
description: Organize Python modules, facades, lazy exports, and package boundaries.
---

# File Organization

## Core rule

Organize files by ownership and feature locality. A reader should find the code for one feature or extension by opening one cohesive folder or distribution. Do not scatter files for the same feature across top-level categories, export helpers, and generic registries. Folder placement owns code. It must not become discovery truth for an open extension family.

Prefer short one-word file and folder names. Use a two-word name only for an established domain phrase such as `user_auth`, `text_index`, or `jsonl`. Re-examine any file name with three or more words, any obscure abbreviation, and any file name that repeats parent-folder context.

## Do

- Keep all code for the same feature under the owning folder.
- Keep each independently extensible implementation as a cohesive bundle containing its manifest/descriptor, implementation, configuration schema, assets, tests, docs, and migrations where practical. Bundled and external implementations use the same declared registration/selection contract. A durable registry is optional unless the product promises managed discovery or lifecycle.
- Group small internal implementations as sibling modules only when the family is not promised as an independently installable extension surface.
- Promote a feature to a subfolder when it has several real internal parts; keep those parts inside that folder.
- Use `base.py` for package-local base classes and contracts.
- Use `registry.py` for the family-owned catalog/resolver facade or durable registration and discovery behavior; concrete extension inventory belongs in extension descriptors, not in a privileged import list.
- Use `utils.py` for exposable local helper functions that belong to this package but are not broad shared-infrastructure utilities.
- Use `_utils.py` for internal helper functions shared inside one package. Whether a helper deserves to exist is governed by [clean](clean.md).
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

For a package layout decision, read [layout](files/layout.md); for comparative examples, read [examples](files/example.md).
