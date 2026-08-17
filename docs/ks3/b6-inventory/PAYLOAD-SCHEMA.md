# B6 — Health and drugs · instrument payload schema

**What this is.** The contract between the three lesson authors and the B6 engine pass (MRB-244).
One section per instrument kind. Every key below is a key the renderer in `build_ks3.py` actually
reads; keys marked **required** raise a `ValueError` at build time when missing, and the build is
red. Nothing here is aspirational — if the renderer stops reading a key, this file changes with it.

**Source of truth for the copy.** `KS3 B6 lessons/b6-0N-*.dc.html`, Design's approved delivery.
Every string quoted below is lifted from those files verbatim. **Never retype a science-bearing
string** — `node tools/extract_design_payload.js <page> [CONST...]` extracts the constants, and the
static markup prose is in the page body.

**⚠️ Tone is a gate on this unit, and it reaches into the engine.** Clinical, no scare copy, no
euphemism, and **no doses, thresholds or methods anywhere** — NOTES-B6 §1, and it is a safeguarding
property of the pages rather than a register preference. No renderer in this unit computes,
formats, rounds or scales a quantity of any substance. The single instrument that counts anything
counts **hours of waiting**. If an engine change in this section finds itself writing a
number-formatting helper, that is the signal to stop and ask.

Two items are settled and must not be re-opened by any pass: **the vape paragraph (flag 9) ships
exactly as written**, and **paracetamol's "may feel fine for a day or two" (flag 4) stays**.

**Where the instrument lives.** All three B6 instruments sit on a `practical` segment
(`<section class="ks3-block ks3-dark ks3-practical">`) — measured off Design's own markup on all
three pages, no exceptions. That means **every one of them is on ink**, and the stylesheet scopes
its colour rules `.ks3-dark …` accordingly. Nothing in this file changes on a light ground because
nothing in B6 is on one.

**No figures.** NOTES-B6 flag 14: the unit names no diagram slots and draws none. Its visuals are
the three instruments, which is why their internal geometry is described here rather than treated
as decoration.

---

## 0 · Keys the SHELL reads, not the instrument

These sit on the same activity record, beside `kind`, and are read by `r_activity` before your
renderer runs. They are listed here because the authors have to supply them and they are easy to
miss; they are not part of any instrument's own payload.

| Key | Type | Req | Drives |
|---|---|---|---|
| `kind` | str | **yes** | the dispatch key — one of the three names in §1–§3 |
| `eyebrow` | str | no | the block's eyebrow. All three B6 blocks author one (e.g. `At the bench · one dose, one bloodstream`); without it the shell prints its fixed `Investigate` |
| `heading` | str | no | the block `<h2>` (e.g. `Follow the dose`) |
| `prompt` | str | no | the lede paragraph under the head row |
| `head_counter` | dict | no | the right-aligned mono progress readout on the head row, as a **count**. Shapes below |
| `progress` | dict | no | the same readout as a **named state**. ⊕ new in MRB-244. See below |

`ground` is **not** authored on any B6 instrument block: the `practical` shell is already ink.

### `head_counter`, and the ⊕ `full` key added for this unit

Four shapes, one element, one JS updater:

| Key | Type | Drives |
|---|---|---|
| `format` | str | the count template. `{n}` = the live count, `{total}` = `total` |
| `total` | int | the denominator, and the clamp |
| `zero` | str | **opt-in.** A bespoke sentence at `n = 0`, replacing `0 of 5` |
| `full` | str | **opt-in, ⊕ new in MRB-244.** A bespoke sentence at `n ≥ total` |
| `off` / `on` | str | the two-state form, used instead of `format` |

**`full` is the mirror of `zero` and it was added for b6-01.** Design's readout on that page has
*three* states — `not started` → `stage 3 of 5` → **`all five stages`** — and without `full` the end
of the journey reads `stage 5 of 5`, which says the student is standing on the last stage rather
than that the dose has been followed all the way round. b6-01 currently authors `zero` and not
`full`; adding `"full": "all five stages"` completes Design's drawn readout. Nothing else in the key
stage authors it and no shipped counter moves.

### ⊕ `progress` — the head-row readout as a named state

```python
progress = {"idle": "clock not started", "running": "clock running",
            "clear": "cleared"}
```

