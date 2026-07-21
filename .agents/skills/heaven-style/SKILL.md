---
name: heaven-style
description: Heaven-style code and architecture guide for general Python package development and TypeScript repositories, with conditional conventions for HeavenBase-lineage projects. Use when writing, reviewing, designing architecture, refactoring, or aligning tests/docs; apply repository policy first, then shared architecture and the matched language rules.
metadata:
  version: 0.1.2.0
---

# Heaven Style

## Default Use

Use Heaven Style when coding, reviewing, refactoring, or aligning docs/tests in Python packages or TypeScript repositories. Reading this file is enough for normal coding tasks. First identify the target language, repository toolchain, declared infrastructure owners, and compatibility policy, then load only the rules needed for public APIs, shared utilities, storage/query behavior, extension points, broad refactors, or an unclear tradeoff.

For Python, use the target package's public facade, utility layer, configuration owner, database layer, and error helpers when the repository declares them; otherwise use normal Python standard-library or established dependency APIs directly. Do not add HeavenBase merely to satisfy this skill. In a HeavenBase-lineage repository that explicitly adopts its infrastructure, prefer `heavenbase`, `heavenbase.utils`, and `CM_HVNB` for their owned concerns. For TypeScript, transfer Heaven's design intent rather than Python mechanics; start at [TypeScript architecture](references/rules/code/typescript/architecture.md), then use the TypeScript type, module, async, documentation, and environment rules.

Repo-specific `AGENTS.md` wins for environment, command wrappers, test model policy, demo paths, and release discipline. For shell commands, load [references/rules/project/environment.md](references/rules/project/environment.md).

## Design Philosophy

After the target repository's `AGENTS.md`, runtime contract, and public compatibility policy, these principles govern design. A repository may waive one explicitly with evidence; incidental local style does not silently override an architecture boundary.

- **Minimal mental model.** Expose the shortest domain-shaped front door. Prefer an owning object when identity or lifecycle is real and a direct function when behavior is stateless. Common flows should read as `obj = Class(...); obj.verb()` or one explicit function call. Avoid constructor side effects, nested pipelines, hidden magic, and clever metaprogramming. An average engineer or agent should reconstruct the architecture from one page.
- **Lego-style extension parity.** For every genuinely open extension family, bundled and independently developed implementations are peers: the same descriptor, Registry resolution, loader, validation, lifecycle, public configuration, invocation, inspection, and contract tests apply regardless of source. An extension may live outside the host package without requiring a host source edit or release. Origin such as `system`, `local`, or `remote` is provenance and policy metadata, never a privileged dispatch path. See [extension points](references/rules/project/extension.md).
- **Open registries, closed unions.** Open provider/backend/handler families extend through authoritative registration and resolution APIs rather than central `if provider ==` chains, fixed package scans, or handwritten built-in import lists. Closed syntax trees, protocols, and state machines use discriminated variants plus exhaustive handling. Do not turn a closed set into a mutable registry or an open ecosystem into an ever-growing switch.
- **Service interfaces are adapters.** Service packages expose core behavior through a small Python SDK, place orchestration and transport contracts in a real [`api/` boundary](references/rules/project/interfaces.md), and keep CLI, GUI, MCP, TUI, and other interfaces as thin wrappers over that boundary.
- **SOLID as boundary diagnostics.** Use [Python SOLID](references/rules/code/python/solid.md) or [TypeScript architecture](references/rules/code/typescript/architecture.md) for SRP, OCP, LSP, ISP, and DIP checks during class, backend, provider, strategy, registry, and architecture work; do not use SOLID slogans to justify speculative layers.
- **Shared infrastructure by ownership.** Prefer the target repository's declared utility, configuration, database, logging, and platform owners. When none exists, use language-standard or established dependency APIs directly and add a shared abstraction only when multiple real consumers need the same policy. HeavenBase-specific helpers apply only to repositories that explicitly adopt them.
- **Break and fix within the declared compatibility policy.** Internal renames and redesigns update all owned call sites in the same change. Published packages and external protocols follow the repository's support policy; any migration shim has a named consumer, removal condition, and test rather than becoming a permanent parallel API.
- **Compact, explicit code.** Use direct data flow, guard clauses, canonical domain verbs, typed boundaries, and loud contextual failures. In Python, use repository-provided helpers such as `raise_mismatch` only when they exist and own the behavior; in TypeScript, apply strict types, explicit ownership, and promise/lifecycle rules.
- **Docs are part of the code.** Declare separate user, engineering, development-log, and scratch surfaces. An operational repository declares exactly one writable task authority; a template-source repository may carry an inert queue starter for generated projects but must not masquerade as owning live project work. Architecture pages, generated artifacts, and examples must match implementation; label current behavior, accepted target, remaining gap, and non-goal. Close work by promoting durable truth, removing closed task state, and deleting or superseding stale material. See [documentation and task lifecycle](references/rules/project/docs.md).

