# Development Log

This rolling log records change, verification, and handoff evidence. New entries go first. Stable behavior belongs in user or engineering documentation. Blueprint is a template source with no live queue, so its newest entry always hands off with `Next: none`; instantiated projects own their own task authority.

## 2026-07-21 — Blueprint 0.1.2.0 release boundary

- Task: direct user request
- Changed: Corrected Blueprint to a queue-free template source with an inert downstream starter, made `heaven-style` task authority conditional on repository role, hardened real-tree initialization and document cleanup, and replaced the obsolete release-branch/PyPI path with an independently verified master tag plus immutable GitHub Release artifacts.
- Verified: The full repository gate passed 39 tests across documentation, skill, template-sync, and real-tree rename contracts; fresh wheel/sdist metadata, isolated installation, package version, `bp`, and `blueprint-gui` smoke checks passed.
- Next: none

## 2026-07-21 — Documentation lifecycle enforcement

- Task: direct user request
- Changed: Established four documentation surfaces, an initial queue contract later corrected to an inert template starter, an expiring scratch lane, a compact deterministic skill index, and reviewed Blueprint-to-HeavenBase synchronization with exact inventory plus adapted-state fingerprints.
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
