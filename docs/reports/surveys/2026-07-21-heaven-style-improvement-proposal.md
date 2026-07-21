# Heaven-Style 0.1.2.0 Improvement Proposal

- Status: Actioned; accepted recommendations are reflected in Blueprint, with residual ideas left unqueued
- Date: 2026-07-21
- Task: direct user request
- Follow-up: none
- Target: Blueprint's canonical `.agents/skills/heaven-style/`
- Version decision: Preserve exactly `0.1.2.0` as an explicit no-bump waiver
- Evidence: `Blueprint:docs/reports/surveys/2026-07-21-cdase-workflow-comparison-survey.md`

## Placement and promotion rule

This Blueprint-owned research artifact intentionally names CDASE, Blueprint, DeepSeek Harness, and repository-qualified evidence. The editor policy forbids those reference-repository names, local checkout paths, and incidental provenance in distributed skill text and reusable source-neutral guidance; it does not forbid named evidence in a dated Blueprint survey.

Promote only source-neutral rules, examples, validators, and tests from this survey into the installed skill.

## Decision summary

Improve `heaven-style` by making its existing promises smaller, more explicit, and mechanically credible. Do not turn the skill into a CDASE-style workflow engine.

The current decision is:

1. Accept the four-surface docs lifecycle, one rolling development log, expiring scratch, and current/target/gap/non-goal status vocabulary. Blueprint is a queue-free template with inert `docs/tasks.template.yaml`; an instantiated operational repository promotes that starter to its sole live `docs/tasks.yaml`. HeavenBase currently owns that live queue with `HB-001`.
2. Accept the hermetic compact skill index, deterministic docs/index/template checks, focused invalid fixtures, and one repository-owned offline aggregate gate. The index validates field types and link containment, and its digest covers indexed Markdown, scripts, and assets.
3. Accept explicit Blueprint-to-HeavenBase source classification and manifest-v2 evidence for template-owned surfaces: reviewed source revision/digest, exact-path inventory, adapted-consumer fingerprint, and traversal/symlink rejection.
4. Retain transactional/offline skill installation and exact mirroring as an unqueued recommendation. The canonical skill has been installed globally and matches Blueprint, but current `install.py` still deletes the verified target before replacement validation, so installation is not yet transactional.
5. Retain narrowing the universal Typer/Click/argparse mandate as an unqueued recommendation.
6. Keep additional workflow metadata, decision-record structure, and agent-system criteria as non-active ideas until repeated use justifies a direct request or an operational-project task.

The version remains `0.1.2.0` throughout. The user has explicitly waived the normal fourth-segment bump.

## Accepted current slice and remaining problem

Blueprint preserves baseline `c2c3e48`; current 0.1.2.0 master contains the actioned control-plane slice and the repository collects 41 tests. External publication state is owned by the hosted release evidence, not this report.

| Area | Before this slice | Accepted current slice | Remaining state |
| --- | --- | --- | --- |
| Documentation authority | Goals, plans, reports, and dated progress could become competing state | Four surfaces, one authority order, one bounded log, expiring scratch, and a repository-role boundary | Actioned and verified |
| Task state | Template and operational task ownership were not distinguished | Blueprint has inert `docs/tasks.template.yaml` and no live queue; rename instantiates one live queue, and HeavenBase owns `docs/tasks.yaml`/`HB-001` | Actioned |
| Skill index | 1,197-line metadata dump with volatile timestamp and broad runtime import | 285-line `heaven-style-index/v2` projection with deterministic digest over indexed Markdown/scripts/assets, graph checks, metadata-type validation, local-link containment, atomic generation, and `--check` | Actioned |
| Validation evidence | No focused top-level invalid fixtures | Docs, index, and template-sync contract fixtures exercise accepted and rejected states | Actioned |
| Repository gate | Hook/CI inventories could drift | `scripts/check.bash fast|full` owns the check inventory and is called by hook/CI; the fast path runs offline | Actioned; current tree collects 41 tests |
| Blueprint consumer sync | Implicit/manual source relationship | Exact/adapted/excluded policy, source coverage check, byte drift, manifest v2 with source identity/revision/digest, consumer identity/ref, exact-path inventory, and adapted-consumer fingerprint; managed traversal and symlinks are rejected | Actioned; exact file copying is not a multi-file transaction |
| Skill installation | Deletes a verified target before replacement validation; default flow may refresh a Git reference | Canonical 0.1.2.0 skill is installed globally and byte-aligned, but the mutation sequence is unchanged | Recommendation only; no task assigned |
| Python CLI policy | Typer, Click, and argparse required universally in more than one home | Unchanged | Recommendation only; no task assigned |
| Extra task/routing metadata | Applicability and handoff largely prose-driven | Operational repositories own task state; Blueprint's route metadata remains intentionally compact | Not active work |

