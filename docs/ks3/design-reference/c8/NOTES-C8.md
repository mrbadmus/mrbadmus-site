# C8 — The periodic table · author's notes

**Seven lessons. Statutory coverage is complete; the unit diverges from §7's
lesson count by design — see §2.** Everything is draft and unreviewed.

---

## 1. Statutory coverage

| Lesson | Statements |
|---|---|
| `metals-and-non-metals` | `KS3.C.PT.01`, `KS3.C.PT.03`, `KS3.C.PT.05` |
| `mendeleev-and-the-table-that-predicted` | `KS3.C.PT.02` |
| `groups-and-periods` | `KS3.C.PT.03` |
| `group-1-the-alkali-metals` | `KS3.C.PT.04` |
| `group-7-the-halogens` | `KS3.C.PT.04` |
| `group-0-and-why-groups-exist` | `KS3.C.PT.04` |
| `metal-and-non-metal-oxides` | `KS3.C.PT.06` |

**Every statutory statement in C1–C8 is now covered.** `PT.06` — the chemical
properties of metal and non-metal oxides with respect to acidity — was the last
gap, and it was closed by `c8-07` on **23 August 2026**.

⊖ **CORRECTED 23 Aug 2026. This paragraph used to say the gap "was closed by
`c8-07`, authored 21 Aug 2026", and that was not true when it was written.**
What happened on 21 August is that Design DREW
`c8-07-metal-and-non-metal-oxides.dc.html` — a real, finished artboard, not a
stub. No lesson record existed: `ks3_data/c8/` held `lesson_01` to `lesson_06`
and nothing else, the slot rendered a coming-soon page, and three other files
(`chemistry_c8_periodic.py`, `ks3_data/c8/__init__.py` and
`ks3_instrument_liveness.py`) each said so in their own words.

The correction is dated rather than silently overwritten because the false claim
cost a run: a later session read the `.dc.html` on disk, took it for the build,
and reported `c8-07` as done. **MRB-205 is what makes that a distinction and not
a technicality — Design draws, Code renders.** A page in the design reference is
half a lesson, and this file is the half that says which half is finished, so a
sentence here claiming a build that has not happened is the one kind of error
the file cannot afford.

Everything below in §8 was accurate as a BRIEF throughout, and the build
followed it.

---

## 2. Divergence from §7 — flagged for ruling

§7 lists five lessons and folds the group work into one:
*Patterns you can predict: Groups 1, 7 and 0 (MODEL)*.

This build has **three separate group lessons** instead (04, 05, 06), plus the
oxides lesson. Net: seven built where five were specified.

The case for unbundling: the three groups are three different instruments and
one of them exists to contradict another. Group 1 is a sequential water-trough
run; group 7 is a 3 × 3 displacement grid; group 0 has no reaction to run at
all and turns into a prediction exercise. Compressed into one lesson, group 7's
reversed trend becomes a paragraph rather than a grid the student fills in and
is surprised by — and that surprise is the single most valuable moment in the
unit.

The case against: it is 40% over the specified lesson count for one statutory
statement.

**RULED (a), 21 Aug 2026 — keep all three group lessons and add the oxides
lesson, giving a seven-lesson unit.** ⊕ The ruling was taken on 21 August and
BUILT on 23 August; §1 above records why the two dates are kept apart. The alternatives were (b) merge 04–06 into
one and match §7 exactly at five, and (c) move oxides to C9 where the
reactivity series lives. (b) was rejected because the compression falls almost
entirely on group 7, and group 7's reversed trend is the single most valuable
surprise in the unit — it needs the grid the student fills in, not a paragraph.
(c) was rejected because `PT.06` is a periodic-table statement: the whole point
is that position in the table predicts whether the oxide is acidic or basic, and
that argument does not survive being moved next to the reactivity series.

The cost of (a) is a seven-lesson unit, which is accepted.

Also flagged: `c8-02`'s archetype was authored as MODEL and has been corrected
to INVESTIGATION per §7. The lesson body was written to the MODEL shape and
still reads as one — it is a gap-prediction exercise, not an investigation with
a plan and a control. **Confirm whether the archetype label or the lesson
should move.**

---

## 3. Six lessons, five shapes

- **`c8-01`** — a **six-sample property sorter**. Three of the six break one of
  the rules in the reference table and are still what they are.
