"""P4 lesson 01 — What a force is: twelve questions (MRB-223).

Written against Design's page. The wall and the skateboard, the five
interaction cases and the three questions are hers.

The discriminations, in the order the lesson builds them:

  · a force takes TWO objects, and naming one is half an answer;
  · a force is not stuff and does not run out (`FORCE-12`);
  · a surface pushing back is doing something, even though it is not
    alive (`FORCE-13`);
  · some forces act across a gap (`FORCE-14`) — the harder band sits
    here and on the pair-on-different-objects idea;
  · movement, speed and energy are not forces (`FORCE-15`).

⚠️ POSITION IS AUTHORED — index cycles 2, 3, 0, 1, giving three of each.

⚠️ Rung 1 (the header) and Rung 2 (the magnet and the paperclip) are NOT
restated; check 6 of `verify_questions.py` forbids it.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P4"
LESSON = "what-a-force-is"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-01-e01",
        "band": "easier",
        "text": "A force is…",
        "options": [
            {"text": "something an object stores inside it and spends as it "
                     "moves", "correct": False,
             "why": "A force is not stuff and cannot be stored. It exists "
                    "only while two objects are interacting."},
            {"text": "how fast an object is travelling", "correct": False,
             "why": "That is speed. A force is what one object does to "
                    "another, not how quickly it moves."},
            {"text": "a push or a pull on one object, caused by a second "
                     "object", "correct": True},
            {"text": "the movement an object makes", "correct": False,
             "why": "Movement is a result, not the force. The force has to "
                    "be named at both ends."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e02",
        "band": "easier",
        "text": "Forces are measured in…",
        "options": [
            {"text": "kilograms", "correct": False,
             "why": "Kilograms measure mass. A force is measured in newtons, "
                    "and the two are different quantities."},
            {"text": "metres per second", "correct": False,
             "why": "That is a speed. Nothing in it is a force."},
            {"text": "joules", "correct": False,
             "why": "Joules measure energy. A force can be there with no "
                    "energy going anywhere at all — a table holding a book."},
            {"text": "newtons", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e03",
        "band": "easier",
        "text": "Which of these is a complete description of a force?",
        "options": [
            {"text": "The rope pulls the sledge with 200 N.", "correct": True},
            {"text": "There is a force of 200 N on the sledge.",
             "correct": False,
             "why": "That names one object. The second one — whatever is "
                    "doing the pulling — is missing."},
            {"text": "The sledge is moving with 200 N.", "correct": False,
             "why": "Moving is not a force, and a moving object does not "
                    "carry newtons around inside it."},
            {"text": "There is 200 N of force.", "correct": False,
             "why": "Neither object is named, so nothing has been described "
                    "— only a number given."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-e04",
        "band": "easier",
        "text": "About how big is the force of an apple resting on your "
                "hand?",
        "options": [
            {"text": "1 000 N", "correct": False,
             "why": "That is roughly the weight of a small motorbike. An "
                    "apple is about a thousand times less."},
            {"text": "1 N", "correct": True},
            {"text": "100 N", "correct": False,
             "why": "That is about the weight of a ten-year-old child, not "
                    "of an apple."},
            {"text": "0 N", "correct": False,
             "why": "You can feel it, so something is pressing down. A force "
                    "of 0 N would feel like nothing at all."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-01-s01",
        "band": "standard",
        "text": "A swimmer pushes water backwards with their hand and moves "
                "forwards. What pushes the swimmer forwards?",
        "options": [
            {"text": "Their own muscles", "correct": False,
             "why": "Muscles are part of the swimmer, and a force needs a "
                    "SECOND object. The muscles move the arm; the water "
                    "moves the swimmer."},
            {"text": "The lane rope", "correct": False,
             "why": "It is not touched. The forward push comes from the "
                    "thing the hand is pressing on."},
            {"text": "Their own speed", "correct": False,
             "why": "Speed is not an object, so nothing can be on the other "
                    "end of it."},
            {"text": "The water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s02",
        "band": "standard",
        "text": "A book lies still on a table. Which statement is right?",
        "options": [
            {"text": "There are no forces on the book, because nothing is "
                     "happening.", "correct": False,
             "why": "Take the table away and the book falls, which is not "
                    "what happens to an object with no forces on it."},
            {"text": "The table pushes up on the book with the same force "
                     "the book presses down with.", "correct": True},
            {"text": "The table cannot push, because it is not alive.",
             "correct": False,
             "why": "A force needs no effort and no intention. Every surface "
                    "presses back on whatever presses into it."},
            {"text": "Only the book's weight acts, and the table simply gets "
                     "in the way.", "correct": False,
             "why": "Getting in the way IS pushing back. The surface is "
                    "squashed very slightly and pushes."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s03",
        "band": "standard",
        "text": "A tow bar pulls a caravan forwards with about 2 000 N. What "
                "does the caravan do to the tow bar?",
        "options": [
            {"text": "Nothing — the tow bar is the one doing the pulling.",
             "correct": False,
             "why": "Forces come in pairs. If the bar pulls the caravan, the "
                    "caravan pulls the bar."},
            {"text": "It pushes the tow bar forwards with about 2 000 N.",
             "correct": False,
             "why": "The size is right and the direction is wrong. The pair "
                    "acts in OPPOSITE directions."},
            {"text": "It pulls back along the bar with about 2 000 N.",
             "correct": True},
            {"text": "It pulls back, but with much less force, because it is "
                     "being dragged.", "correct": False,
             "why": "The two forces in a pair are the same size, whichever "
                    "object is winning."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-s04",
        "band": "standard",
        "text": "A footballer kicks a ball. The boot and the ball are in "
                "contact for about a hundredth of a second. What is the "
                "force on the ball once the boot has left it?",
        "options": [
            {"text": "The boot's push, still acting until the ball slows "
                     "down.", "correct": False,
             "why": "The boot's push stops existing the moment they "
                    "separate. Nothing was handed over."},
            {"text": "The force the ball was given, gradually running out.",
             "correct": False,
             "why": "A force is not a supply. The ball keeps its speed, not "
                    "a force."},
            {"text": "No force from the boot at all — only the air and the "
                     "Earth act on it.", "correct": True},
            {"text": "The force is in the ball's movement, so it acts on "
                     "nothing and needs no second object", "correct": False,
             "why": "Movement is not a force. Every force on the ball has a "
                    "second object at the other end of it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-01-h01",
        "band": "harder",
        "text": "The Earth pulls the Moon with about 200 billion billion N. "
                "How hard does the Moon pull the Earth?",
        "options": [
            {"text": "With the same force, about 200 billion billion N.",
             "correct": True},
            {"text": "Much less, because the Moon is much smaller.",
             "correct": False,
             "why": "Size does not split the pair. The two forces in an "
                    "interaction are always the same size."},
            {"text": "Not at all — only the bigger object pulls.",
             "correct": False,
             "why": "Then the force would have only one object, which is not "
                    "possible. Tides are the Moon's pull, arriving."},
            {"text": "It depends on which one is moving.", "correct": False,
             "why": "The pair is the same size whether either is moving or "
                    "not. Motion is not part of the description."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h02",
        "band": "harder",
        "text": "If the two forces in every pair are equal and opposite, why "
                "does anything ever move?",
        "options": [
            {"text": "Because one of the pair is always slightly bigger.",
             "correct": False,
             "why": "They are exactly equal. Nothing about the pair is "
                    "uneven."},
            {"text": "Because the two forces act on DIFFERENT objects, and "
                     "only forces on the same object can cancel.",
             "correct": True},
            {"text": "Because the pair only exists while the objects are "
                     "touching.", "correct": False,
             "why": "The pair exists across a gap too — the Earth and the "
                    "Moon — and things still move."},
            {"text": "Because one of the forces is used up in moving the "
                     "object, leaving the other to act alone", "correct": False,
             "why": "Nothing is used up. Both forces act for exactly as long "
                    "as the interaction lasts."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h03",
        "band": "harder",
        "text": "A magnet lifts a paperclip across a two-centimetre gap. The "
                "air is then pumped out of the gap. What happens to the "
                "pull?",
        "options": [
            {"text": "It stops, because there is nothing left to carry it.",
             "correct": False,
             "why": "The gap does not need filling. This is the whole point "
                    "of a non-contact force."},
            {"text": "It gets weaker, because the air was helping.",
             "correct": False,
             "why": "The air was doing nothing for the magnetism. Removing "
                    "it changes nothing about the pull."},
            {"text": "It is exactly the same.", "correct": True},
            {"text": "It gets stronger, because nothing is in the way any "
                     "more.", "correct": False,
             "why": "The air was never in the way. The pull is unchanged in "
                    "both directions."},
        ],
        "figure": None,
    },
    {
        "id": "p4-01-h04",
        "band": "harder",
        "text": "A rocket in deep space fires its engine and speeds up, with "
                "nothing around it. Which pair of objects is the force "
                "between?",
        "options": [
            {"text": "The rocket and space itself.", "correct": False,
             "why": "Space is not an object and cannot be one end of a "
                    "force. Something with mass has to be thrown."},
            {"text": "The rocket and the planet it left.", "correct": False,
             "why": "That pull is real but it acts towards the planet, and "
                    "it is not what the engine is doing."},
            {"text": "The rocket and its own fuel tank.", "correct": False,
             "why": "The tank is part of the rocket. A force needs a second "
                    "object, not another part of the first one."},
            {"text": "The rocket and the exhaust gas it throws backwards.",
             "correct": True},
        ],
        "figure": None,
    },
]
