---
title: "OpenCPN Portsmouth NH Setup — MBTiles and Compass Calibration"
category: sources
source-type: personal-notes
source-date: 2026-05
ingested: 2026-05-06
tags: [OpenCPN, MBTiles, satellite, compass, calibration, Portsmouth]
---

# OpenCPN Portsmouth NH Setup — MBTiles and Compass Calibration

**Type:** personal-notes
**Author/Origin:** Edgar Gilchrist
**URL or file:** ~/Documents/Charts/opencpn-portsmouth-setup.md

## Summary

Documents the OpenCPN configuration Edgar assembled in Portsmouth NH for displaying satellite imagery and NOAA charts — primarily as a platform for hand bearing compass calibration from a fixed land position. The workflow centers on a custom Python script that downloads ESRI World Imagery tiles and packages them as MBTiles, reaching zoom 18–19 and superseding the earlier QGIS/QuickMapServices approach (which was capped at zoom 14).

The calibration technique uses OpenCPN's satellite layer to identify fixed landmarks, measure magnetic bearings to them, and compare to a hand compass reading — no boat required.

## Key Takeaways

- Python script at `~/tools/OpenCPN/download_mbtiles.py` downloads ESRI World Imagery as MBTiles with `--preset harbor` (zoom 16) or `--preset wharf` (zoom 18)
- Downloaded files: `penobscot-esri-z16.mbtiles` (622 MB, Penobscot Bay) and `portsmouth-esri-harbor-z16.mbtiles` (25 MB) in `~/Documents/Charts/MBTiles/`
- MBTiles must be manually added to OpenCPN via Options > Charts > Chart Files > Add Directory
- NOAA ENC/US_NH catalog is configured but charts not yet downloaded; key chart is 13278 (Portsmouth Harbor)
- Compass calibration from land: drop waypoint at standing position, measure bearing to fixed landmark in OpenCPN, compare to hand compass — difference is compass error
- Portsmouth NH magnetic variation: ~14.5°W in 2026 (vs. Penobscot Bay ~15–16°W)
- OpenCPN must be set to magnetic bearings (Options > Ships > Use magnetic bearings) for the calibration workflow; WMM variation is applied automatically

## Contradictions / Surprises

- The previous wiki note in `navigation-apps.md` stated "Zoom 16 fails with a JPG only supports fully opaque colors error" — that was specific to the QGIS workflow. The Python script reaches zoom 16 and above without that problem.
- MOBAC was also rejected earlier (SSL cert errors, zoom 15 cap) — the Python script fully bypasses MOBAC.

## Pages Updated

- [[navigation-apps]] — replaced QGIS MBTiles workflow with Python script; updated chart directory list; added OpenCPN land-based calibration tip
- [[compass]] — added land-based calibration with OpenCPN as a standalone section