CDASE shows the value of explicit lifecycle, traceability, target resolution, and delivery reconciliation, but also demonstrates that repeated `MUST` prose drifts without enforcement. DeepSeek Harness shows how to close that gap with generated views, invariants, real-entry tests, transactional lifecycle, and one source per fact.

## Acceptance status

- [x] `heaven-style` remains exactly version `0.1.2.0` under the explicit no-bump waiver.
- [x] A pure read-only command rejects malformed or incorrectly typed skill metadata, duplicate IDs, broken `related_rules`, absolute/escaping/broken local links, and stale generated index content; its digest covers indexed Markdown, scripts, and assets.
- [x] The index check performs no network, user-config, database, global-skill, or repository writes.
- [x] Blueprint has one documented offline aggregate repository gate with focused docs/index/template fixtures and no live template-source queue.
- [x] Broad/high-risk guidance connects outcomes to evidence and names stop/approval conditions proportionally.
- [x] New validators/generators require valid and invalid fixtures plus freshness checks; template-sync fixtures cover adapted drift, retired exact paths, traversal, and symlinks.
- [x] Template manifest v2 fingerprints adapted consumer counterparts and records the exact-path inventory in addition to source/consumer identity and source revision/digest.
- [x] Distributed skill text keeps CDASE/DeepSeek/local-checkout provenance out of source-neutral guidance.
- [x] The canonical skill was installed globally and the installed tree matches Blueprint; this is not misreported as evidence of transactional publication.
- [x] The current repository collects 41 tests, while external publication is verified independently by the release workflow.

Residual recommendations are not acceptance failures or task state: make install/mirror publication transactional and offline by default, and make multi-adapter CLI parity conditional on a repository that actually supports multiple hosts.

## Non-goals

- Reproduce Scenario → Feature → Function artifacts.
- Add a workflow server, Hub, persistent conversation log, or mandatory run log.
- Make repository documents supreme over code, tests, or user instructions.
- Require approval between every documentation, design, test, and code phase.
- Require a clean working tree or base-branch synchronization before read-only work.
- Add a manual API registry for every repository.
- Make every package, workflow, or capability a plugin.
- Require 100% coverage, a snapshot for every change, or a decision note for every non-trivial edit.
- Introduce compatibility versions or parallel APIs solely to preserve every semantic change.
- Edit or clean unrelated user changes outside the accepted Blueprint slice.

## Authority and precedence contract

This proposal is subordinate to the following order:

1. The user's current instruction, target-repository `AGENTS.md`, runtime contract, compatibility policy, and permissions.
2. Blueprint's canonical skill source, repository policy, code, tests, and generated artifacts.
3. HeavenBase shipped code/tests and current architecture for repositories that explicitly adopt HeavenBase-lineage infrastructure.
4. Accepted Blueprint plans and current reports, followed by comparative lessons from CDASE and DeepSeek Harness.
5. Planned or aspirational reference designs only as labeled targets.

Consequences:

- Blueprint owns `heaven-style`; the skill is excluded from Blueprint's consumer template sync and is never edited in HeavenBase.
- Blueprint-to-HeavenBase sync applies only to files classified by `.blueprint-template.yaml`. Exact files are byte-owned by Blueprint, adapted files require consumer review, and excluded files remain outside the template contract. Manifest v2 records the exact-path inventory and fingerprints adapted consumer counterparts; managed paths cannot be absolute, escape via `.`/`..`, or traverse symlinks.
- HeavenBase ADR 0011 is accepted architecture with implementation planned. Its standalone Registry, installer, built-in seed, and full Registry-first migration must not be described as shipped 0.1.2.0 behavior.
- CDASE and DeepSeek Harness contribute design evidence, not authority, commands, dependencies, identity policy, or repository layout.
- The installed skill contains only source-neutral criteria. This report may retain named evidence because it is the research trail, not a distributed rule.

## Design principles

### 1. Critical promises need an enforcement owner

Each strong rule must be identifiable as one or more of:

- mechanically enforced by code;
- exercised by a test or scan;
- checked by the agent review loop;
- reserved for an explicit human decision.

Do not claim mechanical safety for agent-reviewed prose. Do not add a validator without an invalid fixture that proves the real top-level gate rejects it.

### 2. Governance is proportional to risk

