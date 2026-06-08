# Contributing Scaffold

This file is a placeholder for projects created from Blueprint. Replace it with real contribution guidance for your repository.

## After Initializing From Blueprint

1. Replace this title with `Contributing to <Project>`.
2. Point contributors to `docs/README.md` and the project issue tracker.
3. Record the default branch, PR title conventions, and required checks (`bash scripts/flake.bash --ci`, `bash scripts/test.bash`, and so on).
4. Describe how to run `bash scripts/rename.bash` if the repo is still being turned into a downstream project.
5. Remove template-only notes that do not apply to the real project.

## Blueprint Maintainer Notes

While Blueprint remains the upstream template:

- Use the standard issue templates (`Bug Report`, `Feature Request`, `Documentation`, `Question`) like any downstream project should.
- Keep changes focused; match existing script and docs conventions.
- Run `bash scripts/sync-env.bash --check`, `bash scripts/flake.bash --ci`, and `bash scripts/test.bash` before opening a pull request.
- Do not commit secrets, local `.venv` paths, or machine-specific overrides.

## Pull Requests

Use the pull request template in `.github/pull_request_template.md`.

For template work, describe whether the change affects downstream projects created with **Use this template** or only Blueprint maintenance.
