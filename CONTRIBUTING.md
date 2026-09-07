# Contributing to Blueprint

Read [`docs/README.md`](docs/README.md), then inspect ready work:

```bash
uv run python scripts/docs.py tasks --ready
```

Change dependencies in `pyproject.toml`. Run `uv lock` after each change.

Run these gates before a pull request:

```bash
uv lock --check
bash scripts/check.bash full
uv build
```

Keep the existing package boundary until a concrete consumer or release need justifies another distribution. Keep `blueprint.cli` as an adapter.

Keep imports inert. Validate external data at one boundary. Use complete type hints and semantic docstrings on public APIs.

The maintained branches are `typescript` and `python`. Apply each Heaven Style edit byte-for-byte to both branches. Confirm parity with `bash scripts/check-skill-sync.bash`.

Do not commit secrets, virtual environments, generated build output, or machine-specific configuration.

Use the pull request template. State whether the change affects downstream repositories.
