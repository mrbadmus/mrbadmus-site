# B5 — Reproduction · instrument payload schema

**⚠️ Written AFTER the fact, and that is the whole point of the warning at the top.** This file was
supposed to be the contract between the eight B5 authoring passes and the B5 engine pass. It was
never written: a session limit on 16 Aug 2026 killed the engine pass before it produced a single
renderer, and the eight authoring passes therefore authored their payloads against Design's approved
pages and `ks3_data/b5/__init__.py` rather than against an agreed schema
(`ks3_data/_parked_biology_b5_reproduction.py` records this precisely).

So this document is **descriptive, not prescriptive**: it records the schema the renderers were
built to, derived by reading the eight lesson records one key at a time. Where two records name one
idea differently — and four of them do — the renderer accepts **both** spellings and both are listed
below, with the divergence marked ⚠️. **No key in `ks3_data/b5/` was renamed to fit this file.**
Renaming them is a follow-up, and it is a data change with a full gate run behind it, not a tidy-up.

**What this is now.** One section per instrument kind. Every key below is a key a renderer in
`build_ks3.py` actually reads; keys marked **required** raise a `ValueError` at build time when
missing, and the build is red. Nothing here is aspirational — if a renderer stops reading a key,
this file changes with it.

**Source of truth for the copy.** `docs/ks3/design-reference/b5/b5-0N-*.dc.html`, Design's approved delivery.
Every student-facing string in the records is lifted from those files byte-identical. **On this unit
that is not a style preference: it is a safeguarding one.** Five of the eight lessons are human
reproduction, read by 12- and 13-year-olds. `lifestyle-and-the-developing-foetus` carries the
load-bearing case — the placenta as a NEUTRAL surface governed by size and solubility — and its
anti-blame refutation and legal line are lifted whole or not at all.

**Where the instruments live.** ⚠️ **ALL EIGHT sit on a `practical` segment** —
`<section class="ks3-block ks3-dark ks3-practical">` — measured off Design's own markup on all
eight pages, no exceptions:

| Page | Anchor | Design's shell | Segment |
|---|---|---|---|
| b5-01 | `#s-jobs` | `ks3-block ks3-dark ks3-practical` | `practical` |
| b5-02 | `#s-compare` | `ks3-block ks3-dark ks3-practical` | `practical` |
| b5-03 | `#s-dial` | `ks3-block ks3-dark ks3-practical` | `practical` |
| b5-04 | `#s-cross` | `ks3-block ks3-dark ks3-practical` | `practical` |
| b5-05 | `#s-cross` | `ks3-block ks3-dark ks3-practical` | `practical` |
| b5-06 | `#s-parts` | `ks3-block ks3-dark ks3-practical` | `practical` |
| b5-07 | `#s-becomes` | `ks3-block ks3-dark ks3-practical` | `practical` |
| b5-08 | `#s-sort` | `ks3-block ks3-dark ks3-practical` | `practical` |

**That means every one of them is on ink**, and every colour rule in `shared/ks3.css` under
`/* ═══ BEGIN B5 ═══ */` is scoped `.ks3-dark …` at (0,2,0), because `.ks3-dark p` is (0,1,1) and
beats a bare instrument class. `ground` is **not** authored on any B5 instrument block: the
`practical` shell is already ink.

**Nothing in this unit animates, uses a timer, or draws to a canvas** (NOTES-B5 §2). The engine adds
no `transition` and no `@keyframes` for B5, so there is no reduced-motion obligation to satisfy and
nothing to degrade.

---

## 0 · Three chassis, eight kinds

The eight instruments are drawn by **three** renderers, and the sharing is deliberate rather than an
economy. NOTES-B5 §6: *"b5-05 reuses b5-04's instrument shape deliberately … If Code refactors
either one, keep them identical — the repetition is the argument."*

