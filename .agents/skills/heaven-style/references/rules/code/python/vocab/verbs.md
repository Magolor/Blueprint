---
name: oop
description: Choose Python collection, CRUD, lifecycle, and configuration vocabulary.
---

# OOP vocabulary

## Summary

Public APIs use one name per concept and type annotations on parameters and returns. Prefer the terms below before inventing alternate names. For whether a concept deserves a public class or function at all, also apply [api](../api.md).

## Paired operation families

Choose the whole family by its data/lifecycle model, not one fashionable verb in isolation. Member methods belong to the natural domain owner. Canonical names and supported aliases share one implementation and observable contract; see [aliases](aliases.md). CLI commands use the same concepts as SDK methods.

| Model | Canonical family | Contract |
| --- | --- | --- |
| KV configuration/cache | `get`, `set`, `unset`, `setdef`, `clear` | Lookup by key; assign; remove key; assign only if absent; remove all contents. Preserve falsy values and meaningful null/None. `setdef` returns the existing or newly assigned value. |
| Rich rows/entities | `upsert`, `insert`, `remove`, `get` | Merge/create by identity; create only; remove member; exact identity lookup. `update` explicitly changes an existing member. |
| Rich selection | `retrieve`, `query`, `search` | Retrieval or structured selection can expose filters, projections, ranking, or other control beyond exact `get`. Use `search` for fuzzy/ranked discovery. Do not invent fetch/get/load synonyms for the same operation. |
| Resource access | `open`, `close`, `dispose`; `connect` when appropriate | Open/close access; connect a remote/session resource; dispose owned runtime resources. Document whether close allows reopening and whether disposal is final. |
| Resource existence | `create`, `destroy`, `drop` | Create an owned resource; destroy its lifecycle/existence; drop destructive schema/storage objects. Keep these distinct from closing a handle or removing one row. |
| Persistence | `load`, `dump` or `save`, `flush` | Read persisted state; write a file/artifact snapshot; flush buffered changes. These names promise persistence, usually filesystem I/O. They are not generic in-memory conversion verbs. |
| Setup | `setup`, `init`, `reset` | Setup is usually global/one-time; init prepares a project or routinely initialized scope. Expose reset when meaningful, commonly as an explicit setup option. Constructors still avoid hidden activation/I/O. |
| Representation | `encode`, `decode`; paired `from*`, `to*` | Encode/decode representations; construct/export a domain value with explicit format or source. Keep text, bytes, JSON-shaped data, and display distinct. |
| Discovery/collection | `list`, `register`, `add`, `rename`, `clear` | List members; make discoverable; add to an in-memory collection; rename identity/label under its documented contract; clear contents. |

### Single and multiple values

Prefer one versatile operation: `upsert(product)` and `upsert([product])`. Keep input cardinality, return shape, ordering, error behavior, and transaction semantics explicit. A single input can return one result and a collection can return a collection when overloads/types express that distinction. Do not silently conflate partial success with atomic success.

Do not introduce `batch_*`/`batch*` merely to accept a collection. A separate bulk operation is justified only by a materially different contract that the ordinary operation cannot express clearly, such as a streaming job or different transaction/result semantics. Internal batching for performance alone need not add a public verb.

### Persistence versus value conversion

`load` may reopen an object from a persisted registry, config store, or artifact; it does not mean arbitrary lookup from an in-memory map. Use `get` for that lookup. Paired format utilities may use their established language vocabulary (Python `loads_*`/`dumps_*` for text/bytes); document that format suffix and do not confuse those with unsuffixed persistence methods. `save`/`dump` are paired with `load`, and `flush` commits buffers. Immediate KV/entity writes use `set`/`upsert`, not a redundant save step.

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

## Engines and lifecycle

Use `connect`, `close`, `flush`, `drop`, `start`, `stop`, and `reset` for lifecycle verbs. `drop` is destructive schema/storage removal. `clear` removes contents but keeps the object.

For file, mapping, copy, and projection operations, read [value operations](value.md).

Prefer explicit setup reset policy: `setup(reset=True)` in Python or `setup({ reset: true })` in TypeScript. Reset remains a member operation when the object has a useful independent reset lifecycle; the option does not justify hidden constructor setup.
