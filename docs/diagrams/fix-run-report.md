# Described-diagrams fix run — report

Ticket: MRB-352 (fix run for the audit in `described-diagrams-audit.md`).
Branch: `feat/diagrams`. Started 23 Sep 2026.

**The rule being enforced (Mide's, standing):** a question about a diagram
must SHOW the diagram. It must never describe it in words.

> Status: IN PROGRESS. Sections fill as the run lands.

## 1. The frozen-window ruling, and the production re-check

Mide ruled on 23 Sep 2026 that exactly 28 frozen-window rows may be edited in
place — same `id`, same band/tier, same `bank_position`, with the only changes
being a `figure` and a reword that points at it. The ruling is made explicit in
tooling as `frozen_window_allowlist.py`, which carries the 28 ids, the ruling
text, the evidence below, and three asserts so the list cannot silently grow.
The gates stay strict for every other frozen row; `frozen_window_guard.py`
(new, this run) proves it.

### The re-check, run read-only against production immediately before the load

The chat's earlier read said 0 hits across 7 assignments / 51 questions. Re-run
independently here, and widened to cover pupils' answer history as well:

| check | result |
|---|---|
| the 28 ids are unique, and match audit §4 exactly | ✅ 28/28 |
| `assignment_questions.source_ref` hits | **0** |
| `assignment_question_attempts.question_ref` hits | **0** |
| `quiz_question_attempts.question_ref` hits | **0** |
| `unit_check_attempts.question_ids` hits | **0** |
| where the 28 live | 16 in `ks3_assignment_bank`, 12 in `ks4_assignment_bank` |
| production corpus at time of check | KS3 16,946 rows · KS4 16,765 rows |

**No pupil's past answer sits under any of the 28.** There is also a second,
independent reason the ruling is safe that was not part of its original
rationale: `assignment_question_attempts` stores `question_text` — a SNAPSHOT
of the stem at attempt time — so even a future attempt would keep the wording
the pupil actually saw. Repairing a bank row cannot rewrite a child's record.

### ⊕ A correction to the audit

Audit §2 states: *"every `figure` field on a flagged KS3 row was `None`."*
That is **not true for three of the 28**. `b9-01-e03`, `b9-01-s03` and
`b10-03-h01` each already carry a figure id (`b9-oak-wood-web-thread`,
`b10-base-pairs`), in the source files and on production alike. Six KS3 bank
rows carry one in total.

The examiner was still right to flag them, and the reason matters: nothing
resolves that id on the question-serving path, so those rows render as words
with no picture. The audit's conclusion held; its stated evidence did not.

## 2. A live defect found on the way in (not in the audit)

Worth stating before the build, because it is the sharpest argument for the
whole feature and it is already reaching children.

Six KS3 bank rows carry a `figure`. Their `bank_position`s are **1, 2, 3, 4, 6
and 8 — every one inside the auto-composition window** (`bank_position < 12`),
which is exactly the set of rows the automatic weekly assignment draws from.

Set work is sealed against them: `bankForScope()` filters `.is('figure', null)`
on both the pool read and the count read, and `rowIsSettable()` refuses them
again, with a comment saying plainly that the assignment renderer has no
figure path so the question "would reach a child as a stem that says 'look at
the diagram' with no diagram."

**The automatic weekly composer has no such guard.** `bankFor()` selects
`figure` and forwards it, and `shared/student-live.js` then discards it
(`g: null`). So the protection that was reasoned out for Set work was never
applied to the path that actually composes most assignments.

The plainest case is `b9-03-e02`, at position 1:

> "Use the web. Which animal in this wood feeds on only one thing?"

A child can be served that today, with no web anywhere on the page. The
question is unanswerable except by guessing.

This run removes the landmine rather than extending the seal: once a figure
renders, the three Set work seals lift and the six rows become correct on
every path instead of merely hidden on one.

## 3. What was built

| piece | where |
|---|---|
| two SHARED primitives — `_plot` (axis labels and UNITS are required positional args, so a graph without units cannot be drawn) and `_triangle` (raises unless the relationship is a product) | `ks3_art/kit.py` |
| a KS4 drawing package that IMPORTS the KS3 kit rather than forking it — 36 drawers: the full AQA symbol set, a parametrised circuit builder (topology, branches, a meter in series or bridged, cell orientation, a deliberate gap), dot-and-cross molecules, graphs, free-body diagrams, triangles | `ks4_art/` |
| the manifest builder — reuses `build_ks3`'s own `SVG_ART`, so a lesson page and a question show the SAME BYTES | `build_figures.py` |
| the frozen-window guard | `frozen_window_guard.py` |
| the ruling as data, with its own asserts | `frozen_window_allowlist.py` |
| the KS4 + ladder `figure` columns | `supabase/migrations/…mrb352_figure_columns.sql` |
| worksheet PDF vectors, DOCX raster, the too-tall guard, the three seals lifted | backend `figure-render.js`, `worksheet.js`, `server.js`, `set-work-scope.js` |

**The manifest carries only figures a QUESTION references.** A lesson figure
is already inlined into its lesson page, so shipping all of them to a child's
phone is pure download weight — that took KS3 from 21 figures/409KB to
16/90KB, and the site manifest is split per key stage so a KS3 pupil never
downloads KS4 circuit symbols.

## 4. Content: rows fixed, rows left

### The frozen 28 — the priority set, complete

All 28 resolved: **23 repaired, 5 deliberately left.**

| | repaired | left |
|---|---:|---:|
| KS3 (16) | 15 | 1 |
| KS4 (12) | 8 | 4 |

**Left, with reasons** — leaving a row is a legitimate outcome, and the test
is whether a picture GENUINELY BELONGS, not whether one could be added:

| id | why |
|---|---|
| `c1-02-e03` | describes pouring water from a cylinder into a dish — a hypothetical experiment, not an on-page diagram. No withheld picture to restore. |
| `ks4-food-chains-webs-s02` | states food-web facts in prose, not a picture description; no node-and-arrow ecology drawer exists and building one is scope. |
| `ks4-condensation-polymerisation-h02` | the repeat-unit drawer places flat labels and cannot show two DISTINCT reacting groups (–OH, –COOH) without a chemistry error an examiner would reject. Honest prose beats a wrong picture. |
| `ks4-circuit-symbols-e04` | a convention question. Showing both symbols labelled gives the answer away; unlabelled makes it a different, harder task. |
| `ks4-circuit-symbols-h02` | **escalated, not declined** — its marked answer misidentifies the AQA thermistor symbol. Repairing it means changing the science, which is Mide's gate. See ACCURACY-ESCALATIONS E1. |

### What a repair looks like

| before | after |
|---|---|
| "In the circuit symbols, a circle with a cross inside it means…" | "Which component's circuit symbol is shown in the diagram?" |
| "Which component is drawn as a rectangle with an arrow through it?" | "Which component is shown in the diagram?" |
| "A student draws a 40 N arrow and a 25 N arrow pointing opposite ways, then a 15 N arrow underneath…" | "Look at the diagram. Why do the two lower bars exactly fill the top one?" |
| "In the oak wood web, exactly one arrow touches the ladybirds: it runs from the aphids to the ladybirds…" | "Look at the oak wood web. Find the ladybirds, and look at the arrows touching them." |
| "A skydiver's velocity–time graph rises steeply from the origin, then curves so that its gradient falls to zero at 55 m/s after 14 s…" | "The graph shows a skydiver's velocity against time." |

**The rule applied throughout: once the picture is shown, delete every clause
that merely restates what it shows.** A stem that shows the diagram AND
describes it has not been repaired, it has been padded — and it is EASIER
than the original, because noticing the feature was half the thinking tested.
A POINTER stays ("find the ladybirds"); a DESCRIPTION goes.

### Still to do
The remaining 179 non-frozen rows (87 confirmed, 92 borderline) are NOT done.
The frozen set was taken first because those rows sit inside the automatic
composition window and reach pupils from Mon 28 Sep; the rest do not have
that deadline. The machinery they need is built and landed, so they are
content work on a working system, not a new build.

## 5. Rendering

| surface | state |
|---|---|
| KS3 lesson pages | ✅ live — every drawn figure reads at 390, 768 and 1440 (`ks3_figure_sweep` green) |
| worksheet PDF | ✅ real vectors, with the too-tall guard |
| worksheet DOCX | ✅ raster via `@resvg/resvg-js`, cached per figure id per process |
| teacher Set work preview / swap | ✅ the three seals lifted; figure rows are now offerable |
| pupil's assignment page | ⚠️ **NOT DONE** — see below |
| practice | ⚠️ **NOT DONE** — the column ships in the migration; the renderer does not |
| KS4 lesson-page quizzes | ⚠️ **NOT DONE** |

⚠️ **The pupil-facing render is the largest thing this run did not finish.**
`shared/student-live.js` still discards the served `figure` (`g: null`), and
the template's figure slot is still wired to seven hard-coded Design demo
keys. The backend SERVES the figure — that half is done and tested — but the
page still throws it away.

**What this means concretely:** a teacher can set a figure-bearing question
and print it correctly, and the pupil answering it on screen still sees no
diagram. So the landmine in §2 is NOT yet removed for the pupil surface; it
is removed for Set work and the worksheet.

Until that lands, the KS3 production load must NOT go out — loading figure
ids that the pupil's page cannot draw would put MORE "look at the diagram"
questions in front of children, which is the exact defect this run exists to
remove. That is why §7 reports nothing loaded to production.

## 6. Accuracy and the examiner pass

### The pass caught a physics error this run had itself introduced

`p10-motor-arrows-marked` (for the frozen row `p10-05-h02`) was drawn with
its two force arrows **the wrong way round**, and its docstring asserted the
error confidently: *"the left wire carries current INTO the page (⊗) and
feels an upward push."*

It does not. F = I L × B, with x̂ right, ŷ up, ẑ out of the page: the field
runs N (left) to S (right) so B = +x̂; the left wire's current goes into the
page so L = -ẑ; and (-ẑ) × (x̂) = **-ŷ — a DOWNWARD push.** Fleming's left
hand agrees: index finger right, second finger into the page, thumb down.

**Why it nearly survived.** `p10-05-h02` asks why the two arrows must be the
same LENGTH, so the swap did not change the correct answer, and no gate can
see it — the sweep measures readability, not physics. The lesson's own prose
says only "one up and one down", which is true either way. It was caught by
rendering the figure and reading it against the rule.

A motor diagram that turns the wrong way teaches the wrong thing, and an
examiner would mark it wrong. Corrected, with the wrong reasoning kept in the
drawer's docstring rather than quietly swapped.

### What else the pass checked
- every AQA symbol against the symbol sheet — in particular the three pupils
  confuse: plain rectangle = fixed resistor, rectangle with a line through =
  fuse, variable resistor's diagonal carries an ARROW, the thermistor's line
  turns up with no arrowhead, the LDR's two arrows point IN (light, not heat)
- every graph carries labelled axes WITH UNITS
- no figure makes a distractor true — `ks4-circuit-symbols-h04`'s circuit is
  drawn deliberately WITHOUT the ammeter, because the question asks where one
  should go; `ks4-covalent-bonding-s04`'s ammonia is drawn deliberately WRONG,
  because the stem is about a student's mistaken drawing
- no alt text names the component a question asks the pupil to name

## 7. What is live on production

**Nothing. No production write of any kind was made by this run.**

| | state |
|---|---|
| production DDL | none — forbidden, and none attempted |
| production content load | **not done**, deliberately — see §5 |
| production reads | yes, read-only: the frozen-window re-check and the guard's baseline |
| TEST | migration applied (forward → rollback → forward); no content loaded |

**Why the KS3 production load was NOT run**, despite the brief asking for it:
the pupil's assignment page still discards the `figure` it is served. Loading
the repaired rows would ship stems that say "look at the diagram" to a
surface that cannot draw one — strictly worse than the defect being fixed.
The repaired stems are SAFE on the worksheet and in Set work, and unsafe on
the page a child actually answers on, so the load waits for the renderer.

The three proofs are wired and ready (`export_ks3_questions.py --verify`
gives aggregate checksum, row-by-row comparison and the anon-read negative
control), and `frozen_window_guard.py --baseline` already holds the
before-state captured from production for the byte-identical proof.

## 8. The KS4 `figure` column — migration md5s and the production-load command

**Production was NOT touched. No DDL, no `supabase db push`, no `--load prod`.**
The chat applies the column and then tells Mide to run the load.

### The migration

Two nullable `text` columns, additive, `add column if not exists` (safe to run
twice), no data migration, no RLS change, no index:

| | file | md5 |
|---|---|---|
| forward | `supabase/migrations/20260923120000_mrb352_figure_columns.sql` | `49522dcc44b27f6b56801d88fb8b80eb` |
| rollback | `supabase/rollbacks/20260923120000_mrb352_figure_columns_rollback.sql` | `3519fe66ae688a01ffbc52bbaa2d19ab` |

⚠️ **It adds TWO columns, not one.** `ks4_assignment_bank.figure` is the one
the brief named. `ks3_ladder_questions.figure` is added alongside it because
requirement 4 includes PRACTICE, and practice serves the ladder mirror — three
of the audit's confirmed rows are ladder rungs, and a rung with nowhere to put
a figure id is a rung this run cannot fix. Same shape, same manifest, same
nullable/read-optional contract. Flagged here loudly because it is a scope
addition to the named branch, not a silent one.
`ks3_assignment_bank.figure` already existed (MRB-288) and is untouched.

### Rehearsed on TEST (`qeppkiswvclkkwbxmlok`), full cycle

1. before — `information_schema.columns` → `[]`, neither column present
2. forward → both present, `text`, nullable
3. rollback → both absent again
4. forward again → both present
5. the absent-column probe proved against a genuinely nonexistent column,
   returning exactly the `42703 … does not exist` shape `_has_figure_column()`
   keys off
6. `_has_figure_column()` run live against TEST with the column present → True

TEST is left **forward-applied**, ready for the KS4 content load.

### Working with OR without the column

`export_ks4_questions.py` probes once and, when the column is absent, drops
`figure` from the INSERT list, from the row comparison and from **both sides**
of the checksum — so an unmigrated project compares like-for-like instead of
reporting phantom drift on all 16,765 rows. It prints a "column-absent mode"
line rather than failing. The backend does the same on its bank column lists.

### The exact production-load command (for Mide, after the chat applies the column)

```bash
python3 export_ks4_questions.py --subject <subject> --load prod
python3 export_ks4_questions.py --subject <subject> --project prod --verify
```

The literal token `prod` must be typed in full; the key is read only from
`~/.mrbadmus/prod.env`; and the target is proved from the key's own JWT `ref`
claim (`urklkrwevjtlfbwnipjn`) rather than from any URL beside it.



### New: `frozen_window_guard.py` (fast) — the exception made narrow

MRB-335 froze `bank_position` 0–11, but **nothing in the estate hashed a frozen
row's CONTENT.** `ks4_pool_check` check 4a only re-derives that positions 0–11
still hold 4 easier / 4 standard / 4 harder. So before this run, a content
change to a frozen row nobody meant to touch would have passed every gate.

That was tolerable while no one was allowed to edit a frozen row. It stops
being tolerable the moment 28 of them may be edited. So the exception ships
with the gate that bounds it:

1. every frozen row NOT on the 28-id allowlist is byte-identical to production
2. an allowlisted row may differ ONLY in `text`, `options`, `figure` — `id`,
   `band`, `tier`, `triple_only`, `bank_position` must be unchanged
3. the allowlist is exactly 28 ids, none stale, none outside the window
4. positions 0–11 hold the same IDS IN THE SAME ORDER per leaf — stronger than
   the 4/4/4 count check, and the property that actually keeps every
   auto-composed assignment stable

It reuses the exporters' own `checksum()` normalisation and
`_has_figure_column()` probe rather than re-implementing either — a second
implementation of a hash is a second thing to drift.

⚠️ **It SKIPS LOUDLY (exit 3) rather than passing** when it cannot read
production: *"This is NOT a pass. The frozen window has not been compared
against anything."* A gate that quietly passes when it checked nothing is
worse than no gate. `--baseline <file>` captures the fingerprints to disk so
the same comparison can be made offline, and before/after a load.

**Before-state, captured from PRODUCTION and verified:**

```
allowlist   28 id(s) (14 confirmed, 14 borderline), 0 stale, 0 moved outside the window
✅ KS3  2220 frozen authored, 2220 in reference, 0 unexpected diff(s), 0 leaf order mismatch(es)
✅ KS4  3168 frozen authored, 3168 in reference, 0 unexpected diff(s), 0 leaf order mismatch(es)
```

5,388 frozen rows, all byte-identical, leaf order intact. The same command is
re-run after the content lands; §7 carries the after-state.

## 9. Screenshots — for Mide to eyeball

All in `$MRB_SHOTS` (`~/tmp/mrb352-shots`).

**The figures, cropped, at phone (390px) and desktop (1280px)** — 24 files,
`fig_<id>_<phone|desktop>.png`:

| figure | what it shows | for |
|---|---|---|
| `p8-lamp-symbol` | a circle with two lines crossing inside it | "Which component's circuit symbol is shown?" |
| `p8-resistance-chart-recap` | the log-scale resistance chart, Ω→TΩ | "Why is its axis built like this?" |
| `p4-resultant-beam-recap` | three bars to one scale, 40 N = 25 N + 15 N | "Why do the two lower bars fill the top one?" |
| `p10-motor-arrows-marked` | coil between N and S, ⊗ pushed down, ⊙ pushed up | "Why must they be the same length?" |
| `p10-horseshoe-field-gap` | parallel field arrows between the jaws | the borderline P10 row |
| `p9-charge-matrix-grid` | the nine charge combinations, one "Nothing" cell | "How many give no force at all?" |
| `p9-field-point-marked` | a field map with one point marked, NO force arrow | drawing the push would give the answer |
| `b10-height-bars-touching` | touching bars, axes "height / cm" and "number of students" | "What are the touching bars claiming?" |
| `b4-gas-exchange-bars` | three bars, the net bar asserted = photo − resp | "What is the third bar showing?" |
| `b3-digestion-timing` | all six charted stops | comparing stomach and small intestine |
| `b5-egg-sperm-scale` | egg vs sperm diameters to one scale | the twenty-times claim |
| `c1-particle-states` | solid/liquid/gas, one reference particle each, same size | "Why does the diagram do that?" |

**The pupil's page**, both widths, both themes: `q2_*`, `q3_*`
(`_360_light`, `_360_dark`, `_desktop_light`, `_desktop_dark`).
⚠️ The `q2_*` set was captured BEFORE the paint fix and shows the
solid-black-disc bug — kept deliberately as the before/after pair.

## 10. Gates

All green at the tip: verify_questions (185 lessons, 16,946 questions, nine
checks), verify_answer_positions, pool_ownership, question_bank,
ks4_pool_check, verify_answer_lengths, set_work_scope_check,
gate_watches_check (53 gates), gate_coverage, build_figures,
ks3_figure_sweep ("every drawn figure reads at 390, 768 and 1440"),
student_behaviour, student_parity, ks3_instrument_liveness,
consumer_flag_off, frozen_window_guard.

Backend: worksheet 428+, set_work_v2 452, ks4_bank_read 35,
assignment_compose 109, compose_subject_scope 30, generate_week_guard 16.

## 11. Decisions I made

**1. `figure` holds an ID, never an SVG blob.** The drawing lives in one
build-time manifest that every consumer resolves by id. Storing SVG in the
column would bloat every bank row and every md5 proof, make a drawing fix
require a bank re-load, and duplicate alt text per row. The manifest is
mirrored to the backend the way `curriculum-tree.json` already is
(`curriculum_tree_mirror`), so this is an existing proven pattern, not a new
idea.

**2. The migration adds TWO columns, not one.** The brief named
`ks4_assignment_bank.figure`. I added `ks3_ladder_questions.figure` alongside
it because requirement 4 includes practice, practice serves the ladder mirror,
and three confirmed rows are ladder rungs — without it those three cannot be
fixed at all. Same branch, same rehearsal, named loudly here and in the
migration's own comment rather than slipped in.

**3. `@resvg/resvg-js`, not `sharp`, for the DOCX raster**, and rasterise once
per figure id per process with the result cached (the `_markPng` precedent).
Render Starter is 512MB with ~180MB headroom at the permitted concurrency, and
those numbers were measured with no image decoding in the pipeline at all.
Caching by id means raster cost is bounded by the size of the figure catalogue
(tens), never by question count — so a 1,450-question worksheet does not
invalidate the existing concurrency thresholds.

**4. The manifest carries only figures a QUESTION references.** A lesson figure
is already inlined into its lesson page at build time; shipping all of them to
a pupil's phone is pure download weight. Measured 452KB total, 409KB of it KS3
lesson figures that no question looks up. Restricting to referenced ids, and
splitting the site manifest per key stage, keeps a KS3 pupil from downloading
KS4 circuit symbols. The manifest now tracks demand rather than supply, and
grows by itself as content references arrive.

**5. `ks4-circuit-symbols-h02` left byte-identical** despite being on the
allowlist — its marked-correct answer misidentifies the AQA symbol, so drawing
it faithfully would print the error instead of merely describing it. Fixing it
means changing the science, which is Mide's sole gate. Escalated, not decided.
See `ACCURACY-ESCALATIONS.md` E1.

**6. The two bonding lesson-quiz rows left byte-identical** — they sit under
the separate eight-frozen-fields law in `architecture_v2.md`, which Mide's
23 Sep ruling does not cover. No gate enforces that freeze, which is exactly
why it was looked up rather than tested. Escalated. See E2.

**7. Alt text describes geometry, never identification.** "A rectangle with a
diagonal arrow drawn across it", not "variable resistor". Describing the shape
is not giving the answer away — it is what a sighted pupil already sees, and a
screen-reader user is entitled to the same information, no more and no less.

## 12. The most instructive failure of this run — a green suite over a fixture that did not occur

Worth writing up properly, because the suite was green and the feature did not
work, and the gap between those two facts was invisible from inside the tests.

The backend's worksheet work reported **422 assertions passing, 0 failing**,
including named proofs that a figure produced real drawn vector content in the
PDF, that the DOCX carried an image part, that the raster cache worked, and
that the too-tall guard shrank to a floor. All true. All measured against
**three hand-written placeholder figures.**

I mirrored the real manifest across and drove one large render. Every
figure-bearing PDF died at the first figure:

    ERR figure svg: unsupported element <title>

`ks3_art/kit.py`'s `_svg_open` REFUSES to emit a figure without `<title>` and
`<desc>` — they are what `role="img"` and `aria-labelledby` point at. So those
elements are on 36 of the 41 real figures, and the translator rejected every
one of them. **The PDF half of the feature could not render a single real
figure, with 422 assertions green over it.**

Measuring the corpus rather than guessing then showed the subset was short by
more than that one element:

| element | in how many of the 41 real figures | supported before |
|---|---:|---|
| `title` / `desc` | 36 | ❌ threw |
| `text` | **23** | ❌ threw |
| `defs` / `marker` | 2 | ❌ threw |

`<text>` is the serious one: it carries the axis labels and units that this
ticket makes an accuracy requirement. A graph printed with no axis labels is
not a cosmetic loss, it is a wrong diagram.

**What actually went wrong** was not the subset — a narrow subset that fails
loudly is a good design, and it is kept. It was that **the fixtures were not
drawn from the real corpus**, so the tests could only ever prove the
translator handled shapes the translator's author had already thought of.

**The fix that matters** is therefore not "add these elements". It is the
assertion now required: push EVERY figure in `figures.json` through both
renderers and fail if any one throws. 41 small SVGs, cheap, and it is the only
thing here that would have caught this without a human driving a real render.

This is the `project_cold_pass_value` lesson again, in a new place: a green
drive is evidence only about what it watches, and a fixture is part of what it
watches.

## 13. Deviations

**Deviation: the brief asked for the KS3 production load → not done → the
pupil's page still discards the figure.** Loading repaired stems onto a
surface that cannot draw them is worse than the defect. Named in §5 and §7,
with the renderer now in progress. This is the one deliberate departure from
the brief's instructions, and it is the one I am most confident about.

**Deviation: the migration adds TWO columns, not the one named.**
`ks3_ladder_questions.figure` alongside `ks4_assignment_bank.figure`, because
requirement 4 includes practice and practice serves the ladder. Same branch,
same rehearsal, flagged in §8 and in the migration's own comment.

**Deviation: `tools/mrb338_leafcheck.py` was edited.** The brief said content
lands through `mrb338_land.sh`; that script's leaf checker predates the
ruling and failed every one of the 28 authorised edits, so nothing could
land through it at all. Taught it the allowlist — narrowly (only those 28
ids; an id change is still a hard failure) and loudly (every waiver prints by
row and field). This implements the brief's own instruction to make the
exception explicit in the tooling; it is not a weakened gate.

**Deviation: `build_ks3.py`'s `r_figure` was edited** — a high-collision
shared file. Three guarantees had to live somewhere, and the drawer was the
wrong place because one page renders the same art through BOTH the figure
and inline paths. See the commit for the reasoning.

**Deviation: the RSS measurement the backend brief asked for was run by me,
not the agent**, after it reported the gap honestly rather than inventing a
number. That turned out to matter: the measurement it did run used an
unreachable scenario, and two separate recommendations to throttle production
came out of it. Both were wrong. See ACCURACY-ESCALATIONS E4.

### Mistakes I made
- **I edited tracked files while `prepush_gate.py --record` was running**, twice, which invalidated receipts mid-flight (a receipt refuses to attest against a dirty tree — correctly). The right order is: finish edits, commit, then record once. Cost: two wasted slow-gate runs.
- **I mis-diagnosed the figure sweep as a concurrency artefact.** I had run the sweep while a `verify_ks3` rebuild was rewriting the same tree, which is a real hazard and was a reasonable first suspicion — but re-running it clean still failed, so the hypothesis was wrong and there were three genuine defects underneath.
- **I extrapolated a memory measurement instead of measuring it**, and recommended a production change on the strength of it. Corrected in E4, with the wrong reasoning kept.

---

## 14. Landing — what shipped, and the two defects the evidence sheet found

Written after §§1–13, at the end of the run.

### The branch is pushed

`feat/diagrams`, both repos. Site tip `c5e3bad57`.

Every slow gate this branch affects is green and carries a receipt:
18 ran fresh, 11 passed on an unchanged receipt, 6 were skipped by rule as
unaffected, 17 skipped for a missing precondition (the drive passwords this
run is forbidden to set — see below).

One red, pushed under an explicit override recorded in the history:

```
GATE-OVERRIDE: teacher_admin_foreign_class — inherited red, C7 REMINDERS x 3, untouched by this run
```

That is the inherited red CLAUDE.md already names. Its failure output this
run is the same three `C7. REMINDERS — the control is drawn on the foreign
class` checks recorded before this branch existed, and nothing here goes
near the teacher admin screen.

### KS4 is loaded to TEST, and proved there

`python3 export_ks4_questions.py --load test` → **16,765 rows upserted**.

Proved without `--verify`, which is unavailable to this run by rule
(it needs `MRB_TEST_STUDENT_PASSWORD`, which the brief forbids setting;
it refuses with exit 3 and says so, rather than passing quietly — the
right behaviour):

| | |
|---|---|
| project, from the service-role key's own `ref` claim | `qeppkiswvclkkwbxmlok` (TEST) |
| rows, Python / TEST | 16,765 / 16,765 |
| aggregate md5, Python | `a893b07dae87f98c04e37db48e2abba7b19f695022495dd9f1d02ddb963fbf48` |
| aggregate md5, TEST | `a893b07dae87f98c04e37db48e2abba7b19f695022495dd9f1d02ddb963fbf48` |
| rows carrying a figure on TEST | 8 — the eight repaired KS4 rows, and no others |

**Production remains untouched.** No DDL, no load. See §8 for the column
migration and the exact production command for Mide.

### The before/after evidence sheet

23 pages — one per repaired, figure-bearing frozen row (the brief asked for
12). `ba_<id>.png` in `$MRB_SHOTS`, built by a scratch script outside the
repo. BEFORE is read live from production read-only, so it is the row a
pupil would be served today; AFTER is this branch's authored Python; the
figure is the real manifest SVG, the same bytes the pupil gets. The
credited option is marked in both panels, so the question Mide has to
answer — *does the picture hand over the answer?* — can be answered by
looking.

**Two defects, both in the evidence sheet, neither in the product** — and
both worth recording, because each was a wrong belief I held and not merely
a typo:

1. **I marked the wrong option as the answer, because I assumed index 0.**
   The two key stages do not agree on where the answer lives. **KS3**
   options are dicts carrying `correct: true`. **KS4** options are plain
   strings and the answer is a separate `correct_index` column. Neither is
   reliably index 0 — `p8-01-e04` is index 1 ("a lamp"),
   `ks4-distance-time-graphs-h02` is index 1 ("slower there"). Assuming
   index 0 marks a *distractor* as the answer, in both. The authored
   content was correct throughout; only my sheet was wrong. ⚠️ This also
   narrows a belief worth not carrying forward: "authored KS4 is index-0 by
   design" is a statement about the gate `verify_answer_positions` watches,
   NOT a property of a bank row you can read positionally.

2. **The figure painted as a solid black disc — the fifth instance of the
   root cause in `figure-contract.md` §8.** The sheet is a standalone page
   and did not load `ks3.css`, so the figure's classes resolved to nothing
   and `fill` fell back to black. I had written §8 about exactly this and
   then did it again in the first surface I built afterwards. Fixed by
   reusing `build_student_port._figure_paint_css()` — the helper that
   already solves it — rather than hand-rolling a sixth variant. **The
   lesson §8 should have carried and did not: a new surface that shows a
   figure must import the paint helper, not re-derive which rules it
   needs.**

The second one is the more useful finding of the two. A documented root
cause did not stop me reproducing it, which means the documentation was
doing less work than a shared helper would. That is now the shape of the
fix everywhere a figure is drawn.

### Still not done

Unchanged from §4: the 179 non-frozen rows (87 confirmed, 92 borderline),
and the KS3 production load, which stays held for the reason in §13 —
the renderer that draws these figures lives on this branch and is not
merged, so loading repaired stems to production now would put "Look at the
diagram" in front of pupils on a site with no diagram.
