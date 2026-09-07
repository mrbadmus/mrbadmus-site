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
]
