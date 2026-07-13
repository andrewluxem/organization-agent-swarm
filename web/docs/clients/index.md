# Supported clients

The same roster is generated into project-scoped adapters for four coding-agent
clients. Each client reads its adapters from its own directory in the repository.

| Client | Adapter directory | File type |
|---|---|---|
| Claude Code | `.claude/agents/` | Markdown with YAML frontmatter |
| Codex | `.codex/agents/` | TOML |
| Cursor | `.cursor/agents/` | Markdown with YAML frontmatter |
| OpenCode | `.opencode/agents/` | Markdown with YAML frontmatter |

The platform-neutral role prompts live in `canonical/agents/`. All of these are
**generated** from `swarm/roster.json`; do not edit them by hand.

## Nominative use and independence

Client and platform names identify the **supported interoperability targets**
only. Organization Agent Swarm is an independent project and is **not affiliated
with, sponsored by, or endorsed by** Anthropic, OpenAI, Cursor, or OpenCode. See
the [disclaimer](../governance/index.md).

## Before you grant tool access

Client capabilities and permission behavior **differ** across these tools, and
they change over time. Always **review the generated agent definitions** — the
tools, permissions, and instructions they grant — before you let any agent run
commands or edit files in your environment.

## Per-client pages

- [Claude Code](claude-code.md)
- [Codex](codex.md)
- [Cursor](cursor.md)
- [OpenCode](opencode.md)
