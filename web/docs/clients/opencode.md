# OpenCode

OpenCode reads project agents from `.opencode/agents/`. Each agent is a Markdown
file with YAML frontmatter that declares its `description`, `mode`, and
`permission` policy. The default primary agent is set in `opencode.json`. These
files are generated from `swarm/roster.json`.

## Start with the orchestrator

```bash
opencode
```

`opencode.json` selects `worldwide-marketing-orchestrator` as the default primary
agent. Specialists can also be invoked with `@agent-name`. See the
[kickoff prompts](../examples/kickoff-prompts.md).

## Review before granting access

Builder specialists are generated with `edit: ask`; coordinators and the auditor
are generated with `edit: deny`. Bash permission defaults to `ask`, with a small
allowlist of read-only commands. **Review each agent's `permission` block** before
granting access. Client capabilities and permission behavior may differ from
other clients and may change over time.

## Notes

- The project is not affiliated with or endorsed by the OpenCode project. The
  name is used only to identify this supported client. See the
  [disclaimer](../governance/index.md).
- This page avoids version-specific claims. Consult the client's own current
  documentation for exact behavior.
