/**
 * Lighthouse CI configuration for the Organization Agent Swarm documentation
 * site. Runs against the locally built and served static site with multiple
 * runs so assertions are not based on a single measurement.
 *
 * Thresholds are firm and must not be lowered to obtain a pass. Fix the
 * underlying issue instead. LCP is environment-sensitive; on an unreliable
 * timing host it may be downgraded to a warning and reported as needs-decision.
 */
const BASE = process.env.LHCI_BASE_URL || "http://localhost:8000";

const paths = [
  "/", // home
  "/roster/", // roster overview
  "/organization/team-chart/", // team chart
  "/install/", // installation
  "/governance/", // governance
];

module.exports = {
  ci: {
    collect: {
      url: paths.map((p) => BASE + p),
      numberOfRuns: 3,
      settings: {
        // Documentation is consumed primarily on desktop; the desktop preset
        // gives realistic, reliable timing (the mobile preset's simulated
        // throttling makes LCP unreliable on a local host).
        preset: "desktop",
        chromeFlags: "--no-sandbox --disable-dev-shm-usage",
      },
    },
    assert: {
      assertions: {
        "categories:performance": ["error", { minScore: 0.9 }],
        "categories:accessibility": ["error", { minScore: 1.0 }],
        "categories:best-practices": ["error", { minScore: 0.95 }],
        "categories:seo": ["error", { minScore: 1.0 }],
        "cumulative-layout-shift": ["error", { maxNumericValue: 0.1 }],
        "largest-contentful-paint": ["error", { maxNumericValue: 2500 }],
        "errors-in-console": ["error", { maxLength: 0 }],
      },
    },
    upload: {
      target: "filesystem",
      outputDir: "./.lighthouseci",
    },
  },
};
