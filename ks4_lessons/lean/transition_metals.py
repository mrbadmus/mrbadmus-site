# -*- coding: utf-8 -*-
"""Properties of transition metals, in the lean shape. Spec table: ks4-transition-metals.md (AQA
8462 4.1.3.1 and 4.1.3.2, "(chemistry only)"; there is no 8464 section). Routes TF and TH only,
as the legacy lesson already is, so no card needs a route gate.

LEGACY (batch 11). The ladder (Ks4Practice rungs) and the practice set (the page's own BANK, the
same five items on both routes) stay from the Design page; the practice set does not read the
subtopic `quiz` list, so its fixes are logic_edits. Every stem is kept, so every practice id is kept.

logic_edits:
  1. Rung 2 item 2 (why copper compounds are coloured): credited option the longest (73 against
     23 and 30). Key shortened to "Copper is a transition metal"; same index credited.
  2. Rung 4 reject "Zinc is a typical transition metal": zinc is not one of the spec's examples
     and its status is not settled in this course, so it cannot be a plain wrong answer. Replaced
     by "Transition metals react vigorously with water".
  3. to 7. Practice Q1 to Q5: the credited option was the longest every time (Q1 149 characters;
     replies in capitals and with dashes). Stems kept; the same idea credited each time.

The Haber process catalyst (iron) is kept: 8462 4.10.4.1 names the iron catalyst, so it is on the
Triple spec, and it is the commonest example of a transition-metal catalyst.
"""

LOGIC_EDITS = [
    ("['Copper is a transition metal, and transition-metal compounds are coloured', ['Copper compounds contain water',",
     "['Copper is a transition metal', ['Copper compounds contain water',"),
    ("'“Zinc is a typical transition metal.”'",
     "'“Transition metals react vigorously with water.”'"),
    ('V("Why are transition metals more useful as structural materials than Group 1 metals?", [["Transition metals have high melting points, high density and high strength — Group 1 metals are soft, low-density and too reactive for structural use", true], ["Transition metals are cheaper than Group 1 metals — cost makes them more practical", false], ["Group 1 metals are radioactive — too dangerous for use in buildings", false], ["Transition metals are lighter than Group 1 metals — easier to work with structurally", false]], { "1": "Cost is a practical factor but not the reason given in chemistry. The key reasons are mechanical properties: strength, hardness, melting point.", "2": "Group 1 metals (lithium, sodium, potassium etc.) are NOT radioactive — they are just very reactive with water and oxygen, making them unsuitable for structural use.", "3": "Transition metals are actually DENSER (heavier) than Group 1 metals — the advantages are strength and chemical stability, not lower weight." }),',
     'Q("Why are transition metals more useful as structural materials than Group 1 metals?", \'They are strong, hard and react slowly with water\', [[\'Transition metals are cheaper to buy than Group 1 metals\', \'Cost is not the chemistry reason. Iron is chosen for its strength, hardness and low reactivity.\'], [\'Group 1 metals are radioactive and too dangerous to use\', \'Group 1 metals are not radioactive. They are soft and react vigorously with water and oxygen.\'], [\'Transition metals are lighter, so easier to build with\', \'Transition metals are denser than Group 1 metals.\']]),'),
    ('V("Which transition metal is used as a catalyst in the Haber process to manufacture ammonia?", [["Iron — it acts as a catalyst to speed up the reaction between nitrogen and hydrogen", true], ["Copper — widely used catalyst in many industrial processes", false], ["Platinum — the most effective transition metal catalyst", false], ["Nickel — used in all industrial catalytic processes", false]], { "1": "Copper is a good conductor but not the catalyst used in the Haber process.", "2": "Platinum is a catalyst in catalytic converters for car exhausts — the Haber process uses iron.", "3": "Nickel is used in hydrogenation of vegetable oils — not the Haber process." }),',
     'Q("Which transition metal is used as a catalyst in the Haber process to manufacture ammonia?", \'Iron\', [[\'Copper\', \'Copper is not the Haber process catalyst. Iron is.\'], [\'Platinum\', \'The Haber process uses an iron catalyst.\'], [\'Nickel\', \'Nickel is a catalyst for other reactions. The Haber process uses iron.\']]),'),
    ("Q('Copper(II) sulfate solution is blue and sodium sulfate solution is colourless. What does this show about copper?', 'Copper is a transition metal: transition-metal compounds are often coloured', [['Copper is more reactive than sodium', 'Sodium is far more reactive; colour is not about reactivity.'], ['Copper sulfate is not a salt', 'Both are salts.'], ['Copper is in Group 1', 'Copper is a transition metal in the central block.']]),",
     "Q('Copper(II) sulfate solution is blue and sodium sulfate solution is colourless. What does this show about copper?', 'Copper is a transition metal', [['Copper is more reactive than sodium', 'Sodium is far more reactive. Colour is not about reactivity.'], ['Copper sulfate is not a salt', 'Both are salts.'], ['Copper is in Group 1', 'Copper is a transition metal in the central block.']]),"),
    ("Q('Iron forms the compounds FeCl₂ and FeCl₃. What property of transition metals does this illustrate?', 'They form ions with different charges, here Fe²⁺ and Fe³⁺', [['They are good catalysts', 'Catalysis is a different property.'], ['They have high melting points', 'The two formulas show two ion charges, not melting point.'], ['They react vigorously with chlorine', 'Iron reacts less vigorously with chlorine than sodium does.']]),",
     "Q('Iron forms the compounds FeCl₂ and FeCl₃. What property of transition metals does this illustrate?', 'They form ions with different charges', [['They are useful as catalysts', 'Catalysis is a different property. The two formulae show Fe²⁺ and Fe³⁺.'], ['They have high melting points and densities', 'The formulae show two ion charges, not melting point or density.'], ['They react vigorously with chlorine', 'Iron reacts less vigorously with chlorine than sodium does.']]),"),
    ("Q('Sodium burns vigorously in chlorine to give a white solid. How does hot iron compare?', 'Iron reacts less vigorously, giving orange-brown iron(III) chloride', [['Iron does not react with chlorine at all', 'Hot iron wool does react, just less vigorously.'], ['Iron reacts more vigorously than sodium', 'Transition metals are less reactive than Group 1.'], ['Iron gives a white solid too', 'Iron(III) chloride is orange-brown; transition-metal compounds are coloured.']])",
     "Q('Sodium burns vigorously in chlorine to give a white solid. How does hot iron compare?', 'It reacts less vigorously', [['It does not react with chlorine at all', 'Hot iron does react with chlorine, but less vigorously than sodium.'], ['It reacts more vigorously than sodium', 'Transition metals are much less reactive than Group 1 metals.'], ['It also gives a white solid', 'Iron(III) chloride is brown. Transition-metal compounds are often coloured.']])"),
]

