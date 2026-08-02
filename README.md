# GreetKit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**GreetKit** is an Intent-Driven Development (IDD) skills framework and runtime bootstrap for AI coding agents. It equips coding agents with a structured lifecycle — **Spec → Plan → Tasks → Implement → Review** — and quality guards to ensure high-quality software delivery across multiple platforms.

---

## 🚀 Supported Platforms

GreetKit supports a wide range of AI coding agents and harnesses:

- **Claude Code** (`.claude-plugin/`)
- **Codex** (`.codex-plugin/`)
- **Cursor** (`.cursor-plugin/` & `hooks/hooks-cursor.json`)
- **Kimi Code** (`.kimi-plugin/`)
- **OpenCode.ai** (`.opencode/`)
- **Pi Coding Agent** (`.pi/`)
- **Gemini CLI** (`gemini-extension.json` & `GEMINI.md`)

---

## 💻 Installation & Usage

**1. Install globally on your machine:**
```bash
pip install git+https://github.com/aboalrejal-ai/greetkit.git
```
*(This installs the `greetkit` command globally on your system directly from GitHub).*

**2. Initialize GreetKit inside your specific project:**
Navigate to your project folder and run:
```bash
greetkit init .
```
The CLI will interactively ask which IDE plugins you want to generate (e.g., Claude, Cursor, Antigravity) and will inject the necessary skills and hooks directly into your project.

---

## 🛠 Included Skills (15 Hyper-Optimized Skills)

| Phase | Skill | Summary |
|-------|-------|---------|
| **Define** | `greetkit-spec` | Intent-driven feature specification gathering & boundary setting |
| **Plan** | `greetkit-plan` | Decomposes features into structured architectural plans |
| **Plan** | `greetkit-tasks` | Generates actionable, structured `tasks.md` task lists |
| **Plan** | `greetkit-analyze` | Read-only cross-artifact consistency analyzer |
| **Plan** | `greetkit-constitution` | Manages project governance, principles, and alignment rules |
| **Build** | `greetkit-implement` | Disciplined execution engine with strict scope discipline & debugging |
| **Build** | `greetkit-source-driven` | Grounds framework code in official, source-cited documentation |
| **Build** | `greetkit-frame-animation` | Technical scroll animations using GSAP & Framer Motion |
| **Test** | `greetkit-test-guard` | Universal quality gate preventing test suite bloat & over-mocking |
| **Test** | `greetkit-webapp-testing` | Playwright scripts for runtime browser & UI verification |
| **Guard** | `greetkit-clean-code-guard` | Enforces SOLID, DRY, KISS, YAGNI, & checks LLM failure modes |
| **Guard** | `greetkit-security` | Security hardening, input validation, & OWASP vulnerability prevention |
| **Guard** | `greetkit-docs-guard` | Fact-checks documentation, READMEs, & API docstrings against code |
| **Review** | `greetkit-review` | Multi-axis code review gate & automated CHANGELOG updates |
| **Meta** | `greetkit-using-skills` | Foundational router and bootstrap skill for skill discovery |

---

## 🔄 The IDD Lifecycle

```
1.  greetkit-spec             → Define what we're building (PRD & boundaries)
2.  greetkit-plan             → Architectural breakdown into .gk-plan/
3.  greetkit-tasks            → Generate actionable tasks.md
4.  greetkit-constitution       → Align with project rules & governance
5.  greetkit-analyze          → Verify spec/plan/tasks consistency
6.  greetkit-source-driven    → Verify patterns against official docs
7.  greetkit-frame-animation  → Build smooth scroll animations
8.  greetkit-implement        → Execute plan slice-by-slice with scope discipline
9.  greetkit-test-guard       → Audit and guard test suite quality
10. greetkit-webapp-testing   → Run Playwright runtime UI verification
11. greetkit-clean-code-guard → Guard production code (SOLID, DRY, YAGNI)
12. greetkit-security         → Harden security, OWASP, and secret safety
13. greetkit-docs-guard       → Fact-check READMEs, API docs, and docstrings
14. greetkit-review           → Final 5-axis review gate & CHANGELOG update
```

---

## ⚡ Quickstart

### Python CLI
```bash
# Install local package in editable mode
pip install -e .

# Initialize GreetKit in a project
greetkit init .
```

### Platform Plugins

- **Claude Code**: `/plugin install https://github.com/aboalrejal-ai/greetkit`
- **Kimi Code**: `/plugins install https://github.com/aboalrejal-ai/greetkit`
- **OpenCode**: Add `"plugin": ["greetkit@git+https://github.com/aboalrejal-ai/greetkit.git"]` to `opencode.json`

For full porting and platform installation instructions, see [docs/porting-to-a-new-harness.md](docs/porting-to-a-new-harness.md).

---

## 📖 Documentation

- [IDD Philosophy](docs/philosophy.md)
- [Testing GreetKit](docs/testing.md)
- [Porting to a New Harness](docs/porting-to-a-new-harness.md)
- [Windows Polyglot Hooks](docs/windows/polyglot-hooks.md)
- [CHANGELOG](CHANGELOG.md)

---

## 📄 License

[MIT License](LICENSE)
