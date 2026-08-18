# B8 — Respiration · author's notes

**Complete unit: five of five lessons authored.** Draft — nothing here has been
science-reviewed. Flags are numbered so they can be answered by number.

---

## 0. What exists

| Lesson | Type | Status |
|---|---|---|
| `b8-01-aerobic-respiration` | PROCESS | **authored** |
| `b8-02-why-every-cell-respires` | SYSTEM | **authored** |
| `b8-03-anaerobic-respiration-in-humans` | PROCESS | **authored** |
| `b8-04-fermentation` | PROCESS | **authored** |
| `b8-05-aerobic-vs-anaerobic` | CONTRAST | **authored** |

Statutory position: all four RESP statements covered. `RESP.01` (aerobic and
anaerobic respiration, and the breakdown of organic molecules enabling all other
chemical processes) by b8-01 and b8-02 together — the second clause is the whole
of b8-02 and is the one usually skipped. `RESP.02` (word summary for aerobic
respiration) by b8-01. `RESP.03` (anaerobic respiration in humans and
micro-organisms, including fermentation, and its word summary) by b8-03 and
b8-04. `RESP.04` (differences in reactants, products and implications) by b8-05.

**Filename note:** the slug in `structure.py` is `fermentation`; the lesson
title is *Fermentation and what we use it for*. The file is
`b8-04-fermentation.dc.html`, slug verbatim, per §8.4.

---

## 1. The unit's shape

The five lessons are a single argument, not five topics:

1. **b8-01** establishes the reaction and, through the mass ledger, that nothing
   is created or destroyed.
2. **b8-02** answers *so what* — the statutory clause about enabling every other
   process — and is where the plant case is settled.
3. **b8-03** breaks the aerobic assumption with a demand the supply cannot meet.
4. **b8-04** takes the same anaerobic reaction out of the human body and into an
   organism that lives on it.
5. **b8-05** puts the two side by side and separates rate from yield, which is
   the idea the whole unit exists to land.

b8-05 deliberately holds back the full comparison until last: b8-03 states only
"far less energy" and points forward, so the CONTRAST lesson has something left
to do.

---

## 2. New instruments

### 2.1 `mass-ledger` — flagship of `b8-01`

- **Controls:** four amounts of glucose; *where does it all go?*
- **Readouts:** a two-column in/out table in grams, two totals that match, an
  energy figure held outside both totals, and a three-row exits panel.
- **Model:** stoichiometric, from 180 g glucose + 192 g oxygen giving 264 g
  carbon dioxide + 108 g water, and 15.6 kJ per gram.
- **Note for Code:** the totals match **by construction**, and the legal line
  says so. Energy is deliberately printed outside the totals — it is the visual
  form of the argument that energy is not a substance.

### 2.2 `cell-demand` — flagship of `b8-02`

- **Controls:** five cell tabs, one of them a plant cell; *cut off the oxygen*.
- **Readouts:** what the cell does, an energy-share bar chart, a mitochondria
  note, and what fails first.
- **Payload:** `{cells: [{id, label, name, origin, job, spend: [{name, pct}], mito, fails}]}`.
- **Design note:** the root hair cell is the whole reason the bench exists. It
  is what makes `RESP-03` unarguable, and the *cut off the oxygen* line for it
  sets up b8-02's rung 4 on waterlogged soil.

### 2.3 `oxygen-debt` — flagship of `b8-03`

- **Controls:** four paces; *run for 10 s*; *stop and recover 30 s*; reset.
- **Readouts:** demand, oxygen delivered, lactic acid, breathing rate, plus a
  note that changes with the phase.
- **Model:** oxygen supply climbs 18 units per step to a ceiling of 80; the gap
  between demand and supply accumulates as lactate; recovery clears 22 per 30 s.
- **Note for Code:** the breathing bar is driven by **lactate, not pace**. That
  is the entire teaching point — it must stay high after the runner stops.

### 2.4 `fermenter` — flagship of `b8-04`

- **Controls:** organism, oxygen, temperature, sugar; two preset buttons
  (brewery, yoghurt maker).
- **Outcome precedence:** killed (80 °C) beats starved (no sugar) beats aerobic
  (open vessel) beats fermenting. Each branch has its own outcome text.
- **Note for Code:** the *open and stirred* branch for yeast is not a failure
  state — it is how yeast itself is manufactured, and the text says so. Do not
  let a revision turn it into an error message.

### 2.5 `route-decider` — flagship of `b8-05`

- **Controls:** five situations, three routes, *check it*.
- **The marathon case is the instrument.** Most students pick anaerobic because
  the runner is working hard; the verdict separates *hard* from *is the oxygen
  supply keeping up*.
- Bench marking follows the house rule — no green and red on the options; the
  verdict panel names the answer in a sentence.

---

## 3. Science flags — numbered for review

1. **"Most of the fat you lose is breathed out"** (b8-01 hook, rung 2). Correct,
   and the usual published split is about 84% exhaled as CO2 and 16% as water.
   The lesson says "most" and "the rest as water" rather than quoting figures.
   **Confirm you want it unquantified**, or give me the split to state.
2. **The ledger arithmetic** (b8-01): 180 : 192 : 264 : 108 by mass, and
   15.6 kJ per gram of glucose. Confirm the energy figure and the rounding
   (values under 100 g print to 1 d.p.).
3. **"Respiration is not burning"** (b8-01 think-again): no flame, enzyme-
   controlled small steps, 37 °C. Confirm this framing is wanted, since some
   schemes teach "respiration is a form of combustion".
