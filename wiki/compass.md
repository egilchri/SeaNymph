---
title: Compass — Deviation Table and Correction
category: navigation
tags: [compass, deviation, variation, TVMDC, navigation, fog]
sources: [src-compass-deviation, src-compass-upgrade, src-deviation-assessment]
updated: 2026-04-15
---

# Compass — Deviation Table and Correction

SeaNymph's compass deviation table. This is actual measured data for this specific boat — not generic. Keep a copy in the chart table and one laminated in the cockpit.

---

## SeaNymph Deviation Table

| For (MAG) | Steer (COMP) | Deviation |
|---|---|---|
| 000° | 353° | 7° E |
| 030° | 025° | 5° E |
| 060° | 058° | 2° E |
| 090° | 090° | 0° |
| 120° | 125° | 5° W |
| 150° | 157° | 7° W |
| 180° | 188° | 8° W |
| 210° | 217° | 7° W |
| 240° | 245° | 5° W |
| 270° | 268° | 2° E |
| 300° | 294° | 6° E |
| 330° | 321° | 9° E |

**Reading the table:** If you want to travel on a magnetic bearing of 180°, steer compass 188°. The deviation on that heading is 8° West.

---

## Interpolating Between Table Entries

The table gives values every 30°. For headings between entries, interpolate linearly.

**Example:** Magnetic course 165° — halfway between 150° (dev 7°W) and 180° (dev 8°W):
- Interpolated deviation = 7.5°W ≈ 8°W
- Compass course = 165° + 8° = 173°

In practice, rounding to the nearest degree is fine.

---

## The TVMDC Chain

To convert between True, Magnetic, and Compass:

**True → Compass (plotting a course):**
1. Start with True course (from chart)
2. Apply **Variation** (Penobscot Bay ~16°W in 2025): add westerly variation → gives Magnetic
3. Apply **Deviation** (from table above): add westerly deviation, subtract easterly → gives Compass

**Compass → True (converting a bearing you observed):**
Reverse the process — subtract what you added, add what you subtracted.

**Memory aid:** "Can Dead Men Vote Twice At Elections"
- **C**ompass + **D**eviation(E) - Deviation(W) = **M**agnetic + **V**ariation(E) - Variation(W) = **T**rue

Or simply: **Compass + East = More = True** (easterly corrections increase the number going toward True).

### Worked Example — Penobscot Bay

You want to sail from Rockland to Owl's Head Light. The chart shows a True course of **025°T**.

1. True: 025°
2. Variation: 16°W → Magnetic = 025 + 16 = **041°M**
3. Deviation at ~040° mag ≈ 4°E (interpolating between 030°/5°E and 060°/2°E) → Compass = 041 - 4 = **037°C**

Steer 037° on the compass.

---

## Status: Compensation Is Warranted

> **SeaNymph's current deviation table exceeds professional standards and compensation should be treated as a maintenance item before this season.**

Industry benchmarks for residual deviation:

| Threshold | Meaning |
|---|---|
| **≤ 4°** | ISO 25862:2019 standard for vessels under 500 GT — the target |
| **> 5°** | Mandatory adjustment trigger in many maritime jurisdictions |
| **≥ 7–8°** | Professional compass adjusters consider physical compensation *required* |

SeaNymph's table has a 9° maximum and exceeds 5° on 8 of 12 headings. This meets the threshold where professional adjusters would not consider the compass fit for precision pilotage.

**Practical impact:** At 9° deviation, you are ~810 feet off your intended track per nautical mile — nearly a sixth of a mile over 5 miles. In Maine fog, that's the difference between safe water and a ledge.

**The table is still usable** — applying the corrections in the table gives you the right magnetic course. But there is no margin for error if you misread the table or approximate the wrong heading. After compensation to ≤4°, the corrections are small enough to be inconsequential in most situations.

**Action items:**
1. Attempt DIY compensation this season (see DIY Compensation section below) — likely reduces errors significantly given the cause is the diesel engine
2. If DIY leaves residual > 5°, schedule a professional compass adjuster at haul-out (~$150–300)
3. Check for interference sources: no phones, handheld VHF, or steel objects near the compass when recording the table

---

## SeaNymph's Deviation Pattern

The deviation curve follows a predictable pattern:

- **Northerly headings (300°–060° mag):** Easterly deviation, 2°–9°. The compass reads *less* than magnetic — steer a *lower* compass number to achieve the intended magnetic bearing.
- **Southerly headings (120°–240° mag):** Westerly deviation, 5°–8°. The compass reads *more* than magnetic — steer a *higher* compass number.
- **Zero crossing: 090° magnetic** — no deviation on this heading.
- **Maximum deviation: 9°E at 330° mag** and **8°W at 180° mag**.

The 9° maximum is significant in fog — a course planned on the chart can be off by a full compass card division if deviation is ignored.

---

## When Deviation Matters Most

**Fog navigation** is when this table earns its place. In a Maine fog, the compass may be your primary navigation instrument. Deviation uncorrected on a southerly heading (180° mag, 8°W dev) means you're actually going 188° magnetic — 8° off course. Over 5 miles that puts you 0.7 miles to one side of your intended track.

**Compass bearings on landmarks:** When taking a bearing on a lighthouse to fix position, you observe a compass bearing and must convert it to true to plot on the chart. Apply deviation (for your current heading) and variation.

**Day sailing:** In clear weather with GPS, deviation is background noise. Do not ignore it in fog or when navigating by compass alone.

---

## CD25D Magnetic Environment

Understanding why the deviation pattern exists helps when adding new equipment or considering a replacement compass.

