---
title: Radar — Seeing and Being Seen
category: systems
tags: [radar, radar-reflector, safety, navigation, fog, singlehanding, Penobscot Bay]
sources: [src-ais-radar, src-radar-reflector-comparison]
updated: 2026-04-29
---

# Radar — Seeing and Being Seen

Two separate but related problems for a fiberglass sailboat in Maine fog: (1) seeing other vessels and obstructions, and (2) being seen by other vessels' radar. Both require active solutions. The CD25D's fiberglass hull is nearly invisible to radar without a good reflector.

---

## Part 1 — Marine Radar (Seeing Others)

### Why Radar on a 25-Footer

Penobscot Bay in July and August is a fog hotspot. Radar is the only tool that lets you navigate safely in dense fog — AIS shows vessels that transmit; radar shows everything: vessels, islands, buoys, lobster pots (sometimes), squall lines, breakwaters. For singlehanding in Maine, radar is as close to mandatory as it gets.

### Radome vs. Open Array

For a sailboat, **radome** is the only sensible choice:
- Enclosed dome — no exposed moving parts to snag sails or rigging
- More compact, less windage aloft
- Lower power consumption than open array
- Slightly shorter range and wider beamwidth than open array, but adequate for coastal work

### Magnetron vs. Solid-State

**Choose solid-state (also called broadband, CHIRP, or pulse compression).** The difference matters:

| Technology | Power | Warm-up | Close-range | Maintenance |
|---|---|---|---|---|
| Magnetron | Higher | 1–3 min warm-up required | Blind zone close in | Magnetron tube wears out, needs replacement |
| **Solid-state** | Lower | Instant-on | Excellent close-range | No vacuum tubes; very reliable |

Solid-state radar is particularly well-suited to a sailboat: lower power draw (critical for battery bank), instant-on when you need it in fog, and no scheduled maintenance. The Raymarine Quantum and Simrad HALO series are solid-state. Furuno DRS4W is digital/solid-state. The older Garmin GMR 18 HD3 is magnetron — adequate but a step behind.

### Key Features to Understand

- **MARPA** (Mini-Automatic Radar Plotting Aid): tracks multiple targets, calculates each target's course, speed, and CPA (closest point of approach). Alerts you before a collision becomes imminent. Very useful singlehanding.
- **Doppler processing**: instantly color-codes moving targets — approaching vessels appear red, receding green. Eliminates the need to watch multiple radar sweeps to determine if something is approaching. Significant cognitive load reduction for a singlehander.
- **Dual-range display**: shows two ranges simultaneously (e.g., 1/4 nm and 6 nm). Keeps close-in and distant pictures without switching.
- **AIS overlay**: when connected to an AIS receiver, overlays AIS targets on the radar picture. Best situational awareness combines radar + AIS.

### Recommended Models for CD25D

| Model | Technology | Power | Price (dome only) | Display | Notes |
|---|---|---|---|---|---|
| **Furuno DRS4W** | Digital/solid-state | Low | $990–$1,300 | iOS tablet via WiFi app | Lowest cost entry; iOS only; no dedicated display included |
| **Raymarine Quantum Q24C** | CHIRP solid-state | 17W tx / 7W standby | $1,125–$1,950 | Raymarine MFD or WiFi | Lowest power of any option; WiFi or Ethernet; excellent choice |
| Si-Tex T-760 | Digital | Not spec'd | ~$1,700 | 7" touchscreen built-in | Standalone; no MFD needed; budget-friendly; no Doppler |
| Simrad HALO20+ | Solid-state | 20W typical / 29W max | ~$2,300 | Simrad MFD | Doppler; excellent close-range; slightly higher power |
| B&G HALO20+ | Solid-state | Similar to Simrad | ~$2,300 | B&G MFD | Same hardware as Simrad HALO, different ecosystem |

**Recommended starting point:** Raymarine Quantum Q24C. Lowest power consumption (critical for a small battery bank with solar), solid-state CHIRP, WiFi option simplifies installation, and can display on a tablet or a Raymarine MFD. Priced mid-range. Widely supported.

**Budget entry:** Furuno DRS4W if you have an iPad and want to try radar without committing to a full MFD.

### Power Considerations

- Raymarine Quantum Q24C: 17W transmitting — roughly 1.4 Ah/hr. A 2-hour passage costs ~3 Ah. Manageable even on a modest battery bank with solar.
- A dedicated 12V circuit with appropriate fusing is required — see [[electrical-system]].
- Total installed cost (dome + mounting hardware + cable + MFD or tablet mount) typically adds $200–$600 to the dome price.

### Mounting on the CD25D

For a 25-foot boat, height is the biggest factor in detection range. Every foot of antenna height extends the radar horizon.

**Recommended location: forward face of the mast, below the steaming light, above the gooseneck.**

- Achieves 15–20 feet above water (good radar horizon)
- Keeps weight lower than the masthead (less impact on stability)
- Forward face avoids mainsail chafe
- Use a dedicated mast bracket to hold the dome several inches off the mast face, so halyards pass freely behind

**Avoid masthead mounting** for a 25-footer — weight and windage aloft hurt stability and sailing performance without proportionate gain in detection range.

**No radar pole needed** if the mast bracket works. Stern radar poles are lowest height and add clutter.

### Radar Limitations

