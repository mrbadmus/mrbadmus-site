# NOTES — KS3 Physics P8 / P9

**P8 and P9 complete.** All seven P8 slots (`p8-01` … `p8-07`) and all three P9
slots (`p9-01` … `p9-03`) are authored, one standalone viewable HTML per lesson,
one folder per unit. This file is the delivery record for both units. §10 is the
component-family registration the coverage gate needs.

---

## 1. Recon: what was and was not available

| Input the brief names | State in this project |
|---|---|
| `ks3_data/structure.py` | Present. Slugs, titles, families and lesson counts taken from it character for character. |
| `ks3_statutory.py` | **Absent.** Ownership checked against `docs/ks3/statutory-register.md`, the generated companion. No ID minted; access is read-only. |
| `docs/ks3/mrb-220-build-contract.md`, incl. §5A | **Absent**, as `NOTES-P4-P6.md` §1 and `NOTES-P6-P7.md` §1 both recorded. Worked to `architecture.md`, the gates README, `CLAUDE.md` (which carries the settled FIFA and formula-block law) and the frozen reference set. |
| `docs/ks3/design-reference/` | Present. P6/P7 taken as the current model, since they are the most recent pages built to the settled `CLAUDE.md` law. |
| Coverage manifest | **Absent.** §10 below is therefore delivered here, as P4/P5, P6/P7 and C9 did. |

---

## 2. Statutory ownership

P8 owns three statements over seven slots (ratio 0.43); P9 owns two over three
(0.67). Both are heavily surplus-slot cases, so the compound statements are split
at clause level. Every clause is claimed exactly once.

| Slot | Statements claimed |
|---|---|
| `p8-01 current-and-circuits` | `KS3.P.CUR.01` clauses *"electric current, measured in amperes, in circuits"* and *"current as flow of charge"* |
| `p8-02 series-and-parallel` | `KS3.P.CUR.01` clause *"series and parallel circuits"* |
| `p8-03 current-at-a-junction` | `KS3.P.CUR.01` clause *"currents add where branches meet"* |
| `p8-04 potential-difference` | `KS3.P.CUR.02` clause *"potential difference, measured in volts, battery and bulb ratings"* |
| `p8-05 resistance` | `KS3.P.CUR.02` clause *"resistance, measured in ohms, as the ratio of potential difference (p.d.) to current"* |
| `p8-06 conductors-and-insulators` | `KS3.P.CUR.03` whole |
| `p8-07 building-and-measuring-a-circuit` | **none** — see FLAG 2 |
| `p9-01 charging-by-rubbing` | `KS3.P.STAT.01` clauses *"separation of positive or negative charges when objects are rubbed together"* and *"transfer of electrons"* |
| `p9-02 forces-between-charges` | `KS3.P.STAT.01` clause *"forces between charged objects"* |
| `p9-03 electric-fields` | `KS3.P.STAT.02` whole |

**FLAG 1 — clause-level ownership still has no notation** (third repeat; first
raised as P4 FLAG 1, restated as P6/P7 FLAG 1). `CUR.01` is split three ways,
`CUR.02` two and `STAT.01` two. A gate counting statements per lesson will read
`CUR.01` as claimed three times. Mide's call: the register needs `.a` / `.b`
sub-IDs, or lesson records need `covers_partial`. **This is now the longest-running
open flag in the build and it is blocking a computable coverage report.**

**FLAG 2 — `p8-07` claims no subject-content clause, deliberately.** It is the
unit's INVESTIGATION slot and it teaches Working Scientifically: where each meter
goes and why, fault-finding from a symptom, repeating a reading, planning a fair
test. Every quantity it uses is owned by `p8-01`, `p8-04` or `p8-05`. The
single-source rule requires each statement to have exactly one owner, not each
lesson to own a statement, so this is legal — but a gate that checks the reverse
will fail it. **If a coverage gate requires every slot to own something, `p8-07`
needs either a WS tag it can count or a split of `CUR.02`.**

---

