# Blueprint

Blueprint is a uv-first Python starter project for future repositories.

`README.en.md` is the canonical English README source. `README.md` is generated from it by `scripts/sync-readme.bash` and the Git pre-commit hook. Translated docs such as `README.zh.md` are maintained separately through the repo-local doc translation workflow.

## Quick Start

```bash
bash scripts/sync-env.bash
bash scripts/sync-env.bash --check
bash scripts/flake.bash --ci
bash scripts/test.bash
uv build
```

## CLI

```bash
uv run bp --help
uv run bp --version
uv run bp setup
uv run bp init
uv run bp config list
uv run bp cfg get blueprint.project.name
uv run bp pj demos .temp --abs
uv run blueprint-gui --help
```

The CLI uses HeavenBase utility classes for project configuration and path resolution.

HeavenBase is declared as a normal runtime dependency and resolves from PyPI (`heavenbase==0.1.0.5`). For local HeavenBase development, use `scripts/sync-env.bash --heavenbase-source` to install an editable source override from `HEAVENBASE_SOURCE`, `../HeavenBase/HeavenBase`, or `HEAVENBASE_REPO_URL`.

## Rename the Template

Use `scripts/rename.bash` to turn Blueprint into a project with independent display, distribution, import, and CLI names:

```bash
bash scripts/rename.bash \
  --project-name "My Project" \
  --dist-name my-project \
  --import-name my_project \
  --cli-name my-tool \
  --yes
bash scripts/sync-env.bash
```

## Layout

| Path | Purpose |
|------|---------|
| `src/blueprint/` | Importable Python package and default SDK surface. |
| `src/blueprint/version.py` | Single source of truth for package version. |
| `src/blueprint/resources/` | Package resource files. |
| `src/blueprint/utils/` | Shared utility code. |
| `docs/README.md` | Project docs menu and authority map. |
| `docs/goals/` | Long-, mid-, and short-term project goals. |
| `docs/resources/` | Stable project references and background. |
| `docs/progress/` | Daily progress folders with summaries and optional notes. |
| `tests/` | Empty test root for future project-specific tests. |
| `demos/` | Empty demo root for future project-specific demos. |
| `demos/assets/` | Committed demo fixtures. |
| `demos/.temp/` | Ignored demo runtime data. |
| `.agents/skills/heaven-style/` | Repo-local Heaven-style agent skill copied from HeavenBase. |
| `.github/workflows/` | GitHub Actions CI. |
| `.githooks/` | Git hooks for README sync and local formatting gates. |
| `scripts/` | Copyable uv-backed repo wrappers. |

## Environment Policy

Edit `requirements.txt` and `requirements-dev.txt` first. `pyproject.toml` reads them through setuptools dynamic metadata; `bash scripts/sync-env.bash` refreshes `uv.lock`, `poetry.lock`, and `environment-dev.yml`.

Use this install priority order:

1. **uv** - `uv.lock` + `uv sync --all-extras` after `bash scripts/sync-env.bash` (default sync installs runtime and all optional extras).
2. **pip** - `pip install -r requirements.txt` and `pip install -e ".[dev]"`, or `pip install -r requirements-dev.txt` when a project documents that path.
3. **pyproject** - `pip install -e ".[dev]"` when only package metadata is available.
4. **conda** - generated `environment-dev.yml` with `-e ".[dev]"` only.
5. **poetry** - optional; `poetry install` after `poetry.lock` is refreshed by `bash scripts/sync-env.bash`.

CI should use `bash scripts/sync-env.bash --check --no-heavenbase` as the generated-file drift gate.

`scripts/sync-env.bash --heavenbase-source` is a temporary source override for local HeavenBase development. It can fail when the sibling checkout is missing, GitHub or the configured remote is private, SSH/HTTPS credentials are unavailable, a proxy/VPN blocks Git, or the remote branch cannot fast-forward. Normal template users should rely on the PyPI dependency instead.

Bash wrappers source `scripts/_env.bash` for shared executable lookup. `uv` is preferred before `uv.exe`; Python commands should go through the helper ladder: active virtualenv, repo `.venv`, `uv run python` or `uv.exe run python`, then system Python as the last fallback. Git hooks set `BLUEPRINT_PYTHON_PREFERENCE=uv-first` (or `REPO_PYTHON_PREFERENCE=uv-first`) so hook-time Python work prefers `uv run python` or `uv.exe run python`.

`README.en.md` can be copied to package resources when a downstream project needs it:

```bash
bash scripts/sync-readme.bash --resource-target heavenbase
bash scripts/sync-env.bash --check --readme-resource-target heavenbase
```

## Agent Setup

`AGENTS.md` is a scaffold for new projects. After copying Blueprint, rewrite it for the real project: point agents to the project docs map, replace package paths and commands, record issue-tracker behavior, and delete template-only guidance.

Repo-local skills live under `.agents/skills`; `.gitignore` explicitly keeps `.agents/` trackable.

## Release Policy

Blueprint includes a PyPI trusted-publishing workflow at `.github/workflows/release.yml`. It only runs on pushes to the `release` branch when the head commit message contains `[release]`.

Before the first downstream release, configure PyPI trusted publishing for the GitHub repository, workflow `release.yml`, and environment `pypi`, then create a matching GitHub environment named `pypi`.

Release from a clean `master` branch:

```bash
bash scripts/release.bash
```

The script creates or reuses a `[release]` commit on `master`, pushes `master`, fast-forwards `release` from `master`, and pushes `release` to trigger the publish workflow.

## Documentation Policy

English doc sync updates canonical English docs and generated docs through `.agents/skills/heaven-style/references/tasks/doc-sync.md`. Chinese or other translations should be refreshed separately through `.agents/skills/heaven-style/references/tasks/doc-trans.md` after English changes are complete.
