#!/usr/bin/env python3
"""
Cross-Platform Bootstrap CLI for the SDLC + Agile + Multi-Agent Framework.

Creates a target project with the framework definition files consolidated under
`.agents/` (role definitions, skills, architecture specs, and templates),
initializes the `docs/` workspace (including a SemVer 2.0.0 `CHANGELOG.md`)
from templates, and configures the root `AGENTS.md` with the project
technology stack.

Generated project layout:

    <target>/
    ├── AGENTS.md
    ├── README.md
    ├── docs/
    │   ├── PRD.md
    │   ├── ARCHITECTURE.md
    │   ├── BACKLOG.md
    │   ├── TEST-PLAN.md
    │   ├── CHANGELOG.md
    │   ├── adr/ADR-001-initial-architecture.md
    │   └── sprints/sprint-1.md
    └── .agents/
        ├── roles/<role>/AGENTS.md
        ├── skills/<skill>/SKILL.md
        ├── architecture/*.md
        └── templates/*.md

Every framework cross-reference copied into the target is rewritten from the
source-repository paths (`agents/`, `skills/`, `architecture/`, `templates/`)
to the generated `.agents/` layout, so references remain valid relative to the
project root.
"""

import argparse
from datetime import date
from pathlib import Path
import re
import shutil
import sys


AGENTS_DIR = ".agents"

# Source repository path prefix -> generated project path prefix.
# None of the replacement outputs contains another prefix from this table.
PATH_REWRITES = (
    ("agents/", f"{AGENTS_DIR}/roles/"),
    ("skills/", f"{AGENTS_DIR}/skills/"),
    ("architecture/", f"{AGENTS_DIR}/architecture/"),
    ("templates/", f"{AGENTS_DIR}/templates/"),
)

FRAMEWORK_LOCATION_LINE = (
    "- **Framework Location**: `.agents/` holds role definitions, skills, "
    "architecture specs, and templates."
)

# Official SemVer 2.0.0 regex (semver.org FAQ) with [.] and [+] classes
# instead of escaped literal dots and plus signs.
SEMVER_PATTERN = re.compile(
    r"^(0|[1-9][0-9]*)[.](0|[1-9][0-9]*)[.](0|[1-9][0-9]*)"
    r"(?:-((?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:[.](?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:[+]([0-9A-Za-z-]+(?:[.][0-9A-Za-z-]+)*))?$"
)

# Operating-system junk that must never be copied into a generated project.
IGNORED_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}