Small, reversible, local work follows the existing fast path. A durable outcome contract or change envelope becomes appropriate when work changes public APIs, storage/schema, security/permissions, release behavior, external systems, multiple modules, multiple sessions, or a contested architecture decision.

### 3. Intended and shipped truth are distinct

Repository policy and specifications describe intent. Code, tests, generated artifacts, packaging, and release configuration describe shipped behavior. A mismatch blocks a confident claim and must be reconciled; neither side automatically wins without identifying its owner.

### 4. One fact has one normative home

Use this ownership model:

| Fact type | Normative home |
| --- | --- |
| Fast invariant and route | `SKILL.md` |
| Task sequence and completion gate | owning task playbook |
| Detailed code/project criterion | owning rule |
| Cross-rule intuition | example |
| Design-only procedure | architect workflow |
| Skill maintenance | editor/skill-update workflow |
| Mechanically derivable inventory | generated index/catalog |

Other surfaces link to the owner rather than paraphrasing it.

### 5. Workflow metadata narrows judgment; it does not replace it

Validated metadata may identify applicability, required inputs, expected output, and likely handoffs. The agent still interprets the actual request and repository. A skill cannot grant permission to write externally, publish, delete, message, or mutate user state.

### 6. Prepare, validate, then publish

Any installer, registry, or generated artifact workflow should prepare privately, validate completely, install rollback before publication, publish at one commit point, and leave the prior state usable on failure.

## Pareto portfolio

Scores are relative: impact and effort range from 1 (low) to 5 (high). Status is authoritative; this table is not a parallel task queue.

| ID | Improvement | Impact | Effort | Risk | Status / owner |
| --- | --- | ---: | ---: | ---: | --- |
| P1 | Hermetic compact skill graph validator and aggregate gate | 5 | 2 | 1 | Accepted current slice |
| P2 | Transactional install/mirror and explicit reference refresh | 5 | 3 | 2 | Recommendation; no task assigned |
| P3 | Real-entry, negative-control, and lifecycle test criteria | 5 | 2 | 1 | Accepted current slice |
| P4 | Conditional semantic interface/interaction port; remove universal three-CLI mandate | 4 | 2 | 2 | Recommendation; no task assigned |
| P5 | Proportional outcome contract, one role-appropriate task authority, and completion reconciliation | 4 | 2 | 1 | Accepted current slice |
| P6 | One-home-per-fact docs lifecycle and generated inventories | 4 | 3 | 2 | Accepted current slice |
| P7 | Schema-light project task state and optional skill routing metadata | 3 | 3 | 2 | Role-aware task contract accepted; extra route metadata not active |
| P8 | Conditional agent-system reconstructability and authority criteria | 3 | 2 | 2 | Existing rules cover current need; no new task |
| P9 | Formal proposed/accepted/rejected decision-note lifecycle | 2 | 3 | 2 | Not accepted; reconsider only after repeated need |

## P1. Hermetic skill graph validator and aggregate gate — accepted

### Rationale

The previous generated index catalogued invalid state instead of rejecting it. The accepted slice turns it into the skill's structural fitness function.

### Implemented design

`scripts/index.py` now owns parsing, graph/link validation, compact projection, deterministic rendering, atomic generation, and exact freshness checking. It uses direct filesystem/YAML operations and does not import HeavenBase runtime infrastructure.

The check path must be pure:

```text
read SKILL/frontmatter/tree
  -> build canonical in-memory model
  -> validate schema and relations
  -> compare generated projection
  -> print deterministic findings
  -> exit 0/1
```

It must not initialize application configuration, databases, global installs, user directories, network clients, or reference synchronization.

### Accepted checks

- `SKILL.md` frontmatter has `name`, `description`, and `metadata.version`.
- Version is present, and the real-tree fixture pins the waived `0.1.2.0` value.
- Every indexed Markdown file has parseable mapping frontmatter.
- IDs are unique across the namespace in which routes resolve them.
- Required fields differ by kind; required scalar/list types are validated.
- `enabled` is boolean when present.
- `related_rules` entries resolve to existing rule IDs.
- Indexed paths come only from the declared skill collections.
- Local Markdown links must be relative, remain contained by the indexed skill tree, and resolve; anchors may remain a separate later check if robust anchor parsing is not yet available.
- A generated file is not hand-edited and the index projection is current.
- The projection contains a normalized source digest over indexed Markdown and collected indexed scripts/assets, and no volatile generation timestamp.
- Compactness remains bounded by the real-tree test at 600 lines and 20,000 bytes.

Enum validation beyond accepted fields, trigger-collision analysis, anchor validation, and provenance scanning are not part of this slice. Add them only with a stable schema, an invalid fixture, and a direct request or operational task when needed.

