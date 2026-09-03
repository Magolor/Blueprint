---
id: overview
title: Rule overview
enabled: true
blocking: true
order: 1
category: overview
keywords: [which rule, what rules apply, rule map, style overview, start here]
description: Use when deciding which heaven-style rule files apply to a task.
---

# Rule overview

Rule frontmatter uses `description` and `keywords` to help agents find relevant files. The Markdown body is the source of truth for behavior.

Each rule uses this body shape where practical:

1. `Core rule` - the normative rule.
2. `Apply when` - situations that should load the rule.
3. `Do` - preferred behavior.
4. `Avoid` - banned or discouraged behavior.
5. `Example` - focused `Anti-pattern:` and `Recommended pattern:` pairs when useful.
6. `Related rules` - cross-rule checks.

## Language selection

Read the target repository's `AGENTS.md`, runtime/package metadata, and public compatibility policy first. Then apply the shared Heaven design philosophy plus exactly the language surface the change touches:

- TypeScript code uses `references/rules/code/typescript/` and the project rules. Checked JavaScript uses relevant parts only when the repository has an explicit `checkJs`/migration policy; do not enable `allowJs` incidentally. TypeScript is a complete Heaven-style surface with its own utilities, API vocabulary, structural types, package graph, async/data boundaries, documentation, compatibility, and toolchain rules.
- Python code uses `references/rules/code/python/` and the project rules. Python remains fully supported; repository-provided utilities stay conditional on the target repository.
- Mixed-language boundaries use both language surfaces only where each side applies, plus an explicit serialized/runtime contract between them.

Repository mechanics win when they are coherent and explicit. When a new or unspecified project has not selected a language, start architecture and examples from the TypeScript surface and its Bun-first environment default. This greenfield default is not permission to migrate an existing coherent Python repository incidentally.

## TypeScript code-quality rules

1. `ts-util` - load for files, paths, resources, serialization, logging, hashing, IDs, temp data, subprocesses, host APIs, or shared utility ownership.
2. `ts-architecture` - load for TypeScript services, public APIs, SOLID boundaries, registries versus unions, capabilities, adapters, strategies, composition roots, or lifecycle ownership.
3. `ts-api` - load for class-versus-function choices, public method vocabulary, collections, constructor/factory design, fallback/control-flow shape, or helper cleanliness.
4. `ts-types` - load for strict compiler contracts, `unknown`, runtime validation, unions, branded identifiers, optionality, readonly ownership, assertions, or resolved configuration.
5. `ts-config` - load for JSON/YAML config, overrides, resolved specs, path edits, revisions, secrets, scopes, persistence, or swappable backends.
6. `ts-modules` - load for `.ts`/`.tsx` layout, ESM, imports/exports, entry points, workspaces, optional integrations, generated code, or packed packages.
7. `ts-async` - load for promises, cancellation, resource lifetime, startup/shutdown, callbacks, retries, subprocesses, or structured errors.
8. `ts-sql` - load for SQL, database clients, query builders, ORMs, migrations, transactions, pools, raw queries, or row validation.
9. `ts-docs` - load for published exports, TSDoc/JSDoc, declaration-facing semantics, examples, or generated API documentation.
10. `ts-compat` - load for renamed exports/subpaths, deprecations, aliases, runtime/package support changes, or config/wire/data migrations.
11. `ts-environment` - load for Bun/package-manager choice, lockfiles, compiler profiles, local tooling, formatter/linter ownership, dependencies, CI, or runtime compatibility.

## Python code-quality rules

1. `util` - load for imports, file I/O, JSON/YAML/pickle/text, shell, logging, hashing, temp paths, or deterministic IDs.
2. `config` - load for tunables, defaults, prompts, templates, resources, paths, model/provider/backend parameters, or disputed literals.
3. `types` - load for public APIs, `typing` imports, Python-version compatibility, dict/list annotations, or schema-shaped data.
4. `docstring` - load for publicly exposed functions, major feature APIs, Google-style `Args`/`Returns`/`Yields`, examples, warnings, or Markdown in docstrings.
5. `oop` - load for public method names, entity/store/client APIs, CRUD, KV, batch, engine lifecycle, specs/configs/plans, or preset/provider/backend models.
6. `model` - load for public API surface design, new classes/functions, user mental models, or DSL/interface choices.
7. `solid` - load for SOLID checks: SRP, OCP, LSP, ISP, DIP, class boundaries, extension points, inheritance contracts, role-specific interfaces, registries, or provider/strategy dependencies.
8. `name` - load for naming reviews, new public symbols, abbreviations, module names, or glossary changes.
9. `files` - load for Python file organization, package folders, internal modules, public exports, lazy export stubs, adapter/provider layout, or feature-local boundaries.
10. `py` - load for Python control-flow shape, comprehensions, guard clauses, and fallback semantics.
11. `clean` - load when adding helper functions, wrappers, adapters, temporary transforms, or abstraction boundaries.
12. `error` - load for validation, unsupported choices, exception boundaries, logging, or swallowed errors.
13. `sql` - load for database access, raw SQL, migrations, DDL, ORM use, and bind parameters.
14. `compat` - load for renames, deprecations, migration shims, `v1/v2` splits, or config schema changes.

