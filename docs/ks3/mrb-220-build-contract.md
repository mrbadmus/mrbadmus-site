# MRB-220 — build contract for B2, C1 (rebuild) and C2

One document that the engine pass and the sixteen authoring passes both build against, so a
kind name, a shell choice or a payload key is decided **once** rather than sixteen times.

Written 16 Aug 2026 by the MRB-220 commander, from Design's three `NOTES-*.md`, the three
`*-inventory/PAYLOAD-MAP.md` measurements, and the generator as it stands on `main` at
`a4109aae6`.

**If this document and a payload map disagree, the map wins on measurement (what Design drew)
and this document wins on naming and schema (what we call it and how it is authored).** Where a
map records something this contract has not anticipated, follow the map and say so in the report.

---

## 0. File ownership — who writes what

| Files | Owner |
|---|---|
| `build_ks3.py`, `shared/ks3.css`, `shared/ks3.js`, `ks3_parity.py`, `verify_ks3.py` | **The engine pass, alone.** No authoring pass edits these. |
| `ks3_data/b2/`, `ks3_data/c1/`, `ks3_data/c2/` and their unit wrappers | **The authoring passes**, one lesson per module, no two passes in one file. |
| `docs/ks3/*` | Commander. |

An authoring pass that finds it needs an engine change **does not make it**. It records the need
and authors against this contract's schema. A schema that turns out to be wrong is one report line;
two passes editing `build_ks3.py` at once is a lost afternoon.

---

## 1. Rulings that bind, and are not re-argued

- **MRB-205** — Design draws, we render. No invented component, block type, layout or page
  structure. Behaviour, physics and detail may be added *inside* a component Design drew where the
  page is silent; an addition may never contradict the page. **Page wins over engine.**
- **MRB-204 as amended 15 Aug 2026** — every formula gets its own block alone, a drawn diagram, a
  staged-reveal worked example, then the student fills the steps before any independent question.
  **TRIANGLE for products** (`A = B × C`). **BALANCE-BEAM / part–whole BAR for sums and
  conservation statements.** A triangle on a sum teaches a false relationship.
  → `c2-06` is a SUM. It gets the beam and the bar. This is settled; see §4.
- **MRB-208** — the trail is carried inline in the header, never a separate breadcrumb row. The
  progress rail is completion-based, never scroll-based, on **both** the ≥1340px side rail and the
  narrow top bar, and **nothing is ticked on load**. KEY FACT is a cream band, 2px ink outline,
  hard orange offset shadow, mono label, display type — **never amber**.
- **MRB-210** — one microscope depth-of-field table for all of KS3: `0.100 mm` at ×40 total,
  `0.040` at ×100, `0.008` at ×400. No unit re-declares it.
- **MRB-196 R10** — CLASSIFY's sort and CONTRAST's settles-it get a lightweight self-check: the
  student is asked whether they had it and answers for themselves. **No green, no red, nothing on
  the option button.** Every other activity kind: no per-option feedback at all.
- **Only the ladder marks correctness** — green tint + drawn ✓ for right, dark ✕ for wrong, never
  the accent for either. **Amber is a wrong IDEA being confronted, never the student.**
- **Sequence is data** — year and half-term never appear in a lesson URL or in a lesson page's
  bytes. Write "a student your age", never "a Year 7".
- **§8.10, no platform self-explanation** — student pages carry no meta-text about how the platform
  works. Default is cut. Legal/safety notes stay, small, at the bottom edge, never a callout.
- **Prose bar** — if a sentence is not teaching or setting up a decision, cut it.
- ⛔ **REVOKED 16 Aug 2026 (MRB-221, Mide).** This line used to read *"every lesson carries the
  under-review marker."* The content has been reviewed; there is no draft state. No lesson carries a
  review marker, the browse-list `Draft` badge is gone with it, and `verify_ks3.py` now asserts the
  marker's **absence**. Kept in place, marked, per §12's reversal rule.

---

## 2. Commander's rulings made for this run

