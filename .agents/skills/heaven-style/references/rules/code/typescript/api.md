---
id: ts-api
title: TypeScript API design and vocabulary
blocking: true
description: Choose TypeScript public objects, functions, options, and entry points.
---

# TypeScript API Design and Vocabulary

## Core rule

Keep the public mental model and class count small. Expose the shortest TypeScript API that matches the domain. Put identity, mutable state, invariants, and lifecycle on an owning object. Use a typed function for a stateless transform. Follow established JavaScript and TypeScript platform vocabulary where it is already strong. Use one domain verb per concept. Do not translate Python spellings mechanically.

An API should be easy to describe in one sentence and easy to discover through imports, types, and autocomplete. New classes, helpers, flags, factories, overloads, aliases, and fluent steps must remove more caller complexity than they add.

## Public front door

- Prefer one supported import and one obvious flow for each task.
- Prefer a method or static factory on an existing domain owner over parallel free-function APIs. Keep independent stateless transforms as functions.
- Use a class when it owns identity, mutable state, invariants, replaceable behavior, registration, or resource lifetime.
- Use a function for parsing, normalization, compilation, projection, formatting, and other stateless transforms.
- Keep constructors synchronous and free of I/O or registration. Use `create`, `connect`, `start`, or a framework lifecycle hook when setup can fail asynchronously.
- Use an options object when several parameters are optional, share a lifecycle, or are likely to evolve. Keep a short positional signature when order and meaning are unambiguous.
- Prefer structural interfaces and composition. Add inheritance only for a real substitutable runtime contract.
- Public examples import through package entry points, not source files, registry internals, or helper factories.

For operation names use [vocabulary](verbs.md); for guards, defaults, and extraction use [flow](flow.md).
