# Development Log

This rolling log records change, verification, and handoff evidence. New entries go first. Stable behavior belongs in user or engineering documentation; active work belongs only in `docs/tasks.yaml`.

## 2026-09-07 — Clean branches and combined skill 0.1.2.23

- Task: direct user request.
- Changed: Combined the remote theme icons with the local manager, component protocol, and file handoff rules. Removed completed reports and plans. Each product branch now has one root commit. This replaces the earlier two-commit history policy.
- Verified: Both full gates pass: 14 TypeScript tests with package checks and 42 Python tests. Skill validation, index freshness, dependency scan, and byte-identical branch trees pass. The global skill is refreshed. No remote push occurred.
- Recovery: Saved the previous local and remote history in an external Git bundle before the rewrite.
- Next: none

## 2026-09-07 — Canonical six-theme icons 0.1.2.21

- Task: direct user request
- Changed: Standardized theme selectors on the Tabler outline family: Sun for Light, Palette for Colorful, Flame for Warm, Moon for Dark, Atom for Utopia, and Eye for Dystopia. Added reusable SVG assets and the upstream MIT license. The compact Light/Warm/Dystopia switch intentionally gives Dystopia the Dark moon while the six-mode selector uses its Eye.
- Verified: Both full branch gates passed (14 TypeScript tests, packed-package validation, and 42 Python tests). Skill validation, index freshness, standalone dependency scan, SVG parsing, and byte-identical skill trees passed. Reinstalled Heaven Style 0.1.2.21 globally.
- Next: none

## 2026-09-07 — Compact contracts and file-based manager handoffs

- Task: STYLE-002 (closed).
- Changed: Heaven Style 0.1.2.22 gives the architect a short component protocol with attributes, member signatures, and implementation obligations while minimizing public classes. The manager dispatches through files with pinned inputs and owned evidence outputs. Documentation starts with a summary, consumer use, success criteria, and references. Confirmed plan briefs expand into linked execution details.
- Evidence: A bounded DSH manager observation found isolated worktrees and prerequisite blocking, but long dispatch prompts, chat-only final-report instructions, and setup corrections without an assignment-file owner. The observation report and closed plan were removed during the later repository cleanup. No live agent was controlled, and no delivery-performance improvement is claimed.
- Verified: Both full gates pass: 14 TypeScript tests with packed-package checks and 42 Python tests. Skill validation, generated index, standalone scan, script compilation, and strict TypeScript checking of the protocol example pass. Both branches contain the same skill tree; the global installation is refreshed.
- Integration: Local synchronization commits used a temporary hook override for the committed-tree identity bootstrap, followed by both full gates. No remote push occurred.
- Next: none

## 2026-09-07 — Manager delivery responsibility

- Task: direct user request
- Changed: Heaven Style 0.1.2.21 defines the manager as the owner of dependencies, delegated implementation, independent review, serial integration, and verified delivery. Assignments use isolated branches/worktrees and explicit ownership. The manager keeps independent work moving, limits resource contention, delegates heavy execution and detailed review, and resolves cross-slice issues. Existing architecture and external-action authority remain intact.
- Verified: Skill validation, generated index, standalone dependency scan, and script compilation pass. Both complete branch gates pass: 14 TypeScript tests with packed-package validation and 42 Python tests. Skill trees are byte-identical on both product branches; the global installation is refreshed. Updated the two existing Python version expectations.
- Integration: Local synchronization commits used a temporary hook override because the identity gate requires both committed trees; both full gates then ran successfully. No remote push occurred.
- Next: none

## 2026-09-07 — Explicit rule groups and design philosophy

- Task: direct user request
- Changed: Heaven Style 0.1.2.20 names eight rule groups and seven workflows in its entry. Added required, source-backed non-GUI philosophy and aligned TypeScript's owning-object guidance with Python while preserving native stateless functions. Recorded legacy source evidence in the maintenance owner.
- Verified: Both full branch gates passed (14 TypeScript tests, package validation, 42 Python tests). Skill validation, index freshness, standalone scan, 261 local links, full reachability, and six exact palettes passed. Entry: 774 words; largest page: 843. Both product branches and the global installation contain the same skill.
- Next: none

## 2026-09-07 — Required reading restored 0.1.2.19

