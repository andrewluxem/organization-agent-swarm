#!/usr/bin/env python3
"""Deterministic public-content checker for Organization Agent Swarm.

Inspects tracked public source files and, when present, the built ``web/site``
output for content that must not ship publicly. Uses only the Python standard
library. Exits non-zero when any violation is found.

Design notes:
- Narrow, documented allowlists are used so meaningful violations are not
  hidden behind blanket exclusions.
- Historical migration records (CHANGELOG.md) are distinguished from active
  terminology.
- The "Consumer Marketing Analytics" role vocabulary is NOT treated as
  analytics tracking; only real tracking signatures are flagged.
- External *runtime asset* references are detected by parsing built HTML for
  asset-loading elements, not by grepping third-party minified bundles.
"""
from __future__ import annotations

import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "web" / "site"
SELF_REL = "scripts/check_public_content.py"

# --- Narrow, documented allowlists ------------------------------------------

# The scanner itself names forbidden strings; it is never a violation source.
ALLOW_SELF = {SELF_REL}

# Third-party, checksummed, provenance-documented vendored assets. These are
# upstream minified files (see web/docs/assets/vendor/mermaid/PROVENANCE.md),
# not authored content, so free-text term scans skip them.
VENDOR_PREFIXES = ("web/docs/assets/vendor/",)

# Retired agent ids may appear ONLY as migration records here.
CHANGELOG_REL = "CHANGELOG.md"

# Files where a localhost / loopback reference is a documented local-development
# or CI-local-server example (not a leaked production reference).
LOCALHOST_ALLOW = {
    SELF_REL,
    "web/README.md",
    "README.md",
    "CONTRIBUTING.md",
    "AGENTS.md",
    "web/.lighthouserc.cjs",
    "web/.pa11yci.cjs",
    "web/lychee.toml",
    ".github/workflows/validate.yml",
}

TEXT_SUFFIXES = {
    ".md", ".markdown", ".txt", ".py", ".toml", ".yml", ".yaml", ".json",
    ".cjs", ".js", ".mjs", ".css", ".html", ".cfg", ".ini",
}

# --- Violation collection ----------------------------------------------------


class Violations:
    def __init__(self) -> None:
        self.items: list[tuple[str, str, int, str]] = []

    def add(self, category: str, path: str, line: int, message: str) -> None:
        self.items.append((category, path, line, message))

    def __bool__(self) -> bool:
        return bool(self.items)


def tracked_files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    return sorted(p for p in out.splitlines() if p)


def is_vendored(rel: str) -> bool:
    return any(rel.startswith(prefix) for prefix in VENDOR_PREFIXES)


def read_lines(rel: str) -> list[str]:
    try:
        return (ROOT / rel).read_text(encoding="utf-8").splitlines()
    except (UnicodeDecodeError, FileNotFoundError):
        return []


# --- Individual checks -------------------------------------------------------

SECRET_PATTERNS = [
    ("AWS access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("generic assigned secret", re.compile(
        r"(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token)\b\s*[:=]\s*[\"'][^\"'\s]{8,}[\"']")),
]

PRIVATE_PATHS = ["/Users/", "C:\\Users\\"]
LOOPBACK = re.compile(r"\b(?:localhost|127\.0\.0\.1|0\.0\.0\.0|::1)\b")
DERIVATION_ZERO = ["Worldwide Automated Marketing"]
DERIVATION_NEGATION_REQUIRED = ["internal organization chart", "source chart"]
NEGATION_TOKENS = ("not", "no", "never", "without", "independent", "independently", "neither", "nor", "non")


def has_negation(text: str) -> bool:
    clean = " " + re.sub(r"[^a-z0-9]+", " ", text.lower()) + " "
    return any((" " + t + " ") in clean for t in NEGATION_TOKENS)
RETIRED_IDS = ["amazon-assistant", "amazon-smile"]
TRACKING_PATTERNS = [
    re.compile(r"googletagmanager\.com"),
    re.compile(r"google-analytics\.com"),
    re.compile(r"\bgtag\s*\("),
    re.compile(r"ga\s*\(\s*[\"'](?:create|send)[\"']"),
    re.compile(r"\b_paq\b"),
    re.compile(r"plausible\.io"),
    re.compile(r"segment\.com/analytics"),
    re.compile(r"\bmixpanel\b", re.I),
    re.compile(r"\bfbq\s*\("),
    re.compile(r"static\.hotjar\.com"),
]


