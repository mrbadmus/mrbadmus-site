# C4 — Chemical reactions · author's notes

**All five lessons. The unit is complete.** Everything is draft and unreviewed.

---

## 1. Statutory coverage — and one referenced statement

| Lesson | Statements |
|---|---|
| `chemical-vs-physical-change` | `KS3.C.CR.01` (the what-counts half) |
| `reactions-rearrange-atoms` | `KS3.C.CR.01` (the rearrangement half) |
| `word-equations` | `KS3.C.CR.02` (the words half) |
| `mass-in-a-reaction` | `KS3.C.AEC.04` — **referenced, not owned** |
| `symbol-equations-and-balancing` | `KS3.C.CR.02` (the symbols half) |

⚠️ **`mass-in-a-reaction` owns nothing.** `AEC.04` is C2's, and C2 `conservation-of-mass`
covers it. This lesson is the §4.6 referencing case: same statement, second
context, taught quantitatively with the four-part treatment. It needs a ruling
of the same kind §4.6 gives for the particle model — **confirm that a
QUANTITATIVE lesson may reference a statement owned by an earlier unit without
double-counting coverage**, or tell me to fold it into C2 and lose the FIFA
treatment.

CR.02 is split across two lessons for the reason AEC.03 was: a word equation is
a sentence, a symbol equation is a model with numbers in it, and the students who
meet them together learn that a formula is a longer name.

---

## 2. What the lessons do

- **`c4-01` (CONTRAST)** — three pairs, each pair chosen so the *visible* clue
  appears on both sides: bubbling twice, colour change twice, heat twice. The
  explanation-chain builder is the CONTRAST family's "linked comparison" step,
  and it is the one place in the unit where the model answer is shown in full.
- **`c4-02` (MODEL)** — the atom rearranger, in three stages, including a
  loose-atom stage that is honest about being unreal. The **impossible-product
  panel** is the flagship's second half: ask it for ammonia or gold and it
  refuses, which is where balancing is born three lessons later.
- **`c4-03` (MODEL)** — the equation builder, with distractors that are the real
  errors: heat, energy, a flame, limewater from a different test tube, and
  "bubbles" instead of the gas's name.
- **`c4-04` (QUANTITATIVE)** — the balance bench, then the four-part treatment
  in full, then FIFA worked and FIFA scaffolded.
- **`c4-05` (MODEL)** — the balancer, with coefficients as +/− controls and live
  per-element counters. The forbidden move is offered as a **button**, not a
  warning: adding a small 2 to the water balances the equation and silently
  turns the product into bleach.

---

## 3. Instrument kinds

`change-pairs` (`c4-01`), `atom-rearranger` (`c4-02`), `equation-builder`
(`c4-03`), `balance-bench` + `cover-triangle` in bar mode (`c4-04`),
`coefficient-balancer` (`c4-05`). All DOM.

`atom-rearranger` payload:
`{reactions: [{id, words, reactants: [{label, atoms: []}], products: [...], counts: [{el, n}], gate}], stage: 0|1|2}`.
Atoms are labelled circles; no canvas. Element colours come from one table so
that C8 and every KS4 bonding lesson can reuse it.

`coefficient-balancer` payload:
`{equations: [{id, left: [{parts, atoms}], right: [...], target: []}], coeffs: {}}`.
Formulae are rendered from `parts: [{sym, sub}]` so subscripts are real `<sub>`
elements rather than Unicode — the convention this unit standardises on.

---

## 4. The four-part treatment in `c4-04`, and flag 14 again

Everything the C2 change log asked for is present:

1. the rule alone in its own block, with nothing else in it;
2. **drawn** — as a part–whole bar, not a triangle, because the relationship is
   a sum;
3. the worked example revealing one step at a time, with **F / I / F / A badges**
   visible on each step;
4. the same four steps done by the student on the other reaction, with a
   compare-button per step rather than one reveal at the end.

The cover-the-one-you-want panel is here too, in bar form: three cover buttons,
an opaque plate over the covered cell, the arrangement that falls out, and one
sentence naming the operation.

**So C2's flag 14 now applies to a second lesson, and it is still unanswered.**
If "drawn as a triangle" is literal, both `c2-06` and `c4-04` need redrawing and
the redraw will teach a false relationship. If it means *drawn, in whatever shape
the relationship has*, both are compliant and P1's energy lessons inherit the
answer. I have built the second one the same way as the first deliberately, so
that one ruling settles both rather than accumulating exceptions.

---

## 5. Science flags

1. **Fried egg as the hook example** (`c4-01`). Denaturing is not a single
   reaction and "new substance" is doing simplifying work. Confirm it is
   acceptable at KS3, or I will swap it for toast.
2. **Rust described as reversible in a steelworks** (`c4-01`, `c4-05` neighbours).
   Iron ore is largely iron oxide and smelting does reverse it. Confirm the
   phrasing does not imply a bench-scale reversal.
