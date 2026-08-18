# B10 — payload schema

Written **before** the authoring passes are dispatched, for the same reason B7's was: B5 shipped
without one, seven records then authored against Design's pages rather than an agreed schema, and
five of them named the same four labels nine different ways.

**If this document and Design's page disagree, the page wins on MEASUREMENT (what is drawn) and
this document wins on NAMING (what we call it).** Where the page needs something this schema has
not anticipated, follow the page and say so in the report.

Everything below is measured from the five approved pages in `docs/ks3/design-reference/b10/`, not inferred from
`NOTES-B10.md`. Where the two disagree, §10 says so.

---

## 0. Rules that bind all five instruments

1. **All five are DOM-only.** Grepped across all five pages: no `<canvas>`, no
   `requestAnimationFrame`, no `setTimeout`, no `setInterval`. The only animation is CSS —
   a shared `@keyframes b100N-arrive` on `[data-arrive]`, and a `height`/`width` transition on
   `[data-fill]` (b10-01 bars, b10-04 tally bars), both disabled under
   `prefers-reduced-motion`. An instrument that wants a canvas or a timer is a finding, not a
   licence.
2. **All five flagships ship on `ks3-block ks3-dark ks3-practical`** — measured from the class
   attribute on `<section id="s-bench">` on all five pages. Under `ACTIVITY_SHELLS` in
   `build_ks3.py` that string is `segment: "practical"`. Do not guess the shell from the kind
   name; §4 of the build contract records that B1 got two of six wrong.
3. ⛔ **NO RUNTIME STATE IS AUTHORED.** Under contract R5 a key with no read site is a dead key
   and fails `ks3_key_audit.py`. `plotted`, `predicts`, `shown`, `solved`, `tally`, `last`,
   `picks`, `opened` are all values the *runtime* owns. The renderer initialises its own state.
   **The one exception is an OPENING SELECTION that is not the first entry in its list** — that is
   an authored teaching choice, not runtime state, and it gets a key. Three exist in B10 (§3.2
   `opens_on`, §4 `start`, §5 `start`) and they are named in the shapes below. Where the opening
   selection *is* the first entry (b10-01 `height`, b10-05 `dogs`) **no key is authored** and the
   renderer defaults to index 0.
4. **Every authored key must have a read site in the same pass.** Wire the read or do not author
   the key. "It documents intent" is a comment, not a read site.
5. **Every student-facing string is lifted byte-identical** from the approved page via
   `node tools/extract_design_payload.js <page>`. Never retype science-bearing copy — b10-02's
   scale column and b10-05's seven verdicts are the passages where a retyped digit would be
   invisible and wrong.
6. **B10 benches DO adjudicate a commitment, and that is a deliberate departure from B7 §0.6.**
   B7 ruled "nothing marks correctness except the ladder". Three B10 benches break it as drawn:
   b10-01 prints `Your prediction was right` / `Not what you predicted`, b10-05 prints
   `That is the answer` / `Not quite`, and b10-03 prints `rules this model out` against a failing
   evidence card. Measured, not guessed. The wording is soft in every case and it confronts the
   IDEA, never the student — which is the spirit of the B7 rule even where the letter goes. **Ship
   as drawn; do not "fix" it to match B7,** and do not carry the amber `is-wrong` ladder treatment
   onto a bench. Recorded here so the deviation is a decision rather than a drift.

## 1. One spelling per concept, for the whole unit

Inherited from B7's table unchanged, plus five rows B10 needs. **A concept already in B7's table
keeps B7's spelling** — this is the second unit under the rule, and re-spelling now would cost more
than B5's nine names did.

| Concept | The key | Never |
|---|---|---|
| Lead line above a set of options | `options_label` | `options_lead`, `choose_prompt` |
| The button that runs/commits the bench | `run_label` | `commit_label`, `check_label` |
| The same button once it has been pressed | `run_done_label` | `ran_label`, `done_label` |
| The button that returns it to the start | `reset_label` | `clear_label`, `again_label` |
| Map of branch id → outcome | `verdicts` | `verdict`, `outcomes` |
| A single line of help under a control | `hint` | `hints`, `note` |
| The closing paragraph after the payoff | `close` | `closing`, `after` |
| The short mono line in the bench header | `progress_suffix` | `counter`, `tally_label` |
| An authored non-first opening selection | `start` (a map) / `opens_on` (a single id) | `default`, `initial`, `preset` |
| The sentence-fragment form of an option | `phrase` (sits beside `label` on the option) | `sentence`, `long_label` |

---

## 2. `variation-plotter` — b10-01 `#s-bench`

```python
{"kind": "variation-plotter", "id": "...", "segment": "practical",
 "options_label": "...",                        # "Characteristic" — above the six tabs
 "characteristics": [
   {"id": "...", "label": "...",                # label = tab text; name = panel heading
    "name": "...",
    "data_type": "continuous" | "discontinuous", # ⚠️ LOAD-BEARING — see the gap rule below
    "axis": "...",                              # mono caption under the bars
    "bins": [{"label": "...", "n": int}],       # ORDERED; n = students in that bin
    "shape": "...",                             # answers "what shape is it"
    "cause": "..."}],                           # answers "what caused it" — a SEPARATE question
 "predict_label": "...",                        # "Before you plot it — which shape do you expect?"
 "predict_options": [{"id": "continuous" | "discontinuous", "label": "..."}],
 "kind_lines": {"continuous": "...", "discontinuous": "..."},   # the display-weight verdict line
 "run_label": "...", "run_done_label": "...",   # "Plot the data" / "Plotted"
 "verdicts": {"right": "...", "wrong": "..."},  # the mono tag ONLY — judges the prediction
 "progress_suffix": "..."}                      # "plotted", as in "2 of 6 plotted"
```

### The bar gap is DERIVED, never authored

This is the whole pedagogical point of the instrument and it must not be reduced to a style key.
Design computes, once per selected characteristic:

```js
const gap = c.kind === 'continuous' ? '0px' : '6px';
```

and then gives every bar `width: calc(100% - <gap>)` inside a flex row where each bin owns an equal
`flex: 1 1 0` column. So a continuous characteristic's bars fill their column edge to edge and
**touch**; a discontinuous one's bars are 6px narrower than their column and **stand apart**.

