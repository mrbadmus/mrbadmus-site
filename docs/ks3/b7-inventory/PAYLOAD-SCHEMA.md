# B7 — payload schema

Written **before** the authoring passes were dispatched, which is the whole point of it.

B5 shipped without one. Seven records then authored their payloads against Design's pages rather
than against an agreed schema, and five of them named the same four labels **nine different ways**
(`options_label` / `options_lead` / `commit_label` / `choose_prompt`; `check_label` /
`reveal_label`; `hints` / `hint`; `verdicts` / `verdict`). The engine had to accept a union and
raise when none was present. That is the cost of deciding a key name eight times instead of once.

**If this document and Design's page disagree, the page wins on MEASUREMENT (what is drawn) and
this document wins on NAMING (what we call it).** Where the page needs something this schema has
not anticipated, follow the page and say so in the report.

---

## 0. Rules that bind all four instruments

1. **All four are DOM-only.** No canvas, no `requestAnimationFrame`, no timers anywhere in B7
   (NOTES-B7 §3). An instrument that wants one is a finding, not a licence.
2. **All four ship on `ks3-block ks3-dark ks3-practical`** — measured from Design's own markup on
   all four pages. That is `segment: "practical"`, the ink-dark ground. Do not guess the shell from
   the kind name; §4 of the build contract is explicit that B1 got two of six wrong.
3. ⛔ **NO RUNTIME STATE IS AUTHORED.** NOTES-B7 §1 lists `picks`, `tested`, `ran`, `food` and
   `shown` in its payloads. Those are values the *runtime* owns, not content. Under contract R5 a
   key with no read site is a dead key and fails `ks3_key_audit.py`, and B5 established the
   precedent by deliberately authoring none. The renderer initialises its own state.
4. **Every authored key must have a read site in the same pass.** Wire the read or do not author
   the key. "It documents intent" is a comment, not a read site.
5. **Every student-facing string is lifted byte-identical** from the approved page via
   `node tools/extract_design_payload.js <page>`. Never retype science-bearing copy.
6. **Nothing marks correctness except the ladder.** These are benches: they show a consequence, they
   do not award a tick. Amber is a wrong IDEA being confronted, never the student.

## 1. One spelling per concept, for the whole unit

| Concept | The key | Never |
|---|---|---|
| Lead line above a set of options | `options_label` | `options_lead`, `choose_prompt` |
| The button that runs/commits the bench | `run_label` | `commit_label`, `check_label` |
| The button that returns it to the start | `reset_label` | `clear_label`, `again_label` |
| Map of branch id → outcome | `verdicts` | `verdict`, `outcomes` |
| A single line of help under a control | `hint` | `hints`, `note` |
| The closing paragraph after the payoff | `close` | `closing`, `after` |

## 2. `reactant-remover` — b7-01 `#s-bench`

```python
{"kind": "reactant-remover", "id": "...", "segment": "practical",
 "dials":    [{"id", "name", "options": [{"id", "label", "f"}]}],   # f = rate factor, 0..1
 "readouts": [{"id", "label", "suffix"}],       # rate %, glucose, O2 bubbles/min, CO2 taken
 "test_label": "...",                            # "Test a leaf with iodine"
 "run_label": "...", "reset_label": "...",
 "verdicts": {"<dial-id>": {"tag", "head", "why"},   # one branch per single-factor removal
              "multiple": {...},                     # more than one thing missing
              "none": {...}}}                        # nothing removed
```
**The model is a PRODUCT of the dial factors**, so removing any one takes the rate to zero. The
`multiple` branch is pedagogy, not a fallback: it tells the student to change one variable at a
time, and deleting it would let a student remove three things and learn nothing.

## 3. `leaf-tuner` — b7-02 `#s-tuner`

