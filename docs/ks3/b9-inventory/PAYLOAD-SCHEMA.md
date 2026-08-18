# B9 — payload schema

Written **before** the authoring passes are dispatched, which is the whole point of it. Same
instrument as `docs/ks3/b7-inventory/PAYLOAD-SCHEMA.md`, applied to a six-lesson unit with six
flagship instruments — the largest single-unit instrument count in the biology build.

B5 shipped without a schema. Seven records then authored their payloads against Design's pages
rather than against an agreed schema, and five of them named the same four labels **nine different
ways**. That is the cost of deciding a key name eight times instead of once.

**If this document and Design's page disagree, the page wins on MEASUREMENT (what is drawn) and
this document wins on NAMING (what we call it).** Where the page needs something this schema has
not anticipated, follow the page and say so in the report.

Every line below is measured from the six delivered `.dc.html` files in `KS3 B9 lessons/`, dated
16 Aug, and from `KS3 B9 lessons/support.js`. Nothing is inferred from `NOTES-B9.md`; where NOTES
and the page disagree, §10 records it.

---

## 0. Rules that bind all six instruments

1. **All six are DOM-only.** Measured: `canvas` appears **zero** times, `requestAnimationFrame`
   zero, `setTimeout`/`setInterval` zero, across all six pages. NOTES-B9 §3 says the same. An
   instrument that wants one is a finding, not a licence.
2. **All six ship on `ks3-block ks3-dark ks3-practical`** — measured from Design's own markup on
   all six pages (b9-01 L105, b9-02 L105, b9-03 L104, b9-04 L105, b9-05 L105, b9-06 L104). That is
   `segment: "practical"`, the ink-dark ground. Do not guess the shell from the kind name; §4 of
   the build contract is explicit that B1 got two of six wrong.
3. ⛔ **NO RUNTIME STATE IS AUTHORED.** Design's own state bags hold `shown`, `everTopped`,
   `picked`, `year`, `culled`, `level`, `truthShown`, `active`, `field`. Those are values the
   *runtime* owns, not content. Under contract R5 a key with no read site is a dead key and fails
   `ks3_key_audit.py`. B5 and B7 both authored none. The renderer initialises its own state.
   ⚠️ `culled` in b9-02 is dead in **Design's own code**: `onCull` sets it, `onReset` clears it,
   and `renderVals()` never reads it. Do not carry the key across.
4. **Every authored key must have a read site in the same pass.** Wire the read or do not author
   the key. "It documents intent" is a comment, not a read site.
5. **Every student-facing string is lifted byte-identical** from the approved page via
   `node tools/extract_design_payload.js <page>`. Never retype science-bearing copy.
6. **Nothing marks correctness except the ladder.** These are benches: they show a consequence,
   they do not award a tick. Amber is a wrong IDEA being confronted, never the student.
7. **B9 OWNS the trophic 10:1 for the whole key stage.** B7 flag 19 raised the figure and did not
   own it; b9-01 states it, computes with it, legals it, and b9-05 runs the same arithmetic in the
   opposite direction. Any later lesson that needs the ratio cites b9-01; it is not restated as a
   new teaching claim anywhere else.

## 1. One spelling per concept, for the whole unit

Carried forward from B7 §1 unchanged, plus four B9 additions. Never invent a synonym.

| Concept | The key | Never |
|---|---|---|
| Lead line above a set of options | `options_label` | `options_lead`, `choose_prompt` |
| The button that runs/commits the bench | `run_label` | `commit_label`, `check_label` |
| The button that returns it to the start | `reset_label` | `clear_label`, `again_label` |
| Map of branch id → outcome | `verdicts` | `verdict`, `outcomes` |
| A single line of help under a control | `hint` | `hints`, `note` |
| The closing paragraph after the payoff | `close` | `closing`, `after` |
| The mono line beside the bench heading, two-or-more states | `progress` | `counter`, `status`, `stage_label` |
| The button that advances one step up a chain/round | `step_label` | `next_label`, `up_label` |
| Its spent state, shown when there is nothing above | `step_spent_label` | `done_label`, `top_label` |
| A row of segmented tab buttons that select a scenario | `tabs` | `chains`, `cases`, `switches` |
| One line of prose under the tab row, per selection | `tab_note` | `chem_note`, `why`, `blurb` |

## 2. The shell, measured, on all six pages

Identical on all six. Quoted class attributes are the bytes on the page, not a description.

| Anchor | Design's class attribute | Our `type` / `segment` |
|---|---|---|
| `s-hook` | `class="ks3-block ks3-dark ks3-hook"` | `hook` (phenomenon) |
| `s-bench` | `class="ks3-block ks3-dark ks3-practical"` | the flagship · `segment: "practical"` |
| band section † | *no class at all* — `<section id="…" style="background: var(--ks3-band); border: 3px solid var(--ks3-ink); border-radius: var(--ks3-r-block); padding: 34px 32px;">` | `rule` — band ground, KEY FACT nested with `ground: "card"` |
| `s-think` | `class="ks3-block ks3-misconception"` | `confrontation` — see §3 |
| `s-ladder` | `class="ks3-ladder"` | `quiz` |
| `s-keynote` | `class="ks3-block ks3-dark ks3-keynote"` | `summary` |

