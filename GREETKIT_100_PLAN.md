# GreetKit 100% Readiness — Implementation Plan

> **Execution model:** Work through this plan **phase-by-phase, in order**.
> Each phase is self-contained. After completing a phase, verify before moving to the next.
> All paths are relative to the GreetKit project root: `c:\Users\Abo Alrejal\Desktop\greetkit\`

---

## Phase 1: Critical — Fix the Bootstrap Injection Hook

**Why first:** Without this fix, the entire skill system is dead on arrival. The session-start hook tries to read a non-existent skill name, so no agent ever receives the bootstrap context.

### Task 1.1: Fix skill path in `hooks/session-start`

**File:** `hooks/session-start` (line 11)

**Before:**
```bash
using_greetkit_content=$(cat "${PLUGIN_ROOT}/skills/greetkit-using-system/SKILL.md" 2>&1 || echo "Error reading greetkit-using-system skill. Please ensure the skill exists.")
```

**After:**
```bash
using_greetkit_content=$(cat "${PLUGIN_ROOT}/skills/greetkit-using-skills/SKILL.md" 2>&1 || echo "Error reading greetkit-using-skills skill. Please ensure the skill exists.")
```

### Task 1.2: Fix context message text in `hooks/session-start`

**File:** `hooks/session-start` (line 25)

**Before:**
```bash
session_context="<EXTREMELY_IMPORTANT>\nYou are operating within GreetKit.\n\n**Below is the full content of your 'greetkit-using-system' skill - your core instruction manual. Read it completely before proceeding.**\n\n${using_greetkit_escaped}\n</EXTREMELY_IMPORTANT>"
```

**After:**
```bash
session_context="<EXTREMELY_IMPORTANT>\nYou are operating within GreetKit.\n\n**Below is the full content of your 'greetkit-using-skills' skill - your core instruction manual. Read it completely before proceeding.**\n\n${using_greetkit_escaped}\n</EXTREMELY_IMPORTANT>"
```

### Task 1.3: Verify the fix

Run the hook manually to confirm it reads the correct file:
```bash
# From project root
bash hooks/session-start
```
Expected: JSON output containing the full content of `greetkit-using-skills/SKILL.md`, no error messages.

---

## Phase 2: Platform Plugin Migration

**Why:** Superpowers supports 6 platforms (Claude Code, Codex, Cursor, Kimi, OpenCode, Pi) plus Gemini Extension. GreetKit currently only has Claude Code hooks. We need to port all platform configs.

### Task 2.1: Create `.claude-plugin/` directory

**Action:** Copy `_archive/superpowers-main/.claude-plugin/` → `.claude-plugin/`

**Then modify `.claude-plugin/plugin.json`:**

| Field | Old Value | New Value |
|---|---|---|
| `name` | `"superpowers"` | `"greetkit"` |
| `description` | `"Core skills library for Claude Code: TDD, debugging..."` | `"GreetKit: Intent-Driven Development skills for coding agents — spec, plan, implement, review"` |
| `version` | `"6.2.0"` | `"1.0.0"` |
| `author.name` | `"Jesse Vincent"` | *(your name)* |
| `author.email` | `"jesse@fsck.com"` | *(your email)* |
| `homepage` | `"https://github.com/obra/superpowers"` | *(your repo URL)* |
| `repository` | `"https://github.com/obra/superpowers"` | *(your repo URL)* |

**Then modify `.claude-plugin/marketplace.json`:**

| Field | Old Value | New Value |
|---|---|---|
| `name` | `"superpowers-dev"` | `"greetkit"` |
| `description` | `"Development marketplace for..."` | `"GreetKit: Intent-Driven Development skills marketplace"` |
| `owner.name` | `"Jesse Vincent"` | *(your name)* |
| `owner.email` | `"jesse@fsck.com"` | *(your email)* |
| `plugins[0].name` | `"superpowers"` | `"greetkit"` |
| `plugins[0].description` | *(old text)* | `"GreetKit: Intent-Driven Development skills for coding agents"` |
| `plugins[0].version` | `"6.2.0"` | `"1.0.0"` |
| `plugins[0].author.name` | `"Jesse Vincent"` | *(your name)* |
| `plugins[0].author.email` | `"jesse@fsck.com"` | *(your email)* |

### Task 2.2: Create `.codex-plugin/` directory

**Action:** Copy `_archive/superpowers-main/.codex-plugin/` → `.codex-plugin/`

**Then modify `.codex-plugin/plugin.json`:**

| Field | Old Value | New Value |
|---|---|---|
| `name` | `"superpowers"` | `"greetkit"` |
| `version` | `"6.2.0"` | `"1.0.0"` |
| `description` | `"An agentic skills framework & software development..."` | `"GreetKit: Intent-Driven Development (IDD) skills framework for coding agents"` |
| `author.name` | `"Jesse Vincent"` | *(your name)* |
| `author.email` | `"jesse@fsck.com"` | *(your email)* |
| `author.url` | `"https://github.com/obra"` | *(your GitHub URL)* |
| `homepage` | `"https://github.com/obra/superpowers"` | *(your repo URL)* |
| `repository` | `"https://github.com/obra/superpowers"` | *(your repo URL)* |
| `keywords` | `["brainstorming", "subagent-driven-development", ...]` | `["greetkit", "idd", "skills", "spec", "plan", "implement", "review"]` |
| `interface.displayName` | `"Superpowers"` | `"GreetKit"` |
| `interface.shortDescription` | `"Planning, TDD, debugging..."` | `"Intent-Driven Development: spec, plan, implement, review workflows for coding agents"` |
| `interface.longDescription` | *(old text)* | `"Use GreetKit to guide agent work through intent-driven spec writing, architectural planning, disciplined implementation, and uncompromising code review."` |
| `interface.developerName` | `"Jesse Vincent"` | *(your name)* |
| `interface.defaultPrompt` | *(old text)* | `["I've got an idea for something I'd like to build.", "Let's plan a new feature for this project."]` |
| `interface.websiteURL` | `"https://github.com/obra/superpowers"` | *(your repo URL)* |
| `interface.privacyPolicyURL` | *(GitHub generic)* | *(your privacy policy URL or remove)* |
| `interface.termsOfServiceURL` | *(GitHub generic)* | *(your terms URL or remove)* |
| `interface.brandColor` | `"#F59E0B"` | *(your brand color)* |
| `interface.composerIcon` | `"./assets/superpowers-small.svg"` | `"./assets/greetkit-icon.svg"` *(create or replace)* |
| `interface.logo` | `"./assets/app-icon.png"` | `"./assets/greetkit-logo.png"` *(create or replace)* |

### Task 2.3: Create `.cursor-plugin/` directory

**Action:** Copy `_archive/superpowers-main/.cursor-plugin/` → `.cursor-plugin/`

**Then modify `.cursor-plugin/plugin.json`:**

| Field | Old Value | New Value |
|---|---|---|
| `name` | `"superpowers"` | `"greetkit"` |
| `displayName` | `"Superpowers"` | `"GreetKit"` |
| `description` | `"Core skills library: TDD, debugging..."` | `"GreetKit: Intent-Driven Development skills for coding agents"` |
| `version` | `"6.2.0"` | `"1.0.0"` |
| `author.name` | `"Jesse Vincent"` | *(your name)* |
| `author.email` | `"jesse@fsck.com"` | *(your email)* |
| `homepage` | `"https://github.com/obra/superpowers"` | *(your repo URL)* |
| `repository` | `"https://github.com/obra/superpowers"` | *(your repo URL)* |
| `keywords` | `["skills", "tdd", ...]` | `["greetkit", "idd", "skills", "spec", "plan", "implement", "review"]` |

> **Note:** The `hooks` field points to `"./hooks/hooks-cursor.json"`. We need to also copy the Cursor hooks config.

### Task 2.4: Create Cursor hooks config

**Action:** Copy `_archive/superpowers-main/hooks/hooks-cursor.json` → `hooks/hooks-cursor.json`

This file is already compatible — it points to `./hooks/run-hook.cmd session-start` which we already have. No changes needed.

### Task 2.5: Create `.kimi-plugin/` directory

**Action:** Copy `_archive/superpowers-main/.kimi-plugin/` → `.kimi-plugin/`

**Then modify `.kimi-plugin/plugin.json`:**

| Field | Old Value | New Value |
|---|---|---|
| `name` | `"superpowers"` | `"greetkit"` |
| `version` | `"6.2.0"` | `"1.0.0"` |
| `description` | `"An agentic skills framework..."` | `"GreetKit: Intent-Driven Development skills framework"` |
| `author.name` | `"Jesse Vincent"` | *(your name)* |
| `author.email` | `"jesse@fsck.com"` | *(your email)* |
| `homepage` | `"https://github.com/obra/superpowers"` | *(your repo URL)* |
| `keywords` | `["brainstorming", "subagent-driven-development", ...]` | `["greetkit", "idd", "skills", "spec", "plan", "implement", "review"]` |
| `sessionStart.skill` | `"using-superpowers"` | `"greetkit-using-skills"` |
| `skillInstructions` | All references to `"Superpowers"` | Replace with `"GreetKit"` |
| `skillInstructions` | All references to `"superpowers"` in tool mappings | Replace with `"greetkit"` |
| `interface.displayName` | `"Superpowers"` | `"GreetKit"` |
| `interface.shortDescription` | *(old text)* | `"Intent-Driven Development: spec, plan, implement, review workflows"` |
| `interface.longDescription` | *(old text)* | `"Use GreetKit to guide agent work through intent-driven spec writing, architectural planning, disciplined implementation, and uncompromising code review."` |
| `interface.developerName` | `"Jesse Vincent"` | *(your name)* |
| `interface.websiteURL` | `"https://github.com/obra/superpowers"` | *(your repo URL)* |

### Task 2.6: Create `.opencode/` directory

**Action:** Copy `_archive/superpowers-main/.opencode/` → `.opencode/`

**Modify `.opencode/INSTALL.md`:**
- Replace all occurrences of `superpowers` → `greetkit`
- Replace all occurrences of `Superpowers` → `GreetKit`
- Replace all GitHub URLs `github.com/obra/superpowers` → *(your repo URL)*

**Modify `.opencode/plugins/superpowers.js`:**
- **Rename file** to `.opencode/plugins/greetkit.js`
- Line 67: Change `'using-superpowers'` → `'greetkit-using-skills'`
- Line 76-87: Change `"**Tool Mapping for OpenCode:**"` heading — replace `"Superpowers"` → `"GreetKit"`
- Line 89-97: Change `"You have superpowers."` → `"You are operating within GreetKit."`, change all `"superpowers"` → `"greetkit"`, change `"using-superpowers"` → `"greetkit-using-skills"`

### Task 2.7: Create `.pi/` directory

**Action:** Copy `_archive/superpowers-main/.pi/` → `.pi/`

**Modify `.pi/extensions/superpowers.ts`:**
- **Rename file** to `.pi/extensions/greetkit.ts`
- Line 7: Change `BOOTSTRAP_MARKER` from `"superpowers:using-superpowers bootstrap for pi"` → `"greetkit:greetkit-using-skills bootstrap for pi"`
- Line 12: Change skill path from `"using-superpowers"` → `"greetkit-using-skills"`
- Line 70: Change `"You have superpowers."` → `"You are operating within GreetKit."`
- Line 71: Change `"using-superpowers"` → `"greetkit-using-skills"`, `"Pi session"` stays
- Line 89-97: `piToolMapping()` — replace all `"Superpowers"` → `"GreetKit"`, `"superpowers"` → `"greetkit"`

### Task 2.8: Create `gemini-extension.json`

**Action:** Create `gemini-extension.json` in project root with:

```json
{
  "name": "greetkit",
  "description": "GreetKit: Intent-Driven Development skills for coding agents",
  "version": "1.0.0",
  "contextFileName": "GEMINI.md"
}
```

> **ACTION REQUIRED:** Check if `_archive/superpowers-main/GEMINI.md` exists. If yes, copy it to project root and replace all superpowers references. If no, create a minimal `GEMINI.md` that points to `skills/greetkit-using-skills/SKILL.md`.

### Task 2.9: Create `package.json`

**Action:** Create `package.json` in project root (alongside existing `pyproject.toml`):

```json
{
  "name": "greetkit",
  "version": "1.0.0",
  "description": "GreetKit: Intent-Driven Development skills and runtime bootstrap for coding agents",
  "type": "module",
  "main": ".opencode/plugins/greetkit.js",
  "keywords": [
    "pi-package",
    "greetkit",
    "idd",
    "skills",
    "spec",
    "plan",
    "implement",
    "review"
  ],
  "pi": {
    "extensions": [
      "./.pi/extensions/greetkit.ts"
    ],
    "skills": [
      "./skills"
    ]
  }
}
```

### Task 2.10: Verify all plugin configs

After all plugins are created, verify:
- [ ] Each `plugin.json` has `"name": "greetkit"` and `"version": "1.0.0"`
- [ ] No file contains the string `"superpowers"` (except in `_archive/`)
- [ ] All `sessionStart` fields point to `"greetkit-using-skills"`
- [ ] All skill paths point to `"./skills/"`

---

## Phase 3: Skill Conflict Resolution

### Task 3.1: Fix dead `premium-frontend-ui` references in `greetkit-frame-animation`

**File:** `skills/greetkit-frame-animation/SKILL.md`

Replace every occurrence of `premium-frontend-ui` with standalone guidance since the skill doesn't exist in GreetKit:

**Line 13 (in YAML description):**
- **Before:** `Pairs with the premium-frontend-ui skill for creative philosophy and design-level polish.`
- **After:** *(Remove this line entirely from the YAML description)*

**Lines 23-27 (Design Companion block):**
- **Before:**
```
> **Design Companion:** This skill provides the *technical implementation* for scroll-driven motion.
> For the *creative philosophy*, design principles, and premium aesthetics that should guide **how**
> and **when** to animate, always cross-reference the **premium-frontend-ui** skill.
> Together they form a complete approach: premium-frontend-ui decides the **what** and **why**;
> this skill delivers the **how**.
```
- **After:**
```
> **Design Philosophy:** This skill provides the *technical implementation* for scroll-driven motion.
> Animation should enhance, never overwhelm. Use restraint with motion — animate only
> `transform` and `opacity`, keep durations subtle (0.3s–0.8s), and always respect
> `prefers-reduced-motion`. The best scroll animations feel natural and invisible.
```

**Line 129:**
- **Before:** `- **Premium polish**: follow the **premium-frontend-ui** skill principles for motion timing, easing curves, and restraint — animation should enhance, never overwhelm`
- **After:** `- **Premium polish**: use restraint with motion timing and easing curves — animation should enhance, never overwhelm`

**Lines 146-151 (Related Skills table):**
- **Delete the entire "Related Skills" section** (lines 146-151)

### Task 3.2: Slim down `greetkit-review` Architecture axis

**File:** `skills/greetkit-review/SKILL.md`

The review's Axis 3 (Architecture, lines 56-63) currently inlines SOLID/DRY/KISS/YAGNI rules that overlap with `greetkit-clean-code-guard`. **Delegate instead of duplicate:**

**Before (lines 56-63):**
```markdown
### 3. Architecture

