"""P3 L1 — Speed (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p3/p3-01-speed.dc.html`.

Her page wins outright. The fly and the plane, the three ramps, the three
compare pairs, both worked examples and all four rungs are hers.

── ⚖️ THIS LESSON DEFINES THE QUANTITATIVE FAMILY ─────────────────────

Design's `NOTES-P3.md` §1: this is the first QUANTITATIVE lesson in the
course, so what it does IS the family. The load-bearing step is her (2):

> **The instrument produces raw measurements and refuses to do the
> arithmetic.** The light gates give a distance and a time and a readout
> that says *speed — not measured — you work it out*. An instrument
> that hands over the answer has removed the lesson.

`r_light_gates` asserts that third tile exists, for exactly that reason.
P2's four QUANTITATIVE lessons already inherit the pattern.

── ⚖️ MRB-204 · TRIANGLE, AND CHECKED ────────────────────────────────

`s = d ÷ t` rearranges to `d = s × t` — a genuine product,
so `A = B × C` holds and the triangle encodes a relationship that
exists. Distance sits above the bar; speed and time sit below it. Checked
against the arithmetic, not against the habit. Nothing in this lesson is a
sum, so no beam appears — and `p3-03`, whose arithmetic IS a sum, gets
no triangle for the same reason read the other way.

── ⚖️ RULED · km/h → m/s STAYS, AND ÷ 3.6 IS TAUGHT ─────────────────

Design's flag 3 asks for a ruling. It stays. Compare pair 3 is a
DELIBERATE dead heat — 72 km/h against 20 m/s — and the pair only
works if the conversion is done: without it a student picks one at random
and learns nothing. `KS3.P.MOT.01` names only speed = distance ÷ time, so
the conversion is carried as `touches` rather than `covers`, and it is
taught as a comparison skill rather than as a spec point.

── ⚖️ RULED · THE MEAN IS TAKEN OF THE TIMES, NOT OF THE SPEEDS ──────

Design's flag 2 asks which method to teach, and it is hers: add the three
times, divide by three, then divide the distance once by the mean time.
Rung 3's criteria say exactly that. It is the method that generalises to
the light-gate practical, and it avoids the trap the lesson's own
misconception is about — meaning a student is never asked to average
speeds in the one lesson that teaches why you must not.

── ⚖️ RULED · "THE SPEED BETWEEN THE GATES", AND NO FRICTION LINE ────

Design's flag 1 asks whether to add an explicit "we are ignoring friction
here". No — and not for brevity. Her page never claims the speed is
instantaneous; it says *the speed between the gates*, which is exactly
what the measurement is and is true whether or not the trolley slows. A
friction caveat would introduce an idea the lesson does not use and would
undercut the stretch layer, which is where the instantaneous/average
distinction is properly raised.

── ⚠️ FOUR RAIL STOPS · `s-compare` AND `s-think` ARE NOT AMONG THEM ─

    s-hook · s-track · s-build · s-ladder

Her notes (15 Aug) say SIX stops for this lesson. Her own audit (23 Aug)
records the cut — *"p3-01 drops COMPARE and THINK"* — and the
delivered `RAIL` constant carries four. THE DRAWING WAS MEASURED. Both
sections keep their `id`; the tutor link points at `#s-build`.

── ⚠️ SHELLS ARE MEASURED OFF DESIGN'S CLASS ATTRIBUTE ──────────────

    #s-track   `ks3-block ks3-dark ks3-practical` → `practical`
    #s-compare `ks3-block`                        → `check`
    #s-think   `ks3-block ks3-misconception`      → `misconception`

── ⚠️ MRB-208 · THE RAIL STOP GOES ON THE BLOCK THAT CAN TICK ───────

Design draws the statement, the triangle and the CFIFA inside one
`#s-build`. A `formula` block carries no demand and emits no
`data-stage-done`, so anchoring the stop to it makes a stop that can never
become true. The id goes on the worked example — which is what the
stop's own label, "Your own five steps", names.

── ⚖️ THE `FORCE` FAMILY OPENS HERE ─────────────────────────────────

See `ks3_data/p3/__init__.py` for the ruling. `FORCE-01`..`FORCE-05` are
minted by this lesson, and all five are Design's proposed rows checked
against the delivered page rather than trusted:

    FORCE-01  first to arrive is faster       `#s-compare`, pair 1
    FORCE-02  how fast it LOOKS               `#s-hook`, and pair 2
    FORCE-03  average of the speeds           `#s-think` quote 1
    FORCE-04  divide in the order given       ladder rung 1's distractor
    FORCE-05  a speed camera gives the        `#s-think` quote 2
              journey's speed

`FORCE-05` is NOT in her proposed table — it arrived with the second
misconception quote her 23 Aug audit added to all sixteen P1–P3 lessons.
It is a genuinely separate belief: instantaneous against average, which a
student can hold while being perfectly sound on how to average.
"""

