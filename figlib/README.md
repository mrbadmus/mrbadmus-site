# figlib — Mide's diagram library, in the repo

The one source of every **question** figure: the pupil's assignment page,
practice, Set work, and the worksheet PDF/DOCX. (KS3 **lesson** pages still
draw their own figures with `ks3_art` — architecture law, untouched.)

## Provenance

Brought in on 24 Sep 2026 (MRB-352 run 2) from Mide's working library:

| figlib file | source | md5 of the source |
|---|---|---|
| `physics.py` | `~/Desktop/MrBadmus AI/Image Visualisations/files/physics_p1/physics_diagrams.py` | `b3a03b9d547f6b418582fee14c6b3b6b` |
| `chemistry.py` + `style.py` | `…/files/chem_p1/chem_diagrams.py` | `4475e9b49573e934cc4709b48d294132` |
| `biology.py` | `…/files/biology/bio_diagrams.py` | `c1a80d8607713f35ed6e36337b42be65` |

`physics_p2/` and `chem_p2/` are byte-identical copies of the p1 files and
were not used. `~/Desktop/Science Visuals/` is older and was not used.

**This is now the only copy that matters.** The Desktop files are the
record of where it came from; changes are made here, in the repo, so the
site and the library can never drift apart again.

## What changed on the way in

Everything the library draws by default still draws the same way, except
where a default was wrong. Every change is marked `⊕ figlib` in the code.

**Mechanical**
- `STYLE`, `Canvas`, `_pol` and `export` moved from `chem_diagrams.py` into
  `style.py`, so the three modules import one style core instead of each
  other. Imports are package-relative.
- `cairosvg` is imported lazily inside `export()` only. The site build never
  rasterises and must run without it.

**Corrections (science / AQA accuracy) — flagged for Mide**
- Circuit symbols redrawn to the AQA 8463 v1.1 §4.2.1.1 sheet (p.24): cell
  (only "+" marked), battery (cell, dashed wire, cell), switches (hollow
  contacts, lever dropped clear / joining both), diode and LED (wire through
  the circle to the bar), thermistor (diagonal fully through the body, no
  arrowhead, short horizontal tail at the lower left), LDR (wire into the
  circle to the small rectangle; two arrows IN from the upper left),
  variable resistor (diagonal fully through, arrowhead well outside).
- `symbol_bank()` is headed "AQA" and now shows exactly the AQA list — the
  library's also carried "d.c. power supply" and "Motor", neither on it.
- A lone `("voltmeter",)` in a netlist now bridges the component before it.
  The library drew it across its own empty span of wire — a voltmeter across
  nothing, which reads zero.
- `motor_effect()`: the force on a wire carrying current UP in a field from
  N (left) to S (right) is INTO the page, not out of it. F = I L × B with
  L = +y, B = +x: (+y) × (+x) = −z. Fleming's left-hand rule agrees.
- `states_of_matter()`: the liquid's particles now TOUCH, in a random heap at
  the bottom of the box (`_liquid_pack`: a settle-downward Monte Carlo,
  every particle checked to touch at least two others). The library spaced
  them at least 46 apart with radius 17 — never touching, a denser gas.

