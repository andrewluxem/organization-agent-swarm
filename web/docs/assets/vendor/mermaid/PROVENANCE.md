# Vendored runtime asset provenance

This directory contains a locally vendored, repository-controlled copy of the
Mermaid diagram runtime. It replaces a previous runtime request to an external content delivery
network. No content delivery network is contacted at runtime.

## mermaid.min.js

- **Package:** `mermaid`
- **Exact version:** `11.16.0`
- **Source:** npm registry tarball
  `https://registry.npmjs.org/mermaid/-/mermaid-11.16.0.tgz`
  (file extracted from `package/dist/mermaid.min.js`)
- **Upstream project:** https://github.com/mermaid-js/mermaid
- **Original license:** MIT (see `LICENSE` in this directory)
- **Date vendored:** 2026-07-11
- **SHA-256 (mermaid.min.js):**
  `74d7c46dabca328c2294733910a8aa1ed0c37451776e8d5295da38a2b758fb9b`
- **SHA-256 (source tarball mermaid-11.16.0.tgz):**
  `ff48c94a0a0458b377a5187ad01407184d2a182e6476c2015b7068ff58355fae`
- **SHA-256 (LICENSE):**
  `ec9fb67dcb25eccc416ed56e1aab819222c805a2a4bfe4cb19e7556bf2ffde80`

## mermaid-init.js

A small, framework-free loader authored for this repository. It runs only on
pages that contain a `pre.mermaid-source` element, injects the local
`mermaid.min.js` from a path relative to itself (never a content delivery
network), and renders the diagram. If JavaScript is disabled or fails, the diagram source remains visible
as readable fallback text.

- **Author:** Organization Agent Swarm maintainers
- **License:** Apache-2.0 (same as this repository)

## resize-observer polyfill

Not vendored. `ResizeObserver` is natively available in all current target
browsers (Chromium, Firefox, and Safari have shipped it since 2020), so a
polyfill is not genuinely required. The previous external resize-observer
polyfill request has been eliminated.

## Verifying integrity

```bash
sha256sum web/docs/assets/vendor/mermaid/mermaid.min.js
# expect: 74d7c46dabca328c2294733910a8aa1ed0c37451776e8d5295da38a2b758fb9b
```
