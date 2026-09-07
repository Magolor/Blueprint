# macOS Environment Maintenance

Use the machine's setup repository as the owner of provisioning, tool versions,
package lists, shell configuration, and maintenance commands. The selected
personal setup is recorded in [instance/setup.md](instance/setup.md). That locator
does not make its choices universal Heaven Style rules.

Machine-maintainer agents may change the environment when the user asks them to
maintain, update, repair, or verify it. Setup-pipeline, documentation, and planning
agents should edit reproducible docs/scripts and hand commands to the user.

## Find the owner

1. Read the selected setup repository's `AGENTS.md` and documentation entry point.
2. Read its provisioning guide for new machines or intentional scope changes.
3. Read its maintenance guide for recurring updates.
4. Inspect the selected script, profile, manifest, and lockfile before execution.
5. Verify the actual machine and selected profile. A checked-in profile states
   desired configuration; it does not prove that configuration is installed.

The setup owner must supply these responsibilities. Use its current paths and
commands instead of maintaining a second command list here.

| Responsibility | Required owner or evidence |
| --- | --- |
| Host upkeep | Maintenance script for Homebrew update/upgrade/cleanup/doctor and inventory export; uv tool upgrades/cache cleanup; mise and Corepack; Conda environments and cleanup; rustup; Bun; Docker disk/image/volume inspection and authorized cleanup. |
| Package inventory | Desired package manifests and a separately reviewed observed inventory. An exported `Brewfile.current` does not automatically update the desired Brewfile. |
| Project dependencies | The project manager, scripts, and lockfile. Prefer targeted upgrades. Broad lockfile refreshes require intentional dependency-maintenance scope. |
| Stateful databases | Compose/controller definitions, image tags, data volumes, bootstrap/authentication behavior, and a backup plus recovery procedure. |
| Machine state | A named profile and reviewed observations. Unknown or stale observations remain explicitly unverified. |

## Recover missing environment information

1. Look for the setup locator in the repository policy or instance guidance.
2. If that checkout is absent, ask for its location or the intended setup owner.
   Do not clone or run a provisioning sequence merely because the skill names one.
3. If the machine does not use that setup, inspect only the facts the task needs:
   OS, architecture, memory, active shell, executable paths, repository runtime,
   lockfile, and relevant service endpoint or Docker context.
4. Run `rtk python3 scripts/machine.py --output <note-path>` from the skill root
   when a non-secret observation report will help. Use a known-good Python for
   this standalone script. Missing probes must remain unknown.
5. Record the actual owner and any difference from the expected setup. Do not
   assume Miniforge, mise, Docker Desktop, editor CLIs, or a named Conda environment
   exists because another machine uses it.
6. Continue work whose prerequisites are verified. If a required fact is missing,
   report the exact missing fact and the smallest check or user input that resolves it.
7. For an authorized setup change, follow the owner's new-machine procedure.
   Select or create the actual machine profile. Verify each selected stage before
   proceeding to dependent stages. Never reuse another machine's identity or credentials.

## Guardrails

- Never run `sudo pip install`.
- Never use `pip install` outside an active `.venv` or Conda environment.
- Never use Homebrew Python as a project interpreter.
- Preserve repository metadata. For greenfield JS/TS, Heaven Style treats Bun and
  pnpm as co-preferred: Bun for compact Bun-native work, pnpm for Node-first
  libraries, services, or workspaces. A selected machine setup may choose a
  narrower local-tool default; it does not override a project's declared manager.
- Rustup owns active Rust work in this setup pattern. Never install Rust through
  Homebrew for that work.
- Never put raw secrets in `~/.zshrc`, `~/.bashrc`, setup scripts, committed
  `.envrc` files, shell history, or instance notes.
- Never mount the full home directory into agent containers by default.
- Never run heavy Docker stacks, large Ollama models, and low-latency audio
  sessions together unless resources were intentionally allocated.
- Pin per project. Upgrade intentionally through the owning lockfile or Compose image tag.
- Keep Conda `base` limited to environment management. In the selected setup,
  `main` owns default interactive work and `dev` owns disposable scratch work.

## Stateful service changes

Do not update Dockerized databases during routine upkeep without a concrete fix,
compatibility change, security update, or image refresh requirement. Upgrades can
change data formats, indexes, bootstrap behavior, or authentication.

Inspect service status and recent logs before an authorized update. Pull and
recreate only the selected service through its owner. Inspect that service's
logs and run its operation check afterward. Preserve named volumes unless data
replacement is explicitly part of the operation.

For PostgreSQL major changes, do not replace `pgvector/pgvector:pg17`,
`pgvector/pgvector:pg18`, or a newer major tag on an existing volume without a
migration. Dump, recreate, and restore. The setup guide owns the exact commands.
