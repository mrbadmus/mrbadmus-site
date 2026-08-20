# C6 — Acids and alkalis · author's notes

**Seven lessons. The unit is complete.** Everything is draft and unreviewed.

---

## 1. Statutory coverage

| Lesson | Statements |
|---|---|
| `acids-and-alkalis` | `KS3.C.CR.04` (defining acids and alkalis) |
| `indicators-and-the-ph-scale` | `KS3.C.CR.05` |
| `neutralisation` | `KS3.C.CR.04`, `KS3.C.CR.07` |
| `acids-and-metals` | `KS3.C.CR.06` |
| `acids-and-carbonates` | **none — see §2** |
| `making-a-salt` | `KS3.C.CR.07` (as preparation) |
| `catalysts` | `KS3.C.CR.08` |

All five CR statements owned by C6 are covered. `CR.07` is split across two
lessons on purpose: `neutralisation` establishes the equation and the pH curve,
`making-a-salt` turns it into a preparation with a filtration step.

---

## 2. Divergence from §7 — flagged for ruling

§7 lists the fifth lesson as **Acid + alkali: making a salt (PROCESS)**. This
build has **`acids-and-carbonates` (PROCESS)** in that slot instead, and folds
the acid + alkali salt work into `neutralisation` and `making-a-salt`.

The case for the change: acid + carbonate is the third of the three acid
reaction families, it carries the limewater test, and without it the unit
teaches two reactions of acids and calls it a set. It also sets up C10's
limestone weathering and ocean acidification, which currently arrive with no
prior reaction to hang on.

The case against: it is not in §7 and it owns no statutory statement.

**Ruling wanted.** If it goes, the unit drops to six lessons and the limewater
test needs a home — probably C10-02.

---

## 3. Seven lessons, six shapes

- **`c6-01`** — an **eight-bottle sorter** (acid / alkali / neutral) with a
  where-it-lives tag on each. The reveal is that the most dangerous bottle on
  the bench is an alkali.
- **`c6-02`** — a **pH strip** as persistent reference, plus a **sample bench**
  where the student bands the guess before the indicator goes in.
- **`c6-03`** — a **drop-by-drop titration** with a live pH readout and a bar
  trace. The instrument is the lesson: the trace makes the cliff visible.
- **`c6-04`** — a **4 × 2 grid** (metals × acids), reusing C5-04's
  `reactivity-grid` shape with a smaller table.
- **`c6-05`** — a **five-step rig reveal** plus a **four-solid sorter**.
- **`c6-06`** — a **naming bench** (3 acids × 4 bases, salt name generated) plus
  a **six-step method ordering**.
- **`c6-07`** — a **five-flask comparison** with two controls, a rate readout
  and a recovered-mass readout side by side.

§6 risk noted: 03, 04 and 05 are three consecutive PROCESS lessons. They differ
by instrument — continuous dial, grid, staged rig — which is the same mitigation
C5 used for its four.

---

## 4. Instrument kinds

`bottle-sorter` (`c6-01`), `ph-bench` (`c6-02`), `titration-dial` (`c6-03`),
`reactivity-grid` (`c6-04`), `step-rig` + `solid-sorter` (`c6-05`),
`salt-namer` + `method-order` (`c6-06`), `catalyst-bench` (`c6-07`). All DOM.

Two worth keeping:

`titration-dial` payload: `{curve: [ph…], drops, seenJump}`. The curve is a flat
array indexed by drop count, so re-pointing it at a different acid/alkali pair
is one line. C9 wants nothing from it, but a KS4 titration lesson would.

`method-order` payload: `{steps: [{id, text, why}], shuffled: [id…], order: []}`.
Generic sequence-builder — no chemistry in it at all. C10-03's rock cycle
journey reuses it unchanged, and it is the obvious instrument for any
"put the method in order" task in biology or physics.

`salt-namer` generates the salt name from `base.metal + acid.ending`, so adding
a fourth acid is a one-line change.

---

## 5. Science flags

1. **Acid defined as "releases hydrogen into solution"** (`c6-01`). Deliberately
   avoids H⁺ and ions. Confirm this is the KS3 form you want — the same question
   C2 raised about Dalton.
2. **Alkali defined as a base that dissolves in water**, with the base/alkali
   distinction stated in the explainer and expanded in the stretch. Confirm you
   want the distinction at KS3 rather than deferring it.
3. **pH values used**: battery acid 0, lemon 2, rainwater 6, pure water 7,
   baking soda 9, oven cleaner 13, stomach 2, vinegar 3. All conventional
   classroom figures. Confirm.
4. **"Each pH step is a factor of ten"** (`c6-02` misconception). Correct.
   Confirm you want the logarithmic point made explicitly at KS3 — it is the
   single most-repeated misconception in the topic and the lesson attacks it
   head on.
