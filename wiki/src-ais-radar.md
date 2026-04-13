---
title: "AIS and Radar Research — Receivers, Reflectors, and Marine Radar for CD25D"
category: sources
source-type: ai-research-report
ingested: 2026-04-13
tags: [AIS, radar, radar-reflector, safety, navigation, singlehanding]
---

# AIS and Radar Research — Receivers, Reflectors, and Marine Radar for CD25D

**Files covered:**
- raw/AIS Receiver for Small Sailboat_.md
- raw/AIS Receivers for 25-Foot Sailboats_.md
- raw/Tell me about AIS-Catcher Website and Project.md
- raw/Economical Radar Reflector for Sailboat.md
- raw/Affordable Sailboat Radar Guide.md
- raw/Low-Cost Sailboat Radar Options_.md
- raw/Low-Cost Sailboat Radars Research_.md
- raw/Marine Radar Future for Sailboats_.md (first 80 lines — too large to read fully)

## Summary

Eight files covering AIS receivers (receiver vs. transponder, model comparisons), the AIS-Catcher open-source SDR project, radar reflector selection (with extensive RCS testing data), affordable marine radar options for small sailboats, and future radar technology trends. The radar reflector file is the most technically rigorous in the corpus — it includes specific QinetiQ independent test data (not just manufacturer claims) and makes a compelling evidence-based case for the Echomax EM230 over all cheaper passive options.

## Key Takeaways

- For singlehanding in Penobscot Bay: Class B AIS transponder > receiver alone (others can see you)
- Dual-channel AIS receivers are essential — update 2x faster than single-channel
- em-trak R300 (~$300) is the recommended receiver: dual-channel, NMEA 0183/2000/USB, waterproof
- AIS-Catcher + RTL-SDR dongle is a legitimate DIY monitoring option; NOT for primary navigation use
- CD25D's fiberglass hull has native RCS < 1 m² — essentially invisible to commercial radar without a reflector
- **The only metric that matters for radar reflectors is average RCS at 15–20° heel, not peak RCS**
- Octahedral reflectors (Davis Echomaster, ~$70): near-zero RCS at heel — do not buy
- Firdell Blipper 210-7: ~1.5 m² at heel — minimum acceptable
- **Echomax EM230: ~4.0–4.5 m² at heel — only passive reflector meeting ISO 2.5 m² standard — recommended**
- Echomax EM230 mounting: forward face of mast below steaming light on a dedicated bracket
- Active RTEs (Echomax Active-X, $800+): best performance but expensive and power-dependent
- Marine radar: solid-state/CHIRP radome (not magnetron) preferred for sailboats — lower power, instant-on, no maintenance
- Raymarine Quantum Q24C: 17W transmit (lowest power draw), CHIRP, WiFi option, recommended
- Furuno DRS4W ($990-1,300): good budget entry if you have an iPad
- Radar priority order for SeaNymph: reflector first ($300) → AIS transponder ($400-600) → radar ($1,200-2,000)

## Contradictions / Surprises

> **AI-generated.** The radar reflector file (Economical Radar Reflector for Sailboat.md) is notably more rigorous than most AI research reports — it cites specific QinetiQ test data with actual RCS measurements at different heel angles. This is consistent with real independent testing that exists in the marine safety literature. The conclusions (octahedral reflectors are useless at heel; Echomax EM230 is the best passive option) are consistent with what reputable sources like *Practical Sailor* and UK MCA testing have found. Treat with higher-than-usual confidence for AI-generated content.

> The Marine Radar Future file could not be fully read (too large, first 80 lines only). The partial read covered solid-state dominance, Doppler, AI/ML integration, and miniaturization trends — all consistent with the other radar files.

> The AIS receiver files recommend the em-trak R300 primarily. Class B transponders are discussed as conceptually superior for singlehanding but the files focus more on receive-only receivers. The transponder recommendation in the wiki page goes one step further than the sources explicitly stated.

## Pages Updated

- [[ais]]
- [[radar]]
