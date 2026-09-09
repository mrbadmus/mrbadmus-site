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
            {"text": "Mitochondria, because movement costs energy and food "
                     "releases it there.",
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
            {"text": "A ball of the same volume would have more surface, so "
                     "oxygen would leak back out of it.",
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
                     "fold through capillaries.",
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
            {"text": "A red blood cell destroys its nucleus; a sperm cell "
                     "keeps half a set of chromosomes.",
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

    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-04-e05",
        "band": "easier",
        "text": "What does it mean to call a cell specialised?",
        "options": [
            {"text": "It is built to do one particular job very well.",
             "correct": True},
            {"text": "It is made from a different set of parts from an "
                     "ordinary cell.", "correct": False,
             "why": "It is the same seven parts, tuned. Nothing new is added "
                    "— something is turned up, turned down, or reshaped."},
            {"text": "It is larger than the cells around it, so that it can "
                     "do more work.", "correct": False,
             "why": "Size is not what the word means. A red blood cell is one "
                    "of the smallest cells you have and one of the most "
                    "highly specialised."},
            {"text": "It can turn into any other kind of cell when it is "
                     "needed.", "correct": False,
             "why": "A specialised cell is committed to its job. A red blood "
                    "cell has thrown its nucleus away and can never become "
                    "anything else."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e06",
        "band": "easier",
        "text": "A red blood cell is described as biconcave. What does that "
                "mean?",
        "options": [
            {"text": "It is a perfect sphere.", "correct": False,
             "why": "A sphere is exactly what it is not. Biconcave means "
                    "dished in on both sides, which gives far more surface "
                    "for the same volume."},
            {"text": "It holds two nuclei instead of one.", "correct": False,
             "why": "It holds none at all — it destroys its nucleus as it "
                    "matures. Biconcave describes its shape, not its "
                    "contents."},
            {"text": "It is folded over on itself down the middle.",
             "correct": False,
             "why": "It is not folded in half. It is a disc pressed in at the "
                    "centre on both faces."},
            {"text": "It is a disc dished in on both sides.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e07",
        "band": "easier",
        "text": "What is a root hair cell built to do?",
        "options": [
            {"text": "Hold the plant upright against the wind.",
             "correct": False,
             "why": "That is done by the root system and the stem as a whole. "
                    "This one cell's job is taking water and minerals out of "
                    "the soil."},
            {"text": "Make food for the root using light.", "correct": False,
             "why": "No light reaches a root, and a root hair cell builds no "
                    "chloroplasts at all. Its job is absorbing water and "
                    "dissolved minerals."},
            {"text": "Take water and dissolved minerals out of the soil.",
             "correct": True},
            {"text": "Carry water up the stem to the leaves.",
             "correct": False,
             "why": "Carrying it upwards happens further in, in the tissue "
                    "that runs up the plant. This cell's job is getting the "
                    "water in from the soil."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e08",
        "band": "easier",
        "text": "Which specialised cell can be over a metre long in a human "
                "being?",
        "options": [
            {"text": "The red blood cell", "correct": False,
             "why": "It is one of the smallest cells you have — small enough "
                    "to fold through a capillary. The metre-long one is the "
                    "nerve cell."},
            {"text": "The nerve cell", "correct": True},
            {"text": "The sperm cell", "correct": False,
             "why": "A sperm cell travels a long way, but the cell itself is "
                    "tiny. The cell that is a metre long runs from the spine "
                    "to the toe."},
            {"text": "The root hair cell", "correct": False,
             "why": "Its hair is long compared with the cell body, and the "
                    "whole thing is still microscopic. It is also a plant "
                    "cell, so it is not in a human at all."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e09",
        "band": "easier",
        "text": "Where in a sperm cell are the mitochondria packed?",
        "options": [
            {"text": "In the tip of the tail, where the beating is "
                     "strongest.", "correct": False,
             "why": "The tail is the machinery, not the fuel supply. The "
                    "mitochondria sit in the midpiece and feed the tail from "
                    "there."},
            {"text": "Inside the nucleus, alongside the chromosomes.",
             "correct": False,
             "why": "The nucleus holds chromosomes and nothing else. The "
                    "mitochondria are in the midpiece, between the head and "
                    "the tail."},
            {"text": "Spread evenly all the way along the cell.",
             "correct": False,
             "why": "They are concentrated, not spread. Packing them into the "
                    "midpiece puts the energy supply exactly where the tail "
                    "joins on."},
            {"text": "In the midpiece, just behind the head.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-04-s05",
        "band": "standard",
        "text": "A sperm cell's nucleus carries half a set of chromosomes "
                "rather than a full set. Why is that an advantage rather than "
                "a fault?",
        "options": [
            {"text": "Half a set is lighter, so the cell can swim faster with "
                     "it.", "correct": False,
             "why": "That saving would be nothing beside the tail and the "
                    "midpiece. The reason is about what happens at the end of "
                    "the journey, not during it."},
            {"text": "Half a set is all the instructions a cell that never "
                     "divides will need.", "correct": False,
             "why": "It is not about running this cell. It is about what "
                    "happens when the sperm reaches the egg."},
            {"text": "It is added to the half a set in the egg, making one "
                     "full set between them.", "correct": True},
            {"text": "The missing half is rebuilt from the egg's instructions "
                     "once the sperm arrives.", "correct": False,
             "why": "Nothing is rebuilt. The egg brings its own half, and the "
                    "two halves together make the full set."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s06",
        "band": "standard",
        "text": "The fatty sheath around a nerve cell is wrapped on in "
                "segments, with tiny gaps between them. What do the gaps do?",
        "options": [
            {"text": "The signal jumps from gap to gap instead of creeping "
                     "along, which makes it far faster.", "correct": True},
            {"text": "They let the cell take in food along its length, since "
                     "it is too long to feed from one end.", "correct": False,
             "why": "Food reaches a nerve cell through its membrane like any "
                    "other cell. The gaps are about speed."},
            {"text": "They stop the sheath squeezing the cell shut where it "
                     "is thickest.", "correct": False,
             "why": "The sheath does not squeeze the cell. The gaps are there "
                    "so the signal can jump between them rather than "
                    "travelling every millimetre."},
            {"text": "They let the cell pass its signal sideways to the cells "
                     "beside it.", "correct": False,
             "why": "The signal is handed on at the branched ends, not out of "
                    "the sides. The gaps make it travel faster along this "
                    "cell."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s07",
        "band": "standard",
        "text": "A muscle cell contracts over and over all day, and its "
                "cytoplasm is crammed with mitochondria. Which problem is "
                "that solving?",
        "options": [
            {"text": "Not enough surface.", "correct": False,
             "why": "That problem is solved by changing shape, as a root hair "
                    "cell does. Cramming in mitochondria pays for constant "
                    "work instead."},
            {"text": "Work that never stops.", "correct": True},
            {"text": "Too far to travel.", "correct": False,
             "why": "That is the nerve cell's problem, and it is answered by "
                    "length rather than by mitochondria."},
            {"text": "Nowhere to put the cargo.", "correct": False,
             "why": "That is the red blood cell's problem, and it is the only "
                    "one solved by throwing a part away. A muscle cell "
                    "carries nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s08",
        "band": "standard",
        "text": "A red blood cell lasts about 120 days, and your marrow makes "
                "about two million new ones a second to keep up. Why must "
                "they be replaced so often?",
        "options": [
            {"text": "They are slowly dissolved by the plasma they travel "
                     "along in.", "correct": False,
             "why": "Nothing dissolves them. They wear out because, with no "
                    "nucleus, they can never repair the damage they "
                    "collect."},
            {"text": "They are used up by the oxygen they carry, a little at "
                     "a time.", "correct": False,
             "why": "The oxygen is cargo — picked up and put down again, with "
                    "none of it spent on the cell. What the cell cannot do is "
                    "repair itself."},
            {"text": "They divide themselves out of existence, making two "
                     "smaller cells each time.", "correct": False,
             "why": "A red blood cell can never divide at all. With no "
                    "nucleus it has no instructions to divide with."},
            {"text": "With no nucleus it cannot repair itself, so damage "
                     "builds up and is never mended.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s09",
        "band": "standard",
        "text": "A nerve cell's mitochondria are not spread evenly along its "
                "length. Where are most of them, and why?",
        "options": [
            {"text": "In the middle of the long cable, because that is where "
                     "the signal is furthest from either end of the "
                     "cell.", "correct": False,
             "why": "The middle is pure cable, and the signal jumps along it "
                    "cheaply. The expensive part is at the ends."},
            {"text": "Just under the fatty sheath, which has to be built and "
                     "held in place along the whole cable.", "correct": False,
             "why": "The sheath is made and maintained by the other cells "
                    "wrapped around it. The mitochondria gather where the "
                    "signal is handed on."},
            {"text": "At the branched ends, where passing the signal to the "
                     "next cell is expensive.", "correct": True},
            {"text": "Around the nucleus, so the instructions are always "
                     "powered.", "correct": False,
             "why": "The nucleus needs no power station beside it. The energy "
                    "goes where the signal crosses to the next cell."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-04-h05",
        "band": "harder",
        "text": "One sperm cell has a perfect tail and an empty midpiece. "
                "Another has a full midpiece and no tail. Neither reaches the "
                "egg. What does that show?",
        "options": [
            {"text": "That the tail is the adaptation that really matters, "
                     "since neither of the two cells got anywhere near the "
                     "egg.", "correct": False,
             "why": "One of them had a perfect tail and still failed. A tail "
                    "with nothing powering it is a motor with no fuel."},
            {"text": "That a sperm cell needs only one of the two "
                     "adaptations, and both of these were simply "
                     "unlucky.", "correct": False,
             "why": "Neither arrived, which is the point. Each was missing "
                    "what the other had, and each failed for it."},
            {"text": "That the midpiece matters more, because the energy has "
                     "to come before the movement.", "correct": False,
             "why": "Ranking them misses it. The cell with a full midpiece "
                    "and no tail went nowhere at all, with all the energy it "
                    "needed."},
            {"text": "That the tail and the mitochondria are one adaptation, "
                     "useless apart.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h06",
        "band": "harder",
        "text": "Your bone marrow makes about two million red blood cells "
                "every second. About how many is that in one minute?",
        "options": [
            {"text": "About 33 000, because 2 000 000 ÷ 60 = 33 000.",
             "correct": False,
             "why": "Dividing gives the number made in a sixtieth of a "
                    "second. A minute is sixty seconds, so you multiply."},
            {"text": "About 120 million, because 2 000 000 × 60 = "
                     "120 000 000.", "correct": True},
            {"text": "About 12 million, because 2 000 000 × 6 = 12 000 000.",
             "correct": False,
             "why": "There are sixty seconds in a minute, not six. "
                    "2 000 000 × 60 = 120 million."},
            {"text": "About 7.2 billion, because 2 000 000 × 3600 = "
                     "7 200 000 000.", "correct": False,
             "why": "3600 is the number of seconds in an hour. For one minute "
                    "the multiplier is 60, which gives 120 million."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h07",
        "band": "harder",
        "text": "Losing its nucleus buys a red blood cell more room for "
                "haemoglobin. Why do your other cells not make the same "
                "trade?",
        "options": [
            {"text": "Because they have to repair themselves and divide, and "
                     "both need the instructions the nucleus holds.",
             "correct": True},
            {"text": "Because only a cell that carries oxygen is small enough "
                     "to manage without one.", "correct": False,
             "why": "Size is not the obstacle. What stops the others is that "
                    "they need the instructions, and the nucleus is where "
                    "those instructions are."},
            {"text": "Because a cell can only lose its nucleus while it is "
                     "being made in the marrow.", "correct": False,
             "why": "That is a detail of how it happens, not a reason why the "
                    "trade is refused. A cell with no instructions can never "
                    "repair itself again."},
            {"text": "Because the other cells would have nothing worth "
                     "putting in the extra room the nucleus was using.",
             "correct": False,
             "why": "Any cell could use more room. The trade is refused "
                    "because the price — no repair, no dividing, four months "
                    "of life — is too high."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h08",
        "band": "harder",
        "text": "A frog takes in oxygen straight through its skin, and under "
                "a microscope that skin is covered in tiny folds. Which "
                "problem is the folding solving?",
        "options": [
            {"text": "Work that never stops — the same problem as the sperm "
                     "cell.", "correct": False,
             "why": "Folds add no energy supply and they do not move. Extra "
                    "surface answers a different problem altogether."},
            {"text": "Too far to travel — the same problem as the nerve "
                     "cell.", "correct": False,
             "why": "Nothing here is covering a long distance. Folds add "
                    "surface, and surface is what the oxygen has to cross."},
            {"text": "Not enough surface — the same problem as the root hair "
                     "cell.", "correct": True},
            {"text": "Nowhere to put the cargo — the same problem as the red "
                     "blood cell.", "correct": False,
             "why": "Nothing is being thrown out to make room. The folds add "
                    "surface for oxygen to cross, which is the root hair "
                    "cell's problem too."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h09",
        "band": "harder",
        "text": "A student designs a red blood cell that keeps its nucleus "
                "and is still dished in on both sides, calling it the best of "
                "both. What is wrong with the design?",
        "options": [
            {"text": "Nothing — the two features are independent of each "
                     "other, so a single cell could easily have "
                     "both.", "correct": False,
             "why": "They are not independent. The nucleus sits where the "
                    "dimple has to be, and it fills the space the "
                    "haemoglobin would use."},
            {"text": "The nucleus takes the room the dimple and the "
                     "haemoglobin need.", "correct": True},
            {"text": "A cell with a nucleus could not fold through a "
                     "capillary, whatever shape it was "
                     "given.", "correct": False,
             "why": "Shape is what decides folding, and plenty of cells with "
                    "nuclei change shape. The real cost here is the room the "
                    "nucleus takes up."},
            {"text": "The nucleus would use up some of the oxygen that the "
                     "cell is meant to carry.", "correct": False,
             "why": "Using oxygen is what mitochondria do, and this cell has "
                    "none of those either. The nucleus's cost is space."},
        ],
        "figure": None,
    },

    # ── MRB-338 expansion ───────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-04-e10",
        "band": "easier",
        "text": "What job does a muscle cell do in your body?",
        "options": [
            {"text": "Shorten, and so pull on the bone it is attached to.",
             "correct": True},
            {"text": "Carry oxygen to the parts of the body that are working "
                     "hardest.",
             "correct": False,
             "why": "That is the red blood cell's job. A muscle cell uses "
                    "oxygen up; it never delivers it."},
            {"text": "Push the bones apart so that a joint can open again.",
             "correct": False,
             "why": "A muscle can only pull. A joint is opened by a second "
                    "muscle pulling the other way."},
            {"text": "Send the signal that tells the body when to move.",
             "correct": False,
             "why": "Signals are carried by nerve cells. The muscle cell is "
                    "what receives the signal and acts on it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e11",
        "band": "easier",
        "text": "A ciliated epithelial cell is covered in tiny hairs called "
                "cilia. What do they do?",
        "options": [
            {"text": "They soak up water and dissolved minerals from the air "
                     "passing over them.",
             "correct": False,
             "why": "Absorbing from soil is the root hair cell's job, and "
                    "nothing is absorbed from air here. Cilia move things "
                    "along."},
            {"text": "They anchor the cell in place so that a cough cannot "
                     "shift it.",
             "correct": False,
             "why": "Cilia beat; they are not anchors. It is the beating "
                    "that does the work."},
            {"text": "They beat together in waves, sweeping mucus and "
                     "trapped dirt along.",
             "correct": True},
            {"text": "They release the energy the cell needs to keep beating "
                     "all day.",
             "correct": False,
             "why": "Energy is released in the mitochondria, which this "
                    "cell has plenty of. The cilia spend that energy rather "
                    "than supplying it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e12",
        "band": "easier",
        "text": "Where in your body would you find ciliated epithelial "
                "cells?",
        "options": [
            {"text": "In the marrow inside your bones.",
             "correct": False,
             "why": "That is where red blood cells are made. Ciliated cells "
                    "line the tubes that air travels down."},
            {"text": "Lining your windpipe and the airways into your lungs.",
             "correct": True},
            {"text": "In the wall of your small intestine, facing the "
                     "digested food.",
             "correct": False,
             "why": "The gut lining is folded for absorbing, not ciliated "
                    "for sweeping."},
            {"text": "Just behind the growing tip of a root.",
             "correct": False,
             "why": "A root tip belongs to a plant, and the cell there is "
                    "the root hair cell."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e13",
        "band": "easier",
        "text": "What is the main job of an egg cell?",
        "options": [
            {"text": "Swim to meet the sperm cell halfway.",
             "correct": False,
             "why": "An egg cell has no tail and does not swim. It is moved "
                    "along by the tube it sits in."},
            {"text": "Carry a full set of chromosomes ready for the new "
                     "organism.",
             "correct": False,
             "why": "It carries half a set, so that the sperm cell's half "
                    "can be added to it."},
            {"text": "Release the energy the sperm cell will need for its "
                     "journey.",
             "correct": False,
             "why": "The sperm cell brings its own mitochondria in its "
                    "midpiece. The egg's store feeds what comes after "
                    "fertilisation."},
            {"text": "Carry half a set of chromosomes, and feed the embryo "
                     "that follows.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e14",
        "band": "easier",
        "text": "An egg cell has far more cytoplasm than a sperm cell. What "
                "is it for?",
        "options": [
            {"text": "A store of food for the embryo to live on in its first "
                     "few days.",
             "correct": True},
            {"text": "Making the egg heavy enough to sink to the bottom of "
                     "the tube.",
             "correct": False,
             "why": "Nothing here depends on sinking. The extra cytoplasm "
                    "is a store of food."},
            {"text": "Spare room kept for the sperm cell's tail once the "
                     "sperm arrives.",
             "correct": False,
             "why": "The tail is left outside; only the head goes in. The "
                    "room holds a food store."},
            {"text": "Holding the oxygen the egg will need while it waits to "
                     "be fertilised.",
             "correct": False,
             "why": "Oxygen is not stored in cytoplasm — carrying oxygen is "
                    "haemoglobin's job in a red blood cell. This store is "
                    "food."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e15",
        "band": "easier",
        "text": "A palisade cell is packed with one part far more than most "
                "plant cells are. Which part?",
        "options": [
            {"text": "Vacuoles, so that it can hold a large store of cell "
                     "sap.",
             "correct": False,
             "why": "A plant cell has one permanent vacuole, not many. What "
                    "is packed in here is chloroplasts."},
            {"text": "Nuclei, because it needs a longer list of instructions "
                     "than other cells.",
             "correct": False,
             "why": "Every cell has one nucleus, and working harder needs "
                    "no extra instructions."},
            {"text": "Chloroplasts, where light is used to make food.",
             "correct": True},
            {"text": "Cell walls, stacked up to make the leaf stiff.",
             "correct": False,
             "why": "One cell, one wall. The leaf is held out flat by other "
                    "tissue altogether."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e16",
        "band": "easier",
        "text": "Whereabouts in a leaf are the palisade cells?",
        "options": [
            {"text": "Right at the bottom, in the shade of everything above "
                     "them.",
             "correct": False,
             "why": "Shade is exactly what a cell full of chloroplasts must "
                    "avoid. They sit at the top."},
            {"text": "In one layer just beneath the top surface of the leaf.",
             "correct": True},
            {"text": "Spread evenly through the whole thickness of the leaf.",
             "correct": False,
             "why": "They are packed into one layer near the top, where the "
                    "light arrives first."},
            {"text": "Around the outside edge, where the leaf is thinnest.",
             "correct": False,
             "why": "The edge is a tiny fraction of a leaf. Light falls on "
                    "the top face, and that is where they are."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e17",
        "band": "easier",
        "text": "What does xylem carry, and in which direction?",
        "options": [
            {"text": "Dissolved sugar, from the leaves down to the roots.",
             "correct": False,
             "why": "That is phloem. Xylem carries water and minerals, and "
                    "it carries them upwards."},
            {"text": "Oxygen, from the leaves out to every part of the "
                     "plant.",
             "correct": False,
             "why": "A plant has no blood and xylem carries no oxygen at "
                    "all."},
            {"text": "Water, from the leaves down to the roots that need it.",
             "correct": False,
             "why": "Right cargo, wrong way. Water is taken in at the root "
                    "and travels up."},
            {"text": "Water and dissolved minerals, from the roots upwards.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e18",
        "band": "easier",
        "text": "What does phloem carry?",
        "options": [
            {"text": "Dissolved sugar made in the leaves.",
             "correct": True},
            {"text": "Water taken in by the root hair cells.",
             "correct": False,
             "why": "Water travels up the xylem. Phloem carries the sugar "
                    "the leaves have made."},
            {"text": "The minerals dragged in from the soil against the "
                     "flow.",
             "correct": False,
             "why": "Minerals travel up in the xylem with the water."},
            {"text": "Air, so that cells deep inside the stem can respire.",
             "correct": False,
             "why": "A plant has no air pipes of this kind. Phloem's cargo "
                    "is dissolved sugar."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e19",
        "band": "easier",
        "text": "Which description fits a xylem tube?",
        "options": [
            {"text": "Living cells joined end to end, each with its own "
                     "nucleus and cytoplasm.",
             "correct": False,
             "why": "That describes phloem. In xylem the cells die, and "
                    "what is left is the hollow wall."},
            {"text": "One enormous cell stretched from the root all the way "
                     "to the leaf.",
             "correct": False,
             "why": "No cell is that long. Xylem is many dead cells stacked "
                    "into a single open pipe."},
            {"text": "Dead cells stacked end to end, with the end walls "
                     "between them gone.",
             "correct": True},
            {"text": "A tunnel running between the cells rather than through "
                     "them.",
             "correct": False,
             "why": "The water travels through the hollow dead cells "
                    "themselves, not through a gap beside them."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e20",
        "band": "easier",
        "text": "What does the word adaptation mean?",
        "options": [
            {"text": "A change a cell makes to itself during its life when "
                     "it needs to.",
             "correct": False,
             "why": "A cell does not redesign itself on demand. An "
                    "adaptation is a feature it already has."},
            {"text": "A feature that helps a living thing, or one cell, do "
                     "its job.",
             "correct": True},
            {"text": "A part that specialised cells have and ordinary cells "
                     "do not.",
             "correct": False,
             "why": "No new parts are ever added. An adaptation is usually "
                    "the same part, turned up, turned down or reshaped."},
            {"text": "The job that a cell has been given to do in the body.",
             "correct": False,
             "why": "The job is the job. The adaptation is the feature that "
                    "makes the cell good at it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e21",
        "band": "easier",
        "text": "What is meant by the surface area of a cell?",
        "options": [
            {"text": "The amount of space inside it.",
             "correct": False,
             "why": "That is its volume. Surface area is the outside, which "
                    "everything has to cross to get in."},
            {"text": "The number of parts sitting on the outside of its "
                     "membrane.",
             "correct": False,
             "why": "It is an amount of area, not a count of parts."},
            {"text": "How heavy it is for its size.",
             "correct": False,
             "why": "That has nothing to do with area. Surface area is how "
                    "much outside the cell has."},
            {"text": "The total amount of outside surface it has.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e22",
        "band": "easier",
        "text": "A student thinks a cell has to be big before it counts as "
                "specialised. Which fact shows that is wrong?",
        "options": [
            {"text": "A red blood cell is one of your smallest cells and one "
                     "of your most specialised.",
             "correct": True},
            {"text": "A nerve cell can be over a metre long, from your spine "
                     "to your toe.",
             "correct": False,
             "why": "That is a large specialised cell, so it agrees with "
                    "the student rather than testing the idea."},
            {"text": "An egg cell is far larger than a sperm cell.",
             "correct": False,
             "why": "Both are highly specialised, so comparing their sizes "
                    "settles nothing."},
            {"text": "Palisade cells are packed tightly together near the "
                     "top of a leaf.",
             "correct": False,
             "why": "True, but it says nothing about size. What settles it "
                    "is a very small cell that is very highly specialised."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e23",
        "band": "easier",
        "text": "What is haemoglobin?",
        "options": [
            {"text": "The dish-shaped hollow in the middle of a red blood "
                     "cell.",
             "correct": False,
             "why": "That is the cell's shape described. Haemoglobin is the "
                    "substance filling it."},
            {"text": "The narrow vessel a red blood cell has to fold up to "
                     "get through.",
             "correct": False,
             "why": "That is a capillary. Haemoglobin is inside the cell, "
                    "not around it."},
            {"text": "The red protein that fills the cell and that oxygen "
                     "sticks to.",
             "correct": True},
            {"text": "The part that releases energy from food inside a red "
                     "blood cell.",
             "correct": False,
             "why": "That would be a mitochondrion, and a red blood cell "
                    "has none."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e24",
        "band": "easier",
        "text": "Which cell of a healthy plant contains no chloroplasts at "
                "all?",
        "options": [
            {"text": "The palisade cell",
             "correct": False,
             "why": "It is the most tightly packed with chloroplasts of any "
                    "cell in the plant."},
            {"text": "The root hair cell",
             "correct": True},
            {"text": "A cell in the middle of a leaf",
             "correct": False,
             "why": "Leaf cells sit in the light and hold chloroplasts, "
                    "though fewer than the palisade layer above them."},
            {"text": "A cell just under the surface of a green stem",
             "correct": False,
             "why": "A green stem is green because those cells hold "
                    "chloroplasts too. It is underground that they are "
                    "missing."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e25",
        "band": "easier",
        "text": "As well as a nucleus, the head of a sperm cell carries a "
                "package of enzymes. What are they for?",
        "options": [
            {"text": "Releasing energy for the tail during the swim.",
             "correct": False,
             "why": "Energy is released in the mitochondria packed into the "
                    "midpiece, not by enzymes in the head."},
            {"text": "Digesting food for the sperm cell while it travels.",
             "correct": False,
             "why": "A sperm cell carries no food store and does not feed "
                    "on the way."},
            {"text": "Joining the two half sets of chromosomes together.",
             "correct": False,
             "why": "The two halves come together inside the egg. The "
                    "enzymes act before that, on the way in."},
            {"text": "Breaking a way through the outer layer of the egg.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e26",
        "band": "easier",
        "text": "Both ends of a nerve cell are branched. What is that for?",
        "options": [
            {"text": "Collecting signals in at one end and passing them on "
                     "at the other.",
             "correct": True},
            {"text": "Holding the long cable straight so that it cannot "
                     "tangle.",
             "correct": False,
             "why": "Nothing holds it straight and it does not need to be. "
                    "The branches make contact with other cells."},
            {"text": "Giving the cell more places to take food in along its "
                     "length.",
             "correct": False,
             "why": "Food crosses the membrane anywhere. The branches are "
                    "there for the signal."},
            {"text": "Building the fatty sheath, which is wound on from the "
                     "ends inwards.",
             "correct": False,
             "why": "The sheath is made by other cells wrapped around the "
                    "cable, not by the branches."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e27",
        "band": "easier",
        "text": "Almost all of a root hair cell's surface is on one part of "
                "it. Which part?",
        "options": [
            {"text": "The cell wall around the main body of the cell.",
             "correct": False,
             "why": "The body is a small block. The long hair carries "
                    "nearly all of the surface."},
            {"text": "The permanent vacuole in the middle.",
             "correct": False,
             "why": "The vacuole is inside the cell, so it is not outside "
                    "surface at all."},
            {"text": "The long thin hair pushed out between the soil "
                     "particles.",
             "correct": True},
            {"text": "The membrane around the nucleus.",
             "correct": False,
             "why": "That is deep inside the cell. The surface that matters "
                    "here is the one touching soil water."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e28",
        "band": "easier",
        "text": "The walls between one phloem tube cell and the next are "
                "full of holes. What are those walls called?",
        "options": [
            {"text": "Capillaries",
             "correct": False,
             "why": "A capillary is the narrowest blood vessel in an "
                    "animal. These are sieve plates."},
            {"text": "Sieve plates",
             "correct": True},
            {"text": "Cilia",
             "correct": False,
             "why": "Cilia are tiny beating hairs on an animal cell. These "
                    "are walls with holes through them."},
            {"text": "Root hairs",
             "correct": False,
             "why": "A root hair is a long extension on a cell in the soil, "
                    "not a wall inside a stem."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e29",
        "band": "easier",
        "text": "Your nerve cells and your muscle cells look nothing alike. "
                "What does the nucleus of each one hold?",
        "options": [
            {"text": "The genes for being a nerve cell in one and for being "
                     "a muscle cell in the other.",
             "correct": False,
             "why": "Both hold the whole set. What differs is which of "
                    "those genes the cell uses."},
            {"text": "Half a set of genes each, as in a sperm cell.",
             "correct": False,
             "why": "Half a set belongs to the sex cells alone. Every "
                    "ordinary body cell holds a full set."},
            {"text": "No genes at all in the muscle cell, since it only has "
                     "to contract.",
             "correct": False,
             "why": "Every cell with a nucleus carries genes, and a muscle "
                    "cell has one."},
            {"text": "Exactly the same full set of genes in each of them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e30",
        "band": "easier",
        "text": "What happens to a muscle cell when it contracts?",
        "options": [
            {"text": "It gets shorter and pulls.",
             "correct": True},
            {"text": "It gets longer and pushes.",
             "correct": False,
             "why": "Contract means shorten, and a shortening cell cannot "
                    "push. Muscle only ever pulls."},
            {"text": "It gets wider without changing its length at all.",
             "correct": False,
             "why": "It does thicken a little, but the useful change is "
                    "that it shortens along its length."},
            {"text": "It divides into two smaller cells.",
             "correct": False,
             "why": "Contracting is movement, not division. The cell "
                    "shortens and then relaxes back again."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e31",
        "band": "easier",
        "text": "Which description fits cilia best?",
        "options": [
            {"text": "One long whip-like tail that drives the whole cell "
                     "forwards.",
             "correct": False,
             "why": "That describes a sperm cell's tail. Cilia are many, "
                    "and each one is short."},
            {"text": "A ring of stiff spines holding the cell against the "
                     "tube wall.",
             "correct": False,
             "why": "They are neither stiff nor anchors. They are flexible "
                    "hairs that beat."},
            {"text": "Many short hairs, side by side, that beat together in "
                     "waves.",
             "correct": True},
            {"text": "A folded edge that increases the surface for "
                     "absorbing.",
             "correct": False,
             "why": "A folded edge is a surface adaptation on a gut lining "
                    "cell. Cilia stick out and move."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-e32",
        "band": "easier",
        "text": "What does the mucus in your airways do before the cilia "
                "sweep it away?",
        "options": [
            {"text": "It dissolves oxygen so that it can cross into the "
                     "blood more easily.",
             "correct": False,
             "why": "Gas exchange happens further down, in the lungs. Mucus "
                    "in the airways is a trap."},
            {"text": "It traps the dust and bacteria that are breathed in "
                     "with the air.",
             "correct": True},
            {"text": "It kills every bacterium that lands in it.",
             "correct": False,
             "why": "It traps them, and they are carried up and swallowed. "
                    "Trapping is not killing."},
            {"text": "It keeps the airway open by pressing outwards on the "
                     "walls.",
             "correct": False,
             "why": "The airway is held open by rings of cartilage. Mucus "
                    "is sticky, not stiff."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-04-s10",
        "band": "standard",
        "text": "A ciliated epithelial cell holds far more mitochondria than "
                "the cells beneath it in the lining. Explain why.",
        "options": [
            {"text": "It absorbs minerals from the air against the flow, and "
                     "that has to be paid for.",
             "correct": False,
             "why": "Nothing is absorbed from air, and dragging minerals in "
                    "is the root hair cell's cost. This cell's cost is "
                    "movement."},
            {"text": "Beating hundreds of cilia hour after hour costs "
                     "energy, and mitochondria release it.",
             "correct": True},
            {"text": "It has no nucleus, so its mitochondria have to hold "
                     "the instructions instead.",
             "correct": False,
             "why": "It keeps its nucleus, and a mitochondrion holds no "
                    "instructions in any case."},
            {"text": "Mucus is made inside mitochondria, so a cell handling "
                     "a lot of it needs plenty.",
             "correct": False,
             "why": "Mucus is made by different cells in the same lining. "
                    "Mitochondria release energy and nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s11",
        "band": "standard",
        "text": "Smoke stops the cilia in the airways beating. Suggest what "
                "happens to the mucus that is already there.",
        "options": [
            {"text": "It is absorbed into the blood instead, so nothing "
                     "collects.",
             "correct": False,
             "why": "Mucus is not absorbed anywhere. With nothing moving "
                    "it, it stays where it is."},
            {"text": "It dries out at once, because it is the beating that "
                     "keeps it wet.",
             "correct": False,
             "why": "The beating moves the mucus; it does not moisten it."},
            {"text": "It is swept the other way, down into the lungs, as the "
                     "beating reverses.",
             "correct": False,
             "why": "Nothing reverses. The cilia have stopped, so the mucus "
                    "is not swept anywhere at all."},
            {"text": "It collects, with its trapped dirt, and has to be "
                     "coughed up instead.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s12",
        "band": "standard",
        "text": "An egg cell is many times larger than a sperm cell. Explain "
                "the difference in size.",
        "options": [
            {"text": "The egg carries a food store and never travels; the "
                     "sperm travels and carries none.",
             "correct": True},
            {"text": "The egg holds a full set of chromosomes while the "
                     "sperm holds only half a set.",
             "correct": False,
             "why": "Both carry half a set. What makes the egg large is the "
                    "food store, not the chromosomes."},
            {"text": "The egg has to be large enough for several sperm cells "
                     "to enter it at once.",
             "correct": False,
             "why": "Only one enters, and the membrane changes immediately "
                    "to keep the rest out."},
            {"text": "The egg is larger because it is older, having been "
                     "made long before the sperm was.",
             "correct": False,
             "why": "Age does not decide size. The egg is large because of "
                    "what the embryo will live on."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s13",
        "band": "standard",
        "text": "The moment one sperm cell enters, an egg cell's membrane "
                "changes so that no other can get in. Explain why that "
                "matters.",
        "options": [
            {"text": "It stops the egg losing the food store it has spent so "
                     "long building.",
             "correct": False,
             "why": "The store is inside and none of it is lost. What must "
                    "be kept right is the number of chromosomes."},
            {"text": "It keeps the sperm cell's tail outside, where it "
                     "cannot damage the egg.",
             "correct": False,
             "why": "The tail is left outside in any case; only the head "
                    "goes in."},
            {"text": "A second half set would leave the embryo with too many "
                     "chromosomes.",
             "correct": True},
            {"text": "It seals the enzymes from the sperm's head inside, "
                     "where they are needed.",
             "correct": False,
             "why": "Those enzymes did their work on the way in and are "
                    "finished with."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s14",
        "band": "standard",
        "text": "Palisade cells are tall boxes standing on end in a layer "
                "near the top of a leaf. Explain how the position and the "
                "shape both help.",
        "options": [
            {"text": "Standing on end keeps them out of the light, which "
                     "would otherwise damage their chloroplasts.",
             "correct": False,
             "why": "Light is what they are for, not a danger. They sit "
                    "where it arrives first."},
            {"text": "Light reaches them first, and a tall column holds a "
                     "deep stack of chloroplasts in its path.",
             "correct": True},
            {"text": "The tall shape lets water run down between them to the "
                     "cells underneath.",
             "correct": False,
             "why": "Water arrives through the xylem, not by running down "
                    "gaps between cells."},
            {"text": "Standing on end gives each cell less surface, so the "
                     "leaf loses less water.",
             "correct": False,
             "why": "A tall column has more surface, not less. The shape is "
                    "about intercepting light."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s15",
        "band": "standard",
        "text": "As a xylem cell matures, its contents die and its end walls "
                "break down. Explain how that helps the plant.",
        "options": [
            {"text": "A dead cell needs no food, so the plant saves the "
                     "sugar it would have used.",
             "correct": False,
             "why": "There is a small saving, but the end walls go so that "
                    "the water has a clear run."},
            {"text": "Dead cells cannot be attacked by anything living in "
                     "the soil.",
             "correct": False,
             "why": "Being dead is no protection. What matters is that the "
                    "tube is now open along its whole length."},
            {"text": "The dead contents set hard and hold the stem upright.",
             "correct": False,
             "why": "Support comes from the thickened wall. The inside is "
                    "left empty."},
            {"text": "What is left is an open pipe, so water is not held up "
                     "at every join.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s16",
        "band": "standard",
        "text": "A xylem tube has a thickened, strengthened wall. Give two "
                "things that the strengthening does.",
        "options": [
            {"text": "It stops the tube collapsing, and it helps hold the "
                     "plant up.",
             "correct": True},
            {"text": "It stores minerals until the leaf asks for them, and "
                     "it keeps the tube warm.",
             "correct": False,
             "why": "Nothing is stored in the wall, and warmth is not a "
                    "problem a plant solves this way."},
            {"text": "It stops water leaking sideways, and it makes the tube "
                     "wider than it would be.",
             "correct": False,
             "why": "Thickening a wall makes it stronger, not the tube "
                    "wider. The second job is support."},
            {"text": "It lets the tube squeeze to push water up, and it "
                     "protects the living contents.",
             "correct": False,
             "why": "Xylem does not pump, and there are no living contents "
                    "left in it to protect."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s17",
        "band": "standard",
        "text": "Phloem tubes stay alive, and are helped by companion cells "
                "packed with mitochondria. Explain why.",
        "options": [
            {"text": "The sugar has to be kept warm on the way, and only a "
                     "living cell does that.",
             "correct": False,
             "why": "Temperature is not what the mitochondria are for."},
            {"text": "The sugar would go bad in a dead tube, as food does "
                     "when it is left out.",
             "correct": False,
             "why": "Sugar in solution does not spoil in a pipe. The energy "
                    "is spent loading it and moving it."},
            {"text": "Loading and moving sugar costs energy, and only a "
                     "living cell can spend it.",
             "correct": True},
            {"text": "A dead tube would collapse under the weight of the "
                     "sugar it carries.",
             "correct": False,
             "why": "Xylem is dead and does not collapse. What phloem needs "
                    "living cells for is energy."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s18",
        "band": "standard",
        "text": "Sugar made in a leaf may be needed in a root below it or in "
                "a fruit above it. What does that tell you about phloem?",
        "options": [
            {"text": "It must carry sugar upwards only, since the leaf sits "
                     "above the root.",
             "correct": False,
             "why": "The fruit above the leaf is fed too, so the flow has "
                    "to work both ways."},
            {"text": "It must be able to carry its load in either direction.",
             "correct": True},
            {"text": "It must carry sugar downwards only, because everything "
                     "settles under its own weight.",
             "correct": False,
             "why": "Nothing settles. The plant moves the sugar "
                    "deliberately, and it moves it upwards as well."},
            {"text": "It must be the same tissue as xylem, with the flow "
                     "reversing at night.",
             "correct": False,
             "why": "They are separate tissues with separate cargoes, and "
                    "the xylem's flow does not reverse."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s19",
        "band": "standard",
        "text": "A cell you have never seen before has a long whip-like tail "
                "and a middle section crammed with mitochondria. Deduce its "
                "job.",
        "options": [
            {"text": "It absorbs dissolved minerals, because mitochondria "
                     "mean absorbing.",
             "correct": False,
             "why": "Mitochondria mean energy, not absorbing, and a tail "
                    "would be no use in soil."},
            {"text": "It carries oxygen, because it clearly has energy to "
                     "spare for the trip.",
             "correct": False,
             "why": "A cell built to carry oxygen throws parts out to make "
                    "room and would not spend its own cargo."},
            {"text": "It stores food, because the middle section is so full.",
             "correct": False,
             "why": "The middle is full of mitochondria, which release "
                    "energy rather than store food."},
            {"text": "It travels a long way through liquid, under its own "
                     "power.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s20",
        "band": "standard",
        "text": "A crop is bred to take up more water from dry soil. Which "
                "change to its root hair cells would help most?",
        "options": [
            {"text": "Longer hairs on more of the cells, giving far more "
                     "surface.",
             "correct": True},
            {"text": "Chloroplasts, so that the root can make its own food.",
             "correct": False,
             "why": "No light reaches a root, so chloroplasts there would "
                    "never work."},
            {"text": "A thicker cell wall, so that the cell can push harder "
                     "into the soil.",
             "correct": False,
             "why": "A thicker wall adds no surface, and it is surface that "
                    "collects the water."},
            {"text": "A larger permanent vacuole, so that more water can be "
                     "stored once it is in.",
             "correct": False,
             "why": "Storing is not the problem here; getting the water "
                    "across the surface in the first place is."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s21",
        "band": "standard",
        "text": "A muscle cell and a root hair cell do completely different "
                "jobs, yet both are well supplied with mitochondria. What do "
                "their jobs share?",
        "options": [
            {"text": "Both cells constantly make new parts to replace ones "
                     "that have worn out.",
             "correct": False,
             "why": "Every cell repairs itself. What these two share is a "
                    "job that spends energy without stopping."},
            {"text": "Both have given a part up to make room, so both have "
                     "to work harder.",
             "correct": False,
             "why": "Neither has given anything up. The red blood cell is "
                    "the one that made that trade."},
            {"text": "Both do work that never stops, and work has to be paid "
                     "for.",
             "correct": True},
            {"text": "Both have to move themselves from one place to "
                     "another.",
             "correct": False,
             "why": "A root hair cell never moves anywhere. It is what it "
                    "drags into itself that costs energy."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s22",
        "band": "standard",
        "text": "A student says the nerve cell must be the most specialised "
                "cell in the body because it is the longest. Explain what is "
                "wrong with that.",
        "options": [
            {"text": "Nerve cells are not actually the longest cells, so the "
                     "claim starts from a mistake.",
             "correct": False,
             "why": "They really are the longest by a wide margin. The "
                    "mistake is treating length as the measure."},
            {"text": "How well a cell fits its job is the measure, not how "
                     "big it is.",
             "correct": True},
            {"text": "Length is a disadvantage, so the longest cell must be "
                     "the worst adapted one.",
             "correct": False,
             "why": "Length is exactly what this cell's job needs, so it is "
                    "no disadvantage."},
            {"text": "Nothing is wrong: a cell that goes to more trouble is "
                     "more specialised.",
             "correct": False,
             "why": "Size is not trouble. A red blood cell is tiny and gave "
                    "up more than any other cell in you."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s23",
        "band": "standard",
        "text": "A skin cell and a muscle cell in the same person hold "
                "exactly the same set of genes. Explain how the two end up "
                "so different.",
        "options": [
            {"text": "The muscle cell throws away the genes it does not need "
                     "as it matures.",
             "correct": False,
             "why": "Only the red blood cell loses its nucleus, and even "
                    "then nothing edits the set."},
            {"text": "The genes rearrange themselves into a different order "
                     "in each kind of cell.",
             "correct": False,
             "why": "The order is the same in both. What differs is which "
                    "of them the cell acts on."},
            {"text": "The two sets look alike but are copies of different "
                     "chromosomes.",
             "correct": False,
             "why": "Both cells came from the same first cell and hold the "
                    "same chromosomes."},
            {"text": "Each cell uses a different part of the set and leaves "
                     "the rest switched off.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s24",
        "band": "standard",
        "text": "A sperm cell's tail and a ciliated cell's cilia both beat. "
                "Explain the difference in what the beating achieves.",
        "options": [
            {"text": "The tail moves the cell; the cilia move something past "
                     "a cell that stays put.",
             "correct": True},
            {"text": "The tail moves liquid past the sperm cell, while the "
                     "cilia move their own cell along the airway.",
             "correct": False,
             "why": "That is the two the wrong way round. The sperm swims, "
                    "and the ciliated cell is fixed in the lining."},
            {"text": "Both move their own cell, but the sperm cell is faster "
                     "at it.",
             "correct": False,
             "why": "A ciliated cell goes nowhere. It shifts the mucus "
                    "lying above it."},
            {"text": "Both move liquid past themselves, but the sperm cell "
                     "moves far more of it.",
             "correct": False,
             "why": "The sperm cell is moving itself, which is the whole "
                    "reason it has a tail."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s25",
        "band": "standard",
        "text": "Muscle cells are long, and all of them lie in the same "
                "direction within a muscle. Explain the advantage of that "
                "arrangement.",
        "options": [
            {"text": "It leaves gaps between them for blood vessels to run "
                     "through.",
             "correct": False,
             "why": "Vessels do run between them, but that is not why they "
                    "are aligned."},
            {"text": "Long cells hold more mitochondria than short ones, so "
                     "the muscle has more energy.",
             "correct": False,
             "why": "A muscle of the same size holds much the same "
                    "mitochondria however its cells are arranged."},
            {"text": "Each cell shortens along its length, so all the pulls "
                     "add up in one direction.",
             "correct": True},
            {"text": "It lets the signal pass straight down the muscle "
                     "without any handover.",
             "correct": False,
             "why": "Every cell is still signalled across a junction. The "
                    "arrangement is about the direction of the pull."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s26",
        "band": "standard",
        "text": "A palisade cell and a root hair cell are both plant cells, "
                "but only one of them is green. Explain the difference.",
        "options": [
            {"text": "The root hair cell has chloroplasts, but the soil "
                     "around it stops them working.",
             "correct": False,
             "why": "There are none there to be stopped. A cell builds "
                    "chloroplasts where there is light to use."},
            {"text": "Chloroplasts are only built where light reaches, and "
                     "no light reaches a root.",
             "correct": True},
            {"text": "Only cells in a leaf count as plant cells, so only "
                     "they have chloroplasts.",
             "correct": False,
             "why": "A root hair cell has a wall and a permanent vacuole "
                    "and is fully a plant cell."},
            {"text": "The palisade cell makes its colour from minerals that "
                     "the root has not yet sent up.",
             "correct": False,
             "why": "Minerals do help build chlorophyll, but a root cell is "
                    "colourless because it is in the dark."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s27",
        "band": "standard",
        "text": "The mucus lining your airways is made by different cells "
                "sitting among the ciliated ones. Explain why the two kinds "
                "work as a pair.",
        "options": [
            {"text": "The mucus cells supply the energy that the cilia spend "
                     "on beating.",
             "correct": False,
             "why": "Each cell releases its own energy in its own "
                    "mitochondria. What is shared is the mucus."},
            {"text": "The cilia make the mucus and the other cells sweep it "
                     "away.",
             "correct": False,
             "why": "That is the two jobs swapped over. Cilia beat; the "
                    "other cells make the mucus."},
            {"text": "The mucus holds the cilia upright so that they beat in "
                     "step.",
             "correct": False,
             "why": "Cilia beat perfectly well in a watery layer. The mucus "
                    "is there to trap dirt."},
            {"text": "One kind traps the dirt and the other kind sweeps the "
                     "trapped dirt away.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s28",
        "band": "standard",
        "text": "Nitrate absorbed by a root hair cell is needed in a leaf at "
                "the top of the plant. Which route does it take?",
        "options": [
            {"text": "Up through the xylem, dissolved in the water.",
             "correct": True},
            {"text": "Up through the phloem, alongside the sugar.",
             "correct": False,
             "why": "Phloem carries the sugar the leaf has made. Minerals "
                    "go up with the water instead."},
            {"text": "From cell to cell the whole way, being handed on at "
                     "each one.",
             "correct": False,
             "why": "That would be far too slow across a whole plant, which "
                    "is why transport tubes exist."},
            {"text": "It stays in the root, since minerals are only needed "
                     "where they go in.",
             "correct": False,
             "why": "Nitrate is needed in the leaves, to build chlorophyll "
                    "and new growth, so it has to travel."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s29",
        "band": "standard",
        "text": "A plant standing in wet soil and full sun still has yellow "
                "leaves. Which failure at the root would explain that?",
        "options": [
            {"text": "Its root hairs have been cut back, so no water is "
                     "getting in.",
             "correct": False,
             "why": "The soil is wet and the plant is not wilting, so water "
                    "is clearly arriving."},
            {"text": "Its root cells have grown chloroplasts, which are "
                     "using the minerals up.",
             "correct": False,
             "why": "No root cell builds chloroplasts, because no light "
                    "reaches one."},
            {"text": "Its root cells have no energy left to drag minerals "
                     "in, so nitrate never arrives.",
             "correct": True},
            {"text": "Its xylem has died, so nothing can travel up the stem "
                     "any more.",
             "correct": False,
             "why": "Xylem is dead in a healthy plant too, and water is "
                    "plainly still arriving here."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s30",
        "band": "standard",
        "text": "A fertilised human egg holds 46 chromosomes. Where did they "
                "come from?",
        "options": [
            {"text": "All 46 from the egg, with the sperm supplying only the "
                     "signal to start.",
             "correct": False,
             "why": "Delivering chromosomes is the sperm cell's whole job. "
                    "Each sex cell brings 23."},
            {"text": "23 from the sperm cell and 23 from the egg cell.",
             "correct": True},
            {"text": "46 from each, with half of the 92 then thrown away.",
             "correct": False,
             "why": "Nothing is thrown away. Each sex cell carried half a "
                    "set to begin with."},
            {"text": "23 from each, and then 23 more copied afterwards to "
                     "make the number up.",
             "correct": False,
             "why": "23 and 23 make 46 already, so nothing extra has to be "
                    "copied."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s31",
        "band": "standard",
        "text": "A cell near the underside of a leaf holds far fewer "
                "chloroplasts than a palisade cell does. Suggest why.",
        "options": [
            {"text": "It is a root hair cell that has grown up into the leaf "
                     "by mistake.",
             "correct": False,
             "why": "Root hair cells stay in the root. This is an ordinary "
                    "leaf cell, lower down."},
            {"text": "It is dead, as a xylem cell is, so it has no working "
                     "parts left.",
             "correct": False,
             "why": "It is alive. What differs is how much light reaches "
                    "it."},
            {"text": "Chloroplasts sink under their own weight, so they "
                     "gather at the top of every cell.",
             "correct": False,
             "why": "A cell moves its chloroplasts about; gravity does not "
                    "settle them."},
            {"text": "Much less light gets that far down, so chloroplasts "
                     "there would have little to do.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-s32",
        "band": "standard",
        "text": "Explain why a highly specialised cell is usually no good at "
                "any other job.",
        "options": [
            {"text": "It has been tuned all the way towards one job, and "
                     "that costs it something elsewhere.",
             "correct": True},
            {"text": "It has fewer parts than an ordinary cell, so there is "
                     "less that it can do.",
             "correct": False,
             "why": "Most specialised cells keep every part. Even a red "
                    "blood cell gave up only what its own job could spare."},
            {"text": "It is too small to hold what a second job would need.",
             "correct": False,
             "why": "Size is not the obstacle: a nerve cell is enormous and "
                    "still does one job only."},
            {"text": "It is worn out by the job it does, so it has nothing "
                     "left over.",
             "correct": False,
             "why": "A muscle cell does its job all day for years. Being "
                    "committed is not the same as being worn out."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-04-h10",
        "band": "harder",
        "text": "Compare xylem and phloem. Which statement is true of both "
                "of them?",
        "options": [
            {"text": "Both are made of dead cells whose end walls have "
                     "broken down.",
             "correct": False,
             "why": "Only xylem dies. Phloem tubes stay alive, helped by "
                    "companion cells beside them."},
            {"text": "Both carry their load upwards only, away from the "
                     "roots.",
             "correct": False,
             "why": "Xylem goes up. Phloem goes wherever the sugar is "
                    "needed, which may be up or down."},
            {"text": "Both are tubes built from cells joined end to end.",
             "correct": True},
            {"text": "Both spend energy from mitochondria to move what they "
                     "carry.",
             "correct": False,
             "why": "Phloem does. Xylem does not, because its cells are "
                    "dead and the water is pulled up from above."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h11",
        "band": "harder",
        "text": "A student designs a xylem tube that keeps its living "
                "contents, arguing that a living tube must beat a dead one. "
                "Evaluate the design.",
        "options": [
            {"text": "It would work worse: the contents block the pipe the "
                     "water needs.",
             "correct": True},
            {"text": "It would work better, because a living cell could pump "
                     "the water upwards.",
             "correct": False,
             "why": "Xylem does not pump at all — the water is pulled up "
                    "from the leaves. Living contents would only be in the "
                    "way."},
            {"text": "It would make no difference, because water passes "
                     "through cells either way.",
             "correct": False,
             "why": "Passing through a cell is far slower than running up "
                    "an open pipe, which is why the contents go."},
            {"text": "It would work better, because a living tube could "
                     "repair itself when damaged.",
             "correct": False,
             "why": "Repair would be a real gain, but it is bought by "
                    "blocking the pipe, and the plant has judged that "
                    "trade."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h12",
        "band": "harder",
        "text": "A plant is engineered so that its root cells build "
                "chloroplasts as densely as its palisade cells do. Predict "
                "the result.",
        "options": [
            {"text": "The root would make food, so the plant could get by "
                     "with smaller leaves.",
             "correct": False,
             "why": "Chloroplasts need light and none reaches a root. They "
                    "would sit in the dark doing nothing."},
            {"text": "The root would turn green and start to grow upwards "
                     "towards the light.",
             "correct": False,
             "why": "A root grows downwards, and building chloroplasts does "
                    "not change that."},
            {"text": "The root would absorb minerals faster, because "
                     "chloroplasts release energy.",
             "correct": False,
             "why": "Energy for absorbing comes from mitochondria. "
                    "Chloroplasts use light, and underground there is none."},
            {"text": "No food would be made, and the plant would have paid "
                     "to build them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h13",
        "band": "harder",
        "text": "The flight muscle cells of a bird that migrates for days "
                "without landing hold far more mitochondria than those of a "
                "bird that flies only in short bursts. Suggest why.",
        "options": [
            {"text": "The migrating bird's cells are larger, so they hold "
                     "more of everything.",
             "correct": False,
             "why": "The difference is specific to mitochondria, and it "
                    "matches the work each muscle actually does."},
            {"text": "Work that goes on for days has to be paid for the "
                     "whole time.",
             "correct": True},
            {"text": "Mitochondria store the food the bird will need on the "
                     "journey.",
             "correct": False,
             "why": "They release energy from food; they do not store it. "
                    "The store is fat held elsewhere."},
            {"text": "Extra mitochondria make the muscle lighter, which "
                     "matters most in a flying animal.",
             "correct": False,
             "why": "Adding parts to a cell does not make it lighter. They "
                    "are there because the work never stops."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h14",
        "band": "harder",
        "text": "A root hair is 0.90 mm long and the cell body it grows from "
                "is 0.06 mm across. How many times longer than the body is "
                "the hair?",
        "options": [
            {"text": "0.84 times, because 0.90 − 0.06 = 0.84.",
             "correct": False,
             "why": "Subtracting gives the difference in length, not how "
                    "many times longer. This is a division."},
            {"text": "1.5 times, because 0.90 ÷ 0.06 = 1.5.",
             "correct": False,
             "why": "A power of ten has been dropped: 0.06 × 15 = 0.90, so "
                    "the answer is 15."},
            {"text": "15 times, because 0.90 ÷ 0.06 = 15.",
             "correct": True},
            {"text": "0.067 times, because 0.06 ÷ 0.90 = 0.067.",
             "correct": False,
             "why": "That is the division the wrong way round, and it makes "
                    "the hair shorter than the body."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h15",
        "band": "harder",
        "text": "A red blood cell completes one circuit of the body in about "
                "1 minute and lasts about 120 days. Estimate the number of "
                "circuits it makes in its life.",
        "options": [
            {"text": "About 173 000, because 120 × 24 × 60 = 172 800.",
             "correct": True},
            {"text": "About 2 880, because 120 × 24 = 2 880.",
             "correct": False,
             "why": "That counts the hours the cell lives, and each of "
                    "those hours holds sixty circuits."},
            {"text": "About 7 200, because 24 × 60 × 5 = 7 200.",
             "correct": False,
             "why": "That is five days' worth of minutes. The cell lasts a "
                    "hundred and twenty days."},
            {"text": "About 10 400 000, because 120 × 24 × 60 × 60 = 10 368 "
                     "000.",
             "correct": False,
             "why": "That counts seconds. A circuit takes a minute, so the "
                    "last multiplication by sixty is one too many."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h16",
        "band": "harder",
        "text": "A student compares a nerve cell's fatty sheath to the "
                "plastic coating on an electrical wire. Evaluate the "
                "comparison.",
        "options": [
            {"text": "It fails completely, because the sheath slows the "
                     "signal down rather than speeding it up.",
             "correct": False,
             "why": "Stripping the sheath is what slows a signal down. The "
                    "comparison is not wrong, only incomplete."},
            {"text": "It is perfect: both are insulation, and both are put "
                     "on by the thing they cover.",
             "correct": False,
             "why": "The insulation half holds. But a nerve cell does not "
                    "make its own sheath — other cells wrap around it."},
            {"text": "It fails, because a nerve signal is chemical and "
                     "nothing runs along the cable at all.",
             "correct": False,
             "why": "Chemistry is used at the junction between cells. Along "
                    "the cable a signal really does run."},
            {"text": "Fair on insulation, but the sheath is other living "
                     "cells, laid on in segments with gaps.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h17",
        "band": "harder",
        "text": "Cilia and a sperm cell's tail are built from the same kind "
                "of machinery. Explain why calling cilia “lots of little "
                "tails” is still misleading.",
        "options": [
            {"text": "Because cilia do not move at all, whereas a tail does.",
             "correct": False,
             "why": "Cilia beat constantly. The difference is in what ends "
                    "up moving."},
            {"text": "Because a tail moves its own cell, and cilia move "
                     "fluid past a fixed one.",
             "correct": True},
            {"text": "Because cilia belong to plant cells and tails to "
                     "animal cells.",
             "correct": False,
             "why": "Both belong to animal cells here: the airway lining "
                    "and the sperm cell."},
            {"text": "Because a tail needs energy from mitochondria and "
                     "cilia beat without any.",
             "correct": False,
             "why": "Beating cilia is expensive, which is why a ciliated "
                    "cell holds so many mitochondria."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h18",
        "band": "harder",
        "text": "A chemical that blocks one particular protein is added to "
                "cells in a laboratory. Airway cilia stop beating and sperm "
                "tails stop moving, but nothing else changes. What does that "
                "tell you?",
        "options": [
            {"text": "That the chemical must have been added to two "
                     "different samples by mistake.",
             "correct": False,
             "why": "One chemical, one target, and two kinds of cell stop. "
                    "That points at something the two of them share."},
            {"text": "That cilia and tails both depend on the mucus around "
                     "them in order to move.",
             "correct": False,
             "why": "The chemical blocks a protein inside the cell, and a "
                    "sperm cell swims with no mucus anywhere near it."},
            {"text": "That cilia and a sperm cell's tail are built from the "
                     "same machinery.",
             "correct": True},
            {"text": "That the sperm cells in the sample are covered in "
                     "cilia rather than having a tail.",
             "correct": False,
             "why": "A sperm cell has one tail. A tail and cilia are built "
                    "alike, which is why one block stops both."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h19",
        "band": "harder",
        "text": "A leaf is engineered so that every cell from top to bottom "
                "is a densely packed palisade cell. Suggest one problem that "
                "would cause.",
        "options": [
            {"text": "The lower ones sit in the shade of those above and "
                     "cost more than they return.",
             "correct": True},
            {"text": "The leaf would make no food at all, because the "
                     "palisade layer would be too thick.",
             "correct": False,
             "why": "The upper cells would still work well. It is the "
                    "shaded ones lower down that are wasted."},
            {"text": "The leaf would turn yellow, because there would not be "
                     "enough chlorophyll to go round.",
             "correct": False,
             "why": "There would be far more chlorophyll, not less. The "
                    "trouble is that most of it sits in the dark."},
            {"text": "The leaf could take in no water, because palisade "
                     "cells cannot absorb it.",
             "correct": False,
             "why": "No leaf cell absorbs water from outside; it arrives "
                    "through the xylem in either design."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h20",
        "band": "harder",
        "text": "An egg cell and a sperm cell each carry half a set of "
                "chromosomes, but almost everything else about them differs. "
                "Which pair of trades explains that?",
        "options": [
            {"text": "The sperm gave up its nucleus for speed; the egg gave "
                     "up its mitochondria for room.",
             "correct": False,
             "why": "Neither gave up a nucleus — delivering one is the "
                    "point — and the egg is not short of mitochondria."},
            {"text": "The egg gave up its food store to stay small; the "
                     "sperm gave up its tail to save energy.",
             "correct": False,
             "why": "That is both cells described as the opposite of what "
                    "they are."},
            {"text": "Both gave up the same things, and the difference in "
                     "size is just how they are made.",
             "correct": False,
             "why": "The differences are answers to different problems: one "
                    "has to travel, the other has to provide."},
            {"text": "The sperm spent everything on travelling; the egg "
                     "spent everything on providing.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h21",
        "band": "harder",
        "text": "Root hair cells last only a few days, and new ones form "
                "further back as the root tip pushes on. Explain the "
                "advantage of replacing them.",
        "options": [
            {"text": "Old hairs would grow too long to fit between soil "
                     "particles as the root thickened.",
             "correct": False,
             "why": "Length is what makes a hair work. The advantage is "
                    "about where the new ones are."},
            {"text": "The new ones are in soil whose water and minerals are "
                     "not yet used up.",
             "correct": True},
            {"text": "Building new cells costs the plant less than keeping "
                     "old ones alive.",
             "correct": False,
             "why": "Building a cell is expensive. What is gained is "
                    "reaching soil that has not been drained."},
            {"text": "Old hairs turn green once they have been in the ground "
                     "long enough.",
             "correct": False,
             "why": "Nothing underground turns green, however long it is "
                    "there. There is no light."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h22",
        "band": "harder",
        "text": "A student argues that a red blood cell has no nucleus, so "
                "it must be dead, exactly like a xylem cell. Evaluate that "
                "argument.",
        "options": [
            {"text": "Right on both counts, which is why red blood cells "
                     "last only about 120 days.",
             "correct": False,
             "why": "A xylem cell really is dead; a red blood cell is not. "
                    "It has a membrane, cytoplasm, and a job it is doing "
                    "right now."},
            {"text": "Wrong about the xylem cell, which is alive and simply "
                     "has no nucleus.",
             "correct": False,
             "why": "A mature xylem cell genuinely is dead and hollow. The "
                    "mistake is about the red blood cell."},
            {"text": "Wrong: it is alive and working, but it can no longer "
                     "repair itself or divide.",
             "correct": True},
            {"text": "Wrong: a red blood cell keeps a small nucleus, too "
                     "faint to be seen.",
             "correct": False,
             "why": "There is none left at all. It is pushed out and "
                    "destroyed in the marrow."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h23",
        "band": "harder",
        "text": "A cell lining your stomach sits in acid strong enough to "
                "digest meat. Which combination of features would you "
                "predict for it?",
        "options": [
            {"text": "A thick layer of mucus over it, and quick replacement "
                     "when it is damaged.",
             "correct": True},
            {"text": "No nucleus, so that the acid has less inside the cell "
                     "to damage.",
             "correct": False,
             "why": "Losing the nucleus would leave the cell unable to "
                    "repair itself, which is the last thing this one can "
                    "afford."},
            {"text": "A great many chloroplasts, to build the mucus that "
                     "protects it.",
             "correct": False,
             "why": "Chloroplasts belong to plant cells in the light, and "
                    "what they make is sugar."},
            {"text": "A long thin hair, to spread the acid over a wider "
                     "surface.",
             "correct": False,
             "why": "More surface facing acid is a disadvantage. This cell "
                    "needs protection, not exposure."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h24",
        "band": "harder",
        "text": "Water is pulled to the top of a tree 30 m tall through "
                "xylem tubes narrower than a hair. Explain why those tubes "
                "must be strengthened.",
        "options": [
            {"text": "Because the weight of the water pushes the walls "
                     "outwards and would burst them.",
             "correct": False,
             "why": "The water in xylem is under a pull, not a push. The "
                    "danger is the tube being squeezed shut."},
            {"text": "Because the tube has to be stiff enough to pump, and "
                     "pumping needs a strong wall.",
             "correct": False,
             "why": "Xylem does not pump. Strength is what stops it "
                    "collapsing while the water is pulled through."},
            {"text": "Because the dissolved minerals would wear a thin wall "
                     "away over time.",
             "correct": False,
             "why": "Dissolved minerals do the wall no damage as they pass."},
            {"text": "Because water under that much pull would collapse an "
                     "unsupported tube.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h25",
        "band": "harder",
        "text": "A white blood cell has to reach an infection anywhere in "
                "the body, squeeze out of a blood vessel and swallow "
                "bacteria whole. Which set of features fits that job?",
        "options": [
            {"text": "Biconcave, no nucleus, and packed with haemoglobin.",
             "correct": False,
             "why": "That is a red blood cell, built to carry and deliver. "
                    "A cell that hunts bacteria needs its instructions."},
            {"text": "A flexible shape, a full nucleus and plenty of "
                     "mitochondria.",
             "correct": True},
            {"text": "A long fixed shape with a fatty sheath wrapped along "
                     "it.",
             "correct": False,
             "why": "That is a nerve cell, built to stay where it is and "
                    "carry a signal quickly."},
            {"text": "A thick cell wall, a permanent vacuole and no "
                     "chloroplasts.",
             "correct": False,
             "why": "Those are plant cell parts, and a wall would stop it "
                    "changing shape at all."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h26",
        "band": "harder",
        "text": "One plant of a species is grown in bright sun and another "
                "of the same species in deep shade. Predict a difference "
                "between their leaves.",
        "options": [
            {"text": "The shaded plant's leaves would hold no chloroplasts, "
                     "since there is too little light to use.",
             "correct": False,
             "why": "Little light is a reason to gather more of it, not to "
                    "give up. Chloroplasts are still built."},
            {"text": "The shaded plant's palisade cells would lie flat "
                     "instead of standing on end.",
             "correct": False,
             "why": "The column shape is how a cell holds a deep stack of "
                    "chloroplasts in the light's path, in either plant."},
            {"text": "The shaded plant's leaves would be broader, to catch "
                     "what light there is.",
             "correct": True},
            {"text": "The sunlit plant's leaves would be broader, because "
                     "more light makes everything grow larger.",
             "correct": False,
             "why": "A plant in bright sun has light to spare, and broad "
                    "leaves would also lose more water."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h27",
        "band": "harder",
        "text": "Mitochondria counted per cell: heart muscle about 5 000, "
                "skin about 200, red blood cell 0. Explain the pattern.",
        "options": [
            {"text": "The count follows how much constant work each cell "
                     "does, and one of them does none.",
             "correct": True},
            {"text": "The count follows the size of the cell, and a red "
                     "blood cell is the smallest.",
             "correct": False,
             "why": "Size is not what the count follows. A red blood cell "
                    "has none because it must not burn the oxygen it is "
                    "carrying."},
            {"text": "The count follows how much oxygen a cell handles, so "
                     "the red blood cell should be highest.",
             "correct": False,
             "why": "The red blood cell handles the most oxygen of any cell "
                    "and has none at all, which is the opposite."},
            {"text": "The count follows how long each cell lives, and skin "
                     "cells are replaced fastest.",
             "correct": False,
             "why": "Lifespan does not set it. Heart muscle contracts "
                    "without stopping, and that is what has to be paid for."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h28",
        "band": "harder",
        "text": "A poison stops every mitochondrion working. Which cell "
                "would carry on doing its own job for longest, and why?",
        "options": [
            {"text": "The muscle cell, because it can store energy in "
                     "advance.",
             "correct": False,
             "why": "A muscle cell is among the worst affected: contracting "
                    "is expensive and it never stops for long."},
            {"text": "The sperm cell, because it has more mitochondria to "
                     "lose than any other.",
             "correct": False,
             "why": "Having more to lose is not protection. Its tail stalls "
                    "as soon as the supply fails."},
            {"text": "The root hair cell, because water arrives without any "
                     "energy being spent.",
             "correct": False,
             "why": "Water would keep entering, but this cell's job "
                    "includes dragging minerals in, and that stops."},
            {"text": "The red blood cell, because it has none to lose in the "
                     "first place.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h29",
        "band": "harder",
        "text": "Is a xylem vessel one cell, many cells, or neither? Choose "
                "the best answer.",
        "options": [
            {"text": "One cell, drawn out from the root to the leaf as a "
                     "nerve cell is.",
             "correct": False,
             "why": "Nothing is stretched that far. A vessel is built from "
                    "many cells stacked in a line."},
            {"text": "The remains of many cells, stacked and opened into one "
                     "pipe.",
             "correct": True},
            {"text": "Many cells, each one alive and passing the water on to "
                     "the next.",
             "correct": False,
             "why": "The contents die as the vessel matures, and that is "
                    "what leaves the pipe clear."},
            {"text": "Neither — it is a gap left between the cells as the "
                     "stem grew.",
             "correct": False,
             "why": "The pipe runs through where the cells were, using "
                    "their own walls as its sides."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h30",
        "band": "harder",
        "text": "Suppose a distance of 1.0 m had to be covered by cells 5 mm "
                "long, joined in a line. How many cells would that take, and "
                "how many junctions between them?",
        "options": [
            {"text": "200 cells and 200 junctions.",
             "correct": False,
             "why": "A line of 200 cells has a junction between each "
                    "neighbouring pair, which is 199."},
            {"text": "20 cells and 19 junctions.",
             "correct": False,
             "why": "1.0 m is 1 000 mm, and 1 000 ÷ 5 = 200. Twenty would "
                    "be the answer for 100 mm."},
            {"text": "200 cells and 199 junctions.",
             "correct": True},
            {"text": "5 cells and 4 junctions.",
             "correct": False,
             "why": "5 mm is the length of one cell, not the number of "
                    "them. There are 1 000 mm in a metre."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h31",
        "band": "harder",
        "text": "Suggest why a plant does not simply grow a hair on every "
                "one of its root cells.",
        "options": [
            {"text": "Only the outermost cells touch soil, and a hair costs "
                     "energy to build.",
             "correct": True},
            {"text": "So many hairs would take in more water than the plant "
                     "could ever use.",
             "correct": False,
             "why": "A plant seldom has water to spare, and it can control "
                    "what it takes. The limit is where the soil actually "
                    "touches it."},
            {"text": "The hairs would tangle together and stop the root "
                     "growing downwards.",
             "correct": False,
             "why": "Hairs push between soil particles and do not tangle. "
                    "Most root cells are simply not at the surface."},
            {"text": "A cell with a hair cannot divide, so the root could "
                     "never grow any longer.",
             "correct": False,
             "why": "Root hair cells are made and replaced constantly as "
                    "the root grows on."},
        ],
        "figure": None,
    },
    {
        "id": "b1-04-h32",
        "band": "harder",
        "text": "A single-celled pond organism has to feed, move, sense its "
                "surroundings and reproduce, all with one cell. Compare it "
                "with a specialised cell of yours.",
        "options": [
            {"text": "It is more specialised, because it has to be good at "
                     "more things at once.",
             "correct": False,
             "why": "Specialised means tuned towards one job. Having to do "
                    "everything is the opposite of that."},
            {"text": "It is the same, because both are built from the same "
                     "seven parts.",
             "correct": False,
             "why": "The parts list is shared, but the tuning is not: one "
                    "is committed to a single job and the other cannot be."},
            {"text": "It is less specialised, because it is smaller than the "
                     "cells in your body.",
             "correct": False,
             "why": "Size is not the measure, and many pond organisms are "
                    "larger than your cells are."},
            {"text": "It cannot be tuned all the way towards any one job, "
                     "because it has to do them all.",
             "correct": True},
        ],
        "figure": None,
    },
]
