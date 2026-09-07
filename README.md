# Blueprint

Blueprint is a strict TypeScript starter for a small SDK and command-line package. It uses one pnpm package and one public module boundary.

Blueprint version `0.1.2.3` maps to npm version `0.1.2-3`. The SDK and `bp --version` report the Blueprint version.

## Start

Requirements:

- Node.js 24 or newer.
- The pnpm version in `package.json#packageManager`.

```bash
pnpm install --frozen-lockfile
pnpm check
pnpm exec bp --help
```

Use the SDK:

```ts
import { getProjectInfo } from "@magolor/blueprint";

const info = getProjectInfo({
  project: { name: "My Project" },
  cli: { output: "text" },
});

console.log(info);
```

The function validates, detaches, and freezes its result. `loadConfig()` reads `BLUEPRINT_PROJECT_NAME` and `BLUEPRINT_OUTPUT` when an application needs environment input.

## Architecture

| Path | Responsibility |
| --- | --- |
| `src/index.ts` | Public SDK exports. |
| `src/project.ts` | Stateless project information and version identity. |
| `src/config.ts` | Configuration validation and immutable snapshots. |
| `src/cli.ts` | Closed CLI grammar and SDK adaptation. |
| `tests/` | Behavior and contract tests. |
| `scripts/` | Documentation, package, release, and sync tools. |
| `docs/` | Engineering guidance and task state. |
| `.agents/skills/heaven-style/` | Canonical Heaven Style source. |

Blueprint remains one package. Add a workspace only after a real package, runtime, consumer, or release boundary appears.

## Start a downstream project

1. Create a repository from the template.
2. Change the package name, description, repository links, author, and CLI name in `package.json`.
3. Replace the placeholder project identity in `src/config.ts` and user examples.
4. Rewrite `AGENTS.md` and `BLUEPRINT.md` for the real project.
5. Keep the Heaven Style source unchanged unless you intend to update the shared skill.
6. Run `pnpm install`, `pnpm readme:sync`, and `pnpm check`.

Do not run a repository-wide replacement through `.agents/skills/heaven-style/`.

## Commands

```bash
pnpm tasks --ready
pnpm check:fast
pnpm check
pnpm build
pnpm package:check
pnpm readme:sync
```

`pnpm check` validates documentation, skill parity, format, lint, types, tests, package metadata, and the packed artifact.

Build the runtime container with:

```bash
pnpm container:check
```

## Product branches

- `typescript` is the active product line and hosted default.
- `python` is the Python compatibility line.
- The Heaven Style tree must be byte-identical on both branches.
- The remote contains no other long-lived product branch.

Run `bash scripts/check-skill-sync.bash` to compare committed skill trees. Use `HEAVEN_STYLE_BRANCHES` to replace the default branch set.

## Heaven Style

Blueprint owns the embedded Heaven Style skill. Install its standard local copy with:

```bash
python3 .agents/skills/heaven-style/scripts/install.py
```

Use `--all-harnesses` only when you need every supported local bridge. Do not create duplicate plain-skill copies.

## Documentation and release

Start engineering work at [`docs/README.md`](docs/README.md). `docs/tasks.yaml` is the only live task queue. `docs/DEVLOG.md` records closeout evidence.

The owning product branch dispatches its release workflow. A local commit is not publication. A push or registry release is publication and needs explicit authority.

Blueprint uses the [MIT License](LICENSE).
