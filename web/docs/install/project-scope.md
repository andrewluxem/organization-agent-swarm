# Project-scoped installation

Project scope is the recommended installation. The agent package lives inside the
Git repository it operates on, so the roster and generated adapters are versioned
and reviewed with the rest of your code.

## Steps

1. Copy the package contents into your repository (or clone this repository as a
   starting point).
2. Validate the roster and adapters.

### Bash (macOS or Linux, including a remote macOS host over SSH)

```bash
cd your-repository
python3 scripts/validate_swarm.py
```

### PowerShell (local Windows, PowerShell 5.1 compatible)

```powershell
Set-Location your-repository
python scripts\validate_swarm.py
```

Each client then reads its project-scoped adapters automatically:

- Claude Code: `.claude/agents/`
- Codex: `.codex/agents/`
- Cursor: `.cursor/agents/`
- OpenCode: `.opencode/agents/`

## Start working

Begin with the orchestrator and let it route the work:

```bash
claude --agent worldwide-marketing-orchestrator
```

See the per-client [supported clients](../clients/index.md) pages for the exact
entry point for Codex, Cursor, and OpenCode.

!!! note "No deployment here"
    Project-scoped installation runs entirely on your machine. This page contains
    no production deployment steps.