3. **Steel and brass as mixtures** — consistent with C2 flag 9. No change.
4. **Whipped cream / butter as a physical-then-not boundary** (`c4-01` stretch).
   Butter-making is physical (fat coalescing). Confirm it reads that way rather
   than implying a reaction.
5. **"The atoms are all still there" in burning wax** (`c4-01`) — the products
   weigh more than the wax because oxygen joined. Correct; confirm the sentence
   is clear that the *products* outweigh the *fuel*.
6. **Hydrogen + oxygen balloon hook** (`c4-02`). Confirm you are content with a
   hook a teacher might demonstrate; there is no method on the page and no
   quantity given, deliberately.
7. **Nuclear transmutation named as "not chemistry"** twice (`c4-02`). Same hedge
   as C2 flag 4. Confirm.
8. **Bond breaking costs energy, bond making releases it** (`c4-02` stretch).
   Correct and beyond statutory. Confirm it stays as prose with nothing assessed.
9. **Marble + acid products named as calcium chloride, water and carbon dioxide**
   (`c4-03`). Correct for hydrochloric acid. Confirm naming the salt at KS3.
10. **Iron rusting deliberately excluded from the word-equation cases**, because
    rust is hydrated and the honest equation needs water as a reactant. Confirm
    that omission, or tell me which form to teach.
11. **The masses in `c4-04`**: 152.00 → 149.80 g (2.20 g CO₂) is plausible bench
    data, not measured; 2.40 g Mg → 4.00 g MgO is exact for Mg 24, O 16; the
    rung-3 figures 8.00 → 4.48 g are exact for CaCO₃ → CaO. Confirm all three,
    and confirm 2 d.p. on a balance readout.
12. **"The air in a classroom weighs around 150 kg"** (`c4-04`). A 7 × 8 × 3 m
    room holds about 200 kg; 150 kg suits a smaller room. Confirm or change.
13. **Phlogiston, and negative mass** — a second nature-of-science stretch, after
    C2's two. Confirm you want it, given the `NOS` family question is still open.
14. **"Mass is not quite conserved in nuclear reactions"** (`c4-04` stretch).
    True and easy to over-read. Confirm the hedge is strong enough.
15. **Coefficients capped at 4** in `c4-05`. Every target is reachable. Confirm
    the cap is a help rather than a puzzle-solving crutch.

---

## 6. Misconception register — proposed `REACT` family

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `REACT-01` | If it cannot be undone it is chemical; if it can, it is physical. | `think-commit-reverse` | `think-reveal-glass` | `chemical-vs-physical-change` |
| `REACT-02` | Something disappearing into a liquid is always the same kind of change. | `pair-2-commit` | `pair-2-reveal` | `chemical-vs-physical-change` |
| `REACT-03` | In a reaction the atoms themselves change into other kinds of atom. | `think-commit-mgo-atom` | `think-reveal-no-such-atom` | `reactions-rearrange-atoms` |
| `REACT-04` | New atoms can be made if the conditions are right. | `ask-gold` | `ask-refusal` | `reactions-rearrange-atoms` |
| `REACT-05` | The arrow in an equation means equals, so the sides can be swapped. | `think-commit-arrow` | `think-reveal-direction` | `word-equations` |
| `REACT-06` | Heat, energy or a flame can be written into an equation as a reactant. | `builder-distractor` | `builder-check` | `word-equations` |
| `REACT-07` | Gases have no mass, so a gas escaping cannot change a balance reading. | `think-commit-gas` | `sealed-flask-run` | `mass-in-a-reaction` |
| `REACT-08` | An equation can be balanced by changing the small numbers in a formula. | `forbidden-small-2` | `forbidden-reveal` | `symbol-equations-and-balancing` |
| `REACT-09` | A balanced equation is a correct equation. | `think-commit-maths` | `think-reveal-peroxide` | `symbol-equations-and-balancing` |

`REACT-03` is `ATOM-01` grown up — an atom carrying the properties of its
substance becomes an atom *becoming* another substance. Cross-reference rather
than re-mint. `REACT-08` is `ATOM-09` in its balancing costume, and the
confrontation is deliberately the same substance (H₂O₂) so the two lessons
reinforce each other. `REACT-07` cross-references `ATOM-11` and `PART-05`; the
chain is now four IDs long and it is the strongest argument yet that the
register needs a **cross-family "same belief" link type** rather than a prose
note. That is a request, not a decision.

---

## 7. For Code

- Five instruments, all DOM, no canvas, no animation.
- Rail stops: five in `c4-01`, `c4-02`, `c4-03` and `c4-05`; **seven** in
  `c4-04`, which is the most in the course so far and is the four-part treatment
  costing three stops of its own.
- SVG arrows everywhere an equation appears, never the `→` character — the
  shipped font subsets do not contain it.
- `c4-05` links forward to `c5-01-combustion.html`, which exists.
- No props beyond `showDraft` on any C4 lesson. The instruments have no dial
  that is a teaching decision rather than a student action; inventing one would
  be a tweak for the sake of the panel.
