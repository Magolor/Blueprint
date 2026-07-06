---
id: docstring
title: Docstrings
enabled: true
blocking: true
order: 27
category: code-quality
keywords: [docstring, Google-style, Args, Returns, Yields, Raises, markdown, public API, documentation]
description: Use when adding or reviewing public API docstrings, major feature APIs, generator docs, return docs, examples, warnings, or Markdown markup inside Python docstrings.
---

# Docstrings

## Core rule

Every publicly exposed function, method, classmethod, staticmethod, generator, and major feature API must have complete type annotations and a full Google-style docstring. The docstring starts with a one-line feature summary, then optional explanatory paragraphs, then `Args` and `Returns` or `Yields` sections. Include those sections explicitly even when there are no arguments or the function returns `None`.

## Apply when

- Code adds or changes a public function, method, classmethod, staticmethod, generator, plugin hook, CLI/API entrypoint, or major feature API.
- Code exports a symbol through `__init__.py`, `__all__`, a public facade, examples, README/API docs, or stable extension points.
- Code changes argument types, return types, exceptions, side effects, examples, warnings, or generated API documentation.
- A private helper is large enough that future users may treat it as a feature boundary.

## Do

- Put full annotations in the signature for every public parameter and return value, including `-> None`.
- Keep docstring types aligned with the signature using standard Python annotation spelling: `name (type): ...`; under `Returns` and `Yields`, start the indented line with `type: ...`.
- Start with one concise sentence that names the user-visible feature. End the summary with punctuation.
- Add optional description paragraphs only when they explain caller-visible behavior, side effects, constraints, or mental model.
- Always include `Args`. When there are no caller-provided arguments, write `None.` as the section body. Do not document `self` or `cls`.
- Use `Returns` for normal functions and `Yields` for generators or async generators. Functions returning iterators still use `Returns`.
- For `None` returns, write `None: This function does not return a value.` or a more specific side-effect statement.
- Document `Raises` when callers can trigger or handle the exception. Prefer project exception names or contextual `raise_mismatch` behavior over broad exception families.
- Use `Warnings`, `Notes`, or `Examples` when they change safe usage, explain important caveats, or show realistic public flows.
- Keep examples short, runnable in spirit, and aligned with public imports such as `import heavenbase as hb`.

## Argument descriptions

Write each `Args` entry like a tiny docstring:

- Start with a very short role phrase or sentence that explains what the argument means to the caller.
- Add details only when they affect correct use: allowed ranges, units, defaults not obvious from the signature, path/resource expectations, side effects, warnings, or interactions with other arguments.
- For numeric arguments, state units and inclusive/exclusive bounds when they matter.
- For boolean arguments, explain the enabled behavior and avoid tautologies such as "Whether to enable strict."
- For `Literal[...]`, enum-like strings, constrained integers, or mode arguments, always list every supported value and explain each one, even when the type annotation names them.

```python
def run_checks(scope: Literal["fast", "full"], *, timeout_s: int = 30) -> CheckReport:
    """Run validation checks for the current project.

    Args:
        scope (Literal["fast", "full"]): Validation depth.
            Supported values:
            - `fast`: Run deterministic checks intended for daily development.
            - `full`: Run the full release-gate suite, including slow checks.
        timeout_s (int): Maximum runtime in seconds. Must be greater than 0.

    Returns:
        CheckReport: Validation result with command output and failure metadata.
    """
```

When the same literal set appears across multiple public functions, document the full list once on the main exposed API, owning class, or shared `*Config`/`*Spec`. Secondary APIs should reference that owner by code span, for example "Uses the `CheckScope` values documented on `ProjectChecker.run`." Use Markdown cross-reference links such as `[ProjectChecker.run][package.ProjectChecker.run]` only when the docs renderer supports them; otherwise keep the reference as plain code spans.

## Indentation

Use normal Python docstring indentation plus Google-style section indentation:

- Indent the triple-quoted docstring with the function or method body.
- Put the one-line summary immediately after the opening `"""`.
- Align description paragraphs and section headers such as `Args:`, `Returns:`, `Yields:`, and `Raises:` with the summary text.
- Indent section entries by 4 spaces under the section header.
- For multi-line parameter, return, yield, or exception descriptions, use a hanging indent 4 more spaces under the entry line.
- Keep blank lines between the summary, optional description paragraphs, and each major section.

```python
def render_report(path: str, *, title: str | None = None) -> Report:
    """Render a report from a Markdown source file.

    Args:
        path (str): Markdown source path.
        title (str | None): Optional display title. When omitted, the renderer
            derives the title from the first Markdown heading.

    Returns:
        Report: Rendered report object with resolved metadata.
    """
```

## Avoid

- Omitting `Args`, `Returns`, or `Yields` on public APIs because the signature looks obvious.
- Relying on type hints alone when the public API contract needs caller-readable semantics.
- Weakening docstring types compared with the signature, such as documenting `dict` when the signature uses `ProfileSpec`.
- Repeating implementation steps that callers do not need to know.
- Listing `self` or `cls` in `Args`.
- Mixing Google-style, NumPy-style, and Sphinx `:param:` sections in the same project surface.
- Adding full boilerplate docstrings to tiny private helpers that are easier to read directly.

## Markdown in docstrings

Use the target documentation renderer's markup. When the repo has no local convention, prefer Markdown inside Google-style docstrings because modern auto-documentation stacks such as mkdocstrings and pdoc parse Google-style sections while rendering Markdown-oriented prose.

- Use single backticks for inline identifiers, values, env vars, paths, and short code spans: `ProfileSpec`, `None`, `CM_HVNB`, and `config/default.yml`.
- Use fenced code blocks in `Examples`, with a language when useful. This is the default for Markdown-oriented API docs because it preserves syntax highlighting and reads like normal documentation:

````python
Examples:
    ```python
    ws = hb.HeavenBase.load("shop")
    ws.register(Product)
    ```
````

- Use doubled backticks only when the local docs pipeline is Sphinx/reStructuredText and nearby docs already use that convention, or when Markdown requires a longer backtick fence to include literal backticks inside a code span.
- Use `>>>` prompts only for doctest-style examples that the repo intends to execute with `doctest` or display as an interactive REPL transcript.
- Prefer Markdown links only when the docs renderer supports them. Otherwise use code spans for Python names and keep URLs in surrounding docs.
- Avoid Markdown headings inside function docstrings; the Google-style section names are the structure.
- Avoid raw HTML, tool-specific roles, or complex tables in docstrings unless the target docs pipeline already requires them.

## Examples

### Public function

**Recommended pattern:**

```python
def load_profile(path: str, *, strict: bool = True) -> Profile:
    """Load a profile from a JSON file.

    Args:
        path (str): Filesystem path to the profile JSON file.
        strict (bool): Whether to reject unknown fields.

    Returns:
        Profile: Loaded profile object.

    Raises:
        ProfileError: If the file cannot be decoded or validated.
    """
```

### No arguments and no return value

**Recommended pattern:**

```python
def reset_cache() -> None:
    """Clear cached registry state.

    Args:
        None.

    Returns:
        None: This function does not return a value.
    """
```

### Generator

**Recommended pattern:**

```python
from collections.abc import Iterator


def iter_rows(limit: int | None = None) -> Iterator[Row]:
    """Yield rows from the active result set.

    Args:
        limit (int | None): Maximum number of rows to yield.

    Yields:
        Row: Next row in query order.
    """
```

## Class and property notes

Public classes need a one-line class summary and enough description to explain the object model. Document constructor parameters either in the class docstring or `__init__`, but not both. Public properties may use attribute-style docstrings when an `Args` section would be meaningless; public property setters and feature methods still follow the full function rule.

## Related rules

Also apply [types.md](types.md) for annotation spelling, [model.md](model.md) for public API surface size, [oop.md](oop.md) for method vocabulary, [name.md](name.md) for symbols, and [docs.md](../../project/docs.md) for generated documentation sync.
