# -*- coding: utf-8 -*-
"""Distance-time graphs, in the lean shape. Spec table: docs/lessons/wave1/ks3-distance-time-graphs.md."""

_CURVE = [[round(t / 2.0, 2), round(20 * (3 * (t / 20.0) ** 2 - 2 * (t / 20.0) ** 3), 2)]
          for t in range(0, 21)]

LESSON = {
    "slug": "distance-time-graphs",
    "start": {
        "setup": "A walker goes 6 m along a corridor, waits at a door, then runs on. A sensor draws the journey.",
        "question": "If you had to guess, while the walker waits, does the line go flat, or drop to the bottom?",
        "options": [
            ("It goes flat",
             "It goes flat. The walker is still 6 m from the start. So the line stays at that height."),
            ("It drops to the bottom",
             "It goes flat. The walker is still 6 m from the start. So the line stays at that height."),
        ],
        "answer": 0,
    },
    "words": ["distance-time graph", "gradient", "stationary", "speed"],
    "word_defs": {
        "distance-time graph": "A graph of how far an object is from its start, against time.",
        "gradient": "How steep a line is. On a distance-time graph, the gradient is the speed.",
        "stationary": "Not moving. The distance from the start does not change.",
        "speed": "The distance an object travels each second.",
    },
    "knowledge": [
        {"kind": "card", "title": "Reading the graph",
         "body": [{"figure": "p3-dt-journey"},
                  "A walker goes 6 m, waits at a door, then runs 12 m.",
                  "Time goes along the bottom. Distance from the start goes up the side.",
                  "The line shows how far the walker is from the start at each time.",
                  "The graph shows the journey. It does not show the route."]},
        {"kind": "card", "title": "Gradient is speed",
         "body": ["The gradient is how steep the line is.",
                  "A steeper line means a faster speed.",
                  "A less steep line means a slower speed.",
                  "Gradient = change in distance ÷ change in time.",
                  "That is the speed equation again: speed = distance ÷ time.",
                  "In the graph, the walk is 6 m in 6 s. That is 1 m/s.",
                  "The run is 12 m in 4 s. That is 3 m/s."]},
        {"kind": "card", "title": "A flat line means stopped",
         "body": ["A flat line means the distance is not changing.",
                  "The object is stationary. Its speed is 0 m/s.",
                  "A steady speed is a straight line that slopes up."]},
        {"kind": "reveal", "title": "What each line means",
         "cols": ["Meaning", "Why"],
         "rows": [
             ("Straight line, sloping up", "Steady speed", "The same distance every second."),
             ("A steeper straight line", "Faster", "More distance every second."),
             ("Flat line", "Stopped", "The distance is not changing."),
             ("Line getting steeper", "Speeding up", "The speed is increasing."),
             ("Line getting less steep", "Slowing down", "The speed is decreasing."),
             ("Line sloping down", "Coming back", "The distance from the start is getting smaller."),
         ]},
        {"kind": "card", "title": "Curved lines",
         "body": [{"figure": "p3-dt-curve"},
                  "A curved line means the speed is changing.",
                  "Where the line gets steeper, the object speeds up.",
                  "Where it gets less steep, the object slows down."]},
        {"kind": "card", "title": "Worked example: finding speed from a graph",
         "body": ["A line goes from 10 m at 2 s to 40 m at 12 s. Find the speed.",
                  {"points": ["Convert: nothing. Distance is in m and time is in s.",
                              "Distance moved: 40 m minus 10 m = 30 m",
                              "Time taken: 12 s minus 2 s = 10 s",
                              "Formula: speed (v) = distance (s) ÷ time (t)",
                              "Insert: speed = 30 m ÷ 10 s",
                              "Answer: speed = 3 m/s"]}]},
        {"kind": "card", "title": "Going back to the start",
         "body": ["A line sloping down means the object is coming back.",
                  "Its distance from the start is getting smaller.",
                  "The steepness still shows the speed.",
                  "Distance travelled keeps adding up.",
                  "A lift goes 30 m up and 30 m down. It has travelled 60 m.",
                  "Its distance from the start is 0 m."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A distance-time graph is a picture of the route, so a rising line means uphill.",
              "The line shows distance from the start. It never shows the route."),
             ("A flat line means a steady speed.",
              "A flat line means stopped. A steady speed slopes up."),
             ("A curved line means the object goes round a bend.",
              "A curve means the speed is changing. It does not show the route."),
             ("A steeper line means the object went further.",
              "Steeper means faster. Read how far from the distance axis."),
         ]}]},
    ],
    "key_fact": "A distance-time graph shows distance from the start against time. "
                "The gradient is the speed: steeper means faster, and a flat line means stopped. "
                "A curve means the speed is changing.",
    "deeper": [
        {"kind": "card", "title": "Two objects on one graph",
         "body": ["Two lines can share the same axes.",
                  "Where the lines cross, the objects are at the same place at the same time.",
                  "The steeper line belongs to the faster object."]},
        {"kind": "card", "title": "Speed at one moment",
         "body": ["On a curve, the gradient changes along the line.",
                  "At GCSE you draw a tangent to a curve.",
                  "The gradient of the tangent is the speed at that moment."]},
    ],
    "try": None,
    "tutor_body": "Want to check why a flat line means stopped?",
    "ks4_becomes": "Gradients of curved graphs, velocity-time graphs, and the area under them.",
    "figures": [
        {"id": "p3-dt-journey", "kind": "diagram", "status": "drawn", "art": "dist-time-line",
         "title": "A walk, a wait, then a run",
         "desc": "A distance-time graph. Time runs from 0 to 14 seconds along the bottom. Distance from "
                 "the start runs from 0 to 20 metres up the side. The line climbs from 0 to 6 metres in "
                 "6 seconds, labelled 1 metre per second. It then goes flat for 4 seconds, labelled 0 "
                 "metres per second. It then climbs from 6 to 18 metres in 4 seconds, labelled 3 metres "
                 "per second.",
         "caption": "A walk, a wait, then a run.",
         "data": {"x_max": 14, "y_max": 20, "x_step": 2, "y_step": 5,
                  "x_label": "Time (s)", "y_label": "Distance (m)",
                  "points": [[0, 0], [6, 6], [10, 6], [14, 18]],
                  "speeds": [{"seg": 0, "dx": -14, "dy": -18},
                             {"seg": 1, "dx": 0, "dy": -12},
                             {"seg": 2, "dx": -16, "dy": -4, "anchor": "end"}]}},
        {"id": "p3-dt-curve", "kind": "diagram", "status": "drawn", "art": "dist-time-line",
         "title": "A curved distance-time line",
         "desc": "A distance-time graph. Time runs from 0 to 10 seconds along the bottom. Distance runs "
                 "from 0 to 20 metres up the side. The line starts flat and gets steadily steeper up to "
                 "the middle, labelled speeding up. It then gets less steep until it levels off at "
                 "20 metres, labelled slowing down.",
         "caption": "A line that gets steeper, then less steep.",
         "data": {"x_max": 10, "y_max": 20, "x_step": 2, "y_step": 5,
                  "x_label": "Time (s)", "y_label": "Distance (m)",
                  "points": _CURVE,
                  "notes": [{"t": 2.5, "d": 3.1, "text": "Speeding up", "dx": -61, "dy": -48, "anchor": "start"},
                            {"t": 7.5, "d": 16.9, "text": "Slowing down", "dx": 63, "dy": 60, "anchor": "end"}]}},
    ],
    "figure_caption": {"p3-dt-journey": None, "p3-dt-curve": None},   # the card text already says it
    "ladder_stem": {
        "recall": "A distance-time graph is horizontal between 20 s and 35 s. "
                  "What was happening in those fifteen seconds?",
        "explain": "Explain why the steepness of a distance-time graph shows the speed. "
                   "Explain why a flat section means the object has stopped. "
                   "Use a worked example with numbers.",
        "produce": "A lift rises 30 m in 20 s. It waits 10 s. Then it returns to the ground floor in 15 s. "
                   "Calculate its speed going up and coming down, with units. Say which is faster. "
                   "What is its speed during the wait? "
                   "When it is back on the ground floor, how far has it travelled in total? "
                   "Why is that not the same as its distance from the ground floor?",
    },
    "ladder_ticks": [
        ["Says the steepness shows how many metres are covered in each second, which is the speed.",
         "Says steepness shows the metres covered each second, which is the speed."],
        ["Says a flat section means the distance from the start is not changing, so the object is stopped.",
         "Says a flat line means the distance is not changing, so it is stopped."],
        ["Gives a worked example, such as a line rising 30 m in 10 s showing a speed of 3 m/s.",
         "Gives a worked example, such as 30 m in 10 s is 3 m/s."],
        ["Says the speed is 0 m/s during the wait, because its distance from the ground floor does not change.",
         "Says the speed is 0 m/s in the wait, as the distance does not change."],
        ["Says the total distance travelled is 60 m, because distance travelled only ever adds up, while the distance from the ground floor is back to 0 m.",
         "Says 60 m travelled, but the distance from the ground floor is 0 m."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Slowing down makes the line less steep. A flat line means stopped.",
            1: "Going back makes the line fall towards zero. A flat line stays where it is.",
            3: "A steady speed gives a straight line that still climbs. Flat means no change in distance.",
        },
        "apply": {
            0: "Not always. A steep line over 2 s covers less than a gentle one over 60 s.",
            1: "Time is read along the bottom axis. Steepness shows speed, not time.",
            2: "The graph does not show hills. Steepness is speed.",
        },
    },
}
