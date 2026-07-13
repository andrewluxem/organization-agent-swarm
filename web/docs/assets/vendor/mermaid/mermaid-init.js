/*
 * Local, framework-free Mermaid loader for Organization Agent Swarm docs.
 *
 * The Mermaid runtime is large, so it is loaded ON DEMAND (progressive
 * enhancement) from the vendored, repository-controlled mermaid.min.js — never
 * from a content delivery network. Until a reader activates the "Render diagram"
 * control, the page ships no diagram runtime at all, which keeps first load fast
 * and the default page fully accessible via the adjacent text outline and the
 * readable diagram source.
 *
 * License: Apache-2.0 (same as this repository).
 */
(function () {
  "use strict";

  var self = document.currentScript;
  if (!self) {
    var scripts = document.getElementsByTagName("script");
    self = scripts[scripts.length - 1];
  }
  var base = self && self.src ? self.src.replace(/mermaid-init\.js(\?.*)?$/, "") : "";
  var loaded = false;

  function findMermaidApi() {
    var candidates = [];
    var ns = window.__esbuild_esm_mermaid_nm && window.__esbuild_esm_mermaid_nm.mermaid;
    if (ns) {
      candidates.push(ns);
      if (ns.default) candidates.push(ns.default);
    }
    if (window.mermaid) candidates.push(window.mermaid);
    for (var i = 0; i < candidates.length; i++) {
      var c = candidates[i];
      if (c && typeof c.initialize === "function" && typeof c.run === "function") {
        return c;
      }
    }
    return null;
  }

  function render(nodes) {
    var mermaid = findMermaidApi();
    if (!mermaid) {
      return;
    }
    try {
      mermaid.initialize({
        startOnLoad: false,
        securityLevel: "strict",
        theme: "base",
        flowchart: { useMaxWidth: true },
        themeVariables: {
          primaryColor: "#ffffff",
          primaryTextColor: "#000000",
          primaryBorderColor: "#000000",
          lineColor: "#000000",
          secondaryColor: "#ffffff",
          tertiaryColor: "#ffffff",
          fontSize: "16px",
        },
      });
      nodes.forEach(function (node) {
        node.removeAttribute("aria-hidden");
        node.setAttribute("role", "img");
      });
      mermaid.run({ nodes: nodes });
    } catch (e) {
      // Leave the readable source and text outline in place on failure.
    }
  }

  function loadAndRender(nodes) {
    if (loaded) {
      render(nodes);
      return;
    }
    var script = document.createElement("script");
    script.src = base + "mermaid.min.js";
    script.defer = true;
    script.onload = function () {
      loaded = true;
      render(nodes);
    };
    document.head.appendChild(script);
  }

  function wire() {
    var buttons = document.querySelectorAll("[data-mermaid-render]");
    Array.prototype.forEach.call(buttons, function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("aria-controls");
        var target = id ? document.getElementById(id) : null;
        var nodes = target ? [target] : Array.prototype.slice.call(
          document.querySelectorAll("pre.mermaid-source")
        );
        if (!nodes.length) {
          return;
        }
        btn.disabled = true;
        btn.textContent = "Rendering diagram…";
        loadAndRender(nodes);
        window.setTimeout(function () { btn.hidden = true; }, 50);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wire);
  } else {
    wire();
  }
})();
