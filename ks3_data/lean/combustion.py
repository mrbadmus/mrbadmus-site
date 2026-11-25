# -*- coding: utf-8 -*-
"""Combustion, in the lean shape. Spec table: docs/lessons/wave2/ks3-combustion.md."""

LESSON = {
    "slug": "combustion",
    "start": {
        "setup": "A Bunsen burner has a metal collar with a hole in it. "
                 "With the hole shut, the flame is yellow and leaves soot on a beaker. "
                 "With the hole open, the flame is blue and clean.",
        "question": "If you had to guess, what does the hole in the collar let into the "
                    "burner: more gas, or more air?",
        "options": [
            ("More gas",
             "The gas comes in through the tap at the bottom. The hole in the collar lets in air."),
            ("More air",
             "Right. Air carries oxygen. With plenty of oxygen, the gas burns completely and "
             "the flame is blue."),
        ],
        "answer": 1,
    },
    "words": ["combustion", "fire triangle", "incomplete combustion", "carbon monoxide"],
    "word_defs": {
        "combustion": "A reaction in which a fuel reacts with oxygen and gives out energy.",
        "fire triangle": "The three things a fire needs: fuel, oxygen and heat.",
        "incomplete combustion": "Burning with too little oxygen. It makes carbon monoxide and soot.",
        "carbon monoxide": "A toxic gas with no colour and no smell. Incomplete combustion makes it.",
    },
    "knowledge": [
        {"kind": "card", "title": "What combustion is",
         "body": ["Combustion is a fuel reacting with oxygen.",
                  "It gives out energy as heat and light.",
                  "Burning is the everyday word for combustion.",
                  "Methane, wood, coal and candle wax are all fuels."]},
        {"kind": "card", "title": "The fire triangle",
         "body": [{"figure": "c5-fire-triangle"},
                  "A fire needs three things: fuel, oxygen and heat.",
                  "These are the three sides of the fire triangle.",
                  "Take away any one of them and the fire goes out.",
                  "Put a jar over a lit candle and the flame soon goes out.",
                  "The oxygen in the jar runs low, so the flame goes out."]},
        {"kind": "reveal", "title": "Putting out a fire",
         "cols": ["Side taken away", "How it works"],
         "rows": [
             ("Fire blanket", "Oxygen", "It covers the fire, so air cannot reach it."),
             ("Carbon dioxide extinguisher", "Oxygen", "The gas pushes the air away from the fire."),
             ("Water", "Heat", "It cools the fuel until it is too cool to burn."),
             ("Turning off the gas", "Fuel", "No more gas reaches the flame."),
             ("Firebreak in a forest", "Fuel", "Trees are cleared, so the fire has nothing to burn."),
         ]},
        {"kind": "card", "title": "When water is dangerous",
         "body": ["Never throw water on a burning pan of oil, such as a chip pan.",
                  "The water boils at once and throws burning oil out of the pan.",
                  "At home, do not try to put out a pan fire yourself.",
                  "Turn off the heat if it is safe to do so. Then get out and call 999.",
                  "Never put water on an electrical fire either.",
                  "Water conducts electricity, so you could get an electric shock.",
                  "A carbon dioxide extinguisher is used instead."]},
        {"kind": "card", "title": "Complete combustion",
         "body": ["With plenty of oxygen, a fuel burns completely.",
                  {"figure": "c5-word-complete"},
                  "Methane is the main gas in natural gas. It is made of carbon and hydrogen.",
                  "The carbon ends up in carbon dioxide. The hydrogen ends up in water.",
                  "All the energy the fuel can give is released."]},
        {"kind": "card", "title": "Incomplete combustion",
         "body": ["With too little oxygen, a fuel cannot burn completely.",
                  {"figure": "c5-word-incomplete"},
                  "Some of the carbon ends up in carbon monoxide.",
                  "Some is left as soot. Soot is tiny bits of carbon.",
                  "Less energy is released.",
                  "Soot blackens walls and ceilings, and it can harm your lungs."]},
        {"kind": "reveal", "title": "Complete and incomplete combustion",
         "cols": ["Complete", "Incomplete"],
         "rows": [
             ("Oxygen", "Plenty", "Too little"),
             ("Products from methane", "Carbon dioxide and water",
              "Carbon monoxide, carbon (soot) and water"),
             ("Bunsen burner flame", "Blue", "Yellow"),
             ("Energy released", "More", "Less"),
             ("Beaker held over the flame", "Stays clean", "Gets a black layer of soot"),
         ]},
        {"kind": "card", "title": "The Bunsen burner air hole",
         "body": ["Open the air hole and air mixes with the gas.",
                  "There is plenty of oxygen, so combustion is complete. The flame is blue.",
                  "Shut the air hole and the gas gets too little oxygen.",
                  "Combustion is incomplete, so the flame is yellow.",
                  "The yellow light comes from tiny bits of soot glowing in the flame.",
                  "The blue flame is hotter than the yellow flame."]},
        {"kind": "card", "title": "Why carbon monoxide is dangerous",
         "body": ["Carbon monoxide is toxic.",
                  "It has no colour and no smell, so you cannot tell it is there.",
                  "It stops your blood carrying oxygen around your body.",
                  "Gas boilers and fires must be checked, so they burn completely.",
                  "A carbon monoxide alarm sounds if the gas builds up in a room."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The big yellow flame is hotter, because it is brighter.",
              "The blue flame is hotter. The yellow light is glowing soot.",
              "REACT-10"),
             ("Shutting the air hole makes the flame burn hotter.",
              "Shutting the air hole cuts the oxygen. The flame is cooler and makes soot.",
              "REACT-11"),
             ("Water puts out every kind of fire.",
              "Never use water on burning oil or on an electrical fire."),
             ("You would smell carbon monoxide if it leaked.",
              "Carbon monoxide has no smell. A carbon monoxide alarm can detect it."),
         ]}]},
    ],
    "key_fact": "Combustion is a fuel reacting with oxygen, and a fire needs fuel, oxygen and heat. "
                "With too little oxygen, combustion is incomplete and makes carbon monoxide and soot.",
    "deeper": [
        {"kind": "card", "title": "Hydrogen as a fuel",
         "body": ["Hydrogen contains no carbon.",
                  "When it burns, the only product is water.",
                  "So it makes no carbon dioxide, no carbon monoxide and no soot."]},
        {"kind": "card", "title": "Charcoal",
         "body": ["Charcoal is almost pure carbon.",
                  "With plenty of air, it burns to make carbon dioxide.",
                  "With too little air, it makes carbon monoxide.",
                  "So a barbecue must never be used indoors or in a tent."]},
    ],
    "try": None,
    "tutor_body": "Still not sure why the blue flame is the hot one?",
    "safety_note": "Tie back long hair. Use the yellow safety flame when the burner is not heating "
                   "anything, so everyone can see it is lit. Move hot glass with tongs.",
    "connects_heading": None,
    "ks4_becomes": "Fuels and the pollutants they make, and combustion as an exothermic reaction.",
    "figures": [
        {"id": "c5-fire-triangle", "kind": "diagram", "status": "drawn", "art": "c5-fire-triangle",
         "title": "The fire triangle",
         "desc": "A triangle with a flame drawn in the middle, labelled fire. The word heat is "
                 "beside the left side, oxygen beside the right side and fuel under the base.",
         "caption": "The fire triangle: fuel, oxygen and heat.",
         "data": {"labels": {"fuel": "fuel", "oxygen": "oxygen", "heat": "heat", "fire": "fire"}}},
        {"id": "c5-word-complete", "kind": "diagram", "status": "drawn", "art": "c4-word-row",
         "title": "Complete combustion of methane",
         "desc": "Written left to right. On the left, under the tag Reactants: methane, then a "
                 "plus sign, then oxygen. In the middle, a drawn arrow pointing right. On the "
                 "right, under the tag Products: carbon dioxide, then a plus sign, then water.",
         "caption": "With plenty of oxygen, methane gives carbon dioxide and water.",
         "data": {"left": ["methane", "oxygen"], "right": ["carbon dioxide", "water"]}},
        {"id": "c5-word-incomplete", "kind": "diagram", "status": "drawn", "art": "c4-word-row",
         "title": "Incomplete combustion of methane",
         "desc": "Written left to right. On the left, under the tag Reactants: methane, then a "
                 "plus sign, then oxygen. In the middle, a drawn arrow pointing right. On the "
                 "right, under the tag Products: carbon monoxide, plus carbon, plus water.",
         "caption": "With too little oxygen, some carbon becomes carbon monoxide and some is "
                    "left as soot.",
         "data": {"left": ["methane", "oxygen"], "right": ["carbon monoxide", "carbon", "water"]}},
    ],
    "ladder_stem": {
        "explain": "A gas fire burns with a yellow flame. There is black soot on the wall above "
                   "it. Explain what is going wrong. Explain why it is dangerous. Say why nobody "
                   "can smell the danger.",
        "produce": "A candle in a sealed jar goes out within seconds. A rocket burns fuel far "
                   "above the Earth, where there is almost no air. Use one idea to explain both. "
                   "Say what the rocket must carry.",
    },
    "ladder_feedback": {
        "recall": {
            0: "Carbon monoxide is made when oxygen is short. With plenty, the carbon becomes carbon dioxide.",
            1: "Soot is unburnt carbon from incomplete combustion. The hydrogen in the fuel becomes water.",
            2: "Both come from incomplete combustion. With plenty of oxygen you get carbon dioxide and water.",
        },
        "apply": {
            0: "A flame that is dying down gets smaller. This flame is tall, and the colour shows the air supply.",
            1: "The blue flame is hotter. The yellow light comes from glowing soot.",
            3: "Nothing extra is in the gas. Open the air hole and the same gas burns blue.",
        },
    },
}
