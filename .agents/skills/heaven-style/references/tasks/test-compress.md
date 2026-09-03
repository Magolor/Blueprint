---
id: test-compress
task_kind: test-compress
status: active
enabled: true
order: 34
keywords: [test compression, compress tests, prune tests, TypeScript tests, Bun test, pytest cleanup, legacy tests, test tiers, test markers, suite cleanup]
triggers: [test-compress, compress tests, prune tests, cleanup tests, reduce tests, slim tests, test suite cleanup]
description: Use when auditing and slimming a TypeScript or Python test suite by removing oddly specific, legacy, low-value, brittle, or redundant tests while preserving meaningful behavior coverage.
related_rules: [overview, test, ts-api, ts-compat, clean, model, compat, environment, format, docs, review]
---

# Test Compress Task

## Goal

Turn an overgrown TypeScript or Python test suite into a compact, maintainable coverage set that protects public behavior, important bugs, and meaningful edge/error paths without freezing incidental implementation details.

## Fast Path

1. Read repo `AGENTS.md`, [test.md](../rules/project/test.md), the declared test scripts/configuration, package/runtime metadata, and any named issue/plan/report before editing tests.
2. Inventory repository-declared test locations with `rg --files` and group tests by module, behavior contract, cost, dependency, runtime, and tier/tag status.
3. Classify each cluster as keep, merge, retag, rewrite, or drop. Keep behavior-contract tests, durable regression tests, user-facing edge/error coverage, and integration routes that prove a real supported path.
4. Drop or rewrite tests that only assert old internals, migration leftovers, arbitrary fixture details, incidental order/timing, duplicated branches, overly narrow snapshots, generic `test_works` claims, or unsupported legacy behavior.
5. Keep test code modular and generic: share focused fixtures/factories, parametrize equivalent cases, assert observable outcomes, and avoid test names or assertions that describe non-specified behavior.
6. Preserve the repository's declared test tiers. TypeScript may use package scripts, file globs, projects, tags, or runner configuration; Python may use pytest markers such as `fast`, `full`, `unit`, `integration`, `slow`, `provider`, or `db`. Do not impose one language's tier mechanics on the other.
7. Run targeted or daily-tier tests first, then broader or release-tier validation only when compression touches broad behavior, public contracts, package boundaries, large PR gates, or release gates.

## Keep Criteria

- Public API contracts, CLI behavior, documented examples, and stable config/resource behavior.
- Regression tests for real bugs that could plausibly recur.
- One representative happy path, edge case, and error path per behavior surface.
- Integration/provider tests that prove supported routes and are classified by cost/dependency through the repository's declared mechanism.
- Type-level or packed-consumer tests that protect a published TypeScript contract not observable from source-only runtime tests.

## Drop Criteria

- Oddly specific expectations about private helper calls, fixture shape, object identity, timing, ordering, or serialized whitespace when those details are not contractual.
- Legacy compatibility behavior that the current docs, APIs, and release policy no longer support.
- Redundant tests whose meaningful assertion is already covered by a clearer test at the same or higher behavioral level.
- Low-value generated snapshots or broad smoke tests that pass without proving a contract.

## Completion Gate

Do not mark done until the retained suite has clear tier/tag ownership, deleted tests are justified by non-contract or redundant status, targeted daily tests pass, and any skipped broad validation is explicitly waived with the reason. For substantial suite compression, save the keep/drop rationale in a linked plan or review/refactor report and summarize closure in the development log.

## Verification Commands

Use the scripts declared by the target repository. A Bun-based TypeScript repository commonly uses:

```bash
rtk bun test <target>
rtk bun run test
rtk bun run check
```

A marker-gated Python repository may use:

```bash
rtk bash scripts/test.bash tests/<target> -q
rtk bash scripts/test.bash -m "fast and not full" -q
rtk bash scripts/test.bash -m full
```

Run the whole-suite or aggregate gate when broad confidence is needed for a large PR merge, release, public package change, or sweeping test rewrite.

## Output

Report the number and kind of tests kept, merged, reclassified, rewritten, and dropped; the tier/tag policy now supported by the suite; verification commands; and any broad-suite waiver.
