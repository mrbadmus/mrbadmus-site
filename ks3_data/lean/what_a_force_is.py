# -*- coding: utf-8 -*-
"""What a force is, in the lean shape. Spec table: docs/lessons/wave1/ks3-what-a-force-is.md."""

LESSON = {
    "slug": "what-a-force-is",
    "start": {
        "setup": "You stand on a skateboard and push against a wall. You roll away from it.",
        "question": "If you had to guess, as you roll away, are you still carrying the wall's push with you?",
        "options": [
            ("Yes, until it runs out",
             "No. The wall's push stops when your hands leave it. You roll on because you are already moving."),
            ("No, it has already stopped",
             "No. The wall's push stops when your hands leave it. You roll on because you are already moving."),
        ],
        "answer": 1,
    },
    "words": ["force", "newton", "contact force", "non-contact force"],
    "word_defs": {
        "force": "A push or a pull on an object, caused by a second object.",
        "newton": "The unit of force. Its symbol is N.",
        "contact force": "A force that acts only while two objects touch, such as friction.",
        "non-contact force": "A force that acts across a gap, such as gravity or magnetism.",
    },
    "knowledge": [
        {"kind": "card", "title": "A force is a push or a pull",
         "body": ["A force is a push or a pull.",
                  "Every force acts between two objects.",
                  "To describe a force, name both objects. For example, the tow bar pulls the caravan.",
                  "A force lasts only while the two objects act on each other.",
                  "An object cannot store a force or carry one with it."]},
        {"kind": "card", "title": "Forces come in pairs",
         "body": [{"figure": "p4-force-pair-wall"},
                  "When you push a wall, the wall pushes you back.",
                  "The two forces are the same size and point in opposite directions.",
                  "They act on different objects, one on each.",
                  "The wall's push on you is what makes you roll away.",
                  "A swimmer pushes water backwards. The water pushes the swimmer forwards."]},
        {"kind": "card", "title": "What a force can do",
         "body": [{"points": ["Make an object speed up or slow down.",
                              "Change the direction an object moves in.",
                              "Change an object's shape, such as squashing a sponge.",
                              "Make an object turn, such as a door swinging open."]}]},
        {"kind": "card", "title": "Measuring a force",
         "body": ["An apple resting on your hand presses down with about 1 N.",
                  "A newtonmeter measures force. It has a spring inside.",
                  {"figure": "p4-newtonmeter-reading"},
                  "A bigger pull stretches the spring further, so the pointer moves further down the scale.",
                  "Check it reads zero first. Read the scale at eye level."]},
        {"kind": "reveal", "title": "Contact or non-contact",
         "cols": ["Type", "The two objects"],
         "rows": [
             ("A boot kicks a ball", "Contact", "The boot and the ball"),
             ("Friction slows a sliding book", "Contact", "The book and the table"),
             ("Air resistance slows a cyclist", "Contact", "The cyclist and the air"),
             ("A magnet lifts a paperclip", "Non-contact", "The magnet and the paperclip"),
             ("A rubbed balloon lifts your hair", "Non-contact", "The balloon and your hair"),
             ("The Earth pulls the Moon", "Non-contact", "The Earth and the Moon"),
         ]},
        {"kind": "card", "title": "Forces across a gap",
         "body": ["Gravity, magnetism and static electricity are non-contact forces.",
                  "Nothing has to fill the gap between the objects.",
                  "A magnet pulls a paperclip just as hard with all the air pumped away."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A thrown ball carries a force that slowly runs out.",
              "Nothing carries a force. Air resistance and gravity act on the ball as it flies."),
             ("A table does nothing to a book resting on it.",
              "The table pushes up on the book. That is why the book does not fall through."),
             ("The force is in the ball's movement.",
              "Movement is not a force. A force is one object pushing or pulling another."),
         ]}]},
    ],
    "key_fact": "A force is a push or a pull between two objects, measured in newtons (N). "
                "Contact forces act only while the objects touch. Non-contact forces, such as "
                "gravity and magnetism, act across a gap.",
    "deeper": [
        {"kind": "card", "title": "Why anything moves",
         "body": ["The two forces in a pair act on different objects.",
                  "So they never cancel each other out.",
                  "You push the wall and the wall pushes you, but only you roll away.",
                  "The wall is fixed to the building and the ground, so it stays put."]},
        {"kind": "card", "title": "Some sizes",
         "body": [{"points": ["A hard kick on a football: about 1000 N.",
                              "A car towing a caravan: about 2000 N.",
                              "The Earth pulling the Moon: about 200 billion billion N."]}]},
    ],
    "try": None,
    "before_this": "Nothing. This is where the unit starts.",
    "tutor_body": "Stuck finding the second object for a force?",
    "figures": [
        {"id": "p4-force-pair-wall", "kind": "diagram", "status": "drawn", "art": "force-arrows",
         "title": "A skater pushing a wall",
         "desc": "A skater, drawn as a box on wheels, touches a wall on the right. Both arrows start "
                 "where they touch. An arrow on the skater points left, labelled: wall pushes skater. "
                 "An arrow on the wall points right, labelled: skater pushes wall. The two arrows are "
                 "the same length.",
         "caption": "The skater and the wall push on each other.",
         "data": {"layout": "pair", "touching": True,
                  "objects": [{"label": "Skater"}, {"label": "Wall", "fixed": True}],
                  "arrows": [{"on": 0, "dir": "left", "label": "Wall pushes skater"},
                             {"on": 1, "dir": "right", "label": "Skater pushes wall"}]}},
        {"id": "p4-newtonmeter-reading", "kind": "diagram", "status": "drawn", "art": "newtonmeter",
         "title": "A newtonmeter holding a shoe",
         "desc": "A newtonmeter hangs from a hook. A spring inside it is stretched. Its scale runs "
                 "from 0 N at the top to 10 N at the bottom. It is marked every 1 N and numbered every "
                 "2 N. A shoe hangs from the hook at the bottom. The pointer, at the end of the spring, "
                 "is at 3 N.",
         "caption": "The pointer reads 3 N, so the shoe pulls down with 3 N.",
         "data": {"max_N": 10, "minor_N": 1, "label_every_N": 2, "reading_N": 3, "load": "Shoe"}},
    ],
    "ladder_stem": {
        "recall": "A footballer heads a ball. Which statement describes the forces correctly?",
        "explain": "Someone on a skateboard pushes a wall and rolls backwards. Name both objects and "
                   "both forces in the pair. Say which force moved the skater.",
        "produce": "A spacecraft far from any planet fires its engine and speeds up. There is nothing "
                   "around it to push against. Name the second object in the force that speeds it up. "
                   "Explain how you know there must be one.",
    },
    "ladder_ticks": [
        ["Says the skater pushes the wall forwards.",
         "Says the skater pushes on the wall, towards the wall."],
        ["Says the wall pushes the skater backwards.",
         "Says the wall pushes on the skater, away from the wall."],
        ["Gives both forces the same size, in newtons.",
         "Says the two forces are the same size."],
        ["Says it is the wall’s push on the skater that moved the skater, not the skater’s own push.",
         "Says the wall’s push on the skater is what moved the skater."],
        ["Names the exhaust gas, or the fuel thrown out of the engine, as the second object.",
         "Names the exhaust gas, or burnt fuel, pushed out as the second object."],
        ["Says a force cannot exist with only one object, which is how you know something must be there.",
         "Says a force needs two objects, so something must be there."],
        ["Notes that empty space is not a problem, because the pair does not need anything outside the spacecraft.",
         "Says nothing outside the spacecraft is needed to push against."],
    ],
    "ladder_feedback": {
        "recall": {
            1: "A force cannot be stored or used up. It acts only while two objects interact.",
            2: "Nothing is handed over. The head's push stops when the head and ball separate.",
            3: "Movement is not a force. A force is one object pushing another.",
        },
        "apply": {
            0: "The air does not carry it. The pull is the same with the air pumped away.",
            2: "Something has to lift the paperclip. The magnet's pull does that.",
            3: "A magnet does not use up force. Its pull does not run out.",
        },
    },
}
