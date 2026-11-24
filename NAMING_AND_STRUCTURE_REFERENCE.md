# NAMING AND STRUCTURE REFERENCE
## The Complete System — Beginning to End

**POF 2828 · November 24, 2026 · Working Draft**
**Example series: God IS (G-IS) · Example paper: God as Root (G-IS.01.ROOT)**

This document explains every naming convention, every folder piece, every link, and every classification code used in the Theophysics corpus. It is the single reference all AIs and David use. When this document and any other document disagree, raise it — don't guess which wins.

**Source documents feeding this reference:**
- CHAPEL — Ten Questions, One Record (index.html, Nov 22, 2026)
- MASTER_CLASSIFICATION_SHEET.xlsx (SYNTHESIS, COLLECTIONS, SERIES_REGISTRY, PAPER_REGISTRY, Ten Fields, Types, 21 Master Namer, README sheets)
- The God IS folder on disk: `\\192.168.2.50\h_hp\Obsidian\Axiom\GOD IS\`

---

## Series-specific folder rules

[Math Is Moral folder structure rules](MIM_FOLDER_STRUCTURE_RULES.md) govern the MIM folder pass. For MIM, use that document's Frontside, Backside, depth, and intra-folder numbering rules. The earlier God IS layout in sections 4 and 4b below retains its original context. It is not the MIM migration target.

[Contributor credit and first entries](CONTRIBUTOR_CREDIT.md) defines how meaningful contributions and first crew entries are recorded.

## 1. THE PUNCTUATION GRAMMAR

Four symbols. Each means one thing. No exceptions.

| Symbol | Meaning | Example | Windows-safe? |
|--------|---------|---------|---------------|
| `.` (dot) | Structural level separator | `G-IS.01.ROOT` = series.position.slug | ✅ |
| `-` (hyphen) | God / Jesus / divine subject marker in COMPRESSED codes; plain separator in sequential numbering | `G-IS` = "God Is"; `ISO-001` = just a separator | ✅ |
| `_` (underscore) | Word separator within a level (non-theological) | `MATH_MORAL`, `GOD_AS_ROOT` | ✅ |
| `__` (double underscore) | "Belongs to" / child-of link | `G-IS.01.ROOT__API.261124` | ✅ |

**What does NOT work:** `::` (colon-colon) fails in Windows filenames. Tested and confirmed Nov 24, 2026. Use `__` everywhere — files, links, display. One symbol, no translation layer.

**Reading the punctuation:**
- `G-IS.01.ROOT` → "God Is, paper 1, slug ROOT"
- `G-IS.01.ROOT__RD` → "Research Dossier belonging to God as Root"
- `G-IS.01.ROOT__API.261124.CLS-001` → "API run on Nov 24, 2026, Claims station, run 001, belonging to God as Root"
- `MIM.06.ACTS__ORB` → "ORBITS analysis belonging to Operations Are Acts"

**Rules:**
1. The hyphen `-` in a COMPRESSED series code (where 1-2 letters stand for a longer word) signals a theological/divine subject. `G-IS` = God Is. If Jesus were the explicit subject: `J-` prefix. Non-theological series use underscores: `MATH_MORAL` or abbreviations: `MIM`. **Exception:** when a code already has three digits (like `ISO-001`), the hyphen is just a separator between the prefix and the number — no compression, no theological meaning. The rule is: hyphens carry meaning in compressed codes (1-2 letters representing longer words); they're just separators in three-digit sequential numbering.
2. The dot `.` ONLY separates structural levels. Never inside a slug, never inside a station code.
3. The underscore `_` separates words within a single level. `GOD_AS_ROOT` is one slug. `CLAIMS_AND_EVIDENCE` is one folder name.
4. The double underscore `__` ALWAYS means "this thing belongs to that thing." It's the child-of operator. Everything after `__` is a child record of everything before it.

---

## 2. SERIES NAMING

A series is a set of papers making one argument. Every series gets:

### 2a. The full name
The human-readable title. This is the top-level folder name.
- `GOD IS`
- `Math Is Moral`
- `Be Glad That You're a Loser` (hypothetical)

### 2b. The short code
A 2-4 letter abbreviation derived from the full name. This becomes the clickable link everywhere in the corpus.

| Full Name | Short Code | Rule Applied |
|-----------|-----------|--------------|
| God Is | G-IS | Hyphen because God is the subject |
| Math Is Moral | MIM | Initials, no hyphen (not theological subject) |
| Axiom (parent collection) | AX | First two letters of single-word name |
| Logos Papers | LOGO | First four letters |
| First Principles | FPRI | First letter of each word |
| Genesis to Quantum | GTQ | First letter of each significant word |
| Duality Project | DUAL | First four letters of primary word |

**Rules for deriving short codes:**
1. 2-4 characters. Prefer 3.
2. If God or Jesus is the subject, use a hyphen: `G-IS`, `J-RES` (hypothetical Jesus series)
3. If single word, take 2-3 letters: `AX` for Axiom
4. If multi-word, take initials or a recognizable abbreviation: `MIM`, `GTQ`, `FPRI`
5. Must be unique across the entire corpus
6. Once assigned, NEVER changed. The registry issues it; nobody else mints codes.

### 2c. The series-level file naming pattern
Inside the series code, papers are numbered `01`–`99` (two digits, zero-padded). Position `00` is reserved for the series index/governing document. Position `98` or `99` is reserved for the series map.

**Full paper ID:** `SERIES.POSITION.SLUG`
- `G-IS.01.ROOT` = God Is series, paper 1, slug "ROOT"
- `MIM.06.ACTS` = Math Is Moral series, paper 6, slug "ACTS"
- `MIM.00.INDEX` = Math Is Moral series index

### 2d. Known series (from SERIES_REGISTRY and Series Families sheets)

**In registry (confirmed):**
| Code | Full Name | Status |
|------|-----------|--------|
| MIM | Math Is Moral | EXISTING_PILOT (S0042) |
| G-IS | God Is (was AX_GI) | In use, code needs formal registry entry |
| ONES | One Story | In use |
| FPRI | First Principles | In registry |
| GTQ | Genesis to Quantum | In registry |
| DUAL | Duality Project | In registry |
| LOGO | Logos Papers | In registry |
| MEQU | Master Equation | In registry |

