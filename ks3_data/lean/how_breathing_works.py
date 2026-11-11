# -*- coding: utf-8 -*-
"""How breathing works, in the lean shape. Spec table: docs/lessons/pilot/ks3-how-breathing-works.md."""

LESSON = {
    "slug": "how-breathing-works",
    "start": {
        "setup": None,
        "question": "If you had to guess, how does a healthy lung normally fill with air?",
        "options": [
            ("The chest stretches it open", "The chest stretches it open. Lungs cannot open themselves."),
            ("It stretches itself open", "The chest stretches it open. Lungs cannot open themselves."),
        ],
        "answer": 0,
    },
    "words": ["diaphragm", "intercostal muscles", "volume", "pressure"],
    "knowledge": [
        {"kind": "reveal", "title": "Breathing in and breathing out",
         "cols": ["Breathing in", "Breathing out"],
         "rows": [
             ("Intercostal muscles", "Contract", "Relax"),
             ("Ribs", "Move up and out", "Move down and in"),
             ("Diaphragm", "Contracts and flattens", "Relaxes and domes upwards"),
             ("Chest volume", "Increases", "Decreases"),
             ("Pressure in the chest", "Falls, so it is lower than outside",
              "Rises, so it is higher than outside"),
             ("Air", "Moves in", "Moves out"),
             ("Why air moves", "Air moves from high pressure outside to low pressure inside",
              "Air moves from high pressure inside to low pressure outside"),
         ]},
        {"kind": "card", "title": "Lungs cannot move themselves",
         "body": ["Your lungs cannot move themselves.",
                  "The diaphragm and intercostal muscles do the work.",
                  "The lungs stretch when the chest gets bigger."]},
        {"kind": "card", "title": "Why the pressure changes",
         "body": ["Air particles hit the walls of the chest. This causes pressure.",
                  "The same particles in a bigger space hit the walls less often. So the pressure falls.",
                  "In a smaller space, they hit the walls more often. So the pressure rises."]},
        {"kind": "card", "title": "The bell jar model",
         "body": ["A bell jar is a model of the chest.",
                  {"figure": "b4-bell-jar-model"},
                  "Pull the sheet down. The volume in the jar increases and the pressure falls.",
                  "Air moves in and the balloons inflate.",
                  "Push the sheet up. The volume in the jar decreases and the pressure rises.",
                  "Air moves out and the balloons deflate."]},
        {"kind": "card", "title": "Measuring lung volume",
         "body": [{"figure": "b4-lung-volume-bottle"},
                  "Take the deepest breath you can.",
                  "Then breathe out fully through the tube into the bottle.",
                  "The volume of water pushed out equals the volume of air you breathed out."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The lungs pull air in.",
              "Muscles make the chest bigger, then air moves in."),
             ("Air coming in makes the chest bigger.",
              "The chest gets bigger first. Then air moves in."),
             ("Air gets sucked in.",
              "Air moves in because the pressure outside is higher."),
         ]}]},
    ],
    "key_fact": "Breathing works by changing pressure. Muscles change the volume of the chest, "
                "which changes the pressure inside it. Air always moves from high pressure to "
                "low pressure.",
    "deeper": [
        {"kind": "card", "title": "Where the bell jar model fails",
         "body": [{"points": ["The jar is rigid. Your ribs can move.",
                              "A balloon is one bag. A lung holds millions of tiny air sacs.",
                              "The rubber sheet is flat. A real diaphragm is a dome."]}]},
        {"kind": "card", "title": "Breathing out at rest",
         "body": ["At rest, you do not have to push air out.",
                  "The muscles relax and the stretched lungs spring back to size."]},
        {"kind": "card", "title": "How a wound can collapse a lung",
         "body": ["A wound between the ribs lets air into the space around the lung.",
                  "The pressure around the lung now matches the air outside.",
                  "So a bigger chest no longer stretches that lung.",
                  "The lung collapses, even if it is not damaged."]},
    ],
    "try": None,
    "figures": [
        {"id": "b4-bell-jar-model", "kind": "diagram", "status": "drawn", "art": "bell-jar-model",
         "title": "A bell jar model of the chest",
         "desc": "Two drawings of the same bell jar side by side. Labels name the jar as the chest, "
                 "the two balloons as the lungs, the tube as the trachea and the rubber sheet as "
                 "the diaphragm. On the left the sheet is pulled down and the balloons are "
                 "inflated. On the right the sheet is pushed up and the balloons are small.",
         "caption": "Pull the sheet down and the balloons inflate."},
        {"id": "b4-lung-volume-bottle", "kind": "diagram", "status": "drawn", "art": "lung-volume-bottle",
         "title": "Measuring lung volume with an upturned bottle",
         "desc": "A large bottle full of water stands upside down in a tub of water. A tube runs "
                 "from a person's mouth up into the bottle, and air collects at the top of the "
                 "bottle, pushing the water down. Volume marks run up the side of the bottle.",
         "caption": "The air you breathe out pushes water out of the bottle."},
    ],
    "ladder_stem": {
        "apply": "The balloon starts empty. You seal the tube so no air can get in or out. "
                 "Then you pull the rubber sheet down. What happens?",
    },
    "ladder_feedback": {
        "recall": {
            1: "The air moving is the last step. The muscles go first.",
            2: "The pressure only falls after the volume changes. The muscles go first.",
            3: "The lungs cannot expand themselves. The chest stretches them.",
        },
        "apply": {
            0: "The sheet still moves and the space still gets bigger. The pressure falls.",
            2: "The balloon is empty and the tube is sealed. No air can get in.",
            3: "More space means the particles hit the walls less often. The pressure falls.",
        },
    },
}
