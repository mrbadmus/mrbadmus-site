# -*- coding: utf-8 -*-
"""C3 L5 — Distillation (PROCESS).

Authored against Design's approved page,
`docs/ks3/design-reference/c3/c3-05-distillation.dc.html` (706 lines), and
Design's unit notes, `docs/ks3/design-reference/c3/NOTES-C3.md` §2, §3.4, §4,
§5 and §6.

Every student-facing string is byte-identical to the approved page. `RAIL`,
`MIXTURES`, `CARDS`, `RUNGS` and `SELF_RUNGS` came out of the node extractor;
the hook and confrontation options, the two dial labels, the three gauge
labels, the three control labels, the warm-condenser stage text and the
warm-condenser result panel were lifted from `lessonVals(s)`, which is where
most of this lesson's words live and which a lift of the top-level constants
alone silently loses.

── The two halves are the lesson ───────────────────────────────────────

NOTES §2: a staged run with a thermometer, and the condenser cooling as a
SWITCH THAT CAN BE TURNED OFF. Boil to separate, cool to collect — and doing
only one of the two gets you nothing. The cooling dial is not a setting, it is
the second half of the definition, and a student who turns it off must watch a
perfectly good separation walk out of the open end of the apparatus.

So the state space is enumerated and every reachable state is authored, not
just the successful one:

    dial: mixture ∈ {salt, ink, ethanol}   dial: cooling ∈ {running, off}
    stage 0 (nothing lit) … stage 4 (run finished)      × the predict gate

  * ON LOAD — sea water, cooling running, nothing lit, nothing predicted. The
    gate asks first (`mixtures[].predict`); the bench opens behind it.
  * THE ZERO STATE — predicted, stage 0, Bunsen not lit. Every gauge has a
    resting reading of its own (`gauges[].before` / `before_from`): 20 °C, an
    empty beaker, and the mixture still whole in the flask. No gauge reads a
    blank.
  * HEATING WITH THE COOLING OFF — stages 1 and 2 are unchanged and TRUE:
    boiling really does separate the mixture whether or not anything is there
    to catch it, and `gauges[].reads` still moves the flask reading to
    `left`. Stage 3 takes `warm_condenser.stage_text`, stage 4 takes the
    mixture's own `warm_final`, and the run ends on
    `warm_condenser.result_*`: an empty beaker and a room that smells of it.
  * COOLING WITH NO HEAT — unreachable as a state of its own, and deliberately
    so: cold water through a cold flask is not an event, and the instrument
    has nothing to stage. It is answered in words instead, by the key fact and
    by rung 4, both of which say the cold surface only earns its place once
    something is boiling.

⚠️ A RUN WITH THE COOLING OFF DOES NOT TICK THE RAIL — `completion`. That is
not a punishment and it is not a bug: the rail stop is "run the still", and a
still that collects nothing has not been run. The student is told exactly why,
in the result panel, and one dial gets them there.

── ⊕ AUTHORED, NOT LIFTED: `mixtures[].warm_final` ──────────────────────

Design's page overrides stage 3 when the cooling is off and leaves stage 4
alone, so the last line of a warm-condenser run reads "Clear drops run into
the beaker" over a result panel that says the beaker is empty. That is a
reachable state whose text is false, and the brief's rule is that the prose
changes rather than the instrument. `warm_final` is three new sentences, one
per mixture, written to the same bar; Design's stage-3 override is untouched
and byte-identical. Reported to the commander.

⚑ For Mide's science gate, from Design's NOTES §4 — all three KEPT:
  * flag 7 — reverse osmosis at three to four kilowatt-hours per cubic metre
    (stretch, second paragraph). Modern seawater RO plants run at about this.
  * flag 10 — salt water boiling at "just over 100 °C" and creeping UP as the
    flask concentrates (`salt.temp`, and stage 1). Boiling-point elevation,
    correct, and rarely said at KS3.
  * flag 11 — the ethanol/water still gives "MOSTLY ethanol", and a
    fractionating column is what does better. Correct: one simple still cannot
    reach pure ethanol, and an ethanol/water azeotrope caps it near 95%
    however hard anyone tries. The honesty is kept in `ethanol.collected`, in
    its result text and in the stretch layer; nothing in the lesson retracts
    it later.
  * flag 12 — "steam off boiling sea water tastes salty". The confrontation
    separates VAPOUR from CARRIED DROPLETS and blames the method, not the
    physics. It is right on both halves: pure water vapour carries no salt,
    and a vigorously boiling liquid throws droplets that do. Design calls it
    the sharpest thing in the unit; it is kept whole, and rung 2, `warm_final`
    and question h02 are all consistent with it.
"""

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 202 character for character.
    "slug":        "distillation",
    "title":       "Distillation",
    "discipline":  "chemistry",
    "unit":        "mixtures-and-separation",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚠️ PIS.04 names four techniques and NOTES §1 gives it four lessons, one
    # each. The parent bullet is therefore split at the grain the lessons are
    # written at (`ks3_data/substatements.py`, minted for C3): `04a`
    # filtration, `04b` evaporation and crystallisation, `04c` distillation,
    # `04d` chromatography. This lesson owns `04c` — recovering the solvent,
    # or separating liquids by boiling point.
    #
    # That is bookkeeping and NOT a claim about what may be repeated. Boiling
    # points, "the salt cannot become a gas" and the two-halves rule are
    # taught here and in the three techniques either side of this one, on
    # purpose. `covers` records which lesson is answerable for a clause.
    "covers":      ["KS3.C.PIS.04c"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 2},
                    {"id": "energy", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The hook leans on filtration ("filtering it does nothing at all — you
    # proved that") as well as on the lesson immediately before it.
    "requires":    ["evaporation-and-crystallisation"],
    "assumes":     [],
    "references":  ["filtration"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Evaporation throws the water away. What if the water is "
                    "the thing you cannot live without?",

    # ── the progress rail (§4.8.1 A) — five stops, per NOTES §6 ─────────────
    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",
         "label": "The life raft", "done_when": "committed"},
        {"anchor": "s-still", "short": "STILL",
         "label": "Run the still", "done_when": "one_run_collected"},
        {"anchor": "s-words", "short": "WORDS",
         "label": "Four words", "done_when": "all_cards_flipped"},
        {"anchor": "s-think", "short": "THINK",
         "label": "Salty steam", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    "phenomenon": {
        "kind": "narrative",
        "eyebrow": "Start here",
        "title": "You are on a life raft, surrounded by water, and dying of "
                 "thirst.",
        "prompt": "You have a pan, a fire, a sheet of clear plastic and a cup. "
                  "The sea is right there. Drinking it makes things worse, and "
                  "filtering it does nothing at all — you proved that two "
                  "lessons ago.",
        "commit": "What do you do with the pan, the plastic and the cup?",
        "options": [
            "Filter the sea water through the plastic sheet",
            "Boil it and let it all go into the air",
            "Boil it and catch what comes off on the cold plastic",
            "Leave it in the sun until the salt sinks",
        ],
        "reveal": "Boil the sea water in the pan and hold the plastic above "
                  "it, tilted, with the cup under the low corner. The water "
                  "leaves the sea water as a gas; the salt cannot. Cool the "
                  "gas on the plastic and it turns back into liquid water — "
                  "fresh water — and runs down into the cup. Every "
                  "desalination plant on Earth is a large, expensive version "
                  "of that.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # MIX-10, from NOTES §5. The `statement` is the approved page's own
    # `.ks3-mis-quote`, verbatim and without its quote marks (the renderer adds
    # them) — the register's own phrasing of the same idea is "Boiling carries
    # dissolved salt over with the steam", and the page's line is the one a
    # student reads. `elicited_by` / `confronted_by` keep NOTES' two names for
    # the commitment and the reveal inside the one `#s-think` activity.
    "misconceptions": [
        {"id": "MIX-10",
         "statement": "Steam off boiling sea water tastes salty, so some salt "
                      "must come over with it.",
         "elicited_by": "think-commit-spray",
         "confronted_by": "think-commit-spray"},
    ],

    # ── vocabulary (Law 7) — Design's four cards ────────────────────────────
    "vocabulary": [
        {"term": "Distillation",
         "definition": "Separating a liquid from a mixture by boiling it off "
                       "and condensing it.",
         "note": "Keeps the liquid. Evaporation keeps the solid."},
        {"term": "Condense",
         "definition": "Turn a gas back into a liquid by cooling it.",
         "note": "The opposite of evaporating, and it makes nothing new."},
        {"term": "Distillate",
         "definition": "The liquid collected after condensing.",
         "note": "In sea water, that is the pure water."},
        {"term": "Boiling point",
         "definition": "The temperature at which a liquid turns to gas "
                       "throughout.",
         "note": "Different for each liquid — which is what makes them "
                 "separable."},
    ],

    # ── figures (§4.10) — the unit's ONE declared figure ────────────────────
    # NOTES §6: `c3-distillation-apparatus`, status `needed`. It is declared
    # here so the diagram manifest counts it as a tracked sourcing task, and
    # placed by a `figure` block in `core` below — a record with no block
    # renders nothing and is invisible to the page, and a block with no record
    # renders nothing and is invisible to the manifest. Both, or neither.
    #
    # ⚠️ The approved page draws an honest `.ks3-figure-slot` reading "Figure
    # c3-distillation-apparatus · to be drawn". That tag is NOT authored here:
    # MRB-257 / §8.10 retired it, and `r_figure` at status `needed` now emits
    # nothing at all rather than printing the build's backlog to a
    # twelve-year-old. `caption` is Design's own figcaption, which is the
    # drawing brief and is what the manifest lists.
    "figures": [
        {"id": "c3-distillation-apparatus",
         "kind": "diagram",
         "art": "distillation-apparatus",
         "status": "needed",
         "title": "Distillation apparatus",
         "desc": "A labelled side view of a laboratory still: a "
                 "round-bottomed flask of solution standing over a Bunsen "
                 "burner, with anti-bumping granules drawn in the liquid; a "
                 "thermometer through the neck with its bulb level with the "
                 "side arm; the side arm sloping down into a Liebig "
                 "condenser, whose outer jacket carries cold water in at the "
                 "lower end and out at the upper end, arrows showing the "
                 "water flowing against the vapour; and a beaker at the open "
                 "end catching the distillate.",
         "caption": "Distillation apparatus: round-bottomed flask over a "
                    "Bunsen with anti-bumping granules, thermometer bulb "
                    "level with the side arm, Liebig condenser with cold "
                    "water entering at the bottom and leaving at the top, and "
                    "a beaker collecting the distillate. The apparatus is "
                    "open to the air at the collecting end."},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Design draws both paragraphs inside ONE `.ks3-explainer` section;
        # `r_explainer` emits one paragraph per block, so the paragraph break
        # is kept by authoring two. See the report.
        {"type": "explainer",
         "text": "<strong>Distillation</strong> is evaporation with the "
                 "vapour caught. Boil the solution: the solvent leaves as a "
                 "gas and the dissolved solid stays behind, because it does "
                 "not boil at anything like that temperature. Cool the gas on "
                 "a cold surface and it <strong>condenses</strong> back to a "
                 "liquid — and that liquid is the solvent on its own."},
        {"type": "explainer",
         "text": "Evaporation keeps the solid. Distillation keeps the liquid. "
                 "Same physics, opposite purpose."},

        {"type": "figure", "ref": "c3-distillation-apparatus"},

        # #s-still — the flagship. `class="ks3-block"` alone on Design's page:
        # light ground, so the segment is `check`, not `practical`.
        {"type": "still-run", "id": "run-the-still", "anchor": "s-still",
         "eyebrow": "Your turn · run the still",
         "heading": "Pick a mixture, decide about the cooling water, then run "
                    "it a stage at a time.",
         "demand": "investigate",

         # Two dials. The first names mixtures by id and takes their labels
         # from `mixtures[].name`, so a mixture's name lives once; the second
         # is the switch the lesson turns on. Changing either dial resets the
         # run to stage 0 (and changing the mixture clears the prediction,
         # because the question is a different question).
         "dials": [
             {"id": "mixture", "label": "In the flask", "start": "salt",
              "options": ["salt", "ink", "ethanol"]},
             {"id": "cooling", "label": "Cold water through the condenser",
              "start": "running",
              "options": [
                  {"id": "running", "label": "Running", "cooling": True},
                  {"id": "off", "label": "Turned off", "cooling": False},
              ]},
         ],

         # Three readouts. `before` is the resting reading at stage 0 (the
         # flask takes the mixture's own name, hence `before_from`); `reads`
         # names the field each gauge moves to once the Bunsen is lit.
         "gauges": [
             {"id": "thermometer", "label": "Thermometer at the side arm",
              "before": "20 °C", "reads": "temp",
              # NOTES §6's tweakable prop, `showThermometer`. False hides the
              # reading and the run must be read off the stages instead —
              # front-of-class, not a student default.
              "show_thermometer": True,
              "hidden_value": "covered up"},
             {"id": "beaker", "label": "In the beaker",
              "before": "empty", "reads": "collected",
              "warm_value": "still empty"},
             {"id": "flask", "label": "Left in the flask",
              "before_from": "name", "reads": "left"},
         ],

         "controls": {"start": "Light the Bunsen", "next": "Next stage",
                      "reset": "Reset the still"},

         # ⚠️ The rail's contract. A run counts only when something was
         # collected, which needs the cooling running — see the module
         # docstring.
         "completion": {"runs_required": 1, "requires_cooling": True},

         # The switch turned off. `stage` is 1-based: the stage whose text is
         # replaced is the one where the vapour reaches the condenser, and it
         # is the same sentence for every mixture because the condenser does
         # not care what is in the flask. The final stage differs per mixture
         # and is authored on each (`warm_final`).
         "warm_condenser": {
             "stage": 3,
             "stage_text": "With no cold water in the jacket, the condenser "
                           "is as warm as the vapour. Nothing condenses. The "
                           "vapour goes straight out of the open end and into "
                           "the room — you can smell it, and you will not "
                           "collect it.",
             "result_title": "An empty beaker and a room that smells of it.",
             "result_text": "Boiling separated the mixture perfectly well — "
                            "the flask proves that. Without cooling there was "
                            "nothing to turn the vapour back into a liquid, "
                            "so the separated substance left the apparatus "
                            "and you have none of it. Distillation is two "
                            "jobs: boil to separate, cool to collect. Doing "
                            "one of them gets you nothing."},

         "mixtures": [
             {"id": "salt", "name": "Sea water",
              "temp": "101 °C",
              "left": "Salt, dry in the flask",
              "collected": "Pure water",
              "predict": "Before you heat it: what comes out of the "
                         "condenser?",
              "options": [
                  "Salt water, a bit weaker",
                  "Pure water, with the salt left behind",
                  "Nothing — salt water cannot be separated",
              ],
              "stages": [
                  "The solution boils. The thermometer settles at just over "
                  "100 °C — a little above pure water, because of the "
                  "dissolved salt, and it creeps up as the flask gets "
                  "saltier.",
                  "Water leaves the solution as a gas and travels down the "
                  "side arm. The salt cannot: it has no way of becoming a gas "
                  "at this temperature, so it stays in the flask.",
                  "The vapour meets the condenser, whose outer jacket is full "
                  "of cold water flowing the other way. It cools and "
                  "condenses back to a liquid.",
                  "Clear drops run into the beaker. That is fresh water, and "
                  "the flask now holds a stronger salt solution — eventually "
                  "dry salt.",
              ],
              "warm_final": "Nothing arrives in the beaker. The water left "
                            "the flask as a gas, passed a condenser as warm "
                            "as itself, and is now somewhere in the room. The "
                            "flask is getting saltier all the same — the "
                            "separating worked, the collecting never "
                            "happened.",
              "result_title": "Fresh water in the beaker, salt in the flask.",
              # SYS-7 — the result panel MODELLED tasting a lab distillate.
              # Replaced with the legitimate test for the same claim.
              "result_text": "Boiling separated them because only one of the "
                             "two can become a gas. Cooling collected the one "
                             "that did. Evaporate the distillate to dryness "
                             "and nothing at all is left behind — which is "
                             "exactly the point."},

             {"id": "ink", "name": "Blue ink",
              "temp": "100 °C",
              "left": "Dye, as a ring in the flask",
              "collected": "Colourless water",
              "predict": "Before you heat it: what colour is the liquid in "
                         "the beaker?",
              "options": [
                  "Blue, the same as the ink",
                  "Paler blue",
                  "Colourless",
              ],
              "stages": [
                  "The ink boils at 100 °C. Ink is mostly water with a dye "
                  "dissolved in it, and the dye is not going anywhere.",
                  "Water vapour comes off, colourless. The dye stays behind "
                  "and the ink in the flask gets darker as it concentrates.",
                  "The vapour condenses in the cold jacket of the condenser.",
                  "Colourless drops collect in the beaker. The dye is a ring "
                  "of solid left in the flask.",
              ],
              "warm_final": "The beaker stays dry. The water has gone off "
                            "into the room as a gas and the flask holds a "
                            "darker, more concentrated ink. The dye never "
                            "travelled — and this time neither did anything "
                            "else, as far as you are concerned.",
              "result_title": "Colourless water out, dye left behind.",
              "result_text": "A dye that made the whole liquid blue turns out "
                             "to be a solid dissolved in water. Distillation "
                             "takes the water away from it, and the colour "
                             "never travels."},

             {"id": "ethanol", "name": "Ethanol and water",
              "temp": "78 °C",
              "left": "Water, still in the flask",
              "collected": "Mostly ethanol",
              "predict": "Before you heat it: which liquid comes over first?",
              "options": [
                  "Water, because there is more of it",
                  "Ethanol, because it boils at a lower temperature",
                  "Both together, mixed",
              ],
              "stages": [
                  "The mixture starts to boil at about 78 °C — the boiling "
                  "point of ethanol, not of water.",
                  "The vapour coming off is mostly ethanol. Water is still in "
                  "the flask, because 78 °C is not hot enough to boil it.",
                  "The vapour condenses in the condenser and the first drops "
                  "arrive in the beaker.",
                  "The thermometer starts to climb towards 100 °C. From now "
                  "on what is coming over is mostly water — so this is the "
                  "moment to change the beaker.",
              ],
              "warm_final": "The thermometer climbs towards 100 °C with an "
                            "empty beaker underneath it. The ethanol came off "
                            "first exactly as it should have, and every drop "
                            "of it went out of the open end as a vapour "
                            "instead.",
              "result_title": "Mostly ethanol first, then mostly water.",
              "result_text": "Two liquids, two boiling points, and the "
                             "thermometer tells you which one is coming over. "
                             "Mostly, not purely: a single still cannot fully "
                             "separate them, which is what a fractionating "
                             "column is for."},
         ]},

        {"type": "key-fact", "ref": "boil-then-cool"},

        # #s-words — Design's "Four words". ⚠️ `r_keyword` emits no `id`, so
        # this `anchor` currently reaches no page and the rail's third stop
        # links nowhere. The anchor is authored because it is what Design drew
        # and what the rail points at; the missing `_id_attr(block)` is in the
        # report as a one-line renderer fix, not worked around here.
        {"type": "keyword", "anchor": "s-words",
         # Design's own head and lead, lifted from the approved
         # page. `r_keyword` fell back to "Words to know" and a
         # softer lead until MRB-272 made both authorable.
         "eyebrow": "Four words",
         "lead": "Say your answer out loud before you turn each "
                 "card over. If you cannot say it, you do not "
                 "know it yet.",
         "terms": ["Distillation", "Condense", "Distillate", "Boiling point"]},

        {"type": "misconception", "id": "think-commit-spray",
         "anchor": "s-think", "targets": "MIX-10"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # Cream band, ink outline, accent shadow — never amber. `card` is the
    # ground Design drew it on.
    "key_facts": [
        {"id": "boil-then-cool",
         "text": "Distillation separates a liquid from what is dissolved in "
                 "it, or two liquids with different boiling points. Boil to "
                 "separate, cool to collect — and the thing you keep is the "
                 "one that came over as a gas.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think`, the MIX-10 confrontation. The quote comes from the register
    # entry named by `targets`; `paragraphs` is the line Design prints under
    # it, and the reveal is gated behind the commitment (Law 4).
    "activities": [
        {"id": "think-commit-spray",
         "kind": "predict",
         "demand": "explain",
         "targets": "MIX-10",
         "eyebrow": "Think again",
         "paragraphs": [
             "Sea spray really does taste of salt, and a badly run still "
             "really does give a salty distillate. Commit before you read on.",
         ],
         "options": [
             "Right — dissolved salt boils off with the water, so the "
             "steam is salty",
             "Wrong — the salty taste comes from droplets of liquid, not from "
             "vapour",
             "Right, but only when boiling hard, since fast boiling "
             "carries salt up as gas",
             "Wrong — the salt stays in the sea, so sea spray is not "
             "really salty",
         ],
         "reveal": [
             "There are two different things coming off a boiling pan and "
             "only one of them is a gas. <strong>Water vapour</strong> is "
             "single water particles, and salt cannot travel in it — the salt "
             "has no way to become a gas at 100 °C. What you can see above "
             "the pan is not vapour at all: it is <strong>tiny droplets of "
             "liquid</strong>, and a droplet of sea water is sea water, salt "
             "and all.",
             "So the taste is real and the conclusion is wrong. Boil too hard "
             "and the mixture bumps, throws droplets up the neck of the "
             "flask, and they run into your distillate and make it salty. "
             "That is a fault in the method, not a property of steam — and it "
             "is why you heat gently, use anti-bumping granules, and never "
             "fill the flask more than half full.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # RUNGS → recall + apply, SELF_RUNGS → explain + produce. The option order
    # and the answer index are Design's; neither is moved.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Recall",
            "q": "Sea water is distilled. What is collected in the beaker, "
                 "and what stays in the flask?",
            "options": [
                "Salt is collected; the water stays in the flask",
                "A weaker salt solution is collected",
                "Nothing is collected — the water is destroyed by boiling",
                "Pure water is collected; the salt stays in the flask",
            ],
            "answer": 3,
            "feedback": {
                0: "Salt does not boil at 100 °C, so it cannot travel as a "
                   "gas. Only the water comes over.",
                1: "Only if droplets are thrown over by boiling too hard. "
                   "Done properly, the distillate has no salt in it at all.",
                2: "The water becomes a gas, and the condenser turns it "
                   "straight back into a liquid.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            # SYS-7 — the rung's PREMISE was a student tasting their own
            # distillate. Same question, detected the way a laboratory
            # actually detects it. The answer and all four options are
            # unchanged: boiling too hard is still the reason.
            "q": "A student distils sea water, evaporates their distillate "
                 "to dryness, and finds a faint white residue. What is the "
                 "most likely reason?",
            "options": [
                "Salt dissolves in water, so it travels wherever the water "
                "goes, including as a gas",
                "The condenser was not cold enough, so some of the salt "
                "condensed along with the water",
                "Distillation separates liquids only, so a dissolved solid "
                "always comes over with them",
                "They boiled it too hard, so droplets of salt water were "
                "thrown over into the condenser",
            ],
            "answer": 3,
            "feedback": {
                0: "Salt cannot evaporate at these temperatures. If salt "
                   "arrived, it arrived as liquid droplets, not as a gas.",
                1: "A warm condenser means less distillate collected, not "
                   "salty distillate.",
                2: "It can, and it is the standard method. The fault here is "
                   "in how it was run.",
            }},
        "explain": {
            "title": "Rung 3 · Explain",
            "q": "Explain how distillation separates salt from water. Your "
                 "answer must use boiling points and say where each substance "
                 "is at the end.",
            "field_label": "Your explanation",
            "placeholder": "When the solution is heated…",
            "success": [
                "Says the water boils at around 100 °C and turns into a gas.",
                "Says the salt has a far higher boiling point, so it cannot "
                "become a gas and stays in the flask.",
                "Says the water vapour is cooled in the condenser and "
                "condenses back to a liquid.",
                "Says the collected liquid is water with no salt in it, and "
                "names it as the distillate.",
                "Says nothing new is made — both substances are unchanged, "
                "just in different places.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "You have a pan with a lid, a fire, a cup and no other "
                 "equipment, and you need fresh water from sea water. "
                 "Describe your still, say exactly where the cold surface has "
                 "to be, and explain the one mistake that would make your "
                 "water salty.",
            "field_label": "Your answer",
            "placeholder": "I would boil the sea water in…",
            "success": [
                "Boils the sea water in the pan so the water leaves as a gas.",
                "Puts a cold surface — the lid, tilted, or a sheet — above "
                "the pan for the vapour to condense on.",
                "Positions the cup to catch the drops running off the low "
                "point of that surface.",
                "Says the salt stays in the pan because it cannot become a "
                "gas.",
                "Names the mistake: boiling so hard that droplets of sea "
                "water are thrown onto the cold surface and run into the cup.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Distillation separates a dissolved solid from its solvent, "
                "or two liquids with different boiling points. Boil the "
                "mixture: the substance with the lower boiling point leaves "
                "as a gas. Cool that gas in a condenser and it condenses back "
                "to a liquid — the distillate. The solid stays in the flask "
                "because it cannot become a gas. Boil too hard and droplets "
                "are carried over, which is a fault in the method, not a "
                "property of steam.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Design draws two paragraphs inside one `.ks3-layer-body`; two explainer
    # blocks keep the break. Flags 11 and 7 both live here — "mostly, not
    # purely", and the cost of boiling against a membrane.
    "stretch": [
        {"type": "explainer", "id": "fractionating-column",
         "text": "Two liquids can be separated the same way if their boiling "
                 "points differ. Heat a mixture of ethanol and water and the "
                 "vapour coming off at 78 °C is mostly ethanol; once the "
                 "thermometer climbs towards 100 °C, what is coming over is "
                 "mostly water. Mostly, not purely — a single pass gives you "
                 "an enriched mixture, and getting further needs a "
                 "fractionating column, which is a still with the same trick "
                 "repeated dozens of times up its length. A crude oil "
                 "refinery is a column tens of metres tall, drawing off "
                 "petrol near the top and bitumen at the bottom."},
        {"type": "explainer", "id": "the-cost-of-boiling",
         "text": "Distillation is honest about its cost. Boiling a tonne of "
                 "sea water takes an enormous amount of energy, which is why "
                 "most modern desalination plants avoid boiling altogether "
                 "and force sea water through a membrane instead — around "
                 "three to four kilowatt-hours per cubic metre, several times "
                 "less than a thermal still. On a life raft you have no "
                 "membrane and no fuel either, so the emergency kit contains "
                 "a solar still: a black tray, a clear cover, and the sun "
                 "doing the boiling slowly."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── safety (§1.5) ───────────────────────────────────────────────────────
    # No `safety_note`, deliberately. Design draws none, and this lesson gives
    # no instruction to run a still at the bench — the instrument is the
    # apparatus. The three cautions that matter (heat gently, use anti-bumping
    # granules, never fill past half) are taught inside the confrontation,
    # where they are the reason a distillate comes out salty rather than a
    # notice nobody reads. C6's `making-a-pure-dry-salt` is where the bench
    # instruction lands, and the note belongs with it.

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why the salt cannot come over with the "
                      "steam?",
              "cta": "Ask about this lesson",
              "anchor": "s-think"},

    "ks4_becomes": "Fractional distillation of crude oil and of liquid air, "
                   "and distillation as a required practical.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
