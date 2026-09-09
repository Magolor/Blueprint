---
name: failure-auth-secrets
description: Read when connector, CLI, or provider authentication repeatedly fails.
---

# Auth, MCP, and Secret Lookup Failures

## Summary

Classify credential failures and recover through a scoped, verified access path without exposing secrets.

## Pattern

MCP calls, provider SDKs, CLIs, GraphQL calls, or LLM integrations fail repeatedly. Authentication appears expired, a token/API key is missing from the process environment, or the active shell did not load the expected secrets. Linear is a common and important case. This procedure also applies to Tavily, LLM providers, GitHub, OpenRouter, Portkey, and other local development integrations.

## Response

For GitHub repository visibility or PR/issue permission failures with a valid
login, use [GitHub access recovery](git.md) to compare credential precedence
and resource scope before searching for another secret.

1. Classify the failure as auth/secret lookup, network/proxy, wrong environment, wrong workspace/team, or provider outage.
2. Inspect available secret sources without printing values: `~/.bashrc` or `~/.bash_profile`, repo-local `secret/*.token`, `.env*`, documented env var names, and any repo-provided `secret/setup.bash`.
3. Load only the needed variable into the current process or a scoped command. Keep token values out of chat, logs, committed files, review artifacts, and screenshots.
4. If an MCP repeatedly fails after env/proxy checks, use the provider's direct API path when available. For Linear, prefer the GraphQL API with the discovered token after three identical MCP/auth failures.
5. Record the env var name, credential source, endpoint/API path, and whether the fallback worked, without exposing the secret.
6. If auth debugging blocks the main coding/review task, spawn a narrow subagent when available: "diagnose provider auth only; report env var names, endpoint, command path, and whether direct API works; do not print secrets."

## Do Not

- Do not create duplicate Linear/provider records because lookup failed once.
- Do not log, print, paste, screenshot, or commit secret values.
- Do not keep retrying the same failing MCP call after three identical auth failures. Switch to direct API fallback, or ask for re-authentication when no token exists.
- Do not broaden secret access beyond the specific provider needed for the current task.
