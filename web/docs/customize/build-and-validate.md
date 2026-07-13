# Build and validate

Run this exact, ordered sequence after any roster change. It regenerates every
output, checks for drift, validates structure, and leaves a reviewable diff.

```bash
# 1. Edit the source of truth
#    (edit swarm/roster.json)

# 2. Regenerate the client adapters
python3 scripts/build_adapters.py

# 3. Confirm the adapters match the roster (no-write drift check)
python3 scripts/build_adapters.py --check

# 4. Regenerate the documentation partials
python3 scripts/build_docs.py

# 5. Confirm the documentation matches the roster (no-write drift check)
python3 scripts/build_docs.py --check

# 6. Validate the overall structure
python3 scripts/validate_swarm.py

# 7. Review the complete diff before committing
git diff
```

## Automatic stale-file cleanup

Both generators own their output directories:

- `scripts/build_adapters.py` owns `canonical/agents/` and the four client
  adapter directories.
- `scripts/build_docs.py` owns `web/docs/_generated/`.

When you remove or rename an agent in the roster, the generators delete the
now-orphaned generated files — but **only** inside their own directories and only
for files they produce. Unrelated files are never touched.

## Why generated directories must not contain hand-authored files

Drift checks compare every generated file byte-for-byte against what the roster
implies. A hand-authored file inside a generated directory is either reported as
stale and removed on the next build, or causes a `DRIFT` failure. Keep authored
content in non-generated locations so the drift guard stays trustworthy.

## Expected results

```text
CHECK OK: 100 generated files match swarm/roster.json.
CHECK OK: 4 generated documentation files match swarm/roster.json.
VALID
```