## 3. Formula blocks (MRB-204): triangle, beam, or nothing

> **21 Aug — FIFA is now CFIFA.** All four formula lessons in P8 (`p8-03`,
> `p8-04`, `p8-05`, `p8-06`) were rebuilt to the CFIFA rule in `CLAUDE.md`:
> **C**onvert, **F**ormula, **I**nsert, **F**ine-tune, **A**nswer, five
> click-to-reveal steps instead of four. The C step always appears — where
> nothing needs converting it says so in one sentence. Each lesson now carries
> **two** worked examples and **two** student attempts behind a segmented
> control: one where every reading is already in base units, one where a
> milliamp or millivolt reading has to be divided by 1000 first. The student's
> own attempt commits **four** lines (Convert, Formula, Insert, then number and
> unit) and reveals five. In `p8-06` the bench question's Convert line is
> computed from whatever unit the ammeter is showing — mA, µA, nA or pA — so an
> insulator specimen converts correctly rather than being waved through.
> The Answer note in every conversion case names the size of the error the
> unconverted number would have produced.
>
> **Second pass, same day.** The `Nothing to convert` / `Convert first` labels
> were removed from the student's attempts — they gave away the very decision the
> C step exists to test. The attempts are now `Question 1` and `Question 2` and
> carry no hint; the labels remain on the worked examples, where the point is to
> show the contrast. The attempts were also converted from pick-the-line to
> **write-it-out**: five inputs, one per CFIFA step, with mono placeholders
> (`anything to convert?`, `R = …`, `R = … ÷ …`), a **Check your working**
> button that unlocks on five written lines, and a reveal that quotes the
> student's own line under each model line with an **I had this** self-mark and
> an `n of 5 lines ticked` tally. Seven of the eight attempts in P8 are
> write-it-out; `p8-06`'s second question keeps the pick-the-line variant
> (`mode: 'pick'`) so the lighter form stays in circulation.

Three of the ten lessons carry a formula block. Each has one relationship, alone,
in its own block, in the locked order: diagram, tap-to-reveal CFIFA, then the
student's own five lines on live bench numbers, before anything independent is
asked.

| Lesson | Relationship | Figure | Why |
|---|---|---|---|
| `p8-01` | none | **no block** | A model lesson. Nothing to calculate; charge in coulombs is GCSE. |
| `p8-02` | none | **no block** | A contrast. Both rules it teaches are qualitative. |
| `p8-03` | `I = a + b` | **part–whole bar**, with cover buttons | A sum. A triangle would teach a product that does not exist. The three-branch generalisation `I = a + b + c` is the one permitted extra display line. |
| `p8-04` | `V = a + b` | **part–whole bar**, with cover buttons | Also a sum — the series loop shares the battery's p.d. out. The parallel condition `a = b = V` is the extra display line, and the physics needs it because the same quantity behaves oppositely in the other arrangement. |
| `p8-05` | `V = I × R` | **triangle** | A genuine product, and the statutory statement defines resistance as this ratio. The unit-pairing line `1 Ω is 1 V for each 1 A` is the extra display line. |
| `p8-06` | none | **no block** | See FLAG 3. |
| `p8-07` | none | **no block** | A method lesson. |
| `p9-01` | none | **no block** | See FLAG 4. |
| `p9-02` | none | **no block** | Coulomb's law is A level; `STAT.01` is qualitative. |
| `p9-03` | none | **no block** | Field strength as force per unit charge is GCSE; `STAT.02` says *the idea of* electric field. |

**FLAG 3 — `p8-06` computes a resistance on every state and has no block.** Its
statutory statement says *(quantitative)*, so the bench must divide, and it does:
6.0 V ÷ the ammeter reading, printed line by line in the readout tiles. A block
here would be a second `R = V ÷ I` triangle in the same unit, three slots after
`p8-05`'s. Following the `p6-09` precedent, the block is left out and `p8-05` is
carried as an edge. **If the contract requires a block wherever a page computes,
`p8-06` needs one and it will be a duplicate.**

