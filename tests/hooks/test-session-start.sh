#!/usr/bin/env bash
# Test that session-start hook produces valid JSON and references the correct skill
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

echo "=== Test: session-start hook output ==="

# Run the hook and capture output
output=$(bash "${PROJECT_ROOT}/hooks/session-start" 2>&1)

# Check it's valid JSON (using python as a portable JSON validator)
echo "$output" | python3 -c "import sys, json; json.load(sys.stdin)" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "FAIL: session-start output is not valid JSON"
    echo "Output: $output"
    exit 1
fi

# Check it contains greetkit-using-skills content
if echo "$output" | grep -q "greetkit-using-skills"; then
    echo "PASS: session-start references greetkit-using-skills"
else
    echo "FAIL: session-start does not reference greetkit-using-skills"
    echo "Output: $output"
    exit 1
fi

# Check it does NOT contain old superpowers references
if echo "$output" | grep -qi "superpowers"; then
    echo "FAIL: session-start still contains 'superpowers' references"
    exit 1
fi

echo "PASS: All session-start tests passed"
