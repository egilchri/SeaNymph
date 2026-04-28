---
title: "OpenCPN Mac Satellite Imagery — MBTiles Workflow"
category: sources
source-type: personal-notes
source-date: 2026-04-16
ingested: 2026-04-19
tags: [OpenCPN, navigation, satellite, MBTiles, QGIS, Mac]
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
- **Working tool chain:** QGIS + QuickMapServices (ESRI) + Generate XYZ Tiles (MBTiles)
- Zoom levels 8–14 work reliably; zoom 16 fails with "JPG only supports fully opaque colors" error
- MOBAC (Mobile Atlas Creator) alternative — SSL certificate errors blocked tile download; not recommended
- OpenCPN ingestion: Options → Charts → Chart Files → Add Directory → point at folder containing `.mbtiles` file; no Chart Downloader needed
- Edgar's MBTiles directory: `~/Documents/Charts/MBTiles/`
- First successful output file: `~/Desktop/penobscot-satellite.mbtiles` (294 tiles, ~58 seconds)

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

## Contradictions / Surprises

- The original research doc mentioned SAS.Planet (via Wine) and Sat2Chart as MBTiles tools — QGIS is simpler and native on Mac, no Wine needed
- MOBAC looked promising but SSL cert errors made it non-functional in practice
- Zoom 16 JPG transparency failure is a known QGIS issue with certain basemap sources; zoom 14 gives adequate detail for coastal navigation

## Pages Updated

- [[navigation-apps]] — added Mac/OpenCPN satellite imagery section
