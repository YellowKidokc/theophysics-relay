# AI PLEASE READ ME — Master Excel Folder
## Read this BEFORE touching anything in this folder

**POF 2828 · November 24, 2026**
**Location:** `\\192.168.2.50\h_hp\Desktop\Folders\Folders\Master EXCEL\`

---

## RULE 1: DO NOT DUPLICATE THESE FILES

This is the single most important rule in this folder. Read it twice.

**DO NOT make a copy of an Excel file to edit it.** Edit the original. If your instrument or environment can't edit the original in place, tell David and he will open it in Excel. Do not:

- Copy `MASTER_CLASSIFICATION_SHEET.xlsx` to `MASTER_CLASSIFICATION_SHEET (1).xlsx`
- Copy `Lean 4 - CANONICAL_LEDGER_V2.xlsx` to `Lean 4 - CANONICAL_LEDGER_V2_WORKING.xlsx`
- Save a "working copy" anywhere else and forget about it
- Download it to your sandbox and upload a modified version as a new file

If you must work with a copy (because your environment literally cannot edit in place), then:
1. Name it with `_TEMP_` and today's date: `MASTER_CLASSIFICATION_SHEET_TEMP_261124.xlsx`
2. When you're done, tell David what changed
3. David merges the changes into the original
4. DELETE your temp copy immediately after merge

**If you find duplicates that already exist in this folder** (and there are many), do NOT delete them without David's approval. Flag them. The cleanup is David's job.

---

## RULE 2: THESE FILES POWER THE WHOLE SYSTEM

The Excel files in this folder are not disposable working documents. They are the data layer that the entire naming system, the CHAPEL stations, the bridge grading, the canon process, and the linked record system all read from. When you change a cell in one of these, it changes what the Python scripts produce, what the HTML pages show, and what the API calls return.

**Key files and what they govern:**

| File | What it powers | Touch carefully |
|------|---------------|----------------|
| `MASTER_CLASSIFICATION_SHEET.xlsx` | The Ten Fields, Types, Roles, Arguments, Truth levels, Verification methods, Canon states, 21 workspace roles, Series registry, Paper registry, Discrepancies | YES — this is the classification backbone |
| `Lean 4 - CANONICAL_LEDGER_V2.xlsx` | All Lean 4 formal verification records | YES — formal proof receipts |
| `lexicons_master_enhanced.xlsx` | The master semantic lexicon — all term classifications | YES — vocabulary authority |
| `Isomorphic_Updated.xlsx` | Isomorphism records — the bridge data | YES — feeds the ISO forms |
| `MASTER_EQUATION_SOURCE_OF_TRUTH.xlsx` | Master Equation variables and derivations | YES — the math backbone |
| `THEOPHYSICS_CANON_MASTER.xlsx` | Canon decisions and status | YES — what's ratified |
| `THEOPHYSICS_API_DATA_LOG.xlsx` | All API run records | YES — receipt history |

---

## RULE 3: BACKUPS ARE GOOD, DUPLICATES ARE NOT

A backup has a clear name: `filename.backup-YYYYMMDD.xlsx` or `filename.pre_[what_changed].xlsx`

A duplicate is: `filename (1).xlsx` or `filename_copy.xlsx` or `filename_WORKING.xlsx` that never got merged back.

Backups are good — they're your undo button. Duplicates are poison — they create two sources of truth and nobody knows which one is current.

**Backup naming convention:**
```
ORIGINAL.xlsx                              ← the live file
ORIGINAL.backup-20261124.xlsx              ← backup from Nov 24
ORIGINAL.pre_canon_update_20261124.xlsx    ← backup before a specific change
```

---

## RULE 4: THE NAMING SYSTEM

The complete naming system for the Theophysics corpus is documented in:
- `NAMING_AND_STRUCTURE_REFERENCE.md` — in the theophysics-relay repo on GitHub (https://github.com/YellowKidokc/theophysics-relay)
- Also located at: `\\192.168.2.50\h_hp\Obsidian\.APICALLS\.Templates\`

Read that document before creating any new files, series codes, or paper IDs. The punctuation grammar (what `.` `-` `_` `__` mean), the series codes, the paper addressing, the intra-folder numbering — it's all in there.

---

## RULE 5: KNOWN DUPLICATES IN THIS FOLDER (flagged, not yet cleaned)

These appear to be duplicates or near-duplicates. David needs to rule on which is the keeper:

| Group | Files | Question |
|-------|-------|----------|
| Master Axiom | `Master Axiom.xlsx`, `Master_Axiom.xlsx`, `Master Axiom.zip`, `Master_Axiom.backup_20260710_041459.xlsx` | Which is current? |
| Conspiracy | `Conspiracy_Database_MASTER.xlsx`, `Conspiracy_Theories_Database.xlsx` | Same data? |
| GMF Trilima | `GMF 3 the Trilima.xlsx`, `GMF 3 the Trilima (1).xlsx` | (1) is a copy |
| Master Theory Truths | `MASTER_THEORY_TRUTHS.xlsx`, `MASTER_THEORY_TRUTHS (1).xlsx` | (1) is a copy |
| MTL Consciousness | `MTL_CONSCIOUSNESS_COMBINED.xlsx`, `MTL_CONSCIOUSNESS_COMBINED (1).xlsx` | (1) is a copy |
| Claims Review | `CLAIMS_REVIEW_CANONICAL.xlsx`, `CLAIMS_REVIEW_CANONICAL_derivation_chain_v2.xlsx`, `CLAIMS_REVIEW_CANONICAL_derivation_chain_v2 (2)_ENRICHED.xlsx` | Three versions — which is current? |
| ME Workbook | `MASTER_EQUATION_1.xlsx`, `MASTER_EQUATION_WORKBOOK (3).xlsx`, `MASTER_EQUATION_SOURCE_OF_TRUTH.xlsx` | Three files, one equation |
| Lean 4 | `Lean 4 - CANONICAL_LEDGER_V2.xlsx` plus four backup variants | Backups are fine, but verify the main is current |

---

## WHAT THIS FOLDER IS

This is the data layer for the Theophysics Research Initiative. The Excel files here are the closed-vocabulary registries, the classification backbone, the verification ledgers, and the canon records that the entire system reads from. The Python scripts in `D:\GitHub\pipeline-workflows\` read from these files. The CHAPEL stations, the bridge grading, the canon process — they all trace back to what's in these spreadsheets.

Treat this folder like a database. You don't copy a database to edit it. You query it, change what needs changing, and leave one source of truth.

---

*This README was written Nov 24, 2026. If the rules above conflict with a newer ruling from David, follow David's ruling.*