```python
{"kind": "leaf-tuner", "id": "...", "segment": "practical",
 "dials":    [{"id", "name", "options": [{"id", "label", "r", "w"}]}],  # r = rate, w = water lost
 "readouts": [{"id", "label", "suffix"}],       # both as % of an oak leaf
 "oak_label": "...", "reset_label": "...",
 "oak":      {"<dial-id>": "<option-id>"},      # what the oak shortcut sets
 "verdicts": {"<branch-id>": {"tag", "head", "why"}}}   # six habitat branches
```
⚖️ **The instrument opens on a deliberately BAD leaf** — enormous, thick, many stomata, no cuticle —
so the student's first move makes it worse and discovers the trade-off. The oak button is the
reveal, not the default. Do not author a sensible opening state.
⚑ The numbers are **invented teaching values**; the relative directions are right and the page says
so in its own legal line. That line is not optional decoration.

## 4. `method-breaker` — b7-03 `#s-bench`

```python
{"kind": "method-breaker", "id": "...", "segment": "practical",
 "steps":    [{"id", "num", "title", "detail", "options": [{"id", "label"}]}],
 "run_label": "...", "reset_label": "...",
 "verdicts": {"<branch-id>": {"tag", "head", "why", "conclude"}}}
```
**Fault precedence is load-bearing and ordered**: safety first (a naked flame stops the bench
outright), then result-DESTROYING faults (no ethanol, no destarch), then result-OBSCURING faults
(no boiling, no softening). A branch that reports the wrong fault first teaches the wrong lesson
about which mistakes matter.
⚠️ **The ethanol-over-a-flame branch is a safety branch, not a data branch.** Its `conclude` says
the test never happened. See NOTES-B7 flag 14 — this is the one lesson a student could read as
permission to do something, and its wording is on Mide's gate under MRB-233.

## 5. `trace-it-back` — b7-04 `#s-trace`

```python
{"kind": "trace-it-back", "id": "...", "segment": "practical",
 "foods":     [{"id", "label", "name", "chain": [{"name", "note"}], "verdict"}],
 "step_label": "...", "reset_label": "...",
 "close": "..."}
```
Six foods. The chain is revealed **backwards**, one link per press, each with its own note, and the
food's `verdict` lands only when the chain is fully revealed. Honey and mushroom are the two that
do not end where a student expects, and they are the reason the instrument exists.

## 6. Misconception ids — pre-allocated, do not improvise

| Lesson | Entries | Spare |
|---|---|---|
| b7-01 | `PLANT-01`, `PLANT-02` | `PLANT-09` |
| b7-02 | `PLANT-03`, `PLANT-04` | `PLANT-10` |
| b7-03 | `PLANT-05`, `PLANT-06` | `PLANT-11` |
| b7-04 | `PLANT-07`, `PLANT-08` | `PLANT-12` |

An unclaimed spare stays **permanently unused**, like `DRUG-07` and `REPRO-17`/`20`/`21`/`23`.
Never re-point one at a different belief — ids are permanent.

`confronted_by` and `elicited_by` **must name an element on that lesson's own page** — an activity
`id` or a block `anchor` that the page actually emits. This is gated (MRB-244) and it resolves
against the BUILT page, so a name that renders to nothing fails the build. B7's available section
anchors are `s-hook`, `s-think`, `s-ladder`, `s-keynote` on all four, plus `s-bench`/`s-summary`
(b7-01), `s-tuner`/`s-features` (b7-02), `s-bench`/`s-method` (b7-03), `s-trace`/`s-jobs` (b7-04).

## 7. `figures`

**`figures: []` on all four, and that is deliberate, not an omission.** No page draws an `<img>`, a
`<figure>` or a placeholder — measured, not assumed. NOTES-B7 flag 12 names a leaf cross-section as
the obvious candidate and records that Design taught the internal structure in five cards instead.
§4.10 allows an empty `figures` for a lesson carried by its interactives. **Do not invent a figure
slot to fill the gap, and do not drop the flag** — it is Mide's to rule on.
