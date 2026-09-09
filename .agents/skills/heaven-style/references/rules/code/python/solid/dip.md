---
name: python-solid-dip
description: Read when applying dependency inversion to Python object and dependency boundaries.
---

# DIP: Dependency inversion

## Summary

Domain policy depends on stable role contracts; concrete providers implement those contracts.

## Rule

Keep high-level domain behavior on the owning object and inject the small collaborator it needs. OOP ownership does not mean a workspace must construct a hard-coded provider or import provider-specific APIs.

- Define the contract where its consumer's domain meaning belongs.
- The explicit composition boundary resolves config and creates concrete implementations; high-level policy consumes the resulting contract.
- Provider adapters own SDK types, credentials, connections, and dialect details. Do not leak provider rows through the domain API.
- Prefer an ordinary constructor argument over a service locator or dependency-injection framework when it is sufficient.

## Pattern and Anti-pattern

These are illustrative API sketches. Domain types, package-owned utilities, configuration, composition, and unrelated method bodies are omitted. Production public methods also follow the language's annotation and documentation rules.

**Anti-pattern:**

```python
class Workspace:
    def __init__(self):
        self._backend = PostgresStore()  # Domain policy selects a concrete driver.
```

**Recommended pattern:**

```python
from typing import Protocol


class ProductStore(Protocol):
    def upsert(self, product: Product) -> None: ...

class Workspace:
    def __init__(self, backend: ProductStore) -> None:
        self._backend = backend

    def upsert(self, product: Product) -> None:
        self._backend.upsert(product)
```

Workspace can operate with a different conforming store without importing that driver. The caller still uses ws.upsert(product). Dependency inversion changes internal coupling while preserving the minimal user mental model.

## Review

Trace imports and construction from the domain owner. Provider imports belong to the adapter or composition boundary. Replace the concrete collaborator with a conforming implementation without changing domain policy or the public member-method flow.

Read the other [SOLID principles](../solid.md) together: shrinking the public mental model must preserve independent internal responsibilities.
