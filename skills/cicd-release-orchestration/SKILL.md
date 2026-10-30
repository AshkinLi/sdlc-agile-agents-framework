---
name: cicd-release-orchestration
description: Automates build verification, security scanning, artifact packaging, deployment, and semantic release notes generation.
---

# Skill: CI/CD & Release Orchestration

## 1. Objective
Package, scan, deploy, and monitor QA-approved software releases with automated rollback safety.

## 2. Required Inputs
- QA-approved codebase (`Gate-DOD` passed)
- `docs/ARCHITECTURE.md` and `docs/TEST-PLAN.md`

## 3. Step-by-Step Execution Procedure
1. **Continuous Integration (CI) Verification**:
   - Run clean dependency installation using lockfiles.
   - Execute linter, static type checks, unit tests, integration tests, and E2E tests in an isolated environment.
2. **Security & Compliance Scanning**:
   - Run Static Application Security Testing (SAST) and dependency audit (`npm audit`, `pip-audit`, `cargo audit`, `trivy`, or equivalent).
   - Scan repository history for accidentally committed secrets.
3. **Artifact Build & Packaging**:
   - Build immutable release artifacts (Docker container image, binary executable, or mobile bundle) and generate SHA-256 checksums.
4. **Release Versioning & Changelog (SemVer 2.0.0)**:
   - Determine the next version from the merged change classifications: `MAJOR` for backwards-incompatible public API changes, `MINOR` for backwards-compatible functionality or deprecations, `PATCH` for backwards-compatible fixes (see `skills/semantic-versioning/SKILL.md`).
   - Validate the version string against SemVer 2.0.0 and confirm it matches the project manifest and the target release version in `docs/PRD.md`.
   - Create an immutable annotated tag (`vX.Y.Z`, or `vX.Y.Z-rc.N` for release candidates); never move, delete, or reuse a published tag.
   - Move the `[Unreleased]` entries in `docs/CHANGELOG.md` under the released version with an ISO 8601 date, including linked `US-XXX` and `FR-XX` IDs.
5. **Deployment & Smoke Verification**:
   - Deploy to staging, execute automated smoke tests against health endpoints, and promote to production.
   - If smoke tests or health metrics fail, trigger automated rollback to the previous stable version immediately.

## 4. Validation Checklist
- [ ] Did all CI test suites and security scans pass with zero critical vulnerabilities?
- [ ] Is the release artifact reproducible and tagged with a semantic version?
- [ ] Is `CHANGELOG.md` updated with all completed User Stories and bug fixes?
- [ ] Are post-deployment smoke tests and rollback triggers verified?
- [ ] Is the release version valid SemVer 2.0.0 and identical in the manifest, `docs/CHANGELOG.md`, and Git tag?
- [ ] Is the release tag immutable, and does the changelog section match the released version?
- [ ] Does the bump class match the change impact (no breaking change shipped as `MINOR` or `PATCH`)?
