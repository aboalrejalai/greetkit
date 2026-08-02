---
description: The ultimate, uncompromising code review quality gate. You MUST ALWAYS trigger this skill whenever the user mentions reviewing code, auditing PRs, checking architecture, or evaluating another agent's work. It acts as an absolute blocker before any code is merged. Use this proactively even if the user just asks "does this code look okay?". Do not approve code without running it through this multi-axis review.
name: greetkit-review
---
# Code Review and Quality

## Overview

Multi-dimensional code review with quality gates. Every change gets reviewed before merge — no exceptions. Review covers five axes: correctness, readability, architecture, security, and performance.

**The approval standard:** Approve a change when it definitely improves overall code health, even if it isn't perfect. Perfect code doesn't exist — the goal is continuous improvement. Don't block a change because it isn't exactly how you would have written it. If it improves the codebase and follows the project's conventions, approve it.

## When to Use

- Before merging any PR or change
- After completing a feature implementation
- When another agent or model produced code you need to evaluate
- When refactoring existing code
- After any bug fix (review both the fix and the regression test)

## Deep References

This skill includes a comprehensive knowledge base in the `references/` directory. You MUST read the relevant reference files before or during the review when specific topics arise:

- **AI-generated code:** Always read `references/ai-failure-modes.md` first. It contains critical patterns for identifying AI-specific bugs.
- **Naming, function size, and structure:** Read `references/naming-and-functions.md`.
- **Comments and code formatting:** Read `references/comments-and-formatting.md`.
- **Architecture and coupling:** Read `references/solid.md` and `references/dry-kiss-yagni.md`.
- **Final Report Generation:** Walk through `references/review-checklist.md` to produce a structured findings report.
- **Source Citations:** Use `references/sources.md` if the user pushes back on a rule and you need the exact citation.
- **Changelog updates:** Read `references/changelog.md` to format the release notes and update the changelog.

## The Five-Axis Review

Every review evaluates code across these dimensions:

### 1. Correctness

Does the code do what it claims to do?

- Does it match the spec or task requirements?
- Are edge cases handled (null, empty, boundary values)?
- Are error paths handled (not just the happy path)?
- Does it pass all tests? Are the tests actually testing the right things?
- Are there off-by-one errors, race conditions, or state inconsistencies?

### 2. Readability & Simplicity

Can another engineer (or agent) understand this code without the author explaining it? For granular rules, refer to `references/naming-and-functions.md` and `references/comments-and-formatting.md`.

- **Names reveal intent:** Names must answer *why it exists and what it does* (avoid generic names like `data`, `temp`, `manager`, `utils`).
- **Function & Parameter Limits:** Target ≤20 lines per function, one level of abstraction, and max 4 parameters.
- **Comments explain *why*, never *what*:** Remove comments that paraphrase code, commented-out dead code, or step-number scaffolding.
- **Control Flow:** Keep control flow straightforward (avoid nested ternaries, deep callbacks, or clever tricks).

### 3. Architecture

Does the change fit the system's design? For granular SOLID, DRY, KISS, and YAGNI enforcement, defer to the **greetkit-clean-code-guard** skill — it is the dedicated authority for code quality principles.

During review, focus on architecture-level concerns only:
- Does the change respect existing module boundaries?
- Are new dependencies justified and minimal?
- Is the change in the right layer of the system?
- Could this change be split into smaller, independently-deployable units?

### 4. Security

For comprehensive security analysis, invoke the **greetkit-security** skill. During review, perform a quick security sniff test:

- Are secrets committed to version control or logged?
- Is raw user input used in SQL, HTML, or shell commands?
- Are new dependencies from trusted sources?

### 5. Performance

Does the change introduce performance problems? Check against both backend and frontend standards:

- **Core Web Vitals Thresholds (Frontend):**
  - **LCP (Largest Contentful Paint):** ≤ 2.5s
  - **INP (Interaction to Next Paint):** ≤ 200ms
  - **CLS (Cumulative Layout Shift):** ≤ 0.1
- **Database & Query Hygiene:**
  - Check for N+1 query patterns in data fetching.
  - Verify list endpoints enforce pagination (take/skip limits).
- **Asset & Image Optimization:**
  - Verify images specify explicit width/height to prevent layout shifts (CLS).
  - Check for art direction (`<picture>`), modern formats (AVIF/WebP), and `loading="lazy"` on below-fold images.
- **Execution & Render Efficiency:**
  - Any unbounded loops, synchronous I/O in hot paths, or unnecessary component re-renders.
  - Any large objects created repeatedly in high-frequency loops.

### 6. AI-Specific Guardrails

LLM-generated code has systematic failure modes. Always inspect the diff against `references/ai-failure-modes.md` for these key patterns:

- **Error Handling:** Never swallow errors with broad catch-all blocks or return fake empty/null success values.
- **Contract Trust:** Avoid defensive guards for impossible null/type cases already excluded by declared contracts.
- **API Brittleness & Verification:** Verify all imports, package signatures, and 3rd-party payload shapes against actual docs. Never return canned mock returns (`{"status": "ok"}`).
- **Boundary & Dead Code:** Check boundary conditions (off-by-one, null/empty) and strip unused imports/exports.

## Change Sizing

Small, focused changes are easier to review, faster to merge, and safer to deploy. Target these sizes:

```
~100 lines changed   → Good. Reviewable in one sitting.
~300 lines changed   → Acceptable if it's a single logical change.
~1000 lines changed  → Too large. Split it.
```

**What counts as "one change":** A single self-contained modification that addresses one thing, includes related tests, and keeps the system functional after submission. One part of a feature — not the whole feature.

**Splitting strategies when a change is too large:**

| Strategy | How | When |
|----------|-----|------|
| **Stack** | Submit a small change, start the next one based on it | Sequential dependencies |
| **By file group** | Separate changes for groups needing different reviewers | Cross-cutting concerns |
| **Horizontal** | Create shared code/stubs first, then consumers | Layered architecture |
| **Vertical** | Break into smaller full-stack slices of the feature | Feature work |

**When large changes are acceptable:** Complete file deletions and automated refactoring where the reviewer only needs to verify intent, not every line.

**Separate refactoring from feature work.** A change that refactors existing code and adds new behavior is two changes — submit them separately. Small cleanups (variable renaming) can be included at reviewer discretion.

## Refactoring Discipline

**Preserve observable behavior when refactoring.** When asked to clean up, simplify, or refactor existing code, do not change the contract — same inputs produce the same outputs, same exceptions raised, same side effects. If you spot a bug while refactoring, flag it separately. Bug fixes and refactors are two distinct operations — never bundle them in a single change.

## Change Descriptions

Every change needs a description that stands alone in version control history.

**First line:** Short, imperative, standalone. "Delete the FizzBuzz RPC" not "Deleting the FizzBuzz RPC." Must be informative enough that someone searching history can understand the change without reading the diff.

**Body:** What is changing and why. Include context, decisions, and reasoning not visible in the code itself. Link to bug numbers, benchmark results, or design docs where relevant. Acknowledge approach shortcomings when they exist.

**Anti-patterns:** "Fix bug," "Fix build," "Add patch," "Moving code from A to B," "Phase 1," "Add convenience functions."

## Review Process

### Step 1: Understand the Context

Before looking at code, understand the intent:

```
- What is this change trying to accomplish?
- What spec or task does it implement?
- What is the expected behavior change?
```

### Step 2: Review the Tests First

Tests reveal intent and coverage:

```
- Do tests exist for the change?
- Do they test behavior (not implementation details)?
- Are edge cases covered?
- Do tests have descriptive names?
- Would the tests catch a regression if the code changed?
```

### Step 3: Review the Implementation

Walk through the code with the five axes in mind:

```
For each file changed:
1. Correctness: Does this code do what the test says it should?
2. Readability: Can I understand this without help?
3. Architecture: Does this fit the system?
4. Security: Any vulnerabilities?
5. Performance: Any bottlenecks?
```

### Step 4: Categorize Findings (Caveman Format)
You MUST format your findings strictly according to the `assets/review-report.md` template. Do not invent your own output format. Read the template to see the exact formatting rules and emojis required.

### Step 5: Verify the Verification

Before verifying manually, YOU MUST run the appropriate verification script based on the current operating system. Do NOT guess the terminal commands yourself.

- **Linux / macOS** (bash available): run `.greetkit/scripts/bash/verify_project.sh`
  Example: `bash .greetkit/scripts/bash/verify_project.sh`
- **Windows** (PowerShell available): run `.greetkit/scripts/powershell/verify_project.ps1`
  Example: `powershell -ExecutionPolicy Bypass -File .greetkit/scripts/powershell/verify_project.ps1`

Check the author's verification story:

```
- What tests were run?
- Did the build pass?
- Was the change tested manually?
- Are there screenshots for UI changes?
- Is there a before/after comparison?
```

## Multi-Model Review Pattern & Requesting Code Review

Use different models for different review perspectives to catch blind spots. 
**Mandatory times to request review:** After each subagent task, after a major feature, or before a merge.

**1. Get git SHAs:**
```bash
BASE_SHA=$(git rev-parse HEAD~1)
HEAD_SHA=$(git rev-parse HEAD)
```

