---
name: heaven-style
description: Standalone personal code-quality, architecture, documentation, graphical-interface, and project-management guide for TypeScript and Python repositories. Use when writing or reviewing code or docs, designing architecture or UI, refactoring, or aligning tests; apply repository policy first, then shared design philosophy and the matched language rules.
metadata:
  version: 0.1.2.15
---

# Heaven Style

## Default Use

Use Heaven Style when coding, writing or reviewing documentation, designing or reviewing a graphical interface, refactoring, or aligning tests in TypeScript or Python repositories. Reading this file is enough for normal coding tasks. First identify the target language, repository toolchain, declared infrastructure owners, documentation authority, and compatibility policy, then load only the rules needed for public APIs, shared utilities, storage/query behavior, extension points, graphical surfaces, authored docs, broad refactors, or an unclear tradeoff.

For TypeScript, start from [TypeScript architecture](references/rules/code/typescript/architecture.md), then select the matched utility, API, type, configuration, module, async, SQL/data, documentation, compatibility, and environment rules. Treat browser, server, worker, runtime, and package boundaries as explicit contracts. For Python, use the target package's public facade and declared utility, configuration, database, and error owners; otherwise use normal Python standard-library or established dependency APIs directly. Never add a platform dependency merely to satisfy this skill.

When a new or unspecified project has not selected a language, frame architecture and examples in TypeScript first. This is a greenfield default, not permission to migrate an existing coherent Python repository or overwrite its toolchain conventions.

Repo-specific `AGENTS.md` wins for environment, command wrappers, test model policy, demo paths, and release discipline. For shell commands, load [references/rules/project/environment.md](references/rules/project/environment.md).

## Design Philosophy

After the target repository's `AGENTS.md`, runtime contract, and public compatibility policy, these principles govern design. A repository may waive one explicitly with evidence; incidental local style does not silently override an architecture boundary.

- **First principles and minimal public surface.** Start from the verified user need, real constraints, and declared compatibility promises. Question inherited assumptions, defensive layers, and workaround-shaped behavior when evidence no longer justifies them. Expose the smallest domain-shaped public surface that satisfies the need. Prefer an owning object when identity or lifecycle is real and a direct function when behavior is stateless. Common flows should read as “construct or load the object, then call its domain verb” or one explicit function call. Avoid constructor side effects, nested pipelines, hidden magic, and clever metaprogramming. An average engineer or agent should reconstruct the architecture from one page.
- **Open-extension parity.** When a product promises third-party extensions, bundled and independently developed implementations use the same public family contract and consumer path. Choose the smallest discovery and lifecycle mechanism that satisfies the promise; a persisted catalog, remote acquisition, or hot replacement is optional architecture, not a default. See [extension points](references/rules/project/extension.md).
- **Open registries, closed unions.** Open provider/backend/handler families extend through authoritative registration and resolution APIs rather than central `if provider ==` chains, fixed package scans, or handwritten built-in import lists. Closed syntax trees, protocols, and state machines use discriminated variants plus exhaustive handling. Do not turn a closed set into a mutable registry or an open ecosystem into an ever-growing switch.
- **Service interfaces are adapters.** Expose domain behavior through a small language-native SDK, keep application orchestration transport-neutral, and make CLI, GUI, MCP, TUI, HTTP, and other interfaces adapt that boundary. The roles are required when the responsibilities exist; their folder and package names are repository decisions.
- **SOLID as boundary diagnostics.** Use [TypeScript architecture](references/rules/code/typescript/architecture.md) or [Python SOLID](references/rules/code/python/solid.md) for SRP, OCP, LSP, ISP, and DIP checks during class, backend, provider, strategy, registry, and architecture work; do not use SOLID slogans to justify speculative layers.
- **Shared infrastructure by ownership.** Prefer the target repository's declared utility, configuration, database, logging, and platform owners. When none exists, use language-standard or established dependency APIs directly and add a shared abstraction only when multiple real consumers need the same policy.
- **Break and fix within the declared compatibility policy.** Internal renames and redesigns update all owned call sites in the same change. Published packages and external protocols follow the repository's support policy; any migration shim has a named consumer, removal condition, and test rather than becoming a permanent parallel API.
- **Compact, explicit code.** Use direct data flow, guard clauses, canonical domain verbs, typed boundaries, and loud contextual failures. TypeScript applies strict types, explicit host/package boundaries, and visible promise/resource ownership. Python uses repository-provided helpers such as `raise_mismatch` only when they exist and own the behavior.
- **Docs are part of the code.** Declare a concise authority map plus separate user, engineering, development-log, and scratch surfaces and one writable task queue. The map routes to owners without duplicating volatile state. Architecture pages, generated artifacts, and examples must match implementation; label current behavior, accepted target, remaining gap, and non-goal. Close work by promoting durable truth, removing closed task state, and deleting or superseding stale material. See [documentation and task lifecycle](references/rules/project/docs.md).

