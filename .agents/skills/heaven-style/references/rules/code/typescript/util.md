---
id: ts-util
title: TypeScript utilities and platform APIs
enabled: true
blocking: true
order: 10
category: code-quality
keywords: [TypeScript utilities, Node fs, Bun file, path, URL, JSON, logging, crypto, UUID, temp files, child process, shared helper]
description: Use when TypeScript code touches files, paths, resources, serialization, logging, hashing, IDs, temp data, subprocesses, or shared utility ownership.
---

# TypeScript Utilities and Platform APIs

## Core rule

Use the target runtime's established APIs or the repository's declared platform owner directly. Add a shared utility only when it owns real policy, validation, observability, portability, or repeated behavior. A wrapper that merely renames `node:fs/promises`, `node:path`, `Bun.file`, `JSON`, `crypto`, `fetch`, or another direct API increases indirection without creating ownership.

Runtime portability is an explicit boundary, not an assumed property. Browser, worker, Bun, and Node code may share domain contracts while using separate small adapters for host-specific I/O. Do not hide an unresolved runtime decision behind a catch-all `utils.ts` layer.

## Apply when

- Code reads or writes files, paths, package assets, temp data, environment values, or process state.
- Code parses or emits JSON/YAML/text/base64/hex/binary data.
- Code logs, hashes, generates identifiers, calls `fetch`, or starts a subprocess.
- A change proposes `utils.ts`, `helpers.ts`, a platform abstraction, or a dependency for behavior already supplied by the runtime.

## Ownership ladder

1. Use an existing repository platform/utility owner when it clearly defines the policy.
2. Otherwise use the target runtime or Web-standard API directly.
3. Keep one-off domain transforms local and explicit.
4. Introduce a shared helper or adapter only for repeated policy, validation, portability, observability, or lifecycle.

## Do

- Read `AGENTS.md`, `package.json`, compiler/runtime metadata, nearby imports, and deployment targets before choosing Node-, Bun-, browser-, or worker-specific APIs.
- Prefer Web-standard APIs such as `URL`, `TextEncoder`, `TextDecoder`, `AbortSignal`, `fetch`, `crypto`, and `structuredClone` when every declared host implements the needed contract.
- In Node-targeted code, use explicit `node:` imports such as `node:fs/promises`, `node:path`, `node:url`, `node:crypto`, and `node:child_process`.
- In Bun-only application code, use `Bun.file`, `Bun.write`, or `Bun.spawn` when they make ownership clearer; use Node-compatible APIs when the package promises Node compatibility.
- Resolve module-owned read-only assets from `import.meta.url` or the repository's resource owner. Resolve user-writable state through configuration/platform policy, never relative to a published module's source layout.
- Specify text encodings, validate parsed external data from `unknown`, and keep binary/text conversions explicit.
- Use a repository logger for libraries and services. `console` is acceptable at a deliberate application/CLI boundary or in tiny scripts whose output is the interface.
- Generate security-sensitive randomness and public IDs through platform cryptography or an established repository owner. Do not invent random, hash, or deterministic-ID algorithms casually.
- Give temporary files/directories one owner, private permissions where relevant, random names, and guaranteed cleanup.
- Pass subprocess arguments as arrays, minimize inherited environment/authority, bound output, forward cancellation, and await termination. Detailed lifecycle and error rules live in [async.md](async.md).

## Avoid

- Generic `common.ts`, `helpers.ts`, or `utils.ts` modules with unrelated owners.
- Thin wrappers around a single platform call when they add no policy or portability.
- Sync filesystem or subprocess APIs in request/event-loop paths without a measured reason.
- Shell command strings built from caller-controlled values.
- `JSON.parse(text) as T`, implicit default encodings, or lossy serialization hidden behind a broad helper.
- Assuming `process.cwd()` is the location of a package asset.
- Importing Node/Bun globals into browser- or worker-shared modules.
- Adding a platform framework merely to obtain convenience helpers.

## Example

**Anti-pattern:**

```ts
export async function readJsonFile<T>(path: string): Promise<T> {
  return JSON.parse(await readFile(path, 'utf8')) as T
}
```

The generic assertion manufactures trust and the wrapper owns no schema or policy.

**Recommended pattern:**

```ts
import { readFile } from 'node:fs/promises'

export async function loadProfile(path: string): Promise<Profile> {
  const text = await readFile(path, 'utf8')
  const raw: unknown = JSON.parse(text)
  return ProfileSchema.parse(raw)
}
```

Keep this behavior local while only one feature owns it. Promote a repository helper later only if several consumers need the same schema-independent read, error, telemetry, or runtime-portability contract.

## Review checks

- Is the chosen API valid in every declared runtime for this module?
- Does a helper own policy or merely rename a platform call?
- Are package assets independent from the current working directory?
- Are parsed values validated before entering domain code?
- Are temp data, subprocesses, file handles, and log output owned and cleaned up?
- Does portability live in a narrow adapter instead of an ambiguous global utility layer?

## Related rules

Also apply [types.md](types.md) for `unknown` and decoded shapes, [api.md](api.md) for helper and public-surface decisions, [modules.md](modules.md) for host/package boundaries, [async.md](async.md) for subprocess and resource lifecycle, [config.md](config.md) for writable paths and environment resolution, and [environment.md](environment.md) for the declared runtime.
