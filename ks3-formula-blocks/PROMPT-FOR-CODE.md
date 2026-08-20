# Prompt for Code — the formula block, and nothing else

## Scope, before anything else

You are being given ten complete lesson files. **Nine of them are already live and
you must change exactly one region of each: the formula block that opens the FIFA
sequence.** Everything else on those nine pages stays byte-for-byte as it is on
the live site.

> **ONLY THE FIFA FORMULA BLOCK CHANGES. EVERYTHING ELSE STAYS AS IS.**

Read that as a hard constraint, not a preference. The attached files are the full
pages because that is the only way to hand you the block in context — they are
**not** an instruction to re-deploy the whole page. If your diff for any of the
nine touches anything outside the block described below, the diff is wrong.

Do not change, reformat, re-indent, re-order or "tidy":

- the hook block, its options, or its reveal;
- any bench / instrument, its controls, its readouts, its state machine or its notes;
- the **FIFA worked example itself** — the `Step 0 of 4` counter, the reveal
  button, the four step cards, their maths lines or their notes;
- the student scaffold that follows it (option groups, number field, unit select,
  commit counter, dark reveal panel);
- the key fact, the misconception block, the mastery ladder, its rungs,
  distractors, corrections or criteria;
- the key note, *Going further*, the endmatter, the legal line, the nav, the
  progress rails, the footer;
- any logic outside the named keys in §3;
- tokens, fonts, stylesheets, or the design system.

The tenth file, `p5-01-pressure-force-over-area.dc.html`, is a **brand-new lesson**
(P5 Pressure, slot 1). That one ships whole.

## 1. What the block must look like — the locked pattern

A formula block is **a diagram plus a key. It is never an explanation.** Eight
elements, in this order, and nothing else:

1. **Banner** — the relationship in words, display type, centred, in a card with a
   3px ink border.
2. **Eyebrow** — `The triangle` (or `The bar` for a part–whole bar).
3. **Heading** — `Cover the one you want`.
4. **Cover buttons** — one per symbol, labelled `Cover T`, `Cover F`, `Cover d`.
   Active button is ink-filled with paper text.
5. **The figure**, on the left — triangle filled `--ks3-blue-tint` with ink
   strokes; the covered cell blacks out to `--ks3-ink` and shows its letter in
   `--ks3-ink-ghost`.
6. **The rearrangement it produces**, large display type: `d = T ÷ F`.
7. **One line, verbatim** — *Two things side by side means multiply. One thing
   over another means divide.* (Bars use: *Two parts side by side make the whole.
   Cover the part you want and take the other one away from the whole.*)
8. **The symbol key** — one row per symbol: a boxed display-type letter badge
   (46px, `--ks3-blue-tint`, ink border), the quantity name in body type, and the
   unit as a mono pill (`min-width: 4.6rem`, background `--ks3-accent-text`, label
   `--ks3-ground`, centred). Never a small mono list.

**Banned, explicitly.** These are the things being removed and they must not come
back in any form:

- a sentence per cover state — *"F sits underneath, with T above it. Cover it and
  you are left with T over d — divide."*
- a paragraph arguing why the relationship earns a triangle — *"This one is a
  genuine product, so the triangle is a fair tool."*
- a mono restatement of the formula under the diagram — *"moment in N m = force in
  N × distance in m"*.

One extra display line is allowed **only** where the physics needs it: a balance
condition (`Nothing moving: F₁ × d₁ = F₂ × d₂`) or a unit-pairing warning
(`watts × seconds gives joules`). Load-bearing qualifiers ride **inside the key's
quantity name** — `force, at right angles to the surface` — never in a sentence.

## 2. The nine edits, file by file

| File | Block | Was | Now |
|---|---|---|---|
| `b2-04-biomechanics-forces-in-the-body.dc.html` | `The triangle` section | per-cover sentence + mono unit list | banner `Turning effect = force × distance from the joint`; key T / F / d; keeps `Nothing moving: F₁ × d₁ = F₂ × d₂` |
| `p3-01-speed.dc.html` | `The triangle` section | per-cover sentence + mono unit list | banner `Speed = distance ÷ time`; key d / s / t |
| `p4-07-moments.dc.html` | `#s-formula` | static triangle labelled in words + 2 prose paragraphs + 3 mono lines | interactive cover triangle M / F / d; `at right angles to the handle` moved into the key |
| `p2-01-energy-in-food.dc.html` | `#s-worked` (block above the FIFA steps) | `<canvas>` triangle + prose | SVG cover triangle E / e / m; buttons moved under the heading |
| `p2-03-calculating-energy-transferred.dc.html` | `#s-tri` | `<canvas>` triangle + prose; heading duplicated the formula | SVG cover triangle E / P / t; duplicate `E = P × t` heading deleted; unit pairing kept as the allowed extra line |
| `p1-08-simple-machines.dc.html` | `#s-balance` | 4-sentence paragraph + per-cover prose | **keeps its canvas beam** (a balance of two products is not a triangle); prose cut to one line, result line + key E / F / d added |
| `c2-06-conservation-of-mass.dc.html` | `The bar` block | per-cover sentence; words line unbannered; bar in `--ks3-card` | banner card; bar in `--ks3-blue-tint`; key in grams |
| `c4-04-mass-in-a-reaction.dc.html` | `#s-cover` | `"a sum, not a division, so it has no triangle"` paragraph + per-cover sentence | banner card; eyebrow `The bar`; bar cards in `--ks3-blue-tint`; key in grams |
| `b1-02-using-a-microscope.dc.html` | `#s-formula` | per-cover prose, no result line | result line `total = eye × obj`; key with `no unit` pills; triangle recoloured |

