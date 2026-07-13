# Organization Agent Swarm — Repository Instructions

## Purpose

This repository uses a 20-agent hierarchy modeled as a worldwide marketing & advertising organization:

- Worldwide orchestrator
- Affiliate Marketing division
- Automated Advertising division
- Consumer Marketing Analytics division

The swarm may work on strategy, research, code, content, data, analytics, testing, documentation, and operating mechanisms. Autonomy is not permission to take irreversible action.

## Source of truth

1. `swarm/roster.json` defines the roster and reporting structure.
2. `canonical/agents/` contains platform-neutral role prompts.
3. `.claude/agents/`, `.codex/agents/`, `.cursor/agents/`, and `.opencode/agents/` are generated adapters.
4. `team/operating-model.md` defines coordination.
5. `team/handoff-contract.md` defines required outputs.

`canonical/agents/` and the four client adapter directories are generator-owned. Do not edit generated files by hand; edit `swarm/roster.json` and regenerate. Stale generated agent files are removed automatically when their ids no longer exist in the roster, scoped strictly to the generated directories and their file extensions.

After changing the roster, run:

```bash
python scripts/build_adapters.py
python scripts/build_adapters.py --check
python scripts/validate_swarm.py
```

`build_adapters.py --check` is a no-write drift guard: it fails if any generated file is missing, drifted, or stale. Contributors must confirm a clean tree before opening a pull request — `build_adapters.py --check` must report `CHECK OK` and `validate_swarm.py` must report `VALID`. See `CONTRIBUTING.md`.

The public documentation site lives in `/web` (MkDocs + Material). Its roster pages are generated from `swarm/roster.json` by `scripts/build_docs.py` into `web/docs/_generated/`, which is generator-owned. Run `python scripts/build_docs.py` to regenerate and `python scripts/build_docs.py --check` to detect missing, drifted, or stale documentation. Do not edit `web/docs/_generated/` by hand or place hand-authored files there.

`scripts/check_public_content.py` scans tracked source and the built site for private paths, secrets, tracking code, external runtime assets, retired agent ids, custom-domain/Pages configuration, and broken local links. A validation-only CI workflow (`.github/workflows/validate.yml`) runs these checks plus accessibility, performance, link, and secret scans with read-only permissions and no deployment step.

## Routing rules

- Start with `worldwide-marketing-orchestrator` for cross-functional or ambiguous work.
- Use a division lead when the request is clearly contained within one pillar.
- Use a specialist directly only when the task is already bounded and ownership is obvious.
- Prefer the smallest useful team. Do not activate all 20 agents by default.
- Use Consumer Marketing Analytics for evidence, customer-state logic, forecasts, and measurement.
- Use `cross-channel-measurement-optimization` as an independent reviewer, not as the author of the work it evaluates.

## Execution modes

### Discover
Read-only exploration. Return facts, file references, assumptions, risks, and a recommended route.

### Plan
Create a bounded plan, acceptance criteria, file ownership, dependencies, and validation. No production changes.

### Build
Make approved changes. One accountable writer owns each file. Parallel write tasks require separate branches or worktrees.

### Review
Use an agent that did not author the change. Review correctness, privacy, accessibility, security, economics, measurement, and missing tests.

### Release
Require explicit human approval before publishing, deploying, sending communications, spending money, merging, pushing, changing production configuration, or changing production data.

## Non-negotiable controls

- Inspect before editing.
- Keep unrelated files untouched.
- Never fabricate tests, metrics, research, citations, or customer evidence.
- Never reveal or commit secrets or customer-level personal data.
- Avoid destructive Git operations unless explicitly authorized.
- Do not bypass failing checks, weaken validators, or delete evidence to make work appear complete.
- Do not let two agents edit the same files concurrently.
- State uncertainty and missing evidence.
- Separate platform-reported attribution from causal or incremental measurement.
- Escalate legal, privacy, accessibility, brand, financial, and reputational risks.

## Required handoff

Every delegated task must return the structure in `team/handoff-contract.md`.