### Code criteria

- Parsing and validation functions accept an explicit root and return data/findings rather than exiting internally.
- Diagnostics have stable code prefixes and path/message text.
- Output ordering is deterministic.
- `--check` never writes, including timestamps or caches.
- Generation writes only the declared generated index.
- File and path comparisons are cross-platform.
- Broad imports with unrelated initialization side effects are forbidden on the check path.
- Focused invalid fixtures cover malformed frontmatter, invalid metadata types, duplicate IDs, dangling `related_rules`, and absolute/escaping/broken local links; the real tree proves deterministic compact freshness and that script/asset changes affect the source digest.

### Test cases

- Missing/malformed frontmatter.
- Duplicate IDs.
- Dangling `related_rules`.
- Broken relative link.
- Absolute or escaping local link.
- Invalid metadata field type.
- Indexed script/asset content changes the source digest.
- Stale index.
- Real-tree exact version, deterministic rendering, and compactness.

### Gate contract

Blueprint now owns the inventory in one wrapper:

```bash
rtk bash scripts/check.bash fast
rtk bash scripts/check.bash full
```

The wrapper runs docs, skill-index, and template-source checks before environment/lint/tests; hook and CI point to the same inventory. The aggregate fast gate runs offline, and the current repository gate contains 41 tests.

## P2. Transactional installation, exact mirroring, and explicit refresh — recommendation, not scheduled

### Rationale

The current global install removes the old verified skill before the replacement has been copied, indexed, and validated. A failure can leave no usable install. Mirroring copies over an existing tree without a complete managed reconciliation, leaving stale removed files. Default installation also couples deployment to external reference refresh.

### Transaction model

```text
canonical source
  -> copy to temporary sibling staging directory
  -> optional explicit reference refresh in staging
  -> regenerate index in staging
  -> run full skill validation in staging
  -> preserve current verified target as rollback
  -> atomically publish staged target
  -> remove rollback only after success
```

### Code criteria

- Resolve and validate the exact canonical source and exact target before mutation.
- Stage on the same filesystem as the target when atomic rename is required.
- Never delete the current verified target before staging validates.
- On any pre-commit failure, remove only the staging directory and preserve the target byte-for-byte.
- On commit failure, restore the rollback target or report an exact recoverable path.
- `--dry-run` reports source, target, files, refresh behavior, validation, and publication plan without writes.
- Offline install uses checked-in assets and does not touch the network.
- Reference refresh is an explicit operation/flag, not an incidental read-like check.
- Mirror reconciles the managed skill tree exactly, removing stale managed paths while preserving unrelated paths only when the target contract explicitly allows them.
- Refuse to mirror into a broad/unverified location or over a non-`heaven-style` target.
- Temporary and rollback paths are narrowly scoped and never derived from an unresolved broad environment variable.
- Installation reports whether global, mirror, Claude plugin, or reference refresh state changed.

### Failure-injection tests

- Copy fails halfway: old target remains.
- Index generation fails: old target remains.
- Validation fails: old target remains.
- Atomic publication fails: rollback is restored or retained with exact instructions.
- A file removed from the canonical skill disappears from a managed mirror.
- An unrelated sentinel outside the managed mirror root remains unchanged.
- Dry run performs zero writes.
- Offline installation makes zero network calls.
- Temporary target roots isolate every test from the user's actual global install.

## P3. Stronger test evidence — accepted current slice

### Rationale

CDASE says tests are contracts but does not enforce its central workflow. DeepSeek Harness demonstrates that numeric coverage alone also misses real integration defects. The best portable rule is to test the actual contract boundary and prove new gates reject bad input.

### Accepted additions to `references/rules/project/test.md`

- A new validator, permission gate, policy gate, schema gate, or architecture check needs a deliberately invalid case that fails through the real top-level runner.
- Integration-sensitive behavior needs at least one test through the public, composed, loaded, packaged, generated, or deployed entry path that can expose the relevant failure.
- Tests assert external state, durable events, emitted protocol values, files, or cleanup—not an agent's self-report that it succeeded.
- Mock only nondeterministic or external boundaries; keep downstream shipping composition real when economical.
- Async/lifecycle tests use events or promises rather than arbitrary sleeps.
- A disposer/teardown contract proves the resource or registration is gone immediately after awaited cleanup.
- Generated artifacts have freshness checks, not hand-maintained expected inventories.
- Snapshot only a small canonical assembled surface; do not freeze every incidental string or renderer detail.
- Coverage thresholds remain repository policy, not a universal Heaven-style number.

