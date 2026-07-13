# Get started

There are two ways to install the swarm. **Project scope is the preferred path**
because it keeps the agent definitions versioned alongside the repository they
operate on.

- [Project scope](project-scope.md) — recommended. The package lives in your
  repository and each client reads its adapters from there.
- [User scope](user-scope.md) — copies the generated adapters into your per-user
  client directories with the provided installer scripts.
- [Verify](verify.md) — confirm the roster and adapters are intact.

## Requirements

- **Python 3** (for the validator and generators).
- **Git**.
- One or more supported clients: [Claude Code](../clients/claude-code.md),
  [Codex](../clients/codex.md), [Cursor](../clients/cursor.md), or
  [OpenCode](../clients/opencode.md).

!!! warning "Generated directories are generator-owned"
    `canonical/agents/` and the four client adapter directories are **generated**
    from `swarm/roster.json`. Do not edit them by hand and do not place
    hand-authored files inside them. Edit the roster and regenerate instead — see
    [Customize](../customize/index.md).

## Shells used in these docs

Command examples use two shells:

- **Bash** — for macOS or Linux, including a **remote macOS machine reached over
  SSH**.
- **PowerShell** — for a **local Windows machine**. The PowerShell examples are
  written to work with Windows PowerShell 5.1.

Run each example in the shell that matches where your repository actually lives.
Do not mix a local Windows path into a remote SSH session or vice versa.
