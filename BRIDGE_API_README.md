# AI README — BRIDGE LAYER API CALL
## First Draft — Expect This To Be Wrong In Places

**POF 2828 · November 24, 2026**
**Status: SKETCH — every AI reviews, challenges, and improves before build**

This sits inside the BRIDGE/ folder at the series level (e.g., `MIM/00_MIM_SERIES/BRIDGE/`). The 00 folder holds all 21 workspace role folders plus CHAPEL, ORBITS, BRIDGE, API, and the rest. BRIDGE is its own layer alongside CHAPEL, not inside it.

---

## 1. WHAT THE BRIDGE API CALL DOES

It takes a claim from one domain and asks: **does this have a structural counterpart in another domain?**

This is the hardest call in the system because "structural counterpart" means different things depending on what kind of connection you're looking at. A mathematical isomorphism is not the same as a grammatical parallel is not the same as a theological echo. Each needs different evidence and a different grading standard.

The call reads from CHAPEL (specifically CLS, PRF, EVD, LNK) and writes to BRIDGE.

---

## 2. THE SEVEN BRIDGE TYPES

I'm going to be wrong on some of these. The categories need crew review. But here's the starting taxonomy:

### Type 1: MATHEMATICAL ISOMORPHISM (ISO-M)
**What it is:** Two equations from different domains share the same mathematical structure — same form, same variable relationships, same behavior under the same operations.

**Example:** Yukawa potential V(r) = −αs/r + k·r in strong force ↔ Love as the binding force with the same distance-dependent behavior.

**Evidence required:**
- Both equations written out explicitly
- Variable-by-variable mapping showing which term in domain A corresponds to which term in domain B
- Proof that the mapping preserves the mathematical operations (not just the shape of the equation)
- At least one prediction or constraint that the isomorphism generates in the target domain

**Grading standard:** Does the mapping survive substitution? If you plug the mapped variables in, does the equation still produce valid results in the target domain?

**Where we're likely wrong:** Some of these will be analogy dressed up as isomorphism. The test is whether the mapping is PREDICTIVE — does it tell you something you didn't already know in the target domain? If it only confirms what you already knew, it might be analogy.

---

### Type 2: GRAMMATICAL / STRUCTURAL PARALLEL (ISO-G)
**What it is:** Two systems from different domains share the same logical grammar — the same kinds of operations, the same kinds of constraints, the same kinds of transformations — even though the objects are different.

**Example:** The grammar of forgiveness (debt → payment → release → restoration) has the same structure as error correction (corruption → detection → correction → verification). Same grammar, different objects.

**Evidence required:**
- The grammar spelled out as a sequence of typed operations
- Both instances mapped step-by-step
- Identification of where the grammar BREAKS — which step doesn't have a counterpart, or has an extra step

**Grading standard:** Does the grammar generate the same constraints in both domains? If step 3 requires step 2 in domain A, does it also require step 2's counterpart in domain B?

**Where we're likely wrong:** Grammatical parallels can be forced. Four-step processes can be made to look like any other four-step process if you're flexible enough with the labels. The test is whether the ORDER and the NECESSITY transfer — not just the number of steps.

---

### Type 3: EMPIRICAL CORRELATION (ISO-E)
**What it is:** A measured quantity in one domain correlates with a measured quantity in another domain beyond what chance would predict.

**Example:** PEAR-LAB consciousness-intention correlation at 6.35σ. Global Consciousness Project at 6σ. PROP-COSMOS at 5.7σ.

**Evidence required:**
- The measurement protocol for each domain
- The statistical analysis (p-value, sigma, effect size)
- Identification of potential confounds
- Whether the correlation is PREDICTED by the framework or discovered after the fact (prediction is stronger)

**Grading standard:** Sigma level. Below 3σ = interesting. 3-5σ = noteworthy. Above 5σ = strong. But sigma alone isn't enough — a high sigma on a confounded measurement is still confounded.

