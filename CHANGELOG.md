# CHANGELOG — GreetKit Evolution & Architecture 🚀

**Dates of Documentation:** July 11, 2026 (Initial Migration) | July 25, 2026 (Final Polish & Purge) | August 2, 2026 (Full Skill Consolidation & Staging)  
**Team:** Developer & AI Assistant (Antigravity)  
**Purpose:** To serve as the ultimate technical and historical reference for `GreetKit`. Any AI agent opening this project should read this document to instantly understand the architecture, philosophy, and capabilities of the project without needing to scan everything.

---

## 🎯 Vision & Philosophy: Intent-Driven Development (IDD)

**GreetKit** is a comprehensive, standalone system for **Intent-Driven Development (IDD)**. It was built as a clean, powerful alternative to other tools (like SpecKit), featuring its own CLI, completely isolated folder architecture, and elite-tier agent skills.

Our core philosophy shifts from "Spec-Driven" to "Intent-Driven":
> *"You express your intent. The system turns it into reality."*

The IDD pipeline is strictly enforced through a robust workflow of intelligent agent skills:
1. **Intent / Spec (`greetkit-spec` & `greetkit-clarify`)**: Captures the user's idea, asks exactly 3-5 smart questions to resolve ambiguity, and outputs a strict PRD in `.gk-specs/`.
2. **Plan (`greetkit-plan`)**: Converts the PRD into an architectural implementation plan and actionable, atomic tasks mapped in `.gk-plan/`.
3. **Implement (`greetkit-implement`)**: The execution engine that writes code, phase-by-phase, marking tasks as complete.
4. **Review (`greetkit-review`)**: The uncompromising quality gate that verifies the implementation against the plan and core project constitution before finalization.

---

## 🏗️ Architecture & Isolation

To ensure GreetKit runs perfectly without conflicting with other tools, we engineered a completely isolated ecosystem:
- **`.greetkit/`**: The core hidden directory replacing old systems. It contains `extensions/`, `integrations/`, `memory/` (for the Constitution), `scripts/`, and `workflows/`.
- **`.gk-plan/`**: Dedicated directory for technical plans and task tracking.
- **`.gk-specs/`**: Dedicated directory for product specifications.
- **Context Markers**: `AGENTS.md` strictly uses `<!-- GREETKIT START -->` and `<!-- GREETKIT END -->` tags to manage state and context hand-offs between skills.

---

## 🛠️ The Migration Journey (Step-by-Step)

### Phase 1: CLI Foundation
1. **Core Setup**: Initialized `greetkit` as a pip-installable Python package (`pyproject.toml`).
2. **Interactive UI**: Built a robust CLI using `Typer`, `Rich`, and `readchar`. Features include interactive arrow-key selection for AI agents (e.g., `agy`) and script environments (bash/ps), plus a dynamic, tree-style progress tracker (`StepTracker`).

### Phase 2: Asset Consolidation
1. **Templates**: Migrated all foundational markdown templates (plans, specs, constitution, checklists) into `greetkit/templates/templates`.
2. **Scripts**: Centralized all core execution scripts (Bash and PowerShell) into `greetkit/scripts`.

### Phase 3: Skills Migration & Rebranding
1. **Importing Power**: Extracted 15+ high-tier agent skills (including the core triad: `plan`, `implement`, `review`, plus `git-*` utilities).
2. **Rebranding**: Renamed all skills from `speckit-*` to `greetkit-*`.
3. **Instruction Update**: Rewrote the `SKILL.md` internal prompts to exclusively reference the new `.gk-*` directories and GreetKit context markers.

### Phase 4: Dynamic Scaffolding & Manifests
To match advanced architectural standards, the `greetkit init` command was programmed to dynamically generate:
- Complete directory trees for `extensions`, `integrations`, `memory`, and `workflows`.
- Configuration files (`init-options.json`, `integration.json`, `feature.json`).
- A fully populated `extensions.yml` containing Git hook bindings for every stage of the IDD pipeline.
- Secure SHA-256 manifest files (`agy.manifest.json`, `greetkit.manifest.json`) for tracking skill versions and integrity.

### Phase 5: The Final Polish & Purge (July 25, 2026)
To guarantee 100% independence and flawless execution, a deep architectural sweep was conducted:
1. **Centralized Script Execution**: Fixed critical path bugs inside `greetkit-plan`, `greetkit-implement`, and `greetkit-review` `SKILL.md` files. They now correctly trigger scripts exclusively from the centralized `.greetkit/scripts/` directory, rather than relying on legacy relative paths.
2. **Purging Spec-Kit Remnants**: 
   - Deleted the obsolete `.specify/` and `specs/` directories.
   - Wiped 14+ leftover `speckit-*` skill folders from `.agents/skills/` to prevent agent confusion.
   - Updated `AGENTS.md` context markers globally.
