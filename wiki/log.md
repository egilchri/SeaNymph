# SeaNymph Wiki Log

Append-only chronological record of all wiki operations.

Format: `## [YYYY-MM-DD] <operation> | <description>`

Operations: `ingest`, `query`, `lint`, `init`, `update`

---

## [2026-06-18] ingest | SeaNymph HIN and Insurance Policy Record

Created src-seanymph-vin-insurance.md from raw/SeaNymphVinAndInsurance.md. Captured HIN (CPDY0054M82J), Foremost Insurance Classic Elite Package policy number and renewal date (2026-08-29). Added HIN to cd25d-overview.md "This Boat" section; added current policy table to insurance.md.

## [2026-05-23] update | DC wiring diagram generated

Created wiki/assets/dc-wiring-diagram.png and wiki/wiring-diagram.md. Diagram shows full DC topology: solar→MPPT→house battery, house and start batteries on ACR studs A/B, SmartShunt on house battery negative, negative bus bar. Alternator routing and DC panel connection marked as assumed/dashed. Generator script saved as generate_wiring_diagram.py.

## [2026-05-23] ingest | Blue Sea SI-ACR 7610 Official Installation Manual

Created src-blue-sea-acr-manual.md from raw/blue_sea_acr_install.pdf. Captured full wiring diagram (inboard engine configuration), terminal specs, wire sizing chart, fuse ratings, and LED status table. Corrected GND fuse rating in battery-management.md from 10–15A to 1A (official spec). PDF stored in raw/.

## [2026-05-23] ingest | Bus Bar / Positive Cable Routing Photo

Created src-busbar-wiring-photo.md from PXL_20250919_132001736.jpg. Confirms yellow = primary positive cable color throughout SeaNymph DC system. Corrected prior error in battery-management.md (yellow cables are main positive distribution, not solar-specific). Added SeaNymph-specific cable color code table to electrical-system.md.

## [2026-05-22] ingest | Battery Wiring Photos — SeaNymph As-Installed

Created src-battery-wiring-photos.md from 3 photos of the battery compartment (Sep 2025 + May 2026 label close-up). Confirmed SI-ACR 7610 is physically installed. Updated battery-management.md (planned → installed, added wiring color notes and Victron device observation). Updated batteries.md (planned → installed). Note: PXL_20250924_145114219.jpg is a tar archive, not a real image.

## [2026-05-04] query | Where to get advice on Zodiac inflatable repair

Added Inflatable Repair section to dinghy.md: PVC vs Hypalon material ID, soapy-water leak finding, valve leak (most common), PVC patch procedure (MEK prep, rounded patch, 24hr cure, cold-weather caveat), and resources (Zodiac factory kits, West Marine Rockland, Cruisers Forum, YouTube).

## [2026-05-05] update | Lint "project" items — three new pages created

Created maintenance-schedule.md (engine hour intervals from 1GM service manual, spring commissioning checklist, fall winterization summary, annual haul-out tasks, multi-year schedule). Created singlehanding-overview.md (MOB prevention, harness/tether/jackline doctrine, essential gear, watchkeeping, passage planning, reefing solo, docking/anchoring). Created safety-gear.md (USCG required gear, PFD/harness selection, tether/jacklines, EPIRB vs PLB, fire extinguisher, annual checklist). Updated index.md: maintenance added to maintenance category, singlehanding category now has two pages. Fixed stale "to be created" links in cd25d-overview.md and seacocks.md.

## [2026-05-06] update | Created opencpn.md synthesis page

Created wiki/opencpn.md (category: navigation) consolidating all OpenCPN content: chart directories, MBTiles Python script (~/tools/OpenCPN/download_mbtiles.py) with presets, downloaded files inventory, WMM and Deviation plugins, magnetic bearings setting, land-based calibration workflow. Added [[opencpn]] to See Also in navigation-apps.md and compass.md. Added to index.md.

## [2026-05-06] ingest | OpenCPN Portsmouth NH Setup — MBTiles and Compass Calibration

Ingested Edgar's OpenCPN Portsmouth NH setup notes. Replaced QGIS/QuickMapServices MBTiles workflow in navigation-apps.md with the Python script approach (zoom 18–19 vs. zoom 14 max; QGIS workflow is superseded). Updated chart directory inventory: added ENC/US_NH (catalog only, 13278 Portsmouth Harbor not yet downloaded). Added "OpenCPN Tips and Tricks" section to navigation-apps.md with land-based compass calibration workflow. Added matching land-based calibration section to compass.md. Created src-opencpn-portsmouth-setup.md. Edgar lives in Portsmouth NH; SeaNymph is in Rockland. Portsmouth NH variation 14.5°W vs. Penobscot Bay 15–16°W noted in both pages.