**FLAG 4 — `p9-01` reports a charge and has no block.** `Q = n × e` is a genuine
product and would take a triangle cleanly, but the coulomb as a unit and the
elementary charge are both beyond this stage, and `STAT.01` names neither. The
bench reports a count of electrons in words and a charge in nanocoulombs as
readouts, with no arithmetic asked of the student. **A reviewer might reasonably
ask for the block or for the nanocoulomb figure to be dropped; the count of
electrons alone would weaken the "equal and opposite" point, which is why both
are there.**

**FLAG 5 — two part–whole bars in one unit, three slots apart.** `p8-03` and
`p8-04` both carry a bar, and the visual similarity is deliberate: current splits
at a junction, p.d. splits round a loop, and the two are the pair of rules
students most often swap. Each block states its own relationship from nothing.
It is still worth a reviewer confirming that the repetition reads as a designed
pairing rather than a copied component.

---

## 4. Where these units must teach from nothing

- **No lesson assumes sequence.** Every cross-lesson reference is an edge in
  *Connects to* or a link inside *Going further*, phrased as an offer.
- **`p8-01`, `p8-02` and `p8-03` each define current from nothing.** Three
  definitions of the same word is deliberate: a school may run P8 in any order,
  and a student arriving at the junction lesson first must not be stranded.
- **`p8-04` restates that the current is the same everywhere in a series loop**
  rather than depending on `p8-01` for it, because the p.d. argument needs it.
- **`p8-05` and `p8-06` each define resistance from nothing**, and `p8-06`
  restates the ratio in its explainer rather than pointing at `p8-05`.
- **`p8-07` restates what each meter is for** rather than assuming `p8-01` or
  `p8-04`, since it is the lesson a teacher is most likely to run first as a
  practical.
- **`p9-02` restates that rubbing separates charge in one clause**, and `p9-03`
  restates induction in one clause, so neither P9 lesson depends on its
  predecessor.
- **`p9-01` names insulators and conductors from nothing**, with `p8-06` as an
  edge, because P9 may be taught before P8.

---

## 5. The benches: one practical each, and the whole state space

| Lesson | Instrument | Reachable states | Notes authored |
|---|---|---|---|
| `p8-01` | One loop, one ammeter, three sockets for it | 4 cells × 2 switch × 3 positions = 24 | 3 branches keyed to **what the loop is doing**: broken at the switch, complete on one cell, complete on more than one. Every branch names the live reading and states that the other two positions give the same. |
| `p8-02` | Two identical bulbs, one 3.0 V battery, rewireable | 2 arrangements × 3 removals = 6 | 4 branches keyed to **arrangement and whether a bulb is out**. All six states covered. |
| `p8-03` | A junction with two branches, three ammeters | 4 components × 4 = 16 | 4 branches keyed to **what the branches do**: nothing flowing, one branch open, branches equal, branches unequal. 1 + 6 + 3 + 6 = 16. |
| `p8-04` | One series loop, one voltmeter, four places for it | 2 batteries × 3 second components × 4 positions = 24 | 4 branches keyed to **what the voltmeter is across**: the battery, both components, a component with a share, the wire link with none. |
| `p8-05` | One component under test, an ammeter and a voltmeter, variable supply | 5 components × 8 supply settings = 40 | 3 branches keyed to **what the ratio does**: low ohmic, high ohmic, and the filament lamp whose ratio climbs. |
| `p8-06` | A test gap on a fixed 6.0 V supply | 7 specimens × 2 lengths = 14 | 4 branches keyed to **band**: the copper short-circuit case, conductor, poor conductor, insulator. The length control adds a sentence to every non-copper state. |
| `p8-07` | One lamp, two meters to place, one connection to tighten | 2 × 2 × 2 = 8 | 5 branches: loose connection (which dominates), correct, ammeter shorting the lamp, voltmeter strangling the loop, both wrong. |
| `p9-01` | Two dry insulators, rubbed | 7 × 7 materials × 20 strokes = 980 | 3 branches keyed to **which way the electrons go**: same material (none), left above right, left below right. Every branch names the live count, both charges and the two controls that set them. |
| `p9-02` | Two spheres on insulating stands | 3 × 3 states × 17 separations = 153 | 4 branches keyed to **what the pair does**: nothing, repel, attract, attract weakly by induction. |
| `p9-03` | A field map with a movable test point | 4 arrangements × 25 positions = 100 | 5 branches: on top of a charge (no value), single positive, single negative, dipole, two positives — the last with its own null-point branch at the exact mid-point. |

