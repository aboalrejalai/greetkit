#!/usr/bin/env bash
# Simple syntax check for shell scripts in hooks/ and scripts/
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

echo "=== Test: Shell script syntax check ==="

FAILURES=0

for script in "${PROJECT_ROOT}/hooks/session-start" "${PROJECT_ROOT}/scripts/bash"/*.sh; do
    if [ -f "$script" ]; then
        if bash -n "$script"; then
            echo "  OK: $(basename "$script")"
        else
            echo "  FAIL: $(basename "$script") syntax error"
            FAILURES=$((FAILURES + 1))
        fi
    fi
done

if [ "$FAILURES" -gt 0 ]; then
    echo "FAIL: ${FAILURES} scripts have syntax errors"
    exit 1
fi

echo "PASS: All shell scripts passed syntax check"