LESSON = {
    "slug":  "speed",
    "title": "Speed",
    "discipline": "physics",
    "unit": "Describing motion",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.MOT.01"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "motion", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": [],
    "assumes": [],
    "references": [],
    "ks4_links": [],

    "meta_description": "A fly crossing your view looks fast. A plane "
                        "crossing the sky looks slow. One of them covers 250 "
                        "metres every second. Measure a trolley through two "
                        "light gates and work the number out yourself.",

    "big_question": "A fly crosses your view in half a second. A plane takes "
                    "a full minute to cross the same patch of sky. Which one "
                    "is actually faster — and what would you have to "
                    "know to say?",

    "rail": [
        {"anchor": "s-hook",  "short": "HOOK",
         "label": "Fly or plane",          "done_when": "committed"},
        {"anchor": "s-track", "short": "GATES",
         "label": "Two light gates",       "done_when": "three_runs_recorded"},
        {"anchor": "s-build", "short": "CFIFA",
         "label": "Your own five steps",   "done_when":
         "both_attempts_opened"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The slow-looking one covers 250 metres every second.",
        "prompt": "The fly is 30 cm from your eye and takes half a second to "
                  "cross your view. The plane is 10 km up and takes a minute "
                  "to cross the same patch of sky. One of them would cross a "
                  "football pitch in less than half a second, and it is not "
                  "the fly.",
        "commit": "So what would you have to know to say which is faster?",
        "options": [
            "Which of them crossed your view the fastest",
            "How far each one travelled, and how long it took",
            "Which of the two of them is the bigger object",
            "How far away each of them is from your eye",
        ],
        "answer": 1,
        "reveal": "How fast something <em>looks</em> depends on how far away "
                  "it is. Speed does not. It is one number built from two "
                  "measurements — how far, and how long — and "
                  "<strong>until you have both you have nothing to "
                  "compare.</strong>",
    },

    "misconceptions": [
        {"id": "FORCE-02",
         "statement": "How fast something looks is how fast it is going.",
         "elicited_by": "s-hook",
         "confronted_by": "compare-pairs"},
        {"id": "FORCE-01",
         "statement": "Whichever one gets there first is going faster.",
         "elicited_by": "compare-pairs",
         "confronted_by": "compare-pairs"},
        {"id": "FORCE-03",
         "statement": "The average speed for a journey is the average of the "
                      "speeds you travelled at.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
        {"id": "FORCE-04",
         "statement": "Speed is worked out by dividing the two numbers in "
                      "the order you were given them.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
        {"id": "FORCE-05",
         "statement": "A speed camera tells you how fast you were going on "
                      "the journey.",
         "elicited_by": "s-think",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A sprinter covers 100 m in 12 s. A marathon runner covers "
                 "42 000 m in 7200 s. The sprinter travels far less ground "
                 "and is far faster. <strong>Distance alone settles nothing "
                 "and time alone settles nothing</strong>; the two have to be "
                 "put together."},

        # ── #s-track · the light gates ─────────────────────────────────
        {"type": "light-gates",
         "id": "light-gates",
         "anchor": "s-track",
         "eyebrow": "The light gates · the timer gives you a time, nothing "
                    "else",
         "heading": "You own both measurements.",
         "prompt": "The trolley rolls off the ramp and breaks two beams. The "
                   "clock starts at the first gate and stops at the second. "
                   "You choose how far apart the gates are.",
         "gate": {
             "prompt": "Commit first. You raise the ramp so the trolley rolls "
                       "faster. What does the gate timer read?",
             "options": [
                 "A bigger number, because it is going faster",
                 "A smaller number, because it crosses the gap sooner",
                 "The same, because the gap has not changed",
                 "It depends how heavy the trolley is",
             ],
             "answer": 1,
         },
         "ramps": [
             {"id": "low",  "label": "Low",    "speed_ms": 0.55},
             {"id": "med",  "label": "Medium", "speed_ms": 0.95},
             {"id": "high", "label": "High",   "speed_ms": 1.45},
         ],
         "start_ramp": 1,
         "gap_min": 0.40,
         "gap_max": 2.00,
         "gap_step": 0.20,
         "gap_start": 1.20,
         "scatter_pct": 3,
         "runs_to_record": 3,
         "columns": ["Run", "Ramp", "Distance", "Time"],
         # ⚖️ THE THIRD READOUT IS THE WHOLE FAMILY PATTERN. An instrument
         # that hands over the answer has removed the lesson, so this one
         # says so on its face. `r_light_gates` refuses a payload without it.
         "readouts": [
             {"id": "gap",   "label": "Gate separation"},
             {"id": "time",  "label": "Gate timer"},
             {"id": "speed", "label": "Speed",
              "value": "not measured — you work it out"},
         ],
         "release_label": "Release the trolley",
         "record_label": "Record this run",
         "alt": "A trolley released from a ramp rolls along a runway and "
                "breaks two light beams 1.20 metres apart. The timer runs "
                "only while the trolley is between the beams.",
         # ⚖️ TWO CLOSING SENTENCES, AND THE ROWS CHOOSE. `close` names a
         # method — average the three times, divide the distance by it —
         # and that method only works if the three runs are repeats of ONE
         # measurement. The bench lets the distance and the ramp change
         # between runs, so it also has to say when they have.
         "close": "Three runs, three different times, and the same distance "
                  "every time. That scatter is why one reading is never "
                  "enough — and the mean of the three times is what you "
                  "divide into.",
         "close_mixed": "You changed the setup between runs, so these times "
                        "are not repeats of one measurement — there is no "
                        "single distance to divide by the mean. Set the "
                        "gates and the ramp once, then take three runs."},

        {"type": "key-fact", "ref": "two-measurements-one-number"},

        # ── #s-build · the formula, then CFIFA ─────────────────────────
        # ⚠️ NO ANCHOR ON THE FORMULA — MRB-208. See the note above.
        {"type": "formula",
         "id": "speed-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Speed = distance ÷ time",
         "support": [
             "m with s gives m/s",
             "km with h gives km/h",
             "and the two cannot be mixed",
         ],
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. Distance d sits above a "
                           "dividing line; speed s and time t sit below it, "
                           "multiplied together. Covering one letter leaves "
                           "the way to work it out.",
             "top":   {"label": "d", "button": "Cover d",
                       "text": "Distance is on its own at the top, with the "
                               "other two side by side underneath. Cover it "
                               "and you are left with s × t — "
                               "multiply."},
             "left":  {"label": "s", "button": "Cover s",
                       "text": "Speed sits underneath, with distance above "
                               "it. Cover it and you are left with d over t "
                               "— divide."},
             "right": {"label": "t", "button": "Cover t",
                       "text": "Time sits underneath, with distance above "
                               "it. Cover it and you are left with d over s "
                               "— divide."},
             "close": "Two things side by side means multiply. One thing "
                      "over another means divide.",
         }},

        {"type": "worked-example", "id": "cfifa-speed-plain",
         "anchor": "s-build"},
        {"type": "worked-example", "id": "cfifa-speed-convert"},
        # ⊕ MRB-223 — HER CARD GRID, at the end of #s-build where she drew it
        # (under the attempt; see the vocabulary note). Eyebrow and lead are
        # hers verbatim. NOT a rail stop — her RAIL has four stops and this is
        # inside the third. The engine's block is its own section rather than
        # a div inside the CFIFA one, which is the one structural difference
        # and is registered in DEPARTURES-P3.md.
        {"type": "keyword",
         "eyebrow": "Three words you have just used",
         "lead": "Say what each one means out loud. Then turn the card and "
                 "check yourself.",
         "terms": ["Speed", "Average speed", "Metre per second"]},

        # ── #s-compare · NOT a rail stop ───────────────────────────────
        {"type": "compare-pairs",
         "id": "compare-pairs",
         "anchor": "s-compare",
         "eyebrow": "Three pairs · one of them is a dead heat",
         "heading": "Work each one out before you choose.",
         "prompt": "Two things, both plausible, where the eye gives the "
                   "wrong answer. Do the division first.",
         "pairs": [
             {"id": "p1", "label": "Pair 1",
              "a": "Sprinter — 100 m in 10.5 s",
              "b": "Cyclist — 400 m in 32 s",
              "answer": "b",
              "sums": "100 ÷ 10.5 = 9.52 m/s · 400 ÷ 32 = "
                      "12.50 m/s",
              "why": "The sprinter finishes first and is slower. Finishing "
                     "first only means the distance was shorter."},
             {"id": "p2", "label": "Pair 2 · the one from the top of the "
                                   "page",
              "a": "Fly — 1.5 m in 0.8 s, 30 cm from your eye",
              "b": "Plane — 15 000 m in 60 s, 10 km up",
              "answer": "b",
              "sums": "1.5 ÷ 0.8 = 1.88 m/s · 15 000 ÷ 60 = "
                      "250 m/s",
              "why": "The plane is over a hundred times faster than the "
                     "thing that looked fast. Distance from you changes how "
                     "it looks, not how fast it goes."},
             {"id": "p3", "label": "Pair 3 · different units",
              "a": "Car — 72 km/h",
              "b": "Racing cyclist — 20 m/s",
              "answer": "same",
              "sums": "72 km/h ÷ 3.6 = 20 m/s",
              "why": "A dead heat. Two speeds cannot be compared until they "
                     "are in the same unit — 3.6 converts km/h to m/s, "
                     "because there are 1000 m in a km and 3600 s in an "
                     "hour."},
         ],
         "same_label": "A dead heat",
         "close": "One of the three was a dead heat and the eye could not "
                  "have told you which."},

        # ── #s-think · NOT a rail stop ─────────────────────────────────
        {"type": "misconception", "id": "think-average-speed",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary"},
    ],

    "activities": [
        {"id": "think-average-speed",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-03",
         "statements": [
             {"quote": "I walked 100 m at 1 m/s, then ran 100 m at 5 m/s. So "
                       "my average speed was 3 m/s.",
              "targets": "FORCE-03",
              "body": [
                  "Halfway between 1 and 5 is 3, and the two distances are "
                  "equal, so it looks safe. It is not. Walking 100 m at "
                  "1 m/s takes 100 s; running 100 m at 5 m/s takes 20 s. The "
                  "whole journey is 200 m in 120 s, which is "
                  "<strong>1.67 m/s</strong>.",
                  "You spent five times as long walking as running, so the "
                  "walk counts five times as much. That is why the answer "
                  "sits close to walking pace and nowhere near 3 m/s. "
                  "<strong>Average speed is always the total distance "
                  "divided by the total time — never the average of the "
                  "speeds.</strong>",
              ]},
             {"quote": "A speed camera tells you how fast you were going on "
                       "the journey.",
              "targets": "FORCE-05",
              "body": [
                  "It tells you how fast you were going over a few metres of "
                  "it. That is an instantaneous speed — measured over a "
                  "stretch so short that the speed has no time to change "
                  "— and it can be far above or far below the average "
                  "for the trip. Average-speed checks on motorways exist "
                  "because the two numbers are different: they time you "
                  "between two gantries and work out distance ÷ time, "
                  "which no single camera can do.",
              ]},
         ]},

        {"id": "cfifa-speed-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Five lines, every time · CFIFA",
         "heading": "A trolley crosses gates 1.20 m apart in 0.84 s.",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1.20 m stays 1.20 m · 0.84 s stays 0.84 s",
              "note": "The gap is already in metres and the time is already "
                      "in seconds, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "s = d ÷ t",
              "note": "Cover s on the triangle: d sits over t, so you "
                      "divide."},
             {"letter": "I", "label": "Insert",
              "line": "s = 1.20 m ÷ 0.84 s",
              "note": "Distance on top, because distance is on top of the "
                      "triangle."},
             {"letter": "F", "label": "Fine-tune",
              "line": "1.20 ÷ 0.84 = 1.4285…",
              "note": "Metres divided by seconds leaves metres per second."},
             {"letter": "A", "label": "Answer",
              "line": "s = 1.43 m/s",
              "note": "Two decimal places, and the unit."},
         ]},

        {"id": "cfifa-speed-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Five lines, every time · CFIFA",
         "heading": "A car covers 1.8 km of motorway in 90 s.",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn on your own runs above."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1.8 km × 1000 = 1800 m",
              "note": "The formula wants metres, and a kilometre is a "
                      "thousand of them, so multiply by 1000."},
             {"letter": "F", "label": "Formula",
              "line": "s = d ÷ t",
              "note": "Cover s on the triangle: d sits over t, so you "
                      "divide."},
             {"letter": "I", "label": "Insert",
              "line": "s = 1800 m ÷ 90 s",
              "note": "The converted distance goes in. The kilometre reading "
                      "never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "1800 ÷ 90 = 20",
              "note": "Metres divided by seconds leaves metres per second."},
             {"letter": "A", "label": "Answer",
              "line": "s = 20 m/s",
              "note": "Insert 1.8 instead of 1800 and the answer comes out a "
                      "thousand times too small."},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "two-measurements-one-number",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A speed is two measurements made into one number: distance "
                 "÷ time. On its own, neither measurement can tell you "
                 "which is faster."},
    ],

    "ladder": {
        "recall": {
            "q": "A trolley crosses two light gates 1.5 m apart in 0.60 s. "
                 "What is its speed?",
            "options": ["2.5 m/s", "0.4 m/s", "0.9 m/s", "2.5 m"],
            "answer": 0,
            "feedback": {
                1: "That is 0.60 ÷ 1.5 — time divided by distance. "
                   "Distance goes on top, as it does on the triangle.",
                2: "That is 1.5 × 0.60. Multiplying gives you a "
                   "distance, not a speed.",
                3: "The number is right and the unit is not. Metres divided "
                   "by seconds gives metres per second.",
            }},
        "apply": {
            # ⚠️ MRB-278 — across P3's six ladder sets the answer sits at
            # 0, 1, 2 and 3, so no button beats reading. Feedback keys are
            # option indices and move with their own option.
            "q": "A runner covers the first 200 m in 40 s, then the next "
                 "200 m in 60 s. What is their average speed for the whole "
                 "400 m?",
            "options": ["4.17 m/s", "4 m/s", "5 m/s", "3.33 m/s"],
            "answer": 1,
            "feedback": {
                0: "That is the average of 5 m/s and 3.33 m/s. Averaging the "
                   "speeds ignores that more time was spent on the slower "
                   "part.",
                2: "That is the first 200 m only. The question asks for the "
                   "whole journey.",
                3: "That is the second 200 m only. The whole journey is "
                   "400 m in 100 s.",
            }},
        "explain": {
            "q": "A student times a trolley over the same 1.20 m three times "
                 "and gets 0.81 s, 0.84 s and 0.90 s. Say what they should "
                 "do with the three numbers before working out a speed, and "
                 "why one run on its own is not good enough.",
            "field_label": "Your explanation",
            "placeholder": "The three times are different because…",
            "success": [
                "Says the three readings are not identical, and that this is "
                "normal rather than a mistake.",
                "Names a reason the times vary — the release, the "
                "trolley running slightly crooked, or where it was let go.",
                "Says to add the three times and divide by three to get a "
                "mean time.",
                "Uses the mean time in speed = distance ÷ time, with "
                "the distance staying 1.20 m.",
                "Says that using one run means the answer depends on which "
                "run you happened to pick.",
            ]},
        "produce": {
            "q": "You have a tape measure and a phone stopwatch, and you want "
                 "the speed of someone walking down a corridor. Describe how "
                 "you would measure it, and say what the biggest source of "
                 "error is and how you would cut it down.",
            "field_label": "Your method",
            "placeholder": "I would measure…",
            "success": [
                "Measures a distance along the corridor and marks a clear "
                "start and finish.",
                "Times how long the walk takes between those two marks.",
                "Divides distance by time and gives the unit as m/s.",
                "Names starting and stopping the stopwatch by eye — "
                "reaction time — as the biggest error.",
                "Reduces it in a named way: a longer distance, repeating and "
                "taking a mean, or someone standing at each mark.",
            ]},
    },

    "key_note": "Speed = distance ÷ time, in metres per second. It "
                "turns two measurements into one number, so any two journeys "
                "can be compared. Finishing first is not the same as "
                "travelling fastest, and average speed is total distance "
                "÷ total time.",

    "stretch": [
        {"id": "over-what-stretch",
         "type": "explainer",
         "text": "A roadside speed camera measures you over about half a "
                 "metre of road. An average-speed camera measures you over "
                 "two kilometres. Both are doing distance ÷ time, and "
                 "they can disagree completely: you can pass every camera at "
                 "exactly the limit and still have averaged more than the "
                 "limit in between, or crawl through a jam and pass one "
                 "camera far too fast. <strong>Neither reading is a lie. A "
                 "speed is only ever the speed over the stretch you divided "
                 "by, and how long that stretch is changes the "
                 "answer.</strong>"},
    ],

    "support": [],

    "vocabulary": [
        # ⊕ MRB-223, 25 Aug 2026 — DESIGN'S THREE CARDS, AS SHE WROTE THEM.
        # Her p3-01 is the ONLY physics page in the key stage that draws a
        # vocabulary card grid ("Three words you have just used", inside
        # #s-build under the CFIFA attempt), and the live page never placed
        # it. Her `CARDS` constant carries `term` / `def` / `note` for these
        # three; they were merged into one definition each here, and the
        # grid was never authored. Now: her term (capitalised, as on her
        # card), her `def` as the definition and her `note` as the note,
        # byte for byte, and the `keyword` block below places them. `mean`
        # is not one of her cards and stays as it was — it still feeds the
        # unit's word box and the flashcards.
        {"term": "Speed",
         "definition": "How far something travels in a certain time — "
                       "distance divided by time.",
         "note": "Not \"how fast it looks\". A plane looks slow because it "
                 "is far away."},
        {"term": "Average speed",
         "definition": "Total distance divided by total time for a whole "
                       "journey.",
         "note": "It is not the average of the speeds. Time spent slowly "
                 "counts for more."},
        {"term": "Metre per second",
         "definition": "The unit of speed: the number of metres travelled in "
                       "each second.",
         "note": "Written m/s. The slash means \"divided by\", which is where "
                 "it comes from."},
        {"term": "mean",
         "definition": "Add the readings and divide by how many there were. "
                       "Here it is taken of the TIMES, then the distance is "
                       "divided once."},
    ],

    "tutor": {
        "anchor": "s-build",
        "prompt": "Ask Mr Badmus AI",
        "body": "Stuck on which number to divide by which?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Acceleration, motion graphs that carry direction as "
                   "well as size, and the equations of motion — all built "
                   "on distance ÷ time.",

    "ws": ["measurement", "analysis-and-evaluation"],
}
