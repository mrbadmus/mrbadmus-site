# C9 — Metals and materials · author's notes

**Four lessons. Every slot in `ks3_data/structure.py` is authored.**
Everything is draft and unreviewed.

Slugs are taken character for character from `structure.py`:
`the-reactivity-series`, `predicting-displacement`, `getting-metals-out-of-rocks`,
`ceramics-polymers-and-composites`.

---

## 1. Statutory coverage

| Lesson | Statements |
|---|---|
| `the-reactivity-series` | `KS3.C.MATS.01` |
| `predicting-displacement` | `KS3.WS.EXP.02` |
| `getting-metals-out-of-rocks` | `KS3.C.MATS.02` |
| `ceramics-polymers-and-composites` | `KS3.C.MATS.03` |

All three subject statements C9 owns are owned **exactly once**, and all three are
covered. `MATS.01` names "metals **and carbon**", so carbon's position is
established in lesson 1 — it is in the reference list, marked as a non-metal, and
the prose says what earns it the place — rather than being left to lesson 3 to
claim as well.

**No sub-IDs were minted.** §11.11 (option a) allows clause-level sub-IDs, and
`MATS.01` could have been split 01a/01b across lessons 1 and 3. It did not need
to be: the whole statement sits in lesson 1 and lesson 3 uses it. A mint is
permanent once referenced, so the cheaper reading is the right one. Nothing in
this delivery requires `ks3_statutory.py` to be regenerated.

