from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ROSTER = ROOT / "swarm" / "roster.json"

# Generated agent-file locations and their file extensions. The generator owns
# exactly these files; it must never create, modify, or delete anything else.
AGENT_DIRS: dict[str, str] = {
    "canonical/agents": ".md",
    ".claude/agents": ".md",
    ".cursor/agents": ".md",
    ".opencode/agents": ".md",
    ".codex/agents": ".toml",
}


def md_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def prompt_body(a: dict[str, Any]) -> str:
    hierarchy = (
        "You are the swarm's primary orchestrator."
        if a["tier"] == "orchestrator"
        else f"You report to `{a['reports_to']}`."
    )
    delegation = (
        "You may delegate only to: " + ", ".join(f"`{x}`" for x in a["children"]) + "."
        if a["children"]
        else "You do not delegate further. Return your work to your parent or the requesting user."
    )
    if a["kind"] == "coordinator":
        action = (
            "Default to coordination and review. Do not make implementation edits unless the user "
            "explicitly assigns them to you. Prefer bounded specialist tasks and require one "
            "accountable owner per output."
        )
    elif a["kind"] == "auditor":
        action = (
            "Remain independent and read-only. Do not repair the work you are evaluating. Report "
            "evidence, severity, and acceptance implications to the parent agent."
        )
    else:
        action = (
            "You may implement only the bounded slice assigned to you. Inspect before editing, keep "
            "unrelated files untouched, and never publish, deploy, send, spend, merge, push, or alter "
            "production data without explicit human approval."
        )
    return (
        f"# {a['title']}\n\n"
        "## Identity\n\n"
        f"You are `{a['id']}`, the **{a['title']}** agent in the Organization Agent Swarm.\n"
        f"{hierarchy}\n"
        f"Your division is **{a['division']}**.\n\n"
        f"## Mission\n\n{a['mission']}\n\n"
        f"## Core responsibilities\n\n{md_list(a['responsibilities'])}\n\n"
        f"## Expected deliverables\n\n{md_list(a['deliverables'])}\n\n"
        f"## Delegation\n\n{delegation}\n\n"
        "## Working method\n\n"
        "1. Read `AGENTS.md`, the current task, and the smallest relevant set of repository files.\n"
        "2. Restate the objective, constraints, evidence available, assumptions, and the exact slice you own.\n"
        "3. Inspect the current state before proposing or making changes.\n"
        "4. Create a bounded plan with acceptance criteria.\n"
        f"5. {action}\n"
        "6. Validate with the repository's real checks. Do not claim a check passed unless you ran it and observed the result.\n"
        "7. Return a concise handoff using the contract below.\n\n"
        "## Boundaries\n\n"
        "- Never expose, invent, or commit secrets, credentials, customer-level personal data, or proprietary material.\n"
        "- Do not use sensitive personal traits for targeting unless the task explicitly establishes a lawful, ethical, and approved basis.\n"
        "- Do not fabricate metrics, customer research, quotations, campaign results, or source attribution.\n"
        "- Treat external-platform reports as inputs, not proof of incrementality.\n"
        "- Flag legal, privacy, accessibility, brand, financial, and reputational risks instead of silently accepting them.\n"
        "- Respect file ownership. Parallel agents must not edit the same files.\n"
        "- Use separate branches or worktrees for parallel write tasks.\n"
        "- Stop and escalate when requirements conflict, evidence is missing, or the task would require an unapproved high-impact action.\n\n"
        "## Handoff contract\n\n"
        "Return:\n\n"
        "```text\n"
        "STATUS: complete | blocked | needs-decision\n"
        f"ROLE: {a['id']}\n"
        "OBJECTIVE:\n"
        "SUMMARY:\n"
        "EVIDENCE:\n"
        "- file, command, data source, or observation\n"
        "CHANGES:\n"
        "- files or artifacts changed; write \"none\" for analysis-only work\n"
        "VALIDATION:\n"
        "- commands/checks run and observed results\n"
        "RISKS:\n"
        "- severity, likelihood, and mitigation\n"
        "DECISIONS NEEDED:\n"
        "- explicit human decisions, or \"none\"\n"
        "NEXT HANDOFF:\n"
        "- recommended agent and bounded next task\n"
        "```\n"
    )


def claude_tools(a: dict[str, Any]) -> str:
    if a["kind"] == "coordinator":
        if a["children"]:
            return "Agent(" + ", ".join(a["children"]) + "), Read, Grep, Glob, Bash"
        return "Read, Grep, Glob, Bash"
    if a["kind"] == "auditor":
        return "Read, Grep, Glob, Bash"
    return "Read, Grep, Glob, Bash, Edit, Write"