**Where we're likely wrong:** Correlation ≠ causation, and in cross-domain work the temptation to read causation into correlation is enormous. The bridge claim should state what the correlation IS, not what it MEANS. Meaning is interpretation; the bridge is the connection.

---

### Type 4: LOGICAL EQUIVALENCE (ISO-L)
**What it is:** Two propositions from different domains are logically equivalent — if one is true, the other must be true, and if one is false, the other must be false.

**Example:** "A self-consistent system cannot prove its own consistency" (Gödel) ↔ "No self-audit can be complete" (moral domain). If Gödel's theorem holds, the moral claim follows by structural equivalence.

**Evidence required:**
- Both propositions stated formally
- The logical derivation showing equivalence (not just similarity)
- Identification of the shared axioms — what do both propositions assume?
- What breaks if one is false — does the other actually fall?

**Grading standard:** Can you derive one from the other using only the shared axioms and the mapping? If you need ADDITIONAL premises in the target domain, it's not equivalence — it's implication at best.

**Where we're likely wrong:** Informal logical equivalence is easy to claim and hard to verify. The step between "these feel equivalent" and "these ARE equivalent" is a formal proof. Without the proof, grade it as PART or ANLG, not ISO.

---

### Type 5: THEOLOGICAL ECHO / WITNESS (WIT)
**What it is:** A finding in one domain independently arrives at something theology already stated — not because it was derived from theology, but because both are pointing at the same underlying reality.

**Example:** Information theory independently arriving at "in the beginning was the Word" — Logos as information, discovered not imposed.

**Evidence required:**
- The theological source (Scripture reference, historical theology)
- The independent finding (paper, experiment, proof) with its own derivation chain that doesn't reference theology
- Demonstration that the independent finding was NOT reverse-engineered from the theological claim
- The specific point of convergence — what exactly do both say?

**Grading standard:** Independence is everything. If the finding was derived from the theological claim, it's not a witness — it's a consequence. The value of a witness is that it arrived at the same place from a completely different starting point.

**Where we're likely wrong:** Independence is hard to establish in a framework that starts from theological axioms. The test: could a researcher who had never read the Bible arrive at this finding through their domain alone? If yes, it's a witness. If the derivation path runs through a theological premise at any point, it's a consequence, not a witness.

---

### Type 6: NOETHER / CONSERVATION BRIDGE (ISO-N)
**What it is:** A symmetry in one domain corresponds to a conserved quantity in another domain via Noether's theorem or its moral analog.

**Example:** Time-translation symmetry preserved in the moral domain → Noether → moral energy is conserved (∇βTαβ = 0). The weak force breaks parity (sin is directional/irreversible) while preserving time-translation (moral energy is conserved). Both simultaneously.

**Evidence required:**
- The symmetry identified in the source domain
- The corresponding conserved quantity in the target domain
- The Noether derivation connecting them
- What breaks if the symmetry is violated — does the conservation law fail?

**Grading standard:** Is the Noether derivation valid? This is a mathematical claim and can be checked formally. Either the symmetry produces the conservation law or it doesn't.

**Where we're likely wrong:** Extending Noether's theorem from physics to morality is exactly the kind of move that works beautifully if the mathematical structure transfers and fails completely if it doesn't. The bridge claim should state clearly what "time-translation symmetry in the moral domain" MEANS — not just that it exists, but what concrete thing it corresponds to.

---

### Type 7: PHASE / STATE BRIDGE (ISO-P)
**What it is:** A phase transition or state change in one domain corresponds to a phase transition or state change in another domain — same critical behavior, same order parameter, same universality class.

**Example:** BEC condensation ↔ salvation — the 12-stage mapping from "Salvation Is a Phase Transition." Temperature → spiritual resistance, condensation → surrender, coherence → sanctification.

**Evidence required:**
- The phase transition identified in both domains
- The order parameter mapping
- Whether the universality class matches (same critical exponents)
- What the critical point corresponds to in the target domain

**Grading standard:** Do the critical exponents match? This is a quantitative test. If the phase transition has the same mathematical character in both domains, the bridge is strong. If only the narrative matches but the mathematics diverge, it's analogy.

