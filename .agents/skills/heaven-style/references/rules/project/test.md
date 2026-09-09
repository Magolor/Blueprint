---
name: test
description: Design meaningful tests, integration evidence, and repository test tiers.
---

# Tests and examples

## Summary

Behavior changes need focused verification through the repository entry point. Start with targeted checks. Broaden them according to risk and repository-defined tiers/tags. Cover the happy path, one meaningful edge case, and one failure path unless the behavior makes one inapplicable and the waiver is explicit.

## Principle

TypeScript repos use their declared runner/scripts and [TypeScript environment](../code/typescript/env.md); package scripts, file/project boundaries, tags, type tests, and packed-consumer checks define their tiers. Python repositories use their declared pytest markers or test tiers. When introducing tiers, prefer a small daily set plus clearly named integration, provider, platform, slow, or release groups rather than one undifferentiated suite.

## Apply when

- Code changes behavior, provider routes, integrations, public APIs, examples, or smoke checks.
- Test coverage, LLM/provider/database/MCP evidence, or no-mock policy is under discussion.

## Do

- Put tests in repository-declared locations; feature-local TypeScript tests and a central Python `tests/` tree are both valid when they match the package convention.
- Start with targeted tests or a smoke probe for touched behavior.
- In TypeScript, add type tests for complex public generic contracts, reusable contract suites for multiple implementations, property tests for parsers/round trips/invariants, and packed-consumer smoke tests for published packages when those risks exist. Do not add every layer mechanically.
- In Python repos that define them, tag tests with `fast`/`full` or clearer project categories so agents can run the useful subset instead of the whole suite by default.
- Prefer targeted or repository-defined daily-tier runs for feature sessions; run the broad/release suite only for cross-cutting refactors, large PR merge gates, release gates, or when touched behavior needs it.
- Run broader repo scripts/wrappers before completion; follow [environment](environment.md) for repository command policy.
- Put at least one risk-appropriate deterministic behavior tier on pull requests. Keep expensive provider/platform matrices for broader gates, but do not reduce PR evidence to formatting alone when executable behavior changed.
- For validators, schemas, generators, and policy checkers, keep a valid golden fixture plus invalid fixtures for the important rejected states. A validator that accepts its negative fixture fails the suite.
- Test import cost and optional-dependency isolation in a fresh subprocess when lazy public imports, plugins, providers, or process-global initialization are part of the contract.
- For an independently extensible family, run one reusable contract suite against bundled and packed external implementations when the product promises that parity.
- Verify durable registration/refresh, deterministic conflicts, version selection, and inert descriptor inspection only when the extension system promises those behaviors.
- Keep runnable examples small. Route runtime output to the repository's declared temp folder.
- Follow `AGENTS.md` for model, cost, credentials, and no-mock policy.

## Avoid

- Generic `test_works` coverage.
- Oddly specific, legacy, duplicated, or implementation-detail tests that freeze non-contract behavior.
- Running every broad, slow, provider, or external-dependency test on every agent feature session when a targeted or daily-tier check covers the changed behavior.
- Documenting provider/backend support before a real route is exercised or explicitly waived.
- Treating a capability declaration, registered handler, generated table, or coverage percentage as proof that the concrete runtime route works.
- Example-generated runtime data outside the declared temp folder.
- Extension tests that exercise only the bundled import path while external discovery, persistence, loading, or provenance takes another route.

## Example

**TypeScript anti-pattern:**

```ts
test('works', async () => {
  expect(await run('ok')).toBeTruthy()
})
```

**TypeScript recommended pattern:**

```ts
test('run returns the result for valid input', async () => { /* ... */ })
test('run accepts an empty optional collection', async () => { /* ... */ })
test('run rejects an unknown mode', async () => { /* ... */ })
```

**Python anti-pattern:**

```python
def test_works():
    assert run("ok")
```

**Python recommended pattern:**

```python
def test_run_happy_path(): ...
def test_run_empty_input(): ...
def test_run_unknown_mode_raises(): ...
```

Python runnable examples start with an `Objective:` docstring when the target repo requires it. TypeScript examples follow the target documentation/test harness and do not copy this Python convention.

## TypeScript verification

Use the target repository's declared scripts. For a Bun repository, run a focused `rtk bun test <path-or-pattern>` while iterating. Then run its `rtk bun run test` or aggregate `rtk bun run check` gate. Typechecking, linting, package packing, and consumer smoke tests provide separate evidence. A successful runtime test does not replace them.

## Python verification examples

```bash
rtk bash scripts/test.bash tests/test_<area>.py -q
rtk bash scripts/test.bash -m "fast and not full" -q
rtk bash scripts/test.bash -m full
rtk bash scripts/test.bash
```

Use repo wrappers for external-database, LLM, full-marker, or slow-marker suites; read `AGENTS.md` for marker and model policy.