† The band anchor differs per lesson: `s-roles` (b9-01), `s-cycle` (b9-02), `s-rules` (b9-03),
`s-who` (b9-04), `s-two` (b9-05), `s-rules` (b9-06). It is the **`rule`** type, exactly as B7
authored `s-summary` / `s-features` — same arrangement, same reason: the section is band, and band
on band is invisible, so the KEY FACT nests as `ground: "card"`.

There is also a `<section class="ks3-layer">` *Going further* on every page (no `id`), and a
`<p class="ks3-legal">` on every page. Both are authored as they were in B7 — `explainer` and the
lesson's `legal` line. Every one of the six legal lines is load-bearing and none is decoration.

## 3. `#s-think` is a `confrontation` on all six — measured, not assumed

Contract §2 R1 makes `#s-think` a `predict` **only where it asks for a commitment and then
reveals**. On all six B9 pages `#s-think` is static markup: `ks3-mis-head`, a `ks3-mis-quote`, a
body paragraph, a `border-top` rule, a second `ks3-mis-quote` and a second body. **No `ks3-options`
list, no `sc-if` reveal, no button, no state.** So all six are `confrontation`, which emits no
`data-stage-done`, and none of them is a rail stop on Design's own page either. Same rule as B1,
meeting the same block.

Two quotes per lesson, twelve in the unit, which is the unit's twelve misconceptions (§8).

## 4. Rail stops — Design draws four, only THREE can tick

Design's `RAIL` is four stops on all six pages. The third is always the band section, and the band
section is **static markup with no control of its own**. Design fakes its completion by pointing
`isDone()` at the bench's state, e.g. b9-01 L400 `if (id === 's-roles') return s.everTopped;`. Our
runtime cannot do that: `doneByDom()` reads DOM signals from the block the stop is anchored to, and
a static band carries none. Exactly the B7 finding, six pages further on.

**Author THREE stops per lesson. Drop the band stop.** Design's own `RAIL`/`RAIL_SHORT` strings are
the `label`/`short` values; keep them byte-identical.

| Lesson | Stop 1 | Stop 2 (bench) | *dropped* | Stop 3 (ladder) | Design's bench threshold, kept |
|---|---|---|---|---|---|
| b9-01 | `s-hook` HOOK "Why chains stop" | `s-bench` BENCH "Climb the chain" | `s-roles` ROLES | `s-ladder` LADDER | `s.everTopped` — reached the top of a chain once |
| b9-02 | `s-hook` HOOK "Still rabbits" | `s-bench` BENCH "Run the years" | `s-cycle` CYCLE | `s-ladder` LADDER | `s.year >= 10` |
| b9-03 | `s-hook` HOOK "The ladybirds" | `s-bench` BENCH "Take one out" | `s-rules` RULES | `s-ladder` LADDER | `s.everDone` — followed one removal to round 3 |
| b9-04 | `s-hook` HOOK "The poster" | `s-bench` SHELF "The shelves" | `s-who` WHO | `s-ladder` LADDER | `s.level !== 'all'` — pollinators removed or halved |
| b9-05 | `s-hook` HOOK "Safe in water" | `s-bench` BENCH "Climb the chain" | `s-two` TWO | `s-ladder` LADDER | `s.everTopped` |
| b9-06 | `s-hook` HOOK "How many daisies" | `s-bench` BENCH "Survey it" | `s-rules` RULES | `s-ladder` LADDER | `s.truthShown` — sampled AND revealed the truth |

`done_when` values, matching the thresholds above: `committed`, then
`chain_topped` / `ten_years_run` / `removal_followed` / `pollinators_removed` /
`chain_topped` / `truth_revealed`, then `ladder_complete`. Contract R2: `done_when` is read by the
gate (`verify_ks3.py`), not the runtime, and must name a condition the page can actually reach.

## 5. `chain-ledger` — b9-01 `#s-bench`

```python
{"kind": "chain-ledger", "id": "...", "segment": "practical",
 "eyebrow": "...", "heading": "...", "prompt": "...",
 "progress": {"before": "level {n} of {total}", "after": "top of the chain"},
 "tabs_label": "The chain",                       # mono label above the tab row
 "start_kj": 10000,
 "factor": 10,                                    # energy falls x1/10 per step
 "chains": [{"id", "label",
             "levels": [{"name", "role", "note"}]}],   # field 4, wood 4, sea 5
 "step_label": "Who eats them?", "step_spent_label": "Nothing above this",
 "reset_label": "Back to the producers",
 "verdict": {"lead": "Ten thousand kilojoules entered at the bottom and ",
             "mid":  " arrived here — ", "tail": "% of it. Add one more level …"}}
```