**Where we're likely wrong:** Phase transition language is seductive because it has a built-in narrative (before → critical point → after). Almost anything with a dramatic change can be described as a "phase transition" loosely. The test is the mathematics — do the equations of state actually match?

---

## 3. THE FOUR GRADES

Every bridge gets exactly one grade:

| Grade | Meaning | Evidence bar |
|-------|---------|-------------|
| **ISO** | Full structural isomorphism | Formal proof that the mapping preserves operations, is predictive in the target domain, and survives substitution |
| **PART** | Partial match | The mapping holds for some operations but breaks for others; the break points are identified |
| **ANLG** | Analogy | The domains share a resemblance but the mapping is not operation-preserving; the resemblance is specified |
| **WIT** | Independent witness | Two independent derivation paths arrive at the same conclusion from different starting points |

**Grading rules:**
1. Default is ANLG until proven otherwise. The burden is on the bridge to earn a higher grade.
2. ISO requires a formal proof or a formal derivation. "It looks like the same equation" is PART at best.
3. PART requires identification of exactly where the mapping breaks. "It mostly works" without naming the failure point is ANLG.
4. WIT requires demonstration of independence. If the derivation path runs through a shared premise, it's not independent.
5. A bridge can be DOWNGRADED but never UPGRADED without new evidence.
6. Grade is per-bridge, not per-paper. One paper can have ISO bridges and ANLG bridges.

---

## 4. THE API CALL — INPUTS AND OUTPUTS

### Input:
```json
{
  "paper_id": "MIM.06.ACTS",
  "source_domain": "physics",
  "target_domain": "theology",
  "claims": ["CLS-001", "CLS-003", "CLS-007"],
  "bridge_type_hint": null,
  "run_date": "261124",
  "runner": "opus-46"
}
```

- `paper_id`: which paper's claims to check
- `source_domain`: where the claim lives natively
- `target_domain`: where we're looking for a counterpart
- `claims`: which specific claims to bridge (from CHAPEL CLS records). If null, run all claims.
- `bridge_type_hint`: optional — if you already know it's a mathematical isomorphism, say so. Otherwise the call classifies.
- `run_date`: YYMMDD
- `runner`: which AI ran this

### Output (per claim):
```json
{
  "bridge_id": "MIM.06.ACTS__BRG.261124-001",
  "source_claim": "CLS-003",
  "source_domain": "physics",
  "source_statement": "Operations in mathematics are acts of will...",
  "target_domain": "theology",
  "target_counterpart": "Every act of creation is an act of will...",
  "target_source": "Genesis 1, John 1:3",
  "bridge_type": "ISO-G",
  "grade": "PART",
  "mapping": {
    "source_term_1": "mathematical operation",
    "target_term_1": "divine act",
    "source_term_2": "operand",
    "target_term_2": "created thing",
    "source_term_3": "result",
    "target_term_3": "creation"
  },
  "preserves": ["ordering", "composition", "identity"],
  "breaks_at": ["invertibility — divine acts are not always reversible in the same sense mathematical operations are"],
  "prediction": "If this bridge holds, then mathematical operations that are non-commutative should correspond to divine acts where order matters (e.g., creation before judgment, not the reverse)",
  "independence": null,
  "confidence_note": "PART because the invertibility break is real — mathematical operations have inverses; divine acts may not. The ordering preservation is strong.",
  "state": "DRAFT",
  "needs_review": ["Is invertibility really a break, or does grace function as the 'inverse operation'?"]
}
```

### What the output must always include:
1. **The mapping** — term by term, what corresponds to what
2. **What preserves** — which operations or properties survive the mapping
3. **Where it breaks** — honestly, specifically, named
4. **A prediction** — what the bridge tells you that you didn't already know
5. **A confidence note** — why this grade and not a higher one
6. **What needs review** — open questions the AI couldn't settle

---

## 5. THE PIPELINE

