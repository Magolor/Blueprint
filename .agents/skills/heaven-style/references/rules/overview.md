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

- Python code uses `references/rules/code/python/` and the project rules.
- TypeScript code uses `references/rules/code/typescript/` and the project rules. Checked JavaScript uses relevant parts only when the repository has an explicit `checkJs`/migration policy; do not enable `allowJs` incidentally. These rules translate Heaven's design intent and replace Python-only mechanics such as standard-library/import conventions, Google-style docstring sections, `__init__.pyi`, and pytest markers. Repository-specific Python helpers never transfer automatically.
- Mixed-language boundaries use both language surfaces only where each side applies, plus an explicit serialized/runtime contract between them.

Repository mechanics win when they are coherent and explicit. For new TypeScript repositories without contrary metadata, the TypeScript environment rule supplies the Bun-first default.

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

## Code-design examples

Examples teach reusable design intuition without adding another normative rule:

1. `example-open-capability-vocabulary` - read [open capability vocabulary](../examples/code/open-capability-vocabulary.md) when an open extension family keeps gaining hard-coded feature fields, base methods, switches, or unvalidated escape hatches.

## TypeScript code-quality rules

1. `ts-architecture` - load for TypeScript services, public APIs, SOLID boundaries, registries versus unions, capabilities, adapters, strategies, composition roots, or lifecycle ownership.
2. `ts-types` - load for strict compiler contracts, `unknown`, runtime validation, unions, branded identifiers, optionality, readonly ownership, assertions, or resolved configuration.
3. `ts-modules` - load for `.ts`/`.tsx` layout, ESM, imports/exports, entry points, workspaces, optional integrations, generated code, or packed packages.
4. `ts-async` - load for promises, cancellation, resource lifetime, startup/shutdown, callbacks, retries, subprocesses, or structured errors.
5. `ts-docs` - load for published exports, TSDoc/JSDoc, declaration-facing semantics, examples, or generated API documentation.
6. `ts-environment` - load for Bun/package-manager choice, lockfiles, compiler profiles, local tooling, formatter/linter ownership, dependencies, CI, or runtime compatibility.

## Project rules

1. `environment` - load when running shell commands, selecting the repository's Python or TypeScript toolchain, adding wrappers/scripts, or fixing wrong-environment failures for coding agents.
2. `format` - load when running or reviewing lint, format, import order, or repo command wrappers.
3. `test` - load when adding behavior, tests, examples, smoke checks, provider routes, or LLM/MCP integration evidence.
4. `docs` - load when changing user-facing APIs, Mintlify pages, sibling docs repos, generated artifacts, Linear status, release notes, or commits.
5. `review` - load for PR/diff review, inline comments, waivers, or final quality gates.
6. `extension` - load when adding or reviewing any open plugin/provider/backend/handler family, Registry, manifest, entry point, resolver/loader, or bundled/external parity—even before a registry exists.
7. `interfaces` - load when a package is provided as a service; when separating Python SDK, `api/`, CLI, GUI, MCP, or TUI layers; or when designing REST/OpenAPI, concurrent requests, modular Typer/Click/argparse CLIs, minimal Python GUIs, or React/Tauri desktop apps.

Examples live inside their owning rules. Do not add a separate demo rule surface unless a future project has concrete evidence that search/routing works better with separate example files.

## Design rules

On-demand references outside the default coding loop; load only when the task matches:

1. `gui-style` (`references/design/gui-style.md`) - load for GUI, frontend, dashboard, app-shell, desktop-tool, theme/token, or design-system work in any framework.

## Failure playbooks

Use `references/failures/` when command failures block progress:

1. `failure-env` - Python, `uv`, shell, PATH, or wrong environment failures.
2. `failure-network-proxy` - CLI/API network failures, VPN/proxy ambiguity, or provider connectivity.
3. `failure-auth-secrets` - MCP/provider auth expiry, missing API keys, Linear/Tavily/LLM token failures, or direct API fallback.
4. `failure-linear-pressure` - Linear project issue limits, noisy progress comments, or stale Done/Duplicated/Outdated issue cleanup.
