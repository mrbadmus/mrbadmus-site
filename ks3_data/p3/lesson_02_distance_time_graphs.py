"""P3 L2 — Distance–time graphs (INVESTIGATION).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p3/p3-02-distance-time-graphs.dc.html`.

Her page wins outright. The seven sensor readings, the three read-back
questions, the four walking modes and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA FIGURE, AND THAT IS MEASURED ──────────────

This lesson draws no triangle and no beam, and the word "triangle" appears
zero times on Design's page. That is correct rather than an omission: the
speed here is a GRADIENT read off a line, not a quantity computed from a
rule. A triangle would invite a student to divide two numbers they have
not measured. The lesson's one arithmetic moment — 12 m in 4 s gives
3 m/s — is deliberately the same division `p3-01` already drew, and it
is named as such.

── ⚖️ RULED · THE PLOTTING GRID IS REAL BUTTONS, NOT A CANVAS ────────

Design's §2.2 and her "For Code" §6 both insist on it, and she is right in
a way that is easy to lose: *"If that is re-implemented as canvas clicks
during the port, it will silently drop keyboard access — the R15
failure will not show up in a screenshot."* Every intersection is a real
`<button>` with an accessible name naming its coordinates. `r_graph_plot`
asserts the button count matches the grid, for that reason.

⚠️ And the feedback for a wrong tap is a LOCATION STATEMENT, never a mark
(R3): the page says where the student actually tapped, in the graph's own
units, and leaves the verdict to them.

── ⚖️ RULED · "DISTANCE FROM THE START" STAYS AS STRETCH ─────────────

Design's flag 7 asks whether the distance-travelled / distance-from-start
contrast is legitimate KS3 stretch or GCSE creep. It stays, in the stretch
layer, with no assessment attached — and rung 4's last criterion asks
for it, which is where it earns its place. It is displacement in
everything but name, and the page never uses the word. `KS3.P.MOT.02` is
about representing a journey; a graph that can never come down is a
different representation of the SAME journey, so it is inside the
statement rather than beyond it.

── ⚖️ RULED · "A FLAT LINE IS STOPPED, NOT SLOW" IS THE KEY FACT ─────

Design's flag 8 worries that a student who has just learned "steeper =
faster" will read flat as "slowest possible = very slow". Her page attacks
it twice — read-back question 1 and ladder rung 1 — and that is
enough, because both make the student COMMIT to an answer rather than read
a correction. Kept as she drew it.

── ⚠️ FOUR RAIL STOPS · `s-think` IS NOT ONE ────────────────────────

    s-hook · s-plot · s-match · s-ladder

Her notes say five. Her 23 Aug audit records the cut ("the remaining nine
drop THINK only") and the delivered `RAIL` carries four. The drawing was
measured. `#s-think` keeps its id.

── ⚠️ SHELLS ARE MEASURED OFF DESIGN'S CLASS ATTRIBUTE ─────────────

    #s-plot    `ks3-block`                        → `check`
    #s-match   `ks3-block ks3-dark ks3-practical` → `practical`
    #s-think   `ks3-block ks3-misconception`      → `misconception`

── ⚖️ THREE MINTS IN THE `FORCE` FAMILY ───────────────────────────

    FORCE-06  the graph is a picture of the route  `#s-think` quote 1
    FORCE-07  a flat line means a steady speed     `#s-plot` read-back q1
    FORCE-08  a curve means going round a bend     `#s-think` quote 2

Design's proposed table names the first two (as her `FORCE-05`/`FORCE-06`)
and a third, "a steeper line means it went further", which she attaches to
rung 2. That belief IS on the page — it is rung 2's first distractor
— but it is the SAME error as FORCE-07 read from the other side: both
are reading a gradient as something other than a speed. It takes no row of
its own, following P1's precedent for a second quote that re-dresses an
existing belief. `FORCE-08` replaces it and is a genuinely separate one
that arrived with her 23 Aug second quote.
"""