```
0. LOAD DEFAULTS from .TEMPLATES/BRIDGE/:
   a. LOGICAL_ROLE_AND_DEPENDENCY_MAP — the 101-term dependency spine with 72 edges
   b. SPIRITUAL_TERMS_REGISTER — 625 terms with D/M status flags
   c. SPIRITUAL_DEPENDENCY_GRAPH — the full edge graph (.json)
   d. CORE_OPERATOR_MAP — ORBITS↔grace operations mapping
   e. ROOT_PREDICATE_REGISTER — foundational predicates
   f. ORBITS_XSTATE_CROSSWALK — 821 classified IDs
   
   These are the STARTING knowledge. The bridge call checks every claim
   against this existing graph FIRST before searching the broader corpus.

1. Read CHAPEL CLS records for the paper
2. For each claim, identify the native domain
3. For each claim, check against the DEFAULT graph:
   a. Does this claim's term appear in the 101-term dependency map? What's its role?
   b. What's its D/M status? (D0 = no definition, M0 = no math — flag these)
   c. What edges already exist from this term? (from the 72 proposed edges)
   d. Is this term isolated? (from the 33 isolated terms list)
4. For each claim, search for NEW counterparts beyond the defaults:
   a. Check the Ten Laws canonical spiritual terms table
   b. Check existing bridge records in LNK and ISO
   c. Search the corpus for related claims in other papers
   d. If the claim has a mathematical form, check for structural matches
5. For each candidate counterpart, classify the bridge type (ISO-M, ISO-G, ISO-E, ISO-L, WIT, ISO-N, ISO-P)
6. For each bridge, build the mapping:
   a. Term-by-term correspondence
   b. What preserves, what breaks
   c. Generate a prediction if possible
7. Grade: ISO / PART / ANLG / WIT
8. Write the bridge record
9. Flag anything that needs human review
10. UPDATE the dependency graph — new edges discovered get appended to the graph
```

---

## 6. WHAT THIS CALL READS FROM