**There is no `gap` key, no `spacing` key and no `chart_type` key.** The gap is a pure function of
`data_type`, and `data_type` is already carried because the verdict line and the prediction check
both read it. Authoring the gap separately would let a record ship touching bars for blood group.
The histogram/bar-chart convention is taught by the rendering, so the rendering must not be
overridable.

Bar height is `max(3, (n / max(n over that characteristic's bins)) * 100)` percent — the floor of 3
keeps a one- or two-student bin visible. `maxN` is per characteristic, so each graph is scaled to
its own tallest bin.

### State and controls

| State | Owner | Controls that mutate it |
|---|---|---|
| `char` — selected characteristic id | runtime, opens on `characteristics[0]` | six tabs, one per characteristic |
| `predicts` — `{charId: "continuous"\|"discontinuous"}` | runtime | two predict buttons; only shown while `!plotted[char]` |
| `plotted` — `{charId: true}` | runtime, sticky | the run button |

The run button is `disabled` unless a prediction exists for the current characteristic and it has
not already been plotted — **the student cannot see the graph before committing to a shape**, which
is the instrument's gate. Once plotted, the predict buttons disappear (`askPredict: !plotted`) and
the plot cannot be re-run for that characteristic. **There is no reset.** Six characteristics ×
one prediction each is the whole exercise.

Verdict panel, in order: mono tag (`verdicts.right`/`verdicts.wrong`) → `kind_lines[data_type]` in
display weight → `shape` → a rule, then `**What causes it:** ` + `cause`. The rule and the bold
lead-in are chassis; the split between `shape` and `cause` is content, and it is the second half of
the lesson's argument.

Six characteristics, measured: `height`, `span`, `mass` (continuous, 7/6/6 bins) and `blood`,
`tongue`, `eyes` (discontinuous, 4/2/3 bins).

---

## 3. `zoom-bench` — b10-02 `#s-bench`

```python
{"kind": "zoom-bench", "id": "...", "segment": "practical",
 "levels": [{"name": "...", "scale": "...", "body": "..."}],   # ORDERED outermost → innermost, 6
 "in_label": "...", "in_done_label": "...",     # "Zoom in" / "As far in as it goes"
 "reset_label": "...",                          # "Back out"
 "close": "...",                                # revealed only when all six are open
 "progress": {"all": "...", "step_prefix": "...", "step_join": "..."},   # "all six levels" | "level 3 of 6"
 "say_it_back": {
   "options_label": "...",                      # "Say it back — which one is which?"
   "opens_on": "...",                           # ⚠️ id of question 2, NOT the first — see below
   "questions": [{"id": "...", "label": "...", "answer": "..."}]}}       # exactly 4
```

### 3.1 The six levels and their scale figures — verbatim

The scale column **is the argument**, so every figure is quoted here exactly as the page prints it.
A retyped zero in row 6 would be invisible and wrong.

| # | `name` | `scale` (verbatim) |
|---|---|---|
| 1 | `A person` | `1.6 m` |
| 2 | `A cell` | `0.02 mm` |
| 3 | `The nucleus` | `0.006 mm` |
| 4 | `A chromosome` | `0.002 mm long` |
| 5 | `A gene` | `a section of the strand` |
| 6 | `The bases` | `0.0000003 mm apart` |

**Row 5 prints no number at all.** That is measured, not an omission in this document — a gene has
no characteristic length, and Design says so in words instead. Do not "complete" the column.

**Cross-check against the brief, both claims verified against what the page actually prints:**

- *"two metres of DNA per cell"* — the page prints it three times, and they agree. Hook `<h2>`:
  "Two metres of DNA, in a nucleus you cannot see." Hook prompt: "measures about two metres."
  Say-it-back answer `longest`: "about two metres per cell if you uncoiled it all." ✅ Consistent.
  It is **not** in the `levels` list — it lives in the hook and in the say-it-back panel only.
- *nucleus ~0.006 mm* — printed twice, in two notations, and they agree. Hook prompt: "around six
  thousandths of a millimetre across." Level 3 `scale`: `0.006 mm`. ✅ Consistent.

⚠️ **What does NOT hold is the thousandfold claim.** Both `NOTES-B10 §1.2` and the page's own bench
lead say the scale "drops by roughly a factor of a thousand at every step". Worked from the printed
figures: 1.6 m → 0.02 mm is ~10⁵; 0.02 → 0.006 mm is ~3×; 0.006 → 0.002 mm is ~3×; row 5 has no
figure; 0.002 mm → 0.0000003 mm is ~7000×. Not one of the four measurable steps is a thousandfold.
See §10, finding 2 — this is Mide's to rule on, and it is a copy fix, not a schema fix.

### 3.2 `opens_on` is authored because it is not the first question

`state.quiz` opens on `'contains'`, which is `questions[1]` — *"What contains what?"*, the question
that states the whole nesting. That is a teaching choice and it gets a key. The four questions,
measured: `longest`, `contains`, `howmany`, `same`.

### 3.3 State and controls

| State | Owner | Controls |
|---|---|---|
| `shown` — int, 1..6 | runtime, opens at 1 | `in_label` button (`shown+1`, capped at 6, disabled at 6); `reset_label` button (back to 1) |
| `quiz` — question id | runtime, opens on `opens_on` | four question tabs |

A level renders its `body` only once `shown` reaches it; the `name` and `scale` are visible from the
start at 45% opacity, so the student can see how far there is to go. The current level carries an
alert-coloured border. `close` renders only at `shown === 6`.

**The say-it-back panel is inside `<section id="s-bench">`, not a block of its own** — measured. It
is therefore part of this payload, not a second activity. Its answers are always visible for the
selected question; it gates nothing and marks nothing.

---

## 4. `model-builder` — b10-03 `#s-bench`

```python
{"kind": "model-builder", "id": "...", "segment": "practical",
 "dials": [{"id": "...", "name": "...",
            "options": [{"id": "...", "label": "...", "phrase": "..."}]}],  # 3 dials: 3 × 2 × 2
 "start":   {"<dial-id>": "<option-id>"},   # ⚠️ Pauling's WRONG triple helix — deliberate
 "correct": {"<dial-id>": "<option-id>"},
 "evidence": [{"id": "...", "name": "...", "what": "...", "why": "...",
               "requires": {"<dial-id>": "<option-id>"},   # model must match ALL of these
               "forbids":  {"<dial-id>": "<option-id>"}}], # model must NOT match ALL of these
 "verdict_tags": {"pass": "...", "fail_one": "...", "fail_many": "..."},
 "verdicts": {"pass": "...", "fail": "..."},
 "progress_suffix": "..."}                  # "tests passed", as in "2 of 4 tests passed"
```

