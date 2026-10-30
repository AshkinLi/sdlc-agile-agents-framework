---
name: prd-generation
description: Generates a standardized, traceable Product Requirements Document (PRD) from business ideas or feature requests.
---

# Skill: Product Requirements Document (PRD) Generation

## 1. Objective
Produce a complete `docs/PRD.md` file based on `templates/PRD-TEMPLATE.md`. The output must give downstream Architecture, Scrum, Engineering, and QA agents exact specifications without ambiguity.

## 2. Required Inputs
- Stakeholder problem statement, business goals, or feature request.
- Existing system constraints (if applicable).

## 3. Step-by-Step Execution Procedure
1. **Define Product Purpose & Vision**:
   - Write a 1-paragraph executive summary of the product.
   - Define 3 to 5 measurable Success Metrics (KPIs) with target numbers.
2. **Identify User Personas**:
   - List each user role, their primary goal, and their technical constraint.
3. **Specify Functional Requirements (`FR-XX`)**:
   - Assign a unique ID (`FR-01`, `FR-02`, ...).
   - Assign a MoSCoW priority (`Must Have`, `Should Have`, `Could Have`, `Won't Have`).
   - Write clear requirement statements using the active voice: `"The system shall [action] when [trigger]."`
4. **Write Gherkin Acceptance Criteria**:
   - For every `FR-XX`, write at least two scenarios (one happy path, one edge/error path):
     ```gherkin
     Scenario: [Descriptive Title]
       Given [Initial Context / Precondition]
       When [Actor Performs Action]
       Then [Expected Observable Outcome]
     ```
5. **Specify Non-Functional Requirements (`NFR-XX`)**:
   - Quantify Performance (latency, throughput), Security (auth protocol, encryption standard), Reliability (uptime %, RPO/RTO), and Compatibility targets.
6. **Declare Scope Boundaries**:
   - List explicit `In-Scope` and `Out-of-Scope` items to prevent scope creep.
7. **Declare the Target Release Version (SemVer 2.0.0)**:
   - Set the target release version in the PRD metadata using `MAJOR.MINOR.PATCH` (start at `0.1.0` during initial development).
   - Classify the release impact (`MAJOR`, `MINOR`, `PATCH`) and list every breaking public API change with a migration note.
   - Follow `skills/semantic-versioning/SKILL.md` for bump rules, precedence, and validation.

## 4. Validation Checklist (Self-Correction Before Completion)
- [ ] Does the file follow the exact section structure of `templates/PRD-TEMPLATE.md`?
- [ ] Does every `FR-XX` have a unique ID, MoSCoW priority, and Gherkin acceptance criteria?
- [ ] Are all vague terms replaced with quantifiable numbers?
- [ ] Are all `[TBD]` placeholders resolved or explicitly listed in the Open Questions table with an assigned owner?
- [ ] Does the PRD declare a valid SemVer 2.0.0 target release version and a version impact?
- [ ] Are all breaking public API changes listed with a migration note and a `MAJOR` bump?
