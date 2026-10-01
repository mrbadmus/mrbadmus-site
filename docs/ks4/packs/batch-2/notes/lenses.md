# lenses — author's notes (batch-2)

## Lesson record

```python
dict(slug="lenses", source_file="lenses.dc.html",
     subject="physics", topic_id="waves",
     title="Lenses", spec="4.6.2.5", family="Model",
     routes=["TF", "TH"], review_state="draft", batch="batch-2",
     block_map={"s-bench": "practical", "s-build": "worked-example", "s-eye": "check"})
```

`block_map` is needed for the three lesson-built sections. The pilot's
series-parallel lesson maps its bench to "practical" too. All 13 sections
classify through the real compile path in a scratch build.

Spec: AQA 8463 4.6.2.5 (physics only). It is not in 8464. The pack header's
"6.6.3" is wrong twice over (examination §1). The eyebrow reads "AQA Physics
(8463) 4.6.2.5 · Model" and the key note "AQA 4.6.2.5 (8463)". The spectacles
section is labelled with its true home, AQA Biology 4.5.2.3.

## Family: MODEL, and why

One structure, the ray model (two or three standard rays from the top of the
object), predicts every image a lens makes. The flagship is a parameter
instrument with a prediction at each change of regime, which is what MODEL
asks for. BATCH-PLAN's provisional family is confirmed.

## Instruments and the demand each trains

- **Flagship (L) — the lens bench** (`s-bench`). Per the commander's brief, the
  pupil moves an object along the axis of a convex lens (f = 10 cm) through
  five regimes: 30 cm (beyond 2F), 20 (at 2F), 15 (between F and 2F), 10 (at F)
  and 6 (inside F). A range slider (keyboard and touch) and a "Next position"
  button move it. Before any ray is drawn, the pupil predicts real / virtual /
  no image, magnified / same size / diminished, and upright / inverted. "Draw
  the rays" is locked until those are in. The three standard rays then draw
  themselves on (SMIL stroke-dash, 1 s), and traced-back dashed lines and the
  image fade in after them; with reduced motion all of it appears at once.
  Verdicts are per property, plus a why line. A readout links to the equation:
  image distance, which side, image height, and "magnification = h ÷ 4.0 = …".
  A Concave tab adds two more set-ups (30 cm and 6 cm), which show that the
  regime never changes. That makes 7 set-ups in all.
  Ray geometry: thin-lens v = uf/(u − f), drawn with AQA's convention of one
  bend at the centre line. The plate uses an affine stretch (10 px/cm across,
  15 px/cm up) so tall images fit. That keeps rays straight and crossings
  exact; the legal line says so.
  Demand: predict and then describe the image (the three properties AQA marks)
  from the object's position relative to F and 2F.
- **Mid-size 1 — "Complete the ray diagram"** (`s-build`). This is the "do"
  half of the bench's watch. Four steps: where ray 1 goes after the lens,
  where ray 2 goes, where the image top is, and then, with the object inside F,
  where the virtual image is (trace back with dashed lines). Each step accepts
  the right choice and redraws the figure. A wrong choice gets its
  misconception feedback and the pupil tries again. Demand: the construction
  rules behind "Complete the ray diagram" (Law 6, production of a drawing, in
  choice form).
- **Mid-size 2 — Ks4Sort "Convex, concave, or both?"** (`s-sort`), seven
  statements. Demand: compare the two lenses, which is what AQA's 4-mark
  Compare question asks for.
- **Micro — the spectacles predict** (`s-eye`, Ks4Choice with a drawn
  short-sighted eye).
- **CFIFA** (`Ks4Cfifa`) on magnification. The source has no FIFA examples, so
  everything is new (⚑). Foundation and Higher numbers differ (`R.isHigher`):
  - Foundation worked: 10 cm ÷ 4.0 cm = 2.5 (nothing to convert);
    7.0 mm ÷ 2.0 cm → 20 mm, = 0.35 (convert). Attempts: 12 ÷ 3.0 = 4.0;
    6.0 mm ÷ 2.4 cm → 24 mm, = 0.25.
  - Higher worked (rearranging): 0.40 × 15 cm = 6.0 cm (nothing to convert);
    2.6 cm wing image ÷ 4.0 mm → 26 mm, = 6.5 (convert). Attempts: object =
    18 ÷ 2.4 = 7.5 cm; 6.0 mm → 0.60 cm, 0.60 ÷ 0.25 = 2.4 cm.
- **Equation block**: "On the sheet": magnification = image height ÷ object
  height, with the rearrangement and a units card (same unit, mm or cm; no unit).

No required practical: 8463 has no lens RP, only an AT 4/8 opportunity
(examination §5).

## Misconceptions and where each is confronted

