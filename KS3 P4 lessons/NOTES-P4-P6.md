# NOTES — KS3 Physics P4 / P5 / P6

**P4 and P5 complete.** All nine P4 slots and all four P5 slots are authored
(`p4-01` … `p4-09`, `p5-01` … `p5-04`), which is thirteen of the twenty-two slots
in the group. P6 (nine slots) remains. This file is the
running record for the whole three-unit group and is updated with each batch,
so the sections below are complete for what exists and marked *pending* for
what does not.

---

## 1. Recon: what was and was not available

| Input the brief names | State in this project |
|---|---|
| `ks3_data/structure.py` | Present. Slugs, titles, families and lesson counts taken from it character for character. |
| `ks3_statutory.py` | **Absent.** Ownership was checked against `docs/ks3/statutory-register.md`, the generated companion. No ID was minted; access is read-only. |
| `docs/ks3/mrb-220-build-contract.md` | **Absent**, as `docs/ks3/gates/README.md` recorded on 17 Aug and `NOTES-C9.md` §9 repeated on 18 Aug. Worked to `architecture.md`, which declares itself law and self-contained, plus the gates README and the frozen reference set. |
| `docs/ks3/design-reference/` | Present — `KS3 Reference Set (offline).html`. |
| `docs/ks3/audits/2026-08-18-ks3-biology.md` | **Absent.** The audit's findings were taken from the summary in the brief. Where the summary and the shipped code disagree, the disagreement is flagged in §9 rather than guessed at. |
| Coverage manifest | **Absent.** §10 below is therefore delivered here, as C9 did. |

---

## 2. Statutory ownership — how eleven statements were spread over nine slots

P4 owns eleven statements (`docs/ks3/statutory-register.md`, ratio 1.22). Three
of them are compound bullets that name several ideas in one line, and splitting
those across lessons is unavoidable at nine slots. Each **clause** is claimed
exactly once; no clause is claimed twice.

| Slot | Statements claimed |
|---|---|
| `p4-01 what-a-force-is` | `KS3.P.FORCES.01` whole; `KS3.P.FORCES.05` clause *"forces measured in newtons"* |
| `p4-02 drawing-and-adding-forces` | `KS3.P.FORCES.02` clauses *"using force arrows in diagrams"* and *"adding forces in 1 dimension"* |
| `p4-03 balanced-and-unbalanced` | `KS3.P.FORCES.02` clause *"balanced and unbalanced forces"*; `KS3.P.BAL.01` whole |
| `p4-04 what-forces-do-to-motion` | `KS3.P.FMOT.01` whole; `KS3.P.FMOT.02` whole |
| `p4-05 friction` | `KS3.P.FORCES.04` clause *"with rubbing and friction between surfaces"* |
| `p4-06 air-and-water-resistance` | `KS3.P.FORCES.04` clauses *"with pushing things out of the way"* and *"resistance to motion of air and water"* |
| `p4-07 moments` | `KS3.P.FORCES.03` whole |
| `p4-08 springs-and-hookes-law` | `KS3.P.FORCES.04` clause *"associated with deforming objects; stretching and squashing – springs"*; `KS3.P.FORCES.05` clause *"measurements of stretch or compression as force is changed"*; `KS3.P.FORCES.06` whole; `KS3.P.FORCES.07` whole |
| `p4-09 non-contact-forces` | `KS3.P.FORCES.08` whole |

**FLAG 1 — clause-level ownership has no notation in the register.** The register
records ownership per *statement*, per *unit*. Splitting `FORCES.04` and
`FORCES.05` across lessons is the only way nine slots can carry eleven
statements, and every KS3 scheme in the wild does the same, but the data model
in `architecture.md` §4.4 has no sub-index for a clause. Either the register
needs `.a` / `.b` sub-IDs or lesson records need a `covers_partial` field.
Until then a build gate counting statements per lesson will read `FORCES.04` as
claimed three times. **This is a data-model question, not a science one, and it
is Mide's call.**

P5 (ratio 0.75) and P6 (ratio 0.67) are the opposite problem: fewer statements
than slots. P5's three statements are allocated as follows, and only `PRES.02`
is split — it names two different physical ideas in one line and has to be.

| Slot | Statements claimed |
|---|---|
| `p5-01 pressure-force-over-area` | `KS3.P.PRES.03` whole |
| `p5-02 pressure-in-liquids` | `KS3.P.PRES.02` clause *"pressure in liquids, increasing with depth"* |
| `p5-03 upthrust-floating-and-sinking` | `KS3.P.PRES.02` clause *"upthrust effects, floating and sinking"* |
| `p5-04 atmospheric-pressure` | `KS3.P.PRES.01` whole |

