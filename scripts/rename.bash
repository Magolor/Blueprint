#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
cd "${ROOT}"
source "${ROOT}/scripts/_env.bash"
export PYTHONDONTWRITEBYTECODE=1

OLD_PROJECT="Blueprint"
OLD_IMPORT="blueprint"
OLD_IMPORT_UPPER="BLUEPRINT"
OLD_CLI="bp"
OLD_GUI_CLI="blueprint-gui"
TEMPLATE_START_MARKER='<!-- blueprint-template-only:start -->'
TEMPLATE_END_MARKER='<!-- blueprint-template-only:end -->'

PROJECT_NAME=""
DIST_NAME=""
IMPORT_NAME=""
CLI_NAME=""
YES=0

usage() {
    cat <<'EOF'
Usage: bash scripts/rename.bash --project-name NAME --dist-name NAME --import-name NAME --cli-name NAME [OPTIONS]

Rename this Blueprint template into a real project.

Options:
  --project-name NAME  Display name, e.g. "My Project".
  --dist-name NAME     Python distribution name, e.g. my-project.
  --import-name NAME   Python import package name, e.g. my_project.
  --cli-name NAME      Console command name, e.g. my-tool.
  --yes                Run without interactive confirmation.
  -h, --help           Show this help message.

Example:
  bash scripts/rename.bash --project-name "My Project" --dist-name my-project --import-name my_project --cli-name my-tool --yes
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --project-name)
            PROJECT_NAME="${2:-}"
            shift 2
            ;;
        --dist-name)
            DIST_NAME="${2:-}"
            shift 2
            ;;
        --import-name)
            IMPORT_NAME="${2:-}"
            shift 2
            ;;
        --cli-name)
            CLI_NAME="${2:-}"
            shift 2
            ;;
        --yes)
            YES=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "error: unknown option: $1" >&2
            usage
            exit 1
            ;;
    esac
done

require_value() {
    local name="$1"
    local value="$2"
    if [[ -z "${value}" ]]; then
        echo "error: ${name} is required" >&2
        usage
        exit 1
    fi
}

require_value "--project-name" "${PROJECT_NAME}"
require_value "--dist-name" "${DIST_NAME}"
require_value "--import-name" "${IMPORT_NAME}"
require_value "--cli-name" "${CLI_NAME}"

if [[ "${PROJECT_NAME}" == *$'\n'* || "${PROJECT_NAME}" == *$'\r'* ]]; then
    echo "error: --project-name must be a single line" >&2
    exit 1
fi

if [[ ! "${DIST_NAME}" =~ ^[a-z0-9]([a-z0-9._-]*[a-z0-9])?$ ]]; then
    echo "error: --dist-name must be a valid lowercase Python distribution name" >&2
    exit 1
fi

