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
            {"text": "The force pulling something down towards the Earth, "
                     "measured in newtons.",
             "correct": True},
            {"text": "The amount of matter in something, measured in "
                     "kilograms.",
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
            {"text": "At the handle, because the same force acting further "
                     "from the hinge has a bigger turning effect.",
             "correct": True},
            {"text": "At the handle, because a handle is designed to make a "
                     "push into a bigger force.",
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
                     "your hand travels much further round.",
             "correct": False,
             "why": "Your hand does travel further, and that is what you pay "
                    "with. The force is the same; it is the turning effect "
                    "that has grown."},
            {"text": "The same force acting further from the nut has a bigger "
                     "turning effect: turning effect = force × distance.",
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
            {"text": "The muscle distance should be divided by, not "
                     "multiplied — and what comes out is not in newtons.",
             "correct": True},
            {"text": "The weight should be 2 N rather than 20 N, and the "
                     "answer should be divided by 0.32 m.",
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
                     "all three readings are capped.",
             "correct": False,
             "why": "No cap is being hit — the leg press reads 1422 N. What "
                    "one person gives you is a fair comparison between the "
                    "three groups."},
            {"text": "It means a difference between the readings is a "
                     "difference between the muscle groups, not between "
                     "people.",
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
]
