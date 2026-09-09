# Blueprint Maintainer Contract

This page owns decisions for the upstream Python template. Downstream projects must replace template-specific policy.

## Product lines

Blueprint has two long-lived branches:

- `typescript` is the active TypeScript starter and hosted default.
- `python` is the maintained Python starter.

Each release branch preserves its existing remote root and adds one consolidated commit for the current alpha. Product files can differ. The embedded Heaven Style tree must remain byte-identical across both branches.

## Python package boundary

The Python line contains one package. It exposes one SDK facade and one `bp` CLI adapter.

The package has no third-party runtime dependency. Importing it performs no I/O and changes no external state.

`pyproject.toml` owns direct dependency declarations and package metadata. `uv.lock` owns the resolved development and release environment.

External configuration enters as an object or environment mapping. One boundary validates it and creates immutable dataclass values. A stateless SDK function returns project information. The CLI owns only argument and output adaptation.

## Version identity

Blueprint and Heaven Style are frozen at **0.2.0 alpha 1**. npm, the TypeScript SDK/CLI, and skill metadata use `0.2.0-alpha.1`; the Python package and SDK/CLI use the equivalent PEP 440 spelling `0.2.0a1`.

Keep these versions unchanged during maintenance. Resume version advancement only after HeavenBase 2 publishes a release strictly newer than this alpha, or the user explicitly changes this policy. A local version edit, planned release, or unrelated repository tag does not lift the freeze. Before advancing, record the qualifying HeavenBase 2 release URL and version here and update the policy explicitly. This condition does not authorize publication or ongoing monitoring.

## Artifact contract

The release gate performs these actions:

1. Check the frozen uv environment.
2. Validate documentation and the skill graph.
3. Run format, lint, and behavior tests.
4. Build the source distribution and wheel.
5. Inspect package metadata and import the public SDK.

Source-only success is not release evidence.

## Harness support

`AGENTS.md` and `.agents/skills/` are the canonical agent surfaces. The global Heaven Style install uses `~/.agents/skills/heaven-style`.

Claude Code uses the generated plugin bridge. Do not create another plain skill copy.

## External actions

A local commit is not publication. In this repository, publication means a push, package registry release, deployment, or other external state change.

The owning branch dispatches its verification workflow. Template archives are prepared locally or uploaded as workflow artifacts. A GitHub prerelease is published separately after both branches pass verification. See [release preparation](docs/resources/release.md).