README_TEMPLATE = """# {project_name}

This project was initialized from the Universal SDLC + Agile + Multi-Agent
Development Framework. The framework integrates the Software Development Life
Cycle (SDLC), Agile methodologies, and autonomous AI Agents.

## 1. Project Context

| Field | Value |
| :--- | :--- |
| **Project Name** | `{project_name}` |
| **Application Type** | `{app_type}` |
| **Primary Language** | `{primary_lang}` |
| **Build Command** | `{build_cmd}` |
| **Test Command** | `{test_cmd}` |
| **Linter Command** | `{lint_cmd}` |
| **Versioning** | `Semantic Versioning 2.0.0` |
| **Initial Version** | `{initial_version}` |

## 2. Directory Structure

```text
{project_name}/
├── AGENTS.md                                   # Root entry point: global directives, project context, routing table
├── README.md
├── docs/                                       # Project artifacts
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── BACKLOG.md
│   ├── TEST-PLAN.md
│   ├── CHANGELOG.md
│   ├── adr/
│   │   └── ADR-001-initial-architecture.md
│   └── sprints/
│       └── sprint-1.md
└── .agents/                                    # Framework definition files used by the agents
    ├── roles/
    │   ├── product-manager/AGENTS.md
    │   ├── system-architect/AGENTS.md
    │   ├── scrum-master/AGENTS.md
    │   ├── software-engineer/AGENTS.md
    │   ├── qa-engineer/AGENTS.md
    │   └── devops-engineer/AGENTS.md
    ├── skills/
    │   ├── prd-generation/SKILL.md
    │   ├── system-architecture-design/SKILL.md
    │   ├── agile-backlog-management/SKILL.md
    │   ├── tdd-code-implementation/SKILL.md
    │   ├── automated-qa-validation/SKILL.md
    │   ├── cicd-release-orchestration/SKILL.md
    │   └── semantic-versioning/SKILL.md
    ├── architecture/
    │   ├── 01-framework-overview.md
    │   └── 02-agile-sdlc-workflow.md
    └── templates/
        ├── PRD-TEMPLATE.md
        ├── ADR-TEMPLATE.md
        ├── SPRINT-BACKLOG-TEMPLATE.md
        ├── TEST-PLAN-TEMPLATE.md
        └── CHANGELOG-TEMPLATE.md
```

All framework definition files used by the agents live under `.agents/`; the
root `AGENTS.md` remains the entry point, and `docs/` holds the project
artifacts.

## 3. Framework Definition Files

| Path | Purpose |
| :--- | :--- |
| `AGENTS.md` | Global directives, project context (Section 2), and agent routing table |
| `.agents/roles/<role>/AGENTS.md` | Role definitions: PM, SA, SM, SWE, QA, DevOps |
| `.agents/skills/<skill>/SKILL.md` | Executable skill procedures |
| `.agents/architecture/` | SDLC + Agile workflow specifications |
| `.agents/templates/` | Reference artifact templates |
| `docs/` | Project artifacts: PRD, architecture, backlog, sprint, test plan, ADRs, changelog |
| `docs/CHANGELOG.md` | SemVer 2.0.0 release history (single source of release notes) |

## 4. Release Versioning (SemVer 2.0.0)

This project uses [Semantic Versioning 2.0.0](https://semver.org/). Version
increments must match the compatibility impact of each change:

| Change type | Version bump |
| :--- | :--- |
| Backwards-incompatible public API change | `MAJOR` |
| Backwards-compatible functionality or public API deprecation | `MINOR` |
| Backwards-compatible bug fix | `PATCH` |
| Initial development before a stable public API | `0.y.z` (start at `0.1.0`) |
| Release candidate | `X.Y.Z-rc.N` |

- The version MUST be identical in the project manifest, `docs/CHANGELOG.md`,
  and the Git tag (`vMAJOR.MINOR.PATCH` or `vMAJOR.MINOR.PATCH-rc.N`).
- Released versions and tags are immutable: never modify, reuse, or re-point
  them; corrections require a new version.
- Bump rules, precedence, validation commands, and per-role gates are defined in
  `.agents/skills/semantic-versioning/SKILL.md` and
  `.agents/architecture/02-agile-sdlc-workflow.md`.

## 5. Next Steps After Initialization

1. Open the project directory in your IDE or AI Agent CLI.
2. Start Phase 1 (Discovery): Instruct the **Product Manager Agent**
   (`.agents/roles/product-manager/AGENTS.md`) to populate `docs/PRD.md` using
   `.agents/skills/prd-generation/SKILL.md`.
3. Follow the sequential quality gates in
   `.agents/architecture/02-agile-sdlc-workflow.md`.
"""


def prompt_value(prompt_text: str, default: str, non_interactive: bool) -> str:
    if non_interactive:
        return default
    try:
        user_input = input(f"{prompt_text} [{default}]: ").strip()
        return user_input if user_input else default
    except EOFError:
        return default


def rewrite_paths(text: str) -> str:
    """Rewrite framework source paths to the generated .agents/ layout."""
    for old_prefix, new_prefix in PATH_REWRITES:
        text = text.replace(old_prefix, new_prefix)
    return text


def render_template(
    src: Path, dst: Path, replacements: dict[str, str], force: bool
) -> None:
    if dst.exists() and not force:
        print(f"[SKIP] {dst} already exists (use --force to overwrite)")
        return
    content = src.read_text(encoding="utf-8")
    for key, value in replacements.items():
        content = content.replace(key, value)
    content = rewrite_paths(content)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(content, encoding="utf-8")
    print(f"[OK] Generated {dst}")


def copy_tree(src_dir: Path, dst_dir: Path) -> int:
    """Copy a source tree, rewriting cross-references in Markdown files."""
    dst_dir.mkdir(parents=True, exist_ok=True)
    copied = 0
    for item in src_dir.rglob("*"):
        if item.name in IGNORED_FILES:
            continue
        relative = item.relative_to(src_dir)
        target_item = dst_dir / relative
        if item.is_dir():
            target_item.mkdir(parents=True, exist_ok=True)
            continue
        target_item.parent.mkdir(parents=True, exist_ok=True)
        if item.suffix == ".md":
            content = rewrite_paths(item.read_text(encoding="utf-8"))
            target_item.write_text(content, encoding="utf-8")
        else:
            shutil.copy2(item, target_item)
        copied += 1
    return copied


