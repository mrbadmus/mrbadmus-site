# P3 — Describing motion · author's notes

Three lessons, complete unit. Draft — nothing here has been science-reviewed.
For Mide (examiner review) and Claude Code (build). Flags are numbered so they
can be worked through and answered by number, as with B1.

---

## 0. How the queue was resolved — please sanity-check this first

The brief says to read `ks3_data/structure.py` **and `ks3_data/half_terms.py`**.
**`half_terms.py` does not exist in the repository** — `ks3_data/` contains
`structure.py` only, and `structure.py`'s docstring points at a
`default_sequence.py` which is also absent. Read-only access, so nothing was
added.

The queue was therefore resolved from `structure.py` alone, using declaration
order within each discipline and the `typical_year` field:

| Brief | Year-7 units of that discipline, in declaration order | Resolved |
|---|---|---|
| First Physics unit of Year 7 | **P3** describing-motion, P4 forces, P11 matter-and-the-particle-model | **P3 — Describing motion** |
| Second Biology unit of Year 7 | B1 cells, **B2** movement, B3 nutrition | **B2 — Movement: skeleton and muscles** |
| Second Chemistry unit of Year 7 | C1 particles, **C2** atoms-elements-compounds, C3 mixtures | **C2 — Atoms, elements and compounds** |

Two things corroborate P3: it is first in declaration order among the Year-7
physics units, and its opening lesson `speed` is a `QUANTITATIVE` lesson, which
the brief predicted the first physics unit would be. P4 and P11 both open on a
`MODEL` lesson.

**If a `half_terms.py` exists somewhere I cannot see and it sequences P4 or P11
first, this is the wrong unit and I have built it in good faith on the only
data present.** Say the word and it is three lessons of rework, not thirteen.

**Filenames.** The brief's example was `p1-01-…`. I have used the unit code, as
B1 did: `p3-01-speed`, `p3-02-distance-time-graphs`, `p3-03-relative-motion`.
`p1-` would collide with unit P1 (energy transfers) when that is authored.
Slugs are taken verbatim from `structure.py` and are unchanged.

---

## 1. The QUANTITATIVE family pattern — defined here for the first time

There was no QUANTITATIVE pattern. `p3-01-speed` is the first one in the
course, so what it does is now the family. Stating it explicitly, as asked.

> **QUANTITATIVE: the student's own measurements come before the formula, and
> the formula is applied to those measurements, not to given ones.**
>
> 1. **The phenomenon is a comparison that cannot be settled by looking.** Two
>    things, both plausible, where the eye gives the wrong answer. The lesson
>    exists because a number is needed, not because a formula is due.
> 2. **The instrument produces raw measurements and refuses to do the
>    arithmetic.** The light gates give a distance and a time and a readout that
>    says *speed — not measured — you work it out*. An instrument that hands
>    over the answer has removed the lesson.
> 3. **The measurements scatter.** Three runs, three different times. This is
>    where the mean comes from, and it is why one reading is never enough.
> 4. **Then the four-part formula sequence**, in the ruled order: formula alone
>    in its own block, drawn as a triangle; worked example revealed one step at
>    a time; the student filling in the same steps on **their own numbers**;
>    only then a full question.
> 5. **The misconception is a reasoning error about the quantity, never an
>    arithmetic slip.** Here: averaging two speeds instead of dividing total by
>    total.
> 6. **One rung of the ladder is a measurement rung** — what to do with three
>    readings that disagree — and one is a design rung: measure this yourself
>    with a tape and a stopwatch, and name the biggest error.

The step that carries the family is (2). Everything else follows from
refusing to let the instrument calculate.

**Consequence for the other QUANTITATIVE lessons in the map** (`B2
biomechanics`, `C2 conservation-of-mass`, `C4 mass-in-a-reaction`, `P1 simple
machines`, all of `P2`, `P5 pressure`, `P8 resistance`, `P11 density`, `P12
gravity-and-weight`, `how-far-is-a-light-year`): each needs an instrument that
*measures* and does not *compute*. Where no such instrument is possible — a
light year, for instance — the pattern degrades to given data, and that should
be a deliberate, noted exception rather than a default. Flag 13 below.

---

## 2. New instruments — none of these exist, all four are needed

