---
title: Shore Power and ELCI Breaker
category: systems
tags: [shore-power, ELCI, AC, electrical, safety, Blue-Sea]
sources: [src-elci-shore-power]
updated: 2026-04-13
---

# Shore Power and ELCI Breaker

The CD25D uses a 30-amp shore power connection (120V AC) when docked. The key safety upgrade for this system is an ELCI main breaker.

## ELCI Breaker — What It Is and Why It Matters

**ELCI (Equipment Leakage Circuit Interrupter)** detects ground fault current as small as 30mA and trips the circuit instantly. This is the primary protection against **electric shock drowning (ESD)** — a real hazard at marinas where AC current can leak into the water around a boat with a faulty electrical system.

**ABYC E-11 requirement:** An ELCI must be installed within 10 feet of the shore power inlet. On the CD25D, the main AC panel (near the companionway/galley area) is typically within this distance.

**Recommended unit:** Blue Sea Systems A-Series ELCI Main Circuit Breaker, Double Pole, 120V AC, 30A (Part # 3102100). Features:
- 30A overcurrent protection
- 30mA ground fault trip
- Double-pole (interrupts both hot and neutral)
- Optional reverse polarity indicator (illuminates if shore power is miswired at the pedestal)
- Magnetic hydraulic, trip-free design
- Mounting: #6-32 SS screws, 6–8 in-lb torque

## Installation Notes

**Wire colors (US 120V AC shore power):**
- Black = Hot (line)
- White = Neutral
- Green = Ground

**Wiring sequence:**
1. Shore power inlet → Line terminals on ELCI
2. ELCI Load terminals → AC distribution panel
3. Both hot and neutral pass through the toroidal sensing coil — the ground wire does NOT pass through it
4. Connect reverse polarity indicator wires to neutral and ground on the line (shore) side

**Critical:** Do not ground the neutral conductor on the load side of the ELCI — this will cause nuisance tripping.

**Nuisance tripping** (ELCI trips for no apparent reason) on older boats often indicates pre-existing ground-neutral bonds in the AC or DC systems. Troubleshoot by disconnecting appliances one at a time while using a multimeter to check for ground-neutral connections with shore power disconnected.

## Shore Power Safety Checklist

- Test ELCI monthly using the test button — it should trip immediately
- If reverse polarity indicator illuminates, disconnect shore power immediately and investigate the pedestal wiring
- Use marine-grade 30A shore power cord (10 AWG minimum)
- Install a galvanic isolator to prevent stray current corrosion from the dock's shore power ground
- Never swim near the boat when connected to shore power

## AC Wire Sizing (ABYC E-11)

| Gauge | Rating |
|---|---|
| 14 AWG | 15A |
| 12 AWG | 20A |
| 10 AWG | 30A |

All AC wiring must be marine-grade tinned stranded copper.

## See Also

- [[electrical-system]]
- [[batteries]]