- Task: direct user correction (closed).
- Changed: Expanded the entry to 561 words with explicit SOLID and OOP/API vocabulary. Code work requires the complete applicable language and shared project rule trees, recursively. Architecture adds every design workflow and code-design comparison. GUI requires all GUI guidance and six palettes. Added a reading procedure that rejects index-only, top-level-only, and truncated reading; unchanged context may be reused within the task. Removed conflicting optional-reading shortcuts from entry, maps, task guides, and maintenance policy.
- Verified: All 123 Markdown pages remain reachable; 243 local links and anchors resolve; all six palette blocks are unchanged; the largest page remains 843 words. Both full gates pass: 14 TypeScript tests with packed-package checks and 42 Python tests. Index freshness and standalone dependency checks pass. The baseline snapshots and two-commit layout are preserved.
- Next: none

## 2026-09-07 — Progressive reading and language alignment 0.1.2.18

- Task: `STYLE-001` (closed).
- Changed: Replaced repeated entry, task, and language catalogs with conditional routes. Split large references by reader decision; added the requested GUI style/theme/techstack hierarchy and six exact palette files. Paired Python and TypeScript API, vocabulary, SOLID, types, files, naming, flow, documentation, comment, error, and configuration topics while preserving native mechanics. Removed redundant workflow text, navigation lists, and a routing-only maintenance alias. Synchronized and installed Heaven Style `0.1.2.18`.
- Measured: Shipped Markdown decreased from 60,229 to 44,834 whitespace-delimited words, including frontmatter and fenced examples. Entry: 3,098 to 361; rule map: 1,422 to 262; task map: 997 to 172; GUI entry: 5,021 to 323. The largest page is 843 words. The corpus now has 122 smaller Markdown pages; the generated index remains below its existing 600-line/20,000-byte bounds. Reference caches, scripts, and the generated index are excluded from the Markdown word comparison.
- Verified: All pages are reachable from the entry; 224 local Markdown links and anchors resolve; all six CSS palettes remain byte-exact. Reviewed retained API-documentation, lifecycle, configuration, compatibility, task-authority, and environment contracts. Skill validation, deterministic index, standalone dependency scan, compilation, and identity of all 129 managed files pass. Full TypeScript gate passes 14 tests and packed-package checks; full Python gate passes 42 tests after updating its two version expectations. Mechanical checks support semantic review and do not measure model performance.
- History: The user requested exactly two commits per product branch: a root snapshot immediately before this refactor and one complete refactor commit. That change preserved each snapshot tree and retained byte-identical skill trees; the later cleanup replaces this history layout. The hosted default remains `typescript`. Initial synchronization used a temporary hook override; both complete gates ran afterward.
- Next: none

## 2026-09-07 — Repository review and publication readiness

- Task: direct user review, commit, and push request (closed).
- Reviewed: Both product branches and their unpublished changes; Heaven Style `0.1.2.17`, environment-asset ownership, machine reporting, branch identity, installed index, and repository gates.
- Fixed: The Python pre-commit hook referenced retired setup scripts and staged obsolete paths. It now calls the current read-only `scripts/check.bash fast` gate without generating or staging unrelated files. Git fixture commands now discard inherited Git environment settings. A regression check verifies that fixture creation preserves the caller repository configuration, index, and branches.
- Verified: Complete TypeScript gate with 14 tests and packed-package checks; complete Python gate with 42 tests; skill dependency scan, installed index freshness, and byte-identical skill trees. Both branches were ahead of origin without divergence at review time. The user authorized publishing both branches.
- Next: none

## 2026-09-07 — Controlled English and environment ownership 0.1.2.17