## [2026-05-05] update | Lint "soon" items — dinghy winterization, to-purchase additions

Added dinghy/outboard winterization section to dinghy.md (Yamaha F2.5 carb dry, flush, storage orientation, Zodiac deflate/clean/303/inspect) with checklist. Added matching checklist block to winterizing.md. Fixed winterizing.md checklist which still said "API CD 15W-40" (corrected to API CB/CC, SAE 20W or 30). Added 303 Aerospace Protectant and Zodiac PVC repair kit to to-purchase.md dinghy section.

## [2026-05-05] lint | Full wiki scan — fixes applied

Scanned all 40+ wiki pages. Fixed three critical items: (1) winterizing.md had wrong Yanmar 1GM oil spec (API CD / 15W-40) — corrected to API CB or CC / SAE 20W or 30 per official service manual; (2) todo.md closed two completed items (hull number ID, lint pass); (3) cd25d-overview.md fixed broken [[cd25d-engine]] link → [[engine]]. Remaining issues logged in lint report: dinghy winterization missing, singlehanding category empty, maintenance-schedule page needed, to-purchase missing 303 Protectant and PVC kit, safety-gear page needed.

## [2026-05-04] ingest | Zodiac CFR 240 HIN decode and material ID (raw/zodiac1.md)

AI HIN decode confirmed model (Zodiac CFR 240, not just Cadet 240), year (January 1999), and material (PVC — thermo-welded Strongan Duotex). Created src-zodiac-material.md. Updated dinghy.md: corrected model name, added HIN and year, simplified material ID section to state PVC confirmed, added sandpaper test, added UV protection guidance (303 Aerospace Protectant). Simplified repair materials section — Hypalon options removed now that PVC is confirmed.

## [2026-05-04] ingest | Yamaha F2.5 outboard specs (raw/yamaha_outboard.md)

AI research report with owner annotation confirming short shaft model (F2.5SMHB). Created src-yamaha-f25.md. Updated dinghy.md: replaced generic "2.5 HP gas outboard" description with confirmed model, full spec table, pre-storage carb-dry procedure, and storage orientation note.

## [2026-05-04] ingest | Zodiac Cadet 240 specs (raw/zodiac.md)

AI analysis of the dinghy photo reading the transom data plate. Created src-zodiac-specs.md. Updated dinghy.md: model confirmed as Zodiac Cadet 240; max engine corrected from 6–8 HP to 4 HP (plate-rated); added max load (270 kg / 595 lbs) and capacity (3 persons). AI report incorrectly identified floor as slatted — retained inflatable air deck per owner correction.

## [2026-05-04] ingest | Zodiac dinghy photo (raw/zodiac.jpg)

Photo of SeaNymph's Zodiac tender stored ashore. Created src-zodiac-photo.md. Updated dinghy.md: added physical description (white/gray tubes, gray hard transom), clarified floor type (slatted boards over soft base, not bare soft floor), added foot pump and grab handle details. Key correction: prior page implied purely soft floor; photo confirms slatted board floor requiring seasonal inspection.

## [2026-04-30] ingest | Yanmar 1GM Service Manual (SM/1GM·2GM·3GM(D)·3HM)

Ingested official Yanmar 1GM service manual (483 pages; read ~40 targeted pages). This is the correct manual for SeaNymph's engine. Created source page: src-yanmar-1gm-service-manual.md. Full rewrite of engine.md with authoritative 1GM data. Key facts: displacement 293cc, 6.5 HP continuous @ 3400rpm, oil 1.3L crankcase + 0.25L clutch (same oil, CB/CC grade), oil change every 100 hours, oil filter every 300 hours, impeller inspect every 250/replace every 500 hours, zinc every 500 hours, rubber hoses replace every 4 years. V-belt tension: 5-7mm (water pump) and 10mm (alternator) with 10kg force. KM2A clutch uses same oil as crankcase (not separate gear oil). All significantly different from prior AI-sourced data.

## [2026-04-30] ingest | Yanmar 1GM10 Operation Manual (0AGMM-EN0013, 2018)