- **`c8-02`** — a **gap-filler**: a 3 × 3 neighbour grid with one dashed empty
  square, three predictions from the neighbours, then Mendeleev's 1871 figures
  against the 1886 measurements in one table.
- **`c8-03`** — a **tappable table**, twenty elements, four periods, eight
  groups, with an address readout and a family line for each square.
- **`c8-04`** — a **water trough** run three times, one metal at a time.
- **`c8-05`** — a **3 × 3 displacement grid**, `reactivity-grid` from C5-04 with
  halogens substituted.
- **`c8-06`** — an **outer-electron strip** (four rows of dots), a
  **four-unknown prediction file**, and a **three-use judgement block**.

§6 note: 04 and 05 are both PATTERN and adjacent, which is the risk §6 warns
about. They are deliberately paired — the second one exists to break the trend
the first one establishes — and the instruments differ.

---

## 4. Instrument kinds

`property-sorter` (`c8-01`), `gap-filler` (`c8-02`), `table-reader` (`c8-03`),
`water-trough` (`c8-04`), `reactivity-grid` (`c8-05`), `shell-strip` +
`unknown-file` (`c8-06`). All DOM.

`reactivity-grid` has now been used three times (C5-04 metals, C6-04 metals ×
acids, C8-05 halogens). C5's notes asked for the order to be kept as data
rather than inferred from array position; that has held, and C8-05 sets
`rank: 0..2` on the halogens. C9's reactivity series will be the fourth use and
the first with more than four rows.

`table-reader` payload: `{EL: {sym, name, num, group, period, kind, note},
LAYOUT: [{label, cells: [key|null]}], FAMILIES: {group: text}}`. Layout is
separate from element data, so the same twenty elements can be redrawn as a
long-form table without touching the notes. C9 and any KS4 table lesson want
this one.

`shell-strip` renders eight dots per row and fills `n` of them. It is the only
place in the chemistry sequence where electron count is shown visually, and it
stops short of shells-within-shells deliberately.

---

## 5. Science flags

1. **Graphite conducting** used as the discriminating case in both `c8-01`'s
   hook and its misconception. Correct. Confirm the same example carrying two
   blocks is acceptable.
2. **Mercury and bromine** as the two liquid elements at room temperature
   (`c8-01` rung 2). Correct.
3. **Sodium described as "cuts like hard cheese" and floating** (`c8-01`
   sample E). Correct and deliberately placed to break the "metals are hard and
   heavy" habit before C8-04 needs it.
4. **Metallic bonding explained as free outer electrons** (`c8-01` stretch),
   deriving five properties from one idea. This is KS4 content in one paragraph.
   Confirm it stays.
5. **Germanium figures**: predicted mass 72 vs measured 72.6; predicted density
   5.5 vs measured 5.32; predicted oxide XO₂ vs GeO₂. All correct as
   historically recorded. Confirm.
6. **Newlands ridiculed, and the "alphabetical order" jibe** (`c8-02`
   misconception). Historically attested. Confirm you want the anecdote.
7. **Tellurium/iodine swap explained by proton number** (`c8-02` decision 2 and
   stretch), including the statement that Mendeleev was right for a reason he
   could not have known. Confirm the nature-of-science framing.
8. **Noble gases absent from Mendeleev's table** (`c8-02` stretch, `c8-06`
   hook). Correct — argon 1894.
9. **Group number = outer electrons** stated for groups 1, 2, 7 and 0
   (`c8-03`, `c8-06`). Correct at KS3. Helium's two electrons are noted as the
   exception in `c8-06`'s shell strip detail.
10. **Group 1 trend explained by atomic size and distance of the outer
    electron** (`c8-04` stretch, `c8-06`). Correct and it is the mechanism that
    makes group 7's reversal predictable rather than arbitrary.
11. **Melting points**: lithium 180 °C, sodium 98 °C, potassium 63 °C
    (`c8-04`). Correct. **Density is deliberately not given as a trend** —
    Li 0.53, Na 0.97, K 0.86 is not monotonic and the lesson says only that they
    all float. Confirm that omission is wanted.
12. **Potassium's lilac flame and possible spitting** (`c8-04`). Correct.
13. **Rubidium predictions** (`c8-04`) and **astatine predictions**
    (`c8-05` rung 4). Both extrapolations, both flagged as such in the lesson.
