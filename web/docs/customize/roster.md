# Edit the roster

`swarm/roster.json` is the single source of truth for the roster and reporting
hierarchy. Change agents there, then regenerate.

## What lives in the roster

Each agent record carries its `id`, `title`, `tier`, `division`, `reports_to`,
`kind`, `description`, `mission`, `responsibilities`, `deliverables`, `keywords`,
and `children`. The generators read these fields to produce the client adapters
and the generated documentation.

## Safe editing rules

- Keep `id` values stable. An `id` change is a breaking change and must be
  recorded in `CHANGELOG.md`.
- Keep parent and child references consistent — a child's `reports_to` must match
  the parent that lists it in `children`.
- Use neutral, capability-based terminology.
- Do not edit generated files to change an agent — edit the roster and
  regenerate.

## Then regenerate and validate

Follow the exact sequence on [Build and validate](build-and-validate.md). Both
generators prune stale files automatically, so removing an agent from the roster
cleanly removes its generated adapters and documentation on the next build.
