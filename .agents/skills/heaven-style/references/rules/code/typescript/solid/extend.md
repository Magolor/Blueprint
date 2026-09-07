---
id: ts-solid-extend
title: TypeScript extension boundaries
description: Read for TypeScript extension boundaries.
blocking: true
---

# TypeScript extension boundaries

### Separate open and closed variation

- A **closed** set known to the compiler—an AST, protocol state, or result union—uses a discriminated union and an exhaustive `switch`.
- An **open** set expected to gain providers, backends, serializers, tools, or strategies uses a registry, injected map, or strategy object.
- Never dispatch an open provider family with `if (provider === ...)` or a central provider-name switch.
- For internal-only variation, one explicit composition root may enumerate implementations. A family that promises independent extensions gives bundled and external contributions the same public registration/selection contract. Add a catalog/resolver/loader only when installed discovery, inert inspection, or managed lifecycle requires it.

**Anti-pattern:**

```ts
function run(provider: string, request: Request): Promise<Result> {
  if (provider === 'sqlite') return runSqlite(request)
  if (provider === 'redis') return runRedis(request)
  throw new Error(`unknown provider: ${provider}`)
}
```

**Recommended pattern:**

```ts
interface Backend {
  readonly id: string
  run(request: Request): Promise<Result>
}

class BackendRegistry {
  readonly #items = new Map<string, Backend>()

  register(backend: Backend): () => void {
    if (this.#items.has(backend.id)) {
      throw new Error(`backend already registered: ${backend.id}`)
    }
    this.#items.set(backend.id, backend)
    let active = true
    return () => {
      if (!active) return
      active = false
      if (this.#items.get(backend.id) === backend) {
        this.#items.delete(backend.id)
      }
    }
  }

  get(id: string): Backend {
    const backend = this.#items.get(id)
    if (!backend) throw new Error(`unknown backend: ${id}`)
    return backend
  }
}
```

For a closed union:

```ts
type Expr =
  | { kind: 'value'; value: boolean }
  | { kind: 'not'; value: Expr }
  | { kind: 'and'; values: readonly Expr[] }

function assertNever(value: never): never {
  throw new Error(`unhandled expression: ${JSON.stringify(value)}`)
}

function evaluate(expr: Expr): boolean {
  switch (expr.kind) {
    case 'value': return expr.value
    case 'not': return !evaluate(expr.value)
    case 'and': return expr.values.every(evaluate)
    default: return assertNever(expr)
  }
}
```

Do not add an `assertNever` default to a deliberately merge-extensible/open union; document and test its fallback policy instead.

### Prefer capability facts over concrete names

- Providers own readonly, validated capability metadata.
- Routing asks what an implementation can do, not what its name is.
- Capability claims, runtime health, fallback reason, and actual execution mode must agree.
- An unavailable optional provider may remain inspectable, but data operations fail contextually; never return empty success or stale mirrored data.

**Anti-pattern:**

```ts
const supportsVector = backend.id === 'pgvector' || backend.id === 'lance'
```

**Recommended pattern:**

```ts
interface BackendCapabilities {
  readonly vectorSearch: boolean
  readonly transactions: boolean
}

if (!backend.capabilities.vectorSearch) {
  throw new UnsupportedCapabilityError('vector-search', { backend: backend.id })
}
```

### Keep interfaces role-specific

- The required base contract contains only behavior every implementation can honor.
- Split optional behavior into capability interfaces, adapters, or separate registries.
- Use structural guards when runtime selection needs to prove an optional capability.
- Do not add no-op methods or methods that exist only to throw “unsupported”.

```ts
interface RowBackend {
  get(id: RowId): Promise<Row | undefined>
  upsert(row: Row): Promise<void>
}

interface VectorSearch {
  nearest(vector: readonly number[], limit: number): Promise<readonly Match[]>
}

function hasVectorSearch(value: RowBackend): value is RowBackend & VectorSearch {
  return 'nearest' in value && typeof value.nearest === 'function'
}
```
