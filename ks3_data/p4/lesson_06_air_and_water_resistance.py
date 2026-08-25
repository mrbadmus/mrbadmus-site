"""P4 L6 — Air and water resistance (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p4/p4-06-air-and-water-resistance.dc.html`.

Her page wins outright. The skydiver, the fall bench, the four-stage strip
and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA BLOCK, AND NONE IS OWED ───────────────────

The quantitative content here is the BALANCE of weight against resistance,
which the bench already draws as two arrows and a leftover. Design carries
a fixed four-stage figure instead of a formula, and that figure is the
counterpart of the live bench rather than a second instrument. There is no
relationship to put in a triangle and the drag equation is not KS3.

── ⚖️ RULED · RESISTANCE GROWS WITH THE SQUARE OF THE SPEED ──────────

`drag = weight × f²`, where `f` is the speed as a share of that object's
own steady speed. That is why it reaches the weight at `f = 1` for EVERY
object without the drawing knowing anything about the object, and it is
why the arrow grows so slowly at first and then so fast. The *Going
further* layer states the rule in words and the bench obeys it, so the
page and the drawing cannot disagree.

── ⚖️ RULED · 125 PER CENT IS A REAL STATE AND IT HAS ITS OWN BRANCH ─

It is the second after a canopy opens: resistance above weight, resultant
UPWARDS, and the skydiver still going down the whole time. Design gives it
a branch of its own because it is the one place a student will read an
upward resultant as upward motion — which is `FORCE-34` exactly. The
parachute case gets a second branch again, because there the state is not
a transient overshoot but a designed one.

── ⚖️ RULED · THE HAILSTONE'S READINGS TAKE TWO DECIMAL PLACES ───────

The bench spans 1 N to 750 N. One rounding rule across that range prints
`0.0 N` for the hailstone at half speed — a bench saying the resistance
is nothing when it is a quarter of the weight. Design switches precision
on the object, and so does the port.

── ⚖️ RULED · "ABOUT" ON EVERY TERMINAL SPEED AND EVERY WEIGHT ───────

The skydiver figure depends on mass, altitude and posture. These are
typical values, the foot line says so, and the hedge is what keeps them
honest.

── ⚠️ FOUR RAIL STOPS, AND `s-stages` TICKS ON THE GATE ──────────────

    s-hook · s-bench · s-stages · s-ladder

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    FORCE-32  heavier things always fall faster
    FORCE-33  air resistance is a fixed force, the same at any speed
    FORCE-34  when the parachute opens you get pushed back up
    FORCE-35  terminal velocity is a speed limit rather than a balance

`FORCE-34` has no `elicited_by`: nothing on the page asks the student to
commit to it, and it is confronted because it sits underneath the state
the bench lets them reach. `FORCE-35` is not in Design's table — it
arrived with her own sentence *"this is terminal velocity, and it is a
balance, not a limit"*, which is a correction with no elicitation and
therefore a belief the page is answering.
"""

