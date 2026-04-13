---
title: Engine — Yanmar 1GM10 Overview and Maintenance
category: systems
tags: [engine, Yanmar, 1GM10, raw-water-pump, exhaust, winterizing]
sources: [src-misc]
updated: 2026-04-13
---

# Engine — Yanmar 1GM10 Overview and Maintenance

SeaNymph's engine is a **Yanmar 1GM10**, a single-cylinder freshwater-cooled diesel with raw water cooling heat exchanger. It is the standard diesel auxiliary on Cape Dory 25D hulls built in the early–mid 1980s. The engine is reliable and simple but has specific maintenance requirements and at least one known critical risk.

---

## Engine Specifications

| Specification | Value |
|---|---|
| Model | Yanmar 1GM10 |
| Configuration | Single cylinder, 4-stroke diesel |
| Displacement | 232 cc |
| Output | ~9 HP at 3,200 RPM |
| Cooling | Freshwater (closed loop) with raw water heat exchanger |
| Oil type | API CD mineral-based, SAE 15W-40 **only** |
| Oil capacity | ~1.3 liters |
| Raw water pump | 128170-42200 |
| Thermostat opens | 42°C |
| Thermostat fully open | 52°C |

> **Oil type is non-negotiable:** API CD mineral oil only. No synthetics. The 1GM was designed for and tested with API CD mineral oil; Yanmar does not recommend synthetic on this engine.

---

## Engine Compartment Components

### Wet Exhaust System

The CD25D uses a wet exhaust — seawater is mixed with exhaust gas to cool it before discharge overboard.

**Key components visible in the engine compartment:**

**Exhaust mixing elbow:** A metal pipe where hot exhaust gases from the engine mix with raw cooling water. This cools the exhaust to a safe temperature for the rubber hose downstream. The mixing elbow is a wear item — inspect annually for corrosion and pinhole leaks.

**Vernalift muffler (waterlock):** A black cylinder labeled "VERNALIFT." It performs two functions:
1. Muffles exhaust sound
2. Acts as a waterlock — prevents seawater from siphoning back up the exhaust into the engine when the engine is off. This is a critical safety function. If the muffler fails or is incorrectly oriented, the engine can hydrolock (fill with water) while at rest.

**Exhaust hose:** Large-diameter black rubber hose connecting the mixing elbow to the Vernalift, and from the Vernalift to the through-hull discharge. Inspect for hardness, cracks, and chafe against adjacent surfaces.

### Engine Wiring Harness

The circular four-pin electrical connector near the engine is the main interface between the engine sensors and the instrument panel in the cockpit. The harness transmits:
- Engine coolant temperature
- Oil pressure warning signal
- Tachometer signal
- Alternator charging output
- Alarm signals (overheat, low oil pressure)

If the cockpit instruments stop responding to engine conditions (no RPM reading, no temperature gauge response), check this connector first — it can corrode and lose contact without being obviously damaged.

### Ventilation Hose

The white corrugated hose in the engine compartment is the engine bay ventilation hose. On a diesel, this ensures proper air circulation for combustion. Inspect for kinks or blockage.

---

## Raw Water Pump — Critical Failure Risk

The raw water pump (Yanmar part 128170-42200) is a rubber-impeller pump that circulates seawater through the heat exchanger to cool the freshwater circuit. It is a wear item with an important safety caveat.

### Dangerous Location

On the 1GM10, the raw water pump is positioned **directly above the ferrous oil drain/pipe.** If the pump's mechanical seal fails, it drips. That drip lands on the iron oil pipe and causes accelerated corrosion. If that pipe rusts through, the result is sudden catastrophic oil loss.

**How to catch it early:** The pump has a **weep hole** — a small drilled opening in the pump body. A few drops of water from the weep hole indicates normal seal wear. A steady drip or stream indicates imminent seal failure. Inspect the weep hole and the pipe below it at every engine check.

### Impeller

The rubber impeller is the most common consumable. Replace every 2 years or when:
- Flow rate drops (engine runs warm)
- Broken or missing vane in the impeller housing (always check the housing when replacing — broken vane pieces can lodge in the heat exchanger)
- Impeller is hard or cracked

### Rebuild vs. Replace Decision

- **Rebuild:** Economical if only the impeller has failed and the pump body and bearings are in good shape. Impeller kits are inexpensive ($15–30). Quality impeller kits: Poseidon Marine (~$47 full kit), Parts4Engines (~$55 full kit).
- **Replace entire pump:** When bearings are worn (rough feel when rotated by hand), shaft seal is leaking, or the pump body is corroded. A replacement pump is ~$150–300 depending on source.

### Bearing Brands to Specify When Rebuilding

If replacing pump bearings: **KOYO, SKF, or NTN** — these are the quality Japanese/European bearing manufacturers used in Yanmar OEM applications. Avoid generic Chinese bearings for a saltwater application.

### Seal Orientation (Rebuild Reference)

When rebuilding the pump:
- **Water seal:** Spring faces the impeller (toward the wet side)
- **Oil seal:** Spring faces the bearings (toward the dry/bearing side)
Getting this backward causes premature seal failure.

### Post-Rebuild Checks

After any raw water pump work:
1. **Confirm seacock is open before starting.** Running the pump dry for even 30 seconds destroys the impeller.
2. Run engine and check for leaks from the pump body and weep hole.
3. After shutting down, check engine oil: **milky oil = water contamination = a failed gasket or head problem.** This is a serious finding requiring immediate diagnosis before any further running.

---

## Electrical Connections at the Mast Base

The wiring at the base of the mast (connections for mast lighting, wind instruments, VHF antenna coax) is exposed to condensation, bilge splash, and sea spray. Connections here are vulnerable.

**Sealing method for mast base wiring:**

For wire splices and terminal connections at the mast base, use **3M Temflex 2155 self-amalgamating rubber splicing tape:**

1. Clean surfaces completely (isopropyl alcohol)
2. Start wrap 2 inches below the connection
3. Stretch the Temflex tape to **half its original width** as you wrap — this is what activates its self-fusing property
4. **50% overlap** per wrap — no gaps
5. Extend 2 inches past the connection
6. Press firmly to fuse layers together
7. **Overwrap with 3M Super 33+ or 88 vinyl tape** — Temflex has poor UV resistance; the vinyl tape protects it from sunlight and abrasion

This creates a fully waterproof, self-fused seal that resists immersion. Do not use ordinary vinyl tape alone for mast-base connections — it unravels and lets water in.

---

## Routine Maintenance Schedule

| Task | Interval |
|---|---|
| Check oil level | Every use |
| Check raw water flow (exhaust) | Every use |
| Inspect weep hole and pipe below pump | Monthly underway |
| Impeller inspection/replacement | Annually or every 2 years |
| Oil and filter change | Annually (or 100 hours) |
| Fuel filter primary | Annually |
| Fuel filter secondary | Every 2–3 years |
| Zincs (raw water circuit) | Annually |
| Coolant (freshwater circuit) | Every 2–3 years |
| Belts (alternator) | Inspect annually; replace if cracked |

---

## See Also

- [[winterizing]]
- [[electrical-system]]
- [[seacocks]]
- [[batteries]]
