---
name: greetkit-using-skills
description: MANDATORY prerequisite. Use when starting a session or when discovering how GreetKit skills are organized. This is the meta-skill that governs the Intent-Driven Development lifecycle (Spec -> Plan -> Implement).
---

# Using Agent Skills

## Overview

Agent Skills is a collection of engineering workflow skills organized by development phase. Each skill encodes a specific process that senior engineers follow. This meta-skill helps you discover and apply the right skill for your current task.

## Skill Discovery

When a task arrives, identify the development phase and apply the corresponding skill:

```
Task arrives
    │
    ├── New project / feature spec needed? ──────→ greetkit-spec
    ├── Have spec, need architectural plan? ─────→ greetkit-plan
    │   ├── Need granular tasks.md? ─────────────→ greetkit-tasks
    │   ├── Check spec/plan consistency? ───────→ greetkit-analyze
    │   └── Manage project rules/constitution? ──→ greetkit-constitution
    ├── Implementing code? ──────────────────────→ greetkit-implement
    │   ├── Need doc-verified official code? ───→ greetkit-source-driven
    │   └── Scroll / UI animation work? ────────→ greetkit-frame-animation
    ├── Reviewing production code? ──────────────→ greetkit-clean-code-guard
    │   ├── Multi-axis review & CHANGELOG? ──────→ greetkit-review
    │   ├── Security & OWASP hardening? ─────────→ greetkit-security
    │   ├── Reviewing test suite code? ──────────→ greetkit-test-guard
    │   └── Reviewing docs, READMEs, docstrings? → greetkit-docs-guard
    └── Testing web applications? ───────────────→ greetkit-webapp-testing
```

## Core Operating Behaviors

These behaviors apply at all times, across all skills. They are non-negotiable.

### 1. Surface Assumptions

Before implementing anything non-trivial, explicitly state your assumptions:

```
ASSUMPTIONS I'M MAKING:
1. [assumption about requirements]
2. [assumption about architecture]
3. [assumption about scope]
→ Correct me now or I'll proceed with these.
```

Don't silently fill in ambiguous requirements. The most common failure mode is making wrong assumptions and running with them unchecked. Surface uncertainty early — it's cheaper than rework.

### 2. Manage Confusion Actively

When you encounter inconsistencies, conflicting requirements, or unclear specifications:

1. **STOP.** Do not proceed with a guess.
2. Name the specific confusion.
3. Present the tradeoff or ask the clarifying question.
4. Wait for resolution before continuing.

**Bad:** Silently picking one interpretation and hoping it's right.
**Good:** "I see X in the spec but Y in the existing code. Which takes precedence?"

### 3. Push Back When Warranted

You are not a yes-machine. When an approach has clear problems:

- Point out the issue directly
- Explain the concrete downside (quantify when possible — "this adds ~200ms latency" not "this might be slower")
- Propose an alternative
- Accept the human's decision if they override with full information

Sycophancy is a failure mode. "Of course!" followed by implementing a bad idea helps no one. Honest technical disagreement is more valuable than false agreement.

### 4. Enforce Simplicity

Your natural tendency is to overcomplicate. Actively resist it.

Before finishing any implementation, ask:
- Can this be done in fewer lines?
- Are these abstractions earning their complexity?
- Would a staff engineer look at this and say "why didn't you just..."?

If you build 1000 lines and 100 would suffice, you have failed. Prefer the boring, obvious solution. Cleverness is expensive.

### 5. Maintain Scope Discipline

Touch only what you're asked to touch.

Do NOT:
- Remove comments you don't understand
- "Clean up" code orthogonal to the task
- Refactor adjacent systems as a side effect
- Delete code that seems unused without explicit approval
- Add features not in the spec because they "seem useful"

Your job is surgical precision, not unsolicited renovation.

### 6. Verify, Don't Assume

Every skill includes a verification step. A task is not complete until verification passes. "Seems right" is never sufficient — there must be evidence (passing tests, build output, runtime data).