Does the change fit the system's design? Apply SOLID, DRY, KISS, and YAGNI. For deep architectural audits, refer to `references/solid.md` and `references/dry-kiss-yagni.md`.

- **Single Responsibility & Coupling (SRP/DIP):** One actor per module; abstractions live with the client.
- **Extensibility (OCP/LSP):** Extend via polymorphic dispatch; subclasses must never refuse parent contracts.
- **DRY vs Knowledge:** Delete duplicated *knowledge*, not duplicated *text*.
- **YAGNI & Complexity:** Cyclomatic complexity ≤10, nesting depth ≤5. Flag speculative flags, unused abstractions, or reinventing standard libraries.
```

**After:**
```markdown
### 3. Architecture

Does the change fit the system's design? For granular SOLID, DRY, KISS, and YAGNI enforcement, defer to the **greetkit-clean-code-guard** skill — it is the dedicated authority for code quality principles.

During review, focus on architecture-level concerns only:
- Does the change respect existing module boundaries?
- Are new dependencies justified and minimal?
- Is the change in the right layer of the system?
- Could this change be split into smaller, independently-deployable units?
```

### Task 3.3: Slim down `greetkit-review` Security axis

**File:** `skills/greetkit-review/SKILL.md`

The review's Axis 4 (Security, lines 65-77) already correctly delegates to `greetkit-security` on line 67, but then re-lists specific checks. **Keep the delegation, trim the checklist:**

**Before (lines 65-77):**
```markdown
### 4. Security