### Conditional agent-system evidence

For software that sends model-visible prompts, tools, or errors:

- model-visible inputs are logged or otherwise reconstructable;
- "complete" is treated as a report until independent world-state/test evidence confirms it;
- stable model-facing schemas/text are behavioral API surfaces;
- security/isolation claims state what is and is not guaranteed.

Keep this compact in `test.md` initially. Create a separate agent-system rule only after repeated target-repository use proves the surface is stable and too large for the existing owner.

## P4. Conditional semantic interface and interaction ports — recommendation, not scheduled

### Rationale

The current service-interface rule mandates simultaneous Typer, Click, and argparse support for all Python project CLIs. That conflicts with minimal mental models and repository-first toolchain policy when a project only needs one CLI.

CDASE's host-neutral input specification and DeepSeek Harness's typed prompt port support a better general rule: declare semantic interaction once, then add adapters only for real hosts.

### Replacement rule

- Follow the target repository's declared CLI/UI framework by default.
- If the product genuinely supports multiple CLI or UI hosts, define commands/questions/results once in a framework-neutral semantic contract and compile/map thin adapters from it.
- A headless or automation path is required only when the product is intended for agents, CI, or non-interactive embedding.
- Required headless input is structured and fails loud when missing rather than blocking on an unavailable prompt.
- Cancellation is an explicit outcome, not an empty string or generic failure.
- Renderers own presentation; semantic handlers own validation and application behavior.
- The same semantic request must produce equivalent validation, exit/result status, and application effects across supported adapters.
- Do not introduce multiple parser/UI backends merely to satisfy the skill.

### Example contract shape

```text
semantic request
  -> validated input/result union
  -> application service
  -> host adapter rendering

interactive adapter: host-native prompt -> semantic answer
headless adapter: JSON/config -> semantic answer
```

### Targeted edits

- Remove the universal three-backend statement from `SKILL.md` daily notices.
- Rewrite the Python CLI section in `references/rules/project/interfaces.md` as conditional multi-adapter guidance.
- Keep one-registry/parity guidance only where multiple adapters are a declared product requirement.
- Add cancellation, headless structured input, and machine-readable result criteria.

## P5. Proportional outcome contracts and change envelopes — accepted current slice

### Rationale

CDASE's stable criteria and code plan are valuable for risky work but too heavy as universal artifacts. Blueprint already has success criteria, non-goals, touch lists, slices, stop conditions, and rollback posture in different places. Consolidate them for durable work without burdening small changes.

### Trigger

Use an outcome contract/change envelope when any of these applies:

- public API or external protocol change;
- storage/schema/migration change;
- security, permissions, credentials, or external messages;
- release/deployment/publication;
- cross-module or multi-repository change;
- multi-session plan or handoff;
- independently extensible capability;
- destructive or hard-to-reverse operation;
- contested architecture decision.

### Compact template

```markdown
## Outcome contract

| Criterion | Evidence | Status or waiver |
| --- | --- | --- |
| AC-1: observable behavior | focused test / probe / manual gate | pending |

## Change envelope

- Owned surfaces:
- Protected boundaries:
- Frozen/public contracts:
- Compatibility policy:
- Approval/stop conditions:
- Rollback/revert boundary:
- Explicit non-goals:
```

Criterion IDs are local to the durable plan or issue. Do not encode ownership hierarchy in IDs. Manual, visual, operational, or static evidence is allowed when automation is not appropriate, but the evidence owner and limitation must be named.

### Public capability decision

For a public API or genuinely open family, record exactly one outcome:

- reuse an existing contract;
- evolve the owning contract compatibly under repository policy;
- create a new contract because existing semantics do not fit.

This is an analysis field, not a manual global API registry.

### Completion reconciliation

Before "done," reconcile as applicable:

- implementation and owned call sites;
- targeted and broad tests;
- public API/types/schema;
- docs/examples and architecture pages;
- generated artifacts/catalogs;
- compatibility/deprecation state;
- plan/report/issue/PR status;
- known risks, limitations, and waivers.

## P6. One home per fact and generated contracts — accepted current slice

### Rationale

CDASE's active docs contradict one another because boot, sync, trust, identity, and authority rules are restated. `heaven-style` also repeats default criteria across `SKILL.md`, tasks, reviews, and workflows. DeepSeek Harness shows a more maintainable model: concise standing orders, links to an owning rationale/contract, and generated catalogs for inventories.

### Accepted criteria