LESSON = {
    "slug": "transition-metals",
    "start": {
        "setup": None,
        "question": "If you had to guess, could you build a bridge out of sodium?",
        "options": [
            ("No",
             "No. Sodium is soft, melts at 98 °C and reacts with water. Iron, a transition "
             "metal, is hard, strong and slow to react."),
            ("Yes, if it was thick enough",
             "No. Sodium is soft, melts at 98 °C and reacts with water. Iron, a transition "
             "metal, is hard, strong and slow to react."),
        ],
        "answer": 0,
    },
    "words": ["transition metal", "catalyst", "coloured compound"],
    "knowledge": [
        {"kind": "card", "title": "Where the transition metals are",
         "body": [{"slot": "fig:transition-block"},
                  "The transition elements are metals in the central block of the periodic table, "
                  "between Group 2 and Group 3.",
                  "The examples to learn are chromium (Cr), manganese (Mn), iron (Fe), cobalt (Co), "
                  "nickel (Ni) and copper (Cu)."]},
        {"kind": "card", "title": "Different from Group 1",
         "body": ["The transition elements are metals with similar properties which are different "
                  "from those of the elements in Group 1."]},
        {"kind": "reveal", "title": "Transition metals and Group 1 compared",
         "cols": ["Transition metals", "Group 1 metals"],
         "rows": [
             ("Melting point", "High: iron melts at 1538 °C", "Low: sodium melts at 98 °C"),
             ("Density", "High: iron is 7.9 g/cm³", "Low: sodium is 0.97 g/cm³ and floats on water"),
             ("Strength and hardness", "Strong and hard", "Soft: they can be cut with a knife"),
             ("Reaction with oxygen", "Slow", "Fast: they tarnish in air within seconds"),
             ("Reaction with water", "Very slow, or none", "Vigorous: they fizz, giving hydrogen"),
             ("Reaction with halogens", "Less vigorous", "Vigorous: sodium burns in chlorine"),
         ]},
        {"kind": "card", "title": "Ions with different charges",
         "body": ["Many transition elements have ions with different charges.",
                  {"points": [
                      "Iron forms Fe²⁺ and Fe³⁺, so there are two iron chlorides, "
                      "FeCl₂ and FeCl₃.",
                      "Copper forms Cu⁺ and Cu²⁺.",
                      "A Group 1 metal forms only one ion, such as Na⁺.",
                  ]}]},
        {"kind": "card", "title": "Coloured compounds",
         "body": [{"slot": "fig:transition-colours"},
                  "Transition elements form coloured compounds. Group 1 ions do not: sodium "
                  "chloride is white and its solution is colourless."]},
        {"kind": "card", "title": "Catalysts",
         "body": ["Transition metals and their compounds are useful as catalysts. A catalyst "
                  "speeds up a reaction without being used up.",
                  "Iron is the catalyst in the Haber process, which makes ammonia."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Iron fizzes in water like sodium.",
              "Iron reacts very slowly with water, or not at all."),
             ("Transition metals are less dense than Group 1 metals.",
              "They are much denser. Sodium even floats on water."),
             ("Every metal forms just one ion.",
              "Many transition metals form ions with different charges, such as Fe²⁺ and "
              "Fe³⁺."),
         ]}]},
    ],
    "key_fact": "Compared with Group 1 metals, transition metals have higher melting points and "
                "densities, are stronger and harder, and are much less reactive with oxygen, water "
                "and halogens. Many transition elements have ions with different charges, form "
                "coloured compounds and are useful as catalysts.",
    "deeper": [
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Compare</strong>: say what each group does in the same sentence, such as "
             "\"iron has a higher melting point than sodium\".",
             "<strong>Describe</strong>: a typical property with a named example, such as copper(II) "
             "compounds are blue.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-11", "logic_edits": LOGIC_EDITS},
}