def opencode_permission(a: dict[str, Any]) -> str:
    edit_value = "ask" if a["kind"] == "builder" else "deny"
    lines = [
        "permission:",
        f"  edit: {edit_value}",
        "  bash:",
        '    "*": ask',
        '    "git status*": allow',
        '    "git diff*": allow',
        '    "git log*": allow',
        '    "grep *": allow',
        '    "rg *": allow',
        "  task:",
        '    "*": deny',
    ]
    lines.extend(f'    "{child}": allow' for child in a["children"])
    return "\n".join(lines)


def normalized(content: str) -> str:
    """Match how files are persisted: no trailing whitespace, one final newline."""
    return content.rstrip() + "\n"


def expected_files(agents: list[dict[str, Any]]) -> dict[str, str]:
    """Return {relative_path: exact_expected_content} for every generated file."""
    files: dict[str, str] = {}
    for a in agents:
        body = prompt_body(a)

        canonical = (
            "---\n"
            f"id: {a['id']}\n"
            f"title: {json.dumps(a['title'])}\n"
            f"tier: {a['tier']}\n"
            f"division: {json.dumps(a['division'])}\n"
            f"reports_to: {a['reports_to'] or 'null'}\n"
            f"kind: {a['kind']}\n"
            "---\n\n" + body
        )
        files[f"canonical/agents/{a['id']}.md"] = normalized(canonical)

        claude = (
            "---\n"
            f"name: {a['id']}\n"
            f"description: {a['description']}\n"
            f"tools: {claude_tools(a)}\n"
            "---\n\n" + body
        )
        files[f".claude/agents/{a['id']}.md"] = normalized(claude)

        sandbox = "workspace-write" if a["kind"] == "builder" else "read-only"
        codex = (
            f"name = {json.dumps(a['id'])}\n"
            f"description = {json.dumps(a['description'])}\n"
            f"sandbox_mode = {json.dumps(sandbox)}\n"
            f"developer_instructions = {json.dumps(body)}\n"
        )
        files[f".codex/agents/{a['id']}.toml"] = normalized(codex)

        cursor = (
            "---\n"
            f"name: {a['id']}\n"
            f"description: {a['description']}\n"
            "---\n\n" + body
        )
        files[f".cursor/agents/{a['id']}.md"] = normalized(cursor)

        mode = "primary" if a["tier"] == "orchestrator" else "subagent"
        opencode = (
            "---\n"
            f"description: {a['description']}\n"
            f"mode: {mode}\n"
            f"{opencode_permission(a)}\n"
            "---\n\n" + body
        )
        files[f".opencode/agents/{a['id']}.md"] = normalized(opencode)
    return files


def stale_files(expected: dict[str, str]) -> list[str]:
    """Generated agent files present on disk that the current roster no longer defines.

    Scoped strictly to the agent directories and their extension so unrelated
    files are never considered for removal.
    """
    stale: list[str] = []
    for directory, suffix in AGENT_DIRS.items():
        base = ROOT / directory
        if not base.exists():
            continue
        for path in base.glob(f"*{suffix}"):
            rel = path.relative_to(ROOT).as_posix()
            if rel not in expected:
                stale.append(rel)
    return sorted(stale)


def run_check(expected: dict[str, str]) -> int:
    """Regression guard: fail if any generated file is missing, drifted, or stale."""
    problems: list[str] = []
    for rel, content in sorted(expected.items()):
        path = ROOT / rel
        if not path.exists():
            problems.append(f"MISSING  {rel}")
        elif path.read_text(encoding="utf-8") != content:
            problems.append(f"DRIFT    {rel}")
    for rel in stale_files(expected):
        problems.append(f"STALE    {rel}")
    if problems:
        print("Generator drift detected (run: python scripts/build_adapters.py):")
        for problem in problems:
            print(f"  {problem}")
        return 1
    print(f"CHECK OK: {len(expected)} generated files match swarm/roster.json.")
    return 0


def write_all(expected: dict[str, str]) -> list[str]:
    for rel, content in expected.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    removed = stale_files(expected)
    for rel in removed:
        (ROOT / rel).unlink()
    return removed


def main() -> None:
    agents = json.loads(ROSTER.read_text(encoding="utf-8"))["agents"]
    expected = expected_files(agents)

    if "--check" in sys.argv[1:]:
        raise SystemExit(run_check(expected))

    removed = write_all(expected)
    print(f"Built {len(agents)} agents for 4 platforms ({len(expected)} files).")
    if removed:
        print(f"Removed {len(removed)} stale generated file(s):")
        for rel in removed:
            print(f"  {rel}")


if __name__ == "__main__":
    main()
