#!/usr/bin/env bash
# Verify all 15 skills have valid YAML frontmatter with name and description
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$(cd "${SCRIPT_DIR}/../../skills" && pwd)"

echo "=== Test: Skill frontmatter validation ==="

EXPECTED_COUNT=15
FOUND=0
FAILURES=0

for skill_dir in "${SKILLS_DIR}"/greetkit-*/; do
    skill_name=$(basename "$skill_dir")
    skill_file="${skill_dir}SKILL.md"

    if [ ! -f "$skill_file" ]; then
        echo "FAIL: ${skill_name} has no SKILL.md"
        FAILURES=$((FAILURES + 1))
        continue
    fi

    # Check for YAML frontmatter
    if ! head -1 "$skill_file" | grep -q "^---"; then
        echo "FAIL: ${skill_name} SKILL.md missing YAML frontmatter"
        FAILURES=$((FAILURES + 1))
        continue
    fi

    # Check for name field
    if ! grep -q "^name:" "$skill_file"; then
        echo "FAIL: ${skill_name} SKILL.md missing 'name:' field"
        FAILURES=$((FAILURES + 1))
        continue
    fi

    # Check for description field
    if ! grep -q "description:" "$skill_file"; then
        echo "FAIL: ${skill_name} SKILL.md missing 'description:' field"
        FAILURES=$((FAILURES + 1))
        continue
    fi

    # Check name matches directory
    declared_name=$(grep "^name:" "$skill_file" | head -1 | sed 's/^name: *//' | tr -d '"' | tr -d "'" | tr -d '\r')
    if [ "$declared_name" != "$skill_name" ]; then
        echo "WARN: ${skill_name} declares name='${declared_name}' (mismatch)"
    fi

    FOUND=$((FOUND + 1))
    echo "  OK: ${skill_name}"
done

echo ""
echo "Found: ${FOUND} skills, Expected: ${EXPECTED_COUNT}, Failures: ${FAILURES}"

if [ "$FAILURES" -gt 0 ]; then
    echo "FAIL: ${FAILURES} skills have issues"
    exit 1
fi

if [ "$FOUND" -ne "$EXPECTED_COUNT" ]; then
    echo "WARN: Expected ${EXPECTED_COUNT} skills, found ${FOUND}"
fi

echo "PASS: All skill frontmatter valid"
