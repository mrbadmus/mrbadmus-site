"""P4 lesson 09 — Non-contact forces: twelve questions (MRB-223).

Written against Design's page. The balloon and the hair, the eight-case
sorter and the three cards are hers.

The discriminations, in the order the lesson builds them:

  · a contact force vanishes the moment the objects separate;
  · air resistance is CONTACT, because particles strike the surface —
    a gap you cannot see is not a gap;
  · gravity only ever attracts, and the other two can repel
    (`FORCE-46`);
  · nothing needs to be in the gap (`FORCE-44`);
  · astronauts float because they are falling, not because gravity has
    gone (`FORCE-45`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — index cycles 2, 3, 1, 0, giving three of each.

⚠️ Rung 1 (which of these is non-contact) and Rung 2 (why astronauts
float) are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "non-contact-forces"
LESSON_NUMBER = 9

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-09-e01",
        "band": "easier",
        "text": "Which of these is NOT one of the three non-contact forces "
                "named at Key Stage 3?",
        "options": [
            {"text": "Gravity", "correct": False,
             "why": "Gravity is one of the three, and it is the one holding "
                    "you to the planet."},
            {"text": "Magnetism", "correct": False,
             "why": "Magnetism is one of the three — a magnet works "
                    "through paper, air or a vacuum."},
            {"text": "Friction", "correct": True},
            {"text": "The electrostatic force", "correct": False,
             "why": "It is one of the three, and it is the one lifting the "
                    "hair towards the balloon."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e02",
        "band": "easier",
        "text": "Which of these can only ever ATTRACT?",
        "options": [
            {"text": "Magnetism", "correct": False,
             "why": "Like poles repel. A magnet can push as well as pull."},
            {"text": "The electrostatic force", "correct": False,
             "why": "Like charges repel. Two rubbed balloons push each other "
                    "apart."},
            {"text": "Friction", "correct": False,
             "why": "Friction is a contact force, and it neither attracts "
                    "nor repels — it resists sliding."},
            {"text": "Gravity", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e03",
        "band": "easier",
        "text": "A magnet holds a note to a steel fridge door, and it still "
                "holds with a sheet of paper slipped between them. What does "
                "that show?",
        "options": [
            {"text": "That paper is magnetic.", "correct": False,
             "why": "It is not. The pull is between the magnet and the "
                    "steel, straight through the paper."},
            {"text": "That the force does not need the two to be touching.",
             "correct": True},
            {"text": "That the magnet is stuck by friction.",
             "correct": False,
             "why": "Friction needs the surfaces to press together, and it "
                    "would not survive the paper."},
            {"text": "That the note is very light.", "correct": False,
             "why": "It is, but that is not what the paper test shows. The "
                    "test is about whether contact is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-e04",
        "band": "easier",
        "text": "A magnet is brought near a copper coin and nothing happens. "
                "Why?",
        "options": [
            {"text": "The coin is too heavy.", "correct": False,
             "why": "A steel paperclip of the same mass would jump to it."},
            {"text": "The magnet has run out of magnetism.", "correct": False,
             "why": "The same magnet still attracts iron and steel. Nothing "
                    "about it has been used up."},
            {"text": "The air in between is blocking the pull.",
             "correct": False,
             "why": "Magnetism crosses air perfectly well — and a vacuum "
                    "too."},
            {"text": "Copper is not a magnetic material — a magnet does "
                     "not attract all metals.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-09-s01",
        "band": "standard",
        "text": "Why is air resistance filed as a CONTACT force?",
        "options": [
            {"text": "Because air is heavy enough to press down.",
             "correct": False,
             "why": "Its weight is a separate matter. What makes it contact "
                    "is that it touches the surface."},
            {"text": "Because air is made of particles, and they strike the "
                     "surface.", "correct": True},
            {"text": "Because it only acts on objects that are touching the "
                     "ground.", "correct": False,
             "why": "It acts hardest on things that are touching nothing at "
                    "all — a skydiver, for instance."},
            {"text": "Because it is a kind of friction, and friction is "
                     "contact.", "correct": False,
             "why": "Close, but circular. The reason friction is a contact "
                    "force is the same reason: surfaces touching."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s02",
        "band": "standard",
        "text": "A compass needle swings to point north. What kind of force "
                "acts on it, and what does the force DO?",
        "options": [
            {"text": "Gravity, and it pulls the needle down.",
             "correct": False,
             "why": "Gravity does act on the needle, but it is not what "
                    "points it north."},
            {"text": "A contact force from the case, and it turns the "
                     "needle.", "correct": False,
             "why": "Remove the case and the needle still points north. The "
                    "force acts across a gap."},
            {"text": "Magnetism, and it moves the needle sideways.",
             "correct": False,
             "why": "The kind is right. But the needle does not travel "
                    "sideways — it turns on its pivot."},
            {"text": "Magnetism, and it turns the needle — a moment.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s03",
        "band": "standard",
        "text": "A rubbed balloon lifts someone's hair across a clear gap of "
                "a centimetre. What could you do to show it is a force "
                "rather than moving air?",
        "options": [
            {"text": "Blow gently at the hair and compare.",
             "correct": False,
             "why": "That shows air CAN move hair. It does not rule it out "
                    "as the cause here."},
            {"text": "Hold the balloon perfectly still just above the hair "
                     "and see whether the hair still rises.", "correct": True},
            {"text": "Rub the balloon harder.", "correct": False,
             "why": "That makes the effect bigger, and a moving-air "
                    "explanation would predict the same."},
            {"text": "Use a bigger balloon.", "correct": False,
             "why": "Size changes how much charge it can carry, but it does "
                    "not separate the two explanations."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-s04",
        "band": "standard",
        "text": "Which pair of objects is the force between, when a stone "
                "falls after being dropped?",
        "options": [
            {"text": "The stone and the air.", "correct": False,
             "why": "Air resistance is real and it is a contact force, but "
                    "it is not what makes the stone fall."},
            {"text": "The stone and your hand.", "correct": False,
             "why": "Your hand's force ended the moment you let go."},
            {"text": "The stone and the Earth.", "correct": True},
            {"text": "The stone and the ground it is heading for.",
             "correct": False,
             "why": "The ground is part of the Earth, but the pull is from "
                    "the whole planet and acts long before contact."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-09-h01",
        "band": "harder",
        "text": "A magnet attracts a paperclip inside a jar. The air is then "
                "pumped out. What is the modern explanation for the pull "
                "continuing?",
        "options": [
            {"text": "A thin layer of air always remains and carries it.",
             "correct": False,
             "why": "The pull works in a hard vacuum, and between the Earth "
                    "and the Moon, where there is no air to remain."},
            {"text": "The magnet changes the SPACE around it — a field — "
                     "and anything magnetic entering that space feels a "
                     "force.", "correct": True},
            {"text": "The glass of the jar conducts the magnetism.",
             "correct": False,
             "why": "Glass is not magnetic and is doing nothing. Remove the "
                    "jar entirely and the pull is the same."},
            {"text": "The paperclip pulls itself towards the magnet using "
                     "its own magnetism.", "correct": False,
             "why": "It becomes magnetised, but that is half the pair — "
                    "the force still acts between two objects across a gap."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h02",
        "band": "harder",
        "text": "Gravity is by far the WEAKEST of the three non-contact "
                "forces — a small magnet beats the whole Earth on a "
                "paperclip. So why is gravity the one that shapes planets "
                "and galaxies?",
        "options": [
            {"text": "Because gravity gets stronger over long distances.",
             "correct": False,
             "why": "It gets weaker with distance, like the others."},
            {"text": "Because gravity acts instantly and the others do not.",
             "correct": False,
             "why": "None of them acts instantly — a change in any field "
                    "spreads at the speed of light."},
            {"text": "Because gravity never repels, so it only ever adds up "
                     "— while the other two come in two signs and nearly "
                     "cancel on any large object.", "correct": True},
            {"text": "Because planets are made of a special kind of matter.",
             "correct": False,
             "why": "They are made of ordinary atoms, and every one of them "
                    "pulls."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h03",
        "band": "harder",
        "text": "A maglev train floats a centimetre above its track. Sort "
                "the forces on it correctly.",
        "options": [
            {"text": "Lift and drive magnetic; weight gravitational; air "
                     "resistance contact.", "correct": True},
            {"text": "Everything is non-contact, because nothing is "
                     "touching.", "correct": False,
             "why": "Air resistance is still acting and it is a contact "
                    "force — the air particles strike the train."},
            {"text": "Lift is magnetic; everything else is contact.",
             "correct": False,
             "why": "Its weight is the Earth's gravitational pull, which is "
                    "non-contact, and so is the magnetic drive."},
            {"text": "There are no forces on it while it is floating.",
             "correct": False,
             "why": "It has weight, lift, drive and air resistance. It is "
                    "floating because they balance vertically."},
        ],
        "figure": None,
    },
    {
        "id": "p4-09-h04",
        "band": "harder",
        "text": "The space station orbits about 400 km up. Roughly how "
                "strong is the Earth's pull there compared with at ground "
                "level?",
        "options": [
            {"text": "Zero — that is why astronauts float.",
             "correct": False,
             "why": "With zero pull the station would leave in a straight "
                    "line. It is falling, which is why the crew float."},
            {"text": "About a hundredth of it.", "correct": False,
             "why": "Far too small a figure. 400 km is a small addition to "
                    "the Earth's 6 400 km radius."},
            {"text": "About half of it.", "correct": False,
             "why": "Still too weak. You would have to go several thousand "
                    "kilometres up for that."},
            {"text": "Only slightly weaker.", "correct": True},
        ],
        "figure": None,
    },
]
