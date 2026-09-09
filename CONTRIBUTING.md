---
name: blueprint-contributing
description: Read before changing Blueprint code or documentation.
---

# Contributing

English | [简体中文](CONTRIBUTING.zh.md)

## Summary

Start with [repository policy](AGENTS.md) and the [engineering guide](docs/README.md). Keep one outcome per change and inspect the canonical task queue before starting resumable work.

## Check the change

Use the declared runtime and package manager. Run focused checks during implementation and the full gate before review.

```bash
uv sync --all-extras --frozen
bash scripts/check.bash full
```

Keep one native package and one public SDK entry. Validate external input, preserve meaningful failure coverage, and migrate owned callers when interfaces change. Do not add compatibility aliases for retired alpha interfaces.

## Documentation and shared skill

English pages are canonical. Keep `.zh.md` counterparts aligned in meaning, line structure, and code. `README.md` is generated from `README.en.md`.

Edit Heaven Style only in Blueprint and synchronize its exact tree to both product branches. Local commit hooks check the candidate; full gates additionally check committed branch parity.

Use the pull-request template and state the behavior, verification, and material limitations. Contributions use the [MIT License](LICENSE).
