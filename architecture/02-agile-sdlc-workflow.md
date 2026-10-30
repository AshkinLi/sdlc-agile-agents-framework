# End-to-End Agile SDLC Workflow & Quality Gates

## 1. Phase 1: Discovery & Requirements (SDLC: Planning)
- **Active Agent**: Product Manager Agent (`agents/product-manager/AGENTS.md`)
- **Active Skill**: `skills/prd-generation/SKILL.md`
- **Input**: Stakeholder prompt, business goals, user pain points.
- **Process**:
  1. Analyze problem statement and identify target user personas.
  2. Define Functional Requirements (`FR-XX`) and Non-Functional Requirements (`NFR-XX`).
  3. Write Acceptance Criteria in Gherkin syntax (`Given/When/Then`).
  4. Document explicit Out-of-Scope items.
  5. Declare the target release version in SemVer 2.0.0 form and classify the release impact (`MAJOR`, `MINOR`, `PATCH`); list breaking public API changes with a migration note.
- **Output Artifact**: `docs/PRD.md` (based on `templates/PRD-TEMPLATE.md`).
- **Quality Gate 1 (Gate-PRD)**:
  - Zero unresolved `[TBD]` markers exist in `docs/PRD.md`.
  - Every `FR-XX` has at least one testable Gherkin scenario.
  - The PRD declares a valid SemVer target release version and no undeclared breaking change.
  - Human stakeholder approves `docs/PRD.md`.

## 2. Phase 2: Architecture & Technical Design (SDLC: Design)
- **Active Agent**: System Architect Agent (`agents/system-architect/AGENTS.md`)
- **Active Skill**: `skills/system-architecture-design/SKILL.md`
- **Input**: Approved `docs/PRD.md`.
- **Process**:
  1. Select or verify the technology stack in root `AGENTS.md`.
  2. Create C4 model diagrams (Mermaid syntax) for system context and containers.
  3. Define data models, database schemas, and interface contracts (OpenAPI/GraphQL/Protobuf/Header files).
  4. Record major architectural trade-offs in `docs/adr/ADR-XXX.md`.
  5. Document the project public API surface and classify every contract change as `MAJOR`, `MINOR`, `PATCH`, or `NONE`; record the classification in the affected ADR.
- **Output Artifacts**: `docs/ARCHITECTURE.md`, `docs/adr/*.md`, API/Schema contracts.
- **Quality Gate 2 (Gate-ARCH)**:
  - Every `FR-XX` and `NFR-XX` in the PRD maps to a system component.
  - Interface schemas pass syntax validation.
  - The public API is documented and every contract change carries a SemVer impact classification.

## 3. Phase 3: Agile Backlog & Sprint Planning (Agile: Planning)
- **Active Agent**: Scrum Master Agent (`agents/scrum-master/AGENTS.md`)
- **Active Skill**: `skills/agile-backlog-management/SKILL.md`
- **Input**: `docs/PRD.md`, `docs/ARCHITECTURE.md`.
- **Process**:
  1. Decompose PRD features into Epics and granular User Stories (`US-XXX`).
  2. Estimate complexity using Fibonacci story points (`1, 2, 3, 5, 8`). Split any story larger than `8` points.
  3. Map task dependencies and group ready stories into a Sprint Backlog (`docs/sprints/sprint-N.md`).
  4. Assign each story a version impact (`MAJOR`, `MINOR`, `PATCH`, or `NONE`) and record the release target version in the sprint backlog metadata.
- **Output Artifacts**: `docs/BACKLOG.md`, `docs/sprints/sprint-N.md`.
- **Quality Gate 3 (Gate-DOR - Definition of Ready)**:
  - Every User Story in the sprint has a linked `FR-XX`, architectural reference, story point estimate, Gherkin acceptance criteria, and SemVer version impact.
  - The sprint backlog declares a valid target release version.

