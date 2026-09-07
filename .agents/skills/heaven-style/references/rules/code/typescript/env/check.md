---
id: ts-env-check
title: TypeScript dependency and artifact checks
description: Read for TypeScript dependency and artifact checks.
blocking: true
---

# TypeScript dependency and artifact checks

## Package boundaries and artifacts

- A package boundary is earned by independent consumption, runtime/dependency isolation, compatibility/release ownership, or extraction—not by a noun in an architecture diagram.
- Keep source-plane and artifact-plane checks distinct. Workspace aliases can prove source behavior while hiding broken exports, specifiers, declarations, optional peers, or packed files.
- Published packages need explicit `exports`, correct dependency classes, a controlled packed file set, and a clean tarball consumer smoke.
- Apps may bundle for distribution. Libraries should prefer transparent output until bundling solves a real consumer or artifact need.

## Dependency discipline

- Prefer platform capabilities and small maintained packages over dependency chains for trivial wrappers; do not reimplement security-sensitive protocols, parsers, or cryptography casually.
- Classify runtime, peer, optional, and development dependencies from the consumer contract.
- Review ownership, maintenance, license, transitive weight, install scripts, native support, and existing platform overlap before adding a dependency.
- Use the selected manager's allow/trust controls for lifecycle scripts. Default trust lists or package popularity do not replace project review.
- Keep credentials out of source, metadata, command history, and logs. Resolve required environment configuration at one application boundary.

## Verification ladder

Use repository script names when they differ.

For Bun:

```bash
rtk bun ci
rtk bun run check
```

For pnpm:

```bash
rtk pnpm install --frozen-lockfile
rtk pnpm run check
```

During iteration, run only the affected formatter, lint, typecheck, test, build, package, or consumer gate. Finish with the repository aggregate when risk warrants it.

- Run build only when the repository produces an artifact.
- For published packages, pack and install the archive in a clean consumer.
- Test every advertised runtime and environment boundary.
- Keep essential flags in repository scripts so local and CI entry points do not drift.
