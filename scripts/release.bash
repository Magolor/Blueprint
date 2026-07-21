#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"
source "${ROOT}/scripts/_env.bash"

REMOTE="origin"
MASTER_BRANCH="master"

usage() {
    cat <<'EOF'
Usage: bash scripts/release.bash [OPTIONS]

Create or reuse the annotated v<version> tag for the clean, published master
commit and push that tag to trigger the GitHub Release workflow.

Options:
  --remote NAME       Git remote to push. Default: origin.
  -h, --help          Show this help message.
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --remote)
            if [[ $# -lt 2 || "$2" == --* ]]; then
                echo "error: --remote requires a value" >&2
                exit 1
            fi
            REMOTE="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "error: unknown argument: $1" >&2
            usage >&2
            exit 1
            ;;
    esac
done

git_output() {
    git "$@" | tr -d '\r'
}

ref_exists() {
    git rev-parse --verify --quiet "$1" >/dev/null
}

is_ancestor() {
    git merge-base --is-ancestor "$1" "$2" >/dev/null 2>&1
}

version="$(run_python - <<'PY'
from pathlib import Path

namespace = {}
exec(Path("src/blueprint/version.py").read_text(encoding="utf-8"), namespace)
print(namespace["__version__"])
PY
)"

if [[ ! "${version}" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "error: '${version}' is not a stable MAJOR.MINOR.PATCH.N release version" >&2
    exit 1
fi

tag="v${version}"
current_branch="$(git_output branch --show-current)"
if [[ "${current_branch}" != "${MASTER_BRANCH}" ]]; then
    echo "error: release must run from ${MASTER_BRANCH}; current branch is ${current_branch:-detached HEAD}" >&2
    exit 1
fi

dirty="$(git_output status --porcelain --untracked-files=normal)"
if [[ -n "${dirty}" ]]; then
    echo "error: release requires a clean worktree:" >&2
    printf '%s\n' "${dirty}" >&2
    exit 1
fi

if ! git remote get-url "${REMOTE}" >/dev/null 2>&1; then
    echo "error: Git remote '${REMOTE}' does not exist" >&2
    exit 1
fi

echo "Fetching ${REMOTE}/${MASTER_BRANCH}"
git fetch --prune "${REMOTE}" "+refs/heads/${MASTER_BRANCH}:refs/remotes/${REMOTE}/${MASTER_BRANCH}"

remote_master="refs/remotes/${REMOTE}/${MASTER_BRANCH}"
if ! ref_exists "${remote_master}"; then
    echo "error: ${REMOTE}/${MASTER_BRANCH} does not exist" >&2
    exit 1
fi

head_commit="$(git_output rev-parse "${MASTER_BRANCH}^{commit}")"
remote_master_commit="$(git_output rev-parse "${remote_master}^{commit}")"
if [[ "${head_commit}" != "${remote_master_commit}" ]] && ! is_ancestor "${remote_master}" "${MASTER_BRANCH}"; then
    echo "error: ${MASTER_BRANCH} is behind or diverged from ${REMOTE}/${MASTER_BRANCH}; update it before release" >&2
    exit 1
fi

remote_tag_rows="$(git_output ls-remote --tags "${REMOTE}" "refs/tags/${tag}" "refs/tags/${tag}^{}")"
remote_tag_object="$(printf '%s\n' "${remote_tag_rows}" | awk -v ref="refs/tags/${tag}" '$2 == ref { print $1 }')"
remote_tag_commit="$(printf '%s\n' "${remote_tag_rows}" | awk -v ref="refs/tags/${tag}^{}" '$2 == ref { print $1 }')"

if [[ -n "${remote_tag_object}" ]]; then
    if [[ -z "${remote_tag_commit}" ]]; then
        echo "error: ${REMOTE} already has lightweight tag ${tag}; releases require annotated tags" >&2
        exit 1
    fi
    if [[ "${remote_tag_commit}" != "${head_commit}" ]]; then
        echo "error: ${REMOTE}/${tag} points to ${remote_tag_commit}, not ${head_commit}" >&2
        exit 1
    fi
fi

if ref_exists "refs/tags/${tag}"; then
    if [[ "$(git_output cat-file -t "refs/tags/${tag}")" != "tag" ]]; then
        echo "error: local ${tag} is lightweight; releases require annotated tags" >&2
        exit 1
    fi
    local_tag_commit="$(git_output rev-parse "refs/tags/${tag}^{commit}")"
    if [[ "${local_tag_commit}" != "${head_commit}" ]]; then
        echo "error: local ${tag} points to ${local_tag_commit}, not ${head_commit}" >&2
        exit 1
    fi
    if [[ -n "${remote_tag_object}" && "$(git_output rev-parse "refs/tags/${tag}")" != "${remote_tag_object}" ]]; then
        echo "error: local and remote ${tag} annotations differ" >&2
        exit 1
    fi
fi

if [[ "${head_commit}" != "${remote_master_commit}" ]]; then
    echo "Pushing ${MASTER_BRANCH} to ${REMOTE}"
    git push "${REMOTE}" "refs/heads/${MASTER_BRANCH}:refs/heads/${MASTER_BRANCH}"
else
    echo "${REMOTE}/${MASTER_BRANCH} already contains ${head_commit}"
fi

if [[ -n "${remote_tag_object}" ]]; then
    if ! ref_exists "refs/tags/${tag}"; then
        git fetch "${REMOTE}" "refs/tags/${tag}:refs/tags/${tag}"
    fi
    echo "Release tag ${tag} is already published at ${head_commit}"
    exit 0
fi

if ! ref_exists "refs/tags/${tag}"; then
    echo "Creating annotated release tag ${tag}"
    git tag --annotate "${tag}" --message "Blueprint ${version}"
else
    echo "Reusing local annotated release tag ${tag}"
fi

echo "Pushing ${tag} to ${REMOTE}; this triggers the GitHub Release workflow"
git push "${REMOTE}" "refs/tags/${tag}:refs/tags/${tag}"
