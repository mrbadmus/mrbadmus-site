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

Emitted by `build_figures.py` (step 1 of `build_all.py`):
- **site** `shared/figures-ks3.js` / `shared/figures-ks4.js` — one per key
  stage, `window.MRBFigures = Object.assign(window.MRBFigures || {}, {…})`.
  KS3 carries only ids a question references.
- **backend** `figures.json` — the whole manifest, mirrored; the
  `figures_mirror` gate (`build_figures.py --mirror`) compares the backend's
  copy byte for byte, finding the checkout the way `curriculum_tree_mirror`
  does. `figure_manifest` (`build_figures.py --check`) proves the committed
  site files match a fresh build.

## 3. Where drawings come from

⊕ **MRB-352 run 2 (24 Sep 2026): from ONE place — `figlib/`**, Mide's
diagram library brought into the repo as a package (provenance, changes and
the full SVG subset: `figlib/README.md`).

- **KS3 question figures**: `figlib/catalogue_ks3.py`. SAME ids the questions
  already used, SAME meaning, redrawn in the exam-paper house style. KS3
  **lesson** pages are untouched and still draw their own figures with
  `ks3_art` (architecture law), so one id may have two drawings — the
  lesson's and the question's. That is deliberate.
- **KS4**: `ks4_art/catalogue.py` + every `ks4_art/catalogue_*.py` — now
  declarative records only. Their `art` names a builder in `figlib.ART`.
- `verify_questions` check 5 resolves a KS3 question's figure against
  `figlib/catalogue_ks3.py` (it used to ask the lesson, which passed a
  `css-art` figure no question surface could draw).

~~Superseded:~~ *"KS3: already declared in `LESSON["figures"]` and drawn by
`build_ks3.SVG_ART[art](fig)`. `build_figures.py` reuses that registry
verbatim — the lesson page and the question render the SAME bytes. KS4: a
new declarative catalogue drawn by a new `ks4_art/` package whose modules
`from ks3_art.kit import …`."* Kept because it is why run 1's figures
painted through `ks3.css` classes — see §8.

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

## 8. A FIGURE CARRIES ITS OWN PAINT — and the manifest now guarantees it

⊕ **MRB-352 run 2 (24 Sep 2026).** Every figure in the manifest is
**self-painting**: every fill and stroke is an attribute on the shape
itself; there is not one `class=`, `style=` or `var(` in any manifest SVG.
`build_figures.py` enforces it as a hard failure — it refuses to write any
figure if one breaks it — together with the rest of `figlib.checks`: the
worksheet translator's element/attribute subset, AA contrast against what
each label actually sits on, no text on a dark fill, ≥ 11px text and ≥ 1px
strokes in a 320px box, no motor and no d.c. box, Georgia first (or the one lining-figure stack
`style.NUM_FONT` on a label with a digit — `figlib/README.md`). The
`figure_manifest` gate runs the same checks on every push.

**So a consuming surface supplies NO paint.** Put the SVG in the page and
it draws. The figure is a cream paper card of its own (its first shape, a
rect marked `data-role="paper"`), in light and dark mode alike; a print
renderer may drop that one rect on white paper.

Retired, because there is nothing left for them to compensate for:
- `_figure_paint_css()` in `build_student_port.py` — deleted (it extracted
  `ks3.css` rules and `--ks3-*` tokens into the assignment page).
- backend `figure-render.js` `CLASS_STYLES`, `CLASS_STYLE_BLOCK` and
  `KS3_TOKENS` — no longer needed by any manifest figure (workstream B).

### What the rule learned, kept so nobody reintroduces a class

Run 1's figures set colour by CSS class (`ks3-cband-symstroke`,
`ks3-p10fig-*`, …) defined in `shared/ks3.css`, which only a KS3 lesson page
loads. Every other surface failed, silently:

| surface | what happened |
|---|---|
| worksheet PDF | six class-only figures drew a `fill:none` frame as a **solid black rectangle** |
| worksheet DOCX | resvg does not throw on an unresolved `var()` — it painted **zero pixels** |
| pupil's page (1) | `p8-lamp-symbol` painted as a **solid black disc**, crossing lines gone |
| pupil's page (2) | rules copied WITHOUT their tokens → `stroke: var(--ks3-ink)` invalid → **stroke fell back to `none`, figure invisible** |
| evidence sheet | a standalone page without `ks3.css` → the black disc again, a fifth time |

Five surfaces, one cause, and a documented rule did not stop the fifth. The
fix that holds is not a better-documented compensation on each surface; it
is a figure that needs none, checked where it is built.
