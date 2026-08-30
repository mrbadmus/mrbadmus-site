"""C1 L4 — Gas pressure (MODEL).

Authored against Design's approved page,
`docs/ks3/design-reference/c1/c1-04-gas-pressure.dc.html` (820 lines), and its
measured specification, `docs/ks3/c1-inventory/PAYLOAD-MAP.md` §4.

Every student-facing string is byte-identical to the approved page. The
module-scope constants (`TEMPS`, `VOLS`, `COUNTS`, `PREDICTIONS`, `RUNGS`,
`SELF_RUNGS`, `RAIL`) came through `node tools/extract_design_payload.js`; the
strings Design authored INSIDE `renderVals()` — the six `benchNote` branches
(631–644), the `marksLabel` pair (720), the computed `benchAlt` (705–706) and
the single shared wrong-answer fallback (738) — were lifted by hand from the
frozen page at the line numbers the map records.

── This page is the parity reference for a third of the key stage ───────

48 of the 144 registered components are measured on this page, so its spine has
to keep rendering all of them: `.ks3-check`, `.ks3-hook`, `.ks3-misconception`,
`.ks3-keynote`, `.ks3-check .ks3-option`, `.ks3-dark .ks3-option`, the whole
ladder, `.ks3-stretch .ks3-layer-body` and `.ks3-tutor`. Nothing here is
simplified away — the block sequence is Design's, in Design's order, and the
gate's options and the ladder's options both go through the shared
`.ks3-option` control rather than growing a private one.

── Two instruments, and why neither is a `sim` ──────────────────────────

**`collision-counter`** (`#s-bench`) is NOT `SIM_ARIA`'s `gas-pressure`. That
kind is "gas particles bouncing inside a box with a **movable wall**" with a
readout "in words", built by `r_sim` as sliders. Design draws three three-way
segmented groups, a bumps toggle, a live one-second rolling count, a pressure
bar and a fixed-size reference particle, with every readout drawn INSIDE the
canvas. Porting onto `gas-pressure` would drop the bumps toggle, and the bumps
toggle is PART-08's entire confrontation: the grey rings are drawn precisely so
a student can see a crowd of particle-to-particle collisions that the wall
never feels and the count never counts.

⚖️ THE COUNTING IS REAL, NOT A FORMULA. Every wall bounce pushes a timestamp
and entries older than 1000 ms are shifted off, so the number on screen is an
actual count of the last second — which is why "smaller box, same particles,
same speed, and the count is up" is something a student watches happen rather
than something the page asserts. Flashes last 420 ms.

⊕ AND IT IS STILL COUNTED (Mide, 19 Aug 2026). The displayed figure is now a
mean of those counts over ~900 ms, latched twice a second, because the raw
count churned every frame and a student could not read it — let alone see
which WAY it moved when they pressed a control, which is the entire lesson.
Nothing became a formula: the samples averaged are counts divided by the time
spent counting them, and pressure is still exactly `displayed hits × 7`. What
changed is the shutter speed, not the instrument.

⚖️ REDUCED MOTION SCALES THE SPEED BY 0.35 RATHER THAN STOPPING, so the count
still runs and the instrument still teaches. Design's own value; the engine
asks for it inside the tick rather than once at construction (ruling R4).

**`prediction-stack`** (`#s-predict`) is three predictions in ONE block, each
with its own answer index and note, over a shared option set, with a single
shared fallback for a wrong answer. The generic `predict` kind is one prompt,
one option list and one reveal — the wrong shape, and rendering it as one would
lose two thirds of the block.

── Two corrections, both reported ──────────────────────────────────────

⊕ **The canvas aria-label gains the wall-hit count.** The readouts are drawn
inside the canvas, so they reach a screen reader only through `aria-label`, and
Design's label (705–706) reports temperature, container and particle count but
NOT the wall-hit number — the one number the lesson is about. Design's sentence
is carried byte-identical and the count is added as a second sentence, so
nothing is rewritten and nothing is missing. Map §4.6 names this finding.

⊕ **Rail stage 2's predicate is a SET, not a maximum.** Design writes
`touched = Math.max(prev.touched, N)` with N = 1 for temperature, 2 for volume
and 3 for count (709 / 713 / 717), so pressing ONLY the particle-count button
sets `touched = 3`, ticks the stage and makes the head read "all controls
tried" when one was. `three_controls_tried` below means what it says: three
DISTINCT control groups. Map §4.4 names this finding.

⚑ For Mide's science gate:
  * flag 6 holds — pressure is reported as a count and a bar, never in pascals.
    There is no unit anywhere on the bench, deliberately: `p = F/A` is a KS4
    calculation and naming a pascal here would invite it three years early.
    ⊕ SUPERSEDED BY MIDE, 19 Aug 2026, twice over, and kept here because the
    flag records what was believed and the ruling records what replaced it.
    First: pressure IS given a unit, in kilopascals — a `PRESSURE` caption
    over an unlabelled bar is a dial with no value on it, and the quantity
    the lesson exists to build was the one thing on the bench a student could
    not read off. It is a stated calibration (7 kPa per wall hit, anchoring
    the resting bench at atmospheric), never a computed `p = F/A`, so the
    flag's actual worry — KS4 arriving three years early — does not follow.
    Second, and later the same day: pressure is now the BIG number and wall
    hits the small one, because kilopascals are the science and hits are the
    mechanism that explains them.
  * The `benchNote` branch table has a hole Design left. At Warm / Large / 12
    particles no branch matches except the resting one, which opens "Twenty-four
    particles at room temperature." while the canvas draws twelve. Closing it
    needs ONE new authored sentence, which is content and therefore yours — the
    six branches below are reproduced exactly as drawn rather than patched with
    prose you have not seen.
  * The stretch layer's "about 100,000 pascals … something like a tonne pressing
    on your shoulders" is Design's arithmetic, not mine.
"""

