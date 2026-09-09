# Development Log

This log records current alpha preparation. Earlier development history remains in the preserved baseline and local history backup.

## 2026-09-09 — Consolidate corrected alpha release

- Task: RELEASE-002.
- Changed: Consolidated the alpha and style corrections into one release commit above each preserved branch root. Updated bilingual changelogs and guarded replacement instructions. Retained a recovery bundle and original release assets outside the product tree. Removed machine-specific source locators from the historical survey.
- Verified: Both release-preparation gates passed, including 16 TypeScript tests, 44 Python tests, packed TypeScript consumption, and installed Python wheel/CLI checks. Both branches retain the identical 207-file skill tree. GitHub prerelease tags and checksums own the final published commit and archive identity.
- Next: none

## 2026-09-09 — Apply maintainer code-style decisions

- Task: STYLE-003.
- Changed: Added vocabulary folders for paired verbs, explicit nouns, and aliases; preferred single/multiple input on one operation. Aligned utility ownership and clean-rule discovery, logical error guards, compact code, stable-prefix imports, named arguments, ORM-first SQL, package resource guidance, one live API, and Python Black + Flake8. Preserved full Python docstrings, modern typing, native TypeScript controls, and the version freeze. Recorded decisions in the TypeScript branch survey.
- Verified: Both full gates passed (16 TypeScript tests and packed consumer; 44 Python tests). Skill metadata/index validation passed, all 207 tracked skill files match across product branches, and the global installation was refreshed. Rule examples are illustrative; no new database/tooling dependency was introduced.
- Next: none

## 2026-09-09 — Restore object ownership and expand SOLID

- Task: STYLE-002.
- Changed: Strengthened the minimal user mental model with domain-owned member methods and construction/conversion examples. Added SRP, OCP, LSP, ISP, and DIP pages with patterns and anti-patterns for both languages; preserved the version freeze. Compared legacy AgentHeaven, 0.1.2.0, 0.1.2.23, and the alpha release in a decision survey; 22 remaining proposals were not applied.
- Verified: Both full gates passed (16 TypeScript tests and packed consumer; 44 Python tests). Skill metadata/index validation passed; both branches have the same 200-file skill tree, and the global installation was refreshed. SOLID examples are labeled illustrative sketches.
- Next: none

## 2026-09-09 — Restore Heaven Style design conventions

- Task: STYLE-001.
- Changed: Restored external packaged SQL with parameter binding, preferred `fromJson`/`toJson` with equivalent uppercase aliases, KV configuration with externalizable defaults and explicit omission semantics, and package-owned utilities with shared placement for needed generic helpers. Corrected adjacent rules and examples. Kept the version frozen.
- Verified: TypeScript full gate passed (16 tests and packed artifact); Python full gate passed (44 tests). Config and JSON snippets passed focused override, falsy-value, omission, alias, and failure checks. Skill validation and index checks passed. Committed skill trees are byte-identical on both product branches; the global installation was refreshed. SQL examples are illustrative driver/resource contracts, not a live database integration test.
- Next: none

## 2026-09-09 — Alpha template finalization

- Task: RELEASE-001.
- Changed: Finalized the current starter and Heaven Style guidance, community documents, template archive preparation, and meaningful test coverage. Retained one native package per product branch.
- Verified: Both full gates passed (16 TypeScript tests; 44 Python tests), with packed-package and installed-wheel smoke checks. Seven bilingual document pairs passed structural checks. Current source passed the unrelated-reference audit. All 190 tracked skill files match across both branches and the local installation. A verified recovery bundle preserves unsquashed history outside the repository.
- Next: none
