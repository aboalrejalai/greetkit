Finalizing GreetKit For Public Release

# GreetKit Skills Evolution Blueprint & Task Tracker

This document outlines the detailed strategy, analysis, and execution roadmap for replacing the legacy skills in GreetKit with an elite, highly modular, and autonomous skill system inspired by the *Superpowers* philosophy. 

**Note:** This file serves as both the historical architecture documentation and the active task tracker. Checked items `[x]` indicate completed phases. At the end of the project, this document will be updated to list the final approved GreetKit skills.

## 1. The Core Philosophy (Hybrid Autonomy)
We are building a **Flexible/Hybrid Workflow**:
1. **Automatic Autonomy (The Superpowers Model):** The agent will run a foundational initialization skill automatically on the first message (via a background hook, similar to Superpowers' `session-start`). This teaches the agent the rules of GreetKit immediately without the user having to type anything.
2. **Manual Invocation (The SpecKit Model):** Complex, heavy-lifting tasks (like deep architectural planning, rigorous code reviews, or PRD generation) will remain manual. The user invokes them when required, keeping the agent from running overly complex loops unprompted.

---

## 2. Skill Migration & Integration Tasks

The user has already manually purged the legacy archive folders (`spec-kit-main` and `agent-skills-main`). The following phases outline the exact operations we will perform on the `superpowers` skills to migrate them into GreetKit.

### Phase 1 & 2: Migration, Audit, Merging & Naming Standardization [COMPLETED]
- [x] All skills staged, audited, merged, and pruned in `skills/`.
- [x] Renamed all remaining skill directories and frontmatter names to follow the `greetkit-*` convention.

#### Final Core Active Inventory (15 Hyper-Optimized Skills):
1. `greetkit-spec` (Intent-driven spec generator with Boundaries & Reframing)
2. `greetkit-plan` (Architectural planner & `.gk-plan/` generator)
3. `greetkit-implement` (Execution engine with Scope Discipline & Systematic Debugging)
4. `greetkit-review` (Multi-axis quality gate with Web Vitals & Image Optimization)
5. `greetkit-tasks` (Actionable `tasks.md` generator)
6. `greetkit-analyze` (Cross-artifact consistency analyzer - read-only)
7. `greetkit-constitution` (Project governance & constitution manager)
8. `greetkit-security` (Renamed from `security-and-hardening` - OWASP & LLM Security)
9. `greetkit-source-driven` (Renamed from `source-driven-development` - Official docs verification)
10. `greetkit-using-skills` (Renamed from `using-agent-skills` - Meta-skill router)
11. `greetkit-clean-code-guard` (Renamed from `clean-code-guard` - SOLID, DRY, YAGNI, LLM failures)
12. `greetkit-docs-guard` (Renamed from `docs-guard` - README & API documentation verification)
13. `greetkit-test-guard` (Renamed from `test-guard` - Universal test suite quality gate)
14. `greetkit-frame-animation` (Renamed from `frame-animation` - GSAP & Framer Motion scroll animations)
15. `greetkit-webapp-testing` (Renamed from `webapp-testing` - Playwright runtime UI verification)

#### Consolidation & Manual Pruning Log:
- [x] Merged `performance-optimization` rules into `greetkit-review` ➔ Deleted `performance-optimization`
- [x] Merged `spec-driven-development` boundary rules into `greetkit-spec` ➔ Deleted `spec-driven-development`
- [x] Merged `incremental-implementation` Scope Discipline rules into `greetkit-implement` ➔ Deleted `incremental-implementation`
- [x] Merged `debugging-and-error-recovery` root cause debugging rules into `greetkit-implement` ➔ Deleted `debugging-and-error-recovery`
- [x] Deleted redundant/unneeded skills per user directives and manual cleanup: `ci-cd-and-automation`, `code-review-and-quality`, `planning-and-task-breakdown`, `test-driven-development`, `browser-testing-with-devtools`, `code-simplification`, `context-engineering`, `documentation-and-adrs`, `shipping-and-launch`, `frontend-ui-engineering`, `doubt-driven-development`, `api-and-interface-design`, `deprecation-and-migration`, `idea-refine`, `observability-and-instrumentation`.
- [x] Renamed `security-and-hardening` ➔ `greetkit-security`
- [x] Renamed `source-driven-development` ➔ `greetkit-source-driven`
- [x] Renamed `using-agent-skills` ➔ `greetkit-using-skills`
- [x] Surgically streamlined `greetkit-review`: preserved 100% of all GreetKit features, verification scripts, CHANGELOG generation, subagents, and Caveman formatting while linking granular rules to `references/`.

### Phase 3: Final Script Path & Context Alignment [COMPLETED]
- [x] Ensure all skills reference `.greetkit/scripts/` where applicable.
- [x] Verify `AGENTS.md` context markers alignment across the CLI (`<!-- GREETKIT START -->` and `<!-- GREETKIT END -->`).
- [x] Complete review of all imported skills (filtered down to 15 lean, hyper-optimized skills).

### Phase 4: Open Source Packaging & Ready for Publish [COMPLETED]
- [x] Update `greetkit-using-skills` meta-skill with the final approved list of 15 GreetKit skills.
- [x] Rename `GREETKIT_MIGRATION_LOG.md` to `CHANGELOG.md` for open-source standard structure.
- [x] Add standard open-source `LICENSE` (MIT) and `SECURITY.md` policies in the project root.
- [x] Blueprint updated: GreetKit is 100% packaged, structured, and ready for Open Source release!
