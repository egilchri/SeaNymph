---
title: Solar System — Victron MPPT + Renogy Panels
category: systems
tags: [solar, Victron, MPPT, Renogy, electrical, battery-charging]
sources: [src-solar-research]
updated: 2026-04-13
---

# Solar System — Victron MPPT + Renogy Panels

Planned solar charging system for the CD25D. Goal: charge the house battery bank at anchor and reduce dependence on running the engine or shore power for battery maintenance.

## Planned Components

| Component | Model | Notes |
|---|---|---|
| Charge controller | Victron SmartSolar MPPT 75/15 | MPPT (more efficient than PWM). Built-in Bluetooth for monitoring via VictronConnect app. 75V max PV voltage, 15A max charge current. |
| Solar panels | Renogy (100W, likely rigid) | Exact panel TBD — see mounting section |
| Battery connection fuse | 20–25A inline fuse or breaker | Between controller BAT+ terminal and battery positive |
| Wire | 10 AWG tinned copper marine wire | For both panel-to-controller and controller-to-battery runs |
| Deck gland | Scanstrut Deck Seal or equivalent | Waterproof penetration for wiring through deck/cabin |

## Victron MPPT 75/15 — Wiring Procedure

**Critical: always connect battery FIRST, then panels.** Connecting panels before battery can damage the controller.

1. **Cover panels** (or disconnect) before starting
2. **Connect battery positive** to BAT+ terminal with inline fuse near battery
3. **Connect battery negative** to BAT- terminal
4. **Connect panel positive** to PV+ terminal
5. **Connect panel negative** to PV- terminal
6. **Uncover panels** — controller LEDs should illuminate and show charging status

**Optional LOAD output:** The 75/15 has a 15A load output for directly powering DC devices. Useful for controlling small loads (e.g., an anchor light) with automatic low-voltage disconnect to protect the battery. For loads over 15A, connect directly to the battery with appropriate fusing.

## Victron 75/15 Specifications

- Max PV open-circuit voltage: 75V
- Max charge current: 15A
- Battery voltage: auto-detects 12V or 24V
- Bluetooth: yes (SmartSolar version) — use VictronConnect app
- Can handle two 50W panels in series or parallel (verify total voltage/current stays within limits)
- Recommended battery fuse: 20A or 25A

## Renogy Cable Compatibility Issue

Renogy solar panels come with MC4 connectors and cables. The Victron 75/15 uses screw terminals, not MC4 connectors. **The Renogy cables must be modified** — cut off the MC4 connectors and terminate with ring terminals or bare ends for the screw terminals.

> **Note:** A dedicated research file covers this process in detail ("Modifying Renogy Solar Cables for Victron MPPT Screw Terminals"). Key points: use proper MC4 crimping tool to remove connectors cleanly, strip to correct length, use marine-grade ring terminals, and ensure no bare wire is exposed. File was too large to read fully — consult raw source for step-by-step detail.

## Panel Mounting — Location Options

**Stern rail mount (recommended for CD25D):**
- Keeps panels out of foot traffic
- Clear of most shading from boom and crew
- Rail clamps + short stainless arms + panel frame
- Measure stern rail diameter before ordering clamps (commonly 7/8" or 1")
- Estimated hardware cost: $70–$140 for clamps and arms

**Companionway hatch (strongly discouraged):**
- High foot traffic risk — panel will be stepped on
- Severe shading from boom, crew, halyards
- Heat buildup from direct mounting on fiberglass
- Flexible panels in this location typically fail in 1–2 seasons
- Cape Dory forum owners explicitly warn against this

**Removable/portable setup (good for anchor use):**
- Lash panel to sea hood or cockpit area when needed
- Stow when sailing
- Lower risk of damage; less productive while underway

**Flexible vs. rigid panels:**

| Type | Efficiency | Lifespan | Notes |
|---|---|---|---|
| Rigid monocrystalline | 18–23% | 20–25 years | Best long-term value; needs frame/mount |
| Flexible (ETFE coated) | 15–18% | 2–5 years realistic | OK for temporary/removable; poor for permanent deck mount |
| Flexible (PET coated) | 7–15% | 1–3 years | Avoid for marine use |

For a permanent installation, **rigid panels on a stern rail mount is the right answer** for this boat. Flexible panels on the companionway hatch are not recommended.

## Solar System Shopping List (2025 Estimates)

| Item | Est. cost |
|---|---|
| 100W rigid monocrystalline panel | $90–$140 |
| Victron SmartSolar MPPT 75/15 | $90–$130 |
| Stern rail clamps (x2) | $30–$60 |
| Mounting arms/frame material | $40–$80 |
| 10/2 AWG tinned marine wire (per foot) | $1.50–$2.50 |
| MC4 connectors | $10–$20 |
| Inline fuse holder + 20A fuse | $20–$40 |
| Ring terminals (heat shrink) | $15–$25 |
| Deck gland (Scanstrut or similar) | $20–$35 |
| Marine sealant | $15–$25 |
| Zip ties, cable mounts | $10–$15 |
| **Total hardware estimate** | **~$400–$700** |

Prices as of April 2025; verify current pricing. Defender Marine (defender.com) stocks most items.

## Wiring Run Notes

- Measure actual wire runs on the boat before buying wire — add 20% for routing around obstacles
- Run wire through a deck gland, not a bare hole — seal all penetrations watertight
- Keep wire runs as short as possible to minimize voltage drop
- 10 AWG is correct for the 15A controller over typical distances on a 25ft boat

## Integration with Battery System

Solar → Victron MPPT 75/15 → Battery bank → Blue Sea 7610 ACR manages distribution to start battery

The Victron will charge the house bank. When voltage rises above the ACR combine threshold (13.6V for 30 sec or 13.0V for 90 sec), the ACR will combine the banks and the solar will charge both.

## See Also

- [[electrical-system]]
- [[batteries]]
- [[battery-management]]
