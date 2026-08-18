# B11 — payload schema

Written **before** the authoring passes are dispatched, as B7's was, and for the same reason: B5
shipped without one and five records then spelled the same four labels nine different ways.

**If this document and Design's page disagree, the page wins on MEASUREMENT (what is drawn) and
this document wins on NAMING (what we call it).** Where the page needs something this schema has
not anticipated, follow the page and say so in the report.

Everything below is measured from the four approved `.dc.html` files in `docs/ks3/design-reference/b11/`, not
inferred from `NOTES-B11.md`. Where the notes and the delivered bytes disagree, §9 says so.

---

## 0. Rules that bind all four instruments

1. **All four are DOM-only.** `grep -icE "math\.random|<canvas|requestAnimationFrame|setTimeout|
   setInterval"` returns **0 on all four pages**. `support.js`'s only `canvas` hits are Claude
   Design's own preview-harness background (`CANVAS_BG_LIGHT`/`data-dc-canvas`), not a `<canvas>`
   element in a lesson. NOTES-B11 §3 is confirmed in the delivered bytes.
2. **⚑ NO RANDOMNESS ANYWHERE — and it is load-bearing, not incidental.** B11 teaches a process
   people wrongly imagine to be directed; a stochastic bench would let a student watch a run go
   "the wrong way" and conclude the model is broken, or watch a lucky run and conclude selection
   is a lottery. `selection-runner` is a closed-form recurrence (§3). Never introduce a jitter,
   a shuffle or a "more realistic" sampling step into any B11 instrument.
3. **All four flagships ship on `ks3-block ks3-dark ks3-practical`** — the class attribute measured
   verbatim off Design's markup at `#s-bench` on all four pages:
   ```html
   <section id="s-bench" class="ks3-block ks3-dark ks3-practical" style="scroll-margin-top: 92px;">
   ```
   That is `segment: "practical"`, the ink-dark ground, on all four. Do not guess the shell from
   the kind name; §4 of the build contract records that B1 got two of six wrong that way, and
   MRB-245 made a declared-vs-rendered disagreement a build failure.
4. ⛔ **NO RUNTIME STATE IS AUTHORED.** `env`, `seen`, `bark`, `pale`, `gen`, `history`, `species`,
   `pressure`, `field`, `released`, `tried` are all values the *runtime* owns. Under contract R5 a
   key with no read site is a dead key and fails `ks3_key_audit.py`. The renderer initialises its
   own state; §2–§5 record the opening values as **prose**, not as keys.
5. **Every authored key must have a read site in the same pass.** Wire the read or do not author
   the key.
6. **Every student-facing string is lifted byte-identical** from the approved page via
   `node tools/extract_design_payload.js <page>`. Never retype science-bearing copy — B11 carries
   twenty individually-written outcome texts (§4) and twenty-five per-mouse rationales (§2), and
   retyping any of them is a science edit made by accident.
7. **Nothing marks correctness except the ladder.** These are benches: they give a verdict in
   words. Amber is a wrong IDEA being confronted, never the student.

## 1. One spelling per concept, for the whole unit

Inherited from B7's table, unchanged, plus the four B11 additions below the rule.

| Concept | The key | Never |
|---|---|---|
| Lead line above a set of options | `options_label` | `options_lead`, `choose_prompt` |
| The button that runs/commits the bench | `run_label` | `commit_label`, `check_label` |
| The button that returns it to the start | `reset_label` | `clear_label`, `again_label` |
| Map of branch id → outcome | `verdicts` | `verdict`, `outcomes` |
| A single line of help under a control | `hint` | `hints`, `note` |
| The closing paragraph after the payoff | `close` | `closing`, `after` |
| — new in B11 — | | |
| Label above a row of selector tabs | `tabs_label` | `picker_label`, `switch_label`, `group_label` |
| The counter in the bench's top-right | `progress_suffix` | `count_label`, `tried_label` |
| Per-item explanatory line inside a bench | `why` | `reason`, `because`, `detail` |
| Map of state → the line under the readout | `notes` | `messages`, `commentary` |

Two benches carry a per-row map keyed by a second dimension (`chances`/`whys` in §2, `scores` in
§4). Those are **maps keyed by the other axis's id**, never parallel arrays — a parallel array
silently mis-pairs a mouse with another mouse's survival number if anyone reorders the list.

## 2. `advantage-bench` — b11-01 `#s-bench`

```python
{"kind": "advantage-bench", "id": "...", "segment": "practical",
 "eyebrow": "...", "title": "...", "intro": "...",     # "At the bench · one population, five conditions"
 "tabs_label": "...",                                   # "The conditions"
 "progress_suffix": "...",                              # " conditions tried" → "2 of 5 conditions tried"
 "best_suffix": "...", "worst_suffix": "...",           # " · best here" / " · worst here"
 "subjects": [{"id": str, "name": str}],                # the five mice, order fixed and shared by every env
 "envs": [{"id": str, "label": str,                     # `label` = tab text, `name` = panel headline
           "name": str, "note": str,
           "chances": {"<subject-id>": int},            # 0..100, ALL FIVE subjects required
           "whys":    {"<subject-id>": str},            # ALL FIVE required
           "verdict": str}]}
```

