---
name: blueprint
description: Read to create a project from the Python Blueprint template.
---

# Blueprint

English | [简体中文](README.zh.md)

## Summary

Blueprint is a strict Python starter with one SDK, a thin CLI, and Heaven Style agent guidance. This branch contains the current `0.2.0-alpha.1` template.

[![CI](https://github.com/Magolor/Blueprint/actions/workflows/code-quality.yml/badge.svg?branch=python)](https://github.com/Magolor/Blueprint/actions/workflows/code-quality.yml) [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Alpha](https://img.shields.io/badge/version-0.2.0--alpha.1-orange.svg)](CHANGELOG.md)

## Start

For this upstream checkout, fetch both product branches before running the full gate. For a new template repository or extracted archive, complete “Create your project” first, including the upstream-only parity setting.

Use Python 3.10 through 3.14 and uv.

```bash
uv sync --all-extras --frozen
bash scripts/check.bash full
uv run bp --help
```

Use the public SDK from the built or installed package:

```python
from blueprint import get_project_info

print(get_project_info())
```

The result contains the project name, version, and output format. Configuration is validated and immutable. `BLUEPRINT_PROJECT_NAME` and `BLUEPRINT_OUTPUT` configure CLI output; the supported formats are `text` and `json`.

## Create your project

1. Create a repository from the template and choose the required product branch.
2. Replace package, import, CLI, author, and repository identities in the manifest, source, tests, and root documents.
3. Replace upstream policy in `AGENTS.md` and `BLUEPRINT.md`; update citation, contact details, badges, and release ownership.
4. Keep Heaven Style unchanged during product renaming. Remove the two-branch parity gate if your project does not maintain that shared-tree contract.
5. Refresh the lockfile and generated README, then run the full check command above.

## Folder ownership

| Path | Purpose |
| --- | --- |
| `src/` | One native SDK and CLI package. |
| `tests/` | Public behavior, failure paths, and tooling contracts. |
| `scripts/` | Repository checks, generation, and release preparation. |
| `docs/` | Engineering guidance, one task queue, and development evidence. |
| `.agents/skills/heaven-style/` | Canonical shared agent guidance. |

Add folders or packages only for real responsibilities. Empty template directories do not require an application framework, database, GUI, or service.

## Heaven Style

Install or replace the standard local skill with the following command. The TypeScript template uses uv only for this standalone Python helper.

```bash
uv run python .agents/skills/heaven-style/scripts/install.py
```

The default destination is `~/.agents/skills/heaven-style`. Use `--all-harnesses` when the Claude plugin bridge is needed.

## Releases and project information

`typescript` is the hosted default; `python` is the Python starter. Their Heaven Style trees are identical. Python packages use the equivalent version `0.2.0a1`.

Use [release preparation](docs/resources/release.md) for verified template archives. Preparing an archive does not publish a package or GitHub release.

See [Contributing](CONTRIBUTING.md), [Support](SUPPORT.md), [Security](SECURITY.md), [Code of conduct](CODE_OF_CONDUCT.md), [Changelog](CHANGELOG.md), and [Acknowledgements](ACKNOWLEDGEMENTS.md). Citation metadata is in [CITATION.cff](CITATION.cff); the project uses the [MIT License](LICENSE).

The [engineering guide](docs/README.md) owns the documentation map. `docs/tasks.yaml` is the only live queue.