**FLAG 9 — the register expects a P5 `hydraulics` lesson that has no slot.**
`misconception-register.md` routes `ENERGY-11` (force multiplication is free
energy) to "P4 `moments`, P5 `hydraulics`". `structure.py` gives P5 four slots
and none of them is hydraulics. `p5-01` therefore confronts `ENERGY-11` in its
*Going further* — the hydraulic jack, with the distance traded explicitly
against the force — rather than leaving the register pointing at nothing.
**Either the register entry needs re-pointing at `p5-01`, or P5 needs a fifth
slot; it cannot stay as it is.**

---

## 3. MRB-204 on a physics page — how the formula blocks are built

MRB-204 had never been exercised on physics. Every quantitative or
relationship-bearing lesson in this group carries **one formula block per
relationship, alone**, containing three things in this order:

1. **A drawn diagram** — the relationship, drawn, with its labels inside the
   component. Every arrow inside a formula block is an SVG path with its own
   `<text>` label; no `→` character appears anywhere in the group.
2. **A tap-to-reveal worked example** — FIFA, four steps, revealed one at a
   time from `Step 0 of 4`. One line of maths and one sentence per step.
3. **A scaffold the student fills** on the numbers their own bench is showing,
   committed line by line before the four steps open.

Nothing independent is asked until all three have happened.

### Triangle or beam — the ruling applied, lesson by lesson

**Triangle for products only.** A triangle asserts `A = B × C`, and putting one
over a sum teaches a relationship that does not exist.

| Lesson | Relationship | Figure | Why |
|---|---|---|---|
| `p4-02` | resultant = bigger − smaller | **beam** (three aligned bars, 17.5 px per newton) | A difference. The lower two bars fill the top one exactly, which is the fact being taught. |
| `p4-03` | upward force = weight; resultant = weight − upward force | **beam** (two panels, 4 px per newton) | An equality and a difference. Neither is a product. |
| `p4-04` | none | **no formula block** | `FMOT` is qualitative only in statute. The bench works without a quantity beyond the measured gate readings, so no quantity was invented. |
| `p4-05` | none | **no formula block** | Friction is qualitative in statute. The bench measures it in newtons and sets two readings side by side; no relationship was invented in order to have something to put in a triangle. |
| `p4-06` | none | **no formula block** | The quantitative content is the balance of weight against resistance, which the bench already draws as two arrows and a leftover. A fixed four-stage figure carries the sequence instead. |
| `p4-07` | moment = force × distance | **triangle** | A genuine product — the first legitimate triangle in the unit, and the only one in P4. The block says so on the page. |
| `p4-08` | extension ∝ load | **beam plus a graph** | A proportionality read off a straight line, not a three-quantity product. The beam shows three equal helpings; the graph shows the same fact and the bend where the law gives out. |
| `p4-09` | none | **no formula block** | A classification. Nothing to calculate. |
| `p5-01` | pressure = force ÷ area | **triangle** (force at the apex, pressure and area beneath) | A product rearranged. The page says so on its face: the triangle asserts *force = pressure × area*, which is true, and the lesson's own relationship is that product rearranged. |
| `p5-02` | pressure at a depth = weight above ÷ area | **stack** (five one-metre layers of water over 1 m², with the running total beside them) | The new content is where the force comes from — a sum of layers — so the figure is a stack and the arithmetic is `p5-01`'s division. No cover buttons: covering a layer means nothing. |
| `p5-03` | left over = weight − upthrust | **beam** (two panels to one scale: floating, equal; sinking, 17 N left over) | A difference between two opposed forces. No cover buttons. |
| `p5-04` | air pressure = weight of the air above ÷ area | **stack** (five bands of atmosphere, thinning upwards, 101 → 23 kPa) | The same stack as `p5-02` with a squashable fluid, so the rule line drops the proportionality clause — air is not linear with height. |

**FLAG 2 — P4 contains no product until `p4-07`.** Four of the first six
relationships in this unit are additive, which is the trap the brief names:
the reflex is to reach for a triangle because physics has triangles. The first
triangle in the unit group is `moment = force × distance from the pivot`, and
it is worth a reviewer checking that it is the first one they meet. As shipped,
`p4-07` is the only triangle in the nine.

---

## 4. Where P4 must teach from nothing

- **"Moment" arrives in `p4-07`.** B2 `biomechanics-forces-in-the-body` teaches
  *turning effect = force × distance from the joint* and does not use the word,
  deliberately. `p4-07` therefore introduces the word, the pivot and the
  relationship from nothing. It carries the B2 lesson as an edge in *Connects
  to* and as one link inside *Going further*, phrased as an offer rather than a
  recap — never as a sentence assuming it has happened.
