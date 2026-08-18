# B3 — Nutrition and digestion · author's notes

Eight lessons, complete unit. Draft — nothing here has been science-reviewed.
Flags are numbered so they can be answered by number.

Queue resolution and filename convention are in `NOTES-P3.md` §0 and apply
unchanged: slugs are verbatim from `structure.py`.

---

## 1. Statutory coverage

| Lesson | Statements |
|---|---|
| `a-balanced-diet` | `KS3.B.NUT.01` (all seven nutrients, each with function and deficiency) |
| `food-tests` | working-scientifically; no NUT statement of its own |
| `energy-in-food-and-what-you-need` | `KS3.B.NUT.02` |
| `when-diet-goes-wrong` | `KS3.B.NUT.03` |
| `the-digestive-system` | `KS3.B.NUT.04` — the *tissues and organs* clause |
| `enzymes-in-digestion` | `KS3.B.NUT.04` — the *enzymes as biological catalysts* clause |
| `absorption-and-the-small-intestine` | `KS3.B.NUT.04` — the *adaptations to function* clause |
| `bacteria-in-the-gut` | `KS3.B.NUT.05` |

All five NUT statements covered. `NUT.04` is split across three lessons because
it is a compound bullet containing organs, enzymes and adaptations — the §7
splitting argument, applied. `food-tests` carries no statement, same situation
as B2 `joints`: it is a `structure.py` slot and a food-test practical that never
happens is not a science education.

---

## 2. Family patterns as applied

- **CLASSIFY (b3-01)** — commit-then-reveal across a set, not a sorting game.
  Seven nutrients, three amount bands, all seven committed before anything
  opens. The instrument exists to make *one specific wrong answer* visible: a
  student who puts all seven in the same band gets a verdict that names it.
- **INVESTIGATION (b3-02)** — the pattern is *what may you write down*. Every
  result panel ends with a literal claim line, and for a negative it is the
  hedged wording rather than the confident one. Twenty food/test combinations,
  each with its own honest note, including four deliberate false negatives.
- **QUANTITATIVE (b3-03)** — follows `NOTES-P3.md` §1: the ledger reports
  intake and requirement and does the comparison, and the *paper* section does
  the three sums longhand. Requirement is a property of the person, so the
  person is a control, not a constant.
- **CONTRAST (b3-04)** — three columns read across four rows, then five clinics.
  Two of the five clinics have **two** correct answers, and the verdict says so
  when a student ticks only one. Refusing to tick two is the error being taught.
- **SYSTEM (b3-05, b3-08)** — b3-05 is a journey with a time chart that
  contradicts the intuition (stomach 4 h, small intestine 16 h). b3-08 is
  perturbation in the B2 `system-switch` idiom: five jobs, switch each off, and
  switching all five off builds the germ-free mouse from the hook.
- **PROCESS (b3-06)** — a running reaction with three counters, one of which
  never moves. That counter *is* the lesson.
- **MODEL (b3-07)** — build the model up rather than break it down: three
  folding levels, each a multiplier, ending at ~30 m².

---

## 3. New instruments

### 3.1 `band-commit` — flagship of `b3-01` (DOM only)

- **Controls:** seven rows × three band buttons; a reveal locked until all
  seven are committed.
- **Readouts:** per-row real band and real mass with a one-paragraph why; a
  scored verdict tile.
- **Payload:** `{rows: [{id, name, hint, band, mass, why}], bands: [3], picks: {}, open: bool}`.
- **Note for Code:** the verdict has **three** branches, and the all-same-band
  branch is the one that must not be dropped — it is the only place the target
  misconception is named back to the student in their own answer.

### 3.2 `test-bench` — flagship of `b3-02`

- **Controls:** five food tabs, four test tabs, a two-option prediction per
  combination. Predicting **runs** the test (no separate button — the commit is
  the action).
- **Readouts:** a filling tube whose colour is the real result, method, what the
  test detects, an agreement verdict, the honest note, and the claim line.
