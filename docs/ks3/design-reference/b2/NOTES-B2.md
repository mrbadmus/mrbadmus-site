# B2 — Movement: skeleton and muscles · author's notes

Four lessons, complete unit. Draft — nothing here has been science-reviewed.
Flags are numbered so they can be answered by number.

Queue resolution and filename convention are in `NOTES-P3.md` §0 and apply
unchanged: B2 is the second Year-7 Biology unit by declaration order in
`structure.py`, and slugs are verbatim from that file.

---

## 1. Statutory coverage

| Lesson | Statements |
|---|---|
| `what-the-skeleton-does` | `KS3.B.SKEL.01` (all four functions: support, protection, movement, making blood cells) |
| `joints` | `KS3.B.SKEL.01` — the *movement* clause, developed |
| `antagonistic-muscle-pairs` | `KS3.B.SKEL.03` |
| `biomechanics-forces-in-the-body` | `KS3.B.SKEL.02` |

All three SKEL statements are covered, none twice. `joints` has no statement
of its own: the 2014 document does not name joints, but it names movement, and
a movement lesson that never mentions how a bone can move at all is not
teachable. It is a `structure.py` lesson slot, so it is authored; if you would
rather it were merged into `what-the-skeleton-does`, that is a structure change
rather than a content one.

---

## 2. Family patterns as applied

- **SYSTEM (b2-01, b2-03) — perturbation, never labelling.** `b2-01` switches
  off the skull, the ribcage, the femur and the marrow in turn, and follows the
  consequence chain to where it always ends: cells that cannot respire. Four
  parts, four different routes, one destination — and two wildly different
  clocks (ribcage, minutes; marrow, months). No labelled skeleton diagram
  appears anywhere in the unit, deliberately. `b2-03` does the same to a muscle
  pair: switch the triceps off and the arm can still be raised and still be
  dropped, but can never be pushed straight.
- **MODEL (b2-02) — build it, then find where it breaks.** Four joint types
  driven on a bench, then four real places in the body, the last of which
  (the base of the thumb) **is none of the four**. The closing line is that a
  model which fits everything has stopped telling you anything.
- **QUANTITATIVE (b2-04)** — follows the pattern defined in `NOTES-P3.md` §1
  exactly: the rig reports the load and the two distances and refuses to
  report the muscle force; the four-part formula treatment; the student's own
  rig numbers in the scaffolded attempt; and only then a force meter that
  confirms the arithmetic. The "measurement of force exerted by different
  muscles" that the statement asks for is the three-meter comparison, with
  three readings each and a mean.

---

## 3. New instruments

### 3.1 `system-switch` — flagship of `b2-01` (no canvas)

A DOM instrument, not a drawing. Part tabs, a required prediction, a
switch-off button, then a consequence chain revealed as levelled steps.

- **Controls:** four part tabs; four prediction options per part; *switch this
  part off* (locked until a prediction is committed).
- **Readouts:** the chain — one step per row, each tagged with the level it
  happens at (`Cell` / `Tissue` / `Organ` / `Organism`), plus a closing line
  per part and a summary once all four have been opened.
- **Payload:** `{parts: [{id, name, does, prompt, options[4], chain: [{level,
  text}], close}], predicted: {}, opened: {}}`.
- **Note for Code:** the level chips are a rendering of the chain data, not a
  claim that failures always climb. Two of the four chains descend to the cell
  and stop; that is the honest shape and it is the point of the summary line.
  A `showLevels` prop turns the chips off for a class that has not met the
  levels yet.

### 3.2 `joint-bench` — flagship of `b2-02`

- **Controls:** joint type (hinge / ball-and-socket / pivot / fixed); a bend
  slider whose range comes from the joint (and which is **disabled** for pivot
  and fixed); a *try to twist it* toggle.
- **Readouts:** the drawn sweep of allowed movement, the number of directions,
  where in the body you have one, what holds it together, and a written *trade*
  line. When a joint refuses to twist, the refusal is drawn (a dashed ring with
  a drawn cross) **and** written out.