These are decisions the run needed and did not have. Each is recorded so it is not re-taken.

**R1 — `#s-think` is a rail stop in B2, C1 and C2, and renders as `predict`.**
B1's `confrontation` kind deliberately emits no `data-stage-done`, because on B1's approved pages
`#s-think` is static markup with no gate — there is nothing to complete. On these three units'
pages `#s-think` asks for a commitment (options, then a gated reveal), which is a `predict`. A
block that demands a commitment and then reveals **is** a completed activity, and MRB-208 says the
rail is completion-based. So: author these as `predict`, and they tick. This is not a reversal of
B1's ruling; it is the same rule meeting a different block.

**R2 — `done_when` becomes load-bearing in the GATE, not in the runtime.**
`done_when` is authored on every rail stage of every lesson, serialised into `data-rail-stages`,
and read by **nothing** — the runtime decides completion from `data-stage-done` and DOM
heuristics in `doneByDom()`. It is a dead authored key on all twelve live lessons.
B1's own source records the symptom it causes: *"a stage that can never tick"*.

It is **not** wired into the runtime in this run. Re-deriving completion from a declared string
would change ticking behaviour on twelve lessons that are live, verified and in front of students,
to fix a defect that is invisible to them. Instead `verify_ks3.py` gains an assertion that every
declared `done_when` names a condition the page can actually reach, and that every rail stage can
reach done. A wrong value then fails the build, which is what "wired" has to mean for the field to
be worth authoring. Runtime unification is a follow-up ticket, not this run's business.

**R3 — the shipped stylesheet wins over per-page KEY FACT drift.**
Design's B2 pages draw the KEY FACT box with a `6px 6px` shadow, 25px body and `22px 26px`
padding; `shared/ks3.css` ships `5px 5px`, 22px and `18px 22px`. One stylesheet serves all 183
lesson slots, so adopting the page's values restyles B1 — six lessons Mide has already approved —
to match four he has not seen. The ruled *identity* of the box (band ground, 2px ink outline, hard
**accent** offset shadow, mono label, display statement, never amber) is what MRB-208 fixes, and
the shipped CSS satisfies all of it. The numeric drift is recorded in the report as drift, and it
is Mide's to rule on if he wants the page's figures.

**R4 — a defect on an approved page that a ruling already covers is corrected, not reproduced.**
`b2-03` starts its animation loop without consulting `prefers-reduced-motion` (it reads
`this.reduced` once at construction and never checks it in the tick), where `b2-02` does check.
Reduced motion is an accessibility contract, not a matter of taste, and the same page's sibling
implements it correctly — so this is a slip, not an intention. Corrected in the engine, reported.

**R5 — no key is authored without a read site, in the same pass.**
The B1 replay shipped 234 authored keys of which 146 were read by nothing, one of them an approved
science correction that therefore never reached a student. `ks3_key_audit.py` gates this run:
`python3 ks3_key_audit.py B2 C1 C2`. If a key has no read site, either wire the read or do not
author the key. "It documents intent" is not a read site — put it in a comment.

