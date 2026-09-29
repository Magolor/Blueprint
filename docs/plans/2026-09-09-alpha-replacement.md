# Corrected alpha replacement

## Summary

Replace the frozen alpha with corrected Heaven Style rules. Preserve each existing baseline root and one consolidated alpha commit per product branch. Assess downstream adoption separately from the template release.

- Status: Done
- Created: 2026-09-09
- Task: RELEASE-002

## Steps

1. Inspect downstream rule and public-API alignment; preserve unrelated work.
2. Back up local history and the existing release, update release documentation, and consolidate history.
3. Prepare and verify both source archives, reinstall, push with exact leases, and check hosted CI.
4. Replace only the current alpha prerelease and its two tags; verify remote targets and asset digests.

## Closeout

Prepared corrected source archives from one consolidated alpha commit per product branch after both release gates passed. Preserved the old history and release assets outside the product tree. The local downstream assessment identified policy, SQL/resources, KV/collection vocabulary, CLI aliases, and utility adoption work without changing downstream source. Remote publication and exact commit/artifact identity are recorded by the GitHub prerelease and its tags, not duplicated here. No package registry publication is included.
