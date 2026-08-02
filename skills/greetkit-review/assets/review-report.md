# Final Review Report

## Findings (Caveman Format)
Write review comments terse and actionable. One line per finding. Location, problem, fix. No throat-clearing. Use the ultra-compressed format: `L<line>: <severity_emoji> <problem>. <fix>.`

**Legend:**
- `🔴 bug:` Broken behavior, blocks merge. (Example: `L42: 🔴 bug: user can be null. Add guard.`)
- `🟡 risk:` Fragile (race condition, missing check). (Example: `L23: 🟡 risk: no retry on 429. Wrap in withBackoff.`)
- `🔵 nit:` Style, minor, optional. (Example: `L88: 🔵 nit: 50-line fn does 4 things. Extract.`)
- `❓ q:` Genuine question. (Example: `L15: ❓ q: why hardcode this timeout?`)
- `✂️ cut:` Over-engineering or bloat. Use to flag dead code, reinvented stdlib, or unnecessary abstractions that should be deleted/shrunk. (Example: `L42: ✂️ cut: reinvented standard library. Use array.flatMap().`)

**Issues Found:**
- [List findings here using the format above]

---

## Execution Performance Summary
| Metric | Value |
|--------|-------|
| Tasks completed in this cycle | [N] |
| Issues found (🔴 Critical) | [N] |
| Issues found (🟡 Risk) | [N] |
| Issues found (🔵 Nit) | [N] |
| Rounds of review before approval | [N] |