**R6 — the nav brand tile is PARKED and stays parked.**
Design's B2/C1/C2 pages draw the brand as a cream `#FBF3E6` chevron inside a 34px `#E4572E`
tile. MRB-197 (Mide's ruling) is an accent chevron on the ground, and that is what `NAV_BRAND`
emits for all 294 KS3 pages. These three deliveries are **evidence added to the parked entry in
`architecture.md` §8**, not authority to change the mark. Do not adopt the tile. Do not delete the
note.

---

## 3. Where a lesson record goes

Follow B1 exactly (`ks3_data/b1/`), which is the current pattern and supersedes the single-file
shape:

```
ks3_data/b2/__init__.py                  # lessons(), + _normalise() lifting instruments
ks3_data/b2/lesson_01_what_the_skeleton_does.py     # exports LESSON
...
ks3_data/biology_b2_movement.py          # thin UNIT wrapper: from .b2 import lessons
```

C1 is a **rebuild over a live unit**: `ks3_data/chemistry_c1_particles.py` loses its inline
lessons and becomes the wrapper, exactly as `biology_b1_cells.py` did. The superseded bodies stay
reachable in git history — that is the record, and nothing is deleted to tidy up.

**Slugs are permanent (§8.4) and must match `ks3_data/structure.py` character for character.**
They are the join for scheme-of-work rows, progress records and every `requires` edge. Titles may
differ from `structure.py`; slugs may not.

> Known title divergence, for the report, not for silent correction: `structure.py` names C1 L6
> *"Testing the model: does it explain everything?"*; Design's page titles it *"Testing the
> model"*. The page is what a student reads.

**Every student-facing string is lifted byte-identical** from the approved page, via
`node tools/extract_design_payload.js <page> [CONST...]`. Extracted JSON for all sixteen pages is
already in the run's scratchpad. Never retype science-bearing copy; a typo in retyped prose is
invisible and crosses the examiner gate.

---

## 4. The kind roster

`segment` is the SHELL the block renders in and it is a real decision, not a label: `practical` is
ink-dark, `check` is a plain light `ks3-block`. B1 got two of six wrong and it took a layer-C
assertion to catch — an instrument painted on the wrong ground. **Measure the shell from Design's
own markup** (`ks3-block` alone → `check`; `ks3-block ks3-dark ks3-practical` → `practical`) and
follow the measurement, not this table, where they disagree.

### B2 — Movement: skeleton and muscles

| kind | lesson | segment | canvas? | payload |
|---|---|---|---|---|
| `system-switch` | b2-01 | measure | DOM | `{parts:[{id,name,tab,title,does,prompt,options[4],chain:[{level,text}],close}], show_levels}` |
| `job-sort` | b2-01/02/03 | measure | DOM | per-item immediate-reveal sorter — 14 items, the largest single win in the unit |
| `joint-bench` | b2-02 | measure | canvas | `{joints:[…12 fields…], bend_deg, bend_range, twist_allowed, twisting}` |
| `muscle-pair` | b2-03 | measure | canvas + rAF | `{mode:'biceps'|'triceps'|'both'|'none', dead:{biceps,triceps}, angle_deg}` |
| `arm-lever` | b2-04 | measure | canvas, static | `{load_kg, d_muscle_cm, d_load_cm, g:10, meter_fitted}` |
| `lever-steps` | b2-04 | measure | DOM | the four-step scaffolded attempt |
| `meter-compare` | b2-04 | measure | DOM | three meters × three readings + mean |

### C1 — Particles and their behaviour (rebuild)

| kind | lesson | canvas? | notes |
|---|---|---|---|
| `halving-bench` | c1-01 | canvas | cut / undo / cut-ten; **floor is 24 cuts** and the number is load-bearing in rung 2 |
| `gap-test-rig` | c1-01 | DOM | three tests × gap-filled or not |
| `state-bench` | c1-02 | canvas | state ×3, freeze, paths, squash. **The fixed-size reference particle is drawn in every state and may not be removed for layout** |
| `heating-bench` | c1-03 | canvas | scrub 0–100, three jump targets; **boiling plateau ~7:1 longer than melting, and rung 4 depends on it** |
| `collision-counter` | c1-04 | canvas | temp ×3, volume ×3, count ×3; particle–particle bumps are **drawn and explicitly excluded** |
| `random-walk-bench` | c1-05 | canvas + rAF | **the two crossing counters must not reset when `even` flips** — that is the whole confrontation of `PART-11` |
| `evidence-bench` | c1-06 | DOM | 7 tests, 4 pass 3 fail |
| `model-timeline` | c1-06 | DOM | five steps; stops short of "and now we know" |

### C2 — Atoms, elements and compounds

| kind | lesson | canvas? | notes |
|---|---|---|---|
| `claim-switch` | c2-01 | DOM | 3 claims × 4 observations; an observation reads *no longer explained* when a claim it needs is off |
| `test-budget-bench` | c2-02 | DOM | **the budget is the pedagogy.** Default 8. Drop it and the lesson becomes a click-through |
| `mixture-compound-dish` | c2-03 | canvas | proportion control **disabled once heated** — that is itself the lesson |
| `formula-builder` | c2-05 | canvas | five reachable substances; most combinations say **"not a substance"** |
| `balance-bench` | c2-06 | measure | 2 reactions × 2 vessels; third tile reads *not measured — you work it out* |

### Shared

| kind | used by | notes |
|---|---|---|
| `cover-triangle` | b2-04 | **exists** as `r_formula_triangle` with corrected, derived geometry. Payload widens: a `result` slot (Design shows the arrangement in display type *and* a sentence), three closing blocks not one, and Design's button order `F, T, d` with `F` pre-covered |
| `cover-bar` | c2-06 | **NEW.** The part–whole bar: one long bar for *everything before*, split beneath into *left in the flask* + *the gas*, same three cover buttons. Cover keys are `whole` / `left` / `gas`. Verified from the page: **c2-06 contains the word "triangle" zero times** and draws a balance beam with pans |

---

## 5. What is NOT in scope

- **P1–P3 are authored and deliberately held for MRB-223.** If they appear on disk, ignore them.
- No new page structure, no new layout, no component Design has not drawn.
- No change to the nav brand (R6) or `shell()`'s signature — it is composed from two sessions' work
  and the single `trail_html or crumb_html` slot is deliberate.
  ⊕ **`CARVE_OUT_EXPIRY` no longer exists.** This bullet used to protect it, requiring an explicit
  §12 amendment with Mide's decision on the record before it could move. MRB-221 is that amendment:
  Mide revoked the carve-out on 16 Aug 2026 and the constant was deleted rather than moved.

---

## 5A. Amended 19 Aug 2026 — MRB-257, from the KS3 Biology audit

The audit returned 153 findings across 58 lessons and they collapse onto a small number of
repeatable mistakes. Everything below is **binding on Chemistry and Physics** — 113 lessons are
still to be built, and every one of them would otherwise inherit these. This section is MRB-257
decision 8, plus the rules the remediation run itself had to discover.

### 5A.1 The prose bar, extended — an instrument is a source of truth

- **No bench-intro control narration.** If the paragraph above a bench describes buttons that are
  already on screen, cut it. `disturbing-a-food-web` ships no intro paragraph and loses nothing;
  that is the evidence these can be cut outright rather than trimmed. (C6 — 11 of 19 benches.)
- **Any count or figure quoted in prose must match the instrument.** This is the single largest
  family in the audit, it recurred in Chemistry, and it resolves the same way every time:
  **the instrument is the measurement and the prose is what changes.** The number moves only when
  the number is *wrong* — and when it does, the page's own other sentences are usually the
  evidence (`absorption-and-the-small-intestine` said 30 m² and ×60 in four places while the
  readout said 32 and ×63).
  *Adjusting a figure to rescue a sentence is not available.* The figures are what a student reads
  as evidence.
- **A dial that is DRAWN must also be MODELLED.** `gas-pressure`'s container control reached
  `draw()` and nothing else, so the box got smaller and the wall-hit rate did not move — under the
  lesson's own first prediction, which marks "it goes up" correct. Measured: 14.7 / 14.3 / 14.9 per
  second across the three settings.
- **A comparative label over per-state values is COMPUTED, never authored beside them.** The
  alveoli tiles were asked to read *"more oxygen here / less oxygen here"*; authored as two static
  strings that ships a false statement, because in the both-stopped state both sides read 9.3 kPa.
  Derive it from the values and it is true in every reachable state by construction — including the
  equal one, which is worth a student seeing. An authored comparative is a second source for a fact
  the numbers already carry, and the two drift the moment a state is added.
- **Every reachable state has something true to say, and the gate is stated over the STATE SPACE.**
  Three independent toggles is 2³ states, and only four of them are prefixes of document order —
  the fold builder's notes were keyed to *how many* levels were on rather than *which*, so
  villi-only printed the sentence about the folds. Asserting "n notes exist" passes while leaving a
  state uncovered. Walk the subsets.
- **A branch that cannot be reached is authored copy no student will read.** Where a defensive
  branch exists *because* of a property of the payload, gate the property: `claim-switch` now
  refuses a claim no observation needs, which is what its own note asserts out loud.

### 5A.2 Token annotations are law

`shared/tokens.css` states, beside several colours and in capitals, what they may and may not be
used for. Those lines bind, and `verify_ks3.py` now enforces them against **computed size and
painted ground** across every built page.

| Token | Rule |
|---|---|
| `--ks3-accent` | LARGE TEXT ONLY (≥24px, or ≥18.66px at 700+). Never body size. |
| `--ks3-ok` | MARKS AND FILLS ONLY. Never `color:` on text, at any size. |
| `--ks3-ok-text` | body-size green on a LIGHT ground only. |
| `--ks3-ok-dark` | body-size green on an INK-DARK ground only. |
| `--ks3-blue-light` | on ink-dark only. |

**MRB-252's two rulings, recorded here so they stop being re-litigated per unit:**

- **The greens.** The engine had been painting `--ks3-ok` as `color:` on 16–26px readouts across
  six instruments — 3.48:1 on the dark panel, 2.89:1 on the figures tile, which fails even the
  large-text bar. The file already forbade it; what it did not do was offer a legal alternative, so
  the violation had nowhere to go. `--ks3-ok-text` and `--ks3-ok-dark` are minted, and
  `--ks3-ok-dark` is the one KS3 colour with no line in Design's frozen reference — recorded in
  `MINTED_TOKENS` rather than let through Layer A quietly.
- **Amber warns; it never merely labels.** Reserved for warning and confrontation — the `#s-think`
  register, and genuine caution or loss states. By B11 it was carrying four jobs on two benches
  (a wrong idea, a species, "the field you are looking at", "nothing survived", "what you gave
  up"). Nothing was broken — every instance carried a word as well as the colour — but a student
  who has learned across B1–B9 that amber means *careful, this is a wrong idea* cannot then meet
  amber meaning *a moth* without the first meaning wearing away. **Category and selection uses go
  to `--ks3-data`.**
- ⚠️ **No accent-text token on any dark ground, ever.** `--st-accent-text` is specified as the
  small-text partner *on cream*; landing it on a dark ground is the same class of error as the
  on-dark green (audit 3.2 — comparison captions at 1.78:1, on the block whose entire teaching
  point is which column is which).

### 5A.3 Readouts

- **Every countable readout uses `data-format-one`.** "1 portions on the plate", "1 units",
  "No white plants at all in 1 seeds" — one is a state a student passes through on the way to two,
  and on some benches it is the state they reach on purpose.
- **A ratio needs both terms.** `pp × pp` printed "Ratio purple to white — 0.00 : 1"; so did any
  sample of one that came up white. Author the line for each end, and note that a sample of one
  always has one of the two counts at zero.

### 5A.4 Figures

- **Every code-drawn figure's parity rows include at least one assertion tying the visual encoding
  to the fact it teaches**, mutation-tested at source (decision 4).
- **A content-truth row walks EVERY element a defect could touch.** The base-pair figure keyed its
  fills to the column rather than the base and was wrong on 4 of 10 boxes; the obvious form of the
  assertion — four rows, one per letter — catches only two of the four, because a selector returns
  the first match and rung 1 is correct even under the bug. The alveoli row drives **all four**
  states including the equal one, which is the state a load sweep never reaches and the state the
  literal fix got wrong. **An assertion that passes on the majority of a defect is how these reach
  production.**
- **Retiring a declared figure is a `status: "retired"` plus a `retired_reason` on the record**,
  never a deletion — `docs/ks3/diagram-manifest.md` is generated, and a deleted record loses the
  reasoning and lets the figure be re-declared later.

**Added 19 Aug 2026 (MRB-254), from the twelve biology figures.**

- **THE FILLED BADGE MEANS "THIS ONE HAS NO COUNTERPART".** ⊕ Ruled, and written here because
  Design asked for it to be: a numbered badge drawn SOLID, with its numeral reversed out, marks an
  item that has nothing corresponding to it in the set it is being compared with. An open badge
  marks one that does. It carries no colour, it is explained once in the figure's own legend, and
  it is never explained anywhere else. `b5-reproductive-systems` is the first use — three filled
  badges on the female side, none on the male — and it puts the lesson's named misconception
  ("the two systems are mirror images") inside the drawing instead of in a caption underneath it.
  **The next figure that needs "this one has no partner" uses this mark**, rather than inventing a
  second one; two marks for one meaning is how a reader stops trusting either.
  ⚠️ Its hook is `data-counterpart="none"|"paired"` and the content-truth row asserts the FILL and
  the MEANING agree on every badge. On b5-01 the three unpaired structures happen to be the last
  three in the table *and* the last three in the column, so a fill keyed to index or to position
  renders that figure pixel-identically and is wrong the moment a tenth structure or a re-order
  arrives. That is the base-pair defect exactly.
- **A figure that carries no category hue carries the distinction on something else, and says so.**
  The biology set uses shape, dash pattern, position, stroke weight, badge fill inversion and
  numerals — with a label in every case — and `--ks3-data` appears nowhere in it. ⚠️ **`--ks3-data`
  is minted in the engine's `shared/tokens.css` under MRB-252 but is NOT in the shipped
  design-system token files Design draws against.** Reconcile the two before Chemistry figures are
  commissioned, or the same avoidance will be re-invented figure by figure.
- **A `<desc>` walks the drawing in reading order and is 900–2,100 characters**, and it describes
  what is ACTUALLY DRAWN. Where a port corrects the drawing, the `desc` is corrected with it: three
  of the twelve shipped a `desc` that disagreed with the delivery (a tube reaching the middle ovule
  when it reaches the uppermost; a closing note that is not on the plate). A `<desc>` is the whole
  drawing to a reader who cannot see it, and shipping a knowingly false one because it is the
  designer's is the wrong reading of MRB-205.
- **A drawn figure declares its own readable width.** `_svg_open` emits `min-width` from the width
  the drawer was drawn at; the stylesheet's value is a floor, not the answer. One number cannot be
  right for figures 760, 860 and 900 units wide, and the failure is silent — the labels simply
  scale below the legible floor while every font-size in the file stays correct.

### 5A.5 Navigation and sweeps

- **prev/next emitted from the unit `order`**, rolling over into the next unit's first lesson.
  Eleven non-terminal lessons had no link at all to the next lesson in their own unit.
- **Four rail stops.** Design's fourth was restored under MRB-249 and the count is not a
  suggestion: the rail is the completion signal the schools layer is built on, `markStage()` is a
  **structural ratchet** (a call that would lower an already-true stage is a no-op), and a lesson
  that ticks on fewer stops than it draws reports progress it did not earn.
- **§8.10 sweeps run over post-interaction state, not the served HTML.** The `b4-04` slug on
  `what-drugs-do-to-the-body` sits behind four interactions and survived the gate built to catch
  it. Same blind spot as the b1-03 specimen defect.
- **The no-op-press invariant.** *Pressing the control that already claims to be pressed must be a
  no-op; if the section's rendered text changes, what was on screen was not what the control
  claimed.* This is the assertion that catches b1-03, and a count-based invariant cannot: exactly
  one control was pressed before and after, the whole way through, while the page taught that a
  leaf cell has no wall, no vacuole and no chloroplasts.
  ⚠️ Its companion — "a clicked control becomes the pressed one" — was **removed**: load state
  cannot tell a radio group from a toggle bank, and in a toggle bank a second press legitimately
  turns a control off.
  ⚠️ **Presets over a continuous control are not a radio group.** A row of shortcuts onto a slider
  legitimately has none pressed when the slider sits between them; identify them structurally (a
  numeric value hook plus a range input in the same instrument), never by page name. "Two or more
  pressed" remains a defect on a preset row.

### 5A.6 Editing the corpus

- **THE EDITOR-CUT LAW.** An audit's polish table is written for an editor, not a machine: rows say
  *drop X* and leave the seam to judgement. Applied literally, 17 of the biology cuts shipped
  broken sentences — *"foxes eat and die. look at when each peak happens"*, *"Only the conditions
  change, ."*, *"The reason is width. every rung is one big and one small"*. **A cut is re-authored
  so the seam lands as a sentence, previewed against the built page, and never applied as a raw
  string delete.**
- **Corpus-wide matching works on FOLDED LITERALS, never `grep`.** These records routinely split a
  sentence across adjacent Python string literals, so the contiguous substring does not exist in
  the file. `grep -l "awaiting illustration" ks3_data/` found **eight** of the eleven C4 leaks;
  folding with `ast` finds all eleven, which is the count measured from the served pages. A
  grep-driven fix ships 8 of 11 and reports it done.
- ⚠️ **`ast` reports column offsets in UTF-8 BYTES; Python string indices count CHARACTERS.** On an
  ASCII corpus they agree. This corpus is written with em dashes and curly apostrophes, so any
  literal whose final line carries them reports an end column past the real one and the span
  swallows the source after it — on one swap by exactly four characters, two apostrophes at two
  extra bytes each, which ate a closing `),`. Convert before slicing, and **re-parse before
  writing**: that assertion existed for a defect nobody had thought of and is what stopped it.
- **Edits land in the source records, never the built tree**, and the swap harness is a gate with
  an edit inside it: old string exactly once before, zero after, new exactly once after, **and no
  other page changed**. That last clause is the one a careless `sed` over `ks3_data/` gets wrong —
  a sentence authored once can be rendered on two pages.
- **The audit's "Left alone deliberately" list is binding.** Figure hedges, safeguarding wording,
  model-limitation disclosures and predict-first instructions are load-bearing and must not be
  tidied.

### 5A.7 Science authority

Where prose and instrument disagree the instrument wins, and that is a **build** call, not a
science one. A ruling that moves a figure, a model or a claim is recorded **in the record it
touches**, with the working, so the next pass can see why — and a record that has parked something
for Mide says so in the same place. Two chemistry corrections in this run were sitting in exactly
such parked notes, correctly raised months earlier and never resolved.

---

## 6. Gates — a failing gate is a finding, never an obstacle

Never weaken a gate to make something pass.

1. `python3 verify_ks3.py` green.
2. `python3 ks3_key_audit.py B2 C1 C2` green.
3. Byte-identical output across **both** generator orders (KS4-then-KS3 and the reverse).
4. Zero console errors on every new page.
5. Every new assertion **mutation-tested** — an assertion that still passes against a deliberately
   broken page is not an assertion.
6. Every new component has **markup AND CSS AND JS**. A dispatch-table entry is not a component;
   instruments have shipped as bare bullet lists past a green kinds gate.
7. **Freeze transitions before driving any state.** `.ks3-option` transitions background over
   160ms, so a computed-style read straight after a click returns the colour it is *leaving*.
8. Use the harness **device-metrics override** for viewport queries. Shrinking a container does not
   fire a `max-width` media query and will pass silently over a broken layout.
9. Verify CSS against elements that **actually exist on the page**. Dead CSS is evidence to a grep
   and nothing to a browser.
10. Every state seen in a browser, not described: resting, chosen-correct, chosen-wrong, spent,
    locked, reduced-motion.

**Browser harness, learned the hard way:** run a **fresh headless Chrome per page** — the KS3
canvas loops keep running after the driver moves on, and one shared browser accumulates enough of
them to drop the DevTools socket around the twelfth page.