LESSON = {
    "slug":  "air-and-water-resistance",
    "title": "Air and water resistance",
    "discipline": "physics",
    "unit": "Forces",
    "family": "SYSTEM",

    "covers": ["KS3.P.FORCES.04c"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["friction"],
    "assumes": [],
    "references": ["balanced-and-unbalanced", "what-a-force-is",
                   "pressure-force-over-area"],
    "ks4_links": [],

    "meta_description": "A skydiver falls for a minute and stops getting any "
                        "faster. Nothing has caught them and their weight "
                        "has not changed by a newton. Watch the two arrows "
                        "close the gap.",

    "big_question": "A skydiver falls for a minute and stops getting any "
                    "faster. Nothing has caught them, and their weight has "
                    "not changed by a single newton.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The skydiver",   "done_when": "committed"},
        {"anchor": "s-bench",  "short": "FALL",
         "label": "The fall",       "done_when": "gate_and_a_control"},
        {"anchor": "s-stages", "short": "STAGES",
         "label": "Four stages",    "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Falling for a minute, and no longer speeding up.",
        "prompt": "Ten seconds after stepping out of the aircraft a skydiver "
                  "is falling at about 55 metres per second. Twenty seconds "
                  "later, still falling, still nothing underneath them: 55 "
                  "metres per second. It does not go up any further.",
        "commit": "Why does the falling stop getting faster?",
        "options": [
            "Gravity gets weaker as you fall",
            "There is a fastest speed anything can fall at, and every "
            "falling object reaches the same one",
            "Air resistance grows with speed until it matches the weight, "
            "leaving 0 N over",
            "The air is holding the skydiver up completely",
        ],
        "answer": 2,
        "reveal": "Air resistance is not a fixed force. The faster you go, "
                  "the more air you have to shove out of the way every "
                  "second, so the harder it pushes back — and it keeps "
                  "growing until it matches the weight exactly. At that "
                  "point the resultant is 0 N, and with nothing left over "
                  "nothing changes. <strong>The weight was the same 750 N "
                  "the whole way down.</strong>",
    },

    "misconceptions": [
        {"id": "FORCE-32",
         "statement": "Heavier things always fall faster.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "FORCE-33",
         "statement": "Air resistance is a fixed force, the same at any "
                      "speed.",
         "elicited_by": "fall",
         "confronted_by": "fall"},
        {"id": "FORCE-34",
         "statement": "When the parachute opens you are pushed back "
                      "upwards.",
         "confronted_by": "s-think"},
        {"id": "FORCE-35",
         "statement": "Terminal velocity is a speed limit that falling "
                      "cannot pass.",
         "elicited_by": "s-hook",
         "confronted_by": "fall"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Air resistance</strong> and <strong>water "
                 "resistance</strong> are the same idea: moving through a "
                 "fluid means pushing it out of the way, and it pushes back. "
                 "Both act against the motion, both grow as you go faster, "
                 "and both grow when you present a bigger area to the flow. "
                 "Together with friction they are called "
                 "<strong>drag</strong>."},

        # ── #s-bench · the fall ────────────────────────────────────────
        {"type": "fall-balance",
         "id": "fall",
         "anchor": "s-bench",
         "eyebrow": "At the bench · the fall",
         "heading": "Watch the two arrows close the gap",
         "progress": "Change a control to begin",
         "lead": "Pick something falling, then set how fast it is going as a "
                 "share of its own steady speed. The weight arrow never "
                 "changes. The resistance arrow does.",
         "weight_px": 130,
         "start_body": "spread",
         "body_label": "What is falling",
         "zero_label": "0 N",
         "band_anchor": "s-stages",
         "band_at": 1,
         "gate": {
             "prompt": "Commit first. A skydiver has just stepped out and is "
                       "barely moving. What is the air resistance at that "
                       "instant?",
             "options": [
                 "Close to 0 N — barely any air is being pushed aside yet",
                 "750 N — the same as their weight, straight away",
                 "Bigger than their weight, which is why the fall is gentle "
                 "at first",
                 "Half their weight — it always starts at half",
             ],
             "answer": 0,
         },
         "frac": {"label": "How fast it is going", "min": 0, "max": 125,
                  "step": 25, "start": 50},
         "bodies": [
             {"id": "spread", "tab": "Skydiver, spread out",
              "word": "SKYDIVER, ARMS AND LEGS OUT",
              "weight": 750, "term": 55, "w": 200, "r": 14},
             {"id": "head", "tab": "Skydiver, head-down",
              "word": "THE SAME SKYDIVER, HEAD-DOWN",
              "weight": 750, "term": 80, "w": 96, "r": 40},
             {"id": "chute", "tab": "Parachute open",
              "word": "THE SAME SKYDIVER, PARACHUTE OPEN",
              "weight": 750, "term": 6, "w": 120, "r": 14, "canopy": True},
             {"id": "hail", "tab": "A hailstone",
              "word": "A LARGE HAILSTONE, 0.1 KG",
              "weight": 1, "term": 30, "w": 74, "r": 37},
         ],
         # ⚖️ FIVE BRANCHES, KEYED TO HOW THE RESISTANCE COMPARES WITH THE
         # WEIGHT — not to the slider position. `matched` is terminal
         # velocity and `canopy` is the designed overshoot; both are the
         # point of the lesson and neither is a bigger version of `growing`.
         "branches": {
             "at_rest": "Not moving yet, so no air is being pushed aside and "
                        "the resistance is 0 N. The whole {weight} of weight "
                        "is left over, downwards — this is the moment the "
                        "fall speeds up fastest, and it is the same for a "
                        "hailstone as for a skydiver.",
             "growing": "At {pct} per cent of its steady speed the "
                        "resistance is only {drag} against a weight of "
                        "{weight}, so {over} is still left over downwards "
                        "and the fall is still speeding up. Notice how "
                        "little the resistance is at half speed: it grows "
                        "with the square of the speed, so most of it arrives "
                        "late.",
             "matched": "The resistance has grown to exactly {weight}, "
                        "matching the weight. The resultant is 0 N, so "
                        "nothing changes and the fall continues at a steady "
                        "{term} m/s. This is terminal velocity, and it is a "
                        "balance, not a limit.",
             "past": "Going faster than its own steady speed makes the "
                     "resistance {drag}, which is more than the {weight} of "
                     "weight. The {over} left over points upwards, so the "
                     "fall slows until the two match again. Nothing here can "
                     "hold this state.",
             "canopy": "This is the second after the canopy opens: the same "
                       "weight, but a huge area facing the flow, so the "
                       "resistance is {drag} against a weight of {weight}. "
                       "The {over} left over points upwards, which slows the "
                       "fall hard — the skydiver is still going down the "
                       "whole time.",
         },
         "readouts": [
             {"id": "weight", "label": "Weight, down"},
             {"id": "drag", "label": "Resistance, up"},
             {"id": "res", "label": "Resultant"},
             {"id": "verdict", "label": "What happens next"},
         ]},

        # ── #s-stages · one jump, four stages ──────────────────────────
        {"type": "force-band",
         "id": "four-stages",
         "anchor": "s-stages",
         "eyebrow": "One jump, four stages",
         "heading": "The weight arrow is the same in all four.",
         "strip": {
             "aria_label": "Four stages of a skydive drawn to one scale. In "
                           "stage one the downward weight arrow is full "
                           "length and there is no resistance arrow. In "
                           "stage two the upward resistance arrow is about "
                           "half the weight arrow. In stage three the two "
                           "arrows are exactly equal. In stage four, with "
                           "the parachute open, the upward resistance arrow "
                           "is longer than the weight arrow.",
             "weight_px": 98,
             "columns": [
                 {"title": "1 · STEP OUT", "resistance": 0,
                  "caption": "no resistance yet"},
                 {"title": "2 · SPEEDING UP", "resistance": 0.5,
                  "caption": "still some left over"},
                 {"title": "3 · STEADY SPEED", "resistance": 1.0,
                  "caption": "resultant 0 N"},
                 {"title": "4 · CHUTE OPEN", "resistance": 1.2,
                  "caption": "left over, upwards"},
             ],
         },
         "panels": [
             {"num": "1", "name": "Step out",
              "body": "Barely moving, so almost no air is being pushed aside "
                      "and the resistance is close to 0 N. The whole weight "
                      "is left over, and the fall speeds up fastest right "
                      "here."},
             {"num": "2", "name": "Speeding up",
              "body": "Faster means more air shoved aside every second, so "
                      "the resistance grows. Something is still left over "
                      "downwards, so the speed is still rising — but more "
                      "slowly each second."},
             {"num": "3", "name": "Terminal velocity",
              "body": "The resistance has grown until it matches the weight "
                      "exactly. Resultant 0 N, nothing changes, and the fall "
                      "continues at a steady speed of about 55 metres per "
                      "second."},
             {"num": "4", "name": "Parachute opens",
              "body": "A far bigger area facing the flow, so the resistance "
                      "jumps well above the weight. The resultant now points "
                      "upwards, which slows the fall — down to a new steady "
                      "speed of about 6 metres per second."},
         ],
         "close": "Water does the same job with far more force behind it, "
                  "because a cubic metre of water has around eight hundred "
                  "times the mass of a cubic metre of air. That is why a "
                  "swimmer at two metres per second feels more resistance "
                  "than a runner at four, and why boats are shaped the way "
                  "they are."},

        {"type": "key-fact", "ref": "resistance-grows-with-speed"},

        {"type": "misconception", "id": "think-heavier-falls-faster",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-heavier-falls-faster",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-32",
         "statements": [
             {"quote": "Heavier things always fall faster.",
              "targets": "FORCE-32",
              "body": [
                  "Drop a golf ball and a table-tennis ball together and the "
                  "golf ball wins, so the belief has good evidence behind "
                  "it. But look at what is actually different. The two balls "
                  "are almost the same size, so at any given speed the air "
                  "pushes back on them by about the same amount — and that "
                  "push is a small fraction of the golf ball's weight and a "
                  "large fraction of the table-tennis ball's. The light one "
                  "runs out of gap between weight and resistance almost "
                  "immediately and settles to a slow steady speed; the heavy "
                  "one is still speeding up when it lands. Take the air away "
                  "and the difference goes with it: on Apollo 15 an "
                  "astronaut dropped a hammer and a feather on the Moon, and "
                  "they hit the dust together. <strong>Weight is not what "
                  "decides how fast something falls — the balance between "
                  "weight and resistance is.</strong>",
              ]},
             {"quote": "When the parachute opens, you get pushed back up.",
              "targets": "FORCE-34",
              "body": [
                  "The resultant force does point upwards for a few seconds "
                  "— the bench above will show you that — and it is a "
                  "violent few seconds. But <strong>an upward resultant does "
                  "not mean upward motion.</strong> It means the downward "
                  "motion is changing, which here means slowing: from about "
                  "55 metres per second to about 6, in the space of a couple "
                  "of seconds. The skydiver is going downwards the whole "
                  "time. As soon as the speed has dropped far enough, the "
                  "resistance falls back to 750 N, the resultant returns to "
                  "0 N, and the rest of the descent is at a new steady "
                  "speed. Nobody goes up.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "resistance-grows-with-speed",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Air and water resistance act against the motion and grow "
                 "as the object goes faster. When the resistance has grown "
                 "to match the weight, the resultant is 0 N and the falling "
                 "speed stops changing — a steady speed called terminal "
                 "velocity."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "A hailstone with a weight of 1 N is falling at a steady "
                 "speed. What is the air resistance on it?",
            "options": [
                "0 N — it is falling, so nothing is resisting it.",
                "More than 1 N, or it would not have stopped speeding up.",
                "1 N, upwards.",
                "It cannot be worked out without knowing the speed.",
            ],
            "answer": 2,
            "feedback": {
                0: "With 0 N of resistance the whole 1 N would be left over "
                   "and the hailstone would still be speeding up. A steady "
                   "speed means the two match.",
                1: "More than 1 N upwards would leave a resultant upwards, "
                   "which would slow the hailstone down. Steady means equal.",
                3: "The speed would be needed to predict the resistance from "
                   "scratch. Here the steady fall tells you it has already "
                   "grown to match the weight.",
            },
            "title": "Rung 1 · Apply"},
        "apply": {
            "q": "A lead ball and a plastic ball are the same size. Both are "
                 "dropped from a tall tower. Which lands first, and why?",
            "options": [
                "They land together, because gravity pulls on every object "
                "in exactly the same way, so what a thing is made of never "
                "changes how fast it falls.",
                "The lead ball, because heavier things are pulled harder so "
                "they always fall faster.",
                "The plastic ball, because a lighter object gives the air "
                "less to push against, so the air slows it down less and it "
                "reaches the ground first.",
                "The lead ball, because at any speed the resistance on the "
                "two is about the same, and it is a much smaller share of "
                "the lead ball’s weight.",
            ],
            "answer": 3,
            "feedback": {
                0: "True with no air — the Moon test proves it. In air the "
                   "resistance matters, and it holds the light ball back far "
                   "more than the heavy one.",
                1: "The verdict is right and the rule is wrong. In a vacuum "
                   "the two land together despite the difference in weight; "
                   "it is the resistance, not the weight on its own, that "
                   "decides.",
                2: "There is the same amount of ball facing the air — they "
                   "are the same size. What differs is how much weight that "
                   "resistance is working against.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A racing cyclist crouches low over the handlebars and "
                 "wears tight clothing instead of a loose jacket. Explain, "
                 "in terms of forces, why both of these make her faster.",
            "field_label": "Your explanation",
            "placeholder": "Air resistance acts…",
            "success": [
                "Says air resistance acts against her motion, backwards.",
                "Says crouching presents a smaller area to the air.",
                "Says a smaller area means less air pushed aside each "
                "second, so less resistance.",
                "Says loose clothing flaps and catches the air, increasing "
                "the resistance.",
                "Says that with less resistance the same push from her legs "
                "leaves a bigger resultant forwards, or lets her hold a "
                "higher steady speed.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A car with the accelerator held flat to the floor speeds "
                 "up, then settles at a top speed and goes no faster, even "
                 "though the engine is still working just as hard. Explain "
                 "why a car has a top speed at all.",
            "field_label": "Your answer",
            "placeholder": "At low speed the forward force is…",
            "success": [
                "Says the engine gives a forward force that stays roughly "
                "the same.",
                "Says air resistance and friction act backwards against the "
                "motion.",
                "Says the air resistance grows as the car goes faster.",
                "Says the car stops speeding up when the backwards forces "
                "have grown to match the forward force.",
                "Says the resultant is then 0 N, which is why the speed "
                "stays steady rather than the engine running out.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Moving through air or water means pushing it out of the "
                "way, and it pushes back against the motion. That resistance "
                "grows with speed and with the area facing the flow, so a "
                "falling object speeds up until the resistance has grown to "
                "match its weight — after which the resultant is 0 N and "
                "the speed stays the same. Streamlining reduces the "
                "resistance; a parachute is designed to maximise it.",

    "stretch": [
        {"id": "why-it-quadruples",
         "type": "explainer",
         "text": "At the speeds a car or a cyclist travels, air resistance "
                 "does not simply double when the speed doubles — it "
                 "roughly quadruples, because you are hitting twice as much "
                 "air per second and hitting each bit of it twice as hard. "
                 "The bench above uses exactly that rule, which is why the "
                 "resistance arrow grows so slowly at first and then so "
                 "fast. It also explains a fact drivers notice and rarely "
                 "explain: fuel economy falls off a cliff above about 60 "
                 "miles per hour, and driving at 80 rather than 70 costs far "
                 "more than the extra tenth of the speed suggests. For a "
                 "racing cyclist, most of the effort at speed goes into air, "
                 "not into the road, which is why the shape of a helmet "
                 "earns more than the weight of a frame."},
        {"id": "the-shape-everything-that-swims-finds",
         "type": "explainer",
         "text": "Water resistance is the same physics in a much heavier "
                 "fluid, and it sets the shape of everything that swims. "
                 "Fish, dolphins, submarines and torpedoes converge on the "
                 "same long, rounded-nose, tapering-tail form, because water "
                 "separating cleanly from a tapered tail leaves far less of "
                 "a churned-up wake than water tearing away from a blunt "
                 "one. Engineers call that shape streamlined, and "
                 "<strong>the test of it is the wake</strong>: the less mess "
                 "left behind, the less energy has been thrown away. It is "
                 "also why competitive swimmers shave, wear full-body suits "
                 "and spend a fortune on the moment their fingers enter the "
                 "water."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "drag",
         "definition": "The general name for resistance to motion through a "
                       "fluid, together with friction. Always against the "
                       "motion."},
        {"term": "terminal velocity",
         "definition": "The steady speed reached when the resistance has "
                       "grown to match the weight. A balance, not a limit."},
        {"term": "streamlined",
         "definition": "Shaped so that the fluid separates cleanly and "
                       "leaves little wake, which means less resistance."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to work out the terminal velocity of something of your "
                "own?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Drag, terminal velocity as a balance of forces, "
                   "velocity–time graphs of a falling object, and "
                   "streamlining.",

    "convention_note": "The fall bench is a teaching model. Resistance is "
                       "calculated as growing with the square of the speed, "
                       "fitted so that each object reaches the steady speed "
                       "quoted for it, and the speeds and weights are "
                       "typical values rather than measurements. The slider "
                       "is a share of that object's own steady speed, so 125 "
                       "per cent is a state only reached for a few seconds "
                       "— right after a parachute opens. Real resistance "
                       "also depends on air density, which falls with "
                       "altitude, and only the vertical forces are drawn.",

    "ws": [],
}
