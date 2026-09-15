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
                     "catch the smaller readings",
             "correct": False,
             "why": "It is not an instrument fault. A better meter would "
                    "show the same one-sided pattern."},
            {"text": "Because the bar itself stores a little of the energy "
                     "as it bends very slightly",
             "correct": False,
             "why": "A stiff bar stores very little, and it gives that back. "
                    "Something else takes a permanent cut."},
            {"text": "Because friction at the fulcrum fills a thermal store, "
                     "so you always supply extra",
             "correct": True},
            {"text": "Because the load acts as though it is heavier than "
                     "600 N once it starts moving",
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p1-08-e05",
        "band": "easier",
        "text": "What is meant by work done?",
        "options": [
            {"text": "The energy transferred when a force moves through a "
                     "distance",
             "correct": True},
            {"text": "The force that is needed to hold something still "
                     "without moving it",
             "correct": False,
             "why": "Holding still moves nothing, so no distance is covered "
                    "and no energy is transferred."},
            {"text": "The time a machine has been running for",
             "correct": False,
             "why": "That is a time in seconds. Work done is an energy in "
                    "joules."},
            {"text": "The distance a load has been lifted", "correct": False,
             "why": "That is a distance in metres. It has to be multiplied by "
                    "the force to give an energy."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e06",
        "band": "easier",
        "text": "A force of 50 N lifts a load through 2 m. How much energy is "
                "transferred?",
        "options": [
            {"text": "25 J", "correct": False,
             "why": "That is 50 ÷ 2. Work done is force MULTIPLIED by "
                    "distance."},
            {"text": "100 J", "correct": True},
            {"text": "52 J", "correct": False,
             "why": "That is 50 + 2, and a force and a distance cannot be "
                    "added."},
            {"text": "0.04 J", "correct": False,
             "why": "That is 2 ÷ 50, the division upside down as well as the "
                    "wrong operation."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p1-08-s05",
        "band": "standard",
        "text": "A lever lifts a 600 N rock using an effort of 150 N, and the "
                "effort end moves 0.80 m. Ignoring friction, how far does the "
                "rock rise?",
        "options": [
            {"text": "0.20 m", "correct": True},
            {"text": "3.20 m", "correct": False,
             "why": "That multiplies the distance by four. Multiplying the "
                    "force by four must DIVIDE the distance by four."},
            {"text": "0.80 m", "correct": False,
             "why": "Both ends cannot move the same distance, or the lever "
                    "would be giving energy away free."},
            {"text": "120 m", "correct": False,
             "why": "120 is the energy in joules. It still has to be divided "
                    "by the 600 N load."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s06",
        "band": "standard",
        "text": "A ramp 4 m long is used to raise a load through a height of "
                "1 m. Ignoring friction, by what factor is the force "
                "reduced?",
        "options": [
            {"text": "Three times, the difference between 4 m and 1 m",
             "correct": False,
             "why": "It is the RATIO of the two distances that counts, not "
                    "the difference between them."},
            {"text": "Four times, because the ramp is four times as long",
             "correct": True},
            {"text": "It is not reduced at all — the load weighs the same",
             "correct": False,
             "why": "The weight is unchanged, but the push needed along the "
                    "ramp is a quarter of it."},
            {"text": "Four times, and the energy needed is quartered too",
             "correct": False,
             "why": "The force is quartered and the distance is quadrupled, "
                    "so the energy is exactly the same."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p1-08-h05",
        "band": "harder",
        "text": "A pulley system raises an 800 N load through 0.50 m using an "
                "effort of 200 N. Ignoring friction, how far must the rope be "
                "pulled?",
        "options": [
            {"text": "0.125 m", "correct": False,
             "why": "That divides the distance by four. A smaller force must "
                    "move a LONGER distance, not a shorter one."},
            {"text": "0.50 m", "correct": False,
             "why": "If both distances matched, the pulley would be creating "
                    "300 J out of nothing."},
            {"text": "400 m", "correct": False,
             "why": "400 is the energy in joules. It still has to be divided "
                    "by the 200 N effort."},
            {"text": "2.0 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h06",
        "band": "harder",
        "text": "On the lever bench the measured input is always slightly "
                "MORE than the output. What would it mean if a group measured "
                "LESS in than out?",
        "options": [
            {"text": "That the lever is unusually efficient and worth keeping",
             "correct": False,
             "why": "No lever can pass on more than it was given, however "
                    "well made."},
            {"text": "That friction has somehow helped rather than hindered "
                     "on this occasion",
             "correct": False,
             "why": "Friction only ever moves energy into thermal stores, so "
                    "it can never add to the output."},
            {"text": "That it must be a measurement error — energy is not "
                     "created",
             "correct": True},
            {"text": "That the load was lighter than the label on it says",
             "correct": False,
             "why": "A lighter load would change both figures together, and "
                    "still could not put the output above the input."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · easier ─────────────────────────────────
    {
        "id": "p1-08-e07",
        "band": "easier",
        "text": "Which of these is a list of simple machines?",
        "options": [
            {"text": "Lever, ramp, pulley, gear, screw", "correct": True},
            {"text": "Motor, battery, generator, cable", "correct": False,
             "why": "Those all need an energy supply. A simple machine has no "
                    "supply and no moving power source."},
            {"text": "Thermometer, ruler, balance, stopwatch",
             "correct": False,
             "why": "Those are measuring instruments. They trade nothing "
                    "between force and distance."},
            {"text": "Copper, iron, glass, wood", "correct": False,
             "why": "Those are materials rather than machines, and they do "
                    "nothing to a force at all."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e08",
        "band": "easier",
        "text": "What is the fulcrum of a lever?",
        "options": [
            {"text": "The end of the bar where you push down with your own "
                     "hands",
             "correct": False,
             "why": "That is the effort end. The fulcrum is the fixed point "
                    "the bar turns about."},
            {"text": "The end of the bar that rests underneath the load being "
                     "lifted",
             "correct": False,
             "why": "That is the load end. The fulcrum sits between the two, "
                    "or beyond them."},
            {"text": "The fixed point that the bar turns about",
             "correct": True},
            {"text": "The whole length of the bar",
             "correct": False,
             "why": "That is the bar's length. The fulcrum is a point on it, "
                    "not a distance."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e09",
        "band": "easier",
        "text": "Energy transferred is measured in which unit?",
        "options": [
            {"text": "Newtons", "correct": False,
             "why": "Newtons measure force. A newton multiplied by a metre "
                    "gives the unit of energy."},
            {"text": "Joules", "correct": True},
            {"text": "Metres", "correct": False,
             "why": "Metres measure distance, which is only one of the two "
                    "quantities multiplied together."},
            {"text": "Watts", "correct": False,
             "why": "Watts measure power, which is energy per second rather "
                    "than energy itself."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e10",
        "band": "easier",
        "text": "In E = F × d, the distance d must be measured in which unit "
                "for the answer to come out in joules?",
        "options": [
            {"text": "Centimetres", "correct": False,
             "why": "Using centimetres gives an answer a hundred times too "
                    "big. Convert to metres first."},
            {"text": "Millimetres", "correct": False,
             "why": "Millimetres give an answer a thousand times too big. "
                    "The formula wants metres."},
            {"text": "Kilometres", "correct": False,
             "why": "Kilometres give an answer a thousand times too small. "
                    "The formula wants metres."},
            {"text": "Metres", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e11",
        "band": "easier",
        "text": "A force of 35 N drags a crate 4 m across a yard. How much "
                "energy is transferred?",
        "options": [
            {"text": "140 J", "correct": True},
            {"text": "39 J", "correct": False,
             "why": "That is 35 + 4. Force and distance are multiplied, not "
                    "added together."},
            {"text": "8.75 J", "correct": False,
             "why": "That is 35 ÷ 4. Energy is force multiplied by distance "
                    "rather than divided by it."},
            {"text": "31 J", "correct": False,
             "why": "That is 35 − 4. Nothing anywhere in the formula "
                    "subtracts one from the other."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e12",
        "band": "easier",
        "text": "You hold a heavy bag perfectly still for two minutes. How "
                "much energy have you transferred to the bag?",
        "options": [
            {"text": "A great deal, because holding a heavy bag is genuinely "
                     "tiring work to do for two minutes",
             "correct": False,
             "why": "Your muscles do use energy, but none of it is "
                    "transferred to the bag, which has not moved."},
            {"text": "None, because the bag has not moved any distance",
             "correct": True},
            {"text": "The weight of the bag times two minutes",
             "correct": False,
             "why": "Time is not in the formula. Energy is force multiplied "
                    "by the distance moved."},
            {"text": "Exactly the same as if you had lifted it one metre",
             "correct": False,
             "why": "Lifting it a metre moves it a metre. Holding it still "
                    "moves it nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e13",
        "band": "easier",
        "text": "Which quantity can a lever multiply?",
        "options": [
            {"text": "The energy that you supply", "correct": False,
             "why": "Energy is the one thing no machine can multiply. That "
                    "is what conservation forbids."},
            {"text": "The force you apply", "correct": True},
            {"text": "Both the force and the energy together", "correct": False,
             "why": "The force yes, the energy never. Multiplying both would "
                    "be energy for nothing."},
            {"text": "Neither of them, only the direction", "correct": False,
             "why": "A lever genuinely does multiply force, which is why a "
                    "crowbar is useful."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e14",
        "band": "easier",
        "text": "If a machine multiplies your force by six, what happens to "
                "the distance your end moves?",
        "options": [
            {"text": "It is six times as far", "correct": True},
            {"text": "It is one sixth as far as before", "correct": False,
             "why": "That is the load's end. Yours has to travel further, not "
                    "less far."},
            {"text": "It stays exactly the same", "correct": False,
             "why": "If both the force and the distance stayed, the energy "
                    "would have been multiplied by six."},
            {"text": "It is thirty-six times as far", "correct": False,
             "why": "The trade is one for one, not squared. Six times the "
                    "force costs six times the distance."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e15",
        "band": "easier",
        "text": "How many metres is 250 cm?",
        "options": [
            {"text": "25 m", "correct": False,
             "why": "That divides by ten. There are a hundred centimetres in "
                    "a metre, not ten."},
            {"text": "2500 m", "correct": False,
             "why": "That multiplies by ten. Converting centimetres to metres "
                    "makes the number smaller."},
            {"text": "2.50 m", "correct": True},
            {"text": "0.25 m", "correct": False,
             "why": "That divides by a thousand, which is the conversion for "
                    "millimetres rather than centimetres."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e16",
        "band": "easier",
        "text": "How many metres is 75 cm?",
        "options": [
            {"text": "7.5 m", "correct": False,
             "why": "That divides by ten. A centimetre is a hundredth of a "
                    "metre, not a tenth."},
            {"text": "0.075 m", "correct": False,
             "why": "That divides by a thousand, which converts millimetres "
                    "rather than centimetres."},
            {"text": "750 m", "correct": False,
             "why": "That multiplies by ten. Going from centimetres to metres "
                    "makes the number smaller."},
            {"text": "0.75 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e17",
        "band": "easier",
        "text": "What does the C at the start of CFIFA stand for?",
        "options": [
            {"text": "Convert, which puts every quantity into the right unit "
                     "before anything is multiplied",
             "correct": True},
            {"text": "Check, which means reading the question through once "
                     "more before starting on it",
             "correct": False,
             "why": "Checking is a good habit, but the C step is about units "
                    "rather than about re-reading."},
            {"text": "Calculate, which means working out the answer as the "
                     "very first thing you do",
             "correct": False,
             "why": "Calculating comes later. The C step happens before any "
                    "numbers go into a formula."},
            {"text": "Copy, which means writing the question out again at the "
                     "top of your working",
             "correct": False,
             "why": "Copying the question is not one of the five steps. The C "
                    "is for converting units."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e18",
        "band": "easier",
        "text": "Is a ramp a simple machine?",
        "options": [
            {"text": "No, because a ramp has no moving parts of its own at "
                     "all",
             "correct": False,
             "why": "Moving parts are not required. A ramp trades force "
                    "against distance, which is what counts."},
            {"text": "No, because a ramp cannot change the force you need to "
                     "supply",
             "correct": False,
             "why": "It changes it a great deal. Pushing up a long ramp needs "
                    "far less force than lifting."},
            {"text": "Yes, because it trades a smaller force for a longer "
                     "distance",
             "correct": True},
            {"text": "Yes, because it creates extra force from its own shape",
             "correct": False,
             "why": "Nothing creates force from a shape. The ramp trades your "
                    "force against distance."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e19",
        "band": "easier",
        "text": "Is a screw a simple machine?",
        "options": [
            {"text": "Yes — turning it a long way drives it in a short way",
             "correct": True},
            {"text": "No, because a screw only holds two pieces of wood "
                     "together and moves nothing",
             "correct": False,
             "why": "A screw advances as it turns, and that advance is the "
                    "trade a machine makes."},
            {"text": "No, because a screw needs a screwdriver, and it is the "
                     "screwdriver that is the real machine",
             "correct": False,
             "why": "Both are machines. The screw itself trades turning "
                    "distance against forward force."},
            {"text": "Yes, because a screw creates its own force",
             "correct": False,
             "why": "Nothing creates force. The force comes from your hand "
                    "and is traded against distance."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e20",
        "band": "easier",
        "text": "What does a pair of gears do?",
        "options": [
            {"text": "It creates extra turning force out of the shape of the "
                     "teeth on the two wheels themselves",
             "correct": False,
             "why": "Nothing is created. The turning force you supply is "
                    "traded against how far the wheels turn."},
            {"text": "It multiplies the energy supplied, so a small motor can "
                     "do a much larger job",
             "correct": False,
             "why": "Energy is never multiplied. A small motor doing a big "
                    "job simply takes longer over it."},
            {"text": "It trades turning force against how far each wheel "
                     "turns",
             "correct": True},
            {"text": "It stores energy in the teeth for later",
             "correct": False,
             "why": "Gear teeth store nothing. They pass the turning on as it "
                    "arrives."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e21",
        "band": "easier",
        "text": "Why can a machine never give out more energy than it is "
                "given?",
        "options": [
            {"text": "Because the materials are not yet strong enough for it",
             "correct": False,
             "why": "Better materials cut friction. No material lets a "
                    "machine break the sum."},
            {"text": "Because energy can never be created, so there is no "
                     "source for the extra",
             "correct": True},
            {"text": "Because every machine ever built has some friction",
             "correct": False,
             "why": "Friction explains why the output falls SHORT. Even "
                    "without it there would be no extra."},
            {"text": "Because machines are designed to be safe, not powerful",
             "correct": False,
             "why": "Design is not the limit. The law forbids it whatever "
                    "anybody intends."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e22",
        "band": "easier",
        "text": "In a real machine, where does the energy go that does not "
                "arrive at the load?",
        "options": [
            {"text": "It is destroyed by the rubbing",
             "correct": False,
             "why": "Rubbing destroys nothing. It moves energy into thermal "
                    "stores, where it still is."},
            {"text": "It stays in the person or motor that supplied it in the "
                     "first place",
             "correct": False,
             "why": "It was supplied, so it left. The question is where it "
                    "arrived instead."},
            {"text": "It never existed at all, because only the useful part of "
                     "it is really energy anyway",
             "correct": False,
             "why": "All of it is energy. Usefulness does not decide what "
                    "counts."},
            {"text": "Into thermal stores at the joints and bearings",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e23",
        "band": "easier",
        "text": "The fulcrum of a lever is moved much closer to the load. "
                "What happens to the effort needed?",
        "options": [
            {"text": "It becomes larger, because the load end now has the "
                     "shorter arm of the two",
             "correct": False,
             "why": "A short load arm is what makes the effort SMALLER. The "
                    "trade runs the other way."},
            {"text": "It stays the same, because the load has not been "
                     "changed at all",
             "correct": False,
             "why": "The load is the same but the arms are not, and the arms "
                    "decide the effort."},
            {"text": "It becomes smaller, and your end has to travel further",
             "correct": True},
            {"text": "It becomes smaller, and the energy needed falls too",
             "correct": False,
             "why": "The force falls but the energy does not. You pay in "
                    "distance instead."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e24",
        "band": "easier",
        "text": "Which shape properly shows the relationship E = F × d?",
        "options": [
            {"text": "A balance beam, because the two sides have to stay level",
             "correct": False,
             "why": "A beam is for two products either side of an equals "
                    "sign. This is a single product."},
            {"text": "A formula triangle, with E on top", "correct": True},
            {"text": "A part-whole bar for the energy",
             "correct": False,
             "why": "A bar is for a sum. Force and distance are multiplied, "
                    "not added."},
            {"text": "A line graph of the two",
             "correct": False,
             "why": "A graph shows how two quantities vary. A triangle shows "
                    "how to rearrange the formula."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e25",
        "band": "easier",
        "text": "Which shape properly shows the lever rule, where one product "
                "equals another?",
        "options": [
            {"text": "A single formula triangle, with the load on top of it",
             "correct": False,
             "why": "A triangle holds three quantities. The lever rule has "
                    "four and an equals sign."},
            {"text": "A part-whole bar, split into the four quantities",
             "correct": False,
             "why": "A bar shows a sum. Each side of the lever rule is a "
                    "product, not a total."},
            {"text": "A balance beam, with a product on each pan",
             "correct": True},
            {"text": "A pie chart, with one slice for each of the quantities",
             "correct": False,
             "why": "A pie chart shows shares of a whole. Nothing here is a "
                    "share of anything."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e26",
        "band": "easier",
        "text": "Why does a spanner with a long handle loosen a tight nut "
                "more easily than a short one?",
        "options": [
            {"text": "Because a long handle is heavier, and the weight helps "
                     "to turn it",
             "correct": False,
             "why": "Weight is not the mechanism, and a long light spanner "
                    "works just as well."},
            {"text": "Because your hand moves further round, so a smaller "
                     "force does the same job",
             "correct": True},
            {"text": "Because a long handle creates extra turning force out "
                     "of nothing at all",
             "correct": False,
             "why": "Nothing is created. You trade a smaller force for a "
                    "longer journey."},
            {"text": "Because a long handle needs less energy than a short one "
                     "does",
             "correct": False,
             "why": "The energy is the same. Only the force and the distance "
                    "have been traded."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e27",
        "band": "easier",
        "text": "A student inserts 120 rather than 1.20 m into E = F × d. "
                "What happens to the answer?",
        "options": [
            {"text": "It comes out a hundred times too big",
             "correct": True},
            {"text": "It comes out a hundred times too small instead", "correct": False,
             "why": "Using the bigger number gives a bigger answer. The error "
                    "makes it too large."},
            {"text": "It comes out exactly right, because the units cancel "
                     "out later on in the working",
             "correct": False,
             "why": "Nothing cancels. Inserting the wrong number gives the "
                    "wrong answer."},
            {"text": "It comes out ten times too big, because there are ten "
                     "centimetres in a metre",
             "correct": False,
             "why": "There are a hundred centimetres in a metre, so the error "
                    "is a factor of a hundred."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e28",
        "band": "easier",
        "text": "On a lever, what is meant by the effort?",
        "options": [
            {"text": "The weight of whatever thing the lever is being used to "
                     "lift up",
             "correct": False,
             "why": "That is the load. The effort is what you supply at your "
                    "own end."},
            {"text": "The distance the load is raised by one push on the bar",
             "correct": False,
             "why": "That is a distance in metres. The effort is a force in "
                    "newtons."},
            {"text": "The point the bar turns about",
             "correct": False,
             "why": "That is the fulcrum. The effort is the force you "
                    "supply."},
            {"text": "The force you apply at your end of the bar",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e29",
        "band": "easier",
        "text": "On a lever, what is meant by the load?",
        "options": [
            {"text": "The force the lever has to move at the far end",
             "correct": True},
            {"text": "The force you push down with at your end",
             "correct": False,
             "why": "That is the effort. The load is at the other end of the "
                    "lever from you."},
            {"text": "The total length of the bar",
             "correct": False,
             "why": "That is a distance in metres. The load is a force in "
                    "newtons."},
            {"text": "The energy needed to finish the job",
             "correct": False,
             "why": "That is an energy in joules. The load is a force in "
                    "newtons."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e30",
        "band": "easier",
        "text": "Does using a machine reduce the energy a job needs?",
        "options": [
            {"text": "Yes, which is the whole reason that people use machines "
                     "for difficult jobs",
             "correct": False,
             "why": "People use machines to make a job possible, not cheaper "
                    "in energy."},
            {"text": "Yes, as long as the machine has been properly oiled "
                     "before the job starts",
             "correct": False,
             "why": "Oiling reduces the waste, never the job itself. The job "
                    "needs what it needs."},
            {"text": "No, because a machine only reduces the force needed and "
                     "leaves the job the same size",
             "correct": True},
            {"text": "No, because a machine always doubles the energy needed "
                     "for any job at all",
             "correct": False,
             "why": "Friction adds a little, not double. The ideal case is "
                    "exactly the same energy."},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · standard ───────────────────────────────
    {
        "id": "p1-08-s07",
        "band": "standard",
        "text": "A job transfers 480 J using a force of 60 N. How far did the "
                "force move?",
        "options": [
            {"text": "8 m", "correct": True},
            {"text": "28 800 m", "correct": False,
             "why": "That multiplies the two. To find a distance from an "
                    "energy you divide by the force."},
            {"text": "540 m", "correct": False,
             "why": "That adds the two figures together, and an energy cannot "
                    "be added to a force."},
            {"text": "0.125 m", "correct": False,
             "why": "That is 60 ÷ 480, the division the wrong way up."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s08",
        "band": "standard",
        "text": "A crate is dragged 1.5 m and 360 J is transferred. What force "
                "was used?",
        "options": [
            {"text": "540 N", "correct": False,
             "why": "That multiplies the two. To find a force from an energy "
                    "you divide by the distance."},
            {"text": "240 N", "correct": True},
            {"text": "361.5 N", "correct": False,
             "why": "That adds them, and a distance cannot be added to an "
                    "energy."},
            {"text": "0.004 N", "correct": False,
             "why": "That is 1.5 ÷ 360, which is the division upside down."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s09",
        "band": "standard",
        "text": "A lever raises an 800 N load through 0.10 m. How much energy "
                "arrives at the load end?",
        "options": [
            {"text": "8000 J", "correct": False,
             "why": "That is 800 ÷ 0.10. Energy is the force multiplied by "
                    "the distance."},
            {"text": "800 J", "correct": False,
             "why": "That is the force on its own. It still has to be "
                    "multiplied by how far the load rose."},
            {"text": "80 J", "correct": True},
            {"text": "8 J", "correct": False,
             "why": "That is ten times too small. 800 × 0.10 comes to eighty, "
                    "not eight."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s10",
        "band": "standard",
        "text": "A see-saw balances with a 300 N child sitting 2.0 m from the "
                "pivot. How far from the pivot must a 600 N adult sit?",
        "options": [
            {"text": "4.0 m, because the heavier person must sit further out",
             "correct": False,
             "why": "The heavier person sits CLOSER. Their larger force needs "
                    "a shorter distance to balance."},
            {"text": "1.0 m", "correct": True},
            {"text": "2.0 m, because both of them must sit the same distance "
                     "from the pivot",
             "correct": False,
             "why": "Equal distances need equal forces, and 600 N is not "
                    "300 N."},
            {"text": "0.5 m, because 300 ÷ 600 gives one half",
             "correct": False,
             "why": "The child's 300 N × 2.0 m is 600 J, and dividing that by "
                    "600 N gives one metre."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s11",
        "band": "standard",
        "text": "A pulley block has three sections of rope holding the load. "
                "What does that mean for the builder?",
        "options": [
            {"text": "A third of the force, and a third as much rope",
             "correct": False,
             "why": "That would be energy for nothing. A smaller force must "
                    "travel further."},
            {"text": "A third of the force, and a third of the energy too",
             "correct": False,
             "why": "The energy is the same. Only the force has been divided "
                    "by three."},
            {"text": "Three times the force, and a third as much rope to pull",
             "correct": False,
             "why": "That is the trade the wrong way round. More rope "
                    "sections means less force, not more."},
            {"text": "A third of the force, and three times as much rope to "
                     "pull through",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s12",
        "band": "standard",
        "text": "A large gear drives a smaller one. What happens to the "
                "turning force and to the number of turns?",
        "options": [
            {"text": "Both go up, because a small gear is easier to turn",
             "correct": False,
             "why": "Both cannot rise. That would be getting energy from "
                    "nowhere."},
            {"text": "Both go down, because energy is lost at the teeth",
             "correct": False,
             "why": "Friction takes a small share, but the trade itself is "
                    "one up and one down."},
            {"text": "The small gear turns more often with less turning force",
             "correct": True},
            {"text": "The small gear turns less often with more turning force",
             "correct": False,
             "why": "A smaller gear must turn more times to keep up, not "
                    "fewer."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s13",
        "band": "standard",
        "text": "A cyclist changes into a low gear to climb a hill. What has "
                "been traded for what?",
        "options": [
            {"text": "Less force at the pedals, and less energy needed",
             "correct": False,
             "why": "The hill needs the same energy whatever the gear. Only "
                    "the force and the turns change."},
            {"text": "Less force at the pedals, paid for in more turns of "
                     "them",
             "correct": True},
            {"text": "More force at the pedals, paid for in fewer turns",
             "correct": False,
             "why": "A low gear is chosen because it makes the pedals easier, "
                    "not harder."},
            {"text": "Nothing at all, because gears change only the speed",
             "correct": False,
             "why": "Speed changes because the force-distance trade has "
                    "changed. It is not the only thing that moves."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s14",
        "band": "standard",
        "text": "In a wheelbarrow the wheel is at one end and the handles at "
                "the other. Where is the fulcrum?",
        "options": [
            {"text": "At the handles, because that is where the effort is "
                     "supplied",
             "correct": False,
             "why": "The handles are the effort end. The fulcrum is the fixed "
                    "point the barrow turns about."},
            {"text": "At the load in the middle, because that is the heaviest "
                     "part of the whole barrow",
             "correct": False,
             "why": "The load sits between the two, but it is not the pivot. "
                    "The wheel is."},
            {"text": "At the wheel, because that is the point the barrow "
                     "turns about",
             "correct": True},
            {"text": "There is no fulcrum, because a barrow is not a lever",
             "correct": False,
             "why": "A wheelbarrow is a lever, and like every lever it turns "
                    "about a fixed point."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s15",
        "band": "standard",
        "text": "A nut is much harder to crack when it is held near the hinge "
                "of the nutcracker. Explain.",
        "options": [
            {"text": "Near the hinge the nutcracker has to be squeezed for "
                     "longer",
             "correct": False,
             "why": "Time does not come into the lever rule. The arm lengths "
                    "do."},
            {"text": "Near the hinge the nut is squeezed by a smaller area",
             "correct": False,
             "why": "Area is not what a lever trades. The distance from the "
                    "hinge is."},
            {"text": "Near the hinge is a shorter arm, so your force is "
                     "multiplied by less",
             "correct": True},
            {"text": "Near the hinge the nut is harder than it is further out",
             "correct": False,
             "why": "The nut is the same wherever it sits. What changes is "
                    "how much your force is multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s16",
        "band": "standard",
        "text": "A question gives a distance of 600 mm. What does the C step "
                "of CFIFA do with it?",
        "options": [
            {"text": "Divides by a hundred to give 6.00 m before anything is "
                     "multiplied together",
             "correct": False,
             "why": "A hundred is the conversion for centimetres. There are a "
                    "thousand millimetres in a metre."},
            {"text": "Divides by a thousand to give 0.600 m before anything "
                     "is multiplied",
             "correct": True},
            {"text": "Multiplies by a thousand to give 600 000 m for use in "
                     "the formula",
             "correct": False,
             "why": "Converting millimetres to metres makes the number "
                    "smaller, not larger."},
            {"text": "Leaves it as 600, because the unit does not matter",
             "correct": False,
             "why": "It matters a great deal: leaving it gives an answer a "
                    "thousand times too big."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s17",
        "band": "standard",
        "text": "A pull of 40 N moves a drawer 300 mm. How much energy is "
                "transferred?",
        "options": [
            {"text": "12 000 J", "correct": False,
             "why": "That uses 300 rather than 0.300 m, so it is a thousand "
                    "times too big."},
            {"text": "12 J", "correct": True},
            {"text": "0.133 J", "correct": False,
             "why": "That is 40 ÷ 300. Energy is force multiplied by "
                    "distance."},
            {"text": "340 J", "correct": False,
             "why": "That adds the two figures, and a force cannot be added "
                    "to a distance."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s18",
        "band": "standard",
        "text": "Why is the distance your hand moves on a lever not the same "
                "as the distance the load rises?",
        "options": [
            {"text": "Because the load end always moves first",
             "correct": False,
             "why": "Both ends move together. The difference is how far each "
                    "one travels."},
            {"text": "Because the load is heavier than the effort, and heavy "
                     "things always move more slowly",
             "correct": False,
             "why": "Weight is not what sets the two distances. The arm "
                    "lengths are."},
            {"text": "Because the bar bends slightly as it is pushed",
             "correct": False,
             "why": "A stiff bar barely bends, and the difference in "
                    "distances is far larger than any bending."},
            {"text": "Because the two ends are at different distances from "
                     "the fulcrum",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s19",
        "band": "standard",
        "text": "On the lever bench the fulcrum is moved three times and the "
                "load still rises 5 cm. Which column stays near enough the "
                "same?",
        "options": [
            {"text": "Your force, because the load has not changed at all "
                     "between the three runs",
             "correct": False,
             "why": "Your force changes a great deal as the fulcrum moves. "
                    "That is the point of moving it."},
            {"text": "Your distance, because the bar is the same length for "
                     "each of the three runs",
             "correct": False,
             "why": "Your distance changes too, in the opposite direction to "
                    "your force."},
            {"text": "Energy in and energy out, which stay near enough equal "
                     "every time",
             "correct": True},
            {"text": "None of them, because moving the fulcrum changes every "
                     "column in the table",
             "correct": False,
             "why": "The two energy columns stay near enough the same, which "
                    "is what the bench is for."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s20",
        "band": "standard",
        "text": "Moving the fulcrum changes the force you need but not the "
                "energy you supply. Why not?",
        "options": [
            {"text": "Because a smaller force is always paid for with a "
                     "larger distance",
             "correct": True},
            {"text": "Because the fulcrum takes the extra energy and holds "
                     "it until the bar is released",
             "correct": False,
             "why": "A fulcrum stores nothing. It is a fixed point that the "
                    "bar turns about."},
            {"text": "Because the load is lifted more slowly",
             "correct": False,
             "why": "Speed does not appear in the lever rule. The distances "
                    "do."},
            {"text": "Because the bar itself supplies the difference",
             "correct": False,
             "why": "A bar has no energy supply. All of it comes from your "
                    "end."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s21",
        "band": "standard",
        "text": "A jack raises a 2000 N car through 0.40 m. How much energy "
                "reaches the car?",
        "options": [
            {"text": "5000 J", "correct": False,
             "why": "That is 2000 ÷ 0.40. Energy is the force multiplied by "
                    "the distance."},
            {"text": "2000.4 J", "correct": False,
             "why": "That adds them, and a force cannot be added to a "
                    "distance."},
            {"text": "80 J", "correct": False,
             "why": "That is ten times too small: 2000 × 0.40 comes to eight "
                    "hundred."},
            {"text": "800 J", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s22",
        "band": "standard",
        "text": "A jack handle is pushed with 40 N and moves 0.25 m on each "
                "stroke. How many strokes supply 900 J?",
        "options": [
            {"text": "Twenty-two, because 900 ÷ 40 comes to about "
                     "twenty-two strokes",
             "correct": False,
             "why": "Dividing by the force alone leaves the distance out of "
                    "the sum entirely."},
            {"text": "Ninety, because each stroke supplies 10 J",
             "correct": True},
            {"text": "Nine, because each stroke supplies a hundred joules",
             "correct": False,
             "why": "Each stroke supplies 40 × 0.25 = 10 J, not a hundred."},
            {"text": "Thirty-six, from 900 ÷ 25",
             "correct": False,
             "why": "Dividing by 25 uses centimetres. The distance has to go "
                    "into the sum in metres."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s23",
        "band": "standard",
        "text": "Oiling a lever's fulcrum makes the measured input closer to "
                "the output. Why does it never reach it?",
        "options": [
            {"text": "Because the measuring instruments are never accurate "
                     "enough to show the two as equal",
             "correct": False,
             "why": "Better instruments would show the gap more clearly, not "
                    "make it vanish."},
            {"text": "Because oil adds its own weight to the bar, which needs "
                     "extra energy to lift each time",
             "correct": False,
             "why": "A drop of oil weighs almost nothing. The remaining "
                    "friction is what keeps the gap open."},
            {"text": "Because oil cannot remove friction completely, so a "
                     "little always goes to thermal stores",
             "correct": True},
            {"text": "Because oil makes a machine work more slowly",
             "correct": False,
             "why": "Oil makes it easier, not slower, and speed does not "
                    "appear in the energy sum."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s24",
        "band": "standard",
        "text": "A real ramp has friction. Is the energy you actually supply "
                "more or less than force times height?",
        "options": [
            {"text": "Less, because the ramp takes some of the weight",
             "correct": False,
             "why": "The ramp changes the force, not the energy. Friction "
                    "means you supply extra."},
            {"text": "Exactly the same, because the load ends up at the same "
                     "height either way",
             "correct": False,
             "why": "That would be true without friction. With friction you "
                    "always supply a little more."},
            {"text": "Less, because a long ramp needs a much smaller force "
                     "than lifting straight up",
             "correct": False,
             "why": "A smaller force over a longer distance gives the same "
                    "energy, and friction adds to it."},
            {"text": "More, because friction fills thermal stores as well",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s25",
        "band": "standard",
        "text": "Two crowbars, one 1 m long and one 2 m long, are used to "
                "lift the same slab the same height. Compare them.",
        "options": [
            {"text": "Both bars need the same force",
             "correct": False,
             "why": "The arm lengths differ, so the forces differ. Only the "
                    "energy stays put."},
            {"text": "The 2 m bar needs less force and less energy, which is "
                     "why longer bars are chosen",
             "correct": False,
             "why": "The energy is set by the slab and the height. Only the "
                    "force changes."},
            {"text": "The 2 m bar needs more force",
             "correct": False,
             "why": "A longer bar needs LESS force. That is the whole reason "
                    "for using one."},
            {"text": "The 2 m bar needs less force, and the same energy",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s26",
        "band": "standard",
        "text": "Why does sliding a crowbar further under a slab, so the "
                "fulcrum sits close to it, make lifting easier?",
        "options": [
            {"text": "Because the slab becomes lighter once part of it is "
                     "resting on the bar itself",
             "correct": False,
             "why": "Its weight has not changed. What changed is how the "
                    "force is traded."},
            {"text": "Because the load arm is now very short and your arm is "
                     "very long",
             "correct": True},
            {"text": "Because the bar can store energy in itself and then "
                     "release it into the slab",
             "correct": False,
             "why": "A stiff bar stores almost nothing and gives back what "
                    "little it takes."},
            {"text": "Because the ground pushes upwards with the extra force "
                     "and the bar passes it on",
             "correct": False,
             "why": "The ground holds the fulcrum up but supplies no extra "
                    "energy at all."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s27",
        "band": "standard",
        "text": "A screw advances 2 mm for every full turn of its head. What "
                "does that tell you about the trade?",
        "options": [
            {"text": "Your hand travels a long way round for a tiny advance, "
                     "so the force is multiplied",
             "correct": True},
            {"text": "Your hand travels a tiny way round for a long advance, "
                     "so the distance is multiplied instead",
             "correct": False,
             "why": "It is the other way round: a lot of turning gives a very "
                    "small forward movement."},
            {"text": "The energy you supply is multiplied by the number of "
                     "turns you make altogether",
             "correct": False,
             "why": "Energy is never multiplied. Each turn supplies its own "
                    "share and no more."},
            {"text": "Nothing at all, because a screw is not a machine",
             "correct": False,
             "why": "A screw is a simple machine, and 2 mm per turn is "
                    "exactly the trade it makes."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s28",
        "band": "standard",
        "text": "A winch raises a 1200 N load through 3 m. How much energy "
                "arrives at the load?",
        "options": [
            {"text": "400 J", "correct": False,
             "why": "That is 1200 ÷ 3. Energy is force multiplied by "
                    "distance, not divided by it."},
            {"text": "1203 J", "correct": False,
             "why": "That adds them, and a force cannot be added to a "
                    "distance."},
            {"text": "3600 J", "correct": True},
            {"text": "36 000 J", "correct": False,
             "why": "That is ten times too big. 1200 × 3 comes to three "
                    "thousand six hundred."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s29",
        "band": "standard",
        "text": "As the fulcrum slides along the bar, which quantity in the "
                "lever rule is the one that does not change?",
        "options": [
            {"text": "The force at your end",
             "correct": False,
             "why": "Your force is exactly what moving the fulcrum changes."},
            {"text": "The distance your end travels, which is set by how far "
                     "you can reach",
             "correct": False,
             "why": "Your distance changes too, in the opposite direction to "
                    "your force."},
            {"text": "The distance the load rises",
             "correct": False,
             "why": "The load's rise changes as well, unless you deliberately "
                    "hold it fixed."},
            {"text": "The product of force and distance at each end",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s30",
        "band": "standard",
        "text": "Some machines multiply distance instead of force. Which of "
                "these is an example?",
        "options": [
            {"text": "A long ramp, where a gentle push raises a barrel",
             "correct": False,
             "why": "A ramp multiplies force as well, over a longer distance "
                    "than the height gained."},
            {"text": "A crowbar, where a small push lifts a very heavy slab",
             "correct": False,
             "why": "A crowbar multiplies force. Your end travels much "
                    "further than the slab."},
            {"text": "A block and tackle, where one person raises a huge load",
             "correct": False,
             "why": "That multiplies force too, and pays for it in rope "
                    "pulled through."},
            {"text": "A pair of tweezers, where a small squeeze moves the "
                     "tips a long way",
             "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 top-up · harder ─────────────────────────────────
    {
        "id": "p1-08-h07",
        "band": "harder",
        "text": "Why is it allowed to multiply a force but not to multiply "
                "the energy?",
        "options": [
            {"text": "Because force is a conserved quantity and energy is "
                     "not, so only energy is fixed",
             "correct": False,
             "why": "That is the two the wrong way round. Energy is the "
                    "conserved one."},
            {"text": "Because energy is always conserved and force is not",
             "correct": True},
            {"text": "Because a force is measured in newtons",
             "correct": False,
             "why": "Units decide nothing here. It is conservation that "
                    "forbids one and permits the other."},
            {"text": "Because only machines may do it",
             "correct": False,
             "why": "Your own forearm multiplies force in reverse every time "
                    "you lift. Machines are not special."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h08",
        "band": "harder",
        "text": "A run of the lever bench records 25 J in and 23 J out. Where "
                "has the difference gone?",
        "options": [
            {"text": "It was destroyed by the rubbing at the fulcrum during "
                     "the lift",
             "correct": False,
             "why": "Rubbing destroys nothing. It moves energy into a thermal "
                    "store."},
            {"text": "It was never supplied, and the 32 J is a misreading",
             "correct": False,
             "why": "The reading is real, and it is larger than the output "
                    "every single time."},
            {"text": "It is still stored in the bent bar and comes back later",
             "correct": False,
             "why": "A stiff bar bends very little and gives back what little "
                    "it takes."},
            {"text": "It filled a thermal store at the fulcrum",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h09",
        "band": "harder",
        "text": "The bench's measured input scatters upward only. Why would a "
                "scatter in both directions be wrong?",
        "options": [
            {"text": "Because a downward scatter would show a machine giving "
                     "out more than it took in",
             "correct": True},
            {"text": "Because measurements taken in a school laboratory will "
                     "always scatter in one direction only",
             "correct": False,
             "why": "Most measurements scatter both ways. This one does not, "
                    "and the physics is the reason."},
            {"text": "Because friction is too small to be measured by a force "
                     "meter on a school bench",
             "correct": False,
             "why": "Friction here is easily large enough to read, which is "
                    "why the scatter shows at all."},
            {"text": "Because the bench was built to look tidy on the screen",
             "correct": False,
             "why": "It is one-sided because friction is one-sided, not for "
                    "the sake of appearance."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h10",
        "band": "harder",
        "text": "A crate is pushed up a real ramp with friction. Compare the "
                "energy supplied with the gain in the gravitational store.",
        "options": [
            {"text": "The supply is smaller, because the ramp takes some of "
                     "the load off the person pushing",
             "correct": False,
             "why": "The ramp changes the force, not the energy. Friction "
                    "makes the supply larger."},
            {"text": "The supply is exactly equal, because the crate ends at "
                     "the same height whichever route it took",
             "correct": False,
             "why": "That would be true with no friction. A real ramp always "
                    "needs a little extra."},
            {"text": "The supply is larger, because friction fills a thermal "
                     "store on the way up",
             "correct": True},
            {"text": "The two cannot be compared, since one is a force",
             "correct": False,
             "why": "Both are energies in joules, so they compare directly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h11",
        "band": "harder",
        "text": "A 750 N load is pushed up a 5 m ramp to a height of 1 m. "
                "Ignoring friction, what force is needed?",
        "options": [
            {"text": "3750 N, found by multiplying the load by the length of "
                     "the ramp",
             "correct": False,
             "why": "750 × 5 is not a force at all. The energy is 750 × 1, "
                    "and that is divided by 5."},
            {"text": "750 N, because the load is no lighter",
             "correct": False,
             "why": "Its weight is the same, but the push along the slope is "
                    "a fifth of it."},
            {"text": "375 N, because the ramp halves it",
             "correct": False,
             "why": "The ramp divides by five, not by two. The ratio is 5 m "
                    "to 1 m."},
            {"text": "150 N, because 750 × 1 = 750 J and 750 ÷ 5 = 150",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h12",
        "band": "harder",
        "text": "Doubling the length of your side of a lever halves the force "
                "you need. Why does it not halve the energy?",
        "options": [
            {"text": "Because the load is raised twice as high",
             "correct": False,
             "why": "The load rises the same height. It is YOUR end that "
                    "travels twice as far."},
            {"text": "Because the longer bar is a great deal heavier and takes "
                     "the saving back in lifting itself",
             "correct": False,
             "why": "The bar's own weight is a small extra. The real reason "
                    "is the distance your end travels."},
            {"text": "Because your end now has to travel twice as far",
             "correct": True},
            {"text": "Because a longer bar has more friction at the fulcrum "
                     "than a short one does",
             "correct": False,
             "why": "Friction adds a little either way. Even with none, the "
                    "energy would be unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h13",
        "band": "harder",
        "text": "Evaluate: “a block and tackle with more rope sections "
                "gives you more energy to work with.”",
        "options": [
            {"text": "Correct, because each extra rope section adds a share of "
                     "its own to the total energy",
             "correct": False,
             "why": "A rope section adds no energy. It divides the force and "
                    "multiplies the rope pulled."},
            {"text": "Wrong — it gives more FORCE, and takes more rope",
             "correct": True},
            {"text": "Correct, while the rope runs free",
             "correct": False,
             "why": "Frictionless or not, no arrangement of rope creates "
                    "energy."},
            {"text": "Wrong, because extra rope sections change nothing at "
                     "all about the lift",
             "correct": False,
             "why": "They change the force a great deal, which is the whole "
                    "point of using them."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h14",
        "band": "harder",
        "text": "A gear train gives a drill four times the turning force. "
                "What has happened to how fast the bit turns?",
        "options": [
            {"text": "It turns four times as fast, because the gears have "
                     "multiplied both together",
             "correct": False,
             "why": "Multiplying both would be energy for nothing. One of the "
                    "two has to fall."},
            {"text": "It turns at the same speed, because gears only change "
                     "the force and never the speed",
             "correct": False,
             "why": "If the speed were unchanged, the energy each second "
                    "would have been multiplied by four."},
            {"text": "It cannot be said without knowing the motor's power "
                     "rating in watts",
             "correct": False,
             "why": "The trade follows from the gear ratio alone, whatever "
                    "the motor is rated at."},
            {"text": "It turns a quarter as fast",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h15",
        "band": "harder",
        "text": "Why can no simple machine multiply the force AND the "
                "distance at the same time?",
        "options": [
            {"text": "Because the product of the two is the energy, and that "
                     "can never be increased",
             "correct": True},
            {"text": "Because no material is stiff enough to carry both at "
                     "once without bending badly",
             "correct": False,
             "why": "Stiffness is not the limit. No arrangement of any "
                    "material could do it."},
            {"text": "Because a machine can only ever change one quantity in "
                     "a single job",
             "correct": False,
             "why": "It changes both — one up and one down. What it cannot do "
                    "is raise both."},
            {"text": "Because friction always cancels one of the two out",
             "correct": False,
             "why": "Friction reduces the output a little. Even with none, "
                    "both could not rise."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h16",
        "band": "harder",
        "text": "Patent offices refuse perpetual-motion applications without "
                "a working model. What makes that reasonable?",
        "options": [
            {"text": "Because no inspector could ever understand a design of "
                     "that kind well enough to judge it",
             "correct": False,
             "why": "The designs are usually simple. What rules them out is a "
                    "law, not a difficulty."},
            {"text": "Because the law forbids the whole class, so no design "
                     "needs inspecting on its own",
             "correct": True},
            {"text": "Because such machines are dangerous, and a working "
                     "model shows they can be operated safely",
             "correct": False,
             "why": "Safety is not the issue. The machines simply do not "
                    "work."},
            {"text": "Because the patent office lacks the equipment",
             "correct": False,
             "why": "No equipment is needed. Conservation of energy settles "
                    "it without any measurement."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h17",
        "band": "harder",
        "text": "You want a lever that lifts 1200 N using 200 N. What must be "
                "true of the two arm lengths?",
        "options": [
            {"text": "The load arm must be six times the effort arm, so the "
                     "load end travels furthest",
             "correct": False,
             "why": "That would make the lift harder, not easier. The effort "
                    "arm is the long one."},
            {"text": "Both arms must be exactly the same length as one "
                     "another for the lever to balance",
             "correct": False,
             "why": "Equal arms give equal forces, so you would need the "
                    "whole 1200 N."},
            {"text": "The effort arm must be six times the load arm",
             "correct": True},
            {"text": "The arms can be any length, because a lever always "
                     "multiplies force by six",
             "correct": False,
             "why": "The multiplication comes entirely from the ratio of the "
                    "arms, so length is everything."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h18",
        "band": "harder",
        "text": "Why does this lesson use a triangle for E = F × d and a beam "
                "for the lever rule, rather than one shape?",
        "options": [
            {"text": "Because a triangle is meant for younger students and a "
                     "beam for older ones doing the same work",
             "correct": False,
             "why": "Both are used here, on one page. Age has nothing to do "
                    "with it."},
            {"text": "Because a triangle holds one product and a beam holds "
                     "two, either side of an equals sign",
             "correct": True},
            {"text": "Because a triangle works for forces and a beam works "
                     "for energies and distances",
             "correct": False,
             "why": "Both shapes carry forces and distances. It is the SHAPE "
                    "of the relationship that decides."},
            {"text": "Because a beam is easier to draw than a triangle is",
             "correct": False,
             "why": "Drawing is not the reason. The two shapes encode "
                    "genuinely different relationships."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h19",
        "band": "harder",
        "text": "The bench's live readout says 600 N and the recorded table "
                "says 612 N for the same fulcrum. Why the difference?",
        "options": [
            {"text": "The readout is faulty and should be ignored in favour "
                     "of the recorded value",
             "correct": False,
             "why": "Neither is faulty. One is an ideal figure and the other "
                    "a measured one."},
            {"text": "The readout shows the ideal lever and the table shows a "
                     "measured one with friction",
             "correct": True},
            {"text": "The table rounds every single reading up to the nearest "
                     "whole twelve newtons before printing",
             "correct": False,
             "why": "No such rounding happens. The extra is friction, and it "
                    "varies from run to run."},
            {"text": "The load changed weight between the two readings",
             "correct": False,
             "why": "The load is fixed at 600 N throughout. Only the measured "
                    "effort differs."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h20",
        "band": "harder",
        "text": "Suppose a lever could be built with perfect frictionless "
                "bearings. Could its output then exceed its input?",
        "options": [
            {"text": "Yes, because with no friction nothing would hold the "
                     "output back",
             "correct": False,
             "why": "Friction is what makes the output fall SHORT. Removing "
                    "it reaches the input, never passes it."},
            {"text": "Yes, but only by an amount too small to measure",
             "correct": False,
             "why": "Not by any amount. Creation of energy is forbidden "
                    "outright."},
            {"text": "No, because the two would then be exactly equal and never "
                     "any more",
             "correct": True},
            {"text": "No, because perfect bearings would seize up instead",
             "correct": False,
             "why": "The answer does not depend on whether such bearings can "
                    "be made. The law settles it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h21",
        "band": "harder",
        "text": "A load must be raised 1 m. Compare a 4 m ramp with a pulley "
                "having four rope sections, ignoring friction.",
        "options": [
            {"text": "Both quarter the force, and both need the same energy",
             "correct": True},
            {"text": "The ramp quarters the force and the pulley quarters the "
                     "energy as well as the force",
             "correct": False,
             "why": "Neither touches the energy. Only the force is divided."},
            {"text": "The pulley quarters the force and the ramp leaves the "
                     "force exactly as it was",
             "correct": False,
             "why": "A 4 m ramp for a 1 m rise quarters the force just as the "
                    "pulley does."},
            {"text": "Neither changes the force, only the direction of pull",
             "correct": False,
             "why": "Both divide the force by four. A single pulley changes "
                    "only direction, but four sections do more."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h22",
        "band": "harder",
        "text": "Two ramps, 3 m and 6 m long, raise the same load to the same "
                "height. Compare force, distance and energy.",
        "options": [
            {"text": "The 6 m ramp needs half the force, twice the distance, "
                     "and the same energy",
             "correct": True},
            {"text": "The 6 m ramp needs half the force, half the distance and "
                     "the energy",
             "correct": False,
             "why": "Halving both would be energy for nothing. A smaller "
                    "force must travel further."},
            {"text": "The 6 m ramp needs twice the force and half the distance",
             "correct": False,
             "why": "A longer ramp needs LESS force, not more. The trade runs "
                    "the other way."},
            {"text": "Both need the same force and the same energy",
             "correct": False,
             "why": "The forces differ by a factor of two. Only the energy "
                    "stays put."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h23",
        "band": "harder",
        "text": "Does raising a load slowly need less energy than raising the "
                "same load the same height quickly?",
        "options": [
            {"text": "Yes, because working slowly is much less tiring than "
                     "working quickly at the same job",
             "correct": False,
             "why": "Tiredness is about your body, not about the energy the "
                    "load receives."},
            {"text": "Yes, because a slow lift gives the energy more time to "
                     "spread itself out evenly",
             "correct": False,
             "why": "Time does not appear in force times distance at all."},
            {"text": "No, because the energy depends on force and distance, "
                     "and neither has changed",
             "correct": True},
            {"text": "No, because a slow lift needs more energy than a fast "
                     "one over the same height",
             "correct": False,
             "why": "It needs the same. Speed changes the power, which is "
                    "energy per second, not the total."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h24",
        "band": "harder",
        "text": "Evaluate: “friction is always a bad thing in a "
                "machine.”",
        "options": [
            {"text": "Correct, because friction takes a share of the energy "
                     "away from every job",
             "correct": False,
             "why": "It does take a share, but a machine with no friction "
                    "anywhere would be unusable."},
            {"text": "Correct, and a machine with none at all would be a "
                     "perfect one in every way",
             "correct": False,
             "why": "Belts would slip, screws would undo and brakes would "
                    "fail. None of that is perfect."},
            {"text": "Wrong, because friction does not cost a machine any "
                     "energy in the first place",
             "correct": False,
             "why": "It certainly costs energy. That half of the statement "
                    "is right."},
            {"text": "Wrong — it costs energy, but grip, brakes and screws "
                     "all depend on it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h25",
        "band": "harder",
        "text": "A block and tackle with five rope sections raises a load "
                "0.40 m. How much rope must be pulled through?",
        "options": [
            {"text": "0.08 m, because the rope is divided between the five "
                     "sections of the tackle",
             "correct": False,
             "why": "Dividing would mean getting energy free. A smaller force "
                    "must move further."},
            {"text": "0.40 m, because the load and the rope always move the "
                     "same distance as each other",
             "correct": False,
             "why": "If both moved the same, the tackle would be multiplying "
                    "energy by five."},
            {"text": "2.0 m", "correct": True},
            {"text": "5.0 m, because there are five sections of rope",
             "correct": False,
             "why": "The five multiplies the RISE, not a metre. 5 × 0.40 is "
                    "two metres."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h26",
        "band": "harder",
        "text": "A screw jack lifts a car with a force one person can manage. "
                "What is being traded, and for what?",
        "options": [
            {"text": "A small force turning a long way round, for a large "
                     "force moving a very short way",
             "correct": True},
            {"text": "A small force turning a long way round, for a large "
                     "force moving just as far",
             "correct": False,
             "why": "If the load moved just as far, the jack would be "
                    "creating energy."},
            {"text": "A large force turning a short way round, for a small "
                     "force moving a long way up",
             "correct": False,
             "why": "That is the jack in reverse. The person supplies the "
                    "small force."},
            {"text": "Nothing at all — a jack simply makes a car lighter",
             "correct": False,
             "why": "The car's weight is unchanged. Only the force needed at "
                    "the handle is."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h27",
        "band": "harder",
        "text": "A student writes “40 cm = 0.04 m” in the C step. "
                "What has gone wrong, and what follows?",
        "options": [
            {"text": "Nothing has gone wrong, and the answer that follows "
                     "will be exactly right",
             "correct": False,
             "why": "40 cm is 0.40 m. The conversion used is ten times too "
                    "strong."},
            {"text": "They divided by a thousand rather than a hundred, so "
                     "the answer will come out ten times too small",
             "correct": True},
            {"text": "They divided by ten rather than a hundred, so the "
                     "answer will come out ten times too big",
             "correct": False,
             "why": "Dividing by ten would give 4 m. They have gone the other "
                    "way and produced 0.04 m."},
            {"text": "They multiplied instead of dividing, so the answer will "
                     "be a hundred times too large",
             "correct": False,
             "why": "Multiplying would give 4000 m. The error made the number "
                    "smaller, not bigger."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h28",
        "band": "harder",
        "text": "Why must the energy supplied to any real machine be at least "
                "as much as the energy delivered?",
        "options": [
            {"text": "Because machines are built with a safety margin that "
                     "always uses a little extra",
             "correct": False,
             "why": "No margin is designed in. The law forbids the output "
                    "exceeding the input at all."},
            {"text": "Because the load is always heavier than the effort in a "
                     "machine worth using",
             "correct": False,
             "why": "That is about forces. The rule here is about energies, "
                    "and it holds whichever is heavier."},
            {"text": "Because nothing creates energy, so the output can only "
                     "match the input or fall short",
             "correct": True},
            {"text": "Because measuring the input always overestimates it",
             "correct": False,
             "why": "The gap is real rather than a measurement artefact, and "
                    "a better meter shows the same thing."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h29",
        "band": "harder",
        "text": "How would you measure how much energy a lever loses to "
                "friction in a single lift?",
        "options": [
            {"text": "Measure the load and the height only, and take the "
                     "answer as the loss",
             "correct": False,
             "why": "That gives the useful output. The loss is the difference "
                    "between input and output."},
            {"text": "Time the lift and multiply by the force at the effort "
                     "end of the bar",
             "correct": False,
             "why": "Time does not belong in force times distance, so that "
                    "product is not an energy."},
            {"text": "Weigh the bar before and after the lift and find the "
                     "difference in its mass",
             "correct": False,
             "why": "Nothing changes mass. A balance cannot follow energy "
                    "into a thermal store."},
            {"text": "Measure force and distance at both ends, and subtract "
                     "output from input",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h30",
        "band": "harder",
        "text": "Why can a person with a crowbar lift a slab that their "
                "muscles could never lift directly?",
        "options": [
            {"text": "Because the bar supplies the extra force from its own "
                     "strength as it bends",
             "correct": False,
             "why": "A bar supplies nothing. Every newton at the load end "
                    "came from the person's push."},
            {"text": "Because the slab weighs less once one end of it is "
                     "resting on the crowbar",
             "correct": False,
             "why": "Its weight is unchanged. What changed is how the force "
                    "is applied."},
            {"text": "Because the job is spread over a longer push, so a "
                     "force their muscles can make is enough",
             "correct": True},
            {"text": "Because a crowbar reduces the energy the job needs",
             "correct": False,
             "why": "The job needs the same energy. Only the force has been "
                    "traded against distance."},
        ],
        "figure": None,
    },
]
