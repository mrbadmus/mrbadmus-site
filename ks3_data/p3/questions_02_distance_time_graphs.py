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
]
