---
title: Tablet Mount — Cockpit Navigation Display
category: systems
tags: [tablet, navigation, cockpit, DIY, King-Starboard, RAM-Mounts]
sources: [src-misc]
updated: 2026-04-13
---

# Tablet Mount — Cockpit Navigation Display

An Android tablet running OpenCPN or Navionics is SeaNymph's primary navigation display underway. The problem is where to put it — the CD25D's cockpit has constraints that eliminate most obvious mounting locations. This page documents the analysis and recommended design.

See [[navigation-apps]] for software selection.

---

## CD25D Cockpit Constraints

**Tiller sweep eliminates the aft area.** The tiller swings 18–24 inches athwartships. Any mount placed at the aft end of the cockpit will be hit by the tiller — a costly collision with a tablet. Aft cockpit placement is off the table.

**The companionway is an "active zone."** The companionway hatch area is the most-trafficked part of the cockpit: you duck under it going below, reach through it for the VHF, grab things from the chart table, and slide the hatch open/closed throughout the day. Anything mounted at companionway height on the centerline will be in the way.

**Coaming-mounted instruments are possible but commit you to a fixed location.** Screwing directly into the coaming means no adjustment and the risk of drilling through the balsa core without proper protection.

---

## Recommended Design: Articulated Arm on Starboard Bulkhead

**Design A — Articulated arm, starboard side of companionway hatch:**

- Mount a **RAM Mounts** or **Scanstrut** articulated arm on the vertical fiberglass bulkhead to starboard of the companionway opening
- The arm folds out for use and folds flat against the bulkhead when not needed
- Position the tablet at instrument panel height — visible from the helm without standing up, retractable when moving through the companionway

This placement keeps the tiller free, clears the active zone, and doesn't commit to a fixed screen angle.

---

## Mount Hardware Options

### RAM Mounts (Ball-Socket System)

The industry standard for marine electronics mounting. Ball-socket joints allow infinite angle adjustment; the arm holds any position under load.

- **Lifetime warranty** on all RAM hardware — they will replace failed components
- **Relevant components for cockpit install:**
  - RAM-B-138 or similar double-socket arm (~18–24 inches extended)
  - Appropriate tablet tray (RAM-HOL-UN10 or similar)
  - 1" ball base mount for the bulkhead
- **Cost:** $80–150 depending on arm length and tablet holder
- RAM balls and sockets are standardized — mix-and-match across generations

### Scanstrut ROKK Mini

A step up from RAM for a permanent install:
- **Mechanical locking** on all joints — tighter hold, no vibration creep
- IP67 waterproof rated
- Carbon fiber or aluminum finish — more yacht-like appearance
- **Cost:** $150–250
- Scanstrut also makes a powered mount version with integrated charging

**For SeaNymph:** RAM Mounts is the pragmatic choice — lower cost, lifetime warranty, widely available at Hamilton Marine and West Marine. Scanstrut is worth considering if aesthetics matter or if you want the mechanical locking action.

---

## Mounting Substrate — Bulkhead Installation

The cockpit bulkhead on the CD25D is fiberglass. This makes it a good mounting surface.

### If Mounting on the Coaming (Covered Fiberglass)

> **Critical:** The CD25D's coaming top is balsa-core construction. Any through-hole must be potted with epoxy before the fastener is installed.

**Potting procedure:**
1. Drill the hole to the desired fastener size
2. Use a bent dental pick or small knife to excavate ~¼" of balsa core around the hole perimeter on each face
3. Fill the cavity with thickened epoxy (colloidal silica or wood flour)
4. Allow to fully cure (24–48 hours)
5. Re-drill the center hole through the cured epoxy plug
6. Install the fastener — it is now isolated from the balsa core

Without potting: water enters through the hole, wicks into the balsa over years, and creates a wet/delaminated core that requires major repair.

### Fastener Specification

- **316 stainless steel machine screws** — not 304 SS in saltwater
- **Nylock nuts** (nylon insert locking) — regular nuts vibrate loose
- **Fender washers** on the backing side — distribute load over a larger area and prevent pull-through
- **3M 4200** for bedding (removable in future); not 5200 (permanent — difficult to remove)
- **No glue or adhesive** as the primary mounting method — mechanical only

### King Starboard (HDPE) as Backing Plate Material

If the fiberglass alone is too thin to hold load:
- Cut a backing plate from **King Starboard** (HDPE marine board), available at Hamilton Marine
- Starboard is UV-resistant, non-absorbent, easy to drill and machine, and holds fasteners well
- A ¼–⅜" thick piece behind the bulkhead distributes load and gives the nylock nuts a solid purchase
- Alternative: G10 fiberglass sheet (stiffer, harder to cut but excellent structural properties)

---

## Stowing the Tablet

The articulated arm must fold completely clear of the companionway when not in use. Before a tack or gybe, fold the arm flat. Before going below, fold the arm flat.

Options for securing when stowed:
- A small bungee cord from the arm to a nearby cleat
- A snap or velcro patch on the bulkhead at the folded position

---

## Waterproofing and Screen Visibility

Most tablets are not rated for spray. Options:
- **Pelican Vault** soft case with clear touchscreen-compatible front — protects from spray while allowing full touch operation
- **Dedicated marine tablet** (Garmin DriveTrack, Navionics-specific) — waterproof built in but expensive
- **Screen visibility in sunlight:** An anti-glare screen protector significantly improves readability in bright Maine conditions. Set tablet brightness to max underway. Tablet displays vary — test yours in sunlight before committing.

---

## Coaming Instrument Mounting (General Technique)

For instruments mounted directly into the coaming top (compass, chartplotter, etc.) — not RAM arm mounts:

1. Lay out the instrument cutout template on the coaming
2. Pot all holes as above before cutting the final opening
3. Run a bead of 3M 4200 (not 5200) under the instrument flange before tightening
4. Backing plate inside the coaming; fender washers; 316 SS nylock bolts
5. Do not over-torque — the goal is to compress the 4200 sealant, not to crush the fiberglass

---

## See Also

- [[navigation-apps]]
- [[electrical-system]]
- [[cd25d-overview]]