- Does not show vessels inside its minimum detection range (typically 1/16 to 1/4 nm, depending on model — solid-state radars are better here)
- Sea clutter can mask small targets in rough conditions
- Does not identify vessels (AIS does this)
- Does not show lobster pot buoys reliably
- Operator skill matters — learning to read radar takes practice in good conditions before you need it in fog

---

## Part 2 — Radar Reflector (Being Seen)

### The Fiberglass Invisibility Problem

The CD25D's hull is fiberglass, which is transparent to radar. The boat's native radar cross-section (RCS) is typically under 1 m². In moderate sea conditions, this return is lost in sea clutter — the boat effectively disappears from other vessels' radar displays. A container ship's watch officer may not see SeaNymph until she is dangerously close.

This is not hypothetical. Independent tests by US Sailing and UK government labs confirm that fiberglass sailboats without good reflectors are a serious collision risk in conditions that cause other vessels to rely on radar (fog, darkness, rain).

### The Only Metric That Matters: RCS at Heel

Manufacturers advertise peak RCS — measured in a laboratory with the reflector perfectly aligned. This is nearly irrelevant for a sailboat. What matters is the **average RCS when the boat is heeling at 15–20°** — its normal sailing angle.

| Performance | RCS |
|---|---|
| Useless | < 1 m² |
| ISO minimum (ISO 8729-1) | 2.5 m² |
| Good | > 5 m² |
| Excellent (UK MCA standard) | > 10 m² |

### Reflector Types and Performance

| Type | Example | Cost | Avg RCS at 20° Heel | Verdict |
|---|---|---|---|---|
| **Octahedral (folding)** | Davis Echomaster 152 | ~$120–135 | **~0 m²** | Do not buy. Performance collapses at heel. False sense of security. |
| **Tube/cylinder** | Mobri S-2 / Plastimo | ~$70–110 | < 2 m² | Minimal windage; easy to rig on shrouds. "Better than nothing" — inadequate for fog/SAR scenarios. |
| **Tri-lens array** | Firdell Blipper 210-7, Viking Tri-Lens | ~$250–300 | ~1.5–2.0 m² | Minimum acceptable. Below ISO standard but maintains performance at heel. |
| **Stacked dihedral/trihedral array** | **Echomax EM230** | **~$300** | **~4.0 m²** | **Best passive choice.** Consistently maintains performance at heel. |
| **Active RTE (amplified)** | Echomax Active-X | $700–900 | Far exceeds passive | Best raw performance; requires 12V power; more to fail |

**Recommendation: Echomax EM230.** It is the only passive reflector in tests that consistently exceeds the ISO 2.5 m² standard when heeling. The price difference over the Firdell Blipper is small (~$50) for significantly better performance. The cost-per-m²-of-effective-RCS calculation makes it overwhelmingly the better value.

The octahedral "cheap" reflector ($70) is not economical — it provides near-zero protection while creating false confidence.

### Echomax EM230 Specs

- Dimensions: 24.5 cm diameter × 61 cm tall
- Weight: 2.5 kg
- Peak RCS: 24.5 m² (lab)
- Average tested RCS at heel: ~4.0–4.5 m² (independent QinetiQ testing)
- Mount style: mast bracket or halyard

### Mounting on the CD25D

**Optimal location: forward face of the mast, just below the steaming light.**

- Achieves ~15–20 feet above water — extends radar detection range significantly
- Mounting on forward face eliminates mainsail chafe (critical — chafe is the number one reason reflectors are removed)
- Use a dedicated mast bracket to hold the reflector 2–3 inches off the mast face; halyards pass freely behind
- Avoid masthead mounting — weight of 2.5 kg at the very top is significant for a 25-footer; stability and righting moment will suffer
- Avoid stern mounting — too low; shortest detection range

### Active Radar Target Enhancer (RTE) — When It's Worth It

An active RTE detects the incoming radar "ping" and transmits a powerful amplified reply. Effective RCS many times greater than any passive device. Also provides an audible alarm when being painted by a radar (useful watch-keeping alert singlehanding).

- Standby draw: ~23 mA (negligible)
- Transmitting draw: ~155 mA (noticeable but manageable)
- Cost: $800+ for a quality unit (Echomax Active-X is the benchmark)
- Has electronics that can fail; requires power wiring

For coastal daysailing, the Echomax EM230 passive reflector is the practical choice. If SeaNymph moves into offshore passages or extended cruising in heavily trafficked areas, upgrading to an active RTE is worth considering.

### COLREGs Requirement

COLREGs Rule 40: vessels under 20 meters constructed of non-metallic materials "shall, if practicable, be equipped with a radar reflector." The CD25D at 25 feet (7.6 m) qualifies. The "if practicable" language is not an exemption — it acknowledges mounting difficulty while affirming the responsibility.

---

## Summary: Radar Priority List for SeaNymph

1. **Radar reflector (Echomax EM230)** — install first. Cheap relative to radar, immediately makes the boat visible to others. ~$300.
2. **AIS Class B transponder** — makes you visible to commercial traffic with AIS displays. ~$400–600.
3. **Marine radar (Raymarine Quantum Q24C or similar)** — allows you to see in fog. ~$1,200–2,000 installed.

All three together provide comprehensive situational awareness. In the near term, the reflector and AIS transponder offer the most safety per dollar.

## See Also

- [[ais]]
- [[penobscot-bay]]
- [[electrical-system]]
- [[navigation-apps]]
