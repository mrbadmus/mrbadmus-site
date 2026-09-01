"""P4 lesson 02 — Drawing and adding forces: twelve questions (MRB-223).

Written against Design's page. The tug of war, the sledge on ice and the
three-bar beam are hers.

The discriminations, in the order the lesson builds them:

  · an arrow's LENGTH is the size and its DIRECTION is the direction, so
    two equal arrows are a claim (`FORCE-17`);
  · same way adds, opposite ways subtracts (`FORCE-18`);
  · the resultant points the way of the BIGGER force, and the size alone
    is half an answer;
  · the object responds to the leftover, not to the bigger pull
    (`FORCE-16`) — the harder band sits here;
  · a resultant of 0 N is not the same as no forces (`FORCE-19`).

⚠️ POSITION IS AUTHORED — index cycles 1, 0, 3, 2, giving three of each.

⚠️ Rung 1 (90 N against 34 N) and Rung 2 (two equal arrows on a diagram)
are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "drawing-and-adding-forces"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-02-e01",
        "band": "easier",
        "text": "On a force diagram, what does the LENGTH of an arrow show?",
        "options": [
            {"text": "How long the force lasts", "correct": False,
             "why": "Nothing on a force diagram records time. The length is "
                    "the size of the force."},
            {"text": "How big the force is", "correct": True},
            {"text": "How far the object will travel", "correct": False,
             "why": "A force diagram says nothing about distance. It shows "
                    "the forces acting at one moment."},
            {"text": "Which object the force acts on", "correct": False,
             "why": "That is shown by where the arrow STARTS, not by how "
                    "long it is."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e02",
        "band": "easier",
        "text": "Two forces act on a box in the SAME direction: 12 N and "
                "8 N. What is the resultant?",
        "options": [
            {"text": "20 N in that direction", "correct": True},
            {"text": "4 N in that direction", "correct": False,
             "why": "Subtracting is for forces pointing OPPOSITE ways. These "
                    "point the same way, so they add."},
            {"text": "12 N, because the bigger one wins", "correct": False,
             "why": "The smaller force does not disappear. Pointing the same "
                    "way, it adds to the total."},
            {"text": "96 N", "correct": False,
             "why": "That is 12 × 8. Forces along a line are added or "
                    "subtracted, never multiplied together."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e03",
        "band": "easier",
        "text": "A trolley is pulled right with 50 N and left with 50 N. "
                "What is the resultant force?",
        "options": [
            {"text": "100 N to the right", "correct": False,
             "why": "Adding is for forces pointing the same way. These point "
                    "opposite ways."},
            {"text": "50 N to the right", "correct": False,
             "why": "The left-hand pull cancels the right-hand one exactly. "
                    "Nothing is left over."},
            {"text": "0 N", "correct": True},
            {"text": "50 N to the left", "correct": False,
             "why": "Neither direction wins — the two pulls are the same "
                    "size, so the resultant has no size and no direction."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e04",
        "band": "easier",
        "text": "Which of these is a complete answer for a resultant force?",
        "options": [
            {"text": "15", "correct": False,
             "why": "No unit. Fifteen of what?"},
            {"text": "15 N", "correct": False,
             "why": "The unit is there and the direction is missing. A "
                    "resultant needs all three."},
            {"text": "To the right, because the right-hand pull is the one "
                     "that started first", "correct": False,
             "why": "A direction with no size. How hard is it being pushed?"},
            {"text": "15 N to the right", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-02-s01",
        "band": "standard",
        "text": "A cyclist pedals forwards with 120 N. Air resistance pushes "
                "back with 30 N and friction pushes back with 15 N. What is "
                "the resultant force?",
        "options": [
            {"text": "165 N forwards", "correct": False,
             "why": "That adds all three. The two backwards forces are taken "
                    "AWAY from the forward one."},
            {"text": "75 N forwards", "correct": True},
            {"text": "90 N forwards", "correct": False,
             "why": "That subtracts only the air resistance. The friction is "
                    "still acting and still counts."},
            {"text": "105 N forwards", "correct": False,
             "why": "That subtracts only the friction. Both backwards forces "
                    "cancel part of the pedalling."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s02",
        "band": "standard",
        "text": "On a diagram, a 60 N arrow is drawn 6 cm long. How long "
                "should a 20 N arrow on the SAME diagram be?",
        "options": [
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "2 cm, a third of 6 cm", "correct": True},
            {"text": "6 cm, so the diagram looks tidy", "correct": False,
             "why": "Equal lengths are a claim that the forces are equal. "
                    "Drawing them the same makes the diagram say something "
                    "false."},
            {"text": "18 cm", "correct": False,
             "why": "That is three times as long for a force three times "
                    "SMALLER. The scale has been used upside down."},
            {"text": "Any length, as long as it is shorter", "correct": False,
             "why": "The reader takes the length as the measurement, so the "
                    "same scale has to be used for every arrow."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s03",
        "band": "standard",
        "text": "A tug pulls a barge right with 3 kN while a second pulls it "
                "left with 1 200 N. What is the resultant?",
        "options": [
            {"text": "1 800 N to the left", "correct": False,
             "why": "The size is right and the direction is not. The "
                    "resultant points the way of the BIGGER pull, which is "
                    "the 3 kN one."},
            {"text": "1 197 N to the right", "correct": False,
             "why": "That is 1 200 − 3, subtracting before converting. A "
                    "kilonewton is a thousand newtons."},
            {"text": "4 200 N to the right", "correct": False,
             "why": "That adds them. The two pulls point opposite ways, so "
                    "they subtract."},
            {"text": "1 800 N to the right", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s04",
        "band": "standard",
        "text": "A crate is pushed right with 200 N and dragged left by "
                "180 N of friction. What is the crate actually responding "
                "to?",
        "options": [
            {"text": "200 N, because that is the bigger force",
             "correct": False,
             "why": "180 N of that push is cancelled before anything is left "
                    "over. The crate never feels the whole 200 N as a "
                    "resultant."},
            {"text": "380 N, because both forces act on it", "correct": False,
             "why": "They act in opposite directions, so they subtract "
                    "rather than add."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "20 N to the right, 200 N minus 180 N",
             "correct": True},
            {"text": "20 N, but only once the friction stops",
             "correct": False,
             "why": "The friction never stops while it is sliding. The "
                    "leftover 20 N is what is acting the whole time."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-02-h01",
        "band": "harder",
        "text": "A lift hangs still on a cable. The cable pulls up with "
                "5 000 N and the weight pulls down with 5 000 N. Which "
                "statement is right?",
        "options": [
            {"text": "The resultant is 0 N, and both forces are still "
                     "acting.", "correct": True},
            {"text": "The two forces cancel out, so neither exists any more.",
             "correct": False,
             "why": "Both are still there. Cut the cable and you find out "
                    "how real they both were."},
            {"text": "There are no forces on the lift, because it is not "
                     "moving.", "correct": False,
             "why": "A resultant of 0 N and no forces at all look identical "
                    "from outside and are completely different."},
            {"text": "The resultant is 10 000 N, because both act on the "
                     "lift.", "correct": False,
             "why": "They act in opposite directions on the same object, so "
                    "they subtract to nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h02",
        "band": "harder",
        "text": "A student draws a 40 N arrow and a 25 N arrow pointing "
                "opposite ways, then a 15 N arrow underneath. Why do the two "
                "lower bars on the lesson's beam exactly fill the top one?",
        "options": [
            {"text": "Because 25 N and 15 N make 40 N, which is what the "
                     "subtraction says.", "correct": True},
            {"text": "Because the beam is drawn to fit the space available.",
             "correct": False,
             "why": "Then it would prove nothing. The lengths are derived "
                    "from the newtons, at one scale."},
            {"text": "Because the resultant is always a third of the "
                     "biggest force, whatever the other forces are doing", "correct": False,
             "why": "There is no such rule. Change the 25 N and the leftover "
                    "changes with it."},
            {"text": "Because 40 × 25 gives the length of the third bar.",
             "correct": False,
             "why": "Nothing here is multiplied. That is exactly why this "
                    "relationship gets a beam rather than a triangle."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h03",
        "band": "harder",
        "text": "Two equal and opposite forces act on a steering wheel — "
                "one at each side of the rim. The resultant is 0 N, but the "
                "wheel turns. What does this show?",
        "options": [
            {"text": "That the resultant was not really zero.",
             "correct": False,
             "why": "It is exactly zero. Nothing about the arithmetic is "
                    "wrong."},
            {"text": "That equal and opposite forces sometimes add instead.",
             "correct": False,
             "why": "They still subtract to nothing. What has changed is "
                    "where each one acts."},
            {"text": "That WHERE an arrow starts is part of the diagram, not "
                     "just a place to begin drawing.", "correct": True},
            {"text": "That force diagrams do not work on round objects, "
                     "because there is no flat side for an arrow to start "
                     "from",
             "correct": False,
             "why": "They work perfectly well. The diagram is telling you "
                    "about a second effect a force can have."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h04",
        "band": "harder",
        "text": "A rope pulls a boat forwards at an angle to the water while "
                "the current pushes straight backwards. Why can you not just "
                "subtract the two numbers?",
        "options": [
            {"text": "Because the current is always bigger than the pull a "
                     "rope can give.",
             "correct": False,
             "why": "It need not be bigger at all, and its size is not the "
                    "problem. The method fails whichever is bigger."},
            {"text": "Because one of them is a pull and one is a push, and "
                     "opposites never combine.",
             "correct": False,
             "why": "Pushes and pulls subtract perfectly well when they are "
                    "along one line — that is the whole lesson."},
            {"text": "Because a rope cannot exert a force at an angle, only "
                     "straight ahead.",
             "correct": False,
             "why": "It can, and it does. That is precisely the situation "
                    "being described."},
            {"text": "Because adding and subtracting only works for forces "
                     "along the SAME line.", "correct": True},
        ],
        "figure": None,
    },
]
