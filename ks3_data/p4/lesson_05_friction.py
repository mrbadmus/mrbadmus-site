"""P4 L5 — Friction (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p4/p4-05-friction.dc.html`.

Her page wins outright. The stuck crate, the drag bench, the four rules,
the two columns and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA BLOCK, AND NONE IS OWED ───────────────────

Friction is qualitative in `FORCES.04`. The bench measures it in newtons
and sets two readings side by side; **no relationship was invented in
order to have something to put in a triangle.** The coefficient of
friction is not KS3 and does not appear.

── ⚖️ RULED · THE GRIP FIGURES AND THE ONE-FIFTH RULE ARE A MODEL ────

Each surface is given a fixed grip figure chosen to be typical, and the
break-away reading is modelled as one fifth more than the sliding reading.
The foot line declares both. Real surfaces vary with polish, dust, damp
and wear, and a real spring balance reading wanders as you pull — so
these are teaching numbers, and saying so is what keeps the bench honest
while still letting rule 3 be demonstrable.

⚠️ The smallest reading the bench can produce is `4 kg × 10 N/kg × 0.20 =
8 N`. There is no zero state to draw, which is why `r_drag_lane` refuses a
surface with no grip: *a surface with no friction is the misconception
this lesson confronts, not a state it draws.*

── ⚖️ RULED · THE SECOND SENTENCE IS ALWAYS PRESENT ──────────────────

Every bench state carries a surface branch AND a comparison against
another load on the same surface. A student is never left with a reading
whose only meaning is itself — which is what makes rule 3 (*it grows with
how hard they press*) something they have seen rather than been told.

── ⚠️ FOUR RAIL STOPS, AND `s-rules` TICKS ON THE GATE ───────────────

    s-hook · s-bench · s-rules · s-ladder

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    FORCE-28  starting something sliding and keeping it sliding need the
              same push
    FORCE-29  a smooth surface has no friction
    FORCE-30  friction only exists once something is moving
    FORCE-31  a steady speed means friction has been overcome

`FORCE-31` is not in Design's table. It arrived with rung 1's second
option — *"0 N: it is moving, so friction has been overcome"* — and it
is a `p4-03` idea meeting friction for the first time: the student has
accepted that balanced means no change and still reads "overcome" as
"gone". The correction says that if friction were 0 N the sledge would be
speeding up the whole time.
"""

