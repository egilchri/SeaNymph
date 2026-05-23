---
title: Electrical System — Cape Dory 25D Overview
category: systems
tags: [electrical, wiring, DC, AC, panel, marine-grade]
sources: [src-electrical-wiring, src-elci-shore-power]
updated: 2026-04-13
---

# Electrical System — Cape Dory 25D Overview

The CD25D has a simple 12V DC electrical system with an optional AC shore power connection. Factory wiring is several decades old on most hulls — the wiring on these boats is a common source of problems and warrants thorough inspection.

## DC System

- **Voltage:** 12V DC
- **Source:** Battery bank (see [[batteries]])
- **Distribution:** DC panel (location varies by hull — commonly under the main cabin table or near the galley area)
- **Panel type:** Circuit breaker or fuse panel; Blue Sea Systems panels are a common upgrade target

**Known CD25D wiring issues:**
- Factory wiring diagrams are not readily available; configurations varied by production year and dealer
- Older wiring is often undersized by modern standards, uses non-tinned copper (corrodes), and is poorly documented
- Previous owners may have added circuits with no documentation — trace and label before relying on anything

## AC System (Shore Power)

Shore power is a separate 120V AC system, active only when plugged into dock power. The CD25D is a small boat and typically has a simple AC setup: shore inlet → ELCI main breaker → distribution panel → outlets.

**ELCI breaker (see [[shore-power]]):** The ABYC E-11 standard requires an ELCI (Equipment Leakage Circuit Interrupter) within 10 feet of the shore power inlet. This is a safety upgrade for older boats — the ELCI detects leakage current as small as 30mA and trips, preventing electric shock drowning. The Blue Sea A-Series 30A ELCI is the standard recommendation.

## SeaNymph Cable Color Code (As-Installed)

Confirmed from photos (Sep 2025). This is not a standard color scheme — it reflects how SeaNymph's system was actually wired.

| Color | Meaning |
|---|---|
| Yellow | **Positive** — primary positive cable color throughout the DC system; main battery runs, ACR studs, bus bar distribution |
| Black | **Negative / ground** throughout |
| Red | Positive — used on some shorter or secondary positive runs |
| Pink | Positive — observed on ACR stud B; likely a secondary positive run |
| Black corrugated loom | Cable protection sheathing (color carries no electrical meaning) |

> **Note:** Solar MPPT output cable color not yet confirmed. See [[src-busbar-wiring-photo]] and [[src-battery-wiring-photos]].

## Wiring Standards

Always use **marine-grade tinned copper wire** — never automotive or household wire. Tinned copper resists corrosion; untinned copper fails quickly in the marine environment.

| Wire gauge | Max current | Typical use |
|---|---|---|
| 16 AWG | ~13A | Control circuits, instruments |
| 14 AWG | 15A | Lights, small loads |
| 12 AWG | 20A | General circuits |
| 10 AWG | 30A | Solar wiring, larger loads |
| 1/0 AWG | 120A | Main battery cables, ACR main studs |

**Other standards:**
- Use heat-shrink adhesive connectors, not wire nuts or uninsulated butt connectors
- Fuse every circuit as close to the battery positive as practicable
- Label all circuits at both ends
- Protect wires from chafing; use conduit or sheathing in vulnerable runs
- Never run wires through the bilge

## Drilling Fiberglass for Wiring

When running new wires through the deck or cabin:
- Tape the area with blue painter's tape before drilling — prevents gelcoat chipping
- Use a small pilot hole first, then the final size
- Try drilling in reverse at slow speed through the gelcoat, then forward through the laminate
- Seal all penetrations with marine-grade sealant (3M 4200 or Sikaflex 291)
- Check the back side before drilling — existing wires, hoses, or tanks may be in the way

## Singlehanding Implications

- Know your battery switch locations and be able to isolate the battery bank quickly
- Label every circuit so you can identify and isolate a fault at sea
- Keep a multimeter aboard — it's the most useful electrical troubleshooting tool

## See Also

- [[batteries]]
- [[battery-management]]
- [[solar-system]]
- [[shore-power]]
