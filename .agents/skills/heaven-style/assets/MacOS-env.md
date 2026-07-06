# macOS Environment Maintenance

Shared macOS maintenance playbook for Heaven-style agents working with this setup pattern. These operations are OS-wide guidance, not Magolor-M5-specific facts. Keep host identity, hardware details, serial numbers, UUIDs, private paths, and live state in `assets/instance/` only when they are safe to record at all.

Machine-maintainer agents may run these commands when the user asks them to maintain, update, repair, or verify the macOS environment. Setup-pipeline, docs, and planning agents should update docs/scripts and hand commands to the user instead of changing the machine.

## Monthly host routine

Run from a normal terminal when intentionally refreshing machine-level tools:

```zsh
brew update
brew upgrade
brew cleanup
brew doctor
brew bundle dump --force --file ~/Developer/Setup/assets/Brewfile.current

uv tool upgrade --all
uv cache prune

mise upgrade
corepack enable

mamba update -n main --all
mamba update -n dev --all
conda clean --all

rustup update

bun upgrade

docker system df
docker image prune
docker volume ls
```

Review `~/Developer/Setup/assets/Brewfile.current` before using it to update `~/Developer/Setup/assets/Brewfile`. The current file is an inventory artifact, not automatic authority.

## Project dependency routine

Run dependency updates inside the repo that owns the lockfile:

```zsh
cd <repo>

uv sync
uv lock --upgrade-package <package-name>

bun update

cargo update -p <crate-name>
```

Prefer targeted updates. Broad lockfile refreshes are acceptable only during intentional dependency-maintenance work.

## Docker database updates

Do not update Dockerized databases as part of the monthly routine unless there is a concrete fix, compatibility change, security update, or image refresh requirement. Stateful service upgrades can change data formats, indexes, bootstrap behavior, or authentication.

When an update is needed:

```zsh
cd ~/Developer/Containers/compose/databases
docker compose ps
docker compose logs --tail=100
docker compose pull <service-name>
docker compose up -d <service-name>
docker compose logs --tail=100 <service-name>
```

For Postgres major versions, do not blindly change `pgvector/pgvector:pg17`, `pgvector/pgvector:pg18`, or a newer major tag on an existing volume. Dump, recreate, and restore.

## Local guardrails

1. Never `sudo pip install`.
2. Never use `pip install` outside an active `.venv` or Conda environment.
3. Never use Homebrew Python as a project interpreter.
4. Prefer Bun for JS/TS unless repo metadata requires Corepack-pinned pnpm/yarn/npm or Node/npm compatibility.
5. Never install Rust through Homebrew for active Rust work; rustup owns Rust.
6. Never put raw secrets in `~/.zshrc`, `~/.bashrc`, setup scripts, committed `.envrc` files, or shell history.
7. Never mount the full home directory into agent containers by default.
8. Never run heavy Docker stacks, Ollama large models, and low-latency audio sessions at the same time unless resources were intentionally allocated.
9. Pin per project and upgrade intentionally with the owning lockfile or compose image tag.
10. Keep Conda `base` boring; use `main` for default interactive work and `dev` for disposable scratch work.
