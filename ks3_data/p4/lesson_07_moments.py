"""P4 L7 — Moments: the turning effect (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p4/p4-07-moments.dc.html`.

Her page wins outright. The door and the hinge, the spanner and the tight
nut, both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · THE FIRST PRODUCT IN THE UNIT, AND THE ONLY TRIANGLE ─

`moment = force × distance from the pivot` is a GENUINE PRODUCT, so
`A = B × C` holds and the triangle encodes a relationship that exists.
Moment sits above the bar; force and distance sit below it, multiplied.

**This is the only triangle in nine lessons.** Four of the first six
relationships in P4 are additive — a difference, an equality, a leftover
— and Design's own note asks a reviewer to check that this is the first
product a student meets here. Checked against the arithmetic, not against
the habit: `p4-02` is a subtraction, `p4-03` is an equality, `p4-08` is a
ratio read off a straight line, and none of the three gets a triangle.

── ⚖️ RULED · "AT RIGHT ANGLES" IS LOAD-BEARING AND IS NOT DROPPED ───

The lesson handles only the perpendicular case. The symbol key says *force,
at right angles to the handle*; the bench lead says *at right angles to the
handle*; rung 1 says *at right angles*. Dropping the phrase makes the
formula WRONG rather than simplified, because `M = F × d` is false for a
force at any other angle. `r_spanner_rig` refuses a payload with no lead
for exactly that reason.

── ⚖️ RULED · THE NUT'S 12 N m IS A TEACHING THRESHOLD ───────────────

It is fixed so that failure is a state a student can reach, and the foot
line says so. A real fitting depends on how it was tightened, on corrosion
and on whether it has ever been undone. `r_spanner_rig` asserts that at
least one arm CAN clear it at full pull and at least one CANNOT, because a
threshold nothing reaches is a dead state and a threshold everything
clears is half a bench.

── ⚖️ RULED · TWO SCALES, DECLARED SEPARATELY ────────────────────────

The handle is drawn at 1400 px per metre and the pull at 0.9 px per
newton. They are different quantities — a length and a force — so one
scale for both would be meaningless rather than more honest. The foot line
declares the split.

── ⚖️ THE WORD "MOMENT" ARRIVES HERE, FROM NOTHING ───────────────────

`b2-04 biomechanics-forces-in-the-body` teaches *turning effect = force ×
distance from the joint* and deliberately does not use the word. This
lesson therefore introduces the word, the pivot and the relationship from
first principles, and carries the B2 lesson as a `references` edge and as
a link inside *Going further* — phrased as an offer, never as a sentence
assuming it has happened.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-bench · s-formula · s-ladder

⚠️ **MRB-208** — the `s-formula` id goes on the attempt panel.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    FORCE-36  a longer spanner means you are pulling harder
    FORCE-37  the distance is measured from where you are standing
    FORCE-38  a moment is a force, so it is measured in newtons
    FORCE-39  the distance only decides which way it turns, not how much
"""