| Chassis | Kinds | Marker attribute | Wire fn |
|---|---|---|---|
| **commit bench** (§1) | `job-match`, `crossing-bench`, `crosses-panel`, `flower-jobs`, `disperse-sort` | `data-b5cblock` | `wireB5Commit` |
| **comparison rows** (§2) | `gamete-compare`, `what-it-becomes` | `data-cmpblock` | `wireCompareRows` |
| **cycle dial** (§3) | `cycle-dial` | `data-dialblock` | `wireCycleDial` |

Each kind still has its **own block class** (`ks3-jmatch-block`, `ks3-xbench-block`,
`ks3-xpanel-block`, `ks3-fjobs-block`, `ks3-dsort-block`, `ks3-gcmp-block`, `ks3-becomes-block`,
`ks3-dial-block`), because that is what a stylesheet and a parity row hang on, and its own entry in
both `ACTIVITY_KIND_RENDERERS` and `ACTIVITY_KIND_FN`.

---

## 0.1 · Keys the SHELL reads, not the instrument

These sit on the activity record beside `kind` and are read by `r_activity` before a renderer runs.

| Key | Type | Req | Drives |
|---|---|---|---|
| `kind` | str | **yes** | the dispatch key |
| `eyebrow` | str | no | the block's eyebrow. All eight B5 blocks author one |
| `heading` | str | no | the block `<h2>` |
| `prompt` | str | no | the lede paragraph under the head row |
| `head_counter` | dict | no | the right-aligned mono readout on the head row. All eight author one |
| `demand` | str | no | defaulted to `investigate` by `ks3_data/b5/__init__.py::_normalise`; b5-08 authors `classify` |

### ⊕ `head_counter.start` is FILLED BY THE ENGINE for `cycle-dial`