| Source | What it provides |
|--------|-----------------|
| CHAPEL/CLS | The claims to bridge |
| CHAPEL/PRF | Derivation chains (needed to check independence for WIT) |
| CHAPEL/EVD | Evidence sources (needed to verify empirical correlations) |
| CHAPEL/LNK | Existing dependency links (some may already be bridges) |
| NT Spiritual Terms table (from David's system prompt) | The canonical physics↔theology mappings for each of the Ten Laws |
| **LOGICAL_ROLE_AND_DEPENDENCY_MAP** | **DEFAULT BRIDGE INPUT — 101 classified terms with 72 proposed edges, logical roles, dependency spine, gap status. This is the starting graph the bridge call checks every claim against.** |
| **SPIRITUAL_TERMS_REGISTER** | **625 terms with D0/D1/D2 (definition status) and M0/M1/M2 (math status). Tells the bridge call what's defined, what has math, and what's still open.** |
| **SPIRITUAL_DEPENDENCY_GRAPH** | **The full dependency graph (.json + .md). Edges between terms with types.** |
| **CORE_OPERATOR_MAP** | **ORBITS fields mapped to grace operations — Awaken, Respond, Pay, Restore, Declare, Internal Process.** |
| **ROOT_PREDICATE_REGISTER** | **Root predicates — the foundational logical building blocks.** |
| **ORBITS_ACTION_VOCABULARY_AND_XSTATE_CROSSWALK** | **821 IDs (625 spiritual + 196 axiom) with XState machine mapping. Tells the bridge call what has executable verification potential.** |
| Master Equation | The mathematical structure to check isomorphisms against |
| Other papers' CLS records | Cross-series counterpart search |

---

## 7. WHAT THIS CALL WRITES TO

| Destination | What it writes |
|-------------|---------------|
| BRIDGE/ | One bridge record per identified connection |
| BRIDGE/BRG-H | HTML output page (the `-H` convention) |
| API/ | The run receipt with full inputs, outputs, and runner ID |

---

## 8. KNOWN WEAKNESSES — WHERE WE'RE GOING TO BE WRONG

I'm flagging these up front so the crew knows where to push:

1. **The seven types might not be the right seven.** There could be bridge types I'm not seeing, or types that should be merged. The crew should challenge the taxonomy.

2. **The grading is going to be generous at first.** The temptation is to grade everything as ISO when it might be PART or ANLG. The default should be ANLG and the bridge has to EARN a higher grade.

3. **Independence for WIT is genuinely hard to establish** in a framework that starts from theological axioms. We need a rigorous test for "could this have been derived without theology?" and I don't have one yet.

4. **Mathematical isomorphism checking is beyond what a language model can do reliably.** The ISO-M type needs formal verification — either Lean or Z3 or at minimum a Python numerical check. The API call can PROPOSE an ISO-M grade but it should be flagged for formal verification before it's trusted.

5. **The corpus search for counterparts will miss things.** The search depends on what's been claimed and labeled. An unlabeled paper with a perfect counterpart won't be found. This is the labeling problem again — the bridge layer can only find what's been indexed.

6. **Some bridges will be NOVEL — the framework predicts a counterpart that hasn't been found yet.** These are the most valuable and the most dangerous. A predicted counterpart that turns out to exist is a confirmed prediction. A predicted counterpart that doesn't exist is a failed prediction. Both should be tracked.

7. **The phase bridge type (ISO-P) might be too specific.** It could be a subtype of ISO-M rather than its own category. Crew should decide.

8. **I don't know how to handle bridges that cross MORE than two domains.** A three-way bridge (physics ↔ theology ↔ information theory) is a real thing in this framework but the current schema is two-domain. Needs design.

---

## 9. THE NT SPIRITUAL TERMS TABLE — BRIDGE STARTING POINTS

These are the canonical mappings from David's system prompt. Each Law already has a physics↔theology bridge built in. The bridge API call should check every claim against these first:

| Law | Physics | Theology | Symmetry |
|-----|---------|----------|----------|
| 1 | Gravitation (GR) | Sin ↔ Grace | ↔8 |
| 2 | Motion F=ma | Sin Nature ↔ Grace-as-Force | ↔9 |
| 3 | Electromagnetism | Truth ↔ Deception | ↔10 |
| 4 | Strong Force | Love ↔ Captivity | ↔7 |
| 5 | Thermodynamics | Judgment ↔ Heat Death | ↔6 |
| 6 | Information/Shannon | Logos ↔ Chaos | ↔5 |
| 7 | Quantum | Faith ↔ Doubt/Control | ↔4 |
| 8 | Relativity | Grace ↔ Frame Lock | ↔1 |
| 9 | Weak Force | Moral Conservation (directional) | asymmetric |
| 10 | Coherence | Christ ↔ Decoherence | asymmetric |

Laws 1-8 have perfect internal symmetry. Law 9 is directional (breaks parity). Law 10 is sovereign (C IS χ).

The Fruits derivation (Law 4), Justice/Mercy derivation (Law 5), and Moral Conservation derivation (Law 9) are the three LOCKED formalizations. Bridge claims against these have existing mathematical structure to check against.

---

## 10. KIMI'S ISO FORMS — THE CANONICAL FORMAT (DO NOT CHANGE)

The ISO forms at `\\192.168.2.50\h_hp\Desktop\ISO\` are the canonical HTML format for bridge records. 37 exist (iso-001 through ISO-037). These were built by Kimi and are LOCKED — same structure, same colors, same layout. Any new bridge HTML (`BRG-H`) must match this format exactly.

**The five-section structure:**
1. Registry header (ID, title, symmetry pair)
2. Domain Specifications (Domain A: Physics, Domain B: Theology — with descriptions)
3. The Isomorphic Mapping (variable-by-variable, with "What Is NOT Claimed" box)
4. Separator Tests — the four-test gatekeeper:
   - Test A: Structural Preservation (do relations survive the mapping?)
   - Test B: Non-Arbitrariness (is the mapping forced, or could you swap targets?)
   - Test C: Constraint (does the mapping rule things out?)
   - Test D: Bidirectionality (does each side predict the other?)
5. Classification & Evidence (grade, confidence, kill condition, empirical evidence)

**Visual identity:** Gold on black (#c9a84c on #050508), JetBrains Mono for code, Crimson Text serif, grid background, gold glow accents. This is Kimi's design and it stays.

**The four separator tests ARE the grading standard for ISO.** A bridge that passes all four = ISO. Three of four = PART. Fewer = ANLG. This is more specific than what §3 says and supersedes it for the HTML output.

**Numbering:** ISO-001 through ISO-999. Three digits, no compression needed, the hyphen between ISO and the number is just a separator — it does NOT carry the God/Jesus meaning. The hyphen-means-God rule applies to series codes and compressed names, not to sequential numbering that already has three digits.

**Existing ISO forms (37 on disk):**
- iso-001: Gravity ↔ Sin
- iso-002: Superposition ↔ Eden
- iso-003: Collapse ↔ Fall
- iso-004: Born Rule ↔ Trinity
- iso-005: Decoherence ↔ Lifespan
- iso-006: Coherence ↔ Salvation
- iso-007: Substrate ↔ Fracture
- iso-008: Eraser ↔ Atonement
- iso-009: Entropy ↔ Wages of Sin
- iso-011: Seven Attacks and Counters
- ISO-012: Sign Operator
- ISO-013: Grace Operator
- ISO-015: Moral Physics
- ISO-016: Eschatological Attractors
- ISO-018: Cosmological Grace
- ISO-022: Lagrangian Unity
- ISO-025: Immunology ↔ Soteriology
- ISO-026: Addiction ↔ Sin
- ISO-027: Epidemiology ↔ Sin
- ISO-028: Ecology ↔ Ecclesiology
- ISO-029: Music ↔ Trinity
- ISO-030: Genetics ↔ Scripture
- ISO-031: Network ↔ Ecclesiology
- ISO-032: Attachment ↔ Prayer
- ISO-033: Pharmacology ↔ Grace
- ISO-034: Control ↔ Providence
- ISO-035: Cryptography ↔ Revelation
- ISO-036: Fluid ↔ Pneumatology
- ISO-037: Beer-Lambert

Plus supporting files: AAA-000 (Classification Framework), AAA-001 (Boundary Conditions), AAA-002 (BEC Soteriology Audit), AAA-003 (Promotion Checklist), ISO-000 (24 Property Identity), TRINITY-001 (Universal Domain).

---

## 11. AGGREGATION — VIEWS ACROSS ALL BRIDGES

David wants to see all bridges grouped by domain, by law, by type. This is a generated report (a recipe), not a new folder. The individual ISO forms stay as they are. The aggregation queries the bridge index and links back to the forms.

**Example recipes:**
- All bridges touching theology → `WHERE target_domain = 'theology'`
- All bridges for Law 4 (Strong Force / Love) → `WHERE law = 4`
- All ISO-grade bridges → `WHERE grade = 'ISO'`
- All bridges for one paper → `WHERE paper_id = 'MIM.06.ACTS'`
- All bridges by domain pair → `GROUP BY source_domain, target_domain`

Each report is an HTML page generated from the bridge records. It links back to the individual ISO form for each bridge. The ISO forms are the source of truth; the reports are views.

---

## 12. NEXT STEPS

1. **Crew reviews this document.** Challenge the seven types. Challenge the grading. Challenge the pipeline.
2. **Pick one paper and run the bridge call manually** — write out the bridge records by hand for one paper to see if the schema works.
3. **Build the Python script** that automates the call. It reads from CHAPEL, writes to BRIDGE, produces the BRG-H page in Kimi's exact format.
4. **Run on MIM.06.ACTS first** — this is the paper with the most mathematical content and the most bridge candidates.
5. **Build the aggregation recipes** — domain view, law view, grade view.

---

*This is a first draft. I know it's wrong in places. The crew's job is to find where and fix it. The goal is a bridge layer that is honest about what it doesn't know and rigorous about what it claims.*