LESSON = {
    "slug":  "moments",
    "title": "Moments: the turning effect",
    "discipline": "physics",
    "unit": "Forces",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.FORCES.03"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["air-and-water-resistance"],
    "assumes": [],
    "references": ["biomechanics-forces-in-the-body", "what-a-force-is"],
    "ks4_links": [],

    "meta_description": "Push a door at the handle and it swings. Push just "
                        "as hard beside the hinge and it hardly moves. Same "
                        "door, same push — and the difference is a "
                        "multiplication.",

    "big_question": "Push a door open at the handle and it swings. Push just "
                    "as hard right beside the hinge and it hardly moves. "
                    "Same door, same push, different result.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The door and the hinge", "done_when": "committed"},
        {"anchor": "s-bench",  "short": "NUT",
         "label": "Spanner and nut",        "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Triangle and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",         "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The same push, ten centimetres from the hinge.",
        "prompt": "Try it on the next door you go through. Push at the "
                  "handle with one finger and it opens easily. Then push "
                  "with the same finger a hand's width from the hinge, and "
                  "lean.",
        "commit": "Why is the same force so much less use near the hinge?",
        "options": [
            "You push harder at the handle without noticing, because leaning "
            "is easier there",
            "The turning effect depends on the distance from the pivot as "
            "well as the force",
            "The door is heavier near the hinge, so there is more of it to "
            "shift there",
            "The hinge takes the force away, so a push near it never reaches "
            "the door",
        ],
        "answer": 1,
        "reveal": "Turning is not decided by the force alone. It is decided "
                  "by the force <em>and</em> how far from the pivot the "
                  "force acts — and those two multiply together. The hinge "
                  "is the pivot. Ten centimetres out you have a tenth of the "
                  "distance, so a tenth of the turning effect. That product "
                  "has a name: the <strong>moment</strong>.",
    },

    "misconceptions": [
        {"id": "FORCE-36",
         "statement": "A longer spanner means you are pulling harder.",
         "elicited_by": "spanner",
         "confronted_by": "s-think"},
        {"id": "FORCE-37",
         "statement": "The distance is measured from where you are standing.",
         "confronted_by": "s-think"},
        {"id": "FORCE-38",
         "statement": "A moment is a force, so it is measured in newtons.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
        {"id": "FORCE-39",
         "statement": "The distance from the pivot only decides which way "
                      "something turns, not how much.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A <strong>pivot</strong> is the fixed point something turns "
                 "about — a hinge, a nut, a bolt through a seesaw. The "
                 "<strong>moment</strong> of a force is its turning effect "
                 "about that pivot, and it depends on two things: the size "
                 "of the force, and its distance from the pivot. Moments are "
                 "measured in <strong>newton metres, N m</strong>."},

        # ── #s-bench · spanner and a tight nut ─────────────────────────
        {"type": "spanner-rig",
         "id": "spanner",
         "anchor": "s-bench",
         "eyebrow": "At the bench · spanner and a tight nut",
         "heading": "One nut. Two ways to shift it.",
         "progress": "Change a control to begin",
         "lead": "This nut is done up tight: it needs a moment of {need} "
                 "before it will move at all. Choose a spanner. Choose how "
                 "hard you pull, at right angles to the handle.",
         "need": 12,
         "arm_scale": 1400,
         "f_scale": 0.9,
         "arms": [0.05, 0.10, 0.20, 0.30],
         "start_arm": 0.10,
         "arm_label": "Distance from the pivot",
         "force": {"label": "Your pull", "min": 10, "max": 100,
                   "step": 10, "start": 50},
         "gate": {
             "prompt": "Commit first. You swap a 0.10 m spanner for a 0.20 m "
                       "one and pull just as hard. What happens to the "
                       "turning effect?",
             "options": [
                 "It doubles — twice the distance from the pivot",
                 "It stays the same — you are pulling just as hard",
                 "It halves — the pull is spread over a longer handle",
                 "It quadruples — distance counts twice over",
             ],
             "answer": 0,
         },
         # ⚖️ BOTH BRANCHES NAME BOTH ROUTES TO THE THRESHOLD, WITH LIVE
         # FIGURES. That is the product being taught rather than a number
         # being reported.
         "branches": {
             "turns": "That is {moment}, and the nut needs {need}, so it "
                      "moves. Notice what would also have worked: the same "
                      "{force} further out, or as little as {needf} at this "
                      "distance. Both routes reach the same {need}, because "
                      "it is the product that matters.",
             "stuck": "{force} at {arm} gives {moment}, which is short of "
                      "the {need} this nut needs, so nothing happens at all. "
                      "Two ways out: pull with {needf} at this distance, or "
                      "keep your {force} and get {needarm} from the pivot.",
             "stuck_far": "{force} at {arm} gives {moment}, which is short "
                          "of the {need} this nut needs, so nothing happens "
                          "at all. Two ways out: pull with {needf} at this "
                          "distance, or keep your {force} and get {needarm} "
                          "from the pivot — further than any spanner here, "
                          "which is what a length of pipe over the handle is "
                          "for.",
         },
         "readouts": [
             {"id": "force", "label": "Your pull"},
             {"id": "arm", "label": "Distance from pivot"},
             {"id": "moment", "label": "Moment"},
             {"id": "verdict", "label": "The nut"},
         ]},

        {"type": "formula",
         "id": "moment-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Moment = force × distance from the pivot",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. Moment M sits above a "
                           "dividing line; force F and distance d sit below "
                           "it, multiplied together. Covering one letter "
                           "leaves the way to work it out.",
             # ⚠️ NO PROSE PER COVER. Design's 19 Aug re-specification bans
             # the per-cover sentence: the block carries the ARRANGEMENT in
             # display type and one fixed rule line, and the units ride in
             # the symbol key rather than in a mono list.
             "order": ["top", "left", "right"],
             "covered": "top",
             "top":   {"label": "M", "button": "Cover M",
                       "result": "M = F × d", "text": ""},
             "left":  {"label": "F", "button": "Cover F",
                       "result": "F = M ÷ d", "text": ""},
             "right": {"label": "d", "button": "Cover d",
                       "result": "d = M ÷ F", "text": ""},
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["M · moment · N m",
                           "F · force, at right angles to the handle · N",
                           "d · distance from the pivot · m"],
             },
         }},

        {"type": "worked-example", "id": "cfifa-moment-plain"},
        {"type": "worked-example", "id": "cfifa-moment-convert"},
        {"type": "check", "id": "your-turn-moment", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "moment-is-force-times-distance"},

        {"type": "misconception", "id": "think-longer-spanner",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-moment-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A spanner is gripped 0.25 m from the nut and pulled "
                    "with 40 N. What is the moment?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "40 N stays 40 N · 0.25 m stays 0.25 m",
              "note": "The force is already in newtons and the distance "
                      "already in metres, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "moment = force × distance from the pivot",
              "note": "Two quantities multiplied, which is what a triangle "
                      "means."},
             {"letter": "I", "label": "Insert",
              "line": "moment = 40 N × 0.25 m",
              "note": "The 0.25 m is measured from the nut, not along your "
                      "arm."},
             {"letter": "F", "label": "Fine-tune",
              "line": "40 × 0.25 = 10",
              "note": "Newtons times metres leaves newton metres."},
             {"letter": "A", "label": "Answer",
              "line": "moment = 10 N m",
              "note": "Ten newton metres, turning the nut about the pivot."},
         ]},

        {"id": "cfifa-moment-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A door handle is pushed with 12 N, 80 cm from the "
                    "hinge. What is the moment?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own spanner."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "80 cm ÷ 100 = 0.80 m",
              "note": "A newton metre needs the distance in metres, and a "
                      "centimetre is a hundredth of one."},
             {"letter": "F", "label": "Formula",
              "line": "moment = force × distance from the pivot",
              "note": "The hinge is the pivot."},
             {"letter": "I", "label": "Insert",
              "line": "moment = 12 N × 0.80 m",
              "note": "The converted distance goes in. The 80 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "12 × 0.80 = 9.6",
              "note": "Newtons times metres leaves newton metres."},
             {"letter": "A", "label": "Answer",
              "line": "moment = 9.6 N m",
              "note": "Insert 80 instead of 0.80 and the answer comes out a "
                      "hundred times too big."},
         ]},

        {"id": "your-turn-moment",
         "kind": "p4-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         # The spanner opens at 50 N on the 0.10 m arm — 5 N m, short of
         # the nut's 12 N m, so the resting note is the "it holds" one.
         "rest": {"force": "50 N", "arm": "0.10 m", "moment": "5 N m",
                  "fnum": 50, "armnum": "0.10", "mnum": 5,
                  "verdictnote": "Less than the 12 N m the nut needs, so it "
                                 "holds."},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your spanner: {force} at {arm} from the pivot.",
              "lead": "Write all five lines before you check. The numbers "
                      "are the ones your own bench is showing.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{force} stays {force} · {arm} stays {arm}",
                   "note": "The force is already in newtons and the distance "
                           "already in metres, so there is nothing to "
                           "convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "moment = force × distance from the pivot",
                   "note": "A product, so the triangle applies."},
                  {"letter": "I", "label": "Insert",
                   "line": "moment = {force} × {arm}",
                   "note": "Both values come straight off the bench above."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{fnum} × {armnum} = {mnum}",
                   "note": "Newtons times metres leaves newton metres."},
                  {"letter": "A", "label": "Answer",
                   "line": "moment = {moment}",
                   "note": "{verdictnote}"},
              ],
              "close": "The five lines give {moment}, and the handle on the "
                       "bench is drawn {arm} long to match."},
             {"id": "q2", "tab": "Question 2",
              "head": "A nut is turned with 25 N applied 15 cm from the "
                      "pivot. What is the moment?",
              "lead": "This one needs the Convert line to do some work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "15 cm ÷ 100 = 0.15 m",
                   "note": "A newton metre needs the distance in metres, so "
                           "divide the centimetres by 100."},
                  {"letter": "F", "label": "Formula",
                   "line": "moment = force × distance from the pivot",
                   "note": "Two quantities multiplied."},
                  {"letter": "I", "label": "Insert",
                   "line": "moment = 25 N × 0.15 m",
                   "note": "The converted distance goes in. The 15 never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "25 × 0.15 = 3.75",
                   "note": "Newtons times metres leaves newton metres."},
                  {"letter": "A", "label": "Answer",
                   "line": "moment = 3.75 N m",
                   "note": "Insert 15 instead of 0.15 and the answer comes "
                           "out 375 N m."},
              ],
              "close": "The five lines give 3.75 N m. The whole question "
                       "turned on the first one."},
         ]},

        {"id": "think-longer-spanner",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-36",
         "statements": [
             {"quote": "A longer spanner means you are pulling harder.",
              "targets": "FORCE-36",
              "body": [
                  "It does not, and the spring balance proves it: put one on "
                  "the handle and the reading is the same 50 N whether the "
                  "handle is short or long. What changes is what those 50 N "
                  "achieve. <strong>A moment is not a force and is not "
                  "measured in newtons</strong> — it is a force multiplied "
                  "by a distance, measured in newton metres, and a long "
                  "handle buys you turning effect without buying you "
                  "strength. This is why the answer to a seized bolt is "
                  "never simply <em>pull harder</em>: put a length of pipe "
                  "over the spanner and the same arm shifts it.",
              ]},
             {"quote": "Measure the distance from where you are standing.",
              "targets": "FORCE-37",
              "body": [
                  "The distance in the formula is measured from the "
                  "<em>pivot</em>, and nowhere else. Not from the middle of "
                  "the object, not from your feet, not along your arm. On "
                  "the bench above, the pivot is the centre of the nut, so a "
                  "0.20 m spanner means the pull acts 0.20 m from that "
                  "centre. <strong>Get the pivot wrong and every answer that "
                  "follows is wrong</strong>, which is why identifying it is "
                  "the first thing to do in any turning problem — hinge, "
                  "nut, bolt, axle, or in the human body, the joint.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "moment-is-force-times-distance",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "The moment of a force is its turning effect about a pivot, "
                 "and it is the force in newtons multiplied by the distance "
                 "from the pivot in metres. Double the distance and you "
                 "double the turning effect for exactly the same pull."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 1.
    "ladder": {
        "recall": {
            "q": "A spanner is gripped 0.40 m from a bolt and pulled with "
                 "30 N at right angles. What is the moment?",
            "options": [
                "12 N m",
                "75 N m — divide the force by the distance",
                "12 N — a turning effect is a force, so it is in newtons",
                "30 N m — the moment is the force, and the distance only "
                "sets which way it turns",
            ],
            "answer": 0,
            "feedback": {
                1: "Dividing is what you do to find a distance or a force "
                   "from a known moment. To find the moment itself, the two "
                   "multiply.",
                2: "The arithmetic is right and the unit is wrong. A moment "
                   "is a force multiplied by a distance, so its unit is the "
                   "newton metre.",
                3: "The distance changes the size of the turning effect, not "
                   "just its direction. At 0.80 m the same 30 N would give "
                   "twice as much.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "Two people pull with exactly 50 N on the same stiff bolt. "
                 "One uses a 0.10 m spanner, the other a 0.40 m spanner. "
                 "Which statement is right?",
            "options": [
                "They give the same moment, because the moment is decided "
                "by how hard you pull, and the length of the handle only "
                "changes how comfortable it is.",
                "The long spanner gives 20 N m against 5 N m — four times "
                "the turning effect for the same pull.",
                "The short spanner gives more, because the force acts closer "
                "to the bolt.",
                "The long spanner gives more, because a longer spanner "
                "weighs more.",
            ],
            "answer": 1,
            "feedback": {
                0: "The moment is force × distance. Same force, four times "
                   "the distance, four times the moment.",
                2: "Closer to the pivot is weaker, not stronger — that is "
                   "the door-hinge test at the top of this lesson.",
                3: "The verdict is right and the reason is wrong. It would "
                   "still be four times the moment if the long spanner were "
                   "made of something lighter.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Door handles are always fitted at the edge furthest from "
                 "the hinges. Explain why, using the word pivot and the word "
                 "moment.",
            "field_label": "Your explanation",
            "placeholder": "The hinges are the…",
            "success": [
                "Says the hinge line is the pivot.",
                "Says the moment is the force multiplied by the distance "
                "from that pivot.",
                "Says the handle edge is the furthest point from the hinges.",
                "Says the same push therefore gives the largest possible "
                "moment.",
                "Says a handle near the hinges would need a much bigger "
                "force to open the same door.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A wheel nut on a car must be tightened to a moment of "
                 "110 N m. A driver can pull with about 250 N. Work out the "
                 "shortest spanner that would do the job, and explain why "
                 "the manufacturer supplies a long one rather than one of "
                 "exactly that length.",
            "field_label": "Your answer",
            "placeholder": "Rearranging the formula gives…",
            "success": [
                "Rearranges to distance = moment ÷ force.",
                "Works out 110 ÷ 250 = 0.44 m, and gives the unit as metres.",
                "Says a shorter spanner than that would need a bigger pull "
                "than 250 N.",
                "Says a longer spanner reaches the same 110 N m with a "
                "smaller force.",
                "Says something sensible about why that matters — most "
                "people cannot pull 250 N, or it is safer and more accurate "
                "than straining.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A moment is the turning effect of a force about a pivot, "
                "and it equals the force in newtons multiplied by its "
                "distance from the pivot in metres, giving newton metres. "
                "The same force gives a bigger moment further out, which is "
                "why handles, levers and spanners are long. A moment is not "
                "a force, and the distance is always measured from the "
                "pivot.",

    "stretch": [
        {"id": "two-moments-one-pivot",
         "type": "explainer",
         "text": "Once you can work out a moment, you can work out a "
                 "balance. On a seesaw there are two moments about the same "
                 "pivot, one turning it clockwise and one anticlockwise, and "
                 "it balances when the two are equal — <strong>not when the "
                 "two weights are equal</strong>. That is why a child of "
                 "300 N sitting 2 m out balances an adult of 600 N sitting "
                 "1 m out: both make 600 N m, and the seesaw does not care "
                 "which is which. The same arithmetic decides whether a "
                 "crane tips over, how far along a plank a builder can walk, "
                 "and where the counterweight goes on a tower crane, which "
                 "is a lump of concrete whose whole job is to make a moment "
                 "on the other side."},
        {"id": "levers-and-the-body",
         "type": "explainer",
         "text": "Levers are this idea used deliberately: put the pivot near "
                 "the load and you can lift something with far less force "
                 "than its weight, as long as you accept moving your end "
                 "much further. A crowbar, a wheelbarrow, a bottle opener "
                 "and a pair of scissors are all the same machine in "
                 "different clothes. Your own body is full of them too, "
                 "though it usually trades the other way — many muscles "
                 "pull very close to the joint, so they need a large force "
                 "to lift a small load, and buy speed and range of movement "
                 "with it instead. The biomechanics lesson in the skeleton "
                 "unit works through the turning effect at a joint, and is "
                 "the same relationship you have just met here."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "pivot",
         "definition": "The fixed point something turns about — a hinge, a "
                       "nut, a bolt, an axle, a joint. Every distance in the "
                       "formula is measured from it."},
        {"term": "moment",
         "definition": "The turning effect of a force about a pivot: force "
                       "in newtons × distance from the pivot in metres."},
        {"term": "newton metre",
         "definition": "The unit of a moment, written N m. Not a newton — "
                       "a moment is not a force."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a turning problem of your own — a door, a spanner, a "
                "seesaw?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Moments, the principle of moments for a balanced beam, "
                   "levers as force multipliers, and gears.",

    "convention_note": "The spanner bench is a teaching model. The nut is "
                       "given a fixed loosening moment of 12 N m so that "
                       "failure is something you can reach; a real fitting "
                       "depends on how it was tightened, on corrosion and on "
                       "whether it has ever been undone. The pull is taken "
                       "as acting at right angles to the handle, which is "
                       "the only case handled at this stage, and the handle "
                       "is drawn to scale while the force arrow uses a "
                       "separate scale.",

    "ws": [],
}
