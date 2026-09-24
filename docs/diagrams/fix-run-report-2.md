# MRB-352 run 2 — the diagrams fix run, finished and landed

Run date: 23–24 Sep 2026. Unattended. Follows `fix-run-report.md` (run 1).

## ⚠️ For the chat: the one production step left

KS4 content is on TEST only, because production still has no `figure`
column. Everything else in this run is live on production.

| | |
|---|---|
| migration | `supabase/migrations/20260923120000_mrb352_figure_columns.sql` |
| md5 | **`49522dcc44b27f6b56801d88fb8b80eb`** (unchanged since run 1; no new rehearsal needed) |
| rollback | `supabase/rollbacks/20260923120000_mrb352_figure_columns_rollback.sql` (`3519fe66ae688a01ffbc52bbaa2d19ab`) |
| adds | `ks4_assignment_bank.figure` and `ks3_ladder_questions.figure` (nullable text) |

Then, in this order:

1. The chat applies the migration to production.
2. **Restart (or redeploy) the Render backend.** The backend learns that the
   column is missing once per process and remembers it; without a restart it
   keeps serving `figure: null`.
3. From any checkout at or after `0b45476ab`:
   ```bash
   python3 export_ks4_questions.py --load prod
   ```
4. Prove it: 16,765 rows, **sha256
   `01a30073bc959b9f26b0005f3b68bc0e6c02f419f9c539e56e4f270e38aee660`**,
   **96 rows carrying a figure**; then `python3 frozen_window_guard.py`
   against live production must report 0 unexpected diffs.

Until step 1 happens, `export_ks4_questions.py --load prod` **refuses** (exit 5)
because rows being loaded carry figures and the column is absent. That refusal
is deliberate: loading the reworded "the diagram shows…" stems without the
column would put questions in front of pupils that point at a picture nobody
can see. Production's KS4 bank therefore still holds the OLD wording for the
KS4 rows this run changed, which is the safe state.

## 1. What is live on production (proved)

| | state | proof |
|---|---|---|
| backend | `main` = `86a89a8` | `/api/health` `build` field = `86a89a8d5a5d…` |
| site | `main` = `0b45476ab` | live `figures-ks3.js` md5 `efe2cfd6fc7f2df326c30c8e253b74b0`, `figures-ks4.js` md5 `a2fa6f5f66861fbbbaa0a55d61f9178b`, both equal to the committed files; `check_ks3_live.sh` 185/185 |
| KS3 bank | 16,946 rows, 85 carry a figure | sha256 Python = production `a7fdfc853fd94ea0c9da404731205ed87fdae6ccd076b687b5cf9cabbb35d5ed` |
| KS3 ladder | 370 rows | sha256 Python = production `274b7d776c0ba5c3fab179fc46fc5db3bda32d184ba9f8095b39fc5cc02b5a80` |
| KS3 cards | 869 rows, unchanged | `c09a171b608c0bc5941fa88dbf6a24903ae7943ff13a70579b37189ed1846863` |
| auto windows | 185 KS3 leaves, **0 broken** (positions 0–11 contiguous, 4/4/4 bands, one correct option, every figure id in the shipped manifest) | per-leaf script, `~/tmp/mrb352-run2-shots/land-b4/ks3proof.py` |
| RLS | anon read of `ks3_assignment_bank`, `ks3_ladder_questions`, `ks4_assignment_bank` returns `[]` | public anon key |
| frozen window | every frozen row NOT among the 28 is byte-identical to production; the 28 changed only permitted fields; leaf order intact | `frozen_window_guard` run LIVE against production after each KS3 load, and against a pre-load snapshot |
| KS4 | TEST only: 16,765 rows, sha256 `01a30073…e660`, 96 figure rows | Python = TEST |

**The figures draw on the live site.** Proved by driving the live
`mrbadmus.com` pages in headless Chrome with the Supabase and backend calls
answered locally, so the live JavaScript and the live manifest did the drawing:
the pupil's assignment page and the teacher's Set work preview and swap, at
360, 390 and 1280 px, on the default and the graphite (dark) bench themes,
with no sideways scroll. Worksheets: the backend renderer at the pushed commit
drew every one of the 176 figures in PDF and DOCX (`test_worksheet.js`, 783
passed at the end). Screens: `~/tmp/mrb352-run2-shots/live/`, `live-b1/` …
`live-b4/`.

