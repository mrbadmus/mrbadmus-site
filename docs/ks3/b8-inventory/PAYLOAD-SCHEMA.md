# B8 — payload schema

Written **before** the authoring passes are dispatched, which is the whole point of it. Same
instrument as `docs/ks3/b7-inventory/PAYLOAD-SCHEMA.md`, and it inherits that document's naming
table unchanged; only the additions are restated here.

**If this document and Design's page disagree, the page wins on MEASUREMENT (what is drawn) and
this document wins on NAMING (what we call it).** Where the page needs something this schema has
not anticipated, follow the page and say so in the report.

Everything below is measured off the five approved pages in `docs/ks3/design-reference/b8/`, not off `NOTES-B8.md`.
Where the two disagree, §9 says so.

---

## 0. Rules that bind all five instruments

1. **All five are DOM-only.** No `<canvas>`, no `requestAnimationFrame`, no `setTimeout`, no
   `setInterval` anywhere in B8 — grepped across all five pages and returns zero on every term.
   `support.js` is the generic DC React shim (`// GENERATED from dc-runtime/src/*.ts`) and contains
   no lesson logic and no rAF. NOTES-B8 §4 says the same and is, here, correct.
2. **All five instruments ship on `ks3-block ks3-dark ks3-practical`** — measured from Design's own
   markup, on `#s-bench` of all five pages, character for character:

   ```html
   <section id="s-bench" class="ks3-block ks3-dark ks3-practical" style="scroll-margin-top: 92px;">
   ```

   That is `segment: "practical"`, the ink-dark ground. Contract §4 is explicit that B1 got two of
   six wrong by inferring the shell from the kind name. Do not infer it. The shell inventory for the
   whole unit is uniform and complete:

   | Section | class attribute, verbatim | Renders as |
   |---|---|---|
   | `#s-hook` | `ks3-block ks3-dark ks3-hook` | core `hook` |
   | `#s-bench` | `ks3-block ks3-dark ks3-practical` | the instrument, `segment: "practical"` |
   | band section † | *(no `ks3-block` class at all)* — bare `<section id="…" style="…background: var(--ks3-band); border: 3px solid var(--ks3-ink)…">` | core `rule` (b8-05: `comparison`) |
   | `#s-think` | `ks3-block ks3-misconception` | core `misconception` |
   | `#s-ladder` | `ks3-ladder` | core `quiz` |
   | `#s-keynote` | `ks3-block ks3-dark ks3-keynote` | core `summary` |
   | *Going further* | `ks3-layer` (no `id`) | core `explainer` |

   † `#s-summary` (b8-01), `#s-jobs` (b8-02), `#s-equation` (b8-03), `#s-two` (b8-04),
   `#s-table` (b8-05).

3. ⛔ **NO RUNTIME STATE IS AUTHORED.** NOTES-B8 §2.2 sketches a payload; every key in §2–§6 below
   that would have held `picks`, `cut`, `seen`, `opened`, `supply`, `lactate` or `phase` is absent
   deliberately. Those are values the *runtime* owns. Under contract R5 a key with no read site is
   a dead key and fails `ks3_key_audit.py`. The renderer initialises its own state.
4. **Every authored key must have a read site in the same pass.** Wire the read or do not author
   the key.
5. **Every student-facing string is lifted byte-identical** from the approved page via
   `node tools/extract_design_payload.js <page>`. Never retype science-bearing copy.
6. **Nothing marks correctness except the ladder.** These are benches. See §6 for the one place in
   B8 where that rule needs reading carefully.

## 1. Naming — B7's table, plus four B8 additions

B7 §1 stands unchanged (`options_label`, `run_label`, `reset_label`, `verdicts`, `hint`, `close`).
Four concepts B7 did not have:

| Concept | The key | Never |
|---|---|---|
| The spent state of the run button | `ran_label` | `done_label`, `shown_label` |
| The mono counter beside the bench heading | `progress` | `status`, `count_label` |
| How many sub-cases must be worked before the stop ticks | `done_after` | `threshold`, `min_seen` |
| A one-press shortcut that sets every dial at once | `presets` | `shortcuts`, `scenarios` |

`test_label`/`tested_label` from b7-01 are **not** carried forward: they named an iodine test, and
no B8 bench runs one. `run_label`/`ran_label` is the general pair.

## 2. `mass-ledger` — b8-01 `#s-bench`

