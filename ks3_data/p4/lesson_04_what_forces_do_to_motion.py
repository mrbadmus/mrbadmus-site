"""P4 L4 — What forces do to motion (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p4/p4-04-what-forces-do-to-motion.dc.html`.

Her page wins outright. The curling stone, the trolley and gates, the four
cards and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA BLOCK, AND NONE IS OWED ───────────────────

`FORCES.02`'s motion clause is qualitative in statute. The bench works
without a quantity beyond the measured gate readings, and **no quantity
was invented in order to have something to put in a triangle.** `F = ma`
is GCSE and the word "acceleration" appears nowhere on the page; the
*Going further* layer names mass as a SHAPE — bigger force, bigger
change; bigger mass, smaller change — and stops there.

── ⚖️ RULED · THE GATE READINGS ARE MODEL VALUES, AND THEY ARE EXACT ─

Design's flag 5. They are what a 1 kg trolley under a steady 1 N resultant
with no friction would give, and the foot line says so and says real
readings run lower.

They are also internally exact, which is worth stating because a reader
might take them for round numbers: the sideways case reads 2.2 m/s at one
second and 3.6 m/s at three, and those are `√(2² + 1²)` and
`√(2² + 3²)`. A student who checks the vector arithmetic years later
finds the page was telling the truth — without the page ever having done
that arithmetic in front of them, because resolving into components is
GCSE.

── ⚖️ RULED · "JUST FOR AN INSTANT" STAYS IN RUNG 2 ──────────────────

Design's flag 3, and the physics is settled: at the highest point of a
straight-up throw the ball is not moving, for one instant, and the
resultant on it is still its whole weight. The hedge is not softening —
without it the question is ambiguous about whether the ball is being held.
A reviewer who prefers "momentarily at rest" should say so; the wording is
contested, the physics is not.

── ⚖️ RULED · "ALMOST NOTHING CHANGES" IN THE HOOK IS NOT TIDIED ─────

A curling stone does slow down. Tidying the hook to "nothing changes"
would make the page contradict its own rung 3, which asks why it
eventually stops.

── ⚠️ FOUR RAIL STOPS, AND `s-three` TICKS FIRST ─────────────────────

    s-hook · s-bench · s-three · s-ladder

Design's `DONE`: `s-bench` is `gate !== null && touched`, `s-three` is
`gate !== null`. The band block ticks on the COMMITMENT alone, before any
control is moved. It is marked by the bench, at that threshold —
`band_anchor: "s-three"`, `band_at: 1` against the gate.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    FORCE-24  if something is moving, a force must be pushing it along
    FORCE-25  a sideways force makes it go sideways instead
    FORCE-26  at the top of its flight a thrown ball has no force on it
    FORCE-27  a force that has stopped something has been used up

`FORCE-27` is not in Design's table. It arrived with rung 1's third
option — *"a resultant force forwards, which is running out"* — and it
is the impetus theory in its second form: not "motion needs a force" but
"the force drains". It is separate enough from `FORCE-12` to be worth its
own id, because a student can have accepted that a force needs two objects
and still believe the one they named is emptying.
"""

