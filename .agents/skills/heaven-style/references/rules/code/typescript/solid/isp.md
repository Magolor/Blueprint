---
name: typescript-solid-isp
description: Read when applying interface segregation to TypeScript object and dependency boundaries.
---

# ISP: Interface segregation

## Summary

Expose the smallest honest role contract; keep optional capabilities out of the required base.

## Rule

An object should offer predictable member methods for its role. Do not force every backend to implement vector search, graph traversal, transactions, and storage merely to fit one base class.

- Keep common required behavior on the base contract.
- Model optional roles as narrow protocols/interfaces, capability-specific subclasses, or adapters.
- Resolve and validate a capability before invoking it. A boolean claim alone does not prove an implementation or the operation's physical prerequisites.
- Keep ordinary workspace use simple; extension authors can use richer role contracts without exposing that assembly to every caller.

## Pattern and Anti-pattern

These are illustrative API sketches. Domain types, package-owned utilities, configuration, composition, and unrelated method bodies are omitted. Production public methods also follow the language's annotation and documentation rules.

**Anti-pattern:**

```ts
class FileStore implements Backend {
  get(key: string): Product | undefined { /* ... */ }
  nearest(vector: readonly number[]): readonly Match[] {
    throw new Error('unsupported')
  }
}
```

**Recommended pattern:**

```ts
interface RowStore {
  get(key: string): Product | undefined
}

interface VectorSearch {
  nearest(vector: readonly number[]): readonly Match[]
}

// The resolved search object really implements this separate role.
const matches = search.nearest(vector)
```

FileStore implements RowStore alone. A vector implementation may implement both roles. Adding graph search does not add a throwing method to FileStore or enlarge every consumer contract.

## Review

For each required member, name a valid behavior every implementation provides. Move optional operations into their honest role if any implementation can only throw unsupported or return a no-op. Verify capability selection and its real prerequisites before use.

Read the other [SOLID principles](../solid.md) together: shrinking the public mental model must preserve independent internal responsibilities.
