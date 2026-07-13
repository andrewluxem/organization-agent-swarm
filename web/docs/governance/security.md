# Security

This page summarizes the repository's `SECURITY.md`. Consult that file for the
authoritative policy.

## Reporting a vulnerability

Report suspected vulnerabilities **privately**. Once the public repository
exists, use **GitHub private vulnerability reporting** (the repository's private
security advisory workflow). Do **not** open a public issue, discussion, or pull
request for an undisclosed vulnerability, and do not publish reproduction details
before a coordinated fix.

A useful report includes reproduction steps, the affected files, the impact, and
a suggested mitigation.

## Supported versions

Only the **latest released major version** receives security fixes.

## Threat areas of interest

- **Prompt injection** — untrusted content that manipulates an agent.
- **Malicious agent instructions** — roster or adapter content crafted to cause
  harm.
- **Unsafe Bash or tool permissions** — configurations that grant more access
  than intended.
- **Secret leakage** — exposure of credentials, tokens, or personal data.
- **Generated-file supply-chain drift** — tampered generated files that no longer
  match the roster (`scripts/build_adapters.py --check` is the drift guard).
- **Destructive automation** — irreversible operations without human gating.
- **Unreviewed production actions** — releases without explicit human approval.

## Coordinated disclosure

The project follows a coordinated-disclosure model. Give maintainers a reasonable
opportunity to investigate and remediate before any public disclosure.