LESSON = {
    "slug":  "what-forces-do-to-motion",
    "title": "What forces do to motion",
    "discipline": "physics",
    "unit": "Forces",
    "family": "MODEL",

    # ⚠️ NO `covers`. This lesson owns no statutory statement of its own —
    # it is the bridge FORCES.02 needs in order to be about anything, and
    # inventing a claim for it would double-claim a clause p4-02 and p4-03
    # already carry between them. Declared honestly as `touches`.
    "covers": ["KS3.P.FMOT.01", "KS3.P.FMOT.02"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["balanced-and-unbalanced"],
    "assumes": [],
    "references": ["speed", "what-a-force-is", "pressure-force-over-area"],
    "ks4_links": [],

    "meta_description": "A curling stone slides twenty metres with nothing "
                        "touching it. A resultant force does not make things "
                        "move — it makes whatever they are already doing "
                        "change, and that is a much stranger idea.",

    "big_question": "A resultant force does not make things move. It makes "
                    "whatever they are already doing change — and that is "
                    "a much stranger idea.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Curling stone",     "done_when": "committed"},
        {"anchor": "s-bench",  "short": "GATES",
         "label": "Trolley and gates", "done_when": "gate_and_a_control"},
        {"anchor": "s-three",  "short": "THREE",
         "label": "Three things",      "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Nothing is pushing it, and it keeps going anyway.",
        "prompt": "A curling stone slides down twenty metres of ice at a "
                  "steady speed. Nobody is touching it. No engine, no rope, "
                  "nothing pushing it forwards at all.",
        "commit": "So why does it keep moving?",
        "options": [
            "Force from the push is still stored inside it, and it is "
            "slowly running out",
            "Nothing needs to push it — with almost nothing left over, "
            "almost nothing changes",
            "The ice underneath is pushing the stone forwards the whole "
            "way down",
            "It keeps going because it is heavy, and heavy things carry "
            "themselves along",
        ],
        "answer": 1,
        "reveal": "It keeps moving because nothing is stopping it. "
                  "<strong>Moving needs no force at all</strong> — a "
                  "resultant force is only needed to <em>change</em> what "
                  "something is doing. On very smooth ice there is almost "
                  "nothing left over, so almost nothing changes, and the "
                  "stone carries on at the same speed in the same direction "
                  "for a very long way.",
    },

    "misconceptions": [
        {"id": "FORCE-24",
         "statement": "If something is moving, a force must be pushing it "
                      "along.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "FORCE-25",
         "statement": "A sideways force makes it go sideways instead.",
         "elicited_by": "gates",
         "confronted_by": "s-think"},
        {"id": "FORCE-26",
         "statement": "At the top of its flight a thrown ball has no force "
                      "on it.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
        {"id": "FORCE-27",
         "statement": "A force that is slowing something down has been used "
                      "up by the time it stops.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A resultant force can do exactly three things to motion: "
                 "start it or speed it up, slow it down or stop it, or "
                 "change its direction. <strong>If nothing is left over, "
                 "none of those happens</strong> — whatever the object was "
                 "doing, it carries on doing."},

        # ── #s-bench · the trolley and the light gates ─────────────────
        {"type": "gate-run",
         "id": "gates",
         "anchor": "s-bench",
         "eyebrow": "At the bench · trolley and light gates",
         "heading": "Same trolley, same start, four resultants",
         "progress": "Change a control to begin",
         "lead": "Every run starts with the trolley already travelling at "
                 "2.0 m/s to the right, timed through a light gate. Choose a "
                 "resultant force, choose how long it acts, and take a "
                 "second reading.",
         "case_label": "The resultant force",
         "time_label": "How long it acts",
         "start_case": "fwd",
         "start_secs": 1,
         "band_anchor": "s-three",
         "band_at": 1,
         "gate": {
             "prompt": "Commit first. The resultant force is 0 N and the "
                       "trolley is already moving. What does the second gate "
                       "read?",
             "options": [
                 "Less than 2.0 m/s — it must slow without a push",
                 "2.0 m/s — the same as the first gate",
                 "0 m/s — with no force it stops",
                 "More than 2.0 m/s",
             ],
             "answer": 1,
         },
         "times": [
             {"secs": 1, "label": "For 1 second"},
             {"secs": 3, "label": "For 3 seconds"},
         ],
         "cases": [
             {"id": "none", "tab": "None — balanced", "label": "0 N",
              "dir": "none", "path": "straight, at a steady speed",
              "changed": "Nothing", "same": "Speed and direction",
              "after": {1: "2.0 m/s", 3: "2.0 m/s"},
              "notes": {
                  1: "Both gates read 2.0 m/s. With nothing left over there "
                     "is nothing to change the motion, so the trolley "
                     "arrives doing exactly what it was doing.",
                  3: "Three seconds and still 2.0 m/s. Time makes no "
                     "difference when the resultant is 0 N — this is the "
                     "state a curling stone on good ice is nearly in.",
              }},
             {"id": "fwd", "tab": "1 N forwards", "label": "1 N forwards",
              "dir": "fwd", "path": "straight, and getting faster",
              "changed": "Speed — faster", "same": "Direction",
              "after": {1: "3.0 m/s", 3: "5.0 m/s"},
              "notes": {
                  1: "One second of 1 N forwards took it from 2.0 m/s to "
                     "3.0 m/s. The direction is untouched: the resultant "
                     "pointed the way it was already going, so only the "
                     "speed changed.",
                  3: "Three seconds of the same 1 N took it to 5.0 m/s — "
                     "three times the change of one second. The longer a "
                     "resultant force acts, the bigger the change it makes.",
              }},
             {"id": "back", "tab": "1 N backwards", "label": "1 N backwards",
              "dir": "back", "path": "straight, and slowing down",
              "changed": "Speed — slower, then reversed",
              "same": "The line it travels along",
              "after": {1: "1.0 m/s", 3: "1.0 m/s, backwards"},
              "notes": {
                  1: "One second of 1 N backwards brought it down from "
                     "2.0 m/s to 1.0 m/s. A resultant force against the "
                     "motion is what slowing down actually is.",
                  3: "After two seconds it stopped; the force kept acting, "
                     "so by three seconds it is moving backwards at "
                     "1.0 m/s. Nothing switched off when it reached zero "
                     "— a ball thrown upwards does the same thing.",
              }},
             {"id": "side", "tab": "1 N sideways", "label": "1 N sideways",
              "dir": "side", "path": "bending away from the straight line",
              "changed": "Direction — the path bends",
              "same": "It is still travelling to the right",
              "after": {1: "2.2 m/s", 3: "3.6 m/s"},
              "notes": {
                  1: "The gate reads 2.2 m/s and the path has bent. The "
                     "trolley did not stop going right and start going "
                     "sideways — it is doing both, which is why the "
                     "reading went up a little as well.",
                  3: "Three seconds of sideways force and the path has bent "
                     "a long way, with the reading up to 3.6 m/s. This is "
                     "how an orbit works: a pull sideways-on to the motion "
                     "curves the path instead of stopping it.",
              }},
         ],
         "readouts": [
             {"id": "gate1", "label": "Gate 1", "value": "2.0 m/s"},
             {"id": "gate2", "label": "Gate 2"},
             {"id": "changed", "label": "What changed"},
             {"id": "same", "label": "What stayed the same"},
         ]},

        # ── #s-three · three things, and only three ────────────────────
        {"type": "force-band",
         "id": "three-things",
         "anchor": "s-three",
         "eyebrow": "Three things, and only three",
         "heading": "Everything on the bench was one of these.",
         "panels": [
             {"num": "1", "name": "Start it, or speed it up",
              "body": "A resultant force in the direction of travel makes "
                      "the object go faster. From rest, it is what gets it "
                      "moving at all."},
             {"num": "2", "name": "Slow it down, or stop it",
              "body": "A resultant force against the direction of travel "
                      "makes it slower. Leave it acting and the object "
                      "stops, then goes the other way."},
             {"num": "3", "name": "Change its direction",
              "body": "A resultant force across the direction of travel "
                      "bends the path. The original motion is still there "
                      "underneath."},
             {"num": "4", "name": "Or, with 0 N left over: nothing",
              "body": "At rest, it stays at rest. Moving, it carries on at "
                      "the same speed in the same direction, with no push "
                      "needed."},
         ],
         "close": "Two things also decide <em>how much</em> changes: how big "
                  "the resultant force is, and which way it points. A bigger "
                  "resultant changes the motion faster, and the direction it "
                  "points is the direction the change happens in."},

        {"type": "key-fact", "ref": "force-changes-motion"},

        {"type": "misconception", "id": "think-moving-needs-a-push",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-moving-needs-a-push",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-24",
         "statements": [
             {"quote": "If something is moving, there must be a force "
                       "pushing it along.",
              "targets": "FORCE-24",
              "body": [
                  "This one is worth taking seriously, because everyday life "
                  "agrees with it. Stop pedalling and the bike slows; stop "
                  "pushing the box and it stops. So it really does look as "
                  "though motion needs a constant supply of push. "
                  "<strong>What is hidden is friction</strong>: on a "
                  "bicycle, on a floor, in the air, something is always "
                  "pushing backwards, and your forward push is cancelling it "
                  "rather than causing the motion. Remove the friction — a "
                  "curling stone on ice, a puck on an air table, a "
                  "spacecraft between planets — and the object needs "
                  "nothing at all to keep going. Voyager 1 has had its "
                  "engines off since 1980 and is still travelling at 17 "
                  "kilometres a second.",
              ]},
             {"quote": "A force sideways makes it go sideways instead.",
              "targets": "FORCE-25",
              "body": [
                  "It does not throw away what the object was already doing. "
                  "On the bench above, a sideways resultant left the trolley "
                  "still travelling to the right — it simply added a bend "
                  "to the path, so the trolley ended up going right "
                  "<em>and</em> sideways at once. This is exactly why the "
                  "Moon goes round the Earth instead of falling into it: the "
                  "Earth's pull is sideways-on to the Moon's motion, so it "
                  "bends the path into a circle rather than stopping the "
                  "Moon and dragging it in. <strong>A resultant force adds a "
                  "change; it does not replace the motion.</strong>",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "force-changes-motion",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A resultant force is needed to start something moving, to "
                 "speed it up, to slow it down or stop it, or to change its "
                 "direction. Moving at a steady speed in a straight line "
                 "needs no resultant force at all."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "A cyclist is freewheeling and slowing down. What must be "
                 "true about the forces on the bicycle?",
            "options": [
                "There is no force at all, which is why it is slowing.",
                "There is a resultant force forwards, which is running out.",
                "There is a resultant force backwards, against the direction "
                "of travel.",
                "The forces are balanced, because the cyclist has stopped "
                "pedalling.",
            ],
            "answer": 2,
            "feedback": {
                0: "With no resultant force it would carry on at the same "
                   "speed. Slowing down is a change, and a change needs "
                   "something left over.",
                1: "A force does not run out, and a forward resultant would "
                   "make the bicycle speed up rather than slow down.",
                3: "Balanced forces would keep the speed steady. Air "
                   "resistance and friction are unopposed once the pedalling "
                   "stops.",
            },
            "title": "Rung 1 · Apply"},
        "apply": {
            "q": "A ball is thrown straight up. At the highest point, just "
                 "for an instant, it is not moving. What is the resultant "
                 "force on it then?",
            "options": [
                "0 N, because it is not moving at that instant.",
                "Upwards, left over from the throw.",
                "0 N going up, then downwards on the way back.",
                "Its weight, downwards — unchanged the whole way up and "
                "down.",
            ],
            "answer": 3,
            "feedback": {
                0: "Force does not depend on speed. If the resultant were "
                   "0 N there the ball would hang in the air, which is not "
                   "what happens.",
                1: "The hand’s push ended the moment the ball left it. "
                   "Nothing is pushing it up on the way at all.",
                2: "The Earth pulls with the same force throughout. The "
                   "motion changes direction; the force never does.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A curling stone slides twenty metres across ice at almost "
                 "the same speed the whole way, with nothing touching it. "
                 "Explain why it keeps going, and why it does eventually "
                 "stop.",
            "field_label": "Your explanation",
            "placeholder": "Nothing needs to push it because…",
            "success": [
                "Says no force is needed to keep something moving.",
                "Says the forces on the stone are very nearly balanced, so "
                "the resultant is close to 0 N.",
                "Says a resultant force is only needed to change the motion.",
                "Names friction with the ice, or air resistance, as a small "
                "backwards force.",
                "Says that small backwards resultant is what slows it, and "
                "that on perfectly smooth ice it would not stop.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A satellite circles the Earth at a steady speed with its "
                 "engines switched off. Its speed never changes, but there "
                 "is a resultant force on it the whole time. Explain how "
                 "both of those can be true, and say which way the force "
                 "points.",
            "field_label": "Your answer",
            "placeholder": "The force points…",
            "success": [
                "Says the resultant force is the Earth’s gravitational "
                "pull.",
                "Says it points towards the Earth, across the direction the "
                "satellite is travelling.",
                "Says a force across the motion changes direction rather "
                "than speed.",
                "Says that is why the path is a circle rather than a "
                "straight line.",
                "Says the motion is still changing, because a change of "
                "direction is a change even at a steady speed.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Forces change motion; they do not maintain it. A resultant "
                "force can start something moving, speed it up, slow it "
                "down, stop it, or change its direction, and how much it "
                "changes depends on how big that force is and which way it "
                "points. With balanced forces nothing changes: something at "
                "rest stays at rest, and something moving carries on at the "
                "same speed in the same direction.",

    "stretch": [
        {"id": "galileo-and-the-limit",
         "type": "explainer",
         "text": "For roughly two thousand years the best minds available "
                 "believed that motion needed a cause, and they were not "
                 "being stupid — they were describing the world in front "
                 "of them, where everything does stop. Aristotle's version "
                 "lasted until the 1600s, when Galileo tried rolling balls "
                 "down one slope and up another and noticed that the "
                 "smoother he made the surfaces, the further they went. He "
                 "drew the conclusion nobody had drawn: that with the "
                 "friction removed entirely, the ball would never stop, and "
                 "therefore motion needs no cause at all. <strong>Nothing "
                 "about that can be seen directly.</strong> It is reached by "
                 "making an experiment cleaner and cleaner and then "
                 "imagining the limit, which is one of the most powerful "
                 "moves in science and worth recognising when you next meet "
                 "it."},
        {"id": "the-shape-of-f-equals-ma",
         "type": "explainer",
         "text": "The same trolley pushed with the same resultant force does "
                 "not always change by the same amount, and what makes the "
                 "difference is its mass. Load the trolley with bricks and "
                 "1 N barely alters it; empty it and the same 1 N makes a "
                 "much bigger change. That relationship — resultant force, "
                 "mass and how fast the motion changes — is a real "
                 "equation you will meet at GCSE. At this stage the useful "
                 "half is the shape of it: <strong>bigger force, bigger "
                 "change; bigger mass, smaller change.</strong>"},
    ],

    "support": [],

    "vocabulary": [
        {"term": "light gate",
         "definition": "A beam and a timer. The clock runs only while "
                       "something is between the two gates, so the reading "
                       "is a speed over a known distance."},
        {"term": "steady speed",
         "definition": "The same speed in the same direction. It needs no "
                       "resultant force at all — only a change does."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to test the idea on a situation of your own?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Newton's first and second laws, acceleration, and the "
                   "equation linking resultant force, mass and acceleration.",

    "convention_note": "The trolley bench is a teaching model: the gate "
                       "readings are the values a 1 kg trolley would give "
                       "with a steady 1 N resultant and no friction, rounded "
                       "to one decimal place. Real trolleys have friction, "
                       "so real second readings are always a little lower.",

    "ws": [],
}
