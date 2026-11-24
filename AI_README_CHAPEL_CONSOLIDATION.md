# AI README — CHAPEL Folder Consolidation
## What we're doing, how to do it, and what already exists

**POF 2828 · November 24, 2026**
**Status: PROPOSAL — all AIs review and agree before any moves**

---

## 1. THE PROBLEM

The MIM series folder (`\\192.168.2.50\h_hp\Obsidian\MIM\00_MIM_SERIES`) currently has ~45 folders. Many of them are CHAPEL verification stations scattered across separate numbered folders:

- `04_HYPOTHESIS` — this is H (hypothesis form on each claim)
- `05_EVIDENCE` — this is EVD
- `06_FALSIFICATION` — this is FAL
- `07_DEPENDENCIES` — this is LNK
- `13_DEFINITIONS` — this is DEF
- `16_BRIDGE_CLAIMS` — this is ISO/BRG (now its own layer)
- `23_CLAIMS_ATOMS` — this is CLS
- `24_PROOFS_LEAN` — this is PRF + A-L4
- `99_BRIDGE` — this is BRG

Plus duplicates:
- `09_MEDIA` and `31_MEDIA`
- `12_AI_REVIEW` and `33_AI_REVIEW`
- `06_API_RUNS` and `32_API_BATTERY`

David's ruling: **combine all CHAPEL-related folders into ONE folder called CHAPEL.** No folders inside folders inside folders. Two levels max. Open the series folder, see everything flat.

---

## 2. WHAT ALREADY EXISTS — KIMI'S HTML PROTOTYPES

These are the first implementations of CHAPEL on HTML, built by Kimi (Sep 27, 2026). They live at:

```
\\192.168.2.50\h_hp\Desktop\KIMI_corpus_report_2026-09-27\C_P_E_L\
```

### File inventory:

| File | What it is | What it covers | Status |
|------|-----------|---------------|--------|
| `theophysics_atlas_unified_resolution_stack.html` | Multi-resolution viewer | Global → Series → Paper → Atom navigation with 15-field identity band, resolution switching, breadcrumb navigation | Prototype — shows the navigation model |
| `10_parallel_spines.html` | Comparative worldview stress-testing engine | Claims organized by type (primitive, presupposition, definition, empirical, model, theorem, bridge) across parallel spines. Kill conditions visible. Remove/collapse individual claims. | Prototype — shows verification/comparison |
| `atom_ledger_prototype.html` | Consilience Atlas atom ledger | Individual claim atoms with full metadata (identity, domains, type, family, function, source, commitment, standing, dispute, evidence grade, usage runs, graph degree, alerts) | Prototype — shows claim-level data |
| `atom_ledger_snapshot_preview.html` | Ledger snapshot preview | Preview rendering of the atom ledger | Companion to prototype |
| `atom_ledger_snapshot_checks.json` | Validation checks | JSON test results for the ledger snapshot | QA data |
| `atom_ledger_snapshot_desktop.png` | Desktop screenshot | Visual reference for the ledger | Reference |
| `atom_ledger_snapshot_mobile.png` | Mobile screenshot | Visual reference for mobile layout | Reference |

### What we need from these:

1. **The resolution stack** (atlas) is the navigation model for the whole site. Global → Series → Paper → Atom is exactly the down-one-series / across-every-series view the linked record system describes. This needs to be carried forward into the final HTML.

2. **The parallel spines** show how claims from different worldviews/papers sit side by side. This is the CHAPEL verification view — claims with their kill conditions visible. The claim type taxonomy (primitive, presupposition, definition, empirical, model, theorem, bridge) maps onto the CHAPEL station codes.

3. **The atom ledger** is the per-claim data layer. The 15-field identity (`m01_identity` through `m15_alert_state`) overlaps with but is not identical to the ten fields in the MASTER_CLASSIFICATION_SHEET. Reconciliation needed.

### What's NOT done yet:

- The prototypes use the old `C_P_E_L` naming, not CHAPEL
- No ORBITS strip integration
- No witness stand (DEF, ISO, RIV, VER) flow
- No FAL (door) gate
- No bridge layer (now separate from CHAPEL)
- No `-H` output convention
- No connection to the MIM folder structure or the NAMING_AND_STRUCTURE_REFERENCE

### What needs to happen to these HTML files:

1. **Keep them as references** — they show the direction and have working code
2. **Build the new CHAPEL HTML pages** using the CHAPEL index.html (Nov 22) as the template, incorporating the good parts from Kimi's prototypes:
   - The resolution stack navigation model from the atlas
   - The claim type taxonomy from parallel spines
   - The per-claim metadata display from the atom ledger
3. **Every CHAPEL station gets a `-H` page** — either standalone or as a section on a combined paper page
4. **The bridge layer gets its own `-H` page** — `BRG-H` — separate from CHAPEL

---

## 3. THE CONSOLIDATION MAP

### What goes INTO `CHAPEL/`:

| Current folder | CHAPEL station | What moves |
|---------------|---------------|-----------|
| `04_HYPOTHESIS` | H (carried on each claim) | All hypothesis-form files |
| `05_EVIDENCE` | EVD | All evidence files |
| `06_FALSIFICATION` | FAL | All falsification/kill condition files |
| `07_DEPENDENCIES` | LNK | All dependency/link files |
| `13_DEFINITIONS` | DEF | All definition files |
| `23_CLAIMS_ATOMS` | CLS | All claim extraction files |
| `24_PROOFS_LEAN` | PRF + A-L4 | All proof and Lean files |

### What goes INTO `BRIDGE/` (its own layer):

