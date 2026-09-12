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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b2-04-e05",
        "band": "easier",
        "text": "What is the unit that force is measured in?",
        "options": [
            {"text": "The kilogram, written kg.",
             "correct": False,
             "why": "Kilograms measure mass, which is a different quantity. A "
                    "mass of 1 kg weighs about 10 N."},
            {"text": "The newton, written N.",
             "correct": True},
            {"text": "The newton metre, written N m.",
             "correct": False,
             "why": "N m is the unit of turning effect — a force multiplied "
                    "by a distance. A force on its own is in newtons."},
            {"text": "The metre, written m.",
             "correct": False,
             "why": "Metres measure distance, which is one half of a turning "
                    "effect. The force is the other half."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e06",
        "band": "easier",
        "text": "What is weight?",
        "options": [
            {"text": "The force pulling something down towards the Earth, in "
                     "newtons.",
             "correct": True},
            {"text": "The amount of matter in something, measured in "
                     "kilograms on a top-pan balance.",
             "correct": False,
             "why": "That is mass. Weight is the force that mass is pulled "
                    "down with, and it is measured in newtons."},
            {"text": "How hard something is to lift, measured in kilograms.",
             "correct": False,
             "why": "Half right, in the wrong unit. Weight is a force, so it "
                    "is measured in newtons."},
            {"text": "A mass multiplied by its distance from a joint, "
                     "measured in N m.",
             "correct": False,
             "why": "That is a turning effect. Weight is a force on its own, "
                    "before any distance comes into it."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e07",
        "band": "easier",
        "text": "Turning effect = force × distance from the joint. How do you "
                "find the force?",
        "options": [
            {"text": "Multiply the turning effect by the distance.",
             "correct": False,
             "why": "Multiplying is how the turning effect was made in the "
                    "first place. Getting the force back means undoing that, "
                    "which is a division."},
            {"text": "Divide the distance by the turning effect.",
             "correct": False,
             "why": "The right operation, upside down. The turning effect is "
                    "the one on top: force = turning effect ÷ distance."},
            {"text": "Divide the turning effect by the distance.",
             "correct": True},
            {"text": "Subtract the distance from the turning effect.",
             "correct": False,
             "why": "The two are multiplied together, never added or taken "
                    "away — and a distance cannot be subtracted from a "
                    "turning effect in any case."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e08",
        "band": "easier",
        "text": "Distances go into these calculations as metres. How do you "
                "turn 32 cm into metres?",
        "options": [
            {"text": "Multiply by 100, giving 3200 m.",
             "correct": False,
             "why": "That is the conversion the wrong way round. A metre is "
                    "bigger than a centimetre, so the number has to get "
                    "smaller."},
            {"text": "Divide by 10, giving 3.2 m.",
             "correct": False,
             "why": "There are 100 centimetres in a metre, not 10. A forearm "
                    "3.2 m long would reach across a classroom."},
            {"text": "Multiply by 10, giving 320 m.",
             "correct": False,
             "why": "Wrong number and wrong direction. There are 100 cm in a "
                    "metre, and you divide."},
            {"text": "Divide by 100, giving 0.32 m.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e09",
        "band": "easier",
        "text": "What does the word biomechanics mean?",
        "options": [
            {"text": "The study of the forces at work inside a moving body.",
             "correct": True},
            {"text": "The study of how machines are built to copy the way a "
                     "body moves.",
             "correct": False,
             "why": "Robot designers do borrow from bodies, but biomechanics "
                    "is about the forces inside the body itself."},
            {"text": "The study of how bones grow and repair themselves.",
             "correct": False,
             "why": "That is biology too, but it is not about forces. Forces "
                    "are what make this part of it biomechanics."},
            {"text": "The measurement of how fast a body is able to move.",
             "correct": False,
             "why": "Speed is one of the things the arrangement buys, but the "
                    "subject is the forces the skeleton and muscles work "
                    "with."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e10",
        "band": "easier",
        "text": "Which of these describes a lever?",
        "options": [
            {"text": "A bar that makes any job easier by cutting the force "
                     "needed.",
             "correct": False,
             "why": "A lever does not make a job easier by itself. Your "
                    "forearm is one, and it costs force rather than saving "
                    "it."},
            {"text": "A joint that is able to move in more than one "
                     "direction.",
             "correct": False,
             "why": "That describes a type of joint. A lever is the bar that "
                    "turns, not the place it turns at."},
            {"text": "A rigid bar that turns about a fixed point.",
             "correct": True},
            {"text": "A muscle attached a long way from the joint it moves.",
             "correct": False,
             "why": "Where a muscle attaches decides what the lever costs and "
                    "buys. The lever itself is the bar — in your arm, the "
                    "forearm."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e11",
        "band": "easier",
        "text": "The forearm is a rigid bar that turns about a fixed point. "
                "Which is the fixed point?",
        "options": [
            {"text": "The shoulder.",
             "correct": False,
             "why": "The shoulder is the fixed point for the whole arm "
                    "swinging. The forearm turns at the elbow."},
            {"text": "The elbow.",
             "correct": True},
            {"text": "The place where the biceps attaches, about 4 cm along.",
             "correct": False,
             "why": "That is where the force acts, not where the bar turns. "
                    "Both distances in the calculation are measured from the "
                    "elbow."},
            {"text": "The hand, where the load is held.",
             "correct": False,
             "why": "The hand is where the load acts, about 32 cm out. The "
                    "turning happens at the elbow."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e12",
        "band": "easier",
        "text": "Which of these is measured in newtons?",
        "options": [
            {"text": "The distance from the elbow to the hand.",
             "correct": False,
             "why": "Distances are measured in metres, or in centimetres "
                    "before they are converted."},
            {"text": "The mass of the load being held.",
             "correct": False,
             "why": "Mass is measured in kilograms. Multiply it by 10 N/kg "
                    "and you get the weight, and that is in newtons."},
            {"text": "The turning effect of the load about the elbow.",
             "correct": False,
             "why": "A turning effect is a force multiplied by a distance, so "
                    "its unit is N m."},
            {"text": "The pull of a muscle on its tendon.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-e13",
        "band": "easier",
        "text": "Weight in newtons is taken as mass in kilograms × 10 N/kg. "
                "What is the 10 telling you?",
        "options": [
            {"text": "Each kilogram of mass weighs about 10 N on Earth.",
             "correct": True},
            {"text": "A force is always about ten times bigger than a turning "
                     "effect.",
             "correct": False,
             "why": "They are different quantities and there is no fixed "
                    "ratio between them. The 10 links mass to weight."},
            {"text": "There are 10 centimetres in a metre, so distances are "
                     "divided by 10.",
             "correct": False,
             "why": "There are 100. And this 10 is about turning mass into "
                    "weight, not about distance at all."},
            {"text": "A muscle pulls about ten times harder than the load it "
                     "is holding.",
             "correct": False,
             "why": "That ratio comes from the two distances and it is not "
                    "fixed — for a muscle at 4 cm holding a load at 32 cm it is "
                    "eight. The 10 turns mass into weight."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b2-04-s05",
        "band": "standard",
        "text": "The same push is applied to a door once at the handle and "
                "once close to the hinge. Which push turns the door more, and "
                "why?",
        "options": [
            {"text": "Close to the hinge, because the push acts on the "
                     "strongest part of the door.",
             "correct": False,
             "why": "How strong the door is there does not come into it. "
                    "Turning effect is force multiplied by distance from the "
                    "hinge, and close in is the small distance."},
            {"text": "Neither — the same force turns the door by the same "
                     "amount wherever it acts.",
             "correct": False,
             "why": "The force is the same, and it is only half the "
                    "calculation. The other half is how far from the hinge it "
                    "acts."},
            {"text": "At the handle, because the same force further out turns "
                     "more.",
             "correct": True},
            {"text": "At the handle, because a handle is built to turn a "
                     "small push into a much bigger force.",
             "correct": False,
             "why": "The handle adds nothing to the push itself. What it adds "
                    "is distance from the hinge, and distance is what "
                    "multiplies up."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s06",
        "band": "standard",
        "text": "A 2 kg load is held 30 cm from the elbow. What is the "
                "turning effect of that load about the elbow?",
        "options": [
            {"text": "0.6 N m, from 2 × 0.3.",
             "correct": False,
             "why": "That uses the mass rather than the weight. A 2 kg load "
                    "weighs 20 N, so the turning effect is 20 × 0.3."},
            {"text": "6 N m, from 20 × 0.3.",
             "correct": True},
            {"text": "600 N m, from 20 × 30.",
             "correct": False,
             "why": "The distance was left in centimetres. Convert it first: "
                    "30 cm is 0.30 m, and 20 × 0.3 is 6."},
            {"text": "6 N, from 20 × 0.3.",
             "correct": False,
             "why": "The arithmetic is right and the unit is not. A force "
                    "multiplied by a distance is a turning effect, in N m."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s07",
        "band": "standard",
        "text": "A tight nut will not shift with a short spanner but comes "
                "loose with a long one, pulled with the same force. Explain "
                "why.",
        "options": [
            {"text": "The long spanner is heavier than the short one, and its "
                     "extra weight adds to the turn.",
             "correct": False,
             "why": "A spanner's own weight is tiny beside the pull. What the "
                    "length adds is distance from the nut."},
            {"text": "The long spanner is stronger, so far less of the force is "
                     "lost in bending the metal.",
             "correct": False,
             "why": "Nothing is lost in a short spanner. What is missing is "
                    "distance — the same force further out turns more."},
            {"text": "The long spanner increases the force you apply, because "
                     "your hand travels much further round the nut.",
             "correct": False,
             "why": "Your hand does travel further, and that is what you pay "
                    "with. The force is the same; it is the turning effect "
                    "that has grown."},
            {"text": "The same force further from the nut turns more: turning "
                     "effect = force × distance.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s08",
        "band": "standard",
        "text": "Holding a 2 kg load 32 cm from the elbow needs about 160 N in "
                "the biceps, which attaches 4 cm from the joint. The same "
                "load is brought in to 16 cm. What is needed now?",
        "options": [
            {"text": "80 N, because the load's turning effect has halved.",
             "correct": True},
            {"text": "320 N, because bringing the load closer doubles the "
                     "muscle force.",
             "correct": False,
             "why": "It is the other way round. A smaller distance means a "
                    "smaller turning effect to match, so the muscle pulls "
                    "less: 3.2 ÷ 0.04 is 80."},
            {"text": "160 N, because the load itself has not changed.",
             "correct": False,
             "why": "The load has not changed and its distance has. Turning "
                    "effect is force times distance, so halving the distance "
                    "halves it."},
            {"text": "40 N, because halving the distance quarters the force.",
             "correct": False,
             "why": "The two are in simple proportion, not squared. 20 N × "
                    "0.16 m is 3.2 N m, and 3.2 ÷ 0.04 is 80 N."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s09",
        "band": "standard",
        "text": "A student works out the force in a biceps and writes the "
                "answer as 160 N m. What is wrong with it?",
        "options": [
            {"text": "Nothing — a muscle force is a turning effect, so N m is "
                     "the right unit for it.",
             "correct": False,
             "why": "A muscle force is a force. The turning effect is what "
                    "you get after multiplying it by a distance."},
            {"text": "The number: dividing a turning effect by a distance can "
                     "never give 160.",
             "correct": False,
             "why": "6.4 N m divided by 0.04 m is exactly 160. The arithmetic "
                    "is fine; the unit is not."},
            {"text": "The unit: the answer is a force, so it is 160 N. N m "
                     "belongs to a turning effect.",
             "correct": True},
            {"text": "The unit: N m divided by m leaves N/m, so it should be "
                     "written 160 N/m.",
             "correct": False,
             "why": "Dividing newton metres by metres leaves newtons — the "
                    "metres cancel. A slash would mean divided by, and "
                    "nothing here is left over a metre."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s10",
        "band": "standard",
        "text": "Three pulls on a hand grip meter give 312 N, 298 N and "
                "305 N. A classmate says to keep only the biggest, since that "
                "is what the muscle can really do. Why is a mean better?",
        "options": [
            {"text": "Because a mean always comes out smaller than the biggest "
                     "reading, and a smaller figure is the safer one.",
             "correct": False,
             "why": "Being smaller is not the reason. A mean uses all three, "
                    "so it does not rest on whichever one happened to be the "
                    "luckiest."},
            {"text": "Because repeats of the same pull always differ, and one "
                     "reading alone could be the luckiest of three.",
             "correct": True},
            {"text": "Because the biggest of the three readings must be a "
                     "mistake, so it ought to be thrown away.",
             "correct": False,
             "why": "There is nothing wrong with 312 N. All three are real "
                    "readings, which is exactly why all three go into the "
                    "mean."},
            {"text": "Because a mean turns three separate readings into a "
                     "single measurement in newtons.",
             "correct": False,
             "why": "Each reading was already in newtons. A mean deals with "
                    "the spread between repeats; it does not change the "
                    "quantity."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s11",
        "band": "standard",
        "text": "A leg press gave a mean of 1422 N and a biceps pull a mean "
                "of 203 N, measured on the same person. Roughly how many "
                "times bigger is the leg press figure?",
        "options": [
            {"text": "About 3 times bigger.",
             "correct": False,
             "why": "Three times 203 N is about 609 N, and the leg press is "
                    "more than twice that again. Check an answer by "
                    "multiplying it back."},
            {"text": "About 14 times bigger.",
             "correct": False,
             "why": "Fourteen times 203 N is about 2842 N, which is twice the "
                    "leg press reading. The answer is nearer 7."},
            {"text": "About 1219 times bigger.",
             "correct": False,
             "why": "1219 N is the difference between the two, not how many "
                    "times bigger one is. Times bigger is a division: 1422 ÷ "
                    "203."},
            {"text": "About 7 times bigger.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s12",
        "band": "standard",
        "text": "A 2 kg dumbbell held 32 cm from the elbow needs about 160 N "
                "in the biceps, which attaches at 4 cm. What would a 4 kg "
                "dumbbell need, everything else the same?",
        "options": [
            {"text": "About 320 N, because doubling the load doubles the "
                     "turning effect it makes.",
             "correct": True},
            {"text": "About 160 N, because the muscle force is set by the two "
                     "distances alone.",
             "correct": False,
             "why": "The distances set the ratio, not the force. Twice the "
                    "load at the same distance makes twice the turning "
                    "effect, so twice the pull."},
            {"text": "About 80 N, because a heavier load is carried more by "
                     "the bones.",
             "correct": False,
             "why": "Bones do not pull, and a heavier load cannot need a "
                    "smaller pull. 40 N × 0.32 m is 12.8 N m, and 12.8 ÷ 0.04 "
                    "is 320."},
            {"text": "About 640 N, because doubling the load raises the force "
                     "four times over.",
             "correct": False,
             "why": "Load and force are in simple proportion here, not "
                    "squared. Double the load, double the pull."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-s13",
        "band": "standard",
        "text": "Someone works out a muscle force as 20 N × 0.32 m × 0.04 m. "
                "Name the two things wrong with that line.",
        "options": [
            {"text": "The two distances are the wrong way round, and the "
                     "answer should be given in N m.",
             "correct": False,
             "why": "Swapping the distances would not repair it, and the "
                    "answer is a force. The muscle distance has to be divided "
                    "by, not multiplied."},
            {"text": "Nothing is wrong with the line, as long as the answer "
                     "is written in newtons.",
             "correct": False,
             "why": "Multiplying all three together does not give a force, "
                    "and the unit that came out of it would not be newtons "
                    "either."},
            {"text": "The muscle distance must be divided by, not multiplied "
                     "— and the unit is wrong.",
             "correct": True},
            {"text": "The weight should be 2 N rather than 20 N, and the "
                     "answer should then be divided by 0.32 m.",
             "correct": False,
             "why": "A 2 kg load really does weigh 20 N. And it is the "
                    "muscle's distance you divide by, not the load's."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b2-04-h05",
        "band": "harder",
        "text": "One tin of 1 kg is held 30 cm from the elbow. Another of "
                "3 kg is held 10 cm from it. Which needs the bigger pull from "
                "the biceps?",
        "options": [
            {"text": "The 3 kg tin, because it is three times as heavy as the "
                     "other one.",
             "correct": False,
             "why": "Weight is only half of a turning effect. It is three "
                    "times heavier and three times closer in, and the two "
                    "cancel."},
            {"text": "The 1 kg tin, because it is held three times further "
                     "from the joint.",
             "correct": False,
             "why": "Distance is the other half, and the same cancelling "
                    "applies. 10 N × 0.3 m and 30 N × 0.1 m both come to "
                    "3 N m."},
            {"text": "It cannot be decided without knowing where the muscle "
                     "attaches to the forearm.",
             "correct": False,
             "why": "The muscle attaches in the same place both times, so it "
                    "divides both turning effects by the same distance. It "
                    "cannot change which is bigger."},
            {"text": "Neither — both have a turning effect of 3 N m, so both "
                     "need the same pull.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h06",
        "band": "harder",
        "text": "A 1.5 kg tin is held 40 cm from the elbow, and the biceps "
                "attaches 5 cm from the elbow. What force must the biceps "
                "pull with?",
        "options": [
            {"text": "12 N, from 1.5 × 0.4 ÷ 0.05.",
             "correct": False,
             "why": "That uses the mass in place of the weight. A 1.5 kg tin "
                    "weighs 15 N, so the turning effect is 6 N m and the pull "
                    "is 120 N."},
            {"text": "120 N, from 15 × 0.4 ÷ 0.05.",
             "correct": True},
            {"text": "15 N, from 6 N m divided by 0.4 m.",
             "correct": False,
             "why": "That divides by the load's distance instead of the "
                    "muscle's. The muscle is at 0.05 m, and 6 ÷ 0.05 is 120."},
            {"text": "0.3 N m, from 15 × 0.4 × 0.05.",
             "correct": False,
             "why": "All three multiplied together. The muscle distance is "
                    "divided by, and the answer is a force in newtons rather "
                    "than a turning effect."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h07",
        "band": "harder",
        "text": "A student calculates the pull in a biceps holding a load and "
                "gets an answer smaller than the weight of the load. What "
                "rules that answer out, before any arithmetic is checked?",
        "options": [
            {"text": "The muscle acts closer to the joint than the load does, "
                     "so it must pull harder and never less.",
             "correct": True},
            {"text": "A muscle can only pull, and a pull is always bigger "
                     "than a weight it is holding.",
             "correct": False,
             "why": "A pull is not automatically bigger than anything. What "
                    "makes this one bigger is where it acts — much closer to "
                    "the joint than the load."},
            {"text": "The arm is a lever, and a lever always makes the force "
                     "bigger at both of its ends.",
             "correct": False,
             "why": "Levers hand out no free force at either end. This one "
                    "costs force and buys speed; arranged the other way it "
                    "would do the opposite."},
            {"text": "Nothing rules it out — a smaller answer is perfectly "
                     "possible when the load is light.",
             "correct": False,
             "why": "How heavy the load is does not change the ratio. With "
                    "the muscle at 4 cm and the load at 32 cm, the pull is "
                    "eight times the weight whatever the weight is."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h08",
        "band": "harder",
        "text": "The Achilles tendon attaches behind the ankle joint. Elite "
                "sprinters tend to have a slightly shorter heel bone, giving "
                "that tendon a smaller distance to work with. What does that "
                "cost, and what does it buy?",
        "options": [
            {"text": "It costs speed and buys force, because a smaller "
                     "distance needs a smaller pull.",
             "correct": False,
             "why": "A smaller distance needs a bigger pull, not a smaller "
                    "one: F = T ÷ d, so shrinking d raises F."},
            {"text": "It costs nothing and buys force, because a sprinter's "
                     "calf muscle is unusually strong.",
             "correct": False,
             "why": "Nothing here comes free. Whatever the muscle's strength, "
                    "a smaller distance demands a bigger force from it."},
            {"text": "It costs force — a bigger pull every stride — and buys "
                     "speed, because the foot moves further.",
             "correct": True},
            {"text": "It costs force and buys stability, because a shorter "
                     "heel bone is harder to twist over.",
             "correct": False,
             "why": "The trade here is force against speed. A small "
                    "shortening of the calf throws the foot down faster, and "
                    "that is what is bought."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h09",
        "band": "harder",
        "text": "Two people hold identical 20 N loads 32 cm from the elbow. "
                "One has a biceps attached 4 cm from the joint, the other "
                "5 cm. Who needs the bigger pull, and by how much?",
        "options": [
            {"text": "The 5 cm one, at about 200 N against 160 N — more "
                     "distance needs more force.",
             "correct": False,
             "why": "More distance needs less force. Cover F on the triangle: "
                    "F = T ÷ d, so the bigger d gives the smaller F."},
            {"text": "Neither — the load and its distance are the same, so "
                     "both need 160 N.",
             "correct": False,
             "why": "The load's turning effect is the same 6.4 N m for both, "
                    "but they divide it by different muscle distances, so the "
                    "two pulls differ."},
            {"text": "The 4 cm one, at about 160 N against 1.28 N — 6.4 "
                     "divided by 5.",
             "correct": False,
             "why": "The second distance was left in centimetres. 5 cm is "
                    "0.05 m, and 6.4 ÷ 0.05 is 128 N — a plausible muscle "
                    "pull, where 1.28 N is not."},
            {"text": "The 4 cm one, and by about a quarter — 160 N against "
                     "128 N.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h10",
        "band": "harder",
        "text": "A see-saw balances with a 200 N child sitting 1.5 m from the "
                "pivot and a second child 1 m from it on the other side. What "
                "is the second child's weight?",
        "options": [
            {"text": "133 N, from 200 ÷ 1.5.",
             "correct": False,
             "why": "That divides one child's weight by their own distance, "
                    "which answers nothing. Balanced means the two turning "
                    "effects are equal."},
            {"text": "300 N, from 200 × 1.5 then ÷ 1.",
             "correct": True},
            {"text": "200 N, because two children only balance if they weigh "
                     "the same.",
             "correct": False,
             "why": "Equal weights balance only at equal distances. This one "
                    "sits closer in, so it has to be the heavier of the two."},
            {"text": "300 N m, from 200 × 1.5 then ÷ 1.",
             "correct": False,
             "why": "Right arithmetic, wrong quantity. 300 N m is the turning "
                    "effect on each side; the child's weight is a force, in "
                    "newtons."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h11",
        "band": "harder",
        "text": "Holding a 2 kg dumbbell 32 cm from the elbow, a biceps "
                "attached at 4 cm pulls eight times the weight. Where does "
                "the eight come from, and what would it be at 8 cm?",
        "options": [
            {"text": "From the two distances — 32 ÷ 4 is 8 — and at 8 cm it "
                     "would be 4.",
             "correct": True},
            {"text": "From the load's weight divided by the muscle distance, "
                     "and at 8 cm it would still be 8.",
             "correct": False,
             "why": "The eight comes from 32 and 4, the two distances. The "
                    "weight is not in it at all, which is why doubling the "
                    "load leaves the ratio at eight."},
            {"text": "From the muscle's own length, and at 8 cm the muscle "
                     "would be shorter, so 16.",
             "correct": False,
             "why": "Muscle length never enters the arithmetic. What counts "
                    "is the distance from the joint to where each force "
                    "acts."},
            {"text": "From the two distances — 32 ÷ 4 is 8 — and at 8 cm it "
                     "would be 16.",
             "correct": False,
             "why": "The first half is right. But a bigger muscle distance "
                    "gives a smaller ratio, not a bigger one: 32 ÷ 8 is 4."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h12",
        "band": "harder",
        "text": "The hand grip, biceps and leg press readings were all taken "
                "from the same person. Why does that matter when the three "
                "muscle groups are compared?",
        "options": [
            {"text": "It does not matter, as long as the same force meter was "
                     "used for all three.",
             "correct": False,
             "why": "The meter matters and so does the person. Two different "
                    "people can differ from each other by more than two "
                    "muscle groups do."},
            {"text": "It matters because one person can only pull so hard, so "
                     "all three of the readings are capped.",
             "correct": False,
             "why": "No cap is being hit — the leg press reads 1422 N. What "
                    "one person gives you is a fair comparison between the "
                    "three groups."},
            {"text": "Any difference in the readings is between the muscle "
                     "groups, not the people.",
             "correct": True},
            {"text": "It matters because a mean can only be worked out from "
                     "readings taken by one person.",
             "correct": False,
             "why": "A mean is the average of any set of repeats, whoever "
                    "took them. The reason for one person is to keep the "
                    "comparison fair."},
        ],
        "figure": None,
    },
    {
        "id": "b2-04-h13",
        "band": "harder",
        "text": "A weightlifter holds a barbell motionless above their head. "
                "A student says that because nothing is moving, no force is "
                "acting. What is the best reply?",
        "options": [
            {"text": "They are right, and the muscles only produce a force "
                     "while the bar is actually rising.",
             "correct": False,
             "why": "Let go and the bar falls. Something is matching its pull "
                    "the whole time it is held there."},
            {"text": "They are wrong, because the bar is really moving very "
                     "slightly and that is what the muscles produce.",
             "correct": False,
             "why": "Nothing has to move. Turning effects can be equal and "
                    "opposite with the bar dead still, and every one of them "
                    "is real."},
            {"text": "They are wrong, but only about the bar: its weight is a "
                     "force, while the muscles are doing nothing.",
             "correct": False,
             "why": "If the muscles did nothing, the bar's turning effect "
                    "would be unopposed and it would come down. Something is "
                    "matching it."},
            {"text": "They are wrong: nothing moves because the turning "
                     "effects are balanced, not because they are zero.",
             "correct": True},
        ],
        "figure": None,
    },

    # ══ MRB-338 expansion ══════════════════════════════════════════════
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": 'b2-04-e14',
        "band": 'easier',
        "text": 'A turning effect does not just have a size — it also has a direction. What are the two possible directions called?',
        "options": [
            {"text": 'Clockwise and anticlockwise.', "correct": True},
            {"text": 'Forward and backward.', "correct": False,
             "why": 'Those describe straight-line movement. A turning effect describes a rotation, not a straight path.'},
            {"text": 'Positive and negative newtons.', "correct": False,
             "why": 'A newton measures the size of a force. Direction of turning is a separate idea from the unit itself.'},
            {"text": 'Upward and downward.', "correct": False,
             "why": 'Those describe a straight-line direction. A turning effect rotates a bone rather than moving it in a line.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e15',
        "band": 'easier',
        "text": 'Rising onto tiptoes, the calf muscle pulls up on the heel through the Achilles tendon. Which joint does the foot turn about?',
        "options": [
            {"text": 'The knee joint.', "correct": False,
             "why": 'The knee is a separate joint, further up the leg. The calf pulls the foot about the ankle.'},
            {"text": 'The ankle joint.', "correct": True},
            {"text": 'The heel bone itself.', "correct": False,
             "why": 'The heel bone is where the tendon pulls, not a joint the foot can turn about.'},
            {"text": 'The Achilles tendon.', "correct": False,
             "why": 'A tendon carries a pull; it does not act as the fixed point a lever turns about.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e16',
        "band": 'easier',
        "text": 'A wheelbarrow is a simple lever. Which part acts as the pivot?',
        "options": [
            {"text": 'The load in the barrow.', "correct": False,
             "why": 'The load is one of the forces acting on the lever, not the fixed point it turns about.'},
            {"text": 'The handles.', "correct": False,
             "why": 'The handles are where the effort is applied, not the fixed point the barrow turns about.'},
            {"text": 'The wheel.', "correct": True},
            {"text": 'The legs that the barrow rests on.', "correct": False,
             "why": 'The legs only support the barrow when it is set down — they play no part while it is being lifted and wheeled.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e17',
        "band": 'easier',
        "text": 'The kneecap, or patella, sits inside the quadriceps tendon at the front of the knee. What does that do to the distance the tendon acts at?',
        "options": [
            {"text": 'It reduces that distance from the joint.', "correct": False,
             "why": 'The kneecap sits proud of the joint, moving the tendon further out, not closer in.'},
            {"text": 'It has no effect on the distance at all.', "correct": False,
             "why": "The kneecap's whole effect is to move the tendon's path further from the joint."},
            {"text": 'It changes the distance only when the knee is bent.', "correct": False,
             "why": "The kneecap sits in the tendon's path throughout the movement, not only at one particular angle."},
            {"text": 'It increases that distance from the joint.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e18',
        "band": 'easier',
        "text": 'The deltoid muscle raises the arm sideways, away from the body. Which joint does it act at?',
        "options": [
            {"text": 'The shoulder.', "correct": True},
            {"text": 'The elbow.', "correct": False,
             "why": 'The elbow bends and straightens the forearm. Raising the whole arm sideways happens at the shoulder.'},
            {"text": 'The wrist.', "correct": False,
             "why": 'The wrist moves the hand. Lifting the whole arm out to the side is a shoulder movement.'},
            {"text": 'The collarbone.', "correct": False,
             "why": 'The collarbone is a bone, not a joint. The deltoid acts at the shoulder joint itself.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e19',
        "band": 'easier',
        "text": 'A weight has a mass of 250 g. What is that in kilograms?',
        "options": [
            {"text": '2.5 kg.', "correct": False,
             "why": 'That divides by 100 rather than 1000. There are 1000 grams in a kilogram.'},
            {"text": '0.25 kg.', "correct": True},
            {"text": '25 kg.', "correct": False,
             "why": 'That is far too heavy for 250 g, and moves the decimal point the wrong way.'},
            {"text": '0.025 kg.', "correct": False,
             "why": 'That divides by 10,000. Dividing by 1000 gives 0.25, not 0.025.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e20',
        "band": 'easier',
        "text": 'A heavy gate needs to be pushed shut. For the same turning effect, does pushing far from the hinge or close to it need less force?',
        "options": [
            {"text": 'Close to the hinge.', "correct": False,
             "why": 'Close to the hinge is the small-distance end. A smaller distance needs a bigger force for the same turning effect, not a smaller one.'},
            {"text": 'Neither — the force needed is the same either way.', "correct": False,
             "why": 'Turning effect is force times distance, so changing the distance changes the force needed.'},
            {"text": 'Far from the hinge.', "correct": True},
            {"text": 'It depends only on how heavy the gate is.', "correct": False,
             "why": "The gate's weight matters for how much force is needed overall, but where you push still changes it for a given gate."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e21',
        "band": 'easier',
        "text": 'A distance is measured as 0.05 m. What is that in centimetres?',
        "options": [
            {"text": '0.5 cm.', "correct": False,
             "why": 'That multiplies by 10 rather than 100. There are 100 centimetres in a metre.'},
            {"text": '50 cm.', "correct": False,
             "why": 'That multiplies by 1000. Multiplying by 100 gives 5, not 50.'},
            {"text": '500 cm.', "correct": False,
             "why": 'That is a hundred times too big. 0.05 m is a small distance, about the width of two fingers.'},
            {"text": '5 cm.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e22',
        "band": 'easier',
        "text": 'Does the turning effect of a spanner depend on how heavy the spanner itself is?',
        "options": [
            {"text": 'No — only the force applied and its distance from the nut matter.', "correct": True},
            {"text": 'Yes — a heavier spanner always turns the nut more.', "correct": False,
             "why": "Turning effect comes from the force applied and the distance it acts at, not from the tool's own weight."},
            {"text": 'It depends on how tightly the spanner grips the nut.', "correct": False,
             "why": 'A loose grip may slip off, but it changes nothing about the turning effect itself, which is the force applied multiplied by its distance from the nut.'},
            {"text": 'It depends on what metal the spanner is made from.', "correct": False,
             "why": 'The material makes no difference to the turning effect. Only the force and the distance it acts at do.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e23',
        "band": 'easier',
        "text": 'A muscle attaches further from a joint than before, but holds the same load. Does it need more or less force?',
        "options": [
            {"text": 'More force.', "correct": False,
             "why": 'A bigger distance from the joint means less force is needed for the same turning effect, not more.'},
            {"text": 'Less force.', "correct": True},
            {"text": 'Exactly the same force.', "correct": False,
             "why": "Changing the muscle's distance from the joint changes the force needed, since turning effect depends on both."},
            {"text": "It cannot be worked out without knowing the load's own distance.", "correct": False,
             "why": 'With the load unchanged, moving the muscle further out is already enough to say the force falls.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e24',
        "band": 'easier',
        "text": 'A distance is measured as 3 cm. What is that in metres?',
        "options": [
            {"text": '0.3 m.', "correct": False,
             "why": 'That divides by 10 rather than 100. There are 100 centimetres in a metre.'},
            {"text": '3.0 m.', "correct": False,
             "why": 'That leaves the number unchanged, which only works if the units were the same to start with.'},
            {"text": '0.03 m.', "correct": True},
            {"text": '30 m.', "correct": False,
             "why": 'That multiplies rather than divides. Converting centimetres to metres always makes the number smaller.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e25',
        "band": 'easier',
        "text": 'Which turning effect is bigger: 5 N m, or 500 N cm?',
        "options": [
            {"text": '5 N m is bigger.', "correct": False,
             "why": '500 N cm converts to 5 N m exactly, since 500 cm is 5 m. The two figures describe the same size.'},
            {"text": '500 N cm is bigger.', "correct": False,
             "why": '500 cm is 5 m, so 500 N cm is exactly 5 N m — the same size, not a bigger one.'},
            {"text": 'It cannot be compared without a distance in metres.', "correct": False,
             "why": '500 cm converts directly to 5 m, which is enough to compare the two figures directly.'},
            {"text": 'Neither — the two are equal once converted.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e26',
        "band": 'easier',
        "text": 'The kneecap changes the distance the quadriceps tendon acts at. Does that increase or decrease the force the quadriceps needs for the same turning effect?',
        "options": [
            {"text": 'It decreases the force needed.', "correct": True},
            {"text": 'It increases the force needed.', "correct": False,
             "why": 'A bigger distance from the joint means less force is needed for the same turning effect, not more.'},
            {"text": 'It has no effect on the force needed.', "correct": False,
             "why": 'Changing the distance a tendon acts at always changes the force needed for a given turning effect.'},
            {"text": 'It only matters for a bent knee, not a straight one.', "correct": False,
             "why": "The kneecap sits in the tendon's path throughout the movement, changing the distance at every angle."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e27',
        "band": 'easier',
        "text": 'Does a bigger animal always need a bigger turning effect to move one of its joints?',
        "options": [
            {"text": 'Yes — every joint in a bigger animal needs more turning effect.', "correct": False,
             "why": "Turning effect depends on the actual force and distance in a particular movement, not on the animal's overall size."},
            {"text": 'No — it depends on the load and the distances involved, not size alone.', "correct": True},
            {"text": 'Yes, because a bigger animal always has bigger muscles.', "correct": False,
             "why": 'Muscle size affects how much force is available, but the turning effect needed still depends on the specific load and distances.'},
            {"text": 'No, because size makes no difference to any force in the body.', "correct": False,
             "why": 'Size does affect the forces involved in many cases — the point is that it is not the only thing that matters.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e28',
        "band": 'easier',
        "text": 'A load has a mass of 2 kg. What is its weight in newtons?',
        "options": [
            {"text": '2 N.', "correct": False,
             "why": 'That is the mass in kilograms with a newton label attached. Each kilogram weighs about 10 N, so 2 kg weighs 20 N.'},
            {"text": '0.2 N.', "correct": False,
             "why": 'That divides by 10 rather than multiplying. Weight in newtons is the mass in kilograms multiplied by about 10.'},
            {"text": '20 N.', "correct": True},
            {"text": '2000 N.', "correct": False,
             "why": 'That multiplies by 1000, the grams-to-kilograms step, rather than by 10 for weight. 2 kg weighs about 20 N.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e29',
        "band": 'easier',
        "text": "A wheelbarrow's load is moved closer to the wheel, everything else unchanged. Does lifting the handles now need more or less force?",
        "options": [
            {"text": 'More force.', "correct": False,
             "why": 'Moving the load closer to the pivot reduces the turning effect it creates, so less force is needed at the handles, not more.'},
            {"text": 'Exactly the same force.', "correct": False,
             "why": "Changing the load's distance from the wheel changes the turning effect it makes, so the force needed changes too."},
            {"text": 'It cannot be worked out from the information given.', "correct": False,
             "why": 'A smaller distance for the same load already tells you the force needed must fall.'},
            {"text": 'Less force.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e30',
        "band": 'easier',
        "text": 'If the deltoid attached further from the shoulder joint than it really does, would raising the same weight sideways need more or less force from it?',
        "options": [
            {"text": 'Less force.', "correct": True},
            {"text": 'More force.', "correct": False,
             "why": 'A bigger distance from the joint means less force is needed for the same turning effect, not more.'},
            {"text": 'Exactly the same force.', "correct": False,
             "why": "Moving the muscle's attachment point changes the distance it acts at, which changes the force needed."},
            {"text": 'It would depend on how fast the arm is raised.', "correct": False,
             "why": 'Speed of the movement is not part of this calculation. Only the force, the load and their distances from the joint are.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e31',
        "band": 'easier',
        "text": 'A bag is held in the hand and the elbow bends to lift it. In force × distance, which point is that distance measured from?',
        "options": [
            {"text": 'The hand holding the bag.', "correct": False,
             "why": 'The hand is where the load acts. The distance is measured from the fixed point the forearm turns about.'},
            {"text": 'The elbow joint.', "correct": True},
            {"text": 'The shoulder joint.', "correct": False,
             "why": 'The shoulder is a separate joint further up the arm. The forearm turns about the elbow.'},
            {"text": 'The middle of the biceps muscle.', "correct": False,
             "why": 'A muscle belly is not a fixed point, and nothing turns about it. The forearm turns about the elbow.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-e32',
        "band": 'easier',
        "text": 'Is turning effect measured in a single unit like the newton, or in a combined unit?',
        "options": [
            {"text": 'A single unit, exactly like force.', "correct": False,
             "why": 'Turning effect is a force multiplied by a distance, so its unit combines the units of both.'},
            {"text": 'A single unit, exactly like distance.', "correct": False,
             "why": "Turning effect includes a force as well as a distance, so distance's unit alone is not enough."},
            {"text": 'A combined unit, made from two other units multiplied together.', "correct": True},
            {"text": 'It has no unit at all, since it is only a comparison.', "correct": False,
             "why": 'Turning effect is a real, measurable quantity, with the combined unit newton metre.'},
        ],
        "figure": None,
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": 'b2-04-s14',
        "band": 'standard',
        "text": 'Standing on tiptoes, the ground pushes up on the ball of the foot with the whole 600 N of body weight, 10 cm from the ankle joint. The calf muscle pulls through the Achilles tendon 5 cm from the same joint. What force must the calf muscle produce?',
        "options": [
            {"text": '300 N.', "correct": False,
             "why": 'That is 600 ÷ 2 without going through the turning effect. Work out 600 × 0.10 first, then divide by 0.05, which gives 1200 N.'},
            {"text": '1200 N.', "correct": True},
            {"text": '60 N.', "correct": False,
             "why": "That is the turning effect in N m, 600 × 0.10, reported as a force. It still has to be divided by the muscle's own distance."},
            {"text": '6000 N.', "correct": False,
             "why": "That is 600 × 10, the turning effect in newton centimetres, reported as if it were a force. It still has to be divided by the muscle's own distance."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s15',
        "band": 'standard',
        "text": "A wheelbarrow's load weighs 180 N and sits 40 cm from the wheel. The handles are lifted 80 cm from the wheel. What lifting force is needed at the handles?",
        "options": [
            {"text": '180 N.', "correct": False,
             "why": "That is the load's own weight, not the force needed at the handles. The two distances differ, so the forces differ too."},
            {"text": '360 N.', "correct": False,
             "why": 'That doubles the load rather than using its actual distance. Work out 180 × 0.40 first, then divide by 0.80.'},
            {"text": '90 N.', "correct": True},
            {"text": '72 N.', "correct": False,
             "why": 'That is 180 × 0.40, the turning effect in N m, reported as if it were the answer. It still has to be divided by 0.80.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s16',
        "band": 'standard',
        "text": 'Removing a damaged kneecap moves the quadriceps tendon closer to the knee joint than before. Predict the effect on the force needed to straighten the leg against the same load.',
        "options": [
            {"text": 'Less force is needed than before.', "correct": False,
             "why": 'A smaller distance from the joint means more force is needed for the same turning effect, not less.'},
            {"text": 'Exactly the same force is needed.', "correct": False,
             "why": "Moving the tendon's distance from the joint changes the force needed for the same load."},
            {"text": 'No force is needed, since the joint can no longer move.', "correct": False,
             "why": 'The joint still moves — only the distance the tendon acts at has changed, not whether movement is possible.'},
            {"text": 'More force is needed than before.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s17',
        "band": 'standard',
        "text": 'Holding the arm out sideways, a 20 N weight is held in the hand, 60 cm from the shoulder. The deltoid attaches 3 cm from the same joint. What force must the deltoid produce?',
        "options": [
            {"text": '400 N.', "correct": True},
            {"text": '40 N.', "correct": False,
             "why": 'That divides the 12 N m turning effect by 0.3 m instead of 0.03 m — one decimal place out in converting 3 cm.'},
            {"text": '4 N.', "correct": False,
             "why": 'That divides the 12 N m turning effect by 3 rather than by 0.03 m, leaving the deltoid\'s distance in centimetres.'},
            {"text": '1200 N.', "correct": False,
             "why": 'That multiplies 20 × 60 without converting the centimetres to metres first, which inflates the answer.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s18',
        "band": 'standard',
        "text": "A wheelbarrow's load stays at 40 cm from the wheel, but the handles are extended from 80 cm to 120 cm. Predict the effect on the lifting force needed.",
        "options": [
            {"text": 'More force is needed than before.', "correct": False,
             "why": "A bigger distance for the effort means less force is needed for the same load's turning effect, not more."},
            {"text": 'Less force is needed than before.', "correct": True},
            {"text": 'Exactly the same force is needed.', "correct": False,
             "why": 'Changing the handle length changes the distance the lifting force acts at, which changes the force needed.'},
            {"text": 'It cannot be predicted without a new load weight.', "correct": False,
             "why": 'The load and its distance from the wheel are unchanged, so lengthening the handles alone is enough to say the force falls.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s19',
        "band": 'standard',
        "text": 'A student calculates a turning effect using a mass in grams instead of converting it to a weight in newtons first. How far out will the answer be?',
        "options": [
            {"text": 'About 1000 times too small.', "correct": False,
             "why": 'Using grams in place of newtons makes the number far too big, not too small, and the factor is 100 rather than 1000.'},
            {"text": 'Only slightly out, by a few per cent.', "correct": False,
             "why": 'Dividing by 1000 for kilograms and then multiplying by 10 for weight leaves the answer a hundred times out, which is not a few per cent.'},
            {"text": 'About 100 times too big.', "correct": True},
            {"text": 'Not affected at all, since grams and newtons are interchangeable.', "correct": False,
             "why": 'Grams measure mass and newtons measure weight — they are different quantities, and using one for the other puts the answer out a hundredfold.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s20',
        "band": 'standard',
        "text": 'The biceps pulls one way at the elbow and the triceps pulls the other, and the forearm stays perfectly still. What must be true of their two turning effects?',
        "options": [
            {"text": "The biceps' turning effect must be bigger.", "correct": False,
             "why": 'If one turning effect were bigger, the forearm would move towards that side rather than staying still.'},
            {"text": "The triceps' turning effect must be bigger.", "correct": False,
             "why": 'If one turning effect were bigger, the forearm would move towards that side rather than staying still.'},
            {"text": 'Neither muscle can be producing a turning effect at all.', "correct": False,
             "why": 'Both are actively pulling and using energy — nothing moving does not mean nothing is happening.'},
            {"text": 'They must be equal and opposite.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s21',
        "band": 'standard',
        "text": "A wheelbarrow's handles stay at 80 cm from the wheel, but the load is moved from 40 cm to 20 cm from the wheel, still weighing 180 N. What lifting force is now needed?",
        "options": [
            {"text": '45 N.', "correct": True},
            {"text": '180 N.', "correct": False,
             "why": "That is the load's own weight. The force at the handles depends on both distances, not the weight alone."},
            {"text": '90 N.', "correct": False,
             "why": "That was the force before the load was moved. Halving the load's distance halves the force needed again."},
            {"text": '22.5 N.', "correct": False,
             "why": 'That would be a further halving beyond what moving the load once does. 180 × 0.20 ÷ 0.80 is 45, not 22.5.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s22',
        "band": 'standard',
        "text": 'A knee needs a turning effect of 40 N m to straighten against a load. With the kneecap acting 5 cm from the joint, the quadriceps needs 800 N. Without it, acting only 3 cm out, what force would be needed?',
        "options": [
            {"text": 'About 480 N.', "correct": False,
             "why": 'That scales the force down, but a smaller distance needs a bigger force, not a smaller one.'},
            {"text": 'About 1333 N.', "correct": True},
            {"text": '800 N, unchanged.', "correct": False,
             "why": 'The distance has changed from 5 cm to 3 cm, and turning effect depends on that distance, so the force changes too.'},
            {"text": 'About 133 N.', "correct": False,
             "why": 'That is 40 ÷ 0.3 — a decimal place lost in converting 3 cm to metres. 40 N m divided by 0.03 m is about 1333 N.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s23',
        "band": 'standard',
        "text": "A student says a bigger animal's jaw joint must always produce a bigger turning effect than a smaller animal's. What is the flaw in that claim?",
        "options": [
            {"text": 'There is no flaw — bigger animals always have bigger turning effects at every joint.', "correct": False,
             "why": "Turning effect is set by the specific force and distance in a movement, which is not fixed by an animal's overall size."},
            {"text": 'The flaw is that turning effect cannot apply to animals other than humans.', "correct": False,
             "why": 'Turning effect applies to any lever acting about a joint, in any animal with a jaw and a muscle.'},
            {"text": "Turning effect depends on the actual bite force and distances involved, not on the animal's size alone.", "correct": True},
            {"text": 'The flaw is that jaw joints do not use turning effect at all, unlike limb joints.', "correct": False,
             "why": 'A jaw is a lever like any other joint, and turning effect applies to it in exactly the same way.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s24',
        "band": 'standard',
        "text": 'One arm of a nutcracker turns about the hinge at its end. A hand squeezes that arm with 36 N, 24 cm from the hinge, and the nut sits 4 cm from the hinge. What force does the arm press onto the nut?',
        "options": [
            {"text": '3456 N.', "correct": False,
             "why": "That multiplies by the nut's own distance instead of dividing by it, working out 36 × 24 × 4. The hand's distance multiplies and the nut's distance divides: 36 × 24 ÷ 4 = 216 N."},
            {"text": '864 N.', "correct": False,
             "why": "That is 36 × 24, the turning effect in newton centimetres, reported as if it were a force. It still has to be divided by the nut's own 4 cm, and both distances being in centimetres means that conversion cancels: 36 × 24 ÷ 4 = 216 N."},
            {"text": 'The same 36 N the hand squeezes with.', "correct": False,
             "why": 'The hand acts six times further from the hinge than the nut does, so the nut feels six times the squeeze rather than the same: 36 × 24 ÷ 4 = 216 N.'},
            {"text": '216 N.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s25',
        "band": 'standard',
        "text": 'A gate needs 40 N m of turning effect to swing shut. Pushed at 80 cm from the hinge, how much force is needed?',
        "options": [
            {"text": '50 N.', "correct": True},
            {"text": '3200 N.', "correct": False,
             "why": 'That multiplies 40 by 80 without converting centimetres to metres, and without dividing rather than multiplying.'},
            {"text": '0.5 N.', "correct": False,
             "why": 'That divides by 80 rather than 0.80. Converting 80 cm to 0.80 m first gives 50 N, not 0.5 N.'},
            {"text": '32 N.', "correct": False,
             "why": 'That multiplies 40 by 0.80 rather than dividing. Force = turning effect ÷ distance, so 40 ÷ 0.80 is 50.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s26',
        "band": 'standard',
        "text": 'Two people push the same heavy gate shut with the same force, but one pushes twice as far from the hinge as the other. Compare the two turning effects they produce.',
        "options": [
            {"text": 'Both produce exactly the same turning effect.', "correct": False,
             "why": 'Turning effect depends on distance as well as force, so pushing further out with the same force produces more turning effect, not the same.'},
            {"text": 'The one pushing further out produces twice the turning effect.', "correct": True},
            {"text": 'The one pushing closer to the hinge produces more turning effect.', "correct": False,
             "why": 'A bigger distance from the pivot produces a bigger turning effect for the same force, not a smaller one.'},
            {"text": "It cannot be compared without knowing the gate's own weight.", "correct": False,
             "why": "The gate's weight does not enter this comparison — only the two pushers' own forces and distances do."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s27',
        "band": 'standard',
        "text": 'The deltoid needs 400 N to hold a 20 N weight out sideways at 60 cm, attaching 3 cm from the shoulder. If the weight were held at only 30 cm instead, what force would the deltoid need?',
        "options": [
            {"text": '800 N.', "correct": False,
             "why": "That doubles the force, but halving the load's own distance halves the force needed, not doubles it."},
            {"text": '400 N, unchanged.', "correct": False,
             "why": "The load's distance has halved, from 60 cm to 30 cm, and turning effect depends on that distance, so the force changes too."},
            {"text": '200 N.', "correct": True},
            {"text": '100 N.', "correct": False,
             "why": "That halves the force twice over. Halving the load's distance once halves the force once, from 400 N to 200 N."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s28',
        "band": 'standard',
        "text": 'A student says that because a wheelbarrow needs less force at the handles than the load weighs, it must be breaking the turning-effect rule that nothing is free. What is the better explanation?',
        "options": [
            {"text": 'The rule genuinely does not apply to wheelbarrows, only to muscles.', "correct": False,
             "why": 'The same turning-effect rule governs any lever, wheelbarrows included — nothing about it is specific to muscles.'},
            {"text": 'The wheelbarrow really does create force from nothing, which is why it is useful.', "correct": False,
             "why": 'No force is created from nothing. The saving in force is paid for by the effort moving further.'},
            {"text": 'The wheel itself removes the need for the trade of force for distance entirely.', "correct": False,
             "why": 'The wheel acts as the pivot; it does not cancel the trade between force and distance that any lever makes.'},
            {"text": 'The effort travels further than the load moves; force is traded for distance.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s29',
        "band": 'standard',
        "text": 'A gate needs 60 N m to swing shut, and 75 N is needed when pushed at a certain distance from the hinge. What is that distance?',
        "options": [
            {"text": '0.8 m.', "correct": True},
            {"text": '1.25 m.', "correct": False,
             "why": 'That divides the force by the turning effect instead of the other way round. Distance = turning effect ÷ force, so 60 ÷ 75 is 0.8.'},
            {"text": '4500 m.', "correct": False,
             "why": 'That multiplies the two figures together rather than dividing. Multiplying is used to find the turning effect, not the distance.'},
            {"text": '8 m.', "correct": False,
             "why": 'A decimal place has slipped. 60 ÷ 75 is 0.8, not 8 — and 8 m is far longer than any real gate.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s30',
        "band": 'standard',
        "text": 'The kneecap normally adds about 2 cm to the distance the quadriceps tendon acts at. Suggest one reason a badly damaged kneecap that has to be removed changes daily life more than its size might suggest.',
        "options": [
            {"text": 'The knee can no longer bend or straighten at all without the kneecap.', "correct": False,
             "why": 'The joint still bends and straightens — what changes is the force needed to drive it, not whether movement is possible.'},
            {"text": 'The extra force is needed on every stride, not just sometimes.', "correct": True},
            {"text": 'The quadriceps muscle disappears entirely once the kneecap is removed.', "correct": False,
             "why": 'The muscle itself is unaffected by removing the kneecap. Only the distance its tendon acts at has changed.'},
            {"text": "The hamstrings must now do the quadriceps' job instead.", "correct": False,
             "why": 'The hamstrings pull the opposite way to the quadriceps and cannot take over its straightening job.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s31',
        "band": 'standard',
        "text": 'A door is pushed shut with 20 N at 90 cm from the hinge. What turning effect does that produce?',
        "options": [
            {"text": '1800 N m.', "correct": False,
             "why": 'The 90 cm was left unconverted. 90 cm is 0.90 m, and 20 × 0.90 is 18, not 1800.'},
            {"text": '4.5 N m.', "correct": False,
             "why": 'That divides rather than multiplies. Turning effect is force times distance: 20 × 0.90 is 18.'},
            {"text": '18 N m.', "correct": True},
            {"text": '0.18 N m.', "correct": False,
             "why": 'A decimal place has slipped. 20 × 0.90 is 18, not 0.18.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-s32',
        "band": 'standard',
        "text": "Explain why a spanner's own length can make a stubborn nut easier to turn, even though the length itself carries no force.",
        "options": [
            {"text": 'A longer spanner is always heavier, and weight adds to the turning effect.', "correct": False,
             "why": "A longer spanner need not be heavier, and it is not weight that makes the difference. What changes is the distance the same hand-force acts at."},
            {"text": 'A longer spanner grips the nut more tightly at its far end.', "correct": False,
             "why": "Grip on the nut happens at the spanner's head, unaffected by how long the handle is."},
            {"text": "A longer spanner reduces the force needed by changing the nut's own resistance.", "correct": False,
             "why": "The nut's resistance is unaffected by the tool used on it. What changes is the distance the same hand-force acts at."},
            {"text": 'A longer spanner lets the same force act further out, raising turning effect.', "correct": True},
        ],
        "figure": None,
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": 'b2-04-h14',
        "band": 'harder',
        "text": "A student calculates the calf muscle's force for tiptoe standing as 750 N × 12 × 4, leaving both distances in centimetres and multiplying rather than dividing by the muscle's own distance. Name both errors and give the correct force, given 750 N at 12 cm and the muscle at 4 cm.",
        "options": [
            {"text": 'Only the unit conversion is wrong; multiplying by both distances is otherwise correct, giving 3.6 N.', "correct": False,
             "why": "Multiplying by the muscle's own distance instead of dividing by it gives 3.6 N, nowhere near the force a calf must produce. That distance must be divided by."},
            {"text": 'Both steps are wrong, and the correct force is 36 000 N.', "correct": False,
             "why": "36 000 is the student's own uncorrected multiplication, 750 × 12 × 4. Dividing by the muscle's distance instead gives 2250 N."},
            {"text": "Convert to metres, then divide by the muscle's own distance to get 2250 N.", "correct": True},
            {"text": 'Neither is really an error, since the final unit would still be newtons either way.', "correct": False,
             "why": 'Getting newtons as a unit by chance does not mean the number itself is right. Both mistakes change the numerical answer.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h15',
        "band": 'harder',
        "text": 'One wheelbarrow has short handles, 60 cm from the wheel; another has long handles, 120 cm from the wheel, with an identical load at an identical distance from the wheel in both. Compare the effort needed to lift each, and what the long-handled one costs in return.',
        "options": [
            {"text": 'The long-handled one needs less force and costs nothing in return.', "correct": False,
             "why": 'Nothing about a lever is free. The saving in force comes at the cost of the effort moving further.'},
            {"text": 'Both need exactly the same lifting force, since the load and its distance are identical.', "correct": False,
             "why": "The effort's own distance from the wheel differs between the two, and that distance changes the force needed."},
            {"text": 'The short-handled one needs less force, since a shorter lever is always easier to use.', "correct": False,
             "why": 'A shorter effort distance means a bigger force is needed for the same load, not a smaller one.'},
            {"text": 'It needs less force, but the handles move further for the same lift.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h16',
        "band": 'harder',
        "text": 'Removing a damaged kneecap permanently increases the quadriceps force needed to straighten the knee. Explain why this matters more over a lifetime than a single calculation suggests.',
        "options": [
            {"text": 'The extra force applies to every step, adding up over a lifetime.', "correct": True},
            {"text": 'The quadriceps eventually adapts and needs no more force than before.', "correct": False,
             "why": 'The distance the tendon acts at has permanently changed. No amount of adaptation restores the distance the kneecap used to add.'},
            {"text": 'It does not matter more — a single calculation already captures the whole lifetime effect.', "correct": False,
             "why": 'A single calculation shows the extra force for one step. The real cost is that same extra force repeated on every step, for years.'},
            {"text": 'The effect only matters while walking, not while standing still.', "correct": False,
             "why": 'The extra force is needed whenever the quadriceps straightens the knee against a load, which includes many everyday movements besides walking.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h17',
        "band": 'harder',
        "text": 'A surgeon repairs a torn deltoid tendon slightly closer to the shoulder joint than its original attachment point. Predict the long-term effect on lifting the arm sideways, assuming the muscle itself heals fully.',
        "options": [
            {"text": 'No effect at all, since the muscle itself is fully healed.', "correct": False,
             "why": "The muscle's health is not the only factor — where its tendon attaches also decides the force needed for a given load."},
            {"text": 'More force will be needed than before, for the same load.', "correct": True},
            {"text": 'Less force will be needed, since the tendon now acts more directly on the joint.', "correct": False,
             "why": 'A smaller distance from the joint means more force is needed for the same turning effect, not less.'},
            {"text": 'The arm will no longer be able to lift sideways at all.', "correct": False,
             "why": 'The muscle still pulls and still moves the arm — only the force required has changed, not whether the movement is possible.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h18',
        "band": 'harder',
        "text": 'The calf muscle at the ankle and the biceps at the elbow both attach very close to their joints. Explain what this shared arrangement buys, and what it costs, at both joints.',
        "options": [
            {"text": 'Both buy extra force at the far end of the limb, at no real cost to the muscle.', "correct": False,
             "why": 'Attaching close to a joint costs force, since the muscle must pull many times harder than the load — it does not buy extra force for free.'},
            {"text": 'Both buy stability at the joint, at the cost of range of movement.', "correct": False,
             "why": "Attachment distance is about the force-speed trade, not the joint's stability, which comes from the bone shape and ligaments instead."},
            {"text": "Both buy speed and reach at the limb's far end, paid for in extra force.", "correct": True},
            {"text": 'It buys something at the ankle but nothing at the elbow.', "correct": False,
             "why": 'The same force-for-speed trade applies at both joints, since both muscles attach close to their own joint in the same way.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h19',
        "band": 'harder',
        "text": "A human arm and a wheelbarrow are both levers, but a human arm's muscle attaches close to the joint while a wheelbarrow's effort acts far from the wheel. Explain why the two are built the opposite way round.",
        "options": [
            {"text": 'They are not really opposite — both save force the same way.', "correct": False,
             "why": "The arm's own muscle attachment costs force rather than saving it; only the wheelbarrow's arrangement saves force at the effort end."},
            {"text": 'The arm is a mistake of evolution that a wheelbarrow corrects.', "correct": False,
             "why": "The arm's arrangement is exactly suited to what a hand needs to do — reach fast and far — not a design flaw."},
            {"text": 'The difference is only about size, since a wheelbarrow is bigger than an arm.', "correct": False,
             "why": 'Size is not what decides the trade — where the effort acts relative to the pivot and the load does.'},
            {"text": 'The arm trades force for speed; the wheelbarrow trades handle travel for less force.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h20',
        "band": 'harder',
        "text": 'A student\'s working reads: "180 g × 40 × 80 = turning effect." Identify every mistake in that line, for a 180 g load 40 cm from a wheel with handles at 80 cm.',
        "options": [
            {"text": 'Convert the mass to newtons, convert the distances, then divide by the handle distance.', "correct": True},
            {"text": 'Only the missing unit conversion for mass is wrong; the rest of the line is correct.', "correct": False,
             "why": "The centimetres are also unconverted, and multiplying by the handle's own distance is the wrong operation entirely."},
            {"text": 'Only the centimetres need converting; grams are close enough to newtons to leave as they are.', "correct": False,
             "why": 'Grams measure mass, not weight, and must be converted properly — first to kilograms, then to newtons.'},
            {"text": 'The line has no mistakes, since all three numbers are genuinely part of the calculation.', "correct": False,
             "why": 'All three numbers belong in a correct calculation, but none of them is used correctly in this line.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h21',
        "band": 'harder',
        "text": 'A hand-grip force and a leg-press force were measured on the same person and differ enormously. A student argues this proves turning effect plays no part in grip strength, since a hand grip has no obvious lever. Evaluate that.',
        "options": [
            {"text": 'The student is right — turning effect only applies to limb joints, not to the hand.', "correct": False,
             "why": 'The hand and fingers contain small joints worked by tendons in exactly the same force-times-distance way as any other joint.'},
            {"text": "The size gap reflects muscle strength, not the absence of turning effect.", "correct": True},
            {"text": 'The student is right, since grip strength depends only on how hard the muscle contracts.', "correct": False,
             "why": 'How hard a muscle contracts still has to reach the fingers through tendons crossing joints, which is exactly where turning effect applies.'},
            {"text": 'The student is right, because a bigger force can only ever come from a longer lever.', "correct": False,
             "why": 'A bigger force does not have to mean a longer lever — a bigger muscle produces more force at the same distance from the joint.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h22',
        "band": 'harder',
        "text": 'A single muscle pulling one way creates a turning effect in one direction only. Use this, rather than the idea of pushing and pulling, to explain why a joint needs two muscles rather than one.',
        "options": [
            {"text": 'Two muscles are needed because one alone could never produce enough force for any load.', "correct": False,
             "why": 'A single muscle could in principle be strong enough — the reason a second is needed is direction, not strength.'},
            {"text": 'Two muscles are needed only because bones are too heavy for one turning effect to move.', "correct": False,
             "why": 'Bone weight is largely ignored in these calculations, and is not the reason a second muscle is required.'},
            {"text": 'One turning effect cannot reverse itself; a second, opposite one is needed.', "correct": True},
            {"text": 'One muscle already produces turning effects in both directions, so a second is only for backup.', "correct": False,
             "why": "A single muscle's pull only ever creates a turning effect in one direction — never in both."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h23',
        "band": 'harder',
        "text": 'A student claims that because a wheelbarrow makes lifting easier, every lever must make its job easier. Use the biceps at the elbow to evaluate that claim.',
        "options": [
            {"text": 'True — the biceps also reduces the force needed, just by a smaller amount than a wheelbarrow.', "correct": False,
             "why": 'The biceps needs far more force than the load it holds, which is the opposite of a force saving.'},
            {"text": 'True, since every lever in the body is built the same way as a wheelbarrow.', "correct": False,
             "why": "The biceps attaches close to its joint, the opposite arrangement to a wheelbarrow's effort acting far from its pivot."},
            {"text": 'The claim cannot be tested using the biceps, since it is not really a lever at all.', "correct": False,
             "why": 'The forearm, pivoting at the elbow with the biceps pulling on it, is exactly a lever — the same principle as a wheelbarrow, arranged differently.'},
            {"text": "False — the biceps trades force for speed instead of saving force.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h24',
        "band": 'harder',
        "text": 'Doubling the distance from a pivot at which a force acts doubles the turning effect. A student says doubling BOTH the force and the distance must therefore double the turning effect too. Evaluate that.',
        "options": [
            {"text": 'False — doubling both multiplies the turning effect by four.', "correct": True},
            {"text": 'True — doubling either one on its own doubles it, so doubling both must double it as well.', "correct": False,
             "why": 'Force and distance are multiplied together, so doubling both multiplies the result by four, not by two.'},
            {"text": 'True, but only when the force and distance are both small to begin with.', "correct": False,
             "why": 'The relationship holds by the same arithmetic whatever the starting values are — doubling both always multiplies the turning effect by four.'},
            {"text": 'False, because doubling both actually leaves the turning effect completely unchanged.', "correct": False,
             "why": 'Doubling either quantity increases the turning effect. Doubling both increases it far more, to four times the original.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h25',
        "band": 'harder',
        "text": 'A gate needing 60 N m to swing shut is pushed with 50 N at one distance, then with 40 N at a different distance, and produces the same turning effect both times. Compare the two distances used.',
        "options": [
            {"text": 'The two pushes acted at exactly the same distance from the hinge.', "correct": False,
             "why": 'Different forces producing the same turning effect cannot act at the same distance — the smaller force needs a bigger distance.'},
            {"text": 'The 40 N push acted 0.3 m further from the hinge than the 50 N push.', "correct": True},
            {"text": 'The 50 N push acted further from the hinge than the 40 N push.', "correct": False,
             "why": 'The smaller force needs the bigger distance to reach the same turning effect, which is the 40 N push, not the 50 N one.'},
            {"text": "It cannot be worked out without knowing the gate's own weight.", "correct": False,
             "why": "The gate's weight is not needed here — each distance can be found directly from its own force and the fixed turning effect of 60 N m."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h26',
        "band": 'harder',
        "text": "Explain why an engineer measuring a robot arm's motor force would get a misleading answer by fitting the force meter to the gripper at the end, rather than to the motor's own drive shaft.",
        "options": [
            {"text": 'A force meter only works when it is fitted to a living tendon, never to a machine part.', "correct": False,
             "why": 'A force meter reads whatever force is acting where it is fitted, machine or living tissue alike.'},
            {"text": 'The gripper and the drive shaft always read exactly the same force, so it makes no difference.', "correct": False,
             "why": 'The two sit at different distances from the pivot, which is exactly why the same turning effect gives different forces at each point.'},
            {"text": 'The meter at the gripper reads a far smaller force than the motor itself produces.', "correct": True},
            {"text": 'The meter would read a bigger force at the gripper, not a smaller one.', "correct": False,
             "why": 'The gripper sits further from the pivot than the drive shaft does, so the force there is smaller, not bigger.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h27',
        "band": 'harder',
        "text": "A prosthetic knee is deliberately built without a kneecap-style pulley in front of the joint, unlike a real knee. Predict what its designers must have compensated for elsewhere.",
        "options": [
            {"text": 'Nothing — a pulley effect makes no real difference to the force needed.', "correct": False,
             "why": 'A pulley-style structure like the kneecap increases the distance a tendon acts at, which genuinely reduces the force needed for the same job.'},
            {"text": 'A lighter overall structure, since less force is needed without a pulley.', "correct": False,
             "why": 'Without the pulley effect, more force is needed for the same movement, which points towards a stronger structure, not a lighter one.'},
            {"text": 'A change to the material the knee joint itself is entirely made from.', "correct": False,
             "why": "The joint's material does not compensate for a missing pulley effect — the force delivered by the drive mechanism does."},
            {"text": "A stronger motor or gearing, since the tendon's distance is smaller.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h28',
        "band": 'harder',
        "text": 'A student says turning effect direction (clockwise or anticlockwise) is just a label with no real consequence. Use the biceps and triceps pulling on the same forearm to argue against that.',
        "options": [
            {"text": "Their turning effects act in opposite directions, bending one way, straightening the other.", "correct": True},
            {"text": 'The student is right, since both muscles ultimately produce the same size of turning effect.', "correct": False,
             "why": "Size is not the point here — it is the opposite direction of each muscle's turning effect that decides which way the elbow moves."},
            {"text": 'The student is right, because direction only matters for engineered levers, not for muscles.', "correct": False,
             "why": "A muscle's pull creates a turning effect with a real direction in exactly the same way an engineered lever's force does."},
            {"text": 'Direction does matter, but only for the triceps and not for the biceps.', "correct": False,
             "why": "Both muscles' pulls have a direction, and it is the opposition between the two that lets the joint move both ways."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h29',
        "band": 'harder',
        "text": "A physiotherapist recommends a longer-handled tool to a patient with a weak grip, so that less force is needed to turn it. Explain the one thing this trade genuinely costs the patient, using what a wheelbarrow's long handles cost.",
        "options": [
            {"text": 'Nothing at all — a longer handle is a pure improvement with no real trade.', "correct": False,
             "why": 'Every lever trades force for distance somewhere. A longer handle needs less force but moves the hand further for the same turn.'},
            {"text": "The patient's hand must move further to turn the tool through the same angle.", "correct": True},
            {"text": 'The tool becomes weaker and cannot turn a stiff object at all.', "correct": False,
             "why": 'A longer handle increases the turning effect for the same hand force, which makes turning a stiff object easier, not harder.'},
            {"text": "The patient's grip strength itself gets permanently weaker from using it.", "correct": False,
             "why": 'Using a longer-handled tool does not weaken the muscles — the cost is purely in how far the hand must move, not in strength lost.'},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h30',
        "band": 'harder',
        "text": 'A skeleton with an unusually long heel bone is compared with one with a short heel bone, both from animals of the same body weight. Predict which needs less calf-muscle force to raise that body weight onto tiptoes, and why.',
        "options": [
            {"text": 'The short heel bone, since a shorter lever always produces more force at the foot.', "correct": False,
             "why": 'A shorter distance from the joint needs a bigger muscle force for the same turning effect, not a smaller one.'},
            {"text": 'Neither — heel bone length makes no difference to the force needed.', "correct": False,
             "why": "The heel bone's length sets the distance the calf tendon acts at, which directly changes the force the muscle must supply."},
            {"text": "The long heel bone — it gives the tendon a bigger distance, needing less force.", "correct": True},
            {"text": 'The short heel bone, because a shorter bone is stronger and can take a bigger push.', "correct": False,
             "why": "How strong the bone itself is does not set the muscle force needed. The distance the tendon acts at is what does, and a short heel makes that distance smaller."},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h31',
        "band": 'harder',
        "text": "Compare a wheelbarrow's wheel and a human ankle joint acting as pivots. Both are pivots for a lever, yet one reduces the force needed at the effort and the other increases it. Explain why the same role produces opposite outcomes.",
        "options": [
            {"text": "The wheelbarrow's wheel is a better pivot than the ankle joint, since it turns more smoothly.", "correct": False,
             "why": 'How smoothly a pivot turns does not decide whether force is saved or spent — the relative positions of load and effort do.'},
            {"text": 'The ankle is not really a pivot at all, unlike the wheel.', "correct": False,
             "why": 'The ankle acts as a genuine fixed point the foot turns about while standing on tiptoes, exactly like a pivot.'},
            {"text": 'The outcomes are not really opposite, since both arrangements save force in the end.', "correct": False,
             "why": "The calf muscle needs far more force than the load it supports, while the wheelbarrow's handles need far less — a genuine opposite outcome."},
            {"text": "What matters is where the effort acts relative to the load, not the pivot itself.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b2-04-h32',
        "band": 'harder',
        "text": "A student argues that because turning effect is always force multiplied by distance, doubling a muscle's own length must double the turning effect it can produce. Evaluate that.",
        "options": [
            {"text": "False — the distance is measured from the joint to the tendon, not the muscle's own length.", "correct": True},
            {"text": 'True, since a longer muscle is simply a bigger distance.', "correct": False,
             "why": "The formula's distance is from the joint to the tendon's attachment, not the length of the muscle belly itself, which can be far away from either end."},
            {"text": 'True, but only for muscles longer than about ten centimetres.', "correct": False,
             "why": "Muscle length is simply the wrong quantity here, whatever the muscle's size — the formula needs the tendon's distance from the joint."},
            {"text": 'False, because turning effect does not actually depend on distance at all.', "correct": False,
             "why": "Turning effect genuinely does depend on distance — specifically the distance from the joint to where the force acts, not the muscle's own length."},
        ],
        "figure": None,
    },
]