## 4. Phase 4: Iterative Implementation (SDLC: Implementation / Agile: Sprint Execution)
- **Active Agent**: Software Engineer Agent (`agents/software-engineer/AGENTS.md`)
- **Active Skill**: `skills/tdd-code-implementation/SKILL.md`
- **Input**: `docs/sprints/sprint-N.md`, `docs/ARCHITECTURE.md`.
- **Process (Red-Green-Refactor Loop)**:
  1. Pick the highest-priority `TODO` User Story from `docs/sprints/sprint-N.md`.
  2. **RED**: Write automated unit and integration tests that verify the story's Gherkin acceptance criteria. Run the test suite to confirm the tests fail.
  3. **GREEN**: Write the minimum production code required to make the tests pass.
  4. **REFACTOR**: Clean up code structure, remove duplication, and run the linter.
  5. Classify the change impact, bump the project version, and add the matching entry to `docs/CHANGELOG.md` under `[Unreleased]`.
  6. Commit changes with message format: `feat(US-XXX): [short description] [FR-XX]`.
- **Output Artifacts**: Source code, unit/integration tests, Git branch/PR, version bump and `docs/CHANGELOG.md` entry.
- **Quality Gate 4 (Gate-CODE)**:
  - Project builds with zero errors.
  - Linter and static type checks pass with zero warnings.
  - All unit tests pass, and code coverage meets the threshold defined in `docs/PRD.md` (default: >= 80%).
  - The project version and `docs/CHANGELOG.md` entry are present and match the classified change impact.

## 5. Phase 5: Quality Assurance & Verification (SDLC: Testing / Agile: Review)
- **Active Agent**: QA Engineer Agent (`agents/qa-engineer/AGENTS.md`)
- **Active Skill**: `skills/automated-qa-validation/SKILL.md`
- **Input**: Pull Request from SWE Agent, `docs/PRD.md`, `docs/sprints/sprint-N.md`.
- **Process**:
  1. Generate a Requirements Traceability Matrix (RTM) that links `FR-XX` -> `US-XXX` -> Test Case ID (`TC-XXX`).
  2. Execute functional, boundary, negative, and non-functional (performance/security) tests.
  3. If defects occur, log structured bug reports and return the story status to `IN_PROGRESS` for the SWE Agent.
  4. If all tests pass, mark the User Story as `DONE`.
  5. Validate the release version (`MAJOR.MINOR.PATCH[-pre][+build]`), the bump classification, changelog completeness, and backwards compatibility before sign-off.
- **Output Artifacts**: `docs/TEST-PLAN.md`, Automated E2E tests, QA Sign-off Report.
- **Quality Gate 5 (Gate-DOD - Definition of Done)**:
  - 100% of Gherkin acceptance criteria pass automated verification.
  - Zero Critical (`P0`) or High (`P1`) severity defects remain open.
  - The release version is valid SemVer 2.0.0, matches `docs/CHANGELOG.md`, and no breaking change is shipped under `MINOR` or `PATCH`.

## 6. Phase 6: Deployment, Release & Retrospective (SDLC: Deployment & Maintenance)
- **Active Agent**: DevOps Engineer Agent (`agents/devops-engineer/AGENTS.md`) & Scrum Master Agent
- **Active Skill**: `skills/cicd-release-orchestration/SKILL.md`
- **Input**: QA-approved release branch.
- **Process**:
  1. Execute CI/CD pipeline (build artifact, containerize/package, run security vulnerability scans).
  2. Deploy to staging, run smoke tests, and promote to production using Blue/Green or Canary strategy.
  3. Validate the version, publish the immutable SemVer tag (`vX.Y.Z` or `vX.Y.Z-rc.N`), and release the matching `docs/CHANGELOG.md` section; never move or reuse a published tag.
  4. Scrum Master Agent updates Sprint Velocity metrics and logs retrospective action items.
- **Output Artifacts**: Production Release, immutable Git tag (`vX.Y.Z`), `docs/CHANGELOG.md`, Sprint Retrospective Report.
- **Quality Gate 6 (Gate-RELEASE)**:
  - Post-deployment smoke tests pass.
  - Health checks and monitoring alerts show normal baseline metrics.
  - The published tag is valid SemVer, immutable, and identical to the version in the project manifest and `docs/CHANGELOG.md`.
