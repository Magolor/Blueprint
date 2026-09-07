---
id: py-api-example
title: Python API examples
description: Compare owning-object flows, registration, fluent fields, and plain data.
---

# Python API examples

### Constructor side effects

**Anti-pattern:**

```python
project = pkg.Project("shop", profile="debug", _isolated=False, _register_global=False, _set_default=True)
```

**Recommended pattern:**

```python
project = pkg.Project("shop", profile="debug")
project.set_default()
```

Constructor flags are acceptable only for essential construction policy. Lifecycle actions such as becoming the default workspace should be ordinary verbs.

### Build and register

**Anti-pattern:**

```python
pkg.ext.register_profile(
    pkg.ext.profile_spec_from_mapping(
        {
            "name": "agent",
            "tools": ["query", "search"],
        }
    )
)
```

**Recommended pattern:**

```python
pkg.ProfileSpec.from_dict(
    {
        "name": "agent",
        "tools": ["query", "search"],
    }
).register()
```

The spec owns construction from a mapping and registration into its registry. The user should not have to compose extension helper functions for the common path.

### Register an entity

**Anti-pattern:**

```python
class EntityRegistry:
    def register_entity(self, entity: type["Entity"]) -> None: ...

registry.register_entity(Product)
```

**Recommended pattern:**

```python
ws.register(Product)
```

When registration belongs to a workspace, keep the workspace as the owner. When registration belongs to the class or instance itself, expose `register` there:

```python
capsule.register()
toolkit.register()
```

### Fluent field declaration

**Anti-pattern:**

```python
sku = pkg.field(pkg.ShortText, store_to="sql", compute_fn=normalize_sku, description="Stock keeping unit")
```

**Recommended pattern:**

```python
sku = pkg.field(pkg.ShortText).store(to="sql").compute(normalize_sku).desc("Stock keeping unit")
```

Use chained methods when each step configures the same object and keeps the names discoverable in autocomplete.

### Data containers

**Anti-pattern:**

```python
class MetadataAttribute: ...
class Metadata: ...
class Data:
    metadata: Metadata
```

**Recommended pattern:**

```python
class Data:
    metadata: dict[str, object]

value = data.metadata["attr"]
```

Use a dedicated class only when it carries behavior, invariants, lifecycle, or a widely recognized domain concept. If the class only names one field, keep it as a field.
