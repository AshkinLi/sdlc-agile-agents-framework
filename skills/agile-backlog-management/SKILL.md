---
name: agile-backlog-management
description: Decomposes PRD requirements and System Architecture into INVEST-compliant User Stories, estimates effort, and builds Sprint Backlogs.
---

# Skill: Agile Backlog Management

## 1. Objective
Convert `docs/PRD.md` and `docs/ARCHITECTURE.md` into a prioritized Product Backlog (`docs/BACKLOG.md`) and an executable Sprint Backlog (`docs/sprints/sprint-N.md`).

## 2. Required Inputs
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`

## 3. Step-by-Step Execution Procedure
1. **Create Epics**:
   - Group related Functional Requirements (`FR-XX`) into logical Epics (`EPIC-01`, `EPIC-02`, ...).
2. **Write INVEST User Stories (`US-XXX`)**:
   - Ensure each story is **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, and **T**estable.
   - Use standard format: `"As a [Persona], I want to [Action], so that [Business Value]."`
   - Link each `US-XXX` to its parent `FR-XX` and affected architecture components.
3. **Copy & Refine Acceptance Criteria**:
   - Attach the Gherkin scenarios from `docs/PRD.md` and add technical verification criteria from `docs/ARCHITECTURE.md`.
4. **Estimate & Split**:
   - Estimate each story with Fibonacci points (`1, 2, 3, 5, 8`).
   - If a story requires more than `8` points, split it into smaller vertical slices.
5. **Sequence Dependencies & Build Sprint Backlog**:
   - Order stories so foundational tasks (schemas, core interfaces, auth) precede dependent features.
   - Populate `docs/sprints/sprint-N.md` using `templates/SPRINT-BACKLOG-TEMPLATE.md`.
6. **Assign Target Release Version and Story Impact (SemVer 2.0.0)**:
   - Record the target release version in the sprint backlog metadata.
   - Add a version impact (`MAJOR`, `MINOR`, `PATCH`, or `NONE`) to every user story; the highest-impact story determines the release bump (see `skills/semantic-versioning/SKILL.md`).

## 4. Validation Checklist
- [ ] Does every `FR-XX` (`Must Have` and `Should Have`) map to at least one `US-XXX`?
- [ ] Are all stories in the active sprint estimated at `8` points or fewer?
- [ ] Are story dependencies free of circular references?
- [ ] Does every sprint story satisfy the Definition of Ready (DoR)?
- [ ] Does every story declare a SemVer version impact and does the sprint declare a target release version?
- [ ] Does the target release version reflect the highest-impact story in the sprint?
