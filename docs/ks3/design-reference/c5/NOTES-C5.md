# C5 — Types of reaction · author's notes

**All five lessons. The unit is complete.** Everything is draft and unreviewed.

---

## 1. Statutory coverage

| Lesson | Statements |
|---|---|
| `combustion` | `KS3.C.CR.03` (combustion) |
| `thermal-decomposition` | `KS3.C.CR.03` (thermal decomposition) |
| `oxidation` | `KS3.C.CR.03` (oxidation) |
| `displacement` | `KS3.C.CR.03` (displacement) |
| `which-reaction-is-this` | `KS3.C.CR.03` (the whole statement, as discrimination) |

One statutory statement, five lessons. `CR.03` names four reaction types in a
single bullet, and the fifth lesson exists because naming four types is not the
same as telling them apart — which is what an exam asks and what §5.8 rung 2 is
for. If that reads as over-provision, the compression to lose is `c5-05`, and I
would argue against it: the unit's whole value is discrimination.

---

## 2. Four PROCESS lessons in a row — and how they differ

§6 warns that identical block lineups should be a coincidence of need, never a
default. Four consecutive PROCESS lessons is exactly the risk, so each has a
different flagship shape:

- **`c5-01`** — a **parameter bench** (fuel × air supply). The dial that matters
  is a hole in the side of a burner.
- **`c5-02`** — a **staged run** with a cooling gate at the end. The gate is the
  lesson: it does not go back when it cools, which is what separates it from a
  physical change.
- **`c5-03`** — a **four-tube controlled investigation**. Not a stepper at all:
  the four results only mean something read together, and tubes 2 and 3 are the
  controls doing the work.
- **`c5-04`** — a **4 × 4 grid**. Sixteen predictions, and the reactivity order
  falls out of the shape of the completed table rather than being stated.
- **`c5-05`** — CLASSIFY, eight reactions at rising stakes, ending with the
  student writing the rule in their own words.

---

## 3. Instrument kinds

`burner-bench` (`c5-01`), `tube-run` (`c5-02`), `control-tubes` (`c5-03`),
`reactivity-grid` (`c5-04`), `type-sorter` (`c5-05`). All DOM.

`reactivity-grid` is the one worth building properly:
`{metals: [{id, name, order, solution, solColour, deposit}], ran: {}, metal, sol}`.
Every cell's observation text is **generated** from the two metals' data, so
adding a fifth metal is a one-line change. C8 `patterns-in-reactions` and C9
`the-reactivity-series` both want it with more rows.

`control-tubes` payload: `{tubes: [{id, name, setup, chips: [{label, on}], rust, result, why}], preds: {}}`.
The `chips` array is what makes the controlled variables visible at a glance;
any "what does this experiment control?" lesson can reuse it.

---

## 4. Science flags

1. **Flame temperatures**: blue ≈ 1500 °C, yellow ≈ 1000 °C (`c5-01`). Roughly
   right for a Bunsen. Confirm the two figures.
2. **Yellow flame brightness attributed to glowing soot** (`c5-01`). Correct.
   Confirm you want it said this plainly, since it contradicts the intuition the
   misconception block then attacks.
3. **Incomplete combustion products** given as carbon monoxide + carbon + water.
   Correct. Confirm you are happy for both to be named together rather than
   staging them.
4. **Charcoal treated as pure carbon** (`c5-01`). It is mostly carbon with ash
   and volatiles. Confirm the simplification.
5. **Carbon monoxide and haemoglobin** (`c5-01` stretch) — binds far more
   strongly than oxygen and does not readily let go. Confirm the wording, and
   confirm the cross-reference to B4 is wanted.
6. **Hydrogen described as clean at the flame but not necessarily clean as a
   fuel**, because most is made from natural gas. Correct today. Confirm you want
   the qualification at KS3.
7. **Mass figures in `c5-02`**: 4.00 g → 2.58 g for copper carbonate, → 2.24 g
   for calcium carbonate, → 2.52 g for sodium hydrogencarbonate. These are
   computed from formula masses and are consistent; confirm you want numbers at
   all, since no calculation is asked for.
8. **Limestone decomposition at "around 900 °C"** and described as needing more
   than a school Bunsen comfortably gives. Confirm.
9. **Cement at "something like 8% of global carbon dioxide emissions"**
   (`c5-02` stretch). Widely quoted figure. Confirm or replace with a range.
10. **Sodium azide airbags decomposing "in thirty milliseconds"** (`c5-02`
    stretch). Confirm; the number is quoted for the whole inflation.
11. **Rust written as "hydrated iron oxide"** (`c5-03`), avoiding both iron(III)
    and a formula. Confirm this is the KS3 form you want — it is the same
    question C4 flag 10 raises from the other side.
12. **Tube 3's "faintest trace where the oil did not quite seal"** (`c5-03`).
    Deliberately imperfect data. Confirm you want an honest trace rather than a
    clean negative.
