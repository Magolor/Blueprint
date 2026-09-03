---
id: ts-architecture
title: TypeScript architecture
enabled: true
blocking: true
order: 20
category: code-quality
keywords: [TypeScript architecture, SOLID, registry, discriminated union, capability, adapter, strategy, composition root, lifecycle, durable authority, Bun]
description: Use when designing or reviewing TypeScript modules, public APIs, services, adapters, providers, registries, strategies, capabilities, or lifecycle boundaries.
---

# TypeScript Architecture

## Core rule

Apply Heaven-style's language-neutral architecture before TypeScript mechanics: keep the public mental model small, group code by reason to change, depend on stable contracts, register open-ended implementations, make lifecycle explicit, and verify important boundaries with executable checks.

Treat TypeScript as a primary Heaven-style language with its own structural type system, ESM/package graph, host runtimes, and async resource model. Keep state and lifecycle on the owning object, prefer a typed function for a stateless transform, and use structural interfaces and composition before inheritance. Python remains a peer surface for Python repositories; its language mechanics do not define TypeScript design.

## Precedence

1. The target repository's `AGENTS.md`, runtime contract, framework rules, checked-in package manager/lockfile, and release compatibility policy win.
2. Heaven-style architecture governs mental model, ownership, dependency direction, extension seams, and cleanliness unless the repository records a waiver.
3. The `ts-*` rules govern TypeScript utilities, API vocabulary, syntax, types, configuration, modules, docs, async/data behavior, compatibility, and environment. They supersede Python-only mechanics.
4. When none of those decide a tradeoff, choose the smallest design that satisfies the current verified change pressure and can be tested.

Apply TypeScript-native ownership directly. Python-specific utility owners, exception helpers, Google-style docstring sections, facade/stub mechanics, and pytest marker vocabulary remain on the Python side unless a mixed-language repository exposes an explicit interop contract.

## Apply when

- Adding or reshaping services, backends, providers, handlers, strategies, registries, event buses, package boundaries, or public APIs.
- Choosing a class versus a function, inheritance versus composition, a union versus a registry, or eager versus lazy integration loading.
- Adding resource acquisition, connection, cancellation, teardown, or process-global state.
- Reviewing dependency direction, import cycles, capability claims, extension registration, or architecture fitness tests.

## Boundary rules

### Keep one public front door

- Give users one obvious path for each task.
- Put behavior on the object that owns mutable state, identity, or lifecycle.
- Keep stateless parsing, normalization, compilation, and projection as typed functions unless a real domain object improves the model.
- Avoid public wrapper classes, factories, flags, DSLs, or aliases that merely rename another operation.
- Constructors validate and store identity/configuration. Use `static create`, `connect`, `start`, `close`, or `dispose` for work with I/O or asynchronous failure.
- Follow [TypeScript API design and vocabulary](api.md) for class/function choice, lookup/persistence verbs, collection protocols, guard clauses, nullish defaults, and helper cost.

**Anti-pattern:**

```ts
const backend = new RemoteBackend({ connect: true, register: true })
```

**Recommended pattern:**

```ts
const backend = new RemoteBackend(config)
await backend.connect()
registry.register(backend)
```

Use `static async create(config)` only when callers should receive an already-ready object and the creation failure is explicit in the returned promise.

### Separate open and closed variation

- A **closed** set known to the compiler—an AST, protocol state, or result union—uses a discriminated union and an exhaustive `switch`.
- An **open** set expected to gain providers, backends, serializers, tools, or strategies uses a registry, injected map, or strategy object.
- Never dispatch an open provider family with `if (provider === ...)` or a central provider-name switch.
- For internal-only variation, one explicit composition root may enumerate implementations. A family promising independent extensions gives bundled and external contributions the same public registration/selection contract; add a catalog/resolver/loader only when installed discovery, inert inspection, or managed lifecycle requires it.

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

### Split policy, compilation, and execution

- Declarative specs/strategies describe intent and remain readonly; they do not own clients, I/O, mutable caches, or provider dispatch.
- Pure compilers/handlers translate a logical request into a typed execution fragment.
- Adapters/backends own provider I/O and execute fragments; they do not parse the public DSL or query AST.
- Orchestration depends on these contracts and registries, never concrete providers.