## Task Surface

- [references/tasks/code.md](references/tasks/code.md): implementation, bug fix, feature, refactor, tests, docs.
- [references/tasks/code-review.md](references/tasks/code-review.md): diff, PR, branch, module, recent changes, or Linear-issue review.
- [references/tasks/doc-sync.md](references/tasks/doc-sync.md): sync English HeavenBase docs, Mintlify pages, navigation, and sibling docs repos.
- [references/tasks/doc-trans.md](references/tasks/doc-trans.md): line-aligned Chinese (`zh/`) MDX translation when explicitly requested.
- [references/tasks/test-compress.md](references/tasks/test-compress.md): audit and compress pytest suites by pruning low-value tests, preserving behavioral contracts, and tagging fast/full coverage.
- [references/tasks/code-explain.md](references/tasks/code-explain.md): explain architecture, data flow, modules, feature behavior, or code-change comparisons for newcomers.
- [references/tasks/env.md](references/tasks/env.md): maintain system environment plans, guardrails, and local machine-operation handoffs.
- [references/tasks/arch-design.md](references/tasks/arch-design.md): architecture design, periodic architecture review, module boundaries, dependency health, and agile design plans.
- [references/tasks/manager.md](references/tasks/manager.md): track GitHub and Linear status, stale work, recent work, and next-step orchestration.
- [references/tasks/skill-update.md](references/tasks/skill-update.md): update this skill from repo-owned contracts, packaged reference assets, primary public docs, scripts, and recurring verified failure patterns.

Keep task playbooks inside this skill by default. Separate wrapper skills such as `heaven-code` or `heaven-review` are useful only as thin discoverability aliases; they should link here and must not duplicate rule text.

## Normal Coding Loop

1. Inspect `AGENTS.md`, the declared task authority when the repository has one, the project command rule plus matched language environment, issue context if provided, lint/test entrypoints, docs authority map, config patterns, and nearby source before editing.
2. Brainstorm only when requirements or design are uncertain: present the best option plus tradeoffs, then detail the plan once accepted.
3. In an operational repository, claim or create one durable task when work must survive the session, then plan small slices with success criteria, touched APIs, storage/query impact, docs/example impact, tests, and explicit non-goals. A template-source repository without a live task authority uses the direct request or its declared external tracker and never invents an active queue merely to satisfy this skill. Do not create a parallel task list in the plan.
4. For Linear-driven work, read or create the issue, record acceptance criteria, and keep status aligned with the code. For continuous issues, edit one rolling status comment instead of adding routine progress comments.
5. Implement minimal diffs using existing project style, declared infrastructure owners, and the selected language rules. Do not introduce a framework dependency merely to imitate another repository's mechanics.
6. Exercise the behavior with a small probe or demo when useful, then run targeted tests through repository-declared entrypoints.
7. Review the diff against the criteria below, fix confirmed issues, and repeat test/review until no blocking findings remain.
8. Run the repository's static/format gates; sync user/engineering docs, examples, generated artifacts, the development log, scratch cleanup, task/issue state; then report changes, verification, risks, and waivers.

