# AI README — CANON API CALL
## The Judgment Layer — After CHAPEL and BRIDGE

**POF 2828 · November 24, 2026**
**Status: SKETCH — crew review before build**

---

## 1. WHAT CANON DOES

Canon is the judgment layer. It sits AFTER CHAPEL (verification) and BRIDGE (cross-domain connections) have done their work. It aggregates everything those two produced and asks: **where does each claim stand in the canon process?**

Canon PROPOSES. David RULES. No API call moves a claim to "canon" — that's always a human ruling.

**The canon pipeline:**
```
CHAPEL stations produce per-claim records → 
BRIDGE produces cross-domain connections → 
CANON aggregates both into one verdict per claim → 
David rules: canon / open / retired
```

---

## 2. THE SIX CANON STATES

From the MASTER_CLASSIFICATION_SHEET (Canon sheet):

| State | Meaning | Who moves it here |
|-------|---------|-------------------|
| **raw** | Captured, unsorted — just arrived | Automatic (on capture) |
| **draft** | Being written — the paper is in progress | Author |
| **review** | Under audit — CHAPEL stations running, crew reviewing | CHAPEL completion triggers this |
| **candidate** | Proposed for canon — ballot pending | Canon API proposes this |
| **canon** | Ratified | David rules (human only) |
| **retired** | Withdrawn or superseded (kept, never deleted) | David or crew (append-only) |

**The key transitions:**
- `raw → draft` = someone starts writing
- `draft → review` = CHAPEL stations run on the paper
- `review → candidate` = ALL CHAPEL stations pass, BRIDGE grades are in, the Canon API assembles the case
- `candidate → canon` = David rules
- `canon → retired` = superseded by a newer version (old one stays, never deleted)
- Any state → `retired` = withdrawn (David or crew)

---

## 3. WHAT THE CANON API READS

It reads from EVERYTHING that came before:

| Source | What it provides | Why Canon needs it |
|--------|-----------------|-------------------|
| CHAPEL/CLS | All extracted claims | The list of what's being judged |
| CHAPEL/DEF | Definitions | Are the terms grounded? |
| CHAPEL/PRF | Proof chains | Is the derivation valid? |
| CHAPEL/EVD | Evidence catalog | Is the evidence sufficient? |
| CHAPEL/FAL | Kill conditions | Does every claim have one? (The door — nothing passes without this) |
| CHAPEL/LNK | Dependencies | What does it rest on? Is anything beneath it unverified? |
| CHAPEL/RIV | Rival explanations | Has the strongest alternative been addressed? |
| CHAPEL/ISO | Isomorphism grading | Do the cross-domain claims inside the paper hold? |
| CHAPEL/A-L4 | Lean results | Did the formal check pass? |
| CHAPEL/A-Z3 | Z3 results | Did the satisfiability check pass? |
| CHAPEL/A-PY | Python results | Did the computational test pass? |
| BRIDGE/ | Bridge grades | ISO / PART / ANLG / WIT — how strong are the cross-domain connections? |
| ORBITS/ | ORBITS analysis | Is the O/R/B/I/T/S strip complete? |
| Ten Fields | Current truth + verification + canon state | Where does the claim currently stand? |

---

## 4. WHAT THE CANON API WRITES

**Per-claim canon record:**
```json
{
  "claim_id": "CLS-003",
  "paper_id": "MIM.06.ACTS",
  "current_state": "review",
  "proposed_state": "candidate",
  "truth_level": "supported",
  "verification_methods": ["cross_ai", "simulation", "scripture"],
  "chapel_summary": {
    "CLS": "RECEIPTED",
    "DEF": "RECEIPTED",
    "PRF": "RECEIPTED",
    "EVD": "RECEIPTED",
    "FAL": "RECEIPTED — kill condition written",
    "LNK": "RECEIPTED",
    "RIV": "RECEIPTED — strongest rival addressed",
    "ISO": "RECEIPTED — PART grade",
    "A-L4": "NOT_RUN",
    "A-Z3": "NOT_RUN",
    "A-PY": "RECEIPTED — numerical test passed"
  },
  "bridge_summary": {
    "bridge_count": 3,
    "grades": {"ISO": 1, "PART": 1, "ANLG": 1},
    "strongest": "ISO_M — Yukawa potential mapping"
  },
  "blockers": [
    "A-L4 not run — formal verification pending",
    "A-Z3 not run — satisfiability check pending"
  ],
  "recommendation": "CANDIDATE with two open checks. All narrative stations pass. Formal verification pending but not required for candidate status.",
  "confidence_note": "Strong on evidence and cross-domain bridges. Formal verification would upgrade truth from 'supported' to 'established'.",
  "state": "DRAFT",
  "needs_ruling": true
}
```

