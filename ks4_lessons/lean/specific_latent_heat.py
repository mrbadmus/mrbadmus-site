# -*- coding: utf-8 -*-
"""Changes of state and specific latent heat, in the lean shape. Spec table:
ks4-specific-latent-heat.md (AQA 8464 6.3.2.3 / 8463 4.3.2.3, word for word the same). No HT-only
or physics-only line, no required practical. Every route gets the same teaching cards.

LEGACY (batch 3, Ks4Ladder). The ladder (r1..r4), the worked examples and Your turn questions
(cfExamples / cfQuestions, placed by the `cfifa` slot) and the practice set stay from the Design
page. Its eyebrow is route-aware already (8464 6.3.2.3 / 8463 4.3.2.3). The practice set reads the
route's `quiz` list (K.bank): five per route, both old stems kept word for word.

E = m L is on the Physics equation sheet (8463 Appendix, sheet equation 9: "thermal energy for a
change of state = mass × specific latent heat"); the content section words it "energy for a change
of state", which the card uses.

LOGIC_EDITS:
  1, 2. loggerFig (the cooling curve of Y) drew only as the (removed) data-logger bench ran
     (`tEnd = s.logP * 12`): drawn always, complete to 12 minutes, with its complete alt text.
  3. Rung 3 asked "Explain why sweating cools the body", the same question as practice question 2
     ("Why does sweating cool the body?"), so a pupil met it twice. It is now a chain on ice
     cooling a drink: the same spec line (latent heat; energy changes the internal energy, not the
     temperature), one right order. Same rung position, so its id (#r3) is kept."""

LOGIC_EDITS = [
    ("const tEnd = s.logDone ? 12 : s.logP * 12;", "const tEnd = 12;"),
    ("alt: s.logDone ? 'Cooling curve for Y.", "alt: tEnd === 12 ? 'Cooling curve for Y."),
    ("r3: { command: 'Explain', marks: 3, prompt: 'Explain why sweating cools the body. Put the "
     "links in order.',\n          links: ['Sweat on the skin evaporates, changing state from "
     "liquid to gas.', 'Changing state needs energy: the latent heat of vaporisation.', 'That "
     "energy is transferred from the skin, so the skin’s temperature falls.'],\n          "
     "herrings: [{ text: 'Sweat is colder than the skin, so it cools it by conduction.', why: "
     "'Sweat comes out at body temperature. The cooling comes from evaporation.' }, { text: "
     "'Evaporating sweat releases energy into the skin.', why: 'Evaporating takes energy in. "
     "Condensing is the change that releases it.' }] },",
     "r3: { command: 'Explain', marks: 3, prompt: 'Ice at 0 °C is put into a drink at 20 °C. "
     "Explain why the drink cools as the ice melts. Put the links in order.',\n          links: "
     "['The ice melts: it changes state from solid to liquid at 0 °C.', 'Melting needs energy, "
     "the latent heat of fusion, and this energy is transferred from the drink to the ice.', 'So "
     "the internal energy of the drink decreases, and its temperature falls.'],\n          "
     "herrings: [{ text: 'The ice gives its cold to the drink.', why: 'Energy moves from the "
     "warmer drink to the ice. There is no cold to pass on.' }, { text: 'Melting ice releases "
     "energy into the drink.', why: 'Melting takes energy in. Freezing is the change that "
     "releases it.' }] },"),
]

