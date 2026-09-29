---
name: heaven-style-code-drift
description: Read when deciding which legacy AgentHeaven code conventions to restore in Heaven Style.
---

# Heaven Style code-style drift

## Summary

The code-style survey has been decided by the maintainer. Canonical rules now apply the accepted and revised outcomes below, including paired vocabulary, logical guard clauses, stable-prefix imports, ORM-first database access, and shared utility ownership. The original comparison remains historical evidence; it no longer presents an undecided rollback list.

- Status: Decided; canonical skill rules own the implemented behavior.
- Date: 2026-09-09
- Owner: Blueprint maintainer; prepared by Codex.
- Scope: Python and TypeScript code style, with adjacent import, formatting, and API-documentation conventions.
- Related: [Plan](../../plans/2026-09-09-rule-drift.md).
- Staleness: Reassess after a style decision, a new release, or a change to the cited legacy source.

## Maintainer decisions

Decisions recorded on 2026-09-09 under STYLE-003. Here “release” means the drifted 0.2.0-alpha.1 snapshot; “legacy intent” means the original Python/AgentHeaven design, with the maintainer's refinements taking precedence.

| Items | Decision applied |
| --- | --- |
| A1, D15 | Revised: wrapped instance operation > generic wrapped API > ORM > file-read generic SQL > dialect-specific SQL > file-read/transpiled SQL > inline SQL. Reuse existing wrappers; prefer ORM whenever practical. |
| A2–A6 | Confirmed: aligned JSON aliases, KV config, clean/shared utility rules in the catalog, minimal owning-object API, five SOLID principle pages per language. |
| D1 | Revised: maximize stable import prefix; first-party relationships, generic dependencies, specialized dependencies, then incidental utilities. Preserve TypeScript runtime/type/lazy import controls. |
| D2 | Accepted: prefer existing package utility re-exports and owned operations. |
| D3, D4 | Keep established Python CM_* singleton naming without promoting it to a universal convention. Keep pj, drop irrelevant KL/UKF glossary terms, and reserve future TS config naming. No broad historical glossary restoration. |
| D5, D6 | Accept brevity review in both languages. Do not restore src2dst naming as a separate generic convention; shared utility rules own that concern. |
| D7, D8, D20, D21 | Revised into language vocab folders: paired verbs, explicit domain nouns, and supported aliases. Owned KV uses get/set/unset/setdef; native Map.delete remains native. Normalize provider identity such as postgres across SDK/config/CLI. Prefer specific nouns over kind. |
| D9 | Keep toString in TypeScript; do not introduce toStr. |
| D10 | Prefer named arguments whenever possible, with Python keyword-only options and TS options objects. No fixed five-positional-argument threshold. |
| D11 | Restore compact idiomatic code and indentation that follows logical relationships. Error guards precede normal work; parallel alternatives stay parallel. |
| D12 | Retain Python short descriptions plus complete Google Args/Returns/Yields sections. TS uses short, structured semantic TSDoc with flexibility for applicable tags. |
| D13 | Keep modern built-in Python generics and union syntax, subject to supported runtime. |
| D14 | Enforce one live owned version and representation; accepted aliases share it. Explicit real external support obligations remain bounded boundary adapters, not parallel internal APIs. |
| D16 | Keep TypeScript import/resource controls and existing no-owner fallbacks. |
| D17 | No blanket formal extraction rule. Prefer package-owned resources/assets for most static defaults, bootstrap config, built-in instances, and substantial assets; preserve fixed code facts and code-owned validation. No forced folder rename. |
| D18 | No new TypeScript logging policy selected; retain repository ownership. |
| D19 | Enforce Black + Flake8 for Python. No new TypeScript tool choice selected. |
| D22 | Paired lifecycle vocabulary now covers the naming gap. Existing fluent object guidance remains; do not create methods merely to fill a table. |
| Single/multiple inputs | Prefer upsert(x) and upsert([x]) rather than batch_* by default. Distinct batch APIs require a materially different public contract. |

Canonical entry points: [Python vocabulary](../../../.agents/skills/heaven-style/references/rules/code/python/vocab.md), [TypeScript vocabulary](../../../.agents/skills/heaven-style/references/rules/code/typescript/vocab.md), and the [paired rule catalog](../../../.agents/skills/heaven-style/references/rules/overview.md). Implementation detail: mapping conversion is paired as Python from_dict/to_dict and TS fromDict/toDict; existing fromRecord/toRecord can be explicit equivalent aliases. Native and external contracts keep their required spelling.