**Proposed new:**
LAWS, INFO, DRV, APOL, ESCH, EVID

**Need crosswalk:**
- LAW vs LAWS
- ONES vs AXGI (the God IS series was originally coded AX_GI; now proposed as G-IS)

**Proposed for exclusion:**
SRC, ADMIN (these are tools/infrastructure, not content series)

---

## 3. THE PAPER ADDRESS — SERIES.POSITION.SLUG

This is the permanent identity of every paper. It never changes.

**Anatomy:**
```
G-IS.01.ROOT
│    │   │
│    │   └── SLUG: stable keyword for this paper (ROOT, TRUTH, ACTS...)
│    └────── POSITION: two-digit number (01-99), zero-padded
└─────────── SERIES: the short code from the series registry
```

**The slug** is a short, stable keyword. It is chosen when the paper is registered and never renamed. It should be recognizable — someone who knows the paper should be able to guess the slug.

**Existing God IS papers and their addresses:**

| # | Folder on disk | Paper ID | Slug |
|---|---------------|----------|------|
| 01 | 01_GOD_AS_ROOT | G-IS.01.ROOT | ROOT |
| 02 | 02_TRUTH_BEFORE_ARGUMENT | G-IS.02.TRUTH | TRUTH |
| 03 | 03_I_AM | G-IS.03.IAM | IAM |
| 04 | 04_FOUR_DEBTS | G-IS.04.DEBTS | DEBTS |
| 05 | 05_TRINITY_AND_TRUTH | G-IS.05.TRINITY | TRINITY |
| 06 | 06_LOGOS_WORD_INFORMATION | G-IS.06.LOGOS | LOGOS |
| 07 | 07_CREATION_ORDERED_GIFT | G-IS.07.GIFT | GIFT |
| 08 | 08_SCIENCE_AS_WITNESS | G-IS.08.SCIENCE | SCIENCE |
| 09 | 09_CONSCIOUSNESS_AS_WITNESS | G-IS.09.CONSCIOUS | CONSCIOUS |
| 10 | 10_FREEDOM_TRUST_SPACE | G-IS.10.FREEDOM | FREEDOM |
| 11 | 11_FALL_DAMAGED_RECEIVER | G-IS.11.FALL | FALL |
| 12 | 12_EVIL_VANDALIZES | G-IS.12.EVIL | EVIL |
| 13 | 13_COST_JUSTICE_MERCY | G-IS.13.COST | COST |
| 14 | 14_GRACE_EXTERNAL_REPAIR | G-IS.14.GRACE | GRACE |
| 15 | 15_CHRIST_ENTERS_COST | G-IS.15.CHRIST | CHRIST |
| 16 | 16_REDEMPTION_WITHOUT_ERASURE | G-IS.16.REDEEM | REDEEM |
| 17 | 17_RESURRECTION_IDENTITY | G-IS.17.RISEN | RISEN |
| 18 | 18_FRUITS_RESTORED_LIFE | G-IS.18.FRUITS | FRUITS |
| 19 | 19_FRUITS_COUNTERFEITS | G-IS.19.COUNTER | COUNTER |
| 20 | 20_SURVIVED_PRESSURE | G-IS.20.SURVIVE | SURVIVE |

**Note:** The old naming on disk uses `AX_GI_01`, `AX_GI_02`, etc. The new system uses `G-IS.01`, `G-IS.02`. The old names become aliases in the registry. Files on disk are NOT renamed (Rule 0). The index carries both forms.

---

## 4. WHAT'S INSIDE A PAPER FOLDER — THE FRONT SIDE

The front side is everything that exists BEFORE the paper goes through CHAPEL verification. This is the raw material — the research, the sources, the tangents, the media.

### Current God IS inner structure (on disk now):
```
01_GOD_AS_ROOT/
├── 00_CHAPTER_START_CODEX_20261121.md    ← chapter-level governing doc
├── 00_GUIDING_QUESTIONS.md               ← research questions for this paper
├── 01_CLAIMS_AND_EVIDENCE/               ← raw claims, sources, evidence files
├── 02_TANGENTS/                          ← related material, support threads
├── 03_MEDIA/                             ← images, audio, video links
├── AX_GI_01_IX_00_GOD_AS_ROOT.md         ← index file for this paper
├── AX_GI_01_SH_01_GOD_AS_ROOT.md         ← the paper itself (SH = short/shell)
└── media/                                ← media assets
```

### What needs to be added (the missing pieces):

Every paper folder should have all of the following. Items marked **[MISSING]** don't exist yet in God IS and need to be created as part of the folder standardization.

| Code | Name | What it is | Status in God IS |
|------|------|-----------|-----------------|
| `RD` | Research Dossier | Deep research compiled before writing | **[MISSING]** |
| `API` | API Runs folder | All automated station runs for this paper | Exists as `API_01_GOD_IS` at series level |
| `TNG` | Tangents | Related threads, side explorations | Exists as `02_TANGENTS` |
| `CLE` | Claims and Evidence | Raw claims with supporting evidence | Exists as `01_CLAIMS_AND_EVIDENCE` |
| `MED` | Media | Pictures, audio, video, diagrams | Exists as `03_MEDIA` and `media` |
| `YTS` | YouTube Scripts | Transcripts and scripts from video sources | **[MISSING]** |
| `PDF` | PDF Sources | PDF documents used as research sources | **[MISSING]** (may be inside CLE) |
| `AUD` | Audio | Audio files — sermons, interviews, dictation | **[MISSING]** (may be inside MED) |
| `VIZ` | Visualizations | Matplotlib, diagrams, generated images | **[MISSING]** |

### How front-side pieces are named:
```
G-IS.01.ROOT__RD                    ← Research Dossier for God as Root
G-IS.01.ROOT__TNG                   ← Tangents folder
G-IS.01.ROOT__CLE                   ← Claims and Evidence
G-IS.01.ROOT__MED                   ← Media folder
G-IS.01.ROOT__YTS                   ← YouTube Scripts
G-IS.01.ROOT__API                   ← API Runs folder
G-IS.01.ROOT__API.261124.CLS-001    ← Specific API run (date.station-sequence)
```

---

## 4b. INTRA-FOLDER NUMBERING — THE 00-to-999 SCHEMA