`_KIND_HEAD_START` in `build_ks3.py` sets `start = 1` for `cycle-dial` when the record does not
author one. b5-03's dial opens with one of its three cycle lengths already selected and therefore
already **seen** (Design's own state is `seen: { 28: true }`), so Design's page renders
`1 of 3 lengths tried` on first paint. Without this the shipped HTML reads `0 of 3 lengths tried`
until `wireCycleDial` corrects it — a wrong number on screen for an instant and a wrong number
permanently in the bytes a crawler or a JS-off reader gets.

This is a fact about the **instrument**, not about the lesson: it would still be 1 if the author
picked a different opening length. An authored `start` still wins; the engine only fills a blank.

---

## 1 · The commit bench — `job-match`, `crossing-bench`, `crosses-panel`, `flower-jobs`, `disperse-sort`

Design's five blocks, in order: tabs → a panel naming the item → a mono ask → the options → a check
button with a hint beside it → a **cream** panel carrying a verdict word, an answer and a why. b5-05
adds a 0–40 week window under the why; b5-08 adds the deciding-feature line. Nothing else differs.

### 1.0 The four labels, and ⚠️ **the four spellings**

Every one of these five blocks needs the same four labels, and **the five records spell them nine
different ways**. This is the single largest consequence of the missing schema. The renderers accept
the union; the **first** name found wins, and per-kind preference order is given in the code.

| Role | Spellings actually authored | Where |
|---|---|---|
| the mono ask above the options | `options_label` · `options_lead` · `commit_label` · `choose_prompt` | b5-01 · b5-06 · b5-04/b5-05 · b5-08 |
| the check button's label | `check_label` · `reveal_label` | b5-01/b5-04/b5-05 · b5-06/b5-08 |
| the three-state hint container | `hints` · `hint` | b5-01/b5-06/b5-08 · b5-04/b5-05 |
| the two verdict words container | `verdicts` · `verdict` | b5-01/b5-08 · b5-04/b5-05/b5-06 |

And **inside** the hint container the three roles are also spelled three ways:

| Role | Spellings | Where |
|---|---|---|
| nothing chosen yet | `empty` · `idle` | b5-01 · b5-04/b5-05/b5-06/b5-08 |
| chosen, not yet checked | `ready` | all five |
| checked | `checked` · `done` · `opened` | b5-01 · b5-04/b5-05 · b5-06/b5-08 |

`verdicts` / `verdict` is `{right, wrong}` on all five — the one thing every record agreed on.

> **If the records are ever normalised**, the recommended target is `options_label`, `check_label`,
> `hints: {idle, ready, done}` and `verdicts: {right, wrong}` — the majority spelling in each row
> except the ask, where `options_label` reads truest to what it is. That is a data change, and it
> needs the full gate set behind it.

### 1.1 `job-match` — b5-01 `#s-jobs`

| Key | Type | Req | Drives |
|---|---|---|---|
| `functions` | list | **yes** | the shared pool. Each `{id, text}`, both required; duplicate `id` raises |
| `structures` | list | **yes** | one per tab. See below |
| `structures[].id` | str | **yes** | the DOM key: tab, panel row, option list and reveal all carry it |
| `structures[].label` | str | **yes** | the tab's short label |
| `structures[].name` | str | **yes** | the panel's display-type heading |
| `structures[].system` | str | **yes** | the mono line beside it (`Male system` / `Female system`) |
| `structures[].options` | list[str] | **yes** | four `functions[].id`s, **in Design's order** — the A/B/C/D letters follow it. An id outside the pool raises |
| `structures[].func` | str | **yes** | the correct option's id. Must be in the pool |
| `structures[].answer` | str | **yes** | the reveal's display-type answer line — a **sentence**, not the function's text |
| `structures[].why` | str | **yes** | the reveal's reasoning paragraph. `<em>` / `<strong>` allowed |

⚖️ **This block does NOT assert a bijection, and that is deliberate.** Eight structures, nine
functions: `receive` is the vagina's job and the vagina is not a tab, and the oviduct owns two jobs
of its own. Design's prompt warns about exactly that — *"Only one structure has more than one job,
and the reveal says which."* Asserting one-to-one here would fail Design's own approved data, and
trimming the pool to fit would remove the asymmetry the whole lesson is built on. Contrast §1.4.

### 1.2 `crossing-bench` — b5-04 `#s-cross`

| Key | Type | Req | Drives |
|---|---|---|---|
| `choices` (or `directions`) | list | **yes** | the two directions, shared by every substance. Each `{id, label}`. Fewer than two raises |
| `subs[].id` / `.label` / `.name` | str | **yes** | DOM key, tab label, panel heading |
| `subs[].kind` | str | **yes** | the mono line beside the heading (`Small molecule · diffusion`) |
| `subs[].context` | str | **yes** | the paragraph under the heading — the line that makes the direction predictable |
| `subs[].dir` | int **or** str | **yes** | the answer. ⚠️ see below |
| `subs[].answer` | str | **yes** | the reveal's display-type answer line |
| `subs[].why` | str | **yes** | the reasoning. **Always names the concentration difference** (NOTES-B5 §2.2) |

⚠️ **`dir` accepts either spelling.** Design's page stores an **index** (`dir: 0` / `dir: 1`) into a
two-element list; NOTES-B5 §2.2 names the key without saying which. The renderer accepts an integer
index into `choices` **or** a choice `id` string. The reason is on the record: this lesson module was
being authored by a concurrent pass while the renderer was being written, and a build that died over
the spelling of one integer would have parked the unit a second time. As landed, b5-04 uses the
**index** form with `choices` ids `in` / `out`.

⚠️ **b5-04 and b5-05 are twins on purpose.** They share `_b5_commit` because NOTES-B5 §6 requires it.
The only thing b5-05 adds is the week window.

### 1.3 `crosses-panel` — b5-05 `#s-cross`

Everything in §1.2, with `crosses` in place of `dir`, plus:

| Key | Type | Req | Drives |
|---|---|---|---|
| `choices` | list | **yes** | exactly **two** — a yes/no commit. The **first** is the "it crosses" choice |
| `window.label` | str | **yes** | the mono caption over the 0–40 week bar |
| `window.ticks` | list[str] | **yes** | the three tick labels under it (`Week 0` · `Week 20` · `Week 40`) |
| `subs[].crosses` | bool | **yes** | the answer. `true` → `choices[0]`, `false` → `choices[1]` |
| `subs[].win` | [num, num] | **yes** | the window as `[start%, end%]` across the bar. Must satisfy `0 ≤ start ≤ end ≤ 100` |
| `subs[].win_text` | str | **yes** | ⚠️ **snake_case.** NOTES-B5 §2.3 writes it `winText`; the record authors `win_text` and the renderer follows the record. `winText` is accepted as a fallback |

⚖️ **FIVE OF THE SIX CROSS AND ONE DOES NOT, AND THE IMBALANCE IS THE TEACHING POINT.** NOTES-B5
§2.3: *"do not 'balance' the set."* The renderer **raises** if every substance crosses (no exception
left to prove the size rule with) and **raises** if the set is balanced (which teaches that the
placenta sorts). Insulin's `win` is `[0, 0]` and its `win_text` says so in words — which is why the
bar may draw nothing while the text may never be empty.

### 1.4 `flower-jobs` — b5-06 `#s-parts`

| Key | Type | Req | Drives |
|---|---|---|---|
| `jobs` | dict | **yes** | the shared pool, `{key: sentence}`. **Nine keys, one per part** |
| `parts[].id` / `.label` / `.name` | str | **yes** | DOM key, tab label, panel heading |
| `parts[].group` | str | **yes** | the mono line (`Male part · stamen`) |
| `parts[].options` | list[str] | **yes** | four `jobs` keys, in Design's order. A key outside the pool raises |
| `parts[].answer` | str | **yes** | the correct `jobs` key. **The reveal's answer line is `jobs[answer]`** — Design reads `JOBS[part.answer]`, so a wrong pick still sees the right job named in full |
| `parts[].why` | str | **yes** | the reasoning |

⚖️ **HERE IT IS A BIJECTION, AND THE RENDERER PROVES IT.** Nine jobs, nine parts, each job the answer
for exactly one part. NOTES-B5 §2.4 states the rule and the block's own prompt promises it to the
student: *"Every wrong option here is the right answer for a different part, so a guess still teaches
you something."* Unequal counts raise; a job answering two parts raises (which also means one job
answers none — the invented distractor the pool exists to avoid). There is **no per-part `answer`
sentence** on this kind; §1.1's `structures[].answer` has no counterpart here.

