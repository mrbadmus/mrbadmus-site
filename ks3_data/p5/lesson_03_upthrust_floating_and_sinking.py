"""P5 L3 — Upthrust, floating and sinking (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p5/p5-03-upthrust-floating-and-sinking.dc.html`.

Her page wins outright. The beach ball, the five blocks, the two-panel
beam, both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · A BEAM, NOT A TRIANGLE ──────────────────────────────

`left over = weight − upthrust` is a DIFFERENCE between two opposed
forces. Nothing is multiplied, so a triangle would encode a relationship
that does not exist. Design draws two panels to one scale — floating,
equal; sinking, with a leftover — and the block says `R = W − U`.

⚖️ **NO COVER BUTTONS.** Design's flag 0a: a balance has nothing to
cover. Covering one of two opposed arrows asks nothing.

── ⚖️ RULED · EVERY BLOCK IS ONE LITRE, AND THAT IS THE CONTROL ──────

The commit gate asks which of pine and steel gets the bigger upthrust,
and the answer is that they get the SAME — because each pushes aside one
litre. A bench whose blocks differed in volume could not ask the
question. `r_float_tank` requires floaters AND sinkers in the deck, or
the verdict tile is a constant.

── ⚖️ THE FLOATING FRACTIONS FALL OUT OF THE WEIGHTS, AND THEY ARE REAL

Ice at 0.92 kg per litre floats with 92 per cent under, which is the real
figure and is why an iceberg shows so little. Cork sits at 24 per cent,
pine at 50. Nothing is fudged: the fraction is `weight ÷ litre`.

── ⚖️ RULED · A SINKER STILL GETS ITS FULL UPTHRUST ──────────────────

`PRESS-10` is *only things that float get upthrust*, and the tile that
kills it is the spring-balance reading — weight minus upthrust — which
is visibly less than the weight in air. Design's own note: *"a heavy rock
is easier to lift while it is still under the water and suddenly feels
heavier as it breaks the surface."*

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-bench · s-formula · s-ladder

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    PRESS-09  heavy things sink and light things float
    PRESS-10  only things that float get upthrust
    PRESS-11  upthrust depends on how heavy the object is
    PRESS-12  being hollow is what makes something float

`PRESS-10` has no `elicited_by`: nothing asks the student to commit to
it, and it is confronted by the bench's balance-reading tile and by the
second quote. `PRESS-12` is not in Design's table — it arrived with rung
2's fourth option, whose correction is that *a hollow object full of
water sinks*, and it is separate from `PRESS-09`: a student can have
given up "heavy sinks" and still think hollowness is the rule.
"""

