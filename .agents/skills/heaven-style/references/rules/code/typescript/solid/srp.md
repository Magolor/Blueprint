---
name: typescript-solid-srp
description: Read when applying single responsibility to TypeScript object and dependency boundaries.
---

# SRP: Single responsibility

## Summary

Separate reasons to change while keeping the ordinary user flow on its domain owner.

## Rule

A workspace can expose `upsert` without implementing validation, SQL dialects, and connection management itself. The public mental model stays small; private collaborators own independently changing policies. Split by responsibility, not one class per method.

- The entity owns construction and value invariants; the workspace owns workspace mutation policy; the backend owns persistence mechanics.
- Delegate through cohesive member methods. Do not replace one understandable object with public manager/factory/context plumbing.
- Keep independent utilities in the package's shared utils. Do not invent a helper class just to move a line.

## Pattern and Anti-pattern

These are illustrative API sketches. Domain types, package-owned utilities, configuration, composition, and unrelated method bodies are omitted. Production public methods also follow the language's annotation and documentation rules.

**Anti-pattern:**

```ts
class Workspace {
  async upsert(data: unknown): Promise<void> {
    // Parses transport data, chooses SQL dialect, connects, and writes.
  }
}
```

**Recommended pattern:**

```ts
const product = Product.fromJson(data)
await ws.upsert(product)

class Workspace {
  constructor(private readonly backend: ProductStore) {}

  async upsert(product: Product): Promise<void> {
    await this.backend.upsert(product)
  }
}
```

Changing a storage driver should change its adapter; changing product validation should change Product. Workspace coordinates its domain operation. Do not expose those collaborators merely because they exist internally.

## Review

Ask which requirement would change each object. If changing a product field, a storage dialect, and a transaction policy all edits the same implementation, separate those owners. If the caller must learn all of them to save a product, keep their composition behind Workspace.

Read the other [SOLID principles](../solid.md) together: shrinking the public mental model must preserve independent internal responsibilities.