if [[ ! "${IMPORT_NAME}" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
    echo "error: --import-name must be a valid Python identifier" >&2
    exit 1
fi

if run_python -c 'import keyword, sys; raise SystemExit(0 if keyword.iskeyword(sys.argv[1]) else 1)' "${IMPORT_NAME}"; then
    echo "error: --import-name must not be a Python keyword" >&2
    exit 1
fi

if [[ ! "${CLI_NAME}" =~ ^[A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?$ ]]; then
    echo "error: --cli-name must be a valid console command name" >&2
    exit 1
fi

if [[ "${IMPORT_NAME}" != "${OLD_IMPORT}" && -e "src/${IMPORT_NAME}" ]]; then
    echo "error: src/${IMPORT_NAME} already exists" >&2
    exit 1
fi

if [[ ! -f ".blueprint-template.yaml" ]]; then
    echo "error: this checkout is not an uninitialized Blueprint template" >&2
    exit 1
fi

if [[ -e "docs/tasks.yaml" ]]; then
    echo "error: template mode must not contain docs/tasks.yaml" >&2
    exit 1
fi

if [[ ! -f "docs/tasks.template.yaml" ]]; then
    echo "error: docs/tasks.template.yaml is required to initialize the task queue" >&2
    exit 1
fi

is_protected_path() {
    local path="${1#./}"
    local component
    local IFS='/'
    local components=()
    case "${path}" in
        .agents/skills/heaven-style|.agents/skills/heaven-style/*)
            return 0
            ;;
    esac
    read -r -a components <<< "${path}"
    for component in "${components[@]}"; do
        case "${component}" in
            .git|.venv|dist|build|.temp|cache|.cache|__pycache__|.pytest_cache|.mypy_cache|.ruff_cache|*.egg-info)
                return 0
                ;;
        esac
    done
    return 1
}

is_mutable_text_file() {
    local file="$1"
    if is_protected_path "${file}" || [[ "${file}" == "./scripts/rename.bash" ]]; then
        return 1
    fi
    grep -Iq . "${file}"
}

replace_text() {
    local old="$1"
    local new="$2"
    local file="$3"
    OLD_TEXT="${old}" NEW_TEXT="${new}" perl -0pi -e 's/\Q$ENV{OLD_TEXT}\E/$ENV{NEW_TEXT}/g' "${file}"
}

strip_template_blocks() {
    local file="$1"
    TEMPLATE_START_MARKER="${TEMPLATE_START_MARKER}" TEMPLATE_END_MARKER="${TEMPLATE_END_MARKER}" perl -0pi -e \
        's/^[ \t]*\Q$ENV{TEMPLATE_START_MARKER}\E[ \t]*\r?\n.*?^[ \t]*\Q$ENV{TEMPLATE_END_MARKER}\E[ \t]*(?:\r?\n|\z)//gms' \
        "${file}"
}

# Fail before the first mutation when a template-only prose block is malformed.
while IFS= read -r -d '' file; do
    if ! is_mutable_text_file "${file}"; then
        continue
    fi
    starts="$(grep -F -c -- "${TEMPLATE_START_MARKER}" "${file}" || true)"
    ends="$(grep -F -c -- "${TEMPLATE_END_MARKER}" "${file}" || true)"
    if [[ "${starts}" != "${ends}" ]]; then
        echo "error: unmatched template-only marker in ${file}" >&2
        exit 1
    fi
done < <(find . -type f -print0)

# Detect path collisions before editing content. Protected build/runtime trees are
# deliberately outside the rename surface, including a linked-worktree .git file.
while IFS= read -r -d '' path; do
    if is_protected_path "${path}"; then
        continue
    fi
    dir="$(dirname -- "${path}")"
    base="$(basename -- "${path}")"
    new_base="${base//${OLD_IMPORT}/${IMPORT_NAME}}"
    if [[ "${base}" != "${new_base}" && -e "${dir}/${new_base}" ]]; then
        echo "error: cannot rename ${path}; ${dir}/${new_base} already exists" >&2
        exit 1
    fi
done < <(find . -depth -name "*${OLD_IMPORT}*" -print0)

echo "[rename] validating inert template documentation"
run_python scripts/docs.py check

if [[ "${YES}" -ne 1 ]]; then
    printf 'Rename Blueprint to %s (dist=%s, import=%s, cli=%s)? [y/N] ' "${PROJECT_NAME}" "${DIST_NAME}" "${IMPORT_NAME}" "${CLI_NAME}"
    read -r answer
    case "${answer}" in
        y|Y|yes|YES)
            ;;
        *)
            echo "rename cancelled"
            exit 1
            ;;
    esac
fi

# Template history and untranslated prose do not describe the generated project.
rm -f -- "BLUEPRINT.md" "README.zh.md"
while IFS= read -r -d '' path; do
    rm -f -- "${path}"
done < <(find docs/plans docs/reports -type f -name '20??-??-??-*.md' -print0 2>/dev/null)

if [[ "${IMPORT_NAME}" != "${OLD_IMPORT}" && -d "src/${OLD_IMPORT}" ]]; then
    mv "src/${OLD_IMPORT}" "src/${IMPORT_NAME}"
fi

IMPORT_UPPER="$(printf '%s' "${IMPORT_NAME}" | tr '[:lower:]' '[:upper:]')"

while IFS= read -r -d '' file; do
    if ! is_mutable_text_file "${file}"; then
        continue
    fi
    strip_template_blocks "${file}"

    # Preserve the four independent identities before the broad import-package
    # replacement: display name, distribution, Python import, and CLI command.
    replace_text 'name = "blueprint"' "name = \"${DIST_NAME}\"" "${file}"
    replace_text 'keywords = ["blueprint", "starter", "template", "uv", "python"]' "keywords = [\"${DIST_NAME}\", \"python\"]" "${file}"
    replace_text 'description = "Blueprint: a uv-first Python starter project."' "description = \"${PROJECT_NAME}: a Python project.\"" "${file}"
    replace_text 'Blueprint is a uv-first Python starter project for future repositories.' "${PROJECT_NAME} is a Python project." "${file}"
    replace_text '| Task coordination | Template mode keeps `docs/tasks.template.yaml` empty; operational mode uses the promoted `docs/tasks.yaml` as its single writable queue. |' '| `docs/tasks.yaml` | Single writable task queue for active operational work. |' "${file}"
    replace_text 'blueprint-dist' "${DIST_NAME}-dist" "${file}"
    replace_text 'docker build -t blueprint' "docker build -t ${DIST_NAME}" "${file}"
    replace_text 'docker run --rm blueprint' "docker run --rm ${DIST_NAME}" "${file}"
    replace_text "${OLD_GUI_CLI}" "${CLI_NAME}-gui" "${file}"
    replace_text 'bp = "blueprint.cli:main"' "${CLI_NAME} = \"${IMPORT_NAME}.cli:main\"" "${file}"
    replace_text "uv run ${OLD_CLI}" "uv run ${CLI_NAME}" "${file}"
    replace_text "${OLD_CLI} --" "${CLI_NAME} --" "${file}"
    replace_text 'ENTRYPOINT ["bp"]' "ENTRYPOINT [\"${CLI_NAME}\"]" "${file}"
    replace_text 'package="bp"' "package=\"${CLI_NAME}\"" "${file}"

    replace_text "${OLD_PROJECT}" "${PROJECT_NAME}" "${file}"
    replace_text "${OLD_IMPORT_UPPER}" "${IMPORT_UPPER}" "${file}"
    replace_text "${OLD_IMPORT}" "${IMPORT_NAME}" "${file}"
done < <(find . -type f -print0)

if [[ -f "pyproject.toml" ]]; then
    perl -0pi -e '
        s/^authors\s*=.*\r?\n//m;
        s/^\[project\.urls\]\r?\n.*?(?=^\[|\z)//ms;
    ' "pyproject.toml"
fi

mv "docs/tasks.template.yaml" "docs/tasks.yaml"
run_python -c '
from datetime import date
from pathlib import Path
import sys
import yaml

path = Path(sys.argv[1])
data = yaml.safe_load(path.read_text(encoding="utf-8"))
if not isinstance(data, dict) or data.get("tasks") != []:
    raise SystemExit("error: task starter stopped being inert during rename")
data["project"] = sys.argv[2]
data["updated"] = date.today().isoformat()
path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
' "docs/tasks.yaml" "${PROJECT_NAME}"
rm -- ".blueprint-template.yaml"

run_python -c '
from datetime import date
from pathlib import Path
import sys

project = sys.argv[1]
Path("docs/DEVLOG.md").write_text(
    "# Development Log\n\n"
    "This rolling log records concise change, verification, and handoff evidence. "
    "Stable behavior belongs in user or engineering documentation.\n\n"
    f"## {date.today().isoformat()} — {project} initialized\n\n"
    "- Task: direct request\n"
    f"- Changed: Instantiated {project} from the Blueprint project template.\n"
    "- Verified: Template rename and documentation contract.\n"
    "- Next: none\n",
    encoding="utf-8",
)
' "${PROJECT_NAME}"

while IFS= read -r -d '' path; do
    if is_protected_path "${path}"; then
        continue
    fi
    dir="$(dirname -- "${path}")"
    base="$(basename -- "${path}")"
    new_base="${base//${OLD_IMPORT}/${IMPORT_NAME}}"
    if [[ "${base}" != "${new_base}" ]]; then
        mv "${path}" "${dir}/${new_base}"
    fi
done < <(find . -depth -name "*${OLD_IMPORT}*" -print0)

bash scripts/sync-readme.bash
run_python scripts/docs.py check

# A generated project cannot be initialized twice. Retire both the template-only
# entry point and its source-template contract test from the operational tree.
rm -- "scripts/rename.bash" "tests/test_rename.py"

echo "[rename] renamed project to ${PROJECT_NAME} (dist=${DIST_NAME}, import=${IMPORT_NAME}, cli=${CLI_NAME})"
