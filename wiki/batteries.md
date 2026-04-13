---
title: Batteries
category: systems
tags: [batteries, AGM, electrical, Group-24, Lifeline, charging]
sources: [src-battery-research]
updated: 2026-04-13
---

# Batteries

Battery selection and management for the Cape Dory 25D.

## Recommended Type: Group 24 AGM

**AGM (Absorbed Glass Mat)** is the right choice for a CD25D. Maintenance-free, spill-proof, handles deeper discharges than flooded lead-acid, and compatible with all standard charging sources including solar.

**Group 24** is the standard size for this boat. Typical specs: ~79-80 Ah, 12V.

> **Note:** The boat's battery compartment size should be verified before purchasing. Group 24 is the most commonly cited size for CD25D owners, but measure yours.

## Battery Comparison: Lifeline GPL-24T vs. West Marine AGM 79

| Spec | Lifeline GPL-24T | West Marine AGM 79 |
|---|---|---|
| Capacity | 80 Ah | 79 Ah |
| CCA (0°F) | 550 A | 525 A |
| MCA (32°F) | 680 A | 800 A |
| Reserve capacity | 149 min | 135 min |
| Cycle life | ~1,000 cycles @ 50% DoD | ~300 cycles |
| Self-discharge | 2%/month | 3%/month |
| Warranty | 12mo free / 5yr prorated | 18mo free |
| Terminal type | Brass bolt & washer | SAE posts + SS studs |
| Weight | 56 lbs | 53 lbs |
| Manufacturer | Lifeline (military heritage) | East Penn for West Marine |

**Verdict:** For deep-cycle use (running house loads at anchor, solar charging), the **Lifeline GPL-24T is the better battery** — ~3x the cycle life, better reserve capacity, lower self-discharge. More expensive upfront but likely cheaper long-term. Buy from Defender Marine (Defender.com) or East Coast Marine Battery.

If budget is tight or you primarily need starting power, the West Marine AGM 79 is adequate and has a longer free replacement warranty.

## Battery Types — Full Comparison

| Type | Cost | Maintenance | Weight | Cycle life | Notes |
|---|---|---|---|---|---|
| Flooded lead-acid | Lowest | Regular (check water) | Heavy | ~200-500 | Needs ventilation; spills possible |
| AGM | Mid | None | Mid | ~500-1000 | Best all-around for CD25D |
| LiFePO4 (lithium) | Highest | None | Lightest | ~2000-3000 | Requires lithium-compatible charger; significant cost premium |

For a simple coastal cruising boat like the CD25D, **AGM is the pragmatic choice.** Lithium makes sense if you're doing extended offshore passages and need minimum weight and maximum cycle life — not necessary here.

## Charging Sources

The CD25D battery should be charged by:
1. **Engine alternator** — charges while motoring; main charging source underway
2. **Shore power charger** (when at the dock) — Guest ChargePro or equivalent
3. **Solar** — see [[solar-system]]; trickle charging and supplemental charging at anchor

**Guest ChargePro Model 2611/2610:**

> **Note:** Several research files investigated the Guest ChargePro 2611 and 2610. These are older-style marine battery chargers. They are compatible with AGM batteries but must be set to the correct charging profile (some have a selector switch). Using a flooded-battery charge profile on an AGM battery can damage it by overcharging. Verify the charger's AGM compatibility and settings before use.

## Battery Switch / ACR

The Blue Sea 7610 SI-ACR is the planned battery management device — see [[battery-management]] for full detail. It automatically combines and isolates the battery banks based on voltage, ensuring both banks stay charged without risk of draining the start battery.

## Practical Notes

- Keep batteries fully charged when not in use — AGM batteries sulfate if left in a discharged state for extended periods
- In Maine, cold weather reduces effective battery capacity; plan accordingly for fall/winter use
- A fully discharged AGM takes 8-10 hours to recharge from a standard charger; solar is slow (great for maintenance, not fast recharge)
- Check battery terminals periodically for corrosion; clean with baking soda and water; apply dielectric grease

## Local Suppliers (Maine)

- **Hamilton Marine** (Searsport, ME and Portland, ME) — stocks marine batteries
- **Defender Marine** (defender.com) — Lifeline batteries, good pricing
- **West Marine** (Portland, ME) — West Marine AGM batteries

## See Also

- [[electrical-system]]
- [[battery-management]]
- [[solar-system]]