Ingested official Yanmar 1GM10 operation manual (94 pages; read ~50 targeted pages using pdftoppm rendering). Created source page: src-yanmar-1gm10-manual.md. Major rewrite of engine.md. Key corrections to prior wiki content: (1) displacement was 232cc — correct is 318cc; (2) cooling system was "freshwater closed loop" — correct factory spec is direct seawater cooling; (3) oil spec was "API CD, 15W40 only" — correct is API CC or higher, 10W30 or 15W40 both acceptable; (4) oil capacity was ~1.3L — correct is 1.5L; (5) output was "9HP @ 3200rpm" — correct is 8hp continuous @ 3400rpm, 9.1hp max @ 3600rpm; (6) maintenance intervals corrected throughout (oil every 150hrs; impeller inspect 250hrs / replace 1000hrs or 4 years). Added: full official maintenance schedule, wiring color codes, component identification table, troubleshooting quick reference, mixing elbow replacement interval (500hrs/2yr), zinc anode guidance.

## [2026-04-30] ingest | Cape Dory 25D spec values (Gemini research)

Ingested Gemini AI-generated spec sheet (raw/CD25D_spec_values.md). Created source page: src-cd25d-gemini-specs.md. Updated cd25d-overview.md: replaced approximate hull specs with full table (LOA 25', LWL 19', beam 8', draft 3.5', displacement 5,120 lbs, ballast 2,050 lbs); added rig dimensions section (I/J/P/E and total sail area 304 sq ft, mast height ~36.5 ft); added mechanical/tankage section (13 gal fuel, 20 gal water, 10–15 gal holding, Yanmar 1GM10, 2-blade fixed prop); added performance ratios (B/D 40%, D/L 333, capsize 1.86). All values flagged as AI-generated / approximate. Contradiction noted: source says production 1981–1985; wiki had ~1975–1988 (likely includes non-diesel CD25).

## [2026-04-29] ingest | Cape Dory 25D factory brochure (BBDC23790_04_grande.jpeg)

Ingested original Cape Dory Yachts factory brochure. Created source page: src-cd25d-brochure.md. Copied image to wiki/assets/cd25d-brochure.jpeg (committed to git). Updated cd25d-overview.md: added "Sail Plan and Deck Plan" section embedding the brochure image. Key finding: sail plan visually confirms conventional transom stern — corroborates the correction made earlier today. Spec values in brochure partially difficult to read from image; approximate values already in wiki are consistent.

## [2026-04-29] ingest | Radar reflector comparison (AI research)

Ingested AI radar reflector comparison from raw/please make a table of prices and qualities of ra....md. File copied from Downloads to raw/. Created source page: src-radar-reflector-comparison.md. Updated radar.md: added tube/cylinder type (Mobri S-2/Plastimo) to comparison table; added Viking Tri-Lens as named alternative to Firdell Blipper; updated Echomaster pricing to $120–135. Key contradiction flagged: source recommends Echomaster for coastal day sailing — this is incorrect per independent heeling test data already in the wiki; existing guidance stands. No other wiki pages required updating.

## [2026-04-29] ingest | Bushnell Marine 7x50 binoculars — features and warranty

Ingested two AI research files: (1) Bushnell Marine 7x50 specs (waterproof, buoyant, illuminated compass, individual eyepiece focus, ~$305.89) and (2) Bushnell Ironclad Warranty details (20 years post-June-2020, transferable, no receipt; electronics 5 years). Created source page: src-bushnell-binoculars.md. Updated binoculars.md with full Bushnell comparison section and Steiner vs. Bushnell tradeoff table. Updated to-purchase.md (added Bushnell as budget alternative row). Key finding: Bushnell floats (sinks = bad day at $690); tradeoff is no Sports-Auto-Focus equivalent — individual eyepiece focus is a singlehanding liability. Steiner remains recommended for singlehanding; Bushnell is a defensible budget choice.

## [2026-04-28] ingest | Steiner Navigator 7x50 binoculars purchase research

Ingested AI market research on Steiner Navigator 7x50c (Model 2343). Created source page: src-steiner-binoculars.md. Created topic page: binoculars.md. Updated to-purchase.md (added row under Safety/Navigation). Key findings: 7x50 is the marine standard (7.14mm exit pupil, Sports-Auto-Focus critical for singlehanding); Model 2343 Open-Hinge preferred for one-handed grip; current low price ~$690 on Amazon (Edgar observed 2026-04-28) vs. $783.74 at Landfall Navigation or $799.99 in-stock at West Marine Portsmouth; Steiner Heritage Warranty is lifetime and fully transferable — valid on used purchases.

## [2026-04-19] ingest | Jib furler drum toggle options (Schaefer — not applicable)

Ingested AI research doc on CD25D furler drum toggle options. Research assumed Schaefer 1100/2100 series — not applicable to SeaNymph, which is confirmed Harken. Source filed for reference; no wiki pages updated. Correct Harken parts already in [[furler]].