LESSON = {
    "slug":  "friction",
    "title": "Friction",
    "discipline": "physics",
    "unit": "Forces",
    "family": "PROCESS",

    "covers": ["KS3.P.FORCES.04b"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 2}],
    "typical_year": 7,
    "typical_minutes": 60,

    "requires": ["what-forces-do-to-motion"],
    "assumes": [],
    "references": ["balanced-and-unbalanced", "what-a-force-is"],
    "ks4_links": [],

    "meta_description": "Nothing about a crate changes when you start "
                        "sliding it, so why is the first centimetre the "
                        "hardest part? Take two readings from every drag "
                        "test and find out.",

    "big_question": "Nothing about a crate changes when you start sliding "
                    "it. So why is the hardest part of the whole job the "
                    "first centimetre?",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The stuck crate",   "done_when": "committed"},
        {"anchor": "s-bench",  "short": "DRAG",
         "label": "Block and balance", "done_when": "gate_and_a_control"},
        {"anchor": "s-rules",  "short": "RULES",
         "label": "Four rules",        "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "It will not budge, and then suddenly it slides.",
        "prompt": "You lean on a full crate and push harder and harder. "
                  "Nothing. Then it gives, and once it is moving you can "
                  "keep it going with a much gentler push than the one that "
                  "started it.",
        "commit": "Why is starting it harder than keeping it going?",
        "options": [
            "The crate gets lighter once it is moving, so less push is needed "
            "to keep it going",
            "Friction is largest just before sliding starts, and drops once "
            "the surfaces are sliding",
            "Your push gets stronger as you lean into it, so the crate moves "
            "once you push hard enough",
            "The floor stops pushing back once the crate is moving, so "
            "nothing resists it",
        ],
        "answer": 1,
        "reveal": "Friction is a force between two surfaces that resists "
                  "them sliding across each other, and it is at its largest "
                  "just before the sliding starts. Left alone the two "
                  "surfaces settle into one another; once they are sliding "
                  "they never get the chance to settle again, so the "
                  "friction drops. <strong>The crate did not get lighter, "
                  "and your push did not get stronger.</strong>",
    },

    "misconceptions": [
        {"id": "FORCE-28",
         "statement": "Starting something sliding and keeping it sliding "
                      "need the same push.",
         "elicited_by": "s-hook",
         "confronted_by": "drag"},
        {"id": "FORCE-29",
         "statement": "A smooth surface has no friction.",
         "elicited_by": "drag",
         "confronted_by": "s-think"},
        {"id": "FORCE-30",
         "statement": "Friction only exists once something is moving.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "FORCE-31",
         "statement": "A steady speed means the friction has been overcome, "
                      "so there is none left.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Friction</strong> acts between two surfaces that "
                 "are touching, and it always acts against the sliding — "
                 "never with it. It is there before anything moves, which is "
                 "why a book stays put on a sloping desk lid, and it turns "
                 "movement into heat, which is why your hands warm up when "
                 "you rub them."},

        # ── #s-bench · block and spring balance ────────────────────────
        {"type": "drag-lane",
         "id": "drag",
         "anchor": "s-bench",
         "eyebrow": "At the bench · block and spring balance",
         "heading": "Two readings from every drag test",
         "progress": "Change a control to begin",
         "lead": "A spring balance is hooked to the block and pulled "
                 "horizontally. Take one reading at the instant it breaks "
                 "away, and a second while it slides steadily. Change the "
                 "surface. Change the load.",
         "g": 10,
         "scale": 3,
         "start_factor": 1.2,
         "start_surface": "boards",
         "start_mass": 6,
         "surface_label": "The surface underneath",
         "mass_label": "The load in the block",
         "band_anchor": "s-rules",
         "band_at": 1,
         "gate": {
             "prompt": "Commit first. The same block is dragged over carpet, "
                       "then over polished wood. What happens to the "
                       "reading?",
             "options": [
                 "It goes up — polished wood grips harder",
                 "It goes down — less friction between block and wood",
                 "It stays the same — the block has not changed",
                 "It drops to zero — polished wood has no friction",
             ],
             "answer": 1,
         },
         "masses": [4, 6, 8, 10],
         "surfaces": [
             {"id": "wood", "tab": "Polished wood", "grip": 0.20,
              "texture": "gloss",
              "note": "Polished wood gives the smallest readings on the "
                      "bench. The block still needs {slide} N to keep "
                      "sliding, so even a surface that looks slippery is "
                      "doing something — there is no such thing as a floor "
                      "with no friction at all."},
             {"id": "boards", "tab": "Bare floorboards", "grip": 0.35,
              "texture": "planks",
              "note": "Bare boards need {slide} N to keep the block moving, "
                      "roughly {ratio} times the polished-wood reading with "
                      "the same load. Nothing about the block changed. "
                      "Friction is a property of the pair of surfaces, not "
                      "of the block on its own."},
             {"id": "carpet", "tab": "Carpet", "grip": 0.55,
              "texture": "loops",
              "note": "Carpet pushes the sliding reading up to {slide} N. "
                      "The fibres bend and spring back as the block passes "
                      "over them, and every one of those bends takes "
                      "movement out of the block and leaves it as heat."},
             {"id": "rubber", "tab": "Rubber matting", "grip": 0.70,
              "texture": "grit",
              "note": "Rubber matting gives the biggest readings here — "
                      "{slide} N to keep sliding and {start} N to break "
                      "away. This is friction being useful: matting is laid "
                      "in doorways precisely because it is hard to slide "
                      "anything, including a foot, across it."},
         ],
         "compare": "Load it differently and both readings move together. At "
                    "{mass} kg the sliding reading is {slide} N; at {other} "
                    "kg on the same surface it is {otherslide} N. Pressing "
                    "the surfaces together harder gives more friction, and "
                    "the break-away reading stays about a fifth above the "
                    "sliding one whatever the load.",
         "readouts": [
             {"id": "weight", "label": "Weight of the block"},
             {"id": "start", "label": "To break it away"},
             {"id": "slide", "label": "To keep it sliding"},
             {"id": "gap", "label": "The gap"},
         ]},

        # ── #s-rules · four things friction always does ────────────────
        {"type": "force-band",
         "id": "four-rules",
         "anchor": "s-rules",
         "eyebrow": "Four things friction always does",
         "heading": "Every reading on the bench obeyed all four.",
         "panels": [
             {"num": "1", "name": "It acts against the sliding",
              "body": "Always the opposite way to the movement, or to the "
                      "movement that is about to happen. Friction never "
                      "pushes something along."},
             {"num": "2", "name": "It depends on both surfaces",
              "body": "Swap the floor and the reading changes even though "
                      "the block has not. Rough or smooth is a fact about "
                      "the pair, not about one of them."},
             {"num": "3", "name": "It grows with how hard they press",
              "body": "Load the block and every reading rises. On the bench, "
                      "doubling the weight doubled both readings."},
             {"num": "4", "name": "It turns movement into heat",
              "body": "Rub your hands. Feel a brake disc after a long hill. "
                      "The energy does not vanish — it leaves as heat, and "
                      "it is not coming back."},
         ],
         "close": "Friction is not a fault in the world to be designed out. "
                  "Half of it is the problem and half of it is the point: "
                  "the same force that wears out a brake pad is the force "
                  "that lets you walk, and a floor with no friction is a "
                  "floor nobody can stand up on.",
         "columns": [
             {"title": "Wanted here",
              "items": ["Shoes on a wet pavement",
                        "A brake pad on a wheel rim",
                        "A nail staying in a wall",
                        "A tyre turning a corner"]},
             {"title": "Not wanted here",
              "items": ["A bicycle chain",
                        "A drawer that sticks",
                        "A hip joint",
                        "A piston in an engine"]},
         ]},

        {"type": "key-fact", "ref": "friction-against-the-sliding"},

        {"type": "misconception", "id": "think-friction-when-moving",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-friction-when-moving",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-30",
         "statements": [
             {"quote": "Friction only happens once something is moving.",
              "targets": "FORCE-30",
              "body": [
                  "Tilt a desk lid slowly with a book on it. For the first "
                  "few degrees the book stays exactly where it is — and "
                  "gravity is pulling it down the slope the whole time, so "
                  "something must be holding it. That something is friction, "
                  "acting up the slope, matching the pull along the slope "
                  "newton for newton. Keep tilting and there comes an angle "
                  "where friction runs out of matching to do, and the book "
                  "goes. <strong>Friction between surfaces that are not "
                  "sliding is doing most of the work friction does "
                  "anywhere</strong>: it is what stops a ladder slipping, a "
                  "screw turning back out, and a parked car rolling down a "
                  "hill.",
              ]},
             {"quote": "A smooth surface has no friction.",
              "targets": "FORCE-29",
              "body": [
                  "Two sheets of glass are about as smooth as anything you "
                  "will handle, and pressed together they are notoriously "
                  "hard to slide apart — smooth is not the same as "
                  "slippery. Under a microscope no surface is flat: what "
                  "looks polished is a landscape of peaks, and only the "
                  "peaks are actually touching. Sliding means dragging those "
                  "peaks over each other, and on a very smooth surface there "
                  "are so many contact points that the two can stick "
                  "together instead. <strong>What makes something slippery "
                  "is usually a layer of something else in between</strong> "
                  "— water on ice, oil in a bearing, graphite in a lock "
                  "— keeping the two surfaces apart rather than making "
                  "either one smoother.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "friction-against-the-sliding",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Friction is a contact force between two surfaces that "
                 "always acts against the sliding. It depends on both "
                 "surfaces and on how hard they are pressed together, it is "
                 "largest just before sliding starts, and it turns movement "
                 "into heat."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 1.
    "ladder": {
        "recall": {
            "q": "A sledge is pulled across level snow at a steady speed "
                 "with a 40 N pull. What is the friction on it?",
            "options": [
                "40 N, backwards along the snow.",
                "0 N — it is moving, so friction has been overcome.",
                "More than 40 N, because the snow is resisting.",
                "It cannot be worked out without the mass of the sledge.",
            ],
            "answer": 0,
            "feedback": {
                1: "Steady speed means the forces are balanced, not absent. "
                   "If friction were 0 N the sledge would be speeding up the "
                   "whole time.",
                2: "More than 40 N backwards would leave a resultant "
                   "backwards and the sledge would be slowing down, not "
                   "holding a steady speed.",
                3: "The mass would be needed to predict the friction from "
                   "scratch. Here the steady speed tells you it is balanced, "
                   "so it must match the 40 N pull.",
            },
            "title": "Rung 1 · Apply"},
        "apply": {
            "q": "A heavy toolbox sits on a sloping garage roof and does not "
                 "slide. Which statement is right?",
            "options": [
                "There is no friction, because nothing is sliding.",
                "Friction acts up the slope, matching the pull down the "
                "slope, so the resultant is 0 N.",
                "Friction acts down the slope, holding it against the roof.",
                "Friction is 0 N now and will appear the instant it starts "
                "to slide.",
            ],
            "answer": 1,
            "feedback": {
                0: "Then nothing would be holding it and it would slide. "
                   "Friction between surfaces that are not moving is what "
                   "keeps it there.",
                2: "Friction acts against the sliding that would otherwise "
                   "happen. The toolbox would slide down, so friction acts "
                   "up.",
                3: "It is the other way round: friction is at its largest "
                   "just before sliding, and drops slightly once the "
                   "surfaces are moving over each other.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A cyclist oils the chain and fits new brake blocks on the "
                 "same afternoon. Explain why one job is about reducing "
                 "friction and the other is about increasing it, and why "
                 "both make the bicycle better.",
            "field_label": "Your explanation",
            "placeholder": "The chain is oiled because…",
            "success": [
                "Says friction in the chain wastes energy as heat and is "
                "unwanted.",
                "Says the oil keeps the metal surfaces apart so there is "
                "less friction.",
                "Says the brakes need friction, between the blocks and the "
                "wheel rim.",
                "Says that friction acts against the wheel turning, so it "
                "slows the bicycle.",
                "Says friction is wanted or unwanted depending on the job, "
                "not good or bad in itself.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "In curling, two players sweep the ice hard in front of a "
                 "sliding stone. Sweeping melts a very thin film of water on "
                 "the surface. Explain what this does to the forces on the "
                 "stone and why it travels further.",
            "field_label": "Your answer",
            "placeholder": "Sweeping changes…",
            "success": [
                "Says friction between the stone and the ice is the "
                "backwards force acting on it.",
                "Says the water film keeps the two surfaces apart, so the "
                "friction gets smaller.",
                "Says the resultant force on the stone is therefore smaller.",
                "Says a smaller backwards resultant means the stone slows "
                "down more gradually.",
                "Says no force is needed to keep the stone moving, so with "
                "less friction it goes further before stopping.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Friction is a contact force between two surfaces, acting "
                "against the sliding. Its size depends on what the two "
                "surfaces are and how hard they are pressed together, and it "
                "is bigger just before sliding starts than during the slide. "
                "It turns movement into heat, so it is wanted where grip "
                "matters and reduced — by lubricating, by rollers, by "
                "wheels — where it only wastes energy.",

    "stretch": [
        {"id": "only-the-peaks-touch",
         "type": "explainer",
         "text": "Press two flat metal blocks together and they touch far "
                 "less than they appear to. Real surfaces are hills and "
                 "valleys, so contact happens only at the highest peaks — "
                 "and the true area in contact can be a tiny fraction of the "
                 "area you can see and measure with a ruler. Push harder and "
                 "those peaks flatten slightly, bringing more of them into "
                 "contact, which is the reason friction grows with how hard "
                 "the surfaces are pressed together rather than with how big "
                 "the block looks. At the points that do touch, atoms of one "
                 "surface come close enough to bond weakly to atoms of the "
                 "other, and sliding means breaking those bonds and making "
                 "new ones, over and over. <strong>That is where the heat "
                 "comes from</strong>, and it is why the crate is hardest to "
                 "start: given a moment at rest, the peaks settle deeper and "
                 "more of those bonds form."},
        {"id": "a-fifth-of-everything",
         "type": "explainer",
         "text": "Because friction converts movement into heat, and heat "
                 "spreads out and is difficult to use for anything, it is "
                 "the reason no machine gives back everything you put in. "
                 "Estimates of how much of the world's energy ends up wasted "
                 "in rubbing contacts run to something like a fifth of the "
                 "total — which is why bearings, gearbox oil and even the "
                 "dimples on a golf ball are worth engineering carefully. "
                 "The oldest fix is the simplest: get something between the "
                 "two surfaces. Water under a hydroplaning tyre does it "
                 "accidentally and dangerously; oil in a bearing does it "
                 "deliberately, floating the metal apart so the peaks never "
                 "meet. Your knee does it with a fluid that is more slippery "
                 "than any oil humans make."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "friction",
         "definition": "A contact force between two surfaces, always acting "
                       "against the sliding — or against the sliding that "
                       "is about to happen."},
        {"term": "lubricant",
         "definition": "Something put between two surfaces to keep them "
                       "apart, so the peaks never meet. Oil, water, "
                       "graphite, joint fluid."},
        {"term": "spring balance",
         "definition": "A hook, a spring and a scale. It reads the force "
                       "pulling on it, in newtons."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Want to test whether friction is helping or wasting in a "
                "machine of your own?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Work done against friction, energy dissipated to the "
                   "surroundings, and drag as one of the forces in a "
                   "free-body diagram.",

    "convention_note": "The drag bench is a teaching model. Each surface is "
                       "given a fixed grip figure chosen to be typical, and "
                       "the break-away reading is modelled as one fifth more "
                       "than the sliding reading; real surfaces vary with "
                       "polish, dust, damp and wear, and a real spring "
                       "balance reading wanders as you pull. Weight is taken "
                       "as mass in kilograms × 10 N/kg, and only the "
                       "horizontal forces are drawn.",

    "ws": [],
}