- **Payload:** `{joint: id, bend_deg: number, bend_range: [min, max],
  twist_allowed: bool, twisting: bool}`.
- **aria-label:** *"A two-bone model of a hinge joint. The moving bone is set
  at 20 degrees within a range of 0 to 145 degrees, and the joint cannot be
  turned about its long axis at all."*

### 3.3 `muscle-pair` — flagship of `b2-03`

- **Controls:** which muscle contracts (biceps / triceps / both / neither);
  switch either muscle off.
- **Readouts:** live elbow angle; each muscle's state in words (contracted /
  relaxed / switched off); a status line; and an interpretation line that
  changes with the sabotage.
- **Payload:** `{mode: 'biceps'|'triceps'|'both'|'none', dead: {biceps, triceps},
  angle_deg}`.
- **Mechanism:** the arm animates towards a target angle. Both contracted →
  the target is wherever it already is (the joint locks). Nothing contracted →
  it falls under gravity, more slowly than a muscle moves it. This is the
  thing worth keeping: *gravity straightens a hanging arm for free*, which is
  why the triceps is the smaller muscle, and a student can find that out by
  pressing "Neither".

### 3.4 `arm-lever` — flagship of `b2-04`

- **Controls:** load 0.5–5 kg; muscle attachment 3–6 cm; hand distance 32 cm
  or 16 cm; *fit a force meter to the tendon*.
- **Readouts:** weight of the load in N, both distances from the elbow, and a
  muscle-force tile reading **"not measured — you work it out"** until the
  meter is fitted. Drawn: both force arrows and two dimension lines.
- **Payload:** `{load_kg, d_muscle_cm, d_load_cm, g: 10, meter_fitted: bool}`.
- **Design note:** the meter exists so the student can *check* their own
  arithmetic, not skip it. If Code makes the meter reading available before the
  calculation, the lesson is gone.

---

## 4. Science flags — numbered for review

1. **b2-04 ownership — the one that needs a ruling before this unit freezes.**
   §7.4 fixes Forces as **owned by Physics P4, referenced by Biology B2
   (biomechanics)**. But `biomechanics-forces-in-the-body` is an owned lesson
   slot in `structure.py` with no `owned_by` marker, and biomechanics without
   the turning effect of a force is arithmetic with no idea in it. What I have
   done: taught it as **turning effect = force × distance from the joint**,
   with the full four-part formula treatment, and put a pointer in the end
   matter — *"Taught in full in Physics: Forces"*. The word **moment** does not
   appear. Three options: (a) keep as is; (b) cut the calculation from B2 and
   make it reference-only, which guts the QUANTITATIVE lesson; (c) keep, and
   have P4 `moments` open by naming what B2 already did. My recommendation is
   (a) with (c) to follow — but P4 must be written knowing this exists.
2. **g = 10 N/kg**, stated in a small line at the bottom edge of `b2-04`.
   Confirm 10 rather than 9.8 for KS3 throughout the course.
3. **The 4 cm / 32 cm arm.** Biceps insertion at the radial tuberosity is
   typically 4–5 cm from the elbow's axis, and hand-to-elbow around 30–35 cm.
   The lesson uses 4 cm and 32 cm to give a clean ×8. Confirm the figures are
   defensible as typical adult values.
4. **The forearm's own weight is ignored** everywhere in `b2-04`. Real biceps
   forces are therefore somewhat higher than the page's numbers. Rung 2's
   distractor mentions it, and the feedback says it adds but is not the reason.
   Confirm that is the right level of honesty for KS3.
5. **Two million red blood cells per second** (`b2-01`, marrow). Commonly
   quoted figure; confirm.
6. **"Red blood cells wear out after about four months."** ~120 days. Confirm
   the rounding to "about four months".
7. **"You replace roughly a tenth of your skeleton every year"** (`b2-01`,
   think-again block). Adult bone turnover is usually quoted at about 10% a
   year. Confirm.
