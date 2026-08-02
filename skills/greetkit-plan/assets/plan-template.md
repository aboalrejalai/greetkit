---
goal: [Concise Title Describing the Implementation Plan's Goal]
version: [Optional: e.g., 1.0]
date_created: [YYYY-MM-DD]
last_updated: [Optional: YYYY-MM-DD]
status: 'Planned'|'In progress'|'Completed'|'Deprecated'|'On Hold'
tags: [feature, upgrade, architecture, refactor, bug, etc]
---

# Implementation Plan: [Feature/Project Name]

![Status: <status>](https://img.shields.io/badge/status-<status>-<status_color>)

## Overview
**Current State:** [Brief description of how things work now]
**Target State:** [Brief description of how things will work after the implementation]

## 1. Requirements & Constraints
[Explicitly list all requirements & constraints. Use formal identifiers.]
- **REQ-001**: Requirement 1

## 2. Architecture & Alternatives
- [Key decision 1 and rationale]

## 2.1 No-Touch Zones
Files that MUST NOT be modified during this implementation:
- `path/to/sensitive/file` — [Reason why it must not be touched]
- **ALT-001**: [Alternative approach considered and why it was rejected]

## 3. Dependencies & Files
- **DEP-001**: [Library/Framework dependency]

| File Path | Change Type | Description / Dependencies |
|-----------|-------------|----------------------------|
| `path/to/file` | modify/create/delete | [What changes and why] |

## 4. Task Tracking & Phases

### Phase 1: Setup & Infrastructure
- **GOAL**: [Project initialization, tooling, etc.]
- [ ] TASK-001: [Description]

### Phase 2: Foundational (Blocking Prerequisites)
- **GOAL**: [Database setup, core services required by all stories]
- [ ] TASK-002: [Description]
- Checkpoint: Tests pass, builds clean.

### Phase 3: [US1] User Story 1
- **GOAL**: [Deliver end-to-end functionality for US1]
- [ ] TASK-003 [US1]: [Description]
- [ ] TASK-004 [P] [US1]: [Parallelizable task description]
- Checkpoint: US1 acceptance criteria met.

## 5. Detailed Task Definitions
[For each TASK ID, provide the detailed definition following Step 6 format]
### TASK-001: ...

## 6. Risks and Assumptions
| ID | Risk / Assumption | Impact | Mitigation / Note |
|----|-------------------|--------|-------------------|
| RISK-001 | [Risk] | [High/Med/Low] | [Strategy] |
| ASM-001  | [Assumption] | - | [Note] |

## 7. Open Questions
- [Question needing human input]

## 8. Rollback Plan
- [How to undo this change if the implementation fails or causes issues]
