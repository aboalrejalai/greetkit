# Changelog Guidelines and Styling

All changelog entries must follow this professional, corporate-style layout. Do not write generic or lazy bullet points.

## Changelog Entry Format

Each version entry must use the following structure:

```markdown
## [<Version>] - <Date>

### <Release Title>
*<A concise, elegant paragraph describing the main theme of this release (e.g. Quota screen redesign, PDF attachment support, and other bug fixes).*

#### Improvements (<Count>)
- **<Feature Title>**: <Descriptive, clear, professional explanation of the improvement, detailing the visual or behavioral impact (e.g. "Quota screen redesign: clearer, unambiguous view into “used” versus “remaining” credits...").>

#### Fixes (<Count>)
- **<Bug/Fix Title>**: <Detailed description of the fix, explaining the root cause and the improved behavior (e.g. "Improved MCP server stability: increased resilience to unresponsive MCP servers...").>

#### Patches (<Count>)
- **<Patch Title>**: <Any minor updates, dependency bumps, or internal tweaks that do not qualify as major improvements or user-facing fixes.>
```

## Styling Rules
1. **Highlight titles**: Every bullet point must start with `**<Feature/Bug/Patch Title>**: ` followed by the description.
2. **Be detailed**: Do not just say "Fixed bug" or "Updated UI". Provide context on *why* it was done and *what* was changed.
3. **Always include counts**: Even if a section is empty, include it with `(0)` count (e.g. `#### Patches (0)`).
4. **Professional tone**: Use formal, polished, technical English that is easy for users and stakeholders to understand.

## Example Reference

```markdown
## [2.1.4] - June 11, 2026

### Quota Screen Redesign and PDF Support
*Quota screen redesign, PDF attachment support, new /btw slash command, and other bug fixes.*

#### Improvements (7)
- **Quota screen redesign**: clearer, unambiguous view into “used” versus “remaining” credits in the Models tab of the Settings screen.
- **Ask side questions via /btw**: while in a conversation, type ‘/btw’ in the input and select the ‘btw’ option in the menu to write a message to an ephemeral, single-response agent that has the context of your current conversation.
- **Simple conversation search functionality**: cmd/ctrl+F to search for visible text in the conversation view.
- **Support for PDF attachments**: drag and drop PDFs from your filesystem or add PDFs using the media option in the Add Context menu button in the input box.
- **Breadcrumbs in file viewer pane header**: quality-of-life UI to more easily see and navigate directories in your repo.
- **Nested subagents in the overview pane**: see all nested subagents belonging to the main conversation instead of only the subagents that are one level deep.
- **Minor improvements to Projects UX**: you can now greetkit a project name during the creation flow and sort conversations in the left sidebar by worktree.

#### Fixes (4)
- **Improved LaTeX support**: the agent has a better understanding and awareness of its ability to output LaTeX-rendered math text.
- **Improved MCP server stability**: increased resilience to unresponsive MCP servers and improved browser agent self-troubleshooting abilities when using the Chrome DevTools MCP server.
- **MCP server schema compatibility**: the mcp_config.json schema now accepts url in addition to serverUrl as a field.
- **New entries in the sensitive paths list**: .vscode and .cache are now recognized as sensitive paths that require explicit user confirmation before the agent can access them.

#### Patches (0)
```
