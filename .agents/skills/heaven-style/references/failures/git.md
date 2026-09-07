---
id: failure-git-auth
title: GitHub repository and token access failures
description: Diagnose GitHub repository access failures despite a valid login.
---

# GitHub Access Failures

## Pattern

GitHub CLI reports `Could not resolve to a Repository`, REST returns 404 or 403,
or PR and issue operations fail even though browser or SSH Git access works.
Treat repository visibility and operation permissions as separate checks.

## Recovery

1. Verify the intended host and repository name. Use `gh auth status` to identify the active account and credential source without revealing tokens.
2. Check whether `GH_TOKEN` or `GITHUB_TOKEN` is set without printing its value. For github.com, `GH_TOKEN` takes precedence over `GITHUB_TOKEN`, and both override the saved CLI login.
3. Compare a read-only request with the saved login: `env -u GH_TOKEN -u GITHUB_TOKEN gh repo view OWNER/REPO`. If this succeeds while the normal command fails, the environment credential is the failing access path.
4. Check the PAT's resource owner, repository selection, operation permissions, and organization approval or policy. Fine-grained tokens cover one resource owner. Selecting every permission does not extend access to other owners. Check SSO authorization when applicable to the credential type. Do not infer the exact restriction from 404 alone.
5. Keep optional PATs under a documented account-specific environment name. Map that variable to the standard names only for a command that needs that identity and resource scope. Do not automatically replace a working organization login with a personal PAT.
6. Retry the read operation through the verified credential path. For an authorized mutation, check whether the earlier attempt took effect before retrying. Do not create or edit an issue or PR merely to test write access. Permission metadata is evidence, not proof of a completed mutation.
7. If neither credential path works, report the tested identity and access boundary. Request the missing repository grant, token approval, or authentication instead of repeatedly retrying or escalating permissions blindly.

## Scoped PAT use

Use the account-specific variable declared by the local credential configuration.
`GITHUB_MAGOLOR_PAT` is the configured personal PAT name when available; use
the locally documented equivalent on other installations.
Disable shell tracing before credential assignments. Never print a token or put
its literal value in a command, URL, log, or tracked file.

```bash
GH_TOKEN="${GITHUB_MAGOLOR_PAT:?Load the intended account PAT first}" \
GITHUB_TOKEN="${GITHUB_MAGOLOR_PAT:?Load the intended account PAT first}" \
gh repo view OWNER/REPO
```

To return an existing shell to its saved CLI login, unset `GH_TOKEN` and
`GITHUB_TOKEN`. Changing a credential mapping or reloading secrets does not clear
old exports from existing processes. SSH credentials and API credentials are
separate; a successful Git fetch does not validate GitHub API access.

## Sources

- [GitHub CLI environment precedence](https://cli.github.com/manual/gh_help_environment)
- [GitHub personal access token boundaries](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