8. **Astronauts lose 1–2% of bone mass a month** (`b2-01` rung 4). Widely
   quoted for weight-bearing bones. Confirm, and confirm you are happy with
   "even though they eat well and exercise".
9. **The tennis-player's arm.** Denser bone in the racket arm is a real and
   well-replicated finding. Confirm it is safe to state flatly.
10. **The shoulder is the most commonly dislocated joint** (`b2-02` hook).
    True of the joints people usually name. Confirm the phrasing.
11. **Cartilage has no blood supply and is fed by loading** (`b2-02` stretch).
    Correct for articular cartilage; the claim that it therefore heals poorly
    is standard. Confirm the wording is not overstated.
12. **The saddle joint at the base of the thumb** is offered as the case the
    four-type model cannot hold. It is a real fifth type, and the point is
    about models rather than about thumbs. Confirm you want a named
    beyond-the-model example here rather than a vaguer one.
13. **Eccentric contraction** (`b2-03`, movement 4 — lowering a box slowly).
    The biceps is contracting while lengthening. The word *eccentric* is not
    used; the copy says the muscle is "holding on and letting the box down".
    This is the hardest idea in the unit and the one I would most expect you to
    cut. It is also the one that makes "contract" mean something other than
    "get shorter", so it may need to go or need a sentence.
14. **Co-contraction** (`b2-03`, "both"). Contracting both muscles stiffens the
    joint; the stretch layer names steadying a camera and gymnastic rings.
    Confirm this is a legitimate KS3 extension rather than A-level creep.
15. **"Gravity straightens a hanging arm, which is one reason the triceps is
    the smaller of the two."** True and commonly said. Confirm.
16. **Grip / biceps / leg-press force values** in `b2-04`'s three-meter panel
    (305 N, 203 N, 1422 N as means of three). These are plausible adult values,
    not measured ones. If you want real figures from a school dynamometer,
    say so and I will mark them as `pending-data` instead.
17. **No anatomical diagrams anywhere in this unit.** No skeleton, no labelled
    muscle. Everything is either a schematic instrument or prose. If you want a
    real figure — a skeleton photograph for `b2-01`, an X-ray of a joint for
    `b2-02` — those are `figure` slots to add to the diagram manifest, and I
    have not invented placeholders for them.

---

## 5. Misconception register — proposed `BODY` family

A new family. `CELL` is about cells; these are about body systems and how they
do work. Same request as with `FORCE` in P3: **please rule on the family before
any of these IDs are referenced**, since IDs are permanent.

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `BODY-01` | Bones are dead — they are the hard leftovers, like a tent frame. | `think-commit-alive` | `think-reveal-alive` | `what-the-skeleton-does` |
| `BODY-02` | The skeleton's job is holding you up; the other things bones do are extras. | `hook-two-breaks` | `switch-off-chains` | `what-the-skeleton-does` |
| `BODY-03` | How bad a break is depends on how big the bone is. | `hook-two-breaks` | `hook-reveal` | `what-the-skeleton-does` |
| `BODY-04` | Muscles hold the bones together at a joint. | `think-commit-achilles` | `think-reveal-achilles` | `joints` |
| `BODY-05` | All joints work the same way; some are just stiffer than others. | `bench-gate-knee-shoulder` | `joint-bench` | `joints` |
| `BODY-06` | A joint could rotate further if the muscles were stronger or the ligaments looser. | `ladder-r2` | `ladder-r2-feedback` | `joints` |
| `BODY-07` | Muscles push as well as pull. | `hook-commit-door` | `muscle-pair` | `antagonistic-muscle-pairs` |
| `BODY-08` | When a muscle relaxes it stretches itself back out. | `think-commit-stretch` | `think-reveal-stretch` | `antagonistic-muscle-pairs` |
| `BODY-09` | If both muscles of a pair contract, the movement is faster or stronger. | `bench-gate-both` | `muscle-pair-both` | `antagonistic-muscle-pairs` |
| `BODY-10` | A muscle pulls with the same force as the weight it is holding. | `hook-commit-bag` | `arm-lever-rig` | `biomechanics-forces-in-the-body` |
| `BODY-11` | Levers always make things easier, so the body's levers reduce the force needed. | `think-commit-lever` | `think-reveal-lever` | `biomechanics-forces-in-the-body` |