### 1.5 `disperse-sort` — b5-08 `#s-sort`

| Key | Type | Req | Drives |
|---|---|---|---|
| `choices` (or `methods`) | list | **yes** | the five methods, shared. Each `{id, label}`. Fewer than three raises |
| `specimen_label` | str | **yes** | the mono line beside the heading, rendered as `<label> 01` |
| `tell_label` | str | **yes** | the caption on the deciding-feature line in the reveal |
| `specimens[].id` / `.label` / `.name` | str | **yes** | DOM key, tab label, panel heading |
| `specimens[].desc` | str | **yes** | the description. ⚠️ **structure only** — see below |
| `specimens[].answer` | str | **yes** | the correct method id. **The reveal's answer line is `choices[answer].label`** |
| `specimens[].tell` | str | **yes** | the observable that settles it, on a line of its own |
| `specimens[].why` | str | **yes** | the reasoning |

⚖️ **THE DESCRIPTIONS NAME STRUCTURE AND NOTHING ELSE** (NOTES-B5 §2.6). The renderer raises if a
specimen's own first word appears inside its `desc` — naming the plant turns a classification on
evidence into a recall question. The tab still carries the name, because a student has to be able to
come back to one.

⚖️ **The specimen NUMBER is derived from list position** (`%02d`), exactly as Design derives it.
Authoring it would be a second source of truth for a list's own order. A method no specimen is
sorted into raises.

### 1.6 What the commit chassis emits, and what marks what

