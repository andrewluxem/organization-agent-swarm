# Workflows

Workflows show how the orchestrator, division leads, specialists, and the
independent reviewer combine on a real objective. Each one is grounded in a
matching file under `workflows/` in the repository.

Every workflow shares the same discipline:

- **Routing** — the orchestrator picks the smallest useful team, then delegates.
- **Bounded task packets** — each agent gets one objective, clear scope, owned
  files, allowed actions, acceptance criteria, and a stopping condition. See the
  [task packet reference](../reference/task-packet.md).
- **File ownership** — one accountable writer per file; parallel writers use
  separate branches or worktrees.
- **Independent analytics review** — Cross-Channel Measurement and Optimization
  reviews the evidence and must not edit the work it evaluates.
- **Stopping conditions** — agents stop and escalate when requirements conflict,
  evidence is missing, or a high-impact action would be required.
- **Human approval gates** — no release action happens without explicit human
  approval.

## Available workflows

- [Cross-functional launch](cross-functional-launch.md)
- [Lifecycle campaign](lifecycle-campaign.md)
- [Organic growth](organic-growth.md)
