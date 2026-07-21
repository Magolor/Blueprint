---
id: config
title: Config and resources
enabled: true
blocking: true
order: 20
category: code-quality
keywords: [hard-coded, magic number, literals, configuration owner, resources, default, model, timeout, batch size, CM_HVNB]
description: Use when Python code introduces defaults, tunables, prompt or resource paths, model/backend settings, or disputed literals.
---

# Config and resources

## Core rule

Configuration belongs to the component or repository that owns the behavior. Stable library facts may remain constants or typed defaults in code; deployment-, project-, environment-, or user-tunable values belong in the repository's declared configuration system or package resources.

Important caller choices stay visible in public signatures. Resolve omitted values once at the owning boundary into a validated runtime spec; downstream execution should not repeatedly reinterpret raw optionals or read ambient config.

Do not add `CM_HVNB`, HeavenBase, or another configuration framework to an unrelated package solely to follow this skill. When a HeavenBase-lineage repository explicitly declares `CM_HVNB` as the owner, use it for HeavenBase-owned defaults and scopes.

## Constants versus tunables

Constants are stable developer facts: protocol field names, format markers, mathematical identities, fixed sentinels, or deliberately closed enum values.

Tunables are choices a deployment, project, benchmark, user, or caller may change: provider/model names, routes, dimensions, batch sizes, timeouts, retries, paths, thresholds, ports, cache sizes, and prompt/template text. Store them in the owning config or resource surface and validate them before execution.

## Apply when

- Code adds defaults, paths, prompts, templates, provider/backend/model choices, timeouts, retries, thresholds, ports, SQL, or cache sizes.
- A literal may be either a stable invariant or a deployable choice.
- Several layers read the same raw environment/config value or repeat fallback logic.
- Code needs package resources or writable application-state paths.

## Do

- Identify the repository's config owner from `AGENTS.md`, manifests, nearby source, and tests.
- Model related settings as an immutable typed config/spec when that reduces repeated interpretation.
- Keep important public overrides explicit; use `None` or a dedicated sentinel only when omission has distinct meaning.
- Validate and coerce config values once, then pass resolved values to lower layers.
- Load packaged read-only assets through `importlib.resources` or the repository's declared resource API.
- Keep writable user/application state outside installed package resources and resolve it through the owning environment/config policy.
- Keep secrets out of committed defaults and rendered diagnostics.

## Avoid

- Hard-coded deployable choices scattered through execution code.
- Reading environment variables or global config in many downstream functions.
- Making every implementation detail configurable without real change pressure.
- Hiding important caller choices behind ambient global state.
- Treating package-relative filesystem paths as stable when distributions may use another loader.
- Adding a second configuration manager for behavior already owned by the repository's existing one.

## Example

**Anti-pattern:**

```python
def embed(text: str) -> list[float]:
    model = os.environ.get("EMBED_MODEL", "embedding-model")
    batch_size = int(os.environ.get("EMBED_BATCH_SIZE", "32"))
    return _embed(text, model=model, batch_size=batch_size)
```

Every call reinterprets ambient strings and hides the knobs.

**Recommended pattern:**

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class EmbedConfig:
    model: str
    batch_size: int


def embed(text: str, *, config: EmbedConfig) -> list[float]:
    if config.batch_size <= 0:
        raise ValueError("batch_size must be greater than 0")
    return _embed(text, model=config.model, batch_size=config.batch_size)
```

The application boundary owns environment/file/default resolution into `EmbedConfig`; the library function consumes one validated contract.

## Package resource example

```python
from importlib.resources import files


prompt = files("acme.resources").joinpath("prompts/embed.txt").read_text(encoding="utf-8")
```

Use the repository's resource helper instead when it explicitly owns this policy.

## Sentinel example

```python
_UNSET = object()


def fetch(url: str, tag: str | None | object = _UNSET) -> bytes:
    if tag is _UNSET:
        tag = DEFAULT_FETCH_CONFIG.tag
    ...
```

Use a sentinel only when callers must be able to pass `None` intentionally.

## HeavenBase profile

In a repository that explicitly adopts HeavenBase infrastructure, `CM_HVNB` may own shared defaults and scoped overrides, and its resource/path helpers may replace the generic examples above. Verify keys and aliases against that target repository's config tree and tests; illustrative keys are not shipped contracts.

## Related rules

Also apply [util.md](util.md) for path/resource helpers, [types.md](types.md) for typed config contracts, [name.md](name.md) for config key naming, and [format.md](../../project/format.md) for repository commands.