## Python-to-TypeScript intent map

Python's older, more granular rule set remains useful for Python mechanics. The TypeScript surface groups the same design intent by TypeScript ownership rather than mirroring filenames mechanically:

| Python rule | TypeScript counterpart | Porting decision |
| --- | --- | --- |
| `util` | `ts-util` | Direct counterpart using Web/Node/Bun APIs and explicit host boundaries. |
| `config` | `ts-config`, `ts-types` | Direct counterpart; TypeScript adds JSON-shaped validation, detached snapshots, revisions, and async backends. |
| `types` | `ts-types` | Direct counterpart using strict structural types, `unknown`, unions, brands, and readonly ownership. |
| `docstring` | `ts-docs` | Semantic counterpart; TSDoc/JSDoc replaces Google-style Python sections. |
| `oop` | `ts-api`, `ts-architecture` | Counterpart keeps domain vocabulary while following JavaScript protocols and class/function idioms. |
| `model` | `ts-api`, `ts-architecture` | Shared minimal mental model, expressed through TypeScript-native public surfaces. |
| `solid` | `ts-architecture` | Direct architectural counterpart using structural interfaces, composition, registries, and unions. |
| `name` | `ts-api`, `ts-types`, `ts-modules` | Counterpart uses camelCase/PascalCase and TypeScript file/package conventions. |
| `files` | `ts-modules` | Direct counterpart through ESM entry points, exports, workspaces, feature locality, and packed consumers. |
| `py` | `ts-api`, `ts-types` | Language-shape counterpart uses guards, `??`, optional chaining, readable collection operations, and narrowing. |
| `clean` | `ts-api`, `ts-util`, `ts-modules` | Helper-cost and ownership counterpart; no speculative wrappers or utility buckets. |
| `error` | `ts-async`, `ts-types` | Counterpart adds promise ownership, cancellation, stable error facts, and `unknown` catches. |
| `sql` | `ts-sql` | Direct counterpart for binding, rows, transactions, migrations, pools, and driver boundaries. |
| `compat` | `ts-compat` | Direct counterpart across source/types, package/runtime, wire/config, data, and behavior. |

Python-only syntax and packaging mechanics—Google docstring sections, dunder collection methods, `__init__.pyi`, `py.typed`, Python import spelling, and pytest markers—do not transfer. Their contract intent is represented by the mapped TypeScript rule instead.

## Code-design examples

Examples teach reusable design intuition without adding another normative rule:

1. `example-open-capability-vocabulary` - read [open capability vocabulary](../examples/code/open-capability-vocabulary.md) when an open extension family keeps gaining hard-coded feature fields, base methods, switches, or unvalidated escape hatches.
2. `example-local-gui-layout` - read [local GUI layout](../examples/code/local-gui-layout.md) when choosing a cohesive versus workspace topology or wiring UI, host, application, and domain dependencies.

## Project rules

1. `environment` - load when running shell commands, selecting the repository's TypeScript or Python toolchain, adding package scripts/wrappers, or fixing wrong-environment failures for coding agents.
2. `format` - load when running or reviewing lint, format, import order, or repo command wrappers.
3. `test` - load when adding behavior, tests, examples, smoke checks, provider routes, or LLM/MCP integration evidence.
4. `docs` - load when creating, restructuring, reviewing, or syncing authored docs; changing user-facing APIs, YAML metadata, bilingual pairs, generated artifacts, task state, release notes, or documentation authority.
5. `review` - load for PR/diff review, inline comments, waivers, or final quality gates.
6. `extension` - load when adding or reviewing any open plugin/provider/backend/handler family, Registry, manifest, entry point, resolver/loader, or bundled/external parity—even before a registry exists.
7. `interfaces` - load when a package is provided as a service; when separating language-native SDK, application, transport, CLI, GUI, MCP, or TUI roles; or when designing REST/OpenAPI, concurrent requests, package boundaries, cross-language clients, or desktop hosts.

Examples live inside their owning rules. Do not add a separate demo rule surface unless a future project has concrete evidence that search/routing works better with separate example files.

## Design rules

On-demand references outside the default coding loop; load only when the task matches:

1. `gui-style` (`references/design/gui-style.md`) - load for GUI/UX, frontend, dashboard, app-shell, attention hierarchy, theme/color, component unity, spacing, density, motion, maintenance, refactor, transfer, demo, temporary HTML, or interface-review work in any framework.

## Failure playbooks

Use `references/failures/` when command failures block progress:

1. `failure-env` - Bun/Node/Python, package-manager, runtime, shell, PATH, or wrong-environment failures.
2. `failure-network-proxy` - CLI/API network failures, VPN/proxy ambiguity, or provider connectivity.
3. `failure-auth-secrets` - MCP/provider auth expiry, missing API keys, Linear/Tavily/LLM token failures, or direct API fallback.
4. `failure-linear-pressure` - Linear project issue limits, noisy progress comments, or stale Done/Duplicated/Outdated issue cleanup.