LESSON = {
    "slug": "specific-latent-heat",
    "start": {
        "setup": "A splash of boiling water and a puff of steam are both at 100 °C. The steam "
                 "gives a much worse burn.",
        "question": "If you had to guess, is that because the steam spreads over more skin, or "
                    "because it gives the skin more energy?",
        "options": [
            ("It spreads over more skin",
             "It gives the skin more energy. The steam condenses into water on your skin, and "
             "condensing releases a lot of energy with no change in temperature."),
            ("It gives the skin more energy",
             "It gives the skin more energy. The steam condenses into water on your skin, and "
             "condensing releases a lot of energy with no change in temperature."),
        ],
        "answer": 1,
    },
    "words": ["latent heat", "specific latent heat", "fusion", "vaporisation"],
    "knowledge": [
        {"kind": "card", "title": "Latent heat",
         "body": ["The energy needed for a substance to change state is called latent heat.",
                  "When a change of state occurs, the energy supplied changes the energy stored "
                  "(internal energy) but not the temperature."]},
        {"kind": "card", "title": "Specific latent heat",
         "body": ["The specific latent heat of a substance is the amount of energy required to "
                  "change the state of one kilogram of the substance with no change in "
                  "temperature.",
                  {"points": [
                      "Specific latent heat of fusion: change of state from solid to liquid.",
                      "Specific latent heat of vaporisation: change of state from liquid to "
                      "vapour.",
                      "Freezing and condensing transfer the same amount of energy back out.",
                  ]}]},
        {"kind": "card", "title": "The equation",
         "body": ["energy for a change of state = mass × specific latent heat",
                  "E = m L",
                  {"points": ["energy, E, in joules (J)",
                              "mass, m, in kilograms (kg)",
                              "specific latent heat, L, in joules per kilogram (J/kg)"]},
                  "This equation is on the Physics equation sheet. You need to be able to use it "
                  "and rearrange it.",
                  {"slot": "triangle:EQ_SLH"}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Heating and cooling graphs",
         "body": [{"slot": "legacy-fig:loggerFig"},
                  "Liquid Y cools in a cold room. On a graph of temperature against time:",
                  {"points": [
                      "A sloping section: the temperature changes and the state does not. Use "
                      "ΔE = m c Δθ.",
                      "A flat section: the state changes and the temperature does not. Use "
                      "E = m L.",
                      "B to C is Y freezing at 50 °C.",
                  ]}]},
        {"kind": "card", "title": "Energy from a flat section",
         "body": ["The 60 g of Y transfers energy to the room at a steady 30 J every second "
                  "(30 W).",
                  {"points": [
                      "The flat section lasts from 3 to 10 minutes: 7 minutes, which is 420 s.",
                      "Energy transferred: E = P t = 30 × 420 = 12 600 J.",
                      "Specific latent heat of fusion: L = E ÷ m = 12 600 ÷ 0.060 = 210 000 J/kg.",
                  ]}]},
        {"kind": "card", "title": "Measuring the specific latent heat of fusion of water",
         "body": [{"points": [
             "Put an immersion heater in a funnel of crushed ice, with a beaker underneath.",
             "Switch on for a set time. Measure the energy supplied with a joulemeter, and the "
             "mass of water that melts.",
             "Set up a second funnel of ice with no heater, for the same time. Take away the mass "
             "it melts, which came from the warm room.",
             "Then L = E ÷ m.",
         ]}]},
        {"kind": "reveal", "title": "Specific heat capacity or specific latent heat",
         "cols": ["Specific heat capacity", "Specific latent heat"],
         "rows": [
             ("What changes", "The temperature", "The state"),
             ("Equation", "ΔE = m c Δθ", "E = m L"),
             ("Unit", "J/kg °C", "J/kg"),
             ("On a heating graph", "A sloping section", "A flat section"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The temperature stays the same, so no energy is transferred.",
              "Energy is transferred. It changes the internal energy, but not the temperature."),
             ("Use ΔE = m c Δθ for a change of state.",
              "During a change of state Δθ = 0. Use E = m L."),
             ("The latent heat of fusion is for boiling.",
              "Fusion is melting, solid to liquid. Vaporisation is liquid to vapour."),
         ]}]},
    ],
    "key_fact": "The specific latent heat of a substance is the energy needed to change the state "
                "of 1 kg of it with no change in temperature: E = m L. During a change of state, "
                "the energy supplied changes the internal energy but not the temperature.",
    "deeper": [
        {"kind": "card", "title": "Water's values",
         "body": ["For water, the specific latent heat of fusion is 334 000 J/kg and the specific "
                  "latent heat of vaporisation is 2 260 000 J/kg. Boiling 1 kg of water takes "
                  "almost seven times the energy of melting 1 kg of ice."]},
        {"kind": "card", "title": "More than one stage",
         "body": ["Ice at −10 °C heated to water at 20 °C goes through three stages: the ice warms "
                  "(ΔE = m c Δθ), the ice melts (E = m L), the water warms (ΔE = m c Δθ). Work out "
                  "each one, then add them."]},
        {"kind": "card", "title": "Why sweating cools you",
         "body": ["Sweat evaporates from the skin. Evaporating needs energy, the latent heat of "
                  "vaporisation, and this energy is transferred from the skin, so the skin "
                  "cools."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Determine</strong>: get it from the graph, for example a time from where a "
             "flat section starts and ends.",
             "<strong>Calculate</strong>: write every line. With two stages, use one equation for "
             "each, then add.",
             "<strong>Compare</strong>: say how both are alike and how they differ, naming both "
             "each time.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-3", "logic_edits": LOGIC_EDITS},
    "equations": {
        "EQ_SLH": {"name": "Specific latent heat",
                   "written": "energy for a change of state = mass × specific latent heat",
                   "source": "none",
                   "top": {"s": "E", "name": "energy", "unit": "J"},
                   "bottom": [{"s": "m", "name": "mass", "unit": "kg"},
                              {"s": "L", "name": "specific latent heat", "unit": "J/kg"}]},
    },
}