## Coding Criteria

- **Code quality:** follow the target language rules, repository metadata, and local public facade. Python uses the repository's declared infrastructure or normal Python APIs when no owner exists; HeavenBase APIs are conditional lineage conventions. TypeScript uses strict compiler boundaries, explicit ESM/package contracts, and repository-owned local tools.
- **Modularity:** keep ownership boundaries clean; for service packages, separate the core SDK, `api/` orchestration, and thin interfaces; extend open backend/provider/handler families through one authoritative Registry path with built-in/external parity, and model closed protocols with exhaustive variants; avoid planner or business-logic shortcuts.
- **Brevity:** prefer compact readable code, guard clauses, and direct data flow; remove boilerplate, duplicate logic, and unnecessary wrappers without hiding invariants in dense expressions.
- **Ease of use:** keep the user/developer mental model obvious; prefer owning-object methods when identity or lifecycle is real and direct functions when behavior is stateless. Avoid parallel APIs, constructor side-effect flags, unnecessary classes, or alternate-name-heavy methods.
- **Cleanliness:** no ad-hoc hacks, debug prints, dead code, stale placeholders, or unapproved/expired aliases and compatibility shims.
- **API documentation:** Python public APIs use complete type hints and Google-style docstrings. TypeScript published exports and stable seams use semantic TSDoc/JSDoc for meaning, lifecycle, ownership, failure, and constraints that types cannot express; do not copy Python section requirements into TypeScript.
- **Robustness:** validate untrusted boundaries, preserve contextual errors, avoid swallowed exceptions and unowned promises, and cover edge/error/lifecycle paths. Use `raise_mismatch` only where a Python repo provides it.
- **Sync:** tests, examples, docs, architecture markdown, generated artifacts, relevant sibling docs, and issue state must match the code when relevant.

## Daily Notices

- In Python, use the repository's declared utility and configuration owners. If none exists, prefer direct standard-library or established dependency APIs over thin local wrappers. Use `heavenbase.utils` and `CM_HVNB` only where the target repository explicitly adopts HeavenBase infrastructure.
- Keep public APIs small: use the shortest domain-shaped flow, canonical verbs, complete language-native types and API documentation, and one obvious way to do each task.
- In Python, treat public API docstrings as part of the contract: comprehensive Google-style sections should explain arguments, returns or yields, exceptions, examples, and literal options clearly enough to call the API without reading its body.
- For genuinely open provider/backend/handler families, make bundled and external items traverse the same persisted catalog, resolver, loader, validation, lifecycle, and contract tests. Register capabilities instead of editing central planners, routing tables, fixed-path imports, or privileged built-in lists.
- For service packages, keep dependencies flowing `interfaces -> api -> core`: Python exposes the core SDK; CLI/GUI/MCP/TUI call the API boundary. Python CLIs compile one registry to Typer, Click, and argparse, default to Typer, and share Rich output.
- In TypeScript, reserve registries for open extension families and use discriminated unions with exhaustive checks for closed protocols and state machines.
- In TypeScript, repo metadata wins; use Bun by default only for a new repo without a contrary toolchain, commit one lockfile, pin local tools, run frozen installs in CI, and keep compiler/runtime/package exports aligned.
- In TypeScript, keep `strict`, unchecked-index and exact-optional checks enabled; accept external values as `unknown`, validate once at the boundary, and make every promise, cancellation path, and disposable resource visibly owned.
- For docs, verify facts against code, write in friendly professional prose, use realistic code demos, and run Mintlify checks when the docs repo supports them.
- For resumable work in an operational repository, use its one declared task authority. Plans, reports, goals, development logs, GitHub/Linear mirrors, and chat may link to it but must not become competing writable queues. Template-source repositories keep queue starters inert until a concrete project is instantiated.
- Separate user docs, engineering truth, the rolling development log, and expiring scratch. When work closes, promote stable conclusions, remove closed queue rows, and delete or supersede stale plans/reviews/notes instead of preserving execution chatter as current documentation.
- For reviews, assume parallel human/agent work may be happening. Re-read the current diff before judging or fixing, and never revert changes you did not make without explicit approval.
- When maintaining this skill, distill learned rules into source-neutral patterns and anti-patterns. Do not publish private/reference-repo names, local checkout paths, machine-specific setup sources, or incidental implementation provenance.
- Versioning uses `MAJOR.MINOR.PATCH.N[devK]` (for example `0.1.2.1`). The current heaven-style train is `0.1.2`; normally bump `N` for skill-only edits and use optional `devK` for in-development snapshots, unless the user records an explicit no-bump waiver. The skill may lead HeavenBase between releases; align skill `metadata.version` with `heavenbase.version.__version__` on HeavenBase-aligned releases.
- Predecessor names (`pyheaven`, `heaven`, `AgentHeaven`) are legacy; see [references/rules/code/python/compat.md](references/rules/code/python/compat.md).

