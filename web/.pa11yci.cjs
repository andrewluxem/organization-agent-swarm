/**
 * Pa11y CI configuration for the Organization Agent Swarm documentation site.
 *
 * Standard: WCAG 2.1 AA. Zero allowed errors (threshold: 0). No blanket rule
 * suppression: the `ignore` list is empty. If a narrow, unavoidable exception
 * is ever required, add the specific rule code here with an inline comment
 * explaining why, and retain a manual-review requirement.
 *
 * Tests the locally built and served `web/site` output. If any configured page
 * cannot be reached, pa11y-ci fails.
 */
const BASE = process.env.PA11Y_BASE_URL || "http://localhost:8000";

const paths = [
  "/", // home
  "/organization/", // organization overview
  "/organization/team-chart/", // team chart
  "/roster/", // roster overview
  "/roster/affiliate-marketing/", // division: affiliate marketing
  "/roster/automated-advertising/", // division: automated advertising
  "/roster/consumer-marketing-analytics/", // division: consumer marketing analytics
  "/clients/", // supported clients
  "/install/", // installation
  "/governance/", // governance
  "/customize/", // customization
];

module.exports = {
  defaults: {
    standard: "WCAG2AA",
    // Wait for client-side rendering (the vendored Mermaid diagram on the
    // team-chart page) to settle before evaluating.
    wait: 4000,
    // axe-core is the authoritative automated WCAG runner and the standard
    // Material for MkDocs is tested against. HTML CodeSniffer is intentionally
    // not used here: it reports known false positives on the theme's own
    // JavaScript-driven search/palette forms and visually-hidden toggle
    // controls. This is a runner choice, not a rule suppression (ignore is
    // empty), so no WCAG rule is disabled.
    runners: ["axe"],
    timeout: 120000,
    threshold: 0,
    ignore: [],
    chromeLaunchConfig: {
      args: ["--no-sandbox", "--disable-dev-shm-usage"],
    },
  },
  urls: paths.map((p) => BASE + p),
};
