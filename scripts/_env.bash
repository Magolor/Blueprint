#!/usr/bin/env bash

resolve_uv_optional() {
    if [[ -n "${UV_BIN:-}" ]]; then
        return 0
    fi
    if command -v uv >/dev/null 2>&1; then
        UV_BIN="uv"
        return 0
    fi
    if command -v uv.exe >/dev/null 2>&1; then
        UV_BIN="uv.exe"
        return 0
    fi
    return 1
}

resolve_uv() {
    if resolve_uv_optional; then
        return 0
    fi
    echo "error: uv or uv.exe is required but was not found on PATH" >&2
    exit 1
}

venv_python() {
    local venv="$1"
    local candidate
    for candidate in "${venv}/bin/python" "${venv}/Scripts/python.exe" "${venv}/Scripts/python"; do
        if [[ -x "${candidate}" || -f "${candidate}" ]]; then
            printf '%s\n' "${candidate}"
            return 0
        fi
    done
    return 1
}

resolve_python_preference() {
    if [[ -n "${REPO_PYTHON_PREFERENCE:-}" ]]; then
        printf '%s\n' "${REPO_PYTHON_PREFERENCE}"
        return 0
    fi
    if [[ -n "${HEAVENBASE_PYTHON_PREFERENCE:-}" ]]; then
        printf '%s\n' "${HEAVENBASE_PYTHON_PREFERENCE}"
        return 0
    fi
    if [[ -n "${BLUEPRINT_PYTHON_PREFERENCE:-}" ]]; then
        printf '%s\n' "${BLUEPRINT_PYTHON_PREFERENCE}"
        return 0
    fi
    printf '%s\n' "venv-first"
}

resolve_python() {
    if declare -p PYTHON_CMD >/dev/null 2>&1; then
        return 0
    fi

    local preference
    preference="$(resolve_python_preference)"
    local root="${ROOT:-$(pwd -P)}"
    local candidate

    if [[ "${preference}" == "uv-first" ]] && resolve_uv_optional; then
        PYTHON_CMD=("${UV_BIN}" run python)
        return 0
    fi

    if [[ -n "${VIRTUAL_ENV:-}" ]]; then
        if candidate="$(venv_python "${VIRTUAL_ENV}")"; then
            PYTHON_CMD=("${candidate}")
            return 0
        fi
    fi

    if candidate="$(venv_python "${root}/.venv")"; then
        PYTHON_CMD=("${candidate}")
        return 0
    fi

    if resolve_uv_optional; then
        PYTHON_CMD=("${UV_BIN}" run python)
        return 0
    fi

    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD=("python3")
        return 0
    fi

    if command -v python >/dev/null 2>&1; then
        PYTHON_CMD=("python")
        return 0
    fi

    echo "error: Python was not found via active venv, .venv, uv/uv.exe, or system PATH" >&2
    exit 1
}

run_python() {
    resolve_python
    "${PYTHON_CMD[@]}" "$@"
}

run_uv_python() {
    resolve_uv
    "${UV_BIN}" run python "$@"
}