## Scope and method

Compared the complete Python and TypeScript rule trees, including nested examples, across local Git snapshots. Mapped moves and splits before judging semantic changes. Read the legacy prescriptive guide and instruction file, and checked representative entity conversion/configuration code. This is a rule audit, not an exhaustive audit of either product's implementation.

| Evidence | Snapshot and role |
| --- | --- |
| Legacy groundtruth | Local AgentHeaven-dev, clean worktree at `9f2a8d8e8da35d205cf4ac87de6ef8f249314e9e`; style guide (`AgentHeaven-dev/docs/CODE_STYLE.md`) and enforced instructions (`AgentHeaven-dev/.github/instructions/code-style.instructions.md`). |
| Requested baseline | `v0.1.2.0`, `fc1eace`; [historical rule tree](https://github.com/Magolor/Blueprint/tree/v0.1.2.0/.agents/skills/heaven-style/references/rules). |
| Intermediate checkpoint | `2be2b0b`, Heaven Style 0.1.2.23; [historical code tree](https://github.com/Magolor/Blueprint/tree/2be2b0b/.agents/skills/heaven-style/references/rules/code). |
| Release comparison | `v0.2.0-alpha.1`, `728de9b`, and Python companion tag `v0.2.0-alpha.1-python`, `9b94420`. There is no final 0.2.0 tag in this local repository. |
| Before this expansion | `64b5f40`, including the four earlier corrections committed in `471950f`. |
| Accepted target | Current working rules additionally strengthen OOP and split SOLID into five principle pages per language, as requested in this conversation. |

The broader workflow, GUI, distribution, extension-lifecycle, and architecture changes are treated as intentional, following the owner's clarification. They are not a rollback list. Language syntax changes such as camelCase, JavaScript iteration, strict `unknown` boundaries, native ESM, and async disposal are not themselves style regressions.

Legacy evidence is not perfectly uniform. Its vocabulary bans apply to class concepts, while its I/O utility section explicitly permits `load_*`/`dump_*`. Its guide prioritizes canonical methods, but implementation code can still contain exceptions. For example, BaseUKF conversion (`AgentHeaven-dev/src/ahvn/ukf/base.py:972`) directly demonstrates `to_dict`/`from_dict`; nearby code uses older typing syntax. Current user instructions override historical conventions, including the newly authorized JSON aliases and best-effort SQL externalization.

## Comparison

### Accepted corrections

| ID | Drift and timing | Implemented target |
| --- | --- | --- |
| A1 | Legacy §9 externalizes every raw SQL string. 0.1.2.0 already relaxed this to “substantial” SQL; TS later recommended an inline statement. | Practical SQL text lives in packaged resources, including small built-ins; raw/unsafe entry points still bind caller values. See [Python SQL](../../../.agents/skills/heaven-style/references/rules/code/python/sql.md) and [TS SQL](../../../.agents/skills/heaven-style/references/rules/code/typescript/sql.md). |
| A2 | Legacy logical conversion vocabulary became TS `fromJSON`/`toJSON` by 0.1.2.23. | Recommend `fromJson`/`toJson`, with equivalent uppercase aliases sharing behavior. See [TS verbs](../../../.agents/skills/heaven-style/references/rules/code/typescript/vocab/verbs.md). |
| A3 | Legacy §3 uses central KV config and tunable resources. 0.1.2.0 already recommended a caller-supplied frozen EmbedConfig with literals instead of the intended override/config flow. | KV config owns defaults; explicit overrides use None/Ellipsis in Python and undefined/null distinction in TS. Typed resolved specs remain internal execution data. See [Python config](../../../.agents/skills/heaven-style/references/rules/code/python/config.md) and [TS config](../../../.agents/skills/heaven-style/references/rules/code/typescript/config.md). |
| A4 | Legacy §2 prioritizes owned utilities. 0.1.2.0 already required multiple consumers for shared helpers and foregrounded stdlib examples. | Use package utilities such as pj first; needed generic helpers go to shared utils from the first use; specialized one-use expressions stay inline. See [Python util](../../../.agents/skills/heaven-style/references/rules/code/python/util.md) and [TS util](../../../.agents/skills/heaven-style/references/rules/code/typescript/util.md). |
| A5 | Legacy §4 requires a predictable object API. Python retained the core idea; TS by 0.1.2.23 broadly recommended free functions for parsing and projection, diluting ownership even for pure domain operations. | Member methods wherever there is a natural owner: `Entity.fromJson(data)` and `ws.upsert(product)`. Add concrete construction, mutation, internal-composition, and utility exceptions. See [Python API](../../../.agents/skills/heaven-style/references/rules/code/python/api.md) and [TS API](../../../.agents/skills/heaven-style/references/rules/code/typescript/api.md). |
| A6 | SOLID was present but compressed: Python used a combined example page; TS distributed its treatment across a summary, extension, and composition pages. This is an emphasis gap, not a claim that five legacy files disappeared. | Five dedicated principle pages under each language's solid folder, each with owning-object patterns, anti-patterns, consequences, and review guidance. See [Python SOLID](../../../.agents/skills/heaven-style/references/rules/code/python/solid.md) and [TS SOLID](../../../.agents/skills/heaven-style/references/rules/code/typescript/solid.md). |

### Original decision candidates (historical)

The table records the original recommendations before the maintainer decisions above. It is retained for traceability and does not override them.

| ID | Legacy intent → current rule | Timing / evidence | Proposed decision |
| --- | --- | --- | --- |
| D1 | Utility-facade imports first → conventional stdlib/third-party/first-party groups unless the repo says otherwise. | Already changed in 0.1.2.0 [format](https://github.com/Magolor/Blueprint/blob/v0.1.2.0/.agents/skills/heaven-style/references/rules/project/format.md); legacy §§7.6, 13. Current [format](../../../.agents/skills/heaven-style/references/rules/project/format.md). | **Restore package-owned utility imports first** as the style fallback, preserving a repository's explicit organizer configuration. |
| D2 | Prefer utility re-exports of dataclass, deepcopy, datetime, typing primitives → preference now focuses on owned operations, without a general re-export preference. | Already weakened in 0.1.2.0 util/types; legacy §7.6. Current [util](../../../.agents/skills/heaven-style/references/rules/code/python/util.md), [types](../../../.agents/skills/heaven-style/references/rules/code/python/types.md). | **Restore existing package re-exports first**, but do not create a giant facade or force obsolete typing spellings. |
| D3 | `CM_*` is the conventional package config manager and uppercase singleton → `cfg` examples and no explicit manager singleton convention. | CM_* still appears in 0.1.2.23 name.md; removed by the alpha release. Legacy §§3.1, 6. Current [Python names](../../../.agents/skills/heaven-style/references/rules/code/python/name.md). | **Restore CM_* as a documented Python singleton convention**; separately decide whether TS uses CM_* or an ordinary camelCase service binding. This is naming, not an ambient-read requirement. |
| D4 | Shared glossary includes pj, sig2func/func2sig, vdb/mdb, cfg, tmp, res/resp → much smaller generic glossary; TS lacks a parallel shared abbreviation table. | Most reduction already in 0.1.2.0; pj/CM_* removed after 0.1.2.23. Legacy §6.2. Current [Python names](../../../.agents/skills/heaven-style/references/rules/code/python/name.md), [TS names](../../../.agents/skills/heaven-style/references/rules/code/typescript/name.md). | **Restore a paired language glossary** for general abbreviations; leave KL/UKF-specific terms with their owning domain. pj usage has already been restored, but its glossary entry has not. |
| D5 | Frequent names must be terse, and verbose names get shortened on review → TS asks for short clear domain names but lacks Python's explicit three-part re-examination rule. | TS-specific coverage gap; Python kept this rule from 0.1.2.0. Legacy §6. | **Apply the same brevity review to TS**, using semantic word count rather than underscores. Do not shorten into ambiguity. |
| D6 | Pure conversion may use src_to_dst or src2dst → these generic utility naming forms are omitted from the maintained naming guide. | Already omitted in 0.1.2.0 name.md; legacy §6.3. | **Restore aligned transform names for independent shared utilities**, while keeping entity conversion on from*/to* member methods. |
| D7 | Canonical class construction/export vocabulary, with a strong synonym ban → richer lookup/retrieval/load/parse vocabulary with semantic distinctions. | 0.1.2.0 Python oop.md already permits retrieve/load/query/search; TS further distinguishes fetch/find/getOrThrow by 0.1.2.23. Legacy §4.2. Current [Python verbs](../../../.agents/skills/heaven-style/references/rules/code/python/vocab/verbs.md), [TS verbs](../../../.agents/skills/heaven-style/references/rules/code/typescript/vocab/verbs.md). | **Keep distinct meanings, strengthen the synonym ban for the same meaning.** Decide the shared operation matrix explicitly instead of restoring a context-free ban on load/fetch/retrieve. |
| D8 | Python KV vocabulary includes get/set/unset/setdef/clear → TS canonical table uses Map-style delete and omits setdef, while the TS config-store API uses unset. | Cross-language inconsistency already visible by 0.1.2.23. Current [Python value verbs](../../../.agents/skills/heaven-style/references/rules/code/python/vocab/value.md), [TS verbs](../../../.agents/skills/heaven-style/references/rules/code/typescript/vocab/verbs.md), [TS config store](../../../.agents/skills/heaven-style/references/rules/code/typescript/config/store.md). | **Align owned KV APIs to unset/setdef**, keeping native Map.delete native; decide whether an owned delete alias should be supported. |
| D9 | to_str is the canonical object string method and __str__ is the protocol → TS only recommends toString, without an aligned toStr alias. | TS choice present by 0.1.2.23; legacy §4.2 and current Python value verbs. | **Consider toStr with equivalent toString**, following the approved JSON approach. Keep debug rendering and lossless serialization distinct. |
| D10 | Constructors use minimal authoritative fields and no more than about five positional args → numerical bound omitted; TS recommends options when meaning or evolution warrants it. | Python model rule already omitted the bound in 0.1.2.0; legacy §4.3. Current [Python API](../../../.agents/skills/heaven-style/references/rules/code/python/api.md), [TS API](../../../.agents/skills/heaven-style/references/rules/code/typescript/api.md). | **Restore a review trigger around five positional args**, not a mandatory configuration object for every method. |
| D11 | Compress first, accept a small readability tradeoff, expand on review → compress only when readable. | Already softened in 0.1.2.0 py.md; legacy §7 and enforced instruction 6. Current [Python flow](../../../.agents/skills/heaven-style/references/rules/code/python/flow.md), [TS flow](../../../.agents/skills/heaven-style/references/rules/code/typescript/flow.md). | **Restore compactness as an explicit default**, while keeping errors, SQL/prompts, and complicated branches clear. |
| D12 | Public docstrings are short, with Args/Returns when non-obvious → Python always requires full Args and Returns/Yields, including Args: None; TS remains more selective. | Already changed in 0.1.2.0 docstring.md. Legacy §12; BaseUKF.to_dict illustrates a compact docstring. Current [Python docs](../../../.agents/skills/heaven-style/references/rules/code/python/doc.md), [TS docs](../../../.agents/skills/heaven-style/references/rules/code/typescript/doc.md). | **Restore concise semantic docs**, retaining complete annotations and documenting real constraints; make mechanically empty sections optional. |
| D13 | Legacy examples use utility-exported Dict/List/Optional → modern built-in generics and union syntax. | Already changed in 0.1.2.0 types.md; legacy §7.6 and representative code. | **Keep modern typing syntax**; restore utility ownership independently. This is an intentional language modernization candidate, not a behavioral regression. |
| D14 | Exactly one live API unless explicitly waived → stable packages and persisted formats follow declared support obligations. | Stable-version exception already in 0.1.2.0 compat.md; current wording expands data-preservation and temporary-shim conditions. Legacy §5. Current [compat](../../../.agents/skills/heaven-style/references/rules/code/python/compat.md). | **Keep real published/data support obligations**, retain the strong one-live-owned-API rule. JSON aliases are explicitly supported semantics, not deprecated compatibility shims. |
| D15 | SQLAlchemy ORM by default, Core only when insufficient → repository-selected ORM/driver, including direct driver use. | Already changed in 0.1.2.0 sql.md; legacy §9. | **Keep the package's selected database owner**, unless you want a separate Python ORM-default rule. External SQL ownership is already restored and is independent of ORM choice. |
| D16 | All paths/resources pass through CM_*.pj and config resource lookup → importlib.resources/new URL examples allowed when no owner exists. | Already generalized in 0.1.2.0 config/util; TS adds ESM mechanics later. Legacy §§2.2, 10. | **Keep the no-owner fallback; foreground owned resource APIs in examples.** Do not require a foreign package solely for resource loading. |
| D17 | All prompts, examples, schemas, seed data, and regex literals are resources → current rules emphasize tunables/assets, do not state an equally broad extraction rule for every schema/regex/fixture. | Already narrower in 0.1.2.0 config/flow. Legacy §§3, 7.7, 10. | **Decide extraction by artifact ownership:** restore long/changeable schemas, regexes, prompts and fixture data as resources; keep small fixed format markers and compiler-owned schemas in code. |
| D18 | Debug logging explicitly gated by CM_*.get(core.debug) → generic repository logging policy with minimal diagnostics. | Already generalized in 0.1.2.0 error.md; legacy §8. Current [Python errors](../../../.agents/skills/heaven-style/references/rules/code/python/error.md), [TS errors](../../../.agents/skills/heaven-style/references/rules/code/typescript/error.md). | **Restore config-owned debug gating**, with the key declared by the package rather than imposing core.debug on every package. |
| D19 | Black + Flake8 are universal required tools → repository-owned formatter/linter commands; TS allows multiple coherent tool profiles. | Python tool policy generalized by 0.1.2.0; TS preference broadened by 0.1.2.23. Legacy §§1, 13; current format rule. | **Keep repository tool ownership.** Preserve compactness/import semantics as style rules independently of which tool enforces them. |
| D20 | Python from_dict/to_dict and loads_*/dumps_* → TS fromRecord/toRecord and parse*/encode*/decode*/format*, beyond the already-fixed JSON spellings. | TS vocabulary exists by 0.1.2.23; legacy §§4.2, 6.3. Current paired value/verb pages above. | **Choose a complete paired conversion matrix**, distinguishing mapping data, JSON-shaped data, text, bytes, files, and display. Do not treat differently named representations as interchangeable just to align spelling. |
| D21 | Python identifier/object_id and kind/dtype/entity guidance → TS id/*Id and kind-or-type discriminants; Python Spec may include raw declarative input, while TS Request/Spec explicitly separates raw/resolved input. | Present by 0.1.2.23. These are cross-language vocabulary deltas from the 0.1.2 baseline, not claims that the legacy guide specified every modern role. | **Align the meanings and document language spellings**, especially type identity versus instance identity and raw request versus resolved spec. Keep native casing. |
| D22 | Python explicitly lists rename/flush/reset and gives fluent field-declaration patterns → TS canonical list omits those verbs and gives less guidance for fluent methods on the same object. | Python rules already carry these conventions in 0.1.2.0; TS lacks paired coverage by 0.1.2.23. Omission is not a prohibition. | **Fill the paired vocabulary/example gaps**, keeping fluent steps only when they configure one understandable object and reduce caller complexity. Do not add methods solely to complete a table. |

### Coverage and retained rules

The following topic map accounts for the old code rules and every current language subtree. A move or split alone is not listed as drift. Added runtime-specific mechanics are retained unless they conflict with the accepted domain style.

| Topic | Historical → current owners | Disposition |
| --- | --- | --- |
| Public object model | Python model.md → api.md + api/example.md; TS architecture.md → api.md | A5; constructor bound D10. Public facade, hidden implementation plumbing, explicit lifecycle, and no meaningless wrappers retained. |
| Vocabulary | Python oop.md → verbs.md + verbs/value.md; TS api/verbs added before .23 | A2; D7–D9, D20–D22. clone and from*/to* ownership retained. |
| SOLID | Python solid.md combined examples → solid.md + solid/*; TS architecture.md → solid.md + solid/* | A6. Responsibility, substitution, composition, role contracts, inward dependency direction retained. Open/closed family architecture choices excluded from rollback. |
| Configuration | config.md; TS config.md + config/store.md added | A3; D3, D16–D18. Typed resolved execution specs do not replace KV config. Async store persistence architecture is intentional context. |
| Helpers/utilities | Python clean.md, util.md; TS util.md and flow.md | A4; D1–D2. No tiny feature-local helpers, no duplicate utility owner, no hypothetical wrappers retained. |
| Naming | name.md | D3–D6. Native casing, predicate prefixes, one term per concept, no meaningless type suffixes retained. |
| Expression shape | Python py.md → flow.md; TS flow.md | D11. Comprehensions, guards, unpacking, direct returns, explicit falsy/omission semantics retained. |
| Files/exports | Python files.md → files.md + files/layout.md + files/example.md; TS modules.md → files.md + files/package.md + files/optional.md + files/check.md | Cohesive ownership, one public facade, lazy optional dependencies, no accidental deep imports retained. Product/package architecture changes excluded. |
| Types | Python types.md; TS types.md → types.md + types/input.md + types/shape.md | D13. Typed external validation, precise internal shapes, strictness and readonly/ownership distinctions retained. |
| API docs/comments | Python docstring.md → doc.md + doc/format.md + doc/example.md + comment.md; TS docs.md → doc.md + doc/format.md + doc/example.md + doc/check.md + comment.md | D12. Caller-visible contract accuracy and comments explaining non-obvious reasons retained. General Markdown workflow changes excluded. |
| Errors/async | Python error.md; TS async.md → async.md + async/life.md + error.md | D18. Narrow catches, contextual errors, no silent fallback success, explicit cancellation/disposal retained. |
| SQL | Python sql.md; TS sql.md added | A1; D15–D16. Binds, transaction ownership, provider details behind domain boundary retained. |
| Compatibility | Python compat.md; TS compat.md added | D14. Update owned callers, remove obsolete parallel APIs, use explicit migration owners retained. |
| Toolchain/imports | Shared format/environment; TS environment.md → env.md + env/compiler.md + env/check.md | D1, D19. Declared wrappers, compiler strictness, no unused/star imports except utility boilerplate retained. |

### Example consistency follow-up

STYLE-003 aligned utility examples with package-owned contracts and kept SQL functions explicitly labeled private adapter sketches. Domain discriminators now use operation/status/provider in the affected examples. Actual TypeScript import, optional-loading, and runtime controls remain intact.

## Decision implementation verification (STYLE-003)

Both full product gates passed after the decisions: 16 TypeScript tests, 44 Python tests, strict type/lint/format checks, documentation checks, build, publint, and the packed TypeScript consumer. Skill metadata and generated-index validation passed. All 207 tracked skill files match across both branches at tree `46aa65d9920c1f5a344c679f49b63a029a0d202d`; the global installation was refreshed. Examples are illustrative rule contracts, not a new database integration or a published package release. No TypeScript logger/formatter framework was selected.

## Prior verification (STYLE-002)

TypeScript full check passed: documentation, formatting, lint, strict types, 16 tests, skill synchronization, build, publint, and packed consumer verification. Python full check passed with 44 tests. Skill metadata and generated index validation passed. Both branches share the exact skill tree `4333beb3f6116c595336d806de5276ea76d3c396`; the global skill was reinstalled. SOLID snippets are explicitly illustrative API sketches, not independently compiled integration programs.

## Original recommendation and limits (historical)

Prioritize D1–D6, D8–D12, D16–D18, and D20–D22 for restoring the distinctive code style. Keep the deliberate modernizations in D13–D15 and D19 unless there is a concrete contrary requirement. D7 needs a shared semantic vocabulary decision rather than a blanket ban. OOP and SOLID are already accepted work, not pending decisions.

This is the complete set of substantive code-style differences identified in the inspected rule corpus, grouped by decision rather than by every changed sentence. It cannot prove that no nuance was missed. Timing says “already by” when snapshots establish an upper bound; it does not invent the original introducing commit. The local AgentHeaven checkout is the requested groundtruth, not proof of its own historical consistency. No broad architecture rollback or unapproved D-item change has been applied.

The original decision process is closed by the recorded outcomes above. Future changes belong in the canonical rules and normal task queue; this survey is historical evidence, not a second queue.

## References

- Legacy AgentHeaven guide (`AgentHeaven-dev/docs/CODE_STYLE.md`), §§2–13 provide the code-style groundtruth.
- Legacy enforced instruction (`AgentHeaven-dev/.github/instructions/code-style.instructions.md`) provides the compact priority list.
- [Current paired language map](../../../.agents/skills/heaven-style/references/rules/overview.md) routes to the complete normative rules.
- [Release code tree](https://github.com/Magolor/Blueprint/tree/v0.2.0-alpha.1/.agents/skills/heaven-style/references/rules/code) preserves the comparison endpoint before these corrections.
