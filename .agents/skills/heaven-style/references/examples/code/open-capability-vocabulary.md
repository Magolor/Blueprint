---
id: example-open-capability-vocabulary
title: Open capability vocabulary
enabled: true
order: 10
keywords: [code smell, design smell, capability, registry, open extension, OCP, ISP, plugin architecture]
description: Read when an extensible family keeps gaining hard-coded feature fields, feature-specific methods, switches, or unvalidated extra dictionaries.
---

# Open capability vocabulary

Use this example when third parties may add new kinds of optional behavior. The design test is simple:

> Can one extension add a capability without editing the central value type or growing the base interface?

If the vocabulary is intentionally closed, use an enum, discriminated union, or exhaustive match instead. A registry is not automatically better.

## Bad smell: the extension edits the center

```ts
interface BackendCapabilities {
  readonly search: boolean
  readonly graph: boolean
  readonly batchMode: 'none' | 'native'
  readonly extra: Readonly<Record<string, unknown>>
}

class Backend {
  readonly capabilities: BackendCapabilities

  constructor(capabilities: BackendCapabilities) {
    this.capabilities = capabilities
  }

  supportsSearch(): boolean {
    return this.capabilities.search
  }

  supportsGraph(): boolean {
    return this.capabilities.graph
  }
}
```

Smells:

- Every new feature adds a field to one central class.
- The shared interface gains one accessor or predicate per feature.
- Serialization, cloning, docs, and inspection tend to repeat the same feature list.
- `extra` creates a second, unvalidated capability system.
- Provider-specific vocabulary leaks into the abstraction all providers inherit.

The decisive smell is change amplification: adding one optional feature forces unrelated central edits.

## Good smell: the extension supplies a descriptor

```ts
interface Capability<T> {
  readonly id: string
  readonly defaultValue: T
  readonly parse: (value: unknown) => T
  readonly description: string
}

interface CapabilityRegistry {
  register<T>(capability: Capability<T>): Capability<T>
}

interface CapabilityValues {
  get<T>(key: Capability<T>): T
}

interface Backend {
  readonly declared: CapabilityValues
  capability<T>(key: Capability<T>): T
  supports(key: Capability<boolean>): boolean
}

declare class CapabilityBackend implements Backend {
  readonly declared: CapabilityValues
  capability<T>(key: Capability<T>): T
  supports(key: Capability<boolean>): boolean
}
```

An extension declares its own vocabulary and data:

```ts
declare const registry: CapabilityRegistry
declare function capabilityValues(
  values: ReadonlyArray<readonly [Capability<unknown>, unknown]>,
): CapabilityValues

function requireBoolean(value: unknown): boolean {
  if (typeof value !== 'boolean') throw new TypeError('expected boolean')
  return value
}

const SEARCH = registry.register({
  id: 'search',
  defaultValue: false,
  parse: requireBoolean,
  description: 'Whether search is complete and native.',
})

class SearchBackend extends CapabilityBackend {
  override readonly declared = capabilityValues([[SEARCH, true]])
  // The shared base resolves generic capability values and runtime overrides.
}
```

In Python, express the same ownership with typed immutable descriptors, protocol/generic contracts, and validated mappings. Do not copy TypeScript syntax or add a registry to an intentionally closed vocabulary.

Good smells:

- The base protocol stays small: generic read, Boolean support, and runtime override hooks.
- One descriptor owns identity, defaulting, validation, documentation, and serialization policy.
- Static declarations are data; live facts use one generic override mapping.
- Consumers depend on the descriptor they understand, not on provider names.
- A structured capability can use its own focused immutable value type without closing the whole vocabulary.
- Inspection can publish descriptor definitions separately from resolved instance values.

## Review heuristic

For an open extension family, trace the smallest plausible new capability.

- **Bad smell:** it modifies a central capability type, base method list, provider switch, serializer list, and metadata list.
- **Good smell:** it registers one descriptor, declares or overrides one value, and updates only the consumer that understands it.

Prefer the good-smell shape only when independent extensions genuinely own new identifiers. Keep closed domains closed.
