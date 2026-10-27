<!-- GREETKIT START -->
You are working within the GreetKit project repository.

GreetKit is an Intent-Driven Development (IDD) skills framework for coding agents.
It provides 15 specialized skills organized around the IDD lifecycle:
Spec → Plan → Tasks → Implement → Review

For the full skill routing map, read `skills/greetkit-using-skills/SKILL.md`.
For the project philosophy, read `docs/philosophy.md`.
For the current plan (if any), check `greetkit/plans/` directory.
<!-- GREETKIT END -->

## Project structure

- `src/greetkit_cli/` — Python CLI package (Typer + Rich). Entry: `main.py` → commands in `commands/` (`init`, `status`, `upgrade`).
- `skills/` — 15 agent skill directories, each containing a `SKILL.md` with YAML frontmatter (`name:`, `description:`).
- `templates/` — Scaffolding assets copied into target projects by `greetkit init`. Subdirs: `templates/`, `extensions/`, `integrations/`, `memory/`, `workflows/`.
- `scripts/bash/` — Helper shell scripts invoked by skills at runtime (e.g. `verify_project.sh`, `mark_task_done.sh`).
- `scripts/python/` — Python equivalents of some helpers.
- `hooks/` — Session-start hooks and `hooks.json` for Claude/Cursor plugin lifecycle.
- Platform plugin directories: `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`, `.kimi-plugin/`, `.pi/`, `.opencode/`, plus `gemini-extension.json` and `GEMINI.md`.

## Dev setup

```bash
# Python 3.11+ required
pip install -e .          # editable install; exposes `greetkit` CLI
greetkit --help           # verify
```

The OpenCode plugin (`package.json` main: `.opencode/plugins/greetkit.js`) has its own `npm install` inside `.opencode/`.

## Testing

Tests are **bash scripts**, not pytest. Run all three:

```bash
bash tests/hooks/test-session-start.sh && \
bash tests/skills/test-skill-frontmatter.sh && \
bash tests/shell-lint/test-shell-scripts.sh
```

- `test-session-start.sh` — session-start hook outputs valid JSON, injects bootstrap, no legacy refs.
- `test-skill-frontmatter.sh` — all 15 skills have correct YAML frontmatter; `name:` matches directory name.
- `test-shell-scripts.sh` — `bash -n` syntax check on all shell scripts.

Shell linting (requires `shellcheck` on PATH):

```bash
scripts/lint-shell.sh --all          # lint every tracked shell file
scripts/lint-shell.sh --all --format # also format with shfmt
scripts/lint-shell.sh                # only changed files (default)
```

## Version management

Version is tracked in **7 files** listed in `.version-bump.json`. Never edit version strings by hand — use:

```bash
scripts/bump-version.sh <X.Y.Z>   # bump all files
scripts/bump-version.sh --check    # detect drift
scripts/bump-version.sh --audit    # check + find undeclared references
```

`jq` is required by this script.

## CI

The GitHub Actions workflow (`.github/workflows/python-publish.yml`) has its triggers **commented out**. It only runs `pip install -e . && greetkit --help` when active.

## Conventions and gotchas

- **Line endings**: `.gitattributes` forces LF for `*.sh`, `*.cmd`, `*.md`, `*.json`, `*.js`, `*.ts`, and `hooks/session-start`. Do not introduce CRLF.
- **Skill frontmatter**: every `skills/*/SKILL.md` must start with a `---` YAML block containing at least `name:` and `description:`. The `name:` value must exactly match its directory name.
- **OpenCode plugin** (`.opencode/plugins/greetkit.js`): injects the `greetkit-using-skills` skill content into the first user message via `experimental.chat.messages.transform`. It caches the bootstrap content — restart if you change `SKILL.md`.
- **`greetkit init`** scaffolds into a *target project* (not this repo). It copies `skills/`, `templates/`, `scripts/`, and `hooks/` into the target. Changes to those source directories here affect all future inits.
- **No pytest**: the project uses plain bash test scripts. Do not add pytest infrastructure without explicit approval.
- **`_archive/`** is gitignored — safe for temporary stashing.