## Task Surface

Use [Start or Resume a Workflow](references/workflows/start.md) to select a route or prepare a request. Use [Work Type Procedures](references/workflows/work-types.md) for the complete start, resume, verification, and closeout contract.

- [references/tasks/code.md](references/tasks/code.md): implementation, bug fix, feature, refactor, tests, docs.
- [references/tasks/code-review.md](references/tasks/code-review.md): diff, PR, branch, module, recent changes, or Linear-issue review.
- [references/tasks/doc-sync.md](references/tasks/doc-sync.md): create, restructure, review, audit, or sync canonical authored docs, generated documentation, navigation, and declared projections.
- [references/tasks/doc-trans.md](references/tasks/doc-trans.md): YAML-frontmatter, line-aligned English and Simplified Chinese Markdown/MDX pairs when explicitly requested.
- [references/tasks/test-compress.md](references/tasks/test-compress.md): audit and compress TypeScript or Python test suites by pruning low-value tests while preserving behavioral contracts and repository-defined tiers.
- [references/tasks/code-explain.md](references/tasks/code-explain.md): explain architecture, data flow, modules, feature behavior, or code-change comparisons for newcomers.
- [references/tasks/env.md](references/tasks/env.md): maintain system environment plans, guardrails, and local machine-operation handoffs.
- [references/tasks/arch-design.md](references/tasks/arch-design.md): architecture design, periodic architecture review, module boundaries, dependency health, and agile design plans.
- [references/tasks/manager.md](references/tasks/manager.md): track GitHub and Linear status, stale work, recent work, and next-step orchestration.
- [references/tasks/skill-update.md](references/tasks/skill-update.md): update this skill from repo-owned contracts, primary public docs, scripts, and recurring verified failure patterns.

Keep task playbooks inside this skill by default. Separate wrapper skills such as `heaven-code` or `heaven-review` are useful only as thin discoverability aliases; they should link here and must not duplicate rule text.

## Normal Coding Loop

1. Inspect `AGENTS.md`, the declared task queue, the project command rule plus matched language environment, issue context if provided, lint/test entrypoints, docs authority map, config patterns, and nearby source before editing.
2. Brainstorm only when requirements or design are uncertain: present the best option plus tradeoffs, then detail the plan once accepted.
3. Claim or create one durable task when work must survive the session, then plan small slices with success criteria, touched APIs, storage/query impact, docs/example impact, tests, and explicit non-goals. Do not create a parallel task list in the plan.
4. For Linear-driven work, read or create the issue, record acceptance criteria, and keep status aligned with the code. For continuous issues, edit one rolling status comment instead of adding routine progress comments.
5. Implement minimal diffs using existing project style, declared infrastructure owners, and the selected language rules. Do not introduce a framework dependency merely to imitate another repository's mechanics.
6. Exercise the behavior with a small probe or demo when useful, then run targeted tests through repository-declared entrypoints.
7. Review the diff against the criteria below, fix confirmed issues, and repeat test/review until no blocking findings remain.
8. Run the repository's static/format gates; sync user/engineering docs, examples, generated artifacts, the development log, scratch cleanup, task/issue state; then report changes, verification, risks, and waivers.

