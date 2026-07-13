# Handoff contract

Every delegated task returns the same structured handoff, defined in the
repository's `team/handoff-contract.md`. A consistent contract makes evidence,
changes, risks, and open decisions easy to audit.

```text
STATUS: complete | blocked | needs-decision
ROLE:
OBJECTIVE:
SUMMARY:
EVIDENCE:
- file, command, data source, or direct observation
CHANGES:
- files or artifacts changed; use "none" for analysis-only work
VALIDATION:
- command/check and observed result
RISKS:
- severity, likelihood, impact, and mitigation
DECISIONS NEEDED:
- explicit human decisions, or "none"
NEXT HANDOFF:
- agent name and bounded next task
```

## What makes a handoff invalid

A handoff is incomplete when it claims validation without evidence, changes files
outside scope, hides blockers, weakens acceptance criteria, treats attribution as
causality, or omits material risk.
