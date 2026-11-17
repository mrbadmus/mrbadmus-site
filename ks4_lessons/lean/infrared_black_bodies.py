# -*- coding: utf-8 -*-
"""Emission and absorption of infrared, and black bodies, in the lean shape. LEGACY record: the
Design batch-4 page keeps its ladder (Ks4Practice) and practice set, so their question ids
survive. Spec table: ks4-infrared-black-bodies.md (AQA 8463 4.6.3.1 and the all-tier part of
4.6.3.2, physics only, with Required practical activity 10). TF TH only.

The lead's ruling: radiation-balance-temperature owns the 4.6.3.2 (HT only) statements, so this
page carries one TH card that points there, and earthFig (TH only in the logic) is not placed.
Required practical activity 10 is taught here for TF TH (properties-em-waves-1 teaches the same
practical, 8464 Required practical activity 21, on CF CH).

The practice set is a hard-coded bank in the logic (`bankSrc`): fixes are logic_edits. The
question id is a hash of the stem, so every stem is kept and only options and explanations
change.

logic_edits:
  1. Bank item "A metal rod is heated...": one distractor ("At white heat, the peak ... has moved
     into the visible") needs knowledge beyond the spec to reject, and the explanations used
     "emission spectra" and "different electrons". Options and explanations rewritten, each
     distractor definitely wrong; the right option is no longer the longest.
  2. Bank item "Why are the walls of a thermos flask silvered?": dashed explanation tails and
     capitals removed, the right option shortened, the arguable "keeping the flask cool" option
     replaced.
  3. Rung 3 chain (glowing rod): its first two links were two parallel effects of the rising
     temperature, so two orders were right. Rewritten as one forced order. Same rung position."""