## Rule Map

Use [references/rules/overview.md](references/rules/overview.md) to choose files. Common IDs:

- Python code rules: `util`, `config`, `types`, `docstring`, `oop`, `model`, `solid`, `name`, `files`, `py`, `clean`, `error`, `sql`, `compat`.
- TypeScript code rules: `ts-architecture`, `ts-types`, `ts-modules`, `ts-async`, `ts-docs`, `ts-environment`.
- Project rules: `environment`, `format`, `test`, `docs`, `review`, `extension`, `interfaces`.

Load [references/tasks/arch-design.md](references/tasks/arch-design.md) for architecture design, periodic architecture review, module boundaries, refactor plans, goals updates, API standard tables, and step-by-step execution plans before implementation; it routes to [references/workflows/architect.md](references/workflows/architect.md). Load [references/workflows/developer.md](references/workflows/developer.md) for large refactors, public API design, shared utility work, or rule tradeoffs while coding. Load [references/workflows/editor.md](references/workflows/editor.md) only when maintaining this skill.

## Common Gotos

- Python config/default/provider issue: [references/rules/code/python/config.md](references/rules/code/python/config.md).
- Python stdlib/path/file/serialization/shell/logging issue: [references/rules/code/python/util.md](references/rules/code/python/util.md).
- Python public API docstring, Google-style section, or Markdown-in-docstring issue: [references/rules/code/python/docstring.md](references/rules/code/python/docstring.md).
- Python file/package organization, lazy export, or `__init__.pyi` issue: [references/rules/code/python/files.md](references/rules/code/python/files.md).
- Python public API or mental-model issue: [references/rules/code/python/model.md](references/rules/code/python/model.md) and [references/rules/code/python/oop.md](references/rules/code/python/oop.md).
- Python SOLID boundary, inheritance, provider/strategy dependency, or extension-point issue: [references/rules/code/python/solid.md](references/rules/code/python/solid.md).
- Lego-style extension parity, persisted catalogs, manifests, entry points, resolver/loaders, or built-in/external source independence: [references/rules/project/extension.md](references/rules/project/extension.md).
- Open extension vocabulary, hard-coded capability fields, or feature-specific base-method smell: [open capability vocabulary](references/examples/code/open-capability-vocabulary.md).
- TypeScript architecture, open/closed extension seam, capability, strategy, or dependency-boundary issue: [references/rules/code/typescript/architecture.md](references/rules/code/typescript/architecture.md).
- TypeScript strictness, `unknown`, unions, brands, readonly ownership, or resolved-config issue: [references/rules/code/typescript/types.md](references/rules/code/typescript/types.md).
- TypeScript ESM, package exports, feature layout, workspace boundary, or consumer-package issue: [references/rules/code/typescript/modules.md](references/rules/code/typescript/modules.md).
- TypeScript promise, cancellation, lifecycle, callback, error, retry, or subprocess issue: [references/rules/code/typescript/async.md](references/rules/code/typescript/async.md).
- TypeScript TSDoc/JSDoc or published export documentation issue: [references/rules/code/typescript/docs.md](references/rules/code/typescript/docs.md).
- Bun, lockfile, TypeScript compiler, formatter/linter, dependency, or TypeScript CI issue: [references/rules/code/typescript/environment.md](references/rules/code/typescript/environment.md).
- Service package, Python SDK/API split, REST/OpenAPI, CLI/GUI/MCP/TUI, multi-backend Python CLI, or Tauri desktop issue: [references/rules/project/interfaces.md](references/rules/project/interfaces.md).
- Shell commands, `rtk`, `uv`/Bun, or wrapper/package-script policy: [references/rules/project/environment.md](references/rules/project/environment.md).
- Tests/examples/integration issue: [references/rules/project/test.md](references/rules/project/test.md).
- Docs/Mintlify/sibling-doc sync: [references/tasks/doc-sync.md](references/tasks/doc-sync.md).
- Chinese doc translation: [references/tasks/doc-trans.md](references/tasks/doc-trans.md).
- Architecture/module explanation: [references/tasks/code-explain.md](references/tasks/code-explain.md).
- Architecture design, periodic review, refactor plans, goals, and execution plans: [references/tasks/arch-design.md](references/tasks/arch-design.md).
- Project status and orchestration: [references/tasks/manager.md](references/tasks/manager.md).
- Skill maintenance and version alignment: [references/tasks/skill-update.md](references/tasks/skill-update.md).
- Local machine facts: `assets/instance/*.md`; refresh with [scripts/machine.py](scripts/machine.py).
- System environment maintenance: [references/tasks/env.md](references/tasks/env.md); shared macOS operations live in [assets/MacOS-env.md](assets/MacOS-env.md).
- Environment, proxy, auth, or Linear pressure failures: [references/failures/env.md](references/failures/env.md), [references/failures/network-proxy.md](references/failures/network-proxy.md), [references/failures/auth-secrets.md](references/failures/auth-secrets.md), [references/failures/linear-pressure.md](references/failures/linear-pressure.md).