```python
{"kind": "mass-ledger", "id": "the-books-balance",
 "anchor": "s-bench", "segment": "practical", "demand": "investigate",
 "eyebrow": "At the bench · weigh both sides",
 "heading": "The books have to balance",
 "prompt":  "...",                                   # page line 113
 "progress": {"before": "ledger only", "after": "exits shown"},

 "options_label": "Glucose respired",
 "amounts":  [{"id": str, "label": str, "name": str, "grams": int, "note": str}],   # 4
 "start":    "banana",                               # Design's `startAmount` default

 # The model, from the balanced equation. Ratios, not per-amount tables:
 # every printed figure is derived, which is what makes the totals match.
 "per_gram": {"oxygen": 192/180, "carbon_dioxide": 264/180, "water": 108/180, "kj": 15.6},

 "columns":  {"in": "Goes in", "out": "Comes out"},
 "rows_in":  [{"id": "glucose", "name": "Glucose"}, {"id": "oxygen", "name": "Oxygen"}],
 "rows_out": [{"id": "carbon_dioxide", "name": "Carbon dioxide"}, {"id": "water", "name": "Water"}],
 "totals":   {"in": "Total in", "out": "Total out", "energy": "Energy transferred"},
 "units":    {"mass": " g", "energy": " kJ", "dp_below": 100, "group_thousands": True},

 "run_label": "Where does it all go?", "ran_label": "Exits shown",
 "exits_label": "Which way each product leaves",
 "exits": [{"name": str, "route": str}],             # 3 — carbon dioxide, water, energy
 "close": "..."}                                     # `exitsNote`, page line 530
```

**State:** `amount` (one of four ids) and `exits` (bool, one-way — Design has no un-reveal).
**Controls:** four amount tabs → set `amount`; one reveal button → set `exits`.
**Completion:** `exits` → `data-stage-done="1"`. Nothing else on this bench can complete it.

### 2.1 The arithmetic, verified — it balances, exactly, at every amount

180 g glucose + 192 g oxygen → 264 g CO₂ + 108 g H₂O is `C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O` by mass
(180 + 6×32 = 372; 6×44 + 6×18 = 372). Per gram of glucose both sides come to **2.0667**, so the
totals are equal by construction, at any amount, before any rounding. The page's own legal line says
exactly this and it is true.

Checked against Design's printing rule (`x >= 100 ? round(x) : x.toFixed(1)`), the two printed
totals agree at all four amounts and each printed column also sums to its printed total:

| Amount | Glucose | Oxygen | **Total in** | CO₂ | Water | **Total out** | Energy |
|---|---|---|---|---|---|---|---|
| Teaspoon, 4 g | 4.0 g | 4.3 g | **8.3 g** | 5.9 g | 2.4 g | **8.3 g** | 62 kJ |
| Banana, 25 g | 25.0 g | 26.7 g | **51.7 g** | 36.7 g | 15.0 g | **51.7 g** | 390 kJ |
| Plate of pasta, 90 g | 90.0 g | 96.0 g | **186 g** | 132 g | 54.0 g | **186 g** | 1,404 kJ |
| A day, 300 g | 300 g | 320 g | **620 g** | 440 g | 180 g | **620 g** | 4,680 kJ |

Two porting notes fall out of that table and both are load-bearing:

- ⚠️ **The 100 g threshold is per VALUE, not per amount.** At 90 g the same panel prints
  `132 g` beside `54.0 g`. That is Design's rule applied honestly and it must be reproduced, not
  tidied — a student comparing the two columns is reading the totals, and changing the rule changes
  the printed totals.
- ⚠️ **`toLocaleString()` is not a formatting rule.** Design writes `kJ.toLocaleString()`, which is
  the browser's locale, not ours. `units.group_thousands` authors the comma explicitly so the page
  cannot print `1.404 kJ` to a student whose browser is set to a European locale.

**Energy sits outside both totals, in `--ks3-alert`, on the same row.** That is not decoration: it
is the visual form of the argument that energy is not a substance, and rung 2 and the second
`#s-think` paragraph both depend on the student having seen it there. Do not fold it into a total.
15.6 kJ per gram is NOTES flag 2 and stays on Mide's gate.

## 3. `cell-demand` — b8-02 `#s-bench`

```python
{"kind": "cell-demand", "id": "five-cells-one-reaction",
 "anchor": "s-bench", "segment": "practical", "demand": "compare",
 "eyebrow": "At the bench · five cells, one reaction",
 "heading": "What is the energy actually for?",
 "prompt":  "...",                                   # page line 113
 "progress": {"zero": "no cells cut off yet", "some": "{n} of {total} cut off"},

 "options_label": "The cell",
 "spend_label":   "Where its energy goes",
 "mito_label":    "Mitochondria",
 "cells": [{"id", "label", "name", "origin", "job",
            "spend": [{"name", "pct"}],              # 2–3 rows, pct sums to 100
            "mito", "fails"}],                       # 5 cells
 "start": "muscle",                                  # Design's `startCell` default

 "run_label": "Cut off the oxygen", "ran_label": "Oxygen cut off",
 "done_after": 3}
```