3. **CI/CD Foundation**: Created a GitHub Actions workflow (`.github/workflows/python-publish.yml`) to automatically test the CLI and prepare for PyPI publishing (currently commented out/disabled while the project is in active development).

### Phase 6: Skill Staging, Audit & Pruning (August 2, 2026)
1. **Initial Skill Consolidation**: Staged 39 skill modules into `skills/`.
2. **Batch 1 Audit & Pruning**:
   - **Merged & Purged**: Enriched `greetkit-review` with Web Vitals / Image optimization rules from `performance-optimization` (deleted `performance-optimization`). Enriched `greetkit-spec` with Boundary rules from `spec-driven-development` (deleted `spec-driven-development`).
   - **Redundancy Purged**: Deleted `code-review-and-quality` (redundant with `greetkit-review`), `planning-and-task-breakdown` (redundant with `greetkit-plan` & `greetkit-tasks`), and `ci-cd-and-automation` (natively handled by LLMs).
3. **Batch 2 Audit & Pruning**:
   - **Merged & Purged**: Enriched `greetkit-implement` with Scope Discipline rules from `incremental-implementation` (deleted `incremental-implementation`).
   - **Purged**: Deleted `test-driven-development` and `browser-testing-with-devtools` per user directive.
   - **Retained**: Retained `source-driven-development` for official docs verification.
4. **Batch 3 Audit & Pruning**:
   - **Purged**: Deleted `code-simplification` (pending stronger replacement), `context-engineering`, `documentation-and-adrs`, and `shipping-and-launch`.
5. **Batch 4 Audit & Pruning**:
   - **Merged & Purged**: Enriched `greetkit-implement` with Root-Cause Debugging rules from `debugging-and-error-recovery` (deleted `debugging-and-error-recovery`).
   - **Purged**: Deleted `frontend-ui-engineering` (pending stronger replacement) and `doubt-driven-development`.
   - **Retained**: Retained `security-and-hardening` for OWASP and secret protection.
7. **Manual Pruning & Standardized Renaming**:
   - **User Manual Clean**: Deleted remaining redundant skills (`deprecation-and-migration`, `idea-refine`, `observability-and-instrumentation`).
   - **Standardized Naming**: Renamed `security-and-hardening` ➔ `greetkit-security`, `source-driven-development` ➔ `greetkit-source-driven`, and `using-agent-skills` ➔ `greetkit-using-skills`. Updated internal YAML frontmatter `name:` fields to match.
8. **Surgical Streamlining**: Surgically pruned copy-pasted inline text from `greetkit-review` (Sections 2, 3, and 6) while retaining 100% of all GreetKit features, verification scripts, CHANGELOG generation, subagents, Caveman formatting, and deep reference files in `references/`.
10. **Addition & Standardized Renaming of Guard & Animation Skills**:
    - **Renamed**: `clean-code-guard` ➔ `greetkit-clean-code-guard`, `docs-guard` ➔ `greetkit-docs-guard`, `test-guard` ➔ `greetkit-test-guard`, `frame-animation` ➔ `greetkit-frame-animation`, `webapp-testing` ➔ `greetkit-webapp-testing`.
    - **Router Updated**: Updated `greetkit-using-skills` meta-skill to route discovery and lifecycle sequences exclusively across the 15 active `greetkit-*` skills while preserving all Core Operating Behaviors and Failure Modes.
11. **Final Active Inventory**: Exactly 15 lean, hyper-optimized skills in `skills/` directory (1. `greetkit-spec`, 2. `greetkit-plan`, 3. `greetkit-implement`, 4. `greetkit-review`, 5. `greetkit-tasks`, 6. `greetkit-analyze`, 7. `greetkit-constitution`, 8. `greetkit-security`, 9. `greetkit-source-driven`, 10. `greetkit-using-skills`, 11. `greetkit-clean-code-guard`, 12. `greetkit-docs-guard`, 13. `greetkit-test-guard`, 14. `greetkit-frame-animation`, 15. `greetkit-webapp-testing`).

---

## 💡 Notes for Future AI Agents

When opening this project in a new session, **read this file first**. It contains the entire context of the project.
- **Source Code**: The CLI code is in `src/greetkit_cli/`. 
- **Source Assets**: The master templates, skills, and scripts to be distributed are stored in `templates/`, `skills/`, and `scripts/`.
- **Initialized Environment**: The `.greetkit/`, `.agents/`, `.gk-plan/`, and `.gk-specs/` folders currently in the root are the result of running `greetkit init --here`. This repository acts as both the source code for the package AND a live testing ground.
- **Golden Rule**: GreetKit is a premium, intent-driven ecosystem. Do not introduce legacy behaviors, and respect the strict separation of concerns across the Triad skills.
