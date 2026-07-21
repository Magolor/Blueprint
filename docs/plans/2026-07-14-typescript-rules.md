# Heaven-style TypeScript Rules Plan

- Status: Done
- Created: 2026-07-14
- Scope: Add a Bun-first TypeScript rule surface to heaven-style while keeping Python-only conventions and source-repository provenance out of TypeScript guidance.
- Links: `.agents/skills/heaven-style/`, `docs/reports/surveys/2026-07-14-typescript-rules-survey.md`, `docs/progress/2026-07-14/README.md`

## Problem

Heaven-style previously exposed detailed Python rules but only a placeholder TypeScript directory. Its architecture principles are useful across languages, while several Python requirements—Google-style docstrings, Python naming and collection protocols, `heavenbase.utils`, `CM_HVNB`, pytest markers, and uv-based commands—must not be copied mechanically into TypeScript. The new surface needs explicit pattern/anti-pattern guidance, primary public references, and a reproducible Bun-first toolchain.

## Success Criteria

- [x] Heaven-style states a clear precedence order for shared architecture principles, TypeScript-specific rules, repository requirements, and local exceptions.
- [x] TypeScript rules cover language shape, type safety, API/error/async boundaries, modules and exports, tests, documentation, dependencies, and generated code without importing Python-only conventions.
- [x] Environment guidance is Bun-first, lockfile-reproducible, and defines standard format, lint, typecheck, test, and build gates.
- [x] Rules state their rationale and reject product-, framework-, source-repository-, and machine-specific generalization.
- [x] Generic cross-language code-sanity candidates remain separately reviewable before any Python-wide adoption.
- [x] Skill metadata, routing, generated index, standard global install, docs artifacts, and verification are current.

## Non-Goals

- Do not rewrite existing Python rules during this change except for language-aware routing or wording required to expose TypeScript correctly.
- Do not force Bun on repositories whose `AGENTS.md` or checked-in lockfile establishes another runtime/package manager.
- Do not publish private/reference-repository names, local checkout paths, machine-specific setup sources or observed versions, or borrowed product/framework internals.
- Do not add TypeScript application scaffolding to Blueprint.

## Slices

### Slice 1: Rule Boundary and Public References

- Goal: Establish which existing heaven-style rules transfer, which require TypeScript adaptations, and which generic code-sanity patterns merit review.
- Touch: existing skill architecture, target-repository contracts, primary public tool documentation, and survey report.
- Acceptance: Every normative rule has a clear rationale; product/framework-specific details and private/local provenance are excluded.
- Verification: Re-open the owning skill rules and cited primary public specifications; check pattern/anti-pattern consistency.
- Docs: `docs/reports/surveys/2026-07-14-typescript-rules-survey.md`.

### Slice 2: TypeScript Rule Surface

- Goal: Add focused TypeScript coding and environment rules with explicit pattern/anti-pattern pairs.
- Touch: `.agents/skills/heaven-style/SKILL.md`, `references/rules/overview.md`, `references/rules/code/typescript/`, and matched project/task/workflow routing.
- Acceptance: A normal TypeScript task can discover and apply the rules without loading Python-only requirements.
- Verification: Generated index contains all new rule IDs and links resolve.
- Docs: Rule files and this plan.

### Slice 3: Install and Closeout

- Goal: Regenerate skill metadata, install the canonical global copy, and complete repository checks.
- Touch: generated `references/index.yaml`, plan/report/progress status.
- Acceptance: Skill install, index check, scanner, compile, lint, tests, environment drift check, and diff checks pass or have explicit evidence-backed waivers.
- Verification: Commands recorded in the closeout and daily progress note.
- Docs: `docs/progress/2026-07-14/README.md` and final plan closeout.

## Progress

- 2026-07-14: Inventoried the current heaven-style rule, workflow, docs, and generated-index surfaces and reviewed current primary public tool documentation.
- 2026-07-14: Added six TypeScript rules, made shared routing language-aware, regenerated the index, and installed the canonical global copy.
- 2026-07-14: Kept generic cross-language candidates reviewable; no Python code rule absorbed them.
- 2026-07-14: Removed source-repository and machine-specific setup provenance, encoded the source-neutral maintenance rule, and bumped heaven-style to `0.1.1.8`.

## Closeout

- Verification: Skill install/index, scanner, `py_compile`, relative-link check, full and skill-targeted flake, repository tests, environment drift, README drift, and diff/whitespace checks passed. Blueprint reports no tests and exits successfully by design.
- Artifacts: Six rules under `.agents/skills/heaven-style/references/rules/code/typescript/`; survey at `docs/reports/surveys/2026-07-14-typescript-rules-survey.md`; daily closeout at `docs/progress/2026-07-14/README.md`.
- Follow-up: Human review of the survey's source-neutral cross-language candidates before changing Python-wide rules; keep/remove the explicitly marked TypeScript inclusions during that review.
