#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"

SKILL_PATH=".agents/skills/heaven-style"
DEFAULT_BRANCHES="python typescript"
BRANCH_TEXT="${HEAVEN_STYLE_BRANCHES:-${DEFAULT_BRANCHES}}"
FETCH_REMOTE="${HEAVEN_STYLE_FETCH_REMOTE:-}"
CURRENT_BRANCH="${HEAVEN_STYLE_CURRENT_BRANCH:-$(git branch --show-current)}"
EXPECTED_TREE=""
declare -a BRANCHES
declare -a RESULTS=()
declare -A SEEN=()

if [[ $# -gt 0 ]]; then
    BRANCH_TEXT="$*"
fi
BRANCH_TEXT="${BRANCH_TEXT//,/ }"
read -r -a BRANCHES <<<"${BRANCH_TEXT}"

if [[ ${#BRANCHES[@]} -lt 2 ]]; then
    echo "error: configure at least two branches with arguments or HEAVEN_STYLE_BRANCHES" >&2
    exit 2
fi

for branch in "${BRANCHES[@]}"; do
    if ! git check-ref-format --branch "${branch}" >/dev/null 2>&1; then
        echo "error: invalid branch name ${branch}" >&2
        exit 2
    fi
    if [[ -n "${SEEN[${branch}]:-}" ]]; then
        echo "error: duplicate branch ${branch}" >&2
        exit 2
    fi
    SEEN["${branch}"]=1
done

if [[ -n "${SEEN[${CURRENT_BRANCH}]:-}" ]]; then
    if ! git diff --quiet -- "${SKILL_PATH}" || ! git diff --cached --quiet -- "${SKILL_PATH}"; then
        echo "error: ${SKILL_PATH} has uncommitted changes on ${CURRENT_BRANCH}" >&2
        exit 1
    fi
fi

if [[ -n "${FETCH_REMOTE}" ]]; then
    for branch in "${BRANCHES[@]}"; do
        git fetch --no-tags "${FETCH_REMOTE}" "+refs/heads/${branch}:refs/remotes/${FETCH_REMOTE}/${branch}"
    done
fi

resolve_branch() {
    local branch="$1"
    if [[ "${branch}" == "${CURRENT_BRANCH}" ]]; then
        echo "HEAD"
    elif [[ -n "${FETCH_REMOTE}" ]] && git rev-parse --verify --quiet "refs/remotes/${FETCH_REMOTE}/${branch}^{commit}" >/dev/null; then
        echo "refs/remotes/${FETCH_REMOTE}/${branch}"
    elif git rev-parse --verify --quiet "refs/heads/${branch}^{commit}" >/dev/null; then
        echo "refs/heads/${branch}"
    elif git rev-parse --verify --quiet "refs/remotes/origin/${branch}^{commit}" >/dev/null; then
        echo "refs/remotes/origin/${branch}"
    else
        echo "error: required branch ${branch} is unavailable locally or at origin" >&2
        return 1
    fi
}

for branch in "${BRANCHES[@]}"; do
    ref="$(resolve_branch "${branch}")"
    if ! tree="$(git rev-parse "${ref}:${SKILL_PATH}" 2>/dev/null)"; then
        echo "error: ${SKILL_PATH} is missing from ${branch} (${ref})" >&2
        exit 1
    fi
    RESULTS+=("${branch}=${tree}")
    if [[ -z "${EXPECTED_TREE}" ]]; then
        EXPECTED_TREE="${tree}"
    elif [[ "${tree}" != "${EXPECTED_TREE}" ]]; then
        echo "error: ${SKILL_PATH} differs across configured branches" >&2
        printf '  %s\n' "${RESULTS[@]}" >&2
        exit 1
    fi
done

echo "${SKILL_PATH} is byte-identical across ${#BRANCHES[@]} branches (${EXPECTED_TREE})"
printf '  %s\n' "${RESULTS[@]}"
