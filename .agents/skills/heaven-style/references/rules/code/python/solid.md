---
id: solid
title: SOLID boundaries
enabled: true
blocking: true
order: 37
category: code-quality
keywords: [SOLID, SRP, OCP, LSP, ISP, DIP, single responsibility, open closed, Liskov, interface segregation, dependency inversion, backend, provider, strategy, registry, architecture]
description: Use when designing or reviewing SOLID boundaries, class boundaries, extension points, inheritance contracts, adapter interfaces, registries, or strategy/provider dependencies.
---

# SOLID boundaries

## Core rule

Use SOLID as a boundary check, not as ceremony. Classes, modules, and packages should follow **SRP** (single responsibility), **OCP** (open/closed), **LSP** (Liskov substitution), **ISP** (interface segregation), and **DIP** (dependency inversion): one reason to change, stable extension APIs, substitutable subclasses, minimal role-specific interfaces, and abstractions before concrete provider details.

## Apply when

- A change adds or reshapes classes, base classes, protocols, adapters, registries, providers, backends, handlers, or strategies.
- A central planner, registry, switch, or import list must change for every new implementation.
- A subclass needs special call ordering, special constructor semantics, or undocumented capability exceptions.
- A client receives an interface with methods it does not need or cannot implement correctly.
- High-level orchestration imports concrete providers, dialects, drivers, or storage details directly.

## Do

- **SRP (Single Responsibility):** give each class or module one owner and one reason to change.
- **OCP (Open/Closed):** add behavior through registered implementations, strategy objects, adapters, or class-owned metadata instead of editing central conditionals.
- **LSP (Liskov Substitution):** make every subclass honor the base contract for construction, lifecycle, errors, and return types. Represent differences as explicit capability flags or typed overrides.
- **ISP (Interface Segregation):** keep the base interface to required common behavior; split optional capabilities into subclass, protocol, adapter, or registry families.
- **DIP (Dependency Inversion):** make high-level flows depend on base classes, protocols, registries, and config. Concrete providers publish descriptors through the family registration contract and keep provider-specific metadata close to the provider; high-level policy does not import them merely to make them discoverable.

## Avoid

- Catch-all base classes or helper modules that mix lifecycle, parsing, storage, provider metadata, and query execution.
- `if provider == ...` / `if backend == ...` branches in orchestration paths when a registry or strategy API can own the variation.
- Subclasses that mutate caller-owned inputs, require hidden preconditions, return incompatible shapes, or silently ignore base-class guarantees.
- Interfaces that force every implementation to carry unused methods, no-op methods, or provider-specific arguments.
- High-level modules that import concrete driver, dialect, backend, or provider code just to choose behavior.

## Example

### SRP: Single Responsibility

**Anti-pattern:**

```python
# pseudo-code: query execution details omitted
class QueryBuilder:
    def where(self, field: str, op: str, value: object) -> None: ...
    def choose_backend(self, schema: object) -> str: ...
    def storage_plan(self, schema: object) -> dict[str, object]: ...
```

One class changes for user query shape, backend selection, and storage planning.

**Recommended pattern:**

```python
# pseudo-code: query execution details omitted
class QueryBuilder: # Used for Query/Read only
    def where(self, field: str, op: str, value: object) -> None: ...
    def build(self) -> "QuerySpec": ...

class StoragePlanner: # Used for Write/Update/Delete only
    def plan(self, query: "QuerySpec", schema: object) -> "StoragePlan": ...
```

Query syntax changes in `QueryBuilder`; storage placement changes in `StoragePlanner`.

### OCP: Open/Closed

**Anti-pattern:**

```python
# pseudo-code: dumps_json and dumps_csv are existing format helpers
def export(row: dict[str, object], kind: str) -> bytes:
    if kind == "json":
        return dumps_json(row)
    if kind == "csv":
        return dumps_csv(row)
    raise ValueError(f"Unknown export kind {kind!r}")
```

Every new export kind edits the central function.

**Recommended pattern:**

```python
from typing import Protocol


class Exporter(Protocol):
    def dumps(self, row: dict[str, object]) -> bytes: ...


# Registration/install phase: bundled and external exporters use this same descriptor.
catalog.register(
    kind="exporter",
    identifier="json",
    entry_point="acme_json:JsonExporter",
    aliases=("js",),
    provenance={"origin": "system"},
)


def export(row: dict[str, object], exporter: str = "json") -> bytes:
    implementation: Exporter = catalog.load("exporter", exporter)
    return implementation.dumps(row)
```