**State:** `cell` (current tab) and a set of cell ids whose oxygen has been cut. The cut is
**per cell and one-way**: switching tabs does not un-reveal a cell already cut, and returning to it
shows its `fails` line still open.
**Controls:** five cell tabs → set `cell`; one reveal button → add `cell` to the cut set.
**Completion:** three distinct cells cut. Design's own threshold (`seen >= 3`), kept.

⚖️ **The root hair cell is the reason this bench exists.** It is the only plant cell in the five, it
is what makes `RESP-03` unarguable, and its `fails` line — mineral uptake stops, osmosis does not,
so the plant goes short of minerals long before it goes short of water — is what sets up rung 4 on
waterlogged soil and b8-05's `root` case. If a later pass trims the bench to four cells, this is not
the one to cut.

⚑ The percentages are **invented illustrative proportions** and the page's legal line says so. That
line is not optional decoration. NOTES flag 8 offers to replace them with ranked words; that is
Mide's to rule on and this schema does not pre-empt it — the `pct` field survives either way, since
ranked words would still need an order.

## 4. `oxygen-debt` — b8-03 `#s-bench`

```python
{"kind": "oxygen-debt", "id": "run-it-then-stop",
 "anchor": "s-bench", "segment": "practical", "demand": "investigate",
 "eyebrow": "At the bench · supply against demand",
 "heading": "Run it, then stop and watch",
 "prompt":  "...",                                   # page line 113

 "options_label": "Pace",
 "paces": [{"id": "walk",   "label": "Walking",          "demand": 20},
           {"id": "jog",    "label": "Jogging",          "demand": 50},
           {"id": "run",    "label": "Hard run",         "demand": 85},
           {"id": "sprint", "label": "Flat-out sprint",  "demand": 150}],
 "start": "sprint",                                  # Design's `startPace` default

 "model": {"supply_rest": 25, "supply_max": 80, "supply_step": 18, "supply_decay": 10,
           "recover_demand": 25, "recover_clear": 22,
           "lactate_factor": 0.55, "lactate_max": 100,
           "breathing": {"base": 20, "per_supply": 0.6, "per_lactate": 0.5, "max": 100},
           "run_seconds": 10, "recover_seconds": 30, "bar_divisor": 1.6},

 "bars": [{"id": "demand",    "name": "Energy demand",              "suffix": " units",        "tone": "muted"},
          {"id": "aerobic",   "name": "Oxygen delivered (aerobic)", "suffix": " units",        "tone": "ok"},
          {"id": "lactate",   "name": "Lactic acid in the muscle",  "suffix": " units",        "tone": "alert"},
          {"id": "breathing", "name": "Breathing rate",             "suffix": "% of maximum",  "tone": "muted"}],

 "clock":     {"zero": "on the start line", "suffix": " s", "recovering": " · recovering"},
 "phases":    {"ready": "Standing on the line", "recovering": "Stopped — recovering"},
 "shortfall": {"aerobic": "fully aerobic", "repaying": "repaying",
               "borrowed": "{n} units borrowed per 10 s"},
 "notes":     {"rest": "...", "within": "...", "shortfall": "...",
               "debt": "...", "cleared": "..."},     # five, page lines 448–452

 "run_label": "Run for 10 s", "running_label": "Keep going, 10 s",
 "stop_label": "Stop and recover 30 s", "recovering_label": "Recover another 30 s",
 "reset_label": "Back to the start line"}
```

**State:** `pace`, `supply` (starts at 25), `lactate` (starts at 0), `seconds`, `phase`
(`ready` | `running` | `recovering`), and `ever_recovered` (bool, one-way).
**Controls:** four pace tabs → set `pace`; **Run for 10 s** → advance one running step;
**Stop and recover 30 s** → advance one recovery step (disabled while `phase == "ready"`);
**Back to the start line** → reset `supply`, `lactate`, `seconds`, `phase` — and **not**
`ever_recovered` and **not** `pace`.
**Completion:** `ever_recovered`, set the first time a recovery step brings lactate to exactly zero.

### 4.1 ⚠️ The breathing bar is driven by LACTATE, not by pace

This is the entire teaching point of the lesson, and it is one line of arithmetic. Measured off
page line 438:

```
breathing = min(100, round(20 + supply × 0.6 + lactate × 0.5))
```

`pace` does not appear in it. Neither does `demand`. Nothing about the runner's effort reaches the
breathing bar except through `supply`, which decays slowly, and `lactate`, which is what the
recovery is for. The consequence, traced through Design's own numbers from a flat-out sprint:

| Press | supply | lactate | demand shown | **breathing** |
|---|---|---|---|---|
| (opening state) | 25 | 0 | 25 | 35% |
| Run 10 s | 43 | 59 | 150 | 75% |
| Run 10 s | 61 | 100 (capped) | 150 | 100% |
| **Stop 30 s** | 51 | 78 | **25** | **90%** |
| Stop 30 s | 41 | 56 | 25 | 73% |
| Stop 30 s | 31 | 34 | 25 | 56% |
| Stop 30 s | 25 | 12 | 25 | 41% |
| Stop 30 s | 25 | 0 | 25 | 35% ← `ever_recovered` |

The row in bold is the lesson. **The demand bar collapses from 150 to 25 the instant the runner
stops, and the breathing bar stays at 90%.** A student watching the two bars sees the question the
page asks in its own big-question line — the running has finished, something else has not — and the
`notes.debt` string names it: *"The muscles are not asking for this oxygen — the lactic acid is."*

Three defences of that behaviour, all of which the port must keep:

- **Recovery lowers `supply` too** (`max(25, supply − 10)` while lactate remains). Without that
  term breathing would fall on the supply half as well and the effect would be muddied; with it,
  the only thing holding breathing up after two presses is the lactate term.
- **`recover_clear` is 22 per 30 s and lactate caps at 100**, so a sprint takes five recovery
  presses to clear. That is not padding — a student who presses once and leaves has seen breathing
  fall from 100% to 90%, which is the wrong story. The stop only ticks when lactate reaches zero.
- **`run` climbs `supply` by 18 regardless of pace**, so at walking pace the gap never opens and no
  lactate is made. The bench must be able to show the *aerobic* case or the contrast is untestable;
  `notes.within` is the string for it.

⚠️ **Two dead keys in Design's payload — do not author them.** `runDisabled: false` and
`runStyle: ''` are constants on page lines 506–507 and are read for nothing. Under R5 they fail the
key audit. `stopDisabled`/`stopStyle` are real and are computed from `phase`.

⚑ NOTES flag 12: arbitrary units, a fixed aerobic ceiling, lactate as one accumulating quantity, and
"oxygen debt" rather than EPOC. All Mide's, all still open, and none of them changes this shape.

## 5. `fermenter` — b8-04 `#s-bench`

```python
{"kind": "fermenter", "id": "four-dials",
 "anchor": "s-bench", "segment": "practical", "demand": "investigate",
 "eyebrow": "At the bench · one vessel, four dials",
 "heading": "Set the conditions, see what you have made",
 "prompt":  "...",                                   # page line 113
 "progress": {"zero": "nothing changed yet", "some": "{n} set-up{s} tried"},

 "dials": [{"id": "organism", "name": "Organism",    "options": [{"id": "yeast",    "label": "Yeast"},
                                                                 {"id": "bacteria", "label": "Yoghurt bacteria"}]},
           {"id": "oxygen",   "name": "Oxygen",      "options": [{"id": "sealed",   "label": "Sealed vessel"},
                                                                 {"id": "open",     "label": "Open and stirred"}]},
           {"id": "temp",     "name": "Temperature", "options": [{"id": "cold",     "label": "4 °C"},
                                                                 {"id": "warm",     "label": "30 °C"},
                                                                 {"id": "hot",      "label": "80 °C"}]},
           {"id": "sugar",    "name": "Sugar",       "options": [{"id": "yes",      "label": "Supplied"},
                                                                 {"id": "no",       "label": "None"}]}],

 "start":   {"organism": "yeast", "oxygen": "sealed", "temp": "warm", "sugar": "yes"},
 "presets": [{"id": "brewery", "label": "Set it up as a brewery",
              "dials": {"organism": "yeast",    "oxygen": "sealed", "temp": "warm", "sugar": "yes"}},
             {"id": "dairy",   "label": "Set it up as a yoghurt maker",
              "dials": {"organism": "bacteria", "oxygen": "sealed", "temp": "warm", "sugar": "yes"}}],

 "rate_label":    "Rate {n}% of maximum",
 "outcome_label": "What you have made",

 # ORDERED. First match wins. See §5.1.
 "branches": [{"id", "when": {dial_id: option_id, ...}, "rate": int,
               "line": str,                            # the reaction line beside the rate
               "title": str, "body": str,
               "products": [{"name", "tone", "value" | "none_text"}]}],
 "done_after": 2}
```

**State:** the four dial positions and a count of set-ups tried.
**Controls:** nine dial buttons and two preset buttons; every one of them increments the count.
**Completion:** two set-ups tried. Design's own threshold (`seen >= 2`), kept.