| Current folder | What moves |
|---------------|-----------|
| `16_BRIDGE_CLAIMS` | All bridge claim files |
| `99_BRIDGE` | All bridge grading/case files |

### What gets COMBINED (duplicates):

| Current folders | Combined into |
|----------------|--------------|
| `06_API_RUNS` + `32_API_BATTERY` | `API/` |
| `09_MEDIA` + `31_MEDIA` | `MEDIA/` |
| `12_AI_REVIEW` + `33_AI_REVIEW` | `REVIEW/` |
| `11_STORY_QUOTE_LIBRARY` + `30_STORIES_QUOTES` | `STORIES/` |

### What STAYS as-is (not CHAPEL):

| Folder | Reason |
|--------|--------|
| `00_INBOX` | Inbox is intake, not verification |
| `00_STRUCTURE` / `00_TEMPLATES` | Infrastructure |
| `01_CANONICAL` | Canon selection — different from verification |
| `02_PARADIGM` / `03_SYNTHESIS` | Content, not verification |
| `08_OBJECTIONS` | Could be RIV, but keep separate for now — TBD |
| `14_MATH_COMPONENTS` | Content |
| `15_THEOLOGY` | Content |
| `17_SCRIPTURE` | Content |
| `18_RESEARCH_DOSSIER` | Front side — RD |
| `19_OUTSIDE_PAPERS` | Research sources |
| `20_SOURCE_PASSAGES` | Research sources |
| `21_LITERATURE_COMPARISON` | Research |
| `22_DRAFTS` | Writing |
| `25_MATH_TRANSLATION` | Content (MTL) |
| `26_OPERATORS` | Content |
| `27_ORBITS` | ORBITS — its own thing |
| `28_SPIRITUAL_TERMS` | Content |
| `29_YOUTUBE_FAQ` | Content |
| `34_CREW_DECISIONS` | Crew |
| `35_PRIVATE_AUDIT` | PAU |
| `36_PUBLICATION` | PUB |
| `37_CHANGE_LOG` | Log |
| `38_GAPS` | GAP |
| `39_EXPORT_PACKETS` | Export |
| `99_SUPERSEDED` | SUP |

---

## 4. THE TEMPLATE — WHAT EVERY SERIES FOLDER LOOKS LIKE AFTER

```
SERIES_FOLDER/
├── CHAPEL/                    ← ALL verification stations flat
│   ├── CLS/                   ← Claims (one subfolder OK)
│   ├── EVD/                   ← Evidence
│   ├── PRF/                   ← Proofs
│   ├── DEF/                   ← Definitions
│   ├── FAL/                   ← Falsification
│   ├── LNK/                   ← Dependencies
│   ├── ISO/                   ← Isomorphism grading
│   ├── RIV/                   ← Rival explanations
│   ├── VER/                   ← Verdict
│   ├── A-L4/                  ← Lean 4 formal checks
│   ├── A-Z3/                  ← Z3 formal checks
│   └── A-PY/                  ← Python computational tests
├── ORBITS/                    ← ORBITS analysis
├── BRIDGE/                    ← Bridge layer (its own thing)
├── API/                       ← All API runs
├── RD/                        ← Research dossier
├── MEDIA/                     ← All media
├── REVIEW/                    ← AI crew review
├── [content folders as needed]
├── PAU/                       ← Private audit
├── PUB/                       ← Publication and export
├── GAP/                       ← Gaps and next checks
├── SUP/                       ← Superseded editions
└── INBOX/                     ← Inbox
```

**Rules:**
1. Max two levels deep. CHAPEL/ contains station subfolders. That's it.
2. Every station folder contains the same type of files: records, receipts, templates
3. Every station follows the same YAML record format from the CHAPEL index.html
4. One Python script per station that talks to the relay with the same API calls
5. The `-H` marker on any station means it has an HTML output

---

## 5. THE BRIDGE API CALL — NEXT BUILD

After the folder consolidation, the next API call to build is the bridge layer. This one:

- Reads every paper's LNK and ISO records across the whole series (and eventually the whole corpus)
- Produces the cross-series bridge map
- Grades each bridge: ISO / PART / ANLG / WIT
- Generates the BRG-H page

Design happens after the folder structure is locked. This note is a placeholder.

---

## 6. WHAT EACH AI DOES NEXT

| AI | Job |
|----|-----|
| **All** | Review this document. Flag disagreements. Agree on the consolidation map before anything moves. |
| **Codex** | Owns the Python generation/validation contracts (`FINAL_VERIFICATION_CONTRACTS/02_CHAPEL_ONE_RECORD`). Confirm the station subfolders match the validator's expectations. |
| **Fable** | Owns the HTML pages and shell integration. Confirm the `-H` convention works with the current CHAPEL index.html template. |
| **Opus (Claude)** | Wrote this document and the NAMING_AND_STRUCTURE_REFERENCE. Will integrate everyone's feedback and write the final HTML walkthrough. |
| **David** | Rules on the consolidation map. Executes the actual folder moves (Rule 0). |

---

## 7. REFERENCE DOCUMENTS

- `NAMING_AND_STRUCTURE_REFERENCE.md` — the complete naming system (in theophysics-relay repo)
- `CHAPEL — Ten Questions, One Record` — the CHAPEL system spec (index.html + station pages)
- `MASTER_CLASSIFICATION_SHEET.xlsx` — the data layer (SYNTHESIS, COLLECTIONS, SERIES_REGISTRY, PAPER_REGISTRY, Ten Fields, Types, 21 Master Namer)
- Kimi's C_P_E_L prototypes — the first HTML implementations (listed in §2 above)

---

*This is a crew document. Every AI reads it. Nobody moves folders until David approves the map. Rule 0 applies: originals are David's to move.*
