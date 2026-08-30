"""C7 L1 — Energy and changes of state (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c7/c7-01-energy-and-changes-of-state.dc.html`, and
her author's notes `docs/ks3/design-reference/c7/NOTES-C7.md` §1, §2, §3,
§4 flags 2, 3, 4, §5 (`ENER-01`, `ENER-02`) and §6.

Every student-facing string is byte-identical to the approved page except
where a change is marked ⚑ below and reported to the commander. `RAIL`,
`USES`, `RUNGS` and `SELF_RUNGS` came out of the node extractor; the hook
options and reveal, the two explainer paragraphs, the curve block's eyebrow /
heading / lead / button labels, the closing panel, the key fact, the `#s-uses`
eyebrow and heading and lead, the `#s-think` options and its two reveal
paragraphs, the key note and both "Going further" paragraphs were lifted from
`lessonVals(s)` and from the markup, which is where most of this lesson's
words live and where a lift of the top-level constants alone silently loses
them.

═══════════════════════════════════════════════════════════════════════════
⭐ RULING 1 — THE CURVE'S DATA IS REBUILT, BECAUSE THE DATA IS THE ERROR
═══════════════════════════════════════════════════════════════════════════

NOTES-C7 §4 flag 2 is the unit's one real defect and Design flagged it herself:

    "melting flat step 3 minutes, boiling flat step 3 minutes, in a 12-minute
     run. The boiling step is described in the text as 'much longer' than
     melting, which is true in reality (roughly 7× the energy) but **is not
     what the graph shows** … Either the curve gets a longer boiling step or
     the text stops claiming one. Ruling wanted."

The standing build law is *where prose and instrument disagree, the instrument
is the measurement*, and it exists so that nobody fudges DATA to rescue a
SENTENCE. Here the sentence is right and the data is wrong: the specific latent
heat of fusion of water is 334 kJ/kg and of vaporisation 2260 kJ/kg, so at
constant power boiling takes about 6.8 times the energy of melting the same
mass. **So the data changed.** Ruled by the commander, 21 Aug 2026.

    melting plateau   3 minutes flat at   0 °C   — Design's own, unchanged
    boiling plateau   8 minutes flat at 100 °C   — 2.67× as she drew it

The arithmetic, because the point counts are easy to get wrong. A plateau of
*n* minutes is *n + 1* consecutive readings at the same temperature: the
reading on arrival, then one per minute of waiting.

    idx  0  1        −20, −10          ice below freezing        2 readings
    idx  2  3  4  5    0               melting  → 3 min flat     4 readings
    idx  6  7         30,  60          liquid warming            2 readings
    idx  8 … 16      100               boiling  → 8 min flat     9 readings
    idx 17           120               steam                     1 reading
                                                                ───────────
                                                            18 readings

Design's `t`, `state` and per-point `note` are kept wherever they are still
true. Six boiling notes are new prose, marked ⚑ below; every one of them is
teaching rather than filler, because a student who taps eight times deserves
eight things to read.

⚠️ AND THE LESSON SAYS IN WORDS THAT THE DRAWING IS NOT TO SCALE. Nine bars at
100 °C against four at 0 °C is 2.25 : 1 drawn, where the plateaus it represents
are 8 : 3 and the ENERGY they represent is about 7 : 1. Three different ratios,
and only one of them can be a bar chart. So the closing panel states flatly
that the curve is a schematic, that the sloping parts are not to scale, and
that boiling really takes about seven times the energy of melting. Never
present an invented figure as a measurement.

═══════════════════════════════════════════════════════════════════════════
⭐ RULING 2 — THE EQUAL-SLOPE CLAIM IS DELETED, NOT REVERSED
═══════════════════════════════════════════════════════════════════════════

Design's note at `CURVE` index 6 read:

    "Climbing again, at the same rate as it climbed through the ice."

That is false. Ice has a specific heat capacity of about 2.1 kJ/kg/K and
liquid water about 4.18, so at constant power ice warms roughly twice as fast
per joule. It also contradicts her own drawn slopes, which are +10 °C/min
through the ice and +30 °C/min through the water.

It is REMOVED rather than corrected, and that is the ruling. The drawn slopes
cannot carry all four rate relationships truthfully on one tappable curve:
liquid water spans 100 °C and ice only 20 °C, so any usable number of steps
makes water's drawn slope the steeper one, whichever way the sentence is
written. **The teachable content of a heating curve is the PLATEAUS, not the
slopes.** The note at index 6 is replaced with one about the plateau that has
just ended, and no slope comparison is made anywhere on this page.

═══════════════════════════════════════════════════════════════════════════
THE OTHER FLAGS
═══════════════════════════════════════════════════════════════════════════

⚑ flag 3 — LATENT HEAT IS NAMED IN THE STRETCH ONLY, accepted as drawn. It is
not in the main body, not in the vocabulary cards and not in the key note. A
student meets the phenomenon on the bench and the name in the layer they chose
to open, which is the right order.

⚑ flag 4 — JOSEPH BLACK AND WATT stay, accepted as drawn. Historically sound,
and it is the one place in the unit where a student is shown that this idea
was worked out by somebody rather than always known.

⚑ USE 2 IS WHY THIS LESSON HAS A `safety_note`. Steam at 100 °C against water
at 100 °C is a real burn and the page says so; the note names the guard that
belongs with it. It is not a safeguarding block — nothing here touches a
student's own body, health or circumstances in that sense — and C3, C4 and C5
carried none for the same reason.
"""

