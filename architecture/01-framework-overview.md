# System Architecture: SDLC + Agile + Multi-Agent Framework

## 1. Architectural Overview
This framework uses a hierarchical multi-agent architecture to execute software engineering tasks. The architecture separates strategic planning, technical design, iterative scheduling, code execution, quality verification, and release management into isolated agent contexts.

```text
+-----------------------------------------------------------------------+
|                        HUMAN STAKEHOLDER / PO                         |
+-----------------------------------+-----------------------------------+
                                    | Business Vision & Approval Gates
                                    v
+-----------------------------------------------------------------------+
|                      ROOT ORCHESTRATOR (AGENTS.md)                    |
+-----------------------------------+-----------------------------------+
                                    |
        +---------------------------+---------------------------+
        |                           |                           |
        v                           v                           v
+---------------+           +---------------+           +---------------+
|  PM Agent     |---------->|  SA Agent     |---------->|  SM Agent     |
| (Requirements)|  PRD.md   | (Architecture)|  Design   | (Agile Plan)  |
+---------------+           +---------------+           +-------+-------+
                                                                |
                                                   Sprint Tasks |
                                                                v
+-----------------------------------------------------------------------+
|                         AGILE SPRINT EXECUTION LOOP                   |
|                                                                       |
|   +-------------------+     PR / Code     +-------------------+       |
|   |     SWE Agent     |------------------>|     QA Agent      |       |
|   | (TDD Development) |<------------------| (Test & Verify)   |       |
|   +-------------------+   Defect Report   +---------+---------+       |
|                                                     | Verified Build  |
|                                                     v                 |
|                                           +-------------------+       |
|                                           |   DevOps Agent    |       |
|                                           | (CI/CD & Release) |       |
|                                           +-------------------+       |
+-----------------------------------------------------------------------+
```

## 2. Core Principles
1. **Context Isolation**: Each agent loads only the files required for its specific task. This reduces token consumption and prevents context pollution.
2. **Artifact-Driven Communication**: Agents communicate through structured Markdown files, JSON/YAML schemas, and Git commits in the repository. Agents do not rely on unstructured chat history.
3. **Immutable Contracts**: Once an upstream artifact (`PRD.md` or `OPENAPI.yaml`) passes its quality gate, downstream agents cannot modify it without triggering a formal change request.
4. **Shift-Left Verification**: Verification rules (Acceptance Criteria and Test Cases) are defined before the Software Engineer Agent writes application code.
5. **Semantic Versioning**: Every release follows Semantic Versioning 2.0.0 (`MAJOR.MINOR.PATCH`); version increments MUST reflect the compatibility impact of public API changes, and published versions are immutable. See `skills/semantic-versioning/SKILL.md`.

## 3. Universal Adaptability Mechanism
To support any software type, the framework separates **Workflow Logic** from **Tooling Execution**:
- **Workflow Logic** remains constant across all projects (Requirements -> Design -> Backlog -> TDD Code -> QA -> Release).
- **Tooling Execution** is injected dynamically through the root `AGENTS.md` configuration (build commands, test runners, linters, and deployment targets).