- **`p4-09` re-states the contact/non-contact split rather than referring back.**
  `p4-01` already draws the distinction. `p4-09` teaches it as a classification
  from first principles, and its sorter includes air resistance precisely
  because that is the card a student who has only half-heard `p4-01` gets wrong.
- **No lesson assumes sequence.** `p4-01` has no *Before this lesson* section at
  all, and every reference to another lesson in the group is a link in
  *Connects to* / *Next in this unit*, phrased so it reads correctly whether or
  not the student has been there. `p4-04` links to `p3-01 speed` as an edge; it
  does not say "you have met speed".
- **`p4-03` and `p4-04` each stand alone on balance.** `p4-03` teaches balanced
  and unbalanced; `p4-04` teaches what a resultant does. Each re-establishes
  the term it needs in one clause rather than referring back.

---

## 5. The benches: state space and notes

Every bench state that can be reached carries an authored note, including the
on-load state and every zero.

| Lesson | Instrument | Reachable states | Notes authored |
|---|---|---|---|
| `p4-01` | Interaction board | 5 cases × (unopened + 3 picks) | 15 opened-state notes + the unopened state, which shows the question and no diagram |
| `p4-02` | Sledge on ice | 13 × 13 slider pairs | 5 authored branches keyed to **which sliders are non-zero**: both zero, right only, left only, equal, unequal — the unequal branch names the two sizes it is holding |
| `p4-03` | Support rig | 4 supports × 10 masses | 5 authored branches keyed to **which support is selected** and whether it can match the weight; the paper's failure is its own branch |
| `p4-04` | Trolley and light gates | 4 resultants × 2 durations | 8 authored notes, one per combination |
| `p4-05` | Block and spring balance | 4 surfaces × 4 loads | 4 authored branches keyed to **which surface** is under the block, each interpolating the live readings, plus a second always-present sentence comparing the current load with another load on the same surface |
| `p4-06` | The fall | 4 bodies × 6 speeds | 5 authored branches keyed to **how the resistance compares with the weight**: at rest, still growing, exactly matched, past it, and the parachute case of past-it |
| `p4-07` | Spanner and a tight nut | 4 arms × 10 pulls | 2 authored branches keyed to **whether the moment reaches the nut's 12 N m**, each naming both routes to the threshold with live figures |
| `p4-08` | Loading a spring, with a plotted graph | 11 loads × any recorded subset | 5 authored branches keyed to **where the load sits relative to the limit**: zero, on the line, at the limit, past it, permanently deformed |
| `p4-09` | The sorter | 8 cases × (unlabelled + 4 labels) | 8 authored case notes plus the unlabelled state, which shows the diagram and the gap marker but reveals nothing |
| `p5-02` | Probe in a tank | 3 liquids × 11 depths | 3 authored branches keyed to **depth**: at the surface, shallow, deep — each naming the same depth in another liquid, so the liquid is never the only thing that changed |
| `p5-03` | Five blocks, one tank | 5 blocks × held/free | 3 authored branches keyed to **what the forces do**: floating freely, held under with a leftover upwards, and sinking with a leftover downwards |
| `p5-04` | Up the mountain | 6 heights × 3 objects | 2 authored height branches (sea level, above it) × 3 authored object clauses, so all 18 states carry a note; the sea-level state is its own branch because it is the state everything else is compared with |
| `p5-01` | Block on sand | 3 faces × 10 masses | 3 authored branches keyed to **where the pressure sits relative to the sand's limit**: over it, under it but reachable by turning the block, and under it with no face at that mass able to reach it |

Deliberate consequences of the audit findings:

- **No bench narrates its own controls.** No page says "watch the resultant
  readout". Where a bench block has an intro line at all it is an instruction
  ("Set two pulls. Read one arrow.") or the physical set-up.
- **No figure the instrument computes is hard-coded in prose.** Every number in
  a bench sentence is interpolated from the same state the readouts use. The
  worked examples are the one place fixed numbers appear, and they are a fixed
  scenario stated in the heading, not a claim about the bench.
- **Branch on the thing the lesson teaches.** `p4-03` branches on whether the
  support can supply the weight — not on the mass. `p4-04` branches on the
  direction of the resultant — not on the duration alone.
- **`p4-01` refuses a bar for force size.** Its five cases span 2 N to about
  200 billion billion N. A linear bar cannot carry that, so the sizes are
  printed as values with units and the arrows are drawn at a fixed length; only
  the benches whose ranges are linear (`p4-02`, `p4-03`) draw arrows to scale,
  and both say so in their model-limitation line.

---

## 6. Misconception ids — pre-allocated, not minted

`FORCE` is listed in `docs/ks3/misconception-register.md` as a **suggested,
not-yet-opened** family, and the register states plainly that nothing in an
authored lesson may cite `FORCE`, `BODY` or `ATOM` until they appear in the
file. Access here is read-only, so **no id is cited on any page**. The ranges
below are reserved so the four batches can be authored in parallel without
collision, with a named spare in each.

