# -*- coding: utf-8 -*-
"""Compounds, in the lean shape. Spec table: docs/lessons/wave1/ks3-compounds.md."""

LESSON = {
    "slug": "compounds",
    "start": {
        "setup": "Iron and sulfur are heated together, and afterwards a magnet picks up nothing.",
        "question": "If you had to guess, has the iron burnt away, or joined the sulfur?",
        "options": [
            ("It burnt away to nothing", "It joined the sulfur. The iron is still there, joined to sulfur in a new substance."),
            ("It joined the sulfur", "It joined the sulfur. The iron is still there, joined to sulfur in a new substance."),
        ],
        "answer": 1,
    },
    "words": ["compound", "mixture", "chemical reaction", "property"],
    "word_defs": {
        "compound": "Two or more elements chemically joined together.",
        "mixture": "Two or more substances mixed together, not chemically joined.",
        "chemical reaction": "A change that rearranges atoms to make new substances.",
        "property": "What a substance is like or does, such as its colour or magnetism.",
    },
    "knowledge": [
        {"kind": "card", "title": "What a compound is",
         "body": ["A compound is two or more elements chemically joined together.",
                  "The atoms are joined in a fixed ratio.",
                  "Water is always two hydrogen atoms joined to one oxygen atom.",
                  "A compound is made by a chemical reaction."]},
        {"kind": "card", "title": "Iron and sulfur",
         "body": ["Stir iron and sulfur together and you get a mixture.",
                  "A magnet pulls the iron out of the mixture.",
                  "Heat the mixture and it glows as the iron and sulfur react.",
                  "They make a new compound, iron sulfide.",
                  "A magnet cannot pull iron out of iron sulfide. The iron is chemically joined to sulfur.",
                  {"figure": "c2-iron-sulfur"}]},
        {"kind": "reveal", "title": "Telling the mixture from the compound",
         "cols": ["Iron and sulfur mixed", "Iron sulfide"],
         "rows": [
             ("Hold a magnet over it", "The iron is pulled out", "Nothing is pulled out"),
             ("Add dilute acid", "Hydrogen, which burns with a squeaky pop",
              "Hydrogen sulfide, which smells of rotten eggs"),
             ("How much of each", "Any amounts", "Always 7 g of iron to 4 g of sulfur"),
             ("How it looks", "Grey specks and yellow powder", "A grey-black solid, the same all through"),
         ]},
        {"kind": "card", "title": "A fixed ratio",
         "body": ["Iron and sulfur always react in the ratio 7 g to 4 g.",
                  "Heat 14 g of iron with 4 g of sulfur.",
                  "Only 7 g of the iron reacts. The other 7 g of iron is left over.",
                  "A mixture can have any amounts. A compound cannot."]},
        {"kind": "reveal", "title": "Mixtures and compounds",
         "cols": ["Mixture", "Compound"],
         "rows": [
             ("Joined", "No. Each substance stays as it was.", "Yes. The elements are chemically joined."),
             ("Amounts", "Any amounts", "A fixed ratio"),
             ("Properties", "Each part keeps its own properties", "New properties, unlike its elements"),
             ("Separating", "By a physical method, such as a magnet or filtering", "Only by a chemical reaction"),
             ("How it is made", "By mixing", "By a chemical reaction"),
         ]},
        {"kind": "card", "title": "Element, compound or mixture",
         "body": ["In a particle diagram, look at the kinds of atom and what is joined.",
                  {"points": ["Element: only one kind of atom.",
                              "Compound: atoms of different elements joined, the same in every particle.",
                              "Mixture: two or more substances, not joined to each other."]},
                  {"figure": "c2-ecm-particles"}]},
        {"kind": "card", "title": "New properties",
         "body": ["A compound behaves like neither of its elements.",
                  "Sodium is a metal that reacts violently with water.",
                  "Chlorine is a poisonous green gas.",
                  "Joined, they make sodium chloride. That is the salt on your chips."]},
        {"kind": "card", "title": "Hydrogen, oxygen and water",
         "body": ["A mixture of hydrogen and oxygen can explode with a spark.",
                  "The reaction joins the atoms to make water.",
                  "Water puts out fires. It behaves like neither gas.",
                  "Passing electricity through water splits it back into hydrogen and oxygen.",
                  "The atoms stay the same throughout. Only what they are joined to changes."]},
        {"kind": "card", "title": "Naming compounds",
         "body": ["A compound of two elements is named after both.",
                  "If there is a metal, its name comes first.",
                  "The ending of the non-metal changes to -ide:",
                  {"points": ["oxygen becomes oxide, as in magnesium oxide",
                              "chlorine becomes chloride, as in sodium chloride",
                              "sulfur becomes sulfide, as in iron sulfide"]},
                  "An -ate ending means oxygen is in it too.",
                  "Copper sulfate is copper, sulfur and oxygen.",
                  "Calcium carbonate is calcium, carbon and oxygen."]},
        {"kind": "reveal", "title": "Name the compound",
         "cols": ["Compound"],
         "rows": [
             ("Iron and sulfur", "Iron sulfide"),
             ("Sodium and chlorine", "Sodium chloride"),
             ("Magnesium and oxygen", "Magnesium oxide"),
             ("Zinc and oxygen", "Zinc oxide"),
             ("Copper and chlorine", "Copper chloride"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A compound is a very well stirred mixture.",
              "In a compound the atoms are chemically joined. Stirring never joins them."),
             ("The iron is still in iron sulfide, so it is still magnetic.",
              "The iron is chemically joined to sulfur. The new substance is not iron."),
             ("Any substance with more than one atom is a compound.",
              "The atoms must be of different elements. Oxygen gas is an element."),
         ]}]},
    ],
    "key_fact": "A compound is two or more elements chemically joined in a fixed ratio. It has new "
                "properties, unlike its elements. A mixture is not joined, so it can be separated without a chemical reaction.",
    "deeper": [
        {"kind": "card", "title": "Mixture or compound",
         "body": ["Sea water is a mixture. Its saltiness varies from place to place.",
                  "Steel is a mixture. Steelmakers choose how much carbon to add.",
                  "Carbon dioxide is a compound. It is always one carbon atom to two oxygen atoms."]},
    ],
    "try": None,
    "ks4_becomes": "Bonding: what holds the atoms of a compound together, and why it changes the substance.",
    "ladder_stem": {
        "apply": "Iron and sulfur react in a fixed ratio of 7 g to 4 g. A student heats 7 g of iron "
                 "with 8 g of sulfur in a tube. What is in the tube at the end, and how much of each?",
        "explain": "A tube holds either iron and sulfur mixed, or iron sulfide. Describe two "
                   "tests to tell which. Say what each test shows for each one.",
        "produce": "A mixture of hydrogen and oxygen can explode with a spark. Water is made of the same "
                   "two elements. Yet water puts out fires. Explain how both can be true. Say how a "
                   "chemist could turn each into the other.",
    },
    "ladder_ticks": [
        ["Names a magnet, and says the iron would be pulled out of the mixture and nothing would move for "
         "the compound.",
         "Names a magnet. It pulls iron out of the mixture, and nothing out of iron sulfide."],
        ["Names a second test — dilute acid, or weighing what reacts — and says what each would show.",
         "Names a second test, such as dilute acid, and says what each would show."],
        ["Says a chemical reaction — a spark — is what joins them, and that electricity can split water back.",
         "Says a spark makes them react and join. Electricity can split water back."],
    ],
    "figures": [
        {"id": "c2-iron-sulfur", "kind": "diagram", "status": "drawn",
         "art": "particle-boxes",
         "title": "Iron and sulfur, mixed and joined",
         "desc": "Two boxes side by side. The left box, labelled Iron and sulfur mixed, holds small "
                 "separate clumps of grey circles marked Fe and of yellow circles marked S, not touching "
                 "each other. The right box, labelled Iron sulfide, is one block of touching circles in "
                 "rows, grey Fe and yellow S taking turns, one of each.",
         "caption": "Mixed, iron and sulfur are separate. In iron sulfide, they are joined.",
         "data": {"boxes": [
             {"label": "Iron and sulfur mixed", "tag": "mixture", "layout": "clumps",
              "clumps": [["Fe"] * 4, ["S"] * 4, ["Fe"] * 3, ["S"] * 5, ["Fe"] * 4]},
             {"label": "Iron sulfide", "tag": "compound", "layout": "grid", "rows": 4, "cols": 6,
              "atoms": ["Fe", "S"], "pattern": "alternate"},
         ]}},
        {"id": "c2-ecm-particles", "kind": "diagram", "status": "drawn",
         "art": "particle-boxes",
         "title": "Elements, a compound and two mixtures",
         "desc": "Five boxes in a row. Box one, labelled Element: helium, holds eight separate identical "
                 "circles marked He. Box two, labelled Element: nitrogen, holds five separate pairs of "
                 "joined blue circles marked N. Box three, labelled Compound: carbon dioxide, holds five "
                 "separate groups, each a black C circle joined between two red O circles. Box four, "
                 "labelled Mixture: nitrogen and oxygen, holds four joined N pairs and two joined O "
                 "pairs, not joined to each other. Box five, labelled Mixture: oxygen and carbon dioxide, "
                 "holds three joined O pairs and three O-C-O groups, not joined to each other.",
         "caption": "Look at the kinds of atom, and which ones are joined.",
         "data": {"boxes": [
             {"label": "Element: helium", "layout": "spread", "groups": [["He"]] * 8},
             {"label": "Element: nitrogen", "layout": "spread", "groups": [["N", "N"]] * 5},
             {"label": "Compound: carbon dioxide", "layout": "spread", "groups": [["O", "C", "O"]] * 5},
             {"label": "Mixture: nitrogen and oxygen", "layout": "spread",
              "groups": [["N", "N"]] * 4 + [["O", "O"]] * 2},
             {"label": "Mixture: oxygen and carbon dioxide", "layout": "spread",
              "groups": [["O", "O"]] * 3 + [["O", "C", "O"]] * 3},
         ]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "In a mixture nothing is joined. In a compound the elements are chemically joined.",
            2: "The atoms must be of different elements. Oxygen gas has joined atoms, and is an element.",
            3: "That is closer to an element. A chemical reaction can break a compound down.",
        },
        "apply": {
            0: "The ratio in a compound is fixed. Extra sulfur has no iron left to join.",
            1: "The iron runs out. More sulfur cannot make more iron sulfide.",
            2: "The 7 g of iron still reacts with 4 g of sulfur. The other 4 g is left over.",
        },
    },
}
