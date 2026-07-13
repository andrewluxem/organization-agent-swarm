# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

_No changes yet._

## [2.0.0] - 2026-07-11

### Changed

- Orchestrator display title changed to **Worldwide Marketing Orchestrator**.
- Public-facing terminology neutralized to use generic, capability-oriented
  language throughout the roster, adapters, and documentation.

### Breaking

- Renamed agent id `amazon-assistant` -> `assistant-discovery`.
- Renamed agent id `amazon-smile` -> `cause-marketing`.
- Renamed agent id `associates` -> `publisher-programs`.

  Downstream references, routing rules, and saved prompts that used the old
  agent ids must be updated to the new ids.

### Fixed

- The adapter generator now reproduces the authoritative, rich agent
  definitions instead of a reduced form.
- `scripts/build_adapters.py --check` now detects missing, drifted, and stale
  generated files.
- Stale generated agent definitions are safely removed within the
  generator-owned directories when their ids no longer exist in the roster.

[Unreleased]: https://github.com/andrewluxem/organization-agent-swarm/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/andrewluxem/organization-agent-swarm/releases/tag/v2.0.0