def configure_agents_md(src: Path, dst: Path, replacements: dict[str, str]) -> None:
    """Render the root AGENTS.md and expose the .agents/ location."""
    content = src.read_text(encoding="utf-8")
    for key, value in replacements.items():
        content = content.replace(key, value)
    content = rewrite_paths(content)
    lines = content.splitlines()
    if FRAMEWORK_LOCATION_LINE not in lines:
        patched = []
        inserted = False
        for line in lines:
            patched.append(line)
            if not inserted and line.startswith("- **Linter Command**"):
                patched.append(FRAMEWORK_LOCATION_LINE)
                inserted = True
        if not inserted:
            marker = next(
                (index for index, line in enumerate(lines) if line.startswith("## 3.")),
                None,
            )
            if marker is None:
                patched.append(FRAMEWORK_LOCATION_LINE)
            else:
                patched.insert(marker, FRAMEWORK_LOCATION_LINE)
        lines = patched
    dst.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Generated {dst}")


def generate_readme(dst: Path, values: dict[str, str], force: bool) -> None:
    if dst.exists() and not force:
        print(f"[SKIP] {dst} already exists (use --force to overwrite)")
        return
    dst.write_text(README_TEMPLATE.format(**values), encoding="utf-8")
    print(f"[OK] Generated {dst}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Initialize a project with the SDLC + Agile + Multi-Agent Framework. "
            "Framework definition files are consolidated under .agents/."
        )
    )
    parser.add_argument("-t", "--target", help="Target project directory")
    parser.add_argument("-n", "--name", help="Project name")
    parser.add_argument(
        "-a",
        "--type",
        dest="app_type",
        help="Application type (Web / Mobile / Backend API / CLI / Embedded / Desktop)",
    )
    parser.add_argument("-l", "--lang", help="Primary programming language and version")
    parser.add_argument("-b", "--build", help="Project build command")
    parser.add_argument("-s", "--test", help="Project test command")
    parser.add_argument("-c", "--lint", help="Project linter command")
    parser.add_argument(
        "--initial-version",
        default="0.1.0",
        help=(
            "Initial Semantic Versioning 2.0.0 version recorded in "
            "docs/CHANGELOG.md and docs/PRD.md (default: 0.1.0)"
        ),
    )
    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Non-interactive mode; accept defaults for unspecified options",
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Overwrite existing generated files (docs/, README.md)",
    )

    args = parser.parse_args()
    framework_dir = Path(__file__).resolve().parent
    today_str = date.today().isoformat()

    initial_version = args.initial_version.strip()
    if initial_version.startswith("v"):
        print(
            "[ERROR] --initial-version must not include the 'v' tag prefix "
            "(use 0.1.0 instead of v0.1.0)."
        )
        return 1
    if not SEMVER_PATTERN.fullmatch(initial_version):
        print(
            f"[ERROR] --initial-version '{args.initial_version}' is not a valid "
            "Semantic Versioning 2.0.0 version."
        )
        return 1

    print("==================================================================")
    print(" SDLC + Agile + Multi-Agent Framework Bootstrap")
    print("==================================================================")

    target_raw = args.target or prompt_value(
        "1. Enter target project path", str(Path.cwd()), args.yes
    )
    target_dir = Path(target_raw).expanduser().resolve()
    if target_dir == framework_dir:
        print("[ERROR] Target directory must differ from the framework source directory.")
        return 1
    target_dir.mkdir(parents=True, exist_ok=True)

    project_name = args.name or prompt_value(
        "2. Enter project name", target_dir.name, args.yes
    )
    app_type = args.app_type or prompt_value(
        "3. Enter application type (Web/Mobile/Backend API/CLI/Embedded/Desktop)",
        "Backend API",
        args.yes,
    )
    primary_lang = args.lang or prompt_value(
        "4. Enter primary language & version", "TypeScript 5.x", args.yes
    )
    build_cmd = args.build or prompt_value(
        "5. Enter build command", "npm run build", args.yes
    )
    test_cmd = args.test or prompt_value("6. Enter test command", "npm test", args.yes)
    lint_cmd = args.lint or prompt_value(
        "7. Enter linter command", "npm run lint", args.yes
    )

    print(f"\n[INFO] Initializing framework in: {target_dir}")
    print(f"[INFO] Framework definitions: {target_dir / AGENTS_DIR}")
    print(f"[INFO] Initial version: {initial_version}\n")

    # 1. Copy framework definition files into .agents/
    layout = (
        ("agents", "roles"),
        ("skills", "skills"),
        ("architecture", "architecture"),
        ("templates", "templates"),
    )
    for source_name, target_name in layout:
        destination = target_dir / AGENTS_DIR / target_name
        copied = copy_tree(framework_dir / source_name, destination)
        print(f"[OK] Copied {source_name}/ -> {destination} ({copied} files)")

    generate_readme(
        target_dir / "README.md",
        {
            "project_name": project_name,
            "app_type": app_type,
            "primary_lang": primary_lang,
            "build_cmd": build_cmd,
            "test_cmd": test_cmd,
            "lint_cmd": lint_cmd,
            "initial_version": initial_version,
        },
        args.force,
    )

    # 2. Configure root AGENTS.md
    agents_replacements = {
        "[Insert Project Name]": project_name,
        "[Web / Mobile / Backend API / CLI / Embedded / Desktop]": app_type,
        "[Insert Language & Version]": primary_lang,
        "[Insert Build Command]": build_cmd,
        "[Insert Test Command]": test_cmd,
        "[Insert Linter Command]": lint_cmd,
    }
    configure_agents_md(
        framework_dir / "AGENTS.md", target_dir / "AGENTS.md", agents_replacements
    )

    # 3. Initialize docs/ workspace from templates
    doc_replacements = {
        "[Insert Product Name]": project_name,
        "__INITIAL_VERSION__": initial_version,
        "[Insert Target Release Version]": initial_version,
        "YYYY-MM-DD": today_str,
        "Sprint `[N]`": "Sprint `1`",
        "Sprint [N]": "Sprint 1",
        "ADR-`[000]`": "ADR-`001`",
    }
    template_mappings = [
        ("PRD-TEMPLATE.md", target_dir / "docs" / "PRD.md"),
        (
            "ADR-TEMPLATE.md",
            target_dir / "docs" / "adr" / "ADR-001-initial-architecture.md",
        ),
        (
            "SPRINT-BACKLOG-TEMPLATE.md",
            target_dir / "docs" / "sprints" / "sprint-1.md",
        ),
        ("TEST-PLAN-TEMPLATE.md", target_dir / "docs" / "TEST-PLAN.md"),
        ("CHANGELOG-TEMPLATE.md", target_dir / "docs" / "CHANGELOG.md"),
    ]
    for template_name, destination in template_mappings:
        render_template(
            framework_dir / "templates" / template_name,
            destination,
            doc_replacements,
            args.force,
        )

    # 4. Create initial ARCHITECTURE.md and BACKLOG.md placeholders
    arch_doc = target_dir / "docs" / "ARCHITECTURE.md"
    if not arch_doc.exists() or args.force:
        arch_doc.write_text(
            f"# System Architecture: {project_name}\n\n"
            f"- **Status**: `DRAFT`\n"
            f"- **Last Updated**: `{today_str}`\n"
            f"- **Owner**: `System Architect Agent`\n\n"
            f"> Run the **System Architect Agent** "
            f"(`{AGENTS_DIR}/roles/system-architect/AGENTS.md`) "
            f"with `{AGENTS_DIR}/skills/system-architecture-design/SKILL.md` "
            f"after `docs/PRD.md` is approved.\n",
            encoding="utf-8",
        )
        print(f"[OK] Generated {arch_doc}")

    backlog_doc = target_dir / "docs" / "BACKLOG.md"
    if not backlog_doc.exists() or args.force:
        backlog_doc.write_text(
            f"# Product Backlog: {project_name}\n\n"
            f"- **Last Updated**: `{today_str}`\n"
            f"- **Owner**: `Scrum Master Agent`\n\n"
            f"> Run the **Scrum Master Agent** "
            f"(`{AGENTS_DIR}/roles/scrum-master/AGENTS.md`) "
            f"with `{AGENTS_DIR}/skills/agile-backlog-management/SKILL.md` "
            f"to populate Epics and User Stories.\n",
            encoding="utf-8",
        )
        print(f"[OK] Generated {backlog_doc}")

    print("\n==================================================================")
    print(" Bootstrap Complete!")
    print("==================================================================")
    print(f"1. Open target project: cd {target_dir}")
    print("2. Review AGENTS.md (project stack) and README.md (layout)")
    print(f"3. Framework definition files: {target_dir / AGENTS_DIR}")
    print(f"4. Release versioning: SemVer 2.0.0, initial version {initial_version} (docs/CHANGELOG.md)")
    print("5. Start Phase 1: Instruct the Product Manager Agent")
    print(f"   ({AGENTS_DIR}/roles/product-manager/AGENTS.md) to generate docs/PRD.md using")
    print(f"   {AGENTS_DIR}/skills/prd-generation/SKILL.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
