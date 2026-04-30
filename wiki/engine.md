---
title: Engine — Yanmar 1GM10 Overview and Maintenance
category: systems
tags: [engine, Yanmar, 1GM10, raw-water-pump, exhaust, winterizing, maintenance, wiring]
sources: [src-misc, src-yanmar-1gm10-manual]
updated: 2026-04-30
---

# Engine — Yanmar 1GM10 Overview and Maintenance

SeaNymph's engine is a **Yanmar 1GM10** with KM2P marine gear. Single-cylinder, direct seawater-cooled diesel. It is the standard diesel auxiliary on Cape Dory 25D hulls. Simple and reliable, with specific maintenance requirements and one known critical risk (raw water pump location).

---

## Engine Specifications

> **Note:** Values from the official Yanmar 1GM10 Operation Manual (0AGMM-EN0013, 2018). See [[src-yanmar-1gm10-manual]].

| Specification | Value |
|---|---|
| Model | Yanmar 1GM10 |
| Marine gear | KM2P (mechanical cone clutch) |
| Combustion | Swirl pre-combustion chamber, 4-stroke |
| Cylinders | 1 |
| Bore × Stroke | 75 mm × 72 mm |
| Displacement | **318 cc (0.318 L)** |
| Continuous output | 5.9 kW (8 hp metric) @ 3,400 rpm |
| Maximum output | 6.7 kW (9.1 hp metric) @ 3,600 rpm |
| Cooling | **Direct seawater cooling** (rubber impeller pump) |
| Starter motor | 12V DC, 1.0 kW |
| Alternator | 12V, 35A |
| Engine oil capacity | 1.5 L (1.59 qt) total; 0.8 L effective |
| Marine gear oil capacity | 0.3 L (0.32 qt) |
| Reduction ratio (fwd) | 2.21:1, 2.62:1, or 3.22:1 |
| Reduction ratio (rev) | 3.06:1 |
| Engine weight (with gear) | 76 kg (167 lb) |
| Main fuse | 30A |

> **Cooling system note:** The 1GM10 factory spec is **direct seawater cooling** — seawater flows directly through the engine block via the rubber impeller pump. There is no closed freshwater coolant loop on a standard installation. A thermostat regulates flow within the direct seawater circuit. If SeaNymph's engine has a heat exchanger, that would be a non-standard modification — verify on the physical engine.

**Max operating RPM:** 3,400 rpm or less for cruising. Maximum throttle (3,600 rpm) for no more than 5% of operating time (30 minutes per 10 hours). Running at max RPM more than this shortens engine life.

---

## Oil Specifications

### Engine Oil
- **API Service Category:** CC or higher (TBN ≥ 9)
- **Viscosity:** SAE 10W30 or 15W40 — both are acceptable year-round in normal temperatures
- **Never use:** API CG-4 or CH-4 oils
- **Never mix** different oil types or brands
- **Capacity:** 1.5 L (1.59 qt)

### Marine Gear Oil (KM2P)
- **API Service Category:** CD or higher
- **Viscosity:** SAE #20 or #30
- **Capacity:** 0.3 L (0.32 qt)

---

## Official Maintenance Schedule

Source: Yanmar 1GM10 Operation Manual. *(dealer)* = requires authorized Yanmar Marine dealer.

### Before Every Start
- Visual: engine exterior, fuel level, oil level (engine + marine gear), battery charge warning lamp
- After starting: confirm seawater flowing from exhaust outlet, check for fuel/oil/water leaks, note exhaust color

### After Initial 50 Hours of Operation
- Drain fuel tank and fuel filter/water separator
- Change engine oil + replace oil filter element
- Change marine gear oil
- Check/adjust alternator V-belt tension
- Inspect/adjust intake/exhaust valve clearances *(dealer)*
- Inspect/adjust throttle and shift cables *(dealer)*
- Adjust propeller shaft alignment *(dealer)*

### Every 50 Hours
- Drain fuel filter/water separator

