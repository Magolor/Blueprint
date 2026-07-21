# 2026-07-16 Progress

## 0.1.2.0 Version Alignment

- Summary: Aligned the Blueprint package and canonical heaven-style skill metadata with the HeavenBase 0.1.2.0 dashboard and refactor release train.
- Decisions: Kept the published `heavenbase>=0.1.1.1` runtime floor unchanged until HeavenBase 0.1.2.0 is available on PyPI.
- Verification: The isolated `dev` release branch passed environment drift, heaven-style index, lint, tests, and package build checks.
- Next: Raise the Blueprint dependency floor only after the aligned HeavenBase release is published.
