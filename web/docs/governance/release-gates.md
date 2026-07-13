# Release gates

A **release gate** is an action an agent may prepare but must never take on its
own. Each gate requires explicit human approval. This is the core safety property
of the swarm: automation proposes, a human releases.

## Gated actions

- Publishing content or sites.
- Deploying software or configuration.
- Sending communications to real recipients (email, push, SMS, in-app).
- Spending money or committing budget.
- Merging into a protected branch.
- Pushing to a remote.
- Changing production configuration or production data.

## How gates are enforced

- Coordinator and auditor agents are generated without edit or write tools.
- Builder specialists may edit only the bounded slice assigned to them and must
  not take any gated action without approval.
- The independent reviewer issues a launch, continue, modify, or stop
  recommendation, but the human makes the release decision.

If a task would require a gated action to proceed, the agent stops and escalates
rather than acting. See the [decision rights](../organization/decision-rights.md)
table for who owns each decision.
