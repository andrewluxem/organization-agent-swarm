# Organization Agent Swarm

**Organization Agent Swarm** is a portable team of AI coding-agent definitions,
modeled as a worldwide marketing and advertising organization. It gives you a
ready-made hierarchy of specialized agents you can run inside several coding-agent
clients from a single, shared source of truth.

Its structure is a **capability-oriented model** built from common patterns for
organizing marketing, advertising, partnership, and analytics work. It is an
independent, generic design and is **not** derived from any current or former
employer's internal organization chart, roster, or proprietary material. See the
[project disclaimer](governance/index.md).

## What you get

- **20 agents** defined once in `swarm/roster.json` and generated into
  client-specific adapters.
- **1 orchestrator** — the Worldwide Marketing Orchestrator — that frames the
  work, routes it, and returns a single accountable recommendation.
- **3 capability divisions** — Affiliate Marketing, Automated Advertising, and
  Consumer Marketing Analytics — each led by a division lead.
- **16 specialists** that own bounded outputs within their division.
- **4 supported coding-agent clients** — Claude Code, Codex, Cursor, and
  OpenCode — each with generated project-scoped adapters.

## Why a hierarchy

A single general-purpose agent tends to do too much at once. This project splits
work along familiar capability lines so that:

- routing is explicit — the orchestrator picks the smallest useful team;
- scope is bounded — each specialist owns one clear deliverable;
- evidence stays honest — an independent analytics reviewer challenges claims
  before anything is accepted;
- ownership is clear — one accountable writer per file, with branch or worktree
  isolation for parallel work.

## The human approval model

The swarm is designed to **propose**, not to release. No agent may publish,
deploy, send communications, spend money, merge, push, or change production
configuration or data without explicit human approval. Automation does the
analysis and drafting; a human remains the release authority. See
[release gates](governance/release-gates.md).

## Who this is for

- Practitioners who want a structured, multi-agent workflow for marketing,
  growth, content, data, and analytics tasks.
- Teams standardizing agent roles across more than one coding-agent client.
- Anyone who wants a small, auditable, regenerated agent package rather than a
  sprawl of hand-maintained prompts.

!!! note "No adoption or performance claims"
    This documentation describes how the project works. It makes no claims about
    customer adoption, usage counts, or performance improvements.

## Next steps

- [Install the swarm](install/index.md)
- [Explore the roster](roster/index.md)
- [Run a workflow](workflows/index.md)
- [Customize the roster](customize/index.md)
- [Read the governance model](governance/index.md)
