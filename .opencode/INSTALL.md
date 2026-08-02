# Installing GreetKit for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed

## Installation

Add GreetKit to the `plugin` array in your `opencode.json` (global or project-level):

```json
{
  "plugin": ["greetkit@git+https://github.com/aboalrejal-ai/greetkit.git"]
}
```

Restart OpenCode. The plugin installs through OpenCode's plugin manager and registers all skills.

Verify by asking: "Tell me about your GreetKit skills"

OpenCode uses its own plugin install. If you also use Claude Code, Codex, or another harness, install GreetKit separately for each one.

## Migrating from old install

If you previously installed GreetKit using symlinks or manual copies, remove the old setup:

```bash
# Remove old plugin files
rm -f ~/.config/opencode/plugins/greetkit.js
rm -rf ~/.config/opencode/skills/greetkit
```

Then follow the installation steps above.

## Usage

Use OpenCode's native `skill` tool:

```
use skill tool to list skills
use skill tool to load greetkit-spec
```

## Updating

OpenCode installs GreetKit through a git-backed package spec. If updates do not appear, clear OpenCode's package cache or reinstall the plugin.

To pin a specific version:

```json
{
  "plugin": ["greetkit@git+https://github.com/aboalrejal-ai/greetkit.git#v1.0.0"]
}
```

## Troubleshooting

### Plugin not loading

1. Check logs: `opencode run --print-logs "hello" 2>&1 | grep -i greetkit`
2. Verify the plugin line in your `opencode.json`
3. Make sure you're running a recent version of OpenCode

### Windows install issues

If OpenCode cannot install the plugin on Windows, try installing with system npm:

```powershell
npm install greetkit@git+https://github.com/aboalrejal-ai/greetkit.git --prefix "$HOME\.config\opencode"
```

Then use the installed package path in `opencode.json`:

```json
{
  "plugin": ["~/.config/opencode/node_modules/greetkit"]
}
```

### Skills not found

1. Use `skill` tool to list what's discovered
2. Check that the plugin is loading (see above)

### Tool mapping

Skills speak in actions ("create a todo", "dispatch a subagent", "read a file"). On OpenCode these resolve to:

- "Create a todo" / "mark complete in todo list" → `todowrite`
- `Subagent (general-purpose):` template → `task` tool with `subagent_type: "general"` (or `"explore"` for codebase exploration)
- "Invoke a skill" → OpenCode's native `skill` tool
- "Read a file" → `read`
- "Create a file" / "edit a file" / "delete a file" → `apply_patch`
- "Run a shell command" → `bash`
- "Search file contents" / "find files by name" → `grep`, `glob`
- "Fetch a URL" → `webfetch`

## Getting Help

- Report issues: https://github.com/aboalrejal-ai/greetkit/issues
- Full documentation: https://github.com/aboalrejal-ai/greetkit/blob/main/docs/README.opencode.md