def check_terms(files: list[str], v: Violations) -> None:
    for rel in files:
        if rel in ALLOW_SELF or is_vendored(rel):
            continue
        if (ROOT / rel).suffix.lower() not in TEXT_SUFFIXES:
            continue
        lines = read_lines(rel)
        for i, line in enumerate(lines, start=1):
            for token in PRIVATE_PATHS:
                if token in line:
                    v.add("private-path", rel, i, f"forbidden path token {token!r}")
            for label, pat in SECRET_PATTERNS:
                if pat.search(line):
                    v.add("secret", rel, i, f"possible {label}")
            if LOOPBACK.search(line) and rel not in LOCALHOST_ALLOW:
                v.add("localhost", rel, i, "loopback reference outside a documented local-dev file")
            for token in DERIVATION_ZERO:
                if token in line:
                    v.add("employer-derivation", rel, i, f"forbidden phrase {token!r}")
            low = line.lower()
            # Negation may span the sentence; inspect a small lookback window.
            window = " ".join(lines[max(0, i - 3):i]).lower()
            for token in DERIVATION_NEGATION_REQUIRED:
                if token in low and not has_negation(window):
                    v.add("employer-derivation", rel, i,
                          f"phrase {token!r} without a negation/independence marker")
            if rel != CHANGELOG_REL:
                for token in RETIRED_IDS:
                    if token in line:
                        v.add("retired-id", rel, i,
                              f"retired agent id {token!r} outside CHANGELOG migration records")
            for pat in TRACKING_PATTERNS:
                if pat.search(line):
                    v.add("tracking", rel, i, f"analytics/tracking signature {pat.pattern!r}")


# Approved GitHub Pages phase lift: the ONLY sanctioned active site_url is the
# canonical GitHub Pages project URL below. Any other active site_url, a second
# active site_url, an empty/malformed value, a custom domain, or a CNAME remains
# a violation. Analytics/tracking (check_terms) and non-Pages deployment
# permissions (check_workflows) remain forbidden.
ALLOWED_SITE_URL = "https://andrewluxem.github.io/organization-agent-swarm/"


def check_site_url_and_domains(files: list[str], v: Violations) -> None:
    # Exactly one active site_url is allowed, and only the canonical Pages URL.
    # (A commented "# site_url:" line does not match and is ignored.)
    active_site_urls = 0
    for i, line in enumerate(read_lines("web/mkdocs.yml"), start=1):
        m = re.match(r"\s*site_url\s*:\s*(.*?)\s*$", line)
        if not m:
            continue
        active_site_urls += 1
        value = m.group(1).strip().strip('"').strip("'")
        if active_site_urls > 1:
            v.add("site_url", "web/mkdocs.yml", i, "multiple active site_url keys are not allowed")
        elif value != ALLOWED_SITE_URL:
            v.add("site_url", "web/mkdocs.yml", i,
                  "site_url must be exactly the canonical GitHub Pages project URL")
    # No CNAME / custom-domain files anywhere (tracked or built).
    for rel in files:
        if Path(rel).name == "CNAME":
            v.add("custom-domain", rel, 0, "CNAME file is not allowed in this phase")
    if SITE.exists():
        for p in SITE.rglob("CNAME"):
            v.add("custom-domain", str(p.relative_to(ROOT)), 0, "CNAME present in built site")


PAGES_DEPLOY_TOKENS = [
    "deploy-pages", "upload-pages-artifact", "actions/deploy-pages",
    "peaceiris/actions-gh-pages", "pages: write", "id-token: write",
    "deployments: write",
]


# Approved GitHub Pages phase lift: the official artifact-based Pages workflow
# below is the ONLY place these specific official constructs are sanctioned.
# Everywhere else (including validate.yml) they remain violations. Third-party
# deployment (peaceiris/actions-gh-pages), "deployments: write", PATs, secrets,
# gh-pages branch publishing, and pull_request_target remain forbidden even in
# the sanctioned workflow (they are absent from the sanctioned set below).
SANCTIONED_PAGES_WORKFLOW = ".github/workflows/pages.yml"
SANCTIONED_PAGES_TOKENS = {
    "deploy-pages", "actions/deploy-pages",
    "upload-pages-artifact",
    "pages: write", "id-token: write",
}


def check_workflows(v: Violations) -> None:
    wf_dir = ROOT / ".github" / "workflows"
    if not wf_dir.exists():
        return
    for wf in sorted(wf_dir.glob("*.yml")) + sorted(wf_dir.glob("*.yaml")):
        rel = str(wf.relative_to(ROOT))
        for i, line in enumerate(wf.read_text(encoding="utf-8").splitlines(), start=1):
            for token in PAGES_DEPLOY_TOKENS:
                if token in line:
                    if rel == SANCTIONED_PAGES_WORKFLOW and token in SANCTIONED_PAGES_TOKENS:
                        continue  # approved official Pages construct in the sanctioned workflow
                    v.add("pages-deploy", rel, i, f"forbidden deployment/permission token {token!r}")


# --- Built-site external runtime asset check --------------------------------

