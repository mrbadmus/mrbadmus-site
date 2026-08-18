# B7 — Photosynthesis · author's notes

**Complete unit: four of four lessons authored.** Draft — nothing here has been
science-reviewed. Flags are numbered so they can be answered by number.

---

## 0. What exists and what does not

| Lesson | Type | Status |
|---|---|---|
| `b7-01-the-photosynthesis-reaction` | PROCESS | **authored** |
| `b7-02-leaves-built-for-the-job` | MODEL | **authored** |
| `b7-03-testing-a-leaf-for-starch` | INVESTIGATION | **authored** |
| `b7-04-why-almost-all-life-depends-on-it` | SYSTEM | **authored** |

Statutory position: all three PHOT statements are now **covered** —
`KS3.B.PHOT.01` (reactants, products, word summary) by b7-01,
`KS3.B.PHOT.03` (adaptations of leaves) by b7-02, and `KS3.B.PHOT.02`
(dependence of almost all life on photosynthetic organisms) by b7-04.
`KS3.B.NUT.06` (carbohydrates made in leaves, minerals and water from the soil)
is covered by b7-01's van Helmont treatment. b7-03 carries no statement of its
own — it is the practical the other three are argued from, which is why it is
placed third rather than second.

---

## 1. New instruments

### 1.1 `reactant-remover` — flagship of `b7-01`

- **Controls:** four dials — light (bright/dim/dark), carbon dioxide
  (normal/soda lime), water (watered/dry), leaf tested (green/white part of a
  variegated leaf); *test a leaf with iodine*; *reset*.
- **Readouts:** rate as a percentage, glucose made, oxygen bubbles per minute,
  carbon dioxide taken from the jar, then an iodine verdict with a per-condition
  explanation.
- **Model:** each dial contributes a factor; rate is the product, so removing
  any one takes the rate to zero. The verdict text has a dedicated branch for
  each single-factor removal and a *more than one thing is missing* branch that
  tells the student to change one variable at a time.
- **Payload:** `{dials: [{id, name, options: [{id, label, f}]}], picks: {}, tested: bool}`.

### 1.2 `leaf-tuner` — flagship of `b7-02`

- **Controls:** four dials — surface area, thickness, stomata, waxy cuticle.
- **Readouts:** photosynthesis rate and water lost per day, both as a percentage
  of an oak leaf, plus a *where this leaf could live* verdict in six branches.
  Two shortcut buttons: *set it to a real oak leaf* and *start again*.
- **Design note:** the instrument opens on a deliberately bad leaf (enormous,
  thick, many stomata, no cuticle) so the first thing the student does is make
  it worse and then discover the trade-off. The oak button is the reveal.
- **Payload:** `{dials: [{id, name, options: [{id, label, r, w}]}], picks: {}}`.

### 1.3 `method-breaker` — flagship of `b7-03`

- **Controls:** five method steps, each done/skipped, plus *how the ethanol is
  heated* (water bath / Bunsen directly); *add the iodine*; *fresh leaf, full
  method*.
- **Readouts:** one of six outcomes — a tag, what you see, why, and a separate
  *can you conclude anything?* line, which is the part that matters.
- **Fault precedence, deliberate:** safety first (ethanol over a flame ends the
  practical), then the faults that destroy the result (no ethanol, no
  destarching), then the ones that only make it hard to read (no boiling, no
  softening). If two steps are skipped the more serious fault is the one
  reported, which is honest — you would not get as far as the second problem.
- **Payload:** `{steps: [{id, num, title, detail, options}], picks: {}, ran: bool}`.
- **Note for Code:** the *water bath vs naked flame* control is not decoration.
  It is the only place in B7 where a wrong choice ends the experiment rather
  than spoiling it, and its outcome text is the safety teaching for the unit.

### 1.4 `trace-it-back` — flagship of `b7-04`

- **Controls:** six foods; *where did that come from?* stepping one link back at
  a time; *start again*.
- **Readouts:** the chain revealed backwards with a note per link, a step count,
  and a per-food verdict.
- **Payload:** `{foods: [{id, label, name, chain: [{name, note}], verdict}], food, shown}`.
- **Design note:** the chains are deliberately different lengths (bread 2,
  salmon 5) so the count varies and the destination does not. The mushroom is
  the case that looks like a counter-example and is not, and it is the one
  rung 2 tests.

---

## 2. Science flags — numbered for review

1. **Van Helmont's figures** (b7-01 hook): willow 2.3 kg growing to 77 kg in
   five years, in 90 kg of dried soil that lost about 57 g. Converted from his
   pounds and ounces. Confirm the conversions and the rounding, and confirm you
   want him named.
2. **"Nearly all the dry mass came from carbon dioxide"** and the hook's answer
   that he was half right to say water. Confirm the hedge.
3. **The word summary** is given as *carbon dioxide + water gives glucose +
   oxygen*, with *requires light energy, absorbed by chlorophyll* under the
   arrow, and rung 1 penalises putting sunlight on the left. Confirm that is the
   form your scheme wants.
4. **The arrow is drawn as inline SVG**, not typed, in the b7-01 summary block —
   the design system's fonts have no U+2192. Elsewhere in the build (b3-06,
   b4-02, c1-06) the arrow *is* typed inside JS strings and falls back to a
   system font. **Flag: that inconsistency is pre-existing and worth one
   ruling** — either drawn everywhere or typed everywhere.
