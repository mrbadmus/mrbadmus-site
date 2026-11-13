# -*- coding: utf-8 -*-
"""Conservation of mass, in the lean shape. Spec table: docs/lessons/wave1/ks3-conservation-of-mass.md."""

LESSON = {
    "slug": "conservation-of-mass",
    "start": {
        "setup": "A candle burns all night. By morning, the wax has gone.",
        "question": "If you had to guess, where did the wax go?",
        "options": [
            ("Into gas in the air", "Into gas in the air. The wax reacts with oxygen and leaves as invisible gases."),
            ("Into heat and light", "Into gas in the air. The wax reacts with oxygen and leaves as invisible gases."),
        ],
        "answer": 0,
    },
    "words": ["conservation of mass", "reactant", "product", "closed system"],
    "word_defs": {
        "conservation of mass": "The total mass before a reaction equals the total mass after it.",
        "reactant": "A substance you start with in a reaction.",
        "product": "A substance a reaction makes.",
        "closed system": "A sealed container. No substance can get in or out.",
    },
    "knowledge": [
        {"kind": "card", "title": "Atoms are rearranged",
         "body": ["In a chemical reaction, atoms are rearranged into new substances.",
                  "No atoms are made or destroyed.",
                  "So the total mass stays the same.",
                  {"figure": "c2-carbon-burns"}]},
        {"kind": "card", "title": "Conservation of mass",
         "body": ["The total mass of the reactants equals the total mass of the products.",
                  "This is called conservation of mass. It is true for every chemical reaction.",
                  "It is also true when a substance changes state.",
                  "50 g of ice melts to make 50 g of water."]},
        {"kind": "card", "title": "A worked example",
         "body": [{"figure": "c2-word-magnesium"},
                  "2.40 g of magnesium burns in air. It makes 4.00 g of magnesium oxide.",
                  {"points": ["mass of magnesium + mass of oxygen = mass of magnesium oxide",
                              "2.40 g + mass of oxygen = 4.00 g",
                              "mass of oxygen = 4.00 g − 2.40 g = 1.60 g"]},
                  "The oxide is heavier, because oxygen from the air joined the magnesium."]},
        {"kind": "card", "title": "Open or sealed",
         "body": ["Marble chips react with acid and give off carbon dioxide gas.",
                  "In an open flask, the gas escapes. The balance reading goes down.",
                  "In a sealed container, the gas cannot escape. The reading stays the same.",
                  "A sealed container is a closed system.",
                  {"figure": "c2-open-sealed"}]},
        {"kind": "reveal", "title": "When the mass seems to change",
         "cols": ["Balance reading", "Why"],
         "rows": [
             ("Marble chips and acid, open flask", "Goes down", "Carbon dioxide escapes into the air"),
             ("Magnesium burning in air", "Goes up", "Oxygen from the air joins the magnesium"),
             ("A candle burning", "Goes down", "Carbon dioxide and water vapour escape"),
             ("An iron nail rusting", "Goes up", "Oxygen and water from the air join the iron"),
             ("Any reaction in a sealed container", "Stays the same", "No substance can get in or out"),
         ]},
        {"kind": "card", "title": "Burning a candle",
         "body": ["Candle wax reacts with oxygen from the air.",
                  "It makes carbon dioxide and water vapour. Both are gases, and they escape.",
                  "So the candle loses mass.",
                  "The gases weigh more than the wax that burnt. They include the oxygen.",
                  "Burn a candle in a sealed container, and the total mass stays the same.",
                  "Heat and light are energy. They are not made of atoms."]},
        {"kind": "card", "title": "Rusting",
         "body": ["Iron reacts with oxygen and water to make rust.",
                  "The extra mass is oxygen and water from the air, joined to the iron.",
                  "Most of that extra mass is oxygen.",
                  "So a rusty nail is heavier than the nail was.",
                  "Seal a nail in a jar of air. The total mass stays the same.",
                  "The oxygen and water it uses were already inside the jar."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("When something burns, its mass is destroyed.",
              "Its atoms leave as gases. Their mass is still there."),
             ("Heat and light carry the mass away.",
              "Heat and light are energy. They have no mass to weigh."),
             ("A rusty nail is heavier, so mass was made.",
              "Oxygen and water from the air joined the iron. No mass was made."),
         ]}]},
    ],
    "key_fact": "In a chemical reaction, atoms are rearranged, never made or destroyed. So the total mass "
                "of the reactants equals the total mass of the products. If the mass seems to change, "
                "a gas has left or come in.",
    "deeper": [
        {"kind": "card", "title": "Phlogiston",
         "body": ["Chemists once thought burning released a substance called phlogiston.",
                  "Then careful weighing showed that metals get heavier when they burn.",
                  "That helped show the phlogiston idea was wrong."]},
    ],
    "try": None,
    "ladder_stem": {
        "recall": "18 g of a metal reacts completely with 32 g of sulfur. This happens in a sealed "
                  "tube. What mass of metal sulfide is made?",
        "apply": "An iron nail is weighed, left to rust for a month, then weighed again. It is heavier. "
                 "What is the main reason?",
        "explain": "A candle is weighed, burnt for an hour, and weighed again. It has lost 12 g. "
                   "Explain where the 12 g went. Describe an experiment to test your idea.",
        "produce": "Damp steel wool is sealed in a bag and weighed. It is left until the wool rusts. Predict "
                   "the new reading. Then predict the reading if the bag had a small hole. Explain both.",
    },
    "ladder_ticks": [
        ["Says the products are gases — carbon dioxide and water vapour — which floated away.",
         "Says the products are gases, carbon dioxide and water vapour, which escape into the air."],
        ["Says the total mass of the products is more than 12 g, because the oxygen is in them too.",
         "Says the products weigh more than 12 g, because they include the oxygen."],
        ["Describes burning the candle in a sealed container and weighing the whole thing before and after.",
         "Describes burning the candle in a sealed container, weighing it all before and after."],
        ["Says the oxygen that joins the iron was already inside the bag and already on the balance.",
         "Says the oxygen and water that join the iron were already in the bag."],
        ["Explains that more oxygen can be drawn in from outside through the hole.",
         "Explains that more oxygen, or water vapour, can get in through the hole."],
    ],
    "figure_caption": {"c2-word-magnesium": None},      # the card text already says it
    "figures": [
        {"id": "c2-carbon-burns", "kind": "diagram", "status": "drawn",
         "art": "particle-boxes",
         "title": "Carbon and oxygen make carbon dioxide",
         "desc": "Two boxes with a drawn arrow between them. The left box, labelled Reactants: carbon and "
                 "oxygen, holds two separate black C circles and two separate pairs of joined red O "
                 "circles. Under it: 2 carbon atoms, 4 oxygen atoms. The right box, labelled Product: "
                 "carbon dioxide, holds two separate groups, each a black C circle joined between two red "
                 "O circles. Under it: 2 carbon atoms, 4 oxygen atoms.",
         "caption": "The same atoms before and after, so the same mass.",
         "data": {"arrow": True, "boxes": [
             {"label": "Reactants: carbon and oxygen", "layout": "spread",
              "groups": [["C"], ["C"], ["O", "O"], ["O", "O"]], "count": "2 carbon atoms, 4 oxygen atoms"},
             {"label": "Product: carbon dioxide", "layout": "spread",
              "groups": [["O", "C", "O"]] * 2, "count": "2 carbon atoms, 4 oxygen atoms"},
         ]}},
        {"id": "c2-word-magnesium", "kind": "diagram", "status": "drawn", "art": "word-equation",
         "title": "The word equation for burning magnesium",
         "desc": "Magnesium plus oxygen at the top, labelled reactants. A drawn arrow points down to "
                 "magnesium oxide, labelled product.",
         "caption": "The word equation for burning magnesium.",
         "eq": {"left": ["magnesium", "oxygen"], "right": ["magnesium oxide"]}},
        {"id": "c2-open-sealed", "kind": "diagram", "status": "drawn",
         "art": "open-sealed-flask",
         "title": "Marble chips and acid, open and sealed",
         "desc": "Two set-ups side by side, each on a top-pan balance. Left, labelled Open flask: a "
                 "conical flask with marble chips in acid, bubbles rising out of the open neck, and an "
                 "arrow labelled carbon dioxide escapes. Its balance reads Before 152.00 g, After 149.80 g. "
                 "Right, labelled Sealed container: a plastic bottle with its screw cap on, marble chips in "
                 "acid, bubbles staying inside. Its balance reads Before 86.40 g, After 86.40 g.",
         "caption": "Open, the gas escapes and the mass falls. Sealed, it stays the same.",
         "data": {"panels": [
             {"label": "Open flask", "vessel": "flask",
              "arrow_label": "carbon dioxide escapes", "before": "152.00 g", "after": "149.80 g"},
             {"label": "Sealed container", "vessel": "bottle", "note": "carbon dioxide stays inside",
              "before": "86.40 g", "after": "86.40 g"},
         ]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "That is 32 − 18. Nothing was taken away. The two substances joined.",
            1: "That is the sulfur alone. The metal is still in the tube.",
            3: "The metal does not matter. Everything that went in is still in the sealed tube.",
        },
        "apply": {
            0: "Density is not mass. Rearranging what is already there cannot add mass.",
            2: "Water is not soaked up. Oxygen and water react with the iron.",
            3: "Time changes nothing. The nail took in oxygen and water from the air.",
        },
    },
}
