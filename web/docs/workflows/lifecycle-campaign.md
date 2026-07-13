# Lifecycle campaign

Use this for triggered, multi-channel lifecycle programs. It mirrors
`workflows/lifecycle-campaign.md` in the repository.

## Routing

```text
Worldwide Orchestrator
  -> Automated Advertising Lead
      -> Outbound Marketing
      -> Targeting Platform
      -> Deals (when an offer is involved)
  -> Consumer Marketing Analytics Lead
      -> Segmentation and Targeting
      -> Customer Forecasting
      -> Cross-Channel Measurement and Optimization
```

Use **Onsite Publishing** when the journey requires landing pages or
message-center content.

## Controls

- **Outbound Marketing** owns journey logic, suppressions, frequency, and
  deliverability; **Targeting Platform** owns audience contracts and eligibility.
- **Segmentation and Targeting** and **Customer Forecasting** supply evidence;
  **Cross-Channel Measurement and Optimization** decides whether the evidence
  supports launch, continue, modify, or stop, without editing the work.
- Consent, quiet hours, and cross-channel conflicts are stopping conditions.
- Sending to real recipients is a human-approved [release gate](../governance/release-gates.md).