| misconception | where | form |
|---|---|---|
| "A convex lens always forms a real image" (pack `common_mistake`) | bench, the moment the object goes inside F | three-beat Think-again panel |
| "Convex lenses always magnify" (examination §5) | hook (the window looks smaller), bench at 30 cm, r4 reject line | prediction verdict |
| "Concave lenses can form real images" | Concave tab; sort; rung 3 | verdict and why; chain red herring |
| Ray through the centre drawn bending; ray through F still diverging after the lens | constructor step 2 | distractor feedback |
| Image placed where only one ray reaches / at F | constructor step 3 | distractor feedback |
| Virtual image found without dashed back-extensions | constructor step 4 | the correct option names the dashed lines; the figure draws them |
| "Real image = upright" | bench verdicts | verdict |
| Magnification given a unit; heights in mixed units | equation units card, CFIFA convert step and notes, rung 2 unit select ("no unit") | worked "unconverted gives …" notes |
| Myopia corrected with a converging lens | `s-eye` | distractor feedback |

## Command words

Describe the image, Complete the ray diagram, Calculate, Compare. The ladder
uses State (r1), Calculate (r2), Explain (r3) and Compare (r4); Explain is
already used throughout.

## Ladder

- r1: `K.find(slug, R.route, 'magnifying glass')`, which is quiz q1, verbatim,
  under State, 1 mark. The examination prefers q1 for the physics ladder.
  The quiz is identical on TF and TH; `check_rung1_fallback` printed no
  warnings.
- r2: Calculate, 3 marks, with CFIFA convert options, by route. Foundation:
  2.5 cm object, 15 mm image → 0.60, unit "no unit". Higher: magnification 4.0,
  image 1.4 cm, object in mm → 3.5 mm.
- r3: chain, Explain, 3 marks: why a concave lens's image can never be shown on
  a screen. Red herrings: "too small", "the lens absorbs the light".
- r4: Compare, 4 marks, with marking points (examiner-drafted shape §5) and two
  reject lines. The 6-mark eye question belongs to Biology papers.

## Route tags

None needed. The whole lesson is Triple (8463 4.6.2.5 is physics only), so it
ships on TF and TH only. Neither 4.6.2.5 nor 8461 4.5.2.3 carries HT
(examination §2), so nothing is tagged `higher`. Ray diagrams for both lenses
are taught to Triple Foundation, per the examination and the commander's brief.
The pack's `higher` field is **WRONG TAG** (examination R3, C20), and its
content is taught at base Triple. Its "magnification from image and object
distances" line is not in the spec and is **not taught**. The bench readout
uses only the height ratio.

## ⚑ Net-new science-bearing items

- ⚑ Hook: a magnifying glass at arm's length shows a distant window small and
  inverted (a real image, theory 2 regime "beyond 2F").