| Lesson | Range | Spare |
|---|---|---|
| `p4-01` | `FORCE-01` … `FORCE-04` | `FORCE-04` |
| `p4-02` | `FORCE-05` … `FORCE-08` | `FORCE-08` |
| `p4-03` | `FORCE-09` … `FORCE-12` | `FORCE-12` |
| `p4-04` | `FORCE-13` … `FORCE-16` | `FORCE-16` |
| `p4-05` | `FORCE-17` … `FORCE-20` | `FORCE-20` |
| `p4-06` | `FORCE-21` … `FORCE-24` | `FORCE-24` |
| `p4-07` | `FORCE-25` … `FORCE-28` | `FORCE-28` |
| `p4-08` | `FORCE-29` … `FORCE-32` | `FORCE-32` |
| `p4-09` | `FORCE-33` … `FORCE-36` | `FORCE-36` |
| `p5-01` | `PRESS-01` … `PRESS-04` | `PRESS-04` |
| `p5-02` | `PRESS-05` … `PRESS-08` | `PRESS-08` |
| `p5-03` | `PRESS-09` … `PRESS-12` | `PRESS-12` |
| `p5-04` | `PRESS-13` … `PRESS-16` | `PRESS-16` |
| P6 | `WAVE-01` … `WAVE-36`, four per lesson | last of each four |

Authored so far, awaiting minting:

| Proposed id | Statement, as a student holds it | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `FORCE-01` | A moving object has force in it, and the force runs out. | `hook-what-is-a-force` | `s-think` | `p4-01`, `p4-04` |
| `FORCE-02` | A table is not doing anything; it is just there. | *(none — nothing on the page asks for this commitment)* | `s-think` | `p4-01` |
| `FORCE-03` | A force can only act between things that are touching. | `board-paperclip` | `board-paperclip`, `r2` | `p4-01`, `p4-09` |
| `FORCE-05` | The bigger arrow wins, so the object moves at the bigger force. | `hook-sledge` | `s-think` | `p4-02` |
| `FORCE-06` | Force arrows should all be drawn the same length. | `r2` | `s-think` | `p4-02` |
| `FORCE-07` | Forces along a line always add up. | `gate-30-30` | `s-bench` | `p4-02` |
| `FORCE-09` | If something is not moving, there are no forces on it. | `hook-two-books` | `s-think` | `p4-03` |
| `FORCE-10` | Balanced forces mean the object is stopped. | `r2` | `s-think` | `p4-03` |
| `FORCE-11` | Weight in newtons is the same number as the mass in kilograms. | `gate-spring-2kg` | `s-formula` | `p4-03` |
| `FORCE-13` | If something is moving, a force must be pushing it along. | `hook-curling` | `s-think` | `p4-04` |
| `FORCE-14` | A sideways force makes it go sideways instead. | `bench-sideways` | `s-think` | `p4-04` |
| `FORCE-15` | At the top of its flight a thrown ball has no force on it. | `r2` | `r2` | `p4-04` |
| `FORCE-17` | Starting something sliding and keeping it sliding need the same push. | `hook-crate` | `s-bench`, `s-rules` | `p4-05` |
| `FORCE-18` | A smooth surface has no friction. | `gate-carpet-to-wood` | `s-think` | `p4-05` |
| `FORCE-19` | Friction only exists once something is moving. | `r2` | `s-think`, `r2` | `p4-05` |
| `FORCE-21` | Heavier things always fall faster. | `r2` | `s-think`, `r2` | `p4-06` |
| `FORCE-22` | Air resistance is a fixed force, the same at any speed. | `gate-just-stepped-out` | `s-bench` | `p4-06` |
| `FORCE-23` | When the parachute opens you are pushed back upwards. | *(none — nothing on the page asks for this commitment)* | `s-think` | `p4-06` |
| `FORCE-25` | A longer spanner means you are pulling harder. | `gate-swap-spanner` | `s-think` | `p4-07` |
| `FORCE-26` | The distance is measured from where you are standing. | *(none)* | `s-think` | `p4-07` |
| `FORCE-27` | A moment is a force, so it is measured in newtons. | `r1` | `r1`, `s-formula` | `p4-07` |
| `FORCE-29` | Extension is how long the spring is. | *(none)* | `s-explainer`, `s-think` | `p4-08` |
| `FORCE-30` | Double the load always doubles the extension. | `hook-predict-10N` | `s-bench`, `fifa-scaffold` | `p4-08` |
| `FORCE-31` | Past the limit of proportionality the spring snaps. | `hook-predict-10N` | `s-think`, `r2` | `p4-08` |
| `FORCE-33` | A force needs something in between to carry it across. | `hook-balloon` | `s-think` | `p4-09` |
| `FORCE-34` | There is no gravity in space. | `r2` | `s-think`, `r2` | `p4-09` |
| `FORCE-35` | Magnets attract all metals. | *(none)* | `s-three` | `p4-09` |
| `PRESS-01` | A sharp point pushes harder than a blunt one. | `hook-drawing-pin` | `s-think` | `p5-01` |
| `PRESS-02` | Pressure only pushes downwards. | *(none — nothing on the page asks for this commitment)* | `s-think` | `p5-01` |
| `PRESS-03` | Pressure is a force, so it is measured in newtons. | `r1` | `r1`, `s-formula` | `p5-01` |
| `PRESS-05` | More liquid in total means more pressure at the bottom. | `r2` | `s-think`, `r2` | `p5-02` |
| `PRESS-06` | Water is heavier, or packed tighter, deeper down. | `hook-three-holes`, `gate-1m-to-2m` | `s-think` | `p5-02` |
| `PRESS-07` | Pressure in a liquid acts downwards only. | *(none)* | `s-explainer`, `s-bench` | `p5-02` |
| `PRESS-09` | Heavy things sink and light things float. | `r2` | `s-think`, `r2` | `p5-03` |
| `PRESS-10` | Only things that float get upthrust. | *(none — nothing on the page asks for this commitment)* | `s-think`, `s-bench` | `p5-03` |
| `PRESS-11` | Upthrust depends on how heavy the object is. | `gate-pine-vs-steel` | `s-bench` | `p5-03` |
| `PRESS-13` | A vacuum sucks things in. | `hook-crushed-can` | `s-think` | `p5-04` |
| `PRESS-14` | If air pressed that hard we would feel it. | *(none)* | `s-think` | `p5-04` |
| `PRESS-15` | A sealed bag swells at altitude because gravity is weaker. | `gate-sealed-bag`, `r2` | `s-bench`, `r2` | `p5-04` |

