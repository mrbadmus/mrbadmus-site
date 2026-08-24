"""P1 L6 — Radiation (PROCESS).

The second route, and the one that does not need anything to travel through.
p1-05's mechanism was particles handing a vibration along; this one has no
particles in it at all, which is exactly why it is a separate lesson and why
`KS3.P.ECT.02` names the two routes separately.

── ⚖️ THE SCIENCE RULING THIS LESSON IS BUILT ON ────────────────────────

**Radiation needs nothing in between, and that is the whole lesson.** The Sun
is a hundred and fifty million kilometres away across an almost perfect
vacuum, and the warmth arrives anyway. `ENER-14` — "radiation needs air, like
sound does" — is the misconception, and it is a reasonable one for a student
who has just met sound and just met conduction, both of which genuinely do
need matter. `#s-gap` is built to kill it with a measurement rather than an
assertion.

── ⚖️ SCIENCE CORRECTION MADE, AND IT CHANGES WHAT THE BENCH TEACHES ────

The folk version of this lesson is *black absorbs and emits best, white and
shiny are poor*. That is half right and the wrong half is the half students
remember. **For the infrared a warm object actually gives off, it is the
SHINE that matters and the colour barely does.** Matt white paint emits nearly
as well as matt black — its emissivity is about 0.9 against black's 0.95 —
while polished silver is down near 0.05. A Leslie's cube shows this plainly,
and it is what the four faces on `#s-surface` are chosen to show:

    matt black       100        the best, and only just
    matt white        92        nearly as good, and it is WHITE
    dull silver       34        the same metal, roughened
    polished silver   12        the same metal again, polished

Ruled and applied: the bench teaches SHINY vs MATT as the thing that decides
it, with colour a small effect on top. The alternative — printing a
black-beats-white ordering and quietly leaving matt white out — would make a
tidier page by hiding the reading that contradicts it, and MRB-257 §5A.1 is
explicit that the instrument is the measurement and the prose is what changes.

⚠️ **Colour DOES matter for sunlight**, because sunlight is mostly visible and
a black surface absorbs visible light far better than a white one. That is why
a black car gets hotter in the sun and it is a different fact about a
different part of the spectrum. It is in `stretch`, said in full, so the
student who has noticed the apparent contradiction gets the answer rather than
a page that pretends there is no contradiction.

**Good emitters are good absorbers, and the bench measures both.** The two
columns come out in the same order, which is not a coincidence and is not
authored as a claim: `ks3_art/p1.py` checks that the emission ranking and the
absorption ranking agree before it will render the block.
"""

