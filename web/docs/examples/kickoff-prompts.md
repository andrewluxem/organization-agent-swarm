# Kickoff prompts

Copy a prompt, replace the bracketed text, and paste it into your client. These
mirror `examples/prompts.md` in the repository.

## Universal kickoff

```text
Act as the Worldwide Marketing Orchestrator.
Read AGENTS.md, team/operating-model.md, and swarm/roster.json.

Task:
[PASTE THE OBJECTIVE]

First work in Discover and Plan modes only.
Choose the smallest useful set of leads and specialists.
Return:
1. the routing decision;
2. one bounded task packet per agent;
3. file ownership and concurrency plan;
4. acceptance criteria and validation;
5. decisions that require my approval.

Do not edit, publish, deploy, send, spend, merge, push, or change production data yet.
```

## Execute an approved plan

```text
Execute the approved plan using the Organization Agent Swarm.
Use the existing task packets and acceptance criteria.
Keep one writer per file, use isolated branches or worktrees for parallel writes,
wait for all assigned agents, then send the result to
cross-channel-measurement-optimization for independent review.
Do not release anything without my explicit approval.
```

## Independent review

```text
Use cross-channel-measurement-optimization as an independent reviewer.
It must not edit the implementation.
Determine whether the evidence supports launch, continue, modify, or stop.
```