ASSET_ATTRS = {
    "script": ["src"],
    "link": ["href"],
    "img": ["src", "srcset"],
    "source": ["src", "srcset"],
    "iframe": ["src"],
    "embed": ["src"],
    "object": ["data"],
    "audio": ["src"],
    "video": ["src", "poster"],
    "track": ["src"],
}
LINK_ASSET_RELS = {"stylesheet", "preload", "modulepreload", "prefetch", "preconnect", "dns-prefetch"}
EXTERNAL_URL = re.compile(r"^(?:https?:)?//([^/]+)")
LOCAL_HOSTS = {"localhost", "127.0.0.1", "0.0.0.0", "[::1]", "::1"}


class AssetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.external: list[tuple[str, str]] = []  # (tag, url)
        self.mermaid_trigger = False

    def handle_starttag(self, tag: str, attrs) -> None:
        a = {k: (val or "") for k, val in attrs}
        if tag == "pre" and "mermaid" in a.get("class", "").split():
            self.mermaid_trigger = True
        if tag not in ASSET_ATTRS:
            return
        if tag == "link":
            rels = set(a.get("rel", "").lower().split())
            if not (rels & LINK_ASSET_RELS):
                return
        for attr in ASSET_ATTRS[tag]:
            raw = a.get(attr, "")
            if not raw:
                continue
            for token in re.split(r"[,\s]+", raw):
                url = token.strip()
                m = EXTERNAL_URL.match(url)
                if m and m.group(1).split(":")[0] not in LOCAL_HOSTS:
                    self.external.append((tag, url))


def check_built_assets(v: Violations) -> None:
    if not SITE.exists():
        print("NOTE: web/site not built; skipping built-output asset checks "
              "(run: mkdocs build --strict -f web/mkdocs.yml)")
        return
    for html in sorted(SITE.rglob("*.html")):
        rel = str(html.relative_to(ROOT))
        parser = AssetParser()
        try:
            parser.feed(html.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            v.add("html-parse", rel, 0, f"could not parse: {exc}")
            continue
        for tag, url in parser.external:
            v.add("external-asset", rel, 0, f"<{tag}> loads external asset {url}")
        if parser.mermaid_trigger:
            v.add("mermaid-trigger", rel, 0,
                  "found pre.mermaid (would trigger the theme's CDN loader)")


# --- Local Markdown link check ----------------------------------------------

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SNIPPET = re.compile(r'^\s*(?:-{2,}8<-{2,})\s+"([^"]+)"')


def check_markdown_links(files: list[str], v: Violations) -> None:
    md_files = [f for f in files if f.endswith(".md") and not is_vendored(f)]
    for rel in md_files:
        path = ROOT / rel
        for i, line in enumerate(read_lines(rel), start=1):
            sm = SNIPPET.match(line)
            if sm:
                target = sm.group(1)
                # snippets resolve against web/docs (see mkdocs base_path)
                if not (ROOT / "web" / "docs" / target).exists():
                    v.add("broken-snippet", rel, i, f"missing snippet include {target!r}")
                continue
            for m in MD_LINK.finditer(line):
                target = m.group(1).strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                target = target.split(" ", 1)[0]
                if re.match(r"^[a-z][a-z0-9+.\-]*:", target):  # scheme (http:, mailto:)
                    continue
                if target.startswith("#") or not target:
                    continue
                frag = target.split("#", 1)[0]
                if not frag:
                    continue
                resolved = (path.parent / frag).resolve()
                if resolved.exists():
                    continue
                if frag.endswith("/") and (resolved / "index.md").exists():
                    continue
                if (resolved.with_suffix(".md")).exists():
                    continue
                v.add("broken-link", rel, i, f"local link target not found: {frag!r}")


def check_generators(v: Violations) -> None:
    for script in ("scripts/build_adapters.py", "scripts/build_docs.py"):
        proc = subprocess.run(
            [sys.executable, script, "--check"], cwd=ROOT,
            capture_output=True, text=True,
        )
        if proc.returncode != 0:
            v.add("generator-drift", script, 0,
                  f"--check failed: {proc.stdout.strip() or proc.stderr.strip()}")


# --- Main --------------------------------------------------------------------


def main() -> int:
    files = tracked_files()
    v = Violations()
    check_terms(files, v)
    check_site_url_and_domains(files, v)
    check_workflows(v)
    check_built_assets(v)
    check_markdown_links(files, v)
    check_generators(v)

    if not v:
        print("PUBLIC CONTENT OK: no violations found.")
        return 0

    print(f"PUBLIC CONTENT VIOLATIONS: {len(v.items)}")
    for category, path, line, message in sorted(v.items):
        loc = f"{path}:{line}" if line else path
        print(f"  [{category}] {loc} — {message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