Available and working: microscope, system-parts, diffusion, particle-states,
gas-pressure. None of them fits a motion lesson. The four below are implemented
inside the lesson pages so the behaviour is reviewable, but they need to become
real instrument kinds before Code wires the generator.

### 2.1 `light-gates` — flagship of `p3-01-speed`

- **Controls:** ramp height (3 discrete steps: low/medium/high); gate
  separation (range 0.40–2.00 m, step 0.20); release (button); playback speed
  (real time / slow motion ×4).
- **Readouts:** gate separation in metres; gate timer in seconds, counting
  **only while the trolley is between the beams** and freezing at the second
  beam; a results table appending one row per run (`distance`, `time`, ramp);
  and a third tile that deliberately reads *speed — not measured*.
- **Payload:** `{ramp: 'low'|'med'|'high', separation_m: number, runs:
  [{d_m, t_s, ramp}], scatter_pct: 3, playback: 1|4}`.
- **Mechanism:** speed between the gates is constant (see flag 1); each run
  multiplies the ramp's nominal speed by a random 0.97–1.03 so repeated runs
  disagree; `t = separation ÷ speed`.
- **aria-label:** *"A trolley released from a ramp rolls along a runway and
  breaks two light beams 1.20 metres apart. The timer runs only while the
  trolley is between the beams and reads 0.84 seconds."* — the mechanism, not
  the picture.
- **Reduced motion:** the run resolves instantly; the timer and the table carry
  the whole result. Nothing is lost.

### 2.2 `graph-plot` — mid-size of `p3-02-distance-time-graphs`

- **Controls:** a 7 × 7 grid of **real buttons** overlaid on the graph canvas,
  one per intersection, each labelled *"4 seconds, 6 metres"*. Plotting by
  clicking a canvas would have locked out every keyboard and screen-reader
  user; this does not. Then a *join the points* button.
- **Readouts:** points plotted so far, the reading currently being looked for,
  and — when a wrong intersection is chosen — **the coordinates of the cell the
  student actually chose**, in the graph's own units. That is a location
  statement, not a mark (R3).
- **Payload:** `{data: [{t_s, d_m}], plotted: int, joined: bool, axes: {t_max,
  d_max, t_step, d_step}}`.
- **aria-label:** *"A distance–time grid, time 0 to 12 seconds along the
  bottom and distance from the start 0 to 18 metres up the side, with 5 of 7
  sensor readings plotted."*

### 2.3 `journey-match` — flagship of `p3-02-distance-time-graphs`

- **Controls:** four segments × four modes (stand still / walk 1 m/s / jog
  3 m/s / walk back 2 m/s); send the walker; clear the line.
- **Readouts:** a corridor with the walker and a live *"1.7 m from the start"*;
  the graph with the target as a dashed line and the student's own line drawn
  **as the walker moves** (Law 9 — the line is not swapped in at the end); a
  factual end-point comparison, *your line ends at 6 m, the target ends at
  6 m*, with no verdict attached.
- **Payload:** `{segments: [modeId × 4], seg_seconds: 3, target: [modeId × 4],
  modes: [{id, label, v_ms}]}`.
- **aria-label:** *"A corridor with a walker, above a distance–time graph. A
  dashed target line is drawn from 0 to 12 seconds, and the walker's own line
  is drawn in as it moves. The walker is 1.7 metres from the start."*
- **Reduced motion:** the completed line is drawn at once; the walker sits at
  its final position.

### 2.4 `relative-frames` — flagship of `p3-03-relative-motion`

The one I would most like to exist as a shared kind: it is reusable in P4
(forces on a passenger), P6 (Doppler-free sound), and any lesson where a
viewpoint is doing hidden work.

- **Controls:** speed of A (0–30 m/s, step 5); speed of B (same); B's direction
  (same way / opposite way); **observer** (roadside / car A / car B); freeze.
- **Readouts:** four relative speeds — A from the roadside, B from the
  roadside, B from A, A from B — with the one belonging to the current
  observer outlined and amber; a written sentence of what this viewpoint sees;
  and, drawn into the scene, *"stationary here: car A"*.
- **Payload:** `{v_a_ms, v_b_ms, same_direction: bool, observer:
  'ground'|'a'|'b', px_per_m: 6}`.
