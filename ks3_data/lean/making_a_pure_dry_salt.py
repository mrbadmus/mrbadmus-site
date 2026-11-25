# -*- coding: utf-8 -*-
"""Making a pure dry salt, in the lean shape. Spec table: docs/lessons/wave2/ks3-making-a-pure-dry-salt.md.

Rainford 19a (Salts) has no page of its own: naming salts, the word equations for all three
reactions of acids and the uses of salts are taught here, beside 19b (Making a salt).
"""

LESSON = {
    "slug": "making-a-pure-dry-salt",
    "start": {
        "setup": "You are making pure copper sulfate crystals from sulfuric acid and black copper "
                 "oxide powder. Copper oxide does not dissolve in water.",
        "question": "If you had to guess, how much black powder should you add to the acid: only "
                    "just enough, or slightly too much?",
        "options": [
            ("Only just enough",
             "You cannot see when the acid runs out. Any acid left over would end up in your crystals."),
            ("Slightly too much",
             "Right. The extra powder does not dissolve, so you filter it off. No acid is left."),
        ],
        "answer": 1,
    },
    "words": ["salt", "excess", "filtrate", "crystallise"],
    "word_defs": {
        "salt": "The compound made when a metal takes the place of the hydrogen in an acid.",
        "excess": "More than is needed, so some is left over at the end.",
        "filtrate": "The liquid that passes through the filter paper.",
        "crystallise": "To grow crystals by letting a concentrated solution cool slowly.",
    },
    "knowledge": [
        {"kind": "card", "title": "Naming a salt",
         "body": ["A salt's name has two parts.",
                  {"points": ["The first word is the metal, such as copper or sodium.",
                              "The second word comes from the acid."]},
                  "So copper oxide and sulfuric acid make copper sulfate."]},
        {"kind": "reveal", "title": "Which acid gives which salt",
         "cols": ["Salt name ends in", "Example"],
         "rows": [
             ("Hydrochloric acid", "chloride", "sodium chloride"),
             ("Sulfuric acid", "sulfate", "copper sulfate"),
             ("Nitric acid", "nitrate", "potassium nitrate"),
         ]},
        {"kind": "card", "title": "Naming from a metal compound",
         "body": ["The metal can come from the metal itself, or from its oxide, hydroxide or carbonate.",
                  "The metal's name still starts the salt's name.",
                  {"points": ["Magnesium oxide and nitric acid make magnesium nitrate.",
                              "Sodium hydroxide and hydrochloric acid make sodium chloride.",
                              "Calcium carbonate and sulfuric acid make calcium sulfate."]}]},
        {"kind": "reveal", "title": "The general equations",
         "cols": ["Products"],
         "rows": [
             ("alkali + acid", "salt + water"),
             ("metal oxide + acid", "salt + water"),
             ("metal + acid", "salt + hydrogen"),
             ("metal carbonate + acid", "salt + water + carbon dioxide"),
         ]},
        {"kind": "reveal", "title": "Word equations to practise",
         "cols": ["Products"],
         "rows": [
             ("sodium hydroxide + hydrochloric acid", "sodium chloride + water"),
             ("copper oxide + sulfuric acid", "copper sulfate + water"),
             ("zinc + sulfuric acid", "zinc sulfate + hydrogen"),
             ("calcium carbonate + nitric acid", "calcium nitrate + water + carbon dioxide"),
         ]},
        {"kind": "card", "title": "Uses of salts",
         "body": [{"points": ["Sodium chloride flavours food and grits icy roads.",
                              "Potassium nitrate is a fertiliser. It helps crops grow.",
                              "Copper sulfate kills fungi that attack crops.",
                              "Calcium sulfate is used as plaster for walls."]}]},
        {"kind": "card", "title": "Making copper sulfate crystals",
         "body": ["Copper oxide is a base. A base neutralises an acid.",
                  {"figure": "c6-word-copper-sulfate"},
                  {"figure": "c6-salt-steps"},
                  {"points": ["Warm some dilute sulfuric acid in a beaker.",
                              "Add copper oxide a spatula at a time, stirring.",
                              "Stop when black powder is left over. This is excess.",
                              "Filter to remove the extra copper oxide.",
                              "The blue filtrate is copper sulfate solution.",
                              "Heat the filtrate in an evaporating basin until about half the water has gone.",
                              "Leave it to cool slowly. Crystals form.",
                              "Pat the crystals dry with filter paper."]}]},
        {"kind": "card", "title": "Why add too much copper oxide",
         "body": ["You cannot see when the acid has all been used up.",
                  "So you add copper oxide until some is left over.",
                  "Then you know every drop of acid has reacted.",
                  "The extra copper oxide does not dissolve, so filtering removes it.",
                  "Leftover acid could not be filtered out. It would stay in your salt."]},
        {"kind": "card", "title": "Why cool slowly",
         "body": ["Heating boils off some of the water, so the solution becomes concentrated.",
                  "As it cools slowly, the salt comes out as large crystals.",
                  "Boiling it until it is dry gives a powder of tiny crystals instead."]},
        {"kind": "card", "title": "Using an alkali instead",
         "body": ["Sodium hydroxide is an alkali. It dissolves in water.",
                  "So extra sodium hydroxide cannot be filtered off.",
                  "You must add just enough to neutralise the acid.",
                  "But you cannot see when enough alkali has gone in.",
                  {"points": ["Use an indicator to find the volume of alkali that neutralises the acid.",
                              "Mix the same volumes again, with no indicator.",
                              "Evaporate some water and leave it to cool slowly, as before."]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Boiling the solution dry gives the best crystals.",
              "Boiling dry gives a powder. Cooling slowly grows large crystals.",
              "ACID-09"),
             ("Sulfuric acid makes chlorides.",
              "Sulfuric acid makes sulfates. Hydrochloric acid makes chlorides."),
             ("The acid's name comes first in a salt's name.",
              "The metal comes first, as in copper sulfate."),
             ("Copper oxide dissolves in water.",
              "Copper oxide does not dissolve. That is why the extra can be filtered off."),
         ]}]},
    ],
    "key_fact": "A salt is named from its metal and its acid. Hydrochloric acid makes chlorides, "
                "sulfuric acid makes sulfates and nitric acid makes nitrates. For a pure, dry salt, "
                "add an insoluble base, such as copper oxide, in excess. Filter it, then "
                "evaporate some water and let the solution cool slowly.",
    "deeper": [
        {"kind": "card", "title": "When to stop heating",
         "body": ["Dip a cold glass rod into the hot solution, then lift it out.",
                  "If small crystals form on the rod, stop heating.",
                  "The solution is now concentrated enough to crystallise as it cools."]},
        {"kind": "card", "title": "A salt you can name but not make this way",
         "body": ["Calcium carbonate and sulfuric acid make calcium sulfate.",
                  "Calcium sulfate dissolves only a little. It coats the chips and stops the reaction.",
                  "So this method does not work for calcium sulfate."]},
        {"kind": "card", "title": "Writing a method",
         "body": ["Write a method as numbered steps, in the order you do them.",
                  "Each step says what to do and what equipment to use.",
                  "Give amounts where they matter, such as a volume of acid.",
                  "Say why a step matters, such as why you add excess."]},
    ],
    "try": None,
    "tutor_body": "Want to practise naming salts and writing their word equations?",
    "safety_note": "Wear eye protection. Copper compounds are harmful if swallowed, so never taste "
                   "the crystals. Do not boil the solution dry, as it can spit. Let the evaporating "
                   "basin cool before you touch it.",
    # the classic heading "Next in this unit" named lessons that are not next (Unit 3 walk)
    "connects_heading": None,
    "ks4_becomes": "Making a pure, dry soluble salt as a required practical. Writing the formulae "
                   "of salts.",
    "figures": [
        {"id": "c6-word-copper-sulfate", "kind": "diagram", "status": "drawn", "art": "word-equation",
         "title": "The word equation for making copper sulfate",
         "desc": "Copper oxide plus sulfuric acid at the top, labelled reactants. A drawn arrow "
                 "points down to copper sulfate plus water, labelled products.",
         "caption": "Copper oxide neutralises sulfuric acid, making copper sulfate and water.",
         "eq": {"left": ["copper oxide", "sulfuric acid"], "right": ["copper sulfate", "water"]}},
        {"id": "c6-salt-steps", "kind": "diagram", "status": "drawn", "art": "c6-salt-steps",
         "title": "Making copper sulfate crystals in four steps",
         "desc": "Four steps, one under another. Step 1, Excess: a beaker of blue solution, a glass "
                 "rod stirring, a spatula tipping in black powder, and black powder left on the "
                 "bottom. Step 2, Filter: a filter funnel over a conical flask. Black powder stays "
                 "on the filter paper and blue filtrate collects in the flask. Step 3, Evaporate: "
                 "an evaporating basin of blue solution on a gauze and tripod over a flame, with "
                 "steam rising. Step 4, Crystallise: the basin cooling on the bench, with blue "
                 "crystals in it.",
         "caption": "Excess, filter, evaporate, then cool slowly.",
         "data": {
             "colours": {"solution": "#4A86C8", "crystal": "#2F69B5", "powder": "#2B2622",
                         "paper": "#F7F4EE"},
             "steps": [
                 {"title": "Excess", "lines": ["Add copper oxide to", "warm acid, stirring.",
                                               "Stop when black", "powder is left over."]},
                 {"title": "Filter", "lines": ["The extra copper", "oxide stays on the",
                                               "paper. Blue solution", "passes through."]},
                 {"title": "Evaporate", "lines": ["Heat until about half", "the water has gone.",
                                                  "Do not boil it dry."]},
                 {"title": "Crystallise", "lines": ["Leave it to cool", "slowly. Crystals",
                                                    "grow. Pat them dry."]},
             ]}},
    ],
    "ladder_stem": {
        "explain": "You have sulfuric acid and magnesium oxide. Describe how you would make pure, "
                   "dry magnesium sulfate crystals. Explain why each step is needed.",
        "produce": "A student wants sodium chloride crystals from hydrochloric acid and sodium "
                   "hydroxide. Explain why the copper sulfate method will not work. Say what they "
                   "must do instead.",
    },
    "ladder_feedback": {
        "recall": {
            0: "Sulfates come from sulfuric acid. Nitric acid makes nitrates.",
            1: "Chlorides come from hydrochloric acid. Nitric acid makes nitrates.",
            3: "Magnesium hydroxide is a base. The salt's ending comes from nitric acid.",
        },
        "apply": {
            0: "Once the acid is used up, extra copper oxide makes no more salt.",
            1: "Copper oxide does not dissolve. That is why the extra can be filtered off.",
            2: "Copper oxide is a reactant, so it gets used up. The extra is left over.",
        },
    },
}