`label` is the button text; `phrase` is the same option's sentence fragment. The panel heading is
built as `", ".join(phrase for each dial, in dial order)` — e.g. *"Three strands, bases on the
outside, any base with any base."* The two forms genuinely differ (`Two` vs `Two strands`,
`Inside, facing each other` vs `bases on the inside`), so both are content and both are authored.

`requires` / `forbids` exist because three of the four tests are a single equality and the fourth
is a negated conjunction. Design writes them as JS predicates; declaratively:

| `id` | `requires` | `forbids` |
|---|---|---|
| `photo` | `{"strands": "2"}` | — |
| `water` | `{"bases": "in"}` | — |
| `chargaff` | `{"pairing": "specific"}` | — |
| `pauling` | — | `{"strands": "3", "bases": "out"}` |

A card passes when every `requires` pair matches AND the `forbids` map is not matched in full. A
failing card renders its `why` in alert colour under its `what`; a passing card renders only `what`.
`why` is the **elimination text** — the line that names what the evidence rules out.

### 4.1 The four elimination texts — verbatim

- **`photo` · Photo 51 · Franklin and Gosling, 1952** — *"The measured width does not fit this. A
  single strand is too narrow and three strands are too wide — the pattern says two."*
- **`water` · Franklin's water measurements** — *"If the bases are on the outside then the
  phosphates are on the inside, which contradicts the water measurements — and the negative
  phosphates would repel each other."*
- **`chargaff` · Chargaff's ratios, 1950** — *"If any base could pair with any other there would be
  no reason for A and T to come in equal amounts in every organism ever measured."*
- **`pauling` · Pauling's triple helix, early 1953** — *"This is Pauling's model, and it has already
  been ruled out. Its phosphates were crowded into the centre where their negative charges would
  push the molecule apart."*

### 4.2 The full 12 × 4 matrix — worked, not assumed

`P` = consistent, `F` = rules this model out.

| # | strands | bases | pairing | photo | water | chargaff | pauling | passes |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | in | specific | F | P | P | P | 3 |
| 2 | 1 | in | any | F | P | F | P | 2 |
| 3 | 1 | out | specific | F | F | P | P | 2 |
| 4 | 1 | out | any | F | F | F | P | 1 |
| **5** | **2** | **in** | **specific** | **P** | **P** | **P** | **P** | **4 ✅** |
| 6 | 2 | in | any | P | P | F | P | 3 |
| 7 | 2 | out | specific | P | F | P | P | 3 |
| 8 | 2 | out | any | P | F | F | P | 2 |
| 9 | 3 | in | specific | F | P | P | P | 3 |
| 10 | 3 | in | any | F | P | F | P | 2 |
| 11 | 3 | out | specific | F | F | P | F | 1 |
| **12** | **3** | **out** | **any** | **F** | **F** | **F** | **F** | **0 ← `start`** |

**The "exactly one of twelve passes all four" claim HOLDS.** Row 5 — two strands, bases inside,
A with T and C with G — is the unique 4/4, and it is the structure published in April 1953.

Two things the matrix shows that the NOTES do not:

- **`pauling` is not an independent constraint.** It fails only rows 11 and 12, and both of those
  already fail `photo` and `water`. There is no combination anywhere in the twelve that passes the
  other three and fails Pauling. Its job is not to eliminate — it is to make the opening state
  cost four failures instead of three, and to teach flag 8's point that a wrong model is useful
  evidence. **Keep the card. Do not "tidy" it as redundant** — removing it would leave the opening
  state at 3/4 failures and would delete the lesson's only worked example of a rival being ruled
  out.
- **`start` is the unique 0/4 row.** Row 12 is the only combination in the twelve that fails every
  single test. The bench therefore opens with all four cards red — the most emphatic possible
  opening — and every dial the student touches can only improve it. That is elimination as a
  method, presented as a monotone descent. It is not an accident of the preset; it is the preset.

### 4.3 State and controls

| State | Owner | Controls |
|---|---|---|
| `model` — `{strands, bases, pairing}` | runtime, opens on `start` | seven dial buttons (3 + 2 + 2) |
| `solved` — bool, **STICKY** | runtime | set true the first time `model == correct`; never cleared |

⚠️ **There is no run button and no reset button.** Measured: the four evidence cards re-evaluate
live on every dial press. Do not author `run_label` or `reset_label` here — B7's `reactant-remover`
and `method-breaker` both had one, and copying that pattern across would add a control Design did
not draw. The bench header counter (`"n of 4 tests passed"`) is the only running feedback.

`solved` is sticky by construction (`solved: st.solved || ok`): once the student has reached the
double helix, the rail stop stays ticked even if they go back and break the model to explore. That
stickiness is what `data-stage-done="1"` must mirror.

---

## 5. `pea-cross` — b10-04 `#s-bench`

```python
{"kind": "pea-cross", "id": "...", "segment": "practical",
 "genotypes": [{"id": "...", "label": "...", "alleles": ["P", "p"]}],   # PP, Pp, pp
 "parents":   [{"id": "...", "name": "..."}],   # two; both draw the same genotype set
 "start":     {"<parent-id>": "<genotype-id>"}, # ⚠️ Pp × Pp — NOT genotypes[0], see below
 "phenotypes": {"dominant": "...", "recessive": "..."},   # "purple" / "white"
 "one_label": "...", "many_label": "...", "many_n": 100, "reset_label": "...",
 "cross_join": "...",                           # "crossed with", between the two genotype ids
 "last_label": "...",                           # "Most recent seed"
 "last_template": "...",                        # slots {g1} {g2} {p1} {p2} {genotype} {phenotype}
 "tally_rows": [{"id": "...", "name": "..."}],  # "Purple flowers", "White flowers"
 "ratio_template": "...",                       # slot {ratio}, printed to 2 dp
 "no_recessive_template": "...",                # slot {total} — used when the tally has zero white
 "notes": {"one_pure_dominant": "...",          # ⚠️ ORDERED — see the precedence note
           "both_pure_recessive": "...",
           "both_carriers": "...",
           "mixed": "..."},
 "progress": {"none": "...", "suffix_one": "...", "suffix_many": "..."}}
```

