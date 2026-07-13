# User-scoped installation

User scope copies the generated adapters into your per-user client directories.
Project scope is safer because it keeps agents versioned with the repository, but
user scope is useful when you want the swarm available across several local
projects.

The installer scripts copy each generated adapter directory into the matching
per-user client location (for example, the Claude Code, Codex, Cursor, and
OpenCode user directories under your home directory).

### Bash (macOS or Linux, including a remote macOS host over SSH)

```bash
bash scripts/install-user-scope.sh
```

### PowerShell (local Windows, PowerShell 5.1 compatible)

```powershell
./scripts/install-user-scope.ps1
```

The scripts write into your user profile directory (`$HOME` on macOS or Linux,
`%USERPROFILE%` on Windows). They do not require administrator rights and they do
not deploy anything off your machine.

!!! warning "Re-run after regenerating"
    User-scope copies are snapshots. If you change `swarm/roster.json` and
    regenerate, re-run the installer to refresh the per-user copies. Never edit
    the copied adapter files by hand — they are generator-owned.
