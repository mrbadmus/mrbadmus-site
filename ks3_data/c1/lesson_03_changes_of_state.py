"""C1 L3 — Changes of state (PROCESS).

Authored against Design's approved page,
`docs/ks3/design-reference/c1/c1-03-changes-of-state.dc.html` (842 lines), and
its measured specification, `docs/ks3/c1-inventory/PAYLOAD-MAP.md` §3.

Every student-facing string is byte-identical to the approved page. The five
`PHASE` notes — the science core of this lesson — live INSIDE `renderVals`
(page lines 633–644) and not at module scope, so they are lifted from the page
by hand rather than from `tools/extract_design_payload.js`.

── The mass never moves, and it is not state ───────────────────────────

`Mass in the flask · 50.0 g` is hard-coded in Design's markup (line 154) and
must stay hard-coded. It is the entire confrontation of the lesson: the
temperature changes, the picture in the flask changes, and the one number that
could tell you something was lost does not move. `heating-bench` takes it as a
`mass` string, emits it once into the document, and no JS on the page ever
touches it — the renderer raises if it is missing, because a bench without it
is a different lesson.

── Three instruments, two of them authored here ────────────────────────

`heating-bench` (`#s-curve`) and `sort-cards` (`#s-think`) are written for this
lesson. `keyed-commit` (`#s-bubble`) is shared with c1-06 and takes the c1-06
shape — the reply attached per option — so Design's three-branch
`bubbleVerdict` (page lines 750–754) is expressed as four per-option replies.
Two of them (A and B) carry the same fallback sentence, because Design's `else`
branch answers both.

── What was corrected, and why ─────────────────────────────────────────

⚖️ **The plateau ratio.** See the comment on `KEYS` below. Design's drawing
contradicts Design's own prose about a measurable fact, and the fact wins.

⚑ `state.thinkSeen` (page line 429) is initialised and never read or written.
Dead state; it is not carried here.

⚑ For Mide's science gate — three things the page says that only a reader
holding all of it at once will notice:

  1. NOTES §3 flag 4 names **the wrong rung**. It says "Rung 4's answer depends
     on students having seen it"; rung 4 is the wet-towel evaporation question
     and never touches the plateau. **Rung 2** is the plateau rung.
  2. **Eight minutes or six? — CORRECTED, now six in both.** Design's big
     question said the climb stops "for eight full minutes" and Rung 2 says
     "For six minutes the thermometer stays at 0 °C". Two set-ups and two
     numbers for one phenomenon, which a student reads as one. The big question
     now says six, and names the beaker so the vessel matches too; the
     reasoning is on `big_question` below. Nothing about the drawn curve
     changed — its axis is energy, not time.
  3. The Going further layer says condensing steam gives back "roughly five
     times the energy released by the same water cooling from 100 °C to room
     temperature". 2260 kJ/kg against 4.18 × 80 = 334 kJ/kg is 6.8 — the same
     number as the plateau ratio, and the page rounds it to five here and to
     seven there. Both are defensible as "roughly"; they are not the same
     rounding.
"""

# XU-1 (MRB-295/MRB-298, ruled 28 Aug 2026). The estate held four
# definitions of temperature and three were wrong. There is now one, and it
# is authored in ks3_data/quantities.py rather than retyped here.
from ..quantities import (TEMPERATURE_CRITERION, TEMPERATURE_OPTION,
                          TEMPERATURE_SENTENCE, TEMPERATURE_VOCAB)  # noqa: F401