Deliberate consequences of the standing audit findings:

- **No bench narrates its own controls.** No lead sentence says which readout to
  watch. Every lead is either the physical set-up or an instruction.
- **No figure the instrument computes is hard-coded in prose.** Every number in
  every bench sentence is interpolated from the same state the readouts use. The
  worked examples are the only fixed numbers, and each is a stated scenario in
  its own heading.
- **Every comparative label is computed.** `p8-02`'s brightness words, `p8-03`'s
  split ratio, `p8-05`'s verdict on the ratio, `p8-06`'s conductor/insulator
  band and comparison with copper, `p9-02`'s strength word and `p9-03`'s
  direction word are all derived from the live values, never authored per control.
- **Every control is modelled and its effect stated.** `p8-01`'s meter position
  has an authored consequence — that the reading does not change — which is the
  point of the lesson. `p8-06`'s length control names the tenfold factor.
- **Every quantity the lesson names is readable as a number.** Currents in A, mA,
  µA, nA and pA; p.d. in V; resistance in Ω, kΩ, MΩ, GΩ and TΩ; separations in
  cm; charges in nC; electron counts in words.
- **One practical per bench.** `p8-01`'s symbol key, `p8-02`'s comparison table,
  `p8-05`'s two-component results table, `p8-06`'s log chart, `p8-07`'s
  troubleshooting table, `p9-01`'s triboelectric ladder, `p9-02`'s nine-case
  matrix and `p9-03`'s three-field figure are all figures, not instruments.
- **Log scales where the data demands them.** `p8-06`'s resistances span fourteen
  decades and take a chart where every mark is a thousand times the last; it says
  so on the face of the drawing. Nothing else in these units needs one.

---

## 6. Safeguarding

`p8-06` carries the block. It names **Childline, 0800 1111**, inline, in small
type, at the bottom edge above the legal line, and says the service is free, open
at any hour and does not require a name. This is the only page in the two units
that touches a risk in the student's own home: the lesson ends on why a cable is
copper inside and plastic outside, and mains cables and sockets are the place
where that stops being an abstraction.

Two judgements a reviewer should ratify:

- **`p8-07` does not carry the block.** It is a practical-safety lesson, but the
  whole practical runs on cells and the only hazard modelled is a meter being
  damaged. No student's body is at risk on the page.
- **`p9-03` does not carry the block**, although its *Going further* explains why
  a car is safe in a thunderstorm and rung 4 asks for it. That is safety
  information a student is being given, not a risk they are being asked to
  disclose, and adding the block would dilute a block that means something.

---

## 7. Misconception ids — pre-allocated, not minted

`docs/ks3/misconception-register.md` lists no opened family for electricity or
electrostatics, and states that nothing in an authored lesson may cite an
unopened family. Access here is read-only, so **no id is cited on any page.**
Ranges are reserved below so parallel batches cannot collide, with the last of
each four as the named spare.

| Lesson | Range | Spare |
|---|---|---|
| `p8-01` … `p8-07` | `CIRC-01` … `CIRC-28`, four per lesson in slot order | last of each four |
| `p9-01` … `p9-03` | `STAT-01` … `STAT-12`, four per lesson in slot order | last of each four |

Authored so far, awaiting minting:

| Proposed id | Statement, as a student holds it | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `CIRC-01` | The bulb uses up the current, so less comes back than went in. | `gate-after-the-bulb`, `r1` | `s-think`, `s-loop`, `r1` | `p8-01` |
| `CIRC-02` | The electricity has to travel from the cell to the bulb, so there is a delay. | `hook-torch`, `r2` | `s-think`, `r2` | `p8-01` |
| `CIRC-05` | In parallel the current is shared out, so each bulb is dimmer. | `gate-parallel-total` | `s-think`, `s-bench` | `p8-02` |
| `CIRC-06` | In series the first bulb gets the current first, so it is brighter. | *(none)* | `s-think`, `s-bench` | `p8-02` |
| `CIRC-07` | Two bulbs in series are each as bright as one, because the battery has not changed. | `r2` | `r2`, `s-bench` | `p8-02` |
| `CIRC-09` | At a junction the current halves, because there are two ways to go. | `gate-lamp-and-buzzer`, `r1` | `s-think`, `s-junction`, `r1` | `p8-03` |
| `CIRC-10` | Adding a second branch means less current for the first one. | `r2` | `s-think`, `r2` | `p8-03` |
| `CIRC-13` | Voltage flows round the circuit and is used up. | *(none)* | `s-think`, `s-volt` | `p8-04` |
| `CIRC-14` | A voltmeter goes in the loop, like an ammeter. | `r1` of `p8-07` | `s-think`, `s-volt` | `p8-04` |
| `CIRC-15` | A reading equal to the battery's p.d. across one component must be a fault. | `r2` | `r2`, `s-volt` | `p8-04` |
| `CIRC-17` | Resistance is a force pushing back against the current. | *(none)* | `s-think` | `p8-05` |
| `CIRC-18` | A component has one resistance, whatever you test it on. | `gate-10-ohm-twice`, `r2` | `s-think`, `s-bench`, `r2` | `p8-05` |
| `CIRC-21` | An insulator blocks current completely — none at all gets through. | `gate-plastic-ruler`, `r2` | `s-think`, `s-test`, `r2` | `p8-06` |
| `CIRC-22` | Materials are either conductors or insulators, with nothing between. | `hook-cable` | `s-think`, `s-scale` | `p8-06` |
| `CIRC-25` | If a meter reads zero the meter is broken. | `hook-two-pairs` | `s-think`, `s-wire`, `s-fault` | `p8-07` |
| `CIRC-26` | It cannot matter which way round the leads go on a meter. | *(none)* | `s-think` | `p8-07` |
| `STAT-01` | Rubbing creates charge. | `r2` | `s-think`, `s-rub`, `r2` | `p9-01` |
| `STAT-02` | A positive object has had positive charge added to it. | *(none)* | `s-think`, `s-rub` | `p9-01` |
| `STAT-03` | Only one of the two objects ends up charged. | `hook-rod-and-duster` | `hook-reveal`, `s-rub` | `p9-01` |
| `STAT-05` | The rod picks up the paper, so the paper must be charged. | `gate-neutral-sphere`, `r1` | `s-think`, `s-spheres`, `s-matrix`, `r1` | `p9-02` |
| `STAT-06` | They have to touch, or the air has to carry it. | `hook-balloons` | `s-think` | `p9-02` |
| `STAT-09` | A field only exists when something is in it to feel it. | *(none)* | `s-think`, `s-field` | `p9-03` |
| `STAT-10` | The air in the gap must be carrying the force. | `hook-comb-and-water` | `s-think`, `hook-reveal` | `p9-03` |
| `STAT-11` | The field is strongest half-way between two like charges. | `gate-midpoint`, `r2` | `s-field`, `r2` | `p9-03` |

Six entries have no `elicited_by`, which §5.3 allows: nothing on those pages asks
the student to commit to the belief, and each is confronted because it sits
underneath one that is elicited.

---

## 8. Distractors (MRB-177), and hedges that are load-bearing

Every ladder distractor in the ten lessons is a **wrong rule in the correct
answer's own shape**. Five worth pointing at:

- `p8-01` r1 option B is *"0.12 A — the bulb uses up about half of it"*. The
  premise (the bulb takes something) is correct and the thing taken is misnamed,
  which is exactly why students reach for it.
- `p8-02` r2 option D is the **right verdict with the wrong rule** — the bulbs are
  dimmer, but because "the battery divides its charge" rather than because the
  loop got harder to push through — and is marked wrong because the reasoning is
  what is assessed.
- `p8-03` r1 option B, *"1.55 A — add all three readings together"*, adds the
  parts to a whole that was already given. It is the single most common wrong
  answer to a three-branch junction question.
- `p8-05` r1 option D is the **right number with the wrong unit**, 5.0 V for a
  resistance, which is the standard slip when the division is done without
  tracking what volts ÷ amps leaves.
- `p9-02` r1 option B, *"It must be positively charged, because unlike charges
  attract"*, is a true rule applied to a case it cannot settle — the whole point
  of the lesson's closing test.

Rungs 3 and 4 are written as checks on an answer, not recipes: each criterion
names a thing that must be *present in what you wrote*, and every rung 4 is
reachable from the lesson alone.

Hedges that must not be tidied:

- **"about"** on every stated resistance in `p8-06`, every triboelectric
  prediction in `p9-01` and every relative strength in `p9-02`.
- **"in practice"** on the word *insulator* in `p8-06`'s verdict tile. Removing it
  turns a practical judgement into a claim of zero conduction, which the same
  page's own reading contradicts.
- **"typical"** on the seven specimen resistances in `p8-06` and on every rating
  in `p8-04`'s figure.
- **"almost"** on every statement that a voltmeter draws no current, that an
  ammeter has no resistance, that a battery has none, and that the field inside a
  conductor is zero. All four are approximations and all four are stated as such
  in the legal line.
- **"of that lamp, at that moment, at that temperature"** in `p8-05`. The
  qualifier is the content of the lesson's second misconception.
- **"roughly where useful conduction gives out"** on `p8-06`'s chart boundary,
  with *no sharp line* written into the same label.
- **"likely outcome, not a certainty"** for `p9-01`'s transfer direction. Real
  triboelectric series disagree and the legal line says so.
- The `.ks3-legal` line on all ten pages discloses what the bench leaves out and
  which numbers are conventions rather than measurements.

---

## 9. Flags for review

1. **FLAG 1–5 above** are the substantive ones: clause-level ownership (data
   model, third repeat), `p8-07` owning nothing, `p8-06` computing without a
   block, `p9-01` reporting a charge without one, and two part–whole bars three
   slots apart.
2. **FLAG 6 — `p8-05`'s filament-lamp model is a straight line and a real one is
   a curve.** Resistance is taken as rising steadily from about 6 Ω at 1.5 V to
   about 18 Ω at 12 V. The values are typical of a small lamp and the shape is
   wrong in detail; the legal line says so. Correcting it to a curve would change
   the figure in the same lesson and both must move together.
3. **FLAG 7 — `p8-06` prints a current for a bare copper wire across a 6 V
   supply.** The division gives 120 A, which no school supply will deliver. The
   bench reports it and the note and legal line both call it a short circuit
   rather than a measurement. **A reviewer may prefer the state removed; it is
   kept because "copper is the reference" is what the whole chart is measured
   against, and a blank there would be worse.**
4. **FLAG 8 — `p9-01`'s charge model has no ceiling.** Twenty strokes of hair
   against PVC gives about 38 nC, which is on the high side of a rubbed rod but
   not absurd; the model would keep climbing if the slider went further. A real
   charge stops rising because it leaks and because the air eventually breaks
   down. The legal line says so; the model does not implement it.
5. **FLAG 9 — `p9-02`'s induced-attraction coefficient is chosen, not measured.**
   The distance dependence is right in kind (it falls faster than the
   inverse-square force between two charges) and the coefficient is set so the
   effect is readable on the same scale. Stated in the legal line. **Worth a
   reviewer's ruling on whether a chosen coefficient is acceptable where the
   alternative is a state that always reads zero.**