- A task playbook links to detailed rule criteria rather than duplicating them.
- `SKILL.md` keeps only default invariants, the common loop, daily notices that truly affect most turns, and direct routes.
- Rule descriptions/keywords live in frontmatter and are indexed; route lists do not restate full rule prose.
- Generated lists of rules, tasks, services, APIs, events, commands, or plugins are never hand-maintained when the authoritative code/metadata can generate them.
- Generated artifacts carry an ownership header and a freshness command.
- Handwritten docs own semantics, rationale, limitations, and examples that cannot be derived.
- A first compression pass precedes any hard word budget. Add budgets only for standing surfaces whose growth has repeatedly harmed discovery.

### Compression targets

- Remove repeated coding criteria from either `SKILL.md` or task files, leaving one owner and concise links.
- Split task `related_rules` into the minimum always-required set and conditional candidates.
- Resolve `code-explain` versus `arch-design` trigger overlap by intent: explaining shipped behavior versus proposing/reviewing design.
- Keep source-neutral examples; do not mention evidence repositories in the installed skill.

## P7. Schema-light workflow contract — partially accepted

### Rationale

Tasks already have frontmatter, but fields such as applicability, required inputs, output, stop conditions, and handoff are implicit. A small validated contract would improve routing and auditability without creating a workflow engine.

The repository-role-aware queue schema, plan linkage, development-log handoff, and scratch lifecycle are accepted. Blueprint exercises the inert template side; HeavenBase exercises the live operational side. The following skill-routing metadata remains a candidate and is not active work:

### Candidate metadata

```yaml
profiles: [generic, python, typescript, heavenbase-lineage]
required_rules: [environment]
candidate_rules: [test, docs]
output_kind: change
handoffs: [code-review, doc-sync]
```

Do not finalize these names without checking every active task. The minimal accepted schema should express only repeated stable distinctions.

Each task body should make these sections findable, whether or not they are frontmatter:

- Inputs/evidence required.
- Ordered phases.
- Output or mutation type.
- Completion gate.
- Stop/approval conditions.
- Next handoff.

### Authority constraint

Metadata can say that a task may involve an issue, PR, message, release, or external system. It cannot authorize the action. User request, host permissions, and repository policy remain authoritative.

## P8. Conditional agent-system criteria — no new task

Do not import DeepSeek Harness's architecture wholesale. Add only source-neutral criteria that recur in agent or async-service repositories:

- Prepare private state, install rollback, and publish after commit.
- One async operation has one lifecycle owner/controller.
- Registration returns an exact idempotent disposer when it creates a lifetime.
- Teardown reaches quiescence, including child work and pending persistence.
- Events expose immutable facts; mutation/cancel/dispose authority stays with the owner.
- Validate/snapshot/freeze at queue, persistence, worker/process, wire, tool, and model boundaries; borrow readonly typed values inside a trusted same-process boundary.
- Publish notifications and derived state only after the success point that makes them true.
- Explicitly distinguish containment, policy, and authentication from a security sandbox.

Much of this already exists in the TypeScript async/architecture rules. First remove duplication and fill only cross-language gaps. A new rule is justified only if existing owners cannot remain coherent.

## P9. Decision-record lifecycle — not accepted now

Blueprint plans and reports already have statuses. Before adding another artifact family, test whether the architect workflow can cover durable decisions with a lightweight ADR shape:

- proposed: problem, proposal, alternatives, acceptance, risks;
- accepted/implemented: problem, present-tense decision, alternatives, consequences, verification;
- rejected: proposal retained with concise reason;
- superseded: replacement linked.

Require this only for cross-cutting decisions likely to be revisited. Do not require a decision note for ordinary feature work or local cleanup.

## Design conflicts and resolutions

