---
name: ts-files-optional
description: Read before adding optional TypeScript integrations.
---

# Optional TypeScript integrations

## Summary

Load optional integrations only on the selected path and distinguish missing packages from evaluation failures.

## Optional integrations

- Lazy loading controls evaluation, not installation ownership. Model the SDK deliberately as an optional peer (`peerDependencies` plus optional `peerDependenciesMeta`), an `optionalDependency`, or a separate integration package according to who installs/owns it; do not leave a dynamically imported package undeclared.
- Keep optional/heavy SDK imports inside the selected adapter's `create`/`connect` path:

```ts
export async function createVectorBackend(config: VectorConfig): Promise<VectorBackend> {
  let sdk: typeof import('@vendor/vector-sdk')
  try {
    sdk = await import('@vendor/vector-sdk')
  } catch (cause: unknown) {
    if (isMissingPackage(cause, '@vendor/vector-sdk')) {
      throw new MissingIntegrationError('vector', { cause })
    }
    throw new IntegrationLoadError('vector integration failed to load', { cause })
  }
  return new VendorVectorBackend(sdk, config)
}
```

`isMissingPackage` must narrowly prove that the requested top-level package—not one of its transitive imports—is missing. Otherwise preserve the actual evaluation/load failure; do not relabel syntax, initialization, or transitive dependency errors as “please install the integration”. Omitting the catch is preferable when the repository has no trustworthy classifier.

- Do not catch provider connection errors and later return empty success. Either fail creation or preserve a sanitized inspectable health error and make every operation fail contextually.
- Test that importing the package root does not load optional provider modules.
- For published packages, test packed consumers both without the optional SDK (base import works and selected integration fails actionably) and with it (the integration smoke path works).
- Expose optional packages/subpaths explicitly so bundlers and users can keep them out of the base graph.
