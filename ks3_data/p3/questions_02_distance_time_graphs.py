"""P3 lesson 02 — Distance–time graphs: twelve questions (MRB-223).

Written against Design's page. The corridor journey, the flat section and
the cyclist to the postbox are hers.

The discriminations:

  · the upright axis is DISTANCE FROM THE START, so a falling line is a
    return and never a hill (`FORCE-06`);
  · a flat line is STOPPED, not slow (`FORCE-07`) — the key fact, and
    the one a student who has just learned "steeper = faster" gets wrong;
  · steepness is speed, and a steeper line does not mean a longer journey;
  · a curve means the speed is changing, not that the route bends
    (`FORCE-08`).

⚠️ POSITION IS AUTHORED — index cycles 1, 2, 3, 0, giving three of each.

⚠️ Rung 1 (horizontal between 20 s and 35 s) and Rung 2 (line A steeper
than line B) are NOT restated; check 6 of `verify_questions.py` forbids it.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P3"
LESSON = "distance-time-graphs"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p3-02-e01",
        "band": "easier",
        "text": "On a distance–time graph, what does the upright axis show?",
        "options": [
            {"text": "How high above the ground the object is",
             "correct": False,
             "why": "Nothing on this graph is a height. The axis is a "
                    "distance along a journey."},
            {"text": "How far the object is from the start", "correct": True},
            {"text": "How fast the object is going", "correct": False,
             "why": "Speed is not plotted anywhere. It is hiding in the "
                    "steepness."},
            {"text": "How long the object has been travelling",
             "correct": False,
             "why": "That is the other axis, along the bottom."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e02",
        "band": "easier",
        "text": "A distance–time graph has a horizontal section. What is "
                "happening there?",
        "options": [
            {"text": "The object is moving very slowly", "correct": False,
             "why": "Slowly still means the distance from the start is "
                    "changing, so the line would still climb, just gently."},
            {"text": "The object is speeding up", "correct": False,
             "why": "Speeding up makes the line get steeper, not flat."},
            {"text": "The object is stopped", "correct": True},
            {"text": "The object is going back to the start",
             "correct": False,
             "why": "Going back makes the line fall towards zero. Horizontal "
                    "means it stayed where it was."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e03",
        "band": "easier",
        "text": "Where is the speed on a distance–time graph?",
        "options": [
            {"text": "On the upright axis", "correct": False,
             "why": "That axis is distance from the start."},
            {"text": "On the horizontal axis", "correct": False,
             "why": "That axis is time."},
            {"text": "It is written beside the line", "correct": False,
             "why": "Nothing is written beside it. It has to be read off the "
                    "steepness."},
            {"text": "In the steepness of the line", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e04",
        "band": "easier",
        "text": "A line on a distance–time graph falls back towards zero. "
                "What does that mean?",
        "options": [
            {"text": "The object is returning towards the start",
             "correct": True},
            {"text": "The object is going downhill", "correct": False,
             "why": "The graph holds no information about hills at all "
                    "— only how far from the start and how long."},
            {"text": "The object is slowing down", "correct": False,
             "why": "Slowing down makes the line get less steep while still "
                    "climbing. Falling is a different thing."},
            {"text": "The object has stopped", "correct": False,
             "why": "Stopped is a flat line. A falling line is still "
                    "moving."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p3-02-s01",
        "band": "standard",
        "text": "A line goes from 6 m at 8 s to 18 m at 12 s. What is the "
                "speed over that section?",
        "options": [
            {"text": "1.5 m/s", "correct": False,
             "why": "That is 6 ÷ 4, using the starting distance rather "
                    "than the distance covered."},
            {"text": "3 m/s", "correct": True},
            {"text": "4.5 m/s", "correct": False,
             "why": "That is 18 ÷ 4, using the final distance rather "
                    "than the change in it."},
            {"text": "12 m/s", "correct": False,
             "why": "That is the distance covered with no division by the "
                    "time at all."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s02",
        "band": "standard",
        "text": "A cyclist rides 400 m to a postbox on a flat road, waits, "
                "and rides home. What does her graph do?",
        "options": [
            {"text": "Rises, flattens, then rises again to 800 m",
             "correct": False,
             "why": "That is the total-distance-travelled graph. This axis "
                    "is distance FROM THE START, which falls on the way "
                    "home."},
            {"text": "Rises steadily the whole way", "correct": False,
             "why": "That would mean she never stopped and never turned "
                    "round."},
            {"text": "Rises, flattens, then falls back to zero",
             "correct": True},
            {"text": "Rises, then falls, then rises again", "correct": False,
             "why": "There is only one outward leg and one return, with a "
                    "wait between them."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s03",
        "band": "standard",
        "text": "Line A is steeper than line B on the same axes. What must "
                "be true?",
        "options": [
            {"text": "A travelled further than B", "correct": False,
             "why": "Not necessarily. A steep line drawn for two seconds can "
                    "cover less ground than a gentle one drawn for a "
                    "minute."},
            {"text": "A took longer than B", "correct": False,
             "why": "Time is read along the bottom, not from the steepness."},
            {"text": "A started later than B", "correct": False,
             "why": "Where a line starts is a position on the time axis and "
                    "has nothing to do with its gradient."},
            {"text": "A was travelling faster than B", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s04",
        "band": "standard",
        "text": "Why can a distance–time graph not tell you whether a "
                "journey went round a bend?",
        "options": [
            {"text": "Because it plots only how far from the start and how "
                     "long, and neither carries direction",
             "correct": True},
            {"text": "Because the graph is not accurate enough",
             "correct": False,
             "why": "Accuracy is not the issue. The information is simply "
                    "not among the two quantities plotted."},
            {"text": "Because bends only matter at high speed",
             "correct": False,
             "why": "Whether a bend matters is beside the point: the graph "
                    "does not record direction at all."},
            {"text": "Because bends are drawn as curves and this graph has "
                     "none",
             "correct": False,
             "why": "This graph can certainly have curves — they mean "
                    "the speed is changing, not that the route bends."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p3-02-h01",
        "band": "harder",
        "text": "A distance–time graph curves upwards, getting steeper. What "
                "is happening?",
        "options": [
            {"text": "The object is going round a bend", "correct": False,
             "why": "The graph holds no information about direction in "
                    "space. A curve is about the gradient changing."},
            {"text": "The object is speeding up", "correct": True},
            {"text": "The object is slowing down", "correct": False,
             "why": "Slowing down makes the curve get LESS steep as it "
                    "goes."},
            {"text": "The object is going uphill", "correct": False,
             "why": "There is no room for a hill on this graph, in either "
                    "direction."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h02",
        "band": "harder",
        "text": "A lift rises 30 m in 20 s, waits 10 s, then returns to the "
                "ground floor in 15 s. Which part of the graph is steepest?",
        "options": [
            {"text": "The first part, at 1.5 m/s", "correct": False,
             "why": "30 ÷ 20 = 1.5 m/s. The return is 30 ÷ 15 = "
                    "2 m/s, which is steeper."},
            {"text": "The middle part, because waiting takes no distance",
             "correct": False,
             "why": "The middle part is flat — the least steep section "
                    "there is."},
            {"text": "The last part, at 2 m/s", "correct": True},
            {"text": "The first and last are equally steep",
             "correct": False,
             "why": "Same distance, different times: 20 s against 15 s, so "
                    "the gradients differ."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h03",
        "band": "harder",
        "text": "The same cyclist's journey is redrawn with TOTAL DISTANCE "
                "TRAVELLED up the side instead. How does the graph change?",
        "options": [
            {"text": "It becomes a straight line, because the total always "
                     "grows steadily",
             "correct": False,
             "why": "It still flattens while she waits — the total does "
                    "not grow when she is not moving."},
            {"text": "It is identical, because it is the same journey",
             "correct": False,
             "why": "The return leg is the difference: one graph falls and "
                    "the other climbs."},
            {"text": "It falls twice instead of once", "correct": False,
             "why": "It can never fall at all — a distance you have "
                    "travelled cannot be un-travelled."},
            {"text": "The return leg climbs to 800 m instead of falling to "
                     "zero",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h04",
        "band": "harder",
        "text": "Two graphs of one journey are drawn: distance from the "
                "start, and total distance travelled. Which question can "
                "only the first one answer?",
        "options": [
            {"text": "Whether the traveller got back to where they began",
             "correct": True},
            {"text": "How fast the traveller was going at each stage",
             "correct": False,
             "why": "Both carry that in their gradients — the speed is "
                    "readable from either."},
            {"text": "How long the whole journey took", "correct": False,
             "why": "Both use the same time axis, so both answer this "
                    "equally well."},
            {"text": "How far the traveller went in total", "correct": False,
             "why": "That is the question only the SECOND graph answers "
                    "directly."},
        ],
        "figure": None,
    },
]
