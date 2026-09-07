---
id: ts-solid-compose
title: TypeScript composition boundaries
description: Read for TypeScript composition boundaries.
blocking: true
---

# TypeScript composition boundaries

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

Each implementation supplies a concrete operation literal and payload schema. If fragments cross a registry, process, storage, or plugin boundary, carry a discriminator. Validate the payload before narrowing it at that boundary. Do not cast an arbitrary payload into the backend's fragment type.

### Make registry scope and lifecycle explicit

- Prefer injected registry instances owned by a workspace, app, request scope, or test.
- If a process-global registry is necessary, give bootstrap/freeze/reset semantics and prevent silent order dependence.
- Registration validates before mutation and returns a disposer or token when entries have an owner/lifetime.
- Do not rely on side-effect imports for ordinary registration. Internal-only variation may be wired in one composition root. An open external family uses explicit package registration. When the product needs managed discovery, it uses a descriptor/catalog path shared by bundled and external implementations.
- JavaScript's event loop does not make shared mutable state race-free. Serialize per-key operations or use transactional state changes where awaits can interleave.

### Separate durable authority from runtime composition

- A dependency-injection container, plugin context, event bus, or service registry owns live process composition. It is not a durable configuration/catalog authority.
- When the product persists descriptors or configuration, keep them serializable and inspectable without constructing services or executing modules.
- Let one explicit composition root read validated resolved specs. That root creates runtime instances, publishes them after successful startup, and awaits their disposal.
- Do not persist constructors, callbacks, service instances, or framework context identity. Persist stable data that a resolver can interpret through an explicit contract.
