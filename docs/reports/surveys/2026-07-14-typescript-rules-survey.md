# TypeScript Rules Survey

- Status: Current
- Date: 2026-07-14
- Scope: TypeScript architecture, code-sanity, and Bun-first environment conventions for heaven-style.
- Trigger: Add a TypeScript rule surface without copying Python-only mechanics or imposing product/framework-specific conventions.
- Follow-up: Review the cross-language candidates before changing Python-wide or shared rules.
- Staleness trigger: A material TypeScript, Bun, Biome, typescript-eslint, or Node package-contract change; or promotion of a candidate into shared rules.

## Decision Summary

The rule hierarchy is:

1. Follow the target repository's `AGENTS.md`, checked runtime metadata, package manager, lockfile, framework contract, and release compatibility policy.
2. Apply heaven-style's shared architecture: minimal mental model, ownership by reason to change, dependency inversion, registries for open variation, exhaustive variants for closed protocols, explicit lifecycle, one canonical API, and executable architecture checks.
3. Use the `ts-*` rules for TypeScript syntax, types, modules, documentation, async behavior, resources, dependencies, and environment. They supersede Python-only mechanics.
4. When the repository is silent, use the source-neutral Bun-first and strict TypeScript baseline recorded in the skill.

The TypeScript rules are a concrete reviewable policy. They do not change Python code rules wholesale. This report records generic conclusions and public specifications only; it intentionally omits private/reference-repository identities, local checkout paths, machine-specific setup sources, observed local versions, and borrowed package/framework internals.

## Official References