| Conflict | CDASE pressure | DeepSeek Harness pressure | Proposed Heaven-style resolution |
| --- | --- | --- | --- |
| Documentation authority | Docs always override code | Code/types/events generate and verify contracts | Separate intended from shipped truth; mismatch blocks reconciliation |
| Gate strictness | Fixed HARD STOP cadence | Routine gates are mechanized | Human stops only for ambiguous, external, destructive, public, security, migration, or compatibility decisions |
| API discovery | Manual registry before logic | Typed seams require current consumers | Search semantically; create a seam only for demonstrated variation; generate inventories |
| Extensibility | API registry is universal coordination | Everything is a plugin | Preserve open registry versus closed union; no universal plugin architecture |
| Testing | Every criterion should map to tests | 100% coverage plus real-entry/snapshots | Map behavior to evidence; require negative controls and real entry paths by risk; no universal percentage |
| Audit trail | Log every session action | Durable event log reconstructs runtime | Persist durable decisions/evidence only unless replay is a product requirement |
| Change scope | Exact file whitelist | Transactional owners and package seams | Expected surfaces plus protected boundaries; permit necessary tests/docs/generated updates |
| Versioning | Every semantic change creates a version | Pre-release foundation can break and fix | Follow repository compatibility policy; one canonical API; temporary shims need named removal conditions |
| Interface portability | Host-neutral input spec | Typed prompt port and headless config | Semantic port with adapters only for real supported hosts |
| Skill portability | Repository is entire system | Large concrete monorepo policy | Repo policy first; source-neutral rules; proportional governance |
| Python compatibility | One template matrix can look universally reusable | Locked dependencies and consumer source may require different floors | Blueprint declares/tests 3.12–3.13 because locked published HeavenBase 0.1.1.1 contains 3.12-only syntax; HeavenBase 0.1.2.0 source keeps and passes 3.10–3.13; consumer evidence wins over blindly copying the template matrix |
| Permissions | Workflow self-declares authority | Owner handles grant/cancel/dispose | Skill describes checks but never grants external-write authority |
| Version maintenance | Normal skill edit bumps fourth segment | Working tree already records 0.1.2.0 | Explicit no-bump waiver; validator pins 0.1.2.0 for this work |

## Surface and implementation status map

| Surface | Decision | Status |
| --- | --- | --- |
| `docs/README.md`, `AGENTS.md` | Four surfaces, authority order, lifecycle, cleanup | Accepted current slice |
| `docs/tasks.template.yaml`, `scripts/docs.py` | Blueprint has an inert starter and no live queue; validation promotes/requires `docs/tasks.yaml` only after instantiation; historical DEVLOG task IDs remain legal but the newest template entry uses `Next: none` | Accepted current slice |
| `docs/DEVLOG.md`, `docs/scratch/` | One bounded handoff log and 45-day tracked scratch | Accepted current slice |
| `.agents/skills/heaven-style/scripts/index.py` | Pure validation, metadata-type and link-containment checks, compact deterministic projection, Markdown/scripts/assets source digest, atomic generation, `--check` | Accepted current slice |
| `.agents/skills/heaven-style/references/index.yaml` | Generated `heaven-style-index/v2`; never hand-edit | Accepted current slice |
| `tests/test_docs_contract.py`, `tests/test_heaven_style_index.py` | Valid and invalid contract fixtures | Accepted current slice |
| `.blueprint-template.yaml`, `scripts/template_sync.py` | Exact/adapted/excluded source ownership; manifest v2 records exact-path inventory and adapted-consumer fingerprint; managed traversal/symlinks are rejected | Accepted current slice |
| `tests/test_template_sync.py` | Exact and adapted drift, retired exact-path cleanup, unclassified-source rejection, and symlink/path safety | Accepted current slice |
| `scripts/check.bash`, hook, CI | One offline fast/full repository gate inventory | Accepted current slice; current gate contains 41 tests |
| `references/rules/project/{docs,test}.md` and task/workflow owners | One home, generated checks, negative fixtures, proportional closeout | Accepted current slice |
| `.agents/skills/heaven-style/scripts/{install,sync}.py` | Proposed staged publication, rollback, exact mirror, offline default; current global install is verified but delete-before-copy | Recommendation; no task assigned |
| Proposed `tests/test_heaven_style_install.py` | Copy/index/publish failure injection and zero-network checks | Recommendation; no task assigned |
| `SKILL.md`, `references/rules/project/interfaces.md` | Proposed conditional single/multi-backend CLI contract with one normative home | Recommendation; no task assigned |
| Additional task/workflow routing metadata | Add only after stable repeated need | Not active |

## Execution and verification handoff

### Completed current slice

- Preserved baseline `c2c3e48` and all unrelated worktree changes.
- Preserved the explicit `0.1.2.0` no-bump waiver.
- Implemented docs, index, and template-sync validators with focused rejected-state fixtures, including metadata types/link containment, adapted drift, retired exact paths, and managed path/symlink safety.
- Wired one check inventory through the hook and CI.
- Kept the installed skill source-neutral and Blueprint-owned.
- Verified the role-aware docs contract (Blueprint has no live queue; operational fixtures require one), exact index freshness with Markdown/scripts/assets coverage, and template source classification/manifest-v2 evidence.

### Verification completed

Run from Blueprint:

```bash
rtk bash scripts/check.bash fast
rtk git diff --check
```

The actioned docs/index/template slice passed its offline gate. The current Blueprint gate now contains 41 tests, the docs contract identifies Blueprint as a template source with no live queue, and the exact/adapted manifest contract remains enforced. Hosted release evidence remains separate from this report and is not turned into a local task queue.

