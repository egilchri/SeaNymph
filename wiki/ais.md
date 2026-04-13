---
title: AIS — Automatic Identification System
category: systems
tags: [AIS, safety, navigation, collision-avoidance, singlehanding, Penobscot Bay]
sources: [src-ais-radar]
updated: 2026-04-13
---

# AIS — Automatic Identification System

AIS transmits and receives vessel identity, position, course, and speed data on VHF frequencies. For Penobscot Bay singlehanding — with its ferry traffic, commercial fishing vessels, fog, and island blind spots — AIS is one of the highest-value safety investments on the boat.

## Receiver vs. Transponder — The Critical Distinction

| Type | Receives | Transmits | Others See You? | Cost |
|---|---|---|---|---|
| **AIS Receiver** | Yes | No | No | $250–380 |
| **Class B Transponder** | Yes | Yes | **Yes** | $400–800+ |

**For singlehanding, a Class B transponder is strongly preferred over a receiver.** A receiver lets you see commercial traffic; a transponder makes commercial traffic able to see you. In Penobscot Bay with Vinalhaven/North Haven ferry service and active lobster vessel traffic, being visible to others is as important as seeing them.

A receiver is acceptable as a first step and for the specific DIY/SDR use cases below.

## How AIS Works

- Operates on dedicated VHF channels 87B (161.975 MHz) and 88B (162.025 MHz)
- Range: typically 20–30 nautical miles with a mast-top antenna (line of sight — islands and terrain create blind spots)
- Updates other vessels' position data frequently — dual-channel receivers update twice as fast as single-channel
- Mandatory for: commercial vessels over 65 feet, passenger vessels, fishing vessels over 65 feet
- Not mandatory for: recreational sailboats — but Class B transponders are inexpensive enough and the safety argument is strong

**Penobscot Bay limitation:** The bay's numerous islands create line-of-sight shadows. A vessel behind an island may not appear on AIS even within nominal range. AIS complements but does not replace radar or proper watch-keeping.

## Recommended AIS Receivers (Receive-Only)

| Model | Price | Connectivity | Notes |
|---|---|---|---|
| AMEC CYPHO-150 | ~$249 | NMEA 0183 | Dual-channel; budget choice; no USB |
| **em-trak R300** | ~$300 | NMEA 0183 + NMEA 2000 + USB | Dual-channel, compact, waterproof; best overall for a 25-footer |
| Digital Yacht AIS100PRO | ~$350 | NMEA 0183 + USB | Built-in multiplexer; good for mixed NMEA setups |
| McMurdo SmartFind M15 | ~$237 | NMEA 0183 | Budget entry; basic but functional |

**Always choose dual-channel.** Single-channel receivers miss data and update more slowly.

## Antenna: Shared or Dedicated

The AIS receiver needs a VHF antenna. Two options:

1. **Dedicated AIS antenna** — best performance; second antenna run to masthead; modest cost; cleaner installation
2. **VHF antenna splitter** — shares the existing VHF antenna; loses some signal but simpler; requires a quality splitter (not a passive T-connector)

If using a splitter, upgrade any existing RG-58 coaxial cable to LMR-400 to minimize power loss.

## Integration with Chartplotter / Nav App

AIS data reaches the navigation display via:

- **NMEA 0183** — wired serial connection to chartplotter; works with most older and current chart plotters
- **NMEA 2000** — plug-and-play network; em-trak R300 supports this
- **USB → navigation laptop/tablet** — direct USB or via NMEA-to-WiFi gateway (e.g., Digital Yacht WLN10)

For smartphone nav apps (OpenCPN, Navionics): connect receiver to a NMEA-to-WiFi gateway; the app reads the WiFi stream and overlays AIS targets on the chart. This is the same method described in [[navigation-apps]].

## AIS-Catcher — DIY SDR Approach

AIS-Catcher is free open-source software that turns a cheap RTL-SDR USB dongle (~$25–30) into an AIS receiver.

- **Platforms:** Windows, Mac, Linux, Raspberry Pi
- **Community:** aiscatcher.org has a live map fed by the global network of stations; users can contribute their received data
- **Performance:** Surprisingly capable for the price — legitimate for monitoring and experimenting
- **Important caveat:** The developers explicitly state this is for research and educational purposes. **Not suitable for primary navigation or safety-of-life use.** The software can miss targets or have decoding issues that a dedicated receiver would not.

**Practical use case:** AIS-Catcher on a Raspberry Pi at home as a learning/monitoring tool. Understand traffic patterns in Rockland Harbor. Feed data to MarineTraffic or AIS-Catcher network. Do not rely on it for actual navigation.

## MOB (Man Overboard) AIS Devices

Small AIS transmitters worn on a PFD or integrated into a harness can broadcast a distress signal with GPS coordinates to all nearby AIS-equipped vessels when activated. In cold Penobscot Bay water, time-to-rescue is critical. Worth researching as part of singlehanding safety kit.

## Singlehanding Priority

AIS is arguably more important singlehanding than with crew because:
- You are often below or occupied, not watching for traffic
- Chartplotter can alarm on targets with dangerous CPA (closest point of approach) even when you are not at the helm
- Ferry traffic on Rockland–Vinalhaven–North Haven routes is predictable and fast; a Class B transponder makes the ferry's bridge aware of SeaNymph's presence

## See Also

- [[radar]]
- [[navigation-apps]]
- [[penobscot-bay]]
- [[electrical-system]]