⚠️ **Two honest limits on that proof.**
- **Practice** draws no figure, because no ladder rung carries one (0 of 370)
  and the class page has no figure node for practice. The backend now serves
  `figure` on practice, so the gap is the page, not the data.
- **Dark mode.** The pupil's question view stays cream on every theme,
  including graphite with the OS in dark mode, so a figure never actually sits
  on a dark background there. The figure card is cream by design in both
  modes; it was also rendered on the graphite background to prove it reads.

## 2. What was built

- **`figlib/` — Mide's diagram library is now the one source of question
  figures.** It holds one copy of `physics_diagrams.py`, `chem_diagrams.py` and
  `bio_diagrams.py` (provenance and md5s in `figlib/README.md`), with the house
  style (cream `#F3F0E7`, dark-sage labels, near-black strokes, teal, Georgia).
  Run 1's separate drawers in `ks4_art/` are deleted; `ks4_art` now holds only
  catalogue records.
- **The black-disc bug is fixed at the root.** Every figure is now
  self-painting: all colour is inline, on its own cream card marked
  `data-role="paper"`, with no CSS class, `style=` or `var(`.
  `_figure_paint_css()` is deleted. `build_figures.py` is now step 0 of
  `build_all.py`, and it refuses to write a manifest if any figure fails
  `figlib/checks.py`.
- **The checks are hard failures, not warnings:**
  - text contrast ≥ 4.5:1 against what it sits on, and no text on a dark fill;
  - ≥ 11 px text and ≥ 1 px strokes at 360 px;
  - the SVG subset the PDF path can draw;
  - no motor symbol and no d.c. box;
  - numerals ≥ 6 units from the card edge, in lining figures;
  - every label's box, rotated labels included, ≥ 4 units from the edge and not
    overlapping another;
  - every gridline a pupil counts ≥ 3:1 against the paper.

  Each rule proves itself on known-bad drawings (`checks.self_test()`) on
  every build.
- **Backend:**
  - The worksheet renderer accepts the library's SVG.
  - Print drops the cream card, and serif text prints in DejaVu Serif.
  - The `figure` column is detected by the read itself, so production's
    missing column is served as `figure: null`.
  - Practice now serves `figure`.
- **Set work** draws figures on preview, swap and edit. Run 2 found that the
  code did not exist at all.

**Three defects the review rounds missed and only a live drive found:**
- the PDF text cursor, which printed questions on top of each other for about
  an hour on the first backend push;
- the figure manifest loaded without its cache-bust stamp, which would have
  pinned a pupil's first copy for a year;
- Set work having no figure code.

Each is fixed with a test.

## 3. The 28 frozen rows, row by row

All 28 are resolved. None is "left for Mide". Id, band, tier, `triple_only` and
`bank_position` are unchanged on every one. Mide's 23 Sep ruling that a
description question may be replaced in full is recorded in
`frozen_window_allowlist.py`.

