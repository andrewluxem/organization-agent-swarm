# Customize

You customize the swarm by editing one authoritative file — `swarm/roster.json` —
and regenerating everything else. Adapters and generated documentation are
outputs; they are never edited by hand.

- [Edit the roster](roster.md) — change roles, missions, responsibilities, and
  hierarchy safely.
- [Build and validate](build-and-validate.md) — the exact, ordered command
  sequence to regenerate and check for drift.

!!! warning "Generated directories are generator-owned"
    `canonical/agents/`, the four client adapter directories, and
    `web/docs/_generated/` are **generated**. Do not edit them by hand and do not
    add hand-authored files inside them. The generators own those directories and
    prune anything that no longer has a source.
