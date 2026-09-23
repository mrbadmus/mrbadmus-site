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
        "text": "Look at the diagram. Why do the two lower bars exactly "
                "fill the top one?",
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
        "figure": "p4-resultant-beam-recap",
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-02-e05",
        "band": "easier",
        "text": "Where should a force arrow start on a diagram?",
        "options": [
            {"text": "At the edge of the page, pointing inwards",
             "correct": False,
             "why": "The arrow belongs to the object, not to the page, so it "
                    "starts on the object."},
            {"text": "On the object the force is acting on", "correct": True},
            {"text": "On the object causing the force", "correct": False,
             "why": "That would draw the force on the wrong body of the "
                    "pair — each arrow goes on the object being pushed."},
            {"text": "Anywhere, as long as it points the right way",
             "correct": False,
             "why": "Where it starts says what the force acts on, so it "
                    "cannot go just anywhere."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e06",
        "band": "easier",
        "text": "A sledge is pulled right with 30 N while friction pushes "
                "left with 12 N. What is the resultant force?",
        "options": [
            {"text": "42 N to the right", "correct": False,
             "why": "Forces along a line only add when they point the same "
                    "way. These point opposite ways."},
            {"text": "18 N to the left", "correct": False,
             "why": "The size is right but the direction is not: what is left "
                    "over points the way the larger force points."},
            {"text": "18 N to the right", "correct": True},
            {"text": "0 N, because the forces cancel", "correct": False,
             "why": "They only cancel when they are equal, and 30 N is not "
                    "12 N."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-02-s05",
        "band": "standard",
        "text": "A crate is pushed right with 100 N while friction pushes "
                "left with 40 N and a second person pulls left with 25 N. "
                "What is the resultant?",
        "options": [
            {"text": "165 N to the right", "correct": False,
             "why": "That adds all three. Only forces pointing the same way "
                    "add; the two leftward ones subtract."},
            {"text": "35 N to the right", "correct": True},
            {"text": "60 N to the right", "correct": False,
             "why": "That leaves out the 25 N pull, and every force along the "
                    "line has to be counted."},
            {"text": "35 N to the left", "correct": False,
             "why": "The size is right, but 100 N is larger than 65 N, so "
                    "what is left over points right."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s06",
        "band": "standard",
        "text": "On a scale diagram a 20 N arrow is drawn 4 cm long. How long "
                "should a 50 N arrow be on the same diagram?",
        "options": [
            {"text": "4 cm, because all arrows on one diagram match",
             "correct": False,
             "why": "Equal lengths would say the forces are equal, and these "
                    "are not."},
            {"text": "34 cm", "correct": False,
             "why": "That is 50 − 20 + 4. The scale is a multiplication, not "
                    "a difference."},
            {"text": "1.6 cm", "correct": False,
             "why": "That is the scale used upside down; a larger force needs "
                    "a longer arrow, not a shorter one."},
            {"text": "10 cm", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-02-h05",
        "band": "harder",
        "text": "A falling parachutist has 700 N of weight down and, once the "
                "canopy opens, 760 N of drag up. What is the resultant, and "
                "what happens?",
        "options": [
            {"text": "60 N upwards, so the fall slows down", "correct": True},
            {"text": "60 N upwards, so the parachutist is pushed back up into "
                     "the sky",
             "correct": False,
             "why": "A resultant against the motion slows it; it does not "
                    "reverse it while the fall continues."},
            {"text": "1460 N upwards, because the two forces add",
             "correct": False,
             "why": "They point in opposite directions, so they subtract "
                    "rather than add."},
            {"text": "0 N, because the parachute has taken over",
             "correct": False,
             "why": "It is 0 N only once the drag has fallen back to 700 N, "
                    "which happens a little later."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h06",
        "band": "harder",
        "text": "Why is a resultant of 0 N not the same as having no forces "
                "at all?",
        "options": [
            {"text": "Because a resultant of 0 N can only happen when nothing "
                     "is touching the object",
             "correct": False,
             "why": "It is most common when things ARE touching — a book on a "
                    "table is the standard case."},
            {"text": "Because the forces are still acting; they only cancel "
                     "in their effect on the motion",
             "correct": True},
            {"text": "Because 0 N is only ever an approximation to the real "
                     "total",
             "correct": False,
             "why": "It can be exactly zero, and a book that stays put shows "
                    "that it is."},
            {"text": "Because forces cannot be added together in the first "
                     "place",
             "correct": False,
             "why": "Along one line they add and subtract perfectly well; "
                    "that is how a resultant is found."},
        ],
        "figure": None,
    },
    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-02-e07",
        "band": "easier",
        "text": "Which part of a force arrow shows the direction of the "
                "force?",
        "options": [
            {"text": "Where it is on the page", "correct": False,
             "why": "Where it starts says which object is being pushed, and "
                    "that is not the same as which way it acts."},
            {"text": "How long it is drawn", "correct": False,
             "why": "The length is the size of the force in newtons, not its "
                    "direction."},
            {"text": "How thick the line is", "correct": False,
             "why": "Thickness carries no meaning at all on a force diagram."},
            {"text": "The way it points", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e08",
        "band": "easier",
        "text": "A sledge feels a 25 N push and a 15 N push, both towards the "
                "finish line. How big is the single force that would do the "
                "same job?",
        "options": [
            {"text": "10 N in that direction", "correct": False,
             "why": "Subtracting is for forces pointing opposite ways. These "
                    "point the same way."},
            {"text": "40 N in that direction", "correct": True},
            {"text": "25 N, as the bigger one wins", "correct": False,
             "why": "The 15 N does not vanish. Pointing the same way, it adds "
                    "to the total."},
            {"text": "375 N in that direction", "correct": False,
             "why": "That is 25 × 15. Forces along a line are added or "
                    "subtracted, never multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e09",
        "band": "easier",
        "text": "An 85 N shove to the right meets a 30 N drag to the left on a "
                "wooden box. Give the resultant.",
        "options": [
            {"text": "115 N to the right", "correct": False,
             "why": "Adding is for forces pointing the same way, and these "
                    "point opposite ways."},
            {"text": "55 N to the left", "correct": False,
             "why": "The size is right and the direction is not. The resultant "
                    "follows the bigger force."},
            {"text": "55 N to the right", "correct": True},
            {"text": "85 N to the right", "correct": False,
             "why": "The 30 N cancels part of the push before anything is left "
                    "over."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e10",
        "band": "easier",
        "text": "The single force that would have exactly the same effect as "
                "all the forces acting is called the...",
        "options": [
            {"text": "biggest force", "correct": False,
             "why": "The biggest force is only one of them. The single "
                    "replacement is what is left after they combine."},
            {"text": "total weight", "correct": False,
             "why": "Weight is the pull of gravity, which is just one of the "
                    "forces that might be acting."},
            {"text": "starting force", "correct": False,
             "why": "There is no such quantity. Which force came first makes "
                    "no difference."},
            {"text": "resultant force", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e11",
        "band": "easier",
        "text": "On one diagram, two arrows are drawn 4 cm and 8 cm long. "
                "What does that say about the two forces?",
        "options": [
            {"text": "The second force is twice the size of the first",
             "correct": True},
            {"text": "It lasts twice as long", "correct": False,
             "why": "Nothing on a force diagram records time."},
            {"text": "The second force is half the size of the first",
             "correct": False,
             "why": "The longer arrow is the bigger force, so it is the other "
                    "way round."},
            {"text": "The second force acts twice as far away",
             "correct": False,
             "why": "Length is the size of the force, not a distance."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e12",
        "band": "easier",
        "text": "What unit is a resultant force given in?",
        "options": [
            {"text": "Kilograms", "correct": False,
             "why": "Kilograms measure mass. Every force, including a "
                    "resultant, is in newtons."},
            {"text": "Metres per second", "correct": False,
             "why": "That is a speed, and a resultant is a force."},
            {"text": "Newtons", "correct": True},
            {"text": "Centimetres", "correct": False,
             "why": "Centimetres measure the arrow on the paper, not the force "
                    "itself."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e13",
        "band": "easier",
        "text": "A rope pulls a raft to the right with 45 N. Nothing pulls it "
                "to the left. What is the resultant?",
        "options": [
            {"text": "0 N, since a single rope cannot do it", "correct": False,
             "why": "One force on its own is the resultant. Nothing has to "
                    "cancel it."},
            {"text": "45 N to the right", "correct": True},
            {"text": "90 N to the right", "correct": False,
             "why": "There is nothing to double. Only one force is acting."},
            {"text": "45 N in both directions", "correct": False,
             "why": "A resultant has one size and one direction, never two."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e14",
        "band": "easier",
        "text": "How many newtons are there in one kilonewton?",
        "options": [
            {"text": "10", "correct": False,
             "why": "That is the prefix deci- rather than kilo-. A kilo is a "
                    "thousand."},
            {"text": "100", "correct": False,
             "why": "A hundred newtons is a tenth of a kilonewton."},
            {"text": "1 000", "correct": True},
            {"text": "1 000 000", "correct": False,
             "why": "That is a meganewton, a thousand times too many."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e15",
        "band": "easier",
        "text": "Forces along one line that point the SAME way are...",
        "options": [
            {"text": "ignored, since just one of them acts", "correct": False,
             "why": "Any number of forces can act at once, and every one of "
                    "them counts."},
            {"text": "subtracted from each other", "correct": False,
             "why": "Subtracting is what happens when they point opposite "
                    "ways."},
            {"text": "multiplied together", "correct": False,
             "why": "Nothing about combining forces along a line is a "
                    "multiplication."},
            {"text": "added together", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e16",
        "band": "easier",
        "text": "Forces along one line that point OPPOSITE ways are...",
        "options": [
            {"text": "added together", "correct": False,
             "why": "Adding is for forces pointing the same way. Opposite ways "
                    "means one cancels part of the other."},
            {"text": "always equal to zero", "correct": False,
             "why": "Only when the two are the same size. Otherwise something "
                    "is left over."},
            {"text": "divided by each other", "correct": False,
             "why": "There is no division anywhere in combining forces along a "
                    "line."},
            {"text": "subtracted", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e17",
        "band": "easier",
        "text": "A tractor pulls forward with 900 N while mud drags backwards "
                "with 900 N. What is the resultant?",
        "options": [
            {"text": "1 800 N forwards", "correct": False,
             "why": "Adding is for forces the same way. These oppose each "
                    "other."},
            {"text": "900 N forwards", "correct": False,
             "why": "The mud cancels the pull exactly, so nothing at all is "
                    "left over."},
            {"text": "0 N", "correct": True},
            {"text": "900 N backwards", "correct": False,
             "why": "Neither direction wins, because the two forces are the "
                    "same size."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e18",
        "band": "easier",
        "text": "Why must a resultant force always be given with a direction?",
        "options": [
            {"text": "Because a force acts one particular way, and the size "
                     "alone does not say which", "correct": True},
            {"text": "Because the direction tells you how big the force is",
             "correct": False,
             "why": "The size is a separate piece of information, given in "
                    "newtons."},
            {"text": "Because every resultant force points to the right",
             "correct": False,
             "why": "A resultant can point either way along the line, "
                    "depending on which force is bigger."},
            {"text": "Because the direction is what the newton measures",
             "correct": False,
             "why": "The newton measures the size. Direction is written "
                    "separately in words."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e19",
        "band": "easier",
        "text": "A 10 N arrow is drawn 2 cm long. What scale is being used?",
        "options": [
            {"text": "1 cm for every 20 N", "correct": False,
             "why": "At that scale 10 N would be half a centimetre, not two."},
            {"text": "1 cm for every 5 N", "correct": True},
            {"text": "1 cm for every 10 N", "correct": False,
             "why": "At that scale a 10 N arrow would be exactly 1 cm long."},
            {"text": "1 cm for every 2 N", "correct": False,
             "why": "At that scale a 10 N arrow would be 5 cm long."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e20",
        "band": "easier",
        "text": "Two forces of 20 N act on a trolley in opposite directions. "
                "What arrow would you draw for the resultant?",
        "options": [
            {"text": "A short arrow, to show a small resultant",
             "correct": False,
             "why": "A zero-length arrow is not a small arrow. There is "
                    "nothing at all to draw."},
            {"text": "A 40 N arrow", "correct": False,
             "why": "They point opposite ways, so they subtract to nothing "
                    "rather than adding."},
            {"text": "No arrow at all", "correct": True},
            {"text": "Two arrows, one for each force", "correct": False,
             "why": "The resultant is one single arrow by definition, and here "
                    "it has no length."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e21",
        "band": "easier",
        "text": "A resultant force of 0 N means that...",
        "options": [
            {"text": "no forces are acting on the object at all",
             "correct": False,
             "why": "Forces can be acting and still cancel. A rope under "
                    "tension can snap at a resultant of 0 N."},
            {"text": "the forces cancel and nothing is left over",
             "correct": True},
            {"text": "the forces are too small to be measured",
             "correct": False,
             "why": "They can be enormous. What matters is that they cancel."},
            {"text": "a single force is acting on the object",
             "correct": False,
             "why": "A single force is its own resultant, so it could not give "
                    "0 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e22",
        "band": "easier",
        "text": "A box feels 50 N to the right, 20 N to the left and another "
                "10 N to the left. Give the single force left over.",
        "options": [
            {"text": "80 N to the right", "correct": False,
             "why": "That adds all three. Only forces pointing the same way "
                    "add together."},
            {"text": "30 N to the right", "correct": False,
             "why": "That leaves out the 10 N. Every force along the line has "
                    "to be counted."},
            {"text": "20 N to the left", "correct": False,
             "why": "The size is right and the direction is not. The 50 N is "
                    "bigger than the other two together."},
            {"text": "20 N to the right", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e23",
        "band": "easier",
        "text": "A 2 kN pull and a 500 N pull act in the same direction. What "
                "has to happen before they are added?",
        "options": [
            {"text": "The 500 N must be changed into 0.5 kg",
             "correct": False,
             "why": "Kilograms measure mass. The two forces stay forces."},
            {"text": "Nothing: 2 and 500 can be added as they stand",
             "correct": False,
             "why": "They are in different units, so adding the numbers gives "
                    "a meaningless answer."},
            {"text": "The 2 kN must be changed into 2 000 N", "correct": True},
            {"text": "The 2 kN must be changed into 200 N", "correct": False,
             "why": "A kilonewton is a thousand newtons, so 2 kN is 2 000 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e24",
        "band": "easier",
        "text": "Are '25 N to the left' and '25 N to the right' the same "
                "answer?",
        "options": [
            {"text": "Yes, the sizes match", "correct": False,
             "why": "Size is only part of a force. The two point opposite ways "
                    "and would do opposite things."},
            {"text": "Yes, because direction is just a label",
             "correct": False,
             "why": "Direction is part of the measurement, not a label added "
                    "afterwards."},
            {"text": "No, they are different answers", "correct": True},
            {"text": "No, because the sizes must also differ",
             "correct": False,
             "why": "The sizes are identical. It is the direction alone that "
                    "separates them."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e25",
        "band": "easier",
        "text": "Which of these pairs of forces gives the biggest resultant "
                "on a trolley?",
        "options": [
            {"text": "60 N right and 20 N left", "correct": False,
             "why": "Opposite ways, so they subtract: that leaves 40 N."},
            {"text": "50 N right and 10 N right", "correct": True},
            {"text": "30 N right and 30 N left", "correct": False,
             "why": "Equal and opposite, so the resultant is 0 N."},
            {"text": "45 N right and 15 N left", "correct": False,
             "why": "Opposite ways, so they subtract: that leaves 30 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e26",
        "band": "easier",
        "text": "A crate is pulled right with 55 N and left with 35 N. Which "
                "way does the resultant point?",
        "options": [
            {"text": "To the right", "correct": True},
            {"text": "To the left", "correct": False,
             "why": "The resultant follows the bigger force, and 55 N is the "
                    "bigger one."},
            {"text": "Neither way, as they cancel", "correct": False,
             "why": "They only cancel completely when they are equal, and "
                    "these are not."},
            {"text": "Both ways at once", "correct": False,
             "why": "A resultant is one single force with one direction."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e27",
        "band": "easier",
        "text": "Two unequal forces are being drawn on one diagram. Which "
                "rule applies?",
        "options": [
            {"text": "Draw both the same length, and write the sizes on",
             "correct": False,
             "why": "Equal lengths claim equal forces, and the drawing would "
                    "then contradict the labels."},
            {"text": "Draw the bigger force with the longer arrow",
             "correct": True},
            {"text": "Draw the bigger force with the thicker arrow",
             "correct": False,
             "why": "Thickness means nothing. Length is what carries the "
                    "size."},
            {"text": "Draw the first force longer, whichever it is",
             "correct": False,
             "why": "Order has nothing to do with it. Length follows size and "
                    "nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e28",
        "band": "easier",
        "text": "A crate slides across a floor with 12 N of friction acting "
                "to the left and no other force along the line. What is the "
                "resultant?",
        "options": [
            {"text": "0 N, as friction cannot act alone", "correct": False,
             "why": "It certainly can, and then it is the only force in the "
                    "sum."},
            {"text": "12 N to the right", "correct": False,
             "why": "Friction acts to the left here, and a single force IS the "
                    "resultant."},
            {"text": "24 N to the left", "correct": False,
             "why": "Nothing doubles. There is only one force acting."},
            {"text": "12 N to the left", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e29",
        "band": "easier",
        "text": "A boat is pushed 3 N to the east and 9 N to the west. What "
                "is the resultant?",
        "options": [
            {"text": "12 N to the west", "correct": False,
             "why": "Adding is for forces the same way. East and west are "
                    "opposite."},
            {"text": "6 N to the east", "correct": False,
             "why": "The size is right and the direction is not. The 9 N is "
                    "the bigger force."},
            {"text": "6 N to the west", "correct": True},
            {"text": "3 N to the west", "correct": False,
             "why": "That is one of the two forces rather than what is left "
                    "after they combine."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-e30",
        "band": "easier",
        "text": "Why is every arrow on a force diagram labelled with its size "
                "in newtons?",
        "options": [
            {"text": "So the reader does not have to estimate from the "
                     "drawing", "correct": True},
            {"text": "So the arrows can all be drawn the same length",
             "correct": False,
             "why": "A label does not excuse a false drawing. The length still "
                    "has to match the size."},
            {"text": "So the diagram shows how long each force lasts",
             "correct": False,
             "why": "Newtons measure size, not time, and time is not shown at "
                    "all."},
            {"text": "So the reader knows which object is being pushed",
             "correct": False,
             "why": "That is shown by where the arrow starts, not by the "
                    "label."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-02-s07",
        "band": "standard",
        "text": "A car engine pushes a car forwards with 2 400 N while drag "
                "pushes backwards with 900 N. What is the resultant?",
        "options": [
            {"text": "3 300 N forwards", "correct": False,
             "why": "That adds them. The two point opposite ways, so they "
                    "subtract."},
            {"text": "1 500 N forwards", "correct": True},
            {"text": "1 500 N backwards", "correct": False,
             "why": "The size is right and the direction is not: the resultant "
                    "follows the 2 400 N push."},
            {"text": "2 400 N forwards", "correct": False,
             "why": "The drag cancels 900 N of the push before anything is "
                    "left over."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s08",
        "band": "standard",
        "text": "A 1.5 kN pull acts to the right on a trailer and a 700 N "
                "pull acts to the left. What is the resultant?",
        "options": [
            {"text": "800 N to the left", "correct": False,
             "why": "The size is right and the direction is not. 1 500 N is "
                    "the bigger pull."},
            {"text": "698.5 N to the left", "correct": False,
             "why": "That subtracts 1.5 from 700 without converting. A "
                    "kilonewton is a thousand newtons."},
            {"text": "2 200 N to the right", "correct": False,
             "why": "That adds them, and forces pointing opposite ways "
                    "subtract."},
            {"text": "800 N to the right", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s09",
        "band": "standard",
        "text": "A scale of 3 cm to every 15 N is used throughout one diagram. "
                "What length represents 45 N?",
        "options": [
            {"text": "3 cm", "correct": False,
             "why": "Equal lengths would claim the two forces are equal, and "
                    "45 N is three times 15 N."},
            {"text": "33 cm", "correct": False,
             "why": "That is 45 − 15 + 3. The scale is a multiplication, not a "
                    "difference."},
            {"text": "1 cm", "correct": False,
             "why": "That is the scale used upside down: a bigger force needs "
                    "a longer arrow."},
            {"text": "9 cm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s10",
        "band": "standard",
        "text": "A sledge is dragged right with 70 N while two children pull "
                "left with 25 N and 15 N. What is the resultant?",
        "options": [
            {"text": "110 N to the right", "correct": False,
             "why": "That adds all three. Only forces pointing the same way "
                    "add."},
            {"text": "45 N to the right", "correct": False,
             "why": "That subtracts the 25 N only. The 15 N is acting as "
                    "well."},
            {"text": "30 N to the right", "correct": True},
            {"text": "30 N to the left", "correct": False,
             "why": "The size is right and the direction is not: 70 N beats "
                    "40 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s11",
        "band": "standard",
        "text": "A student draws a 30 N arrow and a 45 N arrow the same "
                "length. What has the diagram now claimed?",
        "options": [
            {"text": "That the two forces are equal, which they are not",
             "correct": True},
            {"text": "That the two forces act on different objects",
             "correct": False,
             "why": "Which object is acted on is shown by where each arrow "
                    "starts, not by its length."},
            {"text": "That the drawing is neat and needs no labels",
             "correct": False,
             "why": "Tidiness is not a claim. The lengths still state the "
                    "sizes, truly or falsely."},
            {"text": "That one force lasts longer", "correct": False,
             "why": "Nothing on a force diagram records how long a force "
                    "lasts."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s12",
        "band": "standard",
        "text": "Two ropes pull a crate to the right with 90 N and 60 N. On a "
                "scale of 1 cm to 30 N, what single arrow replaces them?",
        "options": [
            {"text": "30 N to the right, drawn 1 cm long", "correct": False,
             "why": "That subtracts them. Both pull the same way, so they "
                    "add."},
            {"text": "150 N to the right, drawn 5 cm long", "correct": True},
            {"text": "150 N to the right, drawn 150 cm long",
             "correct": False,
             "why": "The scale is 1 cm for every 30 N, so 150 N is 5 cm."},
            {"text": "90 N to the right, drawn 3 cm long", "correct": False,
             "why": "The 60 N rope does not stop pulling because it is the "
                    "smaller one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s13",
        "band": "standard",
        "text": "Why does the resultant point the way the bigger force "
                "points?",
        "options": [
            {"text": "Because the bigger force always acts for longer",
             "correct": False,
             "why": "Time plays no part in it. Both act at the same moment."},
            {"text": "Because the bigger force is nearer to the object",
             "correct": False,
             "why": "Both act on the same object, and distance is not part of "
                    "the sum."},
            {"text": "Because the smaller force stops acting the moment the "
                     "bigger one starts to win the contest", "correct": False,
             "why": "It goes on acting the whole time, cancelling its own "
                    "share of the bigger one."},
            {"text": "Because the smaller force cancels only part of it, and "
                     "the rest is left over", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s14",
        "band": "standard",
        "text": "A trolley has 220 N to the right and 220 N to the left. A "
                "student writes 'resultant = 0 N to the right'. What is "
                "wrong?",
        "options": [
            {"text": "The size should be 440 N", "correct": False,
             "why": "Opposite forces subtract, so the size of 0 N is right."},
            {"text": "A resultant of 0 N never has a direction to give",
             "correct": True},
            {"text": "The direction should be to the left", "correct": False,
             "why": "Neither direction is correct, because there is no "
                    "resultant left to point anywhere."},
            {"text": "The unit should be kilograms", "correct": False,
             "why": "Forces are in newtons; kilograms measure mass."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s15",
        "band": "standard",
        "text": "A student converts 0.8 kN into 80 N and then subtracts "
                "300 N. What has gone wrong?",
        "options": [
            {"text": "0.8 kN is 800 N, so the conversion is out by ten times",
             "correct": True},
            {"text": "0.8 kN cannot be converted into newtons at all",
             "correct": False,
             "why": "It converts perfectly well: multiply the kilonewtons by "
                    "1 000."},
            {"text": "The 300 N should have been converted instead",
             "correct": False,
             "why": "The 300 N is already in newtons and needs nothing doing "
                    "to it."},
            {"text": "Subtracting is the wrong operation to use in a problem "
                     "like this one", "correct": False,
             "why": "Whether to subtract depends on the directions, and the "
                    "error here is in the conversion."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s16",
        "band": "standard",
        "text": "Two forces act on a barge along one line: 5 kN to the east "
                "and 3 500 N to the west. What is the resultant?",
        "options": [
            {"text": "8 500 N to the east", "correct": False,
             "why": "That adds them, and east against west means they "
                    "subtract."},
            {"text": "1 500 N to the west", "correct": False,
             "why": "The size is right and the direction is not: 5 000 N beats "
                    "3 500 N."},
            {"text": "3 495 N to the west", "correct": False,
             "why": "That subtracts 5 from 3 500 before converting the "
                    "kilonewtons."},
            {"text": "1 500 N to the east", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s17",
        "band": "standard",
        "text": "One diagram shows a 12 N arrow 3 cm long and a 20 N arrow "
                "4 cm long. Why is the diagram wrong?",
        "options": [
            {"text": "The two arrows are not drawn to one scale",
             "correct": True},
            {"text": "Force arrows should never be measured in centimetres",
             "correct": False,
             "why": "A scale drawing is exactly how arrows are set out; the "
                    "problem is that the scale changes."},
            {"text": "The 20 N arrow should be the shorter of the two",
             "correct": False,
             "why": "The bigger force takes the longer arrow, so its being "
                    "longer is right."},
            {"text": "Two forces should never be drawn on one diagram",
             "correct": False,
             "why": "Every force acting is drawn, and that is the point of the "
                    "diagram."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s18",
        "band": "standard",
        "text": "A student says a resultant of 25 N means the object travels "
                "at 25 metres per second. What is wrong?",
        "options": [
            {"text": "The resultant should have been 25 kg instead",
             "correct": False,
             "why": "Kilograms are a mass. A resultant is a force, in "
                    "newtons."},
            {"text": "A force is not a speed: it says how hard, not how fast",
             "correct": True},
            {"text": "The speed would be 25 newtons per second",
             "correct": False,
             "why": "There is no such unit, and a force still is not a speed."},
            {"text": "Nothing is wrong, as long as the units are written on",
             "correct": False,
             "why": "Writing the unit does not turn a force into a speed. They "
                    "are different quantities."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s19",
        "band": "standard",
        "text": "A wheelie bin is shoved to the right with 300 N. Friction "
                "takes 120 N off it to the left, and a helper hauls left "
                "with 80 N. What is the resultant?",
        "options": [
            {"text": "500 N to the right", "correct": False,
             "why": "That adds all three. Only forces pointing the same way "
                    "add together."},
            {"text": "180 N to the right", "correct": False,
             "why": "That leaves out the 80 N pull, and every force on the "
                    "line counts."},
            {"text": "100 N to the right", "correct": True},
            {"text": "100 N to the left", "correct": False,
             "why": "The size is right and the direction is not: 300 N beats "
                    "200 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s20",
        "band": "standard",
        "text": "A sledge on ice has a 45 N pull right and a 45 N pull left, "
                "and both ropes are taut. Which statement is right?",
        "options": [
            {"text": "The ropes are slack, because the resultant is 0 N",
             "correct": False,
             "why": "A resultant of 0 N says nothing about the ropes being "
                    "slack; they are under full tension."},
            {"text": "The resultant is 90 N, because both ropes are pulling",
             "correct": False,
             "why": "They pull opposite ways, so they subtract to nothing."},
            {"text": "The resultant is 45 N, because one rope must win",
             "correct": False,
             "why": "Neither wins. Equal opposite pulls leave nothing over."},
            {"text": "The resultant is 0 N, and each rope is under 45 N of "
                     "tension", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s21",
        "band": "standard",
        "text": "A push of 3.2 kN acts right while a rope drags 800 N left. A "
                "student answers '2 400 N to the left'. What is the single "
                "error?",
        "options": [
            {"text": "The size, which should be 4 000 N", "correct": False,
             "why": "That adds them. Opposite directions subtract, so 2 400 N "
                    "is the right size."},
            {"text": "The conversion, as 3.2 kN is 320 N", "correct": False,
             "why": "A kilonewton is a thousand newtons, so 3.2 kN is "
                    "3 200 N."},
            {"text": "The direction, as the resultant follows the bigger "
                     "force", "correct": True},
            {"text": "The unit, which should have been given in kilonewtons "
                     "throughout", "correct": False,
             "why": "Newtons are perfectly correct for an answer of this "
                    "size."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s22",
        "band": "standard",
        "text": "A lawnmower is pushed forwards with 110 N while the grass "
                "drags it back with 45 N. What is the resultant?",
        "options": [
            {"text": "155 N forwards", "correct": False,
             "why": "That adds them, and the two point opposite ways."},
            {"text": "65 N backwards", "correct": False,
             "why": "The size is right and the direction is not. The 110 N "
                    "push is bigger."},
            {"text": "110 N forwards", "correct": False,
             "why": "The grass cancels 45 N of the push before anything is "
                    "left over."},
            {"text": "65 N forwards", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s23",
        "band": "standard",
        "text": "A student draws a resultant arrow longer than both of the "
                "forces that made it, and those forces point opposite ways. "
                "Why must that be wrong?",
        "options": [
            {"text": "Because a resultant arrow is always drawn 1 cm long",
             "correct": False,
             "why": "It is drawn to the same scale as the forces, whatever "
                    "length that gives."},
            {"text": "Because subtracting leaves less than the bigger force, "
                     "never more", "correct": True},
            {"text": "Because a resultant is never drawn on the same diagram",
             "correct": False,
             "why": "It is drawn, usually on its own baseline, and to the same "
                    "scale."},
            {"text": "Because a resultant is always smaller than both of the "
                     "forces that produced it", "correct": False,
             "why": "It is smaller than the bigger one, but it can easily be "
                    "larger than the smaller one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s24",
        "band": "standard",
        "text": "On a diagram drawn at 1 cm to 10 N, the pull right is 7 cm "
                "and the pull left is 3 cm. What is the resultant?",
        "options": [
            {"text": "4 cm to the right", "correct": False,
             "why": "The answer to a force question is a force. Four "
                    "centimetres is the arrow, not the resultant."},
            {"text": "100 N to the right", "correct": False,
             "why": "That adds the two lengths rather than taking one from the "
                    "other."},
            {"text": "40 N to the right", "correct": True},
            {"text": "40 N to the left", "correct": False,
             "why": "The size is right and the direction is not. The longer "
                    "arrow points right."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s25",
        "band": "standard",
        "text": "Two forces along one line give a resultant of 22 N to the "
                "right. One of them is 34 N to the right. What is the other?",
        "options": [
            {"text": "12 N to the left", "correct": True},
            {"text": "12 N to the right", "correct": False,
             "why": "Two rightward forces would add to 46 N rather than "
                    "leaving 22 N."},
            {"text": "56 N to the left", "correct": False,
             "why": "That would leave 22 N pointing left instead, which is the "
                    "wrong way."},
            {"text": "22 N to the left", "correct": False,
             "why": "That would cancel 22 N of the 34 N and leave 12 N, not "
                    "22 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s26",
        "band": "standard",
        "text": "A student writes a resultant force as '35'. What two things "
                "are missing?",
        "options": [
            {"text": "The scale used and the size of the diagram",
             "correct": False,
             "why": "Neither belongs in the answer. A resultant is a size, a "
                    "unit and a direction."},
            {"text": "The unit and the object's speed", "correct": False,
             "why": "A speed is a different quantity and is not part of "
                    "stating a force."},
            {"text": "The direction and how long the force lasts",
             "correct": False,
             "why": "Time is not part of stating a resultant; the unit is."},
            {"text": "The unit and the direction", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s27",
        "band": "standard",
        "text": "A 60 N force and a 25 N force both act on a box along one "
                "line. What are the two possible resultants?",
        "options": [
            {"text": "85 N or 35 N, depending on the directions",
             "correct": True},
            {"text": "85 N, as forces add", "correct": False,
             "why": "They add only when they point the same way. Opposite "
                    "directions subtract."},
            {"text": "35 N, because forces subtract", "correct": False,
             "why": "They subtract only when they oppose each other. The same "
                    "way, they add."},
            {"text": "1 500 N or 2.4 N, from multiplying or dividing",
             "correct": False,
             "why": "Forces along a line are never multiplied or divided "
                    "together."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s28",
        "band": "standard",
        "text": "Why is it wrong to draw a very short arrow when the "
                "resultant is 0 N?",
        "options": [
            {"text": "Because a short arrow would have to be labelled in "
                     "kilograms", "correct": False,
             "why": "Labels are in newtons whatever the size. The problem is "
                    "that the arrow exists at all."},
            {"text": "Because a zero-length arrow is not a small arrow",
             "correct": True},
            {"text": "Because 0 N means the forces have stopped acting",
             "correct": False,
             "why": "Both forces go on acting; it is the resultant that is "
                    "zero."},
            {"text": "Because the arrow should be drawn pointing both ways",
             "correct": False,
             "why": "There is no arrow to draw at all, in either direction."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s29",
        "band": "standard",
        "text": "Three tugs pull a ship along one line: 4 kN east, 2 kN east "
                "and 3 kN west. What is the resultant?",
        "options": [
            {"text": "9 kN east", "correct": False,
             "why": "That adds all three. The westward tug pulls the other "
                    "way, so it is taken off."},
            {"text": "1 kN east", "correct": False,
             "why": "That uses only one of the eastward tugs. Both are "
                    "pulling."},
            {"text": "3 kN east", "correct": True},
            {"text": "3 kN west", "correct": False,
             "why": "The size is right and the direction is not: 6 kN east "
                    "beats 3 kN west."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-s30",
        "band": "standard",
        "text": "A box is pulled right with 75 N and left with 20 N. The left "
                "pull then rises to 90 N. How does the resultant change?",
        "options": [
            {"text": "It stays 55 N to the right", "correct": False,
             "why": "Every force on the line counts, so changing one changes "
                    "the resultant."},
            {"text": "It becomes 165 N to the left, as the pulls add",
             "correct": False,
             "why": "They point opposite ways, so they subtract rather than "
                    "adding."},
            {"text": "It becomes 15 N to the left, having been 55 N to the "
                     "right", "correct": True},
            {"text": "It becomes 15 N to the right, having been 55 N",
             "correct": False,
             "why": "Once the left pull is the bigger one, the resultant "
                    "points left."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-02-h07",
        "band": "harder",
        "text": "Forces of 40 N and 15 N act on a trolley along one line. "
                "What are all the possible sizes of the resultant?",
        "options": [
            {"text": "25 N or 55 N", "correct": True},
            {"text": "55 N, as forces combine by adding", "correct": False,
             "why": "They add only when they point the same way, and here they "
                    "need not."},
            {"text": "25 N, as forces combine by subtracting",
             "correct": False,
             "why": "They subtract only when they oppose, and here they need "
                    "not."},
            {"text": "Any value between 25 N and 55 N", "correct": False,
             "why": "Along ONE line there are only two arrangements, so only "
                    "two answers."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h08",
        "band": "harder",
        "text": "Two forces along one line give a resultant of 12 N to the "
                "right. Which pair works?",
        "options": [
            {"text": "20 N right and 8 N left", "correct": True},
            {"text": "20 N right and 8 N right", "correct": False,
             "why": "Both point right, so they add to 28 N."},
            {"text": "8 N right and 20 N left", "correct": False,
             "why": "That leaves 12 N pointing left, which is the wrong "
                    "direction."},
            {"text": "6 N right and 2 N right", "correct": False,
             "why": "That gives 8 N to the right, not 12 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h09",
        "band": "harder",
        "text": "In a tug of war both sides double their pull. What happens "
                "to the resultant?",
        "options": [
            {"text": "It stays exactly the same, as both grew equally",
             "correct": False,
             "why": "Equal growth is not equal difference: doubling 40 and 25 "
                    "leaves 30, not 15."},
            {"text": "It doubles as well", "correct": True},
            {"text": "It becomes zero, as the two increases cancel",
             "correct": False,
             "why": "Only a resultant of 0 N to start with would stay at "
                    "zero."},
            {"text": "It halves", "correct": False,
             "why": "Nothing is shared and nothing is halved; the difference "
                    "grows."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h10",
        "band": "harder",
        "text": "A sledge is pulled right with 60 N and left with 60 N. One "
                "rope is cut. What is the resultant immediately afterwards?",
        "options": [
            {"text": "0 N, because it was 0 N a moment earlier",
             "correct": False,
             "why": "There is nothing left to cancel the rope that is still "
                    "attached."},
            {"text": "120 N, as the cut releases the other rope's pull",
             "correct": False,
             "why": "Cutting a rope removes a force; it does not double the "
                    "one that remains."},
            {"text": "60 N, in the direction of the rope that is left",
             "correct": True},
            {"text": "30 N, half of 60 N", "correct": False,
             "why": "The remaining rope still pulls its full 60 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h11",
        "band": "harder",
        "text": "Two people pull a rope in opposite directions with 250 N "
                "each. A third joins the left side and pulls with 80 N. What "
                "is the resultant?",
        "options": [
            {"text": "580 N to the left", "correct": False,
             "why": "That adds all three, and the right-hand pull opposes the "
                    "other two."},
            {"text": "80 N to the right", "correct": False,
             "why": "The size is right and the direction is not: the left side "
                    "now totals 330 N."},
            {"text": "170 N to the left", "correct": False,
             "why": "That subtracts 80 from 250. The two left-hand pulls add "
                    "together first."},
            {"text": "80 N to the left", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h12",
        "band": "harder",
        "text": "A box is pushed to the right with 200 N. What single extra "
                "force would make the resultant 60 N to the left?",
        "options": [
            {"text": "140 N to the left", "correct": False,
             "why": "That would leave 60 N pointing right, which is the wrong "
                    "way."},
            {"text": "60 N to the left", "correct": False,
             "why": "That would leave 140 N pointing right, not 60 N left."},
            {"text": "260 N to the left", "correct": True},
            {"text": "260 N to the right", "correct": False,
             "why": "Two rightward forces add, giving 460 N to the right."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h13",
        "band": "harder",
        "text": "Three forces act along one line: 90 N right, 40 N left and "
                "one unknown. The resultant is 0 N. What is the unknown "
                "force?",
        "options": [
            {"text": "0 N, because the other two already cancel",
             "correct": False,
             "why": "They do not cancel: 90 N against 40 N leaves 50 N to the "
                    "right."},
            {"text": "50 N to the right", "correct": False,
             "why": "That would leave 100 N to the right rather than nothing "
                    "at all."},
            {"text": "130 N to the left", "correct": False,
             "why": "That would leave 80 N pointing left, which is not zero."},
            {"text": "50 N to the left", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h14",
        "band": "harder",
        "text": "A student measures the arrows on a diagram with a ruler "
                "instead of reading the labels, and gets a slightly wrong "
                "answer. What does this show?",
        "options": [
            {"text": "That force arrows should never be drawn to scale at all",
             "correct": False,
             "why": "Scale drawing is exactly how the sizes are shown; the "
                    "labels are there as well."},
            {"text": "That the labels carry the sizes, and a drawing can be "
                     "out by a millimetre", "correct": True},
            {"text": "That a ruler should never be used on a force diagram, only "
                     "on an ordinary scale drawing", "correct": False,
             "why": "A ruler is how the arrows are drawn in the first place; "
                    "it simply is not the final authority."},
            {"text": "That the diagram must have been drawn to two scales",
             "correct": False,
             "why": "A single scale drawn slightly imprecisely gives exactly "
                    "this result."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h15",
        "band": "harder",
        "text": "A trailer has a 1.2 kN pull one way and a 350 N pull the "
                "other. Give the resultant and say what had to happen first.",
        "options": [
            {"text": "850 N towards the 1.2 kN pull, after converting it to "
                     "1 200 N", "correct": True},
            {"text": "1 550 N towards the 1.2 kN pull, after adding the two",
             "correct": False,
             "why": "They oppose each other, so they subtract rather than "
                    "add."},
            {"text": "348.8 N towards the 350 N pull, subtracting 1.2 from "
                     "350", "correct": False,
             "why": "The kilonewtons have to be converted before any "
                    "subtraction happens."},
            {"text": "850 N towards the 350 N pull, after converting to "
                     "1 200 N", "correct": False,
             "why": "The resultant follows the bigger force, which is the "
                    "1 200 N one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h16",
        "band": "harder",
        "text": "Asked to combine a 2.5 kN push with a 900 N pull the other "
                "way, a student writes '897.5 N'. Which of the five steps "
                "went wrong?",
        "options": [
            {"text": "The Formula step, as they should have added",
             "correct": False,
             "why": "The two oppose, so subtracting is right; the numbers "
                    "going in were not."},
            {"text": "The Answer step, as the unit is missing", "correct": False,
             "why": "The unit is written. The figure itself came out of the "
                    "wrong numbers."},
            {"text": "The Fine-tune step, as the arithmetic is wrong",
             "correct": False,
             "why": "The arithmetic on the numbers given is correct; the "
                    "numbers were wrong before it."},
            {"text": "The Convert step, as 2.5 kN had to become 2 500 N",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h17",
        "band": "harder",
        "text": "Why can two forces of 30 N each never give a resultant of "
                "30 N when they act along one line?",
        "options": [
            {"text": "Because a resultant is always larger than either force",
             "correct": False,
             "why": "It is smaller whenever the two forces oppose each "
                    "other."},
            {"text": "Because equal forces give 0 N", "correct": False,
             "why": "Pointing the same way they give 60 N, which is not "
                    "zero."},
            {"text": "Because along one line they can only ever give 60 N or 0 N",
             "correct": True},
            {"text": "Because two equal forces cannot act on one object",
             "correct": False,
             "why": "They can, and often do — a tug of war is exactly that."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h18",
        "band": "harder",
        "text": "A trolley has a resultant of 0 N. A student says the two "
                "arrows should not be drawn at all. Why is that wrong?",
        "options": [
            {"text": "Because a diagram records what acts, and both forces "
                     "are acting", "correct": True},
            {"text": "Because the two arrows would be different lengths "
                     "anyway", "correct": False,
             "why": "At a resultant of 0 N they are the same length; the "
                    "reason to draw them is that they are real."},
            {"text": "Because a diagram must always carry exactly four arrows",
             "correct": False,
             "why": "There is no such rule. A diagram carries as many arrows "
                    "as there are forces."},
            {"text": "Because a resultant of 0 N is only ever an estimate",
             "correct": False,
             "why": "It can be exactly zero, and often is."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h19",
        "band": "harder",
        "text": "A tug pulls a barge east with 6 kN while two others pull "
                "west with 2.5 kN and 1 800 N. What is the resultant?",
        "options": [
            {"text": "1 700 N to the east", "correct": True},
            {"text": "10 300 N to the east", "correct": False,
             "why": "That adds all three. The two westward pulls come off the "
                    "eastward one."},
            {"text": "3 500 N to the east", "correct": False,
             "why": "That leaves out the 1 800 N pull, and every force on the "
                    "line counts."},
            {"text": "1 700 N to the west", "correct": False,
             "why": "The size is right and the direction is not: 6 000 N beats "
                    "4 300 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h20",
        "band": "harder",
        "text": "On a scale of 1 cm to 25 N, how long is the resultant arrow "
                "for 40 N right against 15 N left?",
        "options": [
            {"text": "1 cm", "correct": True},
            {"text": "2.2 cm", "correct": False,
             "why": "That is the 55 N you get by adding them, and these two "
                    "oppose each other."},
            {"text": "25 cm", "correct": False,
             "why": "That reads the scale upside down: 25 N is one centimetre, "
                    "not the other way about."},
            {"text": "1.6 cm", "correct": False,
             "why": "That is the 40 N arrow on its own, before the 15 N is "
                    "taken off."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h21",
        "band": "harder",
        "text": "A diagram shows a 50 N arrow and a 10 N arrow, both drawn "
                "5 cm long and pointing opposite ways. Which two false things "
                "does it now say?",
        "options": [
            {"text": "That the forces are equal, and that the resultant is "
                     "0 N", "correct": True},
            {"text": "That the forces are equal, and that they act on "
                     "different objects", "correct": False,
             "why": "Which object is acted on comes from where each arrow "
                    "starts, and nothing here says it is different."},
            {"text": "That the 10 N force is bigger, and that it acts for "
                     "longer", "correct": False,
             "why": "Equal lengths say the forces are equal, and a diagram "
                    "never shows time."},
            {"text": "That the scale is 1 cm to 10 N, and that the 50 N is "
                     "wrong", "correct": False,
             "why": "No single scale fits both arrows, which is why the "
                    "drawing is false rather than mis-scaled."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h22",
        "band": "harder",
        "text": "A crate has 80 N acting to the right and two equal forces "
                "acting to the left. The resultant is 24 N to the right. How "
                "big is each of the two?",
        "options": [
            {"text": "60 N", "correct": False,
             "why": "Two forces of 60 N make 120 N to the left, which would "
                    "leave 40 N pointing left."},
            {"text": "28 N", "correct": True},
            {"text": "24 N", "correct": False,
             "why": "Two forces of 24 N make 48 N, leaving 32 N to the right "
                    "rather than 24 N."},
            {"text": "56 N", "correct": False,
             "why": "That is the total of the two leftward forces, not the "
                    "size of each one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h23",
        "band": "harder",
        "text": "Why does the answer 'resultant = 15' lose marks even when "
                "the arithmetic behind it is right?",
        "options": [
            {"text": "Because the working was not shown alongside it",
             "correct": False,
             "why": "The working is a separate matter. The answer itself is "
                    "incomplete."},
            {"text": "Because a resultant must be written as a whole number",
             "correct": False,
             "why": "There is no such rule; plenty of resultants are not whole "
                    "numbers."},
            {"text": "Because it carries no unit and no direction",
             "correct": True},
            {"text": "Because a resultant should be given in kilonewtons",
             "correct": False,
             "why": "Newtons are correct. The unit is missing altogether, "
                    "which is the point."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h24",
        "band": "harder",
        "text": "A raft has 45 N pushing it north, and both 45 N and 20 N "
                "pushing it south. Give the resultant.",
        "options": [
            {"text": "110 N south", "correct": False,
             "why": "That adds all three, and north opposes south."},
            {"text": "20 N south", "correct": True},
            {"text": "20 N north", "correct": False,
             "why": "The size is right and the direction is not: south totals "
                    "65 N against 45 N north."},
            {"text": "65 N south", "correct": False,
             "why": "That adds the two southward forces and ignores the 45 N "
                    "pushing north."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h25",
        "band": "harder",
        "text": "Two forces along one line combine to give a resultant of "
                "0 N. What must be true of them?",
        "options": [
            {"text": "They are both zero", "correct": False,
             "why": "Two forces of 500 N pointing opposite ways also give "
                    "0 N."},
            {"text": "They are the same size and point opposite ways",
             "correct": True},
            {"text": "They are the same size and point the same way",
             "correct": False,
             "why": "Pointing the same way they would add, giving twice one of "
                    "them."},
            {"text": "One is twice the other and they point opposite ways",
             "correct": False,
             "why": "That leaves the difference between them over, which is "
                    "not zero."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h26",
        "band": "harder",
        "text": "A trolley is pushed right with 400 N and dragged left with "
                "400 N. A second person then adds 90 N to the right. What is "
                "the new resultant?",
        "options": [
            {"text": "890 N to the right", "correct": False,
             "why": "That adds all three, and the leftward drag opposes the "
                    "other two."},
            {"text": "0 N, as the first two already cancelled",
             "correct": False,
             "why": "The new force is not cancelled by anything, so it is left "
                    "over."},
            {"text": "490 N to the right", "correct": False,
             "why": "That forgets the 400 N drag, which is still acting."},
            {"text": "90 N to the right", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h27",
        "band": "harder",
        "text": "Why would drawing every arrow the same length make a force "
                "diagram useless, even with the sizes written on?",
        "options": [
            {"text": "Because equal arrows always mean a resultant of 0 N",
             "correct": False,
             "why": "Only when they oppose each other. Pointing the same way "
                    "they would add."},
            {"text": "Because the labels would then have to be in "
                     "kilonewtons", "correct": False,
             "why": "The unit on the label is not affected by how the arrows "
                    "are drawn."},
            {"text": "Because arrows of equal length cannot be given a "
                     "direction", "correct": False,
             "why": "They still point somewhere; the problem is what their "
                    "length claims."},
            {"text": "Because a reader always takes the length as the "
                     "measurement, so the picture contradicts the labels",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h28",
        "band": "harder",
        "text": "A caravan has a resultant of 250 N. A student says a single "
                "object must therefore be pushing it with 250 N. Why is that "
                "wrong?",
        "options": [
            {"text": "Because a resultant replaces several forces and need "
                     "not come from any one object", "correct": True},
            {"text": "Because a resultant force is always bigger than any of the "
                     "real forces acting on the object", "correct": False,
             "why": "It is often smaller than the biggest real force, whenever "
                    "something opposes it."},
            {"text": "Because a resultant is a speed rather than a force",
             "correct": False,
             "why": "It is a force, measured in newtons, with a direction."},
            {"text": "Because only one object can push a caravan at a time",
             "correct": False,
             "why": "Several objects push and pull at once, which is why a "
                    "resultant is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h29",
        "band": "harder",
        "text": "Two forces act right on a wagon, 3.4 kN and 600 N, and one "
                "acts left with 1 kN. Give the resultant.",
        "options": [
            {"text": "3 000 N to the right", "correct": True},
            {"text": "5 000 N to the right", "correct": False,
             "why": "That adds all three. The leftward kilonewton comes off "
                    "the total."},
            {"text": "2 400 N to the right", "correct": False,
             "why": "That leaves out the 600 N, and every force on the line "
                    "counts."},
            {"text": "3 000 N to the left", "correct": False,
             "why": "The size is right and the direction is not: 4 000 N right "
                    "beats 1 000 N left."},
        ],
        "figure": None,
    },
    {
        "id": "p4-02-h30",
        "band": "harder",
        "text": "A student draws a force arrow starting a little away from "
                "the object rather than on it. Why does that matter?",
        "options": [
            {"text": "Because the arrow would then have to be drawn shorter",
             "correct": False,
             "why": "Length carries the size and is not affected by where the "
                    "arrow begins."},
            {"text": "Because where an arrow starts says which object is "
                     "being pushed", "correct": True},
            {"text": "Because an arrow away from the object points the wrong "
                     "way", "correct": False,
             "why": "It can point in any direction wherever it is drawn; the "
                    "loss is the information about the object."},
            {"text": "Because the resultant would come out with the wrong "
                     "size", "correct": False,
             "why": "The arithmetic is unchanged. What is lost is what the "
                    "diagram says about the object."},
        ],
        "figure": None,
    },
]
