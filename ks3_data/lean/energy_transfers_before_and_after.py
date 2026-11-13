# -*- coding: utf-8 -*-
"""Energy transfers: before and after, in the lean shape.
Spec table: docs/lessons/wave1/ks3-energy-transfers-before-and-after.md."""

LESSON = {
    "slug": "energy-transfers-before-and-after",
    "start": {
        "setup": "A power bank weighs the same on a kitchen scale when full and when flat.",
        "question": "If you had to guess, is the energy in it a kind of stuff?",
        "options": [
            ("Yes, it is stuff", "No, it is not stuff. Energy is a quantity we calculate. Nothing was poured out."),
            ("No, it is not stuff", "No, it is not stuff. Energy is a quantity we calculate. Nothing was poured out."),
        ],
        "answer": 1,
    },
    "words": ["useful energy", "wasted energy", "dissipated", "efficiency"],
    "word_defs": {
        "useful energy": "Energy transferred to the store you wanted.",
        "wasted energy": "Energy transferred to stores you did not want, usually thermal stores.",
        "dissipated": "Spread out into the surroundings, mostly by heating, so it is hard to use.",
        "efficiency": "The fraction of the energy put in that is transferred usefully.",
    },
    "knowledge": [
        {"kind": "card", "title": "Before and after",
         "body": ["To describe a transfer, compare the start with the end.",
                  "Say which store empties and which stores fill.",
                  "Then say how much energy is in each, in joules.",
                  "The total before always equals the total after."]},
        {"kind": "reveal", "title": "What starts a transfer",
         "cols": ["Store that empties", "Stores that fill"],
         "rows": [
             ("Dropping an object", "Gravitational potential", "Kinetic"),
             ("Stretching a spring", "Chemical, in your muscles", "Elastic potential, and thermal in your body"),
             ("Speeding up on a bike", "Chemical, in your muscles", "Kinetic, and thermal in your body"),
             ("Switching on a torch", "Chemical, in the battery", "Thermal, in the torch and the room"),
             ("Burning a fuel", "Chemical, in the fuel", "Thermal, in the surroundings"),
             ("Using food to exercise", "Chemical, in the food", "Kinetic and thermal, in your body"),
         ]},
        {"kind": "card", "title": "How a transfer happens",
         "body": ["To explain how, describe what physically happens.",
                  {"points": ["A force pushes or pulls something through a distance.",
                              "An electric current flows round a circuit.",
                              "A hotter object heats a cooler one.",
                              "Light or sound carries energy away."]},
                  "For example, a cyclist brakes. The brake pads rub on the wheel.",
                  "Friction heats the pads and the wheel."]},
        {"kind": "card", "title": "Useful and wasted energy",
         "body": ["Useful energy goes to the store you wanted.",
                  "Wasted energy goes to stores you did not want.",
                  "Most wasted energy is dissipated to the surroundings by heating.",
                  "Wasted energy is not destroyed. It is spread out too thinly to use.",
                  "A filament bulb gets hot. Most of its energy heats the room.",
                  "An LED gives the same light and wastes much less energy."]},
        {"kind": "card", "title": "Wasted depends on the job",
         "body": ["An electric heater warms a room. That is its job, so it is useful.",
                  "A filament bulb also warms the room. For a bulb, that is wasted.",
                  "In winter, the energy a bulb wastes still helps to warm the room."]},
        {"kind": "card", "title": "Efficiency",
         "body": [{"figure": "p1-sankey-winch"},
                  "Efficiency compares the useful energy out with the total energy in.",
                  "efficiency = useful energy out ÷ total energy in",
                  "Multiply by 100 to give a percentage.",
                  "Efficiency has no unit.",
                  "Most devices waste some energy, so their efficiency is less than 100%.",
                  "Nothing can be more than 100% efficient."]},
        {"kind": "card", "title": "Worked example: efficiency",
         "body": ["A winch takes in 100 J. It gives 70 J to the load's gravitational potential store.",
                  {"points": ["C, convert: both energies are already in joules.",
                              "F, formula: efficiency = useful energy out ÷ total energy in",
                              "I, insert: efficiency = 70 J ÷ 100 J",
                              "F, fine-tune: 70 ÷ 100 = 0.7",
                              "A, answer: 0.7 × 100 = 70%"]},
                  "The other 30 J heats the motor, the cable and the air."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Wasted energy is destroyed.",
              "It is dissipated to the surroundings. The total stays the same."),
             ("Efficiency is useful energy divided by wasted energy.",
              "Always divide the useful energy by the total energy in."),
             ("A device can be 120% efficient.",
              "Nothing gives out more useful energy than it takes in."),
         ]}]},
    ],
    "key_fact": "In any transfer, the total energy before equals the total after. Useful energy goes "
                "to the store you want. Wasted energy is dissipated to the surroundings, mostly by "
                "heating. Efficiency = useful energy out ÷ total energy in.",
    "deeper": [
        {"kind": "card", "title": "Why you cannot get it back",
         "body": ["A warm room holds energy spread out among countless particles.",
                  "It cannot all be gathered back into a battery.",
                  "On their own, transfers run one way: from concentrated stores to spread out ones."]},
        {"kind": "card", "title": "Why you sweat",
         "body": ["When you sprint, most of the energy from your food heats your body.",
                  "Sweat evaporating from your skin carries this extra energy away."]},
    ],
    "try": None,
    "ks4_becomes": "Efficiency from power, and Sankey diagrams for real devices.",
    "figures": [
        {"id": "p1-sankey-winch", "kind": "diagram", "status": "drawn", "art": "sankey",
         "title": "A Sankey diagram for an electric winch",
         "desc": "A wide arrow labelled 100 J in, by an electric current, splits in two. "
                 "A band 70 J wide carries straight on. "
                 "It is labelled 70 J useful, gravitational potential store of the load. "
                 "A band 30 J wide turns down. "
                 "It is labelled 30 J wasted, thermal store of the surroundings.",
         "caption": "The width of each arrow shows the energy. 100 J in = 70 J + 30 J out.",
         "data": {"in": {"label": "Energy in, by an electric current", "J": 100},
                  "useful": {"label": "Gravitational potential store of the load", "J": 70},
                  "wasted": {"label": "Thermal store of the surroundings", "J": 30}}},
    ],
    "ladder_stem": {
        "apply": "Each second, a filament bulb takes in 60 J. Only 3 J is carried away by light. "
                 "Which answer names the store the other 57 J ends up in?",
        "explain": "An electric winch is supplied with 500 J. It lifts a crate. The crate's gravitational "
                   "potential store gains 350 J. Account for all 500 J. Work out the winch's "
                   "efficiency. Explain why this does not break conservation of energy.",
        "produce": "A shop swaps all its filament bulbs for LEDs. In winter, its heating bill goes up "
                   "slightly. Explain why. Say whether the change was still worth making.",
    },
    "ladder_ticks": [
        ["Names where those thermal stores are — motor, gearbox, cable, air.",
         "Names where those thermal stores are, such as the motor, cable and air."],
        ["Says the two columns still total 500 J.",
         "Says the total is still 500 J. Efficiency = 350 ÷ 500 = 70%."],
        ["Says the 150 J is wasted rather than lost, and explains that “wasted” means not doing "
         "the job you wanted.",
         "Says the 150 J is wasted, not destroyed. It did not do the useful job."],
        ["States that 350 J fills the gravitational store of the crate.",
         "States that 350 J fills the crate's gravitational potential store."],
        ["Says the old bulbs were filling a thermal store in the shop as well as giving light.",
         "Says the old bulbs heated the shop as well as lighting it."],
        ["Says that warmth was doing part of the heater’s job, whether or not anyone intended it.",
         "Says the bulbs' wasted energy was doing part of the heater's job."],
        ["Says the heating system has to make up a small part of the difference.",
         "Says the heater must now supply all the energy the old bulbs gave out."],
        ["Concludes that the total energy used still falls, and notes that in summer the old bulbs made the "
         "cooling problem worse.",
         "Says it was still worth it. Over a whole year, the shop needs less energy."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Nothing is used up. If your totals differ, you missed a thermal store.",
            2: "No device creates energy. It only transfers energy between stores.",
            3: "Efficiency tells you how the energy is shared out. The total never changes.",
        },
        "apply": {
            0: "It is not lost. A thermometer would find it in the room.",
            1: "Energy is never used up. Say which store it went to.",
            2: "An electric current is a pathway, not a store.",
        },
    },
}
