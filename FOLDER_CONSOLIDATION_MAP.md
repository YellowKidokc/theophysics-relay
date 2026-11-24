# FOLDER CONSOLIDATION MAP — MIM 00_MIM_SERIES
## Every folder, where it goes, what it needs

**POF 2828 · November 24, 2026**
**Rule 0: David moves. This map is the plan. Nothing moves until David approves.**

---

Use the [MIM folder structure rules](MIM_FOLDER_STRUCTURE_RULES.md) for the two-level Frontside limit and the series Backside. This map lists proposed destinations. Review category mergers, duplicated filenames, and link changes before applying them.

## TAGGING CONVENTION

Before any moves, every folder that's going somewhere gets prefixed with its destination tag so the crew can see on sight what's happening:

- `[→CHAPEL]` — merging into the CHAPEL verification folder
- `[→BRIDGE]` — merging into the BRIDGE layer folder
- `[→COMBINE]` — merging with another folder (destination named)
- `[→KEEP]` — stays as-is in the 21-slot template
- `[→21]` — maps directly to one of the 21 workspace roles
- `[→API]` — merging into the unified API folder
- `[→REVIEW]` — needs David's decision on where it goes

---

## THE COMPLETE MAP

### FOLDERS THAT BECOME CHAPEL (tag: `[→CHAPEL]`)

These are all CHAPEL verification stations scattered across separate folders. They merge into ONE `CHAPEL/` folder with station subfolders.

| Current Folder | CHAPEL Station | Contents become |
|---------------|---------------|-----------------|
| `04_HYPOTHESIS` | H (hypothesis form) | `CHAPEL/HYP/` |
| `05_EVIDENCE` | EVD | `CHAPEL/EVD/` |
| `06_FALSIFICATION` | FAL | `CHAPEL/FAL/` |
| `07_DEPENDENCIES` | LNK | `CHAPEL/LNK/` |
| `08_OBJECTIONS` | RIV (rival explanations) | `CHAPEL/RIV/` |
| `13_DEFINITIONS` | DEF | `CHAPEL/DEF/` |
| `23_CLAIMS_ATOMS` | CLS | `CHAPEL/CLS/` |
| `24_PROOFS_LEAN` | PRF + A-L4 | `CHAPEL/PRF/` and `CHAPEL/A-L4/` |

**What CHAPEL/ looks like after:**
```
CHAPEL/
├── CLS/          ← Claims (from 23_CLAIMS_ATOMS)
├── DEF/          ← Definitions (from 13_DEFINITIONS)
├── PRF/          ← Proofs (from 24_PROOFS_LEAN, derivation files)
├── EVD/          ← Evidence (from 05_EVIDENCE)
├── FAL/          ← Falsification (from 06_FALSIFICATION)
├── LNK/          ← Dependencies (from 07_DEPENDENCIES)
├── RIV/          ← Rival explanations (from 08_OBJECTIONS)
├── ISO/          ← Isomorphism grading (new — from CHAPEL station, NOT bridge)
├── VER/          ← Verdict (new)
├── A-L4/         ← Lean 4 checks (from 24_PROOFS_LEAN, Lean files)
├── A-Z3/         ← Z3 checks (new)
├── A-PY/         ← Python tests (new)
└── HYP/          ← Hypothesis forms (from 04_HYPOTHESIS)
```

**API calls needed for CHAPEL:**
- CLS: Claims extraction API — reads paper, extracts every claim in hypothesis form
- DEF: Definition extraction API — reads paper, extracts and cross-references all defined terms
- PRF: Proof chain API — reads paper, maps derivation chains
- EVD: Evidence cataloging API — reads paper, catalogs all cited evidence with source quality
- FAL: Falsification API — reads paper, generates kill condition for each claim
- LNK: Dependency mapping API — reads paper, maps UP/DOWN/LEFT/RIGHT links
- RIV: Rival explanation API — reads paper, generates strongest alternative explanation for each claim
- ISO: Isomorphism grading API — reads paper's cross-domain claims, runs the four separator tests
- VER: Verdict API — reads all other station outputs, produces per-claim verdict
- A-L4: Lean compilation API — sends claims to Lean 4, records pass/fail
- A-Z3: Z3 satisfiability API — sends logical forms to Z3, records results
- A-PY: Python numerical API — runs computational tests, records outputs

---

### FOLDERS THAT BECOME BRIDGE (tag: `[→BRIDGE]`)

| Current Folder | Contents become |
|---------------|-----------------|
| `16_BRIDGE_CLAIMS` | `BRIDGE/` (bridge claim cases) |
| `99_BRIDGE` | `BRIDGE/` (bridge grading files) |