For detailed security guidance, see `greetkit-security`. Does the change introduce vulnerabilities?

- Is user input validated and sanitized?
- Are secrets kept out of code, logs, and version control?
- Is authentication/authorization checked where needed?
- Are SQL queries parameterized (no string concatenation)?
- Are outputs encoded to prevent XSS?
- Are dependencies from trusted sources with no known vulnerabilities?
- Is data from external sources (APIs, logs, user content, config files) treated as untrusted?
- Are external data flows validated at system boundaries before use in logic or rendering?
```

**After:**
```markdown
### 4. Security

For comprehensive security analysis, invoke the **greetkit-security** skill. During review, perform a quick security sniff test:

- Are secrets committed to version control or logged?
- Is raw user input used in SQL, HTML, or shell commands?
- Are new dependencies from trusted sources?
```

---

## Phase 4: Infrastructure Migration

### Task 4.1: Copy documentation from Superpowers

**Action:** Copy these files, then replace `superpowers`/`Superpowers` → `greetkit`/`GreetKit`:

| Source | Destination | Modifications |
|---|---|---|
| `_archive/superpowers-main/docs/porting-to-a-new-harness.md` | `docs/porting-to-a-new-harness.md` | Replace all `superpowers` → `greetkit`, `Superpowers` → `GreetKit`, `using-superpowers` → `greetkit-using-skills`, update all GitHub URLs |
| `_archive/superpowers-main/docs/testing.md` | `docs/testing.md` | Replace all `superpowers` → `greetkit`, update skill names, paths |
| `_archive/superpowers-main/docs/windows/polyglot-hooks.md` | `docs/windows/polyglot-hooks.md` | Replace all `superpowers` → `greetkit` |
| `_archive/superpowers-main/docs/README.kimi.md` | `docs/README.kimi.md` | Replace all `superpowers` → `greetkit` |
| `_archive/superpowers-main/docs/README.opencode.md` | `docs/README.opencode.md` | Replace all `superpowers` → `greetkit` |

### Task 4.2: Copy automation scripts from Superpowers

**Action:** Copy these scripts, then replace references:

| Source | Destination | Modifications |
|---|---|---|
| `_archive/superpowers-main/scripts/bump-version.sh` | `scripts/bump-version.sh` | Replace `superpowers` → `greetkit`, update file paths to match new plugin directory names |
| `_archive/superpowers-main/scripts/lint-shell.sh` | `scripts/lint-shell.sh` | Replace `superpowers` → `greetkit` |

> **Skip:** `scripts/package-codex-plugin.sh` and `scripts/sync-to-codex-plugin.sh` — these are Superpowers-specific packaging scripts. Port them later if needed.

### Task 4.3: Copy `.gitattributes`

**Action:** Copy `_archive/superpowers-main/.gitattributes` → `.gitattributes`

No modifications needed — the content is generic (LF enforcement for shell/md/json files).

### Task 4.4: Create `.version-bump.json`

**Action:** Create `.version-bump.json` in project root:

```json
{
  "files": [
    { "path": "package.json", "field": "version" },
    { "path": ".claude-plugin/plugin.json", "field": "version" },
    { "path": ".cursor-plugin/plugin.json", "field": "version" },
    { "path": ".codex-plugin/plugin.json", "field": "version" },
    { "path": ".kimi-plugin/plugin.json", "field": "version" },
    { "path": ".claude-plugin/marketplace.json", "field": "plugins.0.version" },
    { "path": "gemini-extension.json", "field": "version" }
  ],
  "audit": {
    "exclude": [
      "CHANGELOG.md",
      "RELEASE-NOTES.md",
      "node_modules",
      ".git",
      ".version-bump.json",
      "scripts/bump-version.sh",
      "_archive"
    ]
  }
}
```

### Task 4.5: Copy GitHub templates

**Action:** Copy the following files:

| Source | Destination | Modifications |
|---|---|---|
| `_archive/superpowers-main/.github/FUNDING.yml` | `.github/FUNDING.yml` | Update with your funding info |
| `_archive/superpowers-main/.github/PULL_REQUEST_TEMPLATE.md` | `.github/PULL_REQUEST_TEMPLATE.md` | Replace `superpowers` → `greetkit` |
| `_archive/superpowers-main/.github/ISSUE_TEMPLATE/bug_report.md` | `.github/ISSUE_TEMPLATE/bug_report.md` | Replace `superpowers` → `greetkit` |
| `_archive/superpowers-main/.github/ISSUE_TEMPLATE/config.yml` | `.github/ISSUE_TEMPLATE/config.yml` | Replace `superpowers` → `greetkit` |
| `_archive/superpowers-main/.github/ISSUE_TEMPLATE/feature_request.md` | `.github/ISSUE_TEMPLATE/feature_request.md` | Replace `superpowers` → `greetkit` |
| `_archive/superpowers-main/.github/ISSUE_TEMPLATE/platform_support.md` | `.github/ISSUE_TEMPLATE/platform_support.md` | Replace `superpowers` → `greetkit` |

### Task 4.6: Create/Replace assets

**Action:**
1. Create `assets/` directory in project root
2. If you have GreetKit-specific icons/logos, place them as:
   - `assets/greetkit-icon.svg` (for Codex composer icon)
   - `assets/greetkit-logo.png` (for Codex logo)
3. If you don't have custom branding yet, copy the Superpowers assets as temporary placeholders:
   - `_archive/superpowers-main/assets/superpowers-small.svg` → `assets/greetkit-icon.svg`
   - `_archive/superpowers-main/assets/app-icon.png` → `assets/greetkit-logo.png`

> **ACTION REQUIRED:** Provide your actual brand assets when ready. The temporary assets are placeholders only.

### Task 4.7: Verify `.greetkit/` scripts path references

The skills reference `.greetkit/scripts/` paths (e.g., `check-prerequisites.ps1`, `setup-plan.sh`, `verify_project.sh`). These scripts **already exist** in the project at `scripts/powershell/` and `scripts/bash/`.

**The `.greetkit/` path convention:** Skills expect these scripts to exist at `.greetkit/scripts/` relative to the **target project** where GreetKit is installed — not in the GreetKit plugin repo itself. This means:
- The `scripts/` directory in GreetKit root contains the **source scripts** that get copied to user projects during `greetkit init`
- Skills reference `.greetkit/scripts/` because that's where the scripts land in the user's project

**Verification:** Confirm that `greetkit init` (or the CLI setup) copies `scripts/` → `.greetkit/scripts/` in the target project.

> **ACTION REQUIRED:** Verify that the `greetkit init` command (in `src/greetkit_cli/`) correctly copies the `scripts/`, `templates/`, and `memory/` directories into the user's `.greetkit/` directory. If `greetkit init` doesn't do this, it needs updating — but that is a separate CLI task, not part of this plan.

---

## Phase 5: Testing Infrastructure

### Task 5.1: Create `tests/` directory structure

Create this structure:
```
tests/
├── hooks/
│   └── test-session-start.sh
├── skills/
│   └── test-skill-frontmatter.sh
└── shell-lint/
    └── test-shell-scripts.sh