- **Mechanism:** everything is drawn with velocity `v − v_observer`; the road
  markings and posts belong to the ground and therefore slide in a car's frame.
  A car's **orientation** comes from its ground velocity, not its relative
  velocity — see flag 11.
- **aria-label:** *"A road with two cars, drawn from the viewpoint of car A,
  where car A is held still and the road slides underneath it. Car A travels at
  25 metres per second and car B at 20 metres per second the same way."*

---

## 3. Science flags — numbered for review

1. **Constant speed between the gates.** `p3-01` models the trolley as moving
   at a steady speed after it leaves the ramp, so the gate timing gives a
   speed rather than an average over a changing speed. Real trolleys slow
   slightly. The page never says "instantaneous"; it says *the speed between
   the gates*. Is that wording acceptable at KS3, or do you want an explicit
   "we are ignoring friction here" line?
2. **±3% scatter, and what to do with it.** Rung 3 asks the student to take the
   **mean of the three times** and then divide once. The alternative — three
   speeds, then mean them — gives a very slightly different number. Confirm
   mean-the-times is the method you want taught, since it is the one that
   generalises to the light-gate practical.
3. **km/h → m/s (÷ 3.6).** Used in `p3-01` compare pair 3 (72 km/h vs 20 m/s, a
   deliberate dead heat) and in the `think again` block of `p3-03` (100 km/h
   trains). `KS3.P.MOT.01` names only speed = distance ÷ time. Every scheme I
   know does the conversion at KS3. Ruling wanted: keep, or rewrite pair 3 into
   a single unit?
4. **The fly and the plane.** Fly: 1.5 m in 0.8 s ≈ 1.9 m/s (houseflies cruise
   around 2 m/s). Airliner: 15 000 m in 60 s = 250 m/s ≈ 900 km/h. Both are
   order-of-magnitude illustrations, not looked-up specimens. Happy?
5. **1.67 m/s.** The walk-then-run average is 200 m ÷ 120 s = 1.6666…, given as
   1.67 m/s throughout, matching the lesson's two-decimal-place convention.
   Confirm you are happy with 1.67 rather than 1.7.
6. **The word "velocity" appears nowhere in this unit**, deliberately — it is
   not in MOT.01–03, and direction-as-sign is not taught here. `p3-03` handles
   direction in words ("forwards", "backwards", "the opposite way") and never
   with a negative number. Confirm that is the line you want held; it decides
   how P4 opens.
7. **"Distance from the start" vs "total distance travelled."** `p3-02`'s
   stretch layer and rung 4 contrast the two graphs. This is displacement in
   everything but name. Legitimate KS3 stretch, or GCSE creep to be cut?
8. **A flat line is stopped, not slow.** Stated as the KEY FACT. Standard, but
   it is the one place where a student who has just learned "steeper = faster"
   can conclude "flat = slowest possible = very slow". The read-back question
   and rung 1 both attack it. Sufficient?
9. **Galilean relativity, unnamed.** `p3-03`'s stretch says no experiment
   inside a smoothly moving room can tell you how fast it is going, and that
   people looked for a stationary frame for two hundred years and there isn't
   one. True for uniform motion; the copy says "smoothly moving" to keep
   acceleration out. Check the wording.
10. **The plane-and-wind rung** (`p3-03` rung 4): 250 + 50 = 300 m/s and
    250 − 50 = 200 m/s, and the round trip takes longer than in still air. That
    last part is the harmonic-mean result, and it is the same reasoning error
    as `p3-01`'s misconception seen from the other side, which is why it is
    there. It is a self-marked rung with criteria. Too hard for KS3?
11. **A car does not turn round when you change viewpoint.** In
    `relative-frames`, a car's drawn orientation follows its **ground**
    velocity while its motion follows its relative velocity — so from car B's
    seat, car A can be drawn facing right while drifting left. That is correct
    and it is also exactly the sort of thing a reviewer flags as a bug. It is
    deliberate. Confirm you want it kept.
12. **30 km every second.** Earth's orbital speed is 29.8 km/s, given as
    "about 30 km every second". Fine?
