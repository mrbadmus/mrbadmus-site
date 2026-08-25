# KS3 P11 and P12 — delivery notes

Written 23 Aug 2026. Both units were empty scaffolds until this run: each folder
held only `support.js` and the `_ds/` tree.

## 1. Slots

Taken from `ks3_data/structure.py` character for character. P11 declares four
lessons and P12 six; both are complete, in slot order, with no renumbering and
no invented lessons.

P11 is listed in `REFERENCING_UNITS` as pulling coverage from C1 and C4. Its
four lessons own density, Brownian motion, temperature/internal energy and the
ice anomaly; states of matter, changes of state, diffusion and gas pressure stay
in C1, and the Connects-to blocks link out to them rather than restating them.

## 2. Shared components

Two child Design Components sit beside the lessons in each folder:

- `Cfifa.dc.html` — the whole five-step worked-example block: the tabbed
  worked examples, the click-to-reveal stepper, and the write-it-out student
  attempt with its self-mark panel. Every lesson that needs a worked example
  mounts it with `<dc-import name="Cfifa" examples="…" questions="…">` and
  supplies only the physics. This is what guarantees the CFIFA rule is
  implemented identically everywhere rather than re-typed per lesson.
- `Bench.dc.html` — the bench shell: commit gate, tab row, optional slider,
  proportional bars, readout cards and the closing note. The lesson computes
  what the bars and readouts say; the component owns the layout.

Both files are byte-identical copies across the folders that use them, so each
unit folder stays self-contained as a zip.

## 3. Benches

No SVG diagram carries a live label anywhere in these ten lessons. Every varying
figure is HTML text — a bar label, a readout card or the note — which sidesteps
the interpolated-text-in-`<text>` trap entirely.

| Lesson | Controls | What varies |
|---|---|---|
| p11-01 | six materials × six volumes | mass, density league table, float or sink |
| p11-02 | four suspensions × five temperatures | molecule speed, visible jiggle, size ratio |
| p11-03 | four amounts of water × six temperatures | internal energy on a log scale |
| p11-04 | four substances × solid/liquid | density of each state, which one floats |
| p12-01 | five locations × five masses | field strength, weight |
| p12-02 | four objects × four locations | weight in four places, mass unchanged |
| p12-03 | four gravitational pairs × four separations | inverse-square fall-off |
| p12-04 | five rungs of the distance ladder | distance, size, star count |
| p12-05 | four dates × three latitudes | daylight hours, noon altitude, insolation |
| p12-06 | five objects | light travel time, distance in m and light years |

p12-05 computes real astronomy: solar declination 0° at the equinoxes and
±23.44° at the solstices, daylight from the standard sunrise equation, noon
altitude as 90° − |latitude − declination|, and energy per square metre as the
sine of that altitude. London on 21 June comes out at 16.5 hours and 61°, which
is right. The legal line records what the model leaves out.

## 4. Conventions applied

- Four rail stops per lesson — hook, bench, the third substantial section, and
  the ladder. The misconception block carries a stop only where the lesson has
  no formula section, matching P4–P10.
- One `[data-key-fact]` block per lesson. In a CFIFA lesson it closes the
  formula section; otherwise it sits between the bench and the misconceptions.
- Two misconception quotes per lesson, the second under a rule.
- Weight in newtons is mass in kilograms × 10 N/kg, stated wherever used.
- No `→`, `✓` or `✕` characters. The end-matter arrows are inline SVG.

## 5. Powers of ten

**New convention, applied here and worth carrying forward.** Unit symbols keep
the Latin-1 superscripts — `m²`, `cm³`, `g/cm³` — which are inside every
shipped font subset and are already used throughout P5. Powers of ten are
written `10^8`, `10^20`, `3.0 × 10^8 m/s`, because U+2070 and U+2074–U+2079
are **not** in the subsets and render as a system-font fallback. No physics
lesson outside P11/P12 used those characters, so nothing needed retrofitting.

## 6. Open

- Neither unit has been science-reviewed. Every page carries the draft flag.
- p12-04's star counts for the Milky Way and Andromeda are estimates with wide
  error bars and are quoted as "about". Confirm you want figures at all rather
  than an order of magnitude.
- p11-02 quotes root-mean-square molecular speeds. Confirm 500 m/s for air and
  590 m/s for water at 20 °C are the figures you want a KS3 page to show.
- p12-03 gives gravitational forces in scientific notation (`1.98 × 10^20 N`).
  Confirm that is not too early for KS3, or ask for words instead.