4. **Mitochondria as former bacteria** (b8-01 *Going further*), about 1.5 billion
   years ago, own DNA, own division. Standard endosymbiosis, stated as "the
   accepted explanation". Confirm at KS3.
5. **"A third of a heart muscle cell's volume is mitochondria"** (b8-01, b8-02).
   Commonly quoted, varies by source and species. Confirm or soften.
6. **"Three weeks, three days, four minutes"** (b8-02 hook and think-again).
   Rules of thumb, not measurements, and the four-minute figure is for the onset
   of brain damage rather than death. **Confirm the framing** — this is the
   flag I would most want answered in B8.
7. **"The brain is about a fiftieth of body mass and uses about a fifth of
   resting energy"** (b8-02 nerve cell). Standard figures. Confirm.
8. **Energy shares on the b8-02 bench are invented proportions**, and the legal
   line says so. Confirm an explicitly illustrative bar chart is acceptable, or
   I will replace the percentages with ranked words.
9. **Root hair cells and active transport** (b8-02, rungs 1 and 3). Active
   transport is not named in the KS3 programme of study. It is used here because
   the statutory clause is *enabling all the other chemical processes* and
   active transport is the clearest example that is not movement. **Confirm you
   want the term introduced at KS3.**
10. **Hibernation** (b8-02 *Going further*): body temperature to a few degrees
    above ambient, heart rate to a handful of beats a minute, disturbance
    costing a serious fraction of the reserve. Confirm.
11. **Delayed-onset muscle soreness is not lactic acid** (b8-03 think-again),
    with blood lactate clearing within about an hour. Well supported and
    contradicts what many PE departments teach. **Confirm you are happy to
    contradict it in print** — I would keep it, but it is the kind of paragraph
    that generates a staffroom conversation.
12. **The oxygen-debt model** (b8-03): arbitrary units, a fixed aerobic ceiling,
    lactate as one accumulating quantity. Confirm the model is acceptable, and
    confirm "oxygen debt" rather than the more modern "excess post-exercise
    oxygen consumption", which I judged wrong for KS3.
13. **The liver's two options for lactate** (b8-03 *Going further*): oxidise it,
    or convert it back to glucose. Correct, unnamed as the Cori cycle. Confirm.
14. **Blood lactate testing and lactate threshold** (b8-03 *Going further*).
    Confirm the claim that it is among the best single predictors of endurance
    performance.
15. **Bread: the ethanol evaporates** (b8-04 hook, rung 2). Correct; trace
    amounts remain in the crumb, which the lesson does not mention. Confirm the
    simplification.
16. **Yeast in an open stirred vessel respires aerobically and is how yeast is
    manufactured** (b8-04 bench). Correct and rarely taught. Confirm.
17. **Fermentation as preservation** (b8-04 think-again), including "weak beer
    was safer than water in medieval cities". The beer claim is widely repeated
    and has been questioned by historians. **Flag: I would keep it as an aside
    or cut it — your call, and it is the one line in B8 that is history rather
    than science.**
18. **Industrial fermentation** (b8-04 *Going further*): insulin from GM
    bacteria, previously from pig and cattle pancreases; penicillin; Quorn;
    ethanol fuel in Brazil. Confirm.
19. **"About twenty times more energy"** (b8-05 throughout). From the usual
    2 vs 38 ATP comparison, so about nineteen. Stated as "about twenty" and the
    legal line says the exact ratio depends on the accounting. Confirm.
20. **The Great Oxygenation Event** (b8-05 *Going further*) described as
    arguably the largest mass extinction in Earth's history, and anaerobic
    respiration as the older process. Confirm at KS3, and confirm the overlap
    with b7-04's oxygen-history paragraph is deliberate rather than repetitive
    — I judged it a callback, but two lessons now tell that story.
21. **No diagrams in the unit.** A mitochondrion and a labelled leaf-and-lung
    gas-flow figure are the obvious candidates and neither is in the diagram
    manifest.

---

## 4. For Code

- Five instruments in §2, all DOM-only. No timers, no canvas anywhere in B8.
- Rail stops: four in all five lessons.
- Cross-links inside B8 form a chain (b8-01 → b8-02 → b8-03 → b8-04 → b8-05) and
  every target exists. **b7-01's forward link to `b8-01-aerobic-respiration`
  now resolves**, which closes the only dangling link B7 shipped with.
- Outward links: c2-06 (twice, from b8-01 — the mass argument leans on it),
  b4-01, b4-04, b4-05, b1-04, b1-06, b3-06, b3-08, b5-02, p1-04, b7-04.
- Tweak props: `showDraft` on all five; `startAmount` on b8-01, `startCell`
  on b8-02, `startPace` on b8-03. b8-04 and b8-05 have preset buttons on the
  bench instead, which do the same job in the page rather than in the panel.

---

## 5. Misconception register — `RESP` family, opened with ten entries

`RESP-01` to `RESP-10`, written into `docs/ks3/misconception-register.md`
with a new prefix row. Two per lesson.

Two overlaps are deliberate and are worth a ruling:

- `RESP-03` (*plants photosynthesise instead of respiring*) sits next to
  `BREATH-13` (*plants respire at night and photosynthesise in the day*).
  B4's is about the timing, B8's is about whether it happens at all. b8-02
  points at b4-05 rather than restating it.
- `RESP-06` and `RESP-09` are both about the aerobic/anaerobic relationship.
  `RESP-06` is *they switch*; `RESP-09` is *rate confused with yield*. They
  are elicited by different activities in different lessons and I judged them
  distinct, but they could be merged if you would rather have nine.