# ── the three segmented control groups ───────────────────────────────────
# Page lines 355–357, lifted by `tools/extract_design_payload.js`. `v` is split
# into the name of the quantity it actually is, because one renderer reads all
# three and `v` would tell it nothing: a speed multiplier, a VOLUME factor and
# a particle count are three different things. (That middle one used to read
# "a linear box scale", and the line below is the whole reason it no longer
# does.)
TEMPS = [
    {"label": "Cold", "speed_multiplier": 0.55},
    {"label": "Warm", "speed_multiplier": 1},
    {"label": "Hot", "speed_multiplier": 1.75},
]
# ⊕ MRB-257, carried to MRB-254 — ONE RATIO, SAID FOUR TIMES.
#
# `scale` was a LINEAR figure — 0.62 and 0.4 — and the three things that read it
# each ended up stating a different ratio for the same dial:
#
#   the LABEL said            half            and  a quarter
#   the DRAWING showed        0.62² = 0.38    and  0.40² = 0.16 of the area
#   the PHYSICS gave          1/0.62 = ×1.6   and  1/0.40 = ×2.5 wall hits
#
# None of the three agreed with either of the others, and the lesson's FIRST
# prediction turns on the third. MRB-257 phase 4 had already fixed the graver
# fault — the dial reached `draw()` and nothing else, so the box got smaller and
# the hit rate did not move at all — and left the numbers as it found them. This
# is the rest of it.
#
# The field is now a VOLUME factor, which is what the label has always claimed
# it was, and the two readers derive from it rather than reusing it:
#
#   · WALL-HIT RATE is `1 / volume`, so half the volume is exactly twice the
#     hits and a quarter is exactly four times. That is `P ∝ 1/V` at constant
#     temperature — the relationship this lesson's `ks4_becomes` names as the
#     gas laws — and it is now true of the instrument rather than asserted
#     beside it.
#   · THE DRAWN BOX is scaled by `√volume` — 0.7071 and 0.5 — so its visible
#     AREA is a half and a quarter. A box drawn at linear 0.5 looks like a
#     quarter, and a student reading "Half size" over it learns that halving
#     means quartering.
#
# ⚠️ THE FIELD IS RENAMED `volume`, deliberately, rather than kept as `scale`
# with new numbers. `scale` is what `draw()` needs and it is now DERIVED; a
# field that still said `scale` while holding a volume would be read as a
# linear number by the next person, which is the mistake being fixed.
VOLS = [
    {"label": "Large", "volume": 1},
    {"label": "Half size", "volume": 0.5},
    {"label": "Quarter size", "volume": 0.25},
]
COUNTS = [
    {"label": "12", "n": 12},
    {"label": "24", "n": 24},
    {"label": "48", "n": 48},
]

