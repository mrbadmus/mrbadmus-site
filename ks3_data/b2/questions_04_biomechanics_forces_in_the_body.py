"""B2 lesson 04 — Biomechanics: forces in the body: twelve questions (MRB-269).

These probe the one relationship the lesson is built on — turning effect =
force × distance from the joint — and the trade it forces on every muscle in
the body: attach close in, pay in force, get back speed and distance. The
distractors are built from the lesson's two declared misconceptions, BODY-10
(a muscle pulls with the same force as the weight it is holding) and BODY-11
(the arm is a lever, and levers make things easier, so the muscle pulls less
than the weight). Around those sit the errors the calculation itself throws
up: multiplying when the triangle says divide, dividing the wrong way up,
losing a decimal place, converting mass to weight by swapping the unit rather
than by × 10 N/kg, and reading the biceps meter as if the force at the hand
were the force in the muscle. The `harder` band takes the rule to three places
the lesson never goes — a jaw closing on back teeth rather than front, a robot
arm with its motor bolted five times further out, and two animal forelimbs
tuned opposite ways — and turns the #s-meters data back on itself.
"""

UNIT = "B2"
LESSON = "biomechanics-forces-in-the-body"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b2-04-e01",
        "band": "easier",
        "text": "Two things decide how much a force turns a bone about a "
                "joint. Which pair?",
        "options": [
            {"text": "How big the force is, and how heavy the bone being "
                     "turned is.",
             "correct": False,
             "why": "The bone's own weight is left out all the way through "
                    "this lesson. Turning effect takes the size of the force "
                    "and its distance from the joint, and nothing else."},
            {"text": "How big the force is, and how far from the joint it "
                     "acts.",
             "correct": True},
            {"text": "How long the muscle is, and how far from the joint it "
                     "acts.",
             "correct": False,
             "why": "Muscle length never enters it. The distance that counts "
                    "runs from the joint to the point where the force acts — "
                    "4 cm for the biceps, not the length of the biceps."},
            {"text": "How big the force is, and how fast the bone ends up "
                     "moving.",
             "correct": False,
             "why": "Speed is what the arrangement buys you, not what sets "
                    "the turning effect. The turning effect is decided before "
                    "anything has moved at all."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e02",
        "band": "easier",
        "text": "You multiply a force in newtons by a distance in metres to "
                "get a turning effect. What unit does that answer carry?",
        "options": [
            {"text": "N m — a newton multiplied by a metre.",
             "correct": True},
            {"text": "N — the same unit as the force itself.",
             "correct": False,
             "why": "A turning effect is not a force. It is a force "
                    "multiplied by a distance, so the metres have to show up "
                    "in the unit as well."},
            {"text": "m — the same unit as the distance itself.",
             "correct": False,
             "why": "Same problem the other way round: now the newtons have "
                    "gone missing. Both quantities were multiplied, so both "
                    "units stay in the answer."},
            {"text": "N/m — newtons shared out over each metre.",
             "correct": False,
             "why": "A slash means divided by, and nothing here was divided. "
                    "Two things side by side means multiply, and the unit "
                    "follows the arithmetic: N m."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e03",
        "band": "easier",
        "text": "A 3 kg load hangs from someone's hand. What weight, in "
                "newtons, is the number that goes into the arithmetic?",
        "options": [
            {"text": "3 N — the number stays and only the unit changes.",
             "correct": False,
             "why": "Mass and weight are different quantities, so swapping "
                    "the unit is not a conversion. Every kilogram is worth "
                    "10 N, which makes 3 kg worth 30 N."},
            {"text": "0.3 N — you divide the mass by ten.",
             "correct": False,
             "why": "That is the conversion upside down. Weight in newtons is "
                    "mass in kilograms × 10 N/kg, so the number gets ten "
                    "times bigger, not ten times smaller."},
            {"text": "30 N — you multiply the mass by ten.",
             "correct": True},
            {"text": "300 N — you multiply the mass by a hundred.",
             "correct": False,
             "why": "It is × 10, not × 100. Check it against the worked "
                    "example: the 2 kg dumbbell weighs 20 N there, not "
                    "200 N."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e04",
        "band": "easier",
        "text": "Three pulls on a hand grip meter read 312 N, 298 N and "
                "305 N, and the result is reported as a mean of 305 N. Why "
                "report a mean instead of one reading?",
        "options": [
            {"text": "Because the meter only settles by the third go, so the "
                     "first two have to be averaged in.",
             "correct": False,
             "why": "Nothing was wrong with the first two readings. Repeats "
                    "of the same pull simply vary, which is why all three go "
                    "into the mean rather than being thrown away."},
            {"text": "Because a mean is bigger than any single reading, and "
                     "muscle force is easily underestimated.",
             "correct": False,
             "why": "A mean sits among its readings, not above them — 305 N "
                    "is smaller than 312 N. It is used because repeats "
                    "differ, never to push a figure up."},
            {"text": "Because the mean turns the readings into newtons, which "
                     "one pull on its own does not give.",
             "correct": False,
             "why": "Each pull was already measured in newtons. A mean deals "
                    "with the spread between repeats; it does not change the "
                    "quantity being measured."},
            {"text": "Because three readings of the same pull are never "
                     "identical, so one alone proves little.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b2-04-s01",
        "band": "standard",
        "text": "On the forearm rig you leave the 2 kg load out at 32 cm and "
                "slide the muscle attachment from 4 cm to 8 cm from the "
                "elbow. What happens to the force the muscle needs?",
        "options": [
            {"text": "It doubles, because the muscle now sits twice as far "
                     "from the elbow.",
             "correct": False,
             "why": "Bigger distance, smaller force. Cover F on the triangle "
                    "and you are left with T ÷ d, so doubling d halves F: "
                    "160 N becomes 80 N."},
            {"text": "It stays the same, because the load and its distance "
                     "have not changed.",
             "correct": False,
             "why": "This is the idea the rig exists to break. The muscle "
                    "force depends on both distances, not on the load alone — "
                    "give the muscle more distance and it needs less pull."},
            {"text": "It halves, because the muscle now has twice the "
                     "distance to work with.",
             "correct": True},
            {"text": "It falls to a quarter, because doubling the distance "
                     "quarters the force.",
             "correct": False,
             "why": "The two are in simple proportion, not squared. The "
                    "turning effect of 6.4 N m divided by 0.08 m is 80 N, "
                    "which is half of 160 N and not a quarter."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s02",
        "band": "standard",
        "text": "Holding a 10 N bag of sugar on a flat hand, someone says "
                "“my biceps must be pulling with 10 N, because that is "
                "what the bag weighs”. What is wrong with that?",
        "options": [
            {"text": "The muscle acts much closer to the elbow than the "
                     "bag, so it needs a far bigger pull.",
             "correct": True},
            {"text": "Nothing is wrong — nothing is moving, so the two forces "
                     "have to be equal to each other.",
             "correct": False,
             "why": "What is equal is the two turning effects, not the two "
                    "forces. Equal turning effects with very unequal "
                    "distances means very unequal forces: about 80 N against "
                    "10 N."},
            {"text": "The biceps pulls less than 10 N, because an arm is a "
                     "lever and levers make a job easier.",
             "correct": False,
             "why": "This lever is arranged the other way round. It buys "
                    "speed and distance at the hand, and the price it pays is "
                    "force — eight times the weight, every time."},
            {"text": "The biceps does pull 10 N, and the bones of the forearm "
                     "carry the rest of the load.",
             "correct": False,
             "why": "Bones do not pull. All of the upward force at the tendon "
                    "is the muscle's own, and the arithmetic puts it at about "
                    "80 N for a 10 N bag."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s03",
        "band": "standard",
        "text": "A load has a turning effect of 8 N m about a shoulder joint, "
                "and the muscle holding it pulls with 400 N. How far from the "
                "joint is that muscle attached?",
        "options": [
            {"text": "3200 m, because 8 × 400 comes to 3200.",
             "correct": False,
             "why": "Cover d on the triangle and T sits over F, so this is a "
                    "division. Multiplying two of the three only works when "
                    "the one you covered is on top."},
            {"text": "50 m, because 400 ÷ 8 comes to 50.",
             "correct": False,
             "why": "Right operation, wrong way up. T is the one on top, so "
                    "it is 8 ÷ 400 — and 50 m from a shoulder joint is longer "
                    "than the person."},
            {"text": "0.2 m, because 8 ÷ 400 comes to 0.2.",
             "correct": False,
             "why": "The right division, but the decimal point has slipped. "
                    "8 ÷ 400 is 0.02, and the difference matters: 2 cm from "
                    "the joint, not 20 cm."},
            {"text": "0.02 m, because 8 ÷ 400 comes to 0.02.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s04",
        "band": "standard",
        "text": "A leg press, a hand grip and a biceps pull were each "
                "measured three times on the same person, giving means of "
                "1422 N, 305 N and 203 N. What does that set of three show?",
        "options": [
            {"text": "That the legs were tested fresh and the arms tested "
                     "once the person was already tired.",
             "correct": False,
             "why": "All three were measured the same way by the same person. "
                    "The pattern tracks the size of the muscle group, and "
                    "nothing in the readings points at tiredness."},
            {"text": "That the bigger the group of muscles, the bigger the "
                     "force it is able to exert.",
             "correct": True},
            {"text": "That a force meter reads higher the nearer it is held "
                     "to the joint being used.",
             "correct": False,
             "why": "A meter reads the force in the pull it is fitted to; "
                    "moving it does not change what it reads. These three "
                    "numbers differ because the muscle groups differ."},
            {"text": "That the biceps is the weakest muscle in the body, "
                     "since it gave the smallest number.",
             "correct": False,
             "why": "Only three groups were tested, so the smallest of three "
                    "is not the smallest in the body. What the set supports "
                    "is that bigger groups pull harder."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b2-04-h01",
        "band": "harder",
        "text": "The muscle that closes your jaw attaches close to the jaw "
                "joint. Your back teeth sit much nearer that joint than your "
                "front teeth do. Which bite is stronger?",
        "options": [
            {"text": "The front teeth, because they are further from the "
                     "joint, and further out always means more force.",
             "correct": False,
             "why": "Further out means more turning effect for a given force "
                    "— but here the turning effect is fixed by the muscle. "
                    "Cover F and F = T ÷ d, so a bigger d gives less force."},
            {"text": "The back teeth, because they sit closer to the "
                     "joint, so the same turning effect gives more force.",
             "correct": True},
            {"text": "Both are the same, because it is one muscle pulling "
                     "with one force whichever teeth you happen to use.",
             "correct": False,
             "why": "The muscle's pull is the same, but the force delivered "
                    "at a tooth is not. That depends on how far the tooth "
                    "sits from the joint."},
            {"text": "The front teeth, because the jaw is a lever, and a "
                     "lever makes the job easier at its far end.",
             "correct": False,
             "why": "Levers do not hand out free force. What is gained in "
                    "distance is paid for in force, so the far end of a lever "
                    "is the weak end — which is why you chew at the back."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h02",
        "band": "harder",
        "text": "An engineer copies a human arm but bolts the motor 20 cm "
                "from the joint instead of 4 cm, with the gripper still 32 cm "
                "out. Against your own arm, what has that design traded?",
        "options": [
            {"text": "Less force needed and a faster gripper too, so the "
                     "design beats a human arm on both counts.",
             "correct": False,
             "why": "Nothing gives you both. The force needed falls and the "
                    "movement at the gripper falls in the same proportion — "
                    "that is the trade, and it runs one way only."},
            {"text": "More force needed, because the motor now sits further "
                     "from the joint than a biceps does.",
             "correct": False,
             "why": "The other way round. F = T ÷ d, so five times the "
                    "distance needs a fifth of the force: where your biceps "
                    "needs 160 N, this motor needs about 32 N."},
            {"text": "Nothing has changed, because the load and its distance "
                     "from the joint are exactly the same.",
             "correct": False,
             "why": "The load's turning effect is unchanged, but the motor "
                    "now has five times the distance to work with, so the "
                    "force it must produce drops to a fifth."},
            {"text": "Less force needed, but the gripper now moves far less "
                     "for the same movement of the motor.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h03",
        "band": "harder",
        "text": "The biceps mean of 203 N came from pulling straight up on a "
                "meter held in the hand. Someone says it proves the biceps "
                "can only ever produce about 203 N. Why is that wrong?",
        "options": [
            {"text": "203 N is the force out at the hand; the biceps "
                     "attaches close in and must pull far harder.",
             "correct": True},
            {"text": "The mean of 196 N, 210 N and 203 N is not 203 N, so the "
                     "reported figure is wrong to start with.",
             "correct": False,
             "why": "Check it: 196 + 210 + 203 is 609, and 609 ÷ 3 is 203. "
                    "The mean is right. What it measures is the force at the "
                    "hand, not the force inside the muscle."},
            {"text": "Three readings can never show what a muscle is capable "
                     "of, however carefully they were each taken.",
             "correct": False,
             "why": "Repeating is what makes a reading trustworthy, not what "
                    "limits it. The problem here is where the meter was, not "
                    "how many times it was read."},
            {"text": "Nothing is wrong — a force meter fitted anywhere on the "
                     "arm would read the muscle's own pull.",
             "correct": False,
             "why": "A meter reads the force where it sits. Fitted to the "
                    "tendon it reads the muscle's pull; held in the hand it "
                    "reads what the hand can deliver, which is far smaller."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h04",
        "band": "harder",
        "text": "A badger's digging forelimb has its muscle attached well out "
                "from the elbow. A cheetah's leg muscles attach very close "
                "in. Which limb is built for force, and which for speed?",
        "options": [
            {"text": "The cheetah for force and the badger for speed, since "
                     "attaching close in gives a muscle more room to pull.",
             "correct": False,
             "why": "Attaching close in gives a muscle less distance, not "
                    "more. What it buys is a fast, far-moving paw, and the "
                    "price of that is a much bigger pull."},
            {"text": "Both are built for force, because what a limb can do "
                     "depends on muscle size and on nothing else.",
             "correct": False,
             "why": "Size does matter — the three meter readings show that — "
                    "but so does where the muscle attaches. The same muscle "
                    "gives force or speed depending on its distance."},
            {"text": "The badger for force and the cheetah for speed: "
                     "distance out buys force, distance in buys movement.",
             "correct": True},
            {"text": "Neither — where a muscle attaches makes no difference, "
                     "only how hard the muscle itself is able to pull.",
             "correct": False,
             "why": "It makes all the difference. A biceps attached 4 cm from "
                    "the elbow needs about 80 N to hold a 10 N bag; attach it "
                    "further out and the same bag needs far less."},
        ],
        "figure": None,
    },
]
