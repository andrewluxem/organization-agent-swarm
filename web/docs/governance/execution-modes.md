# Execution modes

Work moves through explicit modes, defined in the repository's `AGENTS.md`. The
mode sets what an agent is allowed to do.

## Discover

Read-only exploration. Return facts, file references, assumptions, risks, and a
recommended route. No changes.

## Plan

Create a bounded plan with acceptance criteria, file ownership, dependencies, and
validation. No production changes.

## Build

Make approved changes. **One accountable writer owns each file.** Parallel write
tasks require separate branches or worktrees and non-overlapping file ownership.

## Review

Use an agent that did **not** author the change. Review correctness, privacy,
accessibility, security, economics, measurement, and missing tests. The reviewer
does not edit the work it evaluates.

## Release

Require explicit human approval before publishing, deploying, sending
communications, spending money, merging, pushing, changing production
configuration, or changing production data. See [release gates](release-gates.md).
