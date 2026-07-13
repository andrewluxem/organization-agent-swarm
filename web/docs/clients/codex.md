# Codex

Codex reads custom agents from `.codex/agents/`. Each agent is a TOML file with a
`name`, `description`, `sandbox_mode`, and `developer_instructions`. Repository
depth is configured in `.codex/config.toml`. These files are generated from
`swarm/roster.json`.

## Start with the orchestrator

```bash
codex
```

Then ask Codex to use `worldwide-marketing-orchestrator` and delegate through the
configured custom agents. See the [kickoff prompts](../examples/kickoff-prompts.md).

## Review before granting access

Builder specialists are generated with a `workspace-write` sandbox; coordinators
and the auditor are generated `read-only`. **Review each agent's `sandbox_mode`
and instructions** before granting access. Client capabilities and permission
behavior may differ from other clients and may change over time.

## Notes

- The project is not affiliated with or endorsed by OpenAI. The name is used only
  to identify this supported client. See the
  [disclaimer](../governance/index.md).
- This page avoids version-specific claims. Consult the client's own current
  documentation for exact behavior.