`FORCE-02` has no `elicited_by`, which §5.3 allows: nothing on `p4-01` asks the
student to commit to it, and it is confronted because it is the belief sitting
under the first one.

---

## 7. Distractors (MRB-177)

Every ladder distractor in the four authored lessons is a **wrong rule in the
correct answer's own shape** — subject, condition, consequence — not a wrong
number or a vaguer version of the right answer. Two examples:

- `p4-04` rung 1, correct: *"There is a resultant force backwards, against the
  direction of travel."* Distractor: *"There is a resultant force forwards,
  which is running out."* Same shape; the rule inside it is the impetus theory.
- `p4-03` rung 2 option D is the **right verdict with the wrong rule** —
  *"They must be balanced, because balanced forces always mean stopped."* It is
  marked wrong and the correction says why, because the reasoning is the thing
  being assessed.

- `p4-08` rung 1 distractor B is *"10 mm — divide the extension by the load"*,
  which is not a slip: it is the correct first step offered as the whole answer,
  and the correction says exactly that. Distractor D, *"34 mm — add the extra
  4 N on to the 30 mm"*, is the additive rule applied to a proportional
  relationship, which is the single most common wrong shape in this topic.
- `p4-09` rung 2 option C is the **right verdict with the wrong rule** —
  *"the speed of the station cancels out gravity"*. It is marked wrong because
  the reasoning is what is being assessed.

Where an answer requires an order, the word is written into the criterion:
`p4-02` rung 3 criterion 3 reads *"drawn three times as long as"*, not a
drawing instruction, and no ordering answer anywhere in the group relies on a
mark that would announce as punctuation.

---

## 8. Hedges that are load-bearing — do not tidy

- **"about"** on every force size in the `p4-01` interaction board. Those are
  typical values that depend on how hard and how far apart; removing the hedge
  makes twelve false statements.
- **"mass in kilograms × 10 N/kg"** wherever weight appears. Stated in the
  `p4-03` hook, in its formula block, in its key note and in its model line.
- **"at rest and staying at rest"** in the `p4-03` formula step. *At rest* alone
  is not enough: an object momentarily at rest at the top of a throw is at rest
  and the forces on it are not balanced, which is exactly `p4-04` rung 2.
- **"almost nothing changes"** in the `p4-04` hook. A curling stone does slow
  down. Tidying it to "nothing changes" makes the page contradict its own
  rung 3.
- **"just for an instant"** in `p4-04` rung 2. Without it the question is
  ambiguous about whether the ball is being held.
- **"about"** on every terminal speed and weight in `p4-06`, and on the
  estimate of energy lost to friction worldwide in `p4-05`. The skydiver figure
  depends on mass, altitude and posture; the friction figure is a published
  estimate and is written as one.