New exporters publish a descriptor without changing the dispatch path. The `json` descriptor uses no privileged loader because it is bundled; moving it to another distribution changes registration provenance/location, not consumer code. The catalog, resolver, persistence, trust, and lifecycle contract belongs to [extension points](../../project/extension.md), not this SOLID example.

### OCP/ISP: Open Capability Vocabularies

When independent extensions may introduce new capability kinds, keep the base protocol stable and make capability identity an independently registered descriptor. If adding one optional feature requires a new central field, base method, switch branch, and serialization entry, the design has an open/closed and interface-segregation smell. Read [Open capability vocabulary](../../../examples/code/open-capability-vocabulary.md) for the compact bad-smell/good-smell comparison. Keep intentionally closed vocabularies as enums or discriminated unions.

### LSP: Liskov Substitution

**Anti-pattern:**

```python
class Store:
    def get(self, key: str, default: str | None = None) -> str | None:
        return default

class DictStore(Store):
    def get(self, key: str, default: str | None = None) -> str:
        raise KeyError(key)
```

`StrictStore` breaks callers that rely on the base default-on-miss contract.

**Recommended pattern:**

```python
class Store:
    def get(self, key: str, default: str | None = None) -> str | None:
        return default

class DictStore(Store):
    def __init__(self, data: dict[str, str]) -> None:
        self._data = data

    def get(self, key: str, default: str | None = None) -> str | None:
        return self._data.get(key, default)

    def require(self, key: str) -> str:
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value
```

The override preserves the base contract; stricter behavior gets a separate method.

### ISP: Interface Segregation

**Anti-pattern:**

```python
class Backend:
    def get(self, key: str) -> object | None: ...
    def set(self, key: str, value: object) -> None: ...
    def delete(self, key: str) -> None: ...
    def vector_search(self, query: list[float]) -> list[str]: ...
    def graph_traverse(self, start: str) -> list[str]: ...

class FileBackend(Backend):
    def vector_search(self, query: list[float]) -> list[str]:
        raise NotImplementedError("file backend does not support vector search")

    def graph_traverse(self, start: str) -> list[str]:
        raise NotImplementedError("file backend does not support graph traversal")
```

Core storage and optional search/traversal capabilities are forced into one interface.

**Recommended pattern:**

```python
class Backend:
    def get(self, key: str) -> object | None: ...
    def set(self, key: str, value: object) -> None: ...
    def delete(self, key: str) -> None: ...

class VectorBackend(Backend):
    def vector_search(self, query: list[float]) -> list[str]: ...

class GraphBackend(Backend):
    def graph_traverse(self, start: str) -> list[str]: ...

def nearest(backend: VectorBackend, query: list[float]) -> list[str]:
    return backend.vector_search(query)
```

Keep common required behavior on `Backend`; split optional capabilities into capability-specific subclasses, protocols, adapters, or registry families.

### DIP: Dependency Inversion

**Anti-pattern:**

```python
class LogicalType:
    identifier = "json"

    def indexable(self, backend: str) -> bool:
        return backend in {"postgres", "sqlite"} and self.identifier != "json"
```

The logical type now depends on concrete backend policy.

**Recommended pattern:**

```python
from typing import Protocol

class LogicalType(Protocol):
    identifier: str

class Backend:
    indexable_types = {"boolean", "integer", "short-text"}

    def indexable(self, dtype: LogicalType) -> bool:
        return dtype.identifier in self.indexable_types
```

Logical types stay logical. Backend-specific storage policy depends on the logical type abstraction.

## Related rules

Also apply [Open capability vocabulary](../../../examples/code/open-capability-vocabulary.md) for the reusable capability smell comparison, [model.md](model.md) for public mental model, [oop.md](oop.md) for method vocabulary, [files.md](files.md) for ownership-based layout, [clean.md](clean.md) for abstraction cost, [extension.md](../../project/extension.md) for registries, [error.md](error.md) for capability and contract failures, [arch-design.md](../../../tasks/arch-design.md) for architecture design/review tasks, and [architect.md](../../../workflows/architect.md) for design-only workflows.
