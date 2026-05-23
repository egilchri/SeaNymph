---
title: "Blue Sea SI-ACR 7610 Installation Manual (990310020 Rev. 009)"
category: sources
source-type: manual
source-date: 2025-01-01
ingested: 2026-05-23
tags: [electrical, ACR, Blue-Sea, batteries, wiring, dual-battery]
---

# Blue Sea SI-ACR 7610 Installation Manual

**Type:** Manufacturer installation manual
**Author/Origin:** Blue Sea Systems
**File:** raw/blue_sea_acr_install.pdf

## Summary

Official two-page installation manual for the Blue Sea Systems SI-ACR 7610 (and the companion E-Series Dual Circuit Plus battery switch). Includes full wiring diagram for both outboard (combined alternator/starter) and inboard (separate alternator/starter) engine configurations. This is the authoritative source for terminal connections and wiring topology.

## Key Takeaways

### Terminal Connections

| Terminal | Wire gauge | Fuse | Connect to |
|---|---|---|---|
| Stud A | Per charging amps chart | Yes — near battery | One battery bank positive |
| Stud B | Per charging amps chart | Yes — near battery | Other battery bank positive |
| GND | 16 AWG | **1A inline** | DC system ground / negative bus bar |
| SI | 16 AWG | 1–10A inline | Starter solenoid "crank" wire — positive only when cranking |
| LED+ | 16 AWG | 1–2A inline | 12/24V positive source |
| LED signal | 16 AWG | — | Quick connect terminal marked LED |

> **Note:** The manual specifies a **1A fuse** on the GND wire (not 10–15A as previously noted in battery-management.md). This is the correct value per the official manual.

### Wire Size and Fuse Ratings for Stud A/B Cables (AWG)

| Charging Amps | Min Wire Size | Fuse Rating |
|---|---|---|
| ≤60A | #6 AWG | 75–90A |
| ≤80A | #4 AWG | 100–125A |
| ≤100A | #2 AWG | 150A |
| ≤120A | #1 AWG | 175A |

The Yanmar 1GM alternator output is approximately 30–40A, so **#6 AWG with 75–90A fuses** is appropriate for SeaNymph's stud A/B cables.

### Wiring Diagram — Inboard Engine Configuration (Relevant to SeaNymph)

The diagram for "Engines With Separate Alternator and Starter Wires — typical of inboard engines" shows:

```
[ALTERNATOR] ──→ connects to one of:
    1. Starter
    2. Engine terminal of battery switch
    3. Start battery positive
    4. House battery positive
    ("Alternator connected to a larger battery bank is most efficient")

[START BATTERY] ──→ Stud A or B on SI-ACR
[HOUSE BATTERY] ──→ Stud B or A on SI-ACR
[SI-ACR GND]    ──→ Negative bus bar (1A fuse, 16 AWG)
[SI wire]        ──→ Start key switch crank terminal (optional, 1–10A fuse)
[Negative Bus Bar] ──→ Ground
```

Both battery negatives connect to a shared **Negative Bus Bar**, which then connects to ground.

### Key Notes from Manual

- **Terminals A and B are interchangeable** — dual sensing means bank assignment doesn't matter
- Connect ACR **directly to battery positive terminals** through fuses — not via a battery switch (voltage drop fools the ACR)
- If LED is flashing while running (not cranking): SI wire is incorrectly wired to an ignition-on circuit instead of crank-only
- The 120A SI-ACR is **not rated for starting currents** — use the Dual Circuit Plus switch COMBINE position for emergency starting only
- Optional storage switch can be wired to disconnect the GND wire for zero current draw when laid up

### LED Status (Confirmed from Manual)

| LED | Status | Reason |
|---|---|---|
| On (solid) | Combined | Charging active |
| Off | Isolated | Discharging / standby |
| Slow flash | Isolated | Start isolation wire energised (cranking) |
| Fast flash | Isolated | Under voltage lockout — one or both batteries below 9.5V (12V system) |

## Contradictions / Surprises

- Prior wiki entry in `battery-management.md` listed the GND fuse as 10–15A. The official manual specifies **1A**. Corrected.
- The GND fuse protects against fault currents flowing in the small ground wire — 1A is intentionally small to make this wire the weak point.

## Pages Updated

- [[battery-management]]
- [[src-blue-sea-7610]]
