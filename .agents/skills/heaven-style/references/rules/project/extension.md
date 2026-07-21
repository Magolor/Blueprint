---
id: extension
title: Extension points
enabled: true
blocking: false
order: 130
category: project
keywords: [plugin, extension api, lego-style extension, extension parity, registry, persisted registry, entry point, manifest, discovery, capability registration, provider, backend, builtin, remote extension]
description: Use when adding or reviewing open extension families, registries, plugin manifests, discovery/load paths, providers, backends, handlers, strategies, capabilities, or built-in/external parity.
---

# Extension points

## Core rule

Apply this rule only to a genuinely open extension family: one that independent developers are expected to extend without coordinating a host-package edit. Closed syntax trees, protocols, and state machines use exhaustive variants instead; a Registry is not automatically better.

For an open family, enforce **Lego-style extension parity**:

> Bundled and independently developed implementations are peers. An extension may be authored, packaged, stored, and registered outside the host source tree without modifying or releasing the host package. Consumers discover, select, configure, inspect, validate, load, activate, invoke, and test it through the same contracts and runtime path used for bundled implementations.

Origin is metadata, not a routing rule. Trusted installation policy may assign provenance such as `system`, `local`, or `remote`, but origin alone must not change dispatch, validation, capabilities, lifecycle, configuration, or user-facing syntax.

## Apply when

- Code adds or reshapes providers, backends, handlers, strategies, logical types, entities, serializers, plugins, capabilities, registries, or other open families.
- Code changes discovery, manifests, entry points, persistence, loading, activation, planner/router layering, import bootstrap, or registration APIs.
- Bundled implementations use package folders, explicit import lists, self-registration side effects, or a composition root that external implementations cannot use.
- An implementation may live in another distribution, local folder, artifact cache, remote catalog, or a Registry-embedded declarative definition.

## Registry contract

Use one logical Registry view per declared environment as the authoritative catalog of extension descriptors. “Global” means every consumer of that extension family resolves through the same logical authority; it does not require one physical machine-wide database or one mutable process-global service locator.

A descriptor should carry the fields needed for deterministic resolution, normally:

- namespaced kind and canonical identifier;
- implementation version and host-contract compatibility;
- entry point, artifact coordinate, or schema-validated inline definition;
- declared capabilities and configuration schema reference;
- provenance, publisher, integrity, trust, and installation scope;
- enablement plus lifecycle or migration state where relevant.

The uniform path is:

```text
extension reference -> persisted catalog -> deterministic resolver
  -> verified artifact/definition -> loader -> contract validation -> runtime instance
```

Keep these responsibilities distinct even when one public `Registry` facade coordinates them:

1. **Discovery** finds descriptors without importing or executing implementation code.
2. **Registration** validates and atomically persists one descriptor.
3. **Resolution** selects one enabled, compatible version under explicit scope and conflict rules.
4. **Acquisition** materializes a local artifact when the selected descriptor is not already available.
5. **Loading** resolves the entry point lazily.
6. **Activation** validates the runtime contract, configuration, capabilities, and lifecycle.
7. **Invocation** depends only on the shared family contract.
8. **Retirement** disables, upgrades, rolls back, unregisters, or uninstalls safely.

The persisted catalog and in-process runtime cache are related but not the same mutable singleton. Applications, workspaces, tenants, tests, and concurrent processes may need isolated runtime views over the same durable descriptors.

Persisted descriptors are authoritative data; loaded objects are disposable caches. Prefer data-backed listing and inspection that does not import or execute an implementation merely to describe it.

Capability declarations advertise candidates, not successful execution. When a route claims native or provider-specific behavior, require operation-specific compilation, a real provider candidate, and evidence tied to the concrete physical field/resource being executed. Missing, malformed, or stale evidence fails closed. Explanations and diagnostics must report the route actually selected, including fallback, rather than repeating advertised capability metadata.

## Do

