---
name: greetkit-spec
description: "Intent-Driven Feature Specification. Generate a PRD from natural language while resolving ambiguity through max 3 questions."
metadata:
  author: "GreetKit"
---

## User Input
```text
$ARGUMENTS
```

## Goal
To produce a well-structured PRD (`greetkit/specs/[feature-name].md`) using Intent-Driven Development principles, asking max 3 clarifying questions if needed.

## Execution Rules
1. Ensure the `greetkit/specs/` directory exists.
2. **Surface Assumptions & Reframing:** Translate any vague requirements into concrete, measurable success criteria (e.g. "Make page faster" ➔ "LCP < 2.5s").
3. **Clarification Gate:** If ambiguity prevents MVP definition, ask max 3 specific, actionable questions.
4. **Three-Tier Boundary Check:** Explicitly structure boundaries in the spec:
   - **Always do:** Run tests, validate inputs at boundaries, parameterize queries.
   - **Ask first:** Schema changes, adding dependencies, modifying CORS / auth.
   - **Never do:** Commit secrets, remove failing tests, hardcode credentials.
5. Write the final spec to `greetkit/specs/[feature-name].md` based on `assets/spec-template.md`.
6. Update `AGENTS.md` in the project root between `<!-- GREETKIT START -->` and `<!-- GREETKIT END -->` with the active spec path.

