# -*- coding: utf-8 -*-
"""Atoms, elements and compounds, in the lean shape. Spec table: ks4-atoms-elements-compounds.md
(AQA 8464 5.1.1.1 / 8462 4.1.1.1, word for word the same). One HT-only line (balanced half
equations and ionic equations) is taught on the Higher routes only (card gated CH, TH).

LEGACY (batch 2). The ladder (Ks4Ladder, four rungs) and the practice set stay from the Design page.
The practice set is the route's subtopic `quiz` list (K.bank) and Rung 1 is K.find with the needle
'Which of these is a mixture' (falling back to 'key difference between a compound and a mixture'),
so the practice-set fixes are quiz-data edits in all_subtopics_chemistry*.py (all four routes carry
the same items; patches/_subtopic_edits_a.json), not here. Both needles survive unchanged. The
eyebrow is bound per route by the page's own logic (specRef 5.1.1.1 / 4.1.1.1).

logic_edits:
  1. Rung 3 (air is a mixture): links 2 and 3 both followed from link 1, so the chain had two
     valid orders. Link 2 now names the property (each gas's own boiling point) and link 3 uses it,
     so there is one order.
"""

LOGIC_EDITS = [
    ("links: ['The gases in air are not chemically combined with each other.', "
     "'So each gas keeps its own chemical properties, and their proportions can vary.', "
     "'So the gases can be separated by a physical process, such as fractional distillation, "
     "without a chemical reaction.'],",
     "links: ['The gases in air are not chemically combined with each other.', "
     "'So each gas keeps its own properties, including its own boiling point.', "
     "'So the gases can be separated using those different boiling points, by a physical process "
     "with no chemical reaction.'],"),
    # Coordinator's ruling (26 Nov): Rung 4 said "a black solid" and practice item ks4q:...:bab5f37818 says
    # "a grey solid". The practice stem keeps its id, so Rung 4 matches it (rung ids are positional).
    ("The product is a black solid that is not attracted to a magnet",
     "The product is a grey solid that is not attracted to a magnet"),
    # Blind flag B4 (26 Nov): Rung 1 (K.find of the quiz item "Which of these is a mixture?") repeated
    # practice-set item ks4q:atoms-elements-compounds:96647f7b07 word for word. The practice stem keeps its
    # id; Rung 1 (id #r1, positional) asks the same point with different substances. Sea water is not
    # in Rung 3's chain (air), so neither rung gives the other away.
    ("r1: Object.assign(K.find(slug, R.route, 'Which of these is a mixture') || K.find(slug, R.route, 'key difference between a compound and a mixture') || { options: [] }, { command: 'Identify', marks: 1, why: 'Bronze is copper and tin mixed, not chemically combined. Water, sodium chloride and carbon dioxide are all compounds.' }),",
     "r1: { command: 'Identify', marks: 1, prompt: 'Identify which of these substances is a mixture.', "
     "why: 'Sea water is water with salts dissolved in it. They are not chemically combined. The other three are compounds.', "
     "options: [{ text: 'Pure water', correct: false, reply: 'Pure water is one compound, H\\u2082O, with nothing else in it.' }, "
     "{ text: 'Sea water', correct: true, reply: '' }, "
     "{ text: 'Carbon dioxide', correct: false, reply: 'Carbon dioxide is a compound of carbon and oxygen, chemically combined.' }, "
     "{ text: 'Magnesium oxide', correct: false, reply: 'Magnesium oxide is a compound of magnesium and oxygen, chemically combined.' }] },"),
]

