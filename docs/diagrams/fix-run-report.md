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

## 4. Content: rows fixed, rows left

## 5. Rendering

## 6. Accuracy and the examiner pass

## 7. What is live on production

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

## 9. Screenshots

## 10. Gates

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
