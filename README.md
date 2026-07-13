# Organization Agent Swarm

A portable 20-agent team modeled as a worldwide marketing & advertising
organization.

Its structure is based on **common, capability-oriented patterns** for
organizing marketing, advertising, partnership, and analytics work. It is an
independent, generic design and is not derived from any employer's internal
organization chart, roster, or proprietary material. See
[DISCLAIMER.md](DISCLAIMER.md).

Included:

- Claude Code project agents
- OpenAI Codex custom agents
- Cursor project subagents
- OpenCode project agents
- shared roster and hierarchy
- operating model and governance
- task and handoff templates
- example workflows and prompts
- adapter generator and validator
- Bash and PowerShell user-scope installers

Third-party client names (Claude Code, Codex, Cursor, OpenCode) and any other
product or platform names identify the **supported integrations only**. They
are used for identification and interoperability and do not imply affiliation,
sponsorship, or endorsement.

## Structure

```text
AGENTS.md
CLAUDE.md
swarm/roster.json
canonical/agents/
.claude/agents/
.codex/agents/
.cursor/agents/
.opencode/agents/
team/
workflows/
examples/prompts.md
scripts/build_adapters.py
scripts/validate_swarm.py
```

`swarm/roster.json` is the authoritative source. The `canonical/agents/`
directory and the four client adapter directories are **generated outputs** and
**should not be edited manually** — edit the roster and regenerate instead.

## Quick start

Copy the package into a Git repository and run:

```bash
python scripts/validate_swarm.py
```

### Claude Code

```bash
claude --agent worldwide-marketing-orchestrator
```

### Codex

```bash
codex
```

Then ask Codex to use `worldwide-marketing-orchestrator` and delegate through
the configured custom agents.

### Cursor

Open the repository in Cursor, start Agent, and paste the Universal kickoff
prompt from `examples/prompts.md`.

### OpenCode

```bash
opencode
```

`opencode.json` selects `worldwide-marketing-orchestrator` as the default
primary agent. Specialists can also be invoked with `@agent-name`.

## Recommended usage

Do not run all 20 agents on every task. A normal cross-functional run uses one
orchestrator, one to three leads, two to six specialists, and one independent
measurement reviewer.

Use parallelism for discovery, audits, tests, and analysis. Parallel write
tasks require separate branches or worktrees and non-overlapping file ownership.

## Customize

Edit `swarm/roster.json`, then regenerate and validate:

```bash
python scripts/build_adapters.py
python scripts/build_adapters.py --check
python scripts/build_docs.py
python scripts/build_docs.py --check
python scripts/validate_swarm.py
```

`build_adapters.py --check` performs a no-write drift check: it fails if any
generated file is missing, drifted, or stale. Stale generated agent files are
pruned automatically by `build_adapters.py` when their ids leave the roster.

## Documentation site

A public documentation site lives in [`/web`](web/README.md), built with MkDocs and the Material theme. Its roster pages are generated from `swarm/roster.json` by `scripts/build_docs.py` into `web/docs/_generated/`, which is generator-owned. Use `python scripts/build_docs.py` to regenerate and `python scripts/build_docs.py --check` to detect drift. Do not edit the generated documentation by hand. See `web/README.md` for local build instructions.

A validation-only CI workflow (`.github/workflows/validate.yml`, read-only permissions, no deployment) runs generator drift checks, a strict MkDocs build, a public-content scan (`scripts/check_public_content.py`), accessibility (Pa11y CI, WCAG 2.1 AA), performance (Lighthouse CI), link checking (Lychee), and secret scanning (gitleaks). Publishing remains a separate, human-gated step.

## Global installation

Project-scoped installation is safer. For user scope:

```bash
bash scripts/install-user-scope.sh
```

PowerShell:

```powershell
./scripts/install-user-scope.ps1
```

## Role interpretation

The specialist roles are portable and usable in any organization:

- Assistant Discovery -> assistant-led and agentic discovery
- Cause Marketing -> purpose-led and cause marketing
- Publisher Programs -> affiliate and publisher programs

## Project documents

- [LICENSE](LICENSE) — Apache License 2.0
- [NOTICE](NOTICE) — attribution notice
- [DISCLAIMER.md](DISCLAIMER.md) — independence and trademark disclaimer
- [CHANGELOG.md](CHANGELOG.md) — release history
- [CONTRIBUTING.md](CONTRIBUTING.md) — architecture and contribution workflow
- [SECURITY.md](SECURITY.md) — vulnerability reporting
- [SUPPORT.md](SUPPORT.md) — how to get help
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Contributor Covenant 2.1

## Official documentation consulted

- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- OpenAI Codex subagents: https://developers.openai.com/codex/subagents
- OpenAI Codex AGENTS.md: https://developers.openai.com/codex/guides/agents-md
- Cursor subagents: https://cursor.com/docs/subagents
- Cursor rules: https://cursor.com/docs/rules
- OpenCode agents: https://opencode.ai/docs/agents/
