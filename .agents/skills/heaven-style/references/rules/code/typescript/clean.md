---
name: ts-clean
description: Read before extracting TypeScript one-liners, private helpers, or shared utilities.
---

# Helper cleanliness

## Summary

Reuse the package's own utilities first. Keep spontaneous specialized one-use code inline; put needed generic helpers in the package-wide or narrowest subgroup shared utility owner. Do not create small helpers in a single feature module.

## Ownership

1. Existing official package utility, including convenience contracts such as pj: use it.
2. Existing standard/runtime/dependency API when no package owner supplies the operation: use it directly.
3. Specialized one-use expression: write it inline with compact logical flow.
4. Needed generic helper without an existing equivalent: place it in shared utils even for its first consumer.
5. Substantial private feature boundary: give it a focused name and contract when extraction clarifies ownership.

Domain construction and mutation belong to their object member methods; helper cleanliness is not permission to move Entity.fromJson into a free-function factory. Follow [API](api.md).

**Anti-pattern:**

```ts
function joinDataPath(root: string, name: string): string {
  return join(root, 'data', `${name}.json`)
}

const path = joinDataPath(root, name)
```

**Recommended pattern:** the package already owns pj.

```ts
import { pj } from './utils.js'

const path = pj(root, 'data', `${name}.json`)
const activeNames = items.filter(item => item.active).map(item => item.name)
```

Do not extract activeNames into a module-local one-line wrapper just to name the expression. If a missing generic operation has a real current use, define it in shared utils with its reusable contract. Do not require a second caller or add speculative wrappers. Host and trust boundaries remain governed by [utilities](util.md).