A map of state name → label, ≥ 2 entries, rendering the **same paragraph** `head_counter` does.
The block opens on the **first state in the authored order**, so the order is preserved rather
than sorted — an instrument's resting state is the one an author writes first. State names become
`data-state-<name>` attributes and must be lower-case and start with a letter. Authoring both
`progress` and `head_counter` on one activity **raises**: one of them would render and the other
would vanish without a trace.

b6-02 authors it because its readout is not a tally in any shape: three sentences, no number in
any of them, and the transitions decided by two independent facts (has the clock been run, is the
blood clear) rather than by one counter crossing a line.

**⚠️ `progress` is also an INSTRUMENT-owned key on three older kinds** — `fifa-pick`,
`lever-steps` and `random-walk-bench` each read their own and draw their own readout inside their
own component. The shell only takes `progress` when the kind's renderer does **not** consume it,
derived the same way `_KIND_FN_OWNS_OPTIONS` is. So an instrument that starts reading `progress`
tomorrow takes it back from the head row the moment it does, with nobody updating a list.

### ⊕ `support_heading` — a LESSON key, not an activity key

| Key | Type | Req | Drives |
|---|---|---|---|
| `support_heading` | str | no, default `Need a hand?` | the eyebrow on the `ks3-layer ks3-support` block |

**B6 is the first unit in KS3 with a non-empty `support[]`**, so this heading has never rendered on
a page before. The fixed fallback — *Need a hand?* — is a **study-support** offer, the right words
above a hint for a student stuck on the science. All three B6 support layers are **referral**
blocks, and Design heads them *"If any of this is about you or someone you know"*. Left
hard-coded, a page about somebody's drug use would have offered help with the homework, and the
student the block was written for would not have recognised it as addressed to them.

Shaped exactly like `connects_heading` on the end-matter: the lesson's own string when it declares
one, the fixed label when it does not. All 35 shipped lessons ship `"support": []` and render
nothing at all, so every one of them is byte-identical across the change.

---

## 1 · `route-tracer` — b6-01 `#s-dose`

Four drugs, one route, five stages taken one at a time, and a closing panel that is a consequence
rather than a list.

**⚖️ Stage 3 is the instrument.** *Once round the whole body* is the stage that kills `DRUG-02` —
the belief that a painkiller travels to the part that hurts — and NOTES-B6 §2.1 says so in as many
words: *"do not let a future revision collapse stages 2 and 3 to save space."* Stage 2 says the
molecule is dissolved in plasma with no address on it; stage 3 says every organ is offered it
anyway. Merged, what remains is a fact about blood rather than an argument about side effects, and
stage 5 stops being a consequence. **The renderer accepts exactly five stages and raises on any
other number**, and the parity drive re-checks in a browser that rows 2 and 3 are not the same row
twice. Neither can read prose; both make the collapse a red build rather than an edit nobody
notices.

**⚖️ Only two of the five stages belong to the drug, and that is the argument.** Stage 1 is the
drug's own `entry` and stage 4 its own `target`; stages 2, 3 and 5 are the *same sentences* for
caffeine, paracetamol, nicotine and alcohol, because the middle of the journey does not depend on
which molecule is making it. A student who tabs between four drugs and watches the two ends change
while the middle stays word-for-word identical has been shown the generalisation rather than told
it. `body_from` is what keeps that sharing **declared** rather than incidental.

**Shell keys for this block**

```python
eyebrow      = "At the bench · one dose, one bloodstream"
heading      = "Follow the dose"
prompt       = ("Pick a drug and follow one dose of it, one step at a time. Watch step 3 "
                "carefully — it is the step everyone skips, and it is the reason side "
                "effects exist at all.")
head_counter = {"format": "stage {n} of {total}", "total": 5,
                "zero": "not started", "full": "all five stages"}
```

**Instrument payload**

