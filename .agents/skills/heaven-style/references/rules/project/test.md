---
id: test
title: Tests and examples
enabled: true
blocking: true
order: 110
category: project
keywords: [pytest, Bun test, unit test, contract test, property test, type test, fast test, full test, test marker, packed consumer, runnable example, coverage, happy path, edge case, error path]
description: Use when adding or reviewing Python or TypeScript behavior tests, runnable examples, type/contract/property checks, package smoke tests, integration evidence, or provider tests.
---

# Tests and examples

## Core rule

Behavior changes need focused verification through the repository entrypoint. Start targeted, broaden according to risk and repository-defined tiers/tags, and cover the happy path, one meaningful edge case, and one failure path unless the behavior makes one inapplicable and the waiver is explicit.

In Blueprint/HeavenBase Python repos, keep pytest suites intentionally limited and marker-gated: use `fast` for daily checks, reserve `full` for large PR merge or release validation, and add narrower markers such as `unit`, `integration`, `slow`, `provider`, or `db` when they clarify cost or dependency. TypeScript repos use their declared runner/scripts and [TypeScript environment](../code/typescript/environment.md), not pytest vocabulary.

## Apply when

- Code changes behavior, provider routes, integrations, public APIs, examples, or smoke checks.
- Test coverage, LLM/provider/database/MCP evidence, or no-mock policy is under discussion.

## Do

- Put tests in repository-declared locations; feature-local TypeScript tests and a central Python `tests/` tree are both valid when they match the package convention.
- Start with targeted tests or a smoke probe for touched behavior.
- In Python repos that define them, tag tests with `fast`/`full` or clearer project categories so agents can run the useful subset instead of the whole suite by default.
- Prefer targeted or repository-defined fast runs for daily feature sessions; run the full suite only for broad refactors, large PR merge gates, release gates, or when touched behavior needs it.
- Run broader repo scripts/wrappers before completion; follow [environment.md](environment.md) for repository command policy.
- For TypeScript, add type tests for complex public generic contracts, reusable contract suites for multiple implementations, property tests for parsers/round trips/invariants, and packed-consumer smoke tests for published packages when those risks exist. Do not add every layer mechanically.
- For an open extension family, run one reusable contract suite against bundled and external implementations. Add an extraction test proving a bundled implementation can move to an independently registered artifact without changing consumer-facing tests.
- Verify durable registration/refresh, deterministic conflicts and version selection, and descriptor inspection without implementation import when the Registry promises those behaviors.
- Keep runnable examples small and route runtime output to the repo's declared temp folder.
- Follow `AGENTS.md` for model, cost, credentials, and no-mock policy.

## Avoid

- Generic `test_works` coverage.
- Oddly specific, legacy, duplicated, or implementation-detail tests that freeze non-contract behavior.
- Running every full, slow, provider, or external-dependency test on every agent feature session when a targeted or fast check covers the changed behavior.
- Documenting provider/backend support before a real route is exercised or explicitly waived.
- Example-generated runtime data outside the declared temp folder.
- Extension tests that exercise only the bundled import path while external discovery, persistence, loading, or provenance takes another route.

## Example

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

## Blueprint/Python verification commands

```bash
rtk bash scripts/test.bash tests/test_<area>.py -q
rtk bash scripts/test.bash -m "fast and not full" -q
rtk bash scripts/test.bash -m full
rtk bash scripts/test.bash
```

An empty `tests/` directory is valid when the repo has not added tests yet; the wrapper should exit successfully with a no-tests message.

Use repo wrappers for external-database, LLM, full-marker, or slow-marker suites; read `AGENTS.md` for marker and model policy.

## TypeScript verification

Use the target repository's declared scripts. For a Bun repo, run a focused `rtk bun test <path-or-pattern>` while iterating, then its `rtk bun run test` or aggregate `rtk bun run check` gate. Typechecking, linting, package packing, and consumer smoke tests are separate evidence; a green runtime test does not replace them.

## Related rules

Also apply [environment.md](environment.md) for command entrypoints, [format.md](format.md) for lint/format gates, [TypeScript environment](../code/typescript/environment.md) for Bun/type/package checks, [docs.md](docs.md) when examples affect docs, and [review.md](review.md) for completion gates.