### Every 150 Hours
- Change engine oil
- Change marine gear oil
- Inspect battery electrolyte level (wet batteries only — not AGM)

### Every 250 Hours or 1 Year (whichever first)
- Drain fuel tank
- Replace fuel filter element
- Inspect fuel injection nozzle spray pattern *(dealer)*
- Replace engine oil filter element
- **Inspect seawater pump impeller**
- **Inspect zinc anode** — replace if less than 50% of original size
- Clean intake silencer (air filter)
- Clean exhaust/water mixing elbow
- Clean breather pipe
- Check/adjust alternator V-belt tension
- Check wiring connectors
- Inspect/adjust intake/exhaust valve clearances *(dealer)*
- Inspect/adjust throttle and shift cables *(dealer)*

### Every 1000 Hours or 4 Years (whichever first)
- Inspect fuel injection timing *(dealer)*
- **Replace seawater pump impeller** — mandatory even if undamaged
- Check/adjust alternator V-belt tension
- Tighten all major nuts and bolts
- Adjust propeller shaft alignment *(dealer)*

### Key Maintenance Details
- **Alternator V-belt tension:** Correct deflection = 8–10 mm at midpoint between pulleys. Key off, battery switch off before checking.
- **Oil filter torque:** Hand-tighten until gasket seats, then 3/4 turn with wrench; 20–24 N·m (14–17 lb-ft)
- **Zinc anode location:** Inside the anode plug on the engine, labeled "Anticorrosion Zinc." Minimum inspection interval 300 hours; more often in aggressive/corrosive water.
- **Mixing elbow:** Replace every 500 hours or 2 years, whichever first — even if it looks fine. Scale buildup inside narrows the passage and causes overheating.

---

## Raw Water (Seawater) Pump — Critical Failure Risk

The seawater pump circulates cooling water through the engine. Rubber impeller is a consumable.

### Dangerous Location

On the 1GM10, the seawater pump sits **directly above the ferrous oil pipe.** A failing pump seal drips onto that iron pipe and causes accelerated corrosion. If the pipe rusts through, the result is sudden catastrophic oil loss.

**How to catch it early:** The pump has a **weep hole** — a small drilled opening. A few drops = normal wear. A steady drip = imminent seal failure. Inspect at every engine check.

### Impeller Replacement

- **Official Yanmar interval:** Inspect every 250 hours; **replace every 1000 hours or 4 years**, even if not damaged
- Practical trigger: replace sooner if flow drops (engine runs warm), broken/missing vane found in housing, or impeller is hard/cracked
- **Always check the pump housing** when replacing — broken vane pieces can lodge in the cooling passages
- **Impeller rotates counterclockwise** — install blades curved in the correct direction; reversing damages them

### Seal Orientation (Rebuild)
- **Water seal:** Spring faces the impeller (wet side)
- **Oil seal:** Spring faces the bearings (dry side)

### After Any Pump Work
1. Confirm seacock is open before starting. Running dry for 30 seconds destroys the impeller.
2. Run engine, check pump body and weep hole for leaks.
3. After shutdown, check oil — milky oil = water contamination = serious problem requiring immediate diagnosis.

### Parts
- Impeller kits: Poseidon Marine (~$47), Parts4Engines (~$55)
- Replacement pump: ~$150–300 depending on source
- Bearings if rebuilding: specify **KOYO, SKF, or NTN** — avoid generic bearings in a saltwater application

---

## Engine Compartment Components

### Wet Exhaust System

The 1GM10 uses a **wet exhaust** — seawater is injected into the exhaust stream at the mixing elbow to cool it before discharge.

**Mixing elbow:** Where hot exhaust gas mixes with cooling water. Inspect annually for internal scale and corrosion. Replace every 500 hours or 2 years regardless of appearance — scale buildup causes overheating by restricting water flow.