**State held:** current `env` id (opens on `winter`), and `seen` — a set of env ids seeded with the
opening one. **Controls:** five env tabs; each sets `env` and adds that id to `seen`. There is no
reset and no run button — the bench is a switcher, and switching *is* the experiment.
**Completion predicate (Design's):** `seen >= 3` of 5.

### The 5×5 survival matrix, measured

| | winter | drought | owl | crowded | disease |
|---|---|---|---|---|---|
| `big` Large, heavy build | 70 | 40 | 35 | **80 ▲** | 45 ▲* |
| `thick` Thick coat | **90 ▲** | **25 ▼** | 55 | 50 | 45 ▲* |
| `fast` Small and quick | **45 ▼** | **85 ▲** | **80 ▲** | 45 ▼ | 45 ▲* |
| `bold` Bold and exploratory | 55 | 60 | **20 ▼** | 75 | **30 ▼** |
| `pale` Pale sandy fur | 75 | 70 | 25 | 50 | 45 ▲* |

▲ = the renderer's `best here` (green), ▼ = `worst here` (amber). Computed live as `Math.max` /
`Math.min` over the column — **not authored**, which matters for the two findings below.

**The reversals NOTES-B11 §1.1 claims — verified against the numbers:**

- **Thick coat: EXACT.** 90, the column maximum in winter → 25, the column minimum in drought.
  Best on the bench to worst on the bench, same animal, nothing about it changed. This is the
  reversal rung 3 asks the student to explain, and it holds.
- **Small and quick: EXACT, and it is the same reversal read backwards.** 45, the winter minimum →
  85, the drought maximum. The drought verdict names both halves.
- **⚠️ Pale fur: DIRECTIONAL ONLY, NOT EXTREMAL.** NOTES-B11 §1.1 says "the pale mouse best in snow
  and worst against the owl". Measured: pale is **75 in winter — second of five, behind thick at
  90** — and **25 against the owl — second-worst of five, above bold at 20**. The page's own
  verdict copy is careful and correct ("Boldness and pale fur are the liabilities here — and pale
  fur was an advantage in the snow"); it is the NOTES sentence that overclaims. **Do not "fix" the
  numbers to match the notes.** Raising pale to the winter maximum would demote the thick coat and
  destroy the exact reversal rung 3 is built on. Author the matrix as measured.
- **⚠️ The crowded verdict is loose.** It reads "Note that the drought's loser is this
  environment's winner." The drought's *loser* is `thick` at 25; `big`, the crowded winner, scored
  40 in the drought — fourth of five, not last. Lift the sentence byte-identical (it is not
  false — big did badly in the drought) and flag it to Mide as copy, not as a number to change.

### ⚠️ The disease bench renders FOUR mice as "best here" simultaneously

`disease` is `{big: 45, thick: 45, fast: 45, bold: 30, pale: 45}`. The renderer's `best` is
`Math.max` = 45, and `isBest` is `c === best`, so **four of the five mice carry `45% survive ·
best here` in green at once**, while the verdict below says "None of the visible variations helps."

This is the pedagogically most important panel in b11-01 — it is what sets up rung 4 and hands off
to b11-04 — and Design's own renderer contradicts its own verdict on it. **The port must handle
the tie.** The correct treatment, and the one consistent with §0.7 and with the amber rule: when
the column has no unique maximum, mark **nothing** best and **nothing** worst — suppress both
suffixes and both colours, leave every bar in `--ks3-on-dark-muted`, and let the verdict do the
teaching. A panel that says "no variation helps" while painting four green winners teaches the
opposite of its own sentence.

⚑ The percentages are **invented teaching values** and the page's legal line says so. That line is
not optional decoration; it is lifted with the rest.

## 3. `selection-runner` — b11-02 `#s-bench`

```python
{"kind": "selection-runner", "id": "...", "segment": "practical",
 "eyebrow": "...", "title": "...", "intro": "...",
 "tabs_label": "...",                                   # "The tree bark"
 "gen_label": "...", "gen_zero_label": "...",           # "generation " / "generation 0"
 "barks": [{"id": str, "label": str, "note": str,
            "pale_surv": float, "dark_surv": float}],   # 0..1, the ONLY numbers in the model
 "start_pale": 0.9,                                     # the real historical starting point
 "reset_pale": 0.5,
 "history_len": 24,                                     # columns kept; oldest shifts off the left
 "pale_label": "...", "dark_label": "...",              # "Pale" / "Dark", used as "Pale 62%"
 "axis_note": "...",                                    # "pale on top, dark below · one column per generation · oldest on the left"
 "one_label": "...", "ten_label": "...", "reset_label": "...",
 "notes": {"start": str, "control": str, "dark_high": str,
           "pale_high": str, "moving": str}}
```

**State held:** `bark` (opens on `sooty`), `pale` (a float, opens at `start_pale`), `gen` (int),
`history` (a list of `{pale}`, opening `[{pale: start_pale}]`, capped at `history_len`).
**Controls:** three bark tabs (set `bark`; they do **not** reset the population, which is what lets
a student run it sooty then switch to clean and watch it come back); `One generation`;
`Ten generations`; `Start again at fifty-fifty`.
**Completion predicate (Design's):** `gen >= 10`.

### The recurrence — exact, deterministic, closed form

For each generation, with the current pale fraction `p` and the selected bark's two survival rates:

```
survivors_pale = p · pale_surv
survivors_dark = (1 − p) · dark_surv
p′             = survivors_pale / (survivors_pale + survivors_dark)
```

Population size is not modelled at all — only the fraction is carried, which is why the legal line
says the population is held constant. Equivalently, the **odds** `p/(1−p)` are multiplied by
`pale_surv / dark_surv` every generation, which is a fixed constant per bark. There is no sampling,
no drift, no mutation, no migration, and no `Math.random` on the page or in `support.js`.

| bark | `pale_surv` | `dark_surv` | odds multiplier per generation | behaviour |
|---|---|---|---|---|
| `clean` Clean, lichen-covered | 0.85 | 0.45 | ×1.889 pale | pale sweeps to fixation |
| `sooty` Blackened by soot | 0.45 | 0.85 | ×0.529 pale | dark sweeps; from 90% pale, ten generations reach ≈99% dark |
| `mixed` Patchy, partly recovered | 0.70 | 0.70 | ×1.000 — **identity** | ⚑ **THE CONTROL. Nothing moves, exactly, for ever.** |

**The `mixed` bark is not a third scenario, it is the control, and it must stay numerically
exact.** `0.7 == 0.7` makes `p′ === p` bit-for-bit, so the bars do not creep by a rounding pixel
over fifty generations. Any authoring pass that "varies it slightly for realism" destroys the one
panel that shows selection *not* happening — which is the panel that proves the other two are
showing selection rather than an animation.

### ⚠️ The gen-0 note is wrong after a reset

`notes.start` is shown when `gen === 0` and reads "Nine moths in ten are pale, which is where the
British population started." `onReset` sets `pale: 0.5, gen: 0` — so pressing **Start again at
fifty-fifty** displays a fifty-fifty population under a sentence that says nine in ten are pale.
Design's defect, in the delivered bytes. **The port fixes it**: gate `notes.start` on
`gen === 0 && pale === start_pale`, and author a fifth entry `notes.reset` for
`gen === 0 && pale === reset_pale`. Author both; wire both.

⚑ The eyebrow reads "a hundred moths on a tree trunk" and nothing in the model is a count of a
hundred individuals — it is a proportion throughout. Lift the eyebrow byte-identical and leave it;
"a hundred moths" is a reading aid, and the legal line already says the population is held
constant. Recorded so nobody later "adds" a population of 100 to make it literal.

## 4. `pressure-bench` — b11-03 `#s-bench`

```python
{"kind": "pressure-bench", "id": "...", "segment": "practical",
 "eyebrow": "...", "title": "...", "intro": "...",
 "species_label": "...", "pressure_label": "...",       # "The species" / "What happens"
 "progress_suffix": "...",                              # " combination(s) tried"
 "trait_labels": ["Diet", "Breeding rate", "Range", "Genetic variation"],
 "species":   [{"id": str, "name": str, "diet": str, "breeding": str,
                "range": str, "variation": str,
                "scores": {"<pressure-id>": int}}],     # 0..100, ALL FIVE pressures required
 "pressures": [{"id": str, "label": str, "name": str, "note": str}],
 "outcomes":  {"<species-id>": {"<pressure-id>": str}}, # 4 × 5 = TWENTY, all required
 "outcome_label": "...",                                # "Population after fifty years"
 "outcome_suffix": "...",                               # "% of the original population"
 "bands": {"ok": 65, "mid": 40}}                        # ≥65 green, 40–64 muted, <40 amber
```

**State held:** `species` (opens on `dormouse`), `pressure` (opens on `habitat`), `seen` — a set of
`"<species>-<pressure>"` keys seeded with the opening pair. **Controls:** four species tabs and
five pressure tabs; each sets its own axis and records the resulting *pair* in `seen`.
**Completion predicate (Design's):** `seen >= 4` combinations.

### The twenty texts — where each one lives

All twenty are individually written prose in the `OUTCOMES` object literal, b11-03 lines 344–373,
keyed `OUTCOMES[species_id][pressure_id]`. Nothing is generated, concatenated or templated. Lift
all twenty byte-identical; a paraphrase is a science edit.

| | habitat | climate | predator | disease | hunting |
|---|---|---|---|---|---|
| `rat` Brown rat | 85 | 80 | 70 | 65 | 75 |
| `dormouse` Hazel dormouse | **15** | 30 | 45 | 35 | **80** |
| `panda` Giant panda | **20** | 25 | **70** | 40 | 35 |
| `gull` Herring gull | 80 | 70 | 75 | 60 | 65 |

### ⚠️ The every-species-both-ways claim does NOT hold as stated

NOTES-B11 §1.3: "Every species is resilient to at least one pressure and vulnerable to at least
one, so no row reads as a simple ranking." Measured against the bands the page itself renders:

- `dormouse` — resilient (hunting 80, green) and vulnerable (habitat 15, climate 30, disease 35,
  all amber). **Claim holds.**
- `panda` — resilient (predator 70, green) and vulnerable (habitat 20, climate 25, hunting 35,
  amber). **Claim holds.**
- `rat` — **all five scores are 65 or above; every cell renders green.** No amber anywhere. The
  rat row *is* a simple ranking: it is good at everything.
- `gull` — **no cell falls below 60; nothing renders amber.** Its lowest (disease 60) is muted, not
  vulnerable.

So the claim holds for two species of four, and holds for the other two only in the weak sense of
"has a lowest score". This is fine as pedagogy — the rat and the gull are on the bench precisely
*because* generalists shrug off almost everything, and the dormouse/panda contrast is the lesson —
but **the NOTES sentence overstates it and rung 3 depends on the contrast, not on the symmetry.**
Author the scores exactly as measured. Report the discrepancy; it is Design's sentence to withdraw,
not our numbers to bend.

⚑ **`panda` × `predator` = 70 is deliberately a high score that explains nothing**, and its text
says so in terms: "This is the one pressure it handles well, and it explains nothing about why the
species is in trouble." That text is the reason the cell exists. If any pass ever "tidies" the
panda row to make it uniformly bleak, that pedagogy is lost.
⚑ `dormouse` × `hunting` = 80 does the same job in the opposite direction — "which is why the
population is still falling for the other four reasons."

## 5. `blight-bench` — b11-04 `#s-bench`

```python
{"kind": "blight-bench", "id": "...", "segment": "practical",
 "eyebrow": "...", "title": "...", "intro": "...",
 "tabs_label": "...",                                   # "What you planted"
 "progress_suffix": "...", "progress_zero": "...",      # " field(s) tested" / "no blight released yet"
 "total": 1000,
 "fields": [{"id": str, "label": str, "name": str, "note": str,
             "varieties": int,                          # 1 / 4 / 10 / 1000
             "resistant": int,                          # varieties that happen to resist THIS blight
             "variation_word": str,                     # "none" / "4 varieties" / "10 varieties" / "very high"
             "variation_bar": int,                      # 0..100, the drawn width
             "yield_word": str,                         # "highest" / "good" / "good" / "lowest"
             "yield_bar": int}],                        # 0..100, the drawn width
 "bar_labels": ["Plants surviving the blight",
                "Genetic variation in the field",
                "Yield per plant in a good year"],
 "run_label": "...", "ran_label": "...", "reset_label": "...",
 "verdicts": {"<field-id>": str}}                       # one per field — see the note below
```

**State held:** `field` (opens on `clone`), `released` (bool, opens false), `tried` — a set of
field ids, added to on release and **never cleared**. **Controls:** four field tabs (set `field`,
clear `released` — so switching fields re-arms the blight); `Release the blight` (sets `released`,
records `tried`, then disables itself and relabels to "Blight has passed through");
`Clear the field` (clears `released` only, keeps `tried`).
**Completion predicate (Design's):** `tried >= 2` fields.

### The exact computations

```
survivors = round(total × resistant / varieties)      # total = 1000, before release survivors = total
pct       = round(survivors / total × 100)
```

| field | `varieties` | `resistant` | survivors | pct | variation bar | yield bar |
|---|---|---|---|---|---|---|
| `clone` One variety | 1 | **0** | **0** | **0%** | 9 | **100** |
| `four` Four varieties | 4 | 1 | 250 | 25% | 36 | 85 |
| `ten` Ten varieties | 10 | 4 | 400 | 40% | 90 | 85 |
| `landrace` A mixed landrace | 1000 | 620 | 620 | **62%** | 100 | 55 |

**The clone field returns EXACTLY ZERO.** `resistant: 0` over `varieties: 1` is 0 by construction,
not by rounding — there is no arithmetic path to a single survivor. The survivor bar renders amber
at width 0 and the verdict names the Irish potato famine and the Gros Michel. This is the payoff of
the whole lesson and the number must stay integer-exact.

**The trade-off is the yield bar running the other way.** Variation 9 → 36 → 90 → 100 against yield
100 → 85 → 85 → 55. Monotone opposite at the two ends, with `four` and `ten` deliberately tied at
85 in the middle — the trade-off bites at the extremes, not smoothly across the range.

⚠️ **Design derives `variation_word`, `yield_word` and `yield_bar` from the field `id`** with a
chain of `f.id === 'clone' ? … : (f.id === 'landrace' ? … : …)`, so a fifth field would silently
fall into the `else` and be drawn as "good / 85". **We author all three per field instead**, which
is why they are keys above. Same drawn output for these four; portable for any fifth.

⚠️ **`verdicts` is keyed by field id, all four written out**, even though Design's code has three
branches (`clone`, `landrace`, and an `else` shared by `four` and `ten`). The shared branch
interpolates `pct`, so the two fields already print different sentences; keying by id makes that
explicit and removes the same silent-`else` trap. Author `four` and `ten` with the identical
template text — that is a deliberate duplication, not drift.

⚑ Landrace resistance 620/1000 = 62% is invented (NOTES flag 15), chosen so the landrace clearly
beats the ten-variety field without looking immune. The legal line covers it.

## 6. Everything else on the four pages — the full activity roster

Beyond the four flagships there are **no other stateful instruments**. Every remaining interactive
element is an existing generator block. Class attributes below are quoted verbatim from the pages.

| Anchor | Measured `class` | Block type / segment | Interactive? |
|---|---|---|---|
| `#s-hook` | `ks3-block ks3-dark ks3-hook` | `hook` (`r_hook`) | **Yes** — commit-then-reveal, four options, reveal gated behind a choice. All four pages. |
| `#s-bench` | `ks3-block ks3-dark ks3-practical` | activity, `segment: "practical"` | **Yes** — the flagship, §2–§5 |
| `#s-three` / `#s-steps` / `#s-risk` / `#s-banks` | *(no `ks3-block`)* — inline `background: var(--ks3-band); border: 3px solid var(--ks3-ink); border-radius: var(--ks3-r-block); padding: 34px 32px` | `rule` (`r_rule`), same shell B7 measured for `#s-features` | **No** — cards only |
| *(nested inside the above)* | inline `background: var(--ks3-card); border: 2px solid var(--ks3-ink); box-shadow: 5px 5px 0 var(--ks3-accent)` | `key-fact` (`r_key_fact`, accent offset shadow) | No |
| `#s-think` | `ks3-block ks3-misconception` | activity, `segment: "misconception"` | **No — static, see §7** |
| `#s-ladder` | `ks3-ladder` | `quiz` (`r_ladder`) | **Yes** — 2 marked + 2 self-marked rungs, 5 criteria each, "Retry my misses" |
| `#s-keynote` | `ks3-block ks3-dark ks3-keynote` | `summary` | No |
| *(unanchored)* | `ks3-layer` | *Going further* | No |

So the port registers **exactly four new entries in `ACTIVITY_KIND_RENDERERS`**:
`advantage-bench`, `selection-runner`, `pressure-bench`, `blight-bench` — all four
`segment: "practical"`, all four in a `_INSTRUMENT_SEGMENTS` map written in **one pass by the
commander**, per the warning in `ks3_data/b7/__init__.py`.

The hook payload is not a new kind: it is `phenomenon.commit` + `.options` + `.reveal`, already
read by `r_hook`. All four hooks are four-option single-choice with the reveal gated behind a
commitment (R16, Law 1).

## 7. `#s-think` is `confrontation`, not `predict`, on all four pages

Measured: every `#s-think` is a static `ks3-block ks3-misconception` carrying **two** misconception
quotes — a `ks3-mis-quote` + prose, then a second quote + prose behind
`border-top: 2px solid var(--ks3-alert-border)`. **No options, no buttons, no reveal, no
commitment anywhere in the block on any of the four pages.**

Under contract §2 R1 that makes all four `confrontation`, not `predict`. Do not author
`options`/`reveal` into a think-again block to "make it interactive" — the commitment for the
lesson already lives in the hook, and a second one here would double-count.

## 8. The rail — four stops drawn, and FOUR is what we build (MRB-249)

> ⊕ **RULED 18 Aug 2026 — MRB-249. AUTHOR FOUR STOPS. The band stop is a MIRROR.**
>
> This section's verdict is reversed; its *measurement* below is correct and still stands.
> Design draws four, and four is what we build.
>
> The reasoning that produced "author three" was that a static band carries none of the DOM
> signals `doneByDom()` reads, so a stop anchored to it can never tick. That was true of the
> runtime as it stood, and it is no longer true of the runtime — but more importantly it was
> never a reason to drop the stop. **MRB-205 binds and is not re-argued: Design draws, we
> render; the page wins over the engine.** Dropping a stop Design drew is not rendering what
> Design drew, and the band section is 1.2–5.2 KB of real teaching, not a spacer.
>
> Design also states the completion condition herself, in her own `isDone()`, which is a
> **rail-level** function rather than a per-section one:
>
>     if (id === 's-bench') return s.everTopped;
>     if (id === 's-roles') return s.everTopped;
>
> The band is the *payoff* of the instrument beside it. It carries no control because the
> instrument already took the student's commitment. So it is authored as a mirror:
>
>     {"anchor": "s-roles", "short": "ROLES", "label": "Producer, consumer, decomposer",
>      "mirrors": "s-bench", "done_when": "chain_topped"},
>
> `shared/ks3.js` resolves `mirrors` in `wireRail`'s `paint()` — at rail level, where Design
> resolves it. Nothing ticks on load; the mirrored stop ticks the moment its target does.
> `ks3_parity.check_rail_matches_design` now gates the built rail against
> `docs/ks3/rail-manifest.md`, which is generated from Design's delivered pages, so a dropped
> stop **fails the build**. Thirty-five pages had already shipped with one missing.
>
> The tables below record what Design drew. Read the "dropped" column as **"the mirror stop"**,
> and the "Design's bench threshold" column as the mirror's `done_when`.



This is B7's defect again, in a different shape, and it is present on every B11 page.

| Lesson | Stop 1 | Stop 2 | Stop 3 | Stop 4 |
|---|---|---|---|---|
| b11-01 | `s-hook` HOOK ✅ | `s-bench` BENCH ✅ | `s-three` COMPETE ❌ | `s-ladder` LADDER ✅ |
| b11-02 | `s-hook` HOOK ✅ | `s-bench` BENCH ✅ | `s-steps` STEPS ❌ | `s-ladder` LADDER ✅ |
| b11-03 | `s-hook` HOOK ✅ | `s-bench` BENCH ✅ | `s-risk` RISK ❌ | `s-ladder` LADDER ✅ |
| b11-04 | `s-hook` HOOK ✅ | `s-bench` BENCH ✅ | `s-banks` BANKS ❌ | `s-ladder` LADDER ✅ |

**Why stop 3 cannot tick.** Design's own `isDone` gives the third stop the *bench's* predicate
verbatim — `n >= 3` on b11-01, `gen >= 10` on b11-02, `n >= 4` on b11-03, `n >= 2` on b11-04 — so
in Design's preview it lights up the moment the bench does. Our rail does not work that way.
`doneByDom` in `shared/ks3.js` reads, in order: an explicit `data-stage-done`; then `.ks3-rung`
completion; then an opened `[data-reveal]`; then `.ks3-option[aria-pressed="true"]`. A `rule` panel
has **none of the four** — no declaration, no rungs, no reveal, no options. It returns `false` for
ever, and B1's four-of-six lesson could reach at most four stops for exactly this reason.

⊕ **RULED, and the call is made: OPTION 2, THE MIRROR.** MRB-249 settled it for the whole key
stage and B9 has already shipped it. Route 1 — a rail of three — is not available: MRB-205 binds,
Design draws and we render, and dropping a stop she drew is not rendering what she drew. The
"loses nothing" argument was wrong on its own terms as well; the panel is 1.2–5.2 KB of real
teaching, and it is where each lesson's KEY FACT lives.

`mirrors` is resolved in `wireRail`'s `paint()` at rail level, which is where Design resolves it in
her own `isDone()`. Nothing ticks on load; the mirrored stop ticks when its target does. So:

    {"anchor": "s-three", "short": "COMPETE", "label": "…",
     "mirrors": "s-bench", "done_when": "<the bench's own condition>"},

Per lesson: b11-01 `s-three` / three of five environments seen · b11-02 `s-steps` / ten
generations run · b11-03 `s-risk` / four species-pressure combinations seen · b11-04 `s-banks` /
two fields blighted. Those four are Design's own predicates, recorded in the paragraph above.

`ks3_parity.check_rail_matches_design` gates the built rail against
`docs/ks3/rail-manifest.md` — generated from Design's delivered pages — so a rail of three FAILS
THE BUILD naming the page. Also note `#s-think` and `#s-keynote` are on no rail on any page, which
is correct and matches B7.

**The four bench predicates, for whichever route is taken:** b11-01 three of five environments
seen; b11-02 ten generations run; b11-03 four species-pressure combinations seen; b11-04 two fields
blighted. Each instrument emits `data-stage-done` at `0` on load (MRB-208: nothing ticks on load).

## 9. KEY FACT copy — one per lesson, verbatim

Lifted byte-identical from the `key-fact` card nested in each `rule` panel.

**b11-01 (`#s-three`)** — "Individuals of a species vary, and resources are limited, so some
compete more successfully than others. Which variation gives an advantage depends entirely on the
conditions, and the conditions change — so there is no such thing as a generally superior
individual."

**b11-02 (`#s-steps`)** — "Natural selection: individuals vary; those whose variations suit the
conditions survive and reproduce more; they pass those variations to their offspring; over many
generations the population changes. Individuals do not change — populations do."

**b11-03 (`#s-risk`)** — "A species becomes extinct when the environment changes faster than it can
adapt, or in ways its existing variation cannot cope with. Specialists, slow breeders, species with
small ranges and populations with little genetic variation are the most vulnerable. Extinction is
permanent."

**b11-04 (`#s-banks`)** — "Biodiversity is the variety of living things — between species, and
between individuals within a species. It matters because variation is what allows populations to
survive change. Gene banks store seeds, sperm, eggs and tissue so that variation is not lost for
ever if a population is."

## 10. The peppered moth ruling — VERIFIED IN THE DELIVERED BYTES ✅

NOTES-B11 flag 5 records the ruling of 16 Aug: the conclusion is sound, so teach it plainly with no
hedge, and move the method criticism into *Going further*. Checked against b11-02 as delivered.

**(a) Is there any hedge left in the lesson BODY? — NO. Clean.** Every moth-bearing sentence
outside *Going further* states the science flatly:
- bench intro — "Pale and dark moths resting on tree bark, hunted by birds that find whatever they
  can see."
- `sooty` bark note — "…as it did across industrial Britain in the nineteenth century."
- step card 1 — "In the moths, pale and dark forms both existed long before the factories were
  built — dark ones were simply rare."
- think-again — "The moths on the bench above were not turned dark by soot; some were already dark
  and the soot changed which ones got eaten."
- rung 1, rung 3 and all five rung-3 criteria treat the darkening as settled fact.
No "some scientists", no "it is thought", no "the classic story", no "has been questioned"
anywhere in the body. **The hedge is gone.**

**(b) Does the legal line now cover only the bench model? — YES.** Verbatim: *"The moth bench is a
teaching model: survival differences are fixed percentages, the population size is held constant,
and there is no mutation, migration or chance beyond the survival rates themselves."* That is a
statement about the simulation only. The caveat sentence about the science has been cut, as the
ruling required.

**(c) Does *Going further* carry the method story, and does it run to two paragraphs? — YES to
both, CONFIRMED.** `.ks3-layer-body` on b11-02 contains exactly two `<p>` elements:
1. Kettlewell's 1950s release-recapture in Birmingham and Dorset; the fair criticisms (released by
   day, unnatural densities, exposed trunks when the moths rest higher up beneath branches); the
   period when the conclusion was wrongly reported as having fallen with the method; Majerus
   re-running it in the 2000s in natural resting positions at natural densities with birds watched
   taking them, same result more strongly, published 2012 after his death; closing on "A conclusion
   is only ever as good as the method behind it… standing on firmer ground than before."
2. Antibiotic resistance, ending on "finishing a course **as prescribed**" — the wording NOTES
   flag 6 deliberately chose.

⚑ **DESIGN FLAG FOR MIDE — b11-02 is the only lesson in the biology build with a two-paragraph
*Going further*.** Measured: `.ks3-layer-body` holds one `<p>` on b11-01 (the Grants' finches),
b11-03 (kakapo) and b11-04 (Svalbard), and **two** on b11-02. Design offers to move or cut the
antibiotic-resistance paragraph. **Mide's call, and it is a real one** — the moth-method paragraph
is the strongest *how do we know?* story in the build and the antibiotic paragraph is the strongest
*why does this matter today* one, and dropping either loses something. Recorded, not resolved. The
port authors whatever Mide rules; if no ruling arrives, author both paragraphs as delivered.

## 11. Where Design's page and NOTES-B11 disagree

Five, all recorded above, none blocking:

1. **§2 — pale fur's reversal is directional, not extremal.** NOTES §1.1 says best-in-snow /
   worst-against-the-owl; measured, pale is second and second-worst. The page's own copy is
   accurate; the notes overclaim.
2. **§4 — "every species vulnerable to at least one" fails for the brown rat and the herring
   gull.** Neither has a single cell in the amber band. NOTES §1.3 overstates the symmetry.
3. **§3 — the reset leaves a fifty-fifty population under a "nine moths in ten are pale"
   sentence.** A defect in the delivered bytes, not mentioned in NOTES. The port fixes it with a
   fifth `notes.reset` entry.
4. **§2 — the disease bench paints four simultaneous green "best here" winners** under a verdict
   that says none of the variations helps. Not mentioned in NOTES. The port suppresses best/worst
   marking when the column has no unique extreme.
5. **§12 — `EVOL-01` … `EVOL-08` are NOT in the register.** NOTES §4 states they were "written
   into `docs/ks3/misconception-register.md` with a new prefix row". Measured:
   `grep -n "EVOL" docs/ks3/misconception-register.md` returns **nothing**, and there is no `EVOL`
   prefix row. The register work is outstanding; §12 pre-allocates it here so the ids are fixed
   before any authoring pass improvises one.

Two further cross-cutting observations, neither a disagreement:

- **`--ks3-alert` (amber) is used as a data colour throughout B11's benches** — the worst-here bar
  in §2, the dark-moth stack and the "Dark n%" readout in §3, the sub-40 band in §4, and the
  zero-survivors *and* yield bars in §5. Brand rule reserves amber for a wrong idea being
  confronted. The bench verdicts never mark the student, so this does not breach §0.7, but it is
  the same ink doing two jobs on one page. Flagged for the design pass; not a payload key.
- **`showDraft` is the only tweak prop on all four pages** (`data-props` measured identical across
  the four). NOTES §3 names a starting environment (b11-01) and a starting bark (b11-02) as the
  natural second tweaks; neither exists in the delivered bytes.

## 12. Misconception ids — pre-allocated, do not improvise

`EVOL` is a **new prefix** and needs a row in the register's prefix table alongside `PLANT`
(opened 17 Aug 2026 by B7).

| Lesson | Entries | Spare |
|---|---|---|
| b11-01 | `EVOL-01`, `EVOL-02` | `EVOL-09` |
| b11-02 | `EVOL-03`, `EVOL-04` | `EVOL-10` |
| b11-03 | `EVOL-05`, `EVOL-06` | `EVOL-11` |
| b11-04 | `EVOL-07`, `EVOL-08` | `EVOL-12` |

Two per lesson, matching the two quotes measured in each `#s-think` (§7). NOTES §4 asks for
`EVOL-01` and `EVOL-06` to carry a second lesson in `reappears_in` — `natural-selection` and
`disturbing-a-food-web` respectively.

An unclaimed spare stays **permanently unused**, like `DRUG-07` and `REPRO-17`/`20`/`21`/`23`.
Never re-point one at a different belief — ids are permanent.

⊕ 18 Aug 2026 — this table is the RANGE, fixed before any author starts, and B11 already had it
right where B10 did not. Four authors work four files at once and cannot see each other, so an
author who finds a third belief takes that lesson's spare and no one else's. An author who needs a
SECOND spare stops and reports rather than reaching past the table: two lessons minting from the
same next-free number is a collision that permanent ids cannot undo.

⚠️ `EVOL` still has no prefix row in `docs/ks3/misconception-register.md` (§11 item 5). The row is
the engine pass's to add, in the same commit as the instruments, so that the first authoring pass
to reference `EVOL-01` resolves against a register that knows the prefix.

`confronted_by` and `elicited_by` **must name an element on that lesson's own page** — an activity
`id` or a block `anchor` the page actually emits. This is gated (MRB-244) and resolves against the
BUILT page, so a name that renders to nothing fails the build. B11's available section anchors are
`s-hook`, `s-bench`, `s-think`, `s-ladder`, `s-keynote` on all four, plus `s-three` (b11-01),
`s-steps` (b11-02), `s-risk` (b11-03), `s-banks` (b11-04).

## 13. `figures`

**`figures: []` on all four, and that is deliberate, not an omission.** Measured, not assumed:
`grep -icE "<img|<figure|<picture|background-image"` returns **0 on all four pages**. Each page
carries exactly ten `<svg>` elements and every one is UI furniture — the nav chevron, the rail
tick, the ladder's tick and cross marks, the endmatter arrows. Not one is a diagram.

NOTES flag 16 names **a peppered moth pair on two barks** as the obvious candidate and records that
it is not in the diagram manifest. §4.10 allows an empty `figures` for a lesson carried by its
interactives — and b11-02 is carried by `selection-runner`, which shows the same idea moving.
**Do not invent a figure slot to fill the gap, and do not drop the flag** — it is Mide's to rule
on, alongside NOTES §5.2's build-wide observation that the entire biology build has no diagrams
and the manifest has no biology entries at all.

---

## 14. Science rulings — every NOTES-B11 flag, answered ⊕

`docs/ks3/design-reference/b11/README.txt` names three flags to answer first. All sixteen are ruled
here, 18 Aug 2026, under this run's standing authority over KS3 science. **No lesson waits on any of
them and no author re-opens one.** Two require a change to the delivered copy; the rest ship as
drawn.

### Flag 11 — "two thirds of modern medicines". CHANGE IT. This is the real correction in B11.

Design asked to *"soften or attach a figure you are happy to defend"*, and the honest answer is that
there is no fraction here worth defending to a thirteen-year-old. The number moves enormously with
the counting rule: whether a semi-synthetic derivative counts, whether "inspired by a natural
scaffold" counts, which drug classes are in scope, and which window of approvals is measured.
Surveys of newly approved small-molecule drugs land nearer a third to a half depending on all four;
two thirds sits at the top of the range and usually comes from counting anything with a
natural-product ancestor anywhere in its history.

**So do not soften the fraction — remove it, and replace it with kind rather than proportion.** Say
that a great many of our medicines began as compounds found in living things, and then name
examples: aspirin from willow bark, penicillin from a mould, and one plant-derived anticancer drug.

Two reasons this is the better lesson and not merely the safer one. Named examples are far more
memorable at this age than any fraction, and a student who remembers three drugs has the point. And
a fraction can become wrong — this one already is, depending on who counts — where "aspirin came
from willow bark" cannot.

⚠️ This edits authored prose in a `#s-think` body, which is permitted: MRB-177's rule that you never
edit a correction applies to LADDER options, and this is not one. Lift the rest of the block
byte-identical, change only the sentence carrying the fraction, and report the before and after.

### Flag 13 — the Irish potato famine, one clause. KEEP IT TO ONE CLAUSE, and check what the clause SAYS.

One clause is right. The science this lesson owns is that a crop grown from genetically near-
identical plants has no variation to fall back on, so one pathogen can take all of it — and the 1840s
blight is the clearest case there is. The political history is history's to teach and this lesson
should not attempt it.

**But the b11-04 author must check the exact wording, because the risk here is not what the clause
says, it is what a single clause implies.** The blight destroyed the potato crop. What followed —
roughly a million deaths and a million more emigrating — followed from far more than a fungus, and a
clause that reads as *"the blight caused the famine"* teaches a false causal story by omission and
would be fairly criticised for it.

The test: the clause must be about the CROP FAILING, not about the famine's death toll or its causes.
If the delivered wording already does that, ship it untouched. If it attributes the famine itself to
the blight, adjust it to the crop and report the change. Do not expand it to cover the politics —
that is the other failure mode, and it is a science lesson.

### Flag 5 — the two-paragraph *Going further* on b11-02. KEEP BOTH PARAGRAPHS.

Design offers to move or cut the antibiotic-resistance paragraph because the layer now runs to two
where no other lesson's does. Keep both. *Going further* is a layer the STUDENT chose; a student who
opened it is not harmed by a second paragraph, and length uniformity across lessons is a habit, not
a rule. The two do different jobs and neither substitutes for the other: the moth-method story is a
*how do we know?* about the organism the lesson just taught, and antibiotic resistance is natural
selection happening now, in the only context where a student may one day act on it. Moving
antibiotic resistance elsewhere would strand it on a page whose bench is not about selection.

Recorded as a deliberate departure from the build's habit, not an oversight.

### Flag 16 — diagrams. ANSWERED, and the moth pair IS DRAWN.

This flag records that B11 has no diagrams and that a peppered moth pair on two barks is the obvious
candidate. Mide ruled on 18 Aug 2026 that code draws the diagrams itself, inline, and the mechanism
shipped the same day (`SVG_ART` in `build_ks3.py`, `status: "drawn"`, first used for the oak wood web
on b9-01 and b9-03).

**Draw it.** Camouflage is the one idea in this unit that is genuinely and irreducibly visual — the
whole claim is about whether a bird can pick a moth out against a background, and no sentence does
what two panels do. `selection-runner` shows the proportion changing over generations, which is the
consequence; it does not show the thing the consequence follows from.

It is a COMPONENT: it registers in §10.2 of the coverage manifest and carries parity rows, or the
gate cannot see it. Never colour-alone — the two barks must differ by pattern as well as tone, and
each moth must be labelled.

### Flags 1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15 — checked, correct, ship as drawn.

Checked individually, not as a block. The b11-01 survival percentages are illustrative and the legal
line says so, which is the same treatment B9 and B10 use and is acceptable. "Fittest" as best-fitted
*plus* reproductive success is correct and is the definition worth having — the mayfly comparison
earns its place. The Grants' finches are right: Daphne Major, the 1977 drought, a measurable increase
in beak depth within one generation, and the reversal after the 1983 rains; "evolution watched rather
than reconstructed" is a fair framing. Lamarck treated with respect is both better history and better
teaching — a serious theory, right that species change, wrong on mechanism — and Design is right that
the respect makes the correction land harder. "As prescribed" is deliberately the antibiotic wording
that survives the current argument about finishing the course; keep it exactly. Over 99% of species
extinct, five mass extinctions, end-Permian ~90% of marine species, end-Cretaceous 66 Mya are all
standard. The conservative "tens to hundreds of times background" is the right choice where published
estimates run much higher. The four b11-03 species are accurately described, and the dormouse detail
is doing most of the teaching work, correctly. Kakapo: flightless, freeze response, breeding tied to
mast years, low point of 51 — right. Gros Michel and Cavendish, and TR4 moving through Cavendish
plantations — right and current. Svalbard's figures are right, and "well over a million" is the
correct hedge for a holding that grows. The invented 62% landrace resistance is labelled illustrative
and is chosen well: it beats the ten-variety field clearly without reading as immunity.

---

## 15. Two design questions this run does NOT settle — they are Mide's ⊕

Both surfaced from measurement during the B11 engine pass, both are brand or palette decisions rather
than science, and both are pinned in parity rows so the gate names them the day either moves. Recorded
so the next pass does not rediscover them and does not quietly "fix" them either.

### Amber is doing four jobs across B11's benches, and one of them is a species

`--ks3-alert` is ruled as *a wrong IDEA being confronted, never the student*. Nothing here breaches
that — every bench gives its verdict in words, no option button takes a verdict class, and every
amber carries a word as well as the colour, so the never-colour-alone rule holds. **Ships as drawn.**

But measured across the unit it now carries, simultaneously:

| where | what amber means there |
|---|---|
| b11-01 | the worst-here figure and bar (paired with `--ks3-ok` for best-here) |
| b11-02 | **the dark moth stack** and its live figure — amber as a *species*, which is as far from "a wrong idea" as the token gets |
| b11-03 | the sub-40 band on the outcome figure and bar |
| b11-04 | the zero-survivor bar **and, separately, the yield bar** — "nothing came through" and "the cost of variation", two rows apart on one panel |

It is also the chosen-tab ground on all four benches (Design's own `seg()`), so on b11-04 one colour
says *this is the field you are looking at*, *nothing survived* and *this is what you gave up* at the
same time. That is not a rule breach; it is a palette carrying more meaning than one colour can hold,
and whether it matters is a design judgement. **Mide's.**

### `--ks3-ok` at 16px on `--ks3-dark-panel` measures 3.49:1

Below the 4.5:1 that small text needs. It is b11-01's best-here figure and b11-04's survivor value,
and `erun-bar-fixed` already carries the same flag from an earlier unit — so this is the second
sighting, not the first.

**Not repaired here, and the reason is that the obvious repair is a design decision.** `--ks3-ok-text`
is specified at 5.9:1 *on tint*, not on an ink-dark ground; there is no defined on-dark green in the
token set. Inventing one is minting a brand token, which is Mide's call and not a science correction —
and the alternative, dropping the green, would remove the pairing that makes best-here and worst-here
readable as a pair.

Two flags on the same pair from two independent passes is the argument for putting it in front of him.
