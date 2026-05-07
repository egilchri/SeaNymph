---
title: OpenCPN — Setup and Reference
category: navigation
tags: [OpenCPN, MBTiles, satellite, charts, compass, deviation, calibration, Mac]
sources: [src-opencpn-mac-satellite, src-opencpn-portsmouth-setup]
updated: 2026-05-06
---

# OpenCPN — Setup and Reference

Consolidated reference for OpenCPN on this Mac: chart setup, satellite imagery, plugins, and compass workflows. Synthesized from content in [[navigation-apps]] and [[compass]].

## Overview

OpenCPN is the primary chartplotter on this Mac. Uses:
- Pre-trip route planning with NOAA ENC and RNC charts
- Satellite imagery overlay (MBTiles) for harbor and anchorage reconnaissance
- Compass deviation plugin for full TVMDC correction in-app
- Land-based compass calibration from shore

## Chart Directories

All charts live in `~/Documents/Charts/`. The `MBTiles` directory must be added manually (see below); all others are auto-discovered.

| Directory | Contents | Status |
|---|---|---|
| `ENC/US_ME` | Maine ENCs | Downloaded |
| `RNC/US_ME` | Maine raster charts | Downloaded |
| `ENC/US_REGION02` | Region 2 ENCs | Downloaded |
| `GSHHG` | Global coastline data | Downloaded |
| `MBTiles` | Satellite overlays | Added May 2026 |
| `ENC/US_NH` | NH ENCs | Catalog only — charts not yet downloaded; key chart: 13278 (Portsmouth Harbor) |

**Adding the MBTiles directory (one-time):**
1. Options > Charts > Chart Files
2. Add Directory → select `~/Documents/Charts/MBTiles`
3. Apply

## Satellite Imagery (MBTiles)

### Download script

**Script:** `~/tools/OpenCPN/download_mbtiles.py`

Downloads ESRI World Imagery tiles and packages them as MBTiles. Reaches zoom 18–19 — ESRI is the preferred source (USGS National Map caps at zoom 15; MOBAC has SSL errors on Mac and caps at zoom 15; QGIS/QuickMapServices caps at zoom 14).

```bash
# Full harbor area, zoom 10–16, ~25 MB
python3 ~/tools/OpenCPN/download_mbtiles.py --preset harbor

# Tight wharf detail, zoom 10–18, high detail
python3 ~/tools/OpenCPN/download_mbtiles.py --preset wharf

# Custom bounding box
python3 ~/tools/OpenCPN/download_mbtiles.py \
  --west -70.77 --east -70.76 --south 43.07 --north 43.08 \
  --zmax 18 --name my-wharf
```

MBTiles metadata is set to `type=overlay` — OpenCPN renders satellite as background; NOAA ENC symbols (buoys, depths, hazards) layer on top automatically.

### Downloaded files

| File | Area | Zoom | Size |
|---|---|---|---|
| `penobscot-esri-z16.mbtiles` | Penobscot Bay / Rockland ME | 10–16 | 622 MB |
| `portsmouth-esri-harbor-z16.mbtiles` | Portsmouth NH harbor | 10–16 | 25 MB |

All in `~/Documents/Charts/MBTiles/`.

## Plugins

### World Magnetic Model (WMM)

Handles variation automatically using current-year WMM2025 data. Install from the OpenCPN Plugin Manager. No configuration after install; applies whenever magnetic bearings are enabled.

### Deviation Plugin

Handles vessel-specific compass deviation. Enter compass swing data from [[compass]] (magnetic heading → compass reading pairs); the plugin fits a best-fit Fourier curve and generates corrected compass course for any plotted route leg.

Together, WMM + Deviation Plugin complete the full TVMDC chain inside OpenCPN.

## Compass Workflows

### Enable magnetic bearings

**Options > Ships > Use magnetic bearings** — required for the calibration workflow below and for displaying bearings in magnetic rather than true. WMM variation is applied automatically.

### Downloading additional NOAA charts

1. Options > Charts > Chart Downloader
2. Select catalog (e.g., US_NH for Portsmouth area — chart 13278 Portsmouth Harbor)
3. Download → Apply

### Land-based calibration

Check a hand bearing compass from a fixed position on shore — no boat required. Satellite imagery lets you identify precise fixed landmarks and measure magnetic bearings to them from a known position.

**Workflow:**
1. Enable magnetic bearings (see above)
2. Drop a waypoint at your standing position: right-click chart > New Waypoint
3. Right-click a fixed visible landmark on the satellite layer → Measure bearing
4. The displayed value is the magnetic reading your compass should show from that spot
5. Take a bearing to the same landmark with the hand compass
6. Difference = compass error at that heading

Good landmarks: building corners, pier ends, water towers, fixed nav aids. Not buoys — they swing with current and tide.

**Variation note:** Portsmouth NH ~14.5°W; Penobscot Bay ~15–16°W. If calibrating in Portsmouth before a Maine season, the 1–1.5° difference is small enough to ignore for most purposes, but note it for precise work.

This technique checks deviation at a single heading per landmark. For a full multi-heading deviation table, a compass swing on the boat is required — see [[compass]].

## See Also

- [[navigation-apps]] — full app comparison, AIS integration, tide tools
- [[compass]] — SeaNymph deviation table, full TVMDC chain, compensation procedure
- [[penobscot-bay]] — primary sailing area charts and conditions
