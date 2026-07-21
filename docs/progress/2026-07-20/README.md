# 2026-07-20 Progress

## Lego-Style Extension Parity

- Summary: Promoted the confirmed Lego-style extension criterion into heaven-style and made the skill's Python baseline portable to ordinary packages rather than implicitly requiring HeavenBase infrastructure.
- Decisions: Treat “global” as one authoritative logical catalog per declared Context/environment rather than a mutable process singleton; resolve only declared extension families through the Registry; keep ordinary Python imports ordinary; separate discovery, registration, acquisition, loading, activation, and runtime caching; require identical built-in/external paths plus an extraction fitness test.
- Skill touch: Updated `SKILL.md`, the owning `extension` rule, Python infrastructure/organization/SOLID/API rules, project test/format guidance, TypeScript extension seams, architecture/developer/editor workflows, update/version guidance, scanner wording, and the generated index.
- Generic Python boundary: Target-repository infrastructure owners win. With no owner, use standard-library or established dependency APIs directly; never add HeavenBase solely to comply with the skill. HeavenBase utilities/config/database conventions are now an explicit lineage profile.
- Version: Applied the user's explicit no-bump waiver; all skill version metadata remains exactly `0.1.2.0`.
- Verification: Generated index check, Python byte-compilation, Blueprint scanner, `scripts/flake.bash --ci`, `scripts/test.bash`, `scripts/sync-env.bash --check`, targeted diff checks, and the standard global installation at `~/.agents/skills/heaven-style` passed.
- Artifact: `docs/plans/2026-07-20-lego-style-extension-parity.md` is closed as Done.

## HeavenBase Refactor Route

- Summary: Audited the HeavenBase `dev-refactor` checkout read-only and designed a detailed migration from process/fixed-import registries to a persisted, source-neutral component catalog.
- Key finding: The current persistent Registry depends on the selected HeavenBase data Backend plus concrete schema/type/strategy components, while the desired component catalog must exist before that Backend can be resolved. A small stdlib-only `RegistryStore` kernel is therefore the first required implementation slice.
- Route: `docs/plans/2026-07-20-heavenbase-lego-style-extension-refactor.md` specifies contracts, bootstrap order, public developer flow, ten delivery slices, file/test targets, stop conditions, rollback behavior, security policy, documentation updates, and the final built-in extraction gate.
- Scope control: No HeavenBase source file was changed. Built-in manifests will be compiled into a packaged seed and ingested through the same catalog/loader as external bundles; runtime will not scan privileged package folders.
- Next: In HeavenBase, execute Slices 0–3 first: accept the ADR and black-box fitness tests, decouple Registry persistence, add ComponentSpec/BundleSpec/catalog contracts, then prove out-of-tree resolution and activation before migrating domain families.
