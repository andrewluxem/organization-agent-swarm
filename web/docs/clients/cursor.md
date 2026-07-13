# Cursor

Cursor reads project subagents from `.cursor/agents/`. Each agent is a Markdown
file with YAML frontmatter declaring its `name` and `description`. These files
are generated from `swarm/roster.json`.

## Start with the orchestrator

Open the repository in Cursor, start Agent, and paste the Universal kickoff
prompt from the [kickoff prompts](../examples/kickoff-prompts.md) page. Direct the
work to `worldwide-marketing-orchestrator` and let it route from there.

## Review before granting access

**Review each generated subagent definition** before granting it access to run
commands or edit files. Client capabilities and permission behavior may differ
from other clients and may change between versions.

## Notes

- The project is not affiliated with or endorsed by Cursor. The name is used only
  to identify this supported client. See the
  [disclaimer](../governance/index.md).
- This page avoids version-specific claims. Consult the client's own current
  documentation for exact behavior.
