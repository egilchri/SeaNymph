# SeaNymph — Cape Dory 25D Knowledge Wiki

## Purpose

This is a personal knowledge wiki for maintaining and singlehanding a Cape Dory 25D sailboat. The goal is to make Edgar more competent over time — not just to store information, but to build a synthesized, cross-referenced understanding of the boat, its systems, and the seamanship required to operate it safely and confidently alone.

You (the LLM) write and maintain the wiki. Edgar sources material, asks questions, and directs the work. You do the bookkeeping, cross-referencing, and synthesis.

---

## Directory Layout

```
SeaNymph/
├── CLAUDE.md          ← this file (schema and instructions)
├── raw/               ← immutable source documents (manuals, articles, photos, notes)
│   └── assets/        ← images referenced by raw sources
├── wiki/              ← LLM-maintained wiki pages
│   ├── index.md       ← master catalog of all wiki pages
│   └── log.md         ← append-only chronological record of operations
```

Raw sources are never modified. Wiki pages are owned by you.

---

## Wiki Categories

Organize wiki pages under these categories. Use these labels in `index.md`.

| Category | What belongs here |
|---|---|
| `boat` | Cape Dory 25D specs, history, hull characteristics, known quirks |
| `systems` | Individual boat systems: rigging, sails, engine, electrical, plumbing, steering |
| `maintenance` | Scheduled tasks, repair procedures, upgrades, parts/vendors |
| `seamanship` | Skills and techniques: anchoring, docking, heavy weather, tides, weather reading |
| `singlehanding` | Solo-specific techniques, safety gear, passage planning, self-rescue |
| `navigation` | Chart work, aids to navigation, GPS/chartplotter use, rules of the road |
| `sources` | One page per ingested source document — summary and key takeaways |
| `synthesis` | Cross-cutting analyses, comparisons, open questions, to-investigate lists |

---

## Page Format

Every wiki page should follow this structure:

```markdown
---
title: Page Title
category: <category>
tags: [tag1, tag2]
sources: [source-slug-1, source-slug-2]
updated: YYYY-MM-DD
---

# Page Title

One-sentence description of what this page covers.

## [Sections as appropriate]

...content...

## See Also

- [[Related Page 1]]
- [[Related Page 2]]
```

Use Obsidian-style `[[wikilinks]]` for internal cross-references. Wikilinks should match the filename of the target page (without `.md`).

Source pages (category: `sources`) use a slightly different format — see the Source Page Format section below.

---

## Source Page Format

When ingesting a raw source, create a page in `wiki/` named `src-<slug>.md`:

```markdown
---
title: "Source Title"
category: sources
source-type: <article | manual | video-notes | book-chapter | personal-notes>
source-date: YYYY-MM-DD (publication date, if known)
ingested: YYYY-MM-DD
tags: [tag1, tag2]
---

# Source Title

**Type:** article | manual | etc.
**Author/Origin:** ...
**URL or file:** raw/<filename> or https://...

## Summary

Two to four paragraph summary of the source's key content.

## Key Takeaways

- Bullet list of the most actionable or important facts

## Contradictions / Surprises

Note anything that contradicts existing wiki pages, or that was unexpected.

## Pages Updated

List of wiki pages updated as a result of ingesting this source.
```

---

## Operations

### Ingest

When Edgar drops a new source (file in `raw/`, URL, or pasted text) and says "ingest this":

1. Read the source fully.
2. Discuss key takeaways with Edgar briefly — confirm emphasis before writing.
3. Create a source page `wiki/src-<slug>.md`.
4. Update `wiki/index.md` with the new source page entry.
5. Update all relevant existing wiki pages — add new facts, revise outdated claims, add cross-references.
6. If a concept or system mentioned lacks its own wiki page and is important enough, create one.
7. Append an entry to `wiki/log.md`: `## [YYYY-MM-DD] ingest | Source Title`

A single ingest may touch 5–15 wiki pages. That's normal and expected.

### Query

When Edgar asks a question:

1. Read `wiki/index.md` to identify relevant pages.
2. Read those pages.
3. Synthesize an answer with citations to wiki pages (use `[[wikilink]]` format).
4. If the answer is substantial and reusable, offer to file it as a new wiki page (category: `synthesis`).
5. Append to `wiki/log.md`: `## [YYYY-MM-DD] query | Brief description of question`

### Lint

When Edgar asks for a wiki health check:

1. Scan all wiki pages.
2. Report: contradictions, stale claims, orphan pages (no inbound links), concepts without their own page, missing cross-references, obvious data gaps.
3. Suggest new sources to find or questions to investigate.
4. Append to `wiki/log.md`: `## [YYYY-MM-DD] lint | summary`

---

## Conventions

- **Filenames**: lowercase, hyphen-separated. E.g., `standing-rigging.md`, `src-cd25d-owners-manual.md`.
- **Dates**: ISO 8601 (`YYYY-MM-DD`) everywhere.
- **Cape Dory 25D specifics**: The boat is a Cape Dory 25D. When information is CD-25D-specific (vs. general sailboat knowledge), note it explicitly. The "D" variant has a diesel engine (Universal Atomic 4 or Yanmar) rather than an outboard.
- **Singlehanding emphasis**: When adding content about any system or maneuver, always note singlehanding implications — what's harder alone, what adaptations help, what safety risks exist without crew.
- **Maintenance currency**: Whenever a maintenance procedure or part is noted, include the source and date so Edgar can judge staleness.
- **Uncertainty**: If a fact is uncertain or source-dependent, note it with a `> **Note:**` blockquote rather than stating it as fact.

---

## The Boat

**Vessel:** Cape Dory 25D  
**Owner:** Edgar Gilchrist  
**Use case:** Singlehanded daysailing and coastal cruising

The Cape Dory 25D is a 25-foot fiberglass sloop designed by Carl Alberg, built by Cape Dory Yachts. Known for its full-keel, double-ended hull (canoe stern), heavy displacement, and sea-kindly motion. The "D" designation indicates diesel auxiliary. A conservative, traditional design well-suited to coastal singlehanding due to its forgiving motion and simple systems.

*This section should be updated as we learn more specific details about Edgar's boat — hull number, year, engine, current equipment, etc.*