**Parameters added (defaults = the library's own drawing)**
- `circuit(…, layout=QUESTION_LAYOUT, gap="start", aqa_only=True,
  left=[…], right=[…])` — a phone-width frame; a deliberate break in the
  loop; refusal of any non-AQA symbol; components on the loop's sides
  (turned a quarter-turn by rewriting coordinates, never by a transform).
- `states_of_matter(W, H, box_w, box_h, pr, title, …, reference=…,
  solid_grid, liquid_n, gas_n, gas_min)`.
- `covalent_dotcross(formula, title, compact, incomplete, angles, detached,
  dashed, nuclei, seat)` — a cropped canvas; a deliberately wrong drawing
  for "what went wrong?" questions; the exam-paper look.

**New builders** (library style, parametrised — `physics.py`,
`chemistry.py`, `biology.py` under "FIGLIB EXTENSIONS", and `charts.py`):
`symbol_figure`, `symbol_panel`, `question_circuit`, `force_beam`,
`crate_forces`, `horseshoe_gap`, `motor_coil_forces`, `field_point`,
`resolution_triangle`, `oscilloscope_compare`, `box_monomers`, `food_web`,
`dna_ladder`, `moth_pair`, `plant_cell`, `line_graph` (monotone cubic, never
overshoots), `hbar_chart` (linear or log), `column_chart` (histogram or
categories), `table`.

## Phone legibility is designed in, not hoped for

The library draws for a projector: canvases 900–1400 wide, 22px labels.
Shrunk into a 320px phone column that label is 5px. A question figure uses
a narrow canvas, and its text size comes from `style.q_font(W)` — the
smallest size still ≥ 11 CSS px when scaled into 320px — never typed.

## From catalogue record to manifest

```
catalogue record ──figlib.draw──▶ library SVG ──figlib.web.to_manifest_svg──▶
manifest SVG ──figlib.checks──▶ ship (or refuse to write anything)
```

- Records: `figlib/catalogue_ks3.py` (KS3 question figures) and
  `ks4_art/catalogue*.py` (KS4). `{"id", "art", "title", "desc", "params"}`;
  `art` is a key of `figlib.ART`.
- `web.py` — the ONE place web adaptations happen: `viewBox` only (no fixed
  size), `role="img"` + `<title>`/`<desc>`, `<g>` dissolved with its paint
  pushed onto each child, ids prefixed with the figure id, the cream paper
  becomes a rounded card marked `data-role="paper"`, weights numeric,
  numbers rounded.
- `checks.py` — hard failures, in `build_figures.py`: see the next section.

## The SVG a manifest figure may contain

This is the complete set. `build_figures.py` refuses anything else.

| element | attributes |
|---|---|
| `svg` | `viewBox`, `role`, `aria-labelledby`, `preserveAspectRatio` |
| `title`, `desc` | `id` |
| `rect` | `x y width height rx` + paint, `data-role="paper"` (the first shape only) |
| `circle` | `cx cy r` + paint |
| `ellipse` | `cx cy rx ry` + paint |
| `line` | `x1 y1 x2 y2` + paint (always `fill="none"`) |
| `polyline` | `points` + paint (always `fill="none"`) |
| `polygon` | `points` + paint |
| `path` | `d` using only `M L H V C Q Z` + paint |
| `text` | `x y font-family font-size font-weight text-anchor fill`, optional `transform="rotate(a cx cy)"` |

Paint = `fill stroke stroke-width stroke-linecap stroke-linejoin
stroke-dasharray`. Colours are `#hex` or `none`. `font-size`,
`font-weight` (400/700), `stroke-width` and `rx` are bare numbers.
`font-family` starts with Georgia, or is exactly `style.NUM_FONT`
("Times New Roman, Times, Noto Serif, serif") on a label that carries a digit — see
"Fix round 1" below. Never: `class`, `style`, `var()`, `<g>`,
`<defs>`, `<marker>`, gradients, `<use>`, `<tspan>`, `clipPath`, filters,
`opacity`/`fill-opacity`, arcs (`A`), `S`/`T`, any transform but a text
rotation. Arrowheads are polygons.

Also checked on every figure: every shape states its fill; every label is
≥ 4.5:1 against the fill it actually sits on and never on a dark fill;
≥ 11px text and ≥ 1px strokes in a 320px box; no motor (circled M) and no
"d.c." box; no id shared between two figures.

## Adding a figure

1. Find the builder in `figlib.ART`, or add one to the right module in the
   library's style — parametrised, not a one-off.
2. Add a record to `figlib/catalogue_ks3.py` or a `ks4_art/catalogue*.py`.
   `title` is the alt text: what is SHOWN, never the answer.
3. `python3 build_all.py` (it runs `build_figures.py` first). If a check
   fails, fix the drawing — never the check.

## Fix round 1 (MRB-352 run 2, after the examiner and visual reviews)

Library-wide changes, each marked `⊕ fix round 1` in the code:

- **Cell and battery plates are the same line weight** (stroke 3), the
  short plate only shorter — as AQA 8463 v1.1 p.24 draws them. The earlier
  comment called the short plate "a little thicker"; that is a BS
  convention, not AQA's.
- **Numerals line up.** Georgia's default old-style figures made "0" a
  small "o" at phone size. `style.text()` sets any label containing a
  digit in `style.NUM_FONT` = "Times New Roman, Times, serif" (lining
  figures). It is attributes only, and every family in it is serif, so the
  worksheet maps it to the same bundled DejaVu Serif as Georgia.
  `figlib.checks` rule 6 accepts exactly that stack besides Georgia-first,
  nothing else. Chart tick and value numerals are also one step larger
  (`charts._num_size`: 20 against 17 on a 480 canvas).
- **Circuits:** collinear wire segments that meet end to end are joined
  into one `<line>` (`_merge_wires`), which removes the darker seam dots at
  phone scale. A join is refused if it could change what paints over what.
  When a parallel section ends the top run, the return wire drops from the
  junction column itself instead of a second vertical beside it.
- `symbol_figure` centres what is drawn, not the wire. `symbol_panel`
  takes `cols` (a grid; `H` is one row's height) and `fs`.
- `oscilloscope_compare` defaults to 2:1 screens (10 × 5 divisions).
- `covalent_dotcross(detached=…)`: the central atom keeps the electron it
  would have shared, drawn as one unpaired dot on its shell.
- `motor_coil_forces`: force arrow tips land between field lines.
  `field_point`: the arrow at P is a field arrow like the rest.
  `resolution_triangle`: labels at 19. `plant_cell`: the cell-wall leader
  no longer crosses the chloroplast leader.

## Fix round 2 (MRB-352 run 2)

- **`NUM_FONT` gained Noto Serif** before the generic:
  "Times New Roman, Times, Noto Serif, serif". Android and Chrome OS have
  no Times, and Noto Serif is their lining-figure serif. (The round-1
  entry above quotes the old three-family stack.)
- **New hard check (`figlib.checks` rule 7):** every unrotated numeral
  keeps >= 6 units from the card's left and right edges, measured with
  `style.num_width_wide` (digits at 0.60 em, wider than Noto Serif's).
  A histogram's right margin now fits its last boundary numeral that way.

## Batch 1 of the 174 (MRB-352 run 2, KS3 physics)

Five new builders, specified by the examiner (`force-grid`, `graph-panels`,
`wave-line`, `longitudinal`, `bar-field`), 40 new KS3 records. Departures
from the spec's text, each marked ⊕ in the code:

- `bar_field`: a caption gets its own band above its panel (centred inside
  a 320 panel it sat on the outermost line). With `clip=True`, every line
  that leaves the card is also drawn MIRRORED and reversed arriving at S —
  the two-pole field is antisymmetric under x → −x, so this is exact; without
  it the map crowded N and left S bare, which reads as a stronger N pole.
  Point letters avoid lines, dots and the magnet. Two options added for
  sibling figures: `wavy` (each line wiggled about its true path),
  `inside` (lines drawn through the magnet N → S — a student's error) and
  `even` (concentric evenly spaced arches — a student's map with no crowding).
- `graph_panels`: every panel shares one y-axis position (`line_graph(ox=)`)
  so the time axes are identical, as the spec requires.
- `p6-wave-six-crests` uses `start_phase=0`: the spec's −0.25 put the crests
  at u = 0.5, 1.5 … and its dimension (u = 0.25 → 5.25) on zero crossings;
  its own text says crests at 0.25 … 5.25, which is `start_phase=0`.

### Batch 1 fix round (examiner + visual review)

- Circuit labels (`physics._clabel`) now take `style.NUM_FONT` when they
  carry a digit, like every other figlib label. `_clabel` predated
  `style.text()` and hard-coded Georgia, which is why "A1"/"V1" kept
  Georgia's x-height "1". The A/V inside a meter is drawn in symbol ink,
  not label green, so it never reads as an answer letter (AQA p24 draws
  it as part of the symbol). This touches the five KS4 meter figures too.
- `force_grid`: the grid is one square wider than the longest arrow on
  each side (a 7-square arrow no longer ends on the frame), and the grid
  is #948A70, 3.0:1 on the card — counting squares is the task.
- `longitudinal`: the row runs 0.4 wavelength past each end compression,
  so the end compressions are whole bunches; `per_wave` is a parameter
  (six-compressions uses 7).
- `bar_field`: pole points 10 units inside the ends (was 20), launch
  angles re-spread, so lines leave across the pole region and fan; a
  closed line is one that re-enters the S half. A closed loop that leaves
  the END FACE cannot fit an unclipped card at true scale (its apex is
  ~2x the magnet's length away), so the unclipped maps' lines leave the
  long face near the end, and only the clipped maps show end-face lines.
  Arrowheads avoid dots and each other; point letters stay on the card;
  the inside-magnet heads sit 40% along; the `even` map's arches start
  at the corner; new `reversed` option (a whole line, arrow backwards).

## Batch 3 of the 174 (MRB-352 run 2, KS4 physics electricity)

21 new KS4 records in `ks4_art/catalogue_run2_elec.py` (N1–N21 of the
examiner's spec). Library changes, every one a new parameter whose default
is the old drawing (the 94 figures already in the manifest rebuilt byte for
byte), each marked `⊕ MRB-352 run 2 (174)`:

- `circuit()`: `["voltmeter", null, null, {"inline": true}]` is an ordinary
  series component (a voltmeter wrongly IN the loop); `{"ammeter": true}` on
  a component bridges an ammeter across it (`sym_ammeter(leads=)`,
  `_bridge_voltmeter(meter=)`); `{"reverse": true}` on a diode or LED
  mirrors it end for end (`sym_diode/sym_led(reverse=)`) — the LED's
  emission arrows still point up and out.
- `oscilloscope_compare`: a trace whose `caption` is None or omitted draws
  no caption row.
- New module `figlib/ks4elec.py` with `radial_field` (`"radial-field"`): a
  charged sphere with evenly spaced straight radial lines, one arrowhead
  each, and lettered points placed between lines (it refuses a point or
  label that would touch a line). Merged into `ART` from `__init__.py`.

### Batch 3 fix round (examiner + visual review)

- Grids a pupil reads values from are now #948A70 — 3.0:1 on the cream
  card, 3.4:1 on a white scope screen (WCAG 1.4.11): `charts.GRID` (every
  line graph and bar/column chart) and the oscilloscope screen grid
  (`physics._SCOPE_GRID`), whose centre line is darker again (#6F6754).
  The review suggested #A89E86, but that measures 2.3:1 on cream; #948A70
  is the colour `force_grid` already uses for the same reason.
- `line_graph` series option `smooth_from`: an exact straight polyline up
  to that x, then the monotone curve leaving at the straight run's slope
  (no kink, no early bend). Used by `ks4-fig-graph-iv-resistor-bends`.