**2. Dispatch code reviewer subagent:**
Use your Task tool to dispatch a `general-purpose` reviewer agent using this exact prompt template:
```
DESCRIPTION: [Brief summary of what you built]
PLAN_OR_REQUIREMENTS: [What the code should do based on the spec]
BASE_SHA: [Starting commit]
HEAD_SHA: [Ending commit]

Review this code change across the five axes (Correctness, Readability, Architecture, Security, Performance). 
Output your findings using the strict Caveman Format (🔴 bug, 🟡 risk, 🔵 nit, ❓ q).
```

## Code Review Reception (Handling Feedback)

When you receive code review feedback from the user or another agent, remember: code review requires technical evaluation, not emotional performance.

**The Response Pattern:**
1. **READ:** Complete feedback without reacting.
2. **UNDERSTAND:** Restate requirement in your own words.
3. **VERIFY:** Check against codebase reality before implementing.
4. **EVALUATE:** Is it technically sound for THIS codebase?
5. **RESPOND:** Technical acknowledgment or reasoned pushback.
6. **IMPLEMENT:** One item at a time, test each.

**Forbidden Responses:**
- NEVER use performative agreement: "You're absolutely right!", "Great point!", or "Thanks!".
- NEVER blindly say "Let me implement that now" before verifying.

**When to Push Back:**
Push back (with technical reasoning, referencing existing tests/code) when:
- The suggestion breaks existing functionality.
- The reviewer lacks context or violates YAGNI (e.g., asking to build a database for an unused feature).
- It conflicts with previous architectural decisions.

**Acknowledge Correctly:**
If the feedback is correct, just fix it:
✅ "Fixed. [Brief description of what changed]"
✅ "Good catch - [specific issue]. Fixed in [location]."

## Auto-Refactor Mode

**Note:** This is the only mode in which this skill modifies code directly. All other review activity is strictly read-only/advisory, per the skill description above.

By default, this skill is for **reviewing only** (providing findings). However, if the user explicitly commands you to **"review and refactor"**:
1. You are authorized to apply your findings directly to the codebase.
2. The final code must be clean, maintainable, and strictly follow the five-axis rules.
3. Do not split up the code or drastically alter file structures unless requested.
4. Ensure observable behavior is perfectly preserved and all tests remain passing.

## Dead Code Hygiene

After any refactoring or implementation change, check for orphaned code:

1. Identify code that is now unreachable or unused
2. List it explicitly
3. **Ask before deleting:** "Should I remove these now-unused elements: [list]?"

Don't leave dead code lying around — it confuses future readers and agents. But don't silently delete things you're not sure about. When in doubt, ask.

```
DEAD CODE IDENTIFIED:
- formatLegacyDate() in src/utils/date.ts — replaced by formatDate()
- OldTaskCard component in src/components/ — replaced by TaskCard
- LEGACY_API_URL constant in src/config.ts — no remaining references
→ Safe to remove these?
```

## Review Speed

Slow reviews block entire teams. The cost of context-switching to review is less than the waiting cost imposed on others.

- **Respond within one business day** — this is the maximum, not the target
- **Ideal cadence:** Respond shortly after a review request arrives, unless deep in focused coding. A typical change should complete multiple review rounds in a single day
- **Prioritize fast individual responses** over quick final approval. Quick feedback reduces frustration even if multiple rounds are needed
- **Large changes:** Ask the author to split them rather than reviewing one massive changeset

## Handling Disagreements

When resolving review disputes, apply this hierarchy:

1. **Technical facts and data** override opinions and preferences
2. **Style guides** are the absolute authority on style matters
3. **Software design** must be evaluated on engineering principles, not personal preference
4. **Codebase consistency** is acceptable if it doesn't degrade overall health

**Don't accept "I'll clean it up later."** Experience shows deferred cleanup rarely happens. Require cleanup before submission unless it's a genuine emergency. If surrounding issues can't be addressed in this change, require filing a bug with self-assignment.

## Honesty in Review

When reviewing code — whether written by you, another agent, or a human:

- **Don't rubber-stamp.** "LGTM" without evidence of review helps no one.
- **Don't soften real issues.** "This might be a minor concern" when it's a bug that will hit production is dishonest.
- **Quantify problems when possible.** "This N+1 query will add ~50ms per item in the list" is better than "this could be slow."
- **Push back on approaches with clear problems.** Sycophancy is a failure mode in reviews. If the implementation has issues, say so directly and propose alternatives.
- **Accept override gracefully.** If the author has full context and disagrees, defer to their judgment. Comment on code, not people — reframe personal critiques to focus on the code itself.

## Dependency Discipline

Part of code review is dependency review:

**Before adding any dependency:**
1. Does the existing stack solve this? (Often it does.)
2. How large is the dependency? (Check bundle impact.)
3. Is it actively maintained? (Check last commit, open issues.)
4. Does it have known vulnerabilities? (`npm audit`)
5. What's the license? (Must be compatible with the project.)

