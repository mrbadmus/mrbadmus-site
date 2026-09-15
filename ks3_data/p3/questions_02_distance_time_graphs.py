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
            {"text": "The object is going downhill for a while",
             "correct": False,
             "why": "The graph holds no information about hills at all — only "
                    "how far from the start and how long."},
            {"text": "The object is slowing down as it goes", "correct": False,
             "why": "Slowing down makes the line get less steep while still "
                    "climbing. Falling is a different thing."},
            {"text": "The object has stopped where it is", "correct": False,
             "why": "Stopped is a flat line. A falling line is still moving."},
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
            {"text": "Because the graph is not plotted accurately enough to "
                     "show up a change of direction",
             "correct": False,
             "why": "Accuracy is not the issue. The information is simply not "
                    "among the two quantities plotted."},
            {"text": "Because a bend only matters at high speed, and nothing "
                     "here was going fast enough",
             "correct": False,
             "why": "Whether a bend matters is beside the point: the graph "
                    "does not record direction at all."},
            {"text": "Because a bend would have to appear as a curve, and "
                     "this kind of graph never curves",
             "correct": False,
             "why": "This graph can certainly have curves — they mean the "
                    "speed is changing, not that the route bends."},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p3-02-e05",
        "band": "easier",
        "text": "What is plotted along the horizontal axis of a "
                "distance–time graph?",
        "options": [
            {"text": "The time", "correct": True},
            {"text": "The speed", "correct": False,
             "why": "Speed is never plotted on these axes. It has to be "
                    "worked out from the steepness of the line."},
            {"text": "The distance from the start", "correct": False,
             "why": "That goes up the side. Putting it along the bottom would "
                    "give a different graph altogether."},
            {"text": "The direction of travel", "correct": False,
             "why": "Direction is not on either axis, which is why the graph "
                    "cannot show the route."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e06",
        "band": "easier",
        "text": "On a distance–time graph, what does a steeper line mean?",
        "options": [
            {"text": "The object is travelling faster", "correct": True},
            {"text": "The object is travelling uphill", "correct": False,
             "why": "Neither axis carries height. A steep line on level "
                    "ground is just a fast journey."},
            {"text": "The object has travelled for longer", "correct": False,
             "why": "How long it travelled for is read along the bottom, not "
                    "from the steepness."},
            {"text": "The object is further from the start", "correct": False,
             "why": "How far it has come is the height of the line, not how "
                    "steep it is."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e07",
        "band": "easier",
        "text": "A distance–time graph is a straight sloping line. What does "
                "that tell you about the speed?",
        "options": [
            {"text": "The speed is steady", "correct": True},
            {"text": "The speed is increasing", "correct": False,
             "why": "Speeding up makes the line curve and get steeper. A "
                    "straight line has one steepness throughout."},
            {"text": "The speed is zero", "correct": False,
             "why": "A zero speed gives a horizontal line, not a sloping "
                    "one."},
            {"text": "The speed cannot be found from a straight line",
             "correct": False,
             "why": "A straight line is the easiest case: the steepness is "
                    "the speed, and it does not change."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e08",
        "band": "easier",
        "text": "Distance is plotted in metres and time in seconds. What unit "
                "does the steepness of the line have?",
        "options": [
            {"text": "m", "correct": False,
             "why": "Metres alone would be a distance. The steepness divides "
                    "a distance by a time."},
            {"text": "m/s", "correct": True},
            {"text": "s/m", "correct": False,
             "why": "That is the division upside down — it would be the graph "
                    "with the axes swapped over."},
            {"text": "s", "correct": False,
             "why": "Seconds alone would be a time, and a time is not a "
                    "measure of steepness."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e09",
        "band": "easier",
        "text": "A distance–time graph is flat for 10 s. How far does the "
                "object travel in those 10 s?",
        "options": [
            {"text": "10 m, one metre each second", "correct": False,
             "why": "Nothing on the graph says a metre each second. A flat "
                    "line means the distance is not changing."},
            {"text": "It cannot be worked out without the speed",
             "correct": False,
             "why": "The flat line is the speed: it is 0 m/s, so the distance "
                    "covered is 0 m."},
            {"text": "0 m, because the line is not rising", "correct": True},
            {"text": "A short distance, because it is going slowly",
             "correct": False,
             "why": "A flat line is not slow. It is stopped, so no distance "
                    "is covered at all."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e10",
        "band": "easier",
        "text": "A line on a distance–time graph gradually becomes less "
                "steep. What is happening?",
        "options": [
            {"text": "The object is slowing down", "correct": True},
            {"text": "The object is going back towards the start",
             "correct": False,
             "why": "Coming back makes the line fall. A line that is still "
                    "rising is still moving away."},
            {"text": "The object is going downhill", "correct": False,
             "why": "The graph never shows the shape of the ground. The line "
                    "is about distance and time only."},
            {"text": "The object has stopped", "correct": False,
             "why": "Stopped is a completely flat line. This one is still "
                    "rising, just less steeply."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e11",
        "band": "easier",
        "text": "A straight line passes through 0 m at 0 s and 40 m at 10 s. "
                "What is the speed?",
        "options": [
            {"text": "400 m/s", "correct": False,
             "why": "That is 40 × 10. The steepness is found by dividing, not "
                    "multiplying."},
            {"text": "0.25 m/s", "correct": False,
             "why": "That is 10 ÷ 40 — time divided by distance, the wrong "
                    "way round."},
            {"text": "30 m/s", "correct": False,
             "why": "That is 40 − 10, and a distance and a time cannot be "
                    "subtracted."},
            {"text": "4 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e12",
        "band": "easier",
        "text": "A car sits in a car park all morning. What does its "
                "distance–time graph look like?",
        "options": [
            {"text": "A horizontal line all morning", "correct": True},
            {"text": "A straight line sloping gently upwards",
             "correct": False,
             "why": "Any upward slope means the distance is growing, so the "
                    "car would be moving."},
            {"text": "A line falling towards zero", "correct": False,
             "why": "A falling line means coming back towards the start, "
                    "which is still moving."},
            {"text": "No line at all can be drawn", "correct": False,
             "why": "A line can always be drawn. Standing still is a real "
                    "journey with a speed of 0 m/s."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e13",
        "band": "easier",
        "text": "A distance–time graph is a straight line through the origin. "
                "What kind of journey is that?",
        "options": [
            {"text": "One that started slowly and gradually built up "
                     "speed",
             "correct": False,
             "why": "Building up speed makes the line curve. A straight line "
                    "has the same speed all the way."},
            {"text": "One that set off from the start at a steady speed",
             "correct": True},
            {"text": "One that began some distance from the start",
             "correct": False,
             "why": "Passing through the origin is exactly what says it "
                    "began at the start."},
            {"text": "One that stopped partway and set off again",
             "correct": False,
             "why": "A stop puts a horizontal section in the line, so it "
                    "would not be straight."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e14",
        "band": "easier",
        "text": "Why is time always plotted along the bottom of a "
                "distance–time graph?",
        "options": [
            {"text": "Because time is the quantity you choose the readings "
                     "of",
             "correct": True},
            {"text": "Because time is always the larger of the two numbers",
             "correct": False,
             "why": "It very often is not, and which number is larger has "
                    "nothing to do with the axes."},
            {"text": "Because distance cannot be plotted along the bottom",
             "correct": False,
             "why": "It can be, and then the graph means something different. "
                    "The convention is what fixes it."},
            {"text": "Because the graph would be upside down otherwise",
             "correct": False,
             "why": "Swapping the axes does not turn the graph over; it makes "
                    "the steepness mean seconds per metre."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e15",
        "band": "easier",
        "text": "Two journeys are plotted on the same axes and the two lines "
                "cross at 20 s. What does the crossing point mean?",
        "options": [
            {"text": "The two objects collided at that moment",
             "correct": False,
             "why": "The graph does not show the route, so they may be the "
                    "same distance out on quite different roads."},
            {"text": "The two objects were the same distance from the start "
                     "at 20 s",
             "correct": True},
            {"text": "The two objects were travelling at the same speed at "
                     "20 s",
             "correct": False,
             "why": "Equal speed would mean equal steepness, not lines "
                    "meeting."},
            {"text": "One object overtook the other and stopped",
             "correct": False,
             "why": "Stopping would show as a flat section. A crossing alone "
                    "says nothing about stopping."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e16",
        "band": "easier",
        "text": "Which of these is NOT shown anywhere on a distance–time "
                "graph?",
        "options": [
            {"text": "The time the journey took", "correct": False,
             "why": "That is read straight off the bottom axis."},
            {"text": "The shape of the route that was taken", "correct": True},
            {"text": "The distance from the start at any moment",
             "correct": False,
             "why": "That is read straight off the upright axis."},
            {"text": "The speed during any part of the journey",
             "correct": False,
             "why": "The speed is there: it is the steepness of the line."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e17",
        "band": "easier",
        "text": "On a distance–time graph the line passes through 45 m at "
                "15 s. What does that single point tell you?",
        "options": [
            {"text": "The object travelled at 45 m/s for 15 s",
             "correct": False,
             "why": "45 is a distance in metres, not a speed. The point gives "
                    "position, not how fast."},
            {"text": "The object was 45 m from the start after 15 s",
             "correct": True},
            {"text": "The object travelled 45 m in each of the 15 s",
             "correct": False,
             "why": "45 m is the whole distance from the start, not a "
                    "distance covered every second."},
            {"text": "The object stopped after 15 s", "correct": False,
             "why": "One point says nothing about stopping. A stop shows as a "
                    "flat section of line."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p3-02-s05",
        "band": "standard",
        "text": "A line runs straight from 10 m at 5 s to 40 m at 15 s. What "
                "is the speed over that section?",
        "options": [
            {"text": "2.7 m/s", "correct": False,
             "why": "That is 40 ÷ 15, using the readings rather than the "
                    "change in each one."},
            {"text": "0.33 m/s", "correct": False,
             "why": "That is 10 ÷ 30 — the two changes divided the wrong way "
                    "round."},
            {"text": "30 m/s", "correct": False,
             "why": "30 m is how far it went. It still has to be divided by "
                    "the 10 s it took."},
            {"text": "3 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s06",
        "band": "standard",
        "text": "A graph rises for 20 s, stays flat for 10 s, then rises "
                "again for 10 s. For how long was the object moving?",
        "options": [
            {"text": "30 s, the two rising parts", "correct": True},
            {"text": "40 s, the whole time on the graph", "correct": False,
             "why": "The flat 10 s is a stop, and nothing moves during it."},
            {"text": "10 s, the flat part", "correct": False,
             "why": "The flat part is the only time it was NOT moving."},
            {"text": "20 s, the first rising part only", "correct": False,
             "why": "The second rise is movement too, so it has to be counted "
                    "as well."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s07",
        "band": "standard",
        "text": "A line rises from the origin to 60 m at 20 s, then stays "
                "flat until 50 s. What is the average speed for the whole "
                "50 s?",
        "options": [
            {"text": "3 m/s, the speed while it was moving", "correct": False,
             "why": "That leaves out the 30 s spent stopped, and an average "
                    "has to include it."},
            {"text": "1.2 m/s", "correct": True},
            {"text": "60 m/s", "correct": False,
             "why": "60 m is the total distance. It still has to be divided "
                    "by the 50 s."},
            {"text": "1.5 m/s, halfway between 3 m/s and 0 m/s",
             "correct": False,
             "why": "Averaging the two speeds ignores that the stop lasted "
                    "longer than the moving part."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s08",
        "band": "standard",
        "text": "A walker's line runs from the origin to 80 m at 40 s. A "
                "cyclist's runs from the origin to 320 m at 40 s. How many "
                "times faster is the cyclist?",
        "options": [
            {"text": "240 times, the difference between the distances",
             "correct": False,
             "why": "240 m is how much further the cyclist went, not how many "
                    "times faster."},
            {"text": "Twice as fast", "correct": False,
             "why": "Twice 80 m would be 160 m. The cyclist covered four "
                    "times the distance."},
            {"text": "Four times as fast", "correct": True},
            {"text": "The same speed, because both took 40 s",
             "correct": False,
             "why": "The equal time is what lets you compare: in it, one "
                    "covered four times the ground."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s09",
        "band": "standard",
        "text": "On the same axes, line A runs from the origin to 50 m at "
                "10 s and line B from the origin to 50 m at 25 s. Which is "
                "true?",
        "options": [
            {"text": "A is faster, and both travelled the same distance",
             "correct": True},
            {"text": "B is faster, because its line is longer",
             "correct": False,
             "why": "How long the line looks is not the speed. Steepness is, "
                    "and A is steeper."},
            {"text": "A travelled further than B", "correct": False,
             "why": "Both lines finish at 50 m, so both covered the same "
                    "distance."},
            {"text": "They travelled at the same speed for different times",
             "correct": False,
             "why": "Same distance in different times means different speeds: "
                    "5 m/s against 2 m/s."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s10",
        "band": "standard",
        "text": "How would a bus waiting at a stop for 15 s appear on its "
                "distance–time graph?",
        "options": [
            {"text": "A gap of 15 s with no line drawn", "correct": False,
             "why": "The bus still exists during the wait, so the line "
                    "continues — flat."},
            {"text": "A section of line falling for 15 s", "correct": False,
             "why": "A falling line means returning towards the start, not "
                    "waiting."},
            {"text": "A horizontal section 15 s long", "correct": True},
            {"text": "A gently rising section 15 s long", "correct": False,
             "why": "Any rise means the distance is still growing, so the bus "
                    "would be creeping forward."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s11",
        "band": "standard",
        "text": "A line falls straight from 200 m at 60 s to 0 m at 100 s. "
                "How fast was the object travelling on the way back?",
        "options": [
            {"text": "2 m/s", "correct": False,
             "why": "That is 200 ÷ 100, using the whole time instead of the "
                    "40 s the return took."},
            {"text": "0 m/s, because it ended where it began",
             "correct": False,
             "why": "Ending where it began does not mean it stood still — it "
                    "covered 200 m getting there."},
            {"text": "3.3 m/s", "correct": False,
             "why": "That is 200 ÷ 60, using the time at the start of the "
                    "return rather than its length."},
            {"text": "5 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s12",
        "band": "standard",
        "text": "A student says a falling line on a distance–time graph means "
                "the object is slowing down. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — falling and slowing are the same "
                     "thing",
             "correct": False,
             "why": "They are different: one is about direction, the other "
                    "about how steep the line is."},
            {"text": "Falling means coming back towards the start; slowing "
                     "makes the line less steep",
             "correct": True},
            {"text": "Falling means the object has stopped completely",
             "correct": False,
             "why": "Stopped is a flat line. A falling line is still "
                    "moving."},
            {"text": "Falling means the object is going downhill",
             "correct": False,
             "why": "The graph never shows the ground. The upright axis is "
                    "distance from the start, not height."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s13",
        "band": "standard",
        "text": "A dog runs 40 m away from its owner in 10 s, sniffs for "
                "20 s, then runs back in 10 s. What shape is its "
                "distance–time graph?",
        "options": [
            {"text": "A rise, then a flat section, then a fall back to zero",
             "correct": True},
            {"text": "A rise, then a flat section, then a steeper rise",
             "correct": False,
             "why": "Running back reduces the distance from the owner, so the "
                    "line must come down."},
            {"text": "A rise all the way, getting less steep at the end",
             "correct": False,
             "why": "That would be a dog still moving away, only more "
                    "slowly."},
            {"text": "A flat line the whole way, at 40 m", "correct": False,
             "why": "A flat line means never moving, and this dog covered "
                    "80 m altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s14",
        "band": "standard",
        "text": "Which section is faster: one rising 60 m in 10 s, or one "
                "rising 120 m in 30 s?",
        "options": [
            {"text": "The 120 m section, because it covers more ground",
             "correct": False,
             "why": "It also takes three times as long: 120 ÷ 30 is 4 m/s "
                    "against 60 ÷ 10 = 6 m/s."},
            {"text": "The 60 m section, at 6 m/s", "correct": True},
            {"text": "They are the same, because both are straight lines",
             "correct": False,
             "why": "Both being straight only means both speeds are steady. "
                    "It does not make them equal."},
            {"text": "The 120 m section, because its line is longer",
             "correct": False,
             "why": "Length of line is not speed; steepness is, and the "
                    "shorter section is steeper."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s15",
        "band": "standard",
        "text": "Why does the distance–time graph of a car in a traffic jam "
                "have many short flat sections?",
        "options": [
            {"text": "Because the car keeps stopping and starting",
             "correct": True},
            {"text": "Because the car keeps changing direction",
             "correct": False,
             "why": "Turning does not show on the graph at all; only the "
                    "distance from the start does."},
            {"text": "Because the road is flat where the jam is",
             "correct": False,
             "why": "The shape of the road never appears on a distance–time "
                    "graph."},
            {"text": "Because the readings were taken too far apart",
             "correct": False,
             "why": "Widely spaced readings would hide the stops, not create "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s16",
        "band": "standard",
        "text": "Readings of distance and time are taken every 2 s. What does "
                "plotting them give you that a list of numbers does not?",
        "options": [
            {"text": "It makes the readings more accurate",
             "correct": False,
             "why": "Plotting cannot improve a reading. It shows what the "
                    "readings already say."},
            {"text": "It shows the whole journey at once, including where "
                     "nothing happened",
             "correct": True},
            {"text": "It removes the need to measure the distance",
             "correct": False,
             "why": "The distances are what is plotted, so they still have to "
                    "be measured."},
            {"text": "It gives the speed without any working at all",
             "correct": False,
             "why": "The steepness still has to be worked out from two "
                    "readings on the line."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s17",
        "band": "standard",
        "text": "A line is steeper between 0 s and 5 s than it is between 5 s "
                "and 20 s. Which statement must be true?",
        "options": [
            {"text": "The object was further from the start in the first 5 s",
             "correct": False,
             "why": "It is nearest the start at the beginning; steepness is "
                    "about speed, not position."},
            {"text": "The object stopped after 5 s", "correct": False,
             "why": "The later section is less steep but still rising, so it "
                    "kept moving."},
            {"text": "The object travelled faster in the first 5 s",
             "correct": True},
            {"text": "The object travelled further in the first 5 s",
             "correct": False,
             "why": "The later section lasts three times as long, so it may "
                    "well cover more ground even at a lower speed."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p3-02-h05",
        "band": "harder",
        "text": "A distance-from-start graph rises to 100 m in 10 s, stays "
                "flat for 20 s, then falls back to 0 m over the next 20 s. "
                "What is the average speed for the whole 50 s?",
        "options": [
            {"text": "0 m/s, because it finished where it started",
             "correct": False,
             "why": "The graph ends at zero, but the walker really did cover "
                    "200 m of ground getting there."},
            {"text": "2 m/s, from 100 m divided by 50 s", "correct": False,
             "why": "100 m is the outward leg only; the return is 100 m more "
                    "of travelling."},
            {"text": "4 m/s, from 200 m divided by 50 s", "correct": True},
            {"text": "10 m/s, the speed of the fastest section",
             "correct": False,
             "why": "That is the outward leg alone, and an average has to "
                    "include the stop and the return."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h06",
        "band": "harder",
        "text": "A line curves upwards, getting steeper, and then becomes "
                "straight for the rest of the journey. Describe the motion.",
        "options": [
            {"text": "It speeds up, then keeps a steady speed",
             "correct": True},
            {"text": "It speeds up, then stops", "correct": False,
             "why": "A stop is a horizontal line. A straight sloping line is "
                    "steady movement."},
            {"text": "It goes uphill, then along the flat", "correct": False,
             "why": "Neither axis carries height. The graph is about distance "
                    "and time only."},
            {"text": "It slows down, then keeps a steady speed",
             "correct": False,
             "why": "Slowing down makes a curve get LESS steep. This one is "
                    "getting steeper."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h07",
        "band": "harder",
        "text": "Why can a graph of TOTAL DISTANCE TRAVELLED against time "
                "never come back down?",
        "options": [
            {"text": "Because distance already travelled cannot be "
                     "un-travelled",
             "correct": True},
            {"text": "Because the object can never return to where it "
                     "started",
             "correct": False,
             "why": "It often does return. That shows on the "
                    "distance-from-start graph, not on this one."},
            {"text": "Because the time axis only ever increases",
             "correct": False,
             "why": "Time increasing is why the line goes rightwards; it does "
                    "not stop a line falling."},
            {"text": "Because the graph would then show a negative distance",
             "correct": False,
             "why": "A falling line need not reach below zero, so that is not "
                    "what rules it out."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h08",
        "band": "harder",
        "text": "A car's line runs straight from the origin to 600 m at 30 s, "
                "and its speedometer read 20 m/s throughout. Are the two "
                "consistent?",
        "options": [
            {"text": "No — the graph gives 30 m/s, so one reading is wrong",
             "correct": False,
             "why": "30 is the time in seconds, not the speed. The speed is "
                    "600 ÷ 30."},
            {"text": "Yes — the steepness is 600 ÷ 30, which is 20 m/s",
             "correct": True},
            {"text": "No — a speedometer reads instant speed, so it can never "
                     "match a graph",
             "correct": False,
             "why": "For a steady speed the instant value and the average are "
                    "the same number."},
            {"text": "It cannot be decided without the mass of the car",
             "correct": False,
             "why": "Nothing in speed = distance ÷ time uses a mass."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h09",
        "band": "harder",
        "text": "A student finds the steepness of a curved section by joining "
                "its two end points with a ruler. What has that given them?",
        "options": [
            {"text": "The exact speed at the middle of the section",
             "correct": False,
             "why": "It is an average across the whole section, and on a "
                    "curve the speed is different at every point."},
            {"text": "The highest speed reached in the section",
             "correct": False,
             "why": "The highest speed is at the steepest part of the curve, "
                    "which is steeper than the join."},
            {"text": "The average speed across that section", "correct": True},
            {"text": "Nothing usable, because a curve has no steepness",
             "correct": False,
             "why": "A curve has a steepness at every point; joining the ends "
                    "gives a genuine average."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h10",
        "band": "harder",
        "text": "A graph rises 30 m in 10 s, is flat for 20 s, then rises "
                "30 m in 5 s. Which section is fastest, and how fast?",
        "options": [
            {"text": "The first, at 3 m/s, because it comes first",
             "correct": False,
             "why": "Coming first has nothing to do with it: 3 m/s is slower "
                    "than the last section's 6 m/s."},
            {"text": "The flat section, because the line is level there",
             "correct": False,
             "why": "A level line is 0 m/s — the slowest possible, not the "
                    "fastest."},
            {"text": "The last, at 6 m/s", "correct": True},
            {"text": "The last, at 30 m/s", "correct": False,
             "why": "30 m is the distance covered. It has to be divided by "
                    "the 5 s it took."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h11",
        "band": "harder",
        "text": "A runner and a cyclist set off together. The runner's line "
                "is steeper at first, then the cyclist's line crosses it at "
                "100 s. What has happened at the crossing?",
        "options": [
            {"text": "The cyclist has caught up and they are level",
             "correct": True},
            {"text": "The cyclist has reached the runner's top speed",
             "correct": False,
             "why": "Equal speed would be equal steepness, which happens "
                    "before the lines meet, not at the crossing."},
            {"text": "The two have crashed into each other", "correct": False,
             "why": "The graph gives no route, so equal distances from the "
                    "start need not be the same place."},
            {"text": "The runner has stopped for a rest", "correct": False,
             "why": "A rest is a flat section. A crossing on its own says "
                    "nothing about stopping."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h12",
        "band": "harder",
        "text": "A journey's line rises, goes flat, then rises again with "
                "exactly the same steepness as the first part. What does that "
                "tell you?",
        "options": [
            {"text": "The object travelled at the same speed before and after "
                     "the stop",
             "correct": True},
            {"text": "The object travelled the same distance before and after "
                     "the stop",
             "correct": False,
             "why": "Same steepness is same speed. The distances depend on "
                    "how long each part lasted."},
            {"text": "The object returned along the route it came out on",
             "correct": False,
             "why": "Returning would make the line fall. Both rising sections "
                    "are moving away."},
            {"text": "The object took the same time for each moving part",
             "correct": False,
             "why": "Steepness says nothing about how long a section lasts, "
                    "only how fast it was."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h13",
        "band": "harder",
        "text": "A student writes that a flat section means the object is "
                "moving slowly at a steady speed. Correct them, using a "
                "number.",
        "options": [
            {"text": "It is moving at about 1 m/s, which is slow but steady",
             "correct": False,
             "why": "No speed can be read as 1 m/s from a flat line; the "
                    "distance is not changing at all."},
            {"text": "Its steepness is zero, so its speed is 0 m/s and it is "
                     "stopped",
             "correct": True},
            {"text": "Its speed cannot be given a number from a flat line",
             "correct": False,
             "why": "It can, and the number is 0 m/s — a flat line is the "
                    "clearest reading on the graph."},
            {"text": "Its speed is the height of the line in metres",
             "correct": False,
             "why": "The height is the distance from the start. Speed comes "
                    "from steepness, not height."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h14",
        "band": "harder",
        "text": "A train's line rises to 2400 m in 100 s, stays flat for "
                "100 s, then rises to 6000 m by 300 s. What is its average "
                "speed for the whole 300 s?",
        "options": [
            {"text": "30 m/s, the average of 24 m/s and 36 m/s",
             "correct": False,
             "why": "Averaging the two moving speeds leaves out the 100 s "
                    "spent standing still."},
            {"text": "24 m/s, the speed of the first section",
             "correct": False,
             "why": "That is one leg only, and the journey has two more parts "
                    "after it."},
            {"text": "6000 m/s", "correct": False,
             "why": "6000 m is the total distance. It still has to be divided "
                    "by the 300 s."},
            {"text": "20 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h15",
        "band": "harder",
        "text": "A car brakes gently to a stop. Why does its line curve and "
                "flatten out rather than falling?",
        "options": [
            {"text": "Because it is still moving forwards, just more slowly, "
                     "until it stops",
             "correct": True},
            {"text": "Because braking always draws a curve on any graph",
             "correct": False,
             "why": "The curve comes from the speed changing, not from the "
                    "word braking."},
            {"text": "Because the car is going downhill as it brakes",
             "correct": False,
             "why": "The graph never shows the slope of the road; the upright "
                    "axis is distance from the start."},
            {"text": "Because the distance from the start is getting smaller",
             "correct": False,
             "why": "That is what a FALLING line means, and it would need the "
                    "car to reverse."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h16",
        "band": "harder",
        "text": "A pupil's distance-from-home graph shows a walk to school "
                "800 m away taking 600 s, then six hours at school, then the "
                "walk home. Which part is horizontal, and at what height?",
        "options": [
            {"text": "The six hours at school, at a height of 800 m",
             "correct": True},
            {"text": "The six hours at school, at a height of 0 m",
             "correct": False,
             "why": "Zero would mean back at home. At school the pupil is "
                    "800 m from home the whole time."},
            {"text": "The walk home, because it ends at rest",
             "correct": False,
             "why": "The walk home is a falling line; only the moment of "
                    "arrival is at rest."},
            {"text": "No part of it, because the pupil moves around at "
                     "school",
             "correct": False,
             "why": "Moving about the site barely changes the distance from "
                    "home, so the line is drawn flat."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h17",
        "band": "harder",
        "text": "A student plots the same readings with TIME up the side and "
                "distance along the bottom. What does the steepness of their "
                "line now measure?",
        "options": [
            {"text": "The speed, exactly as before", "correct": False,
             "why": "Swapping the axes swaps the division, so it is no longer "
                    "distance over time."},
            {"text": "Nothing — the readings cannot be plotted that way",
             "correct": False,
             "why": "They plot perfectly well. The graph simply means "
                    "something different."},
            {"text": "The seconds taken per metre, which is the speed upside "
                     "down",
             "correct": True},
            {"text": "The total distance travelled during the journey",
             "correct": False,
             "why": "That is read off the axis itself, not from the steepness "
                    "of the line."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · easier ──────────────────────────────────
    {
        "id": "p3-02-e18",
        "band": "easier",
        "text": "A journey's line starts at 15 m when the clock reads 0 s, "
                "rather than at the origin. What does that tell you?",
        "options": [
            {"text": "The graph has a mistake in its first reading",
             "correct": False,
             "why": "A line may begin anywhere on the distance axis. That "
                    "first point is a reading, not an error."},
            {"text": "The object was travelling at 15 m/s when timing began",
             "correct": False,
             "why": "Speed is read from the steepness of the line, not from "
                    "the height of a point."},
            {"text": "The object was already 15 m from the start when timing "
                     "began",
             "correct": True},
            {"text": "The clock was started 15 seconds after the object set "
                     "off",
             "correct": False,
             "why": "15 is read off the distance axis, so it is a length in "
                    "metres and not a time in seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e19",
        "band": "easier",
        "text": "Two walkers are plotted on the same axes. One line begins at "
                "0 s and the other begins at 20 s. What does that tell you?",
        "options": [
            {"text": "The second walker was 20 m behind the first",
             "correct": False,
             "why": "20 is read off the time axis, so it is a time in "
                    "seconds, not a distance."},
            {"text": "The second walker was travelling more slowly",
             "correct": False,
             "why": "Speed is in the steepness of a line, and neither line's "
                    "steepness has been given."},
            {"text": "The second walker's clock was running slowly",
             "correct": False,
             "why": "Both lines share one time axis, so both walkers are "
                    "timed by the same clock."},
            {"text": "The second walker set off 20 seconds later",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e20",
        "band": "easier",
        "text": "Seven readings have been plotted on a distance–time grid. "
                "What is done next to show the whole journey?",
        "options": [
            {"text": "They are joined up in order, from the first reading to "
                     "the last",
             "correct": True},
            {"text": "They are joined by one straight line from the first "
                     "point to the last",
             "correct": False,
             "why": "That hides everything that happened in between, "
                    "including any stop."},
            {"text": "The highest point is circled and the rest left alone",
             "correct": False,
             "why": "The highest point is only the furthest from the start. "
                    "The journey is all seven."},
            {"text": "They are plotted again with the two axes swapped over",
             "correct": False,
             "why": "Time belongs along the bottom, and swapping the axes "
                    "plots something else entirely."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e21",
        "band": "easier",
        "text": "What is the name for the steepness of a line on a graph?",
        "options": [
            {"text": "The origin", "correct": False,
             "why": "The origin is the corner where both axes read zero."},
            {"text": "The interval", "correct": False,
             "why": "An interval is a gap between two readings, not a measure "
                    "of steepness."},
            {"text": "The gradient", "correct": True},
            {"text": "The axis", "correct": False,
             "why": "An axis is one of the two lines the graph is drawn "
                    "against."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e22",
        "band": "easier",
        "text": "A journey's line is shallow for the first part and steep for "
                "the second. Which part was faster?",
        "options": [
            {"text": "The first part", "correct": False,
             "why": "A shallow line covers less distance in each second, so "
                    "it is the slower part."},
            {"text": "Both parts were the same speed", "correct": False,
             "why": "Two sections drawn with different steepness were "
                    "travelled at different speeds."},
            {"text": "The first part, because it lasted longer",
             "correct": False,
             "why": "How long a part lasts is read along the bottom. Speed is "
                    "read from the steepness."},
            {"text": "The second part", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e23",
        "band": "easier",
        "text": "A reading of 12 m at 4 s has to be plotted on a "
                "distance–time grid. Where does the point go?",
        "options": [
            {"text": "4 along the time axis and 12 up the distance axis",
             "correct": True},
            {"text": "12 along the time axis and 4 up the distance axis",
             "correct": False,
             "why": "That swaps the two readings over and plots a journey "
                    "that never happened."},
            {"text": "12 along the time axis and 12 up the distance axis",
             "correct": False,
             "why": "The time reading is 4 s, and it is the time that goes "
                    "along the bottom."},
            {"text": "4 along the time axis and 4 up the distance axis",
             "correct": False,
             "why": "The distance reading is 12 m, and it is the distance "
                    "that goes up the side."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e24",
        "band": "easier",
        "text": "A straight section climbs from 0 m to 20 m between 0 s and "
                "5 s. What is its gradient?",
        "options": [
            {"text": "0.25 m/s", "correct": False,
             "why": "That is 5 ÷ 20, the time divided by the distance."},
            {"text": "4 m/s", "correct": True},
            {"text": "100 m/s", "correct": False,
             "why": "That multiplies 20 by 5. A gradient comes from a "
                    "division."},
            {"text": "15 m/s", "correct": False,
             "why": "That is 20 − 5. A distance and a time cannot be "
                    "subtracted from one another."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e25",
        "band": "easier",
        "text": "A journey's line rises to its highest point at 40 s and then "
                "falls. What was happening at 40 s?",
        "options": [
            {"text": "The object was travelling at its fastest",
             "correct": False,
             "why": "Speed is read from the steepness, and the height of a "
                    "point says nothing about it."},
            {"text": "The object had got back to the start", "correct": False,
             "why": "Back at the start is where the line reaches zero, at the "
                    "bottom of the graph."},
            {"text": "The object was at its furthest from the start and "
                     "turned back",
             "correct": True},
            {"text": "The object was stopped for the whole journey",
             "correct": False,
             "why": "A stopped object draws a flat line all the way, and this "
                    "one rises and then falls."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e26",
        "band": "easier",
        "text": "Why can the line on a distance-from-the-start graph never go "
                "below the time axis?",
        "options": [
            {"text": "Because the graph would then show a negative time",
             "correct": False,
             "why": "Below the time axis is a negative distance, not a "
                    "negative time."},
            {"text": "Because the object would then have to travel backwards "
                     "in time",
             "correct": False,
             "why": "Travelling back towards the start brings the line down "
                    "to zero, and no further."},
            {"text": "Because a graph has no room drawn in below the axis",
             "correct": False,
             "why": "Room could always be drawn. The reason is that the "
                    "quantity itself cannot go there."},
            {"text": "Because you cannot be less than no distance from the "
                     "start",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e27",
        "band": "easier",
        "text": "A line is flat for 10 s and then begins to rise. What "
                "happened?",
        "options": [
            {"text": "The object was moving slowly and then sped up",
             "correct": False,
             "why": "A flat line is stopped, not slow: the distance from the "
                    "start was not changing."},
            {"text": "The object was stopped and then set off again",
             "correct": True},
            {"text": "The object came back to the start and then set off",
             "correct": False,
             "why": "Coming back makes the line fall. A flat line stays at "
                    "the same distance."},
            {"text": "The object went round a bend and then straightened up",
             "correct": False,
             "why": "A distance–time graph holds no directions in space, so "
                    "no bend can appear on it."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e28",
        "band": "easier",
        "text": "A walk at 1 m/s and a run at 4 m/s are drawn on the same "
                "axes. Which line is shallower?",
        "options": [
            {"text": "The walk", "correct": True},
            {"text": "The run", "correct": False,
             "why": "The run covers four metres in each second, so its line "
                    "climbs four times as steeply."},
            {"text": "Both have the same steepness", "correct": False,
             "why": "Two different speeds give two different steepnesses on "
                    "the same axes."},
            {"text": "Whichever of the two lasted longer", "correct": False,
             "why": "How long a journey lasts is read along the bottom and "
                    "does not change the steepness."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e29",
        "band": "easier",
        "text": "A distance–time graph carries two quantities and no others. "
                "Which two?",
        "options": [
            {"text": "Time, and the speed of the object", "correct": False,
             "why": "Speed is not plotted. It is hidden in the steepness and "
                    "has to be worked out."},
            {"text": "Distance from the start, and speed", "correct": False,
             "why": "Speed is not an axis on this graph. Both axes can be "
                    "read straight off."},
            {"text": "Time, and distance from the start", "correct": True},
            {"text": "Time, and the direction the object travelled",
             "correct": False,
             "why": "No direction in space appears anywhere on a "
                    "distance–time graph."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-e30",
        "band": "easier",
        "text": "Which of these journeys draws a horizontal line on a "
                "distance–time graph?",
        "options": [
            {"text": "A car travelling at a steady 30 m/s", "correct": False,
             "why": "A steady speed draws a straight line that climbs, not a "
                    "flat one."},
            {"text": "A car slowing down gently to a stop", "correct": False,
             "why": "Slowing down makes the line get gradually less steep, "
                    "and only flat once it has stopped."},
            {"text": "A car driving back towards where it started",
             "correct": False,
             "why": "Coming back brings the line down towards zero rather "
                    "than holding it level."},
            {"text": "A car waiting at a red light", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ────────────────────────────────
    {
        "id": "p3-02-s18",
        "band": "standard",
        "text": "Between 10 s and 25 s a journey's line climbs steadily from "
                "20 m to 80 m. How fast was the object going?",
        "options": [
            {"text": "4 m/s", "correct": True},
            {"text": "3.2 m/s", "correct": False,
             "why": "That is 80 ÷ 25, using the two end readings instead of "
                    "the change in each."},
            {"text": "6 m/s", "correct": False,
             "why": "That uses 10 s, the starting time, rather than the 15 s "
                    "the climb took."},
            {"text": "2 m/s", "correct": False,
             "why": "The line climbed 60 m, not 30 m: take 20 from 80."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s19",
        "band": "standard",
        "text": "A journey's line climbs to 50 m by 10 s, and then climbs to "
                "80 m by 30 s. Which section was faster, and by how much?",
        "options": [
            {"text": "The second, at 2.7 m/s against 5 m/s", "correct": False,
             "why": "2.7 m/s is 80 ÷ 30, and it is smaller than the first "
                    "section's speed in any case."},
            {"text": "The first, at 5 m/s against 1.5 m/s", "correct": True},
            {"text": "The second, at 1.5 m/s against 5 m/s", "correct": False,
             "why": "1.5 m/s is the second section's speed, and it is the "
                    "smaller of the two."},
            {"text": "Neither: both sections climb, so both are the same "
                     "speed",
             "correct": False,
             "why": "Climbing is not the test. How steeply the line climbs "
                    "is."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s20",
        "band": "standard",
        "text": "Six readings from a motion sensor lie close to a straight "
                "line, but one sits well above it. What is the most likely "
                "explanation?",
        "options": [
            {"text": "The object sped up for a moment, so the line should "
                     "bend up to it",
             "correct": False,
             "why": "One point out of line is a reading to check, not a "
                    "change of speed the other five missed."},
            {"text": "The line should be drawn through every point, however "
                     "it looks",
             "correct": False,
             "why": "One line through all the readings is what evens the "
                    "small errors out."},
            {"text": "The time axis needs rescaling so that the point fits "
                     "the line",
             "correct": False,
             "why": "Changing a scale moves every point, not one, and it "
                    "cannot mend a bad reading."},
            {"text": "That one reading is a mistake, so it is left out of the "
                     "line",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s21",
        "band": "standard",
        "text": "A straight line runs from the origin to 60 m at 30 s. How "
                "far from the start was the object at 20 s?",
        "options": [
            {"text": "30 m", "correct": False,
             "why": "That is half the distance, but 20 s is two thirds of the "
                    "way through rather than half."},
            {"text": "45 m", "correct": False,
             "why": "45 m is reached at 22.5 s on this line, not at 20 s."},
            {"text": "40 m", "correct": True},
            {"text": "20 m", "correct": False,
             "why": "That reads the time off the distance axis; here 20 is a "
                    "number of seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s22",
        "band": "standard",
        "text": "On a graph the time axis is marked every 5 s, and the line "
                "reaches 45 m at the fourth mark. What is the average speed "
                "up to that point?",
        "options": [
            {"text": "2.25 m/s", "correct": True},
            {"text": "11.25 m/s", "correct": False,
             "why": "That divides by 4, the number of marks, instead of by "
                    "the 20 s they stand for."},
            {"text": "9 m/s", "correct": False,
             "why": "That divides by 5 s, the size of one mark, rather than "
                    "by the whole 20 s."},
            {"text": "0.44 m/s", "correct": False,
             "why": "That divides the time by the distance, the wrong way "
                    "round."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s23",
        "band": "standard",
        "text": "A line curves so that it gets less and less steep, and then "
                "becomes flat. Describe the motion.",
        "options": [
            {"text": "It sped up, then held a steady speed", "correct": False,
             "why": "Speeding up makes a line get steeper, and a flat line is "
                    "not a steady speed."},
            {"text": "It slowed down and then stopped", "correct": True},
            {"text": "It went round a bend and then straightened out",
             "correct": False,
             "why": "No bend in space can appear on a distance–time graph, "
                    "because the axes carry no directions."},
            {"text": "It came back towards the start and then stopped",
             "correct": False,
             "why": "Coming back brings the line down, and this line never "
                    "falls."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s24",
        "band": "standard",
        "text": "A van's line has three flat sections of 60 s each within a "
                "journey lasting 600 s. For how long was the van moving?",
        "options": [
            {"text": "180 s", "correct": False,
             "why": "That is the time the van spent stopped, not the time it "
                    "spent moving."},
            {"text": "420 s", "correct": True},
            {"text": "540 s", "correct": False,
             "why": "That takes off one flat section instead of all three."},
            {"text": "600 s", "correct": False,
             "why": "That is the whole journey, including the three stops."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s25",
        "band": "standard",
        "text": "A line climbs to 40 m in 10 s and is then flat until 40 s. A "
                "student says the object travelled at 4 m/s for the whole "
                "40 s. Correct them.",
        "options": [
            {"text": "4 m/s was the speed for the whole journey, and 1 m/s "
                     "for the climb",
             "correct": False,
             "why": "That swaps the two round: 4 m/s is the climb and 1 m/s "
                    "the whole journey."},
            {"text": "The object travelled at 4 m/s throughout, but only for "
                     "the first 10 s",
             "correct": False,
             "why": "The second half of that sentence contradicts the first, "
                    "and the claim was about all 40 s."},
            {"text": "4 m/s was only the first 10 s; over all 40 s the "
                     "average was 1 m/s",
             "correct": True},
            {"text": "The speed cannot be found, because the line stops "
                     "climbing",
             "correct": False,
             "why": "A flat section is a speed of 0 m/s, which is exactly "
                    "what makes the average smaller."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s26",
        "band": "standard",
        "text": "A motion sensor at the start records a walker going out and "
                "coming back. The line falls from 24 m to 0 m over 8 s. How "
                "fast was the walk back?",
        "options": [
            {"text": "24 m/s", "correct": False,
             "why": "That is the distance alone. A speed needs it divided by "
                    "the 8 s taken."},
            {"text": "0.33 m/s", "correct": False,
             "why": "That divides the time by the distance, the wrong way "
                    "round."},
            {"text": "192 m/s", "correct": False,
             "why": "That multiplies the two readings instead of dividing "
                    "them."},
            {"text": "3 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s27",
        "band": "standard",
        "text": "Why can a distance–time graph never have a vertical section?",
        "options": [
            {"text": "It would mean the object had stopped moving",
             "correct": False,
             "why": "A stopped object draws a horizontal line, along which "
                    "time passes and distance does not."},
            {"text": "It would mean covering a distance in no time at all",
             "correct": True},
            {"text": "It would mean the object had gone backwards",
             "correct": False,
             "why": "Going back towards the start draws a line that falls, "
                    "not one that stands upright."},
            {"text": "It would mean the time axis had the wrong scale",
             "correct": False,
             "why": "Any scale still runs left to right, so a vertical line "
                    "would still need zero time."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s28",
        "band": "standard",
        "text": "Two lines on the same axes are parallel, but one stays 20 m "
                "above the other throughout. What does that tell you?",
        "options": [
            {"text": "One object was travelling 20 m/s faster than the other",
             "correct": False,
             "why": "A difference in speed would make the two lines spread "
                    "apart rather than stay parallel."},
            {"text": "One object set off 20 seconds before the other",
             "correct": False,
             "why": "20 is read off the distance axis, so it is a gap in "
                    "metres and not in seconds."},
            {"text": "One object travelled for 20 seconds longer than the "
                     "other",
             "correct": False,
             "why": "How long each lasted is read along the bottom, and "
                    "parallel lines say nothing about it."},
            {"text": "Both held the same speed, one 20 m further from the "
                     "start",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s29",
        "band": "standard",
        "text": "A dog runs 30 m away from its owner and 30 m back in 20 s "
                "altogether. What is its average speed, and where does its "
                "line finish?",
        "options": [
            {"text": "1.5 m/s, and the line finishes at 60 m", "correct": False,
             "why": "1.5 m/s uses one leg only, and a distance-from-the-start "
                    "line cannot finish at 60 m here."},
            {"text": "3 m/s, and the line finishes at 60 m", "correct": False,
             "why": "The speed is right, but the dog ends up beside its "
                    "owner, at 0 m from the start."},
            {"text": "3 m/s, and the line finishes at 0 m", "correct": True},
            {"text": "0 m/s, because it ended where it began", "correct": False,
             "why": "Ending where it began makes the distance from the start "
                    "zero, not the speed."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-s30",
        "band": "standard",
        "text": "Line A is steeper than line B, but B's line ends higher up "
                "the distance axis. Which object finished further from the "
                "start?",
        "options": [
            {"text": "B's, because its line ends higher up", "correct": True},
            {"text": "A's, because its line is steeper", "correct": False,
             "why": "Steepness is speed. How far from the start is read as a "
                    "height, not as a slope."},
            {"text": "A's, because it was travelling faster", "correct": False,
             "why": "A fast object travelling for a short time can finish "
                    "closer than a slow one that keeps going."},
            {"text": "Neither: the two travelled the same distance",
             "correct": False,
             "why": "The two lines end at different heights, so the two "
                    "distances are different."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ──────────────────────────────────
    {
        "id": "p3-02-h18",
        "band": "harder",
        "text": "A line curves upwards. A student lays a ruler so that it "
                "just touches the curve at 20 s and works out the ruler's "
                "steepness. What have they found?",
        "options": [
            {"text": "The speed at that one moment", "correct": True},
            {"text": "The average speed for the whole journey",
             "correct": False,
             "why": "An average over the whole journey comes from joining the "
                    "two end points, not from touching one."},
            {"text": "The total distance travelled by 20 s", "correct": False,
             "why": "A distance is read off the upright axis as a height. "
                    "Steepness gives a speed."},
            {"text": "The time taken to reach 20 m", "correct": False,
             "why": "A time is read along the bottom axis, and a steepness is "
                    "not read off either axis alone."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h19",
        "band": "harder",
        "text": "The same journey is drawn twice, once with the distance axis "
                "running to 100 m and once to 1000 m. Why does the line look "
                "far steeper on the first?",
        "options": [
            {"text": "The object really was travelling faster on that graph",
             "correct": False,
             "why": "One journey cannot have two speeds. Only the drawing has "
                    "changed."},
            {"text": "The time axis must have been shortened as well",
             "correct": False,
             "why": "Nothing has been said about the time axis, and "
                    "stretching the distance axis is enough on its own."},
            {"text": "The distance axis is stretched, so the same climb looks "
                     "bigger",
             "correct": True},
            {"text": "The first graph shows a different, faster part of the "
                     "journey",
             "correct": False,
             "why": "Both graphs show the same journey from beginning to "
                    "end."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h20",
        "band": "harder",
        "text": "A runner goes 200 m out in 50 s and 200 m back in 50 s. On a "
                "graph of TOTAL DISTANCE TRAVELLED, what value does the line "
                "reach at 100 s, and what does the second section do?",
        "options": [
            {"text": "0 m, because the runner came back to where she started",
             "correct": False,
             "why": "That is what the distance-from-the-start graph does. A "
                    "total distance cannot fall."},
            {"text": "400 m, with the second section still climbing at 4 m/s",
             "correct": True},
            {"text": "400 m, with the second section falling at 4 m/s",
             "correct": False,
             "why": "A distance already travelled cannot be un-travelled, so "
                    "this line cannot fall."},
            {"text": "200 m, because she got no further than 200 m away",
             "correct": False,
             "why": "How far away she got is the other graph's question. This "
                    "one adds the two legs together."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h21",
        "band": "harder",
        "text": "A train's graph has time in minutes along the bottom and "
                "distance in kilometres up the side. One section climbs 6 km "
                "in 4 minutes. What is that speed in metres per second?",
        "options": [
            {"text": "1.5 m/s", "correct": False,
             "why": "That is 6 ÷ 4 with neither unit changed, so it is "
                    "kilometres per minute."},
            {"text": "1500 m/s", "correct": False,
             "why": "The kilometres were changed to metres but the minutes "
                    "were left as minutes."},
            {"text": "0.025 m/s", "correct": False,
             "why": "The minutes were changed to seconds but the distance was "
                    "left in kilometres."},
            {"text": "25 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h22",
        "band": "harder",
        "text": "A journey's steepest section works out at 8 m/s, yet the "
                "average speed for the whole trip is 3 m/s. How can both be "
                "true?",
        "options": [
            {"text": "The steepest section must have been measured wrongly",
             "correct": False,
             "why": "Nothing is wrong: a fast section can sit inside a slow "
                    "journey."},
            {"text": "The average is found by halving the fastest section's "
                     "speed",
             "correct": False,
             "why": "An average comes from the total distance and the total "
                    "time, not from the fastest part."},
            {"text": "The rest of the journey was slower or stopped, and "
                     "lasted longer",
             "correct": True},
            {"text": "An average speed is the middle of all the sections' "
                     "speeds",
             "correct": False,
             "why": "The sections are not all the same length, so their "
                    "speeds cannot simply be averaged."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h23",
        "band": "harder",
        "text": "Two students each work out the gradient of the same straight "
                "section and get 2.4 m/s and 2.6 m/s. The arithmetic is right "
                "in both. Why do they differ?",
        "options": [
            {"text": "They read the points off the axes slightly differently",
             "correct": True},
            {"text": "One of them used the total-distance axis instead",
             "correct": False,
             "why": "Only one graph has been drawn, and both were reading the "
                    "same line on it."},
            {"text": "The steepness changes along the section that they "
                     "measured",
             "correct": False,
             "why": "The section is straight, so its steepness is the same "
                    "all the way along it."},
            {"text": "One of them swapped the two axes over before reading",
             "correct": False,
             "why": "Swapping the axes would give a reading in seconds for "
                    "each metre, not 2.6 m/s."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h24",
        "band": "harder",
        "text": "A 3000 m journey averages 5 m/s overall, and its line is "
                "flat for a third of the total time. How fast was the object "
                "moving while it was moving?",
        "options": [
            {"text": "5 m/s", "correct": False,
             "why": "That is the average including the stop, and the moving "
                    "speed has to be bigger than it."},
            {"text": "15 m/s", "correct": False,
             "why": "That divides 3000 m by 200 s, which is the third of the "
                    "time spent STOPPED."},
            {"text": "10 m/s", "correct": False,
             "why": "That divides 3000 m by 300 s, which is half the total "
                    "time rather than two thirds."},
            {"text": "7.5 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h25",
        "band": "harder",
        "text": "A falling section of a line drops from 48 m to 0 m over "
                "12 s. How fast was the object moving, and which way?",
        "options": [
            {"text": "4 m/s, away from the start", "correct": False,
             "why": "A falling line means the distance from the start is "
                    "getting smaller, so it is heading back."},
            {"text": "48 m/s, back towards the start", "correct": False,
             "why": "48 is the distance covered. The speed comes from "
                    "dividing it by the 12 s taken."},
            {"text": "4 m/s, back towards the start", "correct": True},
            {"text": "0.25 m/s, back towards the start", "correct": False,
             "why": "That divides the time by the distance, the wrong way "
                    "round."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h26",
        "band": "harder",
        "text": "A walker sets off from a sensor and holds one steady speed. "
                "The sensor begins recording 5 s late, and its first reading "
                "is 8 m at 5 s. What was the walking speed?",
        "options": [
            {"text": "1.6 m/s", "correct": True},
            {"text": "8 m/s", "correct": False,
             "why": "That treats the first reading as a speed, and it is a "
                    "distance in metres."},
            {"text": "0.625 m/s", "correct": False,
             "why": "That divides 5 s by 8 m, the wrong way round."},
            {"text": "3.2 m/s", "correct": False,
             "why": "That divides 8 m by 2.5 s, halving the time for no "
                    "reason."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h27",
        "band": "harder",
        "text": "Readings taken every 2 s give distances of 0 m, 2 m, 8 m, "
                "18 m and 32 m. What is happening, and what would the next "
                "reading be if the pattern holds?",
        "options": [
            {"text": "Slowing down, and the next reading would be 40 m",
             "correct": False,
             "why": "Each 2 s covers more ground than the one before, so it "
                    "is speeding up rather than slowing."},
            {"text": "Speeding up, and the next reading would be 50 m",
             "correct": True},
            {"text": "A steady speed, and the next reading would be 46 m",
             "correct": False,
             "why": "A steady speed adds the same distance each time, and "
                    "these gaps grow."},
            {"text": "Speeding up, and the next reading would be 64 m",
             "correct": False,
             "why": "64 doubles 32. The gaps grow by 4 m each time, so the "
                    "next gap is 18 m."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h28",
        "band": "harder",
        "text": "Seven readings from a motion sensor lie almost on a straight "
                "line. Why is one straight line drawn through them better "
                "than joining each point to the next?",
        "options": [
            {"text": "Joining the points makes the line too steep to read",
             "correct": False,
             "why": "Joining points changes the shape in both directions, and "
                    "steepness is not the issue."},
            {"text": "One straight line is quicker to draw than seven joins",
             "correct": False,
             "why": "How quick it is to draw is not a reason. What the line "
                    "is for is the reason."},
            {"text": "Joining the points would show speed changes, which "
                     "cannot happen",
             "correct": False,
             "why": "An object can change speed. Here the wobbles come from "
                    "small errors in the readings."},
            {"text": "Each reading carries a small error, and one line evens "
                     "them out",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h29",
        "band": "harder",
        "text": "Two cars cover the same 900 m in the same 60 s. One line is "
                "straight and the other has a flat section in the middle. "
                "What is the same and what is different?",
        "options": [
            {"text": "Both travelled at 15 m/s the whole way along",
             "correct": False,
             "why": "The second car stopped for part of it, so it cannot have "
                    "held one speed."},
            {"text": "The second car's average is lower, because it stopped",
             "correct": False,
             "why": "Same distance and same time give the same average. Only "
                    "the moving speed differs."},
            {"text": "The average is 15 m/s for both, but the second went "
                     "faster when moving",
             "correct": True},
            {"text": "The second car travelled further, because its line is "
                     "longer",
             "correct": False,
             "why": "Both lines end at 900 m, so both cars covered the same "
                    "ground."},
        ],
        "figure": None,
    },
    {
        "id": "p3-02-h30",
        "band": "harder",
        "text": "A car's line climbs at 20 m/s for 50 s and then goes flat. "
                "How long must the flat section last for the average speed "
                "over the whole journey to fall to 8 m/s?",
        "options": [
            {"text": "75 s", "correct": True},
            {"text": "50 s", "correct": False,
             "why": "Making the two parts equal gives 1000 m in 100 s, which "
                    "is 10 m/s."},
            {"text": "125 s", "correct": False,
             "why": "125 s is the total time needed, and 50 s of it has "
                    "already gone."},
            {"text": "25 s", "correct": False,
             "why": "That would give 1000 m in 75 s, which is 13.3 m/s."},
        ],
        "figure": None,
    },
]