## Coding Criteria

- **Code quality:** follow the target language rules, repository metadata, and supported entry points. TypeScript uses strict compiler boundaries, explicit runtime/ESM/package contracts, and repository-owned local tools. Python uses the repository's declared infrastructure or normal Python APIs when no owner exists.
- **Modularity:** name logical roles before choosing folders. Keep domain behavior, application use cases, transports, and user interfaces directionally separate; earn physical package boundaries through independent consumers, runtimes, dependencies, releases, or artifact checks. Use explicit registration for open families and exhaustive variants for closed protocols.
- **Brevity:** prefer compact readable code, guard clauses, and direct data flow; remove boilerplate, duplicate logic, and unnecessary wrappers without hiding invariants in dense expressions.
- **Ease of use:** keep the user/developer mental model obvious; prefer owning-object methods when identity or lifecycle is real and direct functions when behavior is stateless. Avoid parallel APIs, constructor side-effect flags, unnecessary classes, or alternate-name-heavy methods.
- **Cleanliness:** no ad-hoc hacks, debug prints, dead code, stale placeholders, or unapproved/expired aliases and compatibility shims.
- **API documentation:** TypeScript user-facing APIs use semantic TSDoc in `/** ... */`; non-obvious implementation contracts use `//`. Both explain meaning, lifecycle, ownership, failure, and constraints that types cannot express, never names or types alone. Python public APIs use complete type hints and Google-style docstrings. Do not copy either language's documentation mechanics into the other.
- **Authored documentation:** Human-facing Markdown/MDX follows the repository's page and metadata contract, maps claims to authoritative evidence, and uses professional controlled technical prose. Authored bilingual pairs use YAML frontmatter and exact line alignment; this does not add checksum, sidecar, template, or CI requirements.
- **Robustness:** validate untrusted boundaries, preserve contextual errors, avoid swallowed exceptions and unowned promises, and cover edge/error/lifecycle paths. Use `raise_mismatch` only where a Python repo provides it.
- **Sync:** tests, examples, docs, architecture markdown, generated artifacts, relevant sibling docs, and issue state must match the code when relevant.

## Daily Notices