## Verification

Follow [references/rules/project/environment.md](references/rules/project/environment.md). Prefix **every** agent shell command with `rtk` when the session provides it. For repo Python work, prefer repo wrappers or `rtk uv run python`; reserve `rtk python` for deliberate PATH/system-Python diagnostics.

For TypeScript work, preserve the repository's declared package manager and scripts. In a new Bun-based repository, prefer `rtk bun ci` plus checked `bun run` scripts for format, lint, typecheck, test, build, and the aggregate gate; see [TypeScript environment](references/rules/code/typescript/environment.md).

For the Blueprint/Python skill-maintenance repository, an empty `tests/` directory is valid; `rtk bash scripts/test.bash` should report no tests found and exit successfully.

```bash
rtk uv run python .agents/skills/heaven-style/scripts/scan.py <paths>
rtk bash scripts/flake.bash --ci
rtk bash scripts/test.bash
```

For a Bun-based TypeScript target, use the scripts actually declared by that repository, typically:

```bash
rtk bun ci
rtk bun run check
```

When `uv` is unavailable in a known-good skill-maintenance shell, bare `python .agents/skills/heaven-style/scripts/scan.py <paths>` from the repo root is acceptable.

## Review Route

For review requests, load [references/tasks/code-review.md](references/tasks/code-review.md). Reviews are findings-first and severity-marked; save `docs/reports/reviews/` artifacts only for durable Linear/PR gates or when the user asks, and normally wait for human annotation before fixes unless the user asks to proceed.
