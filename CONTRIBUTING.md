# Contributing to Blueprint

Read [`docs/README.md`](docs/README.md), then inspect ready work:

```bash
pnpm tasks --ready
```

Use the Node and pnpm versions declared by the repository. Change dependencies through pnpm. Commit `package.json` and `pnpm-lock.yaml` together.

Run this gate before a pull request:

```bash
pnpm check
```

Keep the existing package boundary until a concrete runtime, consumer, or release need justifies another package. Put public SDK behavior behind `src/index.ts`. Keep `src/cli.ts` as an adapter.

Validate external data at its boundary. Preserve strict internal types and owned immutable values.

The maintained branches are `typescript` and `python`. Apply each Heaven Style edit byte-for-byte to both branches. Confirm parity with `pnpm skill:check`.

Do not commit secrets, dependencies, build output, or machine-specific configuration.

Use the pull request template. State whether the change affects downstream repositories.
