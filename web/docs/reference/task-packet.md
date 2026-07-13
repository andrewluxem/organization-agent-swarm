# Task packet reference

A **task packet** is the bounded unit of delegation. Every delegated task defines
these fields, mirroring `team/task-template.md` in the repository.

```text
# Agent Task Packet

## Objective
[One outcome, stated as a verifiable result.]

## Owner
[Exact agent ID.]

## Context
[Why this matters and where the evidence lives.]

## In scope
-

## Out of scope
-

## File or artifact ownership
-

## Constraints
- No publish/deploy/send/spend/merge/push/production-data changes without human approval.
- Do not edit outside the assigned ownership boundary.
- Do not weaken existing validation.

## Acceptance criteria
-

## Validation
# exact commands

## Required handoff
Return the handoff contract to [parent-agent-id].
```

The completed work is returned using the
[handoff contract](../governance/handoff-contract.md).