14. **Halogen states and colours**: fluorine pale yellow gas, chlorine green
    gas, bromine red-brown liquid, iodine grey-black solid with violet vapour.
    Correct.
15. **Chlorination of water framed against chlorine as a 1915 weapon**
    (`c8-05` stretch). Confirm you want the weapon reference at KS3.
16. **Fluorine's isolation injuring chemists; Moissan 1886** (`c8-05` stretch).
    Correct.
17. **Xenon compounds, Bartlett 1962** (`c8-06` stretch), presented as the
    footnote that qualifies "reacts with nothing". Confirm.
18. **Helium escaping the atmosphere and the MRI/balloon contrast**
    (`c8-06` stretch). Correct. Confirm the editorial edge on party balloons.
19. **Neon signs explained as excitation and emission, explicitly not a
    chemical reaction** (`c8-06` use 3). Correct, and it is physics arriving in
    a chemistry unit on purpose.

---

## 6. Misconception register — proposed `PTAB` family

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `PTAB-01` | If it conducts electricity it must be a metal. | `think-commit-conduct` | `think-reveal-graphite` | `metals-and-non-metals` |
| `PTAB-02` | A liquid element cannot be a metal. | `rung-2` | `rung-2-feedback` | `metals-and-non-metals` |
| `PTAB-03` | Mendeleev's table was accepted because it was tidy. | `think-commit-tidy` | `think-reveal-predictions` | `mendeleev-and-the-table-that-predicted` |
| `PTAB-04` | A gap in a table is a weakness in it. | `decision-3` | `decision-3-reveal` | `mendeleev-and-the-table-that-predicted` |
| `PTAB-05` | Elements next to each other in the table are similar. | `think-commit-neighbours` | `think-reveal-sodium-chlorine` | `groups-and-periods` |
| `PTAB-06` | The group number tells you how many electrons the atom has. | `rung-2` | `rung-2-feedback` | `groups-and-periods` |
| `PTAB-07` | Sodium melted because the water was hot. | `think-commit-melt` | `think-reveal-exothermic` | `group-1-the-alkali-metals` |
| `PTAB-08` | Reactivity always increases going down a group. | `think-commit-trend` | `grid-reveal` | `group-7-the-halogens` |
| `PTAB-09` | The noble gases are unreactive because they are gases. | `think-commit-gas` | `think-reveal-full-shell` | `group-0-and-why-groups-exist` |
| `PTAB-10` | Unreactive means useless. | `uses-block` | `uses-reveal` | `group-0-and-why-groups-exist` |

`PTAB-08` is the unit's most important entry, and it is created by the previous
lesson: C8-04 establishes a trend and C8-05 exists to break it. If §7's merge
(option b in §2) is chosen, `PTAB-08` loses the grid that confronts it and
becomes a sentence.

`PTAB-07` overlaps `ENER-03` from C7 — both are about heat coming out of a
reaction rather than into it. They are elicited by different phenomena and are
worth keeping separate, but the cross-reference should be recorded.

---

## 7. For Code

- Seven instruments, all DOM, no canvas, no animation loops.
- Rail stops: five in every lesson except `c8-06`, which has six.
  ⊖ **CORRECTED 23 Aug 2026: `c8-07` has FIVE, not six.** Its own `RAIL` const
  lists `s-hook s-rule s-bench s-think s-ladder`, and
  `docs/ks3/rail-manifest.md` — generated from the delivered page rather than
  written by hand — records the same five with `s-rule=s-hook`. `README.txt`
  says six as well and is wrong for the same reason. The sixth thing on the
  page is the closing key note, which is a dark section the engine emits and
  has never been a rail stop in any C8 lesson.
- SVG arrows for every equation, per the C4 convention.
- `c8-06`'s forward link to `c8-07-metal-and-non-metal-oxides.html` **now
  resolves**. The intra-unit dead link recorded here as a build blocker is
  closed; no coming-soon row is needed.
- `c8-01` links back to `c7-04-measuring-a-temperature-change.html`, which
  exists.
