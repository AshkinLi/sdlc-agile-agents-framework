---
name: tdd-code-implementation
description: Implements User Stories using strict Red-Green-Refactor Test-Driven Development (TDD) and clean code standards.
---

# Skill: TDD Code Implementation

## 1. Objective
Deliver clean, tested, and working code for a single User Story (`US-XXX`) from the active Sprint Backlog.

## 2. Required Inputs
- Active User Story from `docs/sprints/sprint-N.md`
- `docs/ARCHITECTURE.md` and interface contracts
- Build, Test, and Linter commands from root `AGENTS.md`

## 3. Step-by-Step Execution Procedure
1. **Prepare Context**:
   - Read the target `US-XXX` requirements, Gherkin scenarios, and architectural references.
   - Update the story status in `docs/sprints/sprint-N.md` to `IN_PROGRESS`.
2. **Step 1 - RED (Write Failing Tests)**:
   - Create unit and integration test files that map directly to each Gherkin scenario (happy path, boundary conditions, and error states).
   - Run the project test command. Verify that the new tests fail for the expected reason.
3. **Step 2 - GREEN (Write Minimum Implementation)**:
   - Write production code that follows `docs/ARCHITECTURE.md` to make the failing tests pass.
   - Run the test suite until 100% of tests pass.
4. **Step 3 - REFACTOR (Clean & Optimize)**:
   - Remove duplicated code, improve variable naming, enforce modular boundaries, and add brief comments for complex logic.
   - Run the linter, static type checker, and full test suite to confirm zero regressions.
5. **Version Bump & Changelog (SemVer 2.0.0)**:
   - Classify the change impact (`MAJOR`, `MINOR`, `PATCH`) using `skills/semantic-versioning/SKILL.md`.
   - Bump the project version in the manifest or version source.
   - Add an entry under `## [Unreleased]` in `docs/CHANGELOG.md` with the `US-XXX` and `FR-XX` references.
6. **Commit & Handoff**:
   - Commit with format: `feat(US-XXX): [summary] [FR-XX]`.
   - Update the story status in `docs/sprints/sprint-N.md` to `IN_REVIEW`.

## 4. Validation Checklist
- [ ] Does every Gherkin scenario in `US-XXX` have a corresponding automated test?
- [ ] Do all unit and integration tests pass?
- [ ] Does the linter and compiler report zero errors and zero warnings?
- [ ] Are all configuration values and secrets externalized to environment variables?
- [ ] Is the project version bumped and does `docs/CHANGELOG.md` contain the matching `[Unreleased]` entry?
- [ ] Does the bump class match the actual change impact (no breaking change under `MINOR` or `PATCH`)?
