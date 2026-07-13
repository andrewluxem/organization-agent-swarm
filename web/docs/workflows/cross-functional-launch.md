# Cross-functional launch

Use this when an objective spans partnerships, paid and owned channels, and
measurement. It mirrors `workflows/cross-functional-launch.md` in the repository.

## Sequence

1. The **worldwide orchestrator** frames the outcome, constraints, and decision.
2. The **Affiliate Marketing lead** evaluates partnerships, publishers, creators,
   and onsite distribution.
3. The **Automated Advertising lead** designs channel, audience, creative, offer,
   and outbound execution.
4. The **Consumer Marketing Analytics lead** defines knowledge, segmentation,
   forecast, and measurement requirements.
5. **Specialists** work in bounded, non-overlapping task packets.
6. **Cross-Channel Measurement and Optimization** performs an independent
   acceptance review.
7. The **orchestrator** returns one recommendation.
8. A **human** approves or rejects any release action.

## Controls

- File ownership is assigned per specialist; parallel writers use isolated
  branches or worktrees.
- The independent reviewer does not edit the implementation.
- The workflow stops before any publish, deploy, send, spend, merge, push, or
  production change until a human approves. See
  [release gates](../governance/release-gates.md).