LESSON = {
    "slug":  "distance-time-graphs",
    "title": "Distance–time graphs",
    "discipline": "physics",
    "unit": "Describing motion",
    "family": "INVESTIGATION",

    "covers": ["KS3.P.MOT.02"],
    "touches": ["KS3.WS.ANA.02"],
    "beyond_statutory": False,
    "threads": [{"id": "motion", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["speed"],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "Someone walks down a level corridor and the graph "
                        "climbs, goes flat, then climbs more steeply. The "
                        "floor never changed height. Plot seven readings "
                        "yourself and find out what the height means.",

    "big_question": "Someone walks 6 m down a level corridor, waits at a "
                    "door, then runs the last 12 m. Drawn as a graph, that "
                    "journey rises, goes flat, then rises much more steeply "
                    "— and the floor never changed height. So what is "
                    "the height of the line telling you?",

    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",
         "label": "What the height means", "done_when": "committed"},
        {"anchor": "s-plot",  "short": "PLOT",
         "label": "Plot seven readings",   "done_when": "all_seven_plotted"},
        {"anchor": "s-match", "short": "MATCH",
         "label": "Walk the graph",        "done_when": "target_matched"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The line climbs. The corridor is flat.",
        "prompt": "Someone walks 6 m down a level corridor, waits at a door, "
                  "then runs the last 12 m. Drawn as a graph, that journey "
                  "rises, goes flat, then rises much more steeply. The floor "
                  "never changed height.",
        "commit": "So what is the height of the line telling you?",
        "options": [
            "How high above the ground the walker is",
            "How far the walker is from the start",
            "How fast the walker is going",
            "How long the walker has been walking",
        ],
        "answer": 1,
        "reveal": "The upright axis is <strong>distance from the "
                  "start</strong>. It only comes down if you come back. "
                  "Speed is not plotted anywhere on this graph — it is "
                  "hiding in the steepness, and that is the only place it "
                  "lives.",
    },

    "misconceptions": [
        {"id": "FORCE-06",
         "statement": "A distance–time graph is a picture of the route: the "
                      "line going up means going uphill.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
        {"id": "FORCE-07",
         "statement": "A flat line on a distance–time graph means moving at "
                      "a steady speed.",
         "elicited_by": "graph-plot",
         "confronted_by": "graph-plot"},
        {"id": "FORCE-08",
         "statement": "A curved line on a distance–time graph means the "
                      "object is going round a bend.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Each point is one reading: at this time, that far from the "
                 "start. Join the readings and the whole journey is in one "
                 "picture — <strong>including the parts where nothing "
                 "happened.</strong>"},

        # ── #s-plot · plot the sensor's readings ──────────────────────
        {"type": "graph-plot",
         "id": "graph-plot",
         "anchor": "s-plot",
         "eyebrow": "Plot the sensor's readings yourself",
         "heading": "Seven readings, two seconds apart",
         "prompt": "A motion sensor at the start of the corridor recorded "
                   "the distance every two seconds. Put each reading on the "
                   "grid, in order. The one you are looking for is named "
                   "under the graph.",
         "t_values": [0, 2, 4, 6, 8, 10, 12],
         "d_values": [0, 3, 6, 9, 12, 15, 18],
         "t_label": "Time (s)",
         "d_label": "Distance from the start (m)",
         "data": [
             {"t": 0,  "d": 0},
             {"t": 2,  "d": 3},
             {"t": 4,  "d": 6},
             {"t": 6,  "d": 6},
             {"t": 8,  "d": 6},
             {"t": 10, "d": 12},
             {"t": 12, "d": 18},
         ],
         "join_label": "Join the points",
         # ⚖️ R3 — the reads are COMMITMENTS, and the `why` is a statement
         # about the graph rather than a mark.
         "reads": [
             {"id": "q1",
              "question": "Between 4 s and 8 s, what was the walker doing?",
              "options": ["Walking slowly", "Standing still",
                          "Walking back to the start"],
              "answer": 1,
              "why": "The line is flat there. The distance from the start "
                     "stays at 6 m for four seconds, so the walker is not "
                     "moving at all — a flat line is stopped, not slow."},
             {"id": "q2",
              "question": "Which part of the journey was fastest?",
              "options": ["0 to 4 s", "4 to 8 s", "8 to 12 s"],
              "answer": 2,
              "why": "The last part is the steepest: 12 m in 4 s. The first "
                     "part covers 6 m in 4 s. Steeper line, bigger speed."},
             {"id": "q3",
              "question": "What was the speed over the last four seconds?",
              "options": ["1.5 m/s", "3 m/s", "4.5 m/s"],
              "answer": 1,
              "why": "From 6 m at 8 s to 18 m at 12 s is 12 m in 4 s. "
                     "12 ÷ 4 = 3 m/s — the same division as the "
                     "trolley on the light gates."},
         ],
         "alt": "A distance–time grid, time 0 to 12 seconds along the bottom "
                "and distance from the start 0 to 18 metres up the side, "
                "with seven sensor readings to plot.",
         "close": "Seven readings, one line, and a whole journey — "
                  "including four seconds in which nothing happened at all."},

        {"type": "key-fact", "ref": "gradient-is-the-speed"},

        # ── #s-match · walk the graph ─────────────────────────────────
        {"type": "journey-match",
         "id": "journey-match",
         "anchor": "s-match",
         "eyebrow": "Build the journey that draws this line",
         "heading": "Walk the graph",
         "prompt": "The dashed line is the target. Choose what happens in "
                   "each three-second block, then send the walker down the "
                   "corridor and watch the line draw itself.",
         "seg_seconds": 3,
         "modes": [
             {"id": "still", "label": "Stand still",    "speed_ms": 0},
             {"id": "walk",  "label": "Walk · 1 m/s",   "speed_ms": 1},
             {"id": "jog",   "label": "Jog · 3 m/s",    "speed_ms": 3},
             {"id": "back",  "label": "Walk back · 2 m/s", "speed_ms": -2},
         ],
         "target": ["walk", "still", "jog", "back"],
         "send_label": "Send the walker",
         "clear_label": "Clear the line",
         # ⚖️ THE CLAMP AT 0 m SAYS SO. The walker cannot go back past the
         # start, and a refusal that draws a flat line without a word is a
         # walking walker drawn as a stopped one.
         # ⊕ MRB-297 · 1 Sep 2026 — THE REFUSAL WAS ONLY TRUE OF A FULL
         # CLAMP, AND IT FIRES ON A PARTIAL ONE TOO. It said "a walk-back
         # block moved nothing". `points()` in `shared/ks3.js` sets
         # `refused` from `raw < 0` and then clamps `d` to `max(0, raw)`,
         # so Walk then Walk back gives raw = 3 − 6 = −3: refused, and the
         # walker is moved from 3 m to 0 m. The graph visibly falls three
         # metres while the readout — which REPLACES the distance on a
         # refused block — states that nothing moved. On the page whose key
         # fact is "A flat line is not slow. It is stopped", that is the
         # exact confusion the instrument exists to kill. The clamp is
         # right and stays; the sentence now describes it.
         "back_refused": "The walker cannot go back past the start, so a "
                         "walk-back block stops at 0 m rather than going "
                         "below it.",
         "alt": "A corridor with a walker, above a distance–time graph. A "
                "dashed target line is drawn from 0 to 12 seconds, and the "
                "walker's own line is drawn in as it moves.",
         # ⚖️ R3 — a FACTUAL end-point comparison with no verdict attached.
         "close": "Your line and the target are compared at the end point "
                  "only, as two numbers. Whether that counts as a match is "
                  "your call, not the page's."},

        # ── #s-think · NOT a rail stop ────────────────────────────────
        {"type": "misconception", "id": "think-uphill",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "activities": [
        {"id": "think-uphill",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-06",
         "statements": [
             {"quote": "The line goes up, so she is cycling uphill — "
                       "and where it comes back down she is freewheeling "
                       "down the other side.",
              "targets": "FORCE-06",
              "body": [
                  "A cyclist rides 400 m to the postbox, posts a letter, and "
                  "rides home. Her graph rises, goes flat, then falls back "
                  "to zero — and the road is flat the whole way. The "
                  "falling section is the ride <em>home</em>. Her distance "
                  "from the start is getting smaller, which is the only "
                  "thing that axis can mean. When the line reaches zero she "
                  "is back where she began.",
                  "<strong>There is no room for a hill on this graph.</strong> "
                  "It holds two quantities and no others: how long, and how "
                  "far from the start. The road could be flat, uphill, or a "
                  "spiral staircase, and the graph would be identical.",
              ]},
             {"quote": "A curved line means the object is going round a "
                       "bend.",
              "targets": "FORCE-08",
              "body": [
                  "A distance–time graph knows nothing about direction in "
                  "space — the only thing the axes carry is how far "
                  "along the journey and how long it has taken. A curve "
                  "means the gradient is changing, and the gradient is the "
                  "speed, so <strong>a curve means speeding up or slowing "
                  "down</strong>. An object going round a perfect bend at a "
                  "steady speed draws a straight line here.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "gradient-is-the-speed",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "On a distance–time graph, the steepness of the line is the "
                 "speed. A flat line is not slow. It is stopped."},
    ],

    "ladder": {
        "recall": {
            # ⚠️ MRB-278 — the answer is not always index 0 across P3's six
            # sets. Feedback keys are option indices and move with them.
            "q": "A distance–time graph is horizontal between 20 s and 35 s. "
                 "What was happening in those fifteen seconds?",
            "options": ["It was slowing down", "It was going back to the "
                        "start", "The object was stopped",
                        "It was moving at a steady speed"],
            "answer": 2,
            "feedback": {
                0: "Slowing down makes the line get gradually less steep. "
                   "Flat is not slowing — it has already stopped.",
                1: "Going back makes the line fall towards zero. Horizontal "
                   "means it stayed where it was.",
                3: "A steady speed gives a straight line that still climbs. "
                   "Flat means the distance from the start is not changing "
                   "at all.",
            }},
        "apply": {
            "q": "Two journeys are drawn on the same axes. Line A is steeper "
                 "than line B. Which statement must be true?",
            "options": ["A travelled further than B",
                        "A took longer than B",
                        "A was going uphill and B was on the flat",
                        "A is travelling faster than B"],
            "answer": 3,
            "feedback": {
                0: "Not necessarily. A steep line drawn for two seconds can "
                   "cover less ground than a gentle line drawn for a "
                   "minute.",
                1: "Time is read along the bottom, not from the steepness. A "
                   "steeper line usually takes less time, not more.",
                2: "Nothing on this graph is a hill. Steepness on a "
                   "distance–time graph is speed.",
            }},
        "explain": {
            "q": "A graph rises steeply, then flattens, then rises gently. "
                 "Describe that journey in words and say how you know each "
                 "part, without using the words up or down.",
            "field_label": "Your description",
            "placeholder": "At the start the line is steep, which means…",
            "success": [
                "Says the steep part is the fastest section, and that "
                "steepness means speed.",
                "Says the flat part is stopped, and gives the reason: the "
                "distance from the start is not changing.",
                "Says the gentle part is slower than the first part, not "
                "stopped.",
                "Talks about distance from the start rather than height or "
                "hills.",
                "Reads at least one time or distance off the axes to pin a "
                "section down.",
            ]},
        "produce": {
            "q": "A lift rises 30 m in 20 s, waits 10 s, then returns to the "
                 "ground floor in 15 s. Describe the graph of its distance "
                 "from the ground floor against time, giving the speed of "
                 "each moving part with units. Then say how the graph would "
                 "differ if you plotted total distance travelled instead.",
            "field_label": "Your answer",
            "placeholder": "From 0 to 20 s the line…",
            "success": [
                "First section climbs from 0 to 30 m over 20 s, and gives "
                "30 ÷ 20 = 1.5 m/s.",
                "Middle section is flat for 10 s, at 30 m, because the lift "
                "is stopped.",
                "Last section falls from 30 m back to 0 over 15 s, and gives "
                "30 ÷ 15 = 2 m/s.",
                "Says the last part is faster than the first, and uses the "
                "steeper line as the reason.",
                "Says a total-distance-travelled graph never falls: it would "
                "flatten and then climb to 60 m.",
            ]},
    },

    "key_note": "A distance–time graph plots distance from the start against "
                "time. Steeper means faster, flat means stopped, and a line "
                "coming back down means returning towards the start. It "
                "records a journey; it never draws the route.",

    "stretch": [
        {"id": "the-graph-that-never-falls",
         "type": "explainer",
         "text": "Change the upright axis from <em>distance from the "
                 "start</em> to <em>total distance travelled</em> and the "
                 "same journey gives a different line — one that can "
                 "never come down, because a distance you have already "
                 "travelled cannot be un-travelled. The cyclist's ride home "
                 "now climbs to 800 m instead of falling to zero. "
                 "<strong>Two graphs, one journey, and only one of them can "
                 "tell you that she got home.</strong>"},
    ],

    "support": [],

    "vocabulary": [
        {"term": "distance from the start",
         "definition": "What the upright axis carries. It gets smaller when "
                       "you come back, which is why the line can fall."},
        {"term": "gradient",
         "definition": "How steep the line is. On a distance–time graph the "
                       "gradient IS the speed, and it is the only place the "
                       "speed appears."},
        {"term": "horizontal line",
         "definition": "Stopped. The distance from the start is not "
                       "changing, so nothing is moving — it is not a "
                       "slow speed."},
    ],

    "tutor": {
        "anchor": "s-plot",
        "prompt": "Ask Mr Badmus AI",
        "body": "Not sure why a flat line means stopped?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Gradients of curved graphs, motion graphs where a value "
                   "can be negative, and the area underneath them.",

    "ws": ["analysis-and-evaluation", "measurement"],
}