6. **FLAG 10 — the ohm sign is used as U+03A9 GREEK CAPITAL LETTER OMEGA, not
   U+2126 OHM SIGN.** The shipped font subsets carry the Greek omega and fall back
   on the ohm sign, so U+2126 would silently change typeface. Checked by
   measurement before authoring. `µ` (U+00B5), `−` (U+2212), `×` and `÷` are also
   present and used. **Subscript digits (U+2081 and up) are NOT present in
   Bricolage Grotesque or Instrument Sans**, which is why `p8-03` and `p8-04`
   label their bar parts `a` and `b` rather than with subscripts. This should go
   into the design-system font note.
7. **FLAG 11 — `--ks3-data` still does not exist** (fourth repeat, first raised as
   P4 FLAG 1). These pages use `--ks3-blue-light` for readings and live marks on
   ink-dark blocks and `--ks3-accent` / `--ks3-accent-tint` on cream, always with a
   word in the state so hue is never the only channel. Amber appears only in
   misconception blocks, the FIFA reveal eyebrow, `p8-07`'s LOOSE label and
   `p9-03`'s test-point marker. **Either the token needs adding or audit law 9
   needs amending.**
8. **Four rail stops on every page**, per the brief and matching B9–B11, P4/P5 and
   P6/P7. `NOTES-C9.md` §10 records five citing the same MRB-249; if five is
   current this is a one-line change per lesson.
9. **Practical risk.** Nothing in P8 needs a risk assessment beyond ordinary
   classroom practice; the one hazard worth a teacher's eye is a shorted ammeter,
   which `p8-07` describes rather than instructs and tells the student to answer
   by opening the switch. P9 is entirely dry insulators and hanging spheres.
   `p9-03`'s comb-and-water hook is a home demonstration and is described, not
   instructed.
10. **Nothing was committed to the repo.** Read-only access, as instructed: no
    branch, no commit, no register edit, and no prompt written for Code was run.

---

## 10. For Code — component families registered

**New families minted by this group**