- In TypeScript, use the repository's declared platform, utility, and configuration owners. Otherwise prefer direct Web/Node/Bun or established dependency APIs over thin wrappers, and keep host-specific I/O behind explicit runtime boundaries.
- Keep public interfaces small. Treat exported APIs, package entries, CLI behavior, user-configurable input, user interactions, tools, events, wire/file formats, and documented promises as public surfaces. Each surface must serve a verified need. Use the shortest domain-shaped flow, canonical verbs, complete language-native types and API documentation, and one obvious way to do each task.
- For genuinely open provider/backend/handler families, give bundled and external items the same public contract and selection path. Add persisted discovery, acquisition, trust, or lifecycle machinery only when the product actually promises those capabilities.
- For services, keep dependencies flowing from interfaces and transports through an application boundary into domain behavior. Treat those as logical roles first; use one cohesive package or earned workspace packages according to runtime, dependency, consumer, release, and artifact pressure. A distinct GUI toolchain usually belongs under an app root, but repository policy chooses the exact folder and host.
- In TypeScript, reserve registries for open extension families and use discriminated unions with exhaustive checks for closed protocols and state machines.
- In TypeScript, keep the public vocabulary JavaScript-native: classes own identity/state/lifecycle, stateless transforms stay functions, defaults use `??`, parsed values remain `unknown` until validated, and helpers must own more than a renamed platform call.
- In TypeScript, keep durable configuration independent from process-local dependency injection or plugin contexts: validate JSON-shaped input, retain raw layers, resolve one detached readonly snapshot, and publish only after an async backend commits the expected revision.
- In TypeScript, repo metadata wins. For greenfield work, treat Bun and pnpm as co-preferred: choose Bun for a compact Bun-native app/toolchain, or pnpm for a Node-first library, service, or workspace whose package and artifact fidelity matters. Use other managers only when repository or ecosystem evidence favors them. Commit one lockfile, pin local tools, run frozen installs in CI, and keep compiler/runtime/package exports aligned.
- In TypeScript, keep `strict`, unchecked-index and exact-optional checks enabled; accept external values as `unknown`, validate once at the boundary, and make every promise, cancellation path, and disposable resource visibly owned.
- In TypeScript, use `/** ... */` only for user-facing API documentation and `//` for implementation comments. Follow concise Google-style TSDoc: explain caller-relevant semantics that names and types do not establish; do not manufacture boilerplate for obvious re-exports or private helpers.
- In Python, use the repository's declared utility and configuration owners. If none exists, prefer direct standard-library or established dependency APIs over thin local wrappers.
- In Python, treat public API docstrings as part of the contract: comprehensive Google-style sections should explain arguments, returns or yields, exceptions, examples, and literal options clearly enough to call the API without reading its body.
- For docs, verify facts against their strongest owners, shape the page around reader outcome and recovery, use realistic examples, and apply a non-certified ASD-STE100-inspired clarity pass without weakening modality or exceptions. Repository format wins; authored bilingual pages use YAML frontmatter and exact line alignment, while translation remains separately scoped unless repository policy says otherwise.
- For resumable work, use the one task queue declared by the repository. Plans, reports, goals, development logs, GitHub/Linear mirrors, and chat may link to it but must not become competing writable queues.
- Keep one repository-owned agent policy. When a harness needs a named instruction file that it does not derive from the canonical policy, use the smallest supported checked-in bridge instead of copying the rules; for Claude Code, prefer a root `CLAUDE.md` whose sole content is `@AGENTS.md` when no Claude-only instruction is required.
- Separate user docs, engineering truth, one declared development-log surface, and expiring scratch. A repository may use one rolling log or immutable dated entries behind a routing index; it must not keep competing chronologies. When work closes, promote stable conclusions, remove closed queue rows, and delete or supersede stale plans/reviews/notes instead of preserving execution chatter as current documentation.
- For reviews, assume parallel human/agent work may be happening. Re-read the current diff before judging or fixing, and never revert changes you did not make without explicit approval.
- For GUI/UX work—including maintenance, refactors, transfers, demos, and temporary HTML—treat attention as a finite budget: keep one view-level focus, make every persistent element earn its salience, reuse one element/spacing/motion language, preserve the exact six-mode palette and its named themes, and make maintenance converge instead of creating style islands. See [GUI style](references/design/gui-style.md).
- When maintaining this skill, distill learned rules into source-neutral patterns and anti-patterns. Do not publish private/reference-repo names, local checkout paths, machine-specific setup sources, or incidental implementation provenance.
- Versioning uses `MAJOR.MINOR.PATCH.N[devK]` (for example `0.1.2.3`). Bump `N` for ordinary skill edits and use optional `devK` for in-development snapshots unless the user records an explicit no-bump waiver. The skill version is independent of any target repository's release version.

## Rule Map

Use [references/rules/overview.md](references/rules/overview.md) to choose files. Common IDs:

- TypeScript code rules: `ts-util`, `ts-architecture`, `ts-api`, `ts-types`, `ts-config`, `ts-modules`, `ts-async`, `ts-sql`, `ts-docs`, `ts-compat`, `ts-environment`.
- Python code rules: `util`, `config`, `types`, `docstring`, `oop`, `model`, `solid`, `name`, `files`, `py`, `clean`, `error`, `sql`, `compat`.
- Project rules: `environment`, `format`, `test`, `docs`, `review`, `extension`, `interfaces`.