- **"while the spring obeys Hooke's law"** / **"staying within the straight
  line"** wherever `p4-08` scales a reading up. Without the clause the
  statement is false above 6 N, and the page's own bench disproves it.
- **"at right angles"** on every moment in `p4-07`. The lesson only handles the
  perpendicular case, and the legal line says so; dropping the phrase makes the
  formula wrong rather than simplified.
- **"almost no friction"** in the `p4-09` maglev material. A maglev train still
  has air resistance, which is the point of the rung-4 criteria.
- **"about 100 000 Pa"** for atmospheric pressure in `p5-04`, and *standard-atmosphere*
  on the altitude table. Real pressure moves several kPa with the weather; the
  legal line says so and the hedge is what keeps the six figures honest.
- **"approximate"** on every boiling point in `p5-04`. They are for pure water.
- **"drawn in proportion to each other"** in the `p5-03` legal line. The weight
  arrow is a fixed length and the upthrust arrow is scaled against it, so the two
  compare but neither measures; a minimum length is enforced so a small upthrust
  still draws. Without the sentence the bench looks like a scale drawing.
- **"the atmosphere is pressing on the surface as well"** in the `p5-02` legal
  line. The probe reads gauge pressure, and a reader who does not know that will
  think the tank is at 0 Pa at the surface in an absolute sense.
- **"gives way at 6000 Pa"** in `p5-01`, always with the sand named. Real ground
  has no single failure pressure, and the legal line says the number is fixed so
  that failure is reachable. Dropping the qualifier turns a teaching threshold
  into a claim about soil.
- **"at right angles to the surface"** wherever `p5-01` states the relationship.
  It is the statutory clause *acting normal to any surface*, it is the reason the
  second misconception block exists, and without it the formula is wrong rather
  than simplified.
- **"mass in kilograms × 10 N/kg"** in the `p5-01` bench readout, its scaffold
  and its legal line, as everywhere else in the group.
- The `.ks3-legal` line on all ten pages discloses the model limits: what the
  bench leaves out, and which numbers are conventions rather than measurements.

---

## 9. Flags for review

0a. **P5 has three formula blocks with no cover buttons.** `p5-02` and `p5-04`
   carry a stack of layers and `p5-03` a beam of two opposed forces; none of the
   three can be covered, so none has cover buttons. `CLAUDE.md` was amended to
   record that a part–whole bar keeps its buttons and a balance does not. If a
   reviewer wants covering everywhere, `p5-02` is the only one where it could be
   made to mean anything, and it would have to be a part–whole bar rather than a
   stack.

0. **The formula block was re-specified on 19 Aug and every physics triangle was
   rebuilt to it.** The old pattern carried a sentence per cover state and a
   paragraph justifying the triangle; both are now banned, and the units moved
   from a small mono list to a symbol key with unit pills. Two consequences a
   reviewer should know: `p4-07` and `p5-01` now name their quantities with
   letters (`M`, `F`, `d`; `F`, `P`, `A`) where they previously spelled them out
   inside the triangle, and the *at right angles* qualifier now rides inside the
   symbol key rather than a mono line. The chemistry bar models (`c2-06`,
   `c4-04`) still carry their old per-cover sentence — they were out of scope and
   need the same pass.

1. **`--ks3-data` still does not exist.** Audit law 9 reserves `--ks3-alert` for
   warning and confrontation and directs categories and selection to
   `--ks3-data`. There is no such token in `tokens/shared-tokens.css` or
   `tokens/shared-ks3.css`. These pages therefore use `--ks3-blue-light` for
   selection on ink-dark blocks (physics blue, which the token file marks
   *on ink-dark only*) and `--ks3-accent` / `--ks3-accent-tint` on cream, with a
   word in every state so hue is never the only channel. Amber appears in three
   places only: misconception blocks, the arrow for the force *left over* on the
   `p4-03` rig, and the resultant arrow on `p4-02` — both of which are the
   confrontation the page is built around. **Either the token needs adding or
   law 9 needs amending.**
2. **Four rail stops, per the brief.** `NOTES-C9.md` §10 records *five* stops
   citing the same MRB-249. This group follows the brief's four, matching B9–B11,
   with the misconception block present but unrailed. If five is current, this
   is a one-line change per lesson, not a rewrite.
3. **`p4-04` rung 2 is contested wording, not contested physics.** "At the
   highest point it is not moving" is true of the vertical motion for a single
   instant. It is written with *just for an instant* and with a straight-up
   throw so there is no horizontal component to argue about. A reviewer who
   prefers "momentarily at rest" should say so; the physics is settled.
4. **The `p4-03` sheet of paper has a made-up breaking point of 2 N.** It is
   declared as made up in the model line. It exists so that *unbalanced* is a
   state the student can reach on a support that is not simply absent. If a
   reviewer wants a real number, a sheet of 80 gsm A4 held at two edges is the
   thing to measure, and it will not be a single number.
