from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROSTER = ROOT / "swarm" / "roster.json"

def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)

def frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        fail(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
    return match.group(1)

def yaml_scalar(block: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", block, flags=re.M)
    return match.group(1).strip() if match else None

def main() -> None:
    payload = json.loads(ROSTER.read_text(encoding="utf-8"))
    agents = payload["agents"]
    if len(agents) != 20:
        fail(f"Expected 20 agents, found {len(agents)}")

    ids = [a["id"] for a in agents]
    if len(ids) != len(set(ids)):
        fail("Duplicate agent IDs")
    id_set = set(ids)

    roots = [a["id"] for a in agents if a.get("reports_to") is None]
    if roots != ["worldwide-marketing-orchestrator"]:
        fail(f"Unexpected roots: {roots}")

    records = {a["id"]: a for a in agents}
    for a in agents:
        parent = a.get("reports_to")
        if parent is not None and parent not in id_set:
            fail(f"Missing parent for {a['id']}: {parent}")
        for child in a.get("children", []):
            if child not in id_set:
                fail(f"Missing child for {a['id']}: {child}")
            if records[child].get("reports_to") != a["id"]:
                fail(f"Parent-child mismatch: {a['id']} -> {child}")

    platforms = {
        "claude": ROOT / ".claude" / "agents",
        "codex": ROOT / ".codex" / "agents",
        "cursor": ROOT / ".cursor" / "agents",
        "opencode": ROOT / ".opencode" / "agents",
        "canonical": ROOT / "canonical" / "agents",
    }

    expected = set(ids)
    for platform, directory in platforms.items():
        suffix = ".toml" if platform == "codex" else ".md"
        found = {p.stem for p in directory.glob(f"*{suffix}")}
        if found != expected:
            fail(f"{platform} mismatch; missing={sorted(expected-found)}, extra={sorted(found-expected)}")

    for agent_id in ids:
        if yaml_scalar(frontmatter(platforms["claude"] / f"{agent_id}.md"), "name") != agent_id:
            fail(f"Claude name mismatch: {agent_id}")
        if yaml_scalar(frontmatter(platforms["cursor"] / f"{agent_id}.md"), "name") != agent_id:
            fail(f"Cursor name mismatch: {agent_id}")

        opencode_fm = frontmatter(platforms["opencode"] / f"{agent_id}.md")
        expected_mode = "primary" if agent_id == "worldwide-marketing-orchestrator" else "subagent"
        if yaml_scalar(opencode_fm, "mode") != expected_mode:
            fail(f"OpenCode mode mismatch: {agent_id}")

        with (platforms["codex"] / f"{agent_id}.toml").open("rb") as handle:
            codex = tomllib.load(handle)
        for key in ("name", "description", "developer_instructions"):
            if key not in codex:
                fail(f"Codex {agent_id} missing {key}")
        if codex["name"] != agent_id:
            fail(f"Codex name mismatch: {agent_id}")

    with (ROOT / ".codex" / "config.toml").open("rb") as handle:
        codex_config = tomllib.load(handle)
    if codex_config.get("agents", {}).get("max_depth") != 2:
        fail("Codex max_depth must be 2")

    opencode = json.loads((ROOT / "opencode.json").read_text(encoding="utf-8"))
    if opencode.get("default_agent") != "worldwide-marketing-orchestrator":
        fail("OpenCode default_agent mismatch")

    required = [
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "team" / "operating-model.md",
        ROOT / "team" / "handoff-contract.md",
        ROOT / "examples" / "prompts.md",
    ]
    for path in required:
        if not path.exists():
            fail(f"Missing required file: {path.relative_to(ROOT)}")

    print("VALID")
    print(f"Agents: {len(agents)}")
    print("Hierarchy: 1 orchestrator, 3 leads, 16 specialists")
    print("Adapters: 80 platform-specific agent files")
    print("Platforms: Claude Code, Codex, Cursor, OpenCode")

if __name__ == "__main__":
    main()
