# -*- coding: utf-8 -*-
"""Group 1, in the lean shape. Spec table: ks4-group-1.md (AQA 8464 5.1.2.5 / 8462 4.1.2.5, word for
word the same; no HT-only or chemistry-only lines).

LEGACY (batch 6). The ladder and the practice set (the page's own bankSrc) stay from the Design page;
their fixes are logic_edits. Every practice stem is kept. Batch-6 logic writes \\u escapes.

Every symbol equation on the page balances (atoms counted each side):
  2M + 2H2O -> 2MOH + H2   M 2 = 2, H 4 = 2 + 2, O 2 = 2        (M = Li, Na, K)
  4M + O2   -> 2M2O        M 4 = 4, O 2 = 2
  2M + Cl2  -> 2MCl        M 2 = 2, Cl 2 = 2
Melting points (degC): Li 181, Na 98, K 63, Rb 39. Boiling points in Rung 2: Li 1342, Na 883,
K 759, Rb 688 (data-book values; the Design page's own).

logic_edits (option text and feedback; every credited answer is the same answer):
  1. Practice Q1 (sodium and water): credited option the longest. Now "Sodium hydroxide and
     hydrogen" (29); feedback plain, no capitals.
  2. Practice Q2 (potassium more reactive than lithium): credited option 104 characters with a
     dash. Now "Its outer electron is further from the nucleus" (46); distractors keep their
     misconceptions (more protons, surface area, bigger charge), without dashes.
  3. Practice Q3 (sodium in chlorine): credited option the longest by 4; one distractor longer.
  4. Practice Q4 (lithium goes dull): credited option the longest (49); distractor "reacts with
     nitrogen to form a hydroxide" was garbled chemistry (lithium does react with nitrogen, to a
     nitride). Distractors are now plain misconceptions (dries out, cools down, oil evaporates).
  5. Rung 2 Q1 (sodium in water): credited option 58 against 38. Shortened to 41; one distractor
     written out longer.
"""

LOGIC_EDITS = [
    # 1. Practice Q1
    ("opts: [['Sodium hydroxide (NaOH) and hydrogen gas (H\\u2082)', true],",
     "opts: [['Sodium hydroxide and hydrogen', true],"),
    ("wrong_explanations: { 1: 'Sodium reacts with oxygen to form sodium OXIDE \\u2014 but when it reacts with water specifically, the products are hydroxide and hydrogen.', 2: 'NaCl is the product of sodium reacting with CHLORINE or hydrochloric acid \\u2014 not water.', 3: 'Oxygen is not released when metals react with water. The equation is: 2Na + 2H\\u2082O \\u2192 2NaOH + H\\u2082.' } },",
     "wrong_explanations: { 1: 'Sodium oxide forms with oxygen. With water, the products are sodium hydroxide and hydrogen.', 2: 'Sodium chloride forms with chlorine, not with water.', 3: 'No oxygen is given off: 2Na + 2H\\u2082O \\u2192 2NaOH + H\\u2082.' } },"),
    # 2. Practice Q2
    ("opts: [['Potassium has more electron shells \\u2014 its outer electron is further from the nucleus and more easily lost', true], ['Potassium has more protons \\u2014 so it has a stronger positive charge making it more reactive', false], ['Potassium is a larger atom so it reacts with a larger surface area', false], ['Potassium\\u2019s outer electron has a higher charge than lithium\\u2019s outer electron', false]],",
     "opts: [['Its outer electron is further from the nucleus', true], ['It has more protons, so it has a stronger positive charge', false], ['It is a larger atom, so it has a larger surface area', false], ['Its outer electron has a bigger charge than lithium\\u2019s', false]],"),
    ("wrong_explanations: { 1: 'More protons means stronger nuclear charge \\u2014 this would actually make it HARDER to lose the electron, not easier. But the extra shells and increased distance outweigh the effect of more protons.', 2: 'Surface area affects reaction rate but not inherent reactivity \\u2014 the question is about why K is more reactive than Li in terms of properties.', 3: 'All electrons have the same charge (\\u22121 each) \\u2014 the \\u2018ease of losing\\u2019 them depends on how strongly they are attracted to the nucleus.' } },",
     "wrong_explanations: { 1: 'More protons alone would hold the electron more tightly. The outer electron is much further away, so it is held less strongly.', 2: 'Reactivity here is about how easily the outer electron is lost, not surface area.', 3: 'Every electron has the same charge. What changes is how strongly it is attracted to the nucleus.' } },"),
    # 3. Practice Q3
    ("['A colourless gas, hydrogen', false],",
     "['A colourless gas, which is hydrogen', false],"),
    # 4. Practice Q4
    ("opts: [['It reacts with oxygen in the air to form an oxide', true], ['It dries out', false], ['It reacts with nitrogen to form a hydroxide', false], ['The oil on it evaporates', false]],",
     "opts: [['It reacts with oxygen in the air', true], ['The air dries out its shiny surface', false], ['It cools down after being cut', false], ['The oil left on it evaporates away', false]],"),
    ("wrong_explanations: { 1: 'Metals don\\u2019t dry out; the surface is reacting.', 2: 'A hydroxide forms with water. The dull layer is an oxide.', 3: 'The dulling is a reaction with oxygen.' } },",
     "wrong_explanations: { 1: 'Metals do not dry out. The surface is reacting with oxygen to form an oxide.', 2: 'Cooling does not make it dull. The surface is reacting with oxygen to form an oxide.', 3: 'The dull layer is lithium oxide, made by a reaction with oxygen.' } },"),
    # 5. Rung 2 Q1
    ("{ text: 'Fizzes, melts into a ball and moves rapidly on the surface', correct: true },\n            { text: 'Sinks and fizzes slowly at the bottom', correct: false,",
     "{ text: 'Fizzes, melts into a ball and moves about', correct: true },\n            { text: 'Sinks and fizzes slowly at the bottom of the water', correct: false,"),
]

