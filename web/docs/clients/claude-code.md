# Claude Code

Claude Code reads project agents from `.claude/agents/`. Each agent is a Markdown
file with YAML frontmatter that declares its `name`, `description`, and allowed
`tools`. These files are generated from `swarm/roster.json`.

## Start with the orchestrator

```bash
claude --agent worldwide-marketing-orchestrator
```

Give it your objective and let it route to the smallest useful set of division
leads and specialists. See the [kickoff prompts](../examples/kickoff-prompts.md).

## Review before granting access

Coordinator and auditor agents are generated with read-only tool sets; builder
specialists are generated with edit and write access. **Review each definition's
`tools` line** before granting access so you know exactly what an agent can do in
your environment. Client capabilities and permission behavior may differ from
other clients and may change between versions.

## Notes

- The project is not affiliated with or endorsed by Anthropic. The name is used
  only to identify this supported client. See the
  [disclaimer](../governance/index.md).
- This page avoids version-specific claims. Consult the client's own current
  documentation for exact behavior.
