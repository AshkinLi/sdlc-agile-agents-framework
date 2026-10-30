# QA Test Plan & Traceability Report

| Metadata | Details |
| :--- | :--- |
| **Test Plan ID** | `TP-001` |
| **Target Sprint / Release** | `Sprint [N] / vX.Y.Z` |
| **Release Version Under Test (SemVer)** | `X.Y.Z[-pre][+build]` |
| **Author** | `QA Engineer Agent` |
| **QA Sign-Off Status** | `PENDING / APPROVED / REJECTED` |

## 1. Requirements Traceability Matrix (RTM)
| PRD ID | User Story ID | Test Case ID | Test Type | Test Description | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `FR-01` | `US-101` | `TC-001` | `Unit / Integration` | `[Verify happy path]` | `PASS / FAIL` |
| `FR-01` | `US-101` | `TC-002` | `Boundary / Negative` | `[Verify invalid input handling]` | `PASS / FAIL` |
| `NFR-01` | `Global` | `TC-003` | `Performance` | `[Verify latency < 200ms]` | `PASS / FAIL` |

## 2. Defect Log
| Defect ID | Related Story | Severity | Summary | Steps to Reproduce | Expected vs Actual | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BUG-001` | `US-101` | `P1-High` | `[Issue summary]` | `1. [...] 2. [...]` | `Expected: [...] Actual: [...]` | `OPEN / CLOSED` |

## 3. SemVer 2.0.0 & Version Validation
| Check | Expected | Result |
| :--- | :--- | :--- |
| Version string validity | Matches `MAJOR.MINOR.PATCH[-pre][+build]` without leading zeroes | `PASS / FAIL` |
| Version consistency | Matches PRD target release version, sprint backlog, changelog, and build artifact | `PASS / FAIL` |
| Bump classification | `MAJOR` / `MINOR` / `PATCH` matches the actual change impact | `PASS / FAIL` |
| Compatibility | `MINOR` / `PATCH` preserve backwards compatibility; `MAJOR` includes migration evidence | `PASS / FAIL` |

Reference: `skills/semantic-versioning/SKILL.md`.

## 4. Release Quality Gate Sign-Off (`Gate-DOD`)
- [ ] 100% of `Must Have` Functional Requirements have passing automated tests.
- [ ] Code coverage meets target threshold (`>= 80%`).
- [ ] Zero `P0-Critical` and zero `P1-High` defects remain open.
- [ ] Non-Functional Requirements (`NFR-XX`) verified.
- [ ] Release version is valid SemVer 2.0.0 and consistent across PRD, sprint backlog, changelog, and artifacts.
- [ ] The bump class matches the change impact, and no breaking change is shipped under `MINOR` or `PATCH`.
