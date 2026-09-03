# Blueprint

Blueprint is a strict Python starter for a small SDK and command-line package. It uses one distribution and one public import facade.

The Python compatibility line reports Blueprint version `0.1.2.3`.

## Start

Requirements:

- Python 3.10 through 3.14.
- uv for the repository workflow.

```bash
uv sync --all-extras --frozen
bash scripts/check.bash full
uv run bp --help
```

Use the SDK:

```python
from blueprint import CliConfig, ProjectConfig, ProjectIdentity, get_project_info

info = get_project_info(
    ProjectConfig(
        project=ProjectIdentity(name="My Project"),
        cli=CliConfig(output="text"),
    ),
)

print(info)
```

Configuration uses immutable dataclasses. `load_config()` reads `BLUEPRINT_PROJECT_NAME` and `BLUEPRINT_OUTPUT` when an application needs environment input.

## Architecture

| Path | Responsibility |
| --- | --- |
| `src/blueprint/__init__.py` | Public SDK facade. |
| `src/blueprint/project.py` | Stateless project information. |
| `src/blueprint/config.py` | Configuration validation and immutable values. |
| `src/blueprint/cli.py` | Closed CLI grammar and SDK adaptation. |
| `tests/` | Behavior and contract tests. |
| `scripts/` | Environment, documentation, package, release, and sync tools. |
| `docs/` | Engineering guidance and task state. |
| `.agents/skills/heaven-style/` | Canonical Heaven Style source. |

Blueprint remains one distribution. Add a package split only after a real consumer or release boundary appears.

## Start a downstream project

Create a repository from the template, then run:

```bash
bash scripts/rename.bash \
  --project-name "My Project" \
  --dist-name my-project \
  --import-name my_project \
  --cli-name my-tool \
  --yes
```

The script changes product identifiers. It does not edit Heaven Style. Review `AGENTS.md` and `BLUEPRINT.md`, then run `uv lock` and the complete gate.

## Dependencies

`pyproject.toml` owns direct declarations. `uv.lock` owns the resolved development and release environment.

Blueprint has no third-party runtime dependency.

## Commands

```bash
uv run python scripts/docs.py tasks --ready
uv lock --check
bash scripts/check.bash fast
bash scripts/check.bash full
uv build
```

## Product branches

- `typescript` is the active product line and hosted default.
- `python` is the Python compatibility line.
- The Heaven Style tree must be byte-identical on both branches.
- The remote contains no other long-lived product branch.

Run `bash scripts/check-skill-sync.bash` to compare committed skill trees. Use `HEAVEN_STYLE_BRANCHES` to replace the default branch set.

## Heaven Style

Install the standard local copy with:

```bash
uv run python .agents/skills/heaven-style/scripts/install.py
```

Use `--all-harnesses` only when you need every supported local bridge. Do not create duplicate plain-skill copies.

## Documentation and release

Start engineering work at [`docs/README.md`](docs/README.md). `docs/tasks.yaml` is the only live task queue. `docs/DEVLOG.md` records closeout evidence.

The owning product branch dispatches its release workflow. A local commit is not publication. A push or registry release is publication and needs explicit authority.

Blueprint uses the [MIT License](LICENSE).