```
.ks3-b5c[data-b5c][data-total][data-item][data-check-label]
                  [data-hint-idle][data-hint-ready][data-hint-done]
  .ks3-b5c-tabs   > .ks3-b5c-tab[data-b5c-pick][aria-pressed]
  .ks3-b5c-panel  > .ks3-b5c-item[data-for][hidden]
                      > .ks3-b5c-headrow > .ks3-b5c-name + .ks3-b5c-meta
                      > .ks3-b5c-context           (b5-04, b5-05, b5-08 only)
  .ks3-b5c-ask
  .ks3-b5c-opts[data-for][hidden] > ul.ks3-options
                      > button.ks3-option.ks3-b5c-opt[data-owner][data-opt]
  .ks3-b5c-foot   > button.ks3-reveal-btn.ks3-b5c-check[data-b5c-check]
                  + .ks3-b5c-hint[data-b5c-hint][role=status]
  .ks3-b5c-reveal[data-b5c-reveal][data-answer][hidden]
                  > .ks3-b5c-word > span[data-word=right|wrong][hidden]
                  > .ks3-b5c-answer
                  > .ks3-b5c-why
                  > .ks3-b5c-tell > .ks3-b5c-telllabel      (b5-08)
                  > .ks3-b5c-window > .ks3-b5c-winlabel
                                    > .ks3-b5c-wintrack > .ks3-b5c-winfill
                                    > .ks3-b5c-winticks
                                    > .ks3-b5c-wintext     (b5-05)
```

⚖️ **MRB-196 R10 — nothing is marked on an option button.** A chosen option takes the alert border
`.ks3-dark .ks3-option[aria-pressed="true"]` already gives it and nothing else: no `is-correct`, no
`is-wrong`, no `--ks3-ok`, no `--ks3-danger`, open or not. The verdict word is a mono eyebrow in
`--ks3-accent-text` on the cream panel and it appears **whichever way the pick went**. Only the
mastery ladder marks correctness.

⚖️ **The stop ticks on ALL of them** — eight structures, six substances, nine parts, eight specimens
— which is Design's own `isDone` on all five pages. Nothing is ticked on load (MRB-208): the shell
emits `data-stage-done="0"` and the wiring only raises it when the count is complete.

⚠️ **`.ks3-b5c-opts` exists solely so the `<ul class="ks3-options">` is not the hidden element.**
`.ks3-options` is `display: flex`, and an author `display` beats the UA's `[hidden] { display: none }`
regardless of specificity — MRB-242, the defect that has now shipped seven times.

---

## 2 · Comparison rows — `gamete-compare` (b5-02) and `what-it-becomes` (b5-07)

One table drawn twice, so the plant and the animal sit in the same shape (NOTES-B5 §1).

| Key | Type | Req | Kind | Drives |
|---|---|---|---|---|
| `columns.feature` / `.sperm` / `.egg` | str | **yes** | `gamete-compare` | the three column headers |
| `table.name` / `.before` / `.after` | str | **yes** | `what-it-becomes` | ⚠️ **the same three headers under a different container name.** Both spellings kept; the records disagree and the renderers follow the record |
| `rows[].id` | str | **yes** | both | the row's DOM key |
| `rows[].name` | str | **yes** | both | the first column |
| `rows[].sperm` / `.egg` | str | **yes** | `gamete-compare` | the two data columns |
| `rows[].before` / `.after` | str | **yes** | `what-it-becomes` | ⚠️ the two data columns, differently named |
| `rows[].why` | str | **yes** | both | the paragraph the row expands to |
| `why_label` | str | no | both | ⚠️ **b5-02 authors `"Why:"`; b5-07 authors nothing.** On Design's pages the string is template markup on **both** and data on **neither**, so the engine supplies `Why:` as a Design template constant (`_WHY_LABEL`) when the record is silent. An authored value wins |
| `rows_open_on_load` | bool | no | `gamete-compare` | authored `false`. **`true` raises** — MRB-208, nothing is ticked on load and the stop is all six rows opened |
| `scale.label` / `.note` | str | no | `gamete-compare` | the scale block's caption and its closing paragraph |
| `scale.rows[].name` / `.size` / `.pct` | str/str/num | with `scale` | `gamete-compare` | one bar each; `pct` is a percentage of the widest |