**API call needed:** The Bridge API call (see BRIDGE_API_README.md) — seven bridge types, four grades, exhaustive by default. Reads from CHAPEL CLS/LNK/ISO, writes bridge cases to BRIDGE/, receipts to API/.

---

### FOLDERS THAT GET COMBINED (tag: `[→COMBINE]`)

Duplicates that merge into one folder each:

| Current Folders | Combined Into | 21-Slot Code |
|----------------|--------------|-------------|
| `06_API_RUNS` + `32_API_BATTERY` | `API/` | RCP (Runs and Verification Receipts) |
| `09_MEDIA` + `31_MEDIA` | `MEDIA/` | MED (Media and Assets) |
| `12_AI_REVIEW` + `33_AI_REVIEW` + `_AI_REVIEW_PACKETS` | `REVIEW/` | REV (AI Crew and Review) |
| `11_STORY_QUOTE_LIBRARY` + `30_STORIES_QUOTES` | `STORIES/` | STQ (Stories and Quotations) |
| `05_AUDIT_PRIVATE` + `35_PRIVATE_AUDIT` | `PAU/` | PAU (Private Audit) |

---

### FOLDERS THAT MAP TO 21-SLOT ROLES (tag: `[→21]`)

These already correspond to a workspace role and just need the standard name:

| Current Folder | 21-Slot Code | Standard Name | Notes |
|---------------|-------------|---------------|-------|
| `00_INBOX` | INB | INB_Inbox | ✅ Already correct |
| `00_STRUCTURE` | STR | STR_Structure_and_Navigation | ✅ |
| `00_TEMPLATES` | STR | Part of STR (or stays as infrastructure) | Templates are structure |
| `01_CANONICAL` | CAN | CAN_Canonical_Selection | ✅ |
| `02_PARADIGM` | SYN | SYN_Paradigm_and_Synthesis | Combine with 03_SYNTHESIS |
| `02_STANDARDS` | STR | Part of STR | Standards are structure |
| `03_SERIES_MAP` | STR | Part of STR | Maps are navigation |
| `03_SYNTHESIS` | SYN | SYN_Paradigm_and_Synthesis | Combine with 02_PARADIGM |
| `04_PRECURSORS` | HIS | HIS_Intellectual_History | Precursors = intellectual history |
| `07_RECEIPTS` | RCP | RCP_Runs_and_Verification_Receipts | Merge into API/ |
| `08_ORIENTATION` | STR | Part of STR | Orientation is navigation |
| `09_EVERYDAY` | [→REVIEW] | Needs ruling — everyday what? | |
| `10_ALL_NOTEBOOKLM` | RES | RES_Research_and_Sources | NotebookLM outputs are research |
| `10_TERMS` | TRM | TRM_Terms_and_Definitions | ✅ |
| `11_ARTICLES` | WRT | WRT_Writing_and_Editions | Articles are writing |
| `12_AUDIENCE` | RDR | RDR_Reader_Versions_and_Responses | Audience = reader facing |
| `14_MATH_COMPONENTS` | MTH | MTH_Mathematics_and_Operators | ✅ |
| `15_THEOLOGY` | THE | THE_Theology_and_Scripture_Context | ✅ |
| `17_SCRIPTURE` | THE | Part of THE (theology includes scripture) | Or keep separate — ruling needed |
| `18_RESEARCH_DOSSIER` | RES | RES_Research_and_Sources | ✅ |
| `19_OUTSIDE_PAPERS` | RES | Part of RES | Outside papers are research sources |
| `20_SOURCE_PASSAGES` | RES | Part of RES | Source passages are research |
| `21_LITERATURE_COMPARISON` | RES | Part of RES | Literature comparison is research |
| `22_DRAFTS` | WRT | WRT_Writing_and_Editions | Drafts are writing |
| `25_MATH_TRANSLATION` | MTH | Part of MTH (math translation layer) | ✅ |
| `26_OPERATORS` | MTH | Part of MTH (operators are math) | ✅ |
| `27_ORBITS` | ORB | ORB_ORBITS_Analysis | ✅ Stays its own folder |
| `28_SPIRITUAL_TERMS` | TRM | Part of TRM (spiritual terms are terms) | Or keep separate — ruling needed |
| `29_YOUTUBE_FAQ` | RDR | Part of RDR (YouTube FAQ is reader-facing) | Or STQ if it's story/quote content |
| `34_CREW_DECISIONS` | REV | Part of REV (crew decisions are crew work) | ✅ |
| `36_PUBLICATION` | PUB | PUB_Publication_and_Export | ✅ |
| `37_CHANGE_LOG` | STR | Part of STR (change log is structural) | Or keep separate |
| `38_GAPS` | GAP | GAP_Gaps_and_Next_Checks | ✅ |
| `39_EXPORT_PACKETS` | PUB | Part of PUB (exports are publication) | ✅ |
| `99_SUPERSEDED` | SUP | SUP_Superseded_Editions | ✅ |

