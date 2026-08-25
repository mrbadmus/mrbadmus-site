# KS3 Physics — state of the build, 23 Aug 2026

Second pass. The first pass of this audit listed four open items and one
deliberate-inaction list; all of them are now closed. What follows is the state
after that work.

## What shipped

| Unit | Title | Declared | Authored | Notes file | README |
|---|---|---|---|---|---|
| P1 | Energy transfers | 8 | 8 | NOTES-P1.md | yes |
| P2 | Energy at home | 5 | 5 | NOTES-P2.md | yes |
| P3 | Describing motion | 3 | 3 | NOTES-P3.md | yes |
| P4 | Forces | 9 | 9 | NOTES-P4-P6.md | yes |
| P5 | Pressure | 4 | 4 | NOTES-P4-P6.md | yes |
| P6 | Waves and sound | 9 | 9 | NOTES-P4-P6, NOTES-P6-P7 | yes |
| P7 | Light | 7 | 7 | NOTES-P6-P7.md | yes |
| P8 | Electric circuits | 7 | 7 | NOTES-P8-P9.md | yes |
| P9 | Static electricity | 3 | 3 | NOTES-P8-P9.md | yes |
| P10 | Magnetism and electromagnetism | 5 | 5 | NOTES-P10.md | yes |
| P11 | Matter and the particle model | 4 | 4 | NOTES-P11-P12.md | yes |
| P12 | Space | 6 | 6 | NOTES-P11-P12.md | yes |

**70 of 70 physics lessons are authored.** Every unit matches its
`structure.py` slot list exactly — no renumbering, no invented lessons, no
missing slots.

## Closed in this pass

### 1. CFIFA is now the only worked-example shape in physics

`CLAUDE.md` makes Convert–Formula–Insert–Fine-tune–Answer the standing rule,
with the C step always present. It previously existed only in P8. Nineteen
lessons were rebuilt on it and three new ones were written on it:

- **Rebuilt from four-step FIFA:** P1 `p1-08` · P2 `p2-01`, `p2-03` ·
  P3 `p3-01` · P4 `p4-02`, `p4-03`, `p4-07`, `p4-08` ·
  P5 `p5-01`–`p5-04` · P6 `p6-02`, `p6-05`, `p6-06`, `p6-07` ·
  P7 `p7-01`, `p7-02`
- **Built from nothing:** P2 `p2-02` and `p2-04`, which were declared
  QUANTITATIVE and carried no worked example in any form.
- **New:** P11 `p11-01` · P12 `p12-01`, `p12-02`, `p12-06`.

Every one of them now carries two worked examples — `Nothing to convert` and
`Convert first` — and two student attempts labelled only `Question 1` and
`Question 2`, write-it-out, five empty boxes with a placeholder on the Convert
line alone. `p7-02` is the exception the rule allows: its quantities are angles
in degrees, conversion cannot arise, so it keeps one example and one question
and its C step reads as the no-conversion case.

The rebuild was not a find-and-replace. Rather than re-typing the block into
each lesson, it is now a shared child Design Component — **`Cfifa.dc.html`**,
copied byte-identically into each unit folder and mounted with
`<dc-import name="Cfifa" examples="…" questions="…">`. Each lesson supplies
only the physics. This is what stops the rule drifting again: there is one
implementation, and a change to the block is a change to one file.

P8's four lessons keep their original inline implementation. They are the
reference the rule cites, they already comply, and rewriting compliant pages to
route through a new component is risk for no student-visible gain.

### 2. P1, P2 and P3 now carry the structural conventions

All sixteen lessons gained a `[data-key-fact]` block and a second misconception
quote, matching P4–P12. Any gate counting `[data-key-fact]` now passes on all
seventy.

### 3. Four rail stops everywhere

`NOTES-C9.md` §10 records a correction: the count is four, and the
misconception block loses its stop where the lesson has a fuller third section.
P4–P10 already ran four. P1–P3 ran five, six and seven, and are now four:

- `p1-07` drops ICE and THINK · `p1-08` drops BALANCE and THINK
- `p2-02` drops SORT and THINK · `p2-03` drops TRIANGLE and THINK ·
  `p2-04` drops UNIT, SHAPE and THINK · `p3-01` drops COMPARE and THINK
- the remaining nine drop THINK only

Dropping a stop removes it from the rail. Every section keeps its `id`, so
in-page anchors and the tutor link are untouched.

### 4. P11 and P12 are written

Ten new lessons. P11 owns density, Brownian motion, temperature/internal energy
and the ice anomaly, and references C1 and C4 for the rest of its statutory
coverage as `structure.py` requires. P12 owns gravity and weight, mass vs
weight, Earth–Moon–Sun gravity, the Sun/stars/galaxies, seasons, and the light
year.

Both folders also carry `index.dc.html`, a unit contents page — the working
offline route between the files in the folder — and a second shared component,
**`Bench.dc.html`**, holding the commit gate, tab row, slider, bars and
readouts that every new bench is built from.

### 5. Superscripts

A new convention, applied and recorded. Unit symbols keep the Latin-1
superscripts (`m²`, `cm³`, `g/cm³`) — they are inside every shipped font
subset, they already appear throughout P5, and they render. Powers of ten are
written `10^8`, `10^20`, `3.0 × 10^8 m/s`, because U+2070 and U+2074–U+2079
are **not** in the subsets. The previous pass left the `m²` question open
pending a ruling; this is the ruling, and it needed no retrofit outside P11/P12.

### 6. Prev/next links — ruled, not changed

Every lesson links to site addresses (`p8-06-conductors-and-insulators.html`,
`index.html`, `../index.html`) rather than to the `.dc.html` filenames beside
them. That is correct for mrbadmus.com and only looks broken when a folder is
opened off a disk. Rewriting the hrefs would put wrong URLs on the live site, so
they stand. The offline route is the folder's `README.txt`, and now — in P11 and
P12 — `index.dc.html`. Recommendation for the other ten units: add the same
contents page rather than touch the hrefs.

## Assets — clean

Every folder carries a byte-identical `support.js` and the same seven
design-system files under `_ds/mrbadmusai-design-system-…/`. P1–P7, P11 and P12
additionally carry `Cfifa.dc.html`; P11 and P12 carry `Bench.dc.html` and
`index.dc.html`. No lesson references an image or any other external file, so
there is no unbuilt-asset gap in physics.

## Fixed in the previous pass, still standing

Ten bench captions that were `{{ hole }}` values inside SVG `<text>` elements
and therefore rendered nothing are HTML `<span>` overlays at matching viewBox
percentages, in `#C6B9A7` (6.08:1 on the dark panel). None of the ten new
lessons puts a live label inside an SVG at all — every varying figure is a bar
label, a readout card or the closing note.

## Open

- **Nothing is science-reviewed.** All seventy lessons carry the draft flag.
- **P9 and P10 have no worked examples**, correctly: nothing in either unit is
  quantitative, and the rule is not to invent a calculation to fill the block.
  The same applies to P11 `p11-02`–`p11-04` and P12 `p12-03`–`p12-05`.
- Three content questions on the new units are listed in `NOTES-P11-P12.md` §6.
