---
title: Navigation Apps and Digital Tools
category: navigation
tags: [navigation, chartplotter, Android, OpenCPN, Navionics, compass, AIS, fog, MBTiles, satellite, Mac, QGIS]
sources: [src-penobscot-bay, src-opencpn-mac-satellite]
updated: 2026-04-19
---

# Navigation Apps and Digital Tools

Digital navigation for coastal sailing on Penobscot Bay. Smartphone apps, compass correction, and practical hardware considerations.

## Compass Correction Basics

The TVMDC mnemonic: **True Virgins Make Dull Company** — the chain for converting between True, Variation, Magnetic, Deviation, Compass headings. Add westerly errors, subtract easterly.

- **Variation:** Earth's magnetic field vs. geographic North. Location-dependent, changes slowly. Published on charts in the compass rose. Penobscot Bay: approximately 14–16°W (verify on current chart). Changes ~0.1°/year.
- **Deviation:** Vessel-specific compass error from onboard ferrous metal, electronics, engine. Changes with heading. Must be determined for each compass by swinging the compass.

Most commercial apps handle variation automatically via NOAA World Magnetic Model (WMM2025 is current). None handle deviation internally except OpenCPN.

## Navigation Apps — Comparison

| App | Cost | Compass Deviation | NOAA Charts | Offline | Standout |
|---|---|---|---|---|---|
| **OpenCPN** | One-time purchase (~$10 Android) | Full plugin support | Yes (RNC + ENC) | Yes | Unmatched customization; deviation plugin completes full TVMDC in-app |
| **Navionics Boating** | Annual subscription | Manual only | Yes (integrated) | Subscription feature | Best UI; SonarChart™ bathymetry; ActiveCaptain community |
| **C-MAP** | Freemium/subscription | Manual only | Yes (integrated) | Subscription feature | Comparable to Navionics; better for Navico gear users |
| **Savvy Navvy** | Annual subscription | Manual only | Yes | Subscription feature | Weather + tide-aware autorouting (unique) |
| **AvNav** | Free | Relies on NMEA input | Raster only | Yes | Server architecture — streams to any browser on boat's WiFi |

### Recommendation

**For traditional navigator who wants deviation handled properly:** OpenCPN paid version (by Dave Register on Google Play). Install the World Magnetic Model plugin (handles variation) and the Deviation plugin (handles deviation). Download free NOAA RNC or ENC charts from the integrated Chart Downloader. Steeper learning curve but most powerful.

**For best UX on a day-to-day basis:** Navionics Boating subscription + free "Nautical Calculator" app (by Gabriele Giacomo) for compass correction math. Navionics for charting; Nautical Calculator for TVMDC conversions when precise heading matters.

**For current variation check:** **CrowdMag** app (free, from NOAA) contains current WMM2025 data and functions as a digital compass. Useful to verify variation data from other apps.

## AIS Integration

No smartphone has a built-in AIS receiver. To display AIS targets on a chartplotter app:
1. Connect an external AIS receiver (or transponder) that outputs NMEA 0183 data over Wi-Fi
2. The app connects to the local Wi-Fi NMEA stream and overlays targets on the chart

OpenCPN, Navionics, and C-MAP all support Wi-Fi AIS integration. This is important for Penobscot Bay: commercial ferry traffic (Vinalhaven/North Haven ferries), fishing vessels, and other commercial traffic all transmit AIS. A Class B AIS transponder is strongly recommended for singlehanding.

## Practical Smartphone Navigation Notes

### Power Management

Running a navigation app with screen-on + active GPS is one of the most power-intensive tasks a phone can perform. A full day of navigation will exceed internal battery capacity. Requirements:
- **Reliable 12V charging at the helm** — non-negotiable for using a phone as navigation display
- Disable battery-saving modes (they can interrupt GPS)
- Put phone in **airplane mode** when using offline charts — this kills cellular/WiFi radios (major power drain) while keeping GPS active