5. **Rainwater described as naturally pH 6 because of dissolved CO₂**
   (`c6-02`). Correct, and it is C10-06's content arriving early. Confirm.
6. **The titration curve** in `c6-03`: 1,1,1,1,2,2,2,2,3,3,7,11,11,12,12,12,13,
   13,13,13,13. Integers only, equivalence at drop 10. Shaped correctly for
   strong acid + strong alkali. Confirm you are happy with whole numbers.
7. **Sodium hydroxide "turning the fat in your skin into soap"** (`c6-01`).
   Correct — saponification. Confirm the wording is acceptable.
8. **"Toothpaste is mildly alkaline"** (`c6-03` use 3). True of most
   formulations. Confirm, or soften to "many toothpastes".
9. **Enamel dissolving below pH 5.5** (`c6-02` rung 4). Standard figure.
   Confirm.
10. **Limewater going clear again with excess CO₂** (`c6-05` step 5).
    Correct and deliberately included as honest apparatus behaviour. Confirm you
    want it at KS3 — most textbooks omit it.
11. **Iron chloride** left unspecified as to oxidation state (`c6-04`), matching
    the C5 flag-11 convention.
12. **Copper + acid gives no reaction** (`c6-04`), justified by the reactivity
    series from C5-04. Cross-reference is deliberate.
13. **Manganese dioxide as catalyst, 48 cm³ in 60 s; liver 55 cm³** (`c6-07`).
    Illustrative figures, not measured. Confirm you want numbers here at all.
14. **Catalase named** (`c6-07` stretch) and the boiled-liver control described.
    Cross-links to B8. Confirm.
15. **Dilute acid listed as speeding peroxide decomposition while being
    consumed** (`c6-07` trial 5). This is the discriminating item in the bench —
    faster but not a catalyst. Confirm the chemistry is stated safely enough at
    KS3, since the acid's role is genuinely more complicated than the lesson says.
16. **"Nine tenths of manufactured chemicals pass over a catalyst"**
    (`c6-07` stretch). Widely quoted. Confirm or replace with a range.

---

## 6. Misconception register — proposed `ACID` family

`REACT` is reaction types. These are about acids, alkalis and rates, and they
need their own family. **Rule on the prefix before C9**, which will want to
cross-reference `ACID-07`.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `ACID-01` | Acids are dangerous; alkalis are what makes things safe. | `think-commit-danger` | `think-reveal-oven-cleaner` | `acids-and-alkalis` |
| `ACID-02` | A dilute acid is no longer really an acid. | `judgement-1` | `judgement-1-reveal` | `acids-and-alkalis` |
| `ACID-03` | pH 2 is twice as acidic as pH 4. | `think-commit-scale` | `think-reveal-factor-ten` | `indicators-and-the-ph-scale` |
| `ACID-04` | More indicator gives a different pH reading. | `rung-2` | `rung-2-feedback` | `indicators-and-the-ph-scale` |
| `ACID-05` | Neutralising an acid destroys it; only water is left. | `think-commit-gone` | `think-reveal-salt` | `neutralisation` |
| `ACID-06` | The pH climbs steadily as alkali is added. | `titration-dial` | `curve-reveal` | `neutralisation` |
| `ACID-07` | The bubbles are the metal turning into gas. | `think-commit-fizz` | `think-reveal-hydrogen` | `acids-and-metals` |
| `ACID-08` | A gas that puts out a splint is carbon dioxide. | `think-commit-splint` | `think-reveal-specificity` | `acids-and-carbonates` |
| `ACID-09` | Boiling a solution dry gives the best crystals. | `think-commit-boil` | `think-reveal-slow-cooling` | `making-a-salt` |
| `ACID-10` | A catalyst is used up slowly, which is why it wears out. | `think-commit-consumed` | `think-reveal-poisoning` | `catalysts` |

`ACID-08` is `NOS`-shaped — it is about what counts as a specific test, not
about carbonates. That is the sixth nature-of-science misconception parked in a
content family. The `NOS` call was already overdue before C8 per the C5 notes.

---

## 7. For Code

- Seven instruments, all DOM, no canvas, no animation loops.
- Rail stops: five in `c6-01`, `c6-02`, `c6-04`, `c6-06`, `c6-07`; six in
  `c6-03` and `c6-05`.
- SVG arrows for every equation, per the C4 convention.
- `c6-06` links forward to `c7-01-energy-and-changes-of-state.html` and
  `c6-07` does too — both exist.
- No props beyond `showDraft`.
- `c6-02`'s pH strip uses fifteen literal hex values in a `PH_COLOURS` array,
  not tokens. This is deliberate — they are scientific data, not brand colour —
  but it is the only place in C1–C8 where non-token colour is hard-coded, and
  every cell carries its number so identity is not hue-only. **Confirm.**