- **Payload:** `{foods: [{id, label, has: {testId: bool}, notes: {testId: string}}], tests: [{id, label, detects, method, pos: {colour, name}, neg: {colour, name}}], predictions: {}, ran: {}}`.
- **Design note:** the tube is the only colour-bearing element in the unit, and
  the colour is real (Benedict's blue #2E63B8 → brick red #B03A16). Do not tint
  it with accent tokens.

### 3.3 `person-ledger` — flagship of `b3-03`

- **Controls:** five person tabs; twelve food buttons that add a portion on tap
  and clear at seven; *empty the day*.
- **Readouts:** requirement, running total, a bar that changes colour at ±5%,
  and a balance line naming surplus or shortfall in kJ.
- **Payload:** `{people: [{id, label, name, need, why}], foods: [{id, name, kj}], person: id, plate: {foodId: count}}`.
- **Note for Code:** the *match* panel appears only within 5% and its copy tells
  the student to switch person **without changing the food**. That instruction is
  the experiment; without it the ledger is a calculator.

### 3.4 `enzyme-run` — flagship of `b3-06`

- **Controls:** three enzyme tabs, three pH tabs, a 0–80 °C slider, *run*,
  *fresh tube*.
- **Readouts:** rate as % of maximum; three counters (substrate, product,
  enzyme) with bars; a tick clock; a three-branch verdict.
- **Mechanism:** `rate = tTerm × pTerm`, `tTerm` rising to 1 at 37 °C then
  falling quadratically to 0 by 55 °C, `pTerm` falling linearly with pH gap.
  Above 55 °C a `denatured` flag latches **and does not clear when cooled** —
  only *fresh tube* clears it. That latch is the whole misconception.
- **Payload:** `{enzyme: id, ph: number, temp: number, substrate, product, enzymeCount, denatured: bool, clock}`.

### 3.5 `fold-builder` — flagship of `b3-07`

- **Controls:** three level toggles (folds ×3, villi ×7, microvilli ×3).
- **Readouts:** area in m² from a 0.5 m² base, a bar against the 31.5 m²
  maximum, a note per level count, and the multiple.
- **Payload:** `{base_m2: 0.5, levels: [{id, name, factor, what, scale}], on: {}}`.
- **Note for Code:** the note strings are indexed by *how many* levels are on,
  not by which — four strings, one per count. Length never changes and the copy
  says so at every step.

### 3.6 `job-switch` — flagship of `b3-08`

The B2 `system-switch` shape with five rows and no prediction gate; the payoff
is the all-five-off summary panel.

---

## 4. Science flags — numbered for review

1. **The seven daily figures in `b3-01`** (300 g carbohydrate, 70 g lipid, 45 g
   protein, 0.2 g vitamins in total, 5 g minerals in total, 25 g fibre, 2000 g
   water, for a 13-year-old). These are rounded typical values assembled to make
   the three bands land cleanly. Confirm each, and confirm you are happy with
   *vitamins in total* and *minerals in total* as single rows rather than
   thirteen and a dozen.
2. **Vitamin B12 at 1.5 µg/day** is used in the think-again block to get the
   "two hundred million times" comparison against 300 g of carbohydrate. Check
   the arithmetic and the rhetoric — it is the sharpest sentence in the lesson
   and the easiest to get wrong.
3. **"Four months" to die on Plate A** (`b3-01` hook, scurvy without vitamin C).
   Historical scurvy onset is usually quoted at 1–3 months to symptoms and
   longer to death. Confirm the figure or give me one you are happy with.
4. **Takaki Kanehiro and the barley ships** (`b3-01` stretch). The trial, the
   result and the forty-year gap to thiamine are all standard history. Confirm
   the framing "right about the fix while wrong about the mechanism".
5. **Four false negatives in `b3-02`** are deliberate: potato/Biuret (2%
   protein), apple juice/Biuret (0.3%), milk/iodine (a *true* negative, marked
   as such), and the sucrose case in the stretch layer. Confirm you want
   false negatives designed in rather than a clean grid.
6. **Benedict's needs a reducing sugar** — the stretch layer says caster sugar
   gives a negative and goes positive after acid hydrolysis. Confirm this is
   wanted at KS3; it is the single most common source of a genuinely correct
   method producing a wrong conclusion.
7. **The five requirement figures in `b3-03`** (5800 / 9500 / 9000 / 13 500 /
   25 000 kJ). The rower figure is the one most likely to be challenged. Confirm.
8. **Twelve food kJ values in `b3-03`.** Plausible portion values, not from a
   food table. If you want real figures say so and I will mark the block
   `pending-data`.
9. **`b3-04` tone is a science-bearing question, not only a style one.** The
   lesson covers obesity, starvation and deficiency as three *mechanisms*; it
   reasons from measurements and clinical signs, sets no targets, names no ideal
   body, and the third think-again block explicitly attacks "you can tell what
   someone eats by looking at them". The legal line signposts a trusted adult or
   doctor. **Please review this lesson's tone with the same weight as its
   statements** — see the register's ⚠ note on `DIET-08`.
10. **Clinic 2 and clinic 5 in `b3-04` each have two correct answers.** Clinic 5
    is malabsorption after surgery, where the *diet* is adequate and the *gut*
    is not — it is the bridge into lessons 5–7. Confirm you want a case whose
    cause is not dietary at all inside a diet lesson.
11. **James Lind's 1747 trial** (`b3-04` stretch), including that he
    misinterpreted his own result and recommended a boiled concentrate that
    destroyed the vitamin C. Standard history; confirm the flat statement.
12. **Transit times in `b3-05`** (mouth ~1 min, oesophagus ~8 s, stomach ~4 h,
    small intestine ~16 h, large intestine 12–30 h, rectum a few hours). Wide
    natural variation; the legal line says so. Confirm the figures and the
    caveat.
13. **"You could live without a stomach"** (`b3-05` think-again). True —
    gastrectomy patients digest and absorb. Confirm it is safe to state flatly
    to Year 7.
14. **The gut-is-outside-you topology argument** (`b3-05` stretch), including
    the swallowed-coin comparison. Confirm; it is the most conceptually
    ambitious paragraph in the unit and the one most likely to be cut.
15. **Stomach protease at pH 2 described as "unusual for a protein"**
    (`b3-06`). Correct, and it is offered as a remark rather than as content.
    Confirm.
16. **The rate model in `b3-06` is not a real curve.** Optimum 37 °C, zero at and
    above `DENATURE_C`, linear pH falloff over 4.5 units. The legal line says the
    bench is a simplified model. **RESOLVED, 15 Aug — threshold settled at 50 °C**
    in a single `DENATURE_C` constant used by `rateFor()`, the `tempNote`
    branches and the three prose statements alike; the post-optimum falloff
    divisor moved 18 → 13 so the curve reaches near-zero at the threshold rather
    than dropping off a cliff from 56% at 49 °C. Confirm 50 °C is the figure you
    want, since it is now stated in four places at once.

    **Also fixed in the same pass, and it was the more serious of the two.** The
    `denatured` latch was only ever set inside the run tick, so a student who
    dragged the slider to 60 °C, watched the rate read 0%, and dragged it back to
    37 °C was shown a full recovery to 100% — the instrument built to kill
    `DIET-11` was demonstrating it, and contradicting its own think-again block
    in the process. The latch now fires in `onTemp`, so any temperature at or
    above 50 °C denatures immediately whether or not the reaction is ever run,
    and only *fresh tube* clears it. Enzyme-switch and fresh-tube both re-latch
    if the tube is still hot, which closes the obvious loophole, and the
    `tempNote` now has two denatured branches so "cool it, then take a fresh
    tube" is distinguishable from "cooling changes nothing". **Worth knowing for
    the other units: the same class of defect — a value the prose says must not
    move, wired so that it can — is what `b4-03`'s outward crossing counter and
    `b4-05`'s respiration bar are built around.** Both were checked and both hold.
17. **Surface area of the small intestine given as ~30 m², not 200–300 m²**
    (`b3-07`). This follows the 2014 fresh-tissue measurements, and the stretch
    layer explains the revision and warns that both figures are in print. This
    is the flag I most want a ruling on: if the course's other materials say
    200 m², the two must agree.
18. **The multipliers ×3, ×7, ×3 from a 0.5 m² base** are chosen to land on
    ~30 m². They are not separately sourced measurements. Confirm this is
    acceptable as a model, or give me sourced factors.
19. **Coeliac disease in `b3-07` rung 4** — villous atrophy causing iron
    deficiency on an adequate diet. Confirm the level of detail.
20. **Gut bacteria numbers in `b3-08`**: ~30 trillion bacteria, "several
    million" bacterial genes against ~20 000 human. Order-of-magnitude figures
    that are revised regularly, flagged in the legal line. Confirm.
21. **Germ-free mice needing ~30% more food** (`b3-08` hook, and the payoff
    panel). Widely reported. Confirm the figure and that the four consequences
    listed are the right four.
22. **Newborn vitamin K injection** (`b3-08`, job 2) is used as the evidence
    that gut bacteria make vitamin K. Correct and clinically real. Confirm it is
    appropriate to name a routine medical intervention here.
23. **Faecal microbiota transplant** (`b3-08` stretch) with a ~90% success rate
    for recurrent *C. difficile*. Confirm the figure and that you want this
    example at KS3 — it is memorable, and it is the only genuinely startling
    thing in the unit.
24. **No anatomical diagrams anywhere in this unit.** Two figure slots are
    named in lesson legal lines and are **not yet in the diagram manifest**:
    `b3-gut-labelled` and `b3-villus-labelled`. They need adding, or the
    references need removing.

---

## 5. Misconception register — `DIET` family, minted

Fifteen entries, `DIET-01` to `DIET-15`, written into
`docs/ks3/misconception-register.md` under a new `DIET` family row.

**Minted, not proposed.** The `ENERGY` precedent from P1 is followed: the family
was opened by the unit that needed it, all entries are `review_state: draft`, and
the `statement` field awaits your review before any of them freeze. This is
different from `FORCE`/`BODY`/`ATOM`, which are still awaiting your ruling and
are **not** cited anywhere in this unit.

Three cross-family notes are written into the register rather than here:

- `DIET-14` is `PART-10`/`PART-11` in biological costume, and
  `absorption-and-the-small-intestine` is the first lesson where the belief costs
  a mark. The confrontation names C1 explicitly.
- `DIET-06` and `ENERGY-12` are adjacent and must keep separate confrontations.
- **`DIET-11`/`DIET-12` (enzymes) have an ordering problem worth your attention.**
  B1 `enzymes-and-what-changes-their-rate` is the natural owner of enzymes and is
  **not yet authored**, while B3 needs them for `NUT.04`. B3 teaches them fully.
  When B1's enzyme lesson is written it must re-confront rather than restate, and
  it should probably open by naming what B3 already did.

---

## 6. For Code

- Six instruments in §3. `band-commit`, `job-switch` and `fold-builder` are
  DOM-only and cheap; `enzyme-run` is the only one with a timer.
- Every slider is bound to `input` **and** `change`.
- `enzyme-run` uses `setInterval` at 160 ms for 20 ticks and clears the timer in
  `componentWillUnmount`. Nothing else in the unit animates.
- Rail stops: four in every lesson.
- Cross-links use generator output names (`b3-02-food-tests.html`). Outward
  links go to `b1-06`, `c1-04`, `c1-05`, `c1-06`, `p1-01`, `p1-04`, `p2-01`,
  `p2-03` and `b4-03` — **`b4-03` is a forward link within Biology and resolves
  once B4 is generated.**
- `b3-03` carries the §4.5 ruling-3 forward pointer as a visible dashed panel.
  It is content, not decoration: **do not restyle it into a generic aside, and do
  not remove it without reopening ruling 3.**
- Props are read where declared — the orphan-prop defect noted in NOTES-P1 was
  hit twice while writing this unit (`b3-04` `startCase`, `b3-06` `startTemp`)
  and fixed in the same pass. Declaring a prop and wiring it are one action.
