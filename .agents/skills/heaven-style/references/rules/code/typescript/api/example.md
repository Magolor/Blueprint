---
name: ts-api-example
description: Read when choosing TypeScript entity factories, member methods, and workspace operations.
---

# TypeScript OOP examples

## Summary

Minimize the user mental model by putting operations on the domain objects users already know. Prefer member methods as much as possible, including static construction and pure conversion.

## Domain construction and conversion

The entity owns its representation contract, validation, and construction. Callers discover one canonical conversion family on that entity.

**Anti-pattern:**

```ts
const entity = construct_entity_from_json(data)
const dataOut = entity_to_json(entity)
```

**Recommended pattern:**

```ts
const entity = Entity.fromJson(data)
const dataOut = entity.toJson()
```

Pure conversion still belongs to the domain object. Keep construction and export aligned; do not add a free-function synonym alongside the recommended method.

## Workspace mutation

The workspace owns its mutation scope, configuration, transaction policy, and backend. Express the operation as a member method.

**Anti-pattern:**

```ts
await upsert(ws, product)
```

**Recommended pattern:**

```ts
await ws.upsert(product)
```

Here `product` is an instance. If the domain also supports an entity class or descriptor such as `Product`, use `ws.upsert(Product)` with a documented schema/definition contract. Do not confuse class registration with row mutation or add an overload unless both operations are real product requirements. `Workspace` is the class; `ws` is the scope-owning instance, rather than an implicit global workspace.

## Small mental model, cohesive internals

**Pattern:** `product = Product.fromJson(data); await ws.upsert(product)` in TypeScript, or `product = Product.from_json(data); ws.upsert(product)` in Python. The caller learns the entity and workspace. The workspace may delegate privately to a store, validator, or transaction object, each with its own responsibility.

**Anti-pattern:** require the caller to construct an entity factory, mutation context, backend selector, and upsert manager to save one product. Also avoid placing every backend implementation inside Workspace merely to reduce the public class count. Apply [SOLID](../solid.md) to internal boundaries while keeping the public flow cohesive.

## Independent utilities

**Pattern:** use the package-owned `pj(root, name)` for path construction, or a shared domain-independent normalization function.

**Anti-pattern:** invent `PathJoinManager.create().join(root, name)`, or use the utility exception to move `Entity.fromJson` into `construct_entity_from_json`.

These examples illustrate API ownership; they do not prescribe storage semantics, framework dependencies, or hidden constructor I/O.
