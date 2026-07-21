---
id: workflow-developer
title: Developer workflow
enabled: true
audience: developer
keywords: [advanced usage, large refactor, planning, architecture review, read all rules, public api design]
description: Use when planning broad work, refactoring shared surfaces, designing public APIs, resolving rule tradeoffs, or needing the full Heaven Style rule set.
---

# Developer Workflow

## When to use

Use this surface for advanced planning while **implementing** large refactors, architecture decisions, public API design, rule tradeoffs, or any coding task where `SKILL.md` plus one task playbook is not enough. Typical triggers: cross-module refactors, shared utility changes, new backends/providers, storage/query behavior, Linear milestones with many slices, coding-standard changes, or disputes between rules.

For **design-only** work — doc organization, module designs, architecture reviews, refactor plans, goals updates, API standard tables, or step-by-step execution plans before code — use [../tasks/arch-design.md](../tasks/arch-design.md), which routes to [architect.md](architect.md); return here once implementation starts.

## Decision workflow

1. Classify the work: feature, bug fix, refactor, public API design, review, docs sync, extension, or skill edit.
2. Read [../rules/overview.md](../rules/overview.md), then load every rule likely to affect the touched surface.
3. Read examples inside the highest-risk rules; examples teach one focus but must satisfy all cross-rules.
4. Read the target repo `AGENTS.md`, command wrappers, config defaults, public docs, architecture notes, and nearby implementation patterns.
5. Map each planned change to rule IDs and identify any waiver before implementation starts.
6. Choose minimal diffs that preserve behavior unless the task explicitly asks for a behavior change.
7. Define verification before editing from the target metadata/toolchain: repository static/format/type/test/build/package gates, targeted tests, examples, docs generators, and issue-status updates. Python uses the repository's declared scanner, environment manager, and wrappers; TypeScript uses its checked package manager/scripts and `ts-environment`.

## Linear milestone loop

Use this loop for large stabilization or migration work:

1. Read the Linear issue, comments, linked issues, attached plan files, and previous review artifacts.
2. Convert the objective into slices with acceptance criteria, explicit non-goals, and verification gates.
3. Implement one slice at a time; after each slice, run a focused probe/test and update the local plan.
4. Review the diff, fix confirmed findings, and rerun targeted validation before broader repository verification.
5. Sync docs, examples, generated docs, and Linear issue status before reporting completion.

## Full-rule reading

For Python public APIs, shared utilities, or broad refactors, load:

- `util`, `config`, `types`, `docstring`, `oop`, `model`, `solid`, `name`, `files`, `py`, `clean`, `error`, `sql`

Load `compat` only for a rename, deprecation, schema migration, predecessor-name cleanup, or repository that explicitly adopts the HeavenBase lineage compatibility profile.

For TypeScript public APIs, packages, services, or broad refactors, load:

- `ts-architecture`, `ts-types`, `ts-modules`, `ts-async`, `ts-docs`, `ts-environment`

Load both language groups only when a real interop boundary crosses them.

Load project rules when the task touches release readiness:

- `environment`, `format`, `test`, `docs`, `review`, `extension`, `interfaces`

Load task playbooks when their triggers match:

- [../tasks/code.md](../tasks/code.md) for implementation, bug fix, feature, refactor, tests, or docs.
- [../tasks/code-review.md](../tasks/code-review.md) for reviews of diffs, branches, modules, recent changes, PRs, or Linear issues.
- [../tasks/doc-sync.md](../tasks/doc-sync.md) for English Mintlify docs, navigation, or sibling docs sync.
- [../tasks/doc-trans.md](../tasks/doc-trans.md) for line-aligned Chinese (`zh/`) MDX translation.
- [../tasks/code-explain.md](../tasks/code-explain.md) for newcomer-oriented architecture, dataflow, module, feature, or diff explanations.
- [../tasks/arch-design.md](../tasks/arch-design.md) for architecture design, periodic architecture review, dependency health, module boundaries, and pre-implementation plans.
- [../tasks/manager.md](../tasks/manager.md) for GitHub/Linear status tracking, stale-work triage, and multi-task orchestration.
- [../tasks/skill-update.md](../tasks/skill-update.md) for maintaining this skill, script contracts, and version alignment.

Load failure playbooks when commands repeatedly fail:

- [../failures/env.md](../failures/env.md) for Python, Conda, shell, and PATH failures.
- [../rules/code/typescript/environment.md](../rules/code/typescript/environment.md) for Bun/Node, lockfile, compiler, or TypeScript package-script failures.
- [../failures/network-proxy.md](../failures/network-proxy.md) for CLI/API network or proxy failures.
- [../failures/auth-secrets.md](../failures/auth-secrets.md) for MCP, provider, Linear, Tavily, LLM API key, token, or GraphQL fallback issues.
- [../failures/linear-pressure.md](../failures/linear-pressure.md) for Linear project issue pressure, blocked issue creation, or comment compression.

## Philosophy

Heaven Style is portable across repositories and languages. In Python, use the target repository's declared utility, configuration, database, logging, and error owners; when none exists, prefer direct standard-library or established dependency APIs over speculative wrappers. Never add HeavenBase merely to satisfy the skill. Repositories that explicitly adopt HeavenBase may use `heavenbase`, `heavenbase.utils`, and `CM_HVNB` for their owned concerns. In TypeScript, use repository-owned platform/config boundaries and host capabilities; do not import Python utility mechanics or create a generic helper layer without demonstrated reuse.

Prefer one canonical API within the repository's recorded compatibility policy. Prefer explicit config ownership over hidden globals. Prefer small, composable public surfaces with stable vocabulary over alternate-name-heavy APIs.

## Planning output

A developer-level plan should include:

- Goal and success criteria.
- Rule IDs that govern the change.
- Public APIs/interfaces affected.
- Implementation approach and non-goals.
- Tests, examples, docs, and verification commands.
- Waivers, compatibility choices, migration notes, and issue-status/doc-sync actions.