5. **Carbon dioxide at about 0.04% of air** (b7-01 *Going further*), with the
   greenhouse-enrichment and forest-carbon consequences. Confirm.
6. **"Almost all the oxygen in the atmosphere was made this way"** (b7-01 part
   card). Correct. Confirm at KS3.
7. **PLANT-02 "photosynthesis makes energy"** is confronted by pointing at
   P1's conservation of energy and forward at B8. Confirm you want the physics
   cross-reference doing that work.
8. **Chlorophyll absorbs red and blue, reflects green** (b7-02 think-again), with
   the purple-pink grow-lamp example and the green-filter pondweed result.
   Confirm both examples.
9. **The leaf-tuner numbers are invented** and the legal line says so. The
   relative directions are right; the magnitudes are teaching values. Confirm
   that an explicitly illustrative model is acceptable here.
10. **Autumn colour** (b7-02 *Going further*): pigments already present,
    chlorophyll dismantled, nitrogen and magnesium recovered, leaf dropped
    because a broad leaf loses water it cannot replace in winter. Confirm.
11. **Stomata and guard cells are referenced, not taught** — b4-05 owns them
    (§4.6) and b7-02 says so on the feature card. Confirm that is the right
    side of the ownership line.
12. **No diagrams.** A leaf cross-section is the obvious candidate and is **not
    in the diagram manifest**. b7-02 currently teaches the internal structure in
    five cards instead. **Flag: if you want a cross-section it needs a manifest
    entry and a decision on label depth.**
13. **The starch-test method** (b7-03): destarch two days in the dark, boil in
    water about a minute, boil in ethanol in a water bath, dip in hot water,
    spread on a white tile, add iodine. Confirm the timings and confirm the
    order matches your technicians' version.
14. **Safety wording in b7-03.** Ethanol boils at 78 °C, vapour ignites, water
    bath only, no naked flame; iodine stains and irritates; eye protection.
    The legal line says the bench is not a risk assessment and points at the
    school's own. **Confirm the wording with whoever signs the risk
    assessments** — this is the only lesson in the build where a student could
    read the page as permission to do something.
15. **Why starch and not glucose** (b7-03 *Going further*): glucose is soluble
    and osmotically active, starch is insoluble and compact, and the glycogen
    parallel. Confirm the osmosis argument at KS3 — it is the one place B7
    assumes an idea B-series has not formally taught.
16. **"Roughly half of all photosynthesis happens in the sea"** (b7-04
    think-again and legal line). Estimates range either side of half. Confirm
    the hedge, and confirm you are happy with the flat statement that being the
    planet's only oxygen supply is *not* among the reasons rainforests matter.
17. **"No oxygen worth mentioning for the first two billion years"** and oxygen
    as a waste product poisonous to most life at the time (b7-04). Standard, and
    it forward-references B11. Confirm at KS3.
18. **The chemosynthesis layer** (b7-04 *Going further*): 1977, hydrothermal
    vents, tube worms, energy from chemical reactions rather than light.
    Confirm the date and that you want the *almost* in the lesson title
    explained rather than left as a hedge.
19. **Trophic arithmetic** — "around ten kilograms of grass for every kilogram
    of cow" (b7-04 steak chain) and the rung-3 criterion about a field feeding
    more people as wheat than as beef. The 10% figure is the conventional
    teaching value. Confirm you want it stated this early, since B9 owns
    trophic levels.

---

## 3. For Code

- Four instruments, all DOM-only. No timers, no canvas anywhere in B7.
- Rail stops: four in all four lessons.
- Cross-links: b7-01 → b1-03, p1-01, p1-03, b7-02, b4-05, and forward to
  `b8-01-aerobic-respiration.html`. b7-02 → b7-01, b1-04, b4-05, b4-03.
  b7-03 → b7-01, b3-02, b7-02, b6-03. b7-04 → b7-01, p1-01, p2-05, b4-05.
  **The only forward link is b7-01 → b8-01**, and B8 is the next unit in the
  queue, so it resolves as soon as that unit lands. Everything else exists.
- b7-03 leans on b6-03 by name for the *no comparison group* fault, and b7-04
  leans on b4-05 for plant respiration. Both are references, not restatements —
  keep them that way if the lessons are edited.
- Tweak props: `showDraft` on all four; `startFood` (enum) on b7-04.
  b7-02 and b7-03 have no second tweak — the natural ones are `startLeaf`
  and a *start with the full method* boolean, worth adding at review.

---

## 4. Misconception register — `PLANT` family, opened with eight entries

`PLANT-01` to `PLANT-08`, written into `docs/ks3/misconception-register.md`
with a new prefix row. `PLANT` was one of the three families architecture.md
reserved but had not opened; the "not yet opened" note has been updated. Two
entries per lesson, which is the shape the register prefers.

The four minted while the unit was still partial (`PLANT-05` to `PLANT-08`)
were held back until their owning lessons existed, following the register's own
rule. They are now minted because b7-03 and b7-04 are written.

`BREATH-12` and `BREATH-13` already cover *plants are the opposite of animals*
and *plants respire only at night*; B7 does not restate them and b4-05 keeps
them. `PLANT-08` is close to `BREATH-12` and is deliberately distinct: B4's
entry is about the direction of gas exchange, B7's is about purpose — oxygen as
a waste product rather than a service.
