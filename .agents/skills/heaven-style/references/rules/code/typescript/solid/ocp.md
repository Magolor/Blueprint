---
name: typescript-solid-ocp
description: Read when applying open/closed to TypeScript object and dependency boundaries.
---

# OCP: Open/closed

## Summary

Let an open implementation family grow without editing its callers or central dispatch.

## Rule

Keep one stable, domain-shaped operation. An open family gains implementations through its established registration or injection contract. Bundled and independent implementations follow the same contract when independent extension is promised.

- Concrete providers own their metadata and provider-specific policy.
- Use package configuration for selection; do not embed a tunable default backend name in a signature.
- An intentionally closed vocabulary can use an exhaustive branch. OCP does not require a persistent registry for every variation.

## Pattern and Anti-pattern

These are illustrative API sketches. Domain types, package-owned utilities, configuration, composition, and unrelated method bodies are omitted. Production public methods also follow the language's annotation and documentation rules.

**Anti-pattern:**

```ts
class Workspace {
  async upsert(product: Product): Promise<void> {
    if (this.provider === 'sqlite') { /* provider code */ }
    else if (this.provider === 'postgres') { /* provider code */ }
  }
}
```

**Recommended pattern:**

```ts
class Workspace {
  constructor(private readonly backend: ProductStore) {}

  async upsert(product: Product): Promise<void> {
    await this.backend.upsert(product)
  }
}

const backend = backends.get(cfg.get('storage.backend'))
const ws = new Workspace(backend)
```

A new provider implements ProductStore and joins the family at composition or registration. Workspace.upsert stays unchanged. Verify this with one real alternative when the family promises extensibility; do not build speculative provider matrices.

## Review

Add a real alternative implementation through the promised extension contract. Existing callers and the high-level dispatch path should stay unchanged. Check that bundled providers have no privileged selection path and that a deliberately closed set remains visibly closed.

Read the other [SOLID principles](../solid.md) together: shrinking the public mental model must preserve independent internal responsibilities.
