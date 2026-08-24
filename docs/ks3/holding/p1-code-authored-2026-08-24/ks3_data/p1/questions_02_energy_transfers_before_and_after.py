"""P1 lesson 02 — Energy transfers: before and after: twelve questions.

These probe the sentence the lesson exists to install — one store down,
another store up, by the same amount — over the six processes `KS3.P.ECT.03`
names. The distractors are built from ENER-10, that a falling object is given
its energy by gravity, and from the two habits the bench is aimed at: telling
a story about the middle instead of comparing the two ends, and drawing the
system boundary round the object alone so that energy appears from nowhere.

Answer positions cycle 2, 3, 0, 1. No figures.
"""

UNIT = "P1"
LESSON = "energy-transfers-before-and-after"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-02-e01",
        "band": "easier",
        "text": "A conker falls from a branch and speeds up. Which store "
                "empties?",
        "options": [
            {"text": "The conker's chemical store, used up as it falls",
             "correct": False,
             "why": "Nothing inside the conker is reacting. A chemical store "
                    "empties when substances change into other substances."},
            {"text": "Gravity's own store, which is what gravity is for",
             "correct": False,
             "why": "Gravity is a force, measured in newtons. A force is not "
                    "an amount of energy and has no store to spend."},
            {"text": "The gravitational store",
             "correct": True},
            {"text": "The thermal store of the air around it",
             "correct": False,
             "why": "The air's thermal store actually FILLS a little, as the "
                    "conker pushes past it. It is not what emptied."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e02",
        "band": "easier",
        "text": "A gas hob heats a pan of water. Which pair of stores is "
                "right?",
        "options": [
            {"text": "Thermal down, chemical up",
             "correct": False,
             "why": "That is the right pair the wrong way round. The gas is "
                    "burnt and it is the water that ends up hot."},
            {"text": "Elastic down, thermal up",
             "correct": False,
             "why": "Nothing is stretched, squashed or bent anywhere in a gas "
                    "hob heating a pan."},
            {"text": "Kinetic down, thermal up",
             "correct": False,
             "why": "Nothing was moving fast to start with and nothing has "
                    "slowed down. Ask what the gas is."},
            {"text": "Chemical down, thermal up",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e03",
        "band": "easier",
        "text": "You pull a spring out and hold it stretched. Which store has "
                "filled?",
        "options": [
            {"text": "The elastic store of the spring",
             "correct": True},
            {"text": "The kinetic store of the spring",
             "correct": False,
             "why": "You are holding it still. Nothing is moving at the "
                    "moment the question asks about."},
            {"text": "The chemical store of the spring",
             "correct": False,
             "why": "The steel of the spring is exactly the same substance "
                    "stretched as it was loose. Nothing reacted."},
            {"text": "The gravitational store of your arm",
             "correct": False,
             "why": "You could pull it sideways and the store would fill just "
                    "the same. Nothing about height is involved."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-e04",
        "band": "easier",
        "text": "A cyclist pushes off from a standstill and gets up to speed. "
                "Which store empties?",
        "options": [
            {"text": "The gravitational store, because she leans forward",
             "correct": False,
             "why": "The road is flat, so her height barely changes. Leaning "
                    "is not the same as descending."},
            {"text": "The chemical store in her muscles",
             "correct": True},
            {"text": "The kinetic store, because she is now moving",
             "correct": False,
             "why": "Her kinetic store has FILLED — she went from stopped to "
                    "moving. The question asks what paid for it."},
            {"text": "The elastic store of the tyres",
             "correct": False,
             "why": "The tyres squash and spring back many times a second and "
                    "come out even. Nothing there is paying for the speed."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-02-s01",
        "band": "standard",
        "text": "A torch is switched on and left until the cell goes flat. "
                "Which pair describes it best?",
        "options": [
            {"text": "Electrical down, light up",
             "correct": False,
             "why": "Neither of those is a store. An electric current and "
                    "light are both ways of transferring."},
            {"text": "Chemical down, kinetic up",
             "correct": False,
             "why": "Nothing in a torch speeds up. Half of this is right; ask "
                    "what fills at the end."},
            {"text": "Chemical down, thermal up",
             "correct": True},
            {"text": "Chemical down, light up",
             "correct": False,
             "why": "The first half is right. But light is not a store — it "
                    "crosses the room and fills the walls' thermal store."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s02",
        "band": "standard",
        "text": "A runner eats a banana and runs for twenty minutes, ending "
                "up hot. Which store fills MOST?",
        "options": [
            {"text": "Her kinetic store, because she was moving throughout",
             "correct": False,
             "why": "Her kinetic store fills once, as she gets going, and "
                    "stays roughly level after that. Being hot is the bigger "
                    "clue."},
            {"text": "Her gravitational store, because running lifts her",
             "correct": False,
             "why": "She rises and falls with every stride and comes out "
                    "level, unless the run is uphill."},
            {"text": "Her chemical store, topped up by the banana",
             "correct": False,
             "why": "The banana's chemical store is what EMPTIED. That is "
                    "where the whole thing was paid from."},
            {"text": "Her thermal store, and the air's",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s03",
        "band": "standard",
        "text": "What is the difference between gravity and a gravitational "
                "store?",
        "options": [
            {"text": "Gravity is a force in newtons; the store is energy in "
                     "joules",
             "correct": True},
            {"text": "Gravity acts on Earth and the store acts in space",
             "correct": False,
             "why": "Both exist everywhere there is a mass. The difference is "
                    "what kind of quantity each one is."},
            {"text": "Gravity is what fills the store as an object falls",
             "correct": False,
             "why": "The store EMPTIES as an object falls, and it was filled "
                    "by whoever raised the object."},
            {"text": "They are two names for the same thing",
             "correct": False,
             "why": "They have different units, which is the clearest "
                    "possible sign that they are different quantities."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-s04",
        "band": "standard",
        "text": "Which of these is a way of TRANSFERRING energy rather than a "
                "store that changes?",
        "options": [
            {"text": "The chemical store in a lump of coal",
             "correct": False,
             "why": "A lump of coal left in a bunker for a year still has it. "
                    "That is a store."},
            {"text": "Heating a pan on a hob",
             "correct": True},
            {"text": "The thermal store of a hot radiator",
             "correct": False,
             "why": "Turn the heating off and come back in five minutes: the "
                    "radiator is still warm. Still there means store."},
            {"text": "The kinetic store of a moving lorry",
             "correct": False,
             "why": "Freeze the moment and there is a definite amount there. "
                    "A store, and a large one."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-02-h01",
        "band": "harder",
        "text": "An astronaut on the Moon lifts a hammer and drops it. Gravity "
                "there is about a sixth of ours. What is different from doing "
                "it on Earth?",
        "options": [
            {"text": "Both the lifting and the falling involve less energy",
             "correct": True},
            {"text": "Nothing at all, because gravity supplies no energy "
                     "either way",
             "correct": False,
             "why": "True that gravity supplies none. But the size of the "
                    "force decides how much it costs to lift, and that has "
                    "changed."},
            {"text": "The lifting is the same and the falling is slower",
             "correct": False,
             "why": "The lifting is easier too, and by the same factor. What "
                    "you get back is what you put in."},
            {"text": "The hammer's gravitational store is the same, and it "
                     "just takes longer to empty",
             "correct": False,
             "why": "The store is smaller as well as slower to empty, because "
                    "filling it cost the astronaut less."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h02",
        "band": "harder",
        "text": "A car brakes from 30 mph to a stop. A student says \"the "
                "energy was used up by friction\". What is the accurate "
                "version?",
        "options": [
            {"text": "The kinetic store emptied into the brakes' thermal "
                     "store, and the tyres' and the air's",
             "correct": True},
            {"text": "The kinetic store was destroyed by the friction of the "
                     "brake pads on the discs",
             "correct": False,
             "why": "Nothing destroys energy. Feel a brake disc after a hard "
                    "stop and it will tell you where it went."},
            {"text": "The kinetic store turned into friction, which is a kind "
                     "of energy the brakes make",
             "correct": False,
             "why": "Friction is a force, not a store and not a kind of "
                    "energy. It is the mechanism, not the destination."},
            {"text": "The chemical store in the brake pads emptied to bring "
                     "the car to a stop",
             "correct": False,
             "why": "Brake pads do wear away, but they are not being burnt. "
                    "The car's own movement is what was spent."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h03",
        "band": "harder",
        "text": "A bungee jumper is momentarily still at the lowest point. "
                "Compared with the platform, which stores have changed?",
        "options": [
            {"text": "Gravitational down, kinetic up, elastic unchanged",
             "correct": False,
             "why": "She is STILL at that instant, so her kinetic store is "
                    "empty — exactly as it was on the platform."},
            {"text": "Gravitational up, elastic down, kinetic unchanged",
             "correct": False,
             "why": "She has gone a long way DOWN, so the gravitational store "
                    "emptied. And the cord ends up stretched, not slack."},
            {"text": "Gravitational down, elastic up, kinetic unchanged",
             "correct": True},
            {"text": "Kinetic down, elastic up, gravitational unchanged",
             "correct": False,
             "why": "She started still and ends still, so nothing about her "
                    "kinetic store changed between the two moments — and her "
                    "height certainly did."},
        ],
        "figure": None,
    },
    {
        "id": "p1-02-h04",
        "band": "harder",
        "text": "Why does an energy account for a falling conker only balance "
                "if you include the Earth in the system?",
        "options": [
            {"text": "Because the Earth's gravity is what pushes the conker "
                     "down and has to be paid for",
             "correct": False,
             "why": "A force costs nothing and pays nothing. Ask instead who "
                    "the store belongs to."},
            {"text": "Because the gravitational store is a property of the "
                     "two of them and the gap between",
             "correct": True},
            {"text": "Because the Earth also falls towards the conker and "
                     "gains a kinetic store of its own",
             "correct": False,
             "why": "It does, by an unmeasurably small amount — and that is "
                    "not what makes the account balance."},
            {"text": "Because the ground has to absorb the conker's kinetic "
                     "store when it lands",
             "correct": False,
             "why": "That is true of the landing, which is a later moment. "
                    "The account has to balance during the fall too."},
        ],
        "figure": None,
    },
]