- [Bun TypeScript guidance](https://bun.com/docs/typescript)
- [Bun install and frozen CI](https://bun.com/docs/pm/cli/install)
- [Bun lockfile](https://bun.com/docs/pm/lockfile)
- [Bun lifecycle-script trust](https://bun.com/docs/pm/lifecycle)
- [TypeScript TSConfig reference](https://www.typescriptlang.org/tsconfig/)
- [TypeScript module option guidance](https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options)
- [TypeScript `verbatimModuleSyntax`](https://www.typescriptlang.org/tsconfig/verbatimModuleSyntax.html)
- [typescript-eslint shared configs](https://typescript-eslint.io/users/configs/)
- [typescript-eslint `no-floating-promises`](https://typescript-eslint.io/rules/no-floating-promises/)
- [Node package and export rules](https://nodejs.org/api/packages.html)
- [Biome configuration](https://biomejs.dev/reference/configuration/)

## TypeScript Rules

| Rule | Pattern | Anti-pattern |
| --- | --- | --- |
| Open versus closed variation | Registry/strategy for providers and plugins; exhaustive discriminated-union handling for a closed AST/state machine | Provider-name routing in orchestration, or a mutable registry for a compiler-known closed set |
| Narrow capability contracts | Minimal common interface plus role-specific capability interfaces and guards | Catch-all base contract with no-op or always-unsupported optional methods |
| Compile versus execute | Pure compiler produces a typed fragment; adapter performs provider I/O | Adapter parses the public DSL or compiler owns mutable provider state |
| Capability-driven policy | Readonly validated capability metadata lives with the implementation | Orchestrator branches on concrete implementation names |
| Explicit lifecycle | Constructor stores identity/config; `create`, `connect`, `close`, and disposal are explicit and awaitable | Network/filesystem work hidden in construction; disposal returns before children stop |
| Strict compiler baseline | Strict checks, unchecked-index protection, exact optionals for greenfield code, checked overrides/returns/fallthrough, and explicit type-only imports | Runtime transpilation treated as typechecking |
| Boundary validation | External input remains `unknown` until a runtime schema or focused guard validates it | `JSON.parse(...) as Domain`, double assertions, or non-null assertions as parsing |
| Stable public contracts | Explicit public return types and semantic TSDoc/JSDoc; internal inference remains welcome | Accidental API changes through implementation inference; comments restating names |
| Opaque identifiers | Selective branded/opaque types for confusing cross-boundary IDs | Interchangeable primitive IDs, or branding every local string |
| Resolved configuration | Raw request permits omission; one owner validates/defaults into a complete runtime spec | Repeated `value ?? default` interpretation throughout execution code |
| Ownership-safe readonly data | Readonly input contracts plus clone/freeze when ownership changes | Readonly typing over mutable backing state shared with another owner |
| Promise discipline | Every promise is awaited, returned, or deliberately owned; typed lint protects async boundaries | Unmarked fire-and-forget calls and blanket lint exemptions |
| ESM and package boundaries | Explicit module type, runtime-correct specifiers, package entry points, and declared cross-package dependencies | Source-tree traversal, undeclared dependencies, or aliases that work only in-repo |
| Packed-consumer verification | Inspect and smoke-test the packed artifact from a clean strict consumer | Source tests pass while declarations, exports, packed files, or runtime specifiers are broken |
| Bun-first reproducibility | Existing coherent metadata wins; otherwise Bun, one committed `bun.lock`, local pinned tools, a pinned runtime, and `bun ci` | Mixed lockfiles, global tools, floating downloads, or incidental manager migration |
| Dependency execution control | Inspect untrusted lifecycle scripts and keep the explicit trust set minimal | Assuming a default allowlist or package popularity replaces project review |

## TypeScript Adaptations of Python Rules

| Python intent | TypeScript adaptation | Dropped literal rule |
| --- | --- | --- |
| Small OOP front door | Put state/lifecycle behavior on the owning object; keep stateless transforms as functions | Classes/methods are not universally preferred in TypeScript |
| Typed protocols and public methods | Structural interfaces/type aliases, discriminated unions, explicit public return types | Python annotation spelling |
| Google-style docstrings | TSDoc/JSDoc for semantics, lifecycle, errors, disposal, and non-obvious parameters | Mandatory `Args`/`Returns` sections |
| `__init__.py`/`__init__.pyi` lazy facade | Side-effect-free entry module, explicit exports/subpaths, dynamic optional imports | Python stub/export mechanics |
| `heavenbase.utils` | Use target-repository/platform capabilities; create a shared helper only for proven reuse | Python covered-stdlib policy |
| `CM_HVNB` | One owner validates configuration and resolves request-to-spec once | Python config-manager and sentinel syntax |
| `raise_mismatch` | Contextual typed error or validated lookup with stable code/cause where callers need it | Python utility call |
| Comprehensions and Python protocols | Guard clauses, direct array/object methods, iteration protocols, and readable expressions | Python-specific compact syntax |
| pytest `fast`/`full` markers | Targeted runner scripts, contract suites, and explicit expensive/integration lanes | pytest marker vocabulary |

## Cross-language Candidates for Review

These generic patterns are plausible improvements for both TypeScript and Python. They were not added wholesale to Python. `TS included` means the TypeScript rules contain the narrow form; `Review only` means neither language surface gained the stronger rule.

| Candidate | Pattern | Anti-pattern | Status |
| --- | --- | --- | --- |
| Mechanize standing promises | Discover packages/exports/config fields and fail when an item is skipped; generated artifacts have check modes | Prose-only invariants and manual lists that silently omit new items | Review only |
| Layered failure evidence | Focused tests, reusable implementation contracts, property checks for invariants, and built/external smoke tests as risk requires | One source-level happy-path suite or checking only self-reported success | TS included; review shared/Python |
| Resolve once | Validate/default raw requests at the owning boundary; execution consumes a resolved spec | Consumers repeatedly reinterpret raw optionals | TS included; review shared/Python |
| Fail when knowledge is complete | Reject shape errors immediately and referential errors at the earliest layer with complete knowledge | Silent skip, empty success, or behavior determined by registration order | TS included; review shared/Python |
| Transactional registrations | Validate first, make rollback/disposal available before observers run, and bind cleanup to the owner | Mutate, notify, then leave half-installed state after failure | TS included; review shared/Python |
| Quiescent teardown | Stop notifications, cancel children, await resources, report cleanup failures, then return | Fire cancellation and return while work/listeners remain live | TS included; review shared/Python |
| Callback containment | Observe each subscriber result and apply an explicit continuation/veto policy | One observer exception or rejection starves later observers or corrupts lifecycle | TS included; review shared/Python |
| Structured failure facts | Stable error code/message/cause where callers branch; orthogonal facts stay independent | Parse error strings or make timeout/abort/exit falsely exclusive | TS included; review shared/Python |
| Allowlisted outbound data | Construct wire/process/persistence objects from named allowed fields | Spread an internal object across a boundary and redact afterward | TS included; review shared/Python |
| Tunables versus invariants | Deployment policy is config; protocol/security invariants remain constants; validate tunables at startup | Hard-coded deployable choices or making every invariant configurable | Review only |
| Minimize ambient authority | Pass the smallest environment, credentials, and capabilities; bound output; use exclusive private resources | Full environment inheritance and predictable shared temporary files | TS included for subprocess code; review shared/Python |
| Observe real async state | Drive control flow from events, awaited promises, streams, or durable state | Assume a requested transition completed synchronously | TS included; review shared/Python |
| One authoritative fact | Generate repeated catalogs/graphs from code and check examples; link rather than copy | Repeated hand-maintained API/config tables | TS included for generated checks; review stronger shared/Python gates |
| Narrow explained escapes | Keep suppressions line/file-local with a safety reason and narrow scope | Blanket directory/file-wide lint, type, or coverage disables | TS included; review shared/Python |
| Abstractions need real pressure | Stateless logic stays a function/module; service/plugin/interface splits require lifecycle, replacement, or repeated variation | Service wrappers around helpers or speculative interface/implementation packages | TS included; review shared/Python |

## Non-universal Practices

- Do not migrate a coherent package manager/runtime as incidental feature work.
- Framework hook, plugin, callback, or declaration-merging contracts remain framework-local.
- Multi-package interface/implementation/consumer seams require real independent release or replacement pressure.
- Branching, merge, and compatibility policy belong to the repository and release contract.
- Source-tree package exports require an explicit documented consumer contract.
- Coverage depth follows risk and behavioral contracts; blanket per-file targets are not a generic quality rule.
- Semantic public API documentation is preferable to mandatory comments on every file/export.
- Generated gates are justified by recurring drift, not created speculatively.

## Recommendation

Keep the TypeScript rules source-neutral and validate them against real target-repository work. Review lifecycle/boundary candidates separately from repository-mechanics candidates. Promote a cross-language rule only when the target language has a clear equivalent, focused verification, and a repository-owned enforcement path.