**The verdict line is COMPUTED, not authored per chain** — that is the whole design, and it is why
adding a fourth chain needs no new prose. The exact computation, from page L453 and L515–517:

```
topKJ = 10000 / 10**(total - 1)
pct   = (100 / 10**(total - 1)).toFixed(2) with /\.?0+$/ stripped
verdict = "Ten thousand kilojoules entered at the bottom and " + topKJ.toLocaleString()
        + " arrived here — " + pct + "% of it. Add one more level and there would be a "
        + "tenth of that again, which is not enough to build an animal out of. That is the "
        + "whole reason chains stop."
```
Four-level chains (field, wood) render **"10 arrived here — 0.1% of it"**; the five-level sea chain
renders **"1 arrived here — 0.01% of it"**. Reproduce the rounding exactly: `toFixed(2)` then strip
trailing zeros, so `0.10 → 0.1` and `0.01` survives untouched.

Per row (page L492–504): `energy = 10000/10**i` formatted `toLocaleString() + ' kJ'` when ≥ 1
(row 5 of the sea chain is `1 kJ`); `pct = (100/10**i) + '% of the original'`; bar width
`max(0.6, 100/10**i)` per cent so the top bar stays visible. The list is
`flex-direction: column-reverse` — the producer is drawn at the BOTTOM. That is not styling, it is
the claim the lesson makes about which way energy travels, and the port must keep it.

**State:** selected chain; how many levels revealed (`shown`, starts at 1); a sticky
`everTopped`. **Controls:** three chain tabs (each resets `shown` to 1), one step-up button
(disabled at the top), one reset. The verdict appears only when `shown >= total`.

⚑ Design ships a `startChain` prop (enum `field`/`wood`/`sea`, default `field`). It is an author's
preview dial, not content. Do not author it unless the renderer reads it.

## 6. `cycle-runner` — b9-02 `#s-bench`

```python
{"kind": "cycle-runner", "id": "...", "segment": "practical",
 "eyebrow": "...", "heading": "...", "prompt": "...",
 "progress": {"prefix": "year "},                 # mono line: "year 0", "year 26"…
 "model": {"r": 0.6, "k": 2000, "a": 0.0015, "b": 0.35, "m": 0.35,
           "start_prey": 800, "start_pred": 120, "history": 26,
           "prey_cap_mult": 1.1, "pred_floor": 1},
 "series": {"prey": {"name": "Rabbits", "colour_token": "--ks3-alert"},
            "pred": {"name": "Foxes",   "colour_token": "--ks3-ok"}},
 "chart_caption": "amber = rabbits · green = foxes · each pair is one year, "
                  "oldest on the left · the two are scaled separately",
 "year_label": "One year", "ten_label": "Ten years",
 "cull_label": "Remove every fox", "restore_label": "Let foxes back in",
 "reset_label": "Reset the field",
 "notes": [{"id", "when", "text"}]}                # six branches, ordered — see below
```

**The exact recurrence** (page L401–415), applied `n` times per press:

```
nextPrey = prey + R*prey*(1 - prey/K) - A*prey*pred
nextPred = pred + B*A*prey*pred - M*pred
prey = clamp(0, K*1.1, nextPrey)          # ceiling 2200
pred = clamp(0, K,     nextPred)          # ceiling 2000
if pred < 1: pred = 0                     # extinction floor, not a rounding artefact
history.push({prey, pred}); trim to the last 26
```

⚖️ **K = 2000 is load-bearing and is not a tuning constant.** It is the grass supply. It is the
only reason *Remove every fox* teaches a carrying-capacity result — the rabbits climb, then stop,
crowded and hungry — instead of drawing an exponential curve that would teach the misconception
`#s-think` exists to break. Design says so in a comment on the page (L304–306). **A revision that
drops K, raises it out of reach, or replaces the logistic term with plain growth destroys the
lesson.** The prey ceiling `K*1.1` and the `pred < 1` floor are the two clamps that stop the
discrete model exploding or oscillating negative; both are required.

The chart is 26 paired bars, `max(2, v/max*100)` per cent tall. **The two series are scaled
independently** — `maxPrey = max(600, …)`, `maxPred = max(150, …)` — which is why the caption says
so in words. Merging them onto one scale would flatten the fox series into nothing and the lag,
which is the entire lesson, would become unreadable. Do not "fix" it.

*Remove every fox* toggles `pred` between `0` and `120`, pushes ONE history point and advances the
year by one. It is not a reset.

**Six note branches, in Design's evaluation order** — order is the payload's meaning, first match
wins: `year == 0` · `pred == 0 and prey > K*0.9` (the ceiling) · `pred == 0` (still climbing) ·
`prey > 1200 and pred < 200` · `prey < 500` · else. The second must be tested before the third or
the ceiling note never fires.

## 7. `remove-a-species` — b9-03 `#s-bench`