- Task: `BP-008` (closed).
- Changed: Reviewed and revised all 60 original skill Markdown files using the existing non-certified ASD-STE100-inspired standard. Preserved policy modality, conditions, exceptions, examples, identifiers, and numeric constraints. Reorganized environment assets around the user-selected Setup owner, tracked four non-secret instance guides/snapshots, and removed the blanket instance ignore. The reporter now records unknown probe results without inventing installed tools or running login-shell hooks, bounds each probe, and writes outside the skill by default. Synchronized Heaven Style `0.1.2.17` across both local product branches and reinstalled the common Agent Skill.
- Verified: Preserved 161 code fences, 594 headings, and 413 links outside the intentionally reorganized assets. Frontmatter identities, modal inventory, and numeric constraints pass comparison, apart from the version bump. All 71 tracked skill files are byte-identical across branches. Both full gates pass: 14 TypeScript tests plus packed-consumer checks, and 41 Python tests including four reporter checks. Skill validation, deterministic index, dependency scan, compilation, and installed managed-file identity pass. The two synchronization commits used a temporary hook override because the identity gate requires committed trees on both branches. The Python closeout commit also bypassed its pre-existing hook that references retired `scripts/sync-env.bash`; the declared full gate passed directly. No host provisioning or remote publication was performed.
- Next: none

## 2026-09-07 — GitHub credential recovery 0.1.2.16

- Task: direct user request (closed).
- Changed: Added GitHub repository, PR, and issue authentication recovery with credential precedence, scoped named PAT use, access boundaries, and mutation retry checks. Synchronized Heaven Style 0.1.2.16 across both product branches and refreshed the global installation. Updated Python version assertions.
- Verified: Both complete branch gates pass (14 TypeScript tests plus packed artifact checks; 37 Python tests). Skill validation, deterministic index, dependency scan, compilation, and byte-identical branch trees pass. Used a temporary hook override for the two-branch identity bootstrap, then ran both full gates. No remote was changed.
- Next: none

## 2026-09-02 — Named GUI themes and default slider 0.1.2.14

- Task: direct user request (closed).
- Changed: Named all six GUI themes with short and theme names: Light (Ollama White Grayscale), Colorful (Ollama White), Warm (Anthropic), Dark (GitHub Soft Dark), Utopia (DeepSeek Light), and Dystopia (DeepSeek Dark). Set the default standard three-position slider to Light, Warm, and Dystopia as Dark, while retaining the optional full six-theme dropdown. Bumped Heaven Style to `0.1.2.14`.
- Verified: Canonical skill index and global installation are current; both product branch gates pass; each branch is one clean commit ahead of its remote tip; and the skill trees are byte-identical. The squashed commits used `--no-verify` for the skill identity bootstrap; no remote was changed.
- Next: none

## 2026-08-31 — Three-mode default theme control 0.1.2.13

- Task: direct user request (closed).
- Changed: Added GUI guidance for a compact Light–Warm–Dark three-position slide switch with stable icons, labels, keyboard navigation, and non-color state cues. Added an optional icon-labeled dropdown for the full six-mode palette while preserving one layout, task state, and attention hierarchy.
- Verified: Generated skill index, standalone dependency scan and compilation, formatting/lint/typecheck/tests, package qualification, and byte-identical skill synchronization to both product branches.
- Next: none

## 2026-08-31 — Ollama Light and Color split 0.1.2.12

- Task: direct user request (closed).
- Changed: Split the Ollama family into the default `Light` Ollama White Grayscale mode and an explicit `Color` Ollama White Colorful mode. Kept Dark asymmetric as GitHub Dark, and retained Warm, Utopia, and Dystopia with complete token parity.
- Verified: Official Ollama source review, generated skill index, standalone dependency scan and compilation, formatting/lint/typecheck/tests, package qualification, and byte-identical skill synchronization to both product branches.
- Next: none

## 2026-08-31 — Logical quotation punctuation 0.1.2.10

- Task: direct user request (closed).
- Changed: Synchronized Heaven Style `0.1.2.10` and its Python version assertions. The controlled technical English rule now uses logical quotation punctuation while retaining American English for all other conventions.
- Verified: Skill Creator validation, deterministic indexing, standalone dependency scanning and compilation, both complete branch gates, byte-identical branch skill trees, and the global `0.1.2.10` installation pass. The Python commit used `--no-verify` because its inherited hook still calls a removed environment script; the declared replacement gate passes, and no remote was changed.
- Next: none

## 2026-08-27 — Portable repository governance 0.1.2.9