LESSON = {
    "slug": "infrared-black-bodies",
    "start": {
        "setup": "The wires in a toaster get hotter and hotter.",
        "question": "If you had to guess, what do you see when they get hot enough?",
        "options": [
            ("They start to glow",
             "They glow, first a dull red, then brighter orange. Hot enough, they emit visible "
             "light as well as infrared."),
            ("They stay dark",
             "They glow, first a dull red, then brighter orange. Hot enough, they emit visible "
             "light as well as infrared."),
        ],
        "answer": 0,
    },
    "words": ["infrared radiation", "emit", "absorb", "perfect black body"],
    "knowledge": [
        {"kind": "card", "title": "Everything emits infrared",
         "body": ["All bodies (objects), no matter what temperature, emit and absorb infrared "
                  "radiation.",
                  "The hotter the body, the more infrared radiation it radiates in a given time."]},
        {"kind": "card", "title": "Temperature and emission",
         "body": ["The intensity and wavelength distribution of any emission depends on the "
                  "temperature of the body.",
                  {"slot": "legacy-fig:curveFig"},
                  {"points": [
                      "A hotter body emits more radiation at every wavelength.",
                      "The peak of its emission moves to shorter wavelengths.",
                      "Hot enough, it emits visible light too: it glows red, then orange, then "
                      "yellow and white.",
                      "A metal glowing orange still gives out most of its radiation as infrared.",
                  ]}]},
        {"kind": "card", "title": "Perfect black bodies",
         "body": ["A perfect black body is an object that absorbs all of the radiation incident "
                  "on it.",
                  "A black body does not reflect or transmit any radiation.",
                  "Since a good absorber is also a good emitter, a perfect black body would be the "
                  "best possible emitter."]},
        {"kind": "reveal", "title": "Surfaces and infrared",
         "cols": ["Absorbing infrared", "Emitting infrared"],
         "rows": [
             ("Matt black", "The best absorber", "The best emitter"),
             ("Shiny silver", "The poorest absorber: it reflects most of it",
              "The poorest emitter"),
         ]},
        {"kind": "card", "title": "Required practical activity 10",
         "body": ["Investigate how the amount of infrared radiation absorbed or radiated by a "
                  "surface depends on the nature of that surface.",
                  {"slot": "fig:leslie-cube"},
                  {"points": [
                      "Fill a Leslie cube with hot water. Each of its four faces has a different "
                      "surface: matt black, shiny black, matt white and shiny silver.",
                      "Point an infrared detector at each face in turn, from the same distance.",
                      "Record the reading for each face.",
                  ]},
                  "Matt black radiates the most infrared. Shiny silver radiates the least.",
                  "Keep the distance from the detector the same for every face, and take every "
                  "reading at the same water temperature, so the test is fair."]},
        # routes CH+TH = isHigher, the flag the batch-4 logic binds; the lesson exists on TF/TH only,
        # so this card shows on TH only (17 Nov 2026: ["TH"] gated it on isTH, never bound here).
        {"kind": "card", "title": "Absorbing and emitting together", "routes": ["CH", "TH"],
         "body": ["Whether a body's temperature rises, falls or stays constant depends on the "
                  "balance between the radiation it absorbs and the radiation it emits.",
                  "This is in the lesson on radiation balance and the Earth's temperature."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Cold objects do not emit radiation.",
              "All bodies emit infrared radiation, whatever their temperature."),
             ("A hotter body emits only short wavelengths.",
              "It emits more at every wavelength. The peak moves to shorter wavelengths."),
             ("A perfect black body reflects all radiation.",
              "It absorbs all the radiation incident on it, and reflects none."),
         ]}]},
    ],
    "key_fact": "All bodies, no matter what temperature, emit and absorb infrared radiation, and "
                "the hotter the body, the more infrared radiation it radiates in a given time. A "
                "perfect black body absorbs all of the radiation incident on it; since a good "
                "absorber is also a good emitter, it would be the best possible emitter.",
    "deeper": [
        {"kind": "card", "title": "A model black body",
         "body": ["A box with a tiny hole behaves almost like a perfect black body.",
                  {"slot": "legacy-fig:cavityFig"},
                  "Radiation that enters the hole reflects around inside until it is absorbed. "
                  "Almost none gets back out."]},
        {"kind": "card", "title": "A vacuum flask",
         "body": ["The walls of a vacuum flask are silvered. Shiny surfaces are poor emitters and "
                  "poor absorbers of infrared, so less energy is transferred by radiation."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Compare</strong> two emission curves: say which is higher, and which peaks "
             "at a shorter wavelength.",
             "<strong>Explain</strong> a choice of surface: say whether it absorbs or emits well, "
             "and what that does.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-4",
        "logic_edits": [
            ("opts: [['As its temperature increases it emits more at every wavelength, and the "
             "peak of its emission shifts to shorter wavelengths', true], ['The metal changes "
             "chemical composition as it gets hotter, producing different coloured oxides', "
             "false], ['Different wavelengths of light are produced by different electrons in the "
             "metal', false], ['At white heat, the peak of its emission has moved into the visible "
             "part of the spectrum', false]],\n        wrong_explanations: { 1: 'The colour change "
             "is due to temperature-dependent emission spectra \\u2014 not chemical changes. A pure "
             "metal rod would show the same progression.', 2: 'Different electrons in the metal "
             "contribute to emission, but the pattern follows the temperature-dependent black body "
             "spectrum \\u2014 the overall colour shift is about temperature.', 3: 'The peak moves "
             "to shorter wavelengths, but at white heat it is still in the infrared. The rod looks "
             "white because it now emits all visible wavelengths strongly enough to mix.' } },",
             "opts: [['Its emission increases and shifts to shorter wavelengths', true], ['It is "
             "changing into a different coloured substance', false], ['It emits less infrared as "
             "it gets hotter', false], ['It stops emitting infrared once it glows', false]],\n"
             "        wrong_explanations: { 1: 'The colour change comes from the rising "
             "temperature, not from a chemical change.', 2: 'The hotter the body, the more "
             "infrared it radiates in a given time.', 3: 'It emits more infrared than ever. "
             "Visible light is added as well.' } },"),
            ("opts: [['Silvered walls are poor emitters and poor absorbers of infrared \\u2014 they "
             "reflect radiation back, reducing thermal energy transfer by radiation', true], "
             "['Silver is a good conductor \\u2014 it rapidly distributes heat evenly around the "
             "flask walls', false], ['Silver reacts with oxygen in the air \\u2014 the oxide layer "
             "acts as an insulator', false], ['The bright colour of silver reflects external "
             "light, keeping the flask cool', false]],\n        wrong_explanations: { 1: 'Silver "
             "is an excellent conductor \\u2014 but the silvered wall is there to REDUCE radiation "
             "transfer, not to conduct heat.', 2: 'Silver doesn\\u2019t form a significant "
             "protective oxide layer at room temperature \\u2014 the silvering works by reflection "
             "of radiation.', 3: 'Visible light reflection is not the primary reason \\u2014 "
             "it\\u2019s the IR radiation reflection that reduces thermal energy transfer.' } },",
             "opts: [['Shiny surfaces are poor emitters and poor absorbers of infrared', true], "
             "['Silver conducts energy quickly around the walls', false], ['Silver reacts with air "
             "to make an insulating layer', false], ['Shiny surfaces are the best emitters of "
             "infrared', false]],\n        wrong_explanations: { 1: 'The silvering is there to "
             "reduce the energy transferred by radiation, not to conduct it.', 2: 'The silvering "
             "works by reflecting infrared, not by any chemical layer.', 3: 'Shiny surfaces are "
             "the poorest emitters. Matt black is the best.' } },"),
            ("links: ['As its temperature rises, the rod emits more radiation at every "
             "wavelength.', 'The distribution shifts to shorter wavelengths, so more of the "
             "emission is visible light.', 'Shorter visible wavelengths are added as it heats: red "
             "first, then orange, then yellow-white. The peak is still in the infrared.'],",
             "links: ['As the rod gets hotter, its emission shifts to shorter wavelengths.', "
             "'Once enough is emitted at the longest visible wavelengths, the rod glows red.', "
             "'As it gets hotter still, shorter visible wavelengths are added, so it glows orange "
             "and then yellow-white.'],"),
            # Examiner (EXAMINER.md) MUST/SHOULD fixes, applied after the record's own edits.
            ("{ text: 'An object that absorbs all of the radiation incident on it', correct: true }",
             "{ text: 'An object that absorbs all radiation', correct: true }"),
            ("['Shiny surfaces are poor emitters and poor absorbers of infrared', true]",
             "['Shiny surfaces are poor emitters and absorbers', true]"),
            ("['It emits more at every wavelength, and the distribution is shifted to shorter wavelengths', true]",
             "['It emits more, with its peak at shorter wavelengths', true]"),
        ],
    },
}