Cross-references worth recording now: `BODY-01` resurfaces in B3 (`the
digestive system` — the same "organs are just plumbing" instinct) and in B9;
`BODY-07` is the biology face of the same wrong idea as P4's coming
"forces are things objects have"; `BODY-10`/`BODY-11` will be met again in P4
`moments` and P1 `simple-machines`, where the force-for-distance trade is the
whole lesson — that is the natural place to say "this is the arm again".

---

## 6. For Code

- Four instruments in §3; `system-switch` is DOM-only and the cheapest of the
  four to make real.
- Every slider is bound to `input` **and** `change`.
- `b2-03` animates from one `requestAnimationFrame` loop that mutates instance
  fields, and calls `setState` only when a control changes. `b2-04` does not
  animate at all — it is a static drawing driven by two sliders, which is
  exactly what a diagram-with-numbers should be.
- Rail stops: five in b2-01, b2-02 and b2-03; six in b2-04 (the extra one is
  the force-meter comparison the statutory statement asks for).
- Cross-links use generator output names (`b2-02-joints.html`), and `b2-01`
  links back to `b1-05-levels-of-organisation.html` because the switch-off
  chains are written in levels language and assume it.
- **`b2-04` has no dependency on P4 in code** — no shared component, no import.
  The dependency is entirely editorial and is flag 1.


---

## Change log — 15 Aug 2026 (review round 2)

Four changes from Mide's review, applied across every lesson that carries a
formula. Nothing else was touched.

1. **FIFA is now visible as FIFA.** The worked example and the scaffolded
   attempt both show a lettered badge on each step — **F**ormula, **I**nsert,
   **F**ine-tune, **A**nswer — matching the pattern set in `b1-02`. Step 3 was
   called "Work it out" in round one and is now **Fine-tune**, which is the
   step the letter stands for: do the arithmetic, sort the units, rearrange if
   the thing asked for is not the one on the left. The terser round-one copy is
   kept — the badges were added, the prose was not.
2. **Every formula now carries the cover-the-one-you-want panel.** A drawn
   figure with the chosen quantity physically covered, three cover buttons, the
   arrangement that falls out, and one sentence saying why. It is a real
   instrument, not a static picture.
3. **Ramp height is now visible in the light-gate bench** (`p3-01` only): low,
   medium and high each draw a different ramp, with the slope picked out and a
   height bracket up the back. Changing the setting changes the picture, which
   is what a student needs before the times change too.
4. Notes updated; the three unit zips were rebuilt.

### New instrument kind: `cover-triangle`

Shared shape across all three lessons that use it, and the one to build once.

- **Controls:** one button per quantity in the relationship ("Cover s",
  "Cover d", "Cover t").
- **Readouts:** the drawn figure with an opaque plate over the chosen
  quantity (the covered label stays faintly visible underneath, so a student
  can see what they covered); the arrangement that results, in display type;
  one sentence naming the operation and why.
- **Payload:** `{shape: 'triangle'|'bar', cells: [{id, label, slot:
  'top'|'left'|'right'}], covered: id, results: {id: {result, sentence}}}`.
- **aria-label** describes the mechanism: *"A formula triangle. Distance sits
  above a dividing line; speed and time sit below it, multiplied together.
  Covering one letter leaves the way to work it out."*
- **Reduced motion:** nothing animates; the plate simply appears.

### `b2-04` specifically

The turning-effect triangle (T on top, F × d underneath) now covers, with the
same three-button pattern as `p3-01`. The balanced-moments line
`F₁ × d₁ = F₂ × d₂` was reworded to "Nothing moving:" so it reads as the
condition it is rather than as a fourth arrangement of the triangle.
