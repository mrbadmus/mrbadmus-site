# -*- coding: utf-8 -*-
"""Solids, liquids and gases, in the lean shape. Spec table: docs/lessons/wave1/ks3-solids-liquids-and-gases.md."""

LESSON = {
    "slug": "solids-liquids-and-gases",
    "start": {
        "setup": "A steel bridge is a few centimetres longer in summer than in winter.",
        "question": "If you had to guess, when steel expands in the heat, what gets bigger?",
        "options": [
            ("Each particle swells up",
             "It is the gaps between the particles that grow. Bridges have joints to leave room for this."),
            ("The gaps between them",
             "It is the gaps between the particles that grow. Bridges have joints to leave room for this."),
        ],
        "answer": 1,
    },
    "words": ["solid", "liquid", "gas", "vibrate"],
    "word_defs": {
        "solid": "A state of matter that keeps its own shape and volume.",
        "liquid": "A state of matter that flows and takes the shape of its container.",
        "gas": "A state of matter that spreads out to fill its whole container.",
        "vibrate": "To move quickly back and forth about a fixed position.",
    },
    "knowledge": [
        {"kind": "card", "title": "Three states",
         "body": [{"figure": "c1-three-states"},
                  "Ice, water and steam are one substance in three states.",
                  "The particles are the same in all three. Only their arrangement and movement change."]},
        {"kind": "reveal", "title": "Solid, liquid and gas",
         "cols": ["Solid", "Liquid", "Gas"],
         "rows": [
             ("Arrangement", "Touching, in a regular pattern", "Touching, in no pattern", "Far apart, at random"),
             ("Movement", "Vibrate about fixed positions", "Slide past each other", "Move fast, in random directions"),
             ("Shape", "Keeps its own shape", "Takes the shape of its container", "Fills its container"),
             ("Volume", "Fixed", "Fixed", "Fills the space it is given"),
             ("Squashing", "Almost impossible", "Almost impossible", "Easy"),
             ("Flowing", "Does not flow", "Flows and pours", "Flows and spreads out"),
         ]},
        {"kind": "card", "title": "Why each state behaves as it does",
         "body": ["Particles in solids and liquids attract each other strongly.",
                  "In a solid, these forces hold the particles in fixed positions. So it keeps its shape.",
                  "In a liquid, the particles still touch but can slide past each other.",
                  "So a liquid flows, but its volume stays the same.",
                  "In a gas, the forces between particles are very weak.",
                  "Gas particles move in straight lines until they hit something.",
                  "So a gas spreads out until the walls of its container stop it."]},
        {"kind": "card", "title": "Squashing",
         "body": ["A gas is mostly empty space.",
                  "Squashing it pushes the particles closer together. Each one stays the same size.",
                  "In solids and liquids the particles already touch. There is no space to squash out."]},
        {"kind": "card", "title": "Heating a solid",
         "body": [{"figure": "c1-expansion"},
                  "Heating gives the particles more energy, so they vibrate more.",
                  "They push each other slightly further apart, so the solid expands.",
                  "The number of particles stays the same.",
                  "It is still a solid. The particles still vibrate about fixed positions."]},
        {"kind": "card", "title": "Density",
         "body": ["Density is how much mass is packed into a certain volume.",
                  "Solids and liquids are much denser than gases. Their particles are close together.",
                  "A gas has a very low density, because its particles are far apart.",
                  "A solid is usually a little denser than the same substance as a liquid.",
                  "Water is an odd one out. Ice is less dense than water, so it floats."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Particles in a solid are completely still.",
              "They vibrate about fixed positions.", "PART-04"),
             ("Particles get bigger when a substance is heated or melts.",
              "They move more. Their size never changes.", "PART-03"),
             ("Particles in a liquid are far apart.",
              "They touch, but are not in a pattern."),
             ("Gas and air mean the same thing.",
              "Gas is a state of matter. Air is a mixture of gases."),
         ]}]},
    ],
    "key_fact": "In a solid the particles touch in a regular pattern and vibrate. In a liquid they "
                "touch but slide past each other. In a gas they are far apart and move fast, at random.",
    "deeper": [
        {"kind": "card", "title": "Not everything fits",
         "body": ["Three states is a model, and some materials do not fit it neatly.",
                  "Glass keeps its shape like a solid. Its particles are jumbled like a liquid's.",
                  "Stars are made of plasma, a fourth state of matter."]},
    ],
    "try": None,
    "figure_caption": {"c1-three-states": None,     # no caption on the page, as before
                       "c1-expansion": "The change is drawn far bigger than it really is."},
    "ladder_stem": {
        "explain": "A gas fills any container it is put in. The same amount of liquid sits in a "
                   "puddle at the bottom. Explain both, using the arrangement and movement of the particles.",
        "produce": "A steel railway rail is 30 m long in winter. On a hot summer day it is about 1 cm "
                   "longer. Explain what has happened to the particles. Say clearly what has NOT happened.",
    },
    "ladder_ticks": [
        ["Says nothing holds gas particles together, so they spread until the walls stop them.",
         "Says gas particles hardly attract each other, so they spread until the walls stop them."],
        ["Says liquid particles are touching and attracted to each other, so they stay as one body.",
         "Says liquid particles touch and attract each other, so they stay together."],
        ["Says liquid particles can still slide past each other, which is why the puddle takes the shape of the floor.",
         "Says liquid particles can slide past each other, so the puddle spreads over the floor."],
        ["Says heating gives the particles more energy so they vibrate faster or further.",
         "Says heating gives the particles more energy, so they vibrate more."],
        ["Says the steel is still a solid — the particles are still in fixed positions, just further apart.",
         "Says the steel is still a solid. Its particles are in fixed positions, slightly further apart."],
    ],
    "figures": [
        {"id": "c1-three-states", "kind": "diagram", "status": "drawn",
         "art": "particle-picture",
         "title": "The particles in a solid, a liquid and a gas",
         "desc": "Three boxes, one above the other, each holding identical plain circles drawn the same "
                 "size. The top box, labelled Solid, holds circles touching in neat rows, with short "
                 "curved marks at both ends of every row to show the particles vibrating on the spot. The "
                 "middle box, labelled Liquid, holds circles touching each other in a jumble, filling the "
                 "bottom of the box, with three short curved arrows over the top ones showing them "
                 "sliding. The bottom box, labelled Gas, holds a few circles far apart, each with a "
                 "straight arrow pointing a different way.",
         "caption": "The same particles in each state, arranged and moving differently.",
         "data": {"boxes": [
             {"label": "Solid", "layout": "solid", "rows": 4, "cols": 8, "motion": True},
             {"label": "Liquid", "layout": "liquid", "n": 22, "motion": True},
             {"label": "Gas", "layout": "gas", "n": 8, "motion": True},
         ]}},
        {"id": "c1-expansion", "kind": "diagram", "status": "drawn",
         "art": "particle-picture",
         "title": "The particles in cold steel and in hot steel",
         "desc": "Two boxes, one above the other. The top box, labelled Cold steel, holds circles "
                 "touching in neat rows, with small vibration marks at both ends of each row. The bottom "
                 "box, labelled Hot steel, holds the same number of circles, drawn the same size, in neat "
                 "rows with small gaps between them, and bigger vibration marks. The block of particles in "
                 "the bottom box is wider and taller.",
         "caption": "Heating moves the particles slightly further apart. The particles do not grow.",
         "data": {"boxes": [
             {"label": "Cold steel", "layout": "solid", "rows": 3, "cols": 8, "motion": True},
             {"label": "Hot steel", "layout": "solid", "rows": 3, "cols": 8, "motion": True,
              "spacing": "wider"},
         ]}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "Solid particles touch too, but they sit in a regular pattern.",
            1: "Gas particles are far apart, not close together.",
            2: "The spacing differs. Gas particles are far apart. Solid and liquid particles touch.",
        },
        "apply": {
            0: "The particles do not change with state. Liquid and gas particles of a substance are the same.",
            1: "Particles are the same size in every state. Only the spacing changes.",
            2: "Weight does not stop squashing. Liquid particles already touch, so there is no space to remove.",
        },
    },
}