13. **Aluminium described as more reactive than iron, protected by its oxide**
    (`c5-03` misconception). Correct. Confirm anodising is right to leave out.
14. **Sacrificial protection explained via "gives up its electrons first"**
    (`c5-03` stretch). That is a KS4 explanation in one clause. Confirm it stays
    or should be cut to "corrodes in preference".
15. **Respiration as an oxidation** (`c5-03`, `c5-05` item 7). Correct and the
    B8 cross-link is deliberate. Confirm.
16. **Thermite at "around 2500 °C"** (`c5-04`). Confirm.
17. **The reactivity claim that carbon sits above iron and below aluminium**
    (`c5-04` use 2). Correct and it is C9's content arriving early. Confirm it
    is wanted as a consequence question here.
18. **`c5-05` item 8 answering "none of the four"** — marble and acid, which is
    neutralisation. This is the most unusual thing in the unit: a classification
    question whose answer is that the classification does not cover it. Confirm
    you want it, because it is the item most likely to be marked wrong by a
    teacher skim-reading.

---

## 5. Misconception register — `REACT` continues

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `REACT-10` | A bigger, brighter flame is a hotter flame. | `think-commit-yellow` | `think-reveal-soot` | `combustion` |
| `REACT-11` | Shutting the air off makes a flame burn hotter or more fiercely. | `gate-air-shut` | `burner-bench` | `combustion` |
| `REACT-12` | A substance that goes black when heated has burnt. | `think-commit-black` | `think-reveal-copper-oxide` | `thermal-decomposition` |
| `REACT-13` | A decomposition reverses when it cools. | `cool-gate` | `stage-4-reveal` | `thermal-decomposition` |
| `REACT-14` | Aluminium and stainless steel do not oxidise. | `think-commit-aluminium` | `think-reveal-oxide-layer` | `oxidation` |
| `REACT-15` | Rusting needs water only, or air only. | `tube-predictions` | `four-tube-summary` | `oxidation` |
| `REACT-16` | The displaced metal came out of the metal you added. | `think-commit-nail` | `think-reveal-solution` | `displacement` |
| `REACT-17` | A less reactive metal will displace a more reactive one if you heat it or wait longer. | `grid-lower-cells` | `grid-reveal` | `displacement` |
| `REACT-18` | Each reaction has exactly one type, so two names cannot both be right. | `think-commit-one-box` | `think-reveal-subset` | `which-reaction-is-this` |

`REACT-18` is the unit's most important entry and it is not a factual error —
it is a wrong idea about how classification works. **It is `NOS`-shaped**, like
`CELL-04`, `ATOM-02` and `PART-12`/`PART-13`. That is now the fifth
nature-of-science misconception living in a content family because the `NOS`
call is still open, and the register's own ruling said the decision was due
before `C8 mendeleev`. C8 is the next chemistry unit in the queue. **This is the
last comfortable moment to rule on it.**

---

## 6. For Code

- Five instruments, all DOM, no canvas, no animation loops.
- Rail stops: five in every lesson in the unit.
- SVG arrows for every equation, per the C4 convention.
- `c5-05` links forward to `c6-01-acids-and-alkalis.html`, **which does not
  exist yet** — the generator should render that as a coming-soon row rather
  than a dead link, per §11 decision 8. It is the only forward-dangling link in
  C3, C4 or C5.
- No props beyond `showDraft`. Same reasoning as C4 §7.
- `c5-04`'s grid needs its reactivity order (`order: 0..3`) kept as data, not
  inferred from array position — C9 adds metals in the middle.


---

## 7. `c5-04` — the reactivity series is now on the page (18 Aug 2026)

Ruled by Mide, overriding §3's discovery framing: the series is shown **up front**,
before the grid, not withheld until twelve cells have been run.

A new reference block (`s-series`) carries the full KS3 twelve — potassium down
to gold, with carbon and hydrogen included because they displace on the same
rule. The four bench metals are marked. Deliberate details:

- It is a **reference block, not a rail stop.** Consistent with every other
  reference section in the course (c5-01's fire triangle, c4-01's two columns):
  the rail ticks activities only, so a stop that could never tick is not added.
- The grid's payoff paragraph had to change. It said *"You did not look this
  up"*, which is now false. It now says the sixteen tubes **reproduced** the part
  of the list the bench can reach — which is the honest version of the same
  point, and arguably the better one: the student checks a published order
  against their own data rather than being handed a conclusion.
- `showSeriesUpFront` (default **true**) restores the discovery order when
  false — the block then appears once the pattern emerges at twelve cells. The
  original lesson is a tweak away, not lost.

⚠️ One thing to watch in review: the grid's own teaching claim is weaker now. A
student who consults the list can complete sixteen predictions without reasoning
from evidence at all, and the empty half of the table stops being a discovery.
The lesson still works — reproducing a published order against your own data is
a real scientific move — but it is a **different** move from deriving one, and
`c5-04`'s rung 4 (design an investigation to place an unknown metal) is now the
only place the derivation is actually assessed. Worth a second look at that rung.