Per-skill verification is the local check. The project-wide bar that applies to *every* change, regardless of which skill is active, is the Definition of Done: tests pass, no regressions, behavior verified at runtime, docs updated. See `references/definition-of-done.md`. It complements each task's acceptance criteria rather than replacing them.

## Failure Modes to Avoid

These are the subtle errors that look like productivity but create problems:

1. Making wrong assumptions without checking
2. Not managing your own confusion — plowing ahead when lost
3. Not surfacing inconsistencies you notice
4. Not presenting tradeoffs on non-obvious decisions
5. Being sycophantic ("Of course!") to approaches with clear problems
6. Overcomplicating code and APIs
7. Modifying code or comments orthogonal to the task
8. Removing things you don't fully understand
9. Building without a spec because "it's obvious"
10. Skipping verification because "it looks right"

## Skill Rules

1. **Check for an applicable skill before starting work.** Skills encode processes that prevent common mistakes.

2. **Skills are workflows, not suggestions.** Follow the steps in order. Don't skip verification steps.

3. **Multiple skills can apply.** A feature implementation might involve `greetkit-spec` → `greetkit-plan` → `greetkit-tasks` → `greetkit-implement` → `greetkit-clean-code-guard` → `greetkit-review` in sequence.

4. **When in doubt, start with a spec.** If the task is non-trivial and there's no spec, begin with `greetkit-spec`.

## Lifecycle Sequence

For a complete feature, the typical skill sequence is:

```
1.  greetkit-spec             → Define what we're building (PRD & boundaries)
2.  greetkit-plan             → Architectural breakdown into greetkit/plans/
3.  greetkit-tasks            → Generate actionable tasks.md
4.  greetkit-constitution       → Align with project rules & governance
5.  greetkit-analyze          → Verify spec/plan/tasks consistency
6.  greetkit-source-driven    → Verify patterns against official docs
7.  greetkit-frame-animation  → Build smooth scroll animations (GSAP / Motion)
8.  greetkit-implement        → Execute plan slice-by-slice with scope discipline
9.  greetkit-test-guard       → Audit and guard test suite quality
10. greetkit-webapp-testing   → Run Playwright runtime UI verification
11. greetkit-clean-code-guard → Guard production code (SOLID, DRY, YAGNI)
12. greetkit-security         → Harden security, OWASP, and secret safety
13. greetkit-docs-guard       → Fact-check READMEs, API docs, and docstrings
14. greetkit-review           → Final 5-axis review gate, verify build & update CHANGELOG
```

Not every task needs every skill. A code execution task might only need: `greetkit-implement` → `greetkit-clean-code-guard` → `greetkit-review`.

## Quick Reference

| Phase | Skill | One-Line Summary |
|-------|-------|-----------------|
| Define | greetkit-spec | Intent-driven specs, PRD, and boundaries before code |
| Plan | greetkit-plan | Decompose feature into verifiable architectural plan |
| Plan | greetkit-tasks | Generate actionable tasks.md with user story structure |
| Plan | greetkit-analyze | Read-only consistency check across spec, plan, and tasks |
| Plan | greetkit-constitution | Manage project governance and alignment rules |
| Build | greetkit-implement | Strict execution engine with scope discipline & debugging |
| Build | greetkit-source-driven | Ground implementations in official framework documentation |
| Build | greetkit-frame-animation | GSAP ScrollTrigger & Framer Motion scroll animations |
| Test | greetkit-test-guard | Quality gate against over-mocked or bloated test code |
| Test | greetkit-webapp-testing | Playwright scripts for runtime browser & UI verification |
| Guard | greetkit-clean-code-guard | Clean Code, SOLID, DRY, KISS, YAGNI & LLM failure checks |
| Guard | greetkit-security | OWASP hardening, input validation & secret safety |
| Guard | greetkit-docs-guard | Fact-check documentation against source code truth |
| Review | greetkit-review | Multi-axis review gate, verify_project scripts & CHANGELOG |
| Meta | greetkit-using-skills | Master router for skill discovery and execution rules |
