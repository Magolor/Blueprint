---
id: skill-update
task_kind: skill-update
status: active
enabled: true
order: 40
keywords: [update heaven-style, maintain skill, refresh skill, update rules, update tasks, skill version]
triggers: [skill-update, update heaven-style, stabilize heaven-style]
description: Use when maintaining heaven-style TypeScript or Python rules, tasks, workflows, scripts, indexes, versions, evidence, or failure patterns.
related_rules: [overview, ts-util, ts-architecture, ts-api, ts-types, ts-config, ts-modules, ts-async, ts-sql, ts-docs, ts-compat, ts-environment, util, config, files, clean, error, sql, solid, extension, docs, review, environment, format, test, interfaces]
---

# Skill Update Task

## Goal

Keep `heaven-style` aligned with repository-owned contracts, primary public tool documentation, the docs ecosystem, and recurring verified failure patterns without making normal coding slower, coupling the skill to a target project, or leaking source provenance.

## Architecture

- `SKILL.md` is the fast path. A small coding or review task should succeed from it plus one directly matched task/failure/rule file.
- `references/tasks/` contains stable active workflows only: `code`, `code-review`, `doc-sync`, `doc-trans`, `test-compress`, `code-explain`, `env`, `arch-design`, `manager`, and `skill-update`.
- `references/design/` contains framework-neutral design references for GUI, frontend, desktop, dashboard, and app-shell work.
- `references/tasks/arch-design.md` is the task entry point for architecture design and periodic architecture review.
- `references/rules/` contains project rules plus language-selected code criteria: `code/typescript/` is the primary greenfield surface for utilities, architecture, API vocabulary, types, configuration, modules, async/resources, SQL/data, API docs, compatibility, and environment; `code/python/` preserves the full Python mechanics surface.
- `references/examples/code/` contains source-neutral smell comparisons that build reusable design intuition without creating repository-shaped rules.
- `references/rules/code/typescript/architecture.md` owns TypeScript SOLID diagnostics, including open registries versus closed unions; `references/rules/code/python/solid.md` owns their Python expression. Link rather than duplicating examples.
- `references/workflows/start.md` is the role-neutral route for selecting, starting, handing off, and resuming work.
- `references/workflows/architect.md` is the design-only workflow route: docs organization, module designs, architecture reviews, refactor plans, goals updates, API standard tables, and step-by-step execution plans.
- `references/workflows/developer.md` is the expanded planning/refactor route during implementation.
- `references/workflows/editor.md` is the skill-maintenance route.
- `references/failures/` contains recurring blocker playbooks and safe handoff prompts.
- `scripts/index.py` validates frontmatter, IDs, relations, and local links, then generates a compact deterministic `references/index.yaml` routing projection. Parse errors and broken graph edges fail closed.
- `scripts/install.py` is the standalone one-shot updater: index, then install the standard global copy at `~/.agents/skills/heaven-style`; `--all-harnesses` also installs the Claude Code plugin bridge without writing `~/.claude/skills/heaven-style`; `--mirror` copies into repos that intentionally embed the skill.
- `scripts/scan.py` checks maintenance scripts for syntax and undeclared non-standard-library dependencies. It must remain project-neutral and accept narrow explicit third-party allowances such as the indexer's YAML parser.

## Source and installation

- Edit the canonical skill checkout declared by its owning repository; do not infer another target repository as source of truth.
- After rule/task/script/index changes, run the canonical checkout's `scripts/install.py` for the standard global install.
- Use `--mirror <path>` only for repositories that intentionally embed a copy. Keep one declared canonical source and backport emergency mirror fixes immediately.

## Update Workflow

1. Read this file, `SKILL.md`, `references/workflows/editor.md`, the compact generated `references/index.yaml`, and the changed script/task/rule/design/failure surfaces.
2. Read evidence for the affected language before changing rules. Use target repositories' `AGENTS.md`, manifests, runtime pins, lockfiles, configuration, public contracts, representative implementation/tests, and current primary runtime/compiler/tool documentation.
3. Compare repository-owned docs, generated artifacts, prior review reports, and independently inspected reference repositories when relevant. Extract repeated requirements, not one-off preferences or project vocabulary.
4. Update `SKILL.md` only for daily notices, task routing, and default criteria needed for fast coding. Move detailed or situational guidance into task/rule/failure files.
5. Add or revise a task only when the workflow is stable, repeated, and cannot fit an existing task. Keep tasks non-overlapping.
6. Add or revise failure playbooks when the same blocker pattern appears repeatedly and needs a safe recovery path or subagent handoff.
7. Keep examples grounded in double-checked evidence for their language, but make distributed rules and maintenance docs source-neutral. Do not record target/reference-repository names, absolute local checkout paths, machine-specific setup sources or observed versions, borrowed package/framework internals, or incidental implementation provenance. Preserve the reusable decision criterion, pattern, and anti-pattern; link primary public specifications when useful.
8. Keep the skill version on `MAJOR.MINOR.PATCH.N[devK]`. Bump `N` (and optional `devK`) for ordinary skill edits unless the user explicitly requires version preservation. Do not align it to a target repository release.
9. Run `scripts/install.py` from the canonical skill root to refresh the standard global install. Use `--all-harnesses` when Claude Code should consume the generated plugin bridge too. `install.py` must always leave the index current and must not require a target project package.
10. Run validation, including invalid fixtures for every new gate, and report changed surfaces, evidence sources, version changes, commands, and any waivers.

## Version Criteria

- Schema: `MAJOR.MINOR.PATCH.N[devK]` (for example `0.1.2.3`).
- `MAJOR.MINOR.PATCH` is the skill's release train.
- `N` is the very small frequent-updates fourth segment.
- Optional `devK` (`dev0`, `dev1`, …) marks in-development snapshots; omit for stabilized releases.
- The skill version is independent of every repository it reviews or helps maintain.

## Verification

From the canonical owning repository root when it stores the skill at `.agents/skills/heaven-style/`:

```bash
rtk uv run python .agents/skills/heaven-style/scripts/install.py
rtk uv run python .agents/skills/heaven-style/scripts/index.py --check
rtk uv run python .agents/skills/heaven-style/scripts/scan.py --stdlib-only --allow-import yaml .agents/skills/heaven-style/scripts
rtk uv run python -m py_compile .agents/skills/heaven-style/scripts/index.py .agents/skills/heaven-style/scripts/install.py .agents/skills/heaven-style/scripts/machine.py .agents/skills/heaven-style/scripts/scan.py
rtk bash scripts/flake.bash --ci --paths .agents/skills/heaven-style/scripts
```

These are Python commands because the skill-maintenance scripts are Python. Also run the target evidence repo's declared gates when rule examples or behavior depend on it; TypeScript uses its checked package manager/scripts, while Python uses its wrappers. See [../rules/project/environment.md](../rules/project/environment.md).

`index.py --check` must be hermetic and byte-deterministic: no network, configuration/database initialization, user-level writes, or volatile timestamps. Keep routing output succinct; full keywords, ordering, and relationship metadata remain in the owning frontmatter.