| id | verdict | figure | the point |
|---|---|---|---|
| b10-01-e01 | revise | b10-height-bars-touching | one distractor was made true by the chart |
| b4-05-e04 | revise | b4-gas-exchange-bars | options said "above" for side-by-side bars; one why claimed both processes always run (photosynthesis stops in the dark) |
| b9-01-e03 | revise | b9-oak-wood-web-plain | **Mide's correction:** plain web on cream, dark labels, no text on a dark fill, no key |
| b9-01-s03 | revise | b9-oak-wood-web-plain | same |
| c1-02-e01 | replace | c1-three-states-particles | **Mide's correction:** solid touching and regular; liquid touching, irregular; gas far apart. It was a "why is it drawn like that" question. |
| p10-05-h02 | revise | p10-motor-arrows-marked | forces checked by F = IL × B |
| p4-02-h02 | replace | p4-crate-two-forces | a question about the picture became a real resultant-force question |
| p8-01-e04 | keep | p8-lamp-symbol | already right |
| p9-02-s04 | revise | p9-charge-matrix-blank | the filled grid gave the answer away |
| ks4-circuit-symbols-e01 | revise | …symbol-variable-resistor | **Mide's correction:** the arrow passes fully through the body |
| ks4-circuit-symbols-s03 | revise | …cell-switch-two-lamps-loop | the switch was invisible |
| ks4-circuit-symbols-h02 | replace | ks4-fig-sensor-symbols-student-a-b | **Mide's correction:** A is drawn as the AQA thermistor (credited), B as the AQA LDR; the why points at the drawings |
| ks4-circuit-symbols-h04 | revise | …battery-switch-lamp-resistor-branches | **Mide's correction:** the motor removed; run 1 had drawn one |
| ks4-acceleration-h03 | revise | …velocity-time-skydiver | the first gradient exceeded g; the alt text gave the answer |
| b10-03-h01 | revise | b10-base-pairs | letters were black on black |
| b3-05-s04 | replace | b3-gut-transit-times | its premise (16 h in the small intestine) is false |
| b5-02-h01 | revise | b5-egg-sperm-scale | compares with the sperm head |
| c1-02-e03 | no figure | — | stem pointed at a table the pupil never sees |
| p10-02-s03 | revise | p10-horseshoe-field-gap | |
| p8-06-s03 | revise | p8-resistance-chart-recap | the chart's ×1000 ticks were inconsistent (first gap ×100) |
| p9-03-s01 | revise | p9-field-point-marked | point labelled P |
| ks4-food-chains-webs-s02 | revise | ks4-fig-food-web-moorland | the prose web became a drawn one |
| ks4-covalent-bonding-s04 | revise | …molecule-nh3-missing-bond | N showed 4 outer electrons, not 5 (unintended second error) |
| ks4-condensation-polymerisation-h02 | replace | ks4-fig-polyester-monomers | AQA box notation; the product is withheld because it is the answer |
| ks4-circuit-symbols-e04 | replace | …symbol-battery-2 | **Mide's correction:** description question scrapped |
| ks4-circuit-symbols-e02 | replace | …cell-open-switch-lamp | **Mide's correction:** description question scrapped |
| ks4-direct-alternating-pd-h02 | revise | …oscilloscope-compare-5-10 | X and Y could not be told apart |
| ks4-distance-time-graphs-h02 | revise | …distance-time-runner-400m | the start implied a sprinter's 12 m/s |

**Summary: 1 keep, 20 revise, 6 replace, 1 no figure needed.**

The 16 KS3 rows are live on production. The 12 KS4 rows are live on TEST and
reach production with the command at the top.

## 4. The other flagged rows

**The count is 174, not 179.** The audit's 202 flagged rows (110 confirmed,
92 borderline) minus the 28 leaves 96 confirmed and 78 borderline. The
brief's 87 + 92 cannot be reconciled with the audit.

**All 174 are done, plus one the audit missed (`p8-01-s18`), in four batches.**
Each batch was drafted by an examiner, built, reviewed by a separate Opus
examiner and a separate visual reviewer, fixed, and re-reviewed until a pass
came back clean. Then it landed.

| batch | rows | verdicts | new figures | state |
|---|---:|---|---:|---|
| 1 · KS3 physics | 55 + 6 P10-02 field-map rows + 3 ladder rungs | 27 revise · 14 replace · 11 no figure · 3 keep | 41 | live, prod |
| 2 · biology + chemistry | 36 (34 bank + 2 lesson quiz) | 23 revise · 5 replace · 8 no figure | 28 | KS3 live on prod; KS4 on TEST |
| 3 · KS4 electricity | 44 (8 already done by the motor sweep) | 19 revise · 15 replace · 1 keep · 1 no figure | 21 | TEST (+ 4 live lesson pages) |
| 4 · KS4 physics (other) | 40 | 33 revise · 1 replace · 3 no figure · 3 keep | 34 | TEST (+ 4 live lesson pages) |

The manifest now ships 176 figures (77 KS3, 99 KS4).

**Motor sweep.** No circuit question in either bank now uses a motor symbol.
16 rows were fixed: 12 KS4 and 4 KS3.
- **h04:** frozen, allowlisted, and fixed with the 28.
- **The other 15:** none were frozen.
- **The circuit-symbols lesson page:** it taught that the motor, buzzer and
  a.c. supply are AQA symbols. It now lists exactly the AQA 8463 §4.2.1.1 set.

**Wrong credited answers found and corrected, and every one checked from its
source.** These were errors in the science, not just in how the question was
presented:

| row | what was wrong | now |
|---|---|---|
| ks4-electromagnetism-h07 | credited the wrong end of the solenoid (the grip rule was reversed) | figure drawn so the credited end is true; checked by vector on the render |
| ks4-covalent-bonding-h23 | carbon "counts four" | six |
| c6-03-h10 | explained the jump, not the flat end, of the pH curve | alkali already in excess |
| b5-03-h26 | ovulation "two thirds of the way round" | about 14 days before the end |
| p8-06-h21 | treated a gap on a log axis as a bigger ratio near the top | equal gap = equal ratio |
| p6-01-e17 | its figure printed the answer (0.45 m) | dots two waves apart, 0.90 m marked |
| b3 digestion (lesson + 5 bank rows) | 16 h in the small intestine | about 4 h (2–6); the large intestine takes longest |
| P9 explain rung + hook | "a water stream behaves the same in a vacuum" | a charged comb |

## 5. Sources for every science decision

| decision | source |
|---|---|
| **The AQA circuit symbols.** The thermistor is a diagonal line through the resistor with a short flat tail at the lower left and no arrowhead; the variable resistor's arrow passes fully through; the LDR, diode and LED are drawn inside a circle; a battery is cell, dashed wire, cell; both cell plates are equal weight. **Not on the list:** motor, buzzer, a.c. supply, d.c. box. | AQA GCSE Physics 8463 specification v1.1 (30 Sep 2019), §4.2.1.1, p.24, read from the page image. A rendered copy is at `~/tmp/mrb352-run2-shots/sources/`. |
| h02: Student A drew the thermistor, so A is correct. **Run 1's E1 escalation rested on a wrong belief about the symbol.** | same |
| resolution of forces is assessed by scale drawing only | 8463 §4.5.1.4, p.45 |
| forces on a current-carrying wire; solenoid poles | 8463 §4.7.2.1, 4.7.2.2; F = IL × B worked out on each render |
| pd–time traces, T = 1/f (so the trace leaf stays) | 8463 §4.6.1.2, §4.2.3.1 |
| radial electric field (no F = Eq at GCSE) | 8463 §4.2.5.2 |
| condensation polymerisation (box notation) | AQA 8462 v1.1, §4.7.3.2, p.69 |
| dot-and-cross electron counts | 8462 §4.1.1.7, §4.2.1.4 |
| pH, excess alkali | 8462 §4.4.2.5–4.4.2.6 |
| hormone graphs are Higher only; LH/FSH roles | AQA 8461 §4.5.3.4 |
| variation from many genes plus the environment | 8461 §4.6.1.6, §4.6.2.1 |
| gut transit times | NHS; published small-intestine transit of about 2–6 h |
| ovulation timing | NHS: 10–16 days before the next period |
| resolution, free-body and wave-front diagrams are also in Combined Higher | AQA 8464 §6.5.1.4 (p.145), §6.6.2.2 (p.157) |

## 6. Things only Mide can decide

These are all about **scope or permission**, not the science; the science is
settled above.

1. **Three frozen rows still carry the false "16 hours in the small
   intestine": `b3-05-e02`, `b3-05-h03`, `b3-05-h04`.** They sit inside the
   frozen window and are not on the 28-id allowlist, so the hard line kept them
   byte-identical. Fixing them needs the allowlist extended by three.
2. **`b9-03-e02`** (frozen, not allowlisted) has a weak why for its mice
   option. Same reason.
3. **`ks4-circuit-symbols-s02`** (frozen) describes the LDR symbol in words,
   which breaks rule 2. It was left alone for the same reason.
4. **Three KS4 leaves are tagged `triple_only` but are Combined Higher
   content:** resolving forces, free-body diagrams and wave-front diagrams
   (126 rows). So no Combined Higher pupil is ever set them. The fix changes
   `triple_only` on frozen rows and changes what automatic composition serves,
   so it is Mide's ruling, not this run's. Steps:
   - set `triple_only=False` on all rows of the three leaves;
   - add the three subtopics to `all_subtopics_physics_higher.py`;
   - re-export the curriculum tree and run `curriculum_tree_mirror`,
     `ks4_pool_check`, `ks4_pool_drive` and `set_work_scope_check`;
   - reload the production bank's flags.