Inside every paper folder, files are numbered to show what they are and where they sit in the process. The number tells you the role at a glance. No guessing.

| Range | What lives here | Examples |
|-------|----------------|---------|
| **00–09** | Drafts in order | `00_draft_v1.md`, `01_draft_v2.md`, `02_draft_rewrite.md` |
| **10–19** | Research dossier — deep research, source compilations | `10_deep_research_gravity.md`, `11_source_compilation.md` |
| **20–29** | API call results (readable markdown from station runs) | `20_CLS_extraction_261124.md`, `21_EVD_catalog_261124.md` |
| **30–39** | YouTube evaluations, transcript analyses | `30_youtube_eval_hawking.md`, `31_transcript_analysis.md` |
| **40–49** | Outside papers, literature comparisons | `40_outside_paper_penrose.md`, `41_literature_comparison.md` |
| **50–59** | Tangents, support threads, related explorations | `50_tangent_consciousness.md`, `51_support_thread.md` |
| **60–69** | Math components, equations, derivation notes | `60_equation_derivation.md`, `61_operator_analysis.md` |
| **70–79** | Theology, scripture context, spiritual terms | `70_scripture_context.md`, `71_spiritual_terms.md` |
| **80–89** | Media references, visualization notes, audio notes | `80_media_links.md`, `81_visualization_notes.md` |
| **90–94** | Harvests — mined material from transcripts, books, chats | `90_harvest_podcast.md`, `91_harvest_book.md` |
| **95–98** | Companions — Lean companions, audit files, review packets | `95_lean_companion.md`, `96_audit_file.md` |
| *(no number)* | **THE FINAL PAPER — named, not numbered** | `GOD_AS_ROOT.md` |

**Rules:**
1. Everything with a number is PROCESS — drafts, research, API results, working material. The number tells you what kind and what order.
2. The final paper has NO number prefix. It has its NAME. That's how you know it's the final — it's the only file without a number. `GOD_AS_ROOT.md`, not `99_GOD_AS_ROOT.md`.
3. Drafts (00-09) are in chronological order.
4. The 10-89 range is the working zone — research, API results, YouTube, literature, tangents, math, theology, media. Everything flat, one folder deep max.
5. Files within a range are numbered sequentially: 20, 21, 22... not 20, 25, 30.
6. If a range fills up (more than 10 items in a 10-wide range), the extra items keep counting past the range boundary. The ranges are guidelines, not walls. The number tells you roughly what kind of thing it is.

**How this connects to the SERIES.POSITION.SLUG naming:**

Each paper folder has FOUR things at the top level. That's it. Everything else is inside DRAFTS.

```
G-IS.01.ROOT/
├── 00_NAV.md                            ← navigation / index for this paper
├── 00_AI_README.md                      ← AI record (see below)
├── DRAFTS/                              ← ALL working material (numbered inside)
│   ├── 00_draft_v1.md
│   ├── 01_draft_v2.md
│   ├── 10_deep_research_axiom_roots.md
│   ├── 20_CLS_extraction_261124.md
│   ├── 21_EVD_catalog_261124.md
│   ├── 30_youtube_eval_aquinas.md
│   ├── 50_tangent_trinity_logic.md
│   ├── 60_equation_trinitarian_sym.md
│   ├── 70_scripture_genesis_1.md
│   └── 80_media_links.md
└── GOD_AS_ROOT.md                       ← THE PAPER (named = final product)
```

**The four top-level items:**
1. **00_NAV.md** — navigation/index for this paper. Where everything is, what links where.
2. **00_AI_README.md** — the AI record for this paper. Contains:
   - How we did the folder structure for this paper
   - What we got right and wrong along the way
   - What had to move and why
   - Acknowledgements (which AIs contributed what)
   - The diff — our own record of structural decisions
