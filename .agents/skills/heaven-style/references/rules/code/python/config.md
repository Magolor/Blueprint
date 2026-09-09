---
name: config
description: Define Python configuration, defaults, resources, and provider settings.
---

# Config and resources

## Summary

Configuration is a key/value dictionary owned by the component or repository. Keep changeable defaults in its centralized config service or external resource files whenever practical. Constants in code are for fixed developer facts, not tunable defaults or snapshots of environment variables.

## Principle

Important caller choices stay visible in public signatures. Resolve omitted values once at the owning boundary into a validated runtime spec. Downstream execution should not repeatedly reinterpret raw optionals or read ambient config.

Do not add a configuration framework to an unrelated package solely to follow this skill. Use the owner declared by the target repository.

## Constants versus tunables

Constants are stable developer facts: protocol field names, format markers, mathematical identities, fixed sentinels, or deliberately closed enum values.

Tunables are choices a deployment, project, benchmark, user, or caller may change: provider/model names, routes, dimensions, batch sizes, timeouts, retries, paths, thresholds, ports, cache sizes, and prompt/template text. Store them in the owning config or resource surface and validate them before execution.

## Do

- Identify the repository's config owner from `AGENTS.md`, manifests, nearby source, and tests.
- Keep KV data and lookup as the configuration model. A validated immutable typed spec may carry resolved values into execution; it does not replace the config dictionary or require callers to construct a config class.
- Keep important public overrides explicit. Use `None` for omission when it is not a meaningful value; use `...` (`Ellipsis`) when callers must be able to pass `None`. Resolve only omitted values from the config owner at the call boundary. Preserve explicit `0`, `False`, empty strings, and meaningful `None`.
- Validate and coerce config values once. Then pass resolved values to lower layers.
- Use explicit phases when several sources contribute configuration: **Preset -> Normalize -> Validate -> Apply(profile)**. Each phase has one owner and returns a value suitable for the next. Generic normalization must not absorb provider-, filesystem-, or dialect-specific policy.
- Freeze behavior-changing execution policy into the immutable request/spec identity before caching, retries, serialization, explanation, or execution. Terminal-only flags are valid only when they cannot change the operation's meaning or route.
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

**Anti-pattern:** changeable defaults are frozen into code and bypass central configuration.

```python
MAX_LENGTH = 2048


def embed(
    text: str,
    model: str = "text-embedding-3-small",
    max_len: int = MAX_LENGTH,
    temperature: float = 0.0,
) -> list[float]:
    return _embed(text, model=model, max_len=max_len, temperature=temperature)
```

**Recommended pattern:** illustrative `cfg` is the package's existing KV service, initialized from external defaults and overrides. Its typed lookup validates configured values.

```python
def embed(
    text: str,
    model: str | None = None,
    max_len: int | None = None,
    temperature: float | None = None,
) -> list[float]:
    if model is None:
        model = cfg.get("embed.model", default="text-embedding-3-small")
    if max_len is None:
        max_len = cfg.get("embed.max_len", default=2048)
    if temperature is None:
        temperature = cfg.get("embed.temperature", default=0.0)
    return _embed(text, model=model, max_len=max_len, temperature=temperature)
```

A fallback in `cfg.get` is acceptable; it does not prevent central overrides. Prefer moving changeable fallback values into the external defaults resource too, when practical. Validate caller overrides and resolved domain constraints before `_embed`; lower layers consume the resolved values without rereading ambient config. Native `dict.get` takes its fallback positionally; this project service supports `default=`.

## Package resource example

```python
from importlib.resources import files


prompt = files("acme.resources").joinpath("prompts/embed.txt").read_text(encoding="utf-8")
```

Use the repository's resource helper instead when it explicitly owns this policy.

## Sentinel example

When `None` means “no tag”, use Ellipsis for omission. This sketch assumes the config owner returns a validated `str | None`:

```python
from types import EllipsisType


def fetch(url: str, tag: str | None | EllipsisType = ...) -> bytes:
    if tag is Ellipsis:
        tag = cfg.get("fetch.tag", default=None)
    ...
```

Ellipsis is an API placeholder, not a value to persist in configuration. Keep any repository-required alternative sentinel only for a concrete compatibility constraint.

## Static package resources

Most substantial static/changeable content belongs in resources: default/bootstrap configuration, built-in instance definitions, prompt templates, and seed data. In a modular package system, keep these with the owning package under `resources/` or its established `assets/` folder; no global resource bucket or forced rename is required. Bundle and verify them with the installed/packed package. Keep runtime writable state separate.

This is an ownership preference, not an unconditional ban on every literal, schema declaration, or tiny fixed format marker in code. Preserve language-specific import/resource loading controls. Config data stays KV; typed validation and resolved execution specs can remain code-owned.