⚖️ **THE LEAD COLUMN IS NOT ALWAYS THE FIRST.** `[data-lead]` marks the column Design paints in the
alert: **sperm** on b5-02, **after fertilisation** on b5-07. Hard-coding the first data column would
put b5-07's emphasis on the flower that no longer exists.

⚖️ **THE WHOLE ROW IS THE BUTTON** (NOTES-B5 §2.5) — no separate chevron control — so the tap target
spans the row's full width.

⚠️ **The count is of rows EVER opened, not of rows currently open**, which is Design's own semantics
(`open` is a map whose keys are never deleted). Counting the open ones would untick the rail stop
when a student tidied up after themselves.

⚠️ **The per-cell captions are real elements**, not `content:` on a pseudo-element: below 880px
Design drops the header row and shows them instead, and a screen reader reads them at every width.

---

## 3 · `cycle-dial` — b5-03 `#s-dial`

| Key | Type | Req | Drives |
|---|---|---|---|
| `luteal` | int | **yes** | the fortnight after release. **The one number the release day is derived from** |
| `shed` | int | **yes** | the bleeding window in days — the band on the track, and the first phase's bound |
| `lengths[].days` | int | **yes** | the cycle length. Must exceed both `luteal` and `shed`; duplicates raise |
| `lengths[].label` | str | **yes** | the chip's label |
| `lengths[].note` | str | **yes** | the sentence under the panel once a second length has been tried |
| `length_label` | str | **yes** | the mono caption over the chips |
| `start_length` | int | no | which chip opens pressed. Defaults to the first; must be one of the declared lengths |
| `start_day` | int | no | which day the slider opens on. Defaults to 1 |
| `credit_lengths` | int | no | how many **different** lengths tick the stop. Defaults to 2. **`1` raises** — one is the length the block opens on, so crediting at 1 ticks the stop on load (MRB-208) |
| `day_label` / `prev_label` / `next_label` | str | **yes** | the slider's screen-reader label and the two step buttons' `aria-label`s |
| `day_format` | str | **yes** | the big display-type readout. **Must carry `{n}`** |
| `track.start` | str | **yes** | the left tick under the bar |
| `track.release` | str | **yes** | the middle tick. **Must carry `{n}`** — it is the one label that MOVES, and a fixed string there is a hard-coded release day by another route |
| `track.last` | str | **yes** | the right tick. `{n}` = the cycle length |
| `panels.ovary` / `.uterus` | str | **yes** | the two panel captions |
| `phases[].id` | str | **yes** | ⚠️ **exactly `shed`, `build`, `release`, `held`** — see below |
| `phases[].label` | str | **yes** | the mono phase name beside the day readout |
| `phases[].ovary` / `.uterus` | str | **yes** | what each organ is doing. Both panels are on screen at every day |
| `note_prompt` | str | **yes** | what the note says **before** a second length has been tried — the only line on the page asking for the one action the stop credits |

⚖️ **THE RELEASE DAY IS DERIVED AND NEVER STORED.** `release = length − luteal`, computed at build
time and again on every draw. NOTES-B5 §2.1: *"That is the instrument's whole argument, and
hard-coding release days would destroy it."* A stored 7 / 14 / 21 would render pixel-identical and
teach that day 14 is a fact about people — `REPRO-05`, the misconception this lesson exists to
confront. **A `lengths[]` entry carrying `release`, `release_day`, `ovulation` or `ovulation_day`
raises.**

⚠️ **The four phase ids are a BRANCH, not a list**: `day ≤ shed` → `shed`; `day < release` →
`build`; `day = release` → `release`; otherwise → `held`. A missing id raises, and so does an extra
one the branch can never select.

⚖️ **THE STOP TICKS ON TWO DIFFERENT LENGTHS SEEN**, not on reaching the end of the slider (§2.1).
The opening length counts as seen — Design's state is `seen: { 28: true }` — so the readout opens at
`1 of 3` and the stop is one length away. Nothing is ticked on load.

