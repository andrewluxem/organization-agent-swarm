# Documentation site (`/web`)

This directory holds the public documentation site for **Organization Agent
Swarm**, built with [MkDocs](https://www.mkdocs.org/) and the
[Material](https://squidfunk.github.io/mkdocs-material/) theme. The reusable agent
package stays at the repository root; this site only documents it.

The roster detail pages are generated from `swarm/roster.json` by
`scripts/build_docs.py` into `web/docs/_generated/`. Those files are
generator-owned — do not edit them by hand.

## Local setup

Run these from the **repository root**. Use a local virtual environment so the
documentation tools stay isolated from your system Python.

```bash
python3 -m venv .venv-docs
source .venv-docs/bin/activate
python -m pip install --upgrade pip
python -m pip install -r web/requirements-docs.txt
python scripts/build_docs.py
mkdocs serve -f web/mkdocs.yml
```

On **Windows PowerShell**, activate the virtual environment with:

```powershell
.venv-docs\Scripts\Activate.ps1
```

## Build a static site

```bash
mkdocs build --strict -f web/mkdocs.yml
```

The strict build fails on broken navigation or links, which keeps the site
trustworthy.

## Quality checks (local)

These mirror the validation-only CI in `.github/workflows/validate.yml`. Run them
from the **repository root**. Node.js is pinned in `web/.node-version` (Node 22);
`npm ci` installs the exact pinned dev dependencies from `web/package-lock.json`.

```bash
# 1. Regenerate and validate the package + docs
python3 scripts/build_adapters.py --check
python3 scripts/build_docs.py --check
python3 scripts/validate_swarm.py
mkdocs build --strict -f web/mkdocs.yml
python3 scripts/check_public_content.py   # private paths, secrets, trackers, links
git diff --check

# 2. Accessibility (Pa11y CI, WCAG 2.1 AA) and performance (Lighthouse CI)
npm ci --prefix web
python3 -m http.server 8000 --directory web/site &   # serve the built site
npm --prefix web run test:a11y
npm --prefix web run test:lighthouse
# stop the server when done: kill %1

# 3. Link checking (requires the lychee binary) and secret scanning (gitleaks)
lychee --offline --include-fragments --config web/lychee.toml web/docs
gitleaks dir . --redact
```

Generated reports (`web/.lighthouseci/`), `web/node_modules/`, and any local
static server are local artifacts. They must not be committed. The vendored
Mermaid runtime under `web/docs/assets/vendor/mermaid/` and its provenance are
committed; the diagram loads only from those local paths (no CDN).

## Local artifacts — do not commit

- `.venv-docs/` — the local virtual environment.
- `web/site/` — the built static output (`site_dir`).

Both are ignored by `.gitignore` and must not be committed. This site foundation
contains **no** deployment configuration, CI, custom domain, analytics, or
production URL; those belong to later phases.
