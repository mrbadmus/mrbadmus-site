# B4 — Breathing and gas exchange · instrument payload schema

**What this is.** The contract between the five lesson authors and the B4 engine pass (MRB-244).
One section per instrument kind. Every key below is a key the renderer in `build_ks3.py` actually
reads; keys marked **required** raise a `ValueError` at build time when missing, and the build is
red. Nothing here is aspirational — if the renderer stops reading a key, this file changes with it.

**Source of truth for the copy.** `docs/ks3/design-reference/b4/b4-0N-*.dc.html`, Design's approved delivery.
Every string quoted below is lifted from those files verbatim. **Never retype a science-bearing
string** — `node tools/extract_design_payload.js <page> [CONST...]` extracts the constants, and the
static markup prose is in the page body. Where this file quotes a value it is because that value is
the one Design drew, not because the key has a default.

**Where the instrument lives.** All five B4 instruments sit on a `practical` segment
(`<section class="ks3-block ks3-dark ks3-practical">`) — measured on all five pages, no exceptions.
That means **every one of them is on ink**, and the stylesheet scopes its colour rules `.ks3-dark …`
accordingly. Nothing in this file changes on a light ground because nothing in B4 is on one.

---

## 0 · Keys the SHELL reads, not the instrument

These sit on the same activity record, beside `kind`, and are read by `r_activity` before your
renderer runs. They are listed here because the authors have to supply them and they are easy to
miss; they are not part of any instrument's own payload.

| Key | Type | Req | Drives |
|---|---|---|---|
| `kind` | str | **yes** | the dispatch key — one of the five names in §1–§5 |
| `eyebrow` | str | no | the block's eyebrow. All five B4 blocks author one (e.g. `At the bench · two bags of air`); without it the shell prints its fixed `Investigate` |
| `heading` | str | no | the block `<h2>` (e.g. `Predict the numbers, then see them`) |
| `prompt` | str | no | the lede paragraph under the head row |
| `head_counter` | dict | no | the right-aligned mono progress readout on the head row. Two shapes: `{"format": …, "total": N}` for a count, `{"off": …, "on": …}` for a two-state label. **Every B4 block authors one** — the exact value per lesson is given in each section below |

`ground` is **not** authored on any B4 instrument block: the `practical` shell is already ink.

---

## 1 · `gas-compare` — b4-01 `#s-air`

Four gases, a prediction on each, then a locked reveal that prints both bags side by side.

**Shell keys for this block**

```python
eyebrow      = "At the bench · two bags of air"
heading      = "Predict the numbers, then see them"
prompt       = "For each gas, say what happens to it between going in and coming out."
head_counter = {"format": "{n} of 4 predicted", "total": 4}
```

**Instrument payload**

| Key | Type | Req | Drives |
|---|---|---|---|
| `gases` | list of dict | **yes**, ≥ 2 | one row per gas, in the drawn order. Raises if fewer than 2 |
| `gases[].id` | str | **yes** | the row key. Raises if missing |
| `gases[].name` | str | **yes** | the row label, and the gas name in the reveal table |
| `gases[].in_pct` | number ≥ 0 | **yes** | the **inhaled bar width**, as a percentage of the bar's track. Raises if missing or negative |
| `gases[].out_pct` | number ≥ 0 | **yes** | the **exhaled bar width**. Same |
| `gases[].change` | str | **yes** | the correct prediction — must be one of `choices[].id`. Raises if it is not, because a row whose right answer is not offered can never be predicted correctly |
| `gases[].in_label` | str | **yes** | the printed inhaled figure — `78%`, `variable, often low`. **Authored, not composed from `in_pct`**: water vapour's two cells are words, not percentages, and a template would print `1%` for a figure Design deliberately refused to give |
| `gases[].out_label` | str | **yes** | the printed exhaled figure |
| `gases[].verdict` | str | **yes** | the mono line under the gas name in the reveal (`unchanged`, `falls by about a quarter`) |
| `choices` | list of dict | **yes**, ≥ 2 | the prediction buttons, identical on every row |
| `choices[].id` | str | **yes** | matched against `gases[].change` |
| `choices[].label` | str | **yes** | the button caption |
| `reveal_label` | str | **yes** | the locked button's caption. Raises if missing — a button with no words is not a control |
| `count` | dict | **yes** | the mono line beside the button. Needs **both** `committed` and `scored`; raises without either |
| `count.committed` | str | **yes** | before the reveal. `{n}` = rows committed, `{total}` = row count |
| `count.scored` | str | **yes** | after the reveal. `{n}` = rows predicted correctly |
| `table` | dict | **yes** | the reveal table's three column headings. Needs `gas`, `inhaled`, `exhaled`; raises if any is missing, because the two data columns are also the per-cell captions on a narrow screen and a missing one leaves a bare number |
| `close_lead` | str | **yes** | the display-type lead-in on the closing paragraph (`The two that matter:`) |
| `close` | str (rich) | **yes** | the closing paragraph. `<em>` / `<strong>` allowed |
| `min_bar_pct` | number | no, default `1.5` | the **clamp**. A bar is never drawn narrower than this, so carbon dioxide at 0.04% is visible at all. See the note below |

