# Team chart

The chart below reflects the current, neutral roster in `swarm/roster.json`. It
is a capability-oriented structure: one orchestrator, three division leads, and
sixteen specialists.

The reporting hierarchy is shown below. The diagram is an optional visual aid
rendered **on demand** by a locally vendored Mermaid runtime (no external
content delivery network); until you activate it, no diagram runtime is
loaded. The **Hierarchy outline** further down is its complete, accessible
text equivalent, and the diagram source remains readable at all times.

<button type="button" class="md-button" data-mermaid-render aria-controls="team-chart-diagram">Render diagram</button>

<pre id="team-chart-diagram" class="mermaid-source" aria-hidden="true">
flowchart TD
  accTitle: Organization Agent Swarm reporting hierarchy
  accDescr: The Worldwide Marketing Orchestrator leads three division leads (Affiliate Marketing, Automated Advertising, and Consumer Marketing Analytics), and each division lead leads its specialists.
  ROOT["Worldwide Marketing Orchestrator"]
  ROOT --> AFF["Affiliate Marketing Lead"]
  ROOT --> AUTO["Automated Advertising Lead"]
  ROOT --> ANA["Consumer Marketing Analytics Lead"]
  AFF --> PUB["Publisher Programs"]
  AFF --> ASST["Assistant Discovery"]
  AFF --> CAUSE["Cause Marketing"]
  AFF --> ONSITE["Onsite Publishing"]
  AFF --> INF["Influencers"]
  AUTO --> FREE["Free Search"]
  AUTO --> PAID["Paid Search"]
  AUTO --> SOCIAL["Social Advertising"]
  AUTO --> DYN["Dynamic Advertising"]
  AUTO --> OUT["Outbound Marketing"]
  AUTO --> TARGET["Targeting Platform"]
  AUTO --> DEALS["Deals"]
  ANA --> KP["Knowledge Platform"]
  ANA --> SEG["Segmentation and Targeting"]
  ANA --> FORE["Customer Forecasting"]
  ANA --> MEAS["Cross-Channel Measurement and Optimization"]
</pre>

## Hierarchy outline

The same structure as a textual outline:

- **Worldwide Marketing Orchestrator**
    - **Affiliate Marketing Lead** — Publisher Programs, Assistant Discovery,
      Cause Marketing, Onsite Publishing, Influencers
    - **Automated Advertising Lead** — Free Search, Paid Search, Social
      Advertising, Dynamic Advertising, Outbound Marketing, Targeting Platform,
      Deals
    - **Consumer Marketing Analytics Lead** — Knowledge Platform, Segmentation
      and Targeting, Customer Forecasting, Cross-Channel Measurement and
      Optimization

## Portable capability interpretation

The specialist roles are portable and usable in any organization:

- **Assistant Discovery** covers assistant-led, browser, voice, and AI-agent
  discovery surfaces.
- **Cause Marketing** covers purpose-led, charitable, community, and trust
  programs.
- **Publisher Programs** covers affiliate and publisher programs.
- **Knowledge Platform** is the shared vocabulary, documentation, lineage, and
  institutional-memory layer.
- **Cross-Channel Measurement and Optimization** is the independent evidence and
  acceptance layer.

The authoritative, always-current version of every role is generated from the
roster. See the [Roster](../roster/index.md).
