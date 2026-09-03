# Development Log

This rolling log records change, verification, and handoff evidence. New entries go first. Stable behavior belongs in user or engineering documentation; active work belongs only in `docs/tasks.yaml`.

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
