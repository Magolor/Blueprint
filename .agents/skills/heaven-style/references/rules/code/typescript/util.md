---
name: ts-util
description: Choose TypeScript utilities and explicit host/runtime I/O boundaries.
---

# TypeScript Utilities and Platform APIs

## Summary

Prefer the package's own utilities and code style, including convenience contracts such as `pj`, over equivalent platform calls. When no suitable owner exists, use the target runtime or established dependency directly. Put a currently needed generic helper in package-wide or subgroup shared utils; keep specialized one-use expressions inline.

## Helper and import ownership

Read [clean](clean.md) for inline code versus shared utility placement. Prefer the package's established utility re-exports as well as its wrapped operations, even for convenience symbols, rather than scattering equivalent imports. Do not add a foreign platform dependency or invent a giant facade merely to obtain them. Keep modern language types and the repository's runtime/import constraints.

## Principle

Runtime portability requires an explicit boundary. Do not assume portability. Browser, worker, Bun, and Node code may share domain contracts while using separate small adapters for host-specific I/O. Do not hide an unresolved runtime decision behind a catch-all `utils.ts` layer.

## Ownership ladder

1. Use an existing repository platform/utility owner when it clearly defines the policy.
2. Otherwise use the target runtime or Web-standard API directly.
3. Keep one-off domain transforms local and explicit.
4. Put a needed generic helper in the package-wide or narrowest subgroup shared utility owner, even for its first consumer. Do not create small helpers in a single feature module or add utilities for hypothetical needs.

## Do

- Read `AGENTS.md`, `package.json`, compiler/runtime metadata, nearby imports, and deployment targets before choosing Node-, Bun-, browser-, or worker-specific APIs.
- Prefer Web-standard APIs such as `URL`, `TextEncoder`, `TextDecoder`, `AbortSignal`, `fetch`, `crypto`, and `structuredClone` when every declared host implements the needed contract.
- In Node-targeted code, use explicit `node:` imports such as `node:fs/promises`, `node:path`, `node:url`, `node:crypto`, and `node:child_process`.
- In Bun-only application code, use `Bun.file`, `Bun.write`, or `Bun.spawn` when they make ownership clearer; use Node-compatible APIs when the package promises Node compatibility.
- Resolve module-owned read-only assets from `import.meta.url` or the repository's resource owner. Resolve user-writable state through configuration/platform policy, never relative to a published module's source layout.
- Specify text encodings. Validate parsed external data from `unknown`. Keep binary/text conversions explicit.
- Use a repository logger for libraries and services. `console` is acceptable at a deliberate application/CLI boundary or in tiny scripts whose output is the interface.
- Generate security-sensitive randomness and public IDs through platform cryptography or an established repository owner. Do not invent random, hash, or deterministic-ID algorithms casually.
- Give temporary files/directories one owner, private permissions where relevant, random names, and guaranteed cleanup.
- Pass subprocess arguments as arrays. Minimize inherited environment/authority. Bound output. Forward cancellation. Await termination. Detailed lifecycle and error rules live in [async](async.md).

## Avoid

- Generic `common.ts`, `helpers.ts`, or `utils.ts` modules with unrelated owners.
- Small wrappers confined to one feature module, or duplicates of an existing package-owned utility.
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

**Recommended pattern:** use an existing internal utility owner and the entity's validation contract.

```ts
import { loadJson, pj } from './utils.js'
import { Profile } from './profile.js'

const path = pj(root, 'data', `${name}.json`)
const profile = Profile.fromJson(await loadJson(path))
```

The imports are illustrative package-owned APIs. loadJson returns untrusted data; Profile.fromJson validates it. If no package utility exists, use explicit runtime APIs and validate unknown at the same boundary. Prefer package utilities over adding readJsonFile, joinDataPath, or another small module-local wrapper.

A larger feature-specific loader may remain with its domain owner. A needed small generic helper belongs directly in shared utils, not in the consuming feature module.
