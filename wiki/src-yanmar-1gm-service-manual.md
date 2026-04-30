---
title: "Yanmar 1GM Service Manual (SM/1GM·2GM·3GM(D)·3HM)"
category: sources
source-type: manual
source-date: unknown
ingested: 2026-04-30
tags: [engine, Yanmar, 1GM, maintenance, specs, oil, cooling, troubleshooting]
---

# Yanmar 1GM Service Manual (SM/1GM·2GM·3GM(D)·3HM)

**Type:** Factory service manual (covers 1GM, 2GM, 3GM(D), 3HM)
**Author/Origin:** Yanmar Co., Ltd.
**URL or file:** raw/Yanmar_1GM_Service_Manual.pdf

This is the correct manual for SeaNymph's engine. The 1GM is an earlier, lower-output engine than the 1GM10. Covers: General (specs, exterior views, cross-sections), Basic Engine, Fuel System, Lubrication, Cooling, Electrical, Operating Instructions, Periodic Inspection and Servicing. 483 pages total; read targeted sections (~40 pages).

## Key Takeaways

### 1GM Specifications (Chapter 1)

| Specification | Value |
|---|---|
| Type | Vertical 4-cycle, water-cooled diesel |
| Combustion | Swirl pre-combustion chamber |
| Cylinders | 1 |
| Bore × Stroke | 72 × 72 mm |
| Displacement | **0.293 L (293 cc)** |
| Continuous output | **6.5 HP (DIN) @ 3400 rpm** |
| Maximum (1-hr) output | **7.5 HP (DIN) @ 3600 rpm** |
| Fuel injection timing | 15° BTDC ± 1° |
| Fuel injection pressure | 170 kg/cm² |
| Cooling | Direct seawater cooling — rubber impeller type S |
| Starting | Electric (pinion ring gear starter motor) + manual (camshaft) |
| Clutch | KM2A — servo-cone type |
| Clutch reduction ratios (fwd) | 2.21:1, 2.62:1, 3.22:1 |
| Clutch reduction ratio (rev) | 3.06:1 |
| Engine oil capacity (crankcase) | **1.3 L** |
| Clutch case oil capacity | **0.25 L** |
| Engine weight with clutch (dry) | **70 kg** |
| Overall dimensions | 527 × 410 × 485 mm |
| Battery requirement | 12V, 70 Ah minimum |

### Oil Specifications (Chapter 11)

**Engine and clutch oil (crankcase and KM2A clutch case use the same oil):**
- API Service Classification: **CB or CC grade**
- Viscosity by ambient temperature:
  - Below 10°C (50°F): SAE 10W or 20W/20W
  - 10–20°C (50–68°F): SAE 20W or 20
  - 20–35°C (68–95°F): SAE 30 or 40
  - Above 35°C (95°F): SAE 50

> **Note:** The KM2A clutch case uses the **same oil as the crankcase** — not a separate gear oil. Fill both from the same supply. Never mix different brands.

Recommended brand examples (from manual): Shell Rotella, Shell Talona, Caltex RPM Delo Marine, Mobil Delvac 1100/1200 Series, Esso Lube HD, BP Varellus C3.

**Oil change schedule:**
- 1st change: after ~20 hours (new engine break-in)
- 2nd change: after ~30 hours
- 3rd time onward: **every 100 hours**

### Official Maintenance Schedule (Chapter 13, Table 13-1)

| Task | Interval |
|---|---|
| Check fuel level | Daily |
| Check engine oil level (crankcase + clutch case) | Daily |
| Check oil pressure warning lamp | Daily |
| Check cooling water discharge from exhaust | Daily |
| Check exhaust smoke condition | Daily |
| Check for oil/water/fuel leaks | Daily |
| **Change engine oil + clutch oil** | Initial 20 hrs, 30 hrs, then **every 100 hrs** |
| **Replace oil filter element** | **Every 300 hrs** |
| Adjust V-belts (water pump + alternator) | Initial 50 hrs, then every 250 hrs |
| Check/adjust valve clearances (0.2mm both) | Initial 50 hrs, then every 500 hrs |
| Clean fuel filter | Every 100 hrs |
| Replace fuel filter element | Every 250 hrs |
| Check battery electrolyte level | Every month |
| **Inspect seawater pump impeller** | **Every 250 hrs** |
| **Replace seawater pump impeller** | **Every 500 hrs** |
| Clean intake silencer (air filter) | Every 250 hrs |
| Check/clean thermostat | Every 500 hrs |
| **Replace anticorrosion zinc** | **Every 500 hrs** |
| Check exhaust mixing elbow | Every 500 hrs |
| Check/adjust propeller shaft alignment | Initial 50 hrs, every 250 hrs |
| Tighten cylinder head bolts (M10: 7.5 kg-m) | Initial 50 hrs, every 1000 hrs |
| Check/adjust fuel nozzle + injection timing | Every 1000 hrs |
| **Replace rubber hoses and V-belts** | **Every 4 years** |

### V-Belt Tension Specifications

Apply a 10 kg (22 lb) force at the midpoint of each belt:
- **Water pump belt:** 5–7 mm deflection
- **Alternator belt:** 10 mm deflection

### Daily Maintenance Checklist (before every start)

1. Check engine oil level via dipstick (crankcase: cylinder block exhaust side; clutch: top of clutch case)
2. Check clutch oil level
3. Check fuel level
4. Check cooling water discharge from exhaust outlet pipe after starting
5. Check oil pressure lamp goes out after starting
6. Check exhaust smoke (should clear quickly)
7. Check for leaks

### Drain Locations

- **Cooling water drain (1GM/2GM):** Cylinder block exhaust side drain cock
- **Crankcase dipstick location:** Cylinder block exhaust side
- **Crankcase filler:** Top of rocker arm cover or side of gear case

## Contradictions / Surprises

- **Displacement confirmed:** 293 cc (not 318 cc as in the 1GM10 manual previously ingested)
- **Output confirmed:** 6.5 HP continuous (not 8 HP) — the 1GM is a meaningfully less powerful engine
- **Oil interval is every 100 hours** (the 1GM10 manual says 150 hours — significant difference)
- **Oil filter is every 300 hours** (1GM10 says 250 hours)
- **Impeller replace every 500 hours** (1GM10 says 1000 hours / 4 years — different interval)
- **Zinc replace every 500 hours** (1GM10 says minimum 300 hour inspect interval)
- **Rubber hoses must be replaced every 4 years** — this is explicitly in the maintenance table and was not previously in the wiki
- **KM2A clutch uses same oil as crankcase** — the earlier wiki note about "SAE 20/30 HD gear oil" for the clutch is technically correct (SAE 30 falls within that range) but the manual says use the same engine oil, not a separate gear oil. The nameplate spec "SAE 20/30 HD" aligns with the CB/CC engine oil recommendation for warm conditions.
- **V-belt tension differs from 1GM10:** 1GM10 called for 8–10mm deflection (no force specified); 1GM specifies 5–7mm (water pump) and 10mm (alternator) with 10kg applied force — a more precise spec.

## Pages Updated

- [[engine]] — full rewrite with correct 1GM specs, oil spec, maintenance schedule
- [[winterizing]] — hose replacement interval added