# XU-1 (MRB-295/MRB-298, ruled 28 Aug 2026). The estate held four
# definitions of temperature and three were wrong. There is now one, and it
# is authored in ks3_data/quantities.py rather than retyped here.
from ..quantities import (TEMPERATURE_CRITERION, TEMPERATURE_OPTION,
                          TEMPERATURE_SENTENCE, TEMPERATURE_VOCAB)  # noqa: F401


# ── the heating curve (Design's `CURVE`, rebuilt under RULING 1) ─────────
#
# ⚠️ `t` IS THE MEASUREMENT AND EVERY OTHER NUMBER ON THE PAGE IS DERIVED FROM
# IT. The trace bar's height, whether a point is flat, how long each plateau
# runs and the sentence counts in the closing panel are all computed from this
# list at build time. Nothing is written down twice, so a future re-pointing of
# this instrument at a different substance is one array and no prose.
_CURVE = [
    {"t": -20, "state": "Solid — ice",
     "note": "Below freezing. The particles are locked in a fixed arrangement "
             "and can only vibrate. Energy going in makes them vibrate "
             "faster, so the temperature climbs steadily."},
    {"t": -10, "state": "Solid — ice",
     "note": "Still solid, still climbing. Every joule from the flame is "
             "going into making the particles vibrate harder."},
    {"t": 0, "state": "Solid — at its melting point",
     "note": "The ice has reached 0 °C. The next joule of energy will not "
             "raise the temperature — it will start breaking particles out of "
             "the arrangement instead."},
    {"t": 0, "state": "Melting — solid and liquid together",
     "note": "The thermometer has stopped. The flame has not. Energy is being "
             "spent pulling particles out of the fixed arrangement, and "
             "separating particles does not make the remaining ones move any "
             "faster."},
    {"t": 0, "state": "Melting — solid and liquid together",
     "note": "Still 0 °C, still melting. This is the most energy-hungry part "
             "of the run so far, and the thermometer shows nothing at all."},
    {"t": 0, "state": "Just melted — all liquid",
     "note": "The last of the ice has gone. From here the energy has nothing "
             "to separate, so it goes back into making particles move "
             "faster."},

    # ⚑ RULING 2 — Design's index 6 said the liquid climbs "at the same rate
    # as it climbed through the ice". Removed, not reversed. This note is about
    # the plateau that has just ended, which is what the student has just spent
    # three taps watching.
    {"t": 30, "state": "Liquid — water",
     "note": "Climbing again, and the thermometer is working normally once "
             "more. The three flat minutes did not pause the flame — they "
             "were the energy that melted the ice, and it went somewhere a "
             "thermometer cannot look."},

    {"t": 60, "state": "Liquid — water",
     "note": "Still climbing. Some particles are already escaping from the "
             "surface as vapour — evaporation happens at any temperature — "
             "but the bulk of the liquid is simply warming."},
    {"t": 100, "state": "Liquid — at its boiling point",
     "note": "At 100 °C the liquid is about to change state throughout, not "
             "just at the surface. Bubbles of vapour can now form inside the "
             "liquid."},
    {"t": 100, "state": "Boiling — liquid and gas together",
     "note": "Flat again. Energy is now pulling particles completely away "
             "from each other, which takes far more than merely loosening "
             "them did at 0 °C."},

    # ⚑ Design's index 10, reworded so that it states the comparison as a
    # RATIO OF ENERGY rather than as a property of the drawing. Her sentence
    # ("the boiling step is longer than the melting step for a reason") was
    # true of reality and false of the graph it sat on; it is now true of both.
    {"t": 100, "state": "Boiling — liquid and gas together",
     "note": "Still 100 °C, and the flat run is going to be much longer this "
             "time. Loosening particles so they can slide takes a certain "
             "amount of energy; tearing them right away from each other takes "
             "several times as much."},

    # ⚑ Six new points, six new notes. RULING 1 lengthened the boiling plateau
    # from three minutes to eight, and eight taps need eight things to read.
    {"t": 100, "state": "Boiling — liquid and gas together",
     "note": "Four minutes at the same reading. Nothing is stuck and nothing "
             "is broken: the beaker is emptying, one particle at a time, into "
             "the air above it."},
    {"t": 100, "state": "Boiling — liquid and gas together",
     "note": "The bubbles are not air and they are not nothing. They are "
             "water in the gas state, forming inside the liquid because "
             "every part of it now has enough energy to break away."},
    {"t": 100, "state": "Boiling — liquid and gas together",
     "note": "This is the part of the run that a kettle spends most of its "
             "electricity on. Bringing the water to 100 °C is quick; turning "
             "it into steam is what takes the time and the energy."},
    {"t": 100, "state": "Boiling — liquid and gas together",
     "note": "Turn the flame up and the reading still says 100 °C. A bigger "
             "flame boils the water away sooner; it does not make boiling "
             "water hotter."},
    {"t": 100, "state": "Boiling — liquid and gas together",
     "note": "The steam leaving the beaker is carrying away every joule that "
             "has gone in since the reading stopped moving. That is where the "
             "energy is: not in the beaker, and not lost."},
    {"t": 100, "state": "Just boiled — all gas",
     "note": "The last of the liquid has gone. Everything in the beaker is "
             "now steam at 100 °C, carrying all the energy that boiling put "
             "into it."},
    {"t": 120, "state": "Gas — steam",
     "note": "Climbing once more. Steam above 100 °C is called superheated, "
             "and it is the state that does the work in a power station "
             "turbine."},
]