### 5.1 ⚠️ The precedence tree is ordered and the order is the pedagogy

Measured off the `outcome(d)` method, page lines 442–471, whose own comment reads
*"Order matters: killed beats starved beats aerobic beats fermenting."*

1. **`killed` — `temp == "hot"`.** Rate 0, line `no reaction`.
   Title: *"Nothing, and nothing will happen now"*.
   Body: *"At 80 °C the organism's enzymes are denatured and the cells are dead. Cooling the vessel
   will not bring them back — this is the same permanent change you met in b3-06, and it is why a
   baker uses warm water rather than hot."*
2. **`starved` — `sugar == "no"`.** Rate 0, line `no reaction`.
   Title: *"Nothing — no fuel"*.
   Body: *"A living organism with nothing to respire. Fermentation is respiration, and respiration
   needs a substrate: no sugar, no products, however perfect the other three dials are."*
3. **`aerobic` — `oxygen == "open"`.** Rate 100. Two texts, by organism:
   - **Yeast** — line `glucose + oxygen → carbon dioxide + water`.
     Title: *"Fast growth, and no alcohol"*.
     Body: *"With oxygen available, yeast respires aerobically instead — it gets far more energy per
     glucose, so it grows and divides quickly, and produces carbon dioxide and water rather than
     ethanol. This is exactly how yeast itself is manufactured, in open stirred tanks. It is also
     why a brewer seals the vessel: to force the organism down the route that makes the product."*
   - **Bacteria** — line `contaminated`.
     Title: *"Poor conditions for these bacteria"*.
     Body: *"Lactic acid bacteria of this kind do their work without oxygen, and an open stirred
     vessel also invites in every other organism in the room. Seal it if you want yoghurt rather
     than a science experiment."*
4. **`fermenting` — everything else.** Rate 12 if `temp == "cold"`, else 100. Four texts:
   - **Yeast, cold** — *"Slow fermentation — a sourdough in the fridge"* /
     *"At 4 °C the yeast is alive and unharmed, and everything is happening slowly — molecules
     collide less often. Bakers use this deliberately: an overnight cold rise gives more time for
     flavour to develop while the dough inflates gently."*
   - **Yeast, warm** — *"Beer, wine, or a rising loaf"* /
     *"Sealed, warm and fed. Ethanol and carbon dioxide are being produced steadily. A brewer lets
     the gas out through an airlock and keeps the liquid; a baker keeps the gas in the dough and
     lets the ethanol boil off in the oven. Same reaction, opposite product wanted."*
   - **Bacteria, cold** — *"Barely anything — this is why yoghurt lives in the fridge"* /
     *"The bacteria are alive and almost inactive. This is exactly why a finished yoghurt is
     refrigerated — not to stop the bacteria being there, but to slow them almost to a halt so it
     does not keep souring."*
   - **Bacteria, warm** — *"Yoghurt"* /
     *"Sealed and warm with sugar available. Lactic acid is accumulating, the pH is falling, and the
     milk protein is curdling into a thick set. Left too long it becomes unpleasantly sour, so the
     maker chills it to stop the reaction where they want it."*

⚖️ **The yeast open-and-stirred branch is NOT a failure state.** It is how yeast is manufactured,
the branch text says so in its own words, and it is the branch that teaches why a brewer seals the
vessel. Its rate is **100**, its tone is not amber, and no revision may turn it into an error
message. It is also NOTES flag 16, which asks Mide to confirm the claim — confirming or softening
the science does not make it a failure.

⛔ **`products` is authored per branch and is NEVER derived from `line`.** Design computes
`aerobic = out.line.indexOf('oxygen') >= 0` (page line 478) — a string sniff on the reaction text —
and it is wrong on one live branch: bacteria + open + warm + sugar has `line = "contaminated"`,
which contains no `"oxygen"`, so the sniff fails through to the bacteria branch and the bench prints
**"Lactic acid 100 units"** underneath the words *"Poor conditions for these bacteria"*. The panel
contradicts itself. Authoring `products` on each branch removes the sniff and the defect with it.
The three product shapes, for reference: yeast-fermenting → carbon dioxide + ethanol both at `rate`;
yeast-aerobic → carbon dioxide at `rate`, ethanol `none`; bacteria-fermenting → lactic acid at
`rate`, gas *"none — this route makes no gas"*. **Bacteria-open needs a shape Design never drew;
that is a finding for the report and Mide's to rule on, not something to invent quietly.**

⚑ The bench opens **already set as a brewery** (`start` == the brewery preset), so pressing
*Set it up as a brewery* first changes nothing visible while still counting toward `done_after`.
Measured, deliberate-looking, and harmless — recorded so a later pass does not "fix" it into a
different opening state, which would cost the brewery/yoghurt contrast its symmetry.