```

### Task 5.2: Write `tests/hooks/test-session-start.sh`

```bash
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
```

### Task 5.3: Write `tests/skills/test-skill-frontmatter.sh`

```bash
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
    declared_name=$(grep "^name:" "$skill_file" | head -1 | sed 's/^name: *//' | tr -d '"' | tr -d "'")
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
```

### Task 5.4: Update `docs/testing.md`

Write a new `docs/testing.md` for GreetKit that describes:
- The `tests/hooks/` directory and how to run the session-start test
- The `tests/skills/` directory and how to run the frontmatter validation
- How to run all tests together
- Note: No eval suite (LLM behavior testing) yet — just infrastructure tests

---

## Phase 6: Final Polish

### Task 6.1: Update `README.md`

**File:** `README.md`

Rewrite to be comprehensive. Include:
- What GreetKit is (IDD skills framework)
- Supported platforms (Claude Code, Codex, Cursor, Kimi, OpenCode, Pi, Gemini CLI)
- Installation instructions for each platform
- The 15 skills with one-line descriptions
- The workflow diagram (Spec → Plan → Tasks → Implement → Review)
- Link to `docs/philosophy.md`
- Link to `CHANGELOG.md`
- License badge

### Task 6.2: Update `AGENTS.md`

**File:** `AGENTS.md`

Replace current minimal content with:

```markdown
<!-- GREETKIT START -->
You are working within the GreetKit project repository.

