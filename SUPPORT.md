# Support

Organization Agent Swarm is a community-supported, open-source project. There
is **no guaranteed response time** and support is provided on a best-effort
basis by maintainers and other community members.

## Where to go

- **Reproducible defects** — open a **GitHub Issue** using the bug report
  template. Include reproduction steps, the affected client or adapter, the
  commands you ran, and expected versus observed behavior.
- **Design and usage questions** — use **GitHub Discussions** once it is
  enabled on the repository. Discussions are the right place for "how do I…",
  "is this the intended pattern…", and roadmap conversations.
- **Security vulnerabilities** — do **not** open a public issue. Follow
  [SECURITY.md](SECURITY.md) and use private vulnerability reporting.
- **Code of conduct concerns** — see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Supported scope

Community support covers:

- the roster structure and hierarchy in `swarm/roster.json`;
- the generated adapters in `canonical/agents/`, `.claude/agents/`,
  `.codex/agents/`, `.cursor/agents/`, and `.opencode/agents/`;
- the validation and generation scripts (`scripts/validate_swarm.py`,
  `scripts/build_adapters.py`, and `scripts/build_adapters.py --check`);
- installation using the documented user-scope installers;
- the documented operating model, handoff contract, and example workflows.

## Out of scope

The following are **not** supported here:

- defects in third-party clients (Claude Code, Codex, Cursor, OpenCode) or
  other external platforms and services;
- custom production deployments, private forks, or bespoke integrations;
- legal, privacy, compliance, or trademark review of your specific use;
- recovery from destructive commands or data loss caused by actions taken
  outside the documented, human-gated controls.

Before opening a request, please check existing issues and discussions, and
read [CONTRIBUTING.md](CONTRIBUTING.md) for the expected validation workflow.
