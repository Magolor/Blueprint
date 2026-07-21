---
id: format
title: Imports and formatting
enabled: true
blocking: true
order: 100
category: project
keywords: [import order, line length, flake, black, Biome, ESLint, repo script, package script, wrapper]
description: Use when running or reviewing Python or TypeScript formatters, linters, import order, generated compatibility files, or repository command entry points.
---

# Imports and formatting

## Core rule

Use the repository's declared entrypoints (`scripts/flake.bash`, package scripts, `Makefile`, or equivalent). Do not bypass wrappers/scripts with bare or global tools. For `rtk`, environments, package managers, and wrapper policy, apply [environment.md](environment.md) first.

## Apply when

- Running or reviewing formatting, linting, import order, line length, generated compatibility files, or command wrappers.
- Deciding whether to call Black/Flake8/Biome/ESLint directly or through repo scripts.

## Do

- In Python repos, use the repository's declared wrappers, package scripts, or `Makefile` targets; Blueprint and HeavenBase use `scripts/flake.bash` and `scripts/test.bash`.
- Keep tool configuration in the repository's established owner (`pyproject.toml`, `package.json`, or a checked dedicated config) rather than adding duplicates.
- For TypeScript, keep formatter and linter ownership explicit: prefer Biome for a new lightweight repo, and add type-aware ESLint only for rules that require the type graph. Do not make both tools own formatting or overlapping style rules.
- Use the language's configured import organizer and remove unused imports. For Python without an organizer, alphabetize imports within the established groups.

## Avoid

- Bare tools when wrappers exist.
- In Python, new setup files such as `pytest.ini` or `setup.cfg` unless the tool cannot read `pyproject.toml`.
- Star imports except explicit project utility boilerplate where already established.
- Global TypeScript tools, floating `bunx`/`npx` commands in standing gates, or simultaneous Biome/Prettier formatting.

## Example

**Blueprint/Python anti-pattern:**

```bash
black src
pytest
```

**Blueprint/Python recommended pattern:**

```bash
rtk bash scripts/sync-env.bash
rtk bash scripts/flake.bash -a
rtk bash scripts/test.bash
```

In a Bun-based TypeScript repository, use its declared scripts, typically:

```bash
rtk bun run format:check
rtk bun run lint
rtk bun run typecheck
```

## Python import order

Follow the repository's configured formatter/import sorter. When none exists, use the conventional groups:

1. Standard library.
2. Third-party packages.
3. First-party/local packages.

Alphabetize within groups, separate groups with one blank line, and remove unused imports. Do not reorder repository-mandated facade imports merely to copy another project's utility convention.

## Related rules

Also apply [environment.md](environment.md) for command policy, [test.md](test.md) for test entrypoints, [util.md](../code/python/util.md) when Python import cleanup touches utility-covered stdlib, and [TypeScript environment](../code/typescript/environment.md) when TypeScript tooling changes.