**Vernalift muffler (waterlock):** Black cylinder downstream of the mixing elbow. Functions: (1) muffles exhaust noise, (2) prevents seawater from siphoning back into the engine when stopped. If this fails or is incorrectly oriented, the engine can hydrolock — fill with seawater while at rest.

**Exhaust hose:** Large-diameter rubber hose, mixing elbow → Vernalift → through-hull. Inspect for hardness, cracks, and chafe.

### Engine Wiring Harness

The circular connector near the engine is the main interface between engine sensors and the cockpit instrument panel. It carries:
- Coolant temperature signal
- Oil pressure warning
- Tachometer signal
- Alternator charging output
- Alarm signals (overheat, low oil pressure)

If cockpit instruments stop responding to engine conditions, check this connector first — it corrodes and loses contact without obvious external damage.

### Wiring Color Codes

| Code | Color | Function |
|---|---|---|
| R | Red | Positive (+) |
| B | Black | Negative (−) |
| W | White | Ignition |
| L | Blue | Air heater/glow (optional) |
| RB | Red/Black | Alternator exciter |
| LB | Blue/Black | Alternator charge alarm |
| YW | Yellow/White | Engine oil pressure alarm |
| YB | Yellow/Black | Engine oil pressure sensor |
| WL | White/Blue | Water temperature alarm |
| O | Orange | Tachometer pulse |

---

## Component Identification (Service Side)

Key labeled components visible from the service side:

| # | Component |
|---|---|
| 1 | Nameplate |
| 2 | Thermostat cover |
| 3 | Fuel injection pump |
| 4 | Idle adjuster |
| 5 | Oil filler cap |
| 7 | Engine stop lever |
| 8 | Crankshaft V-pulley |
| 9 | **Seawater pump** |
| 10 | Engine oil filter |
| 11 | Regulator handle |
| 12 | Fuel feed pump |
| 13 | **Engine oil dipstick** |
| 15 | Mixing elbow |
| 16 | Fuel filter |

Non-service side adds: decompression lever, fuel injection valve, intake silencer, tachometer sensor, marine gear dipstick, marine gearbox, starter motor, alternator.

---

## Troubleshooting Quick Reference

| Symptom | Most Likely Cause | First Action |
|---|---|---|
| Oil pressure alarm | Low oil | Check dipstick; add oil |
| Oil pressure alarm | Clogged oil filter | Replace filter + change oil |
| High temp alarm | Seawater not flowing | Stop engine; check seacock, impeller |
| Battery charge warning | Loose/broken V-belt | Check belt; adjust tension |
| Starter turns, won't start | Empty fuel, closed fuel cock | Add fuel, open cock, bleed air |
| Starter turns, won't start | Clogged fuel filter | Replace filter element |
| Starter slow/won't turn | Not in neutral | Shift to neutral |
| Starter slow/won't turn | Weak battery or corroded terminal | Charge battery; clean terminals |
| Black exhaust smoke | Overloaded or dirty air filter | Reduce throttle; clean air filter |
| White exhaust smoke | Timing off or oil burning | Dealer |
| Engine won't turn manually | Internal seizure | Dealer — do not attempt to force |

**After any alarm:** Reduce to low speed immediately. Stop the engine. Identify cause before restarting.

---

## Electrical Connections at the Mast Base

Wiring at the mast base is exposed to condensation, bilge splash, and spray. Use **3M Temflex 2155 self-amalgamating rubber tape** for all splices and terminals here:

1. Clean surface with isopropyl alcohol
2. Start 2 inches below the connection
3. Stretch Temflex to **half its width** as you wrap — this activates self-fusing
4. **50% overlap** per pass
5. Extend 2 inches past connection
6. Press firm to fuse layers
7. **Overwrap with 3M Super 33+ vinyl tape** — Temflex has poor UV resistance

Do not use ordinary vinyl tape alone at the mast base — it unravels and admits water.

---

## See Also

- [[winterizing]]
- [[electrical-system]]
- [[seacocks]]
- [[batteries]]
- [[src-yanmar-1gm10-manual]]
