# Testing GreetKit

GreetKit includes automated test suites to verify plugin manifests, hook outputs, skill frontmatter, and shell script syntax.

## Test Suites

Tests live in the `tests/` directory:

- **`tests/hooks/test-session-start.sh`**: Verifies that the `session-start` hook outputs valid JSON, correctly injects the `greetkit-using-skills` bootstrap context, and contains no legacy references.
- **`tests/skills/test-skill-frontmatter.sh`**: Validates that all 15 GreetKit skills have proper YAML frontmatter with `name:` and `description:` fields, and that declared names match directory names.
- **`tests/shell-lint/test-shell-scripts.sh`**: Verifies bash syntax across all hook and shell scripts in the repository.

## Running Tests

Run all tests together:

```bash
bash -c "bash tests/hooks/test-session-start.sh && bash tests/skills/test-skill-frontmatter.sh && bash tests/shell-lint/test-shell-scripts.sh"
```
