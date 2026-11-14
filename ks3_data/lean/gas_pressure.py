# -*- coding: utf-8 -*-
"""Gas pressure, in the lean shape. Spec table: docs/lessons/wave1/ks3-gas-pressure.md."""

from ..quantities import TEMPERATURE_SHORT

LESSON = {
    "slug": "gas-pressure",
    "start": {
        "setup": "An aerosol can has stopped spraying. When you shake it, it sounds empty.",
        "question": "If you had to guess, is that can really empty inside?",
        "options": [
            ("No, there is gas inside",
             "It is still full of gas. That is why it must never go on a fire."),
            ("Yes, it is really empty",
             "It is still full of gas. That is why it must never go on a fire."),
        ],
        "answer": 0,
    },
    "words": ["pressure", "collision", "temperature"],
    "word_defs": {
        "pressure": "How much force pushes on each square metre of a surface.",
        "collision": "When a moving particle hits something and bounces off.",
        "temperature": TEMPERATURE_SHORT[0].upper() + TEMPERATURE_SHORT[1:] + ".",
    },
    "knowledge": [
        {"kind": "card", "title": "What causes gas pressure",
         "body": ["Gas particles move fast, in random directions.",
                  "They keep colliding with the walls of their container.",
                  "Each collision pushes on the wall. Together, these pushes are the gas pressure.",
                  "Gas pressure pushes on every wall, the top and sides as well as the bottom.",
                  "Particles also bump into each other. Those bumps do not push on the walls.",
                  "So they do not add to the pressure."]},
        {"kind": "reveal", "title": "Changing the pressure",
         "cols": ["What the particles do", "Pressure"],
         "rows": [
             ("Heat the gas in the same container",
              "Move faster, and hit the walls more often and harder", "Goes up"),
             ("Make the container smaller", "Hit the walls more often", "Goes up"),
             ("Add more gas", "More particles hit the walls each second", "Goes up"),
             ("Cool the gas", "Move slower, and hit the walls less often and more gently", "Goes down"),
             ("Let half the gas out", "Half as many particles hit the walls", "Goes down"),
         ]},
        {"kind": "card", "title": "A smaller space",
         "body": [{"figure": "c1-wall-hits"},
                  "At the same temperature, the particles move no faster. The walls are closer, so they get there sooner."]},
        {"kind": "card", "title": "Tyres and pumps",
         "body": ["As a tyre is pumped up, more particles hit its walls each second.",
                  "A tyre warms up as a car is driven along.",
                  "When the tyre cools down, its pressure falls back."]},
        {"kind": "card", "title": "The collapsing can",
         "body": ["A little water is boiled in a can, so steam fills it.",
                  "The can is turned upside down into cold water.",
                  "The steam condenses into a few drops of water.",
                  "Now very few particles inside are hitting the walls.",
                  "The air outside now pushes much harder than the gas inside. It crushes the can."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Gas pressure is particles pushing against each other.",
              "Gas pressure comes from particles hitting the walls."),
             ("Heating a gas makes its particles swell.",
              "They move faster. Their size never changes."),
             ("The air in a pumped-up tyre is packed solid, its particles touching.",
              "They are closer than outside, but still far apart. It is still a gas."),
         ]}]},
    ],
    "key_fact": "Gas pressure is caused by gas particles colliding with the walls of their container. "
                "More collisions each second, or harder ones, mean a higher pressure.",
    "deeper": [
        {"kind": "card", "title": "Air pressure on you",
         "body": ["The air around you presses on you all the time.",
                  "You do not feel it, because your body pushes back just as hard.",
                  "A sealed plastic bottle brought down a mountain gets squashed.",
                  "Lower down, the air outside pushes harder than the air inside.",
                  "Nothing sucks. Things are pushed, by particles, from the side with more collisions."]},
    ],
    "try": None,
    "safety_note": "The collapsing can is a teacher demonstration. Steam and the hot can can burn.",
    "ks4_becomes": "The gas laws: pressure, volume and temperature as numbers you can calculate with.",
    "ladder_stem": {
        "produce": "A car tyre is pumped up correctly on a cold morning. After an hour of motorway driving, "
                   "its pressure is higher. No air has been added. Explain why. Should the driver let some air out?",
    },
    "ladder_ticks": [
        ["Says each particle now reaches a wall more often, because it has less distance to travel.",
         "Says each particle reaches a wall more often, as it has less far to go."],
        ["Says the higher pressure pushes back harder on the handle — the particles are not being squashed themselves.",
         "Says the higher pressure pushes back harder on the handle. The particles stay the same size."],
        ["Says friction with the road and flexing of the rubber heat the air in the tyre.",
         "Says driving warms the tyre and the air inside it."],
        ["Says the number of particles has not changed — no air has been added.",
         "Says the number of particles has not changed. No air has been added."],
        ["Says the driver should not let air out to correct it, because the pressure will fall again as the tyre cools.",
         "Says no air should be let out. The pressure falls again as the tyre cools."],
    ],
    "figures": [
        {"id": "c1-wall-hits", "kind": "diagram", "status": "drawn",
         "art": "particle-picture",
         "title": "The same gas in a big container and in half the space",
         "desc": "Two boxes, one above the other, each holding ten identical circles, far apart, each with a "
                 "straight arrow showing which way it is moving. Where an arrow meets a wall, a small star "
                 "marks a collision. The top box, labelled Big container, has four stars. The bottom box, "
                 "labelled Same gas, half the space, is half as tall, and has eight stars.",
         "caption": None,
         "data": {"boxes": [
             {"label": "Big container", "layout": "gas", "n": 10, "motion": True, "hits": 4},
             {"label": "Same gas, half the space", "layout": "gas", "n": 10, "motion": True, "hits": 8,
              "height": "half"},
         ]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Particles do bump into each other. Only hits on the walls push on the walls.",
            2: "Gas pressure pushes on the top and sides too. Weight cannot explain that.",
            3: "Particles have no aim. They move at random and hit the walls.",
        },
        "apply": {
            0: "Heating makes the particles move faster, so their speed has changed.",
            2: "Faster particles hit the walls more often, so this goes up.",
            3: "The pressure rises. That is why a heated can may burst.",
        },
    },
}