### Unscheduled recommendations

1. If a direct user request prioritizes installer hardening, implement and failure-test staged offline installation and exact mirroring.
2. If a direct user request prioritizes interface guidance, move the complete CLI criterion to one owner and make multi-backend parity conditional.
3. Create no Blueprint queue item from this proposal. An operational consumer may create one task in its own declared authority when it owns the work.

## Specific review criteria

### Correctness

- Accepted: a validator failure cannot be serialized into a nominally valid index and ignored.
- Installer recommendation: a failed install cannot remove the last known-good global skill.
- Installer recommendation: a mirror cannot silently retain a removed managed rule/script.
- Accepted: task metadata cannot refer to missing rule IDs or paths.
- Version checks do not accidentally bump or normalize `0.1.2.0`.

### Modularity

- Parsing, graph validation, projection, writing, staging, publication, and external refresh have distinct owners.
- Validation does not depend on application runtime/configuration initialization.
- Installer recommendation: publication is a transaction, not interleaved copy/delete work.
- Workflow metadata supports routing; task prose owns execution semantics.

### Portability

- Installer recommendation: paths and atomic behavior are tested on supported platforms or limitations are explicit.
- Repository metadata selects the toolchain and interface framework.
- Interface recommendation: multi-host adapters are optional and contract-driven.
- Distributed rules contain no evidence-repository mechanics.

### Evidence quality

- Every new top-level gate has a negative control.
- Installer recommendation: tests inject failure before commit.
- Integration tests use temporary real trees and real command entrypoints.
- Generated output freshness is checked.
- Test reports name commands actually run and any unavailable environment dependency.

### Safety and authority

- Read/check commands have no hidden network or write effects.
- External refresh, global install, mirror, and publication scopes are explicit.
- The skill does not claim authority to create issues, send messages, publish, delete, or change external state without user/repository permission.
- Temporary paths and destructive targets are validated and narrow.

### Documentation

- Intended versus shipped behavior is explicit.
- One normative home exists per fact.
- Generated inventories are marked and never hand-edited.
- Known limitations and waivers are stated without overstating guarantees.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Validator becomes another framework | Validate only stable existing structure; no workflow execution engine |
| Strict checks disturb unrelated repository work | Use focused findings and temporary fixtures; preserve unrelated edits |
| Atomic swap behaves differently across platforms | Same-filesystem staging, platform tests, explicit fallback/rollback contract |
| Source-neutrality scan produces false positives | Narrow scope and explicit allowlists for owned names/assets |
| Routing metadata over-constrains agent judgment | Use metadata to narrow candidates; retain intent interpretation |
| Outcome contracts add bureaucracy | Trigger only for durable/high-risk work; small tasks stay on fast path |
| Generated catalogs erase useful rationale | Generate inventory only; keep semantics and tradeoffs handwritten |
| Interface rewrite removes useful parity | Preserve one-spec/multi-adapter parity when the repo actually declares multiple hosts |
| No-bump version hides a material change | Record the explicit waiver in the change/plan and verify exact version everywhere |
| Blueprint working tree changes concurrently | Re-read status/diff before every edit/review pass and preserve unrelated work |

## Rejected alternatives

### Import CDASE's full lifecycle

Rejected because the artifact and approval cost is disproportionate for a portable coding skill, and the reference lifecycle is not mechanically enforced in its own repository.

### Add more prose before validation

Rejected because the current highest-value gap is credibility of existing contracts, not lack of rules.

### Adopt DeepSeek Harness's plugin and coverage policies

Rejected because those policies are justified by one concrete runtime and toolchain. The portable lessons are ownership, real-entry evidence, generated contracts, and lifecycle fitness—not Cordis or a percentage.

### Put named comparative evidence in distributed Blueprint/skill guidance

Rejected because Blueprint's skill-maintenance policy requires distributed guidance to be source-neutral. Named comparative evidence belongs in Blueprint's dated survey artifacts rather than the installed skill.

### Bump the fourth version segment

Rejected for this work because the user explicitly requires version `0.1.2.0` to remain unchanged.

## If the recommendations are revisited

No follow-up is assigned by this actioned report. If the user requests the highest-impact remaining improvement, harden the installer so a failed attempt cannot remove the last known-good skill, ordinary install is offline, and managed mirrors converge exactly. Use temporary roots and failure injection before any real global publication.

After installer hardening, a separate direct request may move the full CLI compatibility criterion to one normative owner. Do not reopen the completed docs/index/template work or add another workflow schema unless a concrete failure demonstrates the need.
