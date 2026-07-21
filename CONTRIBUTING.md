# Contributing

Use this guide for repository contributions and replace any remaining scaffold-specific detail with concrete project policy.

<!-- blueprint-template-only:start -->
## After Initializing From Blueprint

1. Replace this title with `Contributing to <Project>`.
2. Point contributors to `docs/README.md` and the project issue tracker.
3. Let `scripts/rename.bash` instantiate `docs/tasks.yaml` from the inert starter, keep it as the concrete project's single active queue, and record the default branch, PR title conventions, and required checks (`python scripts/docs.py check`, `bash scripts/flake.bash --ci`, `bash scripts/test.bash`, and so on).
4. Describe how to run `bash scripts/rename.bash` if the repo is still being turned into a downstream project.
5. Remove template-only notes that do not apply to the real project.
<!-- blueprint-template-only:end -->

<!-- blueprint-template-only:start -->
## Blueprint Maintainer Notes

While Blueprint remains the upstream template:

- Use the standard issue templates (`Bug Report`, `Feature Request`, `Documentation`, `Question`) like any downstream project should.
- Keep changes focused; match existing script and docs conventions.
- Do not create a live `docs/tasks.yaml` in Blueprint. Keep maintenance attached to the direct request or an explicitly selected external issue, and close it with concise evidence in `docs/DEVLOG.md` rather than creating task lists in plans, reports, or chat.
- Run `bash scripts/check.bash fast` before opening a pull request and `bash scripts/check.bash full` when the risk warrants the complete suite.
- Classify every new Blueprint path in `.blueprint-template.yaml`. For template-facing changes, review the adapted result in HeavenBase, sync exact files, and refresh HeavenBase's `.blueprint-sync.yaml` before merging Blueprint.
- Do not commit secrets, local `.venv` paths, or machine-specific overrides.
<!-- blueprint-template-only:end -->

## Pull Requests

Use the pull request template in `.github/pull_request_template.md`.

<!-- blueprint-template-only:start -->
For template work, describe whether the change affects downstream projects created with **Use this template** or only Blueprint maintenance.
<!-- blueprint-template-only:end -->
