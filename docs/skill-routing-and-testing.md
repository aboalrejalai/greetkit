# GreetKit Skill Routing, Lifecycle & Local Testing Guide

This guide explains:
1. The exact dependency chain and rules between all 15 skills.
2. What files get created in a project when using GreetKit.
3. How to test GreetKit locally on a real project across different IDEs/harnesses.
4. The technical reality of platform plugin manifests and marketplaces.

---

## 1. Skill Dependency & Routing Map

GreetKit skills are organized into 5 phases. While some skills can be invoked independently, the core IDD workflow has strict prerequisites:

```
[Phase 1: DEFINE]
greetkit-spec (PRD & boundaries)
       │
       ▼
[Phase 2: PLAN]
greetkit-plan (Architectural design → .gk-plan/<feature>.md)
       │
       ├─────────────────────────────────┐
       ▼                                 ▼
greetkit-tasks                   greetkit-constitution
(Actionable tasks.md)            (Governance & principles check)
       │
       ▼
greetkit-analyze
(Read-only consistency check: spec vs plan vs tasks)
       │
       ▼
[Phase 3: BUILD]
greetkit-implement (Slice-by-slice execution engine)
       │
       ├─────────────────────────┬─────────────────────────┐
       ▼                         ▼                         ▼
greetkit-source-driven   greetkit-frame-animation   greetkit-test-guard
(Official framework docs) (GSAP/Framer Motion)       (Test quality gate)
       │
       ▼
[Phase 4: TEST & GUARD]
greetkit-webapp-testing (Playwright browser verification)
       │
       ├─────────────────────────┬─────────────────────────┐
       ▼                         ▼                         ▼
greetkit-clean-code-guard greetkit-security       greetkit-docs-guard
(SOLID/DRY/KISS/YAGNI)    (OWASP & secret safety)   (Doc & README audit)
       │
       ▼
[Phase 5: REVIEW]
greetkit-review (Final 5-axis quality gate & CHANGELOG update)
```

### Prerequisite Matrix

| Skill | Required Prerequisite | Optional Companion | Output Files Created |
|---|---|---|---|
| `greetkit-spec` | None (Entry point) | None | Spec document |
| `greetkit-plan` | `greetkit-spec` | None | `.gk-plan/001-<feature>.md` |
| `greetkit-tasks` | `greetkit-plan` | None | `.gk-plan/tasks.md` |
| `greetkit-constitution` | Existing project | None | `.greetkit/memory/constitution.md` |
| `greetkit-analyze` | `greetkit-spec` + `greetkit-plan` + `greetkit-tasks` | `greetkit-constitution` | None (Analysis report) |
| `greetkit-implement` | `.gk-plan/tasks.md` or `.gk-plan/*.md` | `greetkit-source-driven`, `greetkit-frame-animation` | Code files, updated `.gk-plan/tasks.md` |
| `greetkit-source-driven` | Active coding task | None | Source-grounded code |
| `greetkit-frame-animation` | UI/Frontend task | None | Scroll animation components |
| `greetkit-test-guard` | Test files written | None | Refactored/guarded test files |
| `greetkit-webapp-testing` | Running Web App | None | Playwright scripts, screenshots |
| `greetkit-clean-code-guard` | Code changes written | None | Clean code refactors |
| `greetkit-security` | Code/API endpoints written | None | Security patches |
| `greetkit-docs-guard` | Documentation edited | None | Audited README / docstrings |
| `greetkit-review` | Completed feature & passing tests | All guard skills | `CHANGELOG.md` entry, review report |
| `greetkit-using-skills` | None (Meta-skill) | None | System prompt context |

---

## 2. Files Produced in Target Projects

When a user initializes and uses GreetKit in a project (`greetkit init .`), the following structure is managed:

1. **`.greetkit/`**: Created by `greetkit init`.
   - `.greetkit/templates/`: Spec, plan, tasks, constitution templates.
   - `.greetkit/scripts/`: Powershell and Bash verification scripts.
   - `.greetkit/memory/`: Project constitution (`constitution.md`).
2. **`.gk-plan/`**: Created during feature planning (`greetkit-plan` and `greetkit-tasks`).
   - `.gk-plan/001-<feature-name>.md`: Feature plan.
   - `.gk-plan/tasks.md`: Task tracking list.
3. **`CHANGELOG.md`**: Updated by `greetkit-review` upon passing final review.

---

## 3. How to Test GreetKit Locally Right Now

You do NOT need to wait for public marketplace approval to test GreetKit on your machine. All agent harnesses support direct local or git-path installation.

### Test 1: Testing via Gemini CLI / Antigravity / Gemini IDE
GreetKit automatically works in your current environment because `GEMINI.md` and `.agents/skills` are loaded directly.
1. Open a fresh terminal in a target project.
2. Ask: *"What are your GreetKit skills?"*
3. Verify: The agent should list the 15 skills and know that `greetkit-using-skills` is active.
4. Send prompt: *"Let me specify a new feature for adding user authentication."*
5. Verify: The agent automatically triggers `greetkit-spec`.

### Test 2: Testing via Claude Code CLI
1. Open terminal and run:
   ```bash
   claude plugin install "c:\Users\Abo Alrejal\Desktop\greetkit"
   ```
2. Start a session with `claude`.
3. The `SessionStart` hook in `hooks/session-start` will fire and inject `greetkit-using-skills`.

### Test 3: Testing via Cursor
1. Cursor auto-discovers `.cursor-plugin/plugin.json` when opening the `greetkit` workspace or installing it as an extension.
2. The hook `./hooks/run-hook.cmd session-start` executes at session start.

### Test 4: Testing via OpenCode
Add to your local `~/.config/opencode/opencode.json`:
```json
{
  "plugin": ["c:/Users/Abo Alrejal/Desktop/greetkit"]
}
```

---

## 4. Platform Marketplace vs Direct Git Plugin Truth

- **Direct Plugin Loading (Git/Local)**: `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.kimi-plugin/plugin.json`, etc. allow any user to install GreetKit directly from your GitHub repo URL (`/plugin install https://github.com/aboalrejal-ai/greetkit`).
- **Official Public Marketplaces**: To appear in the official dropdown/catalog in Claude Code or Codex marketplace apps, a PR must be submitted to the official vendor registries (e.g. Anthropic's plugin directory repo). The manifest files we created are the **exact required prerequisite format** for both direct installation and marketplace submission.
- **Author Email**: `aboalrejal@users.noreply.github.com` is GitHub's default privacy email. You can update `plugin.json` files with your preferred contact email prior to publishing.