**Rule:** Prefer standard library and existing utilities over new dependencies. Every dependency is a liability.

## The Review Checklist

When generating your final review report, do not guess the format. You MUST strictly follow the exact checklist and reporting structure provided in `references/review-checklist.md`.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "It works, that's good enough" | Working code that's unreadable, insecure, or architecturally wrong creates debt that compounds. |
| "I wrote it, so I know it's correct" | Authors are blind to their own assumptions. Every change benefits from another set of eyes. |
| "We'll clean it up later" | Later never comes. The review is the quality gate — use it. Require cleanup before merge, not after. |
| "AI-generated code is probably fine" | AI code needs more scrutiny, not less. It's confident and plausible, even when wrong. |
| "The tests pass, so it's good" | Tests are necessary but not sufficient. They don't catch architecture problems, security issues, or readability concerns. |

## Red Flags

- PRs merged without any review
- Review that only checks if tests pass (ignoring other axes)
- "LGTM" without evidence of actual review
- Security-sensitive changes without security-focused review
- Large PRs that are "too big to review properly" (split them)
- No regression tests with bug fix PRs
- Review comments without Caveman severity emojis (🔴, 🟡, 🔵) — makes it unclear what's required vs optional
- Accepting "I'll fix it later" — it never happens

## Verification

After review is complete, verify that:

- [ ] All `🔴 bug` (Critical) issues are strictly resolved.
- [ ] All `🟡 risk` (Important) issues are resolved or explicitly deferred with deep justification.
- [ ] Tests pass and build succeeds.
- [ ] The verification story is documented (what changed, how it was verified).

## Execution Performance Summary
When completing a review cycle, include a brief performance summary at the end of your review report. The exact table format you must use is located in `assets/review-report.md`. Do not recreate it from memory.

## Sync and Archive (Finalization)
If AGENTS.md does not exist in the project root, or contains no `<!-- GREETKIT START -->` / `<!-- GREETKIT END -->` markers, skip this entire section silently — do not create AGENTS.md and do not treat this as an error.

First, identify the active plan from `AGENTS.md` (between the `<!-- GREETKIT START -->` and `<!-- GREETKIT END -->` tags).
If your review determines that the code is correct, perfectly clean, and ALL tasks in the active plan are marked as complete (`[x]`), you assume responsibility for final cleanup:
1. **Changelog Update:** Prior to clearing context, detect and locate the project's `CHANGELOG.md` file (create it in the workspace root if it does not exist).
   - Determine the next version number (by inspecting the current latest version in `CHANGELOG.md` or application config files like `package.json`, `setup.py`, `pyproject.toml`, or `Cargo.toml`). If no version is found, default to `1.0.0`. Propose the version increment to the user.
   - Extract all implemented changes by reviewing the completed tasks in the active plan and running `git log` or `git diff` for the implementation period.
   - Compose a new, detailed release entry following the structure, categories, and corporate styling defined in `references/changelog.md`.
   - Prepend the new entry to `CHANGELOG.md`.
2. **Clear Context:** Remove the active plan reference from `AGENTS.md` (leave the markers empty) to cleanly reset the context for future tasks. (Do not move or archive the completed plan file; leave it in the `greetkit/plans/` directory so the sequence numbering continues correctly).

## Technical Debt Harvesting
If the user asks to "check technical debt" or run "review-debt", you must search the codebase for `// shortcut:` or `# shortcut:` comments. Group them by file and report the exact simplifications made. Tag any shortcut that lacks a documented "upgrade trigger" as a silent risk.

## Orchestration Hand-off
You are part of the `greetkit-plan` -> `greetkit-implement` -> `greetkit-review` triad.
When you finish presenting your review findings, you MUST end your response with a clear, natural question in Arabic asking the user for permission to trigger the next step.

1. **If issues were found:** Ask for permission to trigger the `greetkit-implement` skill to fix them.
   Ask: *"Shall I trigger the greetkit-implement skill so we can fix the errors?"* (Note: Translate to natural Arabic when speaking to the user).
2. **If code is clean but tasks remain:** Ask to continue implementation.
   Ask: *"The code is clean. Shall I trigger the greetkit-implement skill to continue with the remaining tasks?"* (Note: Translate to natural Arabic when speaking to the user).
3. **If ALL tasks are done and code is clean:** Update the changelog, clear the context, and announce completion.
   Ask: *"The code is clean, all tasks are completed, and the changelog has been updated. Shall we start something new?"* (Note: Translate to natural Arabic when speaking to the user).
4. **Documentation Changes:** If the changes exclusively involved documentation (`.md` files), DO NOT review them here. Hand off to `docs-guard`.
   Ask: *"The modifications are strictly documentation-related. Shall I trigger the docs-guard skill to verify them?"* (Note: Translate to natural Arabic when speaking to the user).