- **Encapsulated lead ballast:** Does NOT contribute to the boat's magnetic signature — a good baseline.
- **Yanmar 1GM10 diesel:** A large ferrous mass close to the cockpit bulkhead where the compass mounts. This is the primary source of deviation on most headings.
- **Bronze portlights, stainless chainplates:** Small contributors; must be in permanent position during any compass swing.
- **Electronics (VHF, chartplotter, 12V wiring):** All introduce electromagnetic interference. Even 1° of error puts you 90 feet off track per nautical mile — consequential on a rock-strewn coast. Twist paired wiring near the compass to cancel the electromagnetic fields.
- **Helmsman position:** Tiller steering means the helmsman often sits on the coaming rather than directly behind the compass. Any replacement compass should be readable from an angle.

---

## Compass Compensation (DIY)

If deviation exceeds 10° on any heading, or after adding new electronics near the compass, compensation is worth attempting before paying for a professional swing. Quality compasses (Ritchie, Plastimo) have built-in compensator modules — two adjustable magnets accessed via small screws on the compass housing.

**Before starting:** Put the boat in its fully loaded seagoing state — everything in its permanent stowage position, engine at operating temperature, all electronics on. Twist any new wiring runs near the compass.

**Cardinal heading procedure:**

1. **N/S correction:** Head magnetic North (000°M, verified by GPS COG in slack tide). If compass doesn't read 000°, adjust the athwartship (N-S labeled) compensator screw until it does. Turn the boat exactly 180° by the compass. If it doesn't now read 180°, adjust the same compensator to remove *exactly half* the remaining error — no more.
2. **E/W correction:** Repeat on magnetic East (090°M) and magnetic West (270°M), using the fore-and-aft (E-W) compensator. Same half-error rule.
3. **Iterate:** Repeat both passes until errors are minimized. The remaining residual deviation is what goes in the deviation table.

> **GPS COG as reference:** In slack tide with minimal current, GPS Course Over Ground is a reliable substitute for a distant landmark. Steer directly toward a waypoint and confirm current is negligible before trusting the COG as a true reference.

This procedure reduces deviation — it doesn't eliminate it. A professional compass adjuster will get residual errors under 2° on most headings. DIY gets you to 3–5° on most boats, which still dramatically reduces the correction needed.

---

## Replacement Compass Options

If the current compass fails or deviation cannot be adequately compensated, bulkhead mount is the correct configuration for the CD25D cockpit.

### Steering Compass

| Model | Dial | Key Feature | Notes |
|---|---|---|---|
| **Ritchie BN-202 Navigator** | 4.5" | CombiDial (horizontal + vertical read); DirectiveForce magnets; internal gimbal | Best all-around for dedicated helmsman; 5-year warranty |
| **Plastimo Contest 101** | ~4" | Readable from cockpit AND cabin interior; built-in clinometer (10° increments); works on 10–25° inclined bulkheads | Best for shorthanded/cruising use; ISO 25862 compliant |
| **Ritchie Venture SR-2** | 3.75" | CombiDial; smaller footprint than BN-202 | Good if mounting space is tight |

The **Ritchie BN-202** is the most commonly recommended steering compass for a sailboat in this class. The **Plastimo Contest 101**'s clinometer is a practical bonus — useful for judging when to reef.

Mounting hole for BN-202: **5.75 inches** (146 mm) — verify cockpit bulkhead thickness and backing before cutting.

### Hand-Bearing Compass

SeaNymph does not currently have a dedicated hand-bearing compass. For coastal piloting in Maine — fixing position by bearing on a lighthouse, assessing collision risk — one is worth having.

| Model | Key Feature | Notes |
|---|---|---|
| **Plastimo Iris 50** | Photoluminescent (no batteries needed); prism sighting; one-handed use | Best overall; the standard choice for Maine cruising |
| **Vion Mini 2000** | Infinity focus optics (target and card in simultaneous focus); high-gravity oil damping | Gold standard for precision; eliminates parallax error |

The **Iris 50** is the practical choice — photoluminescent lighting means it works in fog and at night without battery dependency.

---

## Compass Maintenance

- **UV cover:** Use a snap-on cover when the boat is not in use. Prolonged UV exposure crazes the dome and yellows the dampening fluid.
- **Bubble:** A permanent bubble indicates a leak or diaphragm failure. A small bubble (under 3mm) is functional but worsening. A large or growing bubble warrants replacing the bowl assembly — optical clarity matters at night.
- **Lighting wiring:** The 12V compass lighting circuit must be fused and use marine-grade bulbs. Cheap incandescent replacements can introduce magnetic interference that shifts the card.
- **Teak chemicals:** The compound used in teak restoration (acetone, varnish stripper) can attack compass dome acrylic. Mask or remove the compass before working on nearby brightwork.

---

## Keeping the Table Current

Deviation changes over time as the boat's magnetic environment changes — new electronics, relocated instruments, new hardware near the compass. Signs the table may be stale:
- New VHF, chartplotter, or speakers installed near the compass
- Deviation exceeds 10° on any heading (suggests a new source of interference)
- The boat has been struck by lightning

**Re-swinging the compass:** A professional compass adjuster (a "compass adjuster" or rigger) swings the boat on all headings and adjusts the corrector magnets inside the compass housing to minimize deviation. The residual deviation is what appears in this table. Cost: $150–300 at a Maine boatyard. Worth doing every few years or after any significant change to the boat's magnetic environment.

---

## Variation Reference — Penobscot Bay

Magnetic variation in Penobscot Bay is approximately **15–16° West** as of 2025, and decreasing slowly (roughly 0.1° per year). Check the current compass rose on NOAA Chart 13302 for the exact value when planning a cruise.

For quick mental math underway: **use 16°W variation** for Penobscot Bay.

---

## See Also

- [[navigation-apps]]
- [[penobscot-bay]]
- [[cd25d-overview]]