Load [references/workflows/start.md](references/workflows/start.md) when the next task route or resume context is unclear. Load [references/tasks/arch-design.md](references/tasks/arch-design.md) for architecture design, periodic architecture review, module boundaries, refactor plans, goals updates, API standard tables, and step-by-step execution plans before implementation; it routes to [references/workflows/architect.md](references/workflows/architect.md). Load [references/workflows/developer.md](references/workflows/developer.md) for large refactors, public API design, shared utility work, or rule tradeoffs while coding. Load [references/workflows/editor.md](references/workflows/editor.md) only when maintaining this skill.

## Common Gotos

- Start, resume, hand off, or select a workflow: [references/workflows/start.md](references/workflows/start.md).
- TypeScript file/path/resource/serialization/logging/hash/temp/subprocess or host-API issue: [references/rules/code/typescript/util.md](references/rules/code/typescript/util.md).
- TypeScript public API, class-versus-function, method-vocabulary, fallback, control-flow, or helper-cleanliness issue: [references/rules/code/typescript/api.md](references/rules/code/typescript/api.md).
- Open extension contracts, manifests, entry points, optional registries/catalogs, resolver/loaders, or bundled/external parity: [references/rules/project/extension.md](references/rules/project/extension.md).
- Open extension vocabulary, hard-coded capability fields, or feature-specific base-method smell: [open capability vocabulary](references/examples/code/open-capability-vocabulary.md).
- TypeScript architecture, open/closed extension seam, capability, strategy, or dependency-boundary issue: [references/rules/code/typescript/architecture.md](references/rules/code/typescript/architecture.md).
- TypeScript strictness, `unknown`, unions, brands, readonly ownership, or resolved-config issue: [references/rules/code/typescript/types.md](references/rules/code/typescript/types.md).
- TypeScript configuration, JSON/YAML boundaries, overrides, path edits, revisions, secrets, scopes, or storage backends: [references/rules/code/typescript/config.md](references/rules/code/typescript/config.md).
- TypeScript ESM, package exports, feature layout, workspace boundary, or consumer-package issue: [references/rules/code/typescript/modules.md](references/rules/code/typescript/modules.md).
- TypeScript promise, cancellation, lifecycle, callback, error, retry, or subprocess issue: [references/rules/code/typescript/async.md](references/rules/code/typescript/async.md).
- TypeScript SQL, driver/ORM, bind, migration, transaction, pool, or row-validation issue: [references/rules/code/typescript/sql.md](references/rules/code/typescript/sql.md).
- TypeScript TSDoc/JSDoc or published export documentation issue: [references/rules/code/typescript/docs.md](references/rules/code/typescript/docs.md).
- TypeScript rename, package export, runtime floor, deprecation, alias, wire/config, or data-migration issue: [references/rules/code/typescript/compat.md](references/rules/code/typescript/compat.md).
- Bun, pnpm, lockfile, TypeScript compiler, formatter/linter, dependency, Node runtime, or TypeScript CI issue: [references/rules/code/typescript/environment.md](references/rules/code/typescript/environment.md).
- Python config/default/provider issue: [references/rules/code/python/config.md](references/rules/code/python/config.md).
- Python stdlib/path/file/serialization/shell/logging issue: [references/rules/code/python/util.md](references/rules/code/python/util.md).
- Python public API docstring, Google-style section, or Markdown-in-docstring issue: [references/rules/code/python/docstring.md](references/rules/code/python/docstring.md).
- Python file/package organization, lazy export, or `__init__.pyi` issue: [references/rules/code/python/files.md](references/rules/code/python/files.md).
- Python public API or mental-model issue: [references/rules/code/python/model.md](references/rules/code/python/model.md) and [references/rules/code/python/oop.md](references/rules/code/python/oop.md).
- Python SOLID boundary, inheritance, provider/strategy dependency, or extension-point issue: [references/rules/code/python/solid.md](references/rules/code/python/solid.md).
- Service roles, language-native SDK/application/transport split, REST/OpenAPI, CLI/GUI/MCP/TUI, package boundaries, or desktop host issue: [references/rules/project/interfaces.md](references/rules/project/interfaces.md).
- Cohesive versus workspace service layout, app placement, or UI/host/application dependency arrows: [references/examples/code/local-gui-layout.md](references/examples/code/local-gui-layout.md).
- GUI/UX/frontend/dashboard creation, maintenance, refactor, transfer, demo, temporary HTML, attention hierarchy, theme/color, component unity, spacing/density, motion/animation, progressive disclosure, or interface-review issue: [references/design/gui-style.md](references/design/gui-style.md).
- Shell commands, `rtk`, uv, Bun, pnpm, Node runtime, or wrapper/package-script policy: [references/rules/project/environment.md](references/rules/project/environment.md).
- Tests/examples/integration issue: [references/rules/project/test.md](references/rules/project/test.md).
- Authored-doc creation, review, audit, canonical sync, generated docs, or sibling projections: [references/tasks/doc-sync.md](references/tasks/doc-sync.md).
- Line-aligned English–Chinese documentation translation: [references/tasks/doc-trans.md](references/tasks/doc-trans.md).
- Architecture/module explanation: [references/tasks/code-explain.md](references/tasks/code-explain.md).
- Architecture design, periodic review, refactor plans, goals, and execution plans: [references/tasks/arch-design.md](references/tasks/arch-design.md).
- Project status and orchestration: [references/tasks/manager.md](references/tasks/manager.md).
- Skill maintenance and independent versioning: [references/tasks/skill-update.md](references/tasks/skill-update.md).
- Local machine facts: ignored `assets/instance/*.local.md` files; refresh with [scripts/machine.py](scripts/machine.py).
- System environment maintenance: [references/tasks/env.md](references/tasks/env.md); shared macOS operations live in [assets/MacOS-env.md](assets/MacOS-env.md).
- Environment, proxy, auth, or Linear pressure failures: [references/failures/env.md](references/failures/env.md), [references/failures/network-proxy.md](references/failures/network-proxy.md), [references/failures/auth-secrets.md](references/failures/auth-secrets.md), [references/failures/linear-pressure.md](references/failures/linear-pressure.md).

