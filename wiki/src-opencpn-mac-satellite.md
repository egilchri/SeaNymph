---
title: "OpenCPN Mac Satellite Imagery — MBTiles Workflow"
category: sources
source-type: personal-notes
source-date: 2026-04-16
updated: 2026-05-06
ingested: 2026-04-19
tags: [OpenCPN, navigation, satellite, MBTiles, QGIS, Mac, Python]
---

# OpenCPN Mac Satellite Imagery — MBTiles Workflow

**Type:** personal-notes (AI research doc + verified workflow screenshots)
**Author/Origin:** Edgar Gilchrist / AI research session 2026-04-16
**URL or file:** raw/OpenCPN Google Earth Alternatives for Mac.md + Desktop screenshots 2026-04-16

## Summary

The Windows-only Google Earth plugin for OpenCPN does not exist on macOS. The practical Mac alternative is MBTiles: pre-downloaded satellite tiles displayed as a chart layer in OpenCPN, working fully offline. Edgar worked through this on 2026-04-16, first attempting Mobile Atlas Creator (MOBAC) which failed due to SSL certificate errors, then successfully using QGIS with the QuickMapServices plugin.

The resulting `.mbtiles` file is loaded into OpenCPN by adding its containing directory under Options → Charts → Chart Files. The satellite layer then appears as a selectable chart alongside NOAA ENCs and RNCs.

## Key Takeaways

- No Google Earth plugin for Mac OpenCPN — Windows-only technology
- MBTiles is the standard Mac/Linux solution: offline, reliable, no cell signal needed on the water
- **Preferred tool (May 2026):** Python script `~/tools/OpenCPN/download_mbtiles.py` — simpler, no GUI needed, supports zoom up to 18
- **Previous tool chain:** QGIS + QuickMapServices (ESRI) + Generate XYZ Tiles (MBTiles) — still works but more steps
- QGIS zoom 16 fails with "JPG only supports fully opaque colors" error; Python script has no such limit
- MOBAC (Mobile Atlas Creator) — SSL certificate errors and confusing UI; not recommended
- OpenCPN ingestion: Options → Charts → Chart Files → Add Directory → point at folder containing `.mbtiles` file; no Chart Downloader needed
- MBTiles directory must be added **manually** — OpenCPN does not auto-discover it
- Edgar's MBTiles directory: `~/Documents/Charts/MBTiles/`
- First successful output file: `~/Desktop/penobscot-satellite.mbtiles` (294 tiles, ~58 seconds via QGIS)
- Portsmouth harbor file: `portsmouth-esri-harbor-z16.mbtiles` (1,993 tiles, ~25 MB via Python script)

## Verified QGIS Workflow

1. Install QGIS (LTR 3.44 used; 4.0 also available)
2. Install **QuickMapServices** plugin (Plugins menu)
3. Load **ESRI** satellite basemap via QuickMapServices → ESRI
4. Open Processing Toolbox → Raster Tools → **Generate XYZ Tiles (MBTiles)**
5. Set extent to your sailing area, zoom min 8, zoom max 14
6. Set output file to `~/Documents/Charts/MBTiles/<name>.mbtiles`
7. Run — expect ~60 seconds for a Penobscot Bay-sized area at zoom 8–14
8. In OpenCPN: Options → Charts → Chart Files → Add Directory → `~/Documents/Charts/MBTiles`
9. Click "Scan Charts and Update Database" → satellite layer now available

## Preferred Python Script Workflow (May 2026)

Script location: `~/tools/OpenCPN/download_mbtiles.py`

```bash
# Portsmouth harbor, zoom 10-16, ~25 MB
python3 ~/tools/OpenCPN/download_mbtiles.py --preset harbor

# High detail (zoom 18) for a small area
python3 ~/tools/OpenCPN/download_mbtiles.py --west -70.77 --east -70.76 \
  --south 43.07 --north 43.08 --zmax 18 --name my-area
```

- Downloads ESRI World Imagery tiles directly, packages as MBTiles SQLite
- Supports zoom up to 18–19 (wharf/dock level detail)
- No GUI, no SSL issues, progress display with ETA
- Output goes directly to `~/Documents/Charts/MBTiles/`

## QGIS Workflow (April 2026, still valid)

1. Install QGIS (LTR 3.44 used; 4.0 also available)
2. Install **QuickMapServices** plugin (Plugins menu)
3. Load **ESRI** satellite basemap via QuickMapServices → ESRI
4. Open Processing Toolbox → Raster Tools → **Generate XYZ Tiles (MBTiles)**
5. Set extent to your sailing area, zoom min 8, zoom max 14
6. Set output file to `~/Documents/Charts/MBTiles/<name>.mbtiles`
7. Run — expect ~60 seconds for a Penobscot Bay-sized area at zoom 8–14
8. In OpenCPN: Options → Charts → Chart Files → Add Directory → `~/Documents/Charts/MBTiles`
9. Click "Scan Charts and Update Database" → satellite layer now available

## Chart Blending Limitation

OpenCPN 5.12.4 does not support true satellite + ENC blending. JPG tiles are opaque and
cover any chart beneath them. No transparency slider exists in Options → Display (checked
General and Advanced tabs). Workaround: use satellite for visual landmark identification,
switch to ENC view to identify nav aids.

## Contradictions / Surprises

- The original research doc mentioned SAS.Planet (via Wine) and Sat2Chart as MBTiles tools — QGIS is simpler and native on Mac, no Wine needed
- MOBAC looked promising but SSL cert errors made it non-functional in practice
- Zoom 16 JPG transparency failure is a known QGIS issue with certain basemap sources; Python script has no such limit
- USGS National Map Satellite (available in MOBAC) caps at zoom 15 — not enough for wharf-level detail

## Pages Updated

- [[navigation-apps]] — added Mac/OpenCPN satellite imagery section
- [[src-opencpn-portsmouth-setup]] — Portsmouth-specific setup and compass calibration workflow
