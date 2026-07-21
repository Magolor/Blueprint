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
docker build -t blueprint .
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

HeavenBase is declared as a normal runtime dependency and resolves from PyPI through `requirements.txt`. For local HeavenBase development, use `scripts/sync-env.bash --heavenbase-source` to install an editable source override from `HEAVENBASE_SOURCE`, `../HeavenBase/HeavenBase`, or `HEAVENBASE_REPO_URL`.

<!-- blueprint-template-only:start -->
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
<!-- blueprint-template-only:end -->

## Layout

| Path | Purpose |
|------|---------|
| `src/blueprint/` | Importable Python package and default SDK surface. |
| `src/blueprint/version.py` | Single source of truth for package version. |
| `src/blueprint/resources/` | Package resource files. |
| `src/blueprint/utils/` | Shared utility code. |
| `docs/README.md` | Project docs menu and authority map. |
| `docs/goals/` | Long-, mid-, and short-term project goals. |
| `docs/plans/` | Multi-slice plans with checklist progress and verification gates. |
| `docs/resources/` | Stable project references and background. |
| `docs/reports/` | Durable review, refactor, and survey reports. |
| Task coordination | Template mode keeps `docs/tasks.template.yaml` empty; operational mode uses the promoted `docs/tasks.yaml` as its single writable queue. |
| `docs/DEVLOG.md` | One rolling development and handoff log. |
| `docs/scratch/` | Expiring tracked notes; ignored local slop stays under `.temp/notes/`. |
| `Dockerfile` | Runtime container adapter built from `requirements.txt`. |
| `.dockerignore` | Docker build-context exclusions. |
| `tests/` | Behavioral, documentation-contract, and repository-infrastructure tests. |
| `demos/` | Maintained usage examples and demo fixtures. |
| `demos/assets/` | Committed demo fixtures. |
| `demos/.temp/` | Ignored demo runtime data. |
| `.agents/skills/heaven-style/` | Repository-local Heaven-style agent guidance when the project carries a checked-in copy. |
| `.github/workflows/` | GitHub Actions CI. |
| `.githooks/` | Git hooks for README sync and local formatting gates. |
| `scripts/` | Copyable uv-backed repo wrappers. |

## Environment Policy

Edit `requirements.txt` and `requirements-dev.txt` first. `pyproject.toml` reads them through setuptools dynamic metadata; `bash scripts/sync-env.bash` refreshes `uv.lock`, `poetry.lock`, and `environment-dev.yml`, then validates the Docker adapter.

Use this install priority order:

1. **uv** - `uv.lock` + `uv sync --all-extras` after `bash scripts/sync-env.bash` (default sync installs runtime and all optional extras).
2. **pip** - `pip install -r requirements.txt` and `pip install -e ".[dev]"`, or `pip install -r requirements-dev.txt` when a project documents that path.
3. **pyproject** - `pip install -e ".[dev]"` when only package metadata is available.
4. **conda** - generated `environment-dev.yml` with `-e ".[dev]"` only.
5. **poetry** - optional; `poetry install` after `poetry.lock` is refreshed by `bash scripts/sync-env.bash`.
6. **Docker** - `Dockerfile` installs `requirements.txt` first, then installs the project with dependency resolution disabled.

CI should use `bash scripts/sync-env.bash --check --no-heavenbase` as the generated-file drift gate.

After synchronizing the declared environment, run `bash scripts/check.bash fast` for the offline deterministic code/docs contract inventory; CI runs `scripts/sync-env.bash --check --no-heavenbase` separately for lock and adapter drift.

<!-- blueprint-template-only:start -->
Blueprint maintainers must also reconcile every template-facing change with HeavenBase: exact paths are copied, adapted paths are reviewed, and the consumer records the reviewed Blueprint commit and content digest in `.blueprint-sync.yaml`. Configure the canonical checkout with `git config core.hooksPath .githooks` so pre-push enforces that boundary. The globally installed `heaven-style` skill is deliberately excluded from repository sync.
<!-- blueprint-template-only:end -->

Build and smoke-test the runtime image with:

```bash
docker build -t blueprint .
docker run --rm blueprint --version
```

The Dockerfile is an adapter around the same requirements source, not a separate dependency declaration.

