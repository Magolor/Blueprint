---
name: asset-setup
description: Read when locating provisioning, profiles, or maintenance commands.
---

# Personal Machine Setup Owner

## Summary

The selected setup repository owns provisioning, profiles, and maintenance. Its personal locator is not a universal dependency.

## Setup owner

The user-selected setup checkout is `~/Developer/Setup`. This is a personal
locator, not a required path or provisioning dependency for other users.
The upstream repository is [Magolor/Setup](https://github.com/Magolor/Setup).

Read the actual checkout before using its commands. The following paths are
relative to that checkout:

| Need | Owner |
| --- | --- |
| Repository policy and documentation routing | `AGENTS.md`, `README.md`, `docs/README.md` |
| New machine, prerequisite checks, profile binding, stage order, recovery | `docs/setup.md`, `Setup.bash` |
| Machine scope and desired hardware/application/database settings | `profiles/<machine>.yaml` |
| Configuration, credential namespaces, proxy and remote-access identity | `docs/reference/configuration.md` |
| Host upkeep and package constraints | `docs/maintenance.md`, `scripts/routine-update.bash`, `assets/packages/` |
| Shell behavior | `assets/shell/`, applied by `scripts/2-00-shell.bash` |
| Container lifecycle, selectors, and database bootstrap | `assets/docker/control.bash`, `assets/docker/databases/README.md` |
| Model paths and real operation checks | `docs/guides/models.md` |
| Code validation and provisioned-machine validation | `scripts/check.bash`, `scripts/checks/run.bash` |

Setup owns Homebrew applications, Miniforge `main`/`dev`, project uv environments,
Bun local tools, mise Node, Corepack's global pnpm fallback, rustup, and container
configuration. Repository metadata still controls project commands. Setup's
Bun-first local-tool preference and Heaven Style's Bun/pnpm greenfield criteria
apply at different scopes.

If the checkout or required facts are missing, follow
[the recovery procedure](../MacOS-env.md#recover-missing-environment-information).
Do not assume the current machine matches the source snapshot. Bind only its own
profile and credential namespace when provisioning is authorized. Restore secrets
through Setup's documented secure procedure; never copy values into this skill.
