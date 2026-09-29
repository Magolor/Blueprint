---
name: py-doc-format
description: Read when formatting Python docstrings or documenting argument modes.
---

# Python docstring format

## Summary

State argument semantics and use consistent Google-style sections with renderer-compatible markup.

## Argument descriptions

Write each `Args` entry like a tiny docstring:

- Start with a very short role phrase or sentence that explains what the argument means to the caller.
- Add details only when they affect correct use: allowed ranges, units, defaults not obvious from the signature, path/resource expectations, side effects, warnings, or interactions with other arguments.
- For numeric arguments, state units and inclusive/exclusive bounds when they matter.
- For boolean arguments, explain the enabled behavior. Avoid tautologies such as "Whether to enable strict".
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

When the same literal set appears across multiple public functions, document the full list once on the main exposed API, owning class, or shared `*Config`/`*Spec`. Secondary APIs should reference that owner by code span, for example "Uses the `CheckScope` values documented on `ProjectChecker.run`". Use Markdown cross-reference links such as `[ProjectChecker.run][package.ProjectChecker.run]` only when the docs renderer supports them. Otherwise, keep the reference as plain code spans.

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

## Markdown in docstrings

Use the target documentation renderer's markup. When the repo has no local convention, prefer Markdown inside Google-style docstrings because modern auto-documentation stacks such as mkdocstrings and pdoc parse Google-style sections while rendering Markdown-oriented prose.

- Use single backticks for inline identifiers, values, env vars, paths, and short code spans: `ProfileSpec`, `None`, `APP_CONFIG`, and `config/default.yml`.
- Use fenced code blocks in `Examples`, with a language when useful. This is the default for Markdown-oriented API docs because it preserves syntax highlighting and reads like normal documentation:

````python
Examples:
    ```python
    project = pkg.Project.load("shop")
    project.register(Product)
    ```
````

- Use doubled backticks only when the local docs pipeline is Sphinx/reStructuredText and nearby docs already use that convention, or when Markdown requires a longer backtick fence to include literal backticks inside a code span.
- Use `>>>` prompts only for doctest-style examples that the repo intends to execute with `doctest` or display as an interactive REPL transcript.
- Prefer Markdown links only when the docs renderer supports them. Otherwise use code spans for Python names and keep URLs in surrounding docs.
- Avoid Markdown headings inside function docstrings; the Google-style section names are the structure.
- Avoid raw HTML, tool-specific roles, or complex tables in docstrings unless the target docs pipeline already requires them.
