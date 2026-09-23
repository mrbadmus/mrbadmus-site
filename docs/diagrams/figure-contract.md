# The figure contract — one shape, four consumers

Every consumer resolves a figure the same way: **by id, against one build-time
manifest**. Nothing stores or transports SVG per question.

## 1. The `figure` field on a question row

- KS3 bank (`ks3_data/<unit>/questions_NN_*.py`): key `"figure"`, already
  exists, value is a figure id or `None`. Column already on the table.
- KS4 bank (`ks4_data/questions/<subject>/*.py`): key `"figure"`, NEW,
  value is a figure id or `None`. Column ships separately (see §6).
- KS3 ladder rungs and KS4 lesson-page quiz items: key `"figure"`, NEW.

A figure id is `[a-z0-9-]+` and must exist in the manifest. Unknown id = build
failure, never a silent blank.

## 2. The manifest

Built by `build_figures.py`. One record per figure:

```json
{ "<id>": { "svg": "<svg …>…</svg>", "alt": "Circuit symbol: thermistor",
            "w": 320, "h": 200 } }
```

Emitted to two places, byte-identical payload:
- **site**   `shared/figures.js`  — `window.MRBFigures = {…}`
- **backend** `figures.json`      — mirrored, guarded by a `figures_mirror`
  gate in the shape of the existing `curriculum_tree_mirror`
  (`tools/export_curriculum_tree.py --check`). Same proven pattern.

## 3. Where drawings come from

- **KS3**: already declared in `LESSON["figures"]` and drawn by
  `build_ks3.SVG_ART[art](fig)`. `build_figures.py` reuses that registry
  verbatim — the lesson page and the question render the SAME bytes. No fork.
- **KS4**: a new declarative catalogue `ks4_art/catalogue.py`, records of the
  same shape (`id`, `art`, `title`, `alt`, params), drawn by a new `ks4_art/`
  package whose modules `from ks3_art.kit import …`. **Primitives are shared,
  never copied.** New shared primitives (line/curve plotter, formula/force
  triangle) go INTO `ks3_art/kit.py` so both key stages get them.

## 4. Alt text — a hard rule

Every figure carries `alt`. It names WHAT IS SHOWN, never what the answer is.
  ✅ "Circuit symbol: a resistor with an arrow through it"
  ❌ "Circuit symbol: variable resistor"   ← if the question asks to name it
Alt lives on the figure record. Where one figure serves several questions whose
answers differ, alt must be answer-neutral for ALL of them.

## 5. Rendering (four surfaces, one lookup)

| surface | how |
|---|---|
| pupil's assignment page | new `figure` node in `shared/student-runtime.js`; the ONLY innerHTML sink, fed exclusively from the manifest — never from question data |
| practice | same node; practice reads `ks3_ladder_questions`, which gains a `figure` column |
| lesson-page quizzes | `generate_site_v5.py` inlines the SVG at build time |
| teacher Set work preview / swap | same manifest, loaded by `shared/set-work.js` |
| worksheet PDF | PDFKit native vectors |
| worksheet DOCX | `@resvg/resvg-js`, rasterised once per id per process and cached (the `_markPng` precedent) |

⚠️ The SVG string is TRUSTED build-time output. Question text and options stay
on the existing `createTextNode` path and are never given an innerHTML sink.

## 6. The KS4 column

`ks4_assignment_bank.figure text` — migration + rollback on branch
`feat/ks4-figure-column`, rehearsed on TEST (forward → rollback → forward).
**Not applied to production by this run.**

Site and backend must both work WITH OR WITHOUT the column:
- exporter writes `figure` only when the column exists (probe once);
- backend `BANK_COLS` KS4 arm adds `figure` only when present, else serves
  `figure: null`.

## 7. What must be threaded, or the field is silently dropped
`ks4_data._check` (validate), `ks4_data.load_pool` row `dict(...)`,
`export_ks4_questions.COLUMNS` + `checksum()` + `sql_cell()`.
The KS4 validator ignores unknown keys, so an unthreaded `figure` vanishes
without any error at all. This is the single easiest way to ship nothing.

## 8. ⚠️ A FIGURE MUST CARRY ITS OWN PAINT — the rule this feature learned four times

A manifest figure's SVG sets colour by **CSS class** (`ks3-cband-symstroke`,
`ks3-p10fig-*`, …), and those classes live in `shared/ks3.css`. That is fine
on a KS3 lesson page, which loads it. **Every other surface must supply the
paint itself**, and the failure is silent and ugly:

| surface | what happened |
|---|---|
| worksheet PDF | six class-only figures drew a `fill:none` frame as a **solid black rectangle** |
| worksheet DOCX | resvg does not throw on an unresolved `var()` — it painted **zero pixels** |
| pupil's page (1) | `p8-lamp-symbol` painted as a **solid black disc**, crossing lines gone |
| pupil's page (2) | rules copied WITHOUT their tokens → `stroke: var(--ks3-ink)` invalid → **stroke fell back to `none`, figure invisible** |

**The rule, for the next surface:** a consuming surface must provide BOTH

1. the class rules (extract them from `ks3.css`; never retype them), AND
2. **the `--ks3-*` custom properties those rules spend.**

(2) is the one that gets missed, and it fails worse than (1): an unresolved
`var()` makes the declaration invalid at computed-value time, so the property
takes its INITIAL value — and `stroke`'s initial value is `none`. The figure
does not look broken, it looks *absent*, which reads as "no figure here"
rather than as a bug.

⚠️ `--ks3-*` is defined in `student-ds.css` only under `.rd[data-mode="ks3"]`,
the KS3 reading-mode container. A page without one has those tokens undefined
no matter which stylesheets it loads. Re-scope them to the figure wrapper.

Working implementations to copy: `_figure_paint_css()` in
`build_student_port.py` (site) and `CLASS_STYLES` + `KS3_TOKENS` in
`figure-render.js` (backend).
