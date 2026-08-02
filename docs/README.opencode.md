# GreetKit for OpenCode

Complete guide for using GreetKit with [OpenCode.ai](https://opencode.ai).

## Installation

Add GreetKit to the `plugin` array in your `opencode.json` (global or project-level):

```json
{
  "plugin": ["greetkit@git+https://github.com/aboalrejal-ai/greetkit.git"]
}
```

Restart OpenCode. The plugin installs through OpenCode's plugin manager and registers all skills.

Verify by asking: "Tell me about your GreetKit skills"

## Usage

### Finding Skills

Use OpenCode's native `skill` tool to list all available skills:

```
use skill tool to list skills
```

### Loading a Skill

```
use skill tool to load greetkit-spec
```

## How It Works

The plugin does two things:

1. **Injects bootstrap context** via the `experimental.chat.messages.transform` hook, adding GreetKit awareness to every conversation.
2. **Registers the skills directory** via the `config` hook, so OpenCode discovers all GreetKit skills without symlinks or manual config.

### Tool Mapping

Skills speak in actions rather than naming any one runtime's tools. On OpenCode these resolve to:

- "Create a todo" / "mark complete in todo list" → `todowrite`
- `Subagent (general-purpose):` template → OpenCode's `task` tool with `subagent_type: "general"` (or `"explore"` for codebase exploration)
- "Invoke a skill" → OpenCode's native `skill` tool
- "Read a file" → `read`
- "Create a file" / "edit a file" / "delete a file" → `apply_patch`
- "Run a shell command" → `bash`
- "Search file contents" / "find files by name" → `grep`, `glob`
- "Fetch a URL" → `webfetch`

## Troubleshooting

### Plugin not loading

1. Check OpenCode logs: `opencode run --print-logs "hello" 2>&1 | grep -i greetkit`
2. Verify the plugin line in your `opencode.json` is correct
3. Make sure you're running a recent version of OpenCode

## Getting Help

- Report issues: https://github.com/aboalrejal-ai/greetkit/issues
- Main documentation: https://github.com/aboalrejal-ai/greetkit
- OpenCode docs: https://opencode.ai/docs/
