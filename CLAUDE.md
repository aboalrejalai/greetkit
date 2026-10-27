# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

`AGENTS.md` (imported above) holds the setup, test, lint, and version-bump commands and the repo conventions. This file adds the cross-file architecture those commands don't show.

## Two distribution paths share the same source dirs

`skills/`, `hooks/`, `scripts/`, `templates/`, and `skills.sh.json` ship two ways, so an edit to any of them changes both:

1. **As a Python wheel** (`pip install`, then `greetkit init`). `pyproject.toml` `force-include` bundles those repo-root dirs into `greetkit_cli/` inside the wheel. `_find_asset_dir()` in `src/greetkit_cli/commands/init.py` looks for each asset next to the package first, then one level up, then two levels up (the repo root, for editable installs).
2. **As an agent plugin** (Claude/Cursor/Codex/Kimi/OpenCode/Pi/Gemini). The repo root *is* the plugin. `hooks/hooks.json` runs `hooks/run-hook.cmd session-start`, which reads `skills/greetkit-using-skills/SKILL.md` and emits it as session context. The JSON shape depends on the host: `CURSOR_PLUGIN_ROOT` gives `additional_context`, `CLAUDE_PLUGIN_ROOT` gives `hookSpecificOutput.additionalContext`, and anything else gets top-level `additionalContext`. `.opencode/plugins/greetkit.js` does the same injection for OpenCode through a message transform.

`greetkit-using-skills/SKILL.md` is the bootstrap router injected into every session, so treat changes to it as high-impact. `tests/hooks/test-session-start.sh` checks the injection.

## What `greetkit init` writes into a target project

`init.py` holds nearly all CLI logic. The other commands are thin. The mapping from this repo to the target project:

- `templates/*` → `greetkit/internal/` (the tree is copied whole; `constitution-template.md` is also seeded to `greetkit/internal/memory/constitution.md`)
- `scripts/bash` or `scripts/powershell` (only the chosen `--script` variant) → `greetkit/internal/scripts/<variant>/`
- `skills/` → one skills dir per selected integration (`.claude/skills`, `.cursor/skills`, `.agents/skills`, …). `all` expands to every integration.
- `hooks/` → `hooks/`, or `.agents/hooks` when `agy` is the only integration
- It also generates `greetkit/internal/{init-options,integration,feature}.json`, `extensions.yml`, and per-integration `integrations/*.manifest.json` files that list skill files with their SHA-256 hashes.

Without a TTY (piped stdin), `init` skips its prompts. It defaults to the `agy` integration and to `sh` (or `ps` on Windows), and it fails on a non-empty directory unless `--force` is passed.

## Known drift to watch for

- **Version strings disagree.** The plugin manifests tracked by `.version-bump.json` are `1.0.0`, but `pyproject.toml` (`0.1.0`) is not tracked, and `init.py` hardcodes `"0.1.0"` in the JSON it writes. `bump-version.sh` won't update those two places.
- **`greetkit status` is out of step with `init`.** It checks `.specs`, `.plan`, `skills`, and `templates`, but `init` creates `greetkit/specs`, `greetkit/plans`, and per-integration skill dirs.
- **The hardcoded skill count.** The 15-skill count appears in the README, AGENTS.md, `skills.sh.json` groupings, and the frontmatter test. If you add or remove a skill, update all of them.