- Task: `BP-007` (closed).
- Changed: Synchronized the exact Heaven Style `0.1.2.9` tree and Python version assertions. The shared rules now cover concise documentation authority maps, repository-owned decision history, exact external-evidence snapshots with authority limits, one development-log authority, and a one-line Claude Code bridge that keeps `AGENTS.md` authoritative without imposing another project's taxonomy or schema.
- Verified: The complete Python gate passes 37 tests, the TypeScript gate passes 14 tests plus packed-consumer verification, both branches expose byte-identical skill trees, both root `CLAUDE.md` files contain exactly `@AGENTS.md`, and the global common and Claude installations report `0.1.2.9`. History reconstruction used `--no-verify` to cross the dirty-tree identity bootstrap and a stale Python hook reference to removed `scripts/sync-env.bash`; the declared replacement gates pass afterward.
- Next: none

## 2026-08-27 — Heaven Style review communication 0.1.2.7

- Task: direct user request (closed).
- Changed: Made the code-review checklist universal but applicability-based; strengthened first-principles, simplicity, and small-public-interface criteria; added concise guidance for session reports, durable reports, commit and pull-request titles, descriptions, and review comments; and kept other proposed review rules out of scope.
- Verified: Deterministic skill indexing, standalone dependency scanning and compilation, branch skill identity, repository documentation and formatting checks, and the full Python compatibility gate with 37 tests pass.
- Next: none

## 2026-08-26 — Blueprint sanitation and Heaven Style 0.1.2.6

- Task: `BP-006` (closed).
- Changed: Completed all 15 workflow procedures; defined action and task-state contracts; rewrote the TypeScript and Python starters around inert, stateless package boundaries; removed ambient HeavenBase coupling, speculative interfaces, stale artifacts, and tracked machine facts; updated CI and package ownership; and completed a non-certified ASD-STE100 Issue 9 controlled-English review.
- Verified: Deterministic skill indexing and dependency scanning, global installation with preserved local instance notes, 14 TypeScript tests, packed npm consumer checks, 37 Python tests, rename safety, source and wheel builds, distribution metadata, cross-branch skill identity, one-root histories, and public-ref equality pass. Docker remains waived because the local daemon is stopped.
- Next: none

## 2026-08-26 — Source-neutral documentation writing 0.1.2.4

- Task: direct user request.
- Changed: Synchronized the exact Heaven Style `0.1.2.4` tree from the TypeScript product line and updated the Python compatibility assertions. The authored-document route now covers audience outcomes, retrieval-oriented YAML metadata, exact English–Chinese line alignment, evidence-backed operational claims, and non-certified ASD-STE100-inspired prose without expanding existing API-doc, docstring, or inline-comment coverage.
- Verified: The tracked-tree provenance audit reports no reference-repository names, source checkout paths, or project-specific vocabulary. Environment drift checks, deterministic skill indexing, script formatting/lint, the full 29-test Python suite, source and wheel builds, and the cross-branch byte-identity gate pass.
- Next: none

## 2026-08-14 — Python compatibility root 0.1.2.3

- Task: `BP-003` (closed).
- Changed: Preserved the Python-first 0.1.2.3 package as a one-root-commit compatibility branch; added configurable local and GitHub CI enforcement for byte-identical `heaven-style` trees; moved PyPI publishing to manual dispatch from `python`; detached the dirty auxiliary worktree without altering its files or index; and completed the two-branch local/remote transition with `typescript` as GitHub default.
- Verified: The full Python repository gate passes 29 tests; the 0.1.2.3 wheel and source distribution build; configurable valid, remote-divergent, and dirty-tree fixtures exercise the sync gate; both product branches resolve the identical skill tree ID `59c65e67656fc712b595d80de7ba304079177e83`; and GitHub exposes only `python` and `typescript`.
- Next: none

## 2026-08-14 — TypeScript-first Heaven Style 0.1.2.3

- Tasks: direct skill reconciliation request and `BP-001`.
- Changed: Added TypeScript-native utility, API, SQL, and compatibility rules;
  made TypeScript the greenfield default without weakening Python; replaced
  target-project architecture/version/reference coupling with source-neutral
  criteria; made installation offline and target-package-independent; made
  global publication transactional; and made mirrors prune stale managed files
  while preserving explicit local caches and unrelated top-level content.
  Blueprint and the shared skill are synchronized at `0.1.2.3` for the branch
  fork.
- Verified: Deterministic index generation/check, standalone dependency scan,
  script compilation, formatting/lint, environment/README drift, documentation
  contract, installer failure injection and real publication, mirror pruning,
  and the fast repository gate all pass (`26 passed`).
