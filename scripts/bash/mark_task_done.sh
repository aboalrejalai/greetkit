#!/usr/bin/env bash
set -euo pipefail

# ------------------------------------------------------------
# mark_task_done.sh — Bash equivalent of mark_task_done.ps1
# Usage: bash mark_task_done.sh "<TASK-ID>" "<plan-path>"
# ------------------------------------------------------------

TASK_ID=""
PLAN_PATH=""

# Parse positional arguments
for arg in "$@"; do
    if [ -z "$TASK_ID" ]; then
        TASK_ID="$arg"
    elif [ -z "$PLAN_PATH" ]; then
        PLAN_PATH="$arg"
    fi
done

if [ -z "$TASK_ID" ] || [ -z "$PLAN_PATH" ]; then
    echo "Usage: bash mark_task_done.sh \"TASK-001\" \"greetkit/plans/001-feature-name.md\"" >&2
    exit 1
fi

if [ ! -f "$PLAN_PATH" ]; then
    echo "Error: Plan file not found: $PLAN_PATH" >&2
    exit 1
fi

ORIGINAL=$(cat "$PLAN_PATH")

# Replace "- [ ] TASK_ID" (case-insensitive on the brackets) with "- [x] TASK_ID"
# Preserves any tags or text that follow the task ID.
UPDATED=$(echo "$ORIGINAL" | sed -E "s/([-*] \[)[[:space:]]*(\] )($TASK_ID)/\1x\2\3/I" 2>/dev/null || \
          echo "$ORIGINAL" | sed -E "s/([-*] \[)[[:space:]]*(\] )($TASK_ID)/\1x\2\3/")

if [ "$ORIGINAL" = "$UPDATED" ]; then
    echo "Warning: Task '$TASK_ID' not found or already marked as done in $PLAN_PATH"
else
    printf '%s' "$UPDATED" > "$PLAN_PATH"
    echo "Successfully marked '$TASK_ID' as complete in $PLAN_PATH"
fi
