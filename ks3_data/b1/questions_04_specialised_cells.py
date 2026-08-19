"""B1 lesson 04 — Specialised cells: twelve questions (MRB-269).

These probe the one idea the lesson is built on — a specialised cell has no
new parts, only the same seven turned up, turned down or reshaped, and every
tuning is an answer to a physical problem. The distractors are built from the
lesson's three declared misconceptions: CELL-14 (specialised cells are made of
different parts from ordinary cells), CELL-15 (a red blood cell is not really a
cell, then) and CELL-05 (every cell in your body has a nucleus). Three more
come from the sabotage engine's own findings — that water gets in for free and
minerals have to be paid for, that a tail is a motor and a motor needs fuel,
and that a handover between cells costs time rather than strength. The `harder`
band takes the rule somewhere the lesson never goes (a gut lining cell), joins
two specimens against each other (the halved nucleus against the destroyed
one), and turns the key fact back on the one row that looks like an exception
(the fatty sheath).
"""

UNIT = "B1"
LESSON = "specialised-cells"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-04-e01",
        "band": "easier",
        "text": "A sperm cell, a nerve cell, a root hair cell and a red blood "
                "cell look nothing like each other. What do all four have in "
                "common?",
        "options": [
            {"text": "Each is built from its own special set of parts, made "
                     "for the job it does.",
             "correct": False,
             "why": "There is no special parts list. Every one of these is "
                    "built from the same seven parts as a plain cheek cell — "
                    "what differs is how they are tuned."},
            {"text": "They are built from the same seven parts, some turned "
                     "up, some down, some reshaped.",
             "correct": True},
            {"text": "They all carry about the same number of mitochondria "
                     "as each other.",
             "correct": False,
             "why": "Mitochondria are one of the things that differs most. A "
                    "sperm cell is packed with them; a red blood cell has "
                    "none at all."},
            {"text": "They all keep a full nucleus, however unusual the rest "
                     "of the cell is.",
             "correct": False,
             "why": "A red blood cell destroys its nucleus and a sperm cell "
                    "carries only half a set. The nucleus gets tuned like "
                    "everything else."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e02",
        "band": "easier",
        "text": "As a red blood cell matures in the marrow it pushes its "
                "nucleus out and destroys it. What fills the space that is "
                "freed?",
        "options": [
            {"text": "Haemoglobin — the red protein that fills the cell and "
                     "that oxygen sticks to.",
             "correct": True},
            {"text": "Extra mitochondria, to power the trip round and round "
                     "your body.",
             "correct": False,
             "why": "It has no mitochondria at all, and that is deliberate: a "
                    "cell with them would use up some of the oxygen it is "
                    "meant to be delivering."},
            {"text": "A large vacuole, which holds the oxygen as a store "
                     "until it is needed.",
             "correct": False,
             "why": "A permanent vacuole is a plant cell part and it holds "
                    "cell sap. Oxygen is held by haemoglobin, not in a bag of "
                    "liquid."},
            {"text": "Nothing. The space is left empty, which makes the cell "
                     "lighter to push around.",
             "correct": False,
             "why": "Room for cargo is the whole point of the trade. An empty "
                    "space would mean the cell gave up its nucleus for "
                    "nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e03",
        "band": "easier",
        "text": "A root hair cell is a plant cell, but it is not green. Why "
                "not?",
        "options": [
            {"text": "It is not really a plant cell — only the cells up in "
                     "the leaves and stem count.",
             "correct": False,
             "why": "It has a cell wall and a permanent vacuole, so it is a "
                    "plant cell. Being a plant cell has never meant being "
                    "green."},
            {"text": "Its chloroplasts are colourless underground and only "
                     "turn green up in the light.",
             "correct": False,
             "why": "There are no chloroplasts there to change colour. No "
                    "light reaches a root, so the cell never builds them."},
            {"text": "No light reaches a root, so this cell builds no "
                     "chloroplasts at all.",
             "correct": True},
            {"text": "The soil packed tightly around it hides the green "
                     "colour from being seen.",
             "correct": False,
             "why": "Wash the root and it is still not green. The colour is "
                    "missing because the chloroplasts are, not because they "
                    "are covered up."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e04",
        "band": "easier",
        "text": "Some cells never stop working — swimming, sweeping or "
                "contracting all day long. Which part would you expect such a "
                "cell to have far more of?",
        "options": [
            {"text": "A bigger nucleus, because harder work needs a longer "
                     "list of instructions.",
             "correct": False,
             "why": "The nucleus holds the instructions but releases no "
                    "energy. Working harder does not need a longer "
                    "instruction book."},
            {"text": "A thicker cell membrane, so that it can stand up to all "
                     "that constant work.",
             "correct": False,
             "why": "The membrane controls what goes in and out; it is not "
                    "what wears out. Constant work is an energy problem, not "
                    "a strength one."},
            {"text": "A large vacuole, because that is where a cell keeps the "
                     "energy it will spend.",
             "correct": False,
             "why": "A vacuole holds cell sap and keeps a plant cell firm. It "
                    "stores no energy, and animal cells have no permanent "
                    "vacuole anyway."},
            {"text": "Mitochondria, because movement costs energy and that is "
                     "where it is released from food.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-04-s01",
        "band": "standard",
        "text": "A red blood cell contains no mitochondria at all. Why is "
                "that an advantage rather than a fault?",
        "options": [
            {"text": "Mitochondria would make it too heavy to be pushed all "
                     "the way round the body.",
             "correct": False,
             "why": "Weight is not the problem this cell is up against. What "
                    "it is short of is room for cargo and surface to load it "
                    "through."},
            {"text": "With no mitochondria it needs no food at all, so it can "
                     "live for years.",
             "correct": False,
             "why": "It lasts about 120 days and cannot repair itself, "
                    "because it has no nucleus. Losing the mitochondria is "
                    "about the cargo, not about lifespan."},
            {"text": "It cannot use any of the oxygen it is carrying, so the "
                     "whole load gets delivered.",
             "correct": True},
            {"text": "It releases energy straight from the oxygen instead, "
                     "which is faster than using food.",
             "correct": False,
             "why": "Releasing energy from food is a job for mitochondria. "
                    "With none, this cell does not do it at all — and that is "
                    "exactly the point."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s02",
        "band": "standard",
        "text": "Every mitochondrion is taken out of a root hair cell. The "
                "hair, the wall, the vacuole and the nucleus are all left "
                "exactly as they were. What happens next?",
        "options": [
            {"text": "Water still soaks in on its own, but minerals stop "
                     "being pulled in.",
             "correct": True},
            {"text": "Water and minerals both stop entering the cell straight "
                     "away.",
             "correct": False,
             "why": "Water needs no energy — it moves on its own from where "
                    "there is more of it to where there is less. Only the "
                    "minerals stop."},
            {"text": "Minerals keep arriving as normal, but the water stops "
                     "entering.",
             "correct": False,
             "why": "That is the wrong way round. Water is the one that gets "
                    "in for free; minerals are the ones that have to be paid "
                    "for."},
            {"text": "Nothing changes, because it is the hair that does the "
                     "absorbing here.",
             "correct": False,
             "why": "The hair gives the surface, but there is more nitrate "
                    "inside the cell than in the soil, so dragging more in "
                    "against that costs energy the mitochondria supplied."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s03",
        "band": "standard",
        "text": "A sperm cell's midpiece is emptied of mitochondria. Its tail "
                "is still perfectly formed and still attached. What happens "
                "when it sets off?",
        "options": [
            {"text": "The tail drops off, because there is nothing left "
                     "holding it on to the head.",
             "correct": False,
             "why": "The tail is a structure and it is still attached. What "
                    "has been taken away is not what holds it on, it is what "
                    "powers it."},
            {"text": "The tail beats weakly and then stops, because nothing "
                     "is releasing energy for it.",
             "correct": True},
            {"text": "It swims normally, because a tail whips from side to "
                     "side under its own power.",
             "correct": False,
             "why": "A tail is a motor, and a motor needs energy released for "
                    "it. Nothing in a cell moves for free."},
            {"text": "The nucleus stops working, so it has no instructions "
                     "left to deliver.",
             "correct": False,
             "why": "The nucleus is untouched and its half set of chromosomes "
                    "is intact. The problem is that the cell can no longer "
                    "travel far enough to deliver them."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s04",
        "band": "standard",
        "text": "A red blood cell is a disc dished in on both sides, not a "
                "ball. Both shapes would hold the same volume — so why is the "
                "disc better?",
        "options": [
            {"text": "A ball of the same size would leave no room inside it "
                     "for haemoglobin.",
             "correct": False,
             "why": "Same volume means the same room inside. Shape changes "
                    "how much surface the cell has, not how much fits in it."},
            {"text": "A ball would have more surface, so the oxygen would "
                     "leak back out of it.",
             "correct": False,
             "why": "It is the other way round: rounding something up gives a "
                    "given volume the smallest surface it can possibly have."},
            {"text": "The dip in the middle is simply the hollow the nucleus "
                     "left behind.",
             "correct": False,
             "why": "Haemoglobin filled that space long ago. The dish is a "
                    "shape the cell is built into, not a dent left by "
                    "something missing."},
            {"text": "More surface for the same volume, and floppy enough to "
                     "fold through narrow vessels.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-04-h01",
        "band": "harder",
        "text": "A cell lining your small intestine has a heavily folded edge "
                "facing the gut, and its cytoplasm is packed with "
                "mitochondria. Which two of the four problems is it solving?",
        "options": [
            {"text": "Not enough surface, and nowhere to put the cargo.",
             "correct": False,
             "why": "Nothing has been thrown away here to make room — the "
                    "cell keeps all its parts. The mitochondria point at "
                    "constant work, not at cargo space."},
            {"text": "Too far to travel, and work that never stops.",
             "correct": False,
             "why": "The mitochondria do say constant work. But this cell is "
                    "not stretched across a distance: the folded edge is "
                    "about surface, not length."},
            {"text": "Nowhere to put the cargo, and too far to travel.",
             "correct": False,
             "why": "Neither fits. A folded edge is a surface adaptation and "
                    "mitochondria are an energy one, and nothing here has "
                    "been given up or stretched out."},
            {"text": "Not enough surface, and work that never stops.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h02",
        "band": "harder",
        "text": "A red blood cell and a sperm cell both do something unusual "
                "with the nucleus. What is the difference between them?",
        "options": [
            {"text": "Neither of them has a nucleus left, so neither one can "
                     "ever repair itself or divide.",
             "correct": False,
             "why": "A sperm cell does have a nucleus — delivering what is "
                    "inside it is the entire job. It is the red blood cell "
                    "that destroyed its own."},
            {"text": "The red blood cell destroys its nucleus; the sperm cell "
                     "keeps one with half a set of chromosomes.",
             "correct": True},
            {"text": "Both keep a nucleus with half a set of chromosomes, "
                     "ready to be joined to another half.",
             "correct": False,
             "why": "Half a set is the sperm cell alone, so that it can be "
                    "added to the half in the egg. A red blood cell has no "
                    "nucleus left at all."},
            {"text": "The sperm cell destroys its nucleus for speed; the red "
                     "blood cell halves its for room.",
             "correct": False,
             "why": "That is both cells the wrong way round. A sperm cell "
                    "with no nucleus would arrive carrying nothing worth "
                    "delivering."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h03",
        "band": "harder",
        "text": "A student writes: “The nerve cell grows a fatty sheath, so "
                "it has an eighth part that no other cell has.” What is wrong "
                "with that sentence?",
        "options": [
            {"text": "The sheath is other cells wrapped around this one, so "
                     "the nerve cell grows no new part.",
             "correct": True},
            {"text": "Nothing is wrong. A specialised cell grows whatever "
                     "extra parts its own job needs.",
             "correct": False,
             "why": "No cell grows a part that is not on the list of seven. "
                    "Specialisation turns those parts up, turns them down or "
                    "reshapes them — that is all it ever is."},
            {"text": "The sheath is the nerve cell's own, but it is wrong "
                     "that no other cell has one.",
             "correct": False,
             "why": "The problem is not who else has one. It is that the "
                    "nerve cell never built the sheath: other cells wrapped "
                    "themselves around it."},
            {"text": "There is no sheath at all. A nerve signal runs down "
                     "bare cable the whole way.",
             "correct": False,
             "why": "The sheath is really there, and it is what lets the "
                    "signal jump from gap to gap. Strip it off and the signal "
                    "creeps along and leaks."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h04",
        "band": "harder",
        "text": "The nerve running from your spine to your toe is one single "
                "cell over a metre long. Why is that better than a relay of "
                "short cells covering the same distance?",
        "options": [
            {"text": "A signal cannot cross the junction between one cell and "
                     "the next at all.",
             "correct": False,
             "why": "It can — that is how any nerve passes its message on to "
                    "the next cell. A junction is slow, not impossible."},
            {"text": "Short cells could not each carry a fatty sheath, so "
                     "every one of them would conduct slowly.",
             "correct": False,
             "why": "Each short cell could keep its sheath and work "
                    "perfectly. The cost is not inside the cells, it is in "
                    "the gaps between them."},
            {"text": "Every handover is chemical, and chemistry is slower "
                     "than a signal running down a cable.",
             "correct": True},
            {"text": "The signal fades a little at every handover until "
                     "nothing arrives at the other end.",
             "correct": False,
             "why": "The message does arrive — it arrives late. What each "
                    "junction costs is time, and a reflex that arrives late "
                    "is a reflex that failed."},
        ],
        "figure": None,
    },
]
