---
title: Engine — Yanmar 1GM Overview and Maintenance
category: systems
tags: [engine, Yanmar, 1GM, raw-water-pump, exhaust, winterizing, maintenance, wiring]
sources: [src-misc, src-yanmar-1gm-service-manual]
updated: 2026-04-30
---

# Engine — Yanmar 1GM Overview and Maintenance

SeaNymph's engine is a **Yanmar 1GM** with KM2A clutch. Single-cylinder, direct seawater-cooled diesel. Standard on Cape Dory 25D hulls from the early–mid 1980s. Simple, reliable, and light — but with specific maintenance requirements and one known critical risk (raw water pump location).

> **Source:** All specs and maintenance intervals from the official Yanmar 1GM Service Manual. See [[src-yanmar-1gm-service-manual]].

---

## Engine Specifications

| Specification | Value |
|---|---|
| Model | **Yanmar 1GM** |
| Clutch | KM2A (servo-cone type) |
| Combustion | Swirl pre-combustion chamber, 4-stroke |
| Cylinders | 1 |
| Bore × Stroke | 72 mm × 72 mm |
| Displacement | **293 cc (0.293 L)** |
| Continuous output | **6.5 HP @ 3,400 rpm** |
| Maximum (1-hr) output | **7.5 HP @ 3,600 rpm** |
| Fuel injection timing | 15° BTDC ± 1° |
| Cooling | **Direct seawater** (rubber impeller type S) |
| Starting | Electric + manual (decompression lever) |
| Reduction ratio (fwd) | 2.21:1, 2.62:1, or 3.22:1 |
| Reduction ratio (rev) | 3.06:1 |
| Engine oil capacity (crankcase) | **1.3 L** |
| Clutch case oil capacity | **0.25 L** |
| Engine weight (dry with clutch) | 70 kg (154 lb) |
| Battery requirement | 12V, 70 Ah minimum |
| Main fuse | 30A |

---

## Oil Specifications

**Both crankcase and KM2A clutch case use the same oil.** Do not mix brands; fill both from the same supply.

- **API Service Classification:** CB or CC grade
- **Viscosity by ambient temperature:**

| Temperature | SAE Viscosity |
|---|---|
| Below 10°C (50°F) | 10W or 20W/20W |
| 10–20°C (50–68°F) | 20W or 20 |
| 20–35°C (68–95°F) | 30 or 40 |
| Above 35°C (95°F) | 50 |

For Maine coastal use (typical operating temp range 10–25°C), **SAE 20W or 30** is appropriate.

---

## Official Maintenance Schedule

### Before Every Start (Daily)
1. Check engine oil level (dipstick: cylinder block exhaust side)
2. Check clutch case oil level (dipstick: top of clutch case housing)
3. Check fuel level
4. After starting: confirm cooling water flowing from exhaust outlet
5. Confirm oil pressure warning lamp extinguishes after start
6. Check exhaust smoke — should clear within moments
7. Check visually for oil, water, or fuel leaks

### Initial Break-In Period
- **First oil change:** after ~20 hours of operation
- **Second oil change:** after ~30 hours of operation
- After 50 hours: check/adjust V-belt tension, valve clearances, propeller shaft alignment, and tighten cylinder head bolts (M10: 7.5 kg-m)

### Every 100 Hours
- **Change engine oil** (crankcase)
- **Change clutch case oil**
- Clean fuel filter

### Every 250 Hours
- **Inspect seawater pump impeller** — check for wear, nicks, cracks
- Check/adjust V-belt tension (water pump + alternator)
- Replace fuel filter element
- Clean intake silencer (air filter)
- Check/adjust propeller shaft alignment

### Every 300 Hours
- **Replace oil filter element**

### Every 500 Hours
- **Replace seawater pump impeller** (mandatory — even if not damaged)
- **Replace anticorrosion zinc**
- Check/clean thermostat
- Check exhaust mixing elbow

### Every 1000 Hours
- Check/adjust fuel nozzle spray pattern and injection timing *(dealer)*
- Tighten cylinder head bolts

### Every 4 Years (time-based)
- **Replace all rubber hoses and V-belts** regardless of condition

### V-Belt Tension Specs
Apply 10 kg (22 lb) force at midpoint:
- **Water pump belt:** 5–7 mm deflection
- **Alternator belt:** 10 mm deflection

---

## Raw Water (Seawater) Pump — Critical Failure Risk

The rubber impeller pump circulates seawater directly through the engine for cooling. **Official interval: inspect every 250 hours; replace every 500 hours.**

### Dangerous Location

On the 1GM, the seawater pump sits **directly above the ferrous oil pipe.** A failing pump seal drips onto that iron pipe and causes accelerated corrosion. If the pipe rusts through, the result is sudden catastrophic oil loss.

**How to catch it early:** The pump has a **weep hole** — a small drilled opening. A few drops = normal wear. A steady drip = imminent seal failure. Inspect at every engine check.

### Impeller Rotation

The impeller rotates **counterclockwise** when viewed from the drive side. Install blades curved in the correct direction — reversing them causes immediate damage.

### Seal Orientation (Rebuild)
- **Water seal:** Spring faces the impeller (wet side)
- **Oil seal:** Spring faces the bearings (dry side)

### After Any Pump Work
1. Confirm seacock is open before starting. Running dry for 30 seconds destroys the impeller.
2. Run engine, check pump body and weep hole for leaks.
3. After shutdown, check oil — milky appearance = water contamination = serious problem.

---

## Engine Compartment Components

### Wet Exhaust System

The 1GM uses a **wet exhaust** — seawater is injected into the exhaust stream at the mixing elbow.

**Mixing elbow:** Inspect every 500 hours for internal scale and corrosion. Scale buildup restricts water flow and causes overheating.

**Vernalift muffler (waterlock):** Prevents seawater from siphoning back into the engine when stopped. If it fails or is misoriented, the engine can hydrolock — fill with seawater while at rest.

**Exhaust hose:** Large-diameter rubber hose, mixing elbow → Vernalift → through-hull. **Replace every 4 years** per official schedule regardless of appearance.

### Cooling System Note

The 1GM has **direct seawater cooling** — seawater flows directly through the engine block via the rubber impeller pump. A thermostat regulates flow within the seawater circuit (bypass type — maintains stable operating temperature). There is no separate freshwater/antifreeze circuit on a standard installation.

### Engine Wiring Harness

The circular connector near the engine connects engine sensors to the cockpit instrument panel:
- Cooling water temperature (warning lamp)
- Oil pressure (warning lamp)
- Tachometer pulse
- Alternator charge lamp

If cockpit instruments stop responding, check this connector first — corrosion causes loss of contact without obvious external damage.

### Component Locations (Exhaust Side / Bow View)

| Component | Location |
|---|---|
| Dipstick (crankcase) | Cylinder block, exhaust side |
| Oil filler cap | Top of rocker arm cover |
| Mixing elbow | Upper exhaust side |
| Fuel oil filter | Exhaust side |
| Fuel feed pump | Lower exhaust side |
| Idle adjuster | Exhaust side |
| Oil pressure sender | Lower exhaust side |
| Lubricating oil filter | Lower front |
| Crankshaft V-pulley | Front (bow side) |

### Component Locations (Intake Side / Stern View)

| Component | Location |
|---|---|
| Decompression lever | Top, intake side |
| Fuel injection valve | Top |
| Intake silencer | Intake side |
| Tachometer sender | Clutch side |
| Clutch dipstick | Top of clutch case |
| Starter motor | Intake/lower side |
| Output shaft coupling | Clutch end |

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
- [[src-yanmar-1gm-service-manual]]
