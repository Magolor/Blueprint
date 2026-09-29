---
name: format
description: Use repository formatters, linters, import order, and wrappers.
---

# Imports and formatting

## Summary

Use the repository's declared entrypoints (`scripts/flake.bash`, package scripts, `Makefile`, or equivalent). Do not bypass wrappers/scripts with bare or global tools. For `rtk`, environments, package managers, and wrapper policy, apply [environment](environment.md) first.

## Apply when

- Running or reviewing formatting, linting, import order, line length, generated compatibility files, or command wrappers.
- Deciding whether to call Black/Flake8/Biome/ESLint directly or through repo scripts.

## Do

- Keep tool configuration in the repository's established owner (`pyproject.toml`, `package.json`, or a checked dedicated config) rather than adding duplicates.
- For TypeScript, keep formatter and linter ownership explicit. Biome, Oxlint plus Prettier, or ESLint-based profiles can all be coherent. Do not make multiple tools own formatting or overlapping style rules.
- Python code must pass Black and Flake8 through the repository's declared wrappers, package scripts, or `Makefile` targets. Do not replace that pair merely to copy a TypeScript tool profile.
- Use the language's configured import organizer and remove unused imports. For Python without an organizer, alphabetize imports within the established groups.

## Avoid

- Bare tools when wrappers exist.
- In Python, new setup files such as `pytest.ini` or `setup.cfg` unless the tool cannot read `pyproject.toml`.
- Star imports except explicit project utility boilerplate where already established.
- Global TypeScript tools, floating `bunx`/`npx` commands in standing gates, or simultaneous Biome/Prettier formatting.

## Example

In a Bun-based TypeScript repository, use its declared scripts, typically:

```bash
rtk bun run format:check
rtk bun run lint
rtk bun run typecheck
```

**Python anti-pattern when wrappers exist:**

```bash
black src
pytest
```

**Recommended pattern:**

```bash
rtk bash scripts/sync-env.bash
rtk bash scripts/flake.bash -a
rtk bash scripts/test.bash
```

## Stable-prefix import order

Maximize the stable prefix: place broadly shared dependencies and first-party relationships early, and narrow implementation details late. A reader should quickly see how the current module relates to the package before reaching one-use details. Group by the import's role in this module, not solely its distribution or stdlib origin.

For Python, use this order as the default:

1. First-party/local domain imports and established package utility facades that expose the module's relationship to the package.
2. Generic, broadly used third-party or standard APIs, such as SQLAlchemy for an RDB layer.
3. Specialized third-party or one-use standard integrations, such as a DuckDB-specific toolkit.
4. Minor incidental utilities, regardless of source, such as re used by one string operation or typing support.

An established facade can re-export minor utilities; reuse the facade rather than splitting it just to satisfy category labels. Popularity is a hint for stability, not a package ranking rule. Classify the actual dependency role. Alphabetize within a stable group when doing so does not obscure the established grouping.

**Pattern:**

```python
from acme.entity import Entity
from acme.utils import pj

from sqlalchemy import inspect, select

import duckdb

import re
from typing import Protocol
```

These are illustrative imports for a module using those operations, not dependencies to add. **Anti-pattern:** moving re/typing above the domain imports solely because they are stdlib, or interleaving every specialized driver with shared domain dependencies.

For TypeScript, apply the stable-prefix intent within the repository's import controls. Preserve `import type`, `node:` specifiers, explicit package exports, optional/lazy loading, and side-effect ordering. An optional provider must stay lazy even if it is locally owned. Do not move an import to the top merely to improve visual grouping when that changes evaluation or runtime behavior. Keep the selected formatter/import organizer aligned with these rules; explicit repository configuration remains authoritative.
