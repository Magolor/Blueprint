# Blueprint Heaven Style Review

- Status: Actioned
- Scope: The `typescript` and `python` product lines, shared workflows, canonical documentation, CI, packaging, and repository hygiene.
- Trigger: Complete the requested workflow set and prepare one clean public snapshot per branch.
- Comparison base: Local `typescript` at `39bb05b` and local `python` at `971ec7b`.
- Staleness trigger: A new product line, runtime baseline, package boundary, or workflow authority.

## Result

The review found eleven material defects. This sanitation change actions every finding.

Blueprint now has one small package boundary on each branch. The shared workflow manual defines each requested work type through closeout. Current repository docs use controlled technical English.

## Findings and actions

| Severity | Finding | Action |
| --- | --- | --- |
| P0 | Python package import initialized a HeavenBase configuration store. This caused ambient I/O and a bootstrap dependency cycle. | Replaced it with inert local modules and immutable dataclass configuration. |
| P0 | The Python environment generator imported HeavenBase before it could establish its own environment. | Removed the generator and the HeavenBase runtime dependency. `pyproject.toml` and `uv.lock` now own dependency state. |
| P1 | Python exposed three CLI backends, broad aliases, config-store commands, and a placeholder GUI without a product requirement. | Replaced them with one `argparse` adapter over one public function. Removed the GUI entry point. |
| P1 | TypeScript modeled stateless template information as both a `Blueprint` class and a factory. | Replaced both with the direct `getProjectInfo()` function. |
| P1 | TypeScript retained caller configuration without a clear ownership transfer. | The boundary now validates and detaches input before it returns frozen information. |
| P1 | The TypeScript CLI accepted unknown options when a valid command appeared first. | Added a closed command union, exact grammar, and negative behavior tests. |
| P1 | The public agent guide imported a machine-specific absolute file. | Removed the private include and made the repository guide self-contained. |
| P1 | The public skill tracked one workstation inventory and one private Docker topology. | Moved instance facts to ignored `*.local.md` files. The generator writes local files, the index omits them, and installation preserves them. |
| P1 | The workflow page routed work but did not define each work type through resumption and closeout. | Added complete procedures for all 15 requested work types. |
| P2 | The queue omitted `draft` and `postponed`, while the log enforced an arbitrary 50-entry cap. | Added both live states, defined cancellation closeout, and removed the cap. |
| P2 | Current snapshots retained completed plans, downstream GUI evidence, outdated CI majors, and product-line drift. | Removed stale artifacts, updated supported runtime matrices, and updated official action majors. |

## Architecture after sanitation

| Line | Public owner | Boundary admission | Interface adapter | Dependency authority |
| --- | --- | --- | --- | --- |
| TypeScript | `getProjectInfo()` | `defineConfig(unknown)` | `src/cli.ts` | `package.json` and `pnpm-lock.yaml` |
| Python | `get_project_info()` | `define_config(object)` | `blueprint.cli` | `pyproject.toml` and `uv.lock` |

Both lines keep one cohesive package. Neither line has a GUI, service, database, plugin system, workspace, or speculative package split.

## Workflow coverage

`references/workflows/work-types.md` defines start, durable state, resume evidence, verification, and completion for:

- features;
- design proposals;
- discussions;
- bug reports, diagnosis, and fixes;
- documentation updates;
- refactors;
- experiments;
- task management;
- repository hygiene;
- workflow edits;
- large parallel implementation;
- downstream projects;
- test compression;
- surveys;
- integrations.

The manual also defines action authority and task states. It states that a local commit is not publication.

## ASD-STE100 review

This was a non-certified ASD-STE100 Issue 9 review. Formal conformance needs the approved dictionary, trained review, and the complete specification process.

The review used these criteria on canonical repository docs and the new workflow manual:

- Use one stable term for one concept.
- Prefer active voice and direct verbs.
- Put required conditions before the action.
- Use imperative sentences for procedures.
- Keep procedural sentences short.
- Separate one action or fact per sentence where practical.
- Do not remove technical meaning to shorten text.

The rewritten docs use `task`, `plan`, `report`, `owner`, `authority`, `change`, and `publish` consistently. Procedures now start with direct verbs. Long historical execution prose was removed after durable rules moved to current owners.

Primary source: [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) and the [official STE overview](https://www.asd-ste100.org/about_STE.html).

## Currency evidence

- Python 3.14 is an active bugfix release. The compatibility matrix now includes it. Source: [Python active releases](https://www.python.org/downloads/).
- CI action majors were checked against their official release pages on 2026-08-26: [checkout](https://github.com/actions/checkout/releases/latest), [setup-node](https://github.com/actions/setup-node/releases/latest), [setup-python](https://github.com/actions/setup-python/releases/latest), [setup-pnpm](https://github.com/pnpm/action-setup/releases/latest), [setup-uv](https://github.com/astral-sh/setup-uv/releases/latest), [upload-artifact](https://github.com/actions/upload-artifact/releases/latest), and [download-artifact](https://github.com/actions/download-artifact/releases/latest).
- pnpm `11.21.0` remains on the latest stable major. pnpm 12 is still prerelease. Source: [pnpm releases](https://github.com/pnpm/pnpm/releases).

## Test compression result

The TypeScript behavior tests remain compact. Each retained test protects public SDK, configuration, CLI, documentation, CI, or package behavior.

The Python suite previously lacked product behavior tests. The new tests cover SDK identity, configuration defaults, boundary failures, immutability, CLI output, and CLI rejection. Obsolete async and parallel test plugins were removed because no retained test uses them.

## Removed material

The sanitation removed six completed plans, two actioned surveys, six survey screenshots, one stale translation, two tracked private instance notes, empty Python package buckets, a placeholder GUI, and a destructive stale history script.

The pre-rewrite branch tips preserve the prior snapshot during this operation:

- `typescript`: `39bb05b`
- `python`: `971ec7b`

## Verification

Closeout used these gates:

- `rtk pnpm check`
- `rtk pnpm container:check`, when the Docker daemon is available
- `rtk uv sync --all-extras --frozen`
- `rtk bash scripts/check.bash full`
- `rtk uv build`
- deterministic Heaven Style index, scan, installation, and cross-branch tree checks
- one-commit history and public-ref checks for both branches

All available gates pass. The Docker container check is waived because the local daemon is stopped.

## Residual risk

The review does not claim formal ASD-STE100 certification. The product packages remain starter examples, not general application frameworks.

No product architecture finding remains open.
