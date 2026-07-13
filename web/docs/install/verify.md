# Verify the installation

Run the structural validator to confirm the roster and the generated adapters are
intact and consistent.

### Bash (macOS or Linux, including a remote macOS host over SSH)

```bash
python3 scripts/validate_swarm.py
```

### PowerShell (local Windows, PowerShell 5.1 compatible)

```powershell
python scripts\validate_swarm.py
```

## Expected output

```text
VALID
Agents: 20
Hierarchy: 1 orchestrator, 3 leads, 16 specialists
Adapters: 80 platform-specific agent files
Platforms: Claude Code, Codex, Cursor, OpenCode
```

If you also want to confirm that the generated adapters match the roster
byte-for-byte, run the drift check:

```bash
python3 scripts/build_adapters.py --check
```

Expected:

```text
CHECK OK: 100 generated files match swarm/roster.json.
```

!!! warning "Generated directories are generator-owned"
    If the drift check reports `DRIFT`, `MISSING`, or `STALE`, a generated file
    was edited or removed by hand. Regenerate with `python3
    scripts/build_adapters.py` rather than editing generated files directly.
