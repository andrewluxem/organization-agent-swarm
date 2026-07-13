# Security Policy

## Supported versions

Only the **latest released major version** of Organization Agent Swarm is
supported with security fixes. Older versions receive no guaranteed security
maintenance.

| Version | Supported          |
|---------|--------------------|
| Latest released major version | :white_check_mark: |
| Any earlier version           | :x:                |

## Reporting a vulnerability

Please report suspected vulnerabilities **privately**. Once the public
repository exists, use **GitHub private vulnerability reporting** (the
repository's *Security → Report a vulnerability* / private security advisory
workflow).

- **Do not** open a public issue, discussion, or pull request for an
  undisclosed vulnerability.
- **Do not** publish reproduction details publicly before a fix or coordinated
  disclosure timeline has been agreed.

Because this project is not yet a publicly maintained repository, there is
**no guaranteed response SLA** at this time. Reports will be reviewed on a
best-effort basis, and a formal disclosure process will be established when the
repository is published.

### What to include

A useful report includes:

- **Reproduction steps** — the minimal sequence to trigger the issue.
- **Affected files** — the roster, adapter, script, workflow, or template
  involved.
- **Impact** — what an attacker or a careless run could achieve.
- **Suggested mitigation** — a proposed fix or containment, if you have one.

## Threat areas of interest

This project generates and coordinates AI agent definitions, so the most
relevant threat areas include:

- **Prompt injection** — untrusted content that manipulates an agent into
  ignoring its boundaries.
- **Malicious agent instructions** — roster or adapter content crafted to make
  an agent take harmful action.
- **Unsafe Bash or tool permissions** — agent configurations that grant
  broader execution or file access than intended.
- **Secret leakage** — exposure of credentials, tokens, customer-level personal
  data, or other confidential material through agent output or committed files.
- **Generated-file supply-chain drift** — hand-edited or tampered generated
  agent files that no longer match `swarm/roster.json`
  (`scripts/build_adapters.py --check` is the drift guard).
- **Destructive automation** — agents performing irreversible operations
  (deletion, force-push, production writes) without human gating.
- **Unreviewed production actions** — publishing, deploying, sending, spending,
  merging, or changing production data without explicit human approval.

## Automated checks

A validation-only CI workflow (`.github/workflows/validate.yml`) runs on pull
requests and pushes to `main` with read-only permissions and no deployment
step. It includes secret scanning (gitleaks), a public-content scan
(`scripts/check_public_content.py`), accessibility and performance audits, and
link checking. Third-party GitHub Actions are pinned to full commit SHAs, and
vendored runtime assets are checksummed and recorded in provenance files.

## Coordinated disclosure

We follow a coordinated-disclosure model. Please give maintainers a reasonable
opportunity to investigate and remediate before any public disclosure. We will
work with you to confirm the issue, prepare a fix, and agree on a disclosure
timeline that credits reporters who wish to be acknowledged.