**Per-paper canon summary:**
```json
{
  "paper_id": "MIM.06.ACTS",
  "total_claims": 12,
  "by_state": {
    "candidate": 8,
    "review": 3,
    "draft": 1
  },
  "blockers": ["CLS-009 has no kill condition (FAL not passed)"],
  "paper_recommendation": "11 of 12 claims ready for candidate. CLS-009 blocked at the door (FAL).",
  "bridge_coverage": "3 bridges active, 1 ISO, 1 PART, 1 ANLG"
}
```

---

## 5. THE TRUTH LEVELS — HOW THEY CONNECT TO CANON

The Truth field (from the MASTER_CLASSIFICATION_SHEET) tracks how strongly a claim is held. This is SEPARATE from canon state — a claim can be "supported" in truth but still "draft" in canon (hasn't been reviewed yet).

| Truth level | Meaning | What typically gets it here |
|-------------|---------|---------------------------|
| **established** | Proven or verified beyond reasonable dispute | Lean-verified, multiple independent checks |
| **supported** | Strong evidence or argument; open to revision | CHAPEL passes, bridge grades strong |
| **argued** | Reasoned case made; not yet independently checked | Paper written, not yet through CHAPEL |
| **posited** | Taken as axiom or starting point | Axioms — by design, not by proof |
| **conjectured** | Proposed; insufficient support | Early-stage claims |
| **contested** | Serious unresolved objections on record | RIV station raised unaddressed alternatives |
| **refuted** | Shown false; kept for the record | Kill condition triggered (append-only, never deleted) |

**How truth and canon interact:**
- A claim at truth=`established` and canon=`candidate` is ready for David to rule canon
- A claim at truth=`argued` and canon=`review` needs more CHAPEL work before it can be proposed
- A claim at truth=`refuted` automatically goes to canon=`retired` (but David confirms)
- A claim at truth=`posited` and canon=`canon` is an axiom — posited by design, ratified by ruling

---

## 6. THE VERIFICATION METHODS — WHAT HAS CHECKED IT

Multi-select from the Verification sheet. A claim can have several:

| Method | What it means | Proof required |
|--------|-------------|---------------|
| **lean_kernel** | Compiled in Lean by us | file path + SHA256 + #print axioms |
| **external_pin** | Formalized by others (Mathlib, Flypitch, Isabelle) | declaration name + version |
| **smt** | Duplicated in Z3/SMT (second witness) | script + result log |
| **simulation** | Monte Carlo / numerical test, pre-registered | null model + kill threshold + result |
| **source** | Primary historical/scholarly source checked | citation + date checked |
| **scripture** | Scripture cited (KJV) | reference |
| **cross_ai** | Cold-read or multi-AI audit | dated log |
| **none** | Not yet checked | — |

---

## 7. WHERE CANON CONDENSES WITH CHAPEL AND BRIDGE

Here's where we can share work and not duplicate:

### What CHAPEL already produces that Canon reuses (NO new API call needed):

| CHAPEL Station | What Canon takes from it | Canon does NOT re-run this |
|---------------|------------------------|--------------------------|
| CLS | The claim list — Canon iterates over these | ✅ Reuse |
| DEF | Whether definitions are grounded | ✅ Reuse |
| PRF | Whether derivation chains are valid | ✅ Reuse |
| EVD | Evidence quality assessment | ✅ Reuse |
| FAL | Whether kill conditions exist (the door check) | ✅ Reuse |
| LNK | Dependency mapping | ✅ Reuse |
| RIV | Whether rivals are addressed | ✅ Reuse |
| ISO | Isomorphism grades inside the paper | ✅ Reuse |
| A-L4, A-Z3, A-PY | Formal/computational results | ✅ Reuse |
| VER | Per-claim verdict | ✅ Reuse — Canon is basically VER + BRIDGE + history |

### What BRIDGE already produces that Canon reuses:

| Bridge output | What Canon takes | Canon does NOT re-run this |
|--------------|-----------------|--------------------------|
| Bridge grades (ISO/PART/ANLG/WIT) | Aggregated into the canon record | ✅ Reuse |
| Bridge case files | Referenced, not re-analyzed | ✅ Reuse |

### What Canon ADDS that neither CHAPEL nor BRIDGE produces:

| Canon-only output | What it is | Why it's new |
|------------------|-----------|-------------|
| **Canon state tracking** | raw → draft → review → candidate → canon → retired | Neither CHAPEL nor BRIDGE tracks the lifecycle |
| **Blocker identification** | "CLS-009 has no kill condition" | CHAPEL knows FAL failed; Canon knows that blocks candidacy |
| **Historical record** | When each state transition happened, who proposed, who ruled | Append-only, never deleted — the audit trail |
| **Paper-level aggregation** | "11 of 12 claims ready" | Individual stations don't roll up to paper level |
| **Ballot preparation** | Assembles the case for David to rule | CHAPEL and BRIDGE produce evidence; Canon assembles it |

### The condensation:

**Canon API = VER station + BRIDGE summary + state machine + history.**

That's it. VER already reads all the other CHAPEL stations and produces a per-claim verdict. Canon adds:
1. The bridge summary on top of VER's output
2. The state machine (tracking raw → draft → review → candidate → canon → retired)
3. The historical record (who proposed what when)
4. The paper-level roll-up

So the Canon API call is NOT a full re-analysis. It's an aggregation layer. It reads VER + BRIDGE outputs, runs the state machine logic, and produces the canon record. Lightweight. Fast. The heavy lifting was already done by CHAPEL and BRIDGE.

**Can we merge Canon into VER?** Almost. The difference is that VER is per-claim and per-run (it's a station output). Canon is per-claim and per-lifetime (it tracks the whole history). VER tells you what the claim's status is RIGHT NOW. Canon tells you where it's been and where it's going. Keep them separate but have Canon read from VER.

---

## 8. THE CANON FOLDER

Canon lives at the SERIES level (like CHAPEL and BRIDGE), not inside individual paper folders:

```
00_MIM_SERIES/
├── CHAPEL/          ← verification (per paper)
├── BRIDGE/          ← cross-domain connections (per paper and cross-paper)
├── CANON/           ← judgment (per paper, with series roll-up)
│   ├── MIM.01__CAN.md        ← canon record for paper 01
│   ├── MIM.06__CAN.md        ← canon record for paper 06
│   ├── BALLOT/               ← ballot preparation files
│   ├── HISTORY/              ← state transition log (append-only)
│   └── CAN_SERIES_ROLL.md    ← series-level summary
├── ORBITS/
├── API/
└── ...
```

**Naming:**
```
MIM.06.ACTS__CAN                    ← canon record for this paper
MIM.06.ACTS__CAN.CLS-003            ← canon state for specific claim
MIM.06.ACTS__CAN.API.261124-001     ← canon API run receipt
```

---

## 9. THE ARGUMENT TYPES — HOW THE PAPER ARGUES

From the Arguments sheet. Every claim has an argument type that tells you HOW it argues, which affects what Canon needs to see:

| Argument type | What it is | What Canon checks |
|--------------|-----------|------------------|
| **deductive** | Conclusion follows necessarily from premises | PRF must be RECEIPTED |
| **self_defeat** | Denial presupposes what it denies | RIV must show the self-defeat holds |
| **abductive** | Best explanation of the evidence | EVD + RIV — is it really the BEST? |
| **inductive** | Pattern across many cases | EVD — are there enough cases? |
| **isomorphic** | Same structure shown in two domains | BRIDGE grade must be ISO or PART |
| **analogical** | Illustrative similarity, NOT constraining | BRIDGE grade = ANLG (this is honest) |
| **formal** | Machine-checked derivation | A-L4 must be RECEIPTED |
| **testimonial** | Witness, historical record, scripture | EVD source type must match |

**The connection:** A claim typed as "isomorphic" that has a BRIDGE grade of ANLG is internally inconsistent — it claims isomorphism but only earned analogy. Canon flags this. A claim typed as "formal" with A-L4 = NOT_RUN is a claim that hasn't met its own stated bar. Canon flags this too.

---

## 10. THE CONTENT ROLES — WHAT THE PARAGRAPH DOES

From the Roles sheet. These are CONTENT roles (what a passage asserts), different from WORKSPACE roles (what job a folder does):

| Role | What it does |
|------|-------------|
| **claim** | States something as true |
| **evidence** | Supports a claim with data, source, witness or scripture |
| **bridge** | Connects two domains |
| **objection** | States the strongest case against |
| **proof** | Derives a conclusion validly |
| **open_question** | Marks what is not yet settled |

Canon checks that every claim has at least one evidence, that every bridge has a bridge grade, that every objection has been addressed (or the claim is marked "contested"), and that open questions don't accidentally get proposed as candidates.

---

## 11. WHERE WE'RE PROBABLY WRONG

1. **Canon might be too thin to be its own API call.** If it's really just VER + BRIDGE summary + state machine, maybe it's a mode of VER rather than a separate call. But the history tracking and ballot preparation feel like they warrant separation.

2. **The state machine transitions might need more states.** "Review" covers a lot of ground — a paper that just entered CHAPEL vs one that's passed 10 of 12 stations are both "review." Could split into review_early / review_late, but that might be overengineering.

3. **The relationship between paper-level canon and claim-level canon needs work.** Can a paper be "canon" if 11 of 12 claims are canon but one is "contested"? Probably yes — the contested claim is documented. But the rule needs to be explicit.

4. **Retired vs refuted:** A retired claim is withdrawn or superseded. A refuted claim's kill condition was triggered. These are different things but both end up out of canon. The distinction matters for the historical record.

---

## 12. NEXT STEPS

1. **Crew reviews.** Is Canon its own API call or a mode of VER?
2. **Run Canon manually on one paper** — MIM.06.ACTS — to see if the schema works.
3. **Build the state machine** — the transition logic (what has to be true for each state change).
4. **Build the ballot preparation** — what David sees when it's time to rule.

---

*Canon proposes. David rules. The record is append-only. Nothing is deleted. A refuted claim stays — with its kill condition, its history, and the date it fell.*
