# Blueprint Maintainer Contract

This page owns decisions for the upstream template. Downstream projects must replace template-specific policy.

## Product lines

Blueprint has two long-lived branches:

- `typescript` is the active TypeScript starter and hosted default.
- `python` is the maintained Python compatibility starter.

Each branch contains one clean root snapshot. Product files can differ. The embedded Heaven Style tree must remain byte-identical across both branches.

## TypeScript package boundary

The TypeScript line contains one native ESM package. It exposes one SDK boundary and one `bp` CLI adapter.

A workspace would add coordination and release cost. Add one only after a real consumer, runtime, or release boundary appears.

`package.json` owns direct tool versions and commands. `pnpm-lock.yaml` owns resolved dependency state. Node 24 is the runtime baseline.

External configuration enters as `unknown`. One boundary validates and detaches the complete value. A stateless SDK function returns frozen project information. The CLI owns only argument and output adaptation.

## Version identity

Blueprint uses `MAJOR.MINOR.PATCH.N[devK]`. npm does not accept four numeric SemVer components.

Blueprint `0.1.2.3` therefore maps to npm package version `0.1.2-3`. The SDK and CLI still report `0.1.2.3`.

## Artifact contract

`pnpm package:check` performs these actions:

1. Build JavaScript and declarations.
2. Run `publint`.
3. Pack the exact npm artifact.
4. Install the artifact in a disposable consumer.
5. Import the public SDK.
6. Invoke the installed CLI.

Source-only success is not release evidence.

The Dockerfile uses the frozen lock and runs the built CLI. It is an adapter, not a dependency authority.

## Harness support

`AGENTS.md` and `.agents/skills/` are the canonical agent surfaces. The global Heaven Style install uses `~/.agents/skills/heaven-style`.

Claude Code uses the generated plugin bridge. Do not create another plain skill copy.

## External actions

A local commit is not publication. In this repository, publication means a push, package registry release, deployment, or other external state change.

The owning branch dispatches its release workflow. Blueprint does not use a third release branch.