LESSON = {
    "slug":  "upthrust-floating-and-sinking",
    "title": "Upthrust, floating and sinking",
    "discipline": "physics",
    "unit": "Pressure",
    "family": "MODEL",

    "covers": ["KS3.P.PRES.02b"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["pressure-in-liquids"],
    "assumes": [],
    "references": ["balanced-and-unbalanced", "pressure-force-over-area"],
    "ks4_links": [],

    "meta_description": "A steel bolt sinks and a steel ship floats. Hold "
                        "five one-litre blocks under the water and find the "
                        "force that decides which is which.",

    "big_question": "Drop a steel bolt in a bucket and it goes straight to "
                    "the bottom. A steel ship the length of a street floats. "
                    "Same steel.",

    "rail": [
        {"anchor": "s-hook",    "short": "BALL",
         "label": "The beach ball",        "done_when": "committed"},
        {"anchor": "s-bench",   "short": "TANK",
         "label": "Five blocks, one tank", "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "The beam and five steps",
         "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Push a beach ball under and it fights you.",
        "prompt": "Hold one under the surface of a pool. You can feel the "
                  "water shoving it back up the whole time, and the further "
                  "under you push it the harder the shove gets. Let go and "
                  "it leaves the water.",
        "commit": "Where does that upward shove come from?",
        "options": [
            # ⊕ PHASE 3, 25 Aug 2026 — HER four options. These had
            # been invented: her prompt was ported and her answers were
            # not, which the HTML comparison could not see because a
            # `.dc.html` renders them from `{{ opt.text }}`.
            "The water is trying to get out of the way",
            "A floating object has no weight, so nothing holds it down and "
            "it simply stays at the top",
            "The water presses harder on the bottom of the ball than on the "
            "top, and the difference pushes up",
            "The air inside makes it rise on its own",
        ],
        "answer": 2,
        "reveal": "It comes from the pressure being different at different "
                  "depths. The bottom of the ball is deeper than the top, so "
                  "the water pushes <em>up</em> on the bottom harder than it "
                  "pushes <em>down</em> on the top. Those two pushes do not "
                  "cancel, and what is left over is a force upwards. It has "
                  "a name: <strong>upthrust</strong>.",
    },

    "misconceptions": [
        {"id": "PRESS-09",
         "statement": "Heavy things sink and light things float.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "PRESS-10",
         "statement": "Only things that float get upthrust.",
         "confronted_by": "s-think"},
        {"id": "PRESS-11",
         "statement": "Upthrust depends on how heavy the object is.",
         "elicited_by": "tank",
         "confronted_by": "tank"},
        {"id": "PRESS-12",
         "statement": "Being hollow is what makes something float.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Upthrust</strong> is the upward force a liquid or "
                 "gas exerts on anything in it, and it exists because "
                 "pressure increases with depth. It is equal to the weight "
                 "of the liquid the object pushes out of the way. An object "
                 "<strong>floats</strong> when it can push aside a weight of "
                 "liquid equal to its own weight, so that upthrust and "
                 "weight balance; it <strong>sinks</strong> when even fully "
                 "under it cannot push aside that much, so the weight wins."},

        # ── #s-bench · five blocks, one tank ───────────────────────────
        {"type": "float-tank",
         "id": "tank",
         "anchor": "s-bench",
         "eyebrow": "At the bench · five blocks, one tank",
         "heading": "Every block is one litre. Only the weight changes.",
         "progress": "Change a control to begin",
         "lead": "One litre of water weighs {litre}, so a block pushed fully "
                 "under can never get more than that much upthrust. Pick a "
                 "block. Then try holding it right under.",
         "litre_n": 10,
         "g": 10,
         "w_arrow": 120,
         "surface_y": 200,
         "box_px": 120,
         "start_block": 1,
         "block_label": "The block",
         "hold_label": "Your hand",
         "hold_off": "Hold it right under",
         "hold_on": "Let it go",
         "gate": {
             "prompt": "Commit first. Two one-litre blocks, one of pine and "
                       "one of steel, are both held completely under the "
                       "water. Which gets the bigger upthrust?",
             "options": [
                 "The steel, because it is heavier and presses into the "
                 "water harder",
                 "The same on both — each pushes aside one litre of water",
                 "The pine, because it is trying to float",
                 "The steel, because it sinks deeper and pressure grows with "
                 "depth",
             ],
             "answer": 1,
         },
         "blocks": [
             {"id": "cork", "label": "Cork", "name": "cork", "mass": 0.24},
             {"id": "pine", "label": "Pine", "name": "pine", "mass": 0.5},
             {"id": "ice", "label": "Ice", "name": "ice", "mass": 0.92},
             {"id": "alu", "label": "Aluminium", "name": "aluminium",
              "mass": 2.7},
             {"id": "steel", "label": "Steel", "name": "steel", "mass": 7.9},
         ],
         "branches": {
             "floating": "Left alone, the {name} settles with {pct} of it "
                         "under the surface. That is exactly far enough down "
                         "to push aside {weight} of water, which matches its "
                         "own {weight} — upthrust and weight are equal and "
                         "nothing is left over. It is not that the water "
                         "stopped pushing; it is that it pushes exactly "
                         "enough.",
             "held_under": "Held right under, the {name} pushes aside a full "
                           "litre, so the upthrust jumps to {up} against a "
                           "weight of only {weight}. That leaves {over} "
                           "pushing upwards, and it is the force you can "
                           "feel in your hand. Let go and it rises until "
                           "only {restpct} of it is under again.",
             "sinking": "Fully under, the {name} pushes aside one litre of "
                        "water, so it gets the same {up} of upthrust as "
                        "everything else here — and against a weight of "
                        "{weight} that is nowhere near enough. {over} is "
                        "left over, downwards, so it sinks. The upthrust has "
                        "not vanished, though: on a spring balance it would "
                        "read {reading} instead of {weight}.",
         },
         "readouts": [
             {"id": "weight", "label": "Weight in air", "sub": True},
             {"id": "up", "label": "Upthrust now", "sub": True},
             {"id": "reading", "label": "On a spring balance in the water"},
             {"id": "verdict", "label": "What it does"},
         ]},

        {"type": "formula",
         "id": "upthrust-rule",
         "eyebrow": "The relationship · a beam, not a triangle",
         "statement": "It floats when the upthrust equals the weight",
         "support": [
             "R = W − U",
             "Two arrows the same length balance.",
             "The longer one wins, and the leftover is what moves it.",
         ],
         "figure": {
             "art": "p5-opposed-beam",
             "aria_label": "Two force diagrams to one scale. On the left a "
                           "floating pine block: upthrust 5 newtons up, "
                           "weight 5 newtons down, equal arrows, nothing "
                           "left over. On the right a sinking aluminium "
                           "block: upthrust 10 newtons up, weight 27 newtons "
                           "down, leaving 17 newtons downwards.",
             "scale": 8.0,
             "panels": [
                 {"up": 5, "weight": 5, "verdict_a": "EQUAL",
                  "verdict_b": "IT FLOATS"},
                 {"up": 10, "weight": 27},
             ],
         }},

        {"type": "worked-example", "id": "cfifa-upthrust-plain"},
        {"type": "worked-example", "id": "cfifa-upthrust-convert"},
        {"type": "check", "id": "your-turn-upthrust", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "upthrust-is-what-you-push-aside"},

        {"type": "misconception", "id": "think-heavy-sinks",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-upthrust-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A stone weighs 12 N in air. Hanging fully under water, "
                    "the spring balance reads 9 N. What is the upthrust?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "12 N stays 12 N · 9 N stays 9 N",
              "note": "Both readings come off the same spring balance in "
                      "newtons, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "upthrust = weight in air − reading in water",
              "note": "The balance loses exactly what the water is "
                      "supporting."},
             {"letter": "I", "label": "Insert",
              "line": "upthrust = 12 N − 9 N",
              "note": "Both readings come off the same spring balance."},
             {"letter": "F", "label": "Fine-tune",
              "line": "12 − 9 = 3",
              "note": "Newtons take away newtons, so the answer is in "
                      "newtons."},
             {"letter": "A", "label": "Answer",
              "line": "upthrust = 3 N upwards",
              "note": "Three newtons up — and the stone still sinks, "
                      "because 9 N is left over pulling down."},
         ]},

        {"id": "cfifa-upthrust-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A metal cube of mass 1.2 kg hangs from a balance. Fully "
                    "under water the balance reads 8.0 N. What is the "
                    "upthrust?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own block."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1.2 kg × 10 N/kg = 12 N",
              "note": "The subtraction needs two forces, and a mass is not a "
                      "force — weight in newtons is mass in kilograms × "
                      "10 N/kg."},
             {"letter": "F", "label": "Formula",
              "line": "upthrust = weight in air − reading in water",
              "note": "The balance loses exactly what the water is "
                      "supporting."},
             {"letter": "I", "label": "Insert",
              "line": "upthrust = 12 N − 8.0 N",
              "note": "The converted weight goes in. The 1.2 kg never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "12 − 8.0 = 4",
              "note": "Newtons take away newtons, so the answer is in "
                      "newtons."},
             {"letter": "A", "label": "Answer",
              "line": "upthrust = 4 N upwards",
              "note": "Subtract 8.0 from 1.2 and the upthrust comes out "
                      "negative, which no upthrust ever is."},
         ]},

        {"id": "your-turn-upthrust",
         "kind": "p5-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "rest": {"name": "pine", "weight": "5 N", "up": "5 N",
                  "wnum": 5, "unum": 5, "onum": 0,
                  "answer": "nothing left over — it floats",
                  "finenote": "They cancel exactly, which is what floating "
                              "is.",
                  "answernote": "Upthrust and weight are equal, so nothing "
                                "is left over."},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your block: {name}, {weight}, with {up} of upthrust "
                      "on it.",
              "lead": "Write all five lines before you check. The numbers "
                      "are the ones your own tank is showing.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{weight} stays {weight} · {up} stays {up}",
                   "note": "Both are already forces in newtons, so there is "
                           "nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "left over = weight − upthrust",
                   "note": "A difference between two opposite forces, so a "
                           "beam rather than a triangle."},
                  {"letter": "I", "label": "Insert",
                   "line": "left over = {weight} − {up}",
                   "note": "Both figures come off the bench above."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{wnum} − {unum} = {onum}",
                   "note": "{finenote}"},
                  {"letter": "A", "label": "Answer",
                   "line": "{answer}",
                   "note": "{answernote}"},
              ],
              "close": "The five lines give {answer}, and the two arrows on "
                       "the bench are drawn to match."},
             {"id": "q2", "tab": "Question 2",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question. A different
              # one with different numbers had been written here;
              # hers lives in her page's JS, which the HTML
              # comparison could not see.
              "head": "A sinker of mass 0.60 kg hangs from a balance. Fully "
                      "under water the balance reads 4.5 N. What is the "
                      "upthrust?",
              "lead": "This one needs the Convert line to do some "
                      "work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "0.60 kg × 10 N/kg = 6.0 N",
                   "note": "A mass is not a force. Weight in newtons is "
                           "mass in kilograms × 10 N/kg."},
                  {"letter": "F", "label": "Formula",
                   "line": "upthrust = weight in air − reading in water",
                   "note": "The balance loses exactly what the water is "
                           "supporting."},
                  {"letter": "I", "label": "Insert",
                   "line": "upthrust = 6.0 N − 4.5 N",
                   "note": "The converted weight goes in. The 0.60 kg never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "6.0 − 4.5 = 1.5",
                   "note": "Newtons take away newtons, so the answer is in "
                           "newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "upthrust = 1.5 N upwards",
                   "note": "Subtract 4.5 from 0.60 and the upthrust comes "
                           "out negative."},
              ],
              "close": "The five lines give 1.5 N upwards. The whole "
                       "question turned on the first one."},
         ]},

        {"id": "think-heavy-sinks",
         "kind": "predict",
         "demand": "explain",
         "targets": "PRESS-09",
         "statements": [
             {"quote": "Heavy things sink and light things float.",
              "targets": "PRESS-09",
              "body": [
                  "A cargo ship weighs two hundred million newtons and "
                  "floats; a steel bolt weighs half a newton and sinks. "
                  "<strong>Weight alone decides nothing.</strong> What "
                  "decides it is the weight of the object compared with the "
                  "weight of water it can push out of the way — and a hull "
                  "shaped like a hull pushes aside thousands of tonnes of "
                  "sea, while a bolt can only push aside a bolt's worth. "
                  "Squash that same ship into a solid cube and it goes "
                  "straight down, because now it pushes aside almost "
                  "nothing.",
              ]},
             {"quote": "Only things that float get upthrust.",
              "targets": "PRESS-10",
              "body": [
                  "Everything in a liquid gets upthrust, sinkers included. "
                  "Hang a stone from a spring balance and lower it into "
                  "water: the reading drops, and <strong>the amount it drops "
                  "by <em>is</em> the upthrust.</strong> The stone still "
                  "sinks, because the upthrust is not enough to match its "
                  "weight — but it is definitely there, which is why a "
                  "heavy rock is easier to lift while it is still under the "
                  "water and suddenly feels heavier as it breaks the "
                  "surface.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "upthrust-is-what-you-push-aside",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Upthrust is the upward force from a liquid or gas, and it "
                 "equals the weight of what the object pushes out of the "
                 "way. It floats when the upthrust can match its weight, and "
                 "sinks when even fully under it cannot."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 1.
    "ladder": {
        "recall": {
            "q": "A metal cube weighs 45 N in air. Hanging completely under "
                 "water, the spring balance reads 37 N. What is the upthrust "
                 "on it?",
            "options": [
                "8 N",
                "82 N — add the two readings",
                "8 Pa — the water is pressing on it, so the answer is a "
                "pressure",
                "1.2 — divide 45 by 37",
            ],
            "answer": 0,
            "feedback": {
                1: "Adding them makes a force bigger than the cube’s own "
                   "weight. The water takes some of the weight off the "
                   "balance, so the two are subtracted.",
                2: "The arithmetic is right and the unit is wrong. Upthrust "
                   "is a force, measured in newtons; it is caused by a "
                   "pressure difference but it is not a pressure.",
                3: "That is a ratio, not a force, and it has no unit. The "
                   "upthrust is the difference between the two readings.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A steel bolt sinks. A steel ship floats. Which statement "
                 "explains it?",
            "options": [
                "The ship is lighter than the bolt, so the water can hold it "
                "up, while the bolt is too heavy for the same water to "
                "support and goes straight to the bottom.",
                "The hull pushes aside a weight of water equal to the whole "
                "ship’s weight; the bolt can only push aside its own small "
                "volume, which weighs far less than it does.",
                "Steel floats when there is enough of it, because a bigger "
                "object spreads its weight over more water and the water "
                "takes it more easily.",
                "The ship floats because it is hollow, and anything with air "
                "sealed inside it will always float however it is loaded.",
            ],
            "answer": 1,
            "feedback": {
                0: "The ship outweighs the bolt hundreds of millions of "
                   "times over. Weight alone is not what decides it.",
                2: "A solid block of the same steel sinks however large it "
                   "is. It is the shape, and the water it pushes aside, that "
                   "changes the answer.",
                3: "The verdict is right and the rule is wrong. A hollow "
                   "object full of water sinks — being hollow only helps "
                   "because it lets the hull push aside more water than it "
                   "weighs.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "The steel from a ship is melted down and cast into one "
                 "solid block, which sinks. Explain why the ship floated and "
                 "the block does not, using upthrust and the water pushed "
                 "out of the way.",
            "field_label": "Your explanation",
            "placeholder": "The weight of the steel has not…",
            "success": [
                "Says the weight of steel is the same in both cases.",
                "Says the upthrust equals the weight of water pushed out of "
                "the way.",
                "Says the hull shape pushes aside a large volume, and so a "
                "large weight, of water.",
                "Says the solid block pushes aside only a small volume of "
                "water.",
                "Concludes that the hull’s upthrust could match its "
                "weight and the block’s cannot, so the block has a "
                "leftover force downwards.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A submarine dives by letting sea water into its ballast "
                 "tanks and surfaces by blowing it out with compressed air. "
                 "Explain both, and say what stays the same throughout.",
            "field_label": "Your answer",
            "placeholder": "Letting water in makes the submarine…",
            "success": [
                "Says flooding the tanks increases the submarine’s "
                "weight.",
                "Says the upthrust stays the same, because the shape and "
                "volume have not changed.",
                "Says the weight then exceeds the upthrust, leaving a force "
                "downwards, so it dives.",
                "Says blowing the water out lowers the weight below the "
                "upthrust, so it rises.",
                "Says hovering at one depth means weight and upthrust are "
                "balanced, with nothing left over.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Because pressure grows with depth, a liquid pushes up on "
                "the bottom of an object harder than it pushes down on the "
                "top, and the difference is upthrust. Upthrust equals the "
                "weight of the liquid pushed out of the way. Floating is the "
                "balanced case: upthrust equals weight, nothing is left "
                "over. Sinking is the unbalanced one: even fully submerged "
                "the upthrust is smaller than the weight, and the leftover "
                "force takes it down.",

    "stretch": [
        {"id": "the-submarine-trick",
         "type": "explainer",
         "text": "A submarine uses the one thing the blocks on the bench "
                 "could not: <strong>it changes its own weight without "
                 "changing its shape.</strong> Flood the ballast tanks and "
                 "the weight goes up while the upthrust stays exactly the "
                 "same, so it dives; blow the water out with compressed air "
                 "and the weight drops below the upthrust, so it rises. "
                 "Hovering at a set depth means matching the two to within a "
                 "few newtons, which is why submarines trim constantly and "
                 "why a change in the saltiness of the water is something a "
                 "crew has to notice."},
        {"id": "the-plimsoll-line",
         "type": "explainer",
         "text": "The same balance is written on the side of every merchant "
                 "ship as the Plimsoll line — a set of marks showing how "
                 "deep the hull may legally sit in fresh water, in salt "
                 "water, in summer and in winter, because each of those "
                 "changes the weight of water the hull pushes aside. Gases "
                 "do it too: a hot-air balloon floats in air for exactly the "
                 "reason a cork floats in water, since hot air inside the "
                 "envelope weighs less than the cold air it pushes out of "
                 "the way. And the whole idea is old. Archimedes worked out "
                 "the rule about the weight of the fluid displaced more than "
                 "two thousand years ago, and shipbuilders still use it "
                 "unchanged."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "upthrust",
         "definition": "The upward force from a liquid or gas on anything in "
                       "it. Equal to the weight of what the object pushes "
                       "out of the way."},
        {"term": "displaced",
         "definition": "Pushed out of the way. The weight of the liquid "
                       "displaced is the upthrust."},
        {"term": "floats",
         "definition": "Settles at a depth where the upthrust matches the "
                       "weight, so nothing is left over."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got something you cannot decide will float or sink?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Upthrust from the pressure difference across a submerged "
                   "object, density as the test for floating, and "
                   "Archimedes' principle written as an equation.",

    "convention_note": "The tank is a teaching model. Every block is exactly "
                       "one litre and water is taken as 1000 kg per cubic "
                       "metre, so one litre of water weighs 10 N with weight "
                       "as mass × 10 N/kg; the block densities are typical "
                       "values and cork in particular varies a great deal. "
                       "The weight arrow is drawn at a fixed length and the "
                       "upthrust arrow in proportion to it, so the two can "
                       "be compared with each other but not measured off the "
                       "page; ratios beyond about two and a half are clipped "
                       "to fit. How much of a floating block sits below the "
                       "surface is calculated from the weights alone, "
                       "ignoring the shape of the block and the skin of the "
                       "water.",

    "ws": [],
}