GreetKit is an Intent-Driven Development (IDD) skills framework for coding agents.
It provides 15 specialized skills organized around the IDD lifecycle:
Spec → Plan → Tasks → Implement → Review

For the full skill routing map, read `skills/greetkit-using-skills/SKILL.md`.
For the project philosophy, read `docs/philosophy.md`.
For the current plan (if any), check `.gk-plan/` directory.
<!-- GREETKIT END -->
```

### Task 6.3: Global superpowers reference sweep

Run a final grep across the entire project (excluding `_archive/`) to ensure no stale `superpowers` references remain:

```bash
grep -ri "superpowers" --include="*.md" --include="*.json" --include="*.js" --include="*.ts" --include="*.sh" --include="*.ps1" --include="*.yaml" --include="*.yml" . | grep -v "_archive/" | grep -v "node_modules/"
```

Fix any remaining occurrences.

### Task 6.4: Update `.gitignore`

Ensure `.gitignore` includes:
```
node_modules/
.venv/
_archive/
*.pyc
__pycache__/
```

### Task 6.5: Verify complete file tree

After all phases, the project root should contain:

```
greetkit/
├── .agents/skills/              # Agent skill discovery
├── .claude-plugin/              # [NEW] Claude Code plugin config
│   ├── marketplace.json
│   └── plugin.json
├── .codex-plugin/               # [NEW] Codex plugin config
│   └── plugin.json
├── .cursor-plugin/              # [NEW] Cursor plugin config
│   └── plugin.json
├── .github/                     # [UPDATED] GitHub templates
│   ├── FUNDING.yml
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
├── .kimi-plugin/                # [NEW] Kimi plugin config
│   └── plugin.json
├── .opencode/                   # [NEW] OpenCode plugin
│   ├── INSTALL.md
│   └── plugins/greetkit.js
├── .pi/                         # [NEW] Pi extension
│   └── extensions/greetkit.ts
├── .gitattributes               # [NEW] LF enforcement
├── .gitignore
├── .version-bump.json           # [NEW] Version sync config
├── AGENTS.md                    # [UPDATED]
├── CHANGELOG.md
├── LICENSE
├── README.md                    # [UPDATED]
├── SECURITY.md
├── SKILLS_EVOLUTION_BLUEPRINT.md
├── assets/                      # [NEW] Brand assets
│   ├── greetkit-icon.svg
│   └── greetkit-logo.png
├── docs/
│   ├── README.kimi.md           # [NEW]
│   ├── README.opencode.md       # [NEW]
│   ├── philosophy.md
│   ├── porting-to-a-new-harness.md  # [NEW]
│   ├── testing.md               # [NEW]
│   └── windows/
│       └── polyglot-hooks.md    # [NEW]
├── gemini-extension.json        # [NEW]
├── hooks/
│   ├── hooks-cursor.json        # [NEW]
│   ├── hooks.json               # (existing)
│   ├── run-hook.cmd             # (existing)
│   └── session-start            # [FIXED]
├── package.json                 # [NEW]
├── pyproject.toml               # (existing)
├── scripts/                     # (existing — source scripts)
├── skills/                      # (existing — 15 skills)
│   ├── greetkit-analyze/
│   ├── greetkit-clean-code-guard/
│   ├── greetkit-constitution/
│   ├── greetkit-docs-guard/
│   ├── greetkit-frame-animation/  # [FIXED dead refs]
│   ├── greetkit-implement/
│   ├── greetkit-plan/
│   ├── greetkit-review/           # [SLIMMED overlaps]
│   ├── greetkit-security/
│   ├── greetkit-source-driven/
│   ├── greetkit-spec/
│   ├── greetkit-tasks/
│   ├── greetkit-test-guard/
│   ├── greetkit-using-skills/
│   └── greetkit-webapp-testing/
├── skills-lock.json
├── src/greetkit_cli/            # (existing)
├── templates/                   # (existing)
└── tests/                       # [NEW]
    ├── hooks/
    ├── skills/
    └── shell-lint/
```

---

## Post-Completion Checklist

- [ ] Phase 1: session-start hook fixed and verified
- [ ] Phase 2: All 6 platform plugins + Gemini extension created and rebranded
- [ ] Phase 3: Dead skill references removed, review/guard overlap resolved
- [ ] Phase 4: Docs, scripts, configs, assets, GitHub templates migrated
- [ ] Phase 5: Basic test suite created and passing
- [ ] Phase 6: README, AGENTS.md, .gitattributes polished
- [ ] Final grep: zero `superpowers` references outside `_archive/`
- [ ] `_archive/` is now safe to delete