## [2026-04-19] ingest | OpenCPN Mac satellite imagery (MBTiles workflow)

Ingested AI research doc (raw/OpenCPN Google Earth Alternatives for Mac.md) plus verified workflow reconstructed from 8 Desktop screenshots dated 2026-04-16. Created source page: src-opencpn-mac-satellite.md. Updated navigation-apps.md with new Mac/OpenCPN satellite section. Key findings: no Google Earth plugin for Mac OpenCPN; QGIS + QuickMapServices (ESRI) + Generate XYZ Tiles (MBTiles) is the working solution; zoom 8–14 reliable, zoom 16 fails (JPG transparency error); MOBAC failed due to SSL cert errors; OpenCPN ingestion via Options → Charts → Chart Files → Add Directory; Edgar's MBTiles live at ~/Documents/Charts/MBTiles/.

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

## [2026-04-14] ingest | Anchoring Advice for Maine (CCA / Babbitt)

Ingested CCA article by Tom Babbitt on anchoring in Maine. Updated anchoring.md with: circle-the-drop-site procedure, "too good to be true" and "trust your gut" warnings, lobster gear at anchor entanglement risk (including CD25D full keel wrapping in tidal reversals), rope rode failure modes (unlaying under sustained 30-knot load; all-chain "welding the pile" in offshore use), and rode marker safety context (author dragged at 1.5:1 scope due to worn markers). Created src-maine-anchoring-advice.md. Updated index.md and log.md.

## [2026-04-14] ingest | Mooring Advice and Etiquette in Maine (CCA / Babbitt)

Ingested CCA article by Tom Babbitt on Maine moorings. Created wiki/moorings.md covering mooring evaluation criteria (location, condition, size, maintenance), types (rental/guest/private), pickup procedure with hand signals, singlehanded mooring pickup techniques (tiller pilot, slow-motion sail approach, long boat hook), sailing to a mooring (1 boat length per knot coasting rule), and private mooring etiquette. Created src-mooring-advice.md. Updated index.md. Key findings: mooring failures have caused more damage than anchoring mishaps for experienced Maine cruisers; Camden Harbor requires annual inspection tags (meaningful assurance); most other Penobscot Bay harbors have no inspection requirements; never use a fisherman's mooring; always give the mooring a reverse-load tug before settling in.

## [2026-04-14] ingest | SeaNymph Compass Deviation Table (PDF)

Ingested SeaNymph's actual compass deviation table. Created wiki/compass.md with full deviation table, TVMDC correction chain, worked example for Penobscot Bay, deviation pattern analysis (max 9°E at 330° mag, 8°W at 180° mag, zero at 090°), fog navigation context, compass re-swinging guidance, and variation reference (16°W for Penobscot Bay 2025). Created src-compass-deviation.md. Updated index.md. This is primary boat data — not AI-generated.

## [2026-04-14] ingest | CCA Introduction to Cruising Maine (Rubadeau)

Ingested CCA article by R. J. Rubadeau covering the full Maine coast from Kittery to Roque Island. Created source page src-cca-intro-maine.md. Updated penobscot-bay.md with: lobster pot toggle anatomy (loop of submerged warp between toggle and main float = prop fouler), 4-knot tidal current magnitude and beam-current drift calculation, spring tide warning (water falls below chart datum), depth sounder limitation on granite ledges, "leave early/anchor by noon" practice, "focus on one area" planning rule, August-September as best sailing months, MITA (mita.org) and MCHT (mcht.org) ashore resources.

## [2026-04-13] ingest | Misc cluster (~25 files)

Ingested ~25 AI research reports covering winterizing (Yanmar 1GM10 + full boat), winter covers, mast climbing, tablet mounting, Yanmar water pump, marine insurance, Harken furler link plates, epoxy/fiberglass safety, grommet selection, anchor rode marking, and miscellaneous topics. Created 9 topic pages: winterizing.md, winter-cover.md, mast-climbing.md, tablet-mount.md, engine.md, insurance.md, furler.md, canvas-work.md, fiberglass-safety.md. Created source page: src-misc.md. Updated anchoring.md (zip tie depth marking scheme, snatch block brand recommendations), cd25d-overview.md (Alberg archive at Peabody Essex Museum). Updated index.md. Key findings: professional winterization documentation is now essential for Maine insurance claim defense (2025 hard market; freezing exclusion + seaworthy condition clause); Yanmar raw water pump positioned above ferrous oil pipe — weep hole drip is critical warning; epoxy sensitization is permanent/irreversible (OV/P100 cartridge mandatory, not dust mask); spur grommets required for all marine canvas structural applications (plain grommets fail); boom-tent with coated polyester (Top Gun) is the correct winter cover approach. Two winterizing files too large to read fully (first 100 lines each). Carl Alberg's archive (including Cape Dory blueprints) is at Peabody Essex Museum, Phillips Library (research@pem.org, 978-542-1553).

