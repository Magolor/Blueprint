---
id: py-comment
title: Python implementation comments
description: Read for Python implementation comments.
blocking: true
---

# Python implementation comments

Use `#` for non-obvious implementation constraints, ordering, transformations, and rationale. Explain why the code needs the constraint; do not narrate obvious statements or duplicate public contract facts.

Keep caller-visible behavior on the [public docstring](doc.md). A private helper may have a short docstring when its name and annotations do not explain a meaningful boundary. Do not add full public-section boilerplate to tiny private helpers. Follow repository tooling and local comment conventions.