⚠️ **MRB-210 §2** — the day slider is bound through `onRange()`, on `input` **and** `change`. The
−/+ buttons exist for keyboard and small screens and clamp to `[1, length]`; the day is re-clamped
when the length shortens, or a student on day 30 of a 35-day cycle who switches to 21 would be
standing on a day that no longer exists.

---

## 4 · Known payload divergences, recorded rather than fixed

Every one of these is a case where a record and NOTES-B5 (or another record) disagree. **In every
case the renderer follows the record.** None was changed in `ks3_data/`.

| # | Divergence | NOTES-B5 says | The record says | Followed |
|---|---|---|---|---|
| 1 | crosses-panel window text | `winText` (§2.3) | `win_text` | the record; `winText` accepted as fallback |
| 2 | crossing-bench payload | `{subs, picks, opened}` (§2.2) | `picks` / `opened` are **runtime** state and are not authored | the record — a payload key with no read site would fail `ks3_key_audit.py` (R5) |
| 3 | what-it-becomes payload | `{rows, open}` (§2.5) | `open` is runtime state, not authored | the record, same reason |
| 4 | cycle-dial payload | `{lengths: [21,28,35], luteal, shed, length, day, seen}` (§2.1) | `lengths` is a list of **objects** with `days`/`label`/`note`; `length`/`day`/`seen` are runtime and are authored as `start_length` / `start_day` | the record |
| 5 | flower-jobs payload | `parts[].options: [4 keys]` and a per-part `why` (§2.4) | matches, **and there is no per-part `answer` sentence** — the reveal's answer line is `jobs[answer]` | the record and Design's page |
| 6 | disperse-sort payload | `{methods: {5 labels}, specimens}` (§2.6) | `choices: [{id,label}]`, an ordered list rather than a map | the record; `methods` accepted as fallback |
| 7 | the four labels | not specified | nine different spellings across five records | all of them, per §1.0 |
| 8 | `why_label` | not specified | b5-02 authors it, b5-07 does not | the record, with Design's template constant as the fallback |

---

## 5 · Design-vs-engine divergences, and how they were resolved

| # | What | Design | Engine | Why |
|---|---|---|---|---|
| 1 | the tab chip | `seg()` on b5-03/04/05/06/08; a bespoke inline style on **b5-01 alone** | `seg()`'s treatment everywhere | Five blocks that NOTES-B5 §6 requires to stay identical cannot carry two chip designs, and one stylesheet serves 183 lesson slots. Five pages beat one. **Reported as drift** |
| 2 | the check button on ink | `.ks3-reveal-btn` unchanged — ink on an ink border, on a block whose ground **is** `--ks3-ink` | inverted: `--ks3-on-dark` ground, `--ks3-ink` text | The same correction `.ks3-plate-open` (B3) and `.ks3-ledger-clear` (B3) already carry. Design's `_ds` bundle re-ships this very stylesheet, so the defect is inherited rather than drawn |
| 3 | the deciding-feature line (b5-08) | one inline line, `Deciding feature: <tell>` | a mono uppercase caption on its own line above the tell | The record authors `tell_label: "Deciding feature"` **without** the colon. Emitting `": "` would be engine-invented punctuation in student-facing copy; the caption treatment is the one `.ks3-ccheck-evlabel` already uses. **Reported** |
| 4 | the reveal's body colour | inherits `--ks3-ink` from the panel | `--ks3-ink`, explicitly, at (0,2,0) | Same colour; the explicit rule is required because `.ks3-dark p` (0,1,1) beats inheritance |

---

## 6 · The statutory gap, restated so it does not vanish

`KS3.B.REP.02` asks for a *"quantitative investigation of some dispersal mechanisms"*. `b5-08` is a
CLASSIFY lesson in which the student measures nothing. NOTES-B5 flag 43 raises it; ruled on 16 Aug
2026 (MRB-244) to build what is on disk, record the gap and ship. `REP.02c` is minted at the
bullet's **full** width so the register reads covered-with-a-gap rather than covered.

Nothing in this schema closes it. If Design later adds the timing practical, it is a **new kind**,
not a widening of `disperse-sort`.