## [2026-04-15] ingest | SeaNymph Deviation Assessment (AI analysis)

Ingested AI analysis of SeaNymph's actual deviation table. Created source page: src-deviation-assessment.md. Updated compass.md with new "Status: Compensation Is Warranted" section: ISO 25862 ≤4° standard; 9° max = 810 ft/mile error; 8/12 headings exceed 5°; compensation is a current maintenance item, not a periodic one. Action items: DIY compensation attempt this season, professional adjuster if residual >5°, interference check. Updated index.md.

## [2026-04-15] ingest | Cape Dory 25D Compass Upgrade Options (AI research)

Ingested AI research report on compass replacement and compensation for the CD25D. Created source page: src-compass-upgrade.md. Updated compass.md with: CD25D magnetic environment analysis (diesel primary source, lead ballast not a contributor), DIY compensation procedure (cardinal heading 180° method; GPS COG as reference in slack tide), replacement compass options (Ritchie BN-202 4.5" CombiDial top pick; Plastimo Contest 101 for cruising versatility; BN-202 mounting hole 5.75"), hand-bearing compass options (Plastimo Iris 50 practical; Vion Mini 2000 precision), and maintenance section (UV cover, bubble diagnosis, teak chemicals hazard). Updated index.md.

## [2026-04-14] ingest | SeaNymph Chart References (Edgar's notes)

Ingested Edgar's personal chart bookmark list. Created source page: src-penobscot-charts.md. Updated penobscot-bay.md Charts section with full chart table (13302/13315/13316/13312/13321) covering the Rockland-to-MDI passage chain; added OceanGrafix and Maptech Chartbook references. Updated index.md.

## [2026-04-14] ingest | VHF Radio vs Cell Phone (CCA / Guck)

Ingested CCA article by Brian Guck on VHF vs. cell communications for Maine cruising. Created topic page: vhf.md. Created source page: src-vhf.md. Updated index.md. Key findings: USCG direct cell number is 206-815-7220 (206 area code = correct, not a typo); DSC+MMSI+GPS triggers Rescue 21 near-shore quasi-EPIRB capability; foghorns within half-mile can be activated on demand via ch. 83A + 5 mic keys; MMSI from BoatUS ($25) is simplest; Starlink Mini ($229–350 hardware, 12V-30V converter required, $50–165/month) solves data connectivity downeast. VHF advantage over cell: all nearby boats hear ch. 16; CG gets bearing in 3 seconds.

## [2026-04-14] ingest | Lobster Pot Avoidance and Extrication (CCA / Godshalk)

Ingested CCA article by Ernie Godshalk on lobster pot navigation and extrication. Created topic page: lobster-pots.md. Created source page: src-lobster-pots.md. Updated penobscot-bay.md, anchoring.md, and index.md. Key findings: pass on DOWN-current side of any buoy (warp angles upstream = danger zone); two-buoy system — NEVER go between them, submerged line between is the fouling hazard; buoy lying on its side = primary warp buoy in strong current, toggle may be submerged downstream; immediate action if fouled: don't engage prop; pull warp to cleat to ease tension; Shaft Shark is best preventive tool; Fiskars P973 pruner for cutting warp off prop; Maine water 50–60°F requires wetsuit for under-boat swim. Real story: Muscle Ridge Channel fouling, warp burned into cutlass bearing, local lobsterman diver freed it for $100.

## [2026-04-15] update | Created todo.md and to-purchase.md

Created wiki/todo.md (category: synthesis) and wiki/to-purchase.md (category: maintenance). Both seeded from existing wiki content. todo.md organizes open tasks by urgency/type with a completed section. to-purchase.md is a prioritized table with cost estimates and vendor notes, covering safety/nav, electrical, ground tackle, dinghy, autopilot, canvas, and tools. Maptech Waterproof Chartbook: Penobscot Bay added as first user-specified purchase. Updated index.md.

## [2026-04-13] init | Wiki created

Initial wiki structure established for Cape Dory 25D singlehanding and maintenance knowledge base. Created CLAUDE.md schema, index.md, log.md, and seed page cd25d-overview.md. Directory layout: raw/ for immutable sources, wiki/ for LLM-maintained pages.
