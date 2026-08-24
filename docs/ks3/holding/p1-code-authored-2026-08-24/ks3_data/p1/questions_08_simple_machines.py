"""P1 lesson 08 — Simple machines: force for distance: twelve questions.

These probe `KS3.P.ECT.01` in both of its halves: that a machine gives a
bigger force at the expense of a smaller movement, and that force multiplied
by distance comes out unchanged. The distractors are built from ENER-16 — a
ramp means less work — and from the two arithmetic errors the triangle
exists to prevent: adding the two quantities instead of multiplying them, and
dividing the wrong way round.

⚠️ Half of these carry a calculation, because a QUANTITATIVE lesson whose
bank had none would not be testing the family it belongs to.

No figures. Two zeros, three ones, three twos and four threes.
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
                "work is done?",
        "options": [
            {"text": "23 J",
             "correct": False,
             "why": "That is 20 + 3. Work done is force multiplied by "
                    "distance, never added to it."},
            {"text": "20 J",
             "correct": False,
             "why": "That is the force on its own. Pushing something one "
                    "metre and pushing it a kilometre would then be the "
                    "same."},
            {"text": "6.7 J",
             "correct": False,
             "why": "That is 20 ÷ 3. Cover W on the triangle: it sits alone "
                    "at the top, so the other two are side by side — "
                    "multiply."},
            {"text": "60 J",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e02",
        "band": "easier",
        "text": "What does a simple machine do?",
        "options": [
            {"text": "It reduces the work needed to move a load",
             "correct": False,
             "why": "The work is set by the load and the height, and a "
                    "machine changes neither of them."},
            {"text": "It changes the size or direction of a force",
             "correct": True},
            {"text": "It creates extra energy to help you lift things",
             "correct": False,
             "why": "Nothing creates energy. If a crowbar could, it would "
                    "not need you leaning on it."},
            {"text": "It stores energy so you can use it later",
             "correct": False,
             "why": "A wound spring does that. A lever, a ramp and a pulley "
                    "give back what you put in as you put it in."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e03",
        "band": "easier",
        "text": "A machine lets you lift a load with a quarter of the force. "
                "What happens to the distance you move?",
        "options": [
            {"text": "It stays the same",
             "correct": False,
             "why": "Then force × distance would be a quarter of what it was, "
                    "and three quarters of the work would have come from "
                    "nowhere."},
            {"text": "It is a quarter as far",
             "correct": False,
             "why": "That would make the trade sixteen times better than free, "
                    "which is a long way past impossible."},
            {"text": "It is four times as far",
             "correct": True},
            {"text": "It depends which machine it is",
             "correct": False,
             "why": "It is the same for all three machines on the bench, "
                    "which is what makes it a rule rather than a fact about "
                    "levers."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-e04",
        "band": "easier",
        "text": "What is a newton the unit of?",
        "options": [
            {"text": "Force",
             "correct": True},
            {"text": "Work done",
             "correct": False,
             "why": "Work done is measured in joules — the same unit as "
                    "energy, because it is the same thing."},
            {"text": "Distance",
             "correct": False,
             "why": "Distance is in metres. The triangle's three units are "
                    "joules, newtons and metres, one per corner."},
            {"text": "Energy",
             "correct": False,
             "why": "Energy is in joules. A newton is a push or a pull."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-08-s01",
        "band": "standard",
        "text": "A pulley system lets a builder raise a 400 N load with a "
                "force of 100 N. The load rises 2 m. How far must the rope be "
                "pulled?",
        "options": [
            {"text": "2 m",
             "correct": False,
             "why": "That is how far the load rose. If the rope moved the "
                    "same distance the builder would be getting the force "
                    "for nothing."},
            {"text": "0.5 m",
             "correct": False,
             "why": "That is 2 ÷ 4, which is the trade the wrong way round. A "
                    "smaller force always costs a longer distance."},
            {"text": "4 m",
             "correct": False,
             "why": "Check the multiplier: 400 N down to 100 N is four times "
                    "smaller, not two."},
            {"text": "8 m",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s02",
        "band": "standard",
        "text": "A removal firm can lift a 600 N crate 0.20 m onto a lorry, "
                "or push it up a 1.00 m ramp. Which takes less work?",
        "options": [
            {"text": "Lifting, because the distance is shorter",
             "correct": False,
             "why": "The force is five times bigger over that shorter "
                    "distance. Both come to 120 J."},
            {"text": "Neither — they are exactly the same",
             "correct": True},
            {"text": "The ramp, because the force needed is smaller",
             "correct": False,
             "why": "The smaller force is spread over five times the "
                    "distance. That is what a ramp charges you."},
            {"text": "The ramp, but only if the crate has wheels",
             "correct": False,
             "why": "Wheels reduce friction, which is a real saving on a real "
                    "ramp. The work of raising the crate is unchanged by "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s03",
        "band": "standard",
        "text": "On the bench, an equal-armed lever and a single fixed pulley "
                "both gave a multiplier of 1. What are they for?",
        "options": [
            {"text": "Nothing — they are on the bench to show a machine can "
                     "be useless",
             "correct": False,
             "why": "Both are used constantly in real life. A flagpole has a "
                    "fixed pulley at the top."},
            {"text": "Making a load feel lighter without moving it further",
             "correct": False,
             "why": "That is exactly what a multiplier of 1 does NOT do. The "
                    "force is unchanged."},
            {"text": "Changing the direction you have to pull in",
             "correct": True},
            {"text": "Storing energy for a moment so you can release it "
                     "quickly",
             "correct": False,
             "why": "Neither stores anything. Let go and the load comes "
                    "straight back down."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-s04",
        "band": "standard",
        "text": "Every set-up on the bench read 120 J in and 120 J out. Why "
                "was it 120 J every time?",
        "options": [
            {"text": "Because the bench was set to make the numbers work out",
             "correct": False,
             "why": "The numbers work out because the physics does. Change "
                    "the multiplier and both columns still match."},
            {"text": "Because all three machines happen to be equally good",
             "correct": False,
             "why": "They are not equally good at multiplying force — the "
                    "multipliers run from 1 to 6. The work is the same "
                    "anyway."},
            {"text": "Because the machines were assumed to be frictionless",
             "correct": False,
             "why": "That is why in equals out exactly. It is not why the "
                    "number was 120 rather than something else."},
            {"text": "Because the load was always 600 N and the height "
                     "always 0.20 m",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-08-h01",
        "band": "harder",
        "text": "A wheelchair ramp must raise a 900 N chair 0.30 m using no "
                "more than 90 N. How long must it be?",
        "options": [
            {"text": "3 m",
             "correct": True},
            {"text": "270 m",
             "correct": False,
             "why": "270 is the work in joules. You still have to divide it "
                    "by the 90 N you are allowed."},
            {"text": "0.33 m",
             "correct": False,
             "why": "That is 900 ÷ 2700, which is the division upside down. "
                    "A ramp shorter than the step it climbs is not "
                    "possible."},
            {"text": "10 m",
             "correct": False,
             "why": "That is 900 ÷ 90, which is the multiplier rather than "
                    "the length. Multiply it by the 0.30 m rise."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h02",
        "band": "harder",
        "text": "A real ramp needs 135 J in to deliver 120 J to the load. "
                "What does the extra 15 J show?",
        "options": [
            {"text": "That the conservation of energy does not hold for real "
                     "machines",
             "correct": False,
             "why": "It holds perfectly. The 15 J is still there — it warmed "
                    "the ramp and the crate."},
            {"text": "That friction meant more had to go in than came out "
                     "useful",
             "correct": True},
            {"text": "That the crate was heavier than 600 N after all",
             "correct": False,
             "why": "A heavier crate would raise both numbers together, not "
                    "open a gap between them."},
            {"text": "That the ramp gave 15 J back to the person pushing",
             "correct": False,
             "why": "Nothing came back. The 15 J went into the surfaces as "
                    "warmth, which is the one direction friction ever runs."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h03",
        "band": "harder",
        "text": "Why has nobody ever built a machine that gives out more "
                "than it takes in?",
        "options": [
            {"text": "Because friction always takes a share, and no one has "
                     "removed it",
             "correct": False,
             "why": "Even a perfectly frictionless machine could not do it. "
                    "The reason is stronger than friction."},
            {"text": "Because the materials strong enough have not been "
                     "invented yet",
             "correct": False,
             "why": "No material would help. The obstacle is not an "
                    "engineering one."},
            {"text": "Because the extra would have to come from nowhere",
             "correct": True},
            {"text": "Because patent offices stopped accepting the designs",
             "correct": False,
             "why": "They stopped accepting them BECAUSE the designs never "
                    "work, not the other way round."},
        ],
        "figure": None,
    },
    {
        "id": "p1-08-h04",
        "band": "harder",
        "text": "A student writes \"a block and tackle gives four times as "
                "much force out as you put in, so it makes energy\". Which "
                "half is right?",
        "options": [
            {"text": "Neither half — the force is not four times bigger "
                     "either",
             "correct": False,
             "why": "It genuinely is four times bigger. That is what four "
                    "supporting ropes do."},
            {"text": "The second half — energy really is made, and the force "
                     "is unchanged",
             "correct": False,
             "why": "Both wrong. Nothing makes energy, and the force really "
                    "does go up."},
            {"text": "Both halves, as long as the pulleys are frictionless",
             "correct": False,
             "why": "A frictionless machine breaks even exactly. It never "
                    "gets ahead."},
            {"text": "The first half — the force really is four times bigger",
             "correct": True},
        ],
        "figure": None,
    },
]
