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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-07-e05",
        "band": "easier",
        "text": "When you work out a moment, where is the distance measured "
                "from?",
        "options": [
            {"text": "From the pivot to where the force acts", "correct": True},
            {"text": "From where you are standing to the object",
             "correct": False,
             "why": "Where the person stands makes no difference; the turn "
                    "happens about the pivot."},
            {"text": "From the ground up to the force", "correct": False,
             "why": "Height above the ground is not part of it. The pivot is "
                    "the reference point."},
            {"text": "From one end of the object to the other",
             "correct": False,
             "why": "The full length only matters if the pivot happens to be "
                    "at one end."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e06",
        "band": "easier",
        "text": "A force of 40 N acts at right angles, 0.25 m from a pivot. "
                "What is the moment?",
        "options": [
            {"text": "160 N m", "correct": False,
             "why": "That is 40 ÷ 0.25. A moment is force MULTIPLIED by "
                    "distance."},
            {"text": "40.25 N m", "correct": False,
             "why": "That adds the two, and a force and a distance cannot be "
                    "added."},
            {"text": "10 N m", "correct": True},
            {"text": "10 N", "correct": False,
             "why": "The number is right but a moment is measured in newton "
                    "metres, not newtons."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-07-s05",
        "band": "standard",
        "text": "A spanner is gripped 0.30 m from a bolt and pulled at right "
                "angles with 45 N. What moment does it apply?",
        "options": [
            {"text": "150 N m", "correct": False,
             "why": "That is 45 ÷ 0.30, the division where a multiplication "
                    "is needed."},
            {"text": "13.5 N m", "correct": True},
            {"text": "45.3 N m", "correct": False,
             "why": "That adds the force to the distance, which cannot be "
                    "done."},
            {"text": "1350 N m", "correct": False,
             "why": "That uses 30 rather than 0.30 — the centimetres were "
                    "never turned into metres."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s06",
        "band": "standard",
        "text": "How can a light child balance a much heavier adult on a "
                "seesaw?",
        "options": [
            {"text": "By sitting further from the pivot, so the smaller force "
                     "gives the same moment",
             "correct": True},
            {"text": "By sitting closer to the pivot, so the seesaw turns "
                     "less easily",
             "correct": False,
             "why": "Closer in gives a SMALLER moment, so the adult's side "
                    "would go straight down."},
            {"text": "By pushing down harder than their own weight",
             "correct": False,
             "why": "A person sitting still presses with their weight and no "
                    "more."},
            {"text": "It cannot be done — the heavier person always wins",
             "correct": False,
             "why": "Distance can make up the difference entirely, which is "
                    "why seesaws work at all."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-07-h05",
        "band": "harder",
        "text": "A seesaw balances with a 250 N child sitting 1.6 m from the "
                "pivot. Where must a 400 N child sit on the other side?",
        "options": [
            {"text": "1.6 m from the pivot, to match", "correct": False,
             "why": "Equal distances with unequal weights give unequal "
                    "moments, so it would tip."},
            {"text": "2.56 m from the pivot", "correct": False,
             "why": "That multiplies by 1.6 instead of dividing; the heavier "
                    "child must sit nearer, not further."},
            {"text": "1.0 m from the pivot", "correct": True},
            {"text": "0.625 m from the pivot", "correct": False,
             "why": "That is 250 ÷ 400, leaving out the 1.6 m the first child "
                    "is sitting at."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h06",
        "band": "harder",
        "text": "A wheelbarrow is loaded close to the wheel rather than near "
                "the handles. Explain in terms of moments.",
        "options": [
            {"text": "The load is then lighter, so less lifting force is "
                     "needed",
             "correct": False,
             "why": "The load weighs the same wherever it sits; only its "
                    "distance from the wheel changes."},
            {"text": "The wheel becomes the load's pivot, so nothing has to "
                     "be lifted at all",
             "correct": False,
             "why": "The handles still take a share; the point is that the "
                    "share is smaller."},
            {"text": "The wheel carries the whole weight, so the handles "
                     "take none of it",
             "correct": False,
             "why": "The handles always take a share. Moving the load close "
                    "to the wheel makes that share small."},
            {"text": "The load's short distance from the wheel gives it a "
                     "small moment to overcome",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · easier ────────────────────────────────
    {
        "id": "p4-07-e07",
        "band": "easier",
        "text": "A spring balance pulls with 10 N at right angles, 0.30 m "
                "from a pivot. What moment does it produce?",
        "options": [
            {"text": "3 N m", "correct": True},
            {"text": "0.03 N m", "correct": False,
             "why": "That divides the distance by the force. To find the "
                    "moment, the two multiply."},
            {"text": "10.3 N m", "correct": False,
             "why": "That adds the two together, and a force and a distance "
                    "cannot be added."},
            {"text": "30 N m", "correct": False,
             "why": "That treats the distance as 3 m rather than 0.30 m — "
                    "the decimal point has moved a whole place."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e08",
        "band": "easier",
        "text": "A cyclist squeezes a brake lever at right angles with "
                "15 N, gripping it 0.20 m from its pivot pin. What moment "
                "does the squeeze produce?",
        "options": [
            {"text": "0.20 N m", "correct": False,
             "why": "That is only the distance, with the wrong unit "
                    "attached. The force has not been used at all."},
            {"text": "3 N m", "correct": True},
            {"text": "15.2 N m", "correct": False,
             "why": "That adds the two together, which the formula never "
                    "does."},
            {"text": "75 N m", "correct": False,
             "why": "That divides the force by the distance. To find a "
                    "moment, the two multiply."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e09",
        "band": "easier",
        "text": "A stiff tap is turned by a force of 40 N, applied at right "
                "angles just 0.05 m from the spindle at its centre. What "
                "moment results?",
        "options": [
            {"text": "45 N m", "correct": False,
             "why": "That adds the two figures, and the units could not be "
                    "added even if it were allowed."},
            {"text": "800 N m", "correct": False,
             "why": "That divides the force by the distance — the wrong way "
                    "round. To find the moment, the two multiply."},
            {"text": "2 N m", "correct": True},
            {"text": "20 N m", "correct": False,
             "why": "That treats the distance as 0.5 m rather than 0.05 m — "
                    "ten times too big."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e10",
        "band": "easier",
        "text": "A sailor turns a ship's capstan handle at right angles "
                "with 6 N, 2.0 m from the capstan's centre. What moment "
                "does this produce?",
        "options": [
            {"text": "3 N m", "correct": False,
             "why": "That divides the force by the distance. To find the "
                    "moment, the two multiply."},
            {"text": "8 N m", "correct": False,
             "why": "That adds the two together, which the formula never "
                    "does."},
            {"text": "1.2 N m", "correct": False,
             "why": "That treats the 2.0 m as 0.2 m — the decimal place has "
                    "moved."},
            {"text": "12 N m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e11",
        "band": "easier",
        "text": "What is a pivot?",
        "options": [
            {"text": "The fixed point something turns about", "correct": True},
            {"text": "The point where you push or pull on something",
             "correct": False,
             "why": "That is where the force acts. The pivot is the fixed "
                    "point the object turns about."},
            {"text": "The middle of an object", "correct": False,
             "why": "A pivot is not always in the middle — a hinge sits at "
                    "one edge of a door, for example."},
            {"text": "The heaviest part of an object", "correct": False,
             "why": "Weight has nothing to do with where the pivot is."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e12",
        "band": "easier",
        "text": "Which of these is the pivot when a spanner turns a nut?",
        "options": [
            {"text": "The end of the spanner you are holding", "correct": False,
             "why": "That is where the force acts, not the pivot."},
            {"text": "The centre of the nut", "correct": True},
            {"text": "The middle of the spanner", "correct": False,
             "why": "Nothing is fixed there — the spanner turns about the "
                    "nut, not about its own middle."},
            {"text": "Your wrist", "correct": False,
             "why": "The distance in the formula is always measured from "
                    "the pivot, never from the body."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e13",
        "band": "easier",
        "text": "In the formula moment = force × distance, what unit is the "
                "force measured in?",
        "options": [
            {"text": "Newton metres", "correct": False,
             "why": "That is the unit the moment itself comes out in, not "
                    "the force."},
            {"text": "Metres", "correct": False,
             "why": "That is the unit of the distance."},
            {"text": "Newtons", "correct": True},
            {"text": "Joules", "correct": False,
             "why": "A joule measures energy, which is a different quantity "
                    "altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e14",
        "band": "easier",
        "text": "When you work out a moment, the distance from the pivot "
                "should be measured in which unit?",
        "options": [
            {"text": "Centimetres", "correct": False,
             "why": "The distance must be in metres for the formula to "
                    "give newton metres directly; centimetres need "
                    "converting first."},
            {"text": "Newtons", "correct": False,
             "why": "That is the unit of the force, not the distance."},
            {"text": "Newton metres", "correct": False,
             "why": "That is the unit the moment itself comes out in."},
            {"text": "Metres", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e15",
        "band": "easier",
        "text": "A force acts exactly at the pivot itself, so its distance "
                "from the pivot is zero. What is its moment?",
        "options": [
            {"text": "Zero", "correct": True},
            {"text": "The same as the force in newtons", "correct": False,
             "why": "A moment is force multiplied by distance. With a "
                    "distance of zero the product is zero, whatever the "
                    "force is."},
            {"text": "Impossible to work out without more information",
             "correct": False,
             "why": "Multiplying by zero works exactly the same as any "
                    "other multiplication — the answer is zero."},
            {"text": "As big as the force allows", "correct": False,
             "why": "This has it backwards. The pivot is where the distance "
                    "is smallest, not where the moment is biggest."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e16",
        "band": "easier",
        "text": "What is the pivot of a seesaw?",
        "options": [
            {"text": "Wherever a child happens to be sitting at the time",
             "correct": False,
             "why": "That is where a force acts, not the fixed point the "
                    "seesaw turns about."},
            {"text": "The bar or block it rests on in the middle",
             "correct": True},
            {"text": "The end furthest from the child", "correct": False,
             "why": "Nothing is fixed at the end — the seesaw turns about "
                    "its central support."},
            {"text": "The ground underneath it", "correct": False,
             "why": "The seesaw only touches its central support, not the "
                    "whole ground beneath it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e17",
        "band": "easier",
        "text": "What is the pivot when a wheel turns?",
        "options": [
            {"text": "The rim of the wheel", "correct": False,
             "why": "The rim is the part furthest away, where the movement "
                    "happens, not the fixed point it turns about."},
            {"text": "The tyre", "correct": False,
             "why": "The tyre moves with the wheel — it is not the fixed "
                    "point."},
            {"text": "The axle", "correct": True},
            {"text": "The road surface", "correct": False,
             "why": "The road is outside the wheel entirely and plays no "
                    "part in what it turns about."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e18",
        "band": "easier",
        "text": "A screwdriver handle is gripped and turned at right angles "
                "with 12 N, 0.25 m from the blade's centre line. What "
                "moment is applied to the screw?",
        "options": [
            {"text": "0.25 N m", "correct": False,
             "why": "That is just the distance with the wrong unit attached "
                    "— the force has not been used."},
            {"text": "12.25 N m", "correct": False,
             "why": "That adds the two together, and a force and a distance "
                    "cannot be added."},
            {"text": "48 N m", "correct": False,
             "why": "That divides the force by the distance — the wrong way "
                    "round."},
            {"text": "3 N m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e19",
        "band": "easier",
        "text": "A rower pulls an oar at right angles to it with 3 N, 5 m "
                "from the rowlock that acts as its pivot. What moment does "
                "this give?",
        "options": [
            {"text": "15 N m", "correct": True},
            {"text": "8 N m", "correct": False,
             "why": "That adds the two together rather than multiplying "
                    "them."},
            {"text": "1.67 N m", "correct": False,
             "why": "That divides the distance by the force instead of multiplying them."},
            {"text": "150 N m", "correct": False,
             "why": "That multiplies by 50 rather than 5 — a slipped zero."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e20",
        "band": "easier",
        "text": "A very stiff bolt is turned with a socket wrench at right "
                "angles, using 200 N just 0.01 m from the bolt's centre. "
                "What moment does this produce?",
        "options": [
            {"text": "200.01 N m", "correct": False,
             "why": "That adds the two together — a force and a distance "
                    "cannot be added."},
            {"text": "2 N m", "correct": True},
            {"text": "20000 N m", "correct": False,
             "why": "That divides the force by the distance — the wrong way "
                    "round."},
            {"text": "0.2 N m", "correct": False,
             "why": "That treats the distance as 0.001 m rather than "
                    "0.01 m — a misplaced decimal point."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e21",
        "band": "easier",
        "text": "If the force applied to a spanner is increased but the "
                "distance from the pivot stays the same, what happens to "
                "the moment?",
        "options": [
            {"text": "It gets smaller", "correct": False,
             "why": "That is what happens if the force is reduced, not "
                    "increased."},
            {"text": "It stays the same", "correct": False,
             "why": "The moment depends on both force and distance — "
                    "changing the force changes the product."},
            {"text": "It gets bigger", "correct": True},
            {"text": "It changes direction", "correct": False,
             "why": "Increasing a force does not flip which way something "
                    "turns — that depends on which side of the pivot the "
                    "force acts."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e22",
        "band": "easier",
        "text": "A force pulls exactly along the length of a lever, rather "
                "than at right angles to it. What turning effect does that "
                "force have on the lever?",
        "options": [
            {"text": "A very large one, because none of the force is "
                     "wasted on gripping the lever", "correct": False,
             "why": "Pulling along the length gives no useful distance for "
                    "the force to turn the lever through, so it produces no "
                    "turning effect at all, however large the force is."},
            {"text": "The same turning effect it would give at right "
                     "angles", "correct": False,
             "why": "At right angles the full force contributes to "
                    "turning; pulling along the length contributes none of "
                    "it."},
            {"text": "Half of what it would give at right angles",
             "correct": False,
             "why": "The effect is not simply halved — pulling exactly "
                    "along the length gives no turning effect whatsoever."},
            {"text": "None at all — it has no turning effect on the lever",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e23",
        "band": "easier",
        "text": "A seesaw has two children pushing down on opposite sides of "
                "the pivot. In which directions do their moments turn the "
                "seesaw?",
        "options": [
            {"text": "Opposite ways — one turns it clockwise, the other "
                     "anticlockwise", "correct": True},
            {"text": "The same way, because they are both pushing down",
             "correct": False,
             "why": "Pushing down on opposite sides of a pivot turns it in "
                    "opposite directions, not the same one."},
            {"text": "Neither way — the pushes cancel out completely before "
                     "any turning happens", "correct": False,
             "why": "They can balance if the moments are equal, but they "
                    "still act as two opposing turning effects, not as no "
                    "turning at all."},
            {"text": "It depends on how heavy each child is, not on which "
                     "side they sit", "correct": False,
             "why": "Which side of the pivot a force acts on decides the "
                    "direction; the size of the force decides how big the "
                    "moment is, not which way it turns."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e24",
        "band": "easier",
        "text": "The formula moment = force × distance, as used at this "
                "stage, applies when the force acts…",
        "options": [
            {"text": "in any direction at all", "correct": False,
             "why": "This course only covers the case where the force acts "
                    "at right angles to the handle or lever."},
            {"text": "at right angles to the handle or lever",
             "correct": True},
            {"text": "directly along the length of the handle itself",
             "correct": False,
             "why": "A force pulling along the handle itself would not turn "
                    "it at all."},
            {"text": "towards the pivot", "correct": False,
             "why": "A force aimed straight at the pivot has no turning "
                    "effect, whatever its size."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e25",
        "band": "easier",
        "text": "A garden gate is pushed at right angles to its face with "
                "5 N, 4 m from the gatepost hinges. What moment turns the "
                "gate?",
        "options": [
            {"text": "9 N m", "correct": False,
             "why": "That adds the two together instead of multiplying "
                    "them."},
            {"text": "1.25 N m", "correct": False,
             "why": "That divides the force by the distance instead of "
                    "multiplying them."},
            {"text": "20 N m", "correct": True},
            {"text": "0.8 N m", "correct": False,
             "why": "That divides the distance by the force — the wrong "
                    "way round."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e26",
        "band": "easier",
        "text": "Why does a long-handled wheel brace make it easier to undo "
                "a tight wheel nut?",
        "options": [
            {"text": "Because it weighs a lot more, so it applies much more "
                     "force all by itself", "correct": False,
             "why": "Its own weight plays no part — the moment comes from "
                    "the pull applied on the handle."},
            {"text": "Because a long handle grips the nut more tightly",
             "correct": False,
             "why": "The handle does not touch the nut at all — it only "
                    "changes how far from the nut the pull acts."},
            {"text": "Because it makes the nut lighter to move",
             "correct": False,
             "why": "The nut's weight has nothing to do with how tight it "
                    "is fitted."},
            {"text": "Because the same pull gives a bigger moment further "
                     "from the nut", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e27",
        "band": "easier",
        "text": "What acts as the pivot when your arm bends at the elbow?",
        "options": [
            {"text": "The elbow joint", "correct": True},
            {"text": "The hand", "correct": False,
             "why": "The hand is where you might apply or feel a force — it "
                    "is not the fixed point the forearm turns about."},
            {"text": "The muscle", "correct": False,
             "why": "The muscle supplies the force; the joint is what the "
                    "arm turns about."},
            {"text": "The shoulder", "correct": False,
             "why": "The shoulder is a different joint — the pivot for a "
                    "different movement."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e28",
        "band": "easier",
        "text": "A crowbar is used to lift a heavy stone, with the pivot "
                "placed close to the stone. What must be true of the far "
                "end, the end you push?",
        "options": [
            {"text": "It stays perfectly still the whole time while the "
                     "stone lifts", "correct": False,
             "why": "Both ends turn about the same pivot — if the stone's "
                    "end lifts, your end must move too."},
            {"text": "It has to move a much larger distance than the stone "
                     "does", "correct": True},
            {"text": "It needs no force at all to lift the stone",
             "correct": False,
             "why": "A force is still needed at your end — the pivot's "
                    "position lets that force be much smaller than the "
                    "stone's weight, not zero."},
            {"text": "It moves the same distance as the stone", "correct": False,
             "why": "Because your end is much further from the pivot than "
                    "the stone is, it sweeps through a much bigger distance "
                    "for the same turn."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e29",
        "band": "easier",
        "text": "A small hand-crank on a fishing reel is turned at right "
                "angles with 9 N, 0.1 m from its spindle. What moment does "
                "this apply to the reel?",
        "options": [
            {"text": "9.1 N m", "correct": False,
             "why": "That adds the two together instead of multiplying "
                    "them."},
            {"text": "90 N m", "correct": False,
             "why": "That divides the force by the distance — the wrong "
                    "way round."},
            {"text": "0.9 N m", "correct": True},
            {"text": "0.09 N m", "correct": False,
             "why": "That treats the distance as 0.01 m instead of 0.1 m — "
                    "the decimal point has moved."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-e30",
        "band": "easier",
        "text": "A tower crane carries a heavy counterweight on the "
                "opposite arm from its load. What is the counterweight's "
                "job?",
        "options": [
            {"text": "To make the crane very much heavier overall, so that "
                     "even a strong wind cannot blow it over", "correct": False,
             "why": "Wind is a separate matter — the counterweight's job is "
                    "about turning effects, not overall weight."},
            {"text": "To stop the load's arm bending", "correct": False,
             "why": "Bending is a strength question for the metal; the "
                    "counterweight is there for balance, not stiffness."},
            {"text": "To make the crane's motor work less hard",
             "correct": False,
             "why": "The motor still lifts the load regardless — the "
                    "counterweight's job is to stop the crane tipping, not "
                    "to help the motor."},
            {"text": "To provide a moment on the other side of the tower "
                     "that balances the load's moment", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · standard ───────────────────────────────
    {
        "id": "p4-07-s07",
        "band": "standard",
        "text": "A firefighter turns a hydrant valve wheel at right angles "
                "with 20 N, gripping it 25 cm from the valve's spindle. "
                "What moment does that produce?",
        "options": [
            {"text": "5 N m", "correct": True},
            {"text": "500 N m", "correct": False,
             "why": "That uses 25 rather than converting to 0.25 m first — "
                    "the centimetres were never turned into metres."},
            {"text": "0.8 N m", "correct": False,
             "why": "That divides the force by the unconverted 25, instead of multiplying by 0.25 m."},
            {"text": "20.25 N m", "correct": False,
             "why": "That adds the force to the distance, which the "
                    "formula never does."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s08",
        "band": "standard",
        "text": "A door handle is pushed with 8 N, 60 cm from the hinge. "
                "What moment does that give?",
        "options": [
            {"text": "480 N m", "correct": False,
             "why": "That multiplies by 60 instead of 0.60 — the "
                    "centimetres were never converted."},
            {"text": "4.8 N m", "correct": True},
            {"text": "13.3 N m", "correct": False,
             "why": "That divides the force by the distance — the wrong way round."},
            {"text": "8.6 N m", "correct": False,
             "why": "That adds the force to the distance rather than "
                    "multiplying them."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s09",
        "band": "standard",
        "text": "A mechanic uses a torque bar at right angles with 45 N, "
                "8 cm from its pivot pin, to free a seized bracket. What "
                "moment does that produce, in newton metres?",
        "options": [
            {"text": "360 N m", "correct": False,
             "why": "That uses 8 instead of converting to 0.08 m first — "
                    "the centimetres never became metres."},
            {"text": "0.18 N m", "correct": False,
             "why": "That divides the distance by the force instead of "
                    "multiplying them."},
            {"text": "3.6 N m", "correct": True},
            {"text": "45.08 N m", "correct": False,
             "why": "That adds the force to the distance, and the units "
                    "could not be added anyway."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s10",
        "band": "standard",
        "text": "A workshop clamp lever is forced at right angles with "
                "500 N, just 4 mm from its pivot pin. What is the "
                "resulting moment, in newton metres?",
        "options": [
            {"text": "2000 N m", "correct": False,
             "why": "That multiplies by 4 instead of converting the "
                    "millimetres to 0.004 m first."},
            {"text": "125 N m", "correct": False,
             "why": "That divides the force by the unconverted 4, rather than multiplying by 0.004 m."},
            {"text": "504 N m", "correct": False,
             "why": "That adds the force to the distance, treating the 4 "
                    "as though it were already in metres."},
            {"text": "2 N m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s11",
        "band": "standard",
        "text": "A stopcock key is turned with the same 20 N pull, first "
                "gripped 0.10 m from its pivot and then moved out to "
                "0.50 m. How do the two moments compare?",
        "options": [
            {"text": "The long one gives five times the moment.",
             "correct": True},
            {"text": "They are the same, because the pull is the same.",
             "correct": False,
             "why": "The moment is force × distance. Five times the "
                    "distance gives five times the moment."},
            {"text": "The long one gives twenty-five times the moment.",
             "correct": False,
             "why": "Nothing here is squared — the distance appears once in "
                    "the formula."},
            {"text": "The short one gives more, because it acts closer to "
                     "the pivot.", "correct": False,
             "why": "Closer to the pivot gives a smaller moment for the "
                    "same force, not a bigger one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s12",
        "band": "standard",
        "text": "A moment of 6 N m is produced by a 3 N force. If the same "
                "distance is kept but the force is trebled, what is the new "
                "moment?",
        "options": [
            {"text": "9 N m", "correct": False,
             "why": "That adds the increase rather than multiplying the "
                    "whole moment by three."},
            {"text": "18 N m", "correct": True},
            {"text": "2 N m", "correct": False,
             "why": "That divides the original moment by three, the "
                    "opposite of what trebling the force does."},
            {"text": "6 N m", "correct": False,
             "why": "The moment cannot stay the same when the force driving "
                    "it, at an unchanged distance, has trebled."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s13",
        "band": "standard",
        "text": "A rusted pipe fitting needs a moment of 24 N m to turn. "
                "Using a wrench, you can pull with 80 N. What is the "
                "shortest wrench that would do it?",
        "options": [
            {"text": "1920 m", "correct": False,
             "why": "That multiplies the two figures. To find a distance "
                    "from a known moment, the moment is divided by the "
                    "force."},
            {"text": "56 m", "correct": False,
             "why": "That subtracts the force from the moment rather than "
                    "dividing the moment by the force."},
            {"text": "0.3 m", "correct": True},
            {"text": "3.33 m", "correct": False,
             "why": "That divides the force by the moment — the wrong way "
                    "round."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s14",
        "band": "standard",
        "text": "A moment of 15 N m is needed and the spanner is 0.25 m "
                "long. What pull does that need?",
        "options": [
            {"text": "3.75 N", "correct": False,
             "why": "That multiplies the moment by the distance instead of "
                    "dividing by it."},
            {"text": "15.25 N", "correct": False,
             "why": "That adds the two figures, and a moment and a distance "
                    "cannot be added."},
            {"text": "0.017 N", "correct": False,
             "why": "That divides the distance by the moment — the wrong "
                    "way round."},
            {"text": "60 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s15",
        "band": "standard",
        "text": "A moment of 9 N m is produced by a force acting 0.30 m "
                "from the pivot. What size is the force?",
        "options": [
            {"text": "30 N", "correct": True},
            {"text": "2.7 N", "correct": False,
             "why": "That multiplies the moment by the distance instead of "
                    "dividing by it."},
            {"text": "9.3 N", "correct": False,
             "why": "That adds the two figures, which the formula never "
                    "does."},
            {"text": "0.033 N", "correct": False,
             "why": "That divides the distance by the moment — the wrong "
                    "way round."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s16",
        "band": "standard",
        "text": "A stiff bolt needs 21 N m to shift. The longest spanner "
                "available is 0.35 m. What pull is needed?",
        "options": [
            {"text": "7.35 N", "correct": False,
             "why": "That multiplies the moment by the distance instead of "
                    "dividing by it."},
            {"text": "60 N", "correct": True},
            {"text": "0.017 N", "correct": False,
             "why": "That divides the distance by the moment — the wrong "
                    "way round."},
            {"text": "20.65 N", "correct": False,
             "why": "That subtracts the distance from the moment rather "
                    "than dividing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s17",
        "band": "standard",
        "text": "A beam rests on a single support. A 400 N sack hangs 1.5 m "
                "out on one side. A 600 N sack hangs on the other side. How "
                "far out must it hang for the beam to balance?",
        "options": [
            {"text": "2.25 m", "correct": False,
             "why": "That applies the ratio of the two weights the wrong way round; the heavier sack has to hang closer in, not further out."},
            {"text": "1.5 m", "correct": False,
             "why": "Equal distances only balance when the weights are also "
                    "equal, and here they are not."},
            {"text": "1 m", "correct": True},
            {"text": "0.67 m", "correct": False,
             "why": "That divides 400 by 600, leaving out the 1.5 m the first sack hangs at."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s18",
        "band": "standard",
        "text": "A seesaw balances with a 250 N weight 2 m from the pivot "
                "on one side. On the other side, a weight sits 0.5 m from "
                "the pivot. How heavy is it?",
        "options": [
            {"text": "125 N", "correct": False,
             "why": "That divides the first weight by its own 2 m distance, rather than working through the moment."},
            {"text": "62.5 N", "correct": False,
             "why": "That applies the ratio of the two distances the wrong way round, giving a lighter weight where a heavier one is needed."},
            {"text": "500 N", "correct": False,
             "why": "That stops after finding the moment, 500 N m, instead "
                    "of dividing it by the new distance to get the weight."},
            {"text": "1000 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s19",
        "band": "standard",
        "text": "Two equal forces push down on opposite sides of a pivot, "
                "at equal distances from it. What happens?",
        "options": [
            {"text": "The moments are equal and opposite, so the seesaw "
                     "balances.", "correct": True},
            {"text": "The moments add together, doubling the turning "
                     "effect.", "correct": False,
             "why": "Moments on opposite sides of a pivot turn it in "
                    "opposite directions — equal ones cancel rather than "
                    "add."},
            {"text": "Nothing happens, because both forces are pushing "
                     "down rather than up.", "correct": False,
             "why": "The direction of the push does not stop it producing a "
                    "moment; what matters is the distance from the pivot."},
            {"text": "The side with more distance from the ground wins.",
             "correct": False,
             "why": "Distance from the ground plays no part — only "
                    "distance from the pivot decides the size of a moment."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s20",
        "band": "standard",
        "text": "A wheelbarrow's load is placed as close to the wheel as "
                "possible. Explain why this makes it easier to lift the "
                "handles.",
        "options": [
            {"text": "Because the load then weighs less.", "correct": False,
             "why": "The load's weight does not change with where it sits "
                    "in the barrow."},
            {"text": "Because the load's short distance from the wheel "
                     "gives it a small moment for the handles to overcome.",
             "correct": True},
            {"text": "Because the wheel takes the whole of the load's "
                     "weight, leaving nothing at all for the handles to "
                     "lift.", "correct": False,
             "why": "The handles still supply some of the lifting force; "
                    "moving the load close to the wheel only makes that "
                    "share smaller."},
            {"text": "Because the handles then act closer to the pivot "
                     "too.", "correct": False,
             "why": "The handles' distance from the wheel does not change — "
                    "only the load's position does."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s21",
        "band": "standard",
        "text": "A moment of 10 N m is produced by a certain force and "
                "distance. If both the force AND the distance are doubled, "
                "what is the new moment?",
        "options": [
            {"text": "20 N m", "correct": False,
             "why": "Doubling only one of the two would double the moment; "
                    "doubling both multiplies it by four."},
            {"text": "15 N m", "correct": False,
             "why": "That treats the doubling as an addition rather than a "
                    "multiplication."},
            {"text": "40 N m", "correct": True},
            {"text": "10 N m", "correct": False,
             "why": "The moment cannot stay the same when both the force "
                    "and the distance driving it have grown."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s22",
        "band": "standard",
        "text": "A moment of 12 N m is needed. One person can pull with "
                "40 N, another with 60 N. How much shorter can the second "
                "person's spanner be and still work?",
        "options": [
            {"text": "0.5 m shorter", "correct": False,
             "why": "That adds the two required lengths instead of finding "
                    "the difference between them."},
            {"text": "0.3 m shorter", "correct": False,
             "why": "That is the first person's whole spanner length, not "
                    "the difference between the two."},
            {"text": "0.2 m shorter", "correct": False,
             "why": "That is the second person's whole spanner length, not "
                    "the difference between the two."},
            {"text": "0.1 m shorter", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s23",
        "band": "standard",
        "text": "A mechanic swaps a short socket wrench for a longer one on "
                "the same tight nut. What changes?",
        "options": [
            {"text": "The same pull now produces a bigger moment.",
             "correct": True},
            {"text": "The pull needed stays the same, because the nut has "
                     "not changed.", "correct": False,
             "why": "The nut needing the same moment is exactly why a "
                    "longer wrench, with the same pull, now supplies more "
                    "than enough."},
            {"text": "The moment needed to turn the nut becomes smaller.",
             "correct": False,
             "why": "The nut's required moment is fixed by how tightly it "
                    "was done up — the wrench does not change it."},
            {"text": "Nothing changes, because moment only depends on the "
                     "pull, not the wrench length.", "correct": False,
             "why": "The moment is force multiplied by distance, so the "
                    "length of the wrench matters just as much as the "
                    "pull."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s24",
        "band": "standard",
        "text": "A builder starts walking along a plank that overhangs a "
                "scaffold. As they walk further past the edge, what happens "
                "to the moment trying to tip the plank?",
        "options": [
            {"text": "It stays the same, because the builder's weight has "
                     "not changed.", "correct": False,
             "why": "The builder's weight is fixed, but the moment also "
                    "depends on the distance from the scaffold edge, which "
                    "is increasing."},
            {"text": "It gets bigger, because the distance from the edge is "
                     "increasing.", "correct": True},
            {"text": "It gets smaller, because the builder is moving away "
                     "from the scaffold.", "correct": False,
             "why": "Moving further from the pivot increases the moment — "
                    "it does not reduce it."},
            {"text": "It disappears once the builder is fully off the "
                     "scaffold.", "correct": False,
             "why": "The moment exists as long as a weight acts at a "
                    "distance from the pivot — it does not vanish."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s25",
        "band": "standard",
        "text": "A model windmill's hand crank is turned at right angles "
                "with 2.5 N, 40 cm from its pivot. What moment does this "
                "produce?",
        "options": [
            {"text": "100 N m", "correct": False,
             "why": "That uses 40 instead of converting to 0.4 m first."},
            {"text": "6.25 N m", "correct": False,
             "why": "That divides the force by the distance — the wrong way round."},
            {"text": "1 N m", "correct": True},
            {"text": "2.9 N m", "correct": False,
             "why": "That adds the force to the distance rather than "
                    "converting and multiplying."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s26",
        "band": "standard",
        "text": "A moment of 3.6 N m is produced by a force of 12 N. How "
                "far from the pivot is the force acting, in centimetres?",
        "options": [
            {"text": "0.3 cm", "correct": False,
             "why": "That gives the answer in metres but labels it "
                    "centimetres — 0.3 m is 30 cm."},
            {"text": "43.2 cm", "correct": False,
             "why": "That multiplies the moment by the force instead of "
                    "dividing."},
            {"text": "3.33 cm", "correct": False,
             "why": "That divides the force by the moment rather than the "
                    "moment by the force, and never converts to "
                    "centimetres."},
            {"text": "30 cm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s27",
        "band": "standard",
        "text": "Spanner A gives a moment of 8 N m. Spanner B is twice as "
                "long and is pulled with half the force. How do their "
                "moments compare?",
        "options": [
            {"text": "They are the same — the moment is unchanged.",
             "correct": True},
            {"text": "Spanner B gives twice the moment.", "correct": False,
             "why": "Doubling the distance while halving the force leaves "
                    "the product exactly where it started."},
            {"text": "Spanner B gives half the moment.", "correct": False,
             "why": "Halving the force is exactly cancelled out by "
                    "doubling the distance, so the moment does not fall."},
            {"text": "It cannot be worked out without knowing the exact "
                     "numbers.", "correct": False,
             "why": "Doubling one factor while halving the other always "
                    "leaves a product unchanged, whatever the starting "
                    "numbers are."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s28",
        "band": "standard",
        "text": "A weight is held in the hand with the elbow bent. Moving "
                "the weight further from the elbow, while keeping its size "
                "the same, does what to the moment at the elbow joint?",
        "options": [
            {"text": "Reduces it, because the arm has to work less hard "
                     "close in.", "correct": False,
             "why": "Moving the weight FURTHER from the joint increases its "
                    "distance, which increases the moment, not decreases "
                    "it."},
            {"text": "Increases it, because the distance from the pivot has "
                     "grown.", "correct": True},
            {"text": "Leaves it unchanged, because the weight itself has "
                     "not changed.", "correct": False,
             "why": "The moment depends on distance as well as force — a "
                    "bigger distance means a bigger moment even with the "
                    "same weight."},
            {"text": "Makes it impossible to calculate without knowing the "
                     "muscle's own force.", "correct": False,
             "why": "The moment of the weight about the elbow only needs "
                    "the weight's size and its distance from the joint."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s29",
        "band": "standard",
        "text": "A door needs a moment of 18 N m to swing open smoothly. It "
                "is pushed 90 cm from the hinge. What push does that "
                "require?",
        "options": [
            {"text": "16.2 N", "correct": False,
             "why": "That multiplies the moment by the distance instead of "
                    "dividing by it."},
            {"text": "0.2 N", "correct": False,
             "why": "That uses 90 rather than converting to 0.9 m before "
                    "dividing."},
            {"text": "20 N", "correct": True},
            {"text": "0.05 N", "correct": False,
             "why": "That divides the distance by the moment — the wrong "
                    "way round."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-s30",
        "band": "standard",
        "text": "Two spanners are each pulled with the moment their own "
                "nut needs to shift it: Spanner X needs 45 N at 0.20 m, "
                "Spanner Y needs 30 N at 0.30 m. Which nut needs the bigger "
                "moment to shift it?",
        "options": [
            {"text": "Spanner X's nut, because 45 N is the bigger force.",
             "correct": False,
             "why": "A bigger force alone does not decide it — the moments "
                    "here both work out equal, at 9 N m."},
            {"text": "Spanner Y's nut, because 0.30 m is the bigger "
                     "distance.", "correct": False,
             "why": "A bigger distance alone does not decide it either — "
                    "both moments come out the same."},
            {"text": "It cannot be worked out from the information given.",
             "correct": False,
             "why": "Both moments can be calculated directly from the force "
                    "and distance given for each."},
            {"text": "Neither — both nuts need exactly the same moment, "
                     "9 N m.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 expansion · harder ─────────────────────────────────
    {
        "id": "p4-07-h07",
        "band": "harder",
        "text": "A nut needs 15 N m to move. Which of these pulls would NOT "
                "be enough to reach that?",
        "options": [
            {"text": "28 N at 0.50 m", "correct": True},
            {"text": "40 N at 0.375 m", "correct": False,
             "why": "40 × 0.375 = 15 N m exactly, so this one is enough."},
            {"text": "60 N at 0.25 m", "correct": False,
             "why": "60 × 0.25 = 15 N m exactly, so this one is enough too."},
            {"text": "75 N at 0.20 m", "correct": False,
             "why": "75 × 0.20 = 15 N m exactly, enough as well."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h08",
        "band": "harder",
        "text": "A plank pivots at its centre. A 200 N weight sits 1.8 m "
                "from the pivot on the left. On the right, a 300 N weight "
                "sits 0.6 m out and another 100 N weight sits some distance "
                "out too, and the plank balances exactly. How far out is "
                "the second weight on the right?",
        "options": [
            {"text": "3.6 m", "correct": False,
             "why": "That divides the whole 360 N m by 100 without first "
                    "subtracting the 180 N m the 300 N weight already "
                    "supplies."},
            {"text": "1.8 m", "correct": True},
            {"text": "0.6 m", "correct": False,
             "why": "That repeats the other weight's distance rather than "
                    "working out what balance actually requires."},
            {"text": "0.9 m", "correct": False,
             "why": "That halves the left-hand distance rather than "
                    "working out the moment still needed on the right."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h09",
        "band": "harder",
        "text": "A crane's load arm carries a 4000 N load 6 m from the "
                "tower. The counterweight sits 3 m from the tower on the "
                "other side. What counterweight is needed to balance it "
                "exactly?",
        "options": [
            {"text": "2000 N", "correct": False,
             "why": "That multiplies the load by the ratio of distances the "
                    "wrong way round (3 ÷ 6) rather than solving the "
                    "balance properly."},
            {"text": "12000 N", "correct": False,
             "why": "That multiplies the load by the counterweight's own "
                    "distance rather than the load's, and stops before "
                    "dividing by anything."},
            {"text": "8000 N", "correct": True},
            {"text": "24000 N", "correct": False,
             "why": "That stops at the load's own moment, 24000 N m, "
                    "instead of dividing it by the counterweight's distance "
                    "to find the force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h10",
        "band": "harder",
        "text": "A bolt needs 4.5 N m to shift. The only spanner to hand is "
                "150 mm long. What pull, in newtons, does that spanner "
                "need?",
        "options": [
            {"text": "0.03 N", "correct": False,
             "why": "That divides the distance by the moment, the wrong "
                    "way round, and never converts the millimetres."},
            {"text": "675 N", "correct": False,
             "why": "That multiplies rather than divides, using the "
                    "unconverted 150 mm."},
            {"text": "4.65 N", "correct": False,
             "why": "That adds the two figures without converting or "
                    "dividing at all."},
            {"text": "30 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h11",
        "band": "harder",
        "text": "Two people separately manage to shift the same stiff "
                "bolt. One used 90 N on a 0.20 m spanner; the other used "
                "60 N on a longer one. For the second person to have needed "
                "exactly the same moment, how long was their spanner?",
        "options": [
            {"text": "0.30 m", "correct": True},
            {"text": "0.20 m", "correct": False,
             "why": "That is the first person's spanner — the moment stays "
                    "the same but a smaller force needs a bigger distance, "
                    "not an equal one."},
            {"text": "0.13 m", "correct": False,
             "why": "That divides the first person's distance rather than "
                    "scaling it up to match a smaller force."},
            {"text": "12 m", "correct": False,
             "why": "That multiplies the second person's 60 N by the first person's 0.20 m, rather than using the moment the first person actually produced."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h12",
        "band": "harder",
        "text": "A muscle attaches 3 cm from the elbow joint, and a weight "
                "is held in the hand 30 cm from the same joint. For the "
                "muscle's pull to balance the weight's moment about the "
                "elbow, roughly how does the muscle's force compare with "
                "the weight?",
        "options": [
            {"text": "It needs to be about the same size.", "correct": False,
             "why": "The muscle acts ten times closer to the joint than the "
                    "weight does, so an equal force would give only a tenth "
                    "of the weight's moment."},
            {"text": "It needs to be about ten times bigger.",
             "correct": True},
            {"text": "It needs to be about ten times smaller.",
             "correct": False,
             "why": "Acting closer to the pivot means a bigger force, not a "
                    "smaller one, is needed to match the same moment."},
            {"text": "It cannot be worked out without knowing the muscle's "
                     "own weight.", "correct": False,
             "why": "The muscle's own weight plays no part — only its force "
                    "and its distance from the joint matter for its "
                    "moment."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h13",
        "band": "harder",
        "text": "A nut needs at least 8 N m to move. A mechanic has a "
                "12 cm spanner and can pull with at most 55 N. Can they "
                "shift the nut, and by how much do they clear or miss the "
                "threshold?",
        "options": [
            {"text": "Yes, by 1.4 N m.", "correct": False,
             "why": "55 N on a 0.12 m spanner gives 6.6 N m, which is below "
                    "the 8 N m needed, not above it."},
            {"text": "Yes, by 4.6 N m.", "correct": False,
             "why": "That compares the wrong two numbers — the spanner "
                    "only manages 6.6 N m in total."},
            {"text": "No, they fall short by 1.4 N m.", "correct": True},
            {"text": "No, they fall short by 6.6 N m.", "correct": False,
             "why": "6.6 N m is what the spanner DOES manage, not the "
                    "shortfall, which is 8 minus 6.6."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h14",
        "band": "harder",
        "text": "A moment of 40 N m is needed. Tool A can supply up to "
                "200 N; Tool B can supply up to 80 N. What is the shortest "
                "spanner length that would make EACH tool just barely "
                "sufficient?",
        "options": [
            {"text": "Tool A needs 0.5 m and Tool B needs 0.2 m",
             "correct": False,
             "why": "The lengths have been swapped — the weaker tool needs "
                    "the longer spanner, not the stronger one."},
            {"text": "Both tools need exactly 0.2 m", "correct": False,
             "why": "Tool B only supplies 80 N, so at 0.2 m it would give "
                    "just 16 N m, far short of 40 N m."},
            {"text": "Both tools need exactly 0.5 m", "correct": False,
             "why": "Tool A already reaches 40 N m at 0.2 m — giving it "
                    "0.5 m too ignores that it is the stronger tool."},
            {"text": "Tool A needs 0.2 m and Tool B needs 0.5 m",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h15",
        "band": "harder",
        "text": "A metre rule pivots at its centre. A 2 N weight hangs "
                "0.4 m to the left. Two weights hang on the right: 1 N at "
                "0.2 m and another unknown weight at 0.4 m. What is the "
                "unknown weight, for the rule to balance?",
        "options": [
            {"text": "1.5 N", "correct": True},
            {"text": "0.5 N", "correct": False,
             "why": "That divides the 0.2 N m already supplied on the right by the 0.4 m arm, instead of working out what is still needed."},
            {"text": "3 N", "correct": False,
             "why": "That divides the remaining 0.6 N m by the other weight's 0.2 m distance instead of by the 0.4 m where it actually hangs."},
            {"text": "1 N", "correct": False,
             "why": "That repeats the other right-hand weight's size "
                    "instead of completing the balance calculation."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h16",
        "band": "harder",
        "text": "A plank of negligible weight overhangs a workbench by 1.2 m, and a 300 N brick sits right at the overhanging end. A downward force is applied to the supported part of the plank, 0.4 m back from the bench edge. What is the smallest such force that would just stop the plank tipping?",
        "options": [
            {"text": "100 N", "correct": False,
             "why": "That multiplies 300 by the ratio of distances the "
                    "wrong way round (0.4 ÷ 1.2) rather than dividing the "
                    "brick's moment by the new distance."},
            {"text": "900 N", "correct": True},
            {"text": "360 N", "correct": False,
             "why": "That stops at the brick's own moment about the table "
                    "edge, rather than dividing by the distance the holding "
                    "force acts at."},
            {"text": "375 N", "correct": False,
             "why": "That divides the brick's weight by the difference "
                    "between the two distances, rather than using the "
                    "moment properly."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h17",
        "band": "harder",
        "text": "A pipeline valve needs a moment of 90 N m to turn. One engineer can pull with 200 N; a colleague can manage a gentler 120 N. Roughly how much shorter can the stronger engineer's lever be than the one the colleague would need?",
        "options": [
            {"text": "0.20 m shorter", "correct": False,
             "why": "That takes the weaker pull as 140 N rather than 120 N, which shrinks the gap between the two lever lengths."},
            {"text": "0.75 m shorter", "correct": False,
             "why": "That is the whole length of the colleague's lever, not the difference between the two."},
            {"text": "0.30 m shorter", "correct": True},
            {"text": "0.45 m shorter", "correct": False,
             "why": "That is the whole length of the stronger engineer's lever, not the difference between the two."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h18",
        "band": "harder",
        "text": "A moment of 2.4 N m is produced by a 16 N force. A second "
                "setup uses the same force at a distance three times as "
                "long. What is that distance, in centimetres?",
        "options": [
            {"text": "15 cm", "correct": False,
             "why": "That is the original 0.15 m distance correctly "
                    "converted to centimetres, but without trebling it as "
                    "the question asks."},
            {"text": "135 cm", "correct": False,
             "why": "That converts to centimetres first and then trebles again, applying the trebling twice over."},
            {"text": "4.5 cm", "correct": False,
             "why": "That trebles the distance correctly but converts as "
                    "though a metre were ten centimetres rather than a "
                    "hundred."},
            {"text": "45 cm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h19",
        "band": "harder",
        "text": "A wheel has three forces acting on it, all the same size, "
                "at the same distance from the axle. Two act to turn it "
                "clockwise and one acts to turn it anticlockwise. What is "
                "the overall turning effect?",
        "options": [
            {"text": "Clockwise, because two of the three moments are in "
                     "that direction and only one opposes them.",
             "correct": True},
            {"text": "Zero, because the forces are all the same size.",
             "correct": False,
             "why": "Being the same size does not mean they cancel — two "
                    "are turning it one way and only one is opposing them."},
            {"text": "Anticlockwise, because one force is always enough to "
                     "reverse the others.", "correct": False,
             "why": "One equal-sized moment cannot outweigh two others "
                    "acting the other way — the majority direction wins."},
            {"text": "It cannot be worked out without knowing exactly which "
                     "point on the wheel each individual force acts at.",
             "correct": False,
             "why": "With the same size and the same distance from the "
                    "axle, only the number acting in each direction decides "
                    "the outcome."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h20",
        "band": "harder",
        "text": "A seesaw balances with children of 350 N and 490 N "
                "sitting on opposite sides. The lighter child sits 2.1 m "
                "from the pivot. How far out does the heavier child sit?",
        "options": [
            {"text": "1.05 m", "correct": False,
             "why": "That halves the lighter child's distance rather than "
                    "dividing the correct moment by the heavier child's "
                    "weight."},
            {"text": "1.5 m", "correct": True},
            {"text": "2.94 m", "correct": False,
             "why": "That uses the two weights' ratio the wrong way round, "
                    "which finds a distance bigger than the lighter "
                    "child's rather than smaller."},
            {"text": "15 m", "correct": False,
             "why": "That divides 735 by 49 rather than 490 — a misplaced "
                    "decimal point."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h21",
        "band": "harder",
        "text": "A machine's design brief calls for a torque setting of "
                "exactly double a hand tool's maximum moment. The hand "
                "tool manages 40 N at 0.25 m at most. What torque setting "
                "is needed?",
        "options": [
            {"text": "5 N m", "correct": False,
             "why": "That halves the hand tool's own moment rather than "
                    "doubling it."},
            {"text": "10 N m", "correct": False,
             "why": "That is the hand tool's own maximum moment — the "
                    "brief calls for double this, not the same amount."},
            {"text": "20 N m", "correct": True},
            {"text": "80 N m", "correct": False,
             "why": "That doubles the force and the distance both, which "
                    "multiplies the moment by four rather than by two."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h22",
        "band": "harder",
        "text": "A tower crane can position its counterweight at 2 m or "
                "4 m from the tower. Its load of 3000 N sits 8 m out. "
                "Which counterweight position needs a lighter counterweight, "
                "and by how much?",
        "options": [
            {"text": "The 2 m position, by 6000 N", "correct": False,
             "why": "The 2 m position actually needs the HEAVIER "
                    "counterweight, 12000 N, not the lighter one."},
            {"text": "The 4 m position, by 12000 N", "correct": False,
             "why": "That is the full counterweight needed at 2 m, not the "
                    "difference between the two options."},
            {"text": "The 2 m position, by 12000 N", "correct": False,
             "why": "This both picks the wrong position and states the "
                    "wrong figure — the 2 m position needs more "
                    "counterweight, not less."},
            {"text": "The 4 m position, by 6000 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h23",
        "band": "harder",
        "text": "A wheelbarrow's wheel acts as the pivot. A 600 N load "
                "sits 0.3 m from the wheel, and the handles are 1.2 m from "
                "the wheel. What upward force must the handles supply to "
                "lift the load?",
        "options": [
            {"text": "150 N", "correct": True},
            {"text": "216 N", "correct": False,
             "why": "That multiplies the load's moment by the handle "
                    "distance instead of dividing by it."},
            {"text": "180 N", "correct": False,
             "why": "That stops at the load's own moment about the wheel, "
                    "rather than dividing by the handle's distance."},
            {"text": "500 N", "correct": False,
             "why": "That divides the load's weight by the handle distance "
                    "directly, leaving out the load's own 0.3 m distance "
                    "from the wheel altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h24",
        "band": "harder",
        "text": "Two garden shears are identical except that Shears A have "
                "blades twice as long as their handles, and Shears B have "
                "handles twice as long as their blades. For the same hand "
                "grip force, which needs less force to cut a tough stem, "
                "and why?",
        "options": [
            {"text": "Shears A, because a longer blade always cuts more "
                     "easily.", "correct": False,
             "why": "Blade length alone is not the reason — what matters "
                    "here is the ratio of handle length to blade length "
                    "either side of the pivot."},
            {"text": "Shears B, because their longer handles give a bigger "
                     "moment for the same grip force, delivered through a "
                     "shorter blade.", "correct": True},
            {"text": "Neither — both would need exactly the same hand "
                     "force, because simply having a pivot of some kind "
                     "does not by itself decide how the forces are shared "
                     "out on either side of it.", "correct": False,
             "why": "Having the same TYPE of pivot does not mean the same "
                    "ratio of lengths either side of it, and that ratio is "
                    "exactly what has been swapped here."},
            {"text": "Shears A, because a shorter handle needs less force to move, and less movement at the handle means less effort for the hand overall.", "correct": False,
             "why": "A shorter handle, for the same movement of the blade "
                    "tip, needs a bigger hand force, not a smaller one."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h25",
        "band": "harder",
        "text": "A force is applied to a lever, but its line of action "
                "passes exactly through the pivot rather than at any "
                "distance from it. What moment does it produce, and what "
                "does that show about the formula moment = force × "
                "distance?",
        "options": [
            {"text": "A large moment, because the force is acting directly "
                     "on the pivot itself.", "correct": False,
             "why": "Acting through the pivot gives the smallest possible "
                    "distance from it, which is zero, not the largest."},
            {"text": "It cannot be worked out, because the standard formula "
                     "for a moment does not apply to an unusual case like "
                     "this one.", "correct": False,
             "why": "The formula still applies — a distance of zero is a "
                    "perfectly valid value to put into it."},
            {"text": "Zero, because the distance from the pivot in the "
                     "formula is zero, and anything multiplied by zero is "
                     "zero.", "correct": True},
            {"text": "It depends on the size of the force, however small "
                     "the distance is.", "correct": False,
             "why": "However big the force, multiplying by a distance of "
                    "zero always gives zero."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h26",
        "band": "harder",
        "text": "A spanner must supply at least 55 N m. Using it at 0.25 m "
                "needs one pull; using an identical spanner extended by a "
                "pipe to 0.55 m needs another. By how much does the "
                "required pull fall when the pipe is added?",
        "options": [
            {"text": "20 N", "correct": False,
             "why": "That is far smaller than the actual difference between "
                    "the two required pulls, which is 120 N."},
            {"text": "100 N", "correct": False,
             "why": "That is the pull needed WITH the pipe, not the fall in "
                    "pull between the two cases."},
            {"text": "220 N", "correct": False,
             "why": "That is the pull needed WITHOUT the pipe, not the "
                    "difference between the two cases."},
            {"text": "120 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h27",
        "band": "harder",
        "text": "A 1.6 m plank pivots at its centre. A 180 N weight sits "
                "0.8 m from the pivot on the left, at the very end. On the "
                "right, a weight sits 40 cm from the pivot. How heavy must "
                "it be to balance the plank?",
        "options": [
            {"text": "360 N", "correct": True},
            {"text": "90 N", "correct": False,
             "why": "That divides the left-hand moment by the plank's whole 1.6 m length instead of by the 0.40 m the right-hand weight sits at."},
            {"text": "3.6 N", "correct": False,
             "why": "That divides the left-hand moment by 40 instead of "
                    "converting to 0.4 m first."},
            {"text": "72 N", "correct": False,
             "why": "That multiplies 180 by 0.4 rather than dividing the "
                    "left-hand moment by the right-hand distance."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h28",
        "band": "harder",
        "text": "Someone claims that because muscles near a joint need a "
                "much bigger force than the load they lift, the body is an "
                "inefficient machine and a mechanical lever would always be "
                "better. What is the flaw in that argument?",
        "options": [
            {"text": "There is no flaw — a lever with the pivot near the "
                     "load always needs less force, so it is always the "
                     "better choice.", "correct": False,
             "why": "A lever placed that way also needs the load's end to "
                    "move a much smaller distance than your end for the "
                    "same force saving, which is not what the body's "
                    "arrangement gives it."},
            {"text": "It ignores that the body's arrangement buys speed and "
                     "range of movement, which a force-saving lever would "
                     "not give.", "correct": True},
            {"text": "It is flawed because muscles do not really need a "
                     "bigger force than the load — that part is a common "
                     "misunderstanding.", "correct": False,
             "why": "Muscles genuinely do need a much bigger force than the "
                    "load, because they act so close to the joint — that "
                    "part of the claim is correct."},
            {"text": "It is flawed because moments do not apply to the "
                     "human body at all.", "correct": False,
             "why": "A joint acts exactly as a pivot, and the same force × "
                    "distance arithmetic applies to a muscle and a bone as "
                    "to a spanner and a nut."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h29",
        "band": "harder",
        "text": "A car's handbook specifies a wheel nut torque of 1.1 daN m "
                "(1 daN = 10 N). A mechanic's wrench reads in N m. What "
                "should the wrench be set to, and is 9 N m enough?",
        "options": [
            {"text": "1.1 N m, and yes, 9 N m is more than enough",
             "correct": False,
             "why": "1 daN is 10 N, so 1.1 daN m converts to 11 N m, not "
                    "1.1 N m — the conversion factor was missed entirely."},
            {"text": "110 N m, and no, 9 N m is nowhere near enough",
             "correct": False,
             "why": "This uses a conversion factor of 100 instead of 10 — "
                    "1 daN is only ten newtons."},
            {"text": "11 N m, and no, 9 N m is not enough", "correct": True},
            {"text": "11 N m, and yes, 9 N m is enough", "correct": False,
             "why": "11 N m is converted correctly, but 9 is less than 11, "
                    "so the wrench would under-tighten the nut, not "
                    "over-tighten it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-07-h30",
        "band": "harder",
        "text": "A plank rests on a support 0.5 m from one end, and "
                "extends 2.5 m the other way. A 40 N weight sits right at "
                "the short end, 0.5 m from the support. What is the "
                "biggest weight that could be hung at the very far end, "
                "2.5 m from the support, before the plank tips?",
        "options": [
            {"text": "200 N", "correct": False,
             "why": "That scales the weight up by the ratio of distances "
                    "the wrong way round — the far weight needs to be "
                    "smaller than the near one, not five times bigger."},
            {"text": "20 N", "correct": False,
             "why": "That is the short end's own moment in newton metres, "
                    "not a weight in newtons — it still needs dividing by "
                    "the 2.5 m distance."},
            {"text": "33.3 N", "correct": False,
             "why": "That shares the 40 N weight out across the plank's "
                    "total length instead of balancing the moments on each "
                    "side of the support."},
            {"text": "8 N", "correct": True},
        ],
        "figure": None,
    },
]