5. **`p4-04` gate readings are model values, not measurements.** They are what a
   1 kg trolley under a steady 1 N resultant with no friction would give. The
   model line says so and says real readings run lower. The sideways case
   deliberately reports only a speed and a bent path — resolving it into
   components is GCSE and is not done.
6. **`p4-08` carries the group's only risk assessment, and it is the group's
   only instructional prose.** Everywhere else a practical is described, not
   instructed. Finding a limit of proportionality means loading a spring until
   it stops behaving, so that lesson has a five-line amber block: eye
   protection, a padded landing, nothing underneath the hanger, a clamped or
   weighted stand, and loading to destruction as a screened demonstration
   rather than a class activity. This is a deliberate departure from the
   describe-don't-instruct rule and a reviewer should either ratify it or move
   the block into teacher-facing material. Amber is used because audit law 9
   reserves it for warning, which is exactly what this is.
7. **`p4-01` uses "about 200 billion billion N"** rather than standard form.
   The Bricolage and DM Mono latin subsets do not carry superscript digits
   beyond ² and ³, so `2 × 10²⁰` cannot be typeset reliably. Words are used
   instead. If standard form is wanted, the font subsets need extending.
8. **Nothing was committed to the repo.** Read-only access, as instructed: no
   branch, no commit, no register edit, no prompt written for Code was run.

---

## 10. For Code — component families registered

The coverage gate cannot detect a family that was never registered, so every
family minted or reused by this group is listed here.

**New families minted by this group**

| Family | Where it debuts | What it is |
|---|---|---|
| `interaction-board` | `p4-01` | Two named bodies, a force arrow on each drawn from a push/pull branch, a contact-or-gap marker between them, three readout tiles and a note. Data: `{a, b, kind, size, contact, capA, capB, options[], notes[]}`. |
| `force-arrow-strip` | `p4-02` | One-dimensional arrow field: any number of arrows on one axis, each drawn to a single px-per-newton scale with its own label, plus a resultant arrow on a second baseline. Refuses to draw a zero-length arrow and prints `0 N` instead. |
| `beam-part-whole` | `p4-02` | Aligned horizontal bars on one scale with drawn arrowheads and dashed tie-lines, showing that two bars fill a third. The additive counterpart of `formula-triangle`. |
| `beam-opposing` | `p4-03` | Two side-by-side panels, balanced and unbalanced, with vertical arrows on one scale and a third *left over* arrow in the unbalanced panel. |
| `support-rig` | `p4-03` | A load, a selectable support (hatched solid, drawn spring coil whose length tracks the force, intact sheet, torn sheet, nothing), weight and upward arrows drawn to scale, and a leftover arrow when the support cannot match the weight. |
| `gate-run` | `p4-04` | A track with two light gates, a body drawn at a position and offset that follow the case, a dashed path that bends or stops short, a resultant arrow in one of three orientations, and before/after readings. |
| `fifa-reveal` | `p4-02` | The step-at-a-time worked example as a family in its own right: `Step n of 4`, lettered badge, mono label, display maths line, one-sentence note, and a button that disables at four. Reused by `p4-03`. |
| `fifa-scaffold` | `p4-02` | The student's own four lines: two option groups, a number field, a unit `<select>` and (where direction is part of the answer) a direction `<select>`; a commit counter; a dark reveal panel computing the same four lines from live bench state. Reused by `p4-03`, `p4-07`, `p4-08`. |
| `drag-lane` | `p4-05` | Two stacked lanes on one px-per-newton scale, each a block on a textured surface with a pull arrow one way and a friction arrow the other. The surface texture is generated per surface (gloss dashes, plank ticks, carpet loops, grit zigzag). Refuses no arrow: the smallest reading here is 8 N. |
| `fall-balance` | `p4-06` | A falling body with a fixed-length weight arrow down, a resistance arrow up whose length is the weight arrow times the square of the speed fraction, a leftover arrow that flips direction, and speed streaks whose length tracks the fraction. |
| `stage-strip` | `p4-06` | A fixed four-column figure: one body per column, the same weight arrow in each, and a resistance arrow at 0, half, equal and over. All captions literal, no live values — the counterpart to the live bench above it. |
| `formula-triangle` | `p4-07` | The house formula block, rebuilt 19 Aug to the locked pattern in `CLAUDE.md`: words banner, `Cover the one you want`, one cover button per symbol, the triangle in `--ks3-blue-tint` with the covered cell blacked out, the rearrangement in display type, the one-line multiply/divide rule, and a symbol key of badge + name + unit pill. **No prose in the block.** Product relationships only. Applied to `p4-07`, `p5-01`, `p3-01`, `p2-01`, `p2-03` and `b2-04`; `p1-08` keeps its beam and takes the same key. |
| `spanner-rig` | `p4-07` | A hex nut at a marked pivot, a handle drawn to scale in px per metre, a perpendicular force arrow on its own scale, a dimension line between pivot and grip, and a curved turn arrow that is solid when the moment clears the threshold and dashed when it does not. |
| `spring-plot` | `p4-08` | Two figures side by side: a hanging spring whose coil count is fixed and whose pitch stretches with the extension, against a dashed natural-length line; and a graph of extension against load with a dashed line of proportionality, plus points and a joining line built from the readings the student has chosen to record. Points are drawn as arcs in a single `d` attribute rather than `<circle>` elements, so no per-point element is created inside the SVG. |
| `block-on-sand` | `p5-01` | A tray of sand with a fixed grit texture, a block drawn to scale on any of the three faces of one 0.20 × 0.10 × 0.05 m solid, a weight arrow on its own scale above it, a footprint dimension line under it, and a sand surface that either runs straight or opens into a trough with the original level dashed behind it. Data: `{faces[], mass, limit}`. |
| `liquid-column-probe` | `p5-02` | A tank drawn to scale in depth, a probe on a cable at a chosen depth, the column of liquid above the probe face shaded as its own band, a four-way arrow rosette at the face for *equal in every direction*, and a depth dimension line. Data: `{liquids[], depth, faceArea}`. |
| `stack-of-layers` | `p5-02` | A fixed figure: equal layers of fluid over one square metre, each labelled with its own weight, and the running total beside each boundary. Reused by `p5-04` with unequal bands, because air is squashable. The vertical counterpart of `beam-part-whole`. |
| `float-tank` | `p5-03` | A tank, a one-litre block drawn at its floating depth or held under, a fixed-length weight arrow and a proportional upthrust arrow, and a leftover word. Data: `{blocks[], holding}`. |
| `altitude-column` | `p5-04` | A 12 km column with the air still above the marker shaded, fixed height ticks, a marker at the chosen height, and a case panel drawn beside it — a bag swelling in proportion, a pan with a live boiling point, or a barometer dial whose needle is an attribute-hole rotation. |
| `force-sorter` | `p4-09` | Eight cases, two bodies drawn touching or apart depending on the case, a gap marker or a contact marker, a force arrow, and four label buttons that lock on commit. The unlabelled state shows the diagram and reveals no verdict. |