**The clamp is the one dishonest pixel in the unit.** `min_bar_pct` makes the 0.04% bar about
37× too wide. That is why the **numeral sits next to the bar in every cell** and why `in_label` /
`out_label` are required: the bar shows *that* it changed, the numeral is the only thing that says
*by how much*. Do not remove the numerals to tidy the layout, and do not raise the clamp.

**Design's values** (b4-01, `GASES` / `CHOICES`, page lines 345–360):

```python
gases = [
  {"id": "n2",  "name": "Nitrogen",       "in_pct": 78,   "out_pct": 78,
   "change": "same", "in_label": "78%",   "out_label": "78%",
   "verdict": "unchanged"},
  {"id": "o2",  "name": "Oxygen",         "in_pct": 21,   "out_pct": 16,
   "change": "down", "in_label": "21%",   "out_label": "16%",
   "verdict": "falls by about a quarter"},
  {"id": "co2", "name": "Carbon dioxide", "in_pct": 0.04, "out_pct": 4,
   "change": "up",   "in_label": "0.04%", "out_label": "4%",
   "verdict": "rises a hundredfold"},
  {"id": "h2o", "name": "Water vapour",   "in_pct": 1,    "out_pct": 6,
   "change": "up",   "in_label": "variable, often low", "out_label": "saturated",
   "verdict": "rises — and it is warmer"},
]
choices = [
  {"id": "up",   "label": "Goes up"},
  {"id": "down", "label": "Goes down"},
  {"id": "same", "label": "Stays the same"},
]
reveal_label = "Analyse both bags"
count = {"committed": "{n} of {total} committed",
         "scored":    "{n} of {total} predicted correctly"}
table = {"gas": "Gas", "inhaled": "Inhaled air", "exhaled": "Exhaled air"}
close_lead = "The two that matter:"
```

`close` is the paragraph at page line 168, beginning `oxygen falls from 21 to 16, …`.