# ── the heating curve, x = energy in (0–100), T = °C ─────────────────────
#
# ⚖️ **CORRECTED FROM DESIGN, AND THE CORRECTION IS THE POINT.**
#
# Design's own keys are
#     [[0, -20], [12, 0], [26, 0], [60, 100], [92, 100], [100, 120]]
# which draws a melting plateau 14 units wide and a boiling plateau 32 units
# wide — a ratio of **2.29 : 1**. The page's own `PHASE.boiling` note says the
# boiling plateau is "far longer than the melting one … about seven times as
# much energy", and the prose is right: the specific latent heat of
# vaporisation of water is 2260 kJ/kg against a latent heat of fusion of
# 334 kJ/kg, which is **6.77 : 1**. NOTES §3 flag 4 asserts the drawn ratio
# "is real (about 7:1 for water)"; it is not, and the canvas under-draws it by
# a factor of three. An approved page cannot outrank a measured quantity, so
# the drawing is corrected to the prose and never the other way round.
#
# The boiling plateau is extended and the whole axis rescaled to end at 100:
#
#     phase     Design      here      what it draws
#     ice       0 – 12      0 –  6    -20 °C → 0 °C
#     MELTING  12 – 26      6 – 15    9 units
#     water    26 – 60     15 – 34    0 °C → 100 °C
#     BOILING  60 – 92     34 – 95    61 units
#     steam    92 – 100    95 – 100   100 °C → 120 °C
#
# **61 : 9 = 6.78 : 1** against the true 6.77 : 1.
#
# Nothing else about the drawing changes its meaning. The three ramps keep
# Design's own ordering both in width (water > ice > steam) and in slope
# (water > steam > ice), so every other sentence on the page that describes
# the picture — "this stretch is much longer than the ice stretch" — is as
# true of this curve as it was of Design's. The ramps stay schematic rather
# than energy-exact on purpose: an honest axis gives the ice and steam ramps
# about 1.3 units each, and two of the five phase bands become unreachable.
#
# The five phase bands, the two shaded plateaus, the flask's melt and boil
# fractions and the jump targets are all DERIVED from these six points by
# `r_heating_bench`, so this table is the only place the correction had to be
# made and nothing can drift out of step with it.
KEYS = [[0, -20], [6, 0], [15, 0], [34, 100], [95, 100], [100, 120]]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 160 character for character.
    "slug":        "changes-of-state",
    "title":       "Changes of state",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # Carried unchanged from the superseded body in
    # `ks3_data/chemistry_c1_particles.py`. The rebuild moves no statement:
    # PAYLOAD-MAP §7.4 confirms coverage and misconception ownership are
    # untouched by it.
    "covers":      ["KS3.C.PNM.02", "KS3.P.PHYC.01"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 2},
                    {"id": "energy", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 45,

    # ── progression edges ───────────────────────────────────────────────────
    "requires":    ["solids-liquids-and-gases"],
    "assumes":     [],
    # Design's endmatter draws a FORWARD link (page line 324), so `references`
    # points at the next lesson and the card takes its heading.
    "references":  ["gas-pressure"],
    "connects_heading": "Next in this unit",
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    # ── framing ─────────────────────────────────────────────────────────────
    # ⚖️ **CORRECTED FROM DESIGN — one set-up, one number (MRB-228).**
    #
    # Design's big question read "Put ice on a hot ring … for eight full
    # minutes", and rung 2 reads "For six minutes the thermometer stays at
    # 0 °C … during those six minutes". Same phenomenon, same lesson, two
    # numbers, and a student meeting the second after the first has no way to
    # read them as anything but a contradiction.
    #
    # SIX wins, and not by coin toss. Rung 2 states the figure twice inside one
    # question and its distractor feedback is written around that vessel ("the
    # flask is insulated", "use a different beaker") — the number is load-
    # bearing there and the marked item is where a wrong number costs most.
    # The big question states it once, as framing. So the framing moves.
    #
    # The vessel is named here for the same reason: "ice on a hot ring" and "a
    # beaker of ice and water" were also two set-ups, and one lesson gets one.
    #
    # ⚠️ The drawn curve does NOT arbitrate this. Its x-axis is `ENERGY IN →`
    # (see `KEYS` and the bench's `x_label`), not time, so the 9-unit melting
    # plateau is nine units of energy and says nothing about minutes. The
    # plateau RATIO correction above and this one are independent.
    "big_question": "Put a beaker of ice on a hot ring and the temperature "
                    "climbs. Then, for six full minutes, it stops climbing — "
                    "while the flame is still on. Where is that energy going?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, from the page's own RAIL constant (lines 347–353). This is
    # the strongest rail in the unit: every predicate names state the section
    # itself owns, so nothing here ticks on another block's behalf.
    #
    # `done_when` is a GATE field (R2) — the runtime ticks from
    # `data-stage-done`, which each instrument sets from its own predicate.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Sealed bag",
         "done_when": "committed"},
        # ⚖️ BOTH plateaus, not either. A student who scrubs to the middle and
        # stops has seen the argument once; the lesson is that it happens
        # twice, for two different amounts of energy.
        {"anchor": "s-curve",  "short": "CURVE",  "label": "Heating bench",
         "done_when": "both_plateaus_visited"},
        {"anchor": "s-bubble", "short": "BUBBLE", "label": "In the bubble",
         "done_when": "committed"},
        {"anchor": "s-think",  "short": "THINK",  "label": "Melt or dissolve",
         "done_when": "all_cards_sorted"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "demo",
        "title": "Seal it in the bag first.",
        "prompt": "An ice cube, 50 g, sealed inside a bag that nothing can get "
                  "in or out of. Weigh it. Leave it on the bench until it is a "
                  "puddle of water, then weigh the bag again.",
        "commit": "What does the balance read the second time?",
        "options": [
            "Less than 50 g — some of the ice is gone",
            "Exactly 50 g",
            "More than 50 g — water is denser than ice",
            "It depends how long you leave it",
        ],
        "reveal": "50 g. Exactly 50 g, and it will read 50 g again when the "
                  "water evaporates inside the sealed bag, and again if you "
                  "freeze it back. A change of state moves particles around "
                  "and never removes a single one. Keep the mass readout in "
                  "the corner of your eye for the rest of this lesson — it "
                  "will not move once.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Same three PART-* ids as the superseded body, repointed at the blocks
    # that now elicit and confront them (PAYLOAD-MAP §7.4: the register does
    # not move).
    "misconceptions": [
        # The hook elicits this one and the bench is where it is confronted —
        # the mass tile that reads 50.0 g through every state.
        {"id": "PART-05",
         "statement": "When a substance melts or evaporates, some of it is "
                      "lost or destroyed.",
         "elicited_by": "the-heating-bench",
         "confronted_by": "the-heating-bench"},
        {"id": "PART-06",
         "statement": "Melting and dissolving are the same thing.",
         "elicited_by": "melt-or-dissolve",
         "confronted_by": "melt-or-dissolve"},
        {"id": "PART-07",
         "statement": "Bubbles in boiling water are made of air, or of "
                      "nothing.",
         "elicited_by": "the-bubble",
         "confronted_by": "the-bubble"},
    ],

    # Carried from the superseded body. Design's C1 draws no keyword block on
    # any of the six pages (PAYLOAD-MAP §0.7), so no `keyword` block names this
    # and none of it reaches the page — it stays because it is the lesson's
    # term list for the reading-age gate and for the day a support layer is
    # authored.
    "vocabulary": [
        {"term": "melting",
         "definition": "Changing from a solid to a liquid.",
         "note": None},
        {"term": "freezing",
         "definition": "Changing from a liquid to a solid.",
         "note": "Freezing and melting happen at the same temperature for a "
                 "given substance — they are the same doorway, used in "
                 "opposite directions."},
        {"term": "evaporating",
         "definition": "Changing from a liquid to a gas.",
         "note": None},
        {"term": "condensing",
         "definition": "Changing from a gas to a liquid.",
         "note": None},
        {"term": "sublimation",
         "definition": "Changing straight from a solid to a gas, with no "
                       "liquid in between.",
         "note": "Solid carbon dioxide does this — which is why it is called "
                 "dry ice."},
        {"term": "conserved",
         "definition": "Stays the same in total. Nothing is gained or lost.",
         "note": None},
    ],

    # Design's page has no figure slot anywhere in C1 (§0.7), so the two
    # figures the superseded lesson commissioned — `c1-state-change-map` and
    # `c1-sealed-bag` — drop out of the diagram manifest with it. Present and
    # empty, never absent.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Melting, freezing, boiling, condensing, evaporating. Five "
                 "words for the same short list of events: particles gaining "
                 "enough energy to break away from their neighbours, or losing "
                 "enough to be captured again. Nothing else happens. Nothing "
                 "is made and nothing is lost."},

        # ── #s-curve · the heating bench ────────────────────────────────────
        # A LIGHT `ks3-block` (page line 111) — the flagship of a PROCESS
        # lesson, drawn on the shell's own card. Painting it on ink would
        # resolve every text token wrong and turn the graph's cream fill into
        # a hole.
        {"type": "heating-bench", "id": "the-heating-bench", "anchor": "s-curve",
         "demand": "investigate",
         "targets": "PART-05",
         "eyebrow": "The heating bench · scrub through it",
         "heading": "Heat it steadily and watch the temperature refuse to "
                    "rise.",
         "head_counter": {"format": "{n} of {total} plateaus visited",
                          "total": 2},
         "prompt": "50 g of ice at −20 °C in a sealed flask, on a "
                   "ring that delivers the same energy every second from start "
                   "to finish. Drag through the run.",

         # C6's gate: commit to the shape of the curve, then the bench arrives
         # in the space the question was occupying.
         "gate": {
             "prompt": "Commit first. The energy goes in at a steady rate. "
                       "What will the temperature do?",
             "options": [
                 "Rise steadily the whole way, in a straight line",
                 "Rise, then stop twice while the state changes, then rise "
                 "again",
                 "Rise faster and faster as it gets hotter",
                 "Rise to 100 °C and stay there forever",
             ]},

         "keys": KEYS,

         # Five bands, one per segment of `keys`, in the same order. A segment
         # whose two ends are at the same temperature is a plateau, and a
         # plateau carries the two captions the canvas draws: `band` over the
         # shaded stripe on the graph, `banner` across the flask.
         "phases": [
             {"id": "ice", "label": "Ice", "tone": "ink",
              "note": "Solid ice, warming. The energy is going straight into "
                      "making the particles vibrate harder, and the "
                      "thermometer reports it faithfully."},
             {"id": "melting", "label": "Melting", "tone": "accent",
              "band": "MELTING", "banner": "ORDER BREAKING DOWN",
              "note": "The thermometer has stopped at 0 °C and it will not "
                      "move until the last of the ice has gone — but the "
                      "heater has not stopped. Every joule going in now is "
                      "being spent breaking particles out of the rigid "
                      "arrangement. Watch the flask: order is being "
                      "destroyed, and the mass has not shifted by a "
                      "milligram."},
             {"id": "water", "label": "Water", "tone": "ink",
              "note": "All liquid now, and the temperature climbs again. "
                      "Notice this stretch is much longer than the ice "
                      "stretch — water takes more energy per degree than "
                      "almost anything else, which is why the sea moderates "
                      "the climate."},
             {"id": "boiling", "label": "Boiling", "tone": "accent",
              "band": "BOILING", "banner": "BREAKING AWAY COMPLETELY",
              "note": "The second plateau, at 100 °C, and it is far longer "
                      "than the melting one. Melting only loosens the "
                      "particles; boiling has to separate them completely, "
                      "and that costs about seven times as much energy."},
             {"id": "steam", "label": "Steam", "tone": "ink",
              "note": "Steam, above 100 °C, warming quickly — there is almost "
                      "nothing to slow it down now. Same 50 g of water that "
                      "started as ice. Not one particle has been created or "
                      "destroyed in the whole run."},
         ],

         # ⚠️ THE CONSTANT. Emitted once, into the markup, and read by nothing
         # at runtime. See the module docstring.
         "mass": "50.0 g",

         "labels": {"scrub": "Energy put in · drag to move through the run",
                    "temperature": "Temperature",
                    "phase": "What is in the flask",
                    "mass": "Mass in the flask",
                    "unit": "°C"},

         # Design's jump targets sat at the middle of each plateau (19 and 76
         # on the old axis). They move with the axis: 10 is the middle of
         # 6–15 and 64 the middle of 34–95, and both stay inside their band
         # across the whole ±3 window that draws the button as pressed.
         "jumps": [{"label": "Jump to melting", "value": 10},
                   {"label": "Jump to boiling", "value": 64},
                   {"label": "Back to the start", "value": 0}],

         # The graph frame. `grid` is drawn, `ticks` is drawn AND labelled —
         # 50 °C gets a line and no number, exactly as Design draws it.
         "graph": {"t_min": -30, "t_max": 130,
                   "grid": [-20, 0, 50, 100, 120],
                   "ticks": [-20, 0, 100, 120],
                   "y_label": "TEMPERATURE / °C",
                   # ⊕ FONT LAW. `x_label` is a PAYLOAD string: it reaches the
                   # page inside the graph config and is drawn by
                   # `ctx.fillText` on a canvas (shared/ks3.js), where markup
                   # does not exist and a `<sub>`-style tag would be drawn as
                   # its own characters. The shipped latin subsets carry no
                   # U+2192, so the arrow was dropping to a system font in the
                   # middle of the label. Design's convention for a payload
                   # arrow is a WORD — her own c1-06 fix replaced "1913 → now"
                   # with "1913 onwards" — and this is the same move: the axis
                   # says which way it runs in words.
                   "x_label": "ENERGY IN, INCREASING"},

         # The sealed flask, right of the graph. The caption carries the mass
         # again because the drawing has to say it too — a student watching
         # the particles fly apart is not looking at the readout.
         "flask": {"caption": "SEALED FLASK — 50.0 g THROUGHOUT"},

         # Composed identically in Python and in JS, so the resting page and
         # every later frame say the same thing the same way.
         "alt": {"template": "A heating curve for 50 g of water with the "
                             "marker at {t} degrees Celsius, and a flask "
                             "showing the particles as {phase}."},
         "valuetext": "{t} degrees, {phase}"},

        {"type": "key-fact", "ref": "temperature-holds"},

        # ── #s-bubble · the commit with a reply per answer ──────────────────
        # Ink-dark `practical` (page line 173). `keyed-commit` is shared with
        # c1-06 and takes ITS shape — the reply on the option — so Design's
        # three code branches become four authored replies.
        {"type": "keyed-commit", "id": "the-bubble", "anchor": "s-bubble",
         "demand": "predict",
         "targets": "PART-07",
         "eyebrow": "The bubble · a small question with a large answer",
         "heading": "What is inside a bubble in boiling water?",
         "prompt": "A pan of water at a rolling boil. Bubbles form at the "
                   "bottom, rise, and burst at the surface. Commit to what is "
                   "in one.",
         "options": [
             # A and B share Design's `else` branch (page line 754). Written
             # out twice rather than left to a fallback: the shape this kind
             # takes is "every option carries its own reply", and a default
             # would be a second mechanism for one page's convenience.
             {"text": "Air that was dissolved in the water",
              "reply": "Not this one. Follow the consequence of your answer "
                       "through."},
             {"text": "Nothing — it is an empty space",
              "reply": "Not this one. Follow the consequence of your answer "
                       "through."},
             {"text": "Water that has turned into a gas",
              "reply": "Correct — and it is worth knowing why the other three "
                       "fail."},
             {"text": "Hydrogen and oxygen, split apart by the heat",
              "reply": "No. Splitting water into hydrogen and oxygen is a "
                       "chemical change and takes far more energy than a "
                       "kettle has; boiling is a change of state and the "
                       "water is still water."},
         ],
         # ⚑ The map's shape for this kind (§3.5.2, §6.5.2) — and nothing on
         # this page marks the bubble commit, because the reply carries the
         # verdict. It needs a read site in `r_keyed_commit` or it should come
         # out of both lessons; reported rather than dropped unilaterally,
         # because c1-06 authors it too.
         "answer_index": 2,
         # The two paragraphs Design draws as STATIC markup under the computed
         # reply (page lines 192–193), including "Steam is invisible".
         "reveal": [
             "Steam. Water that has boiled into a gas, right there at the "
             "bottom of the pan where it is hottest. If a bubble were air, "
             "the pan would run out of air after a minute and stop bubbling — "
             "and boiling water does not stop bubbling. If a bubble were "
             "empty, the water pressure would crush it instantly.",
             "And the steam you can <em>see</em> above the pan is not steam. "
             "Steam is invisible. What you see is the steam having already "
             "condensed back into tiny drops of liquid water in the cold air "
             "— a change of state happening in front of you, twice, in the "
             "space of a few centimetres.",
         ]},

        # ── #s-think · melt or dissolve ─────────────────────────────────────
        # The sorter is the misconception's mechanism, not a bench of its own,
        # so it renders inside the amber `misconception` shell. `statements`
        # carries Design's own quote, which is shorter and better than the
        # register's line for PART-06 and is the one that renders (an authored
        # statement wins over the register).
        {"type": "sort-cards", "id": "melt-or-dissolve", "anchor": "s-think",
         "demand": "classify",
         "targets": "PART-06",
         "statements": ["Sugar melts in tea."],
         "prompt": "Everyone says it and it is the wrong word. Sort each of "
                   "these into the right column before you read on — the "
                   "sorting is the point, not the score.",
         "buttons": [{"label": "Melting", "value": "melt"},
                     {"label": "Dissolving", "value": "dissolve"}],
         "items": [
             {"id": "s1", "text": "A sugar cube stirred into hot tea",
              "answer": "dissolve",
              "right": "Dissolving. Two substances, and the sugar particles "
                       "spread out among the water particles.",
              "wrong": "Not melting — tea is nowhere near sugar’s melting "
                       "point of about 186 °C. Two substances are involved, "
                       "so this is dissolving."},
             {"id": "s2", "text": "Butter left in a pan over a low flame",
              "answer": "melt",
              "right": "Melting. One substance, heated until its particles "
                       "break out of their fixed positions.",
              "wrong": "Nothing is being spread through a liquid here. One "
                       "substance, heated — that is melting."},
             {"id": "s3", "text": "Salt stirred into cold water",
              "answer": "dissolve",
              "right": "Dissolving. Cold water, so no heating is involved at "
                       "all — and it still happens.",
              "wrong": "The water is cold, so nothing has been heated past a "
                       "melting point. Salt melts at 801 °C."},
             {"id": "s4", "text": "A chocolate bar left on a sunny windowsill",
              "answer": "melt",
              "right": "Melting. One substance, warmed above its melting "
                       "point, and it sets again when it cools.",
              "wrong": "There is no second substance for it to spread into. "
                       "Warmed above its melting point, it melts — and "
                       "re-solidifies on cooling."},
         ],
         # Gated on all four, and the payoff for sorting rather than reading.
         "summary": [
             "Melting needs one substance and heat: the particles of that "
             "substance break out of their fixed positions, and if you cool "
             "it the solid comes straight back. Dissolving needs two "
             "substances and no heat at all: the particles of the solid "
             "separate and slot in among the particles of the liquid, and to "
             "get the solid back you have to remove the liquid.",
             "Sugar in tea is dissolving. Sugar in a dry pan over a flame "
             "really does melt, at about 186 °C. It is an awkward example, "
             "because sugar starts browning and breaking down at around its "
             "melting point — and that browning is a chemical change, not a "
             "melt. Same substance, two entirely different events, and the "
             "word you choose says which one you mean.",
         ]},

        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # A top-level orphan div between the bench and the bubble, on `card`
    # ground (R3: the shipped stylesheet's geometry wins over the page's).
    "key_facts": [
        {"id": "temperature-holds",
         "text": "During a change of state the temperature does not change: "
                 "the energy goes into breaking the particles apart from each "
                 "other, not into speeding them up. Mass stays the same "
                 "throughout.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # Every activity on this page is an instrument, lifted into `activities[]`
    # by `ks3_data/c1/__init__.py`. Present and empty, never absent.
    "activities": [],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Two page-marked, two self-marked, from RUNGS (373–390) and SELF_RUNGS
    # (392–415). The engine prints "Rung N · " and the authored title supplies
    # the label after it.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Recall",
            "q": "What is the name of the change from a gas to a liquid?",
            "options": [
                "Evaporating",
                "Freezing",
                "Condensing",
                "Sublimating",
            ],
            "answer": 2,
            "feedback": {
                0: "That is the other direction — liquid to gas.",
                1: "Freezing is liquid to solid.",
                3: "Sublimation is solid straight to gas, skipping the liquid "
                   "— what dry ice does.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A beaker of ice and water is heated steadily. For six "
                 "minutes the thermometer stays at 0 °C. What is the energy "
                 "doing during those six minutes?",
            "options": [
                "Breaking the particles free from their fixed positions",
                "Nothing — it is being lost to the room",
                "Warming the beaker instead of the water",
                "Making the water particles bigger",
            ],
            "answer": 0,
            "feedback": {
                1: "Heat is being lost to the room the whole time, before and "
                   "after the plateau too — yet the climb only stops while "
                   "ice remains. The ice is what is absorbing it.",
                2: "Use a different beaker and the plateau still lasts the "
                   "same time. It is the ice that is absorbing it.",
                3: "Particles never change size. This is the misconception "
                   "from the last lesson wearing a new hat.",
            }},
        "explain": {
            "title": "Rung 3 · Explain",
            "q": "Explain why the temperature stops rising while ice is "
                 "melting, even though the heater is still supplying energy "
                 "at the same rate.",
            "field_label": "Your explanation",
            "placeholder": "Temperature is a measure of…",
            "success": [
                # XU-1 — this criterion used to read "Says temperature is a
                # measure of how fast the particles are moving", which is
                # wrong, and it is the FIRST time in the course a child is
                # marked on the definition (Y7 HT1). One definition, authored
                # once, in ks3_data/quantities.py.
                TEMPERATURE_CRITERION,
                "Says the energy going in during melting is used to break the "
                "particles apart from each other.",
                "Says that energy is not going into making the particles move "
                "faster.",
                "Says the temperature therefore stays constant until all the "
                "ice has melted.",
                "Says the energy is not lost — it is stored, and released "
                "again when the water freezes.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A wet towel dries on a washing line on a cold day, at 8 °C. "
                 "Water boils at 100 °C. Explain how the water can become a "
                 "gas at a temperature far below its boiling point.",
            "field_label": "Your answer",
            "placeholder": "Not all the particles in the water…",
            "success": [
                "Says the particles in the water do not all move at the same "
                "speed.",
                "Says the fastest particles at the surface can escape even "
                "when the average is low.",
                "Says this is evaporation, and it happens from the surface "
                "only.",
                "Says boiling is different: it happens throughout the liquid, "
                "at one fixed temperature.",
                "Says the water left behind is cooler, because the fastest "
                "particles are the ones that left.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Changes of state are reversible, cost or release energy, and "
                "never change the mass. Temperature holds still at the "
                "melting and boiling points because the energy is buying "
                "separation, not speed.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    "stretch": [
        {"type": "explainer", "id": "steam-burns",
         "text": "The plateau has a practical consequence you have felt. "
                 "Water at 100 °C will scald you; steam at 100 °C — the "
                 "same temperature — will do far worse, because every gram "
                 "of it has to give back the whole boiling plateau's worth "
                 "of energy as it condenses on your skin, and that is about "
                 "seven times the energy released by the same water cooling "
                 "from 100 °C to room temperature. Nothing about the "
                 "temperature reading warns you. This is also how a "
                 "sweating body cools itself, how a fridge works, and why a "
                 "puddle can evaporate on a cold day without ever reaching "
                 "100 °C."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure where the energy goes during the "
                      "plateau?",
              "cta": "Ask about this lesson",
              "anchor": "s-curve"},

    # ⚑ Design's third endmatter card carries this prose (page line 329), and
    # `ks4_becomes` renders only when `ks4_links` is EMPTY. The superseded
    # body's KS4 link is carried, so the card will show the link and this
    # sentence will not render. Both are authored here so the choice is a
    # ruling and not an omission — reported.
    "ks4_becomes": "Specific heat capacity and specific latent heat — the "
                   "plateau, turned into a number you can calculate with.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["measurement", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
