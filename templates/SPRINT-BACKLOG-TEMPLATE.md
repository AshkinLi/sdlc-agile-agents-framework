# Sprint Backlog: Sprint `[N]`

| Metadata | Details |
| :--- | :--- |
| **Sprint Number** | `Sprint [N]` |
| **Sprint Goal** | `[1-sentence measurable objective for this sprint]` |
| **Start / End Date** | `YYYY-MM-DD` to `YYYY-MM-DD` |
| **Planned Capacity** | `[Total Story Points]` |

## 1. Sprint Task Board
| Story ID | Linked FR | Title | Story Points | Dependencies | Status | Assigned Agent |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `US-101` | `FR-01` | `[Story Title]` | `3` | `None` | `TODO` | `SWE-Agent` |
| `US-102` | `FR-02` | `[Story Title]` | `5` | `US-101` | `TODO` | `SWE-Agent` |

---

## 2. User Story Details

### `US-101`: `[Story Title]`
- **Linked PRD Requirement**: `FR-01`
- **Architecture Reference**: `docs/ARCHITECTURE.md#[section]`
- **Story Statement**: As a `[Persona]`, I want to `[Action]`, so that `[Value]`.
- **Story Points**: `3`
- **Status**: `TODO / IN_PROGRESS / IN_REVIEW / DONE / BLOCKED`
- **Acceptance Criteria**:
  ```gherkin
  Scenario: [Scenario Name]
    Given [precondition]
    When [action]
    Then [outcome]
  ```
- **Definition of Ready (DoR) Check**:
  - [x] Mapped to `FR-XX`
  - [x] Architecture contract defined
  - [x] Story points <= 8
  - [x] Testable Gherkin criteria attached
