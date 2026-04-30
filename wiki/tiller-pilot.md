---
title: Tiller Pilot — Raymarine ST2000+
category: systems
tags: [tiller-pilot, autopilot, singlehanding, Raymarine, ST2000, electrical]
sources: [src-tiller-pilot]
updated: 2026-04-13
---

# Tiller Pilot — Raymarine ST2000+

The tiller pilot is the singlehander's most important piece of electronics — it frees both hands for sail trim, navigation, and safety tasks. On a Cape Dory 25D, the Raymarine ST2000+ is the standard recommendation. Planned project, not yet installed.

## Model Selection — ST1000 vs. ST2000

| Feature | ST1000 | ST2000+ |
|---|---|---|
| Max displacement | 6,000 lbs | 6,000 lbs (stated) |
| Push/pull force | 29 lbs | 50 lbs |
| Suitable for CD25D? | Marginal — likely underpowered | Yes |

The CD25D is at the upper end of the ST1000's range. The ST2000+ is the correct choice. Research is consistent on this point: the ST1000 is likely to struggle in any real sea state and strain to failure.

**Simrad alternative:** The Simrad TP32 has explicit stall detection (shuts down before motor damage); the ST2000 does not. If long-term reliability is a priority, the Simrad is worth evaluating. Most CD25D owners who document this use Raymarine.

## Critical Dimension — Tiller Pin to Socket

**589mm** — measured from the tiller pin to the cockpit socket mounting point when the tiller is centered (rudder amidships). This is the stroke distance the pilot must accommodate. Confirm this measurement on the actual boat before purchasing. Getting this wrong means the pilot either can't mount or can't steer full range.

The ST2000+ accommodates approximately 300mm of stroke; the socket position must be set so the pilot's extension range matches the boat's tiller arc.

## Mounting — Starboard Coaming

**Mount the socket on the starboard coaming** — standard practice for tiller pilot installation.

- Keeps the pilot on the opposite side from the companionway for unobstructed movement
- Standard placement for most CD25D installations documented in forums
- Keeps compass deviation from the pilot's motor to a minimum (pilot on starboard, compass to port)

### Coaming Reinforcement

The coaming at the socket mounting point must be reinforced — it takes significant thrust loads.

- Add a backing plate inside the coaming (G10, StarBoard, or 1/4" stainless plate all acceptable here — unlike seacocks, this is not a compression-seal application)
- Use through-bolts (3/8" minimum), not wood screws
- Reinforce any flex before relying on the pilot in heavy conditions

### Tiller Pin / Tiller Bracket

The tiller needs a pin for the pilot's arm to attach to. Options:

1. **Dedicated tiller pin** — drill a hole in the tiller at the correct distance from the rudder head, epoxy-fill and re-drill if needed for a snug fit
2. **Bolt-on tiller bracket** — clamp-on bracket, no drilling
3. **Commercial tiller arm extension** — Raymarine makes a compatible fitting

If drilling the tiller: use a quality marine epoxy plug, let cure fully, then re-drill for the pin. This prevents moisture intrusion into the wood.

## Power Wiring

| Parameter | Value |
|---|---|
| Voltage | 12V DC |
| Wire gauge | 14 AWG tinned marine |
| Fuse | 3A–5A inline fuse at panel |
| Circuit | Dedicated — not shared with other loads |

Wire from the main DC panel to a dedicated breaker or fuse. Do not share the circuit. Run the wire with appropriate support and chafe protection — the pilot should be able to run continuously for multi-hour passages.

**SeaTalk wiring** (if integrating with Raymarine instruments):
- Red: 12V SeaTalk power
- Yellow: SeaTalk data
- Bare/screen: ground

SeaTalk allows the pilot to receive compass heading from a Raymarine instrument and respond to course changes. For basic use (helmsman mode), SeaTalk is optional.

## Battery Draw

| Mode | Current draw |
|---|---|
| Standby | 40 mA |
| Auto (moderate conditions) | 0.5–1.5 A |
| Heavy correcting / rough water | Up to 3A+ |

A typical 2-hour passage in moderate conditions: **1.4–2.4 Ah** drawn. On a Group 24 AGM (79–80 Ah), this is negligible. Even a full day under pilot in normal conditions draws well under 20 Ah — acceptable for a system with 100W solar charging.

## Singlehanding Notes

A tiller pilot is essential, not optional, for singlehanded sailing. Specific considerations:

- **Tiller slop degrades performance.** Any looseness in the rudder head, tiller joint, or socket connection causes the pilot to hunt (constant correction cycles). Eliminate slop before relying on the pilot offshore.
- **Bungee cord backup.** Rig a simple bungee or shock cord from the tiller to a cleat as an emergency steering hold. Not a substitute for the pilot, but buys seconds in a crash scenario.
- **Stall detection.** The ST2000 does not have stall detection — the motor can be damaged if it stalls against a hard load (e.g., getting knocked around in waves with tiller hard over). Simrad TP32 has this. Monitor the pilot in heavy conditions and disconnect if it's struggling.
- **Must store when not in use.** The ST2000 is not waterproof. See [[tiller-pilot-waterproofing]].

## Wind Vane Compatibility

A tiller pilot and a wind vane are **complementary, not competing** tools:

- Tiller pilot: steers to a compass course. Good motoring; good when wind is shifting; good short passages.
- Wind vane: steers to apparent wind angle. Free (no power). Better for long offshore passages in steady conditions.

Many singlehanders use the tiller pilot near shore and in light/shifting wind; the wind vane for offshore work. The CD25D's full keel is well-matched to a wind vane for offshore passage-making. Planning both is reasonable.

## GPS / Chartplotter Integration

The ST2000 can accept NMEA 0183 data from a GPS or chartplotter and steer waypoint-to-waypoint. This requires:

- NMEA 0183 output from the chartplotter at correct baud rate (4800 baud standard)
- Correct sentence type (NMEA RMB or APB recommended)
- SeaTalk or SeaTalk-to-NMEA bridge if mixing Raymarine and non-Raymarine gear

For basic singlehanding in familiar waters, steering to compass heading is sufficient. Waypoint steering is useful for longer coastal passages.

## Calibration

After installation the pilot must be calibrated:

1. **Compass swing** — calibrate the pilot's internal compass away from deviation sources
2. **Rudder gain** — adjusts how aggressively the pilot responds to course error
3. **Counter-rudder** — how much opposite rudder it applies to stop the swing
4. **AutoTrim** — compensates for persistent weather/lee helm

Calibration is done through the ST2000 button sequence (see Raymarine manual). A poorly calibrated pilot hunts constantly and drains the battery. Take the time to calibrate properly.

## See Also

- [[tiller-pilot-waterproofing]]
- [[electrical-system]]
- [[battery-management]]
- [[solar-system]]