13. **Which lesson owns the *instantaneous vs average* distinction?** `p3-01`'s
    stretch layer raises it (a roadside camera measures over half a metre, an
    average-speed camera over two kilometres, and they can disagree). It is not
    in MOT.01–03 and it is not taught as a term anywhere at KS3. I have kept it
    as stretch prose only, with no assessment attached. Confirm, or cut.

---

## 4. Misconception register — the `FORCE` family opens here

The register lists `FORCE` (forces and motion) as a suggested-but-unopened
family. These are kinematics misconceptions, not force ones. **Ruling wanted:
open `FORCE` as below, or mint a separate `MOT` family for describing-motion
and leave `FORCE` for P4?** I have used `FORCE` because that is what the
register's own family table says it covers, and because IDs are permanent — I
would rather you choose the family before these are referenced anywhere.

Proposed rows, for `docs/ks3/misconception-register.md` once ruled:

| ID | Statement (as a student holds it) | Elicited by | Confronted by | Lesson |
|---|---|---|---|---|
| `FORCE-01` | Whichever one gets there first is going faster. | `compare-pairs` | `compare-reveal` | `speed` |
| `FORCE-02` | How fast something looks is how fast it is going. | `hook-fly-or-plane` | `compare-pair-2` | `speed` |
| `FORCE-03` | The average speed for a journey is the average of the speeds you travelled at. | `average-commit` | `walk-run-tally` | `speed` |
| `FORCE-04` | Speed is worked out by dividing the two numbers in the order you were given them. | `build-steps` | `build-reveal` | `speed` |
| `FORCE-05` | A distance–time graph is a picture of the route: the line going up means going uphill. | `think-commit-cyclist` | `think-reveal-cyclist` | `distance-time-graphs` |
| `FORCE-06` | A flat line on a distance–time graph means moving at a steady speed. | `read-back-q1` | `read-back-reveal` | `distance-time-graphs` |
| `FORCE-07` | A steeper line means it went further. | `ladder-r2` | `ladder-r2-feedback` | `distance-time-graphs` |
| `FORCE-08` | An object has one true speed; a speed measured from a moving train is an illusion. | `hook-commit-train` | `relative-frames` | `relative-motion` |
| `FORCE-09` | Two things moving towards each other pass at the speed of one of them. | `think-commit-headon` | `think-reveal-headon` | `relative-motion` |

Expected to resurface: `FORCE-03` in P2 (`energy-in-food`, all the rate work)
and anywhere a mean is taken over unequal intervals; `FORCE-05`/`06` in P6
(waves on a graph) and in **any** graph lesson in biology or chemistry —
`B10 variation` plots something completely different and the same reading error
arrives with it; `FORCE-08` in P4 (`what-forces-do-to-motion`) and P12
(`gravity-earth-moon-and-sun`).

`FORCE-04` is worth a second look: it is arguably the same wrong idea as
`PART-05`-style "the numbers do what they are told", i.e. a mathematics
misconception wearing a science costume. It is the one on this list I would
most expect to be re-homed.

---

## 5. Statutory coverage

| Lesson | Statements |
|---|---|
| `speed` | `KS3.P.MOT.01` |
| `distance-time-graphs` | `KS3.P.MOT.02`, and `KS3.WS.ANA.02` (present data using tables and graphs) |
| `relative-motion` | `KS3.P.MOT.03` |

All three MOT statements are covered by the unit, none is covered twice, and
nothing outside MOT is taught as core. `speed` also does the WS work of
repeat readings and means (`KS3.WS.ANA.01`), which is why rung 3 is a
measurement rung rather than a fourth calculation.

---

## 6. For Code

- **Four new instrument kinds**, specified in §2. The lesson pages contain
  working implementations; they are the specification, not the shipping code.
- **Range inputs are bound to both `input` and `change`**, as established last
  round. Both light-gate and relative-frames sliders depend on it.
- **The plotting grid is real buttons, not canvas hit-testing** (§2.2). If that
  is re-implemented as canvas clicks during the port, it will silently drop
  keyboard access — the R15 failure will not show up in a screenshot.
- **Every canvas animation runs off one `requestAnimationFrame` loop per
  lesson** and mutates instance fields, not React state, so a 60 fps animation
  does not re-render the page. The only `setState` calls from inside a loop are
  at run boundaries. Please keep that shape.