## 3. Logic-side changes — the complete list

Nothing else in any logic class changes.

- **Removed render keys:** `coverSentence` (b2-04, p3-01, c2-06, c4-04),
  `coverNote` (p2-01, p2-03, p1-08), `coverText` (b1-02).
- **Added render keys:** `coverResult` (p2-01, p2-03, p1-08, b1-02 — the other
  files already had it), and `coverTop` / `coverLeft` / `coverRight` (p2-01,
  p2-03, p4-07, p5-01).
- **New in `p4-07`:** a `COVERS` map, `cover: 'M'` in state, and a `coverVals()`
  method included in the `renderVals()` `Object.assign`.
- **Cover-button labels** now read `Cover <symbol>`: p2-01 (`Cover E`, `Cover e`,
  `Cover m`), p2-03 (`Cover E`, `Cover P`, `Cover t`), p1-08 (`Cover E`,
  `Cover F`, `Cover d`, with `The whole relationship` left as it was — it is not a
  symbol).
- **`COVERS[...].sentence` values are still present in p2-01, p2-03, p1-08, c2-06,
  c4-04, p3-01 and b2-04 but are no longer rendered anywhere.** Delete them when
  you port; they are dead data, and leaving them invites someone to put the prose
  back.
- **p2-01 and p2-03 no longer have a triangle canvas.** Their `drawTri()`,
  `triRef` and `triAlt` are now dead and can be deleted. `drawBench()` in p2-03 is
  **not** dead — leave it alone.

## 4. Standing rules these files obey

- No `→`, `✓` or `✕` characters anywhere — the font subsets lack them; all are
  inline SVG.
- No interpolated hole inside an SVG `<text>` element — it renders nothing. Live
  labels are absolutely-positioned HTML spans over a `position: relative` wrapper.
  Attribute holes are fine.
- Formula triangle for **products only**. Sums, differences and balances get a
  beam; a part–whole bar counts as a beam and keeps its cover buttons, because
  covering a part is how you get the subtraction.
- Weight in newtons is mass in kilograms × 10 N/kg wherever it appears.

## 5. `p5-01` — the new lesson

`p5-01-pressure-force-over-area.dc.html`, P5 Pressure slot 1, `QUANTITATIVE`.
Four rail stops (`s-hook`, `s-bench`, `s-formula`, `s-ladder`), a drawing-pin
hook, a block-on-sand bench (3 faces × 10 masses, 3 authored branches keyed to the
sand's 6000 Pa limit), the locked formula block with **force at the apex** because
the product is `force = pressure × area`, a FIFA reveal, a student scaffold on live
bench numbers, one key fact, one misconception block with two entries, a four-rung
ladder, key note, *Going further*, endmatter, legal line.

Two things it needs from you rather than from me — **do not guess these, raise
them**:

1. **Misconception ids.** The page cites none. `PRESS-01` (a sharp point pushes
   harder), `PRESS-02` (pressure only pushes downwards) and `PRESS-03` (pressure is
   a force, so it is in newtons) are proposed and unminted; the register has no
   `PRESS` family open yet.
2. **A dangling register pointer.** `misconception-register.md` routes `ENERGY-11`
   (force multiplication is free energy) to a **P5 `hydraulics`** lesson, and
   `structure.py` gives P5 four slots, none of which is hydraulics. `p5-01`
   confronts `ENERGY-11` in its *Going further* instead. Either re-point the
   register at `p5-01` or open a fifth P5 slot — it cannot stay as it is.

New component family for the register: `block-on-sand` — a sand tray with a fixed
grit texture, a block drawn to scale on any of the three faces of one
0.20 × 0.10 × 0.05 m solid, a weight arrow on its own scale, a footprint dimension
line, and a surface that either runs straight or opens into a trough with the
original level dashed behind it.

## 6. Definition of done

- Nine pages: the diff touches the formula block and nothing else. Diff the rest
  of each file against live and confirm it is empty.
- Every formula block on the site matches §1 in order and content, with no prose.
- No page renders a per-cover sentence, a triangle-justification paragraph, or a
  mono unit list.
- Unit pills read as pills, including single-character units (`g`, `N`, `s`, `m`).
- `p5-01` is added, not merged into anything.
