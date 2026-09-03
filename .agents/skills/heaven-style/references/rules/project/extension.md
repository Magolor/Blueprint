---
id: extension
title: Extension points
enabled: true
blocking: false
order: 450
category: project
keywords: [plugin, extension api, extension parity, registry, catalog, entry point, manifest, discovery, capability registration, provider, backend, lifecycle]
description: Use when adding or reviewing open extension families, plugin contracts, registries, manifests, discovery/load paths, providers, backends, handlers, strategies, capabilities, or bundled/external parity.
---

# Extension Points

## Core rule

First decide whether variation is closed, internally composed, package-extensible, or installation-managed. Do not build an extension platform for a closed protocol or a handful of implementations controlled by one composition root.

When a product promises independent third-party extensions, bundled and external implementations should use the same public family contract and consumer path. Origin may affect trust or installation policy, but should not silently create a second dispatch or validation model.

Parity does **not** require every repository to own a persisted registry, remote catalog, artifact store, or hot-reload lifecycle. Select only the machinery required by the public promise.

## Choose the mechanism by promise

### Closed protocol

Use a discriminated union, exhaustive switch, or fixed interface when variants change with the host and independent packages are not expected. The compiler should expose missing cases.

### Internal composition

Use one explicit composition root when all implementations ship with the application. A runtime map can support tests and dependency injection, but it need not pretend to be durable discovery.

### Package extension

Use public package exports or language entry points, explicit registration, a narrow runtime registry, contract validation, and a disposer/ownership token when independently installed packages contribute behavior. Test one bundled and one independently packed contribution through the same consumer-facing suite.

### Installation-managed ecosystem

Add serializable descriptors, durable catalog state, deterministic resolution, acquisition, integrity/trust policy, version compatibility, activation, rollback, and inert inspection only when the product promises restartable installation, remote discovery, multiple scopes, or managed upgrades.

The responsibilities remain distinct even if one facade coordinates them:

```text
discover -> admit/register -> resolve -> acquire -> load
        -> activate -> invoke -> dispose/retire
```

Not every system needs every step. Lookup must not install dependencies or execute remote code incidentally.

## General contract

- Define the smallest shared capability interface and stable identifier vocabulary.
- Keep high-level policy dependent on the capability contract, not concrete providers.
- Validate configuration and capability claims before publication or invocation.
- Make duplicate identifiers, precedence, replacement, ownership, and teardown deterministic.
- If registrations are removable, return an ownership token or disposer and make stale cleanup unable to remove a newer owner.
- Keep one extension cohesive: implementation, manifest/metadata, configuration schema, assets, tests, docs, and migrations live together where practical.
- Treat advertised capabilities as candidate facts. Runtime evidence and actual results determine what executed.
- Keep interface code and adapters from reaching upward into planners, UIs, or unrelated domains.

## Discovery and trust

- Prefer metadata discovery that does not evaluate implementation code when listing or inspection is a product capability.
- Resolve only constrained package/subpath, language entry-point, or verified artifact coordinates; do not import arbitrary untrusted strings.
- Keep dependency installation outside import/lookup.
- Pin and integrity-check executable artifacts when acquisition is managed by the product.
- Distinguish durable descriptors from process-local loaded objects and caches.
- Reserve protected provenance for the installer/host; extensions do not self-assert privileged origin.

These rules are unnecessary for a simple explicit import at a trusted composition root. Do not add a catalog merely because the vocabulary contains “plugin.”

## TypeScript guidance

- Package `exports`, ordinary dependencies, and dynamic `import()` are loading primitives. Add a registry/catalog only when selection, inspection, scope, or lifecycle needs one.
- Keep registration explicit and side-effect imports exceptional; a package import should not start I/O or mutate unrelated global state.
- Validate external manifests as `unknown` before use.
- Keep runtime registration scope explicit and dispose it deterministically.
- Test public packages from tarballs when independent installation is part of the promise; workspace aliases do not prove the artifact.

## Python guidance

- PyPA entry points are a standard package-discovery adapter. They do not automatically provide persistence, trust policy, acquisition, or activation semantics.
- Prefer explicit registration or entry-point enumeration over arbitrary directory scans at every startup.
- Use `importlib.resources` or the declared package resource API for bundled assets.
- Keep ordinary imports ordinary; constrain any custom finder/loader to a reserved extension namespace.

## Avoid

- A central concrete-provider switch for a family advertised as independently extensible.
- A privileged built-in loader while external contributions use another path.
- A persisted catalog for internal-only variation with no restartable discovery need.
- Import-time self-registration as the only discovery mechanism.
- Runtime lookup that installs dependencies, mutates environments, or executes remote code.
- “Hot reload” without explicit ownership, teardown, and conflict semantics.
- A package-per-provider topology created only for visual symmetry.

## Fitness checks

Choose checks that match the advertised promise:

- **All extension families:** shared contract tests, deterministic selection, failure isolation, and cleanup.
- **Independent packages:** install one packed external implementation without host source edits and run the same consumer suite as a bundled implementation.
- **Inspectable catalogs:** list descriptors without importing implementations and prove aliases/version/scope conflicts resolve deterministically.
- **Managed artifacts:** verify integrity, failed acquisition/publication rollback, restart recovery, and stale-owner safety.
- **Capability routing:** report the implementation and fallback actually used rather than repeating metadata claims.

## Related rules

For TypeScript, apply [architecture](../code/typescript/architecture.md), [API design](../code/typescript/api.md), [modules](../code/typescript/modules.md), [types](../code/typescript/types.md), and [compatibility](../code/typescript/compat.md). For Python, apply [files](../code/python/files.md), [SOLID](../code/python/solid.md), and [mental model](../code/python/model.md). Apply [interfaces](interfaces.md) when an interface exposes the extension and [tests](test.md) for contract and artifact evidence.
