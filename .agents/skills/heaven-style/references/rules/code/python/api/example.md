---
name: py-api-example
description: Read when choosing Python construction, registration, or fluent APIs.
---

# Python API examples

## Summary

Compare owning-object APIs with extra factories, lifecycle flags, and wrapper classes.

## Constructor side effects

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

## Domain construction and conversion

The entity owns its representation contract, validation, and construction. Callers discover one canonical conversion family on that entity.

**Anti-pattern:**

```python
entity = construct_entity_from_json(data)
data_out = entity_to_json(entity)
```

**Recommended pattern:**

```python
entity = Entity.from_json(data)
data_out = entity.to_json()
```

Pure conversion still belongs to the domain object. Keep construction and export aligned; do not add a free-function synonym alongside the recommended method.

## Workspace mutation

The workspace owns its mutation scope, configuration, transaction policy, and backend. Express the operation as a member method.

**Anti-pattern:**

```python
upsert(ws, product)
```

**Recommended pattern:**

```python
ws.upsert(product)
```

Here `product` is an instance. If the domain also supports an entity class or descriptor such as `Product`, use `ws.upsert(Product)` with a documented schema/definition contract. Do not confuse class registration with row mutation or add an overload unless both operations are real product requirements. `Workspace` is the class; `ws` is the scope-owning instance, rather than an implicit global workspace.

## Small mental model, cohesive internals

**Pattern:** `product = Product.fromJson(data); await ws.upsert(product)` in TypeScript, or `product = Product.from_json(data); ws.upsert(product)` in Python. The caller learns the entity and workspace. The workspace may delegate privately to a store, validator, or transaction object, each with its own responsibility.

**Anti-pattern:** require the caller to construct an entity factory, mutation context, backend selector, and upsert manager to save one product. Also avoid placing every backend implementation inside Workspace merely to reduce the public class count. Apply [SOLID](../solid.md) to internal boundaries while keeping the public flow cohesive.

## Independent utilities

**Pattern:** use the package-owned `pj(root, name)` for path construction, or a shared domain-independent normalization function.

**Anti-pattern:** invent `PathJoinManager.create().join(root, name)`, or use the utility exception to move `Entity.fromJson` into `construct_entity_from_json`.

These examples illustrate API ownership; they do not prescribe storage semantics, framework dependencies, or hidden constructor I/O.