LESSON = {
    "slug": "group-1",
    "start": {
        "setup": "Sodium is kept in a jar of oil.",
        "question": "If you had to guess, why is it kept under oil?",
        "options": [
            ("To stop it reacting with air and water",
             "Yes. Sodium reacts quickly with oxygen and with water, and the oil keeps both away."),
            ("To keep it shiny for show",
             "It does stay shiny, but that is a side effect. The oil stops it reacting with oxygen "
             "and with water."),
        ],
        "answer": 0,
    },
    "words": ["alkali metals", "outer electron", "reactivity", "hydroxide"],
    "knowledge": [
        {"kind": "card", "title": "The alkali metals",
         "body": [{"slot": "fig:alkali-shells"},
                  "The elements in Group 1 are known as the alkali metals. They have characteristic "
                  "properties because of the single electron in their outer shell.",
                  "When they react, they lose this electron and form ions with a 1+ charge, such "
                  "as Na⁺."]},
        {"kind": "card", "title": "With water",
         "body": ["The alkali metals react with water to form a metal hydroxide and hydrogen. The "
                  "hydroxide dissolves to make an alkaline solution, which is where the name "
                  "comes from.",
                  {"points": [
                      "sodium + water → sodium hydroxide + hydrogen",
                      "2Li + 2H₂O → 2LiOH + H₂",
                      "2Na + 2H₂O → 2NaOH + H₂",
                      "2K + 2H₂O → 2KOH + H₂",
                  ]}]},
        {"kind": "reveal", "title": "What you see in water",
         "cols": ["Lithium", "Sodium", "Potas\u00adsium"],
         "rows": [
             ("Floats", "Yes", "Yes", "Yes"),
             ("Fizzing", "Gentle", "Vig\u00ador\u00adous", "Very vigorous"),
             ("Also", "Moves around on the surface", "Melts into a ball and moves quickly",
              "The hydrogen ignites, with a lilac flame"),
         ]},
        {"kind": "card", "title": "With oxygen and chlorine",
         "body": [{"points": [
             "A freshly cut surface is shiny, then quickly goes dull as an oxide forms. "
             "sodium + oxygen → sodium oxide: 4Na + O₂ → 2Na₂O. Lithium and potassium are the same: "
             "4Li + O₂ → 2Li₂O, 4K + O₂ → 2K₂O.",
             "Heated in chlorine, they react vigorously to form white solid chlorides. "
             "sodium + chlorine → sodium chloride: 2Na + Cl₂ → 2NaCl. Also 2Li + Cl₂ → 2LiCl and "
             "2K + Cl₂ → 2KCl.",
             "Both reactions get more vigorous going down the group.",
         ]}]},
        {"kind": "card", "title": "Why reactivity increases down the group",
         "body": ["Going down the group, the atoms have more shells, so the outer electron is "
                  "further from the nucleus. It is less strongly attracted, so it is lost more "
                  "easily. The further down the group, the more reactive the metal."]},
        {"kind": "card", "title": "Predicting from a trend",
         "body": ["Melting points: lithium 181 °C, sodium 98 °C, potassium 63 °C. The values fall "
                  "down the group, so predict that rubidium melts below 63 °C. It melts at 39 °C.",
                  "Rubidium and caesium react with water even more vigorously than potassium."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Potassium has more protons, so it holds its outer electron more tightly.",
              "Its outer electron is further from the nucleus, so it is held less tightly."),
             ("The gas given off with water is oxygen.",
              "It is hydrogen. The other product is a metal hydroxide."),
             ("Group 1 gets less reactive going down, like Group 7.",
              "Group 1 metals get more reactive going down the group."),
         ]}]},
    ],
    "key_fact": "The alkali metals have one electron in their outer shell. They react with water to "
                "form a metal hydroxide and hydrogen, with oxygen to form an oxide and with chlorine "
                "to form a chloride. Reactivity increases down the group, because the outer electron "
                "is further from the nucleus and is lost more easily.",
    "deeper": [
        {"kind": "card", "title": "Physical properties",
         "body": ["The alkali metals are soft enough to cut with a knife and have low melting points. "
                  "Lithium, sodium and potassium are less dense than water, so they float."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: what you would see: fizzing, moving, melting, a flame.",
             "<strong>Explain</strong>: distance from the nucleus, attraction, how easily the "
             "electron is lost.",
             "<strong>Predict</strong>: carry the trend on to rubidium and caesium.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": LOGIC_EDITS},
}
