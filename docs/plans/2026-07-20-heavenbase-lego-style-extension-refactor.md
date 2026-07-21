# HeavenBase Lego-Style Extension Refactor Route

- Status: Superseded
- Created: 2026-07-20
- Historical target: HeavenBase `0.1.2.0`; the current route is owned by HeavenBase on its default branch
- Scope: Replace source-tree-privileged component discovery with one persisted, source-neutral component catalog while preserving the current consumer-facing identifier/configuration model.
- Depends on: `docs/plans/2026-07-20-lego-style-extension-parity.md`
- Path convention: All source and test paths below are relative to the HeavenBase repository root.

This Blueprint-local planning copy is no longer active. HeavenBase owns the accepted route in [ADR 0011](https://github.com/Magolor/HeavenBase/blob/master/docs/resources/architecture/adr/0011-standalone-registry-and-lego-resolution.md); future task state belongs to HeavenBase's canonical queue.

## Outcome

An extension author can keep a cohesive bundle outside the `heavenbase` distribution, register it into a declared Context, and then use its backend, logical type, strategy, entity bundle, handler contribution, or other open component exactly as a bundled implementation is used. Bundled status remains visible as trusted provenance such as `builtin` or `system`; it does not select a privileged loader, validation path, runtime registry, public API, or test suite.

The decisive release gate is extraction: move one representative bundled provider to a package-external fixture or distribution and run the same consumer assertions without changing identifiers, configuration, invocation, or expected results.

## Current Evidence

HeavenBase already has strong pieces to preserve:

- `src/heavenbase/utils/registry/registry.py` provides immutable copy-on-write snapshots, aliases, groups, persistence hooks, CAS conflict detection, and integrity checks.
- `src/heavenbase/context.py` is already the composition root and memoizes persistent Registry namespaces.
- Narrow domain registries and public authoring protocols already exist for backends, logical types, strategies, handlers, extensions, storage profiles, serializers, toolkits, and related families.
- `sys-metaschema` exposes registered vocabulary for inspection, and subprocess tests already protect lazy imports.

The remaining privileged paths are concrete and removable:

- `src/heavenbase/_bootstrap.py` imports a fixed inventory of built-in logical types and strategies.
- `src/heavenbase/backends/registry.py` owns `_BUILTIN_BACKEND_MODULES`, `_PROVIDER_DEFAULT_ALIASES`, and provider-priming state.
- `src/heavenbase/handlers/plugins.py` imports a fixed provider module tuple.
- `src/heavenbase/extensions/bootstrap.py` imports a fixed extension-factory tuple.
- Several other open vocabularies self-register as import side effects; `src/heavenbase/entity/base.py` keeps process-only `_PENDING` classes.
- `src/heavenbase/context.py` opens the selected data Backend before any persistent Registry and resolves that Backend by a hard-coded module path from bootstrap configuration.
- `src/heavenbase/registry/_backend.py` persists Registry state through HeavenBase `Backend`, `EntitySchema`, concrete logical types, `StorageBinding`, and `InlineColumn`.

The final two points create the bootstrap cycle: a Registry-first component catalog is needed to resolve the data Backend, but the current persistent Registry needs that data Backend—and multiple extensible components—before it can load.

## Non-Negotiable Invariants

1. **Same path, not equivalent paths.** Built-in and external components produce the same descriptor, enter the same catalog, resolve through the same loader, validate against the same contract, publish into the same runtime projection, and run the same contract tests.
2. **Context ownership.** A `Context` owns the Registry store, component catalog, resolver/loader, runtime caches, configuration, and selected data Backend. “Global Registry” means one authoritative logical catalog for that Context/environment, not an uncontrolled Python process singleton.
3. **Descriptor-first discovery.** `list`, `show`, search, compatibility checks, and conflict resolution read JSON-safe descriptors without importing implementation modules.
4. **No global import hook.** Registry-first applies to HeavenBase component resolution. Ordinary Python imports keep normal semantics.
5. **Explicit acquisition.** Lookup never downloads, installs, changes `sys.path`, or executes remote code. Remote artifacts are explicitly acquired into a local content-addressed cache, verified, and only then registered/activated.
6. **Atomic bundles.** All contributions declared by one bundle are accepted or rejected in one Registry revision. Runtime publication also succeeds as one activation unit or publishes nothing.
7. **Deterministic ownership.** Duplicate identifiers, aliases, replacement, compatibility, scope, disablement, and refresh have explicit rules. Built-ins never silently win, and import/path order never decides.
8. **Stable usage.** Existing identifier-driven calls such as `BackendType.load(...)`, logical-type/strategy lookup, backend configuration, and `workspace.enable_extension(...)` remain the consumer model. External items require no alternate prefix or loader call.
9. **Minimal kernel only.** Bootstrap parsing, raw Registry persistence, component descriptor schemas, trust policy, and resolver interfaces remain directly importable. The kernel is deliberately closed and cannot depend on an extensible HeavenBase component.
10. **No permanent dual system.** Each migration slice may use a short-lived branch-local bridge, but its exit gate removes the corresponding fixed inventory or import side effect. Durable state migration uses a one-shot tool, not a forever compatibility backend.

## Target Architecture

```text
minimal bootstrap.yaml
        |
        v
stdlib-only RegistryStore  <---- SQLite file + atomic CAS
        |
        v
persisted ComponentCatalog <---- ComponentSpec / BundleSpec only
        |
        v
Resolver -> optional explicit acquisition -> Loader -> contract validation
        |
        v
Context-scoped runtime projections and instance caches
        |
        v
selected data Backend -> workspaces -> enabled extensions
```

### Kernel boundary

Add a raw storage protocol that knows only namespace, revision, bytes, digest, and compare-and-set:

```python
class RegistryStore(Protocol):
    def read(self, namespace: str) -> StoredSnapshot | None: ...
    def compare_and_set(
        self,
        namespace: str,
        *,
        expected_revision: int,
        payload: bytes,
        digest: str,
    ) -> int: ...
```

The first implementation should use stdlib `sqlite3`, one row per Registry namespace, transactions, and a schema version. It must not import anything from backends, schema, types, strategies, ConfigManager, extensions, or optional dependencies. SQLite here is bootstrap infrastructure, not a selectable HeavenBase data Backend.

Refactor `Registry.load(...)` to accept `store=` rather than `backend=`. Keep snapshot encoding, key/value codecs, limits, digest checks, and CAS semantics in the Registry layer; keep byte persistence in the store. Add one atomic batch mutation API so a catalog can register or remove an entire bundle with one snapshot commit.

### Persisted contracts

Create `src/heavenbase/components/` as the single owner of extension metadata and activation behavior:

- `spec.py`: immutable, JSON-safe `ComponentKey`, `ComponentSpec`, `ComponentSource`, compatibility, provenance, and activation state.
- `bundle.py`: `BundleSpec`, manifest parsing, dependency/contribution validation, and bundle fingerprinting.
- `catalog.py`: catalog queries, atomic bundle registration/removal, aliases/groups, refresh, enable/disable, and revision snapshots.
- `resolver.py`: deterministic `(kind, identifier)` selection and dependency graph planning.
- `loader.py`: source-specific loading, contract validation, fingerprint cache, and runtime projection publication.
- `sources/`: installed Python object/entry-point, local bundle, acquired artifact, and typed embedded-definition adapters.
- `errors.py`: catalog conflict, compatibility, trust, acquisition, dependency-cycle, load, and contract errors.

For the first release, one Context has one selected record for each `(kind, canonical_identifier)`. `ComponentSpec.version` and compatibility fields are recorded, but do not build a general multi-version dependency solver. Replacement is explicit and optimistic: the caller supplies the expected catalog revision or prior component fingerprint.

Minimum `ComponentSpec` fields:

| Field | Purpose |
|---|---|
| `kind`, `identifier`, `aliases` | Stable source-neutral identity and lookup. |
| `bundle`, `version` | Cohesive ownership/release unit and implementation version. |
| `host_compat`, `python_compat` | Reject incompatible records before import. |
| `families`, `capabilities`, `config_schema` | Planner/inspection metadata available without loading code. |
| `source.kind`, `source.location`, `entry_point` | Installed object, local bundle, verified artifact, or typed embedded payload. |
| `digest`, `publisher`, `provenance`, `tags` | Integrity, attribution, and policy metadata. |
| `dependencies`, `enabled` | Activation graph and lifecycle state. |
| `payload` | Bounded schema-validated declarative content only; executable content uses an artifact or trusted Capsule reference. |

`BundleSpec` owns a bundle ID/version, compatibility, source root/artifact, and an ordered set of component contributions. Registration validates every contribution and alias first, then commits all catalog records in one CAS operation.

### Resolution and loading

Every open-family lookup follows this sequence:

1. Normalize `(kind, identifier)` and read one catalog revision.
2. Resolve aliases and require exactly one enabled compatible descriptor.
3. Resolve the complete dependency graph without importing code; reject cycles with a full path.
4. Require the artifact to be local. If absent, return an acquisition-required error instead of using the network.
5. Verify source containment, digest, trust policy, Python/HeavenBase compatibility, and expected entry-point syntax.
6. Load lazily, validate kind-specific protocol, identifier, capabilities, and declared contribution identity.
7. Publish all bundle contributions into Context-scoped runtime registries only after every contribution validates.
8. Cache by catalog revision plus component/bundle fingerprint, never only by identifier.

Catalog updates affect new Contexts immediately and existing Contexts at explicit `refresh()` boundaries. Generic unloading or hot code replacement is not promised; replacing a loaded executable component normally requires a fresh Context/process.

### Developer and consumer surface

Use the existing `heavenbase.ext` facade for extension authors, adding a compact bundle lifecycle rather than exposing persistence internals:

```python
bundle = hb.ext.Bundle.from_path("./acme-search")
bundle.validate(context=ctx)
bundle.register(context=ctx)
```

Equivalent CLI commands should be `hb ext validate`, `register`, `list`, `show`, `disable`, `remove`, and `refresh`, implemented through the existing parser-neutral CLI architecture. Registration persists metadata; activation is explicit or occurs on first component use.

Consumers continue to use the item, not its source:

```python
backend_type = hb.ext.BackendType.load("acme-search", context=ctx)
workspace.enable_extension("acme-memory")
```

A built-in record may show `provenance="builtin"` and `tags=["system"]`; an external record may show publisher and artifact metadata. The calls, returned contracts, validation, and errors are otherwise identical.

## Migration Map

| Current mechanism | First target | Privileged path removed at exit |
|---|---|---|
| Registry state through data Backend | RegistryStore kernel | `registry/_backend.py` as permanent persistence path |
| `_bootstrap.py` type/strategy lists | Vocabulary bundle manifests | Fixed built-in imports and root-import bootstrap |
| Backend class/builder registries | Backend provider bundles | `_BUILTIN_BACKEND_MODULES`, default alias table, provider priming |
| Handler plugin callables | Provider bundle contributions | Fixed handler provider import tuple |
| Extension factory tuple | Extension bundle records | `extensions/bootstrap.py` inventory |
| Import-time operations/reducers/profiles/etc. | Declarative or Python component specs | Registration as discovery side effect |
| EntityMeta `_PENDING` | Explicit reusable entity components where intended | Process import order as reusable discovery |
| `sys-metaschema` mirror | Catalog mirror plus load status | Any temptation to make metadata rows the loader truth |
| Root/facade built-in maps | Optional convenience/type surface | Built-in maps as runtime discovery authority |

## Delivery Slices

Each slice should be one reviewable PR or a small stack of tightly ordered PRs. Run targeted fast tests per slice; reserve the full release matrix for Slice 10.

### Slice 0 — Accept the architecture and freeze fitness tests

**Touch**

- Add `docs/resources/architecture/adr/0011-registry-first-extension-parity.md`.
- Update `docs/goals/current.md` and `docs/goals/roadmap.md` to name the active migration.
- Add `tests/fixtures/extensions/` outside `src/heavenbase`.
- Add initial `tests/extensions/test_external_bundle_parity.py` and import-spy helpers.

**Work**

- Classify every Registry/list as: open component vocabulary, workspace/runtime state, or deliberately closed protocol. Do not migrate closed CLI command sets, query AST variants, or state machines merely because a Registry exists.
- Decide the old durable Registry-state policy before changing storage: either the pre-release state is explicitly disposable or a one-shot migration command is required.
- Freeze black-box assertions for built-in/backend/type/strategy/extension lookup, configuration, errors, metadata, and subprocess import laziness.
- Specify duplicate, alias, replacement, compatibility, trust, refresh, and activation semantics in the ADR.

**Exit**

- Maintainers accept the kernel exception and extraction test.
- The test fixture proves an out-of-tree folder can be discovered as metadata without importing its implementation; loading may still be expected to fail until Slice 3.

**Stop** if the desired behavior includes implicit remote download, arbitrary live module replacement, or one mutable singleton shared across unrelated Contexts; those require a different security/lifecycle design.

### Slice 1 — Decouple Registry persistence

**Touch**

- `src/heavenbase/utils/registry/registry.py`
- new `src/heavenbase/registry/store.py`
- new `src/heavenbase/registry/sqlite.py`
- `src/heavenbase/registry/__init__.py` and `.pyi`
- `src/heavenbase/context.py`, `src/heavenbase/bootstrap.py`
- `src/heavenbase/resources/configs/bootstrap.yaml`
- `tests/registry/test_registry_store.py`, existing Registry/context/bootstrap tests

**Work**

- Introduce `RegistryStore`, `StoredSnapshot`, and stdlib SQLite CAS storage.
- Move generic encoding/digest/integrity behavior out of `registry/_backend.py`; make `Registry.load(..., store=...)` backend-independent.
- Add `Registry.apply_batch(...)` or equivalent transaction API that computes and persists one next snapshot.
- Let a root Context construct/store the RegistryStore before ConfigManager or the selected data Backend. Child Contexts share or deliberately isolate it according to the ADR.
- Preserve revision/conflict/integrity behavior and capacity limits. Measure snapshot size and write contention before changing the whole-snapshot model.
- If migration is required, add a one-shot command that reads `sys-registry-state` through the old Backend and writes the new store, verifies digests/revisions, then exits. Do not keep runtime fallback.

**Exit**

- A fresh process persists, reloads, conflicts, refreshes, and corrupts a Registry using only the kernel store.
- Importing/opening the store does not import `heavenbase.backends`, `heavenbase.schema`, `heavenbase.types`, or `heavenbase.strategies`.
- `Context` can open a persistent Registry before `Context.backend()`.

**Verify**

```bash
rtk bash scripts/test.bash tests/registry/test_registry.py tests/registry/test_registry_store.py -q
rtk bash scripts/test.bash tests/config/test_bootstrap.py tests/core/test_context.py -q
```

**Rollback:** this slice is independently reversible before catalog state exists. After migration ships, rollback requires the verified reverse migration or restoration of the store file—not a hidden fallback path.

### Slice 2 — Add component and bundle contracts

**Touch**

- new `src/heavenbase/components/` package
- `src/heavenbase/ext.py` and `ext.pyi`
- `src/heavenbase/context.py`
- `tests/extensions/test_component_catalog.py`
- `tests/extensions/test_bundle_manifest.py`

**Work**

- Implement strict JSON codecs for `ComponentSpec` and `BundleSpec`; reject unknown executable payloads, absolute escape paths, invalid identifiers, duplicate contribution keys/aliases, and unsupported schema versions.
- Open `Context.components` over a dedicated persistent namespace such as `system-components`.
- Implement atomic register, inspect, list-by-kind/family/tag/bundle, enable/disable, remove, and refresh operations.
- Require `replace=True` plus expected prior fingerprint/revision for replacement. A component cannot claim protected `builtin`/`system` provenance; the trusted installer assigns it.
- Parse manifests without importing their modules. Manifest paths are locators relative to the bundle root, never component identities.

**Exit**

- Catalog operations survive a subprocess restart.
- Registering a bundle with one bad contribution changes no catalog record or revision.
- Inspection does not import fixture implementation modules.

**Verify**

```bash
rtk bash scripts/test.bash tests/extensions/test_component_catalog.py tests/extensions/test_bundle_manifest.py -q
rtk bash scripts/test.bash tests/registry/test_registry.py tests/core/test_context.py -q
```

### Slice 3 — Resolve, load, validate, and activate sources

**Touch**

- `src/heavenbase/components/resolver.py`, `loader.py`, `sources/`
- public protocols/exports in `src/heavenbase/ext.py` and `.pyi`
- `tests/extensions/test_component_loader.py`
- complete `tests/extensions/test_external_bundle_parity.py`

**Work**

- Support installed `module:attribute`/PyPA-entry-point records, registered local bundles with contained relative module paths, already-acquired content-addressed artifacts, and bounded typed embedded definitions—in that order.
- Keep acquisition as a separate service/API. Ordinary resolution reports missing local material and performs no network or installation.
- Validate source containment and digest before import; validate the returned contract and canonical identity after import.
- Resolve dependency DAGs before loading. Activate a bundle into temporary runtime projections, then publish all projections only after every component succeeds.
- Cache successes by `(catalog_revision, bundle_fingerprint, component_key)`. Cache failures only for that snapshot so a refresh can recover.
- Document that executable replacement applies to a fresh Context/process unless a kind opts into a tested reload contract.

**Exit**

- An out-of-tree fixture resolves in a clean subprocess after registration and passes the same kind contract test as an in-tree fixture.
- Listing or resolving metadata does not execute the fixture; explicit load/activation does.
- Dependency cycles, digest mismatch, wrong kind/identifier, incompatible host version, disabled records, and partial activation fail deterministically.

**Verify**

```bash
rtk bash scripts/test.bash tests/extensions/test_component_loader.py tests/extensions/test_external_bundle_parity.py -q
rtk bash scripts/test.bash tests/core/test_public_api.py -q
```

### Slice 4 — Make Context Registry-first

**Touch**

- `src/heavenbase/context.py`, `src/heavenbase/bootstrap.py`
- `src/heavenbase/resources/configs/bootstrap.yaml`
- `src/heavenbase/registry/_reset.py`
- workspace construction under `src/heavenbase/workspace/`
- configuration/context/workspace tests

**Work**

- Change root startup order to: parse minimal bootstrap; open RegistryStore; open/reconcile component catalog; install built-in catalog seed; resolve configured Backend identifier; then construct Backend, ConfigManager, and workspaces.
- Replace normal `backend.module` bootstrap input with a component identifier plus instance name/options. Keep a module/source only in catalog records.
- Route `Context.backend()` through the component loader and existing Backend contract. Make `context=` ownership explicit where a hidden default would prevent isolation tests.
- Keep `DEFAULT_CONTEXT` for convenience only; domain resolution must be context-aware and testable with an isolated Context.

**Exit**

- The configured Backend can be external and is selected without a bootstrap module path.
- Two isolated Contexts can select conflicting same-named components without leaking runtime caches.
- Config/Registry initialization no longer opens the data Backend as a side effect.

**Verify**

```bash
rtk bash scripts/test.bash tests/config/test_bootstrap.py tests/core/test_context.py tests/config/test_config_manager.py -q
rtk bash scripts/test.bash tests/workspace/test_workspace_registry.py tests/workspace/test_workspace_presets.py -q
rtk bash scripts/test.bash tests/core/test_public_api.py -q
```

### Slice 5 — Package built-ins as ordinary bundles

**Touch**

- co-located manifests in each provider/extension ownership folder
- family manifests for tiny vocabulary items that intentionally release together
- new `scripts/gen_builtin_components.py`
- generated `src/heavenbase/resources/builtin-components.json`
- package-data/build configuration and `scripts/sync-env.bash`

**Work**

- Give each cohesive built-in unit a local manifest. A provider bundle declares its Backend, handlers, dialect/capabilities, strategy adapters, and optional MCP contributions together. A family manifest may own multiple tiny pure vocabulary leaves; do not force artificial one-file packages.
- Generate a deterministic catalog seed at build/sync time. Runtime reads the packaged seed and does not scan `src/heavenbase` folders.
- Reconcile seed records idempotently by bundle fingerprint. The trusted built-in installer, not the manifest author, applies protected provenance/tags.
- Include the generated seed and any bundled manifests/assets in the wheel; add an installed-wheel resource smoke test.

**Exit**

- Every currently privileged built-in has a descriptor plan, even if its runtime migration occurs in later slices.
- Generated-seed drift fails `sync-env --check`.

**Verify**

```bash
rtk uv run python scripts/gen_builtin_components.py --check
rtk bash scripts/sync-env.bash --check
rtk uv build
```

### Slice 6 — Migrate pure vocabularies first

**Touch**

- `src/heavenbase/types/`, `strategies/`, `query/aggregate.py`, handler operations/predicates, storage profiles, schema text, capability descriptors, and their registries
- `src/heavenbase/_bootstrap.py`
- root/type/strategy facades and `.pyi` files
- matching unit/discovery tests

**Work**

- Project catalog descriptors into the existing runtime registries so most domain code keeps its current lookup contracts during migration.
- Migrate logical types and strategies as one dependency-aware slice; then operations, aggregate reducers, predicates, profiles, schema renderers, and other data-like vocabularies.
- Encode simple safe definitions directly only when their schema is bounded and declarative. Python classes/callables remain entry points.
- Remove `_bootstrap.py` inventories and import-side-effect discovery after each family has parity tests.
- Keep static built-in exports/type declarations only as optional convenience. Canonical identifier/config lookup must work for external components without a root export.

**Exit**

- Adding a logical type/strategy/operation requires only its bundle and catalog registration.
- A clean process can resolve an external item before importing any built-in inventory module.

**Verify**

```bash
rtk bash scripts/test.bash tests/core/test_logical_types.py tests/storage/test_storage_strategy.py tests/storage/test_storage_protocol.py -q
rtk bash scripts/test.bash tests/query/test_filter_predicates.py tests/query/test_query_aggregate_features.py tests/extensions/test_discovery.py -q
rtk bash scripts/test.bash tests/core/test_public_api.py -q
```

### Slice 7 — Migrate backend provider bundles

**Touch**

- provider folders under `src/heavenbase/backends/`
- `src/heavenbase/backends/registry.py`, families/capabilities/dialects/adapters
- `src/heavenbase/handlers/plugins.py`, `seed.py`, provider-owned handlers
- provider, handler, routing, and adapter tests

**Work**

- Prove the model with InMem and SQLite first: both register provider bundles and resolve through the catalog even though the kernel store itself uses SQLite independently.
- Then migrate SQL, vector, search, graph, file, Redis, and Surreal providers in focused PRs. Co-locate provider-owned handler/dialect/adapter code where practical.
- Seed handlers by querying configured provider/type/strategy contributions from the catalog, not by importing every provider.
- Remove `_BUILTIN_BACKEND_MODULES`, `_PROVIDER_DEFAULT_ALIASES`, built-in load locks, `load_builtin_handler_plugins()`’s tuple, and provider-priming hooks once the last provider family exits.
- Preserve the existing Backend class/builder contract as a runtime projection; make the catalog the discovery/source truth.

**Exit**

- The same backend config and `BackendType.load(identifier)` tests pass for bundled and package-external provider bundles.
- Importing `heavenbase` does not import provider modules, and inspecting providers imports none of them.
- A provider bundle either publishes Backend + handler/dialect/adapter contributions together or publishes nothing.

**Verify per provider**

```bash
rtk bash scripts/test.bash tests/extensions/test_handler_protocol.py tests/backends/test_backends.py tests/query/test_query_execution_protocol.py -q
rtk bash scripts/test.bash tests/storage/test_strategy_adapter.py tests/query/test_routing_inspection.py -q
```

Also run the touched provider's `detail`/`external` tests when its optional dependency or service is available.

### Slice 8 — Migrate extension/entity bundles and remaining open families

**Touch**

- `src/heavenbase/extensions/bootstrap.py`, base/registry/workspace activation
- system, prompt, agent, memory, and database extension folders
- `src/heavenbase/entity/base.py`
- MCP profiles, toolkits, serializers, Capsule layers, GRAM analyzers, interop inferers, LLM gateways, and other confirmed-open registries

**Work**

- Register all HeavenBase extension bundles through the same `BundleSpec`/loader used by external bundles. “Required” comes from signed runtime policy or declared invariant, not from a special built-in import path.
- Replace live entity classes/setup/API callables in persisted extension metadata with component IDs/entry points. Resolve and validate them during activation.
- Add a reusable `entity` component kind for bundle-owned Python entity classes and bounded inline JSON schemas. Preserve `workspace.register(...)` for explicit ad-hoc workspace schemas; catalog components are reusable definitions, not workspace instances.
- Remove `_PENDING` only if reusable class discovery is deliberately catalog-owned. Ordinary class declaration must never silently persist executable code.
- Migrate remaining registries only when their family is genuinely open. Keep closed protocols exhaustive.

**Exit**

- Built-in and external extension bundles use identical registration, activation, required-policy, workspace API, and entity lifecycle tests.
- No fixed extension factory list remains.

**Verify**

```bash
rtk bash scripts/test.bash tests/extensions/test_extensions.py tests/extensions/test_agent_extension.py tests/extensions/test_memory_extension.py tests/extensions/test_database_extension.py -q
rtk bash scripts/test.bash tests/interfaces/test_mcp.py tests/agents/test_capsule_toolkit.py -q
rtk bash scripts/test.bash tests/workspace/test_workspace_manifest.py -q
```

### Slice 9 — Complete the developer lifecycle and policy controls

**Touch**

- `src/heavenbase/ext.py`/`.pyi`
- parser-neutral CLI registry and new `hb ext` command group
- one cohesive extension-bundle template and local-folder demo
- trust/acquisition/cache configuration and audit metadata

**Work**

- Ship `Bundle.from_path`, `validate`, `register`, `list/show`, `disable`, `remove`, `refresh`, and explicit `acquire` APIs/commands.
- Replace loose backend/strategy/handler templates with one bundle template containing manifest, implementation, config schema, tests, docs, assets, and migrations as needed.
- Add audit fields for who registered/acquired/enabled a bundle, source, digest, timestamp, and catalog revision. Never store secrets in descriptors.
- For remote artifacts, require an immutable coordinate plus digest and, where policy requires, signature/publisher verification. Materialize to a content-addressed cache before registration or activation.
- Define garbage collection separately from disable/remove; never delete a shared cached artifact while another catalog record references it.

**Exit**

- A third-party developer can author in one local folder, validate, register, restart, list without import, and use the item through ordinary HeavenBase consumer syntax.
- Error messages identify catalog key, bundle, source, revision, and failed lifecycle stage without exposing secrets.

**Verify**

```bash
rtk bash scripts/test.bash tests/interfaces/test_cli_core.py tests/extensions/test_external_bundle_parity.py -q
```

### Slice 10 — Extract a built-in and remove every privileged path

**Work**

- Choose a representative non-kernel provider with multiple contributions—prefer Surreal or another cohesive optional provider after its Slice 7 migration.
- Copy/move it into a distribution or fixture outside `src/heavenbase`, register its bundle through the public lifecycle, and run the identical consumer/config/contract assertions. Only provenance/source metadata may differ.
- Delete remaining central built-in inventories, source-tree scans, provider import tuples, discovery side effects, and tests that assert privileged paths.
- Add grep/AST fitness checks that reject new fixed open-family module maps, package-folder discovery, and import-time registration in declared extension families.
- Regenerate capabilities/docs from catalog-backed runtime data and run installed-wheel tests across Linux, macOS, and Windows.

**Release gate**

```bash
rtk uv run python scripts/gen_builtin_components.py --check
rtk uv run python scripts/gen_capabilities.py
rtk bash scripts/test.bash
rtk bash scripts/test.bash -m "full and not external and not llm" -q
rtk bash scripts/test.bash -m external -q
rtk bash scripts/flake.bash --ci
rtk bash scripts/sync-env.bash --check
rtk uv build
rtk uv run --with twine python -m twine check dist/*
rtk git diff --check
```

External-provider tests may be split by available services, but every migrated live provider must pass before its own merge/release gate.

## Cross-Cutting Decisions

### Catalog versus runtime registries

The persisted ComponentCatalog is the discovery/source authority. Existing specialized registries remain useful as Context-scoped runtime projections with strong typed APIs. They may cache loaded classes/callables, but they must be populated only by the component loader and must not invent components through fixed imports or scans.

`sys-metaschema` remains an inspection mirror. Extend it with catalog revision, source/provenance, enabled state, fingerprint, and runtime load status, but never resolve code from metadata entity rows.

### Built-in installation and reconciliation

Built-in manifests are compiled into a deterministic packaged seed. On a new catalog, Context installs that seed atomically. On upgrade, it reconciles only records still owned by the prior built-in fingerprint; it does not overwrite an explicit local replacement. Protected system requirements are enforced as catalog/policy invariants, not a separate loader.

### Trust and remote code

Provenance is evidence, not authorization. Trust policy considers installer authority, publisher/signature, digest, source scope, and component kind. A `builtin` tag cannot be self-declared. Remote listing is harmless metadata; acquisition is explicit; activation requires a verified local artifact. Inline executable strings are forbidden unless represented by an explicitly trusted, versioned Capsule/artifact mechanism.

### Concurrency and refresh

Use Registry CAS for writers and immutable catalog snapshots for readers. Resolve a full activation against one revision. If the revision changes before publication, retry or fail with a conflict; never mix records from two revisions. Existing instances remain pinned to their loaded fingerprint. `refresh()` affects future resolution, and a fresh Context/process is the default upgrade boundary.

If the component snapshot approaches current item/byte limits or CAS contention becomes material, move the component store to row-per-record transactions behind the same RegistryStore/catalog contracts. Do not disable integrity/capacity limits as a shortcut.

### Failure and rollback

- Registration failure leaves the prior catalog revision unchanged.
- Acquisition failure leaves no active record and cleans only its unreferenced staging area.
- Load/validation failure publishes no runtime contribution from that bundle.
- Disable/remove never pretends to unload already imported Python modules; it blocks new resolution and reports pinned instances.
- Built-in seed upgrades retain the prior verified seed/fingerprint until reconciliation completes.
- Each migration slice removes one corresponding privileged path before merge, preventing a long-lived split brain.

## Documentation Touch List for HeavenBase

- `AGENTS.md`: update extension registration and verification commands after the lifecycle ships.
- `docs/README.md`: link the ADR and revised architecture pages.
- HeavenBase's canonical queue, engineering guide, roadmap, and development log track slices and remaining privileged paths.
- `docs/resources/architecture/mental-model.md`: add source-neutral resolution as a core invariant.
- `docs/resources/architecture/registry-context.md`: document RegistryStore, catalog, Context scope, boot order, refresh, and CAS.
- `docs/resources/architecture/extension-layout.md`: replace host-subfolder/export recipes with cohesive manifests and registration.
- `docs/resources/architecture/design-philosophy.md`: add Lego-style parity and extraction fitness.
- `docs/resources/architecture/concepts-and-classes.md`: add RegistryStore, ComponentSpec, BundleSpec, Catalog, Resolver, Loader, and runtime projection roles.
- `docs/resources/architecture/data-flows.md`: add register, acquire, resolve, load, activate, refresh, disable, and remove flows.
- `docs/resources/architecture/backend-strategy-handlers.md`: document provider-bundle contributions and removal of import priming.
- `docs/resources/architecture/config-system.md` and `docs/reference/config-spec.md`: document kernel-store bootstrap and Backend-by-component ID.
- `docs/reference/public-api.md` and `docs/reference/naming-vocabulary.md`: document public lifecycle, identifiers, bundle/source/provenance terms, and upgrade semantics.
- `docs/resources/reports/capabilities.md`: regenerate from catalog-backed runtime data.
- `tests/README.md`: document external fixtures, shared contract suite, subprocess/installed-wheel parity, and extraction tier.
- `README.en.md`, generated `README.md`, and `src/heavenbase/resources/README.md`: add one concise local external-bundle example after the API is stable.
- Add a closeout report under `docs/resources/reports/` after Slice 10. Mark `README.zh.md` stale and route translation separately.

## Completion Criteria

- [ ] A bundle outside the HeavenBase package registers and survives restart without a HeavenBase source edit or release.
- [ ] Built-in and external records differ only in source/provenance metadata and pass the same discovery, loading, validation, lifecycle, and contract tests.
- [ ] The selected data Backend is resolved from the catalog after the independent RegistryStore opens.
- [ ] Catalog inspection imports no component implementation and lookup performs no acquisition/network mutation.
- [ ] Bundle registration and runtime publication are atomic under concurrency.
- [ ] Duplicate, alias, compatibility, trust, enablement, refresh, replacement, and rollback semantics are deterministic and documented.
- [ ] `_bootstrap.py` inventories, `_BUILTIN_BACKEND_MODULES`, handler provider tuples, extension factory tuples, and open-family import-side-effect discovery are removed.
- [ ] One representative built-in provider is extracted outside `src/heavenbase` with unchanged consumer tests.
- [ ] Targeted, full, external, lint, environment-drift, build, package, and cross-platform installed-wheel gates pass.

## Recommended First Execution Block

Implement Slices 0–3 before migrating any domain family. They establish the durable kernel, catalog contract, loader, and out-of-tree proof while the current runtime registries remain intact. Then make Context Registry-first in Slice 4 and migrate families incrementally. Starting by rewriting backends or entities before breaking the Registry/Backend bootstrap cycle would create another temporary privileged loader and should be avoided.
