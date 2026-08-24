"""P1 lesson 08 — Simple machines: twelve questions.

⊕ RUN 1's TWELVE WERE USED AS RAW MATERIAL, NOT ADOPTED (MRB-223).

Run 1's own provenance audit flags `s04` and `h02` as quoting "120 J every
time" and "135 J in for 120 out" off a bench it invented. Design's bench is
a 600 N load lifted 0.05 m on a 2.4 m bar, so the energy delivered to the
load is 600 × 0.05 = **30 J**, and her CFIFA worked example lands on the
same number from the other end: 250 N × 0.12 m = 30 J. Both figures are
internally consistent and neither is 120. `s03` quotes the same bench.

Run 1's generic arithmetic carries over cleanly, because it quotes nothing
from any bench: `e01` (20 N × 3 m) and `h01` (a 900 N chair raised 0.30 m)
are just work-done sums and both are kept.

    CHANGED — six stems kept, option sets rewritten (6):
        e01  20 N over 3 m — plain work done
        e02  what a simple machine does
        e03  a quarter of the force, and what happens to the energy
        h01  the wheelchair ramp
        h03  why nobody has built a machine that gives out more
        h04  "four times the force out, so four times the energy"

    NEW — on Design's OWN numbers, or her material (6):
        e04  the newton, and what it is not
        s01  the pulley at 400 N with a 100 N effort
        s02  her bench: 600 N lifted 0.05 m, so 30 J at the load end
        s03  why the measured input always exceeds 30 J and never falls short
        s04  the beam and the triangles — which shape holds which relation
        h02  the C in CFIFA, on a distance given in centimetres

    DROPPED — invented bench data (3):  run 1's s03, s04 and h02.
    DROPPED — duplicated by a stronger new item (3):  run 1's s01, s02, e04.

⚠️ HER SCIENCE FLAG 20 IS TESTED DIRECTLY BY `s03`. The measured input
scatters upward only — friction costs energy, so a real run always needs a
little more in than comes out, and never less. A student who has watched the
table and understood it can answer `s03`; one who has only read the rule
cannot tell which way the discrepancy should go.

⚠️ Answer positions are 3,0,1,2 · 0,1,2,3 · 3,0,1,2 — three of each index.
Not a clean cycle: `s04`'s options were reordered after a position audit
found index 1 holding four and index 3 only two. MRB-278 measures the COUNT.
⚠️ Every distractor is written to the correct answer's own length (MRB-177).

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P1"
LESSON = "simple-machines"
LESSON_NUMBER = 8

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-08-e01",
        "band": "easier",
        "text": "A force of 20 N pushes a box 3 m across a floor. How much "
                "energy is transferred?",
        "options": [
            {"text": "23 J", "correct": False,
             "why": "That is 20 + 3. The two quantities are multiplied, not "
                    "added."},
            {"text": "6.7 J", "correct": False,
             "why": "That is 20 ÷ 3. Energy is force multiplied by distance."},
            {"text": "17 J", "correct": False,
             "why": "That is 20 − 3. Nothing in the formula subtracts."},
            {"text": "60 J", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e02",
        "band": "easier",
        "text": "What does a simple machine do?",
        "options": [
            {"text": "It trades force against distance, leaving the energy "
                     "unchanged",
             "correct": True},
            {"text": "It creates extra force from the shape of its own "
                     "structure",
             "correct": False,
             "why": "Nothing creates force from nothing. It redistributes "
                    "the force you supply."},
            {"text": "It reduces the total energy a job needs to be done "
                     "with",
             "correct": False,
             "why": "The job needs what it needs. A machine changes the "
                    "shape of it, never the size."},
            {"text": "It converts energy into force so a job becomes "
                     "possible",
             "correct": False,
             "why": "Force and energy are different quantities and one does "
                    "not turn into the other."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e03",
        "band": "easier",
        "text": "A machine lets you lift a load using a quarter of the "
                "force. What happens to the energy you supply?",
        "options": [
            {"text": "It is a quarter as much as lifting it directly would "
                     "need",
             "correct": False,
             "why": "That would be energy for free. Only the force is a "
                    "quarter."},
            {"text": "It is the same, and your end travels four times as far",
             "correct": True},
            {"text": "It is four times as much, because the machine has to "
                     "be driven too",
             "correct": False,
             "why": "Friction adds a little, not four times. Ideally it is "
                    "the same."},
            {"text": "It depends entirely on how long the machine's lever "
                     "arm is",
             "correct": False,
             "why": "The arm sets the force-distance split. The energy is "
                    "the same whatever you choose."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e04",
        "band": "easier",
        "text": "A newton is the unit of which quantity?",
        "options": [
            {"text": "Energy", "correct": False,
             "why": "Energy is measured in joules. A newton times a metre "
                    "gives one."},
            {"text": "Distance", "correct": False,
             "why": "Distance is measured in metres. Newtons measure the "
                    "push or pull."},
            {"text": "Force", "correct": True},
            {"text": "Power", "correct": False,
             "why": "Power is measured in watts — energy per second. You "
                    "meet it in Energy at home."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-08-s01",
        "band": "standard",
        "text": "A pulley system raises a 400 N load using a force of 100 N. "
                "What must the builder do?",
        "options": [
            {"text": "Pull four times as much rope through as the load "
                     "actually rises",
             "correct": True},
            {"text": "Supply a quarter of the energy that lifting it "
                     "directly would take",
             "correct": False,
             "why": "The energy is the same. Only the force has been divided "
                    "by four."},
            {"text": "Attach a counterweight of 300 N to make up the "
                     "difference in force",
             "correct": False,
             "why": "No counterweight is needed. The rope length supplies "
                    "the difference."},
            {"text": "Pull a quarter as much rope through as the load "
                     "actually rises",
             "correct": False,
             "why": "That is backwards, and it would mean getting energy "
                    "for free."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s02",
        "band": "standard",
        "text": "On the bench a 600 N load is lifted 0.05 m. How much energy "
                "arrives at the load end?",
        "options": [
            {"text": "12000 J", "correct": False,
             "why": "That is 600 ÷ 0.05. Energy is force multiplied by "
                    "distance, not divided by it."},
            {"text": "30 J", "correct": True},
            {"text": "600 J", "correct": False,
             "why": "That is the force alone. It has to be multiplied by how "
                    "far the load actually rose."},
            {"text": "3000 J", "correct": False,
             "why": "That is 600 × 5, treating the rise as 5 m rather than "
                    "5 cm. Watch the units."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s03",
        "band": "standard",
        "text": "Your measured energy at the effort end is always a little "
                "MORE than 30 J, never less. Why never less?",
        "options": [
            {"text": "Because the force meter is not sensitive enough to "
                     "read the smaller values",
             "correct": False,
             "why": "It is not an instrument fault. A better meter would "
                    "show the same one-sided pattern."},
            {"text": "Because the bar itself stores a little of the energy "
                     "as it bends slightly",
             "correct": False,
             "why": "A stiff bar stores very little, and it gives that back. "
                    "Something else takes a permanent cut."},
            {"text": "Because friction at the fulcrum fills a thermal store, "
                     "so you always supply extra",
             "correct": True},
            {"text": "Because the load is heavier than 600 N once it starts "
                     "to move upwards",
             "correct": False,
             "why": "Its weight does not change. What changed is where some "
                    "of your energy went."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s04",
        "band": "standard",
        "text": "Why is the lever rule drawn as a beam with a triangle on "
                "each pan, rather than as one triangle?",
        "options": [
            {"text": "Because a triangle can only hold quantities that are "
                     "measured in the same unit",
             "correct": False,
             "why": "Triangles routinely mix units — E in joules over F in "
                    "newtons and d in metres."},
            {"text": "Because a beam is easier for a student to read than a "
                     "triangle would be",
             "correct": False,
             "why": "It is not about ease. The two shapes encode genuinely "
                    "different relationships."},
            {"text": "Because the two sides of the rule are added together "
                     "rather than multiplied",
             "correct": False,
             "why": "Each side is a multiplication. It is the equals sign "
                    "between them that the beam shows."},
            {"text": "Because the rule has four quantities and an equals "
                     "sign, which no triangle holds",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-08-h01",
        "band": "harder",
        "text": "A ramp must raise a 900 N wheelchair 0.30 m using no more "
                "than 90 N. How long must the ramp be?",
        "options": [
            {"text": "0.30 m, because the height is what sets the length "
                     "needed",
             "correct": False,
             "why": "That is the height itself. The ramp has to be longer "
                    "than the rise, by the force ratio."},
            {"text": "10 m, because the force has been reduced by a factor "
                     "of ten",
             "correct": False,
             "why": "Right factor, wrong quantity to apply it to. Multiply "
                    "the RISE by ten, not a metre."},
            {"text": "27 m, found by multiplying the weight by the height "
                     "of the rise",
             "correct": False,
             "why": "900 × 0.30 is the ENERGY, 270 J. Dividing that by 90 N "
                    "gives the length."},
            {"text": "3.0 m, because 900 × 0.30 = 270 J and 270 ÷ 90 = 3.0",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h02",
        "band": "harder",
        "text": "A question gives the distance as 40 cm. Which CFIFA step "
                "catches that, and what does it do?",
        "options": [
            {"text": "Convert — it turns 40 cm into 0.40 m before anything "
                     "is multiplied",
             "correct": True},
            {"text": "Formula — it chooses a version of the equation that "
                     "works in centimetres",
             "correct": False,
             "why": "There is no centimetre version. The formula is the same "
                    "and the units are fixed first."},
            {"text": "Insert — it puts 40 into the equation and notes the "
                     "unit beside it",
             "correct": False,
             "why": "Inserting 40 gives an answer a hundred times too big. "
                    "The fix happens before this."},
            {"text": "Fine-tune — it corrects the answer at the end by "
                     "dividing it by a hundred",
             "correct": False,
             "why": "Correcting at the end works only if you remember. "
                    "Converting first means there is nothing to remember."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h03",
        "band": "harder",
        "text": "Why has nobody ever built a machine that gives out more "
                "energy than it takes in?",
        "options": [
            {"text": "Because the materials available are not yet strong or "
                     "smooth enough to manage it",
             "correct": False,
             "why": "Better materials reduce friction. They cannot get you "
                    "past the total, only closer to it."},
            {"text": "Because friction always removes a little, so the "
                     "output falls just short",
             "correct": True},
            {"text": "Because such a machine would have to be far larger "
                     "than anyone could build",
             "correct": False,
             "why": "Size is irrelevant. No arrangement of any size can "
                    "break the sum."},
            {"text": "Because the patent office has refused to grant a "
                     "patent for any of the designs",
             "correct": False,
             "why": "The refusal follows from the physics rather than "
                    "causing it. The sum is the reason."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h04",
        "band": "harder",
        "text": "A student writes “a block and tackle gives four times "
                "the force out, so four times the energy”. Correct "
                "them.",
        "options": [
            {"text": "The force is not multiplied either — only the "
                     "direction of the pull has changed",
             "correct": False,
             "why": "The force genuinely is multiplied. That part of the "
                    "sentence is right."},
            {"text": "Both halves are right, but only while the rope is "
                     "completely free of friction",
             "correct": False,
             "why": "The second half is never right, frictionless or not. "
                    "Energy is not multiplied."},
            {"text": "Force is multiplied and energy is not — you pull four "
                     "times as much rope through",
             "correct": True},
            {"text": "Energy is multiplied and force is not, because pulleys "
                     "work on distance alone",
             "correct": False,
             "why": "Exactly the wrong way round. Force is the one that may "
                    "be multiplied."},
        ],
        "figure": None,
    },
]