<!-- blueprint-template-only:start -->
See `BLUEPRINT.md` for the template-level dependency-model rationale.
<!-- blueprint-template-only:end -->

`scripts/sync-env.bash --heavenbase-source` is a temporary source override for local HeavenBase development. It can fail when the sibling checkout is missing, GitHub or the configured remote is private, SSH/HTTPS credentials are unavailable, a proxy/VPN blocks Git, or the remote branch cannot fast-forward. Normal installs should rely on the PyPI dependency instead.

Bash wrappers source `scripts/_env.bash` for shared executable lookup. `uv` is preferred before `uv.exe`; Python commands should go through the helper ladder: active virtualenv, repo `.venv`, `uv run python` or `uv.exe run python`, then system Python as the last fallback. Git hooks set `BLUEPRINT_PYTHON_PREFERENCE=uv-first` (or `REPO_PYTHON_PREFERENCE=uv-first`) so hook-time Python work prefers `uv run python` or `uv.exe run python`.

`README.en.md` can be copied to package resources when a downstream project needs it:

```bash
bash scripts/sync-readme.bash --resource-target blueprint
bash scripts/sync-env.bash --check --readme-resource-target blueprint
```

## Agent Setup

<!-- blueprint-template-only:start -->
`AGENTS.md` is a scaffold for new projects. After copying Blueprint, rewrite it for the real project: point agents to the project docs map, replace package paths and commands, record issue-tracker behavior, and delete template-only guidance.
<!-- blueprint-template-only:end -->

Repo-local skills live under `.agents/skills`; `.gitignore` explicitly keeps `.agents/` trackable.

When this repository carries `heaven-style`, its checked-in source installs globally at `~/.agents/skills/heaven-style`:

```bash
uv run python .agents/skills/heaven-style/scripts/install.py
```

For local cross-harness support, install the common Agent Skill plus the Claude Code plugin bridge:

```bash
uv run python .agents/skills/heaven-style/scripts/install.py --all-harnesses
```

Do not copy the skill into `.codex/skills`, `.github/skills`, `.cursor/`, `.opencode/`, `.kilo/skills`, or `~/.claude/skills/heaven-style`. Claude Code support is provided by the generated local plugin so Cursor, OpenCode, and Kilo do not discover duplicate plain skills from Claude-compatible folders.

## Release Policy

Until a downstream project deliberately replaces this policy, the scaffold publishes immutable repository snapshots through GitHub Releases only and never claims a same-named PyPI project. A release is an annotated `v<version>` tag at the published `master` head; `.github/workflows/release.yml` independently verifies the tag policy, runs the full supported-Python source gates, builds and tests the wheel and source distribution, and attaches both artifacts without replacing existing assets.

Release from a clean `master` branch:

```bash
bash scripts/release.bash
```

The script rejects development versions, dirty or non-`master` worktrees, divergent history, lightweight tags, and tag/version conflicts. It publishes `master` when it is strictly ahead, then creates or reuses the annotated tag and pushes it. Re-running it for an already published tag is safe. Before publishing anywhere beyond GitHub Releases, maintainers must establish package-name ownership and an explicit publication policy.

## Documentation Policy

The repository uses four explicit surfaces: the canonical English README for users; `docs/README.md` and its linked durable material for engineers, agents, and architects; `docs/DEVLOG.md` for concise change and handoff evidence; and `docs/scratch/` or ignored `.temp/notes/` for expiring ideas.

<!-- blueprint-template-only:start -->
While `.blueprint-template.yaml` exists, the checkout has no live task queue and `docs/tasks.template.yaml` stays empty. Template agents keep maintenance attached to the direct request or one declared external issue; `scripts/rename.bash` removes template mode and promotes the starter.
<!-- blueprint-template-only:end -->

Operational repositories use `docs/tasks.yaml` as their single writable queue and read it with `rtk uv run python scripts/docs.py tasks --ready`. Run `rtk uv run python scripts/docs.py check` before closeout. Completed operational work leaves the live queue after acceptance evidence is recorded; stable conclusions move into user docs, resources, tests, or code, and temporary notes are promoted or deleted.

English doc sync updates canonical English docs and generated docs through `.agents/skills/heaven-style/references/tasks/doc-sync.md`. Chinese or other translations should be refreshed separately through `.agents/skills/heaven-style/references/tasks/doc-trans.md` after English changes are complete.