| Key | Type | Req | Drives |
|---|---|---|---|
| `drugs` | list of dict | **yes**, ≥ 2 | one tab per drug, in the drawn order. Raises below 2 — there would be nothing to tab between and nothing held constant |
| `drugs[].id` | str | **yes** | the key the tab, the stage list and the closing panel are matched on. Raises if duplicated: two drugs' text would show at once |
| `drugs[].label` | str | **yes** | the tab caption (`Caffeine`) |
| `drugs[].name` | str | **yes** | the panel's headline (`Alcohol (ethanol)`) — **not** the same string as `label` on every drug |
| `drugs[].klass` | str | **yes** | the alert mono line beside the name (`Stimulant`, `Depressant`, `Stimulant, strongly addictive`) |
| `drugs[].where` | str (rich) | **yes** | the muted line under the name — where the drug is met and its legal position |
| `drugs[].entry` | str (rich) | see note | stage 1's body, via `body_from` |
| `drugs[].target` | str (rich) | see note | stage 4's body, via `body_from` |
| `drugs[].elsewhere` | list of dict | **yes**, ≥ 1 | the organ/effect rows in the closing panel. Raises if empty: that panel **is** stage 5, and a drug that reaches the end of the route with nothing to show there has demonstrated that a drug goes to one place |
| `drugs[].elsewhere[].organ` | str | **yes** | the left-hand name (`Liver`, `Every other organ`) |
| `drugs[].elsewhere[].effect` | str (rich) | **yes** | what the drug did there |
| `drugs[].verdict` | str (rich) | **yes** | the **cream panel** closing the journey. The one sentence that says what the route was for |
| `stages` | list of dict | **yes**, **exactly 5** | the journey. See the raise above |
| `stages[].title` | str | **yes** | visible **before** the stage is reached — the map a student reads at step 0, which is why stage 3 is on screen from the start. Raises if two stages share one |
| `stages[].body` | str (rich) | one of two | the body shown when the stage is reached, **the same for every drug** |
| `stages[].body_from` | str | one of two | the name of the per-drug key this stage's body comes from (`entry`, `target`). Raises if the named key is missing on *any* drug — the gap would be one tab silently short while three read correctly |
| `stages[].id` | str | no | not read by this renderer. Authored for legibility |
| `dose_label` | str | **yes** | the mono caption over the tab row (`The dose`) |
| `elsewhere_label` | str | **yes** | the alert mono caption on the closing panel (`Where else the same dose went`) |
| `next_labels` | dict | **yes** | the advance button's three captions. Needs all of `start`, `more`, `done` |
| `next_labels.start` | str | **yes** | at stage 0 (`Take the dose`) — the only instruction a student gets before acting |
| `next_labels.more` | str | **yes** | mid-route (`Next stage`) |
| `next_labels.done` | str | **yes** | at the end, on the now-disabled button (`Journey complete`) |
| `reset_label` | str | **yes** | the restart control (`New dose`) |
| `start_drug` | str | no, default `drugs[0].id` | which drug the block opens on. Raises if it is not one of the declared ids |

**Exactly one of `body` and `body_from` per stage, and the renderer raises on both or neither.**
A stage carrying both would let one of them win silently, and the sharing of stages 2, 3 and 5 is
the block's argument rather than an economy.

**Design's values** (b6-01, `DRUGS` / `STEP_TITLES` / `STEP_2` / `STEP_3`, page lines 338–389):

```python
stages = [
  {"id": "in",        "title": "In",                             "body_from": "entry"},
  {"id": "blood",     "title": "Into the blood",                 "body": STEP_2},   # line 388
  {"id": "circuit",   "title": "Once round the whole body",      "body": STEP_3},   # line 389
  {"id": "target",    "title": "It acts where it fits",          "body_from": "target"},
  {"id": "elsewhere", "title": "And everywhere else it reached",
   "body": "Listed below — and none of them is a fault in the drug."},              # line 489
]
dose_label      = "The dose"
elsewhere_label = "Where else the same dose went"
next_labels     = {"start": "Take the dose", "more": "Next stage",
                   "done": "Journey complete"}
reset_label     = "New dose"
start_drug      = "caffeine"
```

The four drug records are Design's `DRUGS` array at page lines 338–379, lifted whole.

**Behaviour the engine guarantees.**

- One advance control, moving by exactly one. There is no way to reach stage 4 without passing
  stage 3.
- A stage's body is hidden until the stage is reached; the current stage takes the alert border and
  the lifted ground, a reached one keeps a lit chip and a full-strength title.