LESSON = {
    "slug": "atoms-elements-compounds",
    "start": {
        "setup": "Sodium is a metal that reacts with water. Chlorine is a toxic gas. Together they "
                 "make table salt.",
        "question": "If you had to guess, are the sodium and chlorine in salt just mixed together, "
                    "or joined into something new?",
        "options": [
            ("Just mixed together",
             "They are chemically combined into a new substance, sodium chloride. It is safe to "
             "eat, unlike sodium or chlorine."),
            ("Joined into something new",
             "They are chemically combined into a new substance, sodium chloride. It is safe to "
             "eat, unlike sodium or chlorine."),
        ],
        "answer": 1,
    },
    "words": ["element", "compound", "formula", "balanced equation"],
    "knowledge": [
        {"kind": "card", "title": "Atoms and elements",
         "body": ["All substances are made of atoms. An atom is the smallest part of an element that "
                  "can exist.",
                  "An element contains only one type of atom. There are about 100 different "
                  "elements, and they are shown in the periodic table.",
                  "Atoms of each element are represented by a chemical symbol: O represents an atom "
                  "of oxygen, Na represents an atom of sodium, Fe represents an atom of iron."]},
        {"kind": "card", "title": "Compounds",
         "body": ["Compounds are formed from elements by chemical reactions.",
                  "A compound contains two or more elements chemically combined in fixed "
                  "proportions. Water, H₂O, always has two hydrogen atoms for every oxygen atom.",
                  "A compound has different properties from the elements it was made from.",
                  "A compound can only be separated into its elements by chemical reactions."]},
        {"kind": "card", "title": "Chemical reactions",
         "body": ["A chemical reaction always makes one or more new substances.",
                  "It often involves a detectable energy change, such as the mixture getting hot."]},
        {"kind": "card", "title": "Element, compound or mixture",
         "body": [{"slot": "fig:aec-particle-boxes"},
                  {"points": [
                      "Element: only one type of atom. Two atoms of the same element joined together, "
                      "such as O₂, are still an element.",
                      "Compound: two or more elements chemically combined, in the same fixed ratio "
                      "all the way through.",
                      "Mixture: two or more elements or compounds that are not chemically combined.",
                  ]}]},
        {"kind": "reveal", "title": "Compound and mixture compared",
         "cols": ["Compound", "Mixture"],
         "rows": [
             ("Chemically combined", "Yes", "No"),
             ("Proportions", "Fixed", "Can vary"),
             ("Properties", "Different from its elements", "Each substance keeps its own"),
             ("Separated by", "Chemical reactions only", "Physical processes, such as filtration"),
             ("Example", "Water, H₂O", "Air"),
         ]},
        {"kind": "card", "title": "Formulae",
         "body": ["A formula shows the symbols of the elements in a compound and the number of atoms "
                  "of each. The small number counts the atom just before it.",
                  {"points": [
                      "H₂O: 2 hydrogen atoms and 1 oxygen atom.",
                      "CO₂: 1 carbon atom and 2 oxygen atoms.",
                      "H₂SO₄: 2 hydrogen atoms, 1 sulfur atom and 4 oxygen atoms.",
                  ]}]},
        {"kind": "card", "title": "Naming compounds",
         "body": [{"points": [
             "A metal with one non-metal: the non-metal ending changes to -ide. NaCl is sodium "
             "chloride, MgO is magnesium oxide.",
             "A name ending in -ate means oxygen is in the compound too. CaCO₃ is calcium carbonate.",
             "Two non-metals: CO₂ is carbon dioxide (di means two).",
         ]}]},
        {"kind": "card", "title": "Word and symbol equations",
         "body": ["Chemical reactions can be represented by word equations or by equations using "
                  "symbols and formulae.",
                  {"points": [
                      "Word equation: sodium + chlorine → sodium chloride",
                      "Symbol equation: 2Na + Cl₂ → 2NaCl",
                  ]},
                  "Atoms are not made or destroyed in a reaction. So a balanced equation has the "
                  "same number of each type of atom on both sides."]},
        {"kind": "card", "title": "Balancing an equation",
         "body": ["Hydrogen + oxygen → water.",
                  {"points": [
                      "Step 1: H₂ + O₂ → H₂O. Left: 2 H and 2 O. Right: 2 H and 1 O. Oxygen does "
                      "not balance.",
                      "Step 2: H₂ + O₂ → 2H₂O. Right: 4 H and 2 O. Now hydrogen does not balance.",
                      "Step 3: 2H₂ + O₂ → 2H₂O. 4 H and 2 O on each side. Balanced.",
                  ]},
                  {"slot": "fig:aec-balance-water"},
                  "Only change the big numbers in front of a formula. Never change a formula."]},
        {"kind": "card", "title": "Half equations and ionic equations (Higher)", "routes": ["CH", "TH"],
         "body": ["An ionic equation shows only the ions and molecules that change. Chlorine with "
                  "potassium bromide solution:",
                  {"points": ["Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂ (the potassium ions do not change, so they "
                              "are left out)"]},
                  "A half equation shows electrons being lost or gained:",
                  {"points": ["Na → Na⁺ + e⁻", "Cl₂ + 2e⁻ → 2Cl⁻"]},
                  "Both kinds must balance for atoms and for charge. In the ionic equation above, "
                  "the charge is 2− on each side."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("O₂ is a compound because it has two atoms.",
              "O₂ is an element. A compound needs two or more different elements."),
             ("H₂ + O₂ → H₂O₂ balances the equation for water.",
              "H₂O₂ is a different substance. Put numbers in front: 2H₂ + O₂ → 2H₂O."),
             ("Bronze, a metal with a metal, is a compound.",
              "Bronze is copper and tin, not chemically combined. An alloy is a mixture."),
             ("A compound can be separated by filtering or distilling.",
              "Only a chemical reaction separates a compound into its elements."),
         ]}]},
    ],
    "key_fact": "A compound contains two or more elements chemically combined in fixed proportions, "
                "and it can only be separated into its elements by a chemical reaction. A balanced "
                "equation has the same number of each type of atom on both sides, because atoms "
                "are not made or destroyed in a reaction.",
    "deeper": [
        {"kind": "card", "title": "How many elements",
         "body": ["About 100 elements is the number to learn. 118 are known today, but some have only ever "
                  "been made in a laboratory, a few atoms at a time."]},
        {"kind": "card", "title": "Symbols you need",
         "body": ["Learn the names and symbols of the first 20 elements and the elements in Groups 1 "
                  "and 7. Some symbols come from Latin names: Na (sodium), K (potassium), Fe (iron), "
                  "Cu (copper)."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Identify</strong>: pick out the answer from a diagram, a formula or a list.",
             "<strong>Complete</strong>: fill the gaps, such as the numbers that balance an "
             "equation.",
             "<strong>Explain</strong>: give the reason, such as chemically combined or not, "
             "fixed proportions or not.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