---

### FOLDERS THAT NEED DAVID'S RULING (tag: `[→REVIEW]`)

| Current Folder | Question |
|---------------|----------|
| `09_EVERYDAY` | What is this? Everyday use files? Maps to which slot? |
| `17_SCRIPTURE` | Keep separate from 15_THEOLOGY, or merge into THE? |
| `28_SPIRITUAL_TERMS` | Keep separate from 10_TERMS, or merge into TRM? |
| `29_YOUTUBE_FAQ` | Is this reader-facing (RDR) or stories/quotes (STQ)? |
| `37_CHANGE_LOG` | Keep as its own folder or merge into STR? |
| `FORMAL_FOUNDATIONS_DRAFT_20261118` | Where does this go? SYN? CAN? |
| `MIM_Judgment_and_Restoration` | Where does this go? Content folder or paper? |
| `Operator Visuals` | Merge into MTH or MEDIA? |

---

### LOOSE FILES THAT NEED A HOME

| File | Suggested Destination |
|------|----------------------|
| `AI_NOTEPAD_CODEX_OPERATOR_DELTA_2026-11-18.md` | REV/ (crew work) |
| `INCARNATION_CONSTRAINT_AND_RESURRECTION_GLORIFICATION_MODEL.md` | SYN/ or a paper folder |
| `MIM_Operator_Guide.md` | MTH/ |
| `MIM_SERIES_CONNECTION_BRIEF_20261120.md` | STR/ |
| `MIM_The_Moral_Operator_and_the_Delta.md` | MTH/ |
| `OPUS46_AUDIT_42_QUESTIONS_2026-11-15.md` | PAU/ (audit) |
| `QUESTIONS.md` | STR/ or GAP/ |
| `README.md` | Stays at root (00 level) |
| `THE_THREE_EXTRA_FIELDS_2026-11-11.md` | STR/ |

---

## THE FINAL 21-SLOT TEMPLATE + CHAPEL + BRIDGE + API + ORBITS

After consolidation, every series folder looks like this:

```
00_SERIES_FOLDER/
│
├── [System files: .BACKSIDE, .data, desktop.ini, folder-icon.ico, README.md]
│
├── CHAPEL/                    ← [NEW] All verification (12 station subfolders)
├── BRIDGE/                    ← [NEW] Bridge layer (its own thing)
├── ORBITS/                    ← [KEEP] ORB_ORBITS_Analysis (27_ORBITS)
│
├── INB_Inbox/                 ← 00_INBOX
├── REV_AI_Crew_and_Review/    ← 12 + 33 + 34 + _AI_REVIEW_PACKETS combined
├── STR_Structure/             ← 00_STRUCTURE + 00_TEMPLATES + 02_STANDARDS + 03_SERIES_MAP + 08_ORIENTATION + 37_CHANGE_LOG
├── CAN_Canonical/             ← 01_CANONICAL
├── SYN_Paradigm_Synthesis/    ← 02_PARADIGM + 03_SYNTHESIS
├── CAS_The_Case/              ← [NEW if needed]
├── HIS_History/               ← 04_PRECURSORS
├── MTH_Mathematics/           ← 14_MATH_COMPONENTS + 25_MATH_TRANSLATION + 26_OPERATORS
├── THE_Theology/              ← 15_THEOLOGY + 17_SCRIPTURE (if merged)
├── TRM_Terms/                 ← 10_TERMS + 28_SPIRITUAL_TERMS (if merged)
├── RES_Research/              ← 18_RESEARCH_DOSSIER + 19_OUTSIDE_PAPERS + 20_SOURCE_PASSAGES + 21_LITERATURE_COMPARISON + 10_ALL_NOTEBOOKLM
├── WRT_Writing/               ← 11_ARTICLES + 22_DRAFTS
├── RDR_Reader/                ← 12_AUDIENCE + 29_YOUTUBE_FAQ (if reader-facing)
├── STQ_Stories_Quotes/        ← 11_STORY_QUOTE_LIBRARY + 30_STORIES_QUOTES
├── MED_Media/                 ← 09_MEDIA + 31_MEDIA
├── API/                       ← 06_API_RUNS + 07_RECEIPTS + 32_API_BATTERY (all API runs)
├── PAU_Private_Audit/         ← 05_AUDIT_PRIVATE + 35_PRIVATE_AUDIT
├── PUB_Publication/           ← 36_PUBLICATION + 39_EXPORT_PACKETS
├── GAP_Gaps/                  ← 38_GAPS
└── SUP_Superseded/            ← 99_SUPERSEDED
```

