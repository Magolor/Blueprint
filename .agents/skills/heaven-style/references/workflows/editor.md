---
id: workflow-editor
title: Editor workflow
enabled: true
audience: editor
keywords: [maintain heaven-style, edit skill, install skill, update rules, update tasks, update failures, update skill version]
description: Use when maintaining this standalone heaven-style skill, changing rules/tasks/failures/workflows, regenerating indexes, installing mirrors, or bumping its independent version.
---

# Editor Workflow

## When to use

Use this surface only when maintaining `heaven-style`: editing `SKILL.md`, rules, design references, workflows, task/failure playbooks, scripts, assets, generated index metadata, or packaged artifacts.

## Skill maintenance workflow

1. Edit the smallest relevant surface:
   - `SKILL.md` for the fast path, task routing, and high-level criteria.
   - `references/tasks/` for stable repeated workflows.
   - `references/rules/code/typescript/` for the primary greenfield TypeScript surface and `references/rules/code/python/` for fully supported Python mechanics.
   - `references/rules/project/` for cross-language repository, interface, verification, and release criteria.
   - `references/examples/code/` for source-neutral comparisons that support multiple rules without becoming mandatory architecture.
   - `references/design/` for framework-neutral GUI/frontend/desktop design.
   - `references/workflows/` for task routing and role-specific execution guidance.
   - `references/failures/` for recurring operational blockers and safe recovery.
2. Keep active tasks few and non-overlapping. Add one only for a stable repeated workflow that cannot fit an existing task.
3. Use trigger-oriented YAML frontmatter; the Markdown body remains normative.
4. Keep brief examples in their owning rule and reusable cross-rule comparisons in `references/examples/code/`.
5. Keep distributed skill text source-neutral: no target/reference-repository names, absolute local checkout paths, machine-specific setup sources or observed versions, borrowed framework internals, or target release coupling. Retain reusable decision criteria, patterns, anti-patterns, and public primary references.
6. Convert project evidence into general philosophy only when it survives comparison across repositories. Keep project architecture in the owning project's docs.
7. Run the canonical skill checkout's `scripts/install.py` after rule/design/script changes. Use `--all-harnesses` when the Claude Code bridge should be refreshed, and `--mirror <path> --skip-global` only for a repository that intentionally embeds a copy.
8. Run `scripts/index.py --check`, the standalone dependency scan, compilation, repository lint/tests, and any target-evidence checks relevant to the changed rule.

## Commands

From the skill root:

```bash
rtk uv run python scripts/install.py
rtk uv run python scripts/index.py --check
rtk uv run python scripts/scan.py --stdlib-only --allow-import yaml scripts
rtk uv run python -m py_compile scripts/index.py scripts/install.py scripts/machine.py scripts/scan.py
```

From an owning repository root, use its declared wrappers for lint and tests. The skill must not encode one source repository's wrapper names as universal policy.

## Self-compliance

- Maintenance scripts are standalone: they do not import a target project package.
- `install.py` indexes and copies the skill without network/reference-project access.
- `scan.py` parses scripts and reports undeclared non-standard-library imports; explicit allowances stay narrow.
- `index.yaml` is a compact deterministic routing projection and is never hand-edited.
- Distributed files contain no target-project architecture or release-version coupling.
- Rules lead with portable quality criteria and decision gates, not one repository's folder tree or tool lineup.
- The skill version follows `MAJOR.MINOR.PATCH.N[devK]`, increments for ordinary edits, and remains independent of target repository versions.

## Install behavior

- The standard user install path is `~/.agents/skills/heaven-style`.
- Legacy version-suffixed installs are removed only after `SKILL.md` verifies they are the same skill.
- `--all-harnesses` installs the common Agent Skill plus a Claude Code plugin bridge without writing a duplicate plain Claude skill.
- `--mirror` copies the same standalone skill into an explicitly selected repository and regenerates its index.
- Local reference checkouts, if a maintainer uses them as evidence, remain outside the distributed skill and are never refreshed implicitly by installation.