```ts
interface StorageStrategy {
  readonly id: string
  readonly mode: 'inline' | 'side-table' | 'vector'
}

interface Fragment<K extends string, P extends object> {
  readonly backendId: string
  readonly operation: K
  readonly payload: Readonly<P>
}

type Compile<F extends Fragment<string, object>> =
  (request: QueryRequest, context: CompileContext) => F

interface Backend<F extends Fragment<string, object>> {
  execute(fragment: F): Promise<ResultFrame>
}
```

Each implementation supplies a concrete operation literal and payload schema. If fragments cross a registry, process, storage, or plugin boundary, carry a discriminator and validate before narrowing; do not cast an arbitrary payload into the backend's fragment type.

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
- Do not add no-op methods or methods that exist only to throw “unsupported.”

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

### Make registry scope and lifecycle explicit

- Prefer injected registry instances owned by a workspace, app, request scope, or test.
- If a process-global registry is necessary, give bootstrap/freeze/reset semantics and prevent silent order dependence.
- Registration validates before mutation and returns a disposer or token when entries have an owner/lifetime.
- Do not rely on side-effect imports for ordinary registration. Internal-only variation may be wired in one composition root; an open external family uses explicit package registration or, when the product needs managed discovery, a descriptor/catalog path shared by bundled and external implementations.
- JavaScript's event loop does not make shared mutable state race-free. Serialize per-key operations or use transactional state changes where awaits can interleave.

### Separate durable authority from runtime composition

- A dependency-injection container, plugin context, event bus, or service registry owns live process composition. It is not a durable configuration/catalog authority.
- When the product persists descriptors or configuration, keep them serializable and inspectable without constructing services or executing modules.
- Let one explicit composition root read validated resolved specs, create runtime instances, publish them after successful startup, and await their disposal.
- Do not persist constructors, callbacks, service instances, or framework context identity. Persist stable data that a resolver can interpret through an explicit contract.

### Keep dependency direction inward

- Domain policy and orchestration depend on contracts, not SDK clients, databases, UI frameworks, or generated artifacts.
- Volatile provider packages depend on stable interfaces.
- A package may import its own layer or a lower/stabler layer, never a higher composition/UI layer.
- Cross-layer/package cycles and initialization-order-dependent runtime cycles are blockers. A proven intrinsic local cycle needs explicit ownership and a fitness test; otherwise split the misplaced responsibility.
- Use a workspace/package graph check for multi-package repositories; do not rely on reviewer memory.

### Keep optional integrations lazy

- Entry modules and barrels are side-effect-free.
- Optional SDKs load inside the selected adapter's creation/connect path, usually with `await import(...)`.
- A missing optional dependency throws an actionable error naming the feature and install path.
- Published packages expose optional integrations through explicit subpath exports rather than importing all providers from the root.

## Architecture fitness tests

When a boundary is important enough to be a rule, add the smallest executable check that proves it:

- one shared contract suite for every implementation of an interface;
- late registration without central router edits;
- alias/canonical identifier normalization;
- capability-driven routing and truthful unsupported behavior;
- package-root import without loading optional SDKs;
- explicit registry scope and deterministic duplicate handling;
- built/packed consumer test for published entry points;
- dependency-cycle or module-graph check for a real package graph.

Do not create abstract layers or test matrices for imagined implementations. Add the seam when real variation, lifecycle, ownership, or repeated change pressure exists.

## Review checks

- Can a newcomer describe the public flow in one sentence?
- Does every module/class have one reason to change?
- Is open variation registered and closed variation exhaustive?
- Do high-level modules avoid concrete provider imports?
- Are optional capabilities separated from the base contract?
- Are constructors free of hidden I/O and lifecycle effects?
- Does each registry have an owner, scope, duplicate policy, and cleanup story?
- Are capability/fallback claims observable and truthful?
- Is the clean extension path easier than a central shortcut?
- Does at least one focused test enforce each mandatory boundary?

## Related rules

Also apply [utilities and platform APIs](util.md), [API design and vocabulary](api.md), [types.md](types.md), [config.md](config.md), [modules.md](modules.md), [async.md](async.md), [SQL and data access](sql.md), [docs.md](docs.md), [compatibility](compat.md), and [environment.md](environment.md) according to the touched surface. Apply [../../project/extension.md](../../project/extension.md) for open extension work and [../../project/interfaces.md](../../project/interfaces.md) for service roles, package boundaries, and interface layers.
