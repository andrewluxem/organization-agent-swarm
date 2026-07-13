/*
 * Minimal, framework-free accessibility enhancement for Organization Agent
 * Swarm docs. Gives the theme's search dialog an accessible name so it satisfies
 * WCAG 2.1 AA (ARIA dialog name). No remote assets, no tracking.
 *
 * License: Apache-2.0 (same as this repository).
 */
(function () {
  "use strict";
  function enhance() {
    var dialog = document.querySelector('[data-md-component="search"][role="dialog"]');
    if (dialog && !dialog.getAttribute("aria-label")) {
      dialog.setAttribute("aria-label", "Search");
    }
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enhance);
  } else {
    enhance();
  }
})();