```python
{"kind": "remove-a-species", "id": "...", "segment": "practical",
 "eyebrow": "...", "heading": "...",
 "progress": {"none": "nothing removed yet", "mid": "round {n} of {total}",
              "all": "all three rounds"},
 "web_label": "Who eats whom",
 "web_lines": [...],                        # 8 lines, prose, NOT a graph structure
 "tabs_label": "Remove",
 "species": [{"id", "label", "why",
              "rounds": [{"title", "body"}],       # EXACTLY three
              "verdict": "..."}],                  # 6 species
 "step_first_label": "Remove it", "step_label": "And then?",
 "step_spent_label": "Followed to the end",
 "reset_label": "Put it back"}
```

Six removals × three rounds = **18 consequence texts**, plus six verdicts. Their locations in the
delivered page, so the lift can be checked line by line:

| Species | `why` | rounds 1–3 | verdict |
|---|---|---|---|
| `ladybirds` | L334 | L336, L337, L338 | L340 |
| `bluetits` | L342 | L344, L345, L346 | L348 |
| `owls` | L350 | L352, L353, L354 | L356 |
| `caterpillars` | L358 | L360, L361, L362 | L365 |
| `bees` | L367 | L369, L370, L371 | L373 |
| `oak` | L375 | L377, L378, L379 | L381 |

⚠️ **`caterpillars` carries a FOURTH round object at L363, `{ title: '', body: '' }`.** Design
filters it out at render (`sp.rounds.filter(r => r.title)`), so it is invisible on the page and the
counter still reads "of 3". It is an editing artefact. **Do not carry it across** — an empty round
would be a dead payload entry under rule 4, and our renderer has no filter to hide it.

⚖️ **The bees are in the web with NO feeding line, deliberately.** `web_lines` gives them
*"Bees pollinate the wildflowers"* — a service, not a meal — and nothing in the web eats them.
Removing them still empties the web three rounds later, and the verdict says so: *"The bees are in
no food chain here and their removal still empties the web. Feeding is not the only kind of
dependence."* This is the setup for b9-04 and the page names it. **A revision that "tidies" the web
by giving the bees a feeding line, or drops them because they have none, destroys the unit's
strongest link.**

