## Summary

<!-- What does this change and why? Link any related issue. -->

## Affected client or adapter

<!-- Check all that apply. -->

- [ ] Claude Code (`.claude/agents`)
- [ ] Codex (`.codex/agents`)
- [ ] Cursor (`.cursor/agents`)
- [ ] OpenCode (`.opencode/agents`)
- [ ] Canonical prompts (`canonical/agents`)
- [ ] Roster (`swarm/roster.json`)
- [ ] Scripts (`build_adapters.py` / `validate_swarm.py`)
- [ ] Documentation / governance

## Expected vs. observed behavior

<!-- For a fix: what was observed before, and what is expected after. -->

- **Before (observed):**
- **After (expected):**

## Reproduction / verification steps

<!-- For a bug fix, the steps that reproduced the issue and now confirm the fix. -->

## Validation commands run

<!-- Paste the actual output. -->

```shell
$ python scripts/build_adapters.py --check
$ python scripts/validate_swarm.py
$ git diff --check
```

## Breaking-change disclosure

<!-- Does this change any agent id, title, or the reporting hierarchy?
     If yes, describe the impact and confirm CHANGELOG.md is updated. -->

- [ ] No breaking change
- [ ] Breaking change (agent id / title / hierarchy) — documented in `CHANGELOG.md`

## Checklist

- [ ] `python scripts/build_adapters.py --check` reports **CHECK OK**
- [ ] `python scripts/validate_swarm.py` reports **VALID**
- [ ] `git diff --check` is clean (no whitespace errors)
- [ ] I did **not** manually edit any generated agent files (they are generator-owned)
- [ ] I placed no non-generated files inside generated agent directories
- [ ] This PR contains **no** secrets, credentials, PII, or proprietary material
- [ ] Terminology stays neutral and capability-based
- [ ] User-visible changes are recorded in `CHANGELOG.md`
