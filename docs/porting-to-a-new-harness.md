# Porting GreetKit to a New Harness

This guide explains how to add support for a new harness — an IDE, CLI, or agent runner that isn't Claude Code — so that GreetKit skills auto-trigger there the same way they do natively.

It is written in two layers. **Part 1–3** explain how the system works and how to tell whether a harness can be supported at all; read these before you touch anything. **Part 4–8** are a prescriptive procedure for an agent (supervised by a human partner) to execute the port end to end, through distribution. An appendix indexes the current reference integrations so you can copy the closest one.

The integration mechanism differs across harnesses, and it will keep changing. This guide deliberately teaches the **invariants** — the things that must be true no matter the mechanism — and points you at a live reference implementation to copy. When this guide and the code disagree, the code wins; fix the guide.

## Before you start

Adding a harness is the highest-stakes contribution type in this repo. Before writing anything:

- Read `CLAUDE.md` and `.github/PULL_REQUEST_TEMPLATE.md` in full — the contributor rules and the new-harness PR requirements are not optional.
- Search open **and closed** PRs for a prior attempt at this harness. If one exists, understand why it stalled before starting your own.

---

## Part 1 — How GreetKit works across harnesses

GreetKit is the same content everywhere. What changes per harness is the thin layer that delivers that content to the model and translates its instructions into the harness's native tools. Three components:

1. **Skills (harness-agnostic).** Everything in `skills/` is the source of truth, shared verbatim by every harness. Skills are written to describe *actions* — "invoke a skill", "read a file", "dispatch a subagent", "create a todo" — and never name a specific tool. This is what lets one skill body run on Claude Code, Codex, Gemini, pi, and the rest without edits.

2. **Tool mapping (per-harness).** Each harness needs the action vocabulary translated into its real tool names. That translation lives in `skills/greetkit-using-skills/references/<harness>-tools.md` and/or inline in the harness's bootstrap injector (see Part 5). It says, e.g., "*dispatch a subagent* → call `task` with `subagent_type`."

3. **Bootstrap (per-harness).** At the start of every session, the full `skills/greetkit-using-skills/SKILL.md` is injected into the model's context, wrapped in `<EXTREMELY_IMPORTANT>` tags, with the tool mapping appended. That injected skill is what teaches the model that skills exist and that it must check for a relevant skill before acting. **The bootstrap is the entire integration.** Without it, the skill files are inert — present on disk, never invoked.

### Two rules that make this work

**1. Skills name actions, not tools.** Do **not** edit skill bodies to fit your harness. Porting adds a tool-mapping reference and a bootstrap injector; it never reaches into `skills/*/SKILL.md` to swap tool names.

**2. Everything ships through the harness's own install mechanism. Never edit the user's files.** The bootstrap, the skills, and the tool mapping all get delivered *as part of what the harness installs* — a plugin, an extension, a marketplace entry, an extension-bundled context file. A port **must not** reach into a user's global or personal config (`~/.gemini/config/AGENTS.md`, `settings.json`, etc.) to inject anything.

---

## Part 2 — Can this harness be supported?

A harness can support GreetKit only if it can do all of the following. Check these before writing code — if the first one fails, stop.

### Hard requirement: automatic session-start injection

The harness must let you inject text into the model's context **at the start of every session, with no per-session opt-in by your human partner.** This is the one non-negotiable capability.

---

## Part 3 — Definition of done

A port is finished when **all** of these are true:

1. The `greetkit-using-skills` bootstrap loads at session start, every session, with no per-session opt-in.
2. A tool mapping exists for the harness.
3. Skills can actually be invoked and the model follows them.
4. **The acceptance test passes.**
5. Tests cover the integration and pass.
6. A real user can install it through the harness's own mechanism.

---

## Appendix — Reference integrations (current)

| Harness | Entry point | Bootstrap mechanism | Tool mapping |
|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` + `hooks/hooks.json` | shell hook → `hooks/session-start` | native `Skill` tool |
| Codex | `.codex-plugin/plugin.json` | native skill discovery | `references/codex-tools.md` |
| Cursor | `.cursor-plugin/plugin.json` + `hooks/hooks-cursor.json` | shell hook → `hooks/session-start` | Claude Code-compatible |
| Gemini CLI | `gemini-extension.json` + `GEMINI.md` | instructions file `@`-includes bootstrap + mapping | `references/gemini-tools.md` |
| Kimi Code | `.kimi-plugin/plugin.json` | manifest `sessionStart.skill` loads `greetkit-using-skills` | inline `skillInstructions` |
| OpenCode | `.opencode/plugins/greetkit.js` | in-process transform | inline in `greetkit.js` |
| pi | `.pi/extensions/greetkit.ts` | in-process context event | `piToolMapping()` inline |