⚖️ **`oak` is the one removal where the web does NOT reorganise.** Every other verdict describes a
redistribution; the oak's says *"Removing the producer removes the energy itself, which is the one
loss a web cannot absorb."* It is the contrast case and the reason six removals exist rather than
five. (NOTES flag 7 asks Mide to confirm it is worth including; it is his call, not the port's.)

`web_lines` is **prose, not a graph.** No adjacency structure is authored and none is drawn — see
§9 and NOTES flag 17.

## 8. `supermarket-shelf` — b9-04 `#s-bench`

```python
{"kind": "supermarket-shelf", "id": "...", "segment": "practical",
 "eyebrow": "...", "heading": "...", "prompt": "...",
 "progress": {"all": "shelf intact", "half": "half the pollinators",
              "none": "no pollinators"},
 "foods": [{"name", "dep", "cal", "vit", "how"}],   # 12; dep 0..1
 "bars": [{"id": "cal",  "label": "Calories still available", "colour_token": "--ks3-ok"},
          {"id": "vit",  "label": "Vitamins and minerals",    "colour_token": "--ks3-alert"}],
 "remove_label": "Remove every insect pollinator",
 "restore_label": "Bring the pollinators back",
 "half_label": "Lose half of them",
 "notes": {"all": "...", "none": "...", "half": "..."}}
```

The twelve foods exactly as delivered (page L316–329). `dep` = fraction of the crop lost with no
insect pollinators; `cal`/`vit` = this food's share of the shelf's calories and of its vitamins.

| name | dep | cal | vit | how |
|---|---|---|---|---|
| Bread (wheat) | 0 | 22 | 4 | wind-pollinated |
| Rice | 0 | 20 | 3 | wind-pollinated |
| Sweetcorn (maize) | 0 | 14 | 4 | wind-pollinated |
| Potatoes | 0 | 12 | 8 | grown from tubers |
| Milk | 0.15 | 8 | 9 | cattle feed partly insect-pollinated |
| Apples | 0.9 | 4 | 10 | insect-pollinated |
| Strawberries | 0.9 | 2 | 11 | insect-pollinated |
| Tomatoes | 0.7 | 3 | 12 | bumblebee-pollinated |
| Almonds | 1 | 6 | 9 | entirely insect-pollinated |
| Broccoli | 0.8 | 2 | 12 | insect-pollinated |
| Coffee | 0.5 | 1 | 3 | partly insect-pollinated |
| Chocolate (cocoa) | 1 | 6 | 15 | pollinated by midges |

Model (page L419–439): `loss = 0 | 0.5 | 1`; `remaining = 1 - dep*loss`;
`calPct = round(Σ cal*remaining / Σ cal * 100)`, `vitPct` likewise. Tile status:
`remaining < 0.2 → "gone"` (struck through, amber border, 0.6 opacity);
`< 0.85 → "{round(remaining*100)}% of the crop"`; else `"unaffected"`. At `loss == 0` the tile
shows the food's `how` string instead of a status — the dial doubles as the teaching label.

⚖️ **THE GAP BETWEEN THE TWO BARS IS THE ENTIRE LESSON.** Two bars, two colours, two labels, two
percentages, side by side and never combined. The `none` note reads the gap aloud:
*"Calories down to {calPct}%, vitamins and minerals down to {vitPct}%. Nobody starves on what is
left, and nobody stays healthy on it either. That gap between the two bars is the honest version of
the argument for pollinators."* **A revision that merges them into one "food" bar, or renders them
stacked, or drops one for space at a narrow breakpoint, deletes the lesson.** The grid is
`repeat(auto-fit, minmax(220px, 1fr))`, so they wrap to two rows rather than merging — keep that.

Three-state control drawn as **two** buttons: *Remove every insect pollinator* toggles
`none ↔ all`; *Lose half of them* sets `half` unconditionally. There is no path from `half` back to
`all` except by reloading, which is Design's, and is left alone.

## 9. `bioaccumulation` — b9-05 `#s-bench`

```python
{"kind": "bioaccumulation", "id": "...", "segment": "practical",
 "eyebrow": "...", "heading": "...", "prompt": "...",
 "progress": {"before": "level {n} of {total}", "after": "top of the chain"},
 "tabs_label": "The chemical",
 "chemicals": [{"id", "label", "factor", "start", "tab_note"}],   # 3
 "levels": [{"name", "eats"}],                                    # 6 rows
 "harm": 1.0,
 "harm_verdict": "above the level that causes harm",
 "safe_verdict": "no measurable effect",
 "step_label": "Who eats them?", "step_spent_label": "Top of the chain",
 "reset_label": "Back to the water",
 "verdicts": {"flat": "...", "harmful": "...", "below": "..."}}
```

Three persistence settings (page L321–328), all starting at **0.003 ppm**:

| id | label | factor |
|---|---|---|
| `persistent` | Persistent, fat-soluble | **×10** |
| `partial` | Slowly broken down | **×3** |
| `soluble` | Water-soluble, excreted | **×1** |

Six rows (page L330–337): Lake water *the source* · Algae *absorbs from the water* · Water fleas
*eat thousands of algae* · Minnows *eat hundreds of water fleas* · Perch *eat dozens of minnows* ·
Ospreys *eat hundreds of perch a year*. Drawn `column-reverse`, water at the bottom, same as b9-01.

`conc(i) = start * factor**i`. Formatting (`fmt`, page L449) is four-branch and must be reproduced:
`≥10 → 0 dp` · `≥1 → 1 dp` · `≥0.01 → 3 dp` · else `4 dp`.

⚖️ **The ×1 setting is the CONTROL and it produces a flat line.** Its verdict is the only one that
does not compute a number: *"Flat all the way up. The chemical is excreted as fast as it arrives,
so no organism holds more than any other and nothing is at risk. The concentration in the water was
the whole story — which is exactly why the persistent case caught everyone out."* It is what proves
the mechanism is **persistence, not toxicity** — the claim rung 1 marks and `#s-think` confronts.
**A revision that removes it as "the boring one" removes the control from a lesson about controls.**
The dial is a persistence dial, never a toxicity dial; nothing on the bench varies how poisonous
the chemical is.

⚠️ **THE BENCH AND THE PROSE DISAGREE ON THE TOP FIGURE. This is a finding, not a schema choice.**
Measured, `persistent` runs `0.0030 → 0.030 → 0.300 → 3.0 → 30 → **300 ppm**`, and the harmful
verdict computes `Math.round(300/0.003) = 100,000` times. But:
- the hook (L84) says the lake is at **0.0003 ppm** and the birds at **25 ppm**;
- rung 3 (L368) says **0.003 ppm** in the lake, **25 ppm** in the ospreys, *"roughly ten thousand
  times"*;
- NOTES-B9 §1.5 and flag 13 both say **five levels, 0.003 to 25 ppm**.

Three different water figures and two different top figures, in one lesson. A five-row chain
(water + four organisms) at ×10 would land on 30 ppm and ≈10,000×, which is what the hook, the rung
and NOTES all describe — the delivered bench has **six** rows. A second consequence of six rows: at
`harm = 1 ppm`, the **minnows** are already flagged *"above the level that causes harm"* at 3.0 ppm,
which sits against the key fact's *"the animals at the top are harmed first"*. **Do not silently
pick one. Author the port against Design's delivered bench, register the mismatch as a finding, and
send it to Mide with flag 13** — the numbers are a science-accuracy question and that is his gate.

## 10. `quadrat-bench` — b9-06 `#s-bench`

```python
{"kind": "quadrat-bench", "id": "...", "segment": "practical",
 "eyebrow": "...", "heading": "...", "prompt": "...",
 "progress": {"before": "field unsurveyed", "after": "{n} quadrats counted"},
 "side": 10,
 "field": {"centre_row": 7, "centre_col": 2, "reach": 11,
           "base": 2, "peak": 26, "noise": 6, "shade_max": 34},
 "methods_label": "Where you put the quadrats",
 "methods": [{"id": "random", "label": "Random coordinates"},
             {"id": "corner", "label": "The flowery corner"},
             {"id": "path",   "label": "Along the path edge"}],
 "counts_label": "How many",
 "counts": [3, 8, 25],                              # default 8
 "figures": [{"id": "mean",     "label": "Mean per quadrat"},
             {"id": "estimate", "label": "Estimated total"},
             {"id": "real",     "label": "Real total", "hidden_value": "hidden"}],
 "sample_label": "Take the sample", "resample_label": "Survey again",
 "truth_label": "Show the real total",
 "captions": {"unsampled": "one hundred square metres, contents hidden",
              "sampled":   "outlined squares are the ones you counted",
              "revealed":  "every square revealed — the daisies were never spread evenly"},
 "verdicts": {"corner": "...", "path": "...", "chance": "...", "good": "..."}}
```

**How the field is generated** (page L332–342), once, in the initial state:

```
for r in 0..9, for c in 0..9:
    richness = max(0, 1 - (|c-2| + |r-7|)/11)     # Manhattan falloff from (row 7, col 2)
    base     = 2 + richness**2 * 26               # squared → a tight cluster, not a gradient
    cell     = max(0, round(base + (random() - 0.5) * 6))
```

⚠️ **It is NOT seeded and NOT deterministic.** `Math.random()` is called 100 times per page load
(the only two `Math.random()` calls in the whole unit are here — b9-02 contains none). The field is
therefore **regenerated on every reload**, so two students never see the same field and no student
sees the same one twice. Design's legal line states this as intended:
*"The field is generated once when the page loads, with the daisies clustered towards one corner as
they usually are in real ground."* NOTES-B9 §3 nonetheless asks Mide to confirm it is wanted rather
than a fixed seed. **Carry the behaviour across as delivered and carry the question with it** — a
seed would make the verdict percentages reproducible for a teacher demonstrating at the front, and
that is a product decision, not a port decision.

Sampling pools (page L451–460), and this is where the pedagogy lives:

| method | pool | size |
|---|---|---|
| `random` | every square | 100 |
| `corner` | `r >= 5 and c <= 4` — the bottom-left quadrant, i.e. the cluster | 25 |
| `path` | `r <= 2` — the top three rows, farthest from the cluster | 30 |

Drawn **without replacement** (`splice`), `n = min(count, len(pool))`.
`mean = Σ field[i] / n`; `estimate = round(mean * 100)`; `errPct = round((estimate - total)/total * 100)`.

⚖️ **Increasing the sample size fixes the random case and does NOTHING for the two biased ones.
That separation is the whole point of the instrument.** It falls out of the pools: 3 → 8 → 25
random squares converge on the true mean, while 25 corner squares are drawn from a 25-cell pool
that is entirely inside the cluster — so the largest sample on the biased setting is the *most*
stably wrong, and is in fact **deterministic**, because it exhausts its pool. The verdicts say it in
words: corner — *"Take twenty-five instead of three and the answer does not improve — it just stops
wobbling. That is what bias means, and it is the one error more work cannot fix."*; path — *"Bias
has no favourite direction; it simply follows wherever you chose to look."* **A revision that
"balances" the pools, or lets sample size shrink the bias, deletes `NOS-04`'s confrontation.**

Four verdict branches, in Design's order, first match wins: `corner` · `path` · `random and n <= 3`
(chance, not bias) · else (`good`). The third must be tested after the two biased ones.

Two-stage completion: *Take the sample* then *Show the real total*, the second disabled until the
first has run, and re-sampling clears the reveal. The rail ticks on the reveal, not the sample —
Design's threshold, kept.

## 11. Every non-flagship activity, per page

Identical roster on all six lessons. Nothing else is drawn.

| `type` | anchor | segment / shell | notes |
|---|---|---|---|
| `hook` (`phenomenon`) | `s-hook` | `ks3-block ks3-dark ks3-hook` | Four options, a wager, **never marked** — no `answer` key. Reveal is gated on `hookChoice !== null`. One per lesson, six in the unit. |
| *flagship* | `s-bench` | `practical` | §§5–10 |
| `rule` | band † | band ground, no class | 3–4 cards (`kind`/`name`/`body`), a display statement, and on b9-01 an extra closing paragraph. KEY FACT nested, `ground: "card"`. |
| `key-fact` | inside `rule` | `card` | §12 — verbatim |
| `confrontation` | `s-think` | `ks3-block ks3-misconception` | Two quotes + two bodies, static. §3. |
| `quiz` (`ladder`) | `s-ladder` | `ks3-ladder` | Two marked rungs (4 options, one `correct`, three `correction` strings) + two self-marked rungs (5 criteria each). Score line *"You got {n} of 4."*, note *"You marked rungs 3 and 4 yourself."*, retry note *"Clears the ticks on rungs 3 and 4 and keeps what you wrote."* |
| `summary` (`key_note`) | `s-keynote` | `ks3-block ks3-dark ks3-keynote` | One paragraph. |
| `explainer` | *(no id)* | `ks3-layer` | *Going further*. One paragraph on all six. §13. |

† `s-roles` / `s-cycle` / `s-rules` / `s-who` / `s-two` / `s-rules`.

⚠️ Inline `<a href>` runs inside `confrontation` and `hook` bodies: `rich()` allows `<em>` and
`<strong>` and nothing else, so the WORDS are unchanged and the hyperlinks are dropped; every
destination survives as a `references` edge. Affected: b9-01 `#s-think` → `p1-03`; b9-02 `#s-think`
→ `b9-03`; b9-03 `#s-think` → `b11-03`; b9-04 hook reveal → `b3-04` (with an inline amber colour
that also goes), `#s-think` → `b3-04`.

## 12. KEY FACT box copy — verbatim, one per lesson

Lifted byte-identical. Never retyped.

**b9-01** (`#s-roles`, page L175)
> The arrows in a food chain show the direction energy travels, so they point from the organism being eaten to the organism eating it. Only about a tenth of the energy at each level reaches the next, which is why chains are short and top predators are rare.

**b9-02** (`#s-cycle`, page L158)
> Predator and prey numbers rise and fall in a repeating cycle, and the predator peak always comes after the prey peak. Each population limits the other, so neither wipes the other out and neither grows without limit.

**b9-03** (`#s-rules`, page L174)
> Removing one species changes the numbers of species it never touched, because every organism in a web is connected to every other through some route. A web with many alternative routes absorbs the change; a web with few does not.

**b9-04** (`#s-who`, page L167)
> Insect pollination is a service one group of organisms provides to another, and human food supply depends on it. Wind-pollinated cereals supply most of our calories; insect-pollinated crops supply most of the variety, the vitamins and the minerals.

**b9-05** (`#s-two`, page L174)
> A toxic substance that cannot be broken down or excreted accumulates in each organism and becomes more concentrated at every step up a food chain, because each predator eats many of the organisms below it. The animals at the top are harmed first, at concentrations that are harmless lower down.

**b9-06** (`#s-rules`, page L181)
> Estimate a population by counting in randomly placed quadrats and scaling up: mean per quadrat, multiplied by the number of quadrat-sized areas in the whole site. Random placement removes bias; more quadrats reduces the effect of chance. They are different problems and need different fixes.

Contract R3: the shipped `shared/ks3.css` KEY FACT treatment wins over any per-page numeric drift.
The ruled identity — band ground, 2px ink outline, hard **accent** offset shadow, mono label,
display statement, never amber — is what all six pages draw, and the shipped CSS satisfies it.

## 13. The two canonical-story rulings — VERIFIED PRESENT IN THE DELIVERED BYTES

Both landed. Quoted from the delivered files, not from NOTES.

**Flag 6 — b9-02 *Going further*, lynx–hare (page L257).** The ruling required: teach the LINKED
CYCLE, do NOT say lynx numbers control hare numbers, keep the trapping-returns-not-a-census point as
evidence handling. All three are on the page:
> …when ecologists later plotted those ledgers they found two wavy lines rising and falling on a cycle of roughly ten years, with the lynx peak trailing the hare peak. A linked cycle in two species, recovered from a company's account books: that is what the data show, and it is the thing worth learning from them. **What they do not show is one animal governing the other.** Hare numbers rise and fall for reasons that reach well past lynx — the shoots and twigs they feed on are stripped after a peak and take years to grow back, and hares living under heavy pressure raise fewer young. **Lynx move within that cycle as much as they drive it.** The record itself also needs reading with care: those ledgers count pelts brought in by trappers, not hares alive in the forest, so the price of fur and the number of people out trapping are in the line too. A ten-year rhythm that survives all of that is a real rhythm. **It is still not a census.**

**Flag 8 — b9-03 *Going further*, Yellowstone (page L273).** The ruling required: teach that removing
a top predator reaches far past its direct prey on the elk-and-willow link, and **"the wolves
changed the rivers" must be GONE.** Measured: the strings `river`, `rivers`, `changed the rivers`
and `meander` appear **zero times** in the delivered file. The paragraph runs the ruled chain:
> Elk numbers fell. Elk behaviour changed too — they stopped feeding for long spells in the open valley bottoms where they were easiest to ambush. Willow and aspen, the plants elk browse hardest, began growing back along those streams. Beavers need willow, and beavers returned to the stretches where it recovered; their dams then changed what could live in the water. Follow the links: a wolf never touches a willow, and never touches a beaver. It is joined to the willow through the elk and to the beaver through the willow, and that is enough. This is the difference between a chain and a web.

The caveat that used to correct the overclaim is gone with it, as ruled. ⚠️ NOTES flag 8 predicted
this "removes the unit's only outbound link to `b6-03`" — **it did not.** `b6-03` survives as an
endmatter *Connects to* link on b9-03 (L289) and as a *Before this lesson* link on b9-06 (L289).
The edge is intact; the note is stale.

## 14. Misconception ids — pre-allocated, do not improvise

⛔ **`ECO-12` MUST NOT BE MINTED.** `docs/ks3/misconception-register.md` permanently reserves it:
*"`ECO-12` — is `NOS-04`."* NOTES-B9 §4 says the family opens *"`ECO-01` to `ECO-12`, two per
lesson"* — that instruction is **superseded by the register** and must not be followed. b9-06's
second entry is `NOS-04` (*A large sample is an accurate sample*), which the register has already
allocated to this exact lesson.

| Lesson | Entries | The two beliefs `#s-think` confronts |
|---|---|---|
| b9-01 | `ECO-01`, `ECO-02` | arrows point at what the animal eats · ninety per cent of the energy is *lost* |
| b9-02 | `ECO-03`, `ECO-04` | the two peaks coincide · remove the predators and the prey do brilliantly |
| b9-03 | `ECO-05`, `ECO-06` | a removal only affects what is directly above and below · you can just put it back |
| b9-04 | `ECO-07`, `ECO-08` | no bees, no food, we would starve · "save the bees" means keeping a hive |
| b9-05 | `ECO-09`, `ECO-10` | the poison gets stronger going up · safe in the water means safe ecosystem |
| b9-06 | `ECO-11`, **`NOS-04`** | throwing the quadrat makes it random · twenty quadrats means an accurate answer |

The `ECO` family is **not yet open** in the register — no `ECO-*` row exists. The B9 authoring pass
mints `ECO-01`…`ECO-11` with a new prefix row, and skips `ECO-12` for ever. The standing rule holds:
nothing is registered ahead of the lesson that needs it.

⚠️ NOTES-B9 cites two ids that do not survive this allocation: §1.2 says the fox-removal button
teaches `ECO-06` (it is `ECO-04` here) and §1.6 says the sample-size separation is the point of
`ECO-12` (it is `NOS-04`). Re-point both when the register row is written.

`confronted_by` and `elicited_by` **must name an element on that lesson's own page** — an activity
`id` or a block `anchor` the page actually emits. This is gated (MRB-244) and resolves against the
BUILT page, so a name that renders to nothing fails the build. B9's available section anchors are
`s-hook`, `s-bench`, `s-think`, `s-ladder`, `s-keynote` on all six, plus the band anchor: `s-roles`
(b9-01), `s-cycle` (b9-02), `s-rules` (b9-03), `s-who` (b9-04), `s-two` (b9-05), `s-rules` (b9-06).

## 15. `figures`

**`figures: []` on all six, and that is deliberate, not an omission.** Measured, not assumed: no
page contains an `<img>` or a `<figure>`. Every `<svg>` on every page is either the nav chevron or a
`ks3-mark` tick/cross/arrow icon — 9 or 10 per page, all of them chrome.

NOTES-B9 flag 17 says a drawn food web is *"the obvious candidate"*, that it is **not in the diagram
manifest**, and that it *"would improve b9-01 and b9-03 more than any other illustration in the
biology build"*. **Verified against the pages, and the flag understates it slightly:** b9-03's web
is delivered as eight lines of who-eats-whom prose (`WEB_LINES`, page L321–330) with no adjacency
structure of any kind, and b9-01's chain is a vertical `column-reverse` list of energy rows — the
nearest thing to a diagram in the unit, and it is a bar chart of one number.

§4.10 allows an empty `figures` for a lesson carried by its interactives. **Do not invent a figure
slot to fill the gap, and do not drop the flag** — it is Mide's to rule on, and it is now the
strongest outstanding diagram request in the biology build.

## 16. Where Design's page and NOTES-B9 disagree

Recorded so the authoring passes do not re-discover them one at a time.

1. **The b9-05 top concentration.** NOTES §1.5 and flag 13 say five levels, 0.003 → 25 ppm. The
   delivered bench has six rows and reaches **300 ppm** at ×10. The lesson's own hook says the water
   is **0.0003 ppm**; rung 3 says 0.003 ppm and 25 ppm. See §9 — this goes to Mide with flag 13.
2. **`ECO-12`.** NOTES §4 opens the family with twelve `ECO` ids. The register forbids `ECO-12`
   permanently. See §14.
3. **`ECO-06`.** NOTES §1.2 points the b9-02 carrying-capacity result at `ECO-06`; sequential
   two-per-lesson allocation makes it `ECO-04`. See §14.
4. **The `b6-03` link.** NOTES flag 8 says dropping the river claim *"removes the unit's only
   outbound link to `b6-03`"*. It does not — the link survives twice. See §13.
5. **`Math.random()` in b9-02.** NOTES §3 says b9-02 and b9-06 *"are the only lessons in the whole
   biology build that use `Math.random()`"* and then says b9-02 does not. Measured: b9-02 contains
   zero calls. The sentence contradicts itself; only b9-06 uses it, 100 times, on load.
6. **b9-03's stray fourth round.** Not in NOTES at all. See §7.
