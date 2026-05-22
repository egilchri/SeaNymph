---
title: Battery Management — Blue Sea 7610 SI-ACR
category: systems
tags: [batteries, ACR, Blue-Sea, dual-battery, electrical, wiring]
sources: [src-blue-sea-7610, src-battery-wiring-photos]
updated: 2026-05-22
---

# Battery Management — Blue Sea 7610 SI-ACR

The Blue Sea Systems 7610 SI-ACR (Automatic Charging Relay with Start Isolation) is installed on SeaNymph. It intelligently manages a dual-battery system — keeping the start battery protected while charging both banks when a charging source is active.

## What It Does

- **Combines** both battery banks when a charging source (alternator, solar, shore power charger) raises voltage above the combine threshold
- **Isolates** them when not charging, so house loads can't drain the start battery
- **Start isolation (SI):** When cranking the engine, it temporarily isolates the house bank from the starting circuit, protecting sensitive electronics from voltage sags

This eliminates the need for a manual 1-2-Both battery switch (though some owners keep a manual switch as a backup).

## Wiring — Terminal by Terminal

| Terminal | Type | Connect to | Fuse required |
|---|---|---|---|
| **Stud A** | 3/8" copper stud | Positive post of Bank 1 (e.g. house battery) | Yes — main cable fuse near battery |
| **Stud B** | 3/8" copper stud | Positive post of Bank 2 (e.g. start battery) | Yes — main cable fuse near battery |
| **GND** | Quick-connect spade | DC system ground | **10–15A inline fuse — mandatory** |
| **SI** | Quick-connect spade | Starter solenoid "crank" terminal (positive only during cranking) | **1–10A inline fuse — mandatory** |
| **LED** | Quick-connect spade | Optional remote LED indicator | 2A fuse on LED+ supply |

**Wire gauges:**
- Studs A & B: **1/0 AWG** (rated for 120A continuous)
- GND: 14–16 AWG
- SI: 16 AWG
- LED: control wire gauge

**Stud torque:** 140 in-lb (15.82 Nm) — use a torque wrench

## Critical Wiring Notes

**GND fuse is not optional.** If a ground fault occurs elsewhere in the system, fault current can flow through the ACR's small ground wire without the fuse — causing it to melt and potentially start a fire. The 10–15A fuse creates a deliberate weak point.

**SI terminal wiring is commonly botched.** The SI terminal must connect to a circuit that is positive **only when cranking**, not when the ignition is in the "run" position. If wired to an "ignition-on" circuit, the ACR will stay in isolation mode permanently, and the house battery will never charge from the alternator. If the LED blinks continuously while the engine is running (not cranking), the SI wiring is wrong.

**Terminals A and B are interchangeable** — dual sensing means it doesn't matter which bank connects to which stud.

**Connect directly to battery positive posts** — not downstream of switches or long cable runs. Voltage drop in cables will fool the ACR into making wrong decisions.

## Combine/Isolate Logic

| Condition | ACR state | Voltage thresholds (12V system) |
|---|---|---|
| Charging source active | Combines after delay | >13.6V for 30 sec, or >13.0V for 90 sec |
| No charging source | Isolates after delay | <12.75V for 30 sec, or <12.35V for 10 sec |
| Engine cranking (SI active) | Force-isolates | Overrides voltage logic |
| Either battery below 9.5V | Under-voltage lockout — won't combine | Protects system from bad battery |
| Either battery above 16.0V | Over-voltage lockout — isolates | Protects from overcharging fault |

## LED Status

| LED state | Meaning |
|---|---|
| Solid ON | Batteries combined — charging active |
| OFF | Batteries isolated — normal standby |
| Slow blink (~1 Hz) | Start isolation active — engine cranking |
| Fast blink (~3 Hz) | Lockout — check battery voltage (<9.5V?) or SI wiring fault |

## Ground Wiring Shopping List

For the GND terminal connection:
- 1/4" female quick-connect spade terminals, tinned copper, 14–16 AWG
- Waterproof inline ATC/ATO fuse holder, 14–16 AWG
- 10A or 15A ATC blade fuse
- Short length of 14 AWG tinned copper marine wire (black or green for ground)
- Marine-grade heat-shrink tubing over all connectors

Ancor brand wire and connectors are the marine standard; available at Hamilton Marine or Defender.

## As-Installed on SeaNymph

Confirmed installed as of September 2025. The ACR is mounted in the battery compartment alongside the battery bank.

**Observed wiring colors (SeaNymph-specific):**
- Red/pink heavy cables — positive runs on studs A and B
- Yellow cables — solar input from Victron MPPT entering the compartment
- Black cables — ground/negative
- Black corrugated split loom — cable protection on longer runs

**Also in the compartment:** A Victron SmartShunt — blue rectangular unit with shunt bar wired inline on the negative circuit (confirmed from photos; specific amperage rating not readable). See [[solar-system]] for Victron MPPT context.

**Documentation:** [[src-battery-wiring-photos]] — photos of actual compartment layout.

## See Also

- [[batteries]]
- [[electrical-system]]
- [[solar-system]]