- ⚑ Bench "why" lines for all seven set-ups (theory 2's image table, C7–C11),
  the concave lines (C4, C5), and the readout numbers from v = uf/(u − f). The
  thin-lens equation itself is not shown to pupils.
- ⚑ Explainer 1 re-cut (principal focus, focal length, the two rays,
  real/virtual definitions; C2 uses AQA's term "principal focus").
- ⚑ The constructor's four steps and every distractor reply.
- ⚑ The sort statements (all trace to 4.6.2.5, C3–C5).
- ⚑ Spectacles: myopia "eyeball too long or lens too strongly curved",
  hyperopia "too short or not curved enough". Both causes are given, per
  examination C17/C18. The eye diagram and its reveal follow 8461 4.5.2.3.
  The distractor reply "The eye cannot push the focus back far enough for
  distant objects" is my wording; worth the examiner's eye.
- ⚑ All CFIFA numbers (no source FIFA exists), rung 2 numbers, rung 3 links,
  rung 4 points, command-word lines and the key fact.
- ⚑ AQA lens symbols are drawn per 4.6.2.5 (examination R8): convex is a line
  with outward-pointing arrowheads, concave a line with inward-pointing ones.

## Frozen items

- q1 and q2 are both correct on TF and TH (examination §4). q2 (myopia) is
  biology content (8461 4.5.2.3) but legitimate on both Triple routes. It stays
  in the bank and is not used as a rung, following the examiner's preference.
- The `equations` field's second equality (image distance ÷ object distance) is
  not in the spec. It is kept in the data verbatim but **not displayed**. The
  equation card shows only the sheet equation.
- `variables` gives f in metres (C13, imprecise). It is not displayed; the page
  uses cm throughout, as AQA questions do.
- q2 wx3 ("typically worsens over time", C31, imprecise) is kept verbatim in
  the bank, since it is frozen and harmless. Flagged here.
- The camera, telescope and microscope theory (R7) is not in the spec and is
  not taught.
- The matching activity is replaced by the sort and the bench.
- The q1 key (rung 1) is the longest option, a frozen length-parity tell. It
  is kept verbatim and flagged here.

## New instruments and helpers

All of them live in the lesson's own Component logic; no `_ext` file:
`image()`, `truthOf()`, `scene()` (the lens bench and the constructor share
it), `ray()`, `dashed()`, `late()`, `lensSym()` (the AQA symbols), `stage()`,
`focusSvg()`, `eyeSvg()`. They use the KS4D primitives and its palette on the
cream plate.

## Word count

About 360 words of template body prose, plus about 200 words of bench why
lines. That is about 560 in total. The longest run before a commitment is
explainer 1, at about 120 words.

## Checks run

Built through `build_ks4`'s own compile and render functions in a scratch
harness; nothing was written into the worktree. TF and TH load with zero
console errors at 390 and 1280 px, with no `undefined`/`NaN`/`[object Object]`.
A scripted pass ran all 7 bench set-ups (right and wrong predictions; "7 of 7
set-ups"), the constructor with a wrong pick then completion, the eye predict,
the CFIFA block (Foundation and Higher numbers differ) and the ladder.
Screenshots were inspected at 390 px. Dark mode was not checked visually
(tokens only, cream plates, as in the pilot).

## Review fixes (1 Oct 2026)

- **S-6** (required): the Higher "Convert first" note now reads "…gives 0.65: a diminished image, but the wing looks bigger through the glass, not smaller." It no longer claims that a magnifying glass never makes a diminished image.
- **Q-L1 / Q-X1** (required): the static pills are replaced by the route chip, the same as using-moles-calculations.
- **Q-L2** (required): "Complete the ray diagram" is now a production task on the diagram itself. Real `<button>` tap targets (38 px, with `aria-label` "Point: …") are absolutely positioned over `buildFig` at plate coordinates:
  - steps 1 and 2: tap a point the ray passes through after the lens (F, 2F, straight on, near-side F / along the axis);
  - step 3: tap the image top (the crossing, F, 2F, lens);
  - step 4 (object inside F): tap the traced-back meeting point (or F, or the diagram edge), plus a "No image: the rays never meet" button.

  A wrong tap draws the pupil's ray to that point as a grey dashed line with a red ×, and shows the existing misconception feedback. A right tap draws the correct ray and moves on. The incoming half of each ray is drawn before the pupil taps. The text MCQ is removed.
- **Q-L3** (required): the WHY lines no longer repeat the real/virtual, upright/inverted and magnified/diminished words that the verdicts already state (cx30, cx20, cx15, cx6, cv30, cv6).
- **Q-L4** (required): the slider label reads "Object distance · F is 10 cm". `aria-valuetext` keeps the full "Object N cm from the lens".
- **A-L1** (applied): verdicts the pupil was never asked (after a "No image" prediction) use the neutral inset style. A wrong "No image" now reads "Image: real. There is an image." instead of "not no image".
- **A-8** (applied): explainer 1 reads "one parallel to the axis, which a convex lens bends through F".
- **A-9** (applied): the eye distractor reply reads "Even with the ciliary muscles relaxed and the lens pulled thin, the eye still focuses distant light in front of the retina."
- **A-10**: kept, as advised.
- **A-11**: the 0.625 display and the label overlap at 6 cm are cosmetic and not changed.
- **A-L2**: no change; the biology section stays with its eyebrow citation, for the examiner to confirm.
- No new `block_map` entry is needed: `s-build` keeps its id and is still mapped to worked-example.

## Review fixes round 2 (1 Oct 2026)

- **Q2-L1** (required): the targets in each step are now sorted left to right on the figure (top to bottom on a tie), so DOM and Tab order follow position. The answer is 2nd, 3rd, 3rd and 2nd in steps 1–4. Step 4 needed one more distractor to the left of the answer: "on the axis at 2F, object's side", with the reply "Nothing meets at 2F. Trace both rays back until they cross." Every accessible label is now generated by `where()` from coordinates only, for example "Point C, below the axis, between F and 2F, far side". The answer-naming `name` strings are deleted from the source.
- **Q2-L2** (required): the rings are unfilled and no longer catch the pointer. They are 32 px with a 3 px border, or 22 px with a 2 px border below 480 px. Each sits in a 44 px transparent button, which keeps the keyboard focus target and its visible focus outline. Taps are handled by the figure itself, which picks the nearest target within 40 px. Rings that sit close together on a phone can no longer steal each other's taps, and nothing is filled over the ray crossing. A keyboard click (`detail === 0`) is ignored by the figure handler, so Enter on a focused ring activates it once.
- Validated in a scratch build (TF and TH, zero console errors, no `undefined`/`NaN`):
  - at 390 px, all four steps were completed by real pointer taps at each ring's centre;
  - at 1280 px, all four were completed by keyboard (focus, Tab to the target, Enter).
- No `block_map` change.