### Redundancy

A smartphone is a consumer device, not a hardened marine instrument. Singlehanding rule: the phone should be backed by at least one of:
- Fixed-mount chartplotter
- Dedicated handheld GPS unit
- Paper charts with the knowledge to use them

Paper charts + "the Taft guide" are the authoritative backup for Penobscot Bay coastal navigation.

### OpenCPN — Creating a Deviation Table

1. Steer the boat on a series of known true headings (use a range on the chart, a known landmark bearing, or celestial observation)
2. Record the ship's compass reading for each
3. Enter pairs into the Deviation plugin
4. Plugin calculates a best-fit curve (Dev = A + B·sin(CC) + C·cos(CC) + D·sin(2CC) + E·cos(2CC))
5. Plugin generates a complete deviation table and can display the corrected compass course for any plotted route leg

## Fog Navigation — Digital Tools

In Maine fog, digital tools are essential:
- **Radar** (separate hardware) — see vessels and obstructions; invaluable for identifying channel markers
- **AIS overlay** — see other vessels' positions, speeds, and identities even when invisible
- **GPS track** — compare your actual track to the chart to catch deviation from course early
- **Depth sounder** — confirm chart depths to verify position

No app substitutes for radar in genuine dense fog.

## Tide and Current Apps

Tide prediction is critical for Penobscot Bay passage planning. Options:
- OpenCPN includes tide and current prediction (uses NOAA data)
- Navionics includes tidal data
- NOAA Tides and Currents website (for pre-trip planning)
- Dedicated apps: PocketTides, Tides Near Me

Key current stations for Penobscot Bay passages:
- Fox Islands Thorofare (modest)
- Casco Passage (more significant — time this)
- Muscle Ridge Channel (can be strong)

## OpenCPN on Mac — Satellite Imagery (MBTiles)

There is no Google Earth plugin for OpenCPN on macOS (the plugin uses Windows-only technology). The standard Mac alternative is **MBTiles**: pre-downloaded satellite tiles displayed as a chart layer, working fully offline — ideal for Maine where cell coverage is unreliable offshore.

### Verified workflow (tested 2026-04-16)

1. Install **QGIS** (LTR 3.44+)
2. Install the **QuickMapServices** plugin (Plugins menu)
3. Load **ESRI** satellite basemap via QuickMapServices → ESRI
4. Open Processing Toolbox → Raster Tools → **Generate XYZ Tiles (MBTiles)**
5. Set extent to your sailing area; zoom min 8, zoom max 14
6. Output to `~/Documents/Charts/MBTiles/<name>.mbtiles`
7. Run — ~60 seconds for a Penobscot Bay-sized area
8. In OpenCPN: **Options → Charts → Chart Files → Add Directory** → point at `~/Documents/Charts/MBTiles`
9. Click "Scan Charts and Update Database" — satellite layer now selectable alongside NOAA charts

**Zoom level note:** Zoom 14 is the reliable maximum. Zoom 16 fails with a "JPG only supports fully opaque colors" error.

**What didn't work:** Mobile Atlas Creator (MOBAC) — SSL certificate errors blocked tile downloads on Mac.

**Other Mac options (untested):**
- **EarthExplorer plugin** — syncs OpenCPN cursor position to a separate Google Earth Pro window (live link, not embedded)
- **KAP files** — raster charts exported from Google Earth; OpenCPN reads natively; useful for tight harbor entrances

Edgar's chart directories on this Mac:
- `~/Documents/Charts/ENC/US_REGION02`
- `~/Documents/Charts/ENC/US_ME`
- `~/Documents/Charts/RNC/US_ME`
- `~/Documents/Charts/GSHHG`
- `~/Documents/Charts/MBTiles` ← satellite tiles here

## See Also

- [[penobscot-bay]]
- [[tiller-pilot]] (ST2000 NMEA/SeaTalk integration)
- [[electrical-system]] (12V power at helm)
