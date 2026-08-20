# C8 — The periodic table · author's notes

**Six lessons. The unit is complete but diverges from §7 — see §2.**
Everything is draft and unreviewed.

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
| — | **`KS3.C.PT.06` is NOT covered** |

**`PT.06` — the chemical properties of metal and non-metal oxides with respect
to acidity — has no lesson.** §7 assigns it to a seventh lesson,
*Metal and non-metal oxides (CONTRAST)*, which is not in this build. It is the
only uncovered statutory statement in C1–C8. It needs writing before the unit
can be called complete against the register.

---

## 2. Divergence from §7 — flagged for ruling

§7 lists five lessons and folds the group work into one:
*Patterns you can predict: Groups 1, 7 and 0 (MODEL)*.

This build has **three separate group lessons** instead (04, 05, 06), and is
missing the oxides lesson. Net: six built where five were specified, and the
wrong five.

The case for unbundling: the three groups are three different instruments and
one of them exists to contradict another. Group 1 is a sequential water-trough
run; group 7 is a 3 × 3 displacement grid; group 0 has no reaction to run at
all and turns into a prediction exercise. Compressed into one lesson, group 7's
reversed trend becomes a paragraph rather than a grid the student fills in and
is surprised by — and that surprise is the single most valuable moment in the
unit.

The case against: it is 50% over the specified lesson count for one statutory
statement, and it starves `PT.06`.

**Ruling wanted, three options.** (a) Keep all three and add the oxides lesson,
giving a seven-lesson unit. (b) Merge 04–06 into one and add oxides, matching
§7 exactly at five. (c) Keep three and move oxides to C9, where the reactivity
series lives. My recommendation is (a); the compression that (b) requires falls
almost entirely on group 7.

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

- Six instruments, all DOM, no canvas, no animation loops.
- Rail stops: five in every lesson except `c8-06`, which has six.
- SVG arrows for every equation, per the C4 convention.
- `c8-06` links forward to **`c8-07-metal-and-non-metal-oxides.html`, which does
  not exist**. Per §11 decision 8 the generator should render that as a
  coming-soon row rather than a dead link — but unlike C5's forward link, this
  one points inside its own unit, which is a different and worse case. It
  should be treated as a build blocker rather than a soft link.
- `c8-01` links back to `c7-04-measuring-a-temperature-change.html`, which
  exists.
- No props beyond `showDraft`.
- `c8-03`'s LAYOUT array uses `null` for empty cells and renders them as dashed
  transparent boxes; the period-1 row is deliberately mostly empty rather than
  collapsed, because the shape of the gap is part of what the table teaches.
