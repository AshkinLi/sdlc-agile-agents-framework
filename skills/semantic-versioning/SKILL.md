---
name: semantic-versioning
description: Enforces Semantic Versioning 2.0.0 across requirements, architecture, implementation, QA, and release artifacts.
---

# Skill: Semantic Versioning 2.0.0 Compliance

## 1. Objective
Ensure every version identifier produced, consumed, or published by the agent workflow is a valid Semantic Versioning 2.0.0 (SemVer) version, and that version increments truthfully communicate the impact of changes to downstream consumers.

Authoritative reference: [Semantic Versioning 2.0.0 specification](https://semver.org/). This skill restates the normative rules for agent execution; the published specification remains the source of truth for edge cases.

## 2. Scope and Definitions
- **Public API**: The stable contract exposed to external consumers. The System Architect Agent MUST document it in `docs/ARCHITECTURE.md`. Examples by application type:
  - **Web / PWA**: documented routes and URL contracts, persisted browser storage schemas, service worker and cache contracts, public configuration.
  - **Backend API**: HTTP paths, request and response schemas, status codes, authentication flows, published events.
  - **CLI**: command names, flags, arguments, exit codes, stdout and stderr contracts.
  - **Library**: exported symbols, type signatures, documented behavior.
  - **Desktop / Mobile / Embedded**: documented user-visible behavior, file formats, IPC and device contracts.
- **Version core**: `MAJOR.MINOR.PATCH` where each part is a non-negative integer written without leading zeroes.
- **Pre-release**: `-<dot.separated.identifiers>` appended to the version core. It has lower precedence than the associated normal version.
- **Build metadata**: `+<dot.separated.identifiers>` appended after the version core or pre-release. It MUST be ignored for precedence.
- **Release tag**: `vMAJOR.MINOR.PATCH` or `vMAJOR.MINOR.PATCH-<pre-release>` in Git. The `v` prefix belongs to the tag name, never to the version string itself.

## 3. Normative Rules (SemVer 2.0.0)
1. Software using SemVer MUST declare a precise public API, either in code or in documentation.
2. A normal version MUST be `MAJOR.MINOR.PATCH` with non-negative integer components and MUST NOT contain leading zeroes.
3. Once a versioned release is published, its contents MUST NOT be modified. Any modification MUST be published as a new version.
4. Major version zero (`0.y.z`) is for initial development. Anything MAY change at any time, and the public API SHOULD NOT be considered stable.
5. Version `1.0.0` defines the public API. Version increments after `1.0.0` MUST follow rules 6 through 11 below.
6. `PATCH` (`x.y.Z`) MUST be incremented only for backwards-compatible bug fixes.
7. `MINOR` (`x.Y.z`) MUST be incremented for new backwards-compatible functionality in the public API, and MUST be incremented when public API functionality is deprecated. It MAY include `PATCH` level changes. `PATCH` MUST reset to `0`.
8. `MAJOR` (`X.y.z`) MUST be incremented for backwards-incompatible public API changes. It MAY include `MINOR` and `PATCH` changes. `MINOR` and `PATCH` MUST reset to `0`.
9. Pre-release identifiers MUST contain only ASCII alphanumerics and hyphens, MUST NOT be empty, and numeric identifiers MUST NOT include leading zeroes. A pre-release version has lower precedence than the associated normal version.
10. Build metadata identifiers MUST contain only ASCII alphanumerics and hyphens, MUST NOT be empty, and MUST be ignored when determining precedence.
11. Precedence rules:
    - Compare `MAJOR`, then `MINOR`, then `PATCH` numerically.
    - A pre-release version has lower precedence than the associated normal version.
    - Compare dot-separated pre-release identifiers left to right: numeric identifiers are compared numerically, alphanumeric identifiers are compared lexically in ASCII sort order, numeric identifiers always have lower precedence than alphanumeric identifiers, and a larger set of identifiers wins when all preceding identifiers are equal.

## 4. Bump Decision Matrix
| Change type | Required bump | Notes |
| :--- | :--- | :--- |
| Backwards-incompatible public API change | `MAJOR` | Removals, renames, type or behavior changes, and changes that break existing clients or persisted data. |
| New backwards-compatible public API functionality | `MINOR` | New optional fields, endpoints, flags, and capabilities. |
| Deprecation of public API functionality | `MINOR` | Removal MUST wait for a subsequent `MAJOR` release with a documented migration path. |
| Backwards-compatible bug fix | `PATCH` | No public API change; incorrect behavior is corrected. |
| Internal refactor, dependency update, documentation-only change | `PATCH` or no release | `MINOR` when new functionality is introduced; `PATCH` when only a fix is delivered. |
| Initial development before a stable public API | `0.y.z` | Start at `0.1.0` and increment `MINOR` for each release during initial development. |
| First stable public API | `1.0.0` | Requires explicit Product Manager and System Architect approval. |
| Pre-release candidate for an upcoming version | `X.Y.Z-<identifier>` | Example: `1.0.0-rc.1`. A pre-release MUST NOT be republished as a normal release. |
| Build or packaging variation with identical API | Same version core plus `+build` metadata | Build metadata MUST NOT be used to communicate compatibility. |

## 5. Release and Tagging Rules
- Tags MUST use `v` plus a valid SemVer version: `git tag -a v1.4.2 -m "Release 1.4.2"`.
- Release tags are immutable: DO NOT delete, move, or re-point a published tag; DO NOT publish two different artifacts under the same version.
- Pre-release tags MUST include the full pre-release identifier: `v2.0.0-rc.1`.
- Build metadata MAY appear in artifact labels but MUST NOT be used to decide precedence.
- If an invalid release is detected, publish a new version that restores compliance (per the SemVer FAQ), document the offending version, and notify consumers.
- Version strings in package manifests, changelogs, documentation, and Git tags MUST match.

## 6. Workflow Gates by Role
| Phase | Owner | Versioning obligation | Artifact |
| :--- | :--- | :--- | :--- |
| Requirements | Product Manager | Declare the SemVer target release version and the version impact of scope changes | `docs/PRD.md` |
| Architecture | System Architect | Document the public API and classify contract changes as `MAJOR`, `MINOR`, `PATCH`, or `NONE` | `docs/ARCHITECTURE.md`, `docs/adr/*.md` |
| Planning | Scrum Master | Assign each sprint and release a target version; a single `MAJOR` impact story forces a `MAJOR` bump | `docs/sprints/sprint-N.md` |
| Implementation | Software Engineer | Bump the version and add a changelog entry for every change | Version manifest, `docs/CHANGELOG.md` |
| Verification | QA Engineer | Validate version grammar, bump class, changelog completeness, and backwards compatibility | `docs/TEST-PLAN.md` |
| Release | DevOps Engineer | Create and publish the immutable version tag and release notes | Git tag, `docs/CHANGELOG.md` |

## 7. Changelog Requirements
- The single changelog is `docs/CHANGELOG.md`; it MUST use `## [Unreleased]` for pending changes.
- Every merged change adds an entry under `Unreleased` with a `US-XXX` and `FR-XX` reference.
- On release, move the `Unreleased` entries under a heading containing the exact version and an ISO 8601 date, for example `## [1.4.2] - 2026-10-30`.
- Released sections MUST NOT be rewritten or reused; corrections are appended in a new release.
- Recommended category headings: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.

## 8. Validation
### 8.1 Version string validation (Python)
```python
import re

SEMVER = re.compile(
    r"^(0|[1-9][0-9]*)[.](0|[1-9][0-9]*)[.](0|[1-9][0-9]*)"
    r"(?:-((?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:[.](?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:[+]([0-9A-Za-z-]+(?:[.][0-9A-Za-z-]+)*))?$"
)


def is_semver(value: str) -> bool:
    return SEMVER.fullmatch(value) is not None
```

### 8.2 Release validation (CI)
```python
import re
import subprocess
import sys

SEMVER = re.compile(
    r"^(0|[1-9][0-9]*)[.](0|[1-9][0-9]*)[.](0|[1-9][0-9]*)"
    r"(?:-((?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:[.](?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:[+]([0-9A-Za-z-]+(?:[.][0-9A-Za-z-]+)*))?$"
)


def is_semver(value: str) -> bool:
    return SEMVER.fullmatch(value) is not None


def main() -> int:
    for tag in subprocess.check_output(
        ["git", "tag", "--list", "v*"], text=True
    ).splitlines():
        version = tag[1:]
        if not is_semver(version):
            print(f"INVALID TAG: {tag}")
            return 1
    with open("docs/CHANGELOG.md", encoding="utf-8") as handle:
        changelog = handle.read()
    for line in changelog.splitlines():
        if line.startswith("## [") and line.endswith("]"):
            value = line[4:-1].strip()
            if value != "Unreleased" and not is_semver(value):
                print(f"INVALID CHANGELOG VERSION: {value}")
                return 1
    print("SemVer validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## 9. Anti-Patterns
- Using `v1.2.3` as the version string. The `v` prefix is allowed only in tag names.
- Omitting version components (`1.2`, `1`) or adding leading zeroes (`01.2.3`).
- Raising `PATCH` for new functionality or raising `MINOR` for a breaking change. Semantics take priority over convenience.
- Reusing, modifying, or re-tagging a published version.
- Using build metadata to encode compatibility or ordering.
- Starting at `1.0.0` before a stable public API is approved.
- Publishing release notes that do not match the manifest version and Git tag.
- Deriving versions from dates, sprint numbers, or marketing names instead of change impact.

## 10. Related Artifacts
- Root policy: `AGENTS.md` (Global Directive 5 and Versioning Policy section).
- Role definitions: `agents/product-manager/AGENTS.md`, `agents/system-architect/AGENTS.md`, `agents/scrum-master/AGENTS.md`, `agents/software-engineer/AGENTS.md`, `agents/qa-engineer/AGENTS.md`, `agents/devops-engineer/AGENTS.md`.
- Skills: `skills/prd-generation/SKILL.md`, `skills/system-architecture-design/SKILL.md`, `skills/agile-backlog-management/SKILL.md`, `skills/tdd-code-implementation/SKILL.md`, `skills/automated-qa-validation/SKILL.md`, `skills/cicd-release-orchestration/SKILL.md`.
- Templates: `templates/PRD-TEMPLATE.md`, `templates/ADR-TEMPLATE.md`, `templates/SPRINT-BACKLOG-TEMPLATE.md`, `templates/TEST-PLAN-TEMPLATE.md`, `templates/CHANGELOG-TEMPLATE.md`.
- Workflow gates: `architecture/02-agile-sdlc-workflow.md`.