- Keep dependency flow inward/downward according to the repository's documented layers; high-level policy depends on extension contracts and the resolver, never concrete implementations.
- Make bundled implementations publish the same descriptor or manifest and enter through the same resolver/loader used by external implementations. Their package folder is an ownership boundary, not a discovery privilege.
- Keep one extension cohesive: colocate its manifest, implementation, configuration schema, assets, tests, docs, and migrations where practical. Shared libraries remain ordinary dependencies rather than duplicated code.
- Use stable artifact and entry-point coordinates. Treat machine-specific paths as locators, not identities.
- Define deterministic duplicate, alias, version, scope-precedence, enablement, refresh, cache-invalidation, and rollback behavior.
- Make registration atomic, persistent, auditable, and reversible. “Register at any time” means no host source edit and activation at the next documented refresh boundary; hot replacement is an optional family capability.
- Stage discovery, validation, acquisition, and initialization before publishing a descriptor or default. On failure, restore only state still owned by the failed operation; stale cleanup must not dislodge a newer registration or owner.
- Treat generated catalogs, capability tables, and loaded-object indexes as non-authoritative projections. Content-address them where practical and record the source revision or digest so unchanged projections are not republished and stale evidence is detectable.
- Keep discovery and inspection free of arbitrary code execution. Remote catalogs advertise candidates; they do not imply installation, trust, enablement, or execution.
- Pin and integrity-check executable artifacts before loading them. Inline Registry content should normally be schema-validated declarative data; embedded executable code receives the same trust treatment as any other executable artifact.
- Reserve a minimal bootstrap kernel for the Registry schema, resolver/loader contracts, trust policy, and one bootstrap path; the extension system must not require itself to load itself.
- Add a shared contract suite plus a parity fitness test that extracts one bundled implementation into an independent artifact and proves consumer-facing tests remain unchanged.

## Avoid

- A central provider switch, router edit, union, built-in table, or handwritten import list for every new implementation.
- A built-in-only loader or validation path even when runtime dispatch later uses a Registry.
- Treating import-time self-registration as the discovery mechanism. It can populate runtime state only after catalog resolution has deliberately loaded that extension.
- Scanning a privileged host-package subfolder while requiring external developers to use another mechanism.
- Replacing ordinary language imports with an unrestricted global import hook.
- Installing dependencies, mutating environments, or executing remote code as an incidental effect of lookup or import.
- Allowing extensions to self-assert protected provenance such as `system` or silently shadow another identifier.
- Backend or adapter code that reaches up into planner, user DSL, CLI, or UI concerns.

## Python package guidance

For installed Python distributions, [PyPA entry points](https://packaging.python.org/en/latest/specifications/entry-points/) are a standard discovery adapter: a group identifies the extension family, a name identifies one contribution, and the object reference loads lazily through [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html#entry-points). Entry points do not by themselves supply the whole persisted Registry, trust policy, remote acquisition, activation lifecycle, or conflict policy.

- Resolve framework extension identifiers through the Registry first; do not make every ordinary Python import consult it.
- Prefer explicit registration, installation, or refresh indexing over scanning arbitrary directories at every startup.
- Use `importlib.resources` or the package's declared resource API for bundle assets rather than assuming a filesystem-relative package path.
- If transparent import syntax is required, constrain the finder/loader to a reserved extension namespace and preserve normal import semantics elsewhere.
- Keep dependency installation outside import-time resolution. The Registry should point to an installed or explicitly materialized artifact.

## Fitness checks

- Register and use an out-of-tree implementation without editing, rebuilding, or releasing the host package.
- Run the same family contract suite against one bundled and one external implementation.
- Move a bundled implementation to an external distribution or local bundle; consumer configuration, invocation, and assertions remain unchanged.
- Restart or open another process and recover the persisted descriptor under explicit refresh semantics.
- Prove duplicate identifiers, aliases, incompatible versions, disabled records, and scope precedence fail or resolve deterministically.
- List and inspect descriptors without importing their implementation modules.
- Prove provenance remains inspectable but does not select a different dispatch or validation path.
- Prove an advertised but unexecutable capability is rejected or honestly explained as fallback.
- Inject failure before publication and after a competing owner takes over; the previous valid state or newer owner must remain visible.

## Related rules

For Python, apply [Open capability vocabulary](../../examples/code/open-capability-vocabulary.md) when optional feature kinds form an open extension vocabulary, [files.md](../code/python/files.md) for cohesive bundle layout, [solid.md](../code/python/solid.md) for OCP/DIP/LSP checks, and [model.md](../code/python/model.md) for user-facing surfaces. For TypeScript, apply [architecture](../code/typescript/architecture.md) and [modules](../code/typescript/modules.md). Apply [interfaces.md](interfaces.md) when CLI, GUI, MCP, TUI, or service APIs expose an extension, and [test.md](test.md) for parity and contract evidence in either language.