**`predicting-displacement` anchors on WS**, per §5.7 / §5.7.1. It teaches no new
subject content by design — it is the lesson where the series from lesson 1 is
turned into a prediction, and `KS3.WS.EXP.02` ("make predictions using scientific
knowledge and understanding") is exactly what the student does eight times. WS
statements are exempt from exactly-once ownership. **Confirm this is the right
anchor** rather than `KS3.WS.ANA.03` (identifying patterns), which the synthesis
panel also serves.

---

## 2. Structural flags

**a. C8's oxides question lands here.** `NOTES-C8.md` §2 offers a ruling with
three options, and option (c) is "keep three group lessons and move oxides to C9,
where the reactivity series lives". This build assumes **no**: `structure.py`
gives C9 four slots and four are authored. If (c) is chosen, C9 becomes a
five-lesson unit, `structure.py` needs the slug, and the `UNIT` array that
generates prev/next in all four pages has to be regenerated. `KS3.C.PT.06`
remains uncovered either way.

**b. The unit before C9 is a lesson that does not exist.** Unit order puts C8's
`metal-and-non-metal-oxides` immediately before `the-reactivity-series`, and it is
unauthored. Lesson 1 therefore renders **no "Before this lesson" section at all**
rather than a cross-unit link to `c8-06`, which is not its predecessor. That is a
decision the generator should confirm: the alternative is to link the last
*authored* lesson of the previous unit and accept that the chain skips a slot.

**c. Prev/next is generated, not hand-written** (§8.10 / audit law 16). Each page
carries the same four-row `UNIT` array and its own `SLUG`, and derives the
endmatter links from position. When the generator owns this, the array is what it
replaces — the markup around it does not change.

---

## 3. Four lessons, four instruments

- **`c9-01`** — a **12-cell reaction audit**: six metals down, cold water and
  dilute acid across. Every cell is predict-then-read. Two cells carry the
  lesson: magnesium in cold water (almost nothing, from the metal students
  expect to be violent) and zinc against copper (identical in water, opposite in
  acid). When all twelve are read, the bench sorts the six into three bands and
  states the order it has just derived.
- **`c9-02`** — an **eight-card prediction deck**. Each card is a proposed
  reaction; the student commits "it happens" or "nothing happens" before it runs.
  Five happen, three do not. When all eight are run they sort into two columns
  and the rule is the only thing left standing.
- **`c9-03`** — a **route bench**: six deliveries, four methods, 24 authored
  verdicts. Silver oxide can be freed three ways and the bench says which of them
  a works would pay for; aluminium oxide cannot be freed by carbon at all.
- **`c9-04`** — a **spec bench**: four jobs carrying tagged requirements, six
  materials on the shelf, exactly one match per job. A rejection is reported as
  the named requirement it fails and why, never as a count.

§6 adjacency: 01 and 02 are both matrix-ish and adjacent, which is the risk §6
warns about. They are different instruments — 01 reads observations off a fixed
matrix to build an order, 02 takes a commitment on a single proposal at a time —
and 02 exists because 01 established the order it uses.

**`reactivity-grid` was deliberately not used.** `NOTES-C8.md` §4 anticipated
C9's series as its fourth use, with more than four rows. It has now been used
three times (C5-04, C6-04, C8-05) and a fourth would be the third metals grid in
the chemistry sequence. C9-01's matrix is a near relative — metal × **reagent**,
cells carrying observations rather than reaction/no-reaction — and it is
registered as a new family in §10. **Ruling wanted:** fold `reaction-audit` into
`reactivity-grid` as a variant, or keep it separate as registered.

---

## 4. Science flags

1. **Magnesium in cold water** (`c9-01`) authored as "almost nothing — after
   several minutes a few tiny bubbles cling to the ribbon", with the note that
   the reaction is real but too slow to watch. Many schemes say flatly "no
   reaction". Confirm the hedge is what you want; it is load-bearing, because the
   band label is "needs acid before much happens" rather than "no reaction with
   water".
2. **Potassium in dilute acid** (`c9-01`) is authored as a cell that is *not
   done*, at any concentration, with the reason: potassium is violent with water
   alone and dilute acid is mostly water, and the water test has already settled
   its position. The cell is readable — the note is the teaching. Confirm safety
   over completeness here.
3. **Potassium in water** carries the only apparatus line on the page: teacher
   demonstration, behind a screen, smallest piece that can be cut. Confirm.
4. **Calcium in water turning cloudy white** (calcium hydroxide, slightly
   soluble) — correct, and it is the observation rung 3 marks.
5. **"Iron chloride"** without the (II) (`c9-01` word equation). Deliberate at
   KS3. Confirm.
6. **Zinc in iron sulfate** (`c9-02` card 7) is real but slow and much less
   obvious than the copper displacements; the observation says so. Confirm the
   hedge rather than dropping the card — it is the only card where the pair are
   adjacent in the series.
7. **Carbon with copper oxide as a displacement** (`c9-02` card 8) — the same
   rule with a non-metal, and it previews lesson 3. Confirm you want it in the
   displacement lesson as well.
8. **Thermite** (`c9-02` Going further): aluminium + iron oxide for rail welding,
   with "it is not a school experiment at any scale" and no temperature figure
   quoted. Confirm you want it at KS3.
9. **Sacrificial zinc anodes** (`c9-02` Going further) explained purely by
   position in the series, with no electrochemistry. Correct at this level.
10. **Silver oxide as the "heat alone" route** (`c9-03`). Silver oxide does
    decompose on heating. The textbook example is mercury oxide, avoided
    deliberately. Confirm the substitution.
11. **Blast furnace** (`c9-03` Going further) states that most of the oxygen is
    taken by carbon monoxide formed from the coke, not by solid carbon. Correct,
    and above the statutory line — it is in the optional layer for that reason.
12. **Zinc leaving the furnace as a vapour and being condensed** (`c9-03`) —
    correct, and it is why zinc's cell reads differently from iron's.
13. **Aluminium costing more than gold in the 1850s** (`c9-03` rung 2 stem).
    Attested. Confirm you want the claim stated flatly.
14. **"Roughly a twentieth of the electricity" for recycled aluminium**
    (`c9-03` Going further). Hedged deliberately; the commonly quoted figure is
    about 5%. Confirm the hedge stays.
15. **Cryolite** is named only in the GCSE line, not in the lesson body.
16. **Concrete spalling** when heated and cooled (`c9-04`, why reinforced
    concrete loses the pizza-oven job) — correct.
17. **Polyethene passing carbon dioxide** so a fizzy drink stored in it goes flat
    in days, where PET holds it (`c9-04`). Correct, and it is the requirement
    that decides the bottle job. Confirm the "in days" timescale.
18. **Glass treated as a ceramic** (`c9-04`, heat-proof glass-ceramic wins the
    stove window). Standard at KS3; some sources separate glasses from ceramics.
    Confirm.
19. **"Stronger but brittle" vs "weaker but tough"** (`c9-04` hook and rung 2).
    The hook asserts the china plate is the stronger material. Confirm.
20. **Composite recycling** (`c9-04` Going further): a cracked carbon frame is
    "currently shredded, burned for its energy, or buried". Hedged with
    "currently" on purpose.

---

## 5. Practicals and risk assessment — FLAGGED

None of these pages prints a method, and none is a substitute for one.

1. **`c9-01`'s bench is a simulation of a demonstration.** Potassium and calcium
   in water, and four metals in dilute hydrochloric acid, all need a written risk
   assessment before anything is run in a room. The page carries an apparatus
   line on the potassium cell only, because that is the cell where the
   *chemistry* needs it; it is not a control measure.
2. **`c9-03`'s copper oxide + carbon reduction** is a standard school practical
   and the one thing in this unit a class is most likely to actually do. It needs
   a risk assessment: strong heating, a reducing mixture, hot residues.
3. **Thermite** (`c9-02` Going further) is named and explicitly excluded. If the
   editorial line is "do not name what a student might try", say so and it comes
   out.

---

## 6. Misconception register — proposed `MATL` family

Range pre-allocated per lesson with a named spare, before authoring
(audit law 15). Every `elicited_by` and `confronted_by` below resolves to an
element id **on its own page**.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `MATL-01` | A metal that does nothing in cold water is unreactive. | `think-commit-water` | `think-reveal-acid` | `the-reactivity-series` |
| `MATL-02` | Reactivity is the same thing as strength or hardness. | `rung-2` | `rung-2-feedback` | `the-reactivity-series` |
| `MATL-03` | Carbon cannot belong in an order of metals. | — | `series-carbon` | `the-reactivity-series` |
| `MATL-04` | *spare, unallocated* | — | — | `the-reactivity-series` |
| `MATL-05` | Any metal will displace any other if it is left long enough. | `think-commit-time` | `think-reveal-never` | `predicting-displacement` |
| `MATL-06` | A less reactive metal can push a more reactive one out of its compound. | `rung-2` | `rung-2-feedback` | `predicting-displacement` |
| `MATL-07` | *spare, unallocated* | — | — | `predicting-displacement` |
| `MATL-08` | Metals are in the ground as metal, and extraction is digging and melting. | `hook-commit` | `hook-reveal` | `getting-metals-out-of-rocks` |
| `MATL-09` | Any oxide gives up its oxygen to carbon if the furnace is hot enough. | `think-commit-hotter` | `think-reveal-aluminium` | `getting-metals-out-of-rocks` |
| `MATL-10` | *spare, unallocated* | — | — | `getting-metals-out-of-rocks` |
| `MATL-11` | If a material shatters, it must be weak. | `hook-commit` | `hook-reveal` | `ceramics-polymers-and-composites` |
| `MATL-12` | Plastic is one material. | `think-commit-plastic` | `think-reveal-family` | `ceramics-polymers-and-composites` |
| `MATL-13` | Strong and tough are the same property. | `rung-2` | `rung-2-feedback` | `ceramics-polymers-and-composites` |
| `MATL-14` | *spare, unallocated* | — | — | `ceramics-polymers-and-composites` |

`MATL-03` has **no `elicited_by`, deliberately**. Nothing on the page asks the
student to commit to the belief that carbon does not belong — the reference list
simply presents it, marked, with the reason. Inventing an anchor to fill the
column would be the dishonest version (law 15).

`MATL-02` and `MATL-13` are cousins: one says reactivity is strength, the other
says strength is toughness. They are elicited by different phenomena in different
lessons and are worth keeping separate, but the pair is the unit's spine — both
are "a word from everyday life is doing service as a technical term".

`MATL-05` overlaps `PTAB-08`'s neighbourhood (C8) in shape only, not in content;
no cross-reference needed. `MATL-08` is the one a Year 9 class is most likely to
arrive holding.

---

## 7. §10 — component family register

Registered here because the **coverage manifest is not in this project**, and an
unregistered family is invisible to the coverage gate. Merge into §10 of the
manifest verbatim; nothing below is described anywhere else in the delivery.

| Family | Minted in | What it is | Payload shape |
|---|---|---|---|
| `reaction-audit` | `c9-01` | Subject × reagent matrix. Cells are predict-then-read; each cell holds its own observation, optional word equation and optional apparatus line. A cell may be *unavailable* (readable, no prediction taken). Synthesis groups the subjects into authored bands and states the derived order. | `METALS: [{id, name, rank, band, form, <reagent>: {happens\|skipped, vigour, obs, eq, care}}]`, `REAGENTS: [{id, label, phrase}]`, `BANDS: [{id, label, note}]` |
| `prediction-deck` | `c9-02` | A deck of proposed events. One commitment per card before the result opens; the result acknowledges the commitment in words without scoring it. Outcome is computed from ranked data, never stored per card. Synthesis sorts the deck into outcome columns with the deciding relation named. | `CARDS: [{id, added, inside, label, setup, obs, eq}]` + a ranked `STRIP: [{name, rank, tag}]` |
| `extraction-route` | `c9-03` | Subject × method chooser. Every (subject, method) pair carries an authored verdict, including "works and is the wrong tool" as distinct from "works" and from "does not work" — a method choice is never scored as a skipped step. Synthesis groups subjects by their best route. | `ORES: [{id, name, metal, route, setup, line, verdicts: {<method>: {works, title, why, eq}}}]`, `METHODS: [{id, label}]`, `ROUTE_GROUPS: [{id, label, note}]` |
| `spec-bench` | `c9-04` | Requirement tags × candidates. A candidate meets a set of requirement ids and carries a reason for each one it fails. Rejection is reported by the identity of the failing requirements, never by how many. Exactly one candidate satisfies each job. | `REQS: {id: label}`, `MATERIALS: [{id, name, cls, meets: [reqId], fails: {reqId: reason}}]`, `JOBS: [{id, name, setup, reqs: [reqId], praise}]` |
| `unit-nav` | all four | Endmatter prev/next generated from unit order instead of hand-written links. Emits nothing when there is no neighbour, rather than linking outside the unit. | `UNIT: [{slug, file, title}]` + page-level `SLUG` |

Reused unchanged, no new registration: the five-stop rail, the four-rung mastery
ladder (two marked, two self-marked), the hook commit, the misconception block,
the key-fact block, the ink-dark key note, the optional layer.

`spec-bench` and `extraction-route` are both "choose a tool, be told what it
costs you" and could be one family with a `requirements` shape. They are
registered separately because `extraction-route`'s verdicts are per pair and
authored, while `spec-bench`'s are derived from tag sets — the payloads do not
convert. Fold them only if the generator would rather own one.

---

## 8. Figures

**None declared, deliberately.** Every diagram this unit could want would be a
worse copy of an instrument that is already on the page: a reactivity ladder
(the reference list in lesson 1), a displacement tube (the deck readout), a
blast-furnace section (the route verdict), a composite cross-section (the family
cards). Audit law 8 says declare only what will be drawn and never one that
duplicates an instrument, so `figures` is empty on all four lessons and the
diagram manifest gains nothing from C9.

The one candidate worth arguing for is a **composite cross-section** — fibres in
a surround, drawn once — because `c9-04`'s key fact describes a structure the
page never shows. It is not declared. Say the word and it becomes the unit's
only figure.

---

## 9. Where the build contract could not be followed

1. **`docs/ks3/mrb-220-build-contract.md` is absent from this project**, as
   `docs/ks3/gates/README.md` already recorded on 17 Aug. I worked to
   `architecture.md`, which declares itself law and self-contained, plus the
   gates README and the frozen reference.
2. **`--ks3-data` does not exist.** Audit law 9 reserves `--ks3-alert` for
   warning and confrontation and says to use `--ks3-data` for categories and
   selection. There is no such token in `tokens/shared-tokens.css` or
   `tokens/shared-ks3.css` — grep returns nothing anywhere in the project. Every
   selection and category state in C9 therefore uses `--ks3-accent` /
   `--ks3-accent-tint` with an `--ks3-ink` outline, exactly as C8-05 does, and
   **every cell also carries a word** ("reacts", "none", "not done", "route
   found", "matched"), so colour is never the only channel. Amber appears only
   where the stylesheet puts it, on misconception blocks. **Either the token
   needs adding or law 9 needs amending** — as written it cannot be complied with.
3. **`ks3_statutory.py` is not in the project.** Ownership was checked against
   `docs/ks3/statutory-register.md`, the generated companion. Access is
   read-only, so nothing was regenerated and no ID was minted (see §1).
4. **The coverage manifest is not in the project**, so §10 above is delivered
   here rather than written into it.

---

## 10. For Code

- Five rail stops per lesson: hook, reference, instrument, misconception, ladder.
  The **reference stop carries no control** — it is ticked by the hook's
  commitment, because the reference exists to be read while the instrument beside
  it is worked (MRB-249). Five stops, not three.
- One `[data-key-fact]` block and one `.ks3-keynote` block per lesson, so gate D
  bites on all four and none of them needs the exemption list.
- Every arrow is inline SVG. No `→`, `✓` or `✕` characters anywhere — the latin
  subsets do not carry them.
- No `.ks3-commit` colour override was added. The class asks for
  `--ks3-alert` at (0,1,0) and `.ks3-dark p` beats it at (0,1,1) on every hook
  block in the course, which is gate A1's finding; the cream that wins is legible
  and these pages do not work around it.
- Ordering answers carry the word: rung 4 criteria in `c9-01` and `c9-03` read
  "places M below zinc", not an arrow diagram.
- Props: `showDraft` only, as everywhere else in the build.
- All four instruments are DOM. No canvas, no animation loop, no timers.
- `c9-01` links forward to `c9-02` and has **no back link** (see §2b). `c9-04`
  has no forward link — C10's first lesson is a different unit and the generator
  should decide whether the chain crosses.
- Bench gates: `c9-01` rail stop ticks at 10 of 12 cells read and its synthesis
  opens at 12, so no band can be empty when the panel appears. `c9-02` ticks at 6
  of 8 and its synthesis opens at 8. `c9-03` ticks at 4 of 6 routes found, panel
  at 6. `c9-04` ticks at 3 of 4 jobs matched, panel at 4.
