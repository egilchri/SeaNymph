---
title: Compass — Deviation Table and Correction
category: navigation
tags: [compass, deviation, variation, TVMDC, navigation, fog]
sources: [src-compass-deviation]
updated: 2026-04-14
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
