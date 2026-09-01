"""P10 L5 — How a motor works (SYSTEM).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p10/p10-05-how-a-motor-works.dc.html`.

Her page wins outright. The swapped leads, the coil between two magnets, the
four parts and all four rungs are hers.

── ⚖️ REVERSE ONE THING AND IT REVERSES; REVERSE BOTH AND IT DOES NOT ──

That is the whole lesson, it is the commit gate, it is rung 1, and it is the
closing line of the four-parts figure. It is also a property of the ARITHMETIC
here rather than of four authored sentences: the direction is the sign of
`current × field`, so the both-reversed case comes out identical by
construction and could not drift into disagreeing with the gate. `MAG-19` is
the belief that two changes must make two differences.

── ⚖️ THE SPLIT RING DOES NOT MAKE IT TURN — IT MAKES IT KEEP TURNING ─

`MAG-18`, and the reason the `plain rings` state is on the bench at all. It
STARTS: the note's first two words are *"It starts."* and half of the
twenty-four turning states are plain-ring states, so a student meets the
distinction rather than reading it. Design's own second Think-again quote says
the same thing in the same words.

── ⚖️ THE COIL IS FROZEN HORIZONTAL ──────────────────────────────────

Her §9 ruling 5, applied and disclosed. Nothing on this bench animates,
nothing has a timer, and the drawing shows the pushes at the position where
the turning effect is largest. The legal line says both halves out loud: that
this is the frozen best case, and that a real single-coil motor's turning
effect falls to nothing twice per turn — which is also why *Going further*
explains that real motors use several coils.

── ⚖️ FRICTION IS REAL, AND IT IS WHY THE LOWEST CURRENT DOES NOTHING ─

Eight of the thirty-two states never start. The note names the number the
turning effect has to beat, the pushes are still drawn and still in the right
directions, and the tile says `not at all`. That is the zero state driven on
purpose: rung 2's whole premise is that a motor can be built and fail to move,
and a bench where every setting turned would leave the rung with nothing
behind it.

── ⚖️ THE STATE SPACE ────────────────────────────────────────────────

    2 current directions × 2 magnet arrangements × 2 rings × 4 currents   32
      never starts, at 0.5 A                                               8
      turns and keeps turning, with the split ring                        12
      turns half a turn and stops, with plain rings                       12

    turning effect  =  100 × current ÷ 4.0 A,   friction at the axle 15
      0.5 A → 13   ·   1.0 A → 25   ·   2.0 A → 50   ·   4.0 A → 100

── ⚠️ NO FORMULA BLOCK, AND NO NEWTON METRE ──────────────────────────

`F = BIL` is GCSE and the turning effect of a coil is beyond that again. The
figure a student reads here is relative, on a scale the readout declares, and
her legal line says in terms that no value in newtons or newton metres is
given because the equation is beyond this stage.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's hook, gate and both rungs all put the correct answer at index 0.
**Her option TEXT and every correction are verbatim; only the ORDER moves.**
This lesson takes indices 2 (hook), 1 (gate), 3 (rung 1) and 1 (rung 2). No
option set on this page is a length tell at MRB-177's threshold, so nothing
was finished.

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ─────────────────────
"""