- Next: `BP-003`

## 2026-08-09 — Durable TypeScript configuration guidance 0.1.2.2

- Task: direct user request — synchronize the Blueprint heaven-style skill after the HeavenBase 0.1.2.2 release review.
- Changed: Added the blocking `ts-config` rule for JSON-shaped configuration, detached readonly snapshots, raw-layer precedence, structured path edits, revision-aware async backends, secrets, bootstrap, and runtime-composition boundaries. Routed the rule from the skill entry point, TypeScript architecture, overview, and deterministic index without changing the existing 0.1.2.2 skill version.
- Verified: The packaged reference checkout is detached at HeavenBase release SHA `adf98c7a`; the skill index check, banned-import scan, script compilation, Black/Flake8 gate, generated-environment check, documentation contract, diff check, and all 20 repository tests pass. The 0.1.2.2 skill is installed in the common Agent Skill path and Claude Code plugin bridge; only the Blueprint GitHub push remains ordered after the formal HeavenBase release.
- Next: none

## 2026-07-29 — Local GUI WebView policy 0.1.2.2

- Task: direct user request
- Changed: Replaced heaven-style's React/Tauri desktop default with TypeScript-first `apps/gui/` UI plus a system WebView host; kept TUI in-package beside CLI; documented dual Python/TypeScript services via one OpenAPI contract; preferred Bun and Node 24+ for GUI TypeScript; added `local-gui-layout` example; bumped Blueprint/heaven-style to `0.1.2.2`.
- Verified: Skill install (`--all-harnesses --skip-sync` after reference sync), `index.py --check`, `scan.py`, `py_compile`, flake on skill scripts, `sync-env.bash`, full test gate (20 passed), and `docs.py check` all passed; global `~/.agents/skills/heaven-style` and Claude plugin bridge show `0.1.2.2`.
- Next: `BP-001`

## 2026-07-22 — GUI/UX philosophy 0.1.2.1

- Task: direct user request
- Changed: Finalized heaven-style's attention-first GUI/UX philosophy for new and existing interfaces; preserved the exact Light, Dark, and Warm palette; made element unity, relational spacing, restrained motion, and convergent maintenance explicit; and published design-only HeavenBase and ParaDev improvement advice.
- Verified: Skill validation, deterministic index, scan, compilation/lint, documentation and generated-environment checks, global all-harness installation, the full repository gate (20 tests), `0.1.2.1` wheel/sdist metadata, and the `bp --help` smoke all passed; canonical theme declarations remained unchanged.
- Next: `BP-001`

## 2026-07-21 — Standalone Blueprint workflow

- Task: direct user request
- Changed: Removed the downstream HeavenBase consumer policy, synchronization tool, tests, and pre-push gate so Blueprint validation and publishing no longer depend on another checkout or branch.
- Verified: Pending the repository fast gate and push.
- Next: `BP-001`

## 2026-07-21 — Documentation lifecycle enforcement

- Task: direct user request
- Changed: Established four documentation surfaces, one task queue, an expiring scratch lane, a compact deterministic skill index, and reviewed Blueprint-to-HeavenBase synchronization with exact inventory plus adapted-state fingerprints.
- Verified: The offline fast gate passed documentation, skill graph, template coverage, formatter/lint, and 26 positive/negative contract tests; the skill scan, compilation, generated environment, and README drift checks passed separately.
- Next: `BP-001`

## 2026-07-20 — Extension parity guidance

- Task: direct
- Changed: Made Lego-style extension parity source-neutral and portable while preserving the `0.1.2.0` no-bump waiver.
- Verified: Skill index, scan, compilation, lint, environment drift, and global installation passed.
- Next: `BP-001`

## 2026-07-14 — TypeScript and service guidance

- Task: direct
- Changed: Added language-selected TypeScript rules and a service-interface architecture rule; kept repository toolchain policy authoritative.
- Verified: Index, local-link, scan, compilation, lint, environment, and README checks passed.
- Next: none

## 2026-06-27 — Initial documentation governance

- Task: direct
- Changed: Introduced goals, plans, resources, reports, and dated progress artifacts; this entry supersedes the dated progress directory after the single-log migration.
- Verified: README, environment, skill-index, scan, lint, and package checks passed at the time.
- Next: none