| Family | Debuts in | What it is |
|---|---|---|
| `circuit-loop` | `p8-01` | A rectangular loop drawn as one base path with gaps at every component position, plus a computed fill path that bridges the gaps nothing occupies. Cell plates, switch lever, bulb glow and meter position are all computed. Data: `{cells, closed, slot}`. **This is the family the whole of P8 is built on.** |
| `symbol-key` | `p8-01` | The fixed eight-symbol figure — cell, battery, lamp, switch, ammeter, voltmeter, resistor, variable resistor — each a small literal SVG in its own card with a name and a one-line note. |
| `two-arrangement-loop` | `p8-02` | The same two bulbs drawn either as one series loop or as two parallel branches, switched wholesale by `<sc-if>` between two literal SVGs, with bulb state (lit / present-and-dark / removed) computed per bulb. |
| `junction-bench` | `p8-03` | A battery feeding two parallel branches, each with its own ammeter and a component slot, plus a main ammeter. Component shapes are built as one stroked path and one filled path per branch, so lamp, resistor, buzzer and empty socket all live in the same two attributes. |
| `beam-part-whole` | reused from `p6-02` | The part–whole bar with cover buttons. Reused by `p8-03` and `p8-04`; **`p8-03` is the first use with unequal parts**, so the split point is a geometry value rather than a half. |
| `voltmeter-tap` | `p8-04` | A series loop with a voltmeter at a fixed position and two computed lead paths routed at two different y levels so they never cross, plus tap dots at the measured points. Four positions: across the battery, across each component, across both. |
| `formula-triangle` | reused from `p5-01` | Unchanged. `p8-05` only. |
| `component-under-test` | `p8-05` | A loop with a variable supply, an ammeter in series and a voltmeter across a swappable component; the component is one computed path plus one computed style, so a thick wire, a thin wire, a resistor and a lamp are the same element at different stroke widths and shapes. |
| `test-gap` | `p8-06` | Two crocodile clips with a specimen block between them on a fixed supply, and a current arrow whose stroke width, dash and presence are all computed from the order of magnitude of the current. **Refuses to draw an arrow below a microamp.** |
| `decade-bars` | `p8-06` | A fixed chart of seven bars on an axis where every mark is a thousand times the last, with a dashed boundary line and a label that says there is no sharp line. All geometry computed at build time from logarithms. Related to `p6-08`'s `log-range-axis` but horizontal and fixed. |
| `meter-placement` | `p8-07` | One loop with two meters whose positions are controls; meter centres, lead paths, tap dots, bridged gaps and a loose-joint pair of contact dots are all computed from three booleans. |
| `fault-table` | `p8-07` | The fixed six-row troubleshooting figure: symptom, likely cause, what to check first. |
| `transfer-pair` | `p9-01` | Two object blocks with a computed electron-transfer arrow between them, computed rows of + or − signs inside each (count scaled to the charge, capped at six), and a dot train in the gap. Draws nothing at all when the two materials match. |
| `tribo-ladder` | `p9-01` | The fixed seven-material ordering, as HTML cards with a numbered badge and an inline-SVG arrow spanning the list. |
| `charge-pair` | `p9-02` | Two spheres on insulating stands at a computed separation, with signs inside, induced signs on the near and far faces of a neutral sphere, a dimension line, and force arrows whose direction (tail-out for repulsion, head-in for attraction) and length are computed. |
| `state-matrix` | `p9-02` | The fixed three-by-three figure of every charge combination, with the verdict in each cell. |
| `field-grid` | `p9-03` | A vector field sampled on a 13 × 7 lattice and emitted as **one** path string: every arrow's direction, length, and head are computed from the summed inverse-square field, and points within a set distance of a charge are omitted. A larger arrow marks the movable test point. **This family is why the lesson needs no hand-authored field lines.** |
| `field-triple` | `p9-03` | The fixed three-card figure — gravitational, magnetic, electric — each a small two-body diagram with a dashed gap and a pair of equal opposite arrows. |

**Reused unchanged from B1–P7**: `ks3-nav`, the top and side progress rails,
`ks3-hook` with `ks3-options`, `ks3-explainer`, `ks3-block ks3-dark ks3-practical`,
`[data-key-fact]`, `ks3-misconception`, `ks3-ladder` with two marked and two
self-marked rungs, `ks3-keynote`, `ks3-layer`, `ks3-endmatter`, `ks3-legal`,
`beam-part-whole`, `formula-triangle`, `fifa-reveal`, `fifa-scaffold`,
`safeguard-block`.

**Notes for the generator**

- **Live labels on a diagram are HTML, not `<text>`.** Every value label in these
  ten pages is an absolutely-positioned `<span>` over a `position: relative`
  wrapper whose percentages match the viewBox. Fixed captions stay as literal
  `<text>`. Attribute holes (`d`, `cx`, `cy`, `width`, `transform`) are
  unaffected. The `<span>`-in-SVG failure is silent, so this is not optional.
- **No `<sc-for>` inside an `<svg>` anywhere.** Repeated marks — cell plates,
  charge signs, grid arrows, contact dots, meter leads — are built as one path
  string in `renderVals()`.
- **Circles that need to be part of a computed path are drawn as two arcs**
  (`a r r 0 1 0 …`), not as `<circle>`, so a component's whole shape can live in
  one attribute. `<circle>` is used only where the centre itself is the computed
  value.
- All instruments are DOM and inline SVG. No canvas, no timers, no animation
  loop, no `Math.random()` anywhere in the group.
- Every arrow, tick and cross is inline SVG. No `→`, `✓` or `✕` character appears
  in any of the ten files; a build check for those three characters passes.
- Props: `showDraft` only, as everywhere else in the build.
- Every page is a standalone `.dc.html` with its own `support.js` and `_ds`
  folder alongside it, matching P4 through P7.
- Forward and back links use the `.html` form of the slug, matching P5–P7.
