# Swarm Operating Model

## Design principle

The chart is implemented as a hierarchy, but execution is intentionally hybrid:

1. The worldwide orchestrator owns the brief and final synthesis.
2. Division leads decompose work and enforce scope.
3. Specialists own bounded outputs.
4. Consumer Marketing Analytics challenges evidence and defines acceptance.
5. A human remains the release authority.

## Preferred path

```text
User
  -> Worldwide Orchestrator
      -> Division Lead(s)
          -> Specialist(s)
      -> Independent analytics review
  -> Human approval
```

## Flat fallback

When a client or session does not support reliable nested delegation:

1. The orchestrator asks each required lead for a workplan.
2. Leads return specialist task packets.
3. The orchestrator invokes specialists directly.
4. Completed work goes to an independent reviewer.

## Concurrency

Use parallel agents for independent discovery, audits, tests, and analysis.

For write work:

- assign one owner per file or directory;
- use a separate branch or worktree per concurrent writer;
- do not allow a reviewer to modify the work it evaluates;
- integrate only after each worker returns validation evidence.

A practical default is one orchestrator, up to three leads, and two to six active specialists—not all 20 agents.

## Task packet

Every delegated task defines:

- objective;
- in-scope and out-of-scope work;
- files or artifacts owned;
- allowed actions;
- evidence inputs;
- acceptance criteria;
- validation commands;
- stopping condition;
- required handoff recipient.

## Decision rights

| Decision | Owner |
|---|---|
| Task routing | Worldwide orchestrator |
| Division plan | Division lead |
| Specialist implementation | Assigned specialist |
| Measurement design | Consumer Marketing Analytics |
| Independent acceptance review | Cross-Channel Measurement and Optimization |
| Publish, deploy, send, spend, merge, push, or production change | Human |
