# Root Orchestrator & Global Agent Configuration

## 1. Global Directives
All AI agents in this repository must follow these core rules:
1. **Source of Truth**: The Product Requirements Document (`docs/PRD.md`) and Architecture Decision Records (`docs/adr/`) are the primary sources of truth. Do not invent requirements.
2. **Deterministic Handoffs**: Each agent must validate input artifacts before execution and verify output artifacts against the Definition of Done (DoD) before handoff.
3. **Traceability**: Every code commit, test case, and pull request must reference a valid User Story ID (for example, `US-101`) and Functional Requirement ID (for example, `FR-01`).
4. **Tech-Stack Agnosticism**: Read the project technology stack from Section 2 of this file before you write code or run commands.

## 2. Project Context (Configure Per Project)
- **Project Name**: `[Insert Project Name]`
- **Application Type**: `[Web / Mobile / Backend API / CLI / Embedded / Desktop]`
- **Primary Language**: `[Insert Language & Version]`
- **Build Command**: `[Insert Build Command]`
- **Test Command**: `[Insert Test Command]`
- **Linter Command**: `[Insert Linter Command]`

## 3. Agent Roster & Routing Table
| Role | Agent Definition Path | Primary Assigned Skill | Output Artifacts |
| :--- | :--- | :--- | :--- |
| Product Manager (PM) | `agents/product-manager/AGENTS.md` | `skills/prd-generation/SKILL.md` | `docs/PRD.md` |
| System Architect (SA) | `agents/system-architect/AGENTS.md` | `skills/system-architecture-design/SKILL.md` | `docs/ARCHITECTURE.md`, `docs/adr/*.md`, API Specs |
| Scrum Master (SM) | `agents/scrum-master/AGENTS.md` | `skills/agile-backlog-management/SKILL.md` | `docs/BACKLOG.md`, `docs/sprints/sprint-N.md` |
| Software Engineer (SWE) | `agents/software-engineer/AGENTS.md` | `skills/tdd-code-implementation/SKILL.md` | Source Code, Unit Tests, Pull Requests |
| QA Engineer (QA) | `agents/qa-engineer/AGENTS.md` | `skills/automated-qa-validation/SKILL.md` | `docs/TEST-PLAN.md`, E2E Tests, QA Sign-off Report |
| DevOps Engineer (DevOps) | `agents/devops-engineer/AGENTS.md` | `skills/cicd-release-orchestration/SKILL.md` | CI/CD Pipelines, IaC, Release Notes |

## 4. Escalation Protocol
- If a requirement is ambiguous, the active agent must stop execution and escalate the question to the **Product Manager Agent**.
- If a technical constraint prevents implementation, the active agent must escalate the issue to the **System Architect Agent**.
- If a test fails 3 consecutive times during implementation, the **Software Engineer Agent** must halt changes and log a blocker in the active Sprint Backlog.