- **`prefers-reduced-motion` is read once on mount** and every instrument has a
  complete non-animated path (light gates resolve instantly, journey-match
  draws the finished line, relative-frames freezes with the readouts intact).
  There is also a user-facing freeze/slow control on two of the three, because
  a student on a school Chromebook may want it without changing an OS setting.
- **Six rail stops in `p3-01`, five in the other two.** The rule I applied:
  a section is a rail stop when it requires a commitment or a completion count,
  including single-tap commitments inside the `think again` block. The
  vocabulary cards in `p3-01` sit **inside** the STEPS section and are not a
  separate stop — they land where the words have just done work.
- **Nothing on any page names a year or a half term.** Grep for "Year" comes
  back clean.
- **Cross-links** use the generator's output names (`p3-02-distance-time-
  graphs.html`), not the `.dc.html` authoring names.

---

## 7. Hand-over note on B1 — not edited, as instructed

While inheriting the pattern from `b1-06-unicellular-organisms.dc.html` I
noticed one thing. **I have not touched the file.**

- `b1-06` declares a `railLabels` boolean prop in `data-props` (section
  "Progress rail") that the logic class never reads. It renders a Tweaks
  control that does nothing. Harmless in the browser, but it will look like a
  broken toggle to anyone reviewing tweaks, and it should either be wired or
  removed when Code touches that file. It is the only one I found; `showDraft`,
  `startMount` and `motionDefault` are all live.

---

## 8. What I would want ruled before the next unit

1. Whether P3 is the intended unit (§0) — this gates everything.
2. `FORCE` vs a new `MOT` family for kinematics misconceptions (§4).
3. km/h → m/s in or out at KS3 (flag 3).
4. Whether "distance travelled vs distance from the start" stays as stretch
   (flag 7).
5. Whether the QUANTITATIVE pattern in §1 is the one you want fixed, since the
   next three units contain four more QUANTITATIVE lessons and they will
   inherit it.


---

## Change log — 15 Aug 2026 (review round 2)

Four changes from Mide's review, applied across every lesson that carries a
formula. Nothing else was touched.

1. **FIFA is now visible as FIFA.** The worked example and the scaffolded
   attempt both show a lettered badge on each step — **F**ormula, **I**nsert,
   **F**ine-tune, **A**nswer — matching the pattern set in `b1-02`. Step 3 was
   called "Work it out" in round one and is now **Fine-tune**, which is the
   step the letter stands for: do the arithmetic, sort the units, rearrange if
   the thing asked for is not the one on the left. The terser round-one copy is
   kept — the badges were added, the prose was not.
2. **Every formula now carries the cover-the-one-you-want panel.** A drawn
   figure with the chosen quantity physically covered, three cover buttons, the
   arrangement that falls out, and one sentence saying why. It is a real
   instrument, not a static picture.
3. **Ramp height is now visible in the light-gate bench** (`p3-01` only): low,
   medium and high each draw a different ramp, with the slope picked out and a
   height bracket up the back. Changing the setting changes the picture, which
   is what a student needs before the times change too.
4. Notes updated; the three unit zips were rebuilt.

### New instrument kind: `cover-triangle`

Shared shape across all three lessons that use it, and the one to build once.

- **Controls:** one button per quantity in the relationship ("Cover s",
  "Cover d", "Cover t").
- **Readouts:** the drawn figure with an opaque plate over the chosen
  quantity (the covered label stays faintly visible underneath, so a student
  can see what they covered); the arrangement that results, in display type;
  one sentence naming the operation and why.
- **Payload:** `{shape: 'triangle'|'bar', cells: [{id, label, slot:
  'top'|'left'|'right'}], covered: id, results: {id: {result, sentence}}}`.
- **aria-label** describes the mechanism: *"A formula triangle. Distance sits
  above a dividing line; speed and time sit below it, multiplied together.
  Covering one letter leaves the way to work it out."*
- **Reduced motion:** nothing animates; the plate simply appears.

### What this changes in the QUANTITATIVE pattern (§1)

Step 4 of the pattern now reads: *the formula alone in its own block, **drawn
and coverable**; the worked example revealed one step at a time with the FIFA
letters shown; the student filling in the same steps on their own numbers.*
The cover panel is part of the family from here on, not an extra.