5. **⚑ Two bonding lesson-quiz items were rewritten under the Bonding v2
   frozen-fields law** (`covalent-bonding#quiz7` in both higher files, and
   `states-of-matter#quiz11`). Rule 2 required the fix. The law's own procedure
   is to flag the change ⚑ for Mide's examiner review, and both items carry a ⚑
   comment. The reviewer recommends accepting both.
6. **`b1-03-e04`** (frozen) now shows a real leaf-cell drawing instead of
   pointing at one that couldn't render. The row itself is byte-identical.

## 7. Decisions I made

1. **The thermistor question was settled from the AQA spec, not escalated.**
   The page image decided it, and it showed run 1's E1 was wrong.
2. **Question figures are exam-paper style, from figlib; lesson pages keep
   their own drawings.** One id can therefore have two drawings. Brief item 7
   asked for this.
3. **Self-painting figures are the root-cause fix,** rather than a better CSS
   helper. Nothing a consuming surface does can turn one black.
4. **The cream card stays cream in dark mode.** It is paper. Legibility is
   enforced by contrast checks rather than by per-theme colours.
5. **Print drops the cream card on white paper;** its colours still meet
   contrast on white.
6. **Gridlines:** major `#8C8268`, minor `#948A70` and thinner, from one shared
   definition, with a 3:1 check. The first choice, `#A89E86`, measured 2.33:1
   and was rejected.
7. **Numerals are set in a lining-figure serif** (Times New Roman → Noto
   Serif), because Georgia's old-style "0" reads as "o" on axes.
8. **The circuit-symbols and trace lesson quizzes were rewritten as text,**
   not given figure support. That support would rebuild 300+ KS4 pages; the
   rewritten questions describe nothing.
9. **Legends that state the arrow convention were removed from every food
   web** (blackbird, oak wood, moorland). AQA webs carry no key, and a key
   rules out the arrow-direction distractor.
10. **Six "name this symbol" stems got distinct wordings.** Identical stems are
    dropped as duplicates by Set work, which would have shrunk the pool
    silently.
11. **The weight–mass figure uses 3.8 N/kg, not 3.7,** so the end point sits
    on a gridline and the reading is exact. The planet is unnamed.
12. **Merged `main` into long branches rather than rebasing.** The branches ran
    to 20+ commits over a 2,600-file restamp; generated output was rebuilt
    with `build_all.py`, never hand-merged.
13. **Rebased the backend onto a new branch (`feat/diagrams-2`) rather than
    force-pushing** the old one.
14. **Built the 174 in four parallel worktrees**, with new builders in new
    modules and new records in new catalogue files, so merges stayed small.
15. **Fixed small adjacent defects in passing:**
    - the Set work step label breaking as "DETAI / L" at 360 px;
    - the P9 lesson's vacuum claim;
    - stale docstrings;
    - CLAUDE.md's generator count, now seven, with `build_figures.py` as
      step 0.
16. **The inherited reds were pushed under the same `GATE-OVERRIDE` text as
    before:**
    - `teacher_admin_foreign_class`, C7 REMINDERS ×3;
    - `set_work`, the same 3 of 424.

    One new red, `set_work`'s `preview_figures_drawable`, was fixed by loading
    TEST first rather than overridden.

## 8. Deviations

- **The shared session scratchpad was wiped from outside mid-run**, deleting
  the specs, reviews, the evidence tool and the landing scripts. Nothing in
  either repo was affected. Every file an agent had written was recovered from
  the agent transcripts into `~/tmp/mrb352-run2-shots/recovered/`, and all
  later working files went there.
- **One figure change reached production** before the backend's PDF
  text-cursor bug was found: about an hour, worksheets only. It was fixed
  forward, not reverted.
- **`MRB_DRIVE_PASSWORD` and `MRB_TEST_STUDENT_PASSWORD` were never set.**
  `export_ks3_questions --verify` and `student_controls_drive` were replaced by
  service-role checksums and intercepted live drives.

## 9. Evidence for Mide

**Before/after sheets:** `~/tmp/mrb352-run2-shots/index.html` holds 201
pages.
- BEFORE is each row as it was live on production, read before that batch's
  load.
- AFTER is the authored row with the real figure the pupil gets, credited
  option marked.

**Reviews:**
- `~/tmp/mrb352-run2-shots/reviews/`
- the round-1–3 files in `recovered/`

**Figure renders at every width, light and dark:** `review*/`, `b*-*/`.