**Dominant/recessive are never named as terms.** The page says "overrides" and "hidden" throughout —
NOTES flag 13 records this as deliberate and holds it back to GCSE. There is no `dominant_term` key
and there must not be one; the *letters* P and p carry it. `phenotypes` maps the two outcomes to
their colour words, which is as far as the vocabulary goes.

### 5.1 The randomness is real, unseeded, and must stay that way

```js
const g1 = a[Math.floor(Math.random() * 2)];
const g2 = b[Math.floor(Math.random() * 2)];
```

One `Math.random()` **per gamete, per parent, per seed**. Measured across all five pages: this is
the only `Math.random()` in B10, and there is no PRNG, no seed, and no seed key anywhere.

**There is no `seed` key in this payload and there must not be one.** B11 is deliberately
all-deterministic; b10-04 is the exception and the reason is the lesson itself. A 3:1 ratio is a
*sampling* result, not a property of any one litter. A seeded bench would deliver 75/25 on cue,
which would teach precisely the misconception the page's own legal line and rung 4 criterion 4 are
written to break ("a small litter may not show the ratio at all, so the prediction is about large
numbers"). The hundred-seed button exists because the one-seed button is not enough, and that only
lands if one seed is genuinely unpredictable.

Two consequences to carry into the build:
- **b10-04's bench is not screenshot-reproducible.** Any parity or render gate must compare the
  chassis and the controls, never the tally numbers, the percentages or the ratio line.
- **Growing a hundred hides the most-recent-seed card** (`last: n === 1 ? last : null`). Measured.
  The single-seed card is the "chance decides each one" story; the hundred-seed run is the
  "only totals show the pattern" story, and they are deliberately never on screen together.

### 5.2 The four notes are ORDERED, and the order is load-bearing

Design evaluates them as an if/else chain, so the first match wins. Author them in this order and
have the renderer test in this order:

1. `one_pure_dominant` — *neither parent can contribute two p* **and** at least one parent is `PP`.
   Every seed is purple however many are grown.
2. `both_pure_recessive` — both parents `pp`. All white, every time.
3. `both_carriers` — both parents `Pp`. This is Mendel's 3:1 and the note says so.
4. `mixed` — everything else (one homozygote × one heterozygote, where the homozygote is `pp`).

Reversing 1 and 2 would be harmless; moving 3 above 1 would not be, because `Pp × Pp` must never
fall through to the generic `mixed` line. Test in the order given.

### 5.3 State and controls

| State | Owner | Controls |
|---|---|---|
| `mum`, `dad` — genotype ids | runtime, opens on `start` | three genotype buttons per parent (six total) |
| `tally` — `{dominant: int, recessive: int}` | runtime | `one_label` (+1 seed), `many_label` (+100 seeds), `reset_label` |
| `last` — `{g1, g2, phenotype}` or null | runtime | set by `one_label`; **cleared by `many_label`** |

⚠️ **Changing either parent's genotype clears the tally and the last seed.** Measured
(`onClick: () => this.setState({ [p.which]: g.id, tally: {purple: 0, white: 0}, last: null })`).
Load-bearing: a student cannot accumulate counts across two different crosses, which would produce a
meaningless ratio. Wire the clear or the instrument silently lies.

`start` is `{parent1: "Pp", parent2: "Pp"}` — the *second* entry in `genotypes`, not the first.
Deliberate: the bench opens on the only cross that produces the 3:1, so the headline result is one
button-press away, and the student has to change something to discover the other cases.

The genotype written on the last-seed card is **always normalised to dominant-first**: a seed that
received `p` then `P` is printed `Pp`, never `pP`. Measured. Carry the normalisation.

---

## 6. `species-cases` — b10-05 `#s-bench`

```python
{"kind": "species-cases", "id": "...", "segment": "practical",
 "verdicts": [{"id": "...", "text": "..."}],    # THREE, ordered; letters A/B/C are derived
 "options_label": "...",                        # "The pair" — above the seven tabs
 "commit_label": "...",                         # "Same species?" — above the three verdicts
 "cases": [{"id": "...", "label": "...",        # label = tab text
            "title": "...", "facts": "...",
            "answer": "<verdict-id>", "why": "..."}],                 # seven
 "run_label": "...", "run_done_label": "...",   # "Check it" / "Settled"
 "verdict_tags": {"right": "...", "wrong": "..."},
 "progress_suffix": "...",                      # "settled", as in "3 of 7 settled"
 "tally": {"all": "...", "remaining_suffix": "..."}}
```

### 6.1 Three verdicts, not two

`VERDICTS`, in order, verbatim: `same` → "Same species"; `different` → "Different species";
`unclear` → **"The test does not settle it"**.

The third is the instrument. It is not a hedge and it is not an "I don't know" — it is the correct
answer for three of the seven cases, and a student who never selects it cannot score above 4/7.
**`verdicts` must stay a three-entry ordered list**, because the A/B/C letters are derived from
position and because dropping to a boolean would delete the lesson.

### 6.2 All seven cases with their verdicts — measured

| # | `id` | `label` | `answer` |
|---|---|---|---|
| 1 | `dogs` | Dane and chihuahua | `same` |
| 2 | `mule` | Horse and donkey | `different` |
| 3 | `liger` | Lion and tiger | `different` |
| 4 | `pipistrelle` | Two pipistrelles | `different` |
| 5 | `bacteria` | Two bacteria | **`unclear`** |
| 6 | `dandelion` | Two dandelions | **`unclear`** |
| 7 | `gulls` | A ring of gulls | **`unclear`** |

One `same`, three `different`, three `unclear`. The three that land on the third verdict are exactly
the three NOTES §1.5 names — bacteria, dandelions, ring species. ✅ Page and NOTES agree here.

The bench lead tells the student to "read the last two carefully", and the case order is authored,
not sorted: the three `unclear` cases are last and consecutive, so the instrument spends its first
four cases establishing the test and its last three showing where it runs out. **Keep the order.**

### 6.3 State and controls

| State | Owner | Controls |
|---|---|---|
| `caseId` | runtime, opens on `cases[0]` (`dogs`, so no `start` key) | seven case tabs |
| `picks` — `{caseId: verdictId}` | runtime | three verdict buttons — **locked once that case is opened** |
| `opened` — `{caseId: true}` | runtime, sticky per case | `run_label` button, disabled until a pick exists and after opening |

Commit-then-reveal, per case: a verdict must be chosen before `run_label` enables, and once pressed
the pick is frozen and the unchosen verdicts drop to 50% opacity. Same gate as `variation-plotter`,
and the same reason.

---

## 7. The chassis blocks, measured on all five pages

Not activity kinds, but recorded because §0.2 exists — do not guess a shell from a name.

| Anchor | Class attribute, measured | What it is |
|---|---|---|
| `#s-hook` | `ks3-block ks3-dark ks3-hook` | Hook chassis. Four `.ks3-option` buttons with `aria-pressed`, then an ungated `.ks3-reveal`. **No option is correct** — any choice reveals the same paragraph. |
| `#s-bench` | `ks3-block ks3-dark ks3-practical` | The flagship. `segment: "practical"` on all five. |
| *(band)* | **no `class` attribute at all** — inline-styled `<section id="…" style="margin: 28px 0 0; … background: var(--ks3-band); border: 3px solid var(--ks3-ink); …">` | Cards + KEY FACT band. **Not an `ACTIVITY_SHELLS` block.** See §8. |
| `#s-think` | `ks3-block ks3-misconception` | Two quotes and two prose paragraphs. **Entirely static.** → `confrontation`, `segment: "misconception"`. See §9. |
| `#s-ladder` | `ks3-ladder` | Four rungs — two page-marked MCQs, two self-marked with five criteria each. Identical structure on all five pages. |
| `#s-keynote` | `ks3-block ks3-dark ks3-keynote` | One paragraph. Static. |

The band anchor differs per lesson and its card shape differs with it — two chassis, not one:

| Lesson | Band anchor | Card shape |
|---|---|---|
| b10-01 | `s-two` | grid, `{kind, name, body, eg}` × 4 |
| b10-02 | `s-model` | grid, `{kind, name, body}` × 4 |
| b10-03 | `s-who` | ordered list with an initials badge, `{initials, name, role, body}` × 4 |
| b10-04 | `s-steps` | ordered list with a number badge, `{num, name, body}` × 4 |
| b10-05 | `s-test` | grid, `{kind, name, body}` × 4 |

## 8. Rail stops: four are drawn, and FOUR is what we build (MRB-249)

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



Every page draws **four** rail stops. `doneByDom()` in `shared/ks3.js` reads, in order:
`data-stage-done` (authoritative in both directions), then `.ks3-rung` completion, then
`[data-reveal]:not([hidden])` / `.ks3-reveal-btn[aria-expanded="true"]`, then any
`.ks3-option[aria-pressed="true"]`.

| Stop | b10-01 | b10-02 | b10-03 | b10-04 | b10-05 | Can it tick? |
|---|---|---|---|---|---|---|
| 1 | `s-hook` | `s-hook` | `s-hook` | `s-hook` | `s-hook` | ✅ — four `.ks3-option[aria-pressed]` |
| 2 | `s-bench` | `s-bench` | `s-bench` | `s-bench` | `s-bench` | ✅ — the activity emits `data-stage-done` |
| 3 | `s-two` | `s-model` | `s-who` | `s-steps` | `s-test` | ❌ **never** |
| 4 | `s-ladder` | `s-ladder` | `s-ladder` | `s-ladder` | `s-ladder` | ✅ — `.ks3-rung` |

**Stop 3 is B7's defect repeated on all five pages.** The band section is static markup: no
`.ks3-option`, no `.ks3-rung`, no `[data-ticks]`, no `[data-reveal]`, no `.ks3-reveal-btn`. Every
clause of `doneByDom()` falls through and it returns `false` forever. Design's own `isDone()` gets
around this by reading the *bench's* state for the band stop — `n >= 3` plotted (b10-01),
`shown >= 6` (b10-02), `solved` (b10-03), `>= 20` seeds (b10-04), `>= 5` cases opened (b10-05) —
i.e. Design deliberately mirrors stop 2 into stop 3. `doneByDom()` cannot read across blocks, so it
cannot reproduce that.

⛔ **REVERSED by MRB-249. The paragraph below is kept, marked, and is NOT what to build.** It read:
*"Draw three stops per page, not four — hook, bench, ladder — which is what B7 landed on for the
same reason. Twenty stops across five lessons, all twenty of which can tick. The alternative
(emitting a mirrored `data-stage-done` on a static band) invents a completion signal for a section
the student cannot complete."* Every clause of that is about the runtime, and none of it was ever a
reason to drop a stop Design drew. `mirrors` is now resolved in `wireRail`'s `paint()` at rail
level — where Design resolves it — so the band stop ticks the moment its target does, and nothing
is invented: the completion signal is the instrument's own.

**AUTHOR FOUR STOPS PER PAGE. TWENTY ACROSS THE UNIT.** The third is a mirror, exactly as B9's
shipped:

    {"anchor": "s-two", "short": "TWO", "label": "…",
     "mirrors": "s-bench", "done_when": "<the bench's own condition>"},

Per lesson the mirror's anchor and `done_when` are: b10-01 `s-two` / three plotted · b10-02
`s-model` / all six levels shown · b10-03 `s-who` / solved · b10-04 `s-steps` / twenty seeds ·
b10-05 `s-test` / five cases opened. Those are Design's own `isDone()` thresholds, recorded in the
paragraph above this one.

`ks3_parity.check_rail_matches_design` gates the built rail against `docs/ks3/rail-manifest.md`,
which is generated from Design's delivered pages — so a rail of three now FAILS THE BUILD naming
the page. Thirty-five pages shipped with a stop missing before that gate existed.

The NOTES are right and this section was wrong: NOTES §3's "Rail stops: four in all five lessons"
is true of what Design drew and true of what we build.

## 9. `#s-think` is `confrontation`, not `predict` — on all five pages

Contract §2 R1 turns on whether the block asks for a commitment. Measured on all five B10 pages:
`#s-think` contains a `.ks3-mis-quote`, a paragraph, a rule, a second `.ks3-mis-quote` and a second
paragraph. **No options. No commit. No gated reveal. No `sc-if` of any kind.** It is B1's case
exactly, so it is `confrontation` with `segment: "misconception"`, it emits no `data-stage-done`,
and it is not a rail stop on any B10 page — which the rails independently confirm, since none of
the five lists `s-think`.

`confrontation` is already registered in `ACTIVITY_KIND_RENDERERS`; no new kind is needed for it.

## 10. Where Design's page and `NOTES-B10.md` disagree

1. **The six zoom levels do not end where the NOTES say.** NOTES §1.2 describes "six nested levels
   from a person to a base pair", and the dispatch brief repeats it as
   person→cell→nucleus→chromosome→**DNA**→**base pair**. The page draws
   person→cell→nucleus→chromosome→**a gene**→**the bases**. Level 5 is a gene, not DNA; level 6 is
   the bases, not a base pair. The page is internally consistent with its own choice — its bottom-out
   paragraph reads "the last four are all the same molecule seen at different magnifications" — and
   the page wins on measurement. **Author `A gene` and `The bases`.** The NOTES line is the one that
   is wrong.
2. **The thousandfold claim is not supported by the figures the page prints.** NOTES §1.2 and the
   page's own bench lead both assert a ~1000× drop per step; the printed scales give ~10⁵, ~3×, ~3×,
   (no figure), ~7000×. This is a **copy/science finding for Mide** (it sits alongside NOTES flag 5,
   which asks him to confirm the figures but not the claim about them). Do not silently change
   either the figures or the sentence — lift both byte-identical and raise the contradiction.
3. **"Rail stops: four in all five lessons" (NOTES §3) is true as drawn and unachievable as built.**
   See §8. Three per page.
4. **b10-02's bench eyebrow says "zoom in five times" over a six-level panel.** Consistent
   arithmetic (six levels, five presses, and the progress line reads "all six levels"), but the two
   numbers sit four lines apart and read as a contradiction. Lift as drawn; noted so it is not
   "corrected" into an error by a later pass.
5. **NOTES §1.5's "bench marking follows the house rule" understates what three benches do.** See
   §0.6 — b10-01, b10-03 and b10-05 all adjudicate a student commitment on the bench, which B7 §0.6
   forbade. Ship as drawn, recorded as a deviation.

## 11. `figures`

**`figures: []` on all five, and that is deliberate, not an omission.** Verified by grep across all
five pages: zero `<img>`, zero `<figure>`, zero `<picture>`, and no placeholder. Every `<svg>` on
every page is chassis — the brand chevron, the rail tick, the ladder tick/cross marks, the endmatter
arrows. Not one is content.

NOTES flag 19 names the two obvious candidates and neither is in the diagram manifest: a
chromosome-to-DNA nesting figure, and Photo 51 itself. §4.10 allows an empty `figures` for a lesson
carried by its interactives, and b10-02's `zoom-bench` is precisely a nesting figure built out of
DOM, so the first candidate is arguably already answered.

⚠️ **Photo 51 is a specific historical photograph with rights attached.** If it is wanted, that is a
licensing decision and Mide's, not a commissioning one, and not one this build can take by drawing
something similar. **Do not invent a figure slot to fill the gap, and do not drop the flag.**

## 12. Misconception ids — pre-allocated, do not improvise

`NOTES-B10 §4` opens the `GENE` family with ten entries, `GENE-01` to `GENE-10`, two per lesson.
Mapped against the two beliefs each page's `#s-think` actually confronts:

| Lesson | Entries | The two beliefs, in page order |
|---|---|---|
| b10-01 | `GENE-01`, `GENE-02` | continuous = environmental / discontinuous = genetic · "if you can measure it with a ruler it is continuous" |
| b10-02 | `GENE-03`, `GENE-04` | chromosomes, genes and DNA are three different things · only the cells that need a gene contain it |
| b10-03 | `GENE-05`, **`NOS-03`** ⊕ | "Watson and Crick discovered DNA" · "a great discovery is one person's flash of insight" |
| b10-04 | `GENE-07`, `GENE-08` | characteristics blend · "it skipped a generation, so the gene disappeared and came back" |
| b10-05 | `GENE-09`, `GENE-10` | organisms that look alike are the same species · "if two animals can have a baby, they are the same species" |

⊕ **SPARES ARE PRE-ALLOCATED, 18 Aug 2026 — reversing the line below on Mide's instruction that
the range be fixed per lesson, with a named spare, BEFORE parallel authors are dispatched.**

| Lesson | Entries | Spare |
|---|---|---|
| b10-01 | `GENE-01`, `GENE-02` | `GENE-11` |
| b10-02 | `GENE-03`, `GENE-04` | `GENE-12` |
| b10-03 | `GENE-05`, `GENE-06` | `GENE-13` |
| b10-04 | `GENE-07`, `GENE-08` | `GENE-14` |
| b10-05 | `GENE-09`, `GENE-10` | `GENE-15` |

The reason is concurrency, not generosity. Five authors work five files at once and none of them
can see the others; an author who finds a third belief and has to "mint a new id at that point"
mints it from the same next-free number as everyone else, and two different beliefs arrive holding
`GENE-11`. Ids are permanent, so that collision cannot be tidied afterwards — one of the two
beliefs would have to be renumbered in a register that has already promised the number is fixed.
A pre-allocated spare per lesson makes the collision impossible.

An unclaimed spare stays **permanently unused**, exactly like `DRUG-07` and
`REPRO-17`/`20`/`21`/`23`. That is the cost, it is nil, and it is much smaller than the cost of the
collision it prevents. Never re-point a spare at a different belief.

⛔ The line this replaces, kept per §12: *"No spare is minted. B7 pre-allocated one spare per lesson
(`PLANT-09`…`PLANT-12`) and B10 does not, so a pass that finds a sixth belief must mint a new id at
that point and record it — it must not re-point one of the ten."* The instruction to mint on the
spot is what changed; the prohibition on re-pointing has not.

⊕ **RULED 18 Aug 2026 — `GENE-06` IS A PERMANENT GAP. b10-03's second belief is `NOS-03`.**

This section was wrong and it is mine, so it is the one that gets corrected. It pre-allocated
`GENE-06` to *"a great discovery is one person's flash of insight"* and said that if a `NOS` family
were ever opened, this would be the first entry that should move. The family had ALREADY been
opened — `docs/ks3/misconception-register.md`'s `NOS` section, written 17 Aug 2026, records that
belief as `NOS-03` and lists `GENE-06` among the numbers that must never be issued. This section is
dated a day later and contradicted it, and it was about to hand the contradiction to five parallel
authors who cannot see each other.

The ruling is not a new decision; it is the third application of one this repo already made twice:

| unit-family id | becomes | status of the unit id |
|---|---|---|
| `ECO-12` | `NOS-04` — minted 18 Aug by b9-06 | permanent gap |
| `REACT-18` | `NOS-06` — reserved | permanent gap |
| **`GENE-06`** | **`NOS-03`** — minted by b10-03 | **permanent gap** |

A nature-of-science belief lives in `NOS`. That is what the family is for, and it is the whole
reason it was opened. The unit-family number is not reissued to anything else, ever — it is a gap
in the same class as `DRUG-07` and `REPRO-17`/`20`/`21`/`23`.

**What the b10-03 author authors: `GENE-05` and `NOS-03`.** An id from another family in a lesson's
`misconceptions` list is normal and already shipped — `ks3_data/b9/lesson_06_sampling_an_ecosystem.py`
carries `ECO-11` and `NOS-04` together, and its own docstring explains why `ECO-12` does not exist.
Follow that file.

**The spare is unaffected: b10-03's spare is still `GENE-13`.**

⚠️ A standing note that came out of this, worth more than the ruling itself: `NOTES-B10 §4` states
its entries were "written into `docs/ks3/misconception-register.md` with a new prefix row". They
were not. `NOTES-B11 §4` says the same of `EVOL` and it was not either, and `NOTES-B5` and
`NOTES-B7` said it before them. **Read a delivery's §4 as an allocation PROPOSAL and check the
register itself.** Four occurrences is a pattern, not four slips.

`confronted_by` and `elicited_by` **must name an element on that lesson's own page** — an activity
`id` or a block `anchor` the page actually emits. Gated under MRB-244 and resolved against the BUILT
page, so a name that renders to nothing fails the build. B10's available section anchors:

| Lesson | Anchors |
|---|---|
| all five | `s-hook`, `s-bench`, `s-think`, `s-ladder`, `s-keynote` |
| b10-01 | + `s-two` |
| b10-02 | + `s-model` |
| b10-03 | + `s-who` |
| b10-04 | + `s-steps` |
| b10-05 | + `s-test` |

## 13. KEY FACT copy — verbatim, one per lesson

Each sits in the band section, in the `5px 5px` accent-shadow box. Contract §2 R3 stands: the
shipped `shared/ks3.css` figures win over Design's per-page `6px 6px` / 25px / `22px 26px` drift.
The copy below is lifted byte-identical and is not to be edited.

**b10-01 · `#s-two`**
> Continuous variation has intermediate values and is plotted as a histogram; discontinuous variation falls into separate groups and is plotted as a bar chart. Whether variation is continuous is a question about the data. What caused it — genes, environment or both — is a separate question with a separate answer.

**b10-02 · `#s-model`**
> DNA is a long molecule found in the nucleus. It is coiled into chromosomes — 46 in a human body cell, in 23 pairs. A gene is a section of DNA carrying the instruction for one characteristic, and the instruction is written in a sequence of four bases.

**b10-03 · `#s-who`**
> DNA is a double helix: two strands twisted round each other, with the bases paired on the inside — A always with T, C always with G. The structure was deduced in 1953 from X-ray diffraction images taken by Rosalind Franklin and Maurice Wilkins, and from Erwin Chargaff's base ratios, by James Watson and Francis Crick.

**b10-04 · `#s-steps`**
> Heredity is the transfer of genetic information from parents to offspring. Each parent passes half their chromosomes in a gamete, so offspring carry two versions of every gene, one from each parent. Versions are not blended: one may be hidden for generations and still be passed on unchanged.

**b10-05 · `#s-test`**
> Two organisms belong to the same species if they can breed together to produce fertile offspring. Members of a species vary enormously in appearance; organisms of different species may look almost identical. Appearance is a clue, not the test.

## 14. Kind roster — five new, one reused

Checked against all currently registered names in `ACTIVITY_KIND_RENDERERS` (`build_ks3.py`). All
five proposed names are free; the near misses are listed so nobody merges them later.

| Lesson | Anchor | `kind` | `segment` | New? | Nearest existing name — do not merge |
|---|---|---|---|---|---|
| b10-01 | `s-bench` | `variation-plotter` | `practical` | new | — |
| b10-02 | `s-bench` | `zoom-bench` | `practical` | new | `zoom-ladder`, `scale-zoom` |
| b10-03 | `s-bench` | `model-builder` | `practical` | new | `model-limit`, `model-timeline`, `fold-builder`, `formula-builder` |
| b10-04 | `s-bench` | `pea-cross` | `practical` | new | `crossing-bench`, `crossing-counter`, `crosses-panel` |
| b10-05 | `s-bench` | `species-cases` | `practical` | new | `clinic-cases`, `removal-cases`, `verdict-cards` |
| all five | `s-think` | `confrontation` | `misconception` | **reused** | — |

Six activity records per page is wrong; it is **two** — the flagship and the confrontation — plus
the hook, band, ladder and keynote chassis. Ten activity records for the unit.

## 15. Tweak props

`showDraft` on all five, and nothing else — measured from the `data-props` attribute on each page's
`<script data-dc-script>`, which carries only `$preview` and `showDraft`. NOTES §3 names
`startCharacteristic` (b10-01) and preset parent genotypes (b10-04) as the natural second tweaks;
neither is drawn. **Do not add them.** Note that the b10-04 one would collide with the `start` key
in §5 if it were ever added, and the `start` key wins — it is content, not a tweak.

---

## 16. Science rulings — the three NOTES flags the delivery held for an answer ⊕

`docs/ks3/design-reference/b10/README.txt` names three flags as needing an answer before publish.
All three are ruled here, 18 Aug 2026, under this run's standing authority over KS3 science. **No
lesson waits on them and no author re-opens them.** All three come out as *ship as drawn*, which is
the point of writing them down: an unanswered flag stops a build, and an answered one that nobody
recorded stops the next one.

### Flag 9 — the credit note on Photo 51 (b10-03, `ks3-support` layer). SHIP AS DRAWN.

Every fact in it is right, and I checked each one rather than the passage as a whole: Raymond
Gosling took Photo 51 working under Franklin at King's; Wilkins showed it to Watson without her
knowledge; Franklin's unpublished MRC report reached Crick through the MRC Biophysics Committee; the
1953 *Nature* paper acknowledged only having been *"stimulated by a knowledge of the general nature
of the unpublished experimental results and ideas"* of the King's group; Franklin died in 1958, aged
37; the prize was 1962 and a Nobel cannot be awarded posthumously.

The treatment is also right, and the reason is worth stating because it is the part a later pass
would be tempted to "improve". The statutory point names Watson, Crick, Wilkins **and** Franklin, so
the history is statutory content rather than enrichment — it has to be taught, and taught
accurately. Design's passage does that, says historians still disagree about interpretation, and
names no villain. It specifically does **not** claim Franklin was denied the prize because of the
credit dispute; she was ineligible because she had died. That distinction is the single most
important sentence in the passage and it is already correct. Do not sharpen it into a grievance and
do not soften it into a coincidence.

⚠️ One observation that is NOT a science point and is Mide's if he wants it: `ks3-support` is the
*"Need a hand?"* layer, which is scaffolding for a student who is stuck. A credit note is neither
scaffolding nor stretch. Design drew it there and MRB-205 says the page wins, so it ships there.
Recorded as a layer-semantics question, not a blocker.

### Flag 10 — a values judgement in a marked rung (b10-03 rung 4). SHIP AS DRAWN, with a check.

The statutory clause is *"the part played by"* the four scientists. A rung that asks a student to
write a fairer acknowledgement is assessing whether they can attribute contributions accurately,
which is exactly that clause. It is not marking their values.

**The criteria are what make that true, so the b10-03 author must verify them rather than assume
them:** every criterion must reward accuracy of attribution — who did what, what was published, what
was not — and none may reward arriving at a particular moral conclusion. NOTES §2 flag 10 says the
criteria "explicitly reward *not* treating it as heroes and villains", which is a rule about
reasoning rather than about a verdict, and that is the right side of the line. If any criterion
turns out to reward a stance instead of a fact, report it and do not ship that criterion.

### Flag 13 — hold "dominant" and "recessive" back to GCSE (b10-04). CONFIRMED. HOLD THEM BACK.

The KS3 programme of study asks for heredity as the process by which genetic information is
transmitted between generations. It does not name dominant or recessive; those are GCSE vocabulary.
Design's lesson says *"overrides"* and *"hidden"* and names neither term. That is correct and it
stays.

The test that matters is not whether the words are absent but whether anything taught here becomes
**wrong** later, and nothing does. "Hidden" is a true description of an allele that is present and
not expressed. "Overrides" is a true description of the relationship. What would break is calling
the hidden version *weaker*, *lost* or *used up* — and that is precisely the belief `GENE-08`
confronts on this page (*"it skipped a generation, so the gene disappeared and came back"*), so the
lesson already argues against its own worst failure mode. P/p, clean dominance and a 3:1 expectation
are standard and correct for Mendel's peas at this level.

**Do not introduce either term as a synonym "for later", not even in a support layer.** A term
introduced without the machinery to use it is a word to be memorised, and the whole reason to hold
it back is that at GCSE it arrives attached to genotypes, gametes and Punnett squares that this
lesson deliberately does not have.

⊕ **The wording above is tightened, 18 Aug 2026, because the b10-04 author measured the page
against it and found it too absolute.** This ruling first said the lesson "names neither term". It
does not literally: `convention_note` says *"a clean dominance rule"* twice, and the *At GCSE this
becomes* card reads *"Alleles, dominant and recessive…"*. Both ship, and a later pass reading the
old phrasing against the page would have reported a defect that is not one.

The real test is not whether the string appears. It is **whether the term is TAUGHT or MARKED**:

| where it appears | verdict | why |
|---|---|---|
| a chip, a bench label, a ladder option, a correction, a criterion | ⛔ **never** | that is teaching it, or marking a student on it |
| `ks4_becomes` — *"At GCSE this becomes"* | ✅ correct, and the opposite of a leak | naming what arrives later is that card's entire job; a student is told the word exists and is not asked to use it |
| `convention_note` — describing the MODEL's scope | ✅ allowed | metalanguage about the simplification, not vocabulary the student is asked to hold. It is the honest admission that peas are tidier than people |

What must stay true either way is the thing the whole ruling protects: nothing taught here becomes
wrong at GCSE. Never describe the hidden version as weaker, lost or used up.

### The histogram's bars TOUCH. Ruled 18 Aug 2026, and it overrides Design's measured pixels.

The engine pass found b10-01's chart row carrying `gap: 4px` on top of the derived bar width, so
continuous bars stood 4px apart — while the same page's axis caption reads *"bars touch because the
categories are ranges"* and its verdict line reads *"a histogram, bars touching"*. It set the row
gap to 0 and flagged it as its one deviation from Design's measurement. **The deviation is correct
and it is confirmed.**

"Follow the page" has no answer here, because the page contradicts itself: its pixels say one thing
and two of its own sentences say the other. When a page disagrees with itself, the tie is broken by
the science, and the science is not ambiguous. **Touching bars are what make a histogram a
histogram.** The gap between bars is the notation for a gap between categories, and continuous data
has none — that is the entire distinction this lesson exists to teach, and it is the distinction
`GENE-01` gets wrong. A four-pixel gap on the continuous chart teaches the discontinuous case in the
one place a student is looking for the difference.

So separation now comes from exactly one place, which is the place schema §2 allows: continuous
bars meet at 0px, discontinuous bars stand at 6px. Both are asserted on painted geometry rather than
on the stylesheet, so a future change to either has to argue with a gate.

This is a rendering correction, not a copy change: Design's caption and verdict are lifted
byte-identical and are now true of the drawing beside them.

### Flags 8, 11, 12, 14, 15, 16 — checked, correct, ship as drawn.

Not in the README's list of three, checked anyway because they are science and this run rules it.
The Pauling triple-helix card earns its place: a wrong model that was useful evidence is a true and
unusually valuable thing to teach. Miescher 1869 and Avery–MacLeod–McCarty 1944 are correct and at
the right depth. Meselson and Stahl paraphrased rather than quoted is the better choice for this
age. Mendel's figures are right. Horse 64 / donkey 62 / mule 63 is right, and "almost always
infertile" with fertile female mules in the legal line is the honest form of it. The pipistrelle
split is real and was recognised on echolocation frequency in the 1990s.