# ── the three judgements (Design's `USES`) ──────────────────────────────
#
# ⚠️ `correct` IS READ ONCE, AT BUILD TIME, AND REACHES NO MARKUP. It is the
# guard `r_energy_uses` asserts against: the answer paragraph a student reads
# has to be consistent with the option the record believes, or the page would
# be arguing with itself in front of them. Nothing here marks (R3).
_USES = [
    {"id": "use-sweat", "correct": "b",
     "q": "Why does sweating cool you down?",
     "options": [
         {"id": "a", "label": "The sweat is cold"},
         {"id": "b", "label": "Evaporating sweat takes energy from your skin"},
         {"id": "c", "label": "It makes the air move"},
     ],
     "answer": "Evaporation takes energy in, and it takes it from the nearest "
               "available source — your skin. The sweat leaves as vapour "
               "carrying that energy with it, and what is left behind is "
               "cooler. This is why a humid day feels so much worse: if the "
               "air is already saturated the sweat cannot evaporate, so the "
               "cooling mechanism stops working."},
    {"id": "use-steam", "correct": "b",
     "q": "Steam at 100 °C and water at 100 °C touch your hand. Which does "
          "more damage?",
     "options": [
         {"id": "a", "label": "The water"},
         {"id": "b", "label": "The steam"},
         {"id": "c", "label": "The same — equal temperatures"},
     ],
     "answer": "The steam, by a long way. Both are at the same temperature, "
               "so a thermometer cannot separate them — but the steam also "
               "carries all the energy that went into boiling it, and it "
               "releases that energy into your skin as it condenses. Same "
               "temperature, very different quantity of energy."},
    {"id": "use-frost", "correct": "a",
     "q": "Orange growers spray their trees with water when a frost is "
          "forecast. Does that help?",
     "options": [
         {"id": "a", "label": "Yes"},
         {"id": "b", "label": "No, it makes it worse"},
         {"id": "c", "label": "It makes no difference"},
     ],
     "answer": "It genuinely helps, and it looks like madness. Freezing gives "
               "energy out, so as the sprayed water turns to ice it releases "
               "energy into the fruit and holds the temperature at 0 °C — "
               "which is cold, but not cold enough to destroy the crop. The "
               "ice coating is doing the protecting."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 234 character for character.
    "slug":        "energy-and-changes-of-state",
    "title":       "Energy and changes of state",
    "discipline":  "chemistry",
    "unit":        "energy-changes-in-reactions",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # `KS3.C.ENER.01` — "energy changes on changes of state (qualitative)" —
    # is one bullet and one lesson, so the parent is owned whole and no clause
    # is minted for it. The three lessons that follow share `ENER.02`, which is
    # split in `ks3_data/substatements.py`.
    "covers":      ["KS3.C.ENER.01"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 3},
                    {"id": "substances-and-reactions", "level": 2}],
    "typical_year": 9,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # ⚠️ `requires` IS THE "BEFORE THIS LESSON" CARD, and Design draws
    # `c6-07-catalysts.html` there — the lesson immediately before this one in
    # the published sequence. NOTES-C7 §2 also says "c7-01 requires C1", which
    # is a different claim: the particle model is what the whole page argues
    # in. That is a `references` edge, not a prerequisite card, because a
    # student arrives here from C6 and not from C1.
    "requires":    ["catalysts"],
    "assumes":     [],
    "references":  ["changes-of-state"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Keep heating a beaker of melting ice and the thermometer "
                    "refuses to move. The energy is still going in — so where "
                    "is it going?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL`, in her order with her ids and her short
    # labels, and matching `docs/ks3/rail-manifest.md` stop for stop
    # (MRB-249). `done_when` restates her own `DONE()`: the hook on a
    # commitment, the curve when the run has been stepped to the end, `#s-uses`
    # when all three are decided, `#s-think` on a commitment, and the ladder
    # when every rung is answered and both self-marked rungs checked.
    #
    # ⊖ `#s-words` IS NOT A STOP. Design's own `RAIL` does not carry it, and
    # the rail ticks ACTIVITIES — a card grid the student turns over records
    # nothing, so a stop there could never tick. c5-04's `#s-series` is the
    # standing precedent for an anchored section that takes no stop.
    #
    # MRB-208: nothing is ticked on load and credit is a ratchet.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Four still minutes", "done_when": "committed"},
        {"anchor": "s-curve",  "short": "CURVE",
         "label": "The heating curve", "done_when": "run_stepped_to_end"},
        {"anchor": "s-uses",   "short": "USES",
         "label": "Three judgements", "done_when": "all_three_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Where the energy went", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `kind` is unread by the generator (it dispatches on which media key is
    # present) and is authored for consistency with C1–C6.
    #
    # ⚠️ THE HOOK CLOSES THE DOOR THE LESSON NEEDS SHUT. "The flame has not
    # changed. Energy is going in at exactly the same rate it was a minute ago"
    # is what makes the question answerable at all: without it, "the heating
    # stopped" is not a wrong answer, it is an untested one.
    "phenomenon": {
        "kind": "narrative",
        "title": "A beaker of ice on a Bunsen. The thermometer climbs to 0 °C "
                 "and then stops for four minutes.",
        "prompt": "The flame has not changed. Energy is going in at exactly "
                  "the same rate it was a minute ago. The ice is visibly "
                  "melting. And the thermometer sits at 0 °C and will not "
                  "move until the last piece of ice has gone — then it climbs "
                  "again.",
        "commit": "Where is the energy going during those four minutes?",
        "options": [
            "It is escaping into the room",
            "It is going into pulling the particles apart",
            "It stops entering while the ice melts",
            "It is destroyed by the change of state",
        ],
        "reveal": "Into pulling the particles apart. In ice the particles are "
                  "held in a fixed arrangement by forces of attraction, and "
                  "melting means breaking out of that arrangement. That takes "
                  "energy — a great deal of it — and while it is being spent, "
                  "none is left over to make the particles move faster. "
                  # XU-1 — this whole latent-heat argument rests on the
                  # definition, and the definition was wrong.
                  "<strong>" + TEMPERATURE_SENTENCE + " During a change of "
                  "state they are not speeding up; they are being "
                  "separated.</strong>",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ BOTH JOINS ON BOTH ROWS RESOLVE AGAINST THIS PAGE'S OWN MARKUP
    # (MRB-244/248), and the universe of legal names is exactly `id="…"` and
    # `data-activity="…"` on the BUILT page.
    #
    # ⊖ NOTES-C7 §5 proposes `think-reveal-latent` for `ENER-01` and
    # `curve-reveal` for `ENER-02`. NO `think-reveal-*` ID CAN BE EMITTED FROM
    # A LANE: `build_ks3.py`'s shared `r_activity` draws the confrontation
    # reveal as `<div class="ks3-reveal ks3-reveal-panel" hidden data-reveal>`
    # with NO id, and `build_ks3.py` is not a file this lane may touch. So
    # `ENER-01`'s confrontation names the ACTIVITY that owns both the
    # commitment and the reveal — the reconciliation c3-03, c4-01 and c5-02 all
    # made, and the one that satisfies Law 3's "a real activity id".
    #
    # ⊕ `ENER-02`'s two names ARE both emitted here, and neither is Design's
    # `curve-reveal`, which is not a name anything draws. `curve-run` is the
    # instrument's own `data-activity`; `curve-close` is an `id` this lesson
    # authors and `r_heating_curve` emits on the closing panel — the panel that
    # says in as many words that the thermometer stopped while the energy did
    # not. Named in the payload rather than composed in the renderer, so the
    # register's join and the markup have one source.
    "misconceptions": [
        {"id": "ENER-01",
         "statement": "While ice is melting it has stopped absorbing heat.",
         "elicited_by": "think-commit-plateau",
         "confronted_by": "think-commit-plateau"},
        {"id": "ENER-02",
         "statement": "A thermometer measures how much energy something has.",
         "elicited_by": "curve-run",
         "confronted_by": "curve-close"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Two paragraphs, so two blocks: `r_explainer` draws one <p>.
        {"type": "explainer",
         "text": "Changing state always involves energy, and the direction is "
                 "fixed. <strong>Melting, evaporating and boiling take energy "
                 "in</strong> — the particles have to be pulled apart against "
                 "the forces holding them together. <strong>Freezing and "
                 "condensing give energy out</strong> — the particles fall "
                 "back together and release it."},
        {"type": "explainer",
         "text": "Nothing new is made and nothing is destroyed. A change of "
                 "state is a <strong>physical change</strong>: the same "
                 "particles, rearranged, and reversible by putting the energy "
                 "back or taking it away again."},

        # #s-curve — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ NO NARRATION OF THE CONTROLS (§5A). The lead says what the flame
        # is doing and what to watch for; it does not say "press the button".
        # The button's own label is the instruction.
        {"type": "heating-curve", "id": "curve-run", "anchor": "s-curve",
         "eyebrow": "Your turn · heat it a minute at a time",
         "heading": "Ice at −20 °C, a steady flame, and a thermometer.",
         "demand": "investigate",
         "prompt": "The flame is steady, so every minute delivers the same "
                   "energy. Step through and watch for the minutes where the "
                   "thermometer refuses to move.",
         "curve": _CURVE,
         # Design's own trace geometry: bar height is `(t + 30) / 150`, so
         # −20 °C draws at 6.7% and 120 °C fills the box. Authored as the two
         # numbers rather than as eighteen heights, because it is a scale and
         # not a set of readings.
         "scale": {"floor": -30, "span": 150},
         "trace_label": "Temperature against time",
         "axis_label": "0 min · · · 17 min",
         "minute_format": "Minute {n}",
         "flat_suffix": " · temperature unchanged",
         "step_label": "Heat for one more minute",
         "end_label": "Run complete",
         "reset_label": "Start again",
         # ⭐ The closing panel, and `ENER-02`'s confrontation site. Rebuilt
         # under RULING 1: the minute counts are the ones this curve actually
         # draws, and the third paragraph is new prose stating that the drawing
         # is a schematic. Never present an invented number as a measurement.
         "close_id": "curve-close",
         "close_title": "Two flat steps in a graph that should be a straight "
                        "climb.",
         "close": [
             "The flame delivered energy at the same rate for all seventeen "
             "minutes. For six of them the temperature rose. For eleven of "
             "them it did not move at all — three minutes at 0 °C and eight "
             "minutes at 100 °C.",
             "Those flat steps are the changes of state, and they are where "
             "the energy went into <strong>separating particles</strong> "
             "rather than speeding them up. The boiling step is much longer "
             "than the melting step, because pulling particles completely "
             "apart takes far more energy than merely letting them slide past "
             "each other.",
             "This curve is a <strong>schematic</strong> and not a "
             "measurement. Boiling a given mass of water really does take "
             "about <strong>seven times</strong> the energy that melting the "
             "same mass takes, and the second flat step is drawn longer for "
             "that reason — but no part of this graph is to scale, and no "
             "number of minutes should be read off it.",
         ]},

        {"type": "key-fact", "ref": "energy-in-energy-out"},

        # #s-uses — three judgements. Light `ks3-block` → `check`.
        {"type": "energy-uses", "id": "uses-outside", "anchor": "s-uses",
         "eyebrow": "Three judgements",
         "heading": "Where this shows up outside a beaker",
         "demand": "classify",
         "head_counter": {"format": "{n} of {total} decided", "start": 0,
                          "total": 3},
         "prompt": "Commit to each before reading. All three are the same "
                   "idea wearing different clothes.",
         "uses": _USES},

        # ⊖ NOT A RAIL STOP. See the `rail` note above.
        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Five words",
         "lead": "Say your answer out loud before you turn each card over. If "
                 "you cannot say it, you do not know it yet.",
         "terms": ["Change of state", "Melting point", "Boiling point",
                   "Physical change", "Temperature"]},

        {"type": "misconception", "id": "think-commit-plateau",
         "anchor": "s-think", "targets": "ENER-01"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── figures (§5.4) ──────────────────────────────────────────────────────
    # None. Design draws no diagram on this page — the instrument IS the
    # picture, a readout with a bar trace beside it — and NOTES-C7 §6 declares
    # no figure anywhere in the unit. §5.4 allows an empty list where it does
    # not allow an absent one.
    "figures": [],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "energy-in-energy-out",
         "text": "Melting and boiling take energy in; freezing and condensing "
                 "give energy out. During a change of state the temperature "
                 "does not change, because the energy is separating particles "
                 "rather than speeding them up.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instrument blocks are lifted out of `core` into
    # this list by `_normalise()` and are never authored here.
    "activities": [
        {"id": "think-commit-plateau",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-01",
         "prompt": "The thermometer genuinely does not move. Commit before "
                   "you read on.",
         # ⚑ MRB-177 / MRB-278 — THE THREE DISTRACTORS ARE RE-AUTHORED AND THE
         # CORRECT OPTION IS UNTOUCHED. Design's set ran 18 words against 11,
         # 10 and 10: strictly the longest and clear of the field by seven,
         # which is exactly the construct the predict gate measures. Each
         # distractor now states a WRONG RULE at the same length in the same
         # shape — 17, 18, 17, 14 — so a student who spots the elaborate one
         # has spotted nothing, and the belief still has to be committed to
         # before it can be confronted.
         "options": [
             "Right — 0 °C is the most energy ice can hold, so it stops "
             "taking any in",
             "Wrong — it is absorbing more energy than at any other point, "
             "and using it to separate particles",
             "Right, because 0 °C is as cold as water can get, so the reading "
             "cannot move further",
             "Wrong — the thermometer is simply too slow to keep up with the "
             "beaker",
         ],
         "reveal": [
             "It is absorbing heat faster than at any other point in the "
             "experiment. Melting a beaker of ice takes several times more "
             "energy than warming the same water by a single degree — the "
             "flat step is not a pause, it is the most energy-hungry part of "
             "the whole run.",
             "The confusion comes from treating the thermometer as an energy "
             "meter. It is not. <strong>A thermometer measures how fast the "
             "particles are moving, and during melting they are not moving "
             "faster — they are being pulled out of position.</strong> Energy "
             "in, no temperature change, and nothing contradictory about it.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her rung
    # labels are the engine's own defaults character for character, so no rung
    # authors a `title`. `feedback` is keyed by the INT index of each wrong
    # option, which is what `_rung_marked` reads.
    #
    # ⚑ MRB-278 · ANSWER POSITION. Design puts the correct option FIRST on
    # every marked rung of every C7 lesson — eight rungs, all at index 0, which
    # is the 100%-at-index-0 defect the position gate was built for. C7's eight
    # are authored LEVEL from the start, two at each index:
    #
    #     c7-01 recall 0 · apply 1     c7-03 recall 1 · apply 0
    #     c7-02 recall 2 · apply 3     c7-04 recall 3 · apply 2
    #
    # Only the ORDER moves. No option text is edited to do it, no correction is
    # rewritten, and every `feedback` key below is re-keyed to the index its
    # own option now sits at.
    "ladder": {
        # Design's set at her own index 0, unchanged: four one-word options, so
        # there is no length tell to clear and nothing to balance.
        "recall": {
            "q": "Which of these changes of state gives energy out?",
            "options": [
                "Condensing",
                "Melting",
                "Boiling",
                "Evaporating",
            ],
            "answer": 0,
            "feedback": {
                1: "Melting takes energy in — the particles have to be pulled "
                   "out of a fixed arrangement.",
                2: "Boiling takes energy in, and more of it than melting does.",
                3: "Evaporating takes energy in, which is exactly why "
                   "sweating cools you.",
            }},
        # The one that catches people. Design's four options and her four
        # corrections, moved so the answer sits at index 1. 10, 12, 5 and 8
        # words: nothing is longest by four or by 1.4×.
        "apply": {
            "q": "A beaker of ice and water is heated steadily. For four "
                 "minutes the temperature stays at 0 °C. What is happening to "
                 "the energy?",
            "options": [
                "It is being lost to the room, so nothing changes",
                "It is being used to separate the particles as the ice melts",
                "It is being destroyed",
                "It stops entering while the ice is melting",
            ],
            "answer": 1,
            "feedback": {
                0: "Some heat always escapes, but the ice is visibly melting "
                   "— the energy is going into the change of state.",
                2: "Energy cannot be destroyed. It is still there, stored in "
                   "the separated particles.",
                3: "The flame has not changed. Energy enters at the same rate "
                   "throughout — the thermometer just cannot show it.",
            }},
        "explain": {
            "q": "Sketch in words the shape of a heating curve for ice heated "
                 "from −20 °C to 120 °C, and explain what is happening to the "
                 "particles in each part.",
            "field_label": "Your explanation",
            "placeholder": "The temperature rises steadily until…",
            "success": [
                "Says the temperature rises while the ice warms.",
                "Says the graph flattens at 0 °C while the ice melts.",
                "Says the energy during the flat step separates the particles "
                "rather than speeding them up.",
                "Says the temperature rises again once all the ice has "
                "melted.",
                "Says there is a second, longer flat step at 100 °C while the "
                "water boils.",
            ]},
        "produce": {
            "q": "A cool box is packed with either 1 kg of ice at 0 °C or 1 kg "
                 "of water at 0 °C. Predict which keeps the food cold for "
                 "longer and explain why, using the ideas from this lesson.",
            "field_label": "Your answer",
            "placeholder": "The ice would keep it cold for longer because…",
            "success": [
                "Says the ice keeps the food cold for longer.",
                "Says both start at the same temperature, so temperature "
                "alone cannot explain it.",
                "Says the ice must absorb energy in order to melt.",
                "Says that absorbed energy is taken from the food and the air "
                "in the box.",
                "Says the water at 0 °C simply warms up straight away, "
                "absorbing far less energy.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # Byte-identical to Design's. It is the only sentence on the page that
    # states all four claims at once: which way each change goes, why the
    # temperature holds, what the flat steps are, and where the energy went.
    "key_note": "Melting, evaporating and boiling take energy in, because the "
                "particles must be separated against the forces attracting "
                "them. Freezing and condensing give the same energy back out. "
                "While a substance is changing state its temperature stays "
                "constant, which produces the flat steps on a heating curve — "
                "the energy is going into separating particles rather than "
                "making them move faster.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # ⚑ Flags 3 and 4 both live here and both are KEPT byte-identical. Latent
    # heat is named HERE and nowhere else on the page, which is flag 3 accepted
    # as drawn; Joseph Black and Watt are flag 4, likewise.
    "stretch": [
        {"type": "explainer", "id": "latent-heat",
         "text": "The energy taken in during a change of state has a name: "
                 "latent heat, from the Latin for hidden. It is hidden in the "
                 "sense that a thermometer cannot see it. Joseph Black worked "
                 "it out in Glasgow in the 1760s by noticing exactly what you "
                 "just plotted — that ice in a warm room takes hours to melt "
                 "while staying at 0 °C the whole time — and the idea went "
                 "straight into James Watt's improvements to the steam "
                 "engine."},
        {"type": "explainer", "id": "steam-and-ice",
         "text": "It is also why steam at 100 °C burns far worse than water "
                 "at 100 °C. Both are at the same temperature, so a "
                 "thermometer cannot tell them apart, but the steam carries "
                 "all the energy that went into boiling it and dumps that "
                 "energy into your skin as it condenses. The same arithmetic "
                 "keeps a cold drink cold: the ice holds the drink at 0 °C "
                 "not by being cold but by absorbing energy while it melts, "
                 "and the moment the last cube disappears the drink starts "
                 "warming."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ The key is `definition`, NOT `gloss` — `build_ks3.py` hard-indexes
    # `v["definition"]`. And the first five `term` strings match the `keyword`
    # block's `terms` BYTE FOR BYTE: `r_keyword` matches by exact string and
    # silently drops a non-match, which renders nothing at all.
    #
    # ⊖ "latent heat" IS DELIBERATELY ABSENT. Flag 3 puts it in the stretch
    # layer only, and a vocabulary card would move it into the main flow.
    "vocabulary": [
        {"term": "Change of state",
         "definition": "A substance going from solid to liquid, liquid to "
                       "gas, or the same journeys backwards. The particles "
                       "are rearranged; no new substance is made.",
         "note": "Melting, boiling, evaporating, condensing and freezing are "
                 "all changes of state."},
        {"term": "Melting point",
         "definition": "The temperature at which a solid becomes a liquid. "
                       "For water it is 0 °C, and it is also the temperature "
                       "at which water freezes.",
         "note": "The thermometer holds at this value for as long as the "
                 "melting lasts."},
        {"term": "Boiling point",
         "definition": "The temperature at which a liquid changes to a gas "
                       "throughout, not just at its surface. For water it is "
                       "100 °C.",
         "note": "Bubbles of vapour forming inside the liquid are what makes "
                 "boiling different from evaporating."},
        {"term": "Physical change",
         "definition": "A change in which no new substance is made. The same "
                       "particles are still there, arranged differently, and "
                       "the change can be undone.",
         "note": "Every change of state is a physical change."},
        {"term": "Temperature",
         "definition": "A measure of how fast the particles in a substance "
                       "are moving. It is not a measure of how much energy "
                       "something contains.",
         "note": "Steam and water at 100 °C are at the same temperature and "
                 "carry very different amounts of energy."},
        {"term": "Evaporating",
         "definition": "Particles escaping from the surface of a liquid and "
                       "becoming a gas. It takes energy in, and it happens at "
                       "any temperature."},
        {"term": "Condensing",
         "definition": "A gas turning back into a liquid as its particles "
                       "fall together. It gives energy out — the same energy "
                       "that boiling took in."},
    ],

    # ── safety (§1.5) — not a callout, and not a safeguarding block ─────────
    # ⚑ NEW PROSE, and the only new prose in this file outside the curve.
    # Reported to the commander (contract §16) rather than added silently.
    #
    # ⊖ NO SAFEGUARDING BLOCK, and that is the right call: nothing on this page
    # touches a student's own body, health or circumstances in the safeguarding
    # sense. C3, C4 and C5 carried none for the same reason.
    #
    # ⊕ A `safety_note` IS earned. Use 2 tells a student, correctly, that steam
    # at 100 °C does far more damage than water at 100 °C, and the whole page
    # is about boiling a beaker dry. Scoped so it adds to the method rather
    # than withdrawing it: it does not say "never boil anything", because the
    # page is about boiling something.
    "safety_note": "Steam burns worse than boiling water, which is the point "
                   "of use 2 and the reason a boiling beaker is watched from "
                   "the side and never from above. Keep hands and face out of "
                   "the plume, and let glassware cool before moving it.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why the thermometer stops?",
              "cta": "Ask about this lesson",
              "anchor": "s-curve"},

    "ks4_becomes": "Specific heat capacity and specific latent heat with real "
                   "calculations, and energy level diagrams for changes of "
                   "state.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["analysis-and-evaluation", "scientific-attitudes"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