LESSON = {
    "slug":        "radiation",
    "title":       "Radiation",
    "discipline":  "physics",
    "unit":        "energy-transfers",
    "family":      "PROCESS",

    "covers":      ["KS3.P.ECT.02c"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "energy", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires":    ["conduction"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   [],
    "connects_heading": "Next in this unit",

    # ⊕ Authored so the page keeps its own 160-character summary
    # rather than a truncated `big_question` (MRB-257 audit 6.12).
    "meta_description": "Infrared crosses a vacuum exactly as well as it crosses "
                        "air. Four surfaces measured two ways, and what really "
                        "decides how well one works.",

    "big_question": "There is nothing at all between here and the Sun for a "
                    "hundred and fifty million kilometres. No air, no dust "
                    "worth speaking of, nothing to hand anything along. The "
                    "warmth arrives anyway.",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "Warmth across nothing", "done_when": "committed"},
        {"anchor": "s-surface", "short": "SURFACES",
         "label": "Four faces, two jobs", "done_when": "all_faces_read"},
        {"anchor": "s-gap",     "short": "GAP",
         "label": "What crosses a vacuum", "done_when": "all_cells_read"},
        {"anchor": "s-think",   "short": "THINK",
         "label": "Does it need air?", "done_when": "committed"},
        {"anchor": "s-ladder",  "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Stand in front of a bonfire on a still night and your face "
                 "is hot before the air is.",
        "prompt": "The air two metres from a bonfire is barely warmer than "
                  "the air behind you. Stand there and your face is "
                  "uncomfortable within seconds. Hold a sheet of card up and "
                  "your face cools instantly, even though the air can still "
                  "get past.",
        "commit": "What is reaching your face?",
        "options": [
            "Hot air, which the card blocks",
            "Something travelling in straight lines that the card stops",
            "The vibration, handed along through the air like it is handed "
            "along a spoon",
            "Nothing — your face only feels hot because you can see the "
            "flames",
        ],
        "reveal": "Something travelling in straight lines: infrared "
                  "radiation. It travels like light does, which is why it "
                  "casts a shadow behind a sheet of card, and why it "
                  "disappears the instant something opaque is in the way. It "
                  "does not need the air, and it barely warms the air on the "
                  "way through.",
    },

    "misconceptions": [
        {"id": "ENER-14",
         "statement": "Radiation needs air to travel through, like sound "
                      "does.",
         "elicited_by": "think-commit-vacuum",
         "confronted_by": "think-commit-vacuum"},
    ],

    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Everything gives off infrared radiation all the time, and "
                 "the hotter it is the more it gives off. It travels in "
                 "straight lines at the speed of light, it needs nothing to "
                 "travel through, and it stops when something absorbs it. "
                 "That is the second route a thermal transfer can take, and "
                 "it is the only one that works across empty space."},

        # #s-surface — the flagship. Ink-dark practical.
        {"type": "radiation-cube", "id": "four-faces", "anchor": "s-surface",
         "eyebrow": "At the bench · a Leslie's cube and four cans",
         "heading": "The same metal, finished four ways",
         "head_counter": {"format": "{n} of 4 faces read", "total": 4},
         "demand": "investigate",
         "prompt": "Every face is the same metal at the same temperature. "
                   "Pick one, commit to where it will come, then read both "
                   "measurements.",
         "gate": {"prompt": "Commit first. Which do you think decides how "
                            "well a surface gives off infrared?",
                  "options": ["How dark it is",
                              "How shiny it is",
                              "How thick the paint is",
                              "Nothing — all four will be the same"]},
         "resting": "Pick a face to read it.",
         "modes": [
             {"id": "emit", "label": "Giving off",
              "caption": "The cube is filled with water at 80 °C and a "
                         "detector sits 10 cm from each face.",
              "readout": "Detector reading", "unit": "units"},
             {"id": "absorb", "label": "Taking in",
              "caption": "Four identical cans, painted the four ways, sit "
                         "the same distance from the same heater for five "
                         "minutes.",
              "readout": "Temperature rise", "unit": "°C"},
         ],
         # ⚖️ `rank` IS THE ORDER. `ks3_art/p1.py` refuses to render this
         # block unless the emission ranking and the absorption ranking are
         # the same ranking — good emitters are good absorbers, and a bench
         # whose two columns disagreed would be teaching the opposite of the
         # law it exists to show.
         "faces": [
             {"id": "matt-black", "name": "Matt black", "rank": 0,
              "emit": 100, "absorb": 14.0,
              "note": "The best at both, and it is the surface every "
                      "textbook names. Look at the margin before deciding it "
                      "wins by a lot."},
             {"id": "matt-white", "name": "Matt white", "rank": 1,
              "emit": 92, "absorb": 12.9,
              "note": "Within a tenth of matt black, and it is white. The "
                      "warmth a warm object gives off is infrared, and to "
                      "infrared this paint is very nearly as black as the "
                      "black one. Colour is a small effect here."},
             {"id": "dull-silver", "name": "Dull silver", "rank": 2,
              "emit": 34, "absorb": 4.8,
              "note": "The bare metal, roughened with wire wool. A third of "
                      "the black face, from a change that is nothing to do "
                      "with colour at all."},
             {"id": "polished-silver", "name": "Polished silver", "rank": 3,
              "emit": 12, "absorb": 1.7,
              "note": "The same metal as the face above, polished. An eighth "
                      "of the matt black face — the biggest gap on the bench, "
                      "and the two surfaces are made of the same substance."},
         ],
         "order_claim": ["matt-black", "matt-white", "dull-silver",
                         "polished-silver"],
         "close": [
             "The two measurements come out in the same order, every time. A "
             "surface that gives off infrared well takes it in well: they "
             "are the same property looked at from two sides.",
             "And the thing that decides it is not what a textbook diagram "
             "usually shows. Matt white came within eight per cent of matt "
             "black; polishing the silver dropped it by two thirds. "
             "<strong>Shiny or matt</strong> is what matters to infrared, "
             "and colour is only a small effect on top of it.",
         ]},

        # #s-gap — the discrimination that kills ENER-14.
        {"type": "across-the-gap", "id": "three-gaps", "anchor": "s-gap",
         "eyebrow": "Three gaps, two routes",
         "heading": "Which route survives having nothing in the way?",
         "head_counter": {"format": "{n} of 6 cells read", "total": 6},
         "demand": "classify",
         "prompt": "A hot block and a cool detector, 10 cm apart, with three "
                   "different things in between. Read all six cells, then "
                   "compare the two rows.",
         "resting": "Pick a cell to read it.",
         "gaps": [
             {"id": "touching", "label": "Pressed together"},
             {"id": "air", "label": "A 10 cm air gap"},
             {"id": "vacuum", "label": "A 10 cm vacuum"},
         ],
         "routes": [
             {"id": "conduction", "label": "Conduction"},
             {"id": "radiation", "label": "Radiation"},
         ],
         "cells": {
             "conduction:touching": {
                 "verdict": "Full", "level": 3,
                 "obs": "The fastest transfer on the bench. The particles of "
                        "one block are in contact with the particles of the "
                        "other, so the vibration is handed straight across."},
             "conduction:air": {
                 "verdict": "Almost none", "level": 1,
                 "obs": "Air particles are far apart and hardly ever touch, "
                        "so there is almost nothing to hand the vibration "
                        "along. A little gets through, very slowly. This is "
                        "why trapped air is such a good insulator."},
             "conduction:vacuum": {
                 "verdict": "None at all", "level": 0,
                 "obs": "Nothing. Not a slow trickle — nothing. Conduction "
                        "is particles knocking into particles, and there are "
                        "no particles, so there is nothing that could "
                        "happen."},
             # ⊖ CORRECTED to level 3. The three pips are a visual encoding
             # of `level`, so level 2 DREW radiation as weaker when the blocks
             # touch. It is not weaker; it is swamped, which the observation
             # already says — and the closing panel's claim is that radiation
             # reads the same in all three gaps.
             "radiation:touching": {
                 "verdict": "Full", "level": 3,
                 "obs": "Both blocks are radiating the whole time, as "
                        "everything above absolute zero does. With the blocks "
                        "touching it is completely swamped by the conduction "
                        "and you would never notice it."},
             "radiation:air": {
                 "verdict": "Full", "level": 3,
                 "obs": "Unaffected by the gap. The infrared crosses the 10 "
                        "centimetres in a third of a nanosecond and hardly "
                        "warms the air on the way, which is why the air in "
                        "the gap stays cool."},
             "radiation:vacuum": {
                 "verdict": "Full", "level": 3,
                 "obs": "Exactly the same reading as through air, to the "
                        "last digit. Taking every particle out of the gap "
                        "changed nothing at all, because radiation was never "
                        "using them."},
         },
         "close": [
             "Read the two rows across. Conduction goes full, almost none, "
             "none — it depends entirely on what is in the gap. Radiation "
             "reads the same in all three.",
             "That is the difference between the two routes in one line, and "
             "it is why the Sun can heat the Earth across a hundred and "
             "fifty million kilometres of nothing.",
         ]},

        {"type": "key-fact", "ref": "needs-nothing"},

        {"type": "keyword", "anchor": "s-words",
         "eyebrow": "Four words",
         "lead": "Say your answer out loud before you turn each card over.",
         "terms": ["Radiation", "Infrared", "Vacuum", "Absorb"]},

        {"type": "misconception", "id": "think-commit-vacuum",
         "anchor": "s-think", "targets": "ENER-14"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    "key_facts": [
        {"id": "needs-nothing",
         "text": "Radiation travels in straight lines at the speed of light "
                 "and needs nothing to travel through — it crosses a vacuum "
                 "exactly as well as it crosses air. Matt surfaces give it "
                 "off and take it in far better than shiny ones do.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    "vocabulary": [
        {"term": "Radiation",
         "definition": "A thermal transfer carried by infrared travelling in "
                       "straight lines, needing nothing in between.",
         "note": "The only one of the routes that works across empty space."},
        {"term": "Infrared",
         "definition": "The kind of radiation a warm object gives off. It is "
                       "just beyond red light and your eyes cannot see it.",
         "note": "Everything gives it off all the time, and the hotter "
                 "something is the more of it there is."},
        {"term": "Vacuum",
         "definition": "A space with no particles in it.",
         "note": "Conduction cannot cross one. Radiation crosses it without "
                 "being affected at all."},
        {"term": "Absorb",
         "definition": "To take radiation in, so that it fills a thermal "
                       "store instead of carrying on.",
         "note": "A surface that absorbs well also gives off well. They are "
                 "the same property."},
    ],

    "activities": [
        {"id": "think-commit-vacuum",
         "kind": "predict",
         "demand": "explain",
         "targets": "ENER-14",
         "prompt": "A hot object is put inside a sealed jar and the air is "
                   "pumped out. A detector outside the jar was reading "
                   "infrared before the pump was switched on. Commit before "
                   "you read on.",
         "options": [
             "The reading drops to zero, because there is nothing to carry "
             "it",
             "The reading halves, because one of the two routes has gone",
             "The reading is unchanged, because radiation was never using "
             "the air",
             "The reading rises, because the air was in the way",
         ],
         "reveal": [
             "Unchanged. Radiation is not a vibration handed from particle "
             "to particle and never was — it travels the way light travels, "
             "and light crosses a vacuum perfectly well. This is what "
             "separates it from sound, which genuinely does stop dead when "
             "the air is pumped out.",
             "What the pump DOES change is the other route. With air in the "
             "jar there was a small, slow conduction as well; with the air "
             "gone that route is exactly zero. So pumping the air out cuts "
             "the total transfer a little and leaves the radiation part "
             "untouched — which is precisely how a vacuum flask works, and "
             "why the inside of one is also silvered.",
         ]},
    ],

    "ladder": {
        "recall": {
            "q": "Which of these does radiation need in order to travel?",
            "options": [
                "Air",
                "Nothing at all",
                "Any material, solid, liquid or gas",
                "Particles that are touching",
            ],
            "answer": 1,
            "feedback": {
                0: "The Sun's warmth reaches us across a hundred and fifty "
                   "million kilometres with no air anywhere along the way.",
                2: "Radiation crosses a vacuum with exactly the same reading "
                   "as it crosses air. That is conduction you are thinking "
                   "of.",
                3: "Particles touching is what conduction needs. Radiation "
                   "works with no particles present at all.",
            }},
        "apply": {
            "q": "A vacuum flask has a silvered inner surface, a vacuum "
                 "between its two walls, and a plastic stopper. Which part "
                 "is doing which job?",
            "options": [
                "The vacuum stops radiation and the silvering stops "
                "conduction",
                "All three parts stop radiation, which is the only route "
                "that matters",
                "The silvering stops conduction and the stopper stops "
                "radiation",
                "The vacuum stops conduction and the silvering cuts "
                "radiation right down",
            ],
            "answer": 3,
            "feedback": {
                0: "The wrong way round. A vacuum is exactly what radiation "
                   "is unaffected by, and silvering is a surface finish, "
                   "which is nothing to do with conduction.",
                1: "The vacuum does nothing to radiation at all. It is there "
                   "for the other route.",
                2: "Silvering is a surface, and a shiny surface is a poor "
                   "emitter — that is a radiation job. The stopper is there "
                   "to stop the hot liquid itself getting out.",
            }},
        "explain": {
            "q": "The bench measured matt white at 92 and matt black at 100, "
                 "but polished silver at only 12 — and the silver faces are "
                 "the same metal as each other. Explain what these numbers "
                 "show about what really decides how well a surface gives "
                 "off infrared.",
            "field_label": "Your explanation",
            "placeholder": "The two matt surfaces are almost the same, even "
                           "though…",
            "success": [
                "Notes that matt white and matt black are close, despite "
                "being opposite colours.",
                "Notes that the two silver faces are the same metal and are "
                "far apart.",
                "Concludes that shiny against matt is what decides it.",
                "Says colour makes only a small difference to infrared.",
                "Says a shiny surface reflects infrared instead of giving it "
                "off or taking it in.",
            ]},
        "produce": {
            "q": "Greenhouses in hot countries are often painted white on "
                 "the outside, and marathon runners are wrapped in shiny "
                 "silver foil at the finish. Both are about radiation and "
                 "they work for different reasons. Explain each one, and say "
                 "which of the two is about visible light and which is about "
                 "infrared.",
            "field_label": "Your two explanations",
            "placeholder": "The greenhouse paint is about…",
            "success": [
                "Says the white paint reflects sunlight, which is mostly "
                "visible light.",
                "Says colour matters for visible light, so white beats black "
                "there.",
                "Says the foil is shiny, and a shiny surface is a poor "
                "emitter of infrared.",
                "Says the runner's own body warmth is infrared, so the foil "
                "keeps it in rather than keeping sunlight out.",
                "Correctly assigns the greenhouse to visible light and the "
                "foil to infrared.",
            ]},
    },

    "key_note": "Radiation carries a thermal transfer in straight lines at "
                "the speed of light and needs nothing in between, so it is "
                "the only route that crosses a vacuum. Matt surfaces give it "
                "off and take it in well; shiny ones reflect it, which is "
                "what a vacuum flask and a survival blanket both use.",

    "stretch": [
        {"type": "explainer", "id": "two-parts-of-the-spectrum",
         "text": "If matt white gives off infrared nearly as well as matt "
                 "black, why does a black car get so much hotter in the sun "
                 "than a white one? Because the two are about different "
                 "parts of the spectrum. Sunlight is mostly VISIBLE light, "
                 "and to visible light white and black are exactly what they "
                 "look like — white reflects most of it and black takes "
                 "nearly all of it in. The warmth a car then gives off is "
                 "INFRARED, and to infrared both paints are close to black. "
                 "So the black car wins the absorbing and ties the emitting, "
                 "and it ends up hotter. A surface has one answer for each "
                 "part of the spectrum, and no rule about colour holds "
                 "across all of it."},
    ],

    "support": [],

    "safety_note": "A Leslie's cube is filled with water near boiling and "
                   "the metal faces reach the same temperature as the water "
                   "inside them.",

    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why matt white does nearly as well as matt "
                      "black?",
              "cta": "Ask about this lesson",
              "anchor": "s-surface"},

    "ks4_becomes": "Infrared as part of the electromagnetic spectrum, "
                   "emission and absorption compared quantitatively, and the "
                   "Earth's radiation balance.",

    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    "review_state": "draft",
}