3. **DRAFTS/** — ALL working material. The 00-89 numbering schema lives in here. Every draft, every research file, every API result, every YouTube eval, every tangent — all inside DRAFTS. Flat, one level, numbered.
4. **THE PAPER** — named, no number. `GOD_AS_ROOT.md`. The product. The only thing without a number.

**What goes on the front side vs back side:**
- Front side (visible in Obsidian): the four items above. Clean. You open the folder, you see the paper, the nav, the AI readme, and the DRAFTS folder.
- Back side (.BACKSIDE): raw JSON from API runs, HTML build outputs, move receipts, generated indexes. Machine-readable, not human-readable.

---

## 5. THE BACK SIDE — CHAPEL STATIONS

The back side is everything produced BY the CHAPEL verification system. These are the records that answer the ten questions.

### The Ten Questions and Their Station Codes:

| # | Question | Station | Code |
|---|----------|---------|------|
| 01 | What exactly are you saying? | Claims | CLS |
| 02 | What do your words mean? | Foundations/Definitions | DEF |
| 03 | Show me your work. | Derivations/Proof | PRF |
| 04 | Who else says so, and where? | Sources/Evidence | EVD |
| 05 | Did a machine agree with you? | Formal checks | A-L4 (Lean 4), A-Z3 (Z3) |
| 06 | Did you run it, and what happened? | Computational tests | A-PY (Python) |
| 07 | What's the best other explanation? | Alternatives/Rivals | RIV |
| 08 | What would prove you wrong? | Falsification/Failure | FAL + VER |
| 09 | What does this rest on, and what rests on it? | Dependencies/Links | LNK + ISO |
| 10 | So what did you add, and how sure are you? | Contribution/Verdict | VER |

### CHAPEL — the six letters laid over every paper:

| Letter | Name | Station | What it holds |
|--------|------|---------|--------------|
| **C** | Claims | CLS | Every claim extracted, in hypothesis form |
| **H** | Hypothesis | (carried on each claim) | Kill condition for each claim — not a room, a property |
| **A** | Analysis | A-PY, A-Z3, A-L4 | Machine checks — Python, Z3, Lean 4 |
| **P** | Proof | PRF | Derivation chains |
| **E** | Evidence | EVD | External sources and citations |
| **L** | Links | LNK | Dependencies up, down, left, right |

### The Door — FAL (Falsification):
Falsification has no letter because every chapel must pass through it. No block closes until every claim has a written kill condition.

### The Witness Stand — DEF, ISO, RIV, VER:
The stand is the judgment layer. CHAPEL is the record (what the paper says and what receipts it can produce). The stand takes the record in and produces a verdict.

### ORBITS — the strip on top of every paper:

| Letter | Name | What it names |
|--------|------|--------------|
| **O** | Operator | What is doing the acting |
| **R** | Readout | What can be measured/observed |
| **B** | Boundary | What constrains the system |
| **I** | Invariant | What cannot change |
| **T** | Transition | What moves from state to state |
| **S** | State | The configuration at a moment |

### The processing pipeline (the flow):
```
CLS → ORB → PRF · EVD · LNK → A-PY · A-Z3 · A-L4 → FAL (door) → DEF · ISO · RIV · VER → block
```

### How back-side records are named:
```
G-IS.01.ROOT__CLS              ← Claims record for God as Root
G-IS.01.ROOT__PRF              ← Proof/derivation record
G-IS.01.ROOT__EVD              ← Evidence record
G-IS.01.ROOT__A-L4             ← Lean 4 formal check
G-IS.01.ROOT__A-Z3             ← Z3 formal check
G-IS.01.ROOT__A-PY             ← Python computational test
G-IS.01.ROOT__RIV              ← Rival explanations
G-IS.01.ROOT__FAL              ← Falsification conditions
G-IS.01.ROOT__LNK              ← Dependency links
G-IS.01.ROOT__ISO              ← Isomorphism grading
G-IS.01.ROOT__DEF              ← Definitions/foundations
G-IS.01.ROOT__VER              ← Verdict/contribution
G-IS.01.ROOT__ORB              ← ORBITS analysis
G-IS.01.ROOT__BRG              ← BRIDGE layer (separate from CHAPEL)
G-IS.01.ROOT__BRG.ISO-001      ← Bridge: isomorphism case #1
G-IS.01.ROOT__BRG.PART-001     ← Bridge: partial match case #1
```

---

## 5b. THE BRIDGE LAYER — SEPARATE FROM CHAPEL

The bridge layer is NOT inside CHAPEL. It is its own folder, its own API call, its own complexity. Bridges are cross-series connections — they link claims across different papers and different series. They have their own grading system (ISO, PART, CON, ANLG, WIT) and their own case files.

**Why separate:**
- CHAPEL verifies one paper's claims. Bridges connect claims ACROSS papers and series.
- Bridge grading gets complicated — isomorphism vs analogy vs partial match vs witness. Each needs its own case.
- The bridge API call reads from EVERY paper's LNK and ISO records across the whole corpus. It's a different kind of operation.
- Bridge cases need their own revision history, their own evidence, their own dispute record.

**Folder:** `BRIDGE/` sits alongside `CHAPEL/`, not inside it.

**Bridge naming:**
```
G-IS.01.ROOT__BRG                            ← Bridge folder for God as Root
G-IS.01.ROOT__BRG.ISO_M-001                  ← Mathematical isomorphism case #1
G-IS.01.ROOT__BRG.ISO_G-001                  ← Grammatical/structural parallel case #1
G-IS.01.ROOT__BRG.ISO_E-001                  ← Empirical correlation case #1
G-IS.01.ROOT__BRG.ISO_L-001                  ← Logical equivalence case #1
G-IS.01.ROOT__BRG.ISO_N-001                  ← Noether/conservation bridge case #1
G-IS.01.ROOT__BRG.ISO_P-001                  ← Phase/state bridge case #1
G-IS.01.ROOT__BRG.WIT-001                    ← Theological witness case #1
G-IS.01.ROOT__BRG.PART-001                   ← Partial bridge case #1 (any type, didn't earn ISO)
G-IS.01.ROOT__BRG.ANLG-001                   ← Analogy case #1 (resemblance only)
G-IS.01.ROOT__BRG.API.261124-001             ← Bridge API run, Nov 24 2026, run #1
```

**The seven bridge types:**

| Code | Type | What it is | Evidence required |
|------|------|-----------|------------------|
| ISO_M | Mathematical isomorphism | Two equations share the same mathematical structure across domains | Variable-by-variable mapping, operation preservation proof, predictive test |
| ISO_G | Grammatical/structural parallel | Two systems share the same logical grammar (same operations, constraints, transformations) | Grammar spelled out as typed operations, step-by-step mapping, identified breaks |
| ISO_E | Empirical correlation | Measured quantities correlate across domains beyond chance | Measurement protocol, statistical analysis (sigma), confound identification |
| ISO_L | Logical equivalence | Two propositions from different domains are logically equivalent | Formal derivation, shared axiom identification, mutual entailment proof |
| ISO_N | Noether/conservation bridge | A symmetry in one domain corresponds to a conserved quantity in another via Noether | Symmetry identification, Noether derivation, conservation law verification |
| ISO_P | Phase/state bridge | A phase transition in one domain corresponds to one in another — same critical behavior | Order parameter mapping, universality class check, critical point correspondence |
| WIT | Theological witness | Independent arrival at the same conclusion from different starting points | Independence demonstration, convergence point specification, no shared derivation path |

**The five grades:**

| Grade | Meaning | Default? |
|-------|---------|----------|
| ISO | Full structural isomorphism — formal proof that mapping preserves operations and is predictive | Earned, never assumed |
| PART | Partial match — mapping holds for some operations, breaks identified | — |
| CON | Consilience — two independent domains converge on the same structure without coordination | Requires verified independence |
| ANLG | Analogy — resemblance but not operation-preserving | **DEFAULT** — every bridge starts here |
| WIT | Independent witness — two paths, same conclusion, no shared premises | Requires independence proof |

**Grading rules:**
1. Default is ANLG until proven otherwise
2. ISO requires formal proof or derivation — "looks like the same equation" is PART at best
3. PART requires naming exactly where the mapping breaks
4. WIT requires demonstration that the derivation paths are independent
5. Bridges can be DOWNGRADED but never UPGRADED without new evidence
6. Grade is per-bridge, not per-paper

**Exhaustive naming — the bridge API call should be run on EVERY claim, even when the bridge seems unlikely.** The cost of running it is negligible (pennies, seconds). The cost of missing a bridge is a connection the framework never makes. Err on the side of too many bridges graded ANLG rather than too few graded ISO.

**API runs for bridges live in the API folder in Obsidian** alongside all other API runs. The bridge record (the case file with the mapping, grades, and evidence) lives in BRIDGE/. The API receipt (the run log) lives in API/.

---

## 5c. THE HTML OUTPUT MARKER — `-H`

Every CHAPEL station and the bridge layer can produce an HTML output — a page (or section of a page) that gets referenced on faiththruphysics.com.

The `-H` suffix marks "this station has an HTML representation."

```
CLS-H     ← Claims page (HTML)
DEF-H     ← Definitions page (HTML)
PRF-H     ← Proofs page (HTML)
EVD-H     ← Evidence page (HTML)
FAL-H     ← Falsification page (HTML)
A-L4-H    ← Lean results page (HTML)
A-PY-H    ← Python results page (HTML)
A-Z3-H    ← Z3 results page (HTML)
LNK-H     ← Dependencies page (HTML)
ISO-H     ← Isomorphism grading page (HTML)
VER-H     ← Verdict page (HTML)
ORB-H     ← ORBITS page (HTML)
RIV-H     ← Rival explanations page (HTML)
BRG-H     ← Bridge layer page (HTML — separate from ISO inside CHAPEL)
```

The `-H` tells the build system: generate an HTML page for this station's records. Each page is either standalone or a section on a combined paper page. The site references these pages by their standard name: `G-IS.01.ROOT__CLS-H.html`.

---

## 6. API RUN NAMING

API runs are automated station executions. They produce receipts. Every run gets a unique name.

**Pattern:** `PAPER_ID__API.YYMMDD.STATION-SEQ`

**Examples:**
```
G-IS.01.ROOT__API.261124.CLS-001    ← Claims extraction, Nov 24 2026, first run
G-IS.01.ROOT__API.261124.CLS-002    ← Claims extraction, Nov 24 2026, second run
G-IS.01.ROOT__API.261124.PRF-001    ← Proof check, same date
G-IS.01.ROOT__API.261201.EVD-001    ← Evidence check, Dec 1
```

**Rules:**
1. Date is YYMMDD (six digits, no separators within)
2. Station code matches the CHAPEL station (CLS, PRF, EVD, A-L4, A-Z3, A-PY, RIV, FAL, LNK, ISO, DEF, VER, ORB) OR the bridge layer (BRG, with bridge type suffix: BRG.ISO_M, BRG.ISO_G, BRG.WIT, etc.)
3. Sequence is a three-digit counter starting at 001 — increments if you run the same station on the same paper on the same day
4. The full run ID is the receipt's permanent identity. It is never reissued.
5. When you run all stations on one paper in one pass, they all get the same date, different station codes

**The API folder for a series sits at the series level:**
```
GOD IS/
├── API_01_GOD_IS/              ← all API runs for the God IS series
│   ├── G-IS.01.ROOT__API.261124.CLS-001.json
│   ├── G-IS.01.ROOT__API.261124.PRF-001.json
│   └── ...
```

**Where API runs live:** All API runs live in the API folder inside the series folder in Obsidian. This is the same folder for CHAPEL station runs AND bridge runs. The station code in the filename tells you which kind of run it was. Bridge API runs use `BRG` as the station code with the bridge type as a suffix:
```
G-IS.01.ROOT__API.261124.BRG.ISO_M-001.json   ← Bridge run, mathematical isomorphism
G-IS.01.ROOT__API.261124.BRG.WIT-001.json      ← Bridge run, witness check
G-IS.01.ROOT__API.261124.BRG-001.json           ← Bridge run, all types (exhaustive)
```

**Exhaustive by default:** The bridge API call runs on EVERY claim in a paper, checking EVERY bridge type. The cost is negligible. The bridge record (case file with mapping and grades) goes to BRIDGE/. The API receipt (run log) goes to API/. Both are linked by the run ID.

**Open ruling (R1):** The exact literal form of the date/run syntax has three candidates. This document uses `YYMMDD.STATION-SEQ`. The older forms `YYYY.api.MM_DD` and `YYMMDD` are historical. One form needs to win and the others become display aliases.

---

## 7. THE 21 WORKSPACE ROLES

Every paper folder can hold up to 21 subfolders, one per workspace role. Folders are created ONLY when something goes in them (they are logical, not pre-stamped).

These are WORKSPACE roles — what job a record is doing inside a series. They are NOT the content roles (claim, evidence, bridge, objection, proof, open_question), which describe what a passage asserts. A record has workspace roles AND a content role mix.

| # | Code | Full Name | Folder Label |
|---|------|-----------|-------------|
| 1 | INB | Inbox | INB_Inbox |
| 2 | REV | AI Crew and Review | REV_AI_Crew_and_Review |
| 3 | STR | Structure and Navigation | STR_Structure_and_Navigation |
| 4 | CAN | Canonical Selection | CAN_Canonical_Selection |
| 5 | SYN | Paradigm and Synthesis | SYN_Paradigm_and_Synthesis |
| 6 | CAS | The Case | CAS_The_Case |
| 7 | HIS | Intellectual History | HIS_Intellectual_History |
| 8 | MTH | Mathematics and Operators | MTH_Mathematics_and_Operators |
| 9 | THE | Theology and Scripture Context | THE_Theology_and_Scripture_Context |
| 10 | TRM | Terms and Definitions | TRM_Terms_and_Definitions |
| 11 | RES | Research and Sources | RES_Research_and_Sources |
| 12 | WRT | Writing and Editions | WRT_Writing_and_Editions |
| 13 | RDR | Reader Versions and Responses | RDR_Reader_Versions_and_Responses |
| 14 | STQ | Stories and Quotations | STQ_Stories_and_Quotations |
| 15 | ORB | ORBITS Analysis | ORB_ORBITS_Analysis |
| 16 | MED | Media and Assets | MED_Media_and_Assets |
| 17 | RCP | Runs and Verification Receipts | RCP_Runs_and_Verification_Receipts |
| 18 | PAU | Private Audit | PAU_Private_Audit |
| 19 | PUB | Publication and Export | PUB_Publication_and_Export |
| 20 | GAP | Gaps and Next Checks | GAP_Gaps_and_Next_Checks |
| 21 | SUP | Superseded Editions | SUP_Superseded_Editions |

**Open rulings against this table:**
- R5: physical display numbering unsigned (# column is view order only)
- TRM/STQ merger still open
- Parent-layer names RIGOR and APPARATUS unchosen

---

## 7b. THE .TEMPLATES FOLDER — REUSABLE ASSETS AND AUDIT TRAIL

All templates live in one place: inside the existing `.APICALLS` folder. The API calls already live there. The templates that define those calls, the bridge defaults, the mind maps, the reference docs — all right next to the calls they serve.

**Location:** `\\192.168.2.50\h_hp\Obsidian\.APICALLS\.Templates\`

No separate templates folder in any series or paper folder. Everything references this one location.

**What goes in here:**

### Generation templates (the Python script reads from these to stamp out new paper folders):
- The standard paper folder template (00_NAV.md, 00_AI_README.md, DRAFTS/, .BACKSIDE/)
- The 21-slot series folder template
- CHAPEL station templates (YAML record shapes from the CHAPEL index.html)
- BRIDGE case file template
- CANON record template
- ORBITS strip template
- API run receipt template

### Mind maps and knowledge graphs (how the corpus connects — reusable reference):
- Kimi's nine mind map HTMLs (from MINDMAP-KIMI/Mind Maps/)
  - 01_One_Axiom_Engine_KIMI_Original.html
  - 02_Comparative_Worldview_Stress_Testing.html
  - 03_Theophysics_Axiom_Node_Graph_188.html
  - 04_Theophysics_Knowledge_Graph.html
  - 05_The_Spine_Map.html
  - 06_One_Axiom_Engine_Corpus_Version.html
  - 07_Worldview_Dependency_Engine.html
  - 08_Theophysics_Atlas_Atom_Story_View.html
  - 09_Trinity_Truth_Foundation.html
- The Master Dual Rail Rosetta (Theophysics_Master_Dual_Rail_Rosetta.html)
- The One Story Master Mindmap (THE_ONE_STORY_MASTER_MINDMAP.html)

### Registers and crosswalks (how the vocabulary was built — audit evidence):
- THEOPHYSICS_SPIRITUAL_TERMS_REGISTER.md — 625 terms, D0/D1/D2 and M0/M1/M2 status (from Codex Nov 9)
- THEOPHYSICS_CORE_OPERATOR_MAP.md — ORBITS fields mapped to grace operations (from Codex Nov 9)
- THEOPHYSICS_LOGICAL_ROLE_AND_DEPENDENCY_MAP.md — 101 terms classified by logical role with Mermaid spine (from Codex Nov 9)
- ORBITS_ACTION_VOCABULARY_AND_XSTATE_CROSSWALK.md — 821 IDs classified with XState mapping (from Codex Nov 9)
- THEOPHYSICS_AXIOM_AND_PROOF_GAP_REGISTER.md — gap tracking (from Codex Nov 9)
- THEOPHYSICS_ROOT_PREDICATE_REGISTER.md — root predicates (from Codex Nov 9)
- THEOPHYSICS_SPIRITUAL_DEPENDENCY_GRAPH.md + .json — the dependency graph (from Codex Nov 9)
- THEOPHYSICS_CROSS_DOMAIN_EXPERIMENT.md — cross-domain test design (from Codex Nov 9)

**These Codex Nov 9 files are BRIDGE DEFAULTS.** The Python bridge script reads them from `.TEMPLATES/BRIDGE/` as its first step (step 0 in the pipeline). Every bridge call starts with this existing knowledge — 101 classified terms, 72 proposed edges, 625 terms with gap status — before searching the broader corpus. The dependency map is the starting graph. The terms register is the gap map. The bridge call checks every claim against them first.

### ISO forms (the canonical bridge format — Kimi's locked HTML):
- All 37 ISO forms (iso-001 through ISO-037) from `\\192.168.2.50\h_hp\Desktop\ISO\`
- Classification framework (AAA-000 through AAA-003)

### CHAPEL HTML prototypes (Kimi's first implementations):
- C_P_E_L prototypes from `\\192.168.2.50\h_hp\Desktop\KIMI_corpus_report_2026-09-27\C_P_E_L\`
  - theophysics_atlas_unified_resolution_stack.html
  - 10_parallel_spines.html
  - atom_ledger_prototype.html
  - atom_ledger_snapshot_preview.html

### Reference documents (the governing specs):
- NAMING_AND_STRUCTURE_REFERENCE.md (this document)
- BRIDGE_API_README.md
- CANON_API_README.md
- AI_README_CHAPEL_CONSOLIDATION.md
- FOLDER_CONSOLIDATION_MAP.md
- MASTER_CLASSIFICATION_SHEET.xlsx (or a copy)

**Rules:**
1. `.TEMPLATES` is READ-ONLY for content. Scripts read from it to generate new folders. Nobody writes working material here.
2. Templates are versioned — when a template changes, the old version moves to `.TEMPLATES/HISTORY/` with a date suffix.
3. The Python generator script reads from `.TEMPLATES` and stamps out a new paper folder with all the right pieces pre-populated.
4. When someone audits the corpus, `.TEMPLATES` is the evidence of methodology — how we structured things, what vocabulary we used, what crosswalks we built.

**The generator script (to be built):**
```
python generate_paper_folder.py --series G-IS --position 21 --slug NEW_PAPER --title "New Paper Title"
```
Reads templates from `.TEMPLATES/`, creates the folder with 00_NAV.md, 00_AI_README.md, DRAFTS/, .BACKSIDE/ all pre-populated with the right headers and YAML shapes. Every new paper folder comes out identical.

---

## 8. THE TEN FIELDS

Every record in the corpus carries up to ten fields. These are the metadata — the labels that make querying possible.

| # | Field | Question | Level | Values From | Required |
|---|-------|----------|-------|-------------|----------|
| 1 | id | What is this, permanently? | file | SERIES.POSITION.SLUG | yes |
| 2 | series | Which collection? | file | Series Registry codes | yes |
| 3 | type | What kind of object? | file | Types list | yes |
| 4 | role_mix | What jobs do its parts do? | file = proportions; paragraph = one role | Roles list | papers: yes |
| 5 | argument | How does it argue? | file/paragraph | Arguments list | claims: yes |
| 6 | truth | How strongly is its central claim held? | file/claim | Truth list | claims: yes |
| 7 | verification | What has actually checked it? | file/claim | Verification list (multi-select) | yes |
| 8 | canon | Where in the canon process? | file | Canon list | yes |
| 9 | subjects | What is it about? | file | Lexicon master (closed vocabulary) | yes |
| 10 | laws | Which of the Ten Laws? | file | 1-10 (multi-select) | if any |

---

## 9. TYPES — What Kind of Object

Every record gets exactly one type.

| Type | Definition | Typical Positions | Notes |
|------|-----------|-------------------|-------|
| paper | Complete argued piece | 01-79 | Has role_mix, argument, truth |
| chapter | Section of a book-length work | 01-79 | Belongs to a book series |
| axiom | Foundational posited claim | 01-79 | truth usually 'posited' |
| lean | Machine-checked formal file | 80-89 | verification must name kernel + hash |
| story | Narrative/declaration-register piece | 01-79 | Body unhedged; audit in sidecar |
| canon | Canon sheet / ratified statement | 00 or 98 | Only canon='canon' items |
| audit | Closing audit: held/broke/overstated | 80-89 | Private by default |
| harvest | Mined material from transcripts/books | 90-94 | Source-cited; never canon on its own |
| prompt | Station prompt, build prompt, handoff | 98 | Versioned; ties to API runs |
| index | Series index, map, TOC | 00 | Navigation only |
| note | Working note, fragment | — | Temporary: must be retyped before review |

---

## 10. ID CLASSES

Specialized permanent ID allocations beyond the standard SERIES.POSITION.SLUG:

| Class | Pattern | Purpose | Status |
|-------|---------|---------|--------|
| M#### | M0001, M0002... | Core equations | Active — one permanent ID per equation |
| L#### | L0001, L0002... | Lean artifacts | Parked — reserved, do not issue yet |

**Core Equations registered:**
- M0001: Master Equation χ
- M0002: Lowe Coherence Lagrangian
- M0003: Grace function
- M0004: Coherence coupling
- M0005: Shannon base layer

Each equation is owned by MEQU series. Revisions keep the ID and add a version record.

---

## 11. THE CHILD-OF LINK — HOW EVERYTHING CONNECTS

The `__` (double underscore) is the child-of operator. It says "this record belongs to that record."

### Complete naming tree for one paper:
```
G-IS                                    ← the series
G-IS.01.ROOT                            ← the paper
G-IS.01.ROOT__RD                        ← research dossier
G-IS.01.ROOT__TNG                       ← tangents
G-IS.01.ROOT__CLE                       ← claims and evidence (front side)
G-IS.01.ROOT__MED                       ← media
G-IS.01.ROOT__YTS                       ← YouTube scripts
G-IS.01.ROOT__VIZ                       ← visualizations
G-IS.01.ROOT__CLS                       ← CHAPEL: claims (back side)
G-IS.01.ROOT__PRF                       ← CHAPEL: proof
G-IS.01.ROOT__EVD                       ← CHAPEL: evidence
G-IS.01.ROOT__A-L4                      ← CHAPEL: Lean 4 check
G-IS.01.ROOT__A-Z3                      ← CHAPEL: Z3 check
G-IS.01.ROOT__A-PY                      ← CHAPEL: Python check
G-IS.01.ROOT__RIV                       ← CHAPEL: rival explanations
G-IS.01.ROOT__FAL                       ← CHAPEL: falsification
G-IS.01.ROOT__LNK                       ← CHAPEL: links/dependencies
G-IS.01.ROOT__ISO                       ← CHAPEL: isomorphism grading
G-IS.01.ROOT__DEF                       ← CHAPEL: definitions
G-IS.01.ROOT__VER                       ← CHAPEL: verdict
G-IS.01.ROOT__ORB                       ← ORBITS strip
G-IS.01.ROOT__API.261124.CLS-001        ← API run: claims, Nov 24, run 1
G-IS.01.ROOT__API.261124.PRF-001        ← API run: proof, Nov 24, run 1
```

### The four directions (from the Linked Record System):
Every record has four directions of travel:

| Direction | Meaning | Example for G-IS.01.ROOT |
|-----------|---------|-------------------------|
| **UP** | Metadata labels about this record | series=G-IS, type=paper, truth=posited, laws=[1] |
| **DOWN** | Contents / children of this record | CLS, PRF, EVD, API runs, media files |
| **LEFT** | Where it came from / what it rests on | Axiom A0, prior papers, source documents |
| **RIGHT** | Where it goes / what rests on it | Papers 02-20 that build on Root, bridge connections |

---

## 12. THE COMBINED CLAIM — WHAT ALL OF THIS PRODUCES

A corpus becomes queryable the moment three things exist:

1. **A permanent ID** that survives moving and renaming (the SERIES.POSITION.SLUG)
2. **A labeled record** describing what the thing is and how it connects (the ten fields + the four directions)
3. **A resolver** that turns any mention of it back into its location (the index database)

Once those exist, the folder stops being the organizing principle and becomes only a default home. Every other thing anyone wants — the disciplined cross-series folder, the clickable name in a document, the mind map, the fifty saved reports — is a generated VIEW over that one layer, holding links and never copies.

**The constraint is not software.** The programs are small and most of them partly exist. The constraint is that a view can only cut on labels that are actually there, which makes disciplined labeling with honest unknowns the entire project.

---

## 13. THE INDEX — WHERE EVERYTHING LIVES

Five tables hold everything:

| Table | What it stores |
|-------|---------------|
| **records** | ID, series, slot, title, type |
| **labels** | Any number of name/value pairs per record (this is UP — open-ended, no schema migration needed for new label kinds) |
| **links** | from, to, type, grade, status, proposer, reviewer |
| **locations** | path, fingerprint, last seen |
| **recipes** | Saved report definitions (YAML) |

**Database ruling:** SQLite on the local PC with ONE writer. Move to Postgres on the NAS when several AIs write at once. NEVER run SQLite on the NAS share — its locking is unreliable over SMB.

**Three-tier labeling:** Location rules do most of it free (a file inside `01_GOD_AS_ROOT` is series G-IS, paper G-IS.01). The classifier proposes the rest. David or the crew confirm the doubtful ones and all real papers.

---

## 14. GRADES AND STATES

A model's output is always **DRAFT**. Only an authorized execution, recorded as a separate receipt, can raise it to:
- **RECEIPTED** — an authorized run confirmed it
- **FAILED** — an authorized run rejected it
- **REFUSED** — the station cannot assess it (outside scope)
- **NOT_RUN** — the station has not been executed

Per-claim states stay visible side by side. There is no averaged score. **Canon is a human ruling.** Nothing moves its own grade.

---

## 15. RULE 0 — THE GOVERNING CONSTRAINT

**No AI and no program moves, renames, or rearranges David's originals.** Moving is David's to do.

**One exception (working rule, unsigned):** An agent may move material into a Z archive whose destination was named in writing for that specific run, and only with a receipt and an undo script.

---

## 16. OPEN RULINGS

These are decisions that have not been signed. None of them block the build (corrected — an earlier draft claimed R0 blocks step 1, which was wrong).

| Ruling | What it is | What it affects |
|--------|-----------|-----------------|
| R0 | Permanent identity convention and S-ID standing | Human-facing form only; record_id is an internal UUID |
| R1 | One literal API date/run syntax | Receipt enumeration and deduplication |
| R3 | Bridge-case physical ownership | Cross-series bridge views |
| R5 | Physical display numbering | Folder ordering on disk |
| CAS granularity | One case file per paper vs one per claim | Report row granularity |
| "Slot" naming collision | (noted in SYNTHESIS sheet, details TBD) | — |

---

## 17. WHAT CAN BE INVENTED FREELY vs WHAT NEEDS A REGISTRY ENTRY

| Layer | Invent freely? | Why |
|-------|---------------|-----|
| **Label kinds** | YES | The labels table is name/value pairs. Make up a new label anytime. No schema change needed. |
| **Recipes** | YES | A recipe is a small YAML file reading from the index. Nothing destructive. |
| **ID classes** | YES, but each needs a registry entry | Cheap to add, expensive to add badly — an issued ID is permanent. |
| **Series codes** | NO — registry-issued only | Must be unique corpus-wide. |
| **Station codes** | NO — fixed vocabulary | CLS, DEF, PRF, EVD, A-L4, A-Z3, A-PY, RIV, FAL, LNK, ISO, VER, ORB |
| **Workspace role codes** | NO — registry entry required | The 21 roles are a closed vocabulary. |

---

## 18. THE PATH END TO END — ONE FILE, FROM ARRIVAL TO REPORT

| Step | What happens | Who acts |
|------|-------------|---------|
| 1. Arrives | Lands in inbox. Recorded as-is. | David drops it. |
| 2. Becomes a record | Scanner gives it an index entry: ID, fingerprint, location. | Scanner proposes; registry confirms. |
| 3. Gets labeled | Six questions answered in order. Location rules → classifier → human. | Three tiers. |
| 4. Gets linked | Four directions: UP (metadata), DOWN (contents), LEFT (source), RIGHT (dependents). | Proposed by anyone; graded on evidence. |
| 5. Index is boss | Five tables hold everything. Rescan re-finds moved files. Never guesses. | One writer. |
| 6. Look at it | Four views, all from the index, none hand-edited: down one series, across by slot, Freeplane map, clickable names. | Generated. |
| 7. Report it | A recipe says what to pull, how to group, what to show. Missing labels → unlabeled bucket. | Anyone writes recipes. |
| 8. Keep it honest | AI Crew review. Checkmark = read this version, not agreed. Issues never erased. | Crew reviews; closure authority closes. |
| 9. Publish | Edit owned Markdown, generate HTML with build manifest. Canon and publication are separate decisions. | David rules canon. |

---

## 19. MAPPING CURRENT FOLDERS TO THE NEW SYSTEM

The God IS series currently uses `AX_GI_XX` naming. Here is the translation:

| Current on disk | New paper ID | Child records use |
|----------------|-------------|-------------------|
| `AX_GI_01_SH_01_GOD_AS_ROOT.md` | `G-IS.01.ROOT` | `G-IS.01.ROOT__CLS`, etc. |
| `AX_GI_02_SH_01_TRUTH_BEFORE_ARGUMENT.md` | `G-IS.02.TRUTH` | `G-IS.02.TRUTH__CLS`, etc. |
| `API_01_GOD_IS/` | `G-IS__API/` | Individual runs: `G-IS.01.ROOT__API.YYMMDD.STN-SEQ` |

**Rule 0 applies:** nothing on disk is renamed. The old names (`AX_GI_01`) become aliases in the index. The new names (`G-IS.01.ROOT`) are the permanent IDs used in links, queries, and new records. Both resolve to the same file.

---

## 20. DECISIONS NEEDED FROM DAVID AND THE CREW

Before this document is final, these need rulings:

1. **G-IS as the series code** — confirm this replaces AX_GI as the permanent code for God Is
2. **Hyphen grammar** — confirm `-` = God/divine subject everywhere, no exceptions
3. **Underscore meaning** — is `_` purely a word separator, or does it carry additional semantic weight?
4. **Front-side folder codes** — confirm the list in §4 (RD, TNG, CLE, MED, YTS, PDF, AUD, VIZ) or modify
5. **API run date format** — confirm YYMMDD as the winner over YYYY.api.MM_DD (this is R1)
6. **The "slot" naming collision** noted in the SYNTHESIS sheet — what collides?
7. **Three-letter rule for all codes** — you said "analysis and APIs, 3 letters, so we might as well keep that." Does every code in the system become exactly 3 letters? Currently some are 2 (RD) and some are 3-4 (A-L4).

---

## 21. NEXT STEPS

1. **Other AIs review this document** and add their sections — particularly around the parts they own (Codex owns the Python generation/validation, Fable owns the HTML pages and shell integration)
2. **All open items get rulings** — particularly the punctuation grammar and front-side folder codes
3. **Build the HTML walkthrough** — using G-IS.01.ROOT as the example paper, with every element highlighted and explained
4. **Refine the actual folders** — go through the God IS series and standardize every paper folder to match this reference

---

*This is a working document. When all AIs agree it is complete and David has signed the open rulings, it becomes the governing reference for the entire corpus. The HTML site is built from this, not the other way around.*
