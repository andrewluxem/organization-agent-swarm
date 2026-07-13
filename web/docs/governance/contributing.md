# Contributing

This page summarizes the repository's `CONTRIBUTING.md`. Consult that file for the
authoritative workflow.

## Source of truth and generated outputs

- `swarm/roster.json` is the single authoritative source for the roster and
  hierarchy.
- `canonical/agents/` and the four client adapter directories, plus
  `web/docs/_generated/`, are **generated outputs**.

## Generated directories are generator-owned

- Never edit generated files by hand.
- Never place hand-authored files inside a generated directory.
- Stale generated files are removed automatically when their source no longer
  exists in the roster, scoped strictly to the generator-owned directories.

## Collaboration rules

- **One accountable writer per file.**
- **Separate branches or worktrees** for concurrent writers.
- **Independent review** for material changes — the reviewer does not author the
  work it evaluates.

## Never commit

Secrets, credentials, tokens, customer-level or personal data, employer-
confidential or proprietary material, or fabricated tests, metrics, research, or
evidence.

## Human-gated actions

No contribution or agent may publish, deploy, send, spend, merge, push, or change
production configuration or data without explicit human approval.

## Expected validation

Before opening a pull request, run and confirm:

```bash
python3 scripts/build_adapters.py --check
python3 scripts/build_docs.py --check
python3 scripts/validate_swarm.py
git diff --check
```

See [Build and validate](../customize/build-and-validate.md) for the full,
ordered customization sequence.