**Reused unchanged from B1–C10**: `ks3-nav`, the top and side progress rails,
`ks3-hook` with `ks3-options`, `ks3-explainer`, `ks3-block ks3-dark ks3-practical`,
`[data-key-fact]`, `ks3-misconception`, `ks3-ladder` with two marked and two
self-marked rungs, `ks3-keynote`, `ks3-layer`, `ks3-endmatter`, `ks3-legal`.

**Notes for the generator**

- **Live labels on a diagram are HTML, not `<text>`.** A `{{ hole }}` used as text
  content inside an SVG `<text>` element renders nothing: the runtime wraps
  interpolated text in a `<span>`, and a `span` created in the SVG namespace is
  not a renderable element. Every diagram in this group therefore sits in a
  `position: relative` wrapper with its value labels as absolutely-positioned
  HTML `<span>`s whose `left`/`top` percentages match the viewBox coordinates;
  where the label moves with the data the whole style string comes from
  `renderVals()`. Fixed captions (`WEIGHT`, `GATE 1`, `PULL RIGHT`) stay as
  literal `<text>`, which renders correctly. Attribute holes are unaffected.
  **This is a runtime limitation worth a line in the build contract** — it costs
  a rewrite per instrument if it is discovered late, and it fails silently.
- All instruments are DOM and inline SVG. No canvas, no timers, no animation
  loop, no `Math.random()` anywhere in the group.
- Every arrow, tick and cross is inline SVG. No `→`, `✓` or `✕` character
  appears in any file.
- `p4-02` and `p4-03` scaffolds read their numbers from bench state, so the
  reveal is never able to contradict the instrument above it.
- Props: `showDraft` only, as everywhere else in the build.
- `p4-01` has no back link — it is the first slot in the unit. Every forward
  link in P4 now resolves to an authored slot; `p4-09` has no forward link
  inside the unit and points sideways instead.
- **`p4-08` records readings rather than computing them all.** The graph only
  shows points the student chose to record, so an incomplete investigation
  looks incomplete. The rail does not count the bench done until two readings
  are plotted.
- **No `<sc-for>` is used inside an `<svg>` anywhere in the group.** Repeated
  marks are built as one path string. This is belt-and-braces alongside the
  `<text>` finding above: a single attribute hole is known to be safe.