**Behaviour the engine guarantees.** Rows lock the instant the reveal opens; the reveal button is
disabled until every row is committed; a correct row is outlined in `--ks3-alert` after the reveal
and an incorrect one loses its panel; the stage ticks when the reveal opens (not when the four
predictions are made — Design's `isDone` reads `airOpen`).

---

## 2 · `bell-jar` — b4-02 `#s-model`

A diaphragm slider, a chest-and-lung picture, four readouts, and the four-step causal chain.

**The chain is the instrument.** Its whole job is that the *first* line is always the muscle and the
*last* line is always the air. Every line of every phase is authored; the engine only chooses which
phase is showing and fills the numbers.

**Shell keys for this block**

```python
eyebrow      = "The bell-jar model · work the diaphragm"
heading      = "Pull the sheet down and read the pressure"
prompt       = ("A sealed jar, a rubber sheet across the bottom, and a balloon on a tube "
                "through the lid. Move the sheet and watch the order in which things change.")
head_counter = {"off": "not moved yet", "on": "model worked"}
```

**Instrument payload**

| Key | Type | Req | Drives |
|---|---|---|---|
| `start` | int 0–100 | no, default `20` | the slider's resting value |
| `rest` | int 0–100 | no, default `20` | the value that counts as *at rest*. Above it the phase is `in`, below it `out`, exactly on it `rest` |
| `model` | dict | **yes** | the physics. Raises if missing or if any of the four numbers is absent |
| `model.volume_base` | number | **yes** | litres at `dia = 0` |
| `model.volume_span` | number | **yes** | litres added across the full slider travel. Volume = `volume_base + (dia/100) × volume_span` |
| `model.pressure_zero` | number 0–1 | **yes** | the slider fraction at which pressure equals atmospheric. Must equal `rest/100` or the chain and the readout disagree about which phase is which — **raises if it does not** |
| `model.pressure_span` | number | **yes** | kPa per unit fraction. Pressure = `−(dia/100 − pressure_zero) × pressure_span` |
| `slider_label` | str | **yes** | the mono caption over the slider (`Diaphragm`) |
| `slider_aria` | str | **yes** | the visually-hidden `<label>` (`Diaphragm position`) |
| `jar_label` | str | **yes** | the caption on the picture panel (`The jar`) |
| `readouts_label` | str | **yes** | the caption on the readout panel (`Readouts`) |
| `chain_label` | str | **yes** | the caption over the chain (`The order of events`) |
| `readouts` | dict | **yes** | the four rows' left-hand labels and the two fixed values |
| `readouts.volume_label` | str | **yes** | `Chest volume` |
| `readouts.volume_format` | str | **yes** | `{volume} L` — one decimal place |
| `readouts.pressure_label` | str | **yes** | `Pressure inside` |
| `readouts.pressure_format` | str | **yes** | `{pressure} kPa` — two decimal places, **signed**, with an explicit `+` when positive |
| `readouts.outside_label` | str | **yes** | `Pressure outside` |
| `readouts.outside_value` | str | **yes** | `0.00 kPa (atmospheric)` — fixed, never computed |
| `readouts.air_label` | str | **yes** | `Air movement` |
| `presets` | list of dict | **yes**, ≥ 1 | the preset buttons under the slider |
| `presets[].label` | str | **yes** | the caption (`Breathe in`) |
| `presets[].value` | int 0–100 | **yes** | the slider value it sets |
| `presets[].id` | str | no | not read by this renderer — authored for legibility only (`two-process-ledger` does read it) |
| `phases` | dict | **yes** | three records keyed `in`, `out`, `rest`. **Raises unless all three are present** — every one is reachable from the slider, and a phase with no text is a chain that goes blank |
| `phases.*.phase_label` | str | **yes** | the alert-coloured line under the picture (`Diaphragm contracted — breathing in`) |
| `phases.*.dia_label` | str | **yes** | the alert-coloured value beside `Diaphragm` (`contracted, flattened`) |
| `phases.*.air` | str | **yes** | the fourth readout's value (`inwards` / `outwards` / `none`) |
| `phases.*.chain` | list of str | **yes**, exactly 4 | the four chain lines, in order. **Raises unless there are exactly four**, and raises if the phase's four are not all present. Templates: `{volume}`, `{pressure}`, `{pressure_abs}` |
| `phases.*.note` | str (rich) | **yes** | the paragraph under the chain |

**`{pressure}` vs `{pressure_abs}` — read this before writing the `in` chain.** `{pressure}` is
signed (`-0.79`); `{pressure_abs}` is the magnitude (`0.79`). A sentence that already carries the
direction in words — *"pressure falls to … below atmospheric"* — must use `{pressure_abs}`, or it
reads *"falls to -0.79 kPa below atmospheric"*, which is a double negative. **Design's own `in`
chain uses the signed value and its `out` chain uses the magnitude** (page lines 457 and 462); the
engine offers both placeholders and takes no view, so this is the author's line to get right. It is
flagged for Mide as a defect on the drawn page, not a design choice.

**Design's values** (b4-02 `renderVals`, page lines 440–524):

```python
start = 20
rest  = 20
model = {"volume_base": 2.2, "volume_span": 3.3,
         "pressure_zero": 0.2, "pressure_span": 1.1}
presets = [{"id": "in",  "label": "Breathe in",  "value": 92},
           {"id": "out", "label": "Breathe out", "value": 4}]
```

Phase text: `in` = lines 455–458, `out` = 460–463, `rest` = 464–467; `note` = line 523 for `rest`
and line 524 for both `in` and `out` (Design authors one moving-state note and shows it in both).
`phase_label` = line 505, `dia_label` = 513, `air` = 510.

**Geometry the engine owns and the author does not.** The chest panel's height
(`28% + 58% × dia/100`) and the lung circle's `scale(0.62 + 0.55 × dia/100)` are drawing, not
science, and live in `shared/ks3.js`. Nothing student-readable comes out of either.

---

## 3 · `crossing-counter` — b4-03 `#s-gradient`

Two switches, four states, and two bars — **neither of which is ever zero**.

**The four states are a lookup table, not a simulation.** Each state carries its own authored note.
A computed version would have to rewrite those four notes as one sentence with numbers in it, and
the notes are where the lesson's argument is.

**Shell keys for this block**

```python
eyebrow      = "At the bench · count the crossings"
heading      = "Both directions, all the time"
prompt       = ("Oxygen molecules cross the alveolus wall in both directions every second. "
                "Switch breathing and blood flow on and off and watch what happens to the "
                "two counts — and to the difference between them.")
head_counter = {"off": "both flows running", "on": "switches used"}
```

**Instrument payload**

| Key | Type | Req | Drives |
|---|---|---|---|
| `switches` | list of dict | **yes**, exactly 2 | the two toggles. Raises unless there are exactly two — four states is `2²` and the lookup table is built from it |
| `switches[].id` | str | **yes** | must be `breathing` for the first and `blood_flow` for the second; `states[]` is keyed on both |
| `switches[].on_label` | str | **yes** | the caption while on (`Breathing: on`) |
| `switches[].off_label` | str | **yes** | the caption while off (`Breathing: stopped`) |
| `switches[].start` | bool | no, default `True` | whether the switch opens on |
| `states` | list of dict | **yes**, exactly 4 | the lookup table. **Raises unless all four `(breathing, blood_flow)` combinations are present exactly once** |
| `states[].breathing` | bool | **yes** | which state this row is |
| `states[].blood_flow` | bool | **yes** | which state this row is |
| `states[].alveolar_kpa` | number > 0 | **yes** | the alveolar oxygen readout, and the **inward** crossing count |
| `states[].blood_kpa` | number > 0 | **yes** | the blood oxygen readout, and the **outward** crossing count. **Raises if ≤ 0** — a zero here draws an outward bar of zero width, and a student who watches the outward bar disappear has learnt the misconception the lesson exists to remove |
| `states[].note` | str (rich) | **yes** | the cream paragraph under the bars for this state |
| `crossings_per_kpa` | number > 0 | no, default `90` | crossings per second per kPa. Counts are `round(kpa × this)` |
| `max_crossings` | number > 0 | no, default `1250` | the bar track's full-scale value. Must exceed the largest count or a bar overflows — **raises if it does not** |
| `tiles` | dict | **yes** | the three readout tiles' labels. Needs `alveolar`, `blood`, `net` |
| `kpa_format` | str | **yes** | `{v} kPa` — one decimal place |
| `crossing_format` | str | **yes** | `{n} per second` — whole numbers |
| `net_zero` | str | **yes** | what the net tile reads when the difference is negligible (`about zero`) |
| `net_zero_below` | number | no, default `20` | the count difference at or under which `net_zero` is printed |
| `bars` | dict | **yes** | the two bars' names. Needs `into` and `out_of`; raises without either |

**Design's values** (b4-03 `renderVals`, page lines 400–470):

```python
switches = [{"id": "breathing",  "on_label": "Breathing: on",
             "off_label": "Breathing: stopped",  "start": True},
            {"id": "blood_flow", "on_label": "Blood flow: on",
             "off_label": "Blood flow: stopped", "start": True}]
states = [
  {"breathing": True,  "blood_flow": True,  "alveolar_kpa": 13.3, "blood_kpa": 5.3,  "note": …},
  {"breathing": True,  "blood_flow": False, "alveolar_kpa": 13.3, "blood_kpa": 13.1, "note": …},
  {"breathing": False, "blood_flow": True,  "alveolar_kpa": 6.0,  "blood_kpa": 5.6,  "note": …},
  {"breathing": False, "blood_flow": False, "alveolar_kpa": 9.3,  "blood_kpa": 9.3,  "note": …},
]
crossings_per_kpa = 90
max_crossings     = 1250
tiles = {"alveolar": "Oxygen in the alveolus",
         "blood":    "Oxygen in the blood",
         "net":      "Net oxygen absorbed"}
kpa_format      = "{v} kPa"
crossing_format = "{n} per second"
net_zero        = "about zero"
bars = {"into": "Crossing INTO the blood", "out_of": "Crossing OUT of the blood"}
```

The four notes are page lines 452–455, in the state order above.

⚠️ **The both-on note quotes its own numbers** — *"1197 in, 477 out"* — and those are
`13.3 × 90` and `5.3 × 90`. If a science review moves either kPa figure, that sentence has to move
with it. The engine cannot check a number embedded in prose, and it does not try to.

---

## 4 · `fault-bench` — b4-04 `#s-bench`

Three factors, one shared list of parts, and a gated reveal. The B2 `system-switch` idiom run
backwards: the student is given a symptom and must **locate** the part, rather than switch a part
off and be told the symptom.

**Shell keys for this block**

```python
eyebrow      = "Locate the fault · three factors"
heading      = "Which part of the system does each one hit?"
prompt       = ("Commit to a part of the system before opening each one. The four options are "
                "the same every time, and only one of the three factors hits the same part twice.")
head_counter = {"format": "{n} of 3 opened", "total": 3}
```

**Instrument payload**

| Key | Type | Req | Drives |
|---|---|---|---|
| `parts` | list of dict | **yes**, ≥ 2 | the option list, identical for every factor. Raises if fewer than 2 |
| `parts[].id` | str | **yes** | matched against `factors[].part` |
| `parts[].text` | str | **yes** | the option's label |
| `question` | str | **yes** | the mono prompt over the options (`Which part of the system is affected?`) |
| `factors` | list of dict | **yes**, ≥ 2 | the tabs, in the drawn order |
| `factors[].id` | str | **yes** | the tab key |
| `factors[].label` | str | **yes** | the tab caption (`Asthma attack`) |
| `factors[].tag` | str | **yes** | the mono line over the scenario (`Factor 2 · during an asthma attack`) |
| `factors[].scenario` | str (rich) | **yes** | the scenario paragraph |
| `factors[].part` | str | **yes** | the id of the part that IS at fault. **Raises unless it is one of `parts[].id`** — a locator whose answer is not on the list cannot be located |
| `factors[].answer` | str | **yes** | the display-type headline in the reveal (`The airways — narrowed bronchioles.`) |
| `factors[].rows` | list of dict | **yes**, ≥ 1 | the reveal's definition rows |
| `factors[].rows[].label` | str | **yes** | the mono `<dt>` (`Reversible?`) |
| `factors[].rows[].text` | str (rich) | **yes** | the `<dd>` |
| `open_label` | str | **yes** | the gated button's caption (`Show what happens`) |
| `hints` | dict | **yes** | the mono line beside the button. Needs all three of `none`, `ready`, `opened` |
| `verdicts` | dict | **yes** | the reveal's mono eyebrow. Needs both `right` and `wrong` |
| `start_factor` | str | no, default first | which tab opens |

**Design's values** (b4-04 `PARTS` / `FACTORS`, page lines 328–380 and 498–520):

```python
parts = [
  {"id": "muscles", "text": "The breathing muscles — diaphragm and intercostals"},
  {"id": "airways", "text": "The airways — bronchi and bronchioles"},
  {"id": "alveoli", "text": "The alveoli — the exchange surface itself"},
  {"id": "blood",   "text": "The blood — what carries the oxygen away"},
]
question   = "Which part of the system is affected?"
open_label = "Show what happens"
hints    = {"none": "choose a part first", "ready": "ready", "opened": "opened"}
verdicts = {"right": "You located it", "wrong": "Not the part you chose"}
```

Factor ids / answers: `exercise` → `muscles`, `asthma` → `airways`, `smoking` → `alveoli`.

**Behaviour the engine guarantees.** Each factor keeps its own pick and its own opened flag, so
moving between tabs finds each exactly as it was left; options lock once that factor is opened; the
button is disabled until a part is picked; the verdict compares the pick against `part` and the
answer is shown either way — **the reveal is never withheld for a wrong answer**. The stage ticks
when all three factors have been opened.

---

## 5 · `two-process-ledger` — b4-05 `#s-ledger`

A light slider, three bars, and a verdict panel whose middle branch is the compensation point.

**The respiration bar never moves.** That is the instrument's argument, and it is why the bar is
drawn from a constant rather than from a curve evaluated at a fixed point.

**Shell keys for this block**

```python
eyebrow      = "At the bench · turn the light up"
heading      = "Two processes, one net figure"
prompt       = ("Respiration is the top bar. Photosynthesis is the second. What a sensor "
                "outside the leaf measures is only the difference — the third.")
head_counter = {"off": "currently dark", "on": "light adjusted"}
```

**Instrument payload**

| Key | Type | Req | Drives |
|---|---|---|---|
| `start_light` | int 0–100 | no, default `0` | the slider's opening value |
| `light_label` | str | **yes** | the mono caption over the slider (`Light level`) |
| `light_aria` | str | **yes** | the visually-hidden `<label>` |
| `dark_label` | str | **yes** | the value shown at light 0 (`darkness`) — Design does not print `0 units` |
| `light_format` | str | **yes** | the value at any other light (`{n} units`) |
| `presets` | list of dict | **yes**, ≥ 1 | the preset buttons |
| `presets[].id` / `.label` / `.value` | str / str / int 0–100 | **yes** | as drawn |
| `resp_rate` | number > 0 | **yes** | the flat respiration rate, in the same relative units as the curve |
| `curve` | dict | **yes** | the photosynthesis curve |
| `curve.max` | number | **yes** | the saturating maximum. **Raises unless `curve.max > resp_rate`** — otherwise photosynthesis can never overtake respiration and the compensation point does not exist |
| `curve.constant` | number > 0 | **yes** | the light constant. Rate = `curve.max × (1 − e^(−light / curve.constant))` |
| `curve.scale` | number > 0 | **yes** | the bar track's full-scale value. Raises if smaller than `curve.max` or `resp_rate` |
| `balanced_window` | number > 0 | no, default `0.25` | the half-width of the balanced window. `abs(net) < this` is the compensation point |
| `rate_format` | str | **yes** | the two rate readouts (`{v} units`) — one decimal place |
| `respiration` | dict | **yes** | needs `name` and `note` |
| `photosynthesis` | dict | **yes** | needs `name`, `note_dark` (shown at light 0) and `note_light` |
| `net` | dict | **yes** | needs `name`, `in_format`, `out_format` and `note` |
| `net.in_format` | str | **yes** | e.g. `net CO₂ in {v} units` |
| `net.out_format` | str | **yes** | e.g. `net CO₂ out {v} units` |
| `verdicts` | dict | **yes** | three branches keyed `balanced`, `uptake`, `release`. **Raises unless all three are present**, each with `tag`, `head` and `why` |
| `balanced_preset` | str | no | the id of the preset that is claimed to BE the compensation point. When authored, **the renderer raises unless that preset's light value lands inside the balanced window**. See below — this is the key that stops the payoff going unreachable silently |

**Two gates on the maths, and they are different gates.** The renderer always raises if *no* light
value between 0 and 100 lands inside the balanced window, because `verdicts.balanced` would then be
copy no student can ever reach. It raises on `balanced_preset` only when you author one — the engine
does not get to decide which preset is the compensation point, but it does hold you to it once you
have said.

**Design's values** (b4-05, page lines 330–345 and `renderVals` 400–410):

```python
start_light     = 0
resp_rate       = 2
curve           = {"max": 9, "constant": 32, "scale": 9}
balanced_window = 0.25
presets = [{"id": "dark",   "label": "Midnight",    "value": 0},
           {"id": "dawn",   "label": "Dawn",        "value": 21},
           {"id": "cloudy", "label": "Overcast",    "value": 48},
           {"id": "bright", "label": "Bright noon", "value": 100}]
```

⚠️ **`dawn = 21` is nowhere near the compensation point, and Design's own copy says it should be.**
This was measured, not assumed:

| light | photosynthesis | net | branch |
|---|---|---|---|
| 0 (Midnight) | 0.00 | −2.00 | release |
| **7** | 1.77 | **−0.23** | **balanced** |
| **8** | 1.99 | **−0.01** | **balanced** |
| **9** | 2.21 | **+0.21** | **balanced** |
| 21 (Dawn) | 4.33 | **+2.33** | uptake |
| 48 (Overcast) | 6.99 | +4.99 | uptake |
| 100 (Bright noon) | 8.61 | +6.61 | uptake |

The window is `light ∈ {7, 8, 9}` — the exact balance is at **8.04**. `NOTES-B4.md` §3.4 states the
dawn preset is tuned to sit inside it; against Design's own curve constants it is not, and pressing
*Dawn* on Design's page reads **Net uptake of carbon dioxide**. The page also contradicts itself:
`verdicts.balanced.why` opens *"This is the dawn reading from the hook"*, which is a claim that
dawn IS the compensation point.

The engine takes no view on which side is right — that is a science-owner call and it is flagged
for Mide. What the author must do is make the page agree with itself:

- set `presets[dawn].value = 8` and author `balanced_preset = "dawn"`, so the copy and the control
  say the same thing and the build holds them together; **or**
- leave `21`, author **no** `balanced_preset`, and change `verdicts.balanced.why` so it no longer
  claims to be the dawn reading — the compensation point is then reachable only by dragging the
  slider onto 7, 8 or 9.

Do not widen `balanced_window` to cover 21: at ±2.4 every reading from midnight to overcast would
report itself as balanced.

**As built.** `ks3_data/b4/lesson_05_stomata_and_gas_exchange_in_plants.py` took the first option —
`presets[dawn].value = 8` with `balanced_preset = "dawn"` — so the copy and the control now say the
same thing and the build holds them together. The underlying question (does *Dawn* belong at the
compensation point, or should the balanced copy stop claiming to be the dawn reading?) is still
Mide's, and it is flagged.

---

## What the renderers do NOT read

Not because they were forgotten — because they belong somewhere else:

- **The five band sections** (`#s-parts`, `#s-limits`, `#s-built`, `#s-smoke`, `#s-stomata`) are not
  instruments. None has a control, a commitment or any state; each is a card grid or a numbered
  list with a KEY FACT box inside it. They are ordinary blocks and are not covered by anything in
  this file.
- **`data-stage-done`** is emitted by the shell and set by the wiring, never authored.
- **The rail.** Each instrument ticks its own stage; `done_when` is documentation only
  (`build_ks3.py` puts it in `data-rail-stages` and nothing reads it).