## Verification

Follow [references/rules/project/environment.md](references/rules/project/environment.md). Prefix **every** agent shell command with `rtk` when the session provides it.

For TypeScript work, preserve the repository's declared package manager and scripts. In greenfield work choose Bun or pnpm from runtime, package-consumer, and workspace evidence, then use that manager's frozen install and checked scripts; see [TypeScript environment](references/rules/code/typescript/environment.md).

For repo Python work, prefer repo wrappers or `rtk uv run python`; reserve `rtk python` for deliberate PATH/system-Python diagnostics.

```bash
rtk uv run python .agents/skills/heaven-style/scripts/scan.py --stdlib-only --allow-import yaml .agents/skills/heaven-style/scripts
rtk bash scripts/flake.bash --ci
rtk bash scripts/test.bash
```

For a Bun-based TypeScript target, use the scripts actually declared by that repository, typically:

```bash
rtk bun ci
rtk bun run check
```

When `uv` is unavailable in a known-good skill-maintenance shell, bare `python` for the skill's standalone maintenance scripts is acceptable.

## Review Route

For code, diff, branch, PR, module, or recent-change reviews, load [references/tasks/code-review.md](references/tasks/code-review.md). Code reviews are findings-first and severity-marked; save `docs/reports/reviews/` artifacts only for durable Linear/PR gates or when the user asks, and normally wait for human annotation before fixes unless the user asks to proceed. For authored-document reviews or audits, keep [documentation writing and sync](references/tasks/doc-sync.md) as the primary route and use the target repository's review/report policy.