LESSON = {
    "slug": "how-a-motor-works",
    "title": "How a motor works",
    "discipline": "physics",
    "unit": "Magnetism and electromagnetism",
    "family": "SYSTEM",

    # ⚠️ `.04b`, NOT the parent. See `p10-04` and
    # `ks3_data/substatements.py`: `covers` is exactly-once across the key
    # stage, and Design's §1 claims the parent on both lessons.
    #
    # ⚠️ AND `MAG.02` IS NOT CARRIED HERE, although her §1 claims it a third
    # time. This page draws a field between two magnets; it never plots one
    # with a compass, and plotting with a compass is what `MAG.02` names. A
    # `touches` that the page does not do is worse than none, because it is
    # the row a scheme-of-work reader would trust.
    "covers": ["KS3.P.MAG.04b"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 3},
                {"id": "forces-and-fields", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 60,

    # ⚠️ Design's §3: this page RESTATES that a current makes a magnetic
    # field, so it does not depend on `p10-04`. The edge is the honest reading
    # order and nothing is assumed.
    "requires": ["electromagnets"],
    "assumes": [],
    # ⚠️ `moments`, NOT `turning-forces`. The first cut named a slug that does
    # not exist anywhere in the key stage, and the engine DROPPED the edge in
    # SILENCE — the built page simply carried one reference where two were
    # authored, with nothing raised by the build or by any gate. Found by
    # resolving every P10 edge against `ks3_data.build_units()` by hand.
    # P4's lesson on the turning effect of a force is `moments`, and it is the
    # right edge: two opposite pushes either side of an axle is a pair of
    # moments, which is the one idea this lesson borrows from forces.
    "references": [{"unit": "P8", "lesson": "current-and-circuits"},
                   {"unit": "P4", "lesson": "moments"}],
    "ks4_links": [],

    "meta_description": "A wire carrying a current in a magnetic field is "
                        "pushed sideways — and two opposite pushes either "
                        "side of an axle are what turns a motor.",

    # ⊕ Integration, 25 Aug 2026 — HER LEDE, verbatim (Phase 3 revert; the
    # authored question was a paraphrase no row claimed).
    "big_question": "A wire carrying a current inside a magnetic field is pushed. "
                    "Arrange for the push to keep going the same way round, and "
                    "you have a motor.",

    "rail": [
        {"anchor": "s-hook",  "short": "MOTOR",
         "label": "Swap the wires",     "done_when": "committed"},
        {"anchor": "s-bench", "short": "BENCH",
         "label": "Reverse one thing",  "done_when": "gate_and_a_control"},
        # ⚠️ Design's `DONE` gives this stop the GATE alone; the bench marks
        # it through `band_anchor` / `band_at`. See `ks3_art/p10.py`.
        {"anchor": "s-parts", "short": "PARTS",
         "label": "Four parts",         "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",     "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Swap the two wires and the motor runs backwards.",
        "prompt": "A small electric motor is connected to a battery and its "
                  "shaft spins clockwise. Take both wires off, put them back "
                  "the other way round, and the same motor spins "
                  "anticlockwise at the same speed. Nothing inside it has "
                  "been touched.",
        "commit": "Why does swapping the wires reverse it?",
        # ⚠️ MRB-278 — position 2.
        # ⊕ MRB-297, 1 Sep 2026 — distractor 1 widened. The correct option
        # was the longest by 5, which is a tell below the gate's constant
        # as well as at it. The balance now holds at 1.
        "options": [
            "The battery pushes rather than pulls when it is the other way "
            "round",
            "The magnets inside are flipped right over by the current "
            "arriving from the other side",
            "The current now runs the other way round the coil, so the push "
            "on each side reverses",
            "The motor always alternates direction, and swapping the wires "
            "just resets it",
        ],
        "answer": 2,
        "reveal": "The direction of the push on a current-carrying wire in a "
                  "field depends on which way the current is going. Swapping "
                  "the leads sends the current round the coil the other way, "
                  "so both sides are pushed the opposite way and the coil "
                  "turns the opposite way. The magnets inside have not moved, "
                  "and they could not be flipped by a current — they are "
                  "permanent magnets bonded to the case.",
    },

    "misconceptions": [
        {"id": "MAG-17",
         "statement": "The coil is pulled round because the magnets attract "
                      "it.",
         "elicited_by": "motor",
         "confronted_by": "s-think"},
        {"id": "MAG-18",
         "statement": "The split ring is what makes it turn.",
         "elicited_by": "motor",
         "confronted_by": "s-think"},
        {"id": "MAG-19",
         "statement": "Reversing the current and the magnets reverses it "
                      "twice over.",
         "elicited_by": "motor",
         "confronted_by": "motor"},
        # ⊕ MINTED FROM THE COMMIT GATE'S THIRD OPTION AND RUNG 1'S SECOND.
        # Separate from `MAG-19`, and it reaches a different wrong answer by a
        # different route: `MAG-19` treats the two reversals as adding up to a
        # double reversal, while this one treats current and field as two
        # forces along one line that can cancel each other to a standstill. A
        # student holding it has not yet met the idea that the push is at
        # right angles to both.
        {"id": "MAG-20",
         "statement": "If the current and the field are both reversed they "
                      "work against each other, so the coil stops.",
         "elicited_by": "motor",
         "confronted_by": "motor"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Put a wire that is carrying a current into a magnetic "
                 "field, and the wire is <strong>pushed sideways</strong> — "
                 "at right angles both to the field and to the current. This "
                 "is the one new fact the whole lesson rests on, and it is "
                 "easy to show: a loose wire between the poles of a horseshoe "
                 "magnet jumps the moment the current is switched on."},
        {"type": "explainer",
         "text": "Which way it is pushed depends on <strong>two</strong> "
                 "things: the direction of the current, and the direction of "
                 "the field. Reverse the current and the push reverses. "
                 "Reverse the magnets and the push reverses. Reverse both and "
                 "it goes back to where it started."},
        {"type": "explainer",
         "text": "Now bend the wire into a rectangular loop and hang it on an "
                 "axle between the poles. The current runs one way along the "
                 "left-hand side of the loop and the other way along the "
                 "right-hand side, so the two sides are pushed in "
                 "<strong>opposite</strong> directions — one up, one down. A "
                 "pair of opposite pushes on either side of an axle is a "
                 "turning effect, and the loop turns."},
        {"type": "explainer",
         "text": "There is a catch. After half a turn the two sides have "
                 "swapped places, and the pushes now fight the rotation "
                 "instead of driving it. The fix is the <strong>split-ring "
                 "commutator</strong>: the loop's two ends are joined to two "
                 "half-rings that press against fixed contacts, so every half "
                 "turn the connection swaps and the current through the loop "
                 "reverses. The push therefore keeps driving the same way "
                 "round, and the motor keeps going."},

        # ── #s-bench · a coil on an axle between two magnets ───────────
        {"type": "motor-coil",
         "id": "motor",
         "anchor": "s-bench",
         "eyebrow": "At the bench · a coil on an axle between two magnets",
         "heading": "Reverse one thing at a time.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Four controls live"},
         # ⚠️ HER SECOND SENTENCE IS CUT. It read "Set which way the current
         # goes round, which way round the magnets are, whether the split ring
         # is fitted, and how much current flows" — four clauses naming four
         # controls already on screen (5A.1). The orientation sentence stays:
         # which way the drawing is seen from is the one thing a student
         # cannot work out by looking.
         "lead": "The coil is drawn face on, with the field running across "
                 "the page between the two magnets.",
         "band_anchor": "s-parts",
         "band_at": 1,
         # ⚖️ THE TURNING EFFECT HAS TO BEAT THIS BEFORE ANYTHING MOVES. At
         # 0.5 A it reads 13 against a friction of 15, which is the state
         # rung 2's premise depends on.
         "friction": 15,
         "max_current": 4,
         "currents": [0.5, 1, 2, 4],
         "start_dir": 0,
         "start_mag": 0,
         "start_comm": 0,
         "dir_label": "Current round the coil",
         "mag_label": "The magnets",
         "comm_label": "At the axle",
         "current_control": {"label": "Current", "min": 0, "max": 3,
                             "step": 1, "start": 2, "value": "2.0 A"},
         "gate": {
             "prompt": "Commit first. A working motor has its battery leads "
                       "swapped and its two magnets turned round, both at the "
                       "same time. Which way does it now spin?",
             # ⚠️ MRB-278 — position 1.
             "options": [
                 "The other way round, because two changes were made",
                 "Exactly as it did before — two reversals cancel",
                 "It stops, because the current and the field now oppose each "
                 "other",
                 "The other way round and more slowly, because the field is "
                 "now fighting the current",
             ],
             "answer": 1,
         },
         # ⚖️ THE SIGNS ARE THE PHYSICS. Direction of turn is the sign of
         # `current × field`, so the both-reversed case is identical to the
         # untouched one by construction rather than by an authored sentence
         # that could drift away from the gate.
         "dirs": [
             {"id": "down-left", "label": "Down the left side", "sign": 1},
             {"id": "up-left", "label": "Up the left side", "sign": -1},
         ],
         "mags": [
             {"id": "north-left", "label": "North on the left", "sign": 1},
             {"id": "south-left", "label": "South on the left", "sign": -1},
         ],
         "comms": [
             {"id": "split", "label": "Split ring fitted",
              "caption": "SPLIT RING AT THE AXLE"},
             {"id": "plain", "label": "Plain rings instead",
              "caption": "PLAIN RINGS AT THE AXLE"},
         ],
         "readouts": [
             {"id": "left", "label": "The left-hand side is", "sub": "—"},
             {"id": "torque", "label": "Turning effect",
              "sub": "where 100 is the strongest setting here"},
             {"id": "spin", "label": "It spins"},
             {"id": "keep", "label": "Does it keep going"},
         ],
         # ⚠️ `{current}` is the current in amps to one decimal, `{torque}`
         # the turning effect on the declared scale, `{friction}` the friction
         # at the axle, `{leftdir}` / `{rightdir}` the two push directions,
         # `{spin}` the direction of turn, `{dirlabel}` the chosen current
         # control's own words and `{fielddir}` which way the field runs.
         "branches": {
             "never": {
                 "keep": "no — it never starts",
                 "note": "At {current} A the turning effect reads {torque} on "
                         "this scale, and the friction at the axle is worth "
                         "about {friction}. The pushes are there — the "
                         "left-hand side is being pushed {leftdir} and the "
                         "right-hand side {rightdir} — but they are not yet "
                         "enough to move it. Turn the current up and it "
                         "starts. Nothing about the direction has changed; "
                         "only the size has."},
             "split": {
                 "keep": "yes — the split ring keeps it going",
                 "note": "The current runs {dirlabel} and the field runs "
                         "{fielddir}, so the left-hand side is pushed "
                         "{leftdir} and the right-hand side {rightdir} — two "
                         "opposite pushes on either side of the axle, which "
                         "is a turning effect, and the coil goes {spin} with "
                         "a strength of {torque} on this scale. The split "
                         "ring swaps the connections every half turn, so as "
                         "each side crosses to the other half of the field "
                         "the current through it reverses too and the push "
                         "keeps driving the same way round. Reverse the "
                         "current on its own and it runs the other way; "
                         "reverse the magnets on their own and it runs the "
                         "other way; reverse both and you are back where you "
                         "started."},
             "plain": {
                 "keep": "no — half a turn and it stops",
                 "note": "It starts. The left-hand side is pushed {leftdir} "
                         "and the right-hand side {rightdir}, so the coil "
                         "swings {spin} at a strength of {torque} — and then "
                         "it stops. With plain rings the current through the "
                         "coil never changes direction, so once the two sides "
                         "have swapped over at the half turn the same pushes "
                         "are fighting the rotation instead of driving it. "
                         "The coil settles upright. Fit the split ring "
                         "instead and the current reverses at exactly that "
                         "moment, which is the entire job that part does."},
         },
         "words": {
             "up": "up",
             "down": "down",
             "clockwise": "clockwise",
             "anticlockwise": "anticlockwise",
             "still": "not at all",
             "left_is": "pushed {dir}",
             "right_is": "the right-hand side is pushed {dir}",
             "field_lr": "left to right",
             "field_rl": "right to left",
         }},

        # ── #s-parts · four parts, and what each one is for ────────────
        {"type": "mag-band",
         "id": "parts",
         "anchor": "s-parts",
         "eyebrow": "The figure",
         "heading": "Four parts, and what each one is for",
         "tiles": [
             {"id": "part-magnets", "eyebrow": "The magnets",
              "body": "Provide a field across the gap. Turn them round and "
                      "everything reverses."},
             {"id": "part-coil", "eyebrow": "The coil",
              "body": "Carries current up one side and down the other, so the "
                      "two sides are pushed opposite ways and the coil "
                      "turns."},
             {"id": "part-split", "eyebrow": "The split ring", "accent": True,
              "body": "Swaps the connections every half turn, so the current "
                      "through the coil reverses just as the coil passes "
                      "upright. Without it the motor stops after half a "
                      "turn."},
             {"id": "part-brushes", "eyebrow": "The brushes",
              "body": "Fixed contacts that press on the split ring, so "
                      "current can reach a part that is spinning."},
         ],
         "close": "Reverse the current: it runs the other way. Reverse the "
                  "magnets: it runs the other way. Reverse both: it runs "
                  "exactly as it did. That last one is the test of whether "
                  "you have understood the rule rather than memorised a "
                  "picture."},

        {"type": "key-fact", "ref": "pushed-sideways"},

        {"type": "misconception", "id": "think-the-magnets-pull-it",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-the-magnets-pull-it",
         "kind": "predict",
         "demand": "explain",
         "targets": "MAG-17",
         "statements": [
             {"quote": "The coil is pulled round because the magnets attract "
                       "it.",
              "targets": "MAG-17",
              "body": [
                  "Switch the current off and the coil hangs there — the "
                  "magnets do nothing to a coil of copper wire, because "
                  "copper is not a magnetic material and there is nothing to "
                  "attract. What acts is a force on the <em>moving charge</em> "
                  "in the wire, and it appears only while a current flows. It "
                  "is also at right angles to both the field and the current, "
                  "which is not what attraction looks like: the coil is not "
                  "pulled towards either magnet, it is pushed up on one side "
                  "and down on the other.",
              ]},
             {"quote": "The split ring is what makes it turn.",
              "targets": "MAG-18",
              "body": [
                  "It is what makes it <em>keep</em> turning. Remove the "
                  "split ring and the coil still starts — you can see it kick "
                  "on the bench — but only for half a turn, because after "
                  "that the sides have changed places and the same pushes are "
                  "now fighting the rotation. The split ring does not create "
                  "the turning effect; it reverses the current at the moment "
                  "the turning effect would otherwise start working against "
                  "you.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "pushed-sideways",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A wire carrying a current in a magnetic field is pushed "
                 "sideways, and the direction of the push depends on both the "
                 "current direction and the field direction. In a motor a "
                 "coil on an axle has its two sides pushed opposite ways, "
                 "which turns it, and a split-ring commutator reverses the "
                 "current every half turn so the turning effect keeps driving "
                 "the same way round."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. Rungs take indices 3 and 1. Design
    # put both at 0; her option TEXT and every correction are verbatim and
    # only the ORDER moves.
    "ladder": {
        "recall": {
            "q": "A motor is running clockwise. Its two magnets are turned "
                 "round so the poles swap, and nothing else is changed. What "
                 "happens?",
            "options": [
                "It runs clockwise still, because the current has not changed",
                "It stops, because the two changes cancel out",
                "It runs anticlockwise, but more slowly, because the field is "
                "now working against the current",
                "It runs anticlockwise, at the same speed",
            ],
            "answer": 3,
            "feedback": {
                0: "The push depends on the field as well as the current. "
                   "Change either one on its own and the push reverses.",
                1: "Only one thing was changed. Reversing the current as well "
                   "would put it back to clockwise — that is the case where "
                   "two changes cancel.",
                2: "The direction reverses but the size does not change. The "
                   "magnets are just as strong turned round.",
            },
            "title": "Rung 1 · Predict the reversal"},
        "apply": {
            "q": "A student builds a motor but fits two plain rings instead "
                 "of a split ring. What do they see when the current is "
                 "switched on?",
            "options": [
                "Nothing happens, because plain rings cannot carry a current",
                "The coil turns about half a turn and then stops",
                "The coil spins normally, because the split ring only makes "
                "it faster",
                "The coil spins the wrong way round",
            ],
            "answer": 1,
            "feedback": {
                0: "Plain rings carry current perfectly well — the coil does "
                   "start to turn. What they cannot do is swap the "
                   "connections over.",
                2: "It is not a speed part. Without the swap, the pushes "
                   "start fighting the rotation after half a turn.",
                3: "The direction it starts in is set by the current and the "
                   "field, and plain rings do not change either. The problem "
                   "is that it does not keep going.",
            },
            "title": "Rung 2 · Diagnose the fault"},
        "explain": {
            "q": "Explain why a coil carrying a current between two magnets "
                 "turns, rather than simply being pushed to one side.",
            "field_label": "Your explanation",
            "placeholder": "A wire carrying a current in a field is…",
            "success": [
                "Says a wire carrying a current in a magnetic field is pushed "
                "sideways.",
                "Says the direction of the push depends on the current "
                "direction and the field direction.",
                "Says the current runs in opposite directions along the two "
                "sides of the coil.",
                "Says the two sides are therefore pushed in opposite "
                "directions, one up and one down.",
                "Says two opposite pushes on either side of an axle give a "
                "turning effect rather than a sideways one.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A cordless drill has a switch marked forward and reverse, "
                 "and the motor inside has permanent magnets that cannot be "
                 "moved. Explain what that switch must be doing, and explain "
                 "why the drill still needs a split ring in both settings.",
            "field_label": "Your answer",
            "placeholder": "The magnets cannot move, so the only thing left "
                           "to change is…",
            "success": [
                "Says the direction of the push depends on the current and "
                "the field, and the field is fixed here.",
                "Says the switch must therefore reverse the direction of the "
                "current through the motor.",
                "Says reversing the current reverses the push on each side of "
                "the coil, so the coil turns the other way.",
                "Says the split ring is what reverses the current every half "
                "turn so the coil keeps going round.",
                "Says that job still has to be done whichever way the drill "
                "is running, so the split ring is needed in both settings.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A wire carrying a current in a magnetic field is pushed "
                "sideways, at right angles to both. Which way it is pushed "
                "depends on the current direction and on the field direction, "
                "so reversing either one reverses the push and reversing both "
                "changes nothing. A motor is a coil on an axle in a field: "
                "the current runs up one side and down the other, the two "
                "sides are pushed opposite ways, and the coil turns. After "
                "half a turn the sides have swapped and the pushes would "
                "fight the rotation, so a split-ring commutator reverses the "
                "current every half turn and the motor keeps going.",

    "stretch": [
        {"id": "why-real-motors-have-several-coils",
         "type": "explainer",
         "text": "Real motors have more than one coil, set at angles to each "
                 "other, and the commutator has a segment for each. That "
                 "fixes two problems at once: the turning effect of a single "
                 "coil drops to nothing twice per turn, when the coil is "
                 "upright and the pushes are pulling it apart rather than "
                 "round, and a single-coil motor therefore runs unevenly and "
                 "will not start at all from that position. With several "
                 "coils, one of them is always well placed, and the machine "
                 "starts from wherever it happens to be sitting."},
        {"id": "run-it-backwards",
         "type": "explainer",
         "text": "Run the same machine backwards and it becomes a generator. "
                 "Turn the coil by hand instead of feeding it current and a "
                 "voltage appears across its ends, because moving a wire "
                 "through a field pushes the charge in it along. Almost every "
                 "power station on Earth is doing that, on an enormous scale, "
                 "with steam or water or wind turning the coil."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "coil",
         "definition": "A loop of wire on an axle between the magnets. The "
                       "current runs one way along one side of it and the "
                       "other way along the other side, so the two sides are "
                       "pushed in opposite directions."},
        {"term": "turning effect",
         "definition": "What a pair of opposite pushes on either side of an "
                       "axle produces. One push on its own would move the "
                       "coil sideways; two opposite ones turn it instead."},
        {"term": "split-ring commutator",
         "definition": "Two half-rings on the axle, joined to the two ends of "
                       "the coil. Every half turn they swap which contact "
                       "each end touches, so the current through the coil "
                       "reverses and the push keeps driving the same way "
                       "round."},
        {"term": "brushes",
         "definition": "Fixed contacts that press against the split ring, so "
                       "that a current can reach a part of the machine that "
                       "is spinning."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to check which way a coil will turn?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Fleming's left-hand rule, the force on a conductor worked "
                   "out from flux density, current and length, and the "
                   "generator effect.",

    # ⚖️ MRB-297 · Mide's wording. Approved 1 Sep 2026, recorded on the
    # ticket as `## RULED — 1 Sep 2026`. Not to be edited.
    #
    # ⊕ 1 Sep 2026. This note used to be shared byte-for-byte with
    # `lesson_04_electromagnets.py`, which has no spinning part. Mide has
    # split the two rigs. The spinning-part warning stays HERE, where there
    # IS a spinning part — a coil on an axle turned by a split-ring
    # commutator — and now LEADS the note instead of trailing it. The
    # reasoning is written up in full in lesson 04.
    "safety_note": "Eye protection on. Keep fingers, hair and loose "
                   "sleeves clear of the spinning part. The coil gets hot "
                   "within a minute, so switch off between tries and let "
                   "it cool. Use only the low-voltage supply your teacher "
                   "gives you.",

    "convention_note": "The bench is a teaching model. The coil is drawn face "
                       "on and frozen in the horizontal position, where the "
                       "turning effect is at its largest; a real coil's "
                       "turning effect falls to nothing twice per turn as it "
                       "passes upright, which is why real motors use several "
                       "coils rather than one. The turning effect shown is a "
                       "relative figure with the largest setting here set to "
                       "100, and it is taken as rising in proportion to the "
                       "current; no value in newtons or newton metres is "
                       "given, because the equation for the force on a "
                       "conductor is beyond this stage. The magnets are "
                       "treated as producing the same field whichever way "
                       "round they are, the friction at the axle is treated "
                       "as one fixed amount, and the coil is treated as one "
                       "turn. A real motor without a split ring does not stop "
                       "dead at the half turn but rocks to a halt over "
                       "several swings.",

    "ws": ["analysis"],
}