**Count:** CHAPEL + BRIDGE + ORBITS + API + 17 workspace roles = 21 named folders + 4 system folders. Open the series folder, see everything flat, no nesting beyond one level inside CHAPEL.

---

## WHAT WE DON'T HAVE YET — NEW API CALLS NEEDED

These are the API calls that don't exist and need to be built:

| API Call | What it does | Reads from | Writes to | Priority |
|----------|-------------|-----------|----------|----------|
| **CLS** Claims Extraction | Reads paper, extracts every claim in hypothesis form with kill condition | Paper markdown/HTML | CHAPEL/CLS/ | HIGH — everything starts here |
| **DEF** Definition Extraction | Reads paper, extracts all defined terms, cross-references against TRM | Paper + TRM_Terms/ | CHAPEL/DEF/ | HIGH — without definitions, nothing is grounded |
| **PRF** Proof Chain | Reads paper, maps every derivation chain step by step | Paper + existing proofs | CHAPEL/PRF/ | HIGH |
| **EVD** Evidence Catalog | Reads paper, catalogs every cited piece of evidence with source quality | Paper + RES_Research/ | CHAPEL/EVD/ | HIGH |
| **FAL** Falsification | Reads paper, generates kill condition for each claim | Paper + CHAPEL/CLS/ | CHAPEL/FAL/ | HIGH — the door, nothing closes without it |
| **LNK** Dependency Mapping | Reads paper, maps all four directions (UP/DOWN/LEFT/RIGHT) | Paper + other papers' CLS | CHAPEL/LNK/ | MEDIUM |
| **RIV** Rival Explanations | Reads each claim, generates the strongest alternative explanation | CHAPEL/CLS/ + web search | CHAPEL/RIV/ | MEDIUM |
| **ISO** Isomorphism Grading | Reads cross-domain claims, runs four separator tests (Kimi's format) | CHAPEL/CLS/ + Ten Laws table | CHAPEL/ISO/ | MEDIUM |
| **VER** Verdict | Reads all station outputs, produces per-claim verdict and overall paper verdict | All CHAPEL stations | CHAPEL/VER/ | LOW — runs last |
| **A-L4** Lean 4 Check | Sends formalized claims to Lean 4 compiler | CHAPEL/CLS/ (formal claims) | CHAPEL/A-L4/ | MEDIUM |
| **A-Z3** Z3 Check | Sends logical forms to Z3 satisfiability checker | CHAPEL/CLS/ (logical forms) | CHAPEL/A-Z3/ | MEDIUM |
| **A-PY** Python Test | Runs computational/numerical tests on claims | CHAPEL/CLS/ (testable claims) | CHAPEL/A-PY/ | MEDIUM |
| **BRG** Bridge | The full bridge API call — seven types, four grades, exhaustive | CHAPEL/CLS/ + LNK/ + ISO/ | BRIDGE/ | HIGH — this is the cross-domain connection |
| **ORB** ORBITS | Reads paper, identifies Operator/Readout/Boundary/Invariant/Transition/State | Paper | ORBITS/ | MEDIUM |
| **AGG** Aggregation | Runs recipes across all papers — by domain, by law, by grade, by type | All bridge records + all CHAPEL records | Generated reports (HTML) | LOW — runs after everything else |

**Build order:**
1. CLS (claims) — everything depends on this
2. DEF (definitions) — grounds the vocabulary
3. FAL (falsification) — the door, nothing closes without it
4. EVD (evidence) — what supports each claim
5. PRF (proof) — derivation chains
6. BRG (bridge) — the cross-domain connections
7. LNK (dependencies) — the four-direction map
8. ORB (ORBITS) — the strip
9. RIV (rivals) — strongest alternatives
10. ISO (isomorphism grading) — four separator tests
11. A-L4, A-Z3, A-PY (formal/computational) — machine checks
12. VER (verdict) — runs last, reads everything else
13. AGG (aggregation) — recipes and reports

---

## WHAT EACH AI DOES

| AI | Assignment |
|----|-----------|
| **David** | Approves this map. Makes the folder moves. Rules on the [→REVIEW] items. |
| **Opus (Claude)** | Wrote this map, the naming reference, and the bridge API spec. Builds AGG recipes. Audits everything. |
| **Codex** | Builds the Python scripts for each API call. Owns the CHAPEL validator contracts. |
| **Kimi** | Owns the ISO HTML format (LOCKED). Reviews bridge grading. Builds new ISO forms. |
| **Fable** | Owns the CHAPEL HTML pages and shell integration. Builds the walkthrough site. |
| **GPT/Gemini** | Review the consolidation map. Run the bridge call on test papers. |

---

*Nothing moves until David approves. The tags go on the folders first so everyone can see the plan on disk. Then David moves. Then we build the API calls in order.*
