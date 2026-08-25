"""P4 lesson 07 — Moments: twelve questions (MRB-223).

Written against Design's page. The door and the hinge, the spanner and
the tight nut and both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · a moment is force × distance FROM THE PIVOT, and the pivot has to be
    identified first (`FORCE-37`);
  · the unit is the newton metre, because a moment is not a force
    (`FORCE-38`);
  · a longer handle buys turning effect, not strength (`FORCE-36`);
  · the distance changes HOW MUCH, not just which way (`FORCE-39`) —
    the harder band sits here and on rearranging for a distance.

⚠️ POSITION IS AUTHORED — index cycles 3, 0, 2, 1, giving three of each.

⚠️ Rung 1 (30 N at 0.40 m) and Rung 2 (two 50 N pulls on 0.10 m and
0.40 m spanners) are NOT restated; check 6 of `verify_questions.py`
forbids it.
"""

UNIT = "P4"
LESSON = "moments"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-07-e01",
        "band": "easier",
        "text": "The moment of a force is measured in…",
        "options": [
            {"text": "newtons, the same unit the force itself is in", "correct": False,
             "why": "A moment is not a force. It is a force multiplied by a "
                    "distance."},
            {"text": "metres", "correct": False,
             "why": "That is only the distance half. The force half is "
                    "missing."},
            {"text": "joules", "correct": False,
             "why": "A joule is a unit of energy. A moment is a turning "
                    "effect, and the two are different quantities."},
            {"text": "newton metres", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e02",
        "band": "easier",
        "text": "A force of 20 N acts 0.5 m from a pivot, at right angles. "
                "What is the moment?",
        "options": [
            {"text": "10 N m", "correct": True},
            {"text": "40 N m", "correct": False,
             "why": "That is 20 ÷ 0.5. To find the moment the two "
                    "multiply."},
            {"text": "20.5 N m", "correct": False,
             "why": "That adds them. Nothing in moment = force × distance "
                    "adds."},
            {"text": "10 N", "correct": False,
             "why": "The arithmetic is right and the unit is wrong. A moment "
                    "is in newton metres."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e03",
        "band": "easier",
        "text": "What is the pivot when you push a door open?",
        "options": [
            {"text": "The handle", "correct": False,
             "why": "The handle is where the force acts. The pivot is the "
                    "fixed point the door turns about."},
            {"text": "The hinge line", "correct": True},
            {"text": "The middle of the door", "correct": False,
             "why": "Nothing is fixed there. The door swings about its "
                    "hinges."},
            {"text": "Where you are standing", "correct": False,
             "why": "Your position has nothing to do with it. The distance "
                    "is always measured from the pivot."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e04",
        "band": "easier",
        "text": "Why are door handles fitted at the edge furthest from the "
                "hinges?",
        "options": [
            {"text": "Because the door is thinner there.", "correct": False,
             "why": "Thickness has nothing to do with turning. Distance from "
                    "the pivot does."},
            {"text": "Because it is easier to reach.", "correct": False,
             "why": "A handle in the middle would be just as easy to reach "
                    "and much harder to use."},
            {"text": "Because that is the furthest point from the pivot, so "
                     "the same push gives the biggest moment.",
             "correct": True},
            {"text": "Because the hinges would get in the way of your hand, "
                     "not because the distance matters",
             "correct": False,
             "why": "Handles are fitted well clear of hinges anyway. The "
                    "reason is the turning effect."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-07-s01",
        "band": "standard",
        "text": "A nut is turned with 30 N applied 20 cm from the pivot. "
                "What is the moment?",
        "options": [
            {"text": "600 N m", "correct": False,
             "why": "That multiplies by the CENTIMETRES. A newton metre "
                    "needs the distance in metres, so divide by 100 first."},
            {"text": "6 N m", "correct": True},
            {"text": "1.5 N m", "correct": False,
             "why": "That is 30 ÷ 20. To find the moment the two multiply."},
            {"text": "50 N m", "correct": False,
             "why": "That is 30 + 20. Nothing in the formula adds, and the "
                    "units could not be added anyway."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s02",
        "band": "standard",
        "text": "The same 40 N pull is applied to a 0.15 m spanner and then "
                "to a 0.45 m one. How do the moments compare?",
        "options": [
            {"text": "The long one gives three times the moment.",
             "correct": True},
            {"text": "They are the same, because the pull is the same.",
             "correct": False,
             "why": "The moment is force × distance. Three times the "
                    "distance is three times the moment."},
            {"text": "The long one gives nine times the moment.",
             "correct": False,
             "why": "Nothing here is squared. The distance appears once."},
            {"text": "The short one gives more, because the force acts "
                     "closer to the nut.", "correct": False,
             "why": "Closer to the pivot is weaker. That is the door-hinge "
                    "test at the top of the lesson."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s03",
        "band": "standard",
        "text": "A stiff bolt needs 18 N m to move. You can pull with 60 N. "
                "What is the shortest spanner that will do?",
        "options": [
            {"text": "1 080 m", "correct": False,
             "why": "That is 18 × 60. To find a distance from a known "
                    "moment you divide."},
            {"text": "3.3 m", "correct": False,
             "why": "That is 60 ÷ 18 — the wrong way round. Cover d on the "
                    "triangle: M sits over F."},
            {"text": "0.3 m", "correct": True},
            {"text": "18 m", "correct": False,
             "why": "That is the moment with a metre written after it. The "
                    "force still has to be divided in."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s04",
        "band": "standard",
        "text": "Someone says “a longer spanner means I am pulling harder.” "
                "How would you settle it?",
        "options": [
            {"text": "Time how long each takes to shift the nut, since a "
                     "bigger moment should do it faster",
             "correct": False,
             "why": "That measures the outcome, not the pull. It would not "
                    "tell you what the hand is doing."},
            {"text": "Put a spring balance on the handle and read it with "
                     "each spanner.", "correct": True},
            {"text": "Weigh both spanners.", "correct": False,
             "why": "Their weight is not what the hand is supplying, and it "
                    "is not what the claim is about."},
            {"text": "Measure the nut.", "correct": False,
             "why": "The nut is the same in both cases. What is in dispute "
                    "is the force from the hand."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-07-h01",
        "band": "harder",
        "text": "A nut needs 12 N m. You are pulling with 60 N at 0.15 m. "
                "Which of these would ALSO reach the threshold?",
        "options": [
            {"text": "Pulling with 80 N at the same 0.15 m.",
             "correct": True},
            {"text": "Pulling with 60 N at 0.10 m.", "correct": False,
             "why": "That gives 6 N m — less than the 9 N m you already "
                    "have, and further from the threshold."},
            {"text": "Pulling with 40 N at 0.15 m.", "correct": False,
             "why": "That gives 6 N m. Reducing the force takes you further "
                    "away."},
            {"text": "Pulling with 30 N at 0.30 m.", "correct": False,
             "why": "That gives 9 N m — the same as now, because halving "
                    "one and doubling the other leaves the product "
                    "unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h02",
        "band": "harder",
        "text": "A child of 300 N sits 2 m from the centre of a seesaw. "
                "Where must an adult of 600 N sit to balance it?",
        "options": [
            {"text": "4 m from the centre, on the other side.",
             "correct": False,
             "why": "That gives 2 400 N m against the child's 600 N m. The "
                    "heavier person sits CLOSER, not further."},
            {"text": "1 m from the centre, on the other side.",
             "correct": True},
            {"text": "2 m from the centre, on the other side.",
             "correct": False,
             "why": "Equal distances balance only when the weights are "
                    "equal. Here 600 × 2 is twice the child's moment."},
            {"text": "It cannot balance, because the adult is heavier.",
             "correct": False,
             "why": "A seesaw does not care about weight — it cares about "
                    "the two moments about the pivot."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h03",
        "band": "harder",
        "text": "Why does a car manufacturer supply a long wheel brace "
                "rather than one of exactly the shortest workable length?",
        "options": [
            {"text": "Because a long one is cheaper to make.",
             "correct": False,
             "why": "It uses more metal. Cost is not the reason."},
            {"text": "Because a longer brace produces a bigger force in your "
                     "arm.", "correct": False,
             "why": "It does not change the force you can produce at all. It "
                    "changes what that force achieves."},
            {"text": "Because a longer brace reaches the required moment "
                     "with a much smaller force, which most people can "
                     "actually manage.", "correct": True},
            {"text": "Because a longer brace tightens the nut more than a "
                     "short one ever could, whatever force is used on it", "correct": False,
             "why": "Either reaches the same 110 N m. The difference is how "
                    "hard you have to pull to get there."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h04",
        "band": "harder",
        "text": "Many muscles in the human body pull very close to the "
                "joint. What does the body trade for that?",
        "options": [
            {"text": "Nothing — it is simply how the bones happen to be "
                     "arranged.", "correct": False,
             "why": "The arrangement has real consequences, and they are the "
                    "same arithmetic as a spanner."},
            {"text": "It needs a much bigger force, but gains speed and "
                     "range of movement.", "correct": True},
            {"text": "It gains force, and loses speed.", "correct": False,
             "why": "That is the crowbar trade, and it is the other way "
                    "round from what a joint does."},
            {"text": "It makes the moment larger for the same muscle force.",
             "correct": False,
             "why": "Closer to the pivot is a SMALLER moment for the same "
                    "force, which is why the force has to be large."},
        ],
        "figure": None,
    },
]
