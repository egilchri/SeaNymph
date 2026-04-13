# SeaNymph Wiki Log

Append-only chronological record of all wiki operations.

Format: `## [YYYY-MM-DD] <operation> | <description>`

Operations: `ingest`, `query`, `lint`, `init`, `update`

---

## [2026-04-13] ingest | Dinghy cluster (7 files)

Ingested 7 AI research reports covering the Zodiac dinghy, outboard motor selection, Temo 450 electric motor, and towing procedure. Created topic page: dinghy.md. Created source page: src-dinghy.md. Updated index.md. Key findings: tow painter must be 3–5 ft (taut) to keep non-floating line out of prop; Temo 450 (11 lbs, $1,699–1,999) is best electric option for an 8-ft Zodiac; 12V on-boat charging draws 30 Ah (recoverable with solar in a day); Temo reverse is limited (brake only); Rockland Temo service contacts identified (Ocean Pursuits, Midcoast Marine Electronics, +1 207 200-5649). Two files too large to read fully.

## [2026-04-13] ingest | Anchoring cluster (5 files)

Ingested 5 AI research reports covering anchoring for the CD25D. Created topic page: anchoring.md. Created source page: src-anchoring.md. Updated index.md. Key findings: Modern scoop anchor (Rocna/Mantus/Spade, ~22 lbs) recommended as primary; Fortress FX-7 undersized for CD25D's heavy displacement — FX-11 minimum; Fortress resetting failure after 180° wind/tide shift is critical weakness (use modern scoop for overnight stays in tidal anchorages); cockpit winch retrieval via chain hook + snatch block is the no-windlass solution; never run chain on winch drum; balsa-cored deck vulnerable to chain chafe.

## [2026-04-13] ingest | AIS and Radar cluster (8 files)

Ingested 8 AI research reports covering AIS receivers, marine radar, radar reflectors, and the AIS-Catcher SDR project. Created topic pages: ais.md, radar.md. Created source page: src-ais-radar.md. Updated index.md. Key findings: Class B AIS transponder preferred over receiver for singlehanding (makes you visible to others); em-trak R300 (~$300) recommended receiver; octahedral radar reflectors are useless at heel (near-zero RCS at 15-20°); Echomax EM230 (~$300) is the only passive reflector that meets ISO 2.5 m² standard at heel — best passive choice; Raymarine Quantum Q24C recommended radar (lowest power at 17W, solid-state CHIRP, WiFi). Priority order for SeaNymph: reflector → AIS transponder → radar. One file too large to read fully (Marine Radar Future).

## [2026-04-13] ingest | Penobscot Bay cluster (12 files)

Ingested 12 AI research reports covering Penobscot Bay sailing conditions, Rockland Harbor mooring options, bay geology, seafloor topography, cruising itineraries (Rockland to Southwest Harbor), and Android navigation apps. Created topic pages: penobscot-bay.md, rockland-harbor.md, navigation-apps.md. Created source page: src-penobscot-bay.md. Updated index.md. Key findings: NOAA Chart 13302 is primary chart; Taft Guide is the authoritative cruising reference; fog is dominant hazard (radar nearly mandatory); Rockland has sticky mud bottom and predominant south/SW swell; Ocean Pursuits behind breakwater offers best protection; Knight Marine at $1,850/season includes parking/showers and is directly across from Hamilton Marine; Jericho Bay lobster pot warps especially hazardous (perpendicular tidal stream makes them horizontal). One file (Maine Sailing Itinerary) too large to read fully.

## [2026-04-13] ingest | Tiller pilot cluster (9 files)

Ingested 9 AI research reports covering Raymarine ST2000+ installation on the CD25D. Created topic pages: tiller-pilot.md, tiller-pilot-waterproofing.md. Created source page: src-tiller-pilot.md. Updated index.md. Key findings: ST1000 is underpowered for CD25D — ST2000 is correct. 589mm critical tiller-pin-to-socket dimension (verify on actual boat). Socket mounts on starboard coaming with backing plate and through-bolts. Unit is NOT waterproof — two failure modes: water ingress and broken belt. Dedicated 14 AWG 12V circuit, 3–5A fuse. Minimal battery draw (~1.5 Ah/2 hrs). Tiller pilot and wind vane are complementary tools. Two large files could not be read fully (too large).

## [2026-04-13] ingest | Electrical + Solar cluster (~35 files)

Ingested ~35 AI research reports covering DC/AC electrical system, batteries, Blue Sea 7610 ACR, Victron MPPT 75/15 solar, Renogy panel cable modification, shore power, and ELCI breaker. Created topic pages: electrical-system, batteries, battery-management, solar-system, shore-power. Created source pages: src-electrical-wiring, src-battery-research, src-blue-sea-7610, src-solar-research, src-elci-shore-power. Key note: companionway hatch is explicitly discouraged as solar mounting location; stern rail mount recommended. Renogy cable MC4 connectors must be removed for Victron screw terminals.

## [2026-04-13] ingest | Seacock cluster (7 files)

Ingested 7 AI research reports covering seacock replacement on the CD25D. Created topic pages: seacocks.md, seacock-backing-plates.md, seacock-removal-techniques.md. Created source pages: src-seacock-replacement-research.md, src-seacock-wrench-research.md, src-seacock-misc.md. Updated index.md. Key finding: galley sink drain seacock had a specifically noted spongy pad — inspect on next haul-out.

## [2026-04-13] ingest | Misc cluster (~25 files)

Ingested ~25 AI research reports covering winterizing (Yanmar 1GM10 + full boat), winter covers, mast climbing, tablet mounting, Yanmar water pump, marine insurance, Harken furler link plates, epoxy/fiberglass safety, grommet selection, anchor rode marking, and miscellaneous topics. Created 9 topic pages: winterizing.md, winter-cover.md, mast-climbing.md, tablet-mount.md, engine.md, insurance.md, furler.md, canvas-work.md, fiberglass-safety.md. Created source page: src-misc.md. Updated anchoring.md (zip tie depth marking scheme, snatch block brand recommendations), cd25d-overview.md (Alberg archive at Peabody Essex Museum). Updated index.md. Key findings: professional winterization documentation is now essential for Maine insurance claim defense (2025 hard market; freezing exclusion + seaworthy condition clause); Yanmar raw water pump positioned above ferrous oil pipe — weep hole drip is critical warning; epoxy sensitization is permanent/irreversible (OV/P100 cartridge mandatory, not dust mask); spur grommets required for all marine canvas structural applications (plain grommets fail); boom-tent with coated polyester (Top Gun) is the correct winter cover approach. Two winterizing files too large to read fully (first 100 lines each). Carl Alberg's archive (including Cape Dory blueprints) is at Peabody Essex Museum, Phillips Library (research@pem.org, 978-542-1553).

## [2026-04-13] init | Wiki created

Initial wiki structure established for Cape Dory 25D singlehanding and maintenance knowledge base. Created CLAUDE.md schema, index.md, log.md, and seed page cd25d-overview.md. Directory layout: raw/ for immutable sources, wiki/ for LLM-maintained pages.
