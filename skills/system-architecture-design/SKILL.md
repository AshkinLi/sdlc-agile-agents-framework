---
name: system-architecture-design
description: Translates an approved PRD into system architecture diagrams, interface contracts, data models, and Architecture Decision Records (ADRs).
---

# Skill: System Architecture Design

## 1. Objective
Create `docs/ARCHITECTURE.md`, interface contracts, and `docs/adr/ADR-XXX.md` files that satisfy 100% of the Functional and Non-Functional Requirements in `docs/PRD.md`.

## 2. Required Inputs
- `docs/PRD.md`
- Root `AGENTS.md` (Project technology stack settings)

## 3. Step-by-Step Execution Procedure
1. **Map Requirements to Components**:
   - Review all `FR-XX` and `NFR-XX` items in `docs/PRD.md`.
   - Define the high-level system architecture pattern (for example, Layered Monolith, Microservices, Event-Driven, Hexagonal, or Client-Server).
2. **Generate C4 Diagrams in Mermaid**:
   - Create a System Context diagram and a Container/Component diagram inside `docs/ARCHITECTURE.md`.
3. **Define Data Models & Storage**:
   - Write Entity-Relationship Diagrams (ERD) in Mermaid and define exact field types, primary keys, indexes, and constraints.
4. **Define Interface Contracts**:
   - Specify strict interfaces between modules or external clients (OpenAPI 3.1 YAML, GraphQL Schema, Protobuf, or typed function signatures).
   - Define standard error response payloads and status codes.
5. **Author Architecture Decision Records (ADRs)**:
   - Use `templates/ADR-TEMPLATE.md` to record each major technology selection or architectural trade-off in `docs/adr/ADR-001-[topic].md`.
6. **Define Source Directory Layout**:
   - Document the target folder structure for application source code and test suites.

## 4. Validation Checklist
- [ ] Does every `FR-XX` in `docs/PRD.md` map to at least one architectural component?
- [ ] Does the design satisfy all `NFR-XX` constraints (latency, scaling, security)?
- [ ] Are all Mermaid diagrams syntactically valid?
- [ ] Are interface contracts complete with request inputs, outputs, and error states?
