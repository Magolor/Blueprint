# Template release preparation

## Summary

Prepare one verified source archive per product branch for `0.2.0-alpha.1`. Both branches share the exact Heaven Style tree. Template publication is separate from npm or PyPI publication; this release does not publish starter package names to either registry.

## Prepare and verify

Commit current source, then run `bash scripts/release.bash` on each product branch. The script runs the branch gate, builds the package artifact, and writes a Git source archive plus SHA-256 checksum under `.temp/release/`. Untracked files and ignored local caches are absent from the archive. GitHub’s manual release-preparation workflow uploads the same archive format without publishing it.

Before publishing, confirm both branch gates, installed-artifact checks, bilingual meaning and structure, license notices, citation metadata, and the actual archive contents. The current release tree must not contain unrelated project names, private traces, or embedded reference checkouts. Retain only necessary upstream attribution and the minimal version-freeze reference.

## History and publication

Each product branch has two commits: its preserved remote root and one consolidated alpha commit. Keep a recovery bundle of the unsquashed local history outside the product tree. Confirm the remote roots have not changed before publication. For a first alpha publication, push fast-forward from the preserved roots. Replacing an already published alpha requires explicit maintainer authority, a verified recovery bundle and saved release assets, and exact remote object IDs for every overwritten branch and tag. Use an atomic branch push with explicit force-with-lease values; never use an unguarded force push. Preserve unrelated releases and tags.

After explicit publication authorization:

1. Push `typescript` and `python` together with `git push --atomic origin typescript python`.
2. Check hosted CI for both pushed commits.
3. Create annotated tags `v0.2.0-alpha.1` on `typescript` and `v0.2.0-alpha.1-python` on `python`, then push those two tags explicitly.
4. Create a GitHub prerelease on `v0.2.0-alpha.1`, attach both verified archives and checksums, and use the current changelog as the release notes. Link the Python tag in the release body.

Do not claim a release exists until its remote tags, assets, and prerelease page are verified. Registry publication needs a separate package ownership and publication decision.

## Replacing the frozen alpha

Prepare both corrected archives before removing the old prerelease. Confirm remote branch heads still match the saved object IDs. Consolidate the old alpha and maintenance work into one alpha commit above each preserved baseline root. Push both branches atomically with exact leases and verify hosted CI. Replace only the alpha's prerelease and its TypeScript/Python annotated tags, then attach the corrected archives and checksums. Verify tag targets, release metadata, and downloaded asset digests before reporting completion. The recovery bundle and old assets remain outside the product tree.

A closeout documentation change must be included in the consolidated commit and regenerated source archives; never attach an archive from an earlier tree to a new tag. npm and PyPI publication remain separate and are not part of this workflow.