- No props beyond `showDraft`, except `c8-07`, which adds two bench props.
- `c8-03`'s LAYOUT array uses `null` for empty cells and renders them as dashed
  transparent boxes; the period-1 row is deliberately mostly empty rather than
  collapsed, because the shape of the gap is part of what the table teaches.

---

## Change log — 21 Aug 2026 (packaging pass)

Font-law sweep before the unit zip was cut. No change to the science or the
sequence.

- `c8-02`, `c8-03`: oxide formulae inside the prediction and decision
  payloads are plain digits (`XO2`, `GeO2`, `SiO2`, `CO2`, `C2O`, `CO3`,
  `X2O3`). They are strings rendered through holes, so markup is not
  available there — plain digits are the convention.
- `c8-04`: the `metal + water` word equation draws its arrow as inline SVG
  instead of typing U+2192.
- Why: the shipped latin subsets carry neither U+2192 nor subscript digits.

---

## 8. c8-07 · Metal and non-metal oxides — CONTRAST · `KS3.C.PT.06`

Authored 21 Aug 2026, closing the last statutory gap in C1–C8 under ruling (a).

### The teaching, and where the famous version is wrong

The pattern is that **metal oxides are basic and non-metal oxides are acidic**,
and position in the periodic table predicts which — which is why this is a
`PT` statement and not a `CR` one. The famous version of that sentence is wrong
twice, and **both counter-cases are on the bench rather than in a footnote**:

1. **Copper oxide is basic and the water stays at pH 7.** It is a metal oxide
   and it is a base, but it is insoluble, so nothing registers on the pH. A
   student who has been told "metal oxide means alkaline water" reads the
   reading as a refutation of the rule. It is not — it is the difference between
   *base* and *alkali*, and that distinction is why the KEY FACT block defines
   all three of oxide, base and alkali rather than just the pattern.
2. **Water is a non-metal oxide and it is neutral.** Hydrogen oxide sits in the
   tray and reads pH 7. The rule is about oxides of *most* non-metals, and the
   exception is the most common substance in the lesson.

### The bench — `oxide-bench`

Six oxides, two beakers of water, drag-free tray chips. **37 reachable states**,
all enumerated: one empty, six one-oxide, and 30 ordered pairs (order matters
because the comparison sentence names the left reading first).

| Oxide | pH | Solid |
|---|---|---|
| Calcium oxide | 12 | clear residue |
| Magnesium oxide | 10 | thin residue |
| Copper oxide | 7 | heap, insoluble |
| Water | 7 | — |
| Carbon dioxide | 5 | gas |
| Sulfur dioxide | 3 | gas |

**The pH values pair equal on purpose.** Copper oxide and water both read 7, so
the equal branch of the comparison is exercised naturally by two chips a student
would reach for anyway — and the sentence that comes back has to explain why two
identical readings mean two completely different things.

Z-order inside each beaker is fixed: body → water fill → undissolved solid → pH
numeral outside the glass. Water fill uses the fifteen-step pH colour scale from
`c6-02`, so a student who met the scale there reads this bench without being
retaught it.

The comparison sentence is **derived at render from the two readings in six
branches**, never stored per pair.

### Misconceptions

Four tracked, `PTAB-11` to `PTAB-14`. `PTAB-14` is a **named spare reserved for
C9** — registered here so the id cannot be reused, per §5.3.

### Structure

One KEY FACT block carrying all three definitions (oxide, base, alkali) plus the
pattern. Four self-marked answer rungs at B, B, C, D. Amber appears only on
misconceptions. Equations use inline SVG arrows with `aria-label="gives"` and no
Unicode symbols.

### Open

- The forward link in `c8-06` was left pointing at `c8-07` rather than reversed;
  flagged as a deviation at the time and still open if the direction bothers you.
- ⊕ **CLOSED 23 Aug 2026.** This read: *"`c8-07` does not yet carry a Law 7
  vocabulary block … this lesson will fail gate E until a five-card block is
  added."* Correct, and it was the first thing the build had to add that Design
  had not drawn. Five cards are authored on the lesson record and a `keyword`
  block sits at `#s-words`, the same component in the same position as
  `c8-06`'s and not a rail stop on either page. The terms are the three the KEY
  FACT box already defines — oxide, base, alkali — plus **insoluble** and
  **neutral**, which are the two words the bench cannot be read without and are
  each the whole of one of the two counter-cases.
