# Contributing

Thank you for your interest in improving **Organization Agent Swarm**. This
guide explains the repository architecture, the rules that keep generated files
trustworthy, and the workflow every change must follow.

By participating, you agree to abide by our
[Code of Conduct](CODE_OF_CONDUCT.md).

## Repository architecture

```text
AGENTS.md                 Repository-wide source of truth for agents
CLAUDE.md                 Claude Code entry instructions
swarm/roster.json         Authoritative roster and reporting hierarchy
canonical/agents/         Generated platform-neutral role prompts
.claude/agents/           Generated Claude Code adapters
.codex/agents/            Generated OpenAI Codex adapters
.cursor/agents/           Generated Cursor adapters
.opencode/agents/         Generated OpenCode adapters
scripts/build_adapters.py Generator + drift checker (--check)
scripts/validate_swarm.py Structural validator
team/                     Operating model, handoff contract, decision log
workflows/                Example multi-agent workflows
examples/                 Kickoff prompts
```

## Source of truth and generated outputs

- **`swarm/roster.json` is the single authoritative source** for the roster,
  agent metadata, and the reporting hierarchy. Nearly every substantive change
  starts here.
- **`canonical/agents/` and the four client adapter directories**
  (`.claude/agents/`, `.codex/agents/`, `.cursor/agents/`, `.opencode/agents/`)
  are **generated outputs**. They are produced from `swarm/roster.json`.
- **`web/docs/_generated/`** holds the documentation roster pages, generated
  from `swarm/roster.json` by `scripts/build_docs.py`. It is generator-owned
  in the same way as the adapter directories.

### Generated directories are generator-owned

- **Never edit generated files by hand.** Any manual edit will be reported as
  drift and overwritten on the next generation.
- To change agent content, edit `swarm/roster.json` (or the generator
  templates in `scripts/build_adapters.py`), then regenerate.
- **Stale generated agent files are removed automatically** when their ids no
  longer exist in the roster. Removal is scoped strictly to the generator-owned
  directories and their file extensions.
- **Never place non-generated files inside the generated agent directories.**
  The generator treats those directories as exclusively its own; unrelated
  files placed there are at risk and violate the ownership model.

### Regeneration and validation commands

```bash
# Regenerate every adapter from swarm/roster.json (also prunes stale files)
python scripts/build_adapters.py

# Regenerate the documentation roster pages under web/docs/_generated/
python scripts/build_docs.py

# Fail if any generated adapter or doc is missing, drifted, or stale (no writes)
python scripts/build_adapters.py --check
python scripts/build_docs.py --check

# Structural validation of the roster and generated adapter set
python scripts/validate_swarm.py
```

Run `build_adapters.py` and `build_docs.py` after any roster change, then confirm
a clean tree with both `--check` commands and `validate_swarm.py`.

## Terminology

Use **neutral, capability-based terminology**. Describe roles by their generic
marketing, advertising, partnership, and analytics function. Do not introduce
employer-specific names, internal project code names, or third-party product
names except where a name is genuinely required for identification or
interoperability documentation (see [DISCLAIMER.md](DISCLAIMER.md)).

## Collaboration model

- **One accountable writer per file.** Each changed file must have a single
  owner responsible for it in a given change.
- **Use separate branches or worktrees for concurrent writers.** Parallel work
  must not edit the same files. Never let two contributors edit the same file
  concurrently on the same branch.
- **Material changes require independent review** — a reviewer who did not
  author the change should assess correctness, privacy, accessibility,
  security, economics, and measurement implications before merge.

## What must never be committed

- Secrets, credentials, API keys, or tokens.
- Customer-level or otherwise personal data (PII).
- Employer-confidential or otherwise proprietary information, internal
  organization charts, or non-public source material.
- Fabricated tests, metrics, research, citations, or customer evidence.

## Human-gated actions

No agent, script, or contribution may **publish, deploy, send communications,
spend money, merge, push, or change production configuration or data** without
explicit human authorization. Automation proposes; humans approve
irreversible or externally visible actions.

## Pull request workflow

1. Branch from the current integration branch; keep unrelated files untouched.
2. Make your change (edit `swarm/roster.json` and/or templates for agent
   changes).
3. Regenerate and validate:

   ```bash
   python scripts/build_adapters.py
   python scripts/build_adapters.py --check
   python scripts/build_docs.py
   python scripts/build_docs.py --check
   python scripts/validate_swarm.py
   python scripts/check_public_content.py
   git diff --check
   ```

4. Confirm the working tree is clean and that generated files were **not**
   hand-edited.
5. Fill out the pull request template, including the validation commands you
   ran, the affected client or adapter, breaking-change disclosure, and the
   confirmations about generated files, secrets, PII, and proprietary material.

A pull request should not be merged until `build_adapters.py --check` reports
`CHECK OK` and `validate_swarm.py` reports `VALID`.

## Documentation quality gates

Changes under `/web` are additionally validated by the CI workflow
(`.github/workflows/validate.yml`): accessibility (Pa11y CI, WCAG 2.1 AA, zero
errors), performance (Lighthouse CI), link checking (Lychee), the public-content
scan, and secret scanning (gitleaks). Node.js is pinned in `web/.node-version`;
install Node dependencies with `npm ci --prefix web`. Do not commit
`web/node_modules/`, `web/.lighthouseci/`, or any generated report. See
`web/README.md` for the exact local commands.