# ── the shared option set for all three predictions ──────────────────────
# Page line 361. One list, three questions: what makes this a stack rather than
# three blocks is that the student answers the same three-way question about
# three different changes, so the three answers are comparable.
PREDICTION_OPTIONS = ["Goes up", "Stays the same", "Goes down"]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 161 character for character.
    "slug":        "gas-pressure",
    "title":       "Gas pressure",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # Carried across unchanged from the superseded body in
    # `ks3_data/chemistry_c1_particles.py` (lines 910–920). PAYLOAD-MAP §7.4:
    # the rebuild moves no coverage and no register entry.
    "covers":      ["KS3.C.PNM.01c"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 2},
                    {"id": "forces-and-fields", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 40,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚑ `requires` moves from `solids-liquids-and-gases` to `changes-of-state`,
    # because Design's endmatter draws "Before this lesson → Changes of state"
    # (line 318) and the endmatter's first card renders `requires`. The old
    # edge is not lost — `changes-of-state` itself requires
    # `solids-liquids-and-gases`, so the graph still reaches it, one hop out.
    "requires":    ["changes-of-state"],
    "assumes":     [],
    # The forward link Design draws on every C1 page (line 324).
    "references":  ["diffusion"],
    "connects_heading": "Next in this unit",
    "ks4_links":   ["chemistry/bonding/states-of-matter"],
    # ⚠️ AUTHORED AND CURRENTLY UNREAD, and it is a collision rather than an
    # oversight. §4.8.1 D renders `ks4_becomes` only when `ks4_links` is EMPTY,
    # and the superseded body's KS4 edge is carried across unchanged above — so
    # the third endmatter card renders the link and Design's sentence (line 329)
    # waits. Dropping either one loses something real: the edge is a true bridge
    # to a live KS4 page, and the sentence is what Design drew. Reported rather
    # than silently resolved; the fix is one rule in `r_endmatter`, not here.
    "ks4_becomes": "The gas laws — pressure, volume and temperature as "
                   "quantities you can calculate with, and the kelvin scale "
                   "that makes them work.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "An empty aerosol can carries a warning: do not put it on a "
                    "fire, it may explode. It is empty. What is there to "
                    "explode?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Page lines 347–353 for the labels, 651–658 for the predicates.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The empty can",     "done_when": "committed"},
        # ⊕ CORRECTED. Design's `touched >= 3` is a MAXIMUM over 1/2/3, so the
        # particle-count button alone ticks it. Three DISTINCT groups.
        {"anchor": "s-bench",  "short": "COUNT",
         "label": "Collision counter", "done_when": "three_controls_tried",
         "threshold": 3},
        {"anchor": "s-predict", "short": "PREDICT",
         "label": "Three predictions", "done_when": "all_predictions_answered"},
        # ⊕ R1 — `#s-think` asks for a commitment on every C1 page, so it is a
        # `predict` and it DOES tick. Not B1's static confrontation.
        {"anchor": "s-think",  "short": "THINK",
         "label": "Swelling particles", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Page lines 81–103.
    "phenomenon": {
        "kind": "narrative",
        "eyebrow": "Start here",
        "title": "Nothing in it, and it still bursts.",
        "prompt": "Shake the can and it sounds empty. Press the nozzle and "
                  "nothing comes out. Put it in a bonfire and within a minute "
                  "it will burst hard enough to be dangerous at ten metres.",
        "commit": "Commit to what bursts it.",
        "options": [
            "Leftover propellant liquid that boils",
            "The gas already inside, hitting the walls harder as it heats",
            "The metal expanding until it tears",
            "Nothing — an empty can is safe",
        ],
        "reveal": "The can is not empty. It is full of gas — it always "
                  "was, and it always will be, because there is no such thing "
                  "as a sealed can with nothing in it. Heat that gas and the "
                  "particles hit the walls harder and more often, and at some "
                  "point the steel gives way. Pressure is not a substance "
                  "stored in the can. It is a count of collisions.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Ids and statements from the register (`docs/ks3/misconception-register.md`
    # lines 105–106) and the superseded body; PAYLOAD-MAP §7.4 confirms the
    # rebuild moves neither. What moves is only WHICH block does the work.
    #
    # ⚠️ PART-09's statement is Design's own quote (line 206), not the
    # register's wording, and that is deliberate: `r_confrontation` prints the
    # lesson's authored statement over the register's, and the page's line is
    # the one a student reads.
    "misconceptions": [
        # Elicited by the bench's commit gate ("Particles pushing against each
        # other" is option A) and confronted by the bumps toggle inside the
        # counter — the grey rings ARE the confrontation.
        {"id": "PART-08",
         "statement": "Gas pressure is the particles pushing against each "
                      "other.",
         "elicited_by": "count-the-hits",
         "confronted_by": "count-the-hits"},
        {"id": "PART-09",
         "statement": "Heating a gas makes the particles swell up, so they "
                      "fill more of the can, so the pressure goes up.",
         "elicited_by": "three-predictions",
         "confronted_by": "think-swelling-particles"},
    ],

    # Design draws no keyword block and no figure slot anywhere in C1
    # (PAYLOAD-MAP §0.7) — but "does not render in the lesson body" is not the
    # same as "is not needed". The TERMS render as the unit page's "Words this
    # unit gives you" chips (build_ks3.py:7851) and the reading-age gate reads
    # them as its exclusion list, so `vocabulary` carries the superseded body's
    # two terms rather than being empty. `figures` genuinely is empty: the
    # counter draws itself on canvas, `phenomenon` names no `art`, and nothing
    # on the page references a figure.
    "vocabulary": [
        {"term": "pressure",
         "definition": "How hard a force pushes on each bit of a surface.",
         "note": "You will meet pressure = force ÷ area as a calculation in "
                 "Physics P5."},
        {"term": "collision",
         "definition": "When a moving particle hits something and bounces off.",
         "note": None},
        # ⊕ ADDED by the rebuild. Temperature is one of the bench's three
        # control groups, it is the subject of prediction 2, of rung 2 and of
        # the whole `#s-think` confrontation, and the lesson's answer to "what
        # does heating change?" is a definition in all but name: speed, and
        # nothing else. The superseded body left the word undefined.
        {"term": "temperature",
         "definition": "How hot or cold something is. The hotter something is, "
                       "the faster its particles are moving.",
         "note": "Heating changes how fast the particles move and nothing else "
                 "— never their size."},
    ],
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page line 106.
        {"type": "explainer",
         "text": "Pressure is the one idea in this unit that people think they "
                 "already understand, which is what makes it dangerous. It "
                 "feels like a squeezing, or a crowdedness, or a force held "
                 "inside the container. It is none of those. It is particles "
                 "hitting a wall, and the whole of this lesson is a machine "
                 "for counting them."},

        # ── #s-bench · collision-counter ─────────────────────────────────
        # A LIGHT `.ks3-block` (page line 109 carries no `ks3-dark`), which
        # `_INSTRUMENT_SEGMENTS` maps to the `check` shell. Painting it on ink
        # would resolve every text token wrong and would put the canvas's own
        # cream drawing on a black surround.
        {"type": "collision-counter", "id": "count-the-hits",
         "anchor": "s-bench",
         "demand": "investigate",
         "targets": "PART-08",
         "eyebrow": "The collision counter · change one thing at a time",
         "heading": "Count the hits on the wall.",
         # Page line 691. `full` is the terminal label Design writes instead of
         # "3 of 3", and it lives beside its own format string rather than in a
         # second key somewhere else — one readout, one place.
         "head_counter": {"format": "{n} of 3 controls tried", "total": 3,
                          "full": "all controls tried"},

         # The commit gate, page lines 118–132. Gating by ABSENCE: answered,
         # the question is gone and the bench arrives in the space it held.
         "gate": {
             "prompt": "Commit first. What actually causes the pressure inside "
                       "a sealed container of gas?",
             "options": [
                 "Particles pushing against each other",
                 "Particles hitting the walls of the container",
                 "The gas trying to escape to a bigger space",
                 "The weight of the gas pressing down",
             ]},

         "temps": TEMPS,
         "vols": VOLS,
         "counts": COUNTS,
         # Page line 419–422: Design's `startTemp` prop defaults to Warm, and
         # `vol: 0, count: 1` are the state's own literals. The resting bench is
         # 24 particles in the large box at room temperature, which is exactly
         # what the resting note describes.
         "start": {"temp": 1, "vol": 0, "count": 1},

         # The three group captions, page lines 140 / 148 / 156.
         "labels": {"temperature": "Temperature",
                    "volume": "Size of the container",
                    "particles": "How many particles"},

         # ⚖️ PART-08's CONFRONTATION. Page lines 165–166 and 492–500. The two
         # button labels are Design's pair (line 720); `caption` is the sentence
         # beside it that says in words what the rings show. `threshold` is the
         # SQUARED separation below which two particles count as bumping, in the
         # box's own 0–1 coordinates — Design's own 0.0022 (line 497).
         "bumps": {"on_label": "Show particle-to-particle bumps",
                   "off_label": "Hide particle-to-particle bumps",
                   "caption": "Particle-to-particle bumps are marked in grey. "
                              "They never touch the wall, so they never add to "
                              "the pressure.",
                   "threshold": 0.0022},

         # Everything drawn INSIDE the canvas. Authored here rather than baked
         # into the drawing code so the words a student reads are in the lesson
         # record like every other authored string in the key stage.
         "canvas_labels": {
             "reference": "ONE PARTICLE — SAME SIZE AT EVERY SETTING",
             "hits": "WALL HITS PER SECOND",
             "pressure": "PRESSURE",
             # ⊕ RULING (Mide, 19 Aug 2026). kPa, not Pa — the unit a student
             # meets on a weather chart and a tyre gauge, and the one that
             # puts atmospheric at a memorable 100 rather than 101325.
             "pressure_unit": "kPa",
             "temperature": "TEMPERATURE",
             "container": "CONTAINER",
             "particles": "PARTICLES"},

         # The bar's full-scale reference: it fills to `min(1, hits / 170)`.
         "pressure_full": 170,

         # ⊕ RULING (Mide, 19 Aug 2026), SUPERSEDING NOTES flag 6. Flag 6 said
         # "pressure is a count and a bar here, never a pascal — the quantity
         # arrives at KS4 with p = F/A behind it". What that produced on the
         # live bench was a `PRESSURE` caption over an unlabelled bar: a dial
         # with no value on it. The number IS the science, and a bar without
         # one teaches nothing quantitative about the very quantity the lesson
         # is building. Pressure is now drawn in kilopascals beside the bar.
         #
         # ⚖️ IT IS A CALIBRATION, AND THE PAGE NEVER CLAIMS OTHERWISE. Twelve
         # particles in a box do not have a pressure worth computing; doing it
         # literally would give about 10⁻²³ kPa, which is rigour used as a lie.
         # This bench is a model of a SAMPLE of a real gas, so it is anchored:
         # the resting setting (Warm · Large · 24) runs at 14.4 wall hits per
         # second, and 7 kPa per hit puts that at ~101 kPa — atmospheric.
         #
         # ⚖️ AND LINEARITY IS THE WHOLE POINT. Pressure is `hits × 7` and
         # nothing else, so double the hit rate is exactly double the pressure
         # at all 27 control combinations. Every prediction in this lesson —
         # smaller box, hotter, more particles — is a statement about that
         # proportionality. A reading that curved, floored, capped or smoothed
         # would quietly teach the opposite. Do not add any of those.
         "kpa_per_hit": 7,
         # ⊕ RULING (Mide, 19 Aug 2026), ANSWERING THE LINE DIRECTLY ABOVE.
         # The flag is kept, not deleted, because what it protects is still
         # protected. It guards ONE property — pressure exactly proportional
         # to the hit rate — and that is untouched: the bench draws
         # `shown_hits × 7` and nothing else, so the arithmetic holds on the
         # two numbers a student can actually see. What is smoothed is the
         # MEASUREMENT, not the relationship. The shipped bench swung 11 to 16
         # hits (77 to 112 kPa) several times a second, which does not teach
         # proportionality either; it hides it behind a number nobody can read.
         # A curve, a floor or a cap would each change kPa AS A FUNCTION OF
         # hits, and none of those is here.
         #
         # `smooth_ms` is how much simulation one displayed reading averages
         # over; `readout_ms` is how often the display is allowed to change.
         # Both are teaching decisions in exactly the way `window_ms` is: a
         # dial a student cannot read is not a more truthful dial.
         "smooth_ms": 900,
         "readout_ms": 500,
         # The rolling window IS the measurement (page line 501), and the flash
         # is how long one collision stays visible (502). Both authored because
         # both are teaching decisions: a 1000 ms window is what makes the
         # number "hits per second" rather than "hits since you arrived".
         "window_ms": 1000,
         "flash_ms": 420,
         # ⊕ Ruling R4. Reduced motion SLOWS the gas rather than freezing it, so
         # the count keeps running and the instrument stays complete. Design's
         # own 0.35 (line 474); the difference is that the engine asks every
         # frame instead of once at construction.
         "reduced_motion_scale": 0.35,

         # The six authored branches, page lines 631–644, IN DESIGN'S ORDER OF
         # EVALUATION — the order is load-bearing, not incidental. `bumps` wins
         # over everything, because when the rings are on they are the subject;
         # `smaller_box` is narrower than `hot` and so must be asked first.
         "notes": {
             "bumps": "The grey rings are particles bumping into each other in "
                      "the middle of the box. There are plenty of them, and "
                      "not one contributes to the pressure — the wall "
                      "never feels them. Pressure is only ever what arrives at "
                      "the wall.",
             "smaller_box": "Smaller box, same particles, same speed — "
                            "and the count is up. Nothing about the gas "
                            "changed; the wall simply moved closer, so each "
                            "particle gets back to it sooner.",
             "hot": "Hot. The count jumps, and notice the reference particle "
                    "at the bottom left has not changed size by a single "
                    "pixel. Speed is doing all the work.",
             "cold": "Cold. Fewer arrivals per second and each one softer. "
                     "Cool a sealed can enough and the outside air will crush "
                     "it, which is the same idea from the other side.",
             "more_particles": "More particles, so more of them arriving. This "
                               "is what you are doing to a tyre when you pump "
                               "it up — not squashing the air, just "
                               "putting more of it in.",
             "resting": "Twenty-four particles at room temperature. Every "
                        "orange flash is one collision with a wall, and the "
                        "number above is how many happened in the last "
                        "second."},

         # ⊕ CORRECTED (map §4.6). Design's sentence is carried byte-identical
         # and ends at "each second."; the wall-hit count is ADDED as a second
         # sentence, because it is the one number the lesson is about and a
         # screen reader can reach it nowhere else — every readout is drawn
         # inside the canvas.
         # ⊕ AND THE PRESSURE JOINS IT (19 Aug 2026), for exactly that reason.
         # It is drawn inside the canvas like everything else, so a label
         # without it would show the ruled figure to sighted students only.
         "alt": {"template": "A sealed box of gas particles at {temp} "
                             "temperature, container {vol}, with {n} "
                             "particles, and a live count of collisions with "
                             "the walls each second. Wall hits in the last "
                             "second: {hits}. Pressure: {kpa}."}},

        {"type": "key-fact", "ref": "pressure-is-collisions"},

        # ── #s-predict · prediction-stack ────────────────────────────────
        # An ink-dark `.ks3-practical` (page line 179), which is what
        # `_INSTRUMENT_SEGMENTS` maps the kind to.
        {"type": "prediction-stack", "id": "three-predictions",
         "anchor": "s-predict",
         "demand": "predict",
         "targets": "PART-09",
         "eyebrow": "Three predictions · then check them on the bench",
         "heading": "Say what will happen before you do it",
         "prompt": "Each of these changes exactly one thing. Predict the "
                   "effect on the wall-hit count, then go back up and try it.",
         # One option set, three questions (page line 361).
         #
         # ⚠️ NOT `options`, which the map's payload block names. `options` is
         # the SHELL's key: `r_activity` renders any `options` it finds as a
         # standard A/B/C answer list, so adopting the map's name emitted a
         # fourth, orphaned copy of "Goes up / Stays the same / Goes down"
         # under the three panels — a list Design does not draw and that
         # answers no question. Measured on the built page, not reasoned about.
         "shared_options": PREDICTION_OPTIONS,
         # Page lines 359–369.
         "predictions": [
             {"id": "p1",
              "question": "The container is made smaller, and nothing else "
                          "changes. What happens to the wall hits each second?",
              "answer": 0,
              "note": "Up. The particles are travelling no faster, but the "
                      "walls are closer, so each particle completes the "
                      "journey between walls more often. Same speed, shorter "
                      "trip, more arrivals."},
             {"id": "p2",
              "question": "The gas is heated, and the container stays exactly "
                          "the same size. What happens to the wall hits each "
                          "second?",
              "answer": 0,
              "note": "Up — and for two reasons at once. Faster particles "
                      "cross the box more often, and each collision carries "
                      "more punch. Both push the pressure up."},
             {"id": "p3",
              "question": "Half the particles are removed, and the temperature "
                          "and container stay the same. What happens to the "
                          "wall hits each second?",
              "answer": 2,
              "note": "Down, by about half. Each remaining particle behaves "
                      "exactly as it did — there are simply fewer of them "
                      "arriving. This is what happens when a tyre leaks."},
         ],
         # ⚠️ ONE shared string for every wrong answer on all three, authored
         # inside `renderVals` at line 738 and therefore absent from the
         # extracted constants — lifted by hand. It sends the student back to
         # the bench instead of giving the answer away, which is why there is
         # only one of it: per-prediction wrong-answer prose would be three
         # more chances to leak the right answer.
         "wrong_note": "Not quite — go back to the bench and try it "
                       "before reading on. Change only the one thing the "
                       "question changes."},

        {"type": "misconception", "id": "think-swelling-particles",
         "anchor": "s-think", "targets": "PART-09"},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Page lines 174–177. ⊕ R3 — `ground: "card"` is authored and the shipped
    # stylesheet's geometry wins; the page's 28px / 22px 26px / 6px 6px /
    # 25px / 1.32 are per-page drift and are not chased. One stylesheet serves
    # 183 lesson slots.
    "key_facts": [
        {"id": "pressure-is-collisions",
         "text": "Gas pressure is caused by particles colliding with the walls "
                 "of the container. More collisions, or harder ones, means "
                 "more pressure.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # The two instruments above are lifted into this list by
    # `ks3_data/c1/__init__.py::_normalise`; only the confrontation is authored
    # here, because it is the one activity that is not an instrument.
    "activities": [
        # ⊕ R1 — a `predict`, not a `confrontation`. The block asks for a
        # commitment (page lines 209–218) and gates its reveal behind it, so it
        # is a rail stop and it ticks. Page lines 201–227.
        {"id": "think-swelling-particles",
         "kind": "predict",
         "demand": "explain",
         "targets": "PART-09",
         "prompt": "This explanation gets the right answer for the wrong "
                   "reason, which is the hardest kind of wrong idea to shift. "
                   "Commit.",
         "options": [
             "True — hotter particles are bigger particles",
             "The particles move faster; their size never changes",
             "The particles multiply, so there are more of them",
             "The particles get heavier, so they hit harder",
         ],
         # Three paragraphs, page lines 222–224. The `<em>` on "speed" is
         # Design's and survives through `rich()`.
         "reveal": [
             "Heating changes the <em>speed</em> of the particles and nothing "
             "else. The reference particle at the bottom of the bench is drawn "
             "at the same size at every temperature setting, and that is not a "
             "simplification — it is the fact.",
             "Here is the test that separates the two explanations. If heating "
             "made particles swell, a hot gas would be harder to squash than a "
             "cold one, because the particles would be taking up more of the "
             "room. It is not. A hot gas squashes just as easily. And if the "
             "particles swelled, the gas would eventually become a solid block "
             "of touching particles — the opposite of what heating does.",
             "Faster particles reach the wall more often, and hit it harder "
             "when they get there. Two effects, one cause, no swelling.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Page lines 371–413. Rung titles are Design's; `_rung_title` strips the
    # "Rung N · " prefix and the engine puts the number back, so both authoring
    # styles render identically.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Recall",
            "q": "What causes the pressure of a gas on the walls of its "
                 "container?",
            "options": [
                "Particles pushing against each other",
                "Particles colliding with the walls",
                "The weight of the gas pressing down",
                "The gas trying to escape",
            ],
            "answer": 1,
            "feedback": {
                0: "Particles do bump into each other, but those bumps are "
                   "nowhere near the wall and do nothing to it.",
                2: "Pressure acts on the top and sides of a container as much "
                   "as the bottom. Weight cannot explain that.",
                3: "Particles have no aim. They travel in straight lines until "
                   "something is in the way.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A sealed metal can of gas is heated. The can does not change "
                 "size. Which of these has NOT changed?",
            "options": [
                "The average speed of the particles",
                "The size of the particles",
                "The number of wall collisions each second",
                "The pressure inside the can",
            ],
            "answer": 1,
            "feedback": {
                0: "Speed is exactly what heating changes.",
                2: "Faster particles reach the wall more often, so this rises.",
                3: "This is what rises, and it is why the warning is on the "
                   "can.",
            }},
        "explain": {
            "title": "Rung 3 · Explain",
            "q": "A bicycle pump is sealed at the end and the handle is pushed "
                 "halfway in. Explain, in terms of particles, why it gets "
                 "harder and harder to push.",
            "field_label": "Your explanation",
            "placeholder": "The same number of particles…",
            "success": [
                "Says the number of particles inside is unchanged.",
                "Says the space they are in has been made smaller.",
                "Says each particle now reaches a wall more often, because it "
                "has less distance to travel.",
                "Says more collisions per second on the walls means higher "
                "pressure.",
                "Says the higher pressure pushes back harder on the handle "
                "— the particles are not being squashed themselves.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A car tyre is correctly inflated on a cold morning. After an "
                 "hour of motorway driving, the pressure gauge reads "
                 "noticeably higher, and no air has been added. Explain, and "
                 "say what a driver should NOT conclude from it.",
            "field_label": "Your answer",
            "placeholder": "Driving heats the tyre because…",
            "success": [
                "Says friction with the road and flexing of the rubber heat "
                "the air in the tyre.",
                "Says the particles move faster when heated.",
                "Says faster particles hit the tyre wall more often and "
                "harder.",
                "Says the number of particles has not changed — no air "
                "has been added.",
                "Says the driver should not let air out to correct it, because "
                "the pressure will fall again as the tyre cools.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Page line 301.
    "key_note": "Pressure = collisions with the wall. Heat it and they come "
                "faster and harder. Shrink it and they come more often. Add "
                "particles and there are more of them arriving. Nothing "
                "swells, and particle-to-particle bumps do not count.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Page lines 304–312. ⚑ MRB-225 — this is where the "you are under pressure
    # right now" argument belongs, and nothing in the lesson body is retracted
    # by it: the body says pressure is a count of collisions, and this says the
    # same thing about the air outside you.
    "stretch": [
        {"type": "explainer", "id": "atmospheric-pressure",
         # ⚠️ This used to read "the weight of roughly ten metres of
         # atmosphere" (c1-13, chem audit 25 Aug 2026) — short by a factor of
         # a thousand: ten metres of AIR is about 120 Pa. 100,000 Pa is the
         # whole air column, tens of kilometres of it, and it pushes about as
         # hard as ten metres of WATER. The ten-metre image is kept and made
         # true. The follow-on arithmetic needed no change: 100,000 N/m² over
         # roughly 0.1 m² of shoulder really is about a tonne-force, so the
         # passage now agrees with itself in both directions.
         "text": "You are under pressure right now — about 100,000 "
                 "pascals of it: the weight of the whole depth of the "
                 "atmosphere above you, which pushes about as hard as ten "
                 "metres of water would, and works "
                 "out at something like a tonne pressing on your shoulders. "
                 "You cannot feel it because the same pressure is pushing out "
                 "from inside you, and the two balance exactly. Remove one "
                 "side of that balance and it becomes obvious immediately: a "
                 "sealed plastic bottle brought down a mountain crumples on "
                 "its own, and a suction cup holds a shelf up using nothing "
                 "but the air that is not inside it. Nothing sucks, ever. "
                 "Things get pushed, by particles, from the side where there "
                 "are more of them."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # Page lines 331–335. The CTA points at this page's own flagship, which is
    # a real destination on the page it is printed on.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still picturing pressure as particles pushing each "
                      "other?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # Carried across unchanged from the superseded body.
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
