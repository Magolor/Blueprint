# Lego-Style Extension Parity Plan

- Status: Done
- Created: 2026-07-20
- Scope: Propose a source-neutral heaven-style criterion for extension parity, then promote the confirmed criterion into the skill.
- Links: `.agents/skills/heaven-style/references/rules/project/extension.md`; `docs/plans/2026-07-20-heavenbase-lego-style-extension-refactor.md`; `docs/progress/2026-07-20/README.md`
- Approval gate: Confirmed by the user on 2026-07-20. The skill was updated under an explicit no-version-bump waiver and remains exactly `0.1.2.0`.

## Proposed Criterion

> **Lego-style extension parity.** For every genuinely open extension family, bundled and independently developed implementations are peers. An extension may be authored, packaged, stored, and registered outside the host source tree without modifying or releasing the host package. Consumers discover, select, configure, inspect, and invoke it through the same public contracts and runtime path used for bundled implementations.
>
> Origin is observable metadata, not a routing rule. A bundled item may carry trusted provenance such as `origin=system`, but origin alone must not change dispatch, validation, capabilities, lifecycle, configuration, or user-facing syntax.
>
> One logical Registry per declared environment is the authoritative catalog of extension identity, kind, compatibility, capabilities, entry point or inline definition, provenance, integrity, enablement, and lifecycle state. Every implementation—including bundled ones—uses the same registration, resolution, validation, loading, activation, and contract-test mechanisms. Open extension families must not depend on handwritten import lists, fixed package subfolders, concrete-name routing, or a privileged built-in loader.

## Architecture Contract

The uniform path is:

```text
extension reference -> persisted catalog -> deterministic resolver
  -> verified artifact/definition -> loader -> contract validation -> runtime instance
```

- **Logical globality, explicit scope.** “Global” means one authoritative Registry view for the owning environment, with documented project, user, system, or remote sources and deterministic precedence. Storage may be a file, database, service, or composition of providers; the contract must not require one physical machine-wide database.
- **Catalog/runtime separation.** The persisted catalog owns descriptors and locators. Runtime instances and caches remain scoped to an application, workspace, tenant, or test. The Registry is not a general service locator or an uncontrolled mutable singleton.
- **Stable, location-independent identity.** Records use a namespaced kind and canonical identifier plus implementation version, host-contract compatibility, entry point, capabilities, provenance, integrity, enablement, and lifecycle metadata. Local filesystem paths are locators, not identities. Duplicate, alias, version, and override behavior must be explicit and deterministic.
- **Discovery before execution.** Listing, inspection, compatibility checks, and conflict resolution must not import or execute extension code. Loading is lazy and happens only after one compatible record has been selected.
- **Controlled acquisition.** Remote catalogs advertise candidates; they do not imply installation, trust, enablement, or execution. Executable artifacts must be acquired explicitly, pinned and integrity-checked, then loaded under the same trust policy as other executable extensions. Registry-embedded content should normally be schema-validated declarative data.
- **Extension resolution, not import replacement.** The framework resolves every extensible item through the Registry first. Ordinary language imports remain ordinary; a custom import finder, if ever needed, must be limited to a reserved extension namespace.
- **Cohesive extension units.** Keep an extension’s manifest, implementation, configuration schema, assets, tests, docs, and migrations together where practical. Shared libraries remain ordinary dependencies. Bundled implementations follow the same bundle and manifest pattern and are indexed through the Registry rather than privileged folder semantics.
- **Explicit activation lifecycle.** Registration is atomic, persistent, auditable, and reversible. Refresh, cache invalidation, upgrade, rollback, disablement, and activation boundaries are defined. Hot replacement is optional, never an implied guarantee.
- **Minimal bootstrap kernel.** Registry schema, resolver/loader contracts, trust policy, and one bootstrap path remain directly available; the extension system must not require itself to load itself.

## Normative Coverage

- [x] Requires an implementation developed outside the host package to register and work without a host source edit, rebuild, or release.
- [x] Requires bundled and external implementations to pass the same contract suite and use identical consumer-facing configuration and invocation.
- [x] Requires extracting one bundled implementation into an independent artifact without changing consumer-facing tests.
- [x] Forbids adding an implementation through a central router, union, import list, or privileged built-in folder scan.
- [x] Requires persisted registration plus deterministic identity conflicts, scope precedence, compatibility, and replacement behavior.
- [x] Keeps provenance and trust inspectable and policy-relevant without creating separate behavior paths.
- [x] Separates discovery, acquisition, loading, and activation so inspection does not execute code and remote presence never implies installation or execution.

## Non-Goals

- Do not use registries for intentionally closed syntax trees, protocols, or state machines; keep those exhaustive.
- Do not promise arbitrary hot reload, dependency mutation during import, or transparent execution of remote code.
- Do not force one physical global database or leak extensions across isolated projects and environments.
- Do not duplicate shared code merely to make each extension folder self-contained.

## Evidence

- The [PyPA entry-points specification](https://packaging.python.org/en/latest/specifications/entry-points/) demonstrates stable group/name/object references for components supplied by separate distributions.
- The [PyPA plugin-discovery guide](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/) distinguishes metadata-based discovery from fixed naming and namespace-package scans.
- Python’s [`importlib.metadata` entry-point API](https://docs.python.org/3/library/importlib.metadata.html#entry-points) separates descriptor inspection from explicit loading.
- Python’s [meta-path import semantics](https://docs.python.org/3/reference/import.html#the-meta-path) support keeping ordinary imports outside the extension Registry unless a reserved namespace deliberately opts in.

## Slices

### Slice 1: Confirm the criterion

- Goal: Review the proposed invariant, boundaries, acceptance tests, and terminology.
- Touch: This plan and the linked daily progress note only.
- Acceptance: Human confirmation or specific requested revisions.
- Verification: Markdown links and `git diff --check` pass; no heaven-style skill file changes.
- Docs: Completed after user confirmation on 2026-07-20.

### Slice 2: Promote into heaven-style

- Goal: Make extension parity normative and discoverable without duplicating the rule.
- Touch: The `extension` rule as owner; a short `SKILL.md` philosophy sentence; conflicting Python/TypeScript registry, import, and file-locality guidance; generated index and progress artifacts.
- Acceptance: The skill explicitly enforces built-in/external parity and the extraction fitness test while preserving open-registry/closed-union boundaries.
- Verification: Run the skill index/check, scanner, repository lint/tests, environment drift checks, and `git diff --check` through repository wrappers.
- Docs: Completed with the explicit no-version-bump waiver; retained `0.1.2.0` exactly.

## Progress

- 2026-07-20: Drafted the proposed criterion and stopped at the approval gate; no heaven-style skill files were changed for this request.
- 2026-07-20: User confirmed the criterion. Promoted it into the owning extension rule, generic Python baseline, SOLID/file/API guidance, TypeScript extension seams, testing rules, architecture workflows, and the generated skill index.
- 2026-07-20: Audited HeavenBase read-only and saved the implementation route in `docs/plans/2026-07-20-heavenbase-lego-style-extension-refactor.md`; no HeavenBase source files were changed.

## Closeout

- Verification: Skill index check, Python byte-compilation, Blueprint scanner, `scripts/flake.bash --ci`, `scripts/test.bash`, `scripts/sync-env.bash --check`, targeted and final `git diff --check`, and standard global-skill installation all passed.
- Version: Explicit user waiver applied; skill metadata and generated index remain `0.1.2.0`.
- Follow-up: Execute the HeavenBase route beginning with the ADR/fitness tests and the Backend-independent RegistryStore kernel.
