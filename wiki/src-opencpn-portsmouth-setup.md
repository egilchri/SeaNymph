# OpenCPN Portsmouth NH Setup

## Goal
Display satellite imagery and NOAA nautical charts for Portsmouth NH in OpenCPN,
for use in hand bearing compass calibration from land.

---

## Satellite Imagery (MBTiles)

### Download script
A Python script was written to download ESRI World Imagery tiles and package them
as MBTiles, bypassing MOBAC (whose UI is unreliable and caps at zoom 15).

Location: `~/tools/OpenCPN/download_mbtiles.py`

### Usage

```bash
# Full Portsmouth harbor, zoom 10-16, ~25 MB, good general overview
python3 ~/tools/OpenCPN/download_mbtiles.py --preset harbor

# Tight wharf area, zoom 10-18, high detail (identify specific structures)
python3 ~/tools/OpenCPN/download_mbtiles.py --preset wharf

# Custom bounding box
python3 ~/tools/OpenCPN/download_mbtiles.py \
  --west -70.77 --east -70.76 --south 43.07 --north 43.08 \
  --zmax 18 --name my-wharf
```

### Downloaded files
| File | Area | Zoom | Size |
|------|------|------|------|
| `penobscot-esri-z16.mbtiles` | Penobscot Bay / Rockland ME | 10–16 | 622 MB |
| `portsmouth-esri-harbor-z16.mbtiles` | Portsmouth NH harbor | 10–16 | 25 MB |

All files saved to: `~/Documents/Charts/MBTiles/`

### Notes
- USGS National Map Satellite (available in MOBAC) caps at zoom 15 — not enough for wharf detail
- ESRI World Imagery goes to zoom 18–19 and is the preferred source
- MBTiles `type` is set to `baselayer` in metadata

---

## Adding MBTiles to OpenCPN

The `MBTiles` directory is **not** auto-discovered by OpenCPN — it must be added manually:

1. **Options > Charts > Chart Files**
2. Click **Add Directory**
3. Select `~/Documents/Charts/MBTiles`
4. Click **Apply**

---

## NOAA ENC Charts (buoys, depths, hazards)

Downloaded directly from NOAA via curl (May 2026) — bypasses the Chart Downloader UI.

```bash
cd ~/Documents/Charts/ENC/US_NH
for url in \
  https://www.charts.noaa.gov/ENCs/US4NH1BC.zip \
  https://www.charts.noaa.gov/ENCs/US4NH1BD.zip \
  https://www.charts.noaa.gov/ENCs/US4NH1BE.zip \
  https://www.charts.noaa.gov/ENCs/US4NH1BF.zip \
  https://www.charts.noaa.gov/ENCs/US4NH1BG.zip \
  https://www.charts.noaa.gov/ENCs/US5NH1AF.zip \
  https://www.charts.noaa.gov/ENCs/US5NH1AG.zip \
  https://www.charts.noaa.gov/ENCs/US5NH1CD.zip \
  https://www.charts.noaa.gov/ENCs/US5NH1DD.zip \
  https://www.charts.noaa.gov/ENCs/US5PSMBC.zip; do
  name=$(basename $url .zip)
  curl -s -o ${name}.zip $url && unzip -q -o ${name}.zip && rm ${name}.zip
done
```

After downloading: **Options > Charts > Scan Charts and Update Database > Apply**

### Chart coverage
| Chart | Description | Scale |
|-------|-------------|-------|
| US4NH1BC–BG | New Hampshire overview | 1:45,000–90,000 |
| US5NH1AF | Bigelow Bight (offshore Portsmouth) | 1:22,000 |
| US5NH1AG | Bigelow Bight – White Island (Isles of Shoals) | 1:22,000 |
| US5NH1CD | Piscataqua River to Great Bay | 1:22,000 |
| US5NH1DD | Piscataqua River and Bellamy River | 1:22,000 |
| US5PSMBC | Rye Harbor and Foss Ledges | 1:22,000 |

### Configured chart directories
- `ENC/US_ME` — Maine ENCs
- `RNC/US_ME` — Maine raster charts
- `ENC/US_REGION02` — Region 2 ENCs
- `GSHHG` — Coastline data
- `MBTiles` — Satellite overlays (added May 2026)
- `ENC/US_NH` — NH ENCs (downloaded May 2026)

---

## Chart Blending Limitation

**OpenCPN 5.12.4 does not support true satellite + ENC blending.**

JPG MBTiles tiles are opaque — they cover any chart rendered beneath them. OpenCPN has
no transparency slider for chart layers (checked Options > Display > General and Advanced).

Workaround: use satellite view for visual landmark identification and bearing measurement;
switch to ENC view when you need to identify nav aids (buoys, lights, hazards).

---

## Magnetic Bearings for Compass Calibration

### Setting
**Options > Ships > Use magnetic bearings** — set to Magnetic.

OpenCPN uses the built-in World Magnetic Model (WMM) to apply local variation automatically.

### Portsmouth NH magnetic variation (2026)
**~14.5° West** — magnetic north is 14.5° west of true north.

If using true bearings manually: subtract 14.5° from true bearing to get magnetic.

### Calibration workflow
1. Drop a waypoint at your standing position (right-click on chart > New Waypoint)
2. Switch to satellite view — zoom in to identify a fixed visible landmark
   (building corner, pier end, water tower)
3. Right-click the landmark > Measure bearing to your waypoint
4. With magnetic bearings enabled, the displayed bearing is what your compass should read
5. Take a bearing to the same landmark with the hand compass
6. Difference = compass error/deviation
7. Repeat with 2–3 landmarks at different bearings to build a deviation table

### Good landmarks for Portsmouth
- Pier ends and wharf corners visible on satellite
- Water tower (visible from many positions)
- Fixed nav aids (cross-reference with ENC view to identify)