## 6. `route-decider` — b8-05 `#s-bench`

```python
{"kind": "route-decider", "id": "which-route-is-running",
 "anchor": "s-bench", "segment": "practical", "demand": "decide",
 "eyebrow": "At the bench · five situations",
 "heading": "Which route is running here?",
 "prompt":  "...",                                   # page line 113

 "cases_label":   "The situation",
 "options_label": "Which route is supplying the energy?",
 "routes": [{"id": "aerobic",   "text": "Almost entirely aerobic"},
            {"id": "both",      "text": "Aerobic, with anaerobic making up a shortfall"},
            {"id": "anaerobic", "text": "Entirely anaerobic — no oxygen is being used"}],
 "cases":  [{"id", "label", "text", "answer", "why"}],   # 5

 "progress": "{n} of {total} settled",
 "tally":    {"remaining": "{n} still to settle", "all": "all five settled"},
 "run_label": "Check it", "ran_label": "Settled",
 "verdicts":  {"right": "That is the one", "wrong": "Not this time"},
 "done_after": 5}
```

**State:** `case` (current tab), a pick per case, and an opened/settled flag per case.
**Controls:** five case tabs → set `case`; three route buttons → set the pick for the current case
(inert once that case is settled); **Check it** → settle the current case (disabled until a pick
exists, and once settled).
**Completion:** all five cases settled. Design's own threshold, kept.

⚖️ **The marathon case is the instrument.** Its answer is `aerobic`, and its `why` names the trap in
the page's own words: *"This is the answer people get wrong because the runner is working hard. Hard
is not the question — whether the oxygen supply keeps up is."* Two of the five (`marathon`,
`sprint`) separate *hard* from *is the supply keeping up*, and `yeast` is the only case on the bench
with no aerobic respiration in it at all. Do not reorder the tabs: `sitting` first is what makes the
marathon feel like a second easy one.

⚠️ **House rule, read precisely.** No green and no red reaches the option buttons — measured, the
only per-option treatment is an amber outline on the student's own pick and a fade to 50% opacity on
the two they did not choose. But the verdict panel **does** say whether they were right, in words:
`verdicts.right` = *"That is the one"*, `verdicts.wrong` = *"Not this time"*, above the answer stated
as a sentence and then the `why`. That is Design's drawing and it is inside the bench, not the
ladder. It is not a violation of §0.6 — nothing is scored, nothing is tallied as a mark, and the
student can settle all five whether right or wrong — but it is the closest B8 comes to the line, and
it is recorded here so the port does not drift either way: **do not add colour, and do not remove
the words.**

## 7. Rail stops — how many can actually tick

> ⊕ **REVERSED 18 Aug 2026 — MRB-249. SHIP FOUR STOPS. The band stop is a MIRROR.**
>
> This section's *measurement* is right and stands; its instruction is reversed. It told five
> B8 lessons to ship three stops, and nine lesson records cite it by name as the authority for
> having done so. Thirty-five pages across B3–B8 and C1 shipped a rail with a stop missing.
>
> **MRB-205 binds and is not re-argued: Design draws, we render; the page wins over the
> engine.** A band section holding a drawn equation and three fact cards is teaching, not a
> spacer, and dropping it from the rail is not rendering what Design drew. Design also states
> the completion condition herself, in a **rail-level** `isDone()`:
>
>     if (id === 's-bench')   return s.exits;
>     if (id === 's-summary') return s.exits;
>
> The band is the payoff of the instrument beside it; it carries no control because the
> instrument already took the commitment. It is authored as a mirror —
> `{"anchor": "s-summary", "mirrors": "s-bench", "done_when": "exits_shown"}` — and
> `shared/ks3.js` resolves it in `wireRail`'s `paint()`, at the level Design resolves it.
> `ks3_parity.check_rail_matches_design` now fails the build on a dropped stop.
>
> Read "the band stop" below as **the mirror stop**, and the bench predicate column as its
> `done_when`.


Design draws **four** stops on all five pages: `s-hook`, `s-bench`, the band section, `s-ladder`.
On Design's own page all four tick, because Design's `isDone()` aliases the band stop to the bench's
state (`s-summary` returns `s.exits`; `s-jobs` and `s-two` return the bench's seen-count; `s-equation`
returns `everRecovered`; `s-table` returns the opened-count).

**On the BUILT page that aliasing does not exist.** `doneByDom()` in `shared/ks3.js` reads only the
DOM inside the stop's own section, in this order: `data-stage-done` (authoritative in both
directions) → `.ks3-rung` all answered → `[data-reveal]:not([hidden])` or
`.ks3-reveal-btn[aria-expanded="true"]` → `.ks3-option[aria-pressed="true"]`. Checked stop by stop:

| Stop | Signal on the built page | Ticks? |
|---|---|---|
| `s-hook` | core `hook` emits `.ks3-option[aria-pressed]` + a gated reveal | **yes** |
| `s-bench` | the instrument emits `data-stage-done="0"` → `"1"` on its own contract (§2–§6) | **yes** |
| band section | `r_rule` / `r_comparison` emit a `<section class="ks3-rule">` — no rungs, no options, no reveal, no `data-stage-done` | **NO** |
| `s-ladder` | `.ks3-rung` × 4 | **yes** |

> **Three of Design's four rail stops can tick, on every one of the five pages.** The count is
> uniform across B8: 3, 3, 3, 3, 3.

**Ship three stops per lesson and drop the band stop, exactly as B7 did** (`ks3_data/b7/lesson_01…py`
line 455: *"THREE stops. Design draws four; `s-summary` is dropped"*). Dropping it is the honest
option and it is already precedent. The alternative — aliasing the band stop to the bench, as Design
does — would tick a stop for something the student did in a different section, which MRB-208's
completion rule exists to prevent.

The `done_when` strings, per contract R2, are read by nothing at runtime but are gated by
`verify_ks3.py` and must name a condition the page can reach:

| Lesson | `s-hook` | `s-bench` | `s-ladder` | Dropped |
|---|---|---|---|---|
| b8-01 | `committed` | `exits_shown` | `ladder_complete` | `s-summary` |
| b8-02 | `committed` | `three_cells_cut` | `ladder_complete` | `s-jobs` |
| b8-03 | `committed` | `debt_repaid` | `ladder_complete` | `s-equation` |
| b8-04 | `committed` | `two_setups_tried` | `ladder_complete` | `s-two` |
| b8-05 | `committed` | `five_cases_settled` | `ladder_complete` | `s-table` |