- **Changing drug resets to stage 0** (Design's own `setState({ drug, step: 0 })`). The closing
  panel is hidden unless *both* the drug matches *and* the route is complete, so there is no order
  of taps that opens nicotine's consequences having followed caffeine's dose.
- The stage ticks when the route is complete, and **unticks if it is restarted** — Design's `isDone`
  is `step >= 5`, a pure function of the state, so a student who presses *New dose* is mid-journey
  again and the rail says so.
- Nothing is ticked on load; nothing is marked right or wrong anywhere in the block, because
  choosing a drug is not answering anything (R3).

**Measured contrast**, driven in a browser on the ink block (`--ks3-dark-panel` #3E3730 unless
stated). The verdict is the unit's first cream-inside-ink element and the one that would have
shipped invisible:

| Element | Colour on ground | Ratio |
|---|---|---|
| `.ks3-route-verdict` | #221E1B on **#FBF3E6** | **15.02:1** |
| `.ks3-route-elselabel` | #FFC53D | 7.42:1 |
| `.ks3-route-organ` | #FBF3E6 | 10.63:1 |
| `.ks3-route-effect` | #E7DECE | 8.77:1 |
| `.ks3-route-name` | #FBF3E6 | 10.63:1 |
| `.ks3-route-class` | #FFC53D | 7.42:1 |
| `.ks3-route-where` | #C6B9A7 | 6.08:1 |
| `.ks3-route-steptitle` reached / resting | #FBF3E6 / #C6B9A7 | 10.63:1 / 6.08:1 |
| `.ks3-route-stepbody` | #E7DECE | 8.77:1 |
| `.ks3-route-doselabel` | #C6B9A7 on #221E1B | 8.58:1 |
| `.ks3-route-tab` resting / chosen | #FBF3E6 on #221E1B / #221E1B on #FFC53D | 15.02:1 / 10.48:1 |

With `.ks3-dark .ks3-route-verdict` unscoped the verdict measures **1.21:1** — the same number
`.ks3-bell-chainlabel` shipped at on B4. That is the mutation the parity row was kept for.

---

## 2 · `clearance-clock` — b6-02 `#s-clock`

Five drinks that add units, six things people believe sober you up, a *wait an hour* control and a
falling blood bar.

**⚖️ The instrument is that NO intervention changes the number of hours.** Not "most of them are
ineffective" — *none of them moves the clock*, and the block exists so a student discovers that by
trying to beat it. NOTES-B6 §2.2 states it as a design note; in the engine it is enforced by
**architecture rather than by care**:

- the chosen fix reaches exactly one thing, in the renderer and in the wiring — **the note that is
  showing** — and appears in no expression that produces a number;
- there is **no rate key on the payload** for a later pass to make conditional;
- **`fixes[]` may carry no numeric field at all** — the renderer raises on one, because a fix
  carrying a number is a rate waiting to be applied;
- the parity drive `clock-run` selects every fix in turn, at rest and again mid-clock, and requires
  the hours and the bar to be **identical across all of them**, in a browser, on the page.

**⚖️ The one honest exception is a sentence, not a branch.** *A big meal first* lowers the **peak**
and not the clock, and Design handles that entirely inside that fix's own `note`: *"The total
amount to break down has not changed, so the hours have not changed."* There is no code path that
treats it differently from the other five, and there must never be one.

**⚖️ Hours = units, and the rate is deliberately NOT a payload key.** One unit an hour is the
lesson's own figure, stated in six places on b6-02 including the key fact and the legal line, and
NOTES-B6 flag 5 has it as a science-review item. A `hours_per_unit` dial is a number a later pass
could make depend on the fix, and this arithmetic is the single claim the whole block rests on. If
the science gate moves the rate, it moves in the renderer, in one place, in a reviewed commit.

**Shell keys for this block**

```python
eyebrow  = "At the bench · one liver, one clock"
heading  = "Try to beat the liver"
prompt   = ("Build an evening's drinks, pick something to speed the clearing up, then "
            "run the clock. Every trick on this bench is one people genuinely believe "
            "in. Only one of them changes anything, and not the thing they think.")
progress = {"idle": "clock not started", "running": "clock running", "clear": "cleared"}
```

**Instrument payload**

| Key | Type | Req | Drives |
|---|---|---|---|
| `drinks` | list of dict | **yes**, ≥ 1 | the pour buttons, in the drawn order |
| `drinks[].id` | str | **yes** | the row key. Raises if duplicated |
| `drinks[].label` | str | **yes** | the caption. The **unit value is appended by the engine** — Design's own `d.label + ' · ' + d.units` — so do not write it into the label |
| `drinks[].units` | int ≥ 1 | **yes** | whole units. Raises on 0, on a fraction and on a negative: the unit values are science (flag 6) and a drink worth nothing is a control that does nothing when pressed |
| `fixes` | list of dict | **yes**, ≥ 2 | the "ways to sober up". Raises below 2 — with a single fix there is nothing to compare against and the clock looks like it was never going to move |
| `fixes[].id` | str | **yes** | the key. Raises if duplicated |
| `fixes[].label` | str | **yes** | the tab caption |
| `fixes[].note` | str (rich) | **yes** | the whole of what a fix does: where the student is told why the number did not move. This is where the *big meal* exception is drawn |
| *(any numeric key on a fix)* | — | **forbidden** | **raises.** No intervention changes the hours — that IS the instrument — so a fix has nothing to contribute a number to |
| `max_units` | int ≥ 1 | **yes** | the cap on the glass. Raises if smaller than the biggest single drink: pressing that drink on an empty glass would add less than the button says |
| `start_units` | int | no, default `0` | the evening the block opens on. Must be 0…`max_units` |
| `start_fix` | str | no, default `fixes[0].id` | which fix is chosen on load. Raises if not a declared id |
| `add_label` | str | **yes** | the mono caption over the drinks (`Add a drink`) |
| `fix_label` | str | **yes** | the mono caption over the fixes (`And to sober up faster`) |
| `units_label` | str | **yes** | `{n} unit{s} drunk` |
| `hours_label` | str | **yes** | `{n} hour{s} to clear` — the alert figure, and the number that never moves |
| `hours_none` | str | **yes** | what the hours readout says with an empty glass (`nothing to clear`) |
| `blood_label` | str | **yes** | the caption over the bar (`Alcohol still in the blood`) |
| `remaining_label` | str | **yes** | `{h} hour{s} elapsed · {r} unit{s} left` |
| `wait_label` | str | **yes** | the advance control (`Wait an hour`) |
| `clear_label` | str | **yes** | the same control once the blood is clear, disabled (`Blood is clear`) |
| `reset_label` | str | **yes** | `Empty the glass` |
| `verdicts` | dict | **yes** | needs all of `empty`, `clear`, `running`; all three are reachable |
| `verdicts.empty` | str | **yes** | nothing drunk |
| `verdicts.clear` | str | **yes** | the payoff: *"…which is exactly the number of units. Every route you tried gave the same number of hours…"* |
| `verdicts.running` | str | **yes** | mid-clock |

### `{s}` — the plural rule

`{n}`, `{r}` and `{h}` are numbers; **`{s}` is the plural suffix of the number placeholder
immediately before it**, left to right. Two templates carry two numbers and two suffixes and the
pairing is *crossed* between them:

```
"{h} hour{s} elapsed · {r} unit{s} left"                 → h, then r
"{r} unit{s} still in the blood after {h} hour{s}."      → r, then h
```

A single global plural would print `1 units` on one of them whichever number it chose; named
suffixes would make the author write the pairing twice and keep the two in step by hand. The
suffix belongs to the number it just followed, which is how the sentence is read.

**Two build errors here, both silent otherwise.** A `{s}` with **no number before it** raises — it
means a number moved and left its suffix behind, and the sentence would read wrong for one value
in every ten. And **anything left in braces after filling** raises: `{q}`, `{units}`, `{hours}`
are not placeholders this readout carries, and without the check they shipped the braces through
to a student with every other gate green.

**Which numbers each template carries:** `units_label` and `hours_label` take `{n}`;
`remaining_label` takes `{h}` and `{r}`; all three verdicts take `{n}`, `{h}` and `{r}`.

**Behaviour the engine guarantees.**

- `hours to clear` = `units drunk`. `remaining` = `max(0, units − hours elapsed)`.
- The bar is `remaining / units`, **not** `remaining / max_units` — Design's own, so a two-unit
  evening and a twelve-unit evening both open full. The bar says how far through *this* clearance
  you are; the hours readout is the only thing that says how long the evening is.
- **Pouring a drink resets the elapsed clock to zero** (Design's `{ units: …, hour: 0 }`). Leaving
  the hours where they were would credit the new units with hours that passed before they existed.
- The wait control is disabled with an empty glass and once the blood is clear, and reads
  `clear_label` in the second case.
- The verdict is hidden until the clock has been run once, then stays. The stage ticks on the same
  event — Design's `everRan` — and not on load, because the block opens with an evening already
  poured.
- *Empty the glass* clears the units and the hours and leaves the verdict in place, reading
  `verdicts.empty`. Design's own.

**Measured contrast** (`--ks3-dark-panel` #3E3730 unless stated):

| Element | Colour on ground | Ratio |
|---|---|---|
| `.ks3-clock-verdict` | #221E1B on **#FBF3E6** | **15.02:1** |
| `.ks3-clock-hours` | #FFC53D | 7.42:1 |
| `.ks3-clock-units` / `-bloodlabel` | #FBF3E6 | 10.63:1 |
| `.ks3-clock-remaining` | #C6B9A7 | 6.08:1 |
| `.ks3-clock-note` | #E7DECE on the 6% wash (#4A433C) | 7.29:1 |
| `.ks3-clock-grouplabel` | #C6B9A7 on #221E1B | 8.58:1 |
| `.ks3-clock-drink` / `-fix` resting | #FBF3E6 on #221E1B | 15.02:1 |
| `.ks3-clock-fix` chosen | #221E1B on #FFC53D | 10.48:1 |
| `.ks3-blockhead-count` | #C6B9A7 on #221E1B | 8.58:1 |

---

## 3 · `claim-check` — b6-03 `#s-claims`

Five claims, each with the evidence someone offered for it, and five faults shared across all five.

**⚖️ The pool is a bijection and the renderer proves it.** Each fault is the right answer for
**exactly one** claim — which is what makes every wrong pick still a **true statement about
evidence**, and what the block's own prompt promises the student: *"a wrong answer still teaches
you something about the claim you picked it for."* Add one invented distractor and that promise
becomes false; drop one and a claim becomes unanswerable. The renderer raises unless the mapping is
one-to-one and onto, and the parity drive re-derives it from the document: every panel's
`data-answer` must be distinct, must exist on the bench, and must name its own fault in the
reveal — checked across **all five**, because an implementation that always prints the first fault
in the list is correct for exactly one claim and that claim is the one the block opens on.

**⚖️ The bench does not mark right and wrong** (MRB-208 R10, restated on Design's own page). A
fault button shows that it was **chosen** — alert border, alert letter — and takes no verdict
class, no green, no red, ever, open or not. What happens at the check is not marking either: the
four that were not chosen drop to `.5`, and a separate cream panel **names** the fault in a
sentence. Only the mastery ladder marks correctness. The drive reads `color`,
`background-color` and `border-color` off **every** option, in the wrong-pick state, and fails on
`--ks3-ok` #12A150 or `--ks3-danger` #FF6B6B anywhere.

**⚠️ The answer line is the CORRECT fault's text, not the chosen one.** Design reads
`FAULTS.find(f => f.id === claim.answer).text`, so a student who picked wrongly is shown the right
fault named in full. That is the whole reason the reveal is not withheld for a wrong answer.

**Shell keys for this block**

```python
eyebrow      = "At the bench · five claims, five faults"
heading      = "Find the fault in the evidence"
prompt       = ("Each claim comes with the evidence someone offered for it. Every fault in "
                "the list below is the real fault of one of these five claims, so a wrong "
                "answer still teaches you something about the claim you picked it for.")
head_counter = {"format": "{n} of 5 checked", "total": 5}
```

**Instrument payload**

| Key | Type | Req | Drives |
|---|---|---|---|
| `claims` | list of dict | **yes**, ≥ 2 | one tab per claim, in the drawn order |
| `claims[].id` | str | **yes** | the key. Raises if duplicated |
| `claims[].label` | str | **yes** | the tab caption (`Natural`, `My grandad`) |
| `claims[].text` | str | **yes** | the claim itself, in display type — the quoted sentence |
| `claims[].evidence` | str (rich) | **yes** | the case made for it, in its own captioned panel |
| `claims[].answer` | str | **yes** | the id of the fault that is this claim's real fault. Raises if not an offered fault, and raises if any fault answers more than one claim |
| `claims[].why` | str (rich) | **yes** | the reasoning, on the cream panel |
| `claims[].settle` | str (rich) | **yes** | what would actually decide it. Raises if missing — a claim with a verdict and no `settle` teaches that bad evidence is a thing to spot rather than a thing to replace |
| `faults` | list of dict | **yes**, **exactly `len(claims)`** | the shared option list |
| `faults[].id` | str | **yes** | matched against `claims[].answer`. Raises if duplicated |
| `faults[].text` | str | **yes** | read **twice** — as the option a student picks, and as the answer line naming the fault — so it has to stand on its own as a sentence |
| `labels` | dict | **yes** | needs all of `claims`, `evidence`, `faults`, `settle` |
| `labels.claims` | str | **yes** | the mono caption over the tabs (`The claim`) |
| `labels.evidence` | str | **yes** | the caption inside the evidence panel (`The evidence offered`) — without it the panel reads as part of the claim rather than as the case made for it |
| `labels.faults` | str | **yes** | the ask above the options (`What is wrong with that evidence?`) |
| `labels.settle` | str | **yes** | the bold lead-in on the last line of the reveal (`What would settle it:`) |
| `verdicts` | dict | **yes** | needs both `right` and `wrong`. Both are **accent eyebrows on the cream panel**, and neither is a mark: the reveal opens either way |
| `check_label` | str | **yes** | the commit button (`Check it`) |
| `checked_label` | str | **yes** | the same button once the claim is checked, disabled (`Checked`) |
| `tally` | dict | **yes** | needs both `format` and `done`. The line beside the button counts **down** |
| `tally.format` | str | **yes** | `{n} still to check` — `{n}` is **claims remaining**, not claims done |
| `tally.done` | str | **yes** | the last one is a sentence rather than "0 still to check" (`all five claims checked`) |
| `start_claim` | str | no, default `claims[0].id` | which claim the block opens on |

**Behaviour the engine guarantees.**

- Every claim keeps **its own pick and its own checked flag** over one shared fault list. Moving
  away from a claim and back finds it exactly as it was, and a fresh claim opens uncommitted.
- The check button is disabled until a fault is picked, and again once the claim is checked.
- The reveal opens **whether the pick was right or wrong**, and names the right fault either way.
- The faults lock when the claim is checked; the unpicked four dim to `.5` and are **not**
  recoloured or struck through — every one of them is a true statement about evidence.
- The stage ticks when **all five** claims are checked (Design's own `isDone`), not before: the
  block's argument is that five different-looking claims fail in five different ways, and a student
  who has checked one has met a claim rather than the comparison.
- Nothing is ticked on load.

**Measured contrast.** The reveal is the largest run of ink-on-cream in the unit — four elements
in one panel, which is exactly the shape of the B4 defect where a panel was rescued and a
paragraph inside it was not:

| Element | Colour on ground | Ratio |
|---|---|---|
| `.ks3-ccheck-word` | #A93411 on **#FBF3E6** | **5.98:1** |
| `.ks3-ccheck-answer` | #221E1B on **#FBF3E6** | **15.02:1** |
| `.ks3-ccheck-why` | #3B342E on **#FBF3E6** | **11.11:1** |
| `.ks3-ccheck-settle` | #3B342E on **#FBF3E6** | **11.11:1** |
| `.ks3-ccheck-claim` / `-ask` / `-fault` | #FBF3E6 on #3E3730 | 10.63:1 |
| `.ks3-ccheck-evidence` | #E7DECE on the 6% wash (#4A433C) | 7.29:1 |
| `.ks3-ccheck-evlabel` | #C6B9A7 on the same | 5.05:1 |
| `.ks3-ccheck-tally` | #C6B9A7 on #3E3730 | 6.08:1 |
| `.ks3-ccheck-tabslabel` | #C6B9A7 on #221E1B | 8.58:1 |
| `.ks3-ccheck-tab` chosen | #221E1B on #FFC53D | 10.48:1 |
| chosen fault letter | #FFC53D on #3E3730 | 7.42:1 |
