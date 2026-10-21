# Development Log

This log records current alpha preparation. Earlier development history remains in the preserved baseline and local history backup.

## 2026-10-21 — Keep Colorful on the Light neutral frame

- Task: none — direct.
- Changed: Design-system revision 5 supersedes the revision-4 Cloud Dancer surface. Colorful now keeps Light's complete Ollama white frame — canvas, surfaces, borders, text, labels, muted text, and code surfaces — and changes only the MUI interaction and status accents plus the Material Design 2 chart colors. Cloud Dancer is removed. Dashboard, HeavenBase-2, and Heaven Style share the revision-5 palette resource. Preserved the version freeze.
- Verified: Skill palette pages match the Dashboard and HeavenBase-2 resources token-for-token; TypeScript and Python full gates, skill indexing, documentation, and branch parity are checked after the shared skill tree is synchronized.
- Next: none

## 2026-10-21 — Unify the six palettes on Material Colorful

- Task: none — direct.
- Changed: The six presets are one shared 50-token contract for Dashboard, HeavenBase-2, and Heaven Style. Colorful copies Light's Ollama white theme, replaces its secondary white surfaces with Pantone Cloud Dancer `#F0EEE9`, and then takes the Material interaction and status accents and the Material Design 2 chart colors; text, labels, borders, and syntax remain the Light values, with `--muted` darkened one step for 4.5:1 on Cloud Dancer. The theme guide now names design-system revision 4. Preserved the version freeze.
- Verified: Skill palette pages match the Dashboard and HeavenBase-2 resources token-for-token; TypeScript and Python full gates, skill indexing, documentation, and branch parity are checked after the shared skill tree is synchronized.
- Next: none

## 2026-10-21 — Restore the pre-revision-2 GUI palettes

- Task: none — direct.
- Changed: Heaven Style returns to the pre-revision-2 Colorful palette and four audited token values. Colorful keeps the white Ollama canvas with its teal accent, colorful option accents, and GitHub-like syntax colors; Light returns to `--muted: #6f6f6f`, while Dark, Utopia, and Dystopia return their code-gutter text colors. The theme guide now names design-system revision 3. Dashboard deliberately keeps its revision-2 beige Colorful palette and documents that difference. Preserved the version freeze.
- Verified: Palette pages match the HeavenBase-2 resource token-for-token; TypeScript and Python full gates, skill indexing, documentation, and branch parity are checked after the shared skill tree is synchronized.
- Next: none

## 2026-09-29 — Consolidate current alpha history

- Task: RELEASE-003.
- Changed: Preserved each branch's original root and consolidated the current alpha into one commit per branch. Saved the earlier Git history and release files in a verified backup outside the product trees. Aligned the Chinese installer text with the Python README. Kept the frozen versions and the unrelated `v0.1.2.0` tag.
- Verified: Both branch release gates, two-commit ancestry, shared Heaven Style parity, and source archive checksums passed.
- Next: none

## 2026-09-29 — Align Heaven Style GUI guidance

- Task: BP-001.
- Changed: Matched all six GUI palette maps to Dashboard's accepted preset resource; aligned theme controls, geometry, typography, localization, and browser/desktop composition guidance. Kept the frozen version and shared skill tree.
- Verified: Palette comparison, skill index/scan/compile checks, both branch gates, branch parity, and byte comparison of the 207 installed skill files passed.
- Next: none

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