`short`/`label` are lifted from Design's own `RAIL_SHORT` / `RAIL` arrays and the dropped entry's
pair goes with it: b8-01 `SUMMARY`/*Word summary*, b8-02 `JOBS`/*Four jobs*, b8-03
`SUMMARY`/*Word summary*, b8-04 `ROUTES`/*Two routes*, b8-05 `TABLE`/*Side by side*.

## 8. `#s-think` — `confrontation` on all five pages

**Measured: static markup, no commitment, on all five.** Every page's `#s-think` is
`ks3-block ks3-misconception` and contains a quoted belief, a paragraph, a 2px `--ks3-alert-border`
rule, a second quoted belief and a second paragraph. There is no options list, no reveal, no button
and no state — the sections' only interactive elements are the cross-links inside the prose.

So under contract §2 R1 these author as **`confrontation`** (core `{"type": "misconception", …}`),
not `predict`. R1's `predict` branch applies where `#s-think` asks for a commitment and then
reveals; B8 does not. Consistent with B7, and with B1's original ruling. `#s-think` is not a rail
stop on any B8 page — Design's `RAIL` never lists it — so `confrontation` emitting no
`data-stage-done` costs nothing.

Available anchors for `elicited_by` / `confronted_by`, which the MRB-244 gate resolves against the
**built** page: `s-hook`, `s-bench`, `s-think`, `s-ladder`, `s-keynote` on all five, plus
`s-summary` (b8-01), `s-jobs` (b8-02), `s-equation` (b8-03), `s-two` (b8-04), `s-table` (b8-05).
The *Going further* layer and the endmatter carry no `id` and may not be named.

Misconception ids, pre-allocated, two per lesson, in NOTES §5's own order — b8-01 `RESP-01`/`RESP-02`,
b8-02 `RESP-03`/`RESP-04`, b8-03 `RESP-05`/`RESP-06`, b8-04 `RESP-07`/`RESP-08`, b8-05
`RESP-09`/`RESP-10`. Ids are permanent and are never re-pointed at a different belief.

## 9. The KEY FACT boxes, verbatim

One per lesson, nested inside the band section on the `card` ground (`box-shadow: 5px 5px 0
var(--ks3-accent)`, measured — the shipped stylesheet's value, so contract R3 does not arise in B8).
Never amber.

- **b8-01** `#s-summary` — "Aerobic respiration is glucose + oxygen giving carbon dioxide + water,
  releasing energy the cell can use. It happens in the mitochondria of every living cell,
  continuously, and it is a chemical reaction — not breathing, which is the muscular job that
  supplies it."
- **b8-02** `#s-jobs` — "Every living cell in every living organism respires continuously, because
  every other chemical process in a cell — movement, growth, repair, active transport and keeping
  warm — has to be paid for out of the energy respiration releases."
- **b8-03** `#s-equation` — "In humans, anaerobic respiration is glucose giving lactic acid, with no
  oxygen used and far less energy transferred. The lactic acid builds up, and the oxygen needed to
  deal with it afterwards is the oxygen debt — which is why you keep breathing hard after you stop."
- **b8-04** `#s-two` — "Fermentation is anaerobic respiration in micro-organisms. In yeast, glucose
  gives ethanol + carbon dioxide; in bacteria such as those in yoghurt, glucose gives lactic acid.
  What we call the food is the organism's waste."
- **b8-05** `#s-table` — "Aerobic respiration uses oxygen, breaks glucose down completely to carbon
  dioxide and water, and releases far more energy per molecule. Anaerobic respiration uses no
  oxygen, breaks glucose down only partly, releases much less energy per molecule — and can do it
  faster, and without waiting."

⚠️ **b8-05's key fact carries the "about twenty times" claim only by implication** ("far more energy
per molecule"). The number itself — *"about twenty times more energy"* — appears in the b8-05 hook
heading, in the `#s-think` first paragraph, in the `s-table` row *Energy per glucose*
("About twenty times more."), in rung 2's third distractor correction and its fourth
("The yields are about twentyfold apart"), in self-rung 3 criterion 4, in the *Going further*
closing sentence, and in the legal line that qualifies it. **Eight sites in one lesson.** It is NOTES
flag 19 (2 vs 38 ATP, so about nineteen, stated as "about twenty"), it is on Mide's gate, and if he
moves the figure it moves in eight places on this page — plus the b8-05 `marathon` case `why`, which
says "at twenty times the fuel cost". Nine.

## 10. `figures`

**`figures: []` on all five, and that is measured, not assumed.** `<img>`, `<figure>` and
`<picture>` each appear **zero times** across the five pages. The only SVG on any page is UI
furniture: the nav chevron, the rail tick, the drawn equation arrow (`viewBox="0 0 60 24"`, engine
geometry — b8-01 and b8-03 only), the endmatter link arrows and the ladder tick/cross marks. No page
leaves a placeholder, an empty frame or a caption with nothing under it.

**NOTES-B8 flag 21 is therefore accurate**: a mitochondrion and a labelled leaf-and-lung gas-flow
figure are the obvious candidates and neither is in `docs/ks3/diagram-manifest.md`. §4.10 allows an
empty `figures` for a lesson carried by its interactives. **Do not invent a figure slot to fill the
gap, and do not drop the flag** — it is Mide's to rule on.

## 11. Where Design's pages and NOTES-B8 disagree

Four, and only the last one blocks anything.

1. **Rail stops.** NOTES §4: *"Rail stops: four in all five lessons."* True of Design's page and
   false of ours — three can tick on the built page (§7). Not a defect in Design's delivery; a
   consequence of `doneByDom()` reading the DOM instead of a component's private state. Resolved
   the way B7 resolved it.
2. **`fermenter` outcome texts.** NOTES §2.4 says *"Each branch has its own outcome text"* and
   counts four branches. The page has **eight** distinct texts, because the fermenting branch splits
   by organism × temperature and the aerobic branch splits by organism (§5.1). The page is right and
   NOTES is counting the precedence tree, not the leaves.
3. **b8-04's `products` panel.** No disagreement with NOTES — NOTES does not mention it — but the
   page contradicts *itself* on the bacteria-open branch (§5, ⛔). Recorded here because the fix
   needs a product shape nobody drew.
4. **The `RESP` misconception register.** NOTES §5 states `RESP-01` to `RESP-10` are *"written into
   `docs/ks3/misconception-register.md` with a new prefix row"*. **They are not.** Grepped: the
   register contains fourteen prefixes — `ATOM BODY BREATH CELL DIET DRUG ECO GENE LIFE NOS PART
   PLANT REACT REPRO` — and no `RESP` row of any kind. The register is the source the MRB-244 gate
   and every `elicited_by` / `confronted_by` join resolve against, so **the `RESP` prefix row and its
   ten entries must be opened as the first act of the authoring pass**, before any lesson record
   names one. Authoring a lesson against ids that do not exist is how a red gate arrives at the end
   of a long build instead of the start of a short one.

Everything else NOTES-B8 asserts that this pass could check — five instruments, all DOM-only, no
timers, no canvas, no diagrams, slugs matching `structure.py` character for character
(`aerobic-respiration`, `why-every-cell-respires`, `anaerobic-respiration-in-humans`, `fermentation`,
`aerobic-vs-anaerobic`), and the tweak props `showDraft` ×5, `startAmount`, `startCell`, `startPace`
— is confirmed against the pages.
