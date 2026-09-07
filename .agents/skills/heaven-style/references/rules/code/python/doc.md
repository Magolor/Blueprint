---
id: docstring
title: Docstrings
blocking: true
description: Write public Python Google-style docstrings and complete annotations.
---

# Python API documentation

Public functions, methods, classmethods, staticmethods, generators, plugin hooks, CLI/API entrypoints, and major feature APIs require complete annotations and Google-style docstrings. This includes symbols exposed through facades, `__all__`, examples, or stable extension points. A substantial private helper that acts as a feature boundary follows the same rule; tiny private helpers need no boilerplate.

- Start with a punctuated one-line feature summary. Add paragraphs only for caller-visible behavior, side effects, constraints, or the object model.
- Annotate every public parameter and return, including `-> None`. Docstring types match signature spelling: `name (type): ...`; returned/yielded values use `type: ...`.
- Always include `Args`, with `None.` when there are no caller arguments. Exclude `self` and `cls`.
- Always include `Returns` for ordinary functions, including functions that return iterators. Use `Yields` for generators and async generators. For a `None` result, state that no value returns or describe the specific side effect.
- Include `Raises` for exceptions callers can trigger or handle. Use project exceptions and contextual `raise_mismatch` only where the repository owns that helper.
- Explain argument roles, units, bounds, defaulting, interactions, and enabled boolean behavior when relevant. Enumerate every supported literal/mode value and its meaning. Shared sets may link to one main API, class, Config, or Spec owner.
- Use `Warnings`, `Notes`, and `Examples` when they change correct use. Examples use the supported public facade.
- Public classes explain the object model. Document constructor arguments on the class or `__init__`, once. Properties may use attribute-style docs; setters and feature methods follow the full function rule.

Use [format and literal examples](doc/format.md) when writing sections or renderer markup, and [function examples](doc/example.md) for no-argument, `None`, and generator forms. Do not mix Google, NumPy, and Sphinx section conventions. Keep caller facts out of [implementation comments](comment.md).
