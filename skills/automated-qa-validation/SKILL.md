---
name: automated-qa-validation
description: Validates implemented User Stories against the PRD using a Requirements Traceability Matrix, automated E2E tests, and defect reporting.
---

# Skill: Automated QA Validation

## 1. Objective
Independently verify that User Stories in `IN_REVIEW` status satisfy all functional, boundary, negative, and non-functional criteria in `docs/PRD.md`.

## 2. Required Inputs
- `docs/PRD.md`
- `docs/sprints/sprint-N.md`
- Source code and test suite from Software Engineer Agent

## 3. Step-by-Step Execution Procedure
1. **Build Requirements Traceability Matrix (RTM)**:
   - Populate `docs/TEST-PLAN.md` (from `templates/TEST-PLAN-TEMPLATE.md`).
   - Map every `FR-XX` -> `US-XXX` -> Test Case ID (`TC-XXX`).
2. **Design & Execute Test Suite**:
   - **Positive Tests**: Verify standard Gherkin happy-path scenarios.
   - **Negative & Boundary Tests**: Test invalid inputs, empty payloads, maximum/minimum limits, unauthorized access, and network timeouts.
   - **Non-Functional Checks**: Verify response time, memory limits, and security headers against `NFR-XX`.
3. **Validate Release Version & Changelog (SemVer 2.0.0)**:
   - Validate the version under test against SemVer 2.0.0 (`MAJOR.MINOR.PATCH[-pre][+build]`).
   - Confirm the version matches the target release version in `docs/PRD.md`, the sprint backlog, and `docs/CHANGELOG.md`.
   - Confirm the bump class matches the change impact; verify backwards compatibility for `MINOR` and `PATCH` and migration evidence for `MAJOR`.
   - Reference: `skills/semantic-versioning/SKILL.md`.
4. **Evaluate Results & Route**:
   - **If All Checks Pass**: Mark the User Story status as `DONE` in `docs/sprints/sprint-N.md` and record the pass result in `docs/TEST-PLAN.md`.
   - **If Any Check Fails**:
     1. Create a Defect Entry (`BUG-XXX`) in `docs/TEST-PLAN.md` with Severity (`P0`-`P3`), Steps to Reproduce, Expected Result, and Actual Result.
     2. Change the User Story status in `docs/sprints/sprint-N.md` back to `IN_PROGRESS`.

## 4. Validation Checklist
- [ ] Is every `FR-XX` in the current sprint linked to at least one executed `TC-XXX`?
- [ ] Were boundary and negative test cases executed in addition to happy-path tests?
- [ ] Are zero `P0` or `P1` defects open before signing off on the sprint release?
- [ ] Is the release version valid SemVer 2.0.0 and consistent across the PRD, sprint backlog, changelog, and build artifacts?
- [ ] Is the bump class consistent with the actual change impact?
