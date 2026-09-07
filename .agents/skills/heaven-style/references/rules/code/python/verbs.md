---
id: oop
title: OOP vocabulary
blocking: true
description: Choose Python collection, CRUD, lifecycle, and configuration vocabulary.
---

# OOP vocabulary

## Core rule

Public APIs use one name per concept and type annotations on parameters and returns. Prefer the terms below before inventing alternate names. For whether a concept deserves a public class or function at all, also apply [api](api.md).

## Do

- Use one canonical method name per concept.
- Prefer Python protocols for collection-like objects before custom accessors.
- Keep retrieval, exact lookup, search, query, and file loading distinct.
- Type public method parameters and returns.

## Avoid

- Synonyms such as `as_dict` and `to_dict` in the same surface.
- `save` for registry, database row, or config writes that persist immediately.
- Free-function front doors when the object model already has a natural class/instance method.

## Collections

Collection-like objects should implement Python protocols first, then explicit exports:

```python
def __len__(self) -> int: ...
def __iter__(self): ...
def __getitem__(self, key: str) -> Row: ...
def to_list(self) -> list[dict[str, object]]: ...
def to_dict(self) -> dict[str, object]: ...
```

Use `add` for mutating in-memory collections, builder lists, or runtime registries when the object is already in memory and no durable global registration happens, for example `Toolkit.add(...)`, or `InteropReport.add(...)`. Prefer collection protocols plus `get`/`__getitem__` for read access.

## Registries and workspace-bound objects

Use `register` when the operation makes an object discoverable in a database, workspace, Python registry, or capability registry:

```python
ws.register(Entity)
capsule.register()
toolkit.register()
Project.load("shop")
# pseudocode — use the repo's handler registration API
register_handler(...)
register_backend(...)
```

Do not use `save` for registry writes. Registry-oriented classes should expose OOP class/instance methods such as `Project.load`, `Project.register`, `Artifact.register`, `Toolkit.register`, and `Artifact.verify`, not free-function front doors like `get_project`, `register_project`, or `verify_manifest`.

## CRUD and search

| Concept | Canonical |
| --- | --- |
| Create only | `insert` |
| Merge/create by key | `upsert` |
| Delete one | `remove` |
| Delete all | `clear` |
| Rename | `rename` |
| Exact single lookup | `get` |
| External retrieval / RAG retrieval | `retrieve` |
| Structured query | `query` |
| Fuzzy or ranked lookup | `search` |

`get` is for exact lookup. `retrieve` is acceptable when the domain means retrieval rather than key access.

## KV CRUD

Use `get`, `set`, `unset`, `setdef`, `clear`, and optionally `__getitem__` / `__setitem__` for natural mapping syntax.

```python
cache.set("token", value)
value = cache.get("token", default=None)
cache.unset("token")
```

Native `dict.get` uses positional fallback; project KV objects may support `default=`.

## Batch verbs

Use `batch_*` when the batch behavior is not equivalent to looping because it changes I/O, transactionality, routing, or performance:

```python
store.batch_upsert(rows)
rows = store.batch_get(ids)
```

## Engines and lifecycle

Use `connect`, `close`, `flush`, `drop`, `start`, `stop`, and `reset` for lifecycle verbs. `drop` is destructive schema/storage removal. `clear` removes contents but keeps the object.

## Specs, configs, plans

- `*Spec`: declarative input contract or normalized request.
- `*Config`: runtime settings and defaults.
- `*Plan`: ordered execution decision.
- `*Engine`: stateful executor or connection-owning runtime.
- `identifier`: stable type/class identifier.
- `object_id`: user-facing object identity.
- `type`: external schema word only; prefer `kind`, `dtype`, or `entity` in Python when clearer.
- `metadata`: opaque extra user/provider data; avoid hiding required fields in it.
- `canonical`: normalized single source of truth.

## Preset system

Use this hierarchy when modeling configurable backends:

```text
Preset = Provider + params
Provider = customizable backend route + provider defaults
Backend = concrete dialect/driver/runtime implementation
```

For LLMs, a preset is a directly callable config containing provider, model, gateway, and model args. Provider plus gateway determines the backend route. Model args tune a request.

For databases, a preset is a named database/provider config. A provider describes an engine family with backend, dialect/driver, and connection args. A backend is the implementation adapter.

For file, mapping, copy, and projection operations, read [value operations](verbs/value.md).
