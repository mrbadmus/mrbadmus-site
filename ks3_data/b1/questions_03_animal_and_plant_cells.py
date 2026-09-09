"""B1 lesson 03 — Animal and plant cells: twelve questions (MRB-269).

The lesson's argument is that one parts list runs both ways: everything in an
animal cell is on the plant's list too, and the plant has three extras. These
twelve probe that argument from the sides the ladder does not — what each part
is made of and does, what goes wrong when the wrong one is blamed, and the
difference between a part that is absent and a part that is merely too small
to see.

The distractors are built from the lesson's two declared misconceptions.
CELL-04 (the wall and the membrane are the same thing, or the wall replaced
it) drives the wrong options in e01, e03, s04 and h03 — every one of them
gives the wall a job that belongs to the membrane, or quietly deletes the
membrane from a plant cell. CELL-03 (every plant cell is green) drives s03 and
h01, where a cell grown in the dark is read as "not a plant" or as having lost
something it never built. A third family, not in the register but everywhere in
the lesson, treats "I cannot see it" as "it is not there": s01, h01 and h04 all
carry a distractor that does exactly that.
"""

UNIT = "B1"
LESSON = "animal-and-plant-cells"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-03-e01",
        "band": "easier",
        "text": "Cellulose is the material that one of the seven parts is "
                "built from. Which part?",
        "options": [
            {"text": "The cell membrane", "correct": False,
             "why": "The wall and the membrane get swapped for each other "
                    "more than any other pair. The membrane is a thin skin a "
                    "few molecules thick, sitting just inside the wall — it "
                    "is not made of cellulose."},
            {"text": "The cell wall", "correct": True},
            {"text": "The vacuole", "correct": False,
             "why": "The vacuole is a bag of watery cell sap, not a solid "
                    "material. Cellulose is what the stiff layer outside the "
                    "membrane is built from."},
            {"text": "The cytoplasm", "correct": False,
             "why": "The cytoplasm is the jelly that fills the cell. "
                    "Cellulose is stiff — it is what makes celery stringy "
                    "and paper possible — and it belongs to the wall."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e02",
        "band": "easier",
        "text": "Which part releases energy from food, by respiration?",
        "options": [
            {"text": "The mitochondria", "correct": True},
            {"text": "The nucleus", "correct": False,
             "why": "The nucleus holds the DNA — the instructions for running "
                    "and building the cell. Holding instructions is not the "
                    "same as releasing energy."},
            {"text": "The chloroplasts", "correct": False,
             "why": "Chloroplasts trap light so the cell can make food. "
                    "Getting the energy back out of that food afterwards is "
                    "the mitochondria's job — and your cells have no "
                    "chloroplasts at all."},
            {"text": "The cytoplasm", "correct": False,
             "why": "Most of the cell's reactions do happen in the cytoplasm, "
                    "and it is what holds the mitochondria in place — but the "
                    "part that releases energy from food is the mitochondria "
                    "themselves."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e03",
        "band": "easier",
        "text": "Which three parts does a plant cell have that an animal cell "
                "does not?",
        "options": [
            {"text": "Cell wall, cell membrane and chloroplasts",
             "correct": False,
             "why": "Every cell on this list has a membrane, plant and animal "
                    "alike. The wall is an extra layer on the outside; it "
                    "never replaced the membrane."},
            {"text": "Cell wall, vacuole and mitochondria", "correct": False,
             "why": "Mitochondria are in both. Your muscle cells are crammed "
                    "with them — they belong to the shared four, not the "
                    "plant's three extras."},
            {"text": "Cell wall, vacuole and nucleus", "correct": False,
             "why": "Both cells have a nucleus. In a plant cell it is pushed "
                    "out to one side by the vacuole, which can make it look "
                    "as though it is not there."},
            {"text": "Cell wall, vacuole and chloroplasts", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e04",
        "band": "easier",
        "text": "In the drawing of a leaf cell the nucleus sits over at one "
                "side, not in the middle. What has pushed it there?",
        "options": [
            {"text": "The cell wall, pressing inwards on everything inside",
             "correct": False,
             "why": "The wall holds the cell's shape from the outside and "
                    "presses nothing inwards. It is the large vacuole in the "
                    "middle that shifts the nucleus aside."},
            {"text": "The chloroplasts, crowding the centre to reach the "
                     "light", "correct": False,
             "why": "Chloroplasts are scattered round the cell and are far "
                    "too small to move a nucleus. The vacuole in the middle "
                    "is what does it."},
            {"text": "The large vacuole, which has taken up most of the "
                     "middle", "correct": True},
            {"text": "The cytoplasm, which is squeezed into the centre",
             "correct": False,
             "why": "It is the other way round. The vacuole takes the middle "
                    "and squeezes the cytoplasm into a thin rim around the "
                    "outside of it."},
        ],
        "figure": "b1-cell-bench",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-03-s01",
        "band": "standard",
        "text": "An unstained cheek cell at ×400 shows you almost nothing. "
                "What does adding methylene blue actually change?",
        "options": [
            {"text": "The nucleus is stained, and becomes the darkest thing "
                     "in the field", "correct": True},
            {"text": "The mitochondria are stained, so now you can count "
                     "them", "correct": False,
             "why": "A stain changes colour, not size. A mitochondrion is "
                    "around a hundred times smaller across than the cell, "
                    "which is below what a school microscope can separate — "
                    "stained or not."},
            {"text": "The membrane is stained, so the edge of the cell shows "
                     "as a dark line", "correct": False,
             "why": "There is a line at the edge of a cheek cell, but it is "
                    "not the membrane — it is just where the cell stops. The "
                    "membrane is a few molecules thick and far too thin to "
                    "resolve."},
            {"text": "The cell wall is stained, which is what makes the "
                     "outline show up", "correct": False,
             "why": "A cheek cell is an animal cell and has no wall at all. A "
                    "stain cannot show you something that is not there."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s02",
        "band": "standard",
        "text": "A pot plant goes a week without water and its leaves flop. "
                "Which part of its cells explains that?",
        "options": [
            {"text": "The walls, which have gone soft now there is no water "
                     "in them", "correct": False,
             "why": "Cellulose walls do not soften. Each wall is exactly as "
                    "stiff as it was — what has dropped is the pressure of "
                    "the vacuole pushing out against it."},
            {"text": "The chloroplasts, which stopped trapping light and let "
                     "the cell fall in", "correct": False,
             "why": "Chloroplasts are about food, not firmness. A wilting "
                    "plant on a sunny windowsill still has every one of its "
                    "chloroplasts."},
            {"text": "The vacuoles, which have lost water and stopped "
                     "pressing on the walls", "correct": True},
            {"text": "The membranes, which have burst and let all the water "
                     "run out", "correct": False,
             "why": "Bursting is what happens when too much water moves in "
                    "and nothing pushes back. Losing water makes a cell go "
                    "limp, not burst."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s03",
        "band": "standard",
        "text": "A student builds a root hair cell and installs chloroplasts "
                "in it. The cell lives. So what is wrong with the build?",
        "options": [
            {"text": "Nothing is wrong — every plant cell needs chloroplasts "
                     "to stay alive", "correct": False,
             "why": "Most of a plant's cells have none. Chloroplasts are only "
                    "built where light reaches, and a root hair cell is "
                    "completely a plant cell without them."},
            {"text": "Nothing will ever switch those chloroplasts on — no "
                     "light reaches a root", "correct": True},
            {"text": "The chloroplasts poison the cell, because a root cannot "
                     "photosynthesise", "correct": False,
             "why": "They do no damage at all — the cell lives. What is wrong "
                    "is waste: machinery installed that will never be "
                    "switched on."},
            {"text": "The vacuole should have been left out too, as only leaf "
                     "cells have one", "correct": False,
             "why": "A root hair cell does have a large vacuole. It has six "
                    "of the seven parts — chloroplasts are the only one it "
                    "goes without."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s04",
        "band": "standard",
        "text": "A cheek cell and a leaf cell are both dropped into pure "
                "water. Only one of them bursts. Which, and why?",
        "options": [
            {"text": "The leaf cell — its wall traps the water inside until "
                     "the pressure splits it", "correct": False,
             "why": "The wall is what saves it. Water passes straight through "
                    "the wall, and the wall then pushes back hard enough to "
                    "stop the cell splitting."},
            {"text": "The cheek cell — its membrane is thinner than the "
                     "membrane of a plant cell", "correct": False,
             "why": "The membrane is the same in both. The difference is the "
                    "stiff wall on the outside of the plant cell, not a "
                    "weaker skin on the animal one."},
            {"text": "Neither — the membrane holds all of the water out of "
                     "both of the cells", "correct": False,
             "why": "Water crosses the membrane easily. The membrane chooses "
                    "what gets in; it does not seal the cell shut."},
            {"text": "The cheek cell — it has no wall to push back as water "
                     "moves in", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-03-h01",
        "band": "harder",
        "text": "Onion skin from a bulb grown underground goes under the "
                "microscope. You see a honeycomb of walls, a nucleus in each "
                "cell and a large pale region in the middle — and no green "
                "anywhere. Which conclusion is safe?",
        "options": [
            {"text": "These are not plant cells, because a plant cell would "
                     "be green", "correct": False,
             "why": "Chloroplasts are only built where light reaches, and no "
                    "light reaches a bulb under the soil. A plant cell "
                    "without them is still completely a plant cell."},
            {"text": "These are plant cells that lost their chloroplasts "
                     "while in the dark", "correct": False,
             "why": "They never built any. A cell in the dark does not lose "
                    "chloroplasts — it is never called on to make them in the "
                    "first place."},
            {"text": "These are plant cells, and a bulb grows where no light "
                     "ever reaches", "correct": True},
            {"text": "The pale region in the middle is where each cell has "
                     "emptied and died", "correct": False,
             "why": "That pale region is the vacuole — a bag of sap pressing "
                    "out against the wall, and a sign the cell is doing "
                    "exactly what it should."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h02",
        "band": "harder",
        "text": "A muscle cell and a cheek cell have exactly the same four "
                "parts. So what makes a muscle cell different?",
        "options": [
            {"text": "It holds far more mitochondria, because it never stops "
                     "needing energy", "correct": True},
            {"text": "It has a cell wall, so it can hold its shape while it "
                     "contracts", "correct": False,
             "why": "A wall would stop it contracting, and changing shape is "
                    "its entire job. No animal cell has one."},
            {"text": "It has a vacuole, to store the water it uses while it "
                     "is working", "correct": False,
             "why": "A big sap-filled bag would be dead weight in something "
                    "that has to move. Animal cells have small temporary "
                    "vacuoles at most."},
            {"text": "It is packed with chloroplasts, so it can feed itself "
                     "while it works", "correct": False,
             "why": "Nothing in your body traps light to make food, and there "
                    "is no light inside your leg for it to trap."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h03",
        "band": "harder",
        "text": "A dissolved mineral is sprayed onto a leaf. It passes "
                "straight through the cell wall but never gets inside the "
                "cell. What stopped it, and why?",
        "options": [
            {"text": "The wall — it is the cell's barrier against anything "
                     "harmful", "correct": False,
             "why": "The wall chooses nothing. Water and dissolved substances "
                    "pass straight through it, which is exactly what this one "
                    "has just done."},
            {"text": "The vacuole — it holds back anything the cell has no "
                     "use for", "correct": False,
             "why": "The vacuole sits inside the cell. The mineral never got "
                    "in, so it never reached one."},
            {"text": "The chloroplasts — they only take in what "
                     "photosynthesis needs", "correct": False,
             "why": "Chloroplasts trap light to make food once they are "
                    "inside the cell. They are not a gate on the way in."},
            {"text": "The membrane — every choice about what enters is made "
                     "there", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h04",
        "band": "harder",
        "text": "At ×400 a student can see 2 of the 4 parts in a stained "
                "cheek cell, and 5 of the 7 in a leaf cell. She says more of "
                "the leaf cell is hidden from her. Is she right?",
        "options": [
            {"text": "Yes — a leaf cell has seven parts, so more of them must "
                     "be out of sight", "correct": False,
             "why": "It has more parts in total, but count what is missing "
                    "rather than what is there: 4 − 2 and 7 − 5 both leave "
                    "two."},
            {"text": "No — the same two are hidden in each: the membrane and "
                     "the mitochondria", "correct": True},
            {"text": "Yes — the wall makes a leaf cell harder to see into "
                     "than a cheek cell", "correct": False,
             "why": "The wall is the clearest thing on the slide — it is what "
                    "draws the honeycomb you can actually see. It hides "
                    "nothing."},
            {"text": "No — nothing is hidden in either; a part you cannot see "
                     "is not there", "correct": False,
             "why": "Both cells have a membrane and mitochondria the whole "
                    "time. A school microscope simply cannot separate "
                    "anything that small."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-03-e05",
        "band": "easier",
        "text": "Which part of a cell holds the instructions for everything "
                "the cell does?",
        "options": [
            {"text": "The cytoplasm", "correct": False,
             "why": "The cytoplasm is the jelly where most of the cell's "
                    "reactions happen. The instructions are kept in the "
                    "nucleus."},
            {"text": "The cell membrane", "correct": False,
             "why": "The membrane controls what gets in and out. It holds no "
                    "instructions — the nucleus does."},
            {"text": "The nucleus", "correct": True},
            {"text": "The mitochondria", "correct": False,
             "why": "Mitochondria release energy from food. They follow the "
                    "cell's instructions; they do not hold them."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e06",
        "band": "easier",
        "text": "In which part of a plant cell is light used to make food?",
        "options": [
            {"text": "The chloroplasts", "correct": True},
            {"text": "The vacuole", "correct": False,
             "why": "The vacuole is a space full of cell sap, and it presses "
                    "outwards to keep the cell firm. Nothing is made in it."},
            {"text": "The cell wall", "correct": False,
             "why": "The wall is a stiff layer of cellulose that gives the "
                    "cell its shape. It makes nothing."},
            {"text": "The mitochondria", "correct": False,
             "why": "Mitochondria release energy from food that already "
                    "exists. Chloroplasts are where the food is made in the "
                    "first place."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e07",
        "band": "easier",
        "text": "Which part is in every cell, plant or animal, and decides "
                "what gets in and out?",
        "options": [
            {"text": "The cell wall", "correct": False,
             "why": "Only a plant cell has a wall, and it decides nothing — "
                    "water and dissolved substances pass straight through "
                    "it."},
            {"text": "The vacuole", "correct": False,
             "why": "A large vacuole belongs to a plant cell, and it stores "
                    "cell sap rather than controlling entry. Every cell has a "
                    "membrane."},
            {"text": "The cytoplasm", "correct": False,
             "why": "Every cell does have cytoplasm, but it is the jelly the "
                    "reactions happen in. The choosing is done at the "
                    "membrane."},
            {"text": "The cell membrane", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e08",
        "band": "easier",
        "text": "A plant cell's large vacuole is not empty. What is inside "
                "it?",
        "options": [
            {"text": "Air, which is what makes a stem light enough to stand "
                     "up.", "correct": False,
             "why": "There is no air in it. It is full of cell sap, and the "
                    "water in that sap presses outwards to keep the cell "
                    "firm."},
            {"text": "Cell sap — water with sugars and salts dissolved in "
                     "it.", "correct": True},
            {"text": "Chlorophyll, which is what makes the plant green.",
             "correct": False,
             "why": "The green is chlorophyll and it sits inside the "
                    "chloroplasts, out in the cytoplasm. The vacuole holds "
                    "cell sap."},
            {"text": "Spare cytoplasm, kept until the cell needs to grow.",
             "correct": False,
             "why": "Cytoplasm fills the rest of the cell around the vacuole. "
                    "What the vacuole holds is a watery sap with sugars and "
                    "salts in it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e09",
        "band": "easier",
        "text": "What is cytoplasm?",
        "options": [
            {"text": "The stiff outer layer that gives a plant cell its "
                     "shape.", "correct": False,
             "why": "That is the cell wall, and only a plant cell has one. "
                    "Cytoplasm is the jelly inside the cell."},
            {"text": "A thin skin that controls what enters and leaves the "
                     "cell.", "correct": False,
             "why": "That is the cell membrane. Cytoplasm is what fills the "
                    "space inside it."},
            {"text": "The jelly that fills the cell, where most of its "
                     "reactions happen.", "correct": True},
            {"text": "A store of water the cell draws on when it dries out.",
             "correct": False,
             "why": "That is closer to the vacuole, which holds cell sap. "
                    "Cytoplasm is the jelly the cell's chemistry happens "
                    "in."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-03-s05",
        "band": "standard",
        "text": "A student draws a plant cell with the cell membrane on the "
                "outside and the wall just inside it. What is wrong with the "
                "drawing?",
        "options": [
            {"text": "They are the wrong way round: wall outside, membrane "
                     "pressed just inside it.", "correct": True},
            {"text": "Nothing — a plant cell can have them either way "
                     "round.", "correct": False,
             "why": "The order is fixed. The wall is built outside the "
                    "membrane, and the membrane lies against it on the "
                    "inside."},
            {"text": "There should be no membrane at all, because in a plant "
                     "the wall does that job.", "correct": False,
             "why": "A plant cell has both. The wall is the box and the "
                    "membrane is the door, and only the membrane chooses what "
                    "comes in."},
            {"text": "The wall should be inside the cytoplasm, wrapped around "
                     "the vacuole.", "correct": False,
             "why": "The wall is the outermost layer of the cell, not "
                    "something buried in it. The vacuole sits in the middle, "
                    "surrounded by cytoplasm."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s06",
        "band": "standard",
        "text": "A student says an animal cell does have a cell wall — it is "
                "just called a membrane instead. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — the two words simply name the same "
                     "outer layer in two different kinds of cell.",
             "correct": False,
             "why": "They are two different structures. A plant cell has both "
                    "at once, which could not happen if they were the same "
                    "thing."},
            {"text": "Animal cells have neither, and are held together by "
                     "their cytoplasm alone.", "correct": False,
             "why": "Every cell here has a membrane, animal cells included. "
                    "What an animal cell does not have is a wall."},
            {"text": "It is the other way round: a plant cell has a wall "
                     "instead of a membrane.", "correct": False,
             "why": "A plant cell has both — wall outside, membrane just "
                    "inside it. The membrane is never replaced."},
            {"text": "They are different things: every cell has a membrane, "
                     "and only a plant cell adds a wall outside it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s07",
        "band": "standard",
        "text": "Onion cells under the microscope look like a honeycomb of "
                "neat boxes. Cheek cells look like rounded blobs with no "
                "fixed shape. Which part explains that?",
        "options": [
            {"text": "The vacuole, which is large enough in a plant cell to "
                     "square the cell off.", "correct": False,
             "why": "The vacuole pushes outwards, but what it pushes against "
                    "is the wall. Take the wall away and the cell would round "
                    "off anyway."},
            {"text": "The cell wall, which is stiff and holds a plant cell in "
                     "a fixed shape.", "correct": True},
            {"text": "The cytoplasm, which is thicker in a plant cell than in "
                     "an animal cell.", "correct": False,
             "why": "The cytoplasm is a jelly in both. What holds a plant "
                    "cell square is the stiff wall of cellulose around it."},
            {"text": "The chloroplasts, packed in tightly enough to square "
                     "the cell up.", "correct": False,
             "why": "Onion skin from a bulb has no chloroplasts at all, and "
                    "its cells are still neat boxes. The wall is what sets "
                    "the shape."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s08",
        "band": "standard",
        "text": "A student says a plant cell does not need mitochondria, "
                "because its chloroplasts make its food for it. What is wrong "
                "with that?",
        "options": [
            {"text": "Nothing — a plant cell really does have chloroplasts "
                     "instead of mitochondria.", "correct": False,
             "why": "A plant cell has both. Making food and releasing energy "
                    "from it are two different jobs, done in two different "
                    "parts."},
            {"text": "Chloroplasts can do the mitochondria's job as well, so "
                     "a cell would manage perfectly well either way.",
             "correct": False,
             "why": "A chloroplast makes food using light. Nothing in it "
                    "releases the energy from that food again — that happens "
                    "in the mitochondria."},
            {"text": "Making food is not the same as releasing energy from "
                     "it, and only mitochondria do the second job.",
             "correct": True},
            {"text": "A plant cell has no mitochondria anyway, so the student "
                     "is right by accident.", "correct": False,
             "why": "It has them, in every plant cell there is. A root hair "
                    "cell keeps an unusually large number of them."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s09",
        "band": "standard",
        "text": "Paper and cotton thread are both made almost entirely of "
                "cellulose. What does that tell you about where they came "
                "from?",
        "options": [
            {"text": "They came from animals, because cellulose is what holds "
                     "animal cells together.", "correct": False,
             "why": "No animal cell has a wall, and cellulose is what a plant "
                    "cell wall is built from. Both of these came from "
                    "plants."},
            {"text": "Nothing at all, because cellulose can be built in a "
                     "factory from any material.", "correct": False,
             "why": "Cellulose is a plant material, and it is what plant cell "
                    "walls are made of. Finding it tells you a plant was "
                    "involved."},
            {"text": "They came from plant cell membranes, which are made of "
                     "cellulose.", "correct": False,
             "why": "The membrane is not the cellulose layer, in a plant or "
                    "anywhere else. Cellulose is what the cell wall is built "
                    "from."},
            {"text": "They came from plants, because cellulose is what plant "
                     "cell walls are made of.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-03-h05",
        "band": "harder",
        "text": "A stick of celery is stiff enough to snap. A student says "
                "the cell walls make it stiff. What is missing from that "
                "answer?",
        "options": [
            {"text": "Nothing is missing — a wall is stiff, so a stalk full "
                     "of walls is stiff.", "correct": False,
             "why": "A box is only as firm as what is inside it. Leave the "
                    "celery out of water and every wall is still there, and "
                    "the stalk flops."},
            {"text": "The vacuoles, full of sap pressing outwards against the "
                     "walls — that is what holds the stalk up.",
             "correct": True},
            {"text": "The chloroplasts, which stiffen the cell from inside "
                     "once light reaches them.", "correct": False,
             "why": "Chloroplasts trap light to make food and have nothing to "
                    "do with stiffness. What presses on the walls is the "
                    "water in the vacuoles."},
            {"text": "The membranes, which push the walls outwards from just "
                     "inside them and keep the cell stretched.",
             "correct": False,
             "why": "The membrane is a thin skin that chooses what enters; it "
                    "pushes on nothing. The outward push comes from sap "
                    "filling the vacuole."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h06",
        "band": "harder",
        "text": "A healthy plant is kept in total darkness with plenty of "
                "water. Its cells still have all seven parts. What happens to "
                "it, and why?",
        "options": [
            {"text": "Very little — a plant cell can release energy from "
                     "light directly whenever it needs to.", "correct": False,
             "why": "Nothing in a cell releases energy from light. Light is "
                    "used to make food, and the energy is released from that "
                    "food afterwards, in the mitochondria."},
            {"text": "It dies at once, because a plant cell cannot survive a "
                     "moment without light.", "correct": False,
             "why": "It lives for a while on the food it has already stored. "
                    "What it cannot do is make any more."},
            {"text": "It carries on as normal, because the mitochondria make "
                     "food in the dark when the chloroplasts "
                     "cannot.", "correct": False,
             "why": "Mitochondria release energy from food; they never make "
                    "any. In the dark nothing at all is making food."},
            {"text": "It starves: with no light the chloroplasts cannot make "
                     "food.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h07",
        "band": "harder",
        "text": "A student's drawing of a leaf cell shows the chloroplasts "
                "floating inside the vacuole, and says that is where the "
                "plant keeps its green. Which correction is right?",
        "options": [
            {"text": "Chloroplasts sit in the cytoplasm, not the vacuole, "
                     "and the green is inside them.", "correct": True},
            {"text": "Chloroplasts sit packed inside the nucleus, which is "
                     "why the nucleus is pushed to one "
                     "side.", "correct": False,
             "why": "The nucleus is pushed aside by the vacuole, and it "
                    "holds instructions rather than chloroplasts. The "
                    "chloroplasts are out in the cytoplasm."},
            {"text": "The drawing is right — the vacuole is where a plant "
                     "cell keeps the green colour that its leaves show "
                     "outside.", "correct": False,
             "why": "The vacuole holds a watery sap of sugars and salts, and "
                    "it is not green. The green is chlorophyll, held inside "
                    "chloroplasts in the cytoplasm."},
            {"text": "Chloroplasts sit inside the cell wall, which is why a "
                     "leaf looks green.", "correct": False,
             "why": "The wall is a layer of cellulose and holds nothing "
                    "inside it. The chloroplasts are in the cytoplasm, "
                    "crowded up towards the light."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h08",
        "band": "harder",
        "text": "In pure water a cheek cell swells and bursts while a leaf "
                "cell keeps its shape. A student concludes that plant cell "
                "membranes are stronger. Why is that wrong?",
        "options": [
            {"text": "Because it is the leaf cell's vacuole doing the "
                     "holding and resisting, not its "
                     "membrane.", "correct": False,
             "why": "The vacuole is filling with water, not resisting it. "
                    "What stops the leaf cell splitting is the stiff wall "
                    "outside the membrane."},
            {"text": "Because the leaf cell lets no water in at all, so "
                     "there is nothing pushing outwards on its "
                     "membrane.", "correct": False,
             "why": "Water enters the leaf cell too — that is why it becomes "
                    "firm. It survives because the wall pushes back, not "
                    "because the water stays out."},
            {"text": "Because both membranes are alike, and it is the wall "
                     "outside that pushes back.", "correct": True},
            {"text": "Because a cheek cell has no membrane, so nothing was "
                     "there to burst.", "correct": False,
             "why": "Every cell here has a membrane, and it is the cheek "
                    "cell's membrane that splits. What it lacks is a wall "
                    "around it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h09",
        "band": "harder",
        "text": "A student writes “Mitochondria make energy for the cell.” "
                "The teacher asks for one word to be changed. Which "
                "correction is right?",
        "options": [
            {"text": "Mitochondria store energy for the cell.",
             "correct": False,
             "why": "Nothing is stored in a mitochondrion. The energy is "
                    "stored in the food, and the mitochondrion is where it is "
                    "released from it."},
            {"text": "Mitochondria release energy for the cell.",
             "correct": True},
            {"text": "Mitochondria collect energy for the cell.",
             "correct": False,
             "why": "Collecting suggests taking energy in from outside, which "
                    "is closer to what a chloroplast does with light. A "
                    "mitochondrion releases what is already in the food."},
            {"text": "Mitochondria make food for the cell.", "correct": False,
             "why": "Making food is the chloroplast's job, and only a plant "
                    "cell has those. Mitochondria release energy from food "
                    "that is already there."},
        ],
        "figure": None,
    },

    # ── MRB-338 expansion ───────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-03-e10",
        "band": "easier",
        "text": "The nucleus holds a cell's DNA. What is DNA?",
        "options": [
            {"text": "A store of energy the cell draws on when food runs "
                     "short.", "correct": False,
             "why": "Energy is released from food in the mitochondria, and "
                    "none of it is kept in the nucleus. DNA is information, "
                    "not fuel."},
            {"text": "The jelly that fills the nucleus and holds it in "
                     "shape.", "correct": False,
             "why": "The jelly is cytoplasm, and it fills the cell around "
                    "the nucleus. DNA is a set of instructions, not a "
                    "material."},
            {"text": "The instructions for running and building the cell.",
             "correct": True},
            {"text": "The green substance a plant uses to trap light.",
             "correct": False,
             "why": "That is chlorophyll, and it sits inside the "
                    "chloroplasts out in the cytoplasm — nowhere near the "
                    "nucleus."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e11",
        "band": "easier",
        "text": "State what a cell wall does for a plant cell.",
        "options": [
            {"text": "It gives the cell a fixed shape, and stops it "
                     "splitting when water floods in.", "correct": True},
            {"text": "It decides which substances are allowed into the "
                     "cell, and which are kept outside it.",
             "correct": False,
             "why": "That is the membrane's job, and a plant cell still has "
                    "one, just inside the wall. Things pass straight through "
                    "the wall itself."},
            {"text": "It traps light so the cell can make its own food.",
             "correct": False,
             "why": "Trapping light is what the chloroplasts do. The wall is "
                    "a stiff layer of cellulose and it makes nothing."},
            {"text": "It stores the water and the dissolved sugars and "
                     "salts that the cell is keeping.", "correct": False,
             "why": "That is the vacuole, which sits inside the cell. The "
                    "wall is the stiff layer around the outside of "
                    "everything."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e12",
        "band": "easier",
        "text": "Where in a plant cell is the cell membrane?",
        "options": [
            {"text": "Nowhere — a plant cell has no membrane, because the "
                     "wall took over that job.", "correct": False,
             "why": "A plant cell has both, and the wall never replaced "
                    "anything. Only the membrane chooses what crosses."},
            {"text": "Wrapped around the outside of the wall, as the cell's "
                     "first layer.", "correct": False,
             "why": "The wall is the outermost layer. The membrane lies "
                    "against it on the inside."},
            {"text": "Deep inside the cell, wrapped around the vacuole to "
                     "hold the sap in.", "correct": False,
             "why": "The membrane wraps the whole cytoplasm, right at the "
                    "edge of the cell. The vacuole sits well inside it."},
            {"text": "Just inside the cell wall, pressed against it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e13",
        "band": "easier",
        "text": "Chlorophyll is the green substance in a plant. Where is it "
                "found?",
        "options": [
            {"text": "Dissolved in the watery sap that fills the vacuole.",
             "correct": False,
             "why": "Cell sap is water with sugars and salts in it, and it "
                    "is not green. The green is held inside the "
                    "chloroplasts."},
            {"text": "Inside the chloroplasts, out in the cytoplasm.",
             "correct": True},
            {"text": "Spread through the cellulose the cell wall is built "
                     "from.", "correct": False,
             "why": "Cell walls are colourless — the walls of an onion bulb "
                    "are the clearest thing on a slide. Chlorophyll sits in "
                    "the chloroplasts."},
            {"text": "In the nucleus, kept alongside the cell's "
                     "instructions.", "correct": False,
             "why": "The nucleus holds DNA and nothing green. Chlorophyll is "
                    "a pigment, held inside chloroplasts."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e14",
        "band": "easier",
        "text": "Which four parts are found in an animal cell and a plant "
                "cell alike?",
        "options": [
            {"text": "Cell membrane, cytoplasm, nucleus and mitochondria",
             "correct": True},
            {"text": "Cell membrane, cytoplasm, nucleus and cell wall",
             "correct": False,
             "why": "Only a plant cell has a wall. A cheek cell has to bend "
                    "as your jaw moves, and a cellulose box would crack."},
            {"text": "Cell membrane, cytoplasm, cell wall and chloroplasts",
             "correct": False,
             "why": "The wall and the chloroplasts are both plant extras. "
                    "The first two on that list are in every cell here."},
            {"text": "Cytoplasm, nucleus, vacuole and mitochondria",
             "correct": False,
             "why": "A large permanent vacuole belongs to a plant cell. The "
                    "other three are indeed in both."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e15",
        "band": "easier",
        "text": "Mitochondria release energy from food. What is that process "
                "called?",
        "options": [
            {"text": "Photosynthesis", "correct": False,
             "why": "Photosynthesis is light being used to make food, and it "
                    "happens in a plant cell's chloroplasts."},
            {"text": "Digestion", "correct": False,
             "why": "Digestion breaks food down before it ever reaches your "
                    "cells. Releasing the energy from it afterwards is "
                    "respiration."},
            {"text": "Respiration", "correct": True},
            {"text": "Wilting", "correct": False,
             "why": "Wilting is a plant drooping when its cells lose water. "
                    "It has nothing to do with energy."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e16",
        "band": "easier",
        "text": "What does the sap inside a plant cell's vacuole do for the "
                "cell?",
        "options": [
            {"text": "It carries the cell's instructions out from the "
                     "nucleus to all of the other parts.", "correct": False,
             "why": "The instructions stay in the nucleus. The sap is water "
                    "with sugars and salts dissolved in it."},
            {"text": "It presses outwards on the wall and keeps the cell "
                     "firm.", "correct": True},
            {"text": "It traps the light the cell needs to make its own "
                     "food.", "correct": False,
             "why": "Light is trapped by the chloroplasts out in the "
                    "cytoplasm. Cell sap is not green and traps nothing."},
            {"text": "It kills anything harmful that gets through the "
                     "wall.", "correct": False,
             "why": "Nothing in the vacuole does that. What decides whether "
                    "something gets into the cell at all is the membrane."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e17",
        "band": "easier",
        "text": "Cells are measured in micrometres (µm). How many "
                "micrometres are there in 1 mm?",
        "options": [
            {"text": "10", "correct": False,
             "why": "A micrometre is far smaller than that. There are 1000 "
                    "of them in a single millimetre."},
            {"text": "100", "correct": False,
             "why": "There are 100 centimetres in a metre, but a micrometre "
                    "is a smaller step again: 1 mm is 1000 µm."},
            {"text": "10 000", "correct": False,
             "why": "That is ten times too many. 1 mm is 1000 µm, and a "
                    "cheek cell is about 60 µm across."},
            {"text": "1000", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e18",
        "band": "easier",
        "text": "A cheek cell contains a membrane, cytoplasm, a nucleus and "
                "mitochondria. How many of those four are also in a leaf "
                "cell?",
        "options": [
            {"text": "Two of them", "correct": False,
             "why": "All four are there. A leaf cell runs off the same list "
                    "and adds three more of its own."},
            {"text": "Three of them", "correct": False,
             "why": "None of the four is left out. The difference between "
                    "the two cells runs one way only."},
            {"text": "All four", "correct": True},
            {"text": "None of them", "correct": False,
             "why": "Every one of them is in a leaf cell too — that is the "
                    "point worth keeping about these two lists."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e19",
        "band": "easier",
        "text": "A root hair cell has six of a plant cell's seven parts. "
                "Which one does it go without?",
        "options": [
            {"text": "Chloroplasts", "correct": True},
            {"text": "The cell wall", "correct": False,
             "why": "It has a wall like every other plant cell. What it goes "
                    "without is chloroplasts, because no light reaches a "
                    "root."},
            {"text": "The vacuole", "correct": False,
             "why": "A root hair cell has a large vacuole. The missing part "
                    "is chloroplasts, and the reason is the dark."},
            {"text": "Mitochondria", "correct": False,
             "why": "It keeps plenty of those — taking minerals out of soil "
                    "needs energy. Chloroplasts are the part it lacks."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e20",
        "band": "easier",
        "text": "A palisade cell sits just under the top surface of a leaf. "
                "How many of the seven parts does it have?",
        "options": [
            {"text": "Four, the same four that an animal cell has",
             "correct": False,
             "why": "It is a plant cell, so it carries a wall, a vacuole and "
                    "chloroplasts on top of those four."},
            {"text": "Six, because no cell anywhere has all seven",
             "correct": False,
             "why": "A palisade cell has all seven. Six is the count for a "
                    "root hair cell, which builds no chloroplasts."},
            {"text": "Five, because it has no vacuole", "correct": False,
             "why": "It has a large vacuole, like other plant cells. Nothing "
                    "is left out of a palisade cell."},
            {"text": "All seven", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e21",
        "band": "easier",
        "text": "Once methylene blue has been added to a cheek cell, which "
                "part becomes the darkest thing in the field of view?",
        "options": [
            {"text": "The mitochondria", "correct": False,
             "why": "They stay invisible. They are far below the size a "
                    "school microscope can separate, stained or not."},
            {"text": "The nucleus", "correct": True},
            {"text": "The cell wall", "correct": False,
             "why": "A cheek cell is an animal cell and has no wall at all. "
                    "A stain cannot show you something that is not there."},
            {"text": "The vacuole", "correct": False,
             "why": "A large permanent vacuole is a plant part. What the "
                    "stain picks out here is the nucleus."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e22",
        "band": "easier",
        "text": "Which part of a plant cell lets water and dissolved "
                "substances pass straight through, choosing none of them?",
        "options": [
            {"text": "The cell membrane", "correct": False,
             "why": "The membrane is exactly where the choosing happens, in "
                    "a plant cell as much as in yours."},
            {"text": "The vacuole", "correct": False,
             "why": "The vacuole is a store deep inside the cell. Anything "
                    "reaching it has already crossed the membrane."},
            {"text": "The cell wall", "correct": True},
            {"text": "The nucleus", "correct": False,
             "why": "The nucleus holds the cell's instructions. Nothing "
                    "enters or leaves the cell by way of it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e23",
        "band": "easier",
        "text": "What is actually in the cytoplasm?",
        "options": [
            {"text": "Dissolved substances, and the other parts of the cell "
                     "held in place.", "correct": True},
            {"text": "Nothing — it is the gap left between the parts.",
             "correct": False,
             "why": "It is crowded, not empty, and nearly all of the cell's "
                    "reactions happen in it."},
            {"text": "Air, drawn in through the membrane, which keeps the "
                     "cell inflated.", "correct": False,
             "why": "There is no air inside a cell. The cytoplasm is a "
                    "jelly, crowded with dissolved substances."},
            {"text": "Water only, with everything else floating on top.",
             "correct": False,
             "why": "It is a jelly with a great deal dissolved in it, and "
                    "the other parts sit within it rather than on it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e24",
        "band": "easier",
        "text": "A microscope is set to ×400. What does that number tell "
                "you?",
        "options": [
            {"text": "You can fit exactly 400 cells into the field of view.",
             "correct": False,
             "why": "Magnification is not a count of cells. It says how much "
                    "bigger the image is than the object."},
            {"text": "The cell you are looking at is 400 µm across.",
             "correct": False,
             "why": "The number is a magnification, not a measurement. A "
                    "cheek cell is about 60 µm across at any setting."},
            {"text": "The image is 400 times wider than the real object.",
             "correct": True},
            {"text": "There are 400 separate parts to count inside one "
                     "cell.", "correct": False,
             "why": "A plant cell has seven parts to name at this stage. The "
                    "400 is how many times bigger the image is."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e25",
        "band": "easier",
        "text": "A wilted plant is watered and stands up again by the "
                "evening. Which part of its cells has filled with water?",
        "options": [
            {"text": "The nucleus", "correct": False,
             "why": "The nucleus holds instructions and does not swell with "
                    "water. What fills is the vacuole."},
            {"text": "The chloroplasts", "correct": False,
             "why": "Chloroplasts trap light and have nothing to do with "
                    "firmness. The vacuoles are what fill and press out."},
            {"text": "The cell walls", "correct": False,
             "why": "A wall is a stiff layer that neither fills nor empties. "
                    "What fills is the vacuole inside it."},
            {"text": "The vacuoles", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e26",
        "band": "easier",
        "text": "What is the correct name for a single one of the structures "
                "called mitochondria?",
        "options": [
            {"text": "Mitochondrias", "correct": False,
             "why": "That is a plural made twice over. One of them is a "
                    "mitochondrion."},
            {"text": "Mitochondrion", "correct": True},
            {"text": "Mitochondria", "correct": False,
             "why": "That is the plural — a cell holds many mitochondria. "
                    "One of them is a mitochondrion."},
            {"text": "Mitochondrium", "correct": False,
             "why": "Close, but the ending is -on: one mitochondrion, "
                    "several mitochondria."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e27",
        "band": "easier",
        "text": "Which part is only built in the cells of a plant that light "
                "actually reaches?",
        "options": [
            {"text": "The cell wall, which every plant cell builds",
             "correct": False,
             "why": "Every plant cell has a wall, roots and bulbs included. "
                    "Chloroplasts are the part that waits for light."},
            {"text": "The vacuole, which fills with cell sap",
             "correct": False,
             "why": "A root hair cell has a large vacuole and has never seen "
                    "light. Chloroplasts are the light-dependent part."},
            {"text": "The chloroplasts", "correct": True},
            {"text": "The mitochondria, which every living cell has",
             "correct": False,
             "why": "Every cell has mitochondria, in the dark as much as in "
                    "the light. Chloroplasts are the part light decides."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e28",
        "band": "easier",
        "text": "A cell loses its nucleus. Which two things can it no longer "
                "do?",
        "options": [
            {"text": "Build new parts, and divide to make new cells.",
             "correct": True},
            {"text": "Release energy from food, and grow.", "correct": False,
             "why": "Energy is released in the mitochondria, and they carry "
                    "on regardless. What is lost is the instructions."},
            {"text": "Take in water, and hold its shape.", "correct": False,
             "why": "Water crosses the membrane, and shape is held by the "
                    "wall in a plant cell. Neither needs the nucleus."},
            {"text": "Trap light, and make its own food.", "correct": False,
             "why": "That is the chloroplasts' job, and an animal cell never "
                    "had it. Losing the nucleus loses the instructions."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e29",
        "band": "easier",
        "text": "Two of a leaf cell's seven parts cannot be seen down a "
                "school microscope. Which two?",
        "options": [
            {"text": "The large vacuole and the nucleus beside it",
             "correct": False,
             "why": "Both are easy to see: a large pale region in the middle "
                    "and a dark spot pushed to one side."},
            {"text": "The cell membrane and the mitochondria",
             "correct": True},
            {"text": "The cell wall and the green chloroplasts",
             "correct": False,
             "why": "Those are the clearest things on the slide — the walls "
                    "draw the honeycomb, and chloroplasts are green ovals."},
            {"text": "The chloroplasts and the mitochondria",
             "correct": False,
             "why": "A chloroplast is several times wider than a "
                    "mitochondrion, and it shows up plainly without a "
                    "stain."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e30",
        "band": "easier",
        "text": "Which part would tell you fastest, down a microscope, that "
                "you are looking at plant tissue rather than animal tissue?",
        "options": [
            {"text": "The nucleus, sitting somewhere near the centre of "
                     "the cell", "correct": False,
             "why": "Both kinds of cell have one, so seeing a nucleus "
                    "settles nothing. A wall is in plant cells only."},
            {"text": "The cytoplasm, filling all of the space inside the "
                     "cell", "correct": False,
             "why": "Every cell is filled with cytoplasm. It cannot tell the "
                    "two kinds of tissue apart."},
            {"text": "The mitochondria, scattered right through the cell",
             "correct": False,
             "why": "They are in both, and you cannot see them anyway — they "
                    "are below what the microscope can separate."},
            {"text": "The cell wall, drawing a honeycomb of neat boxes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e31",
        "band": "easier",
        "text": "A plant cannot move about to find food. Which part of its "
                "cells answers that problem?",
        "options": [
            {"text": "The chloroplasts", "correct": True},
            {"text": "The cell wall", "correct": False,
             "why": "The wall answers a different problem: a plant has no "
                    "skeleton, so each cell holds its own shape."},
            {"text": "The mitochondria", "correct": False,
             "why": "Every living thing has those, moving or not. Making "
                    "food out of light is the chloroplasts' answer."},
            {"text": "The nucleus", "correct": False,
             "why": "Every cell has a nucleus, in animals as much as in "
                    "plants, so it is not one of the plant's extras."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-e32",
        "band": "easier",
        "text": "Which part, if it stopped working, would let substances "
                "leak both into and out of the cell?",
        "options": [
            {"text": "The nucleus, deep inside the cell", "correct": False,
             "why": "Losing the nucleus loses the instructions, not the "
                    "seal. Nothing starts leaking."},
            {"text": "The vacuole, in the middle of the cell",
             "correct": False,
             "why": "The vacuole is a store inside the cell. Emptying it "
                    "makes the cell limp rather than leaky."},
            {"text": "The cell membrane", "correct": True},
            {"text": "The cell wall, around the outside", "correct": False,
             "why": "Substances already pass straight through the wall, so "
                    "it holds nothing in. The membrane is what chooses."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-03-s10",
        "band": "standard",
        "text": "A cheek cell is 60 µm across. Calculate how wide it appears "
                "at ×400, in millimetres.",
        "options": [
            {"text": "0.15 mm", "correct": False,
             "why": "That divides by the magnification. The image is the "
                    "bigger one: 60 µm × 400 = 24 000 µm, which is 24 mm."},
            {"text": "24 mm", "correct": True},
            {"text": "2.4 mm", "correct": False,
             "why": "A power of ten has slipped. 60 µm × 400 = 24 000 µm, "
                    "and 24 000 µm ÷ 1000 = 24 mm."},
            {"text": "24 000 mm", "correct": False,
             "why": "24 000 is the answer in micrometres, not millimetres. "
                    "Dividing by 1000 converts it to 24 mm."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s11",
        "band": "standard",
        "text": "A cell measures 30 mm across in a photograph taken at ×300. "
                "Calculate its real width in micrometres.",
        "options": [
            {"text": "9000 µm", "correct": False,
             "why": "That multiplies where it should divide. The photograph "
                    "is 300 times too big, so the real width is 30 ÷ 300."},
            {"text": "0.1 µm", "correct": False,
             "why": "30 mm ÷ 300 = 0.1 mm, and the question asks for "
                    "micrometres. 0.1 mm is 100 µm."},
            {"text": "10 µm", "correct": False,
             "why": "That is ten times too small — check the conversion. "
                    "0.1 mm is 100 µm, not 10 µm."},
            {"text": "100 µm", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s12",
        "band": "standard",
        "text": "A chloroplast is about 5 µm across and a mitochondrion "
                "about 1 µm. Explain why only one of them can be made out at "
                "×400.",
        "options": [
            {"text": "The chloroplast is five times wider, and that is "
                     "enough to be separated at ×400 while the "
                     "mitochondrion is not.", "correct": True},
            {"text": "The mitochondrion is not in a plant cell at all, so "
                     "at ×400 there is nothing there for the lens to pick "
                     "up.", "correct": False,
             "why": "Every plant cell has mitochondria. They are simply "
                    "below the size the microscope can separate."},
            {"text": "The chloroplast is stained during the practical and "
                     "the mitochondrion is not.", "correct": False,
             "why": "Chloroplasts need no stain at all — the green is "
                    "chlorophyll, already inside them."},
            {"text": "The mitochondrion moves too fast to be caught in the "
                     "field of view.", "correct": False,
             "why": "Speed is not the problem. At about 1 µm across it is "
                    "below what the microscope can separate."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s13",
        "band": "standard",
        "text": "A muscle cell and a cheek cell have the same four parts, "
                "yet a muscle cell holds far more mitochondria. Suggest why.",
        "options": [
            {"text": "Because a muscle cell is bigger, so more of everything "
                     "fits inside it.", "correct": False,
             "why": "Size is not the reason. A cell that works constantly "
                    "needs energy released constantly, whatever its size."},
            {"text": "Because muscle cells make their own food and cheek "
                     "cells do not.", "correct": False,
             "why": "Nothing in your body makes food. Both cells are given "
                    "it ready made."},
            {"text": "Because it contracts all day, and needs energy "
                     "released without stopping.", "correct": True},
            {"text": "Because mitochondria are what pull a muscle cell "
                     "shorter when it contracts.", "correct": False,
             "why": "Contracting is done by the cell itself. The "
                    "mitochondria release the energy that lets it happen."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s14",
        "band": "standard",
        "text": "The top of a leaf is a darker green than its underside. "
                "Explain that difference in terms of cells.",
        "options": [
            {"text": "The waxy coating on the upper surface of a leaf is "
                     "itself green, and the underside of the leaf carries "
                     "none of it at all.", "correct": False,
             "why": "The colour comes from chlorophyll inside chloroplasts, "
                    "not from any coating on the outside."},
            {"text": "The cells on top are larger, so their walls are "
                     "thicker and darker.", "correct": False,
             "why": "Cell walls are colourless — an onion bulb's walls are "
                    "the clearest thing on a slide."},
            {"text": "The vacuoles of the upper cells are filled with green "
                     "sap.", "correct": False,
             "why": "Cell sap is water with sugars and salts in it, and it "
                    "is not green. The green is in the chloroplasts."},
            {"text": "The cells just under the upper surface are packed with "
                     "chloroplasts, because the light reaches them first.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s15",
        "band": "standard",
        "text": "A root hair cell has no chloroplasts but keeps plenty of "
                "mitochondria. Explain why it needs them.",
        "options": [
            {"text": "So that it can make its own food underground, where "
                     "no light has ever reached it.", "correct": False,
             "why": "Making food needs light and chloroplasts, and it has "
                    "neither. Mitochondria release energy from food already "
                    "made."},
            {"text": "Taking minerals out of the soil needs energy, and "
                     "mitochondria release it.", "correct": True},
            {"text": "So it can hold its shape without a cell wall to do "
                     "it.", "correct": False,
             "why": "It has a wall like every plant cell, and mitochondria "
                    "have nothing to do with shape."},
            {"text": "So it has somewhere to store the water it draws from "
                     "the soil.", "correct": False,
             "why": "Water is stored in the vacuole. Mitochondria release "
                    "energy from food."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s16",
        "band": "standard",
        "text": "A cell has every part it needs except mitochondria. "
                "Predict what happens to it.",
        "options": [
            {"text": "It bursts, because nothing is pushing back against "
                     "the water coming in.", "correct": False,
             "why": "Bursting is what a missing wall does. The part left out "
                    "here is the cell's energy supply."},
            {"text": "It survives, because the cytoplasm releases the energy "
                     "instead.", "correct": False,
             "why": "Many reactions happen in the cytoplasm, but the energy "
                    "in food is released in the mitochondria."},
            {"text": "No energy is released from its food, so nothing else "
                     "it has can work.", "correct": True},
            {"text": "It goes limp, because nothing presses out against its "
                     "wall any more.", "correct": False,
             "why": "That is what a missing vacuole does. Losing the "
                    "mitochondria loses the energy supply instead."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s17",
        "band": "standard",
        "text": "Why is a cell with no cytoplasm better described as a bag "
                "than as a cell?",
        "options": [
            {"text": "Nothing holds its parts in place, and its reactions "
                     "have nowhere to happen.", "correct": True},
            {"text": "Nothing is left in it to store the water and the "
                     "dissolved sugars the cell needs.", "correct": False,
             "why": "Water is stored in a plant cell's vacuole. What the "
                    "cytoplasm gives is a place for reactions and a hold on "
                    "the parts."},
            {"text": "Nothing is left to give it a fixed shape.",
             "correct": False,
             "why": "Shape is held by the wall in a plant cell. Without "
                    "cytoplasm, no reaction can happen anywhere."},
            {"text": "Nothing is left inside it that can release the "
                     "energy that is held in its food.", "correct": False,
             "why": "That is the mitochondria's job, and they would still be "
                    "present — with nothing holding them in place."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s18",
        "band": "standard",
        "text": "A student turns a microscope from ×400 up to ×1000 to hunt "
                "for mitochondria, and still sees none. Explain why.",
        "options": [
            {"text": "The mitochondria were destroyed by the stain used on "
                     "the slide, so by ×1000 there was nothing left there "
                     "to find.", "correct": False,
             "why": "A stain adds colour and destroys nothing. The limit "
                    "here belongs to the microscope."},
            {"text": "Mitochondria are only in animal cells, and this is "
                     "a leaf cell.", "correct": False,
             "why": "Every cell here has mitochondria, plant and animal "
                    "alike."},
            {"text": "The slide would need staining again at the higher "
                     "setting.", "correct": False,
             "why": "No stain helps. Mitochondria are below the size this "
                    "microscope can separate at any setting."},
            {"text": "Turning the magnification up gives a bigger blur, not "
                     "more detail — the limit is what the microscope can "
                     "separate.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s19",
        "band": "standard",
        "text": "Chloroplasts show up clearly on an unstained slide of leaf "
                "tissue. Explain why no stain is needed for them.",
        "options": [
            {"text": "They are the only part of the cell large enough to be "
                     "seen at all.", "correct": False,
             "why": "The wall, the vacuole and the nucleus are all visible "
                    "unstained too. What sets chloroplasts apart is colour."},
            {"text": "They are green already, and wide enough to be "
                     "separated at ×400.", "correct": True},
            {"text": "Leaf tissue is too thin for any stain to stick to it.",
             "correct": False,
             "why": "Stains work on leaf tissue perfectly well. Chloroplasts "
                    "simply do not need one."},
            {"text": "A stain would wash the chlorophyll out and leave "
                     "nothing to look at.", "correct": False,
             "why": "Stains add colour rather than removing it. "
                    "Chloroplasts are visible because they are green "
                    "already."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s20",
        "band": "standard",
        "text": "A potato tuber grows underground and is not green, while "
                "the same plant's leaves are. Explain the difference.",
        "options": [
            {"text": "Chloroplasts are only built where light reaches, and "
                     "none reaches a tuber.", "correct": True},
            {"text": "A tuber is not really part of the plant, so its cells "
                     "are built differently.", "correct": False,
             "why": "A tuber is made of ordinary plant cells. What it lacks "
                    "is light, so its cells build no chloroplasts."},
            {"text": "A tuber's cells have no cytoplasm for chloroplasts to "
                     "sit in.", "correct": False,
             "why": "Every cell has cytoplasm. The reason there are no "
                    "chloroplasts is that no light arrives."},
            {"text": "The green drains out of a tuber into the soil around "
                     "it.", "correct": False,
             "why": "Nothing drains anywhere. Chloroplasts are never built "
                    "in the dark in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s21",
        "band": "standard",
        "text": "Limp celery is stood in water for an hour and goes stiff "
                "again. Explain what has happened inside its cells.",
        "options": [
            {"text": "The cell walls have taken up water and hardened.",
             "correct": False,
             "why": "A wall neither softens nor hardens — it was stiff "
                    "throughout. What refills is the vacuole."},
            {"text": "New chloroplasts have been built now that the stalk "
                     "has taken up water.", "correct": False,
             "why": "Chloroplasts are about food, not firmness, and celery "
                    "in a beaker is building none."},
            {"text": "Water has moved back into the vacuoles, which press "
                     "out on the walls again.", "correct": True},
            {"text": "The membranes have sealed, so no more water can "
                     "escape.", "correct": False,
             "why": "The membrane was never leaking. The stalk went limp "
                    "because water had left the vacuoles."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s22",
        "band": "standard",
        "text": "A plant cell is left in very salty water, and water moves "
                "out of it. Predict what happens to the cell.",
        "options": [
            {"text": "It bursts, because the salt pulls the wall apart from "
                     "outside.", "correct": False,
             "why": "Bursting follows water moving in with nothing to push "
                    "back. Here water is leaving."},
            {"text": "Its vacuole shrinks, the push on the wall drops, and "
                     "the cell goes limp.", "correct": True},
            {"text": "Nothing changes, because the wall keeps all the water "
                     "inside the cell.", "correct": False,
             "why": "Water passes straight through the wall. The membrane "
                    "controls what crosses, and water crosses it easily."},
            {"text": "It turns a deeper green, as the chloroplasts are "
                     "packed closer together.", "correct": False,
             "why": "A cell losing water does not change colour, and many "
                    "plant cells hold no chloroplasts at all."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s23",
        "band": "standard",
        "text": "At the edge of a leaf cell there are two lines, one just "
                "inside the other. Name them, from the outside inwards.",
        "options": [
            {"text": "Membrane on the outside, then the wall just inside "
                     "it.", "correct": False,
             "why": "It is the other way round. The wall is built outside "
                    "the membrane, and the membrane lies against it."},
            {"text": "Wall on the outside, then the cytoplasm just inside "
                     "it.", "correct": False,
             "why": "The cytoplasm is further in again. The line pressed "
                    "against the wall is the membrane."},
            {"text": "Two walls, an outer one and an inner one.",
             "correct": False,
             "why": "A plant cell builds one wall. The second line is the "
                    "membrane, doing the job it does in your cells too."},
            {"text": "Wall on the outside, then the membrane just inside "
                     "it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s24",
        "band": "standard",
        "text": "Onion cells show a clear outline down a microscope, while "
                "cheek cells barely show an edge at all. Explain why.",
        "options": [
            {"text": "Onion cells are stained and cheek cells are not.",
             "correct": False,
             "why": "It is the cheek cells that get stained. Onion cells "
                    "show up because of their walls."},
            {"text": "Cheek cells are far smaller than onion cells.",
             "correct": False,
             "why": "The two are much the same order of size. One has a "
                    "stiff wall and the other has only a membrane."},
            {"text": "An onion cell has a stiff wall thick enough to see, "
                     "while a cheek cell has only a membrane, which is far "
                     "too thin.", "correct": True},
            {"text": "Onion cells are dead, so they hold still under the "
                     "lens, while a living cheek cell keeps drifting out of "
                     "focus.", "correct": False,
             "why": "Neither cell is moving on the slide. The wall is what "
                    "draws the outline you can see."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s25",
        "band": "standard",
        "text": "Eight leaf cells sit side by side across a field of view "
                "0.4 mm wide. Calculate the width of one cell.",
        "options": [
            {"text": "50 µm", "correct": True},
            {"text": "5 µm", "correct": False,
             "why": "That is ten times too small. 0.4 mm is 400 µm, and "
                    "400 ÷ 8 = 50."},
            {"text": "0.05 µm", "correct": False,
             "why": "The conversion has gone the wrong way. 0.4 mm is "
                    "400 µm, so each cell is 50 µm."},
            {"text": "3200 µm", "correct": False,
             "why": "That multiplies where it should divide. Eight cells "
                    "share 400 µm between them."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s26",
        "band": "standard",
        "text": "A leaf cell is 50 µm wide and one of its chloroplasts is "
                "5 µm across. How many times wider is the cell?",
        "options": [
            {"text": "45 times", "correct": False,
             "why": "That subtracts one from the other. To compare sizes you "
                    "divide: 50 ÷ 5 = 10."},
            {"text": "10 times", "correct": True},
            {"text": "100 times", "correct": False,
             "why": "That is ten times too many. 50 ÷ 5 = 10."},
            {"text": "250 times", "correct": False,
             "why": "That multiplies the two numbers together. Dividing is "
                    "what compares them: 50 ÷ 5 = 10."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s27",
        "band": "standard",
        "text": "A student says the food you eat gives you energy the moment "
                "you swallow it. Where is that energy actually released?",
        "options": [
            {"text": "In the stomach, as soon as the food is broken down "
                     "there.", "correct": False,
             "why": "Breaking food down is not the same as releasing its "
                    "energy. That happens later, inside your cells."},
            {"text": "In the blood, while the food is carried round the "
                     "body.", "correct": False,
             "why": "Blood carries food and oxygen to the cells. The energy "
                    "is released once they arrive."},
            {"text": "In the nucleus of each cell, which controls "
                     "everything.", "correct": False,
             "why": "The nucleus holds instructions. Energy is released in "
                    "the mitochondria, by respiration."},
            {"text": "In the mitochondria of your cells, by respiration.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s28",
        "band": "standard",
        "text": "Why is a drawing that shows the cytoplasm as clear, empty "
                "space misleading?",
        "options": [
            {"text": "It is crowded — with dissolved substances, and with "
                     "every other part of the cell.", "correct": True},
            {"text": "It is not really there at all in a plant cell, where "
                     "the vacuole takes up all the room.", "correct": False,
             "why": "Every cell here is filled with cytoplasm. It is simply "
                    "not empty."},
            {"text": "It is a solid all the way through, so nothing "
                     "whatever can be dissolved inside it.", "correct": False,
             "why": "It is a jelly rather than a solid, and a great deal is "
                    "dissolved in it."},
            {"text": "It is only found in the narrow space immediately "
                     "around the nucleus and nowhere else.", "correct": False,
             "why": "It fills the whole cell around the other parts, "
                    "squeezed into a rim by the vacuole in a plant cell."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s29",
        "band": "standard",
        "text": "A plant has no skeleton. Which two parts of its cells work "
                "together to hold it upright?",
        "options": [
            {"text": "The membrane and the cytoplasm, which are firm in a "
                     "plant cell.", "correct": False,
             "why": "Both are in your cells too, and you are held up by "
                    "bone. The plant's answer uses parts you do not have."},
            {"text": "The chloroplasts and the nucleus, working from the "
                     "middle of the cell.", "correct": False,
             "why": "One makes food and one holds instructions. Neither "
                    "holds anything up."},
            {"text": "The vacuole and the cell wall.", "correct": True},
            {"text": "The cell wall and the mitochondria, which stiffen it "
                     "as they work.", "correct": False,
             "why": "The wall is half of the answer, but what presses out "
                    "against it is the sap in the vacuole."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s30",
        "band": "standard",
        "text": "Down a school microscope you can make out five parts of a "
                "leaf cell but only two of a cheek cell. Explain why.",
        "options": [
            {"text": "A cheek cell is far too small for a school microscope "
                     "to separate any one part of it from the next one "
                     "along.", "correct": False,
             "why": "You can see its outline and, once stained, its nucleus. "
                    "Size is not what makes the difference."},
            {"text": "The parts of a cheek cell are packed too tightly "
                     "together to separate.", "correct": False,
             "why": "A cheek cell has four parts and plenty of room. It "
                    "simply has fewer large ones."},
            {"text": "A leaf cell has been stained and a cheek cell has "
                     "not.", "correct": False,
             "why": "It is the cheek cell that is stained. A leaf cell's "
                    "extra parts are visible without one."},
            {"text": "All three of the plant's extra parts are large enough "
                     "to see, and the two hidden ones are the same in both "
                     "cells.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s31",
        "band": "standard",
        "text": "In the cheek cell practical each student uses their own "
                "clean swab, which goes straight into disinfectant "
                "afterwards. Explain why.",
        "options": [
            {"text": "Because a used swab would carry the methylene blue "
                     "across onto the next student's slide instead.",
             "correct": False,
             "why": "The stain is added on the slide afterwards. This rule "
                    "is about not passing anything between people."},
            {"text": "Because a swab carries material from one person's "
                     "mouth, and it must not reach anyone else's.",
             "correct": True},
            {"text": "Because the cells die within seconds unless the swab "
                     "is a fresh one.", "correct": False,
             "why": "The cells last long enough to be looked at. The care is "
                    "about hygiene, not freshness."},
            {"text": "Because disinfectant is what makes the cells show up "
                     "under the microscope.", "correct": False,
             "why": "Methylene blue is what makes them show up. Disinfectant "
                    "is there to make the used swab safe."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-s32",
        "band": "standard",
        "text": "A student concludes that an onion has no chloroplasts "
                "anywhere, because the onion cells on their slide were "
                "colourless. What is wrong with that?",
        "options": [
            {"text": "The slide came from the bulb, which grows "
                     "underground; the onion's green leaves above ground are "
                     "full of them.", "correct": True},
            {"text": "Onion cells are not plant cells, so the question does "
                     "not arise.", "correct": False,
             "why": "They are plant cells — walls, vacuoles and all. What is "
                    "missing underground is the light."},
            {"text": "The chloroplasts were washed out of the cells by the "
                     "water used to mount the slide, leaving them "
                     "colourless.", "correct": False,
             "why": "Nothing washes chloroplasts out. Cells grown in the "
                    "dark never build any."},
            {"text": "The stain used on the slide hides green colours.",
             "correct": False,
             "why": "There is no green there to hide — a bulb grows in the "
                    "dark, and its cells build no chloroplasts."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-03-h10",
        "band": "harder",
        "text": "A leaf cell that is really 90 µm wide appears 45 mm across "
                "in a photograph. Determine the magnification.",
        "options": [
            {"text": "×0.5", "correct": False,
             "why": "That divides 45 by 90 without converting the units "
                    "first. 45 mm is 45 000 µm, and 45 000 ÷ 90 = 500."},
            {"text": "×50", "correct": False,
             "why": "A power of ten has slipped somewhere. 45 000 µm ÷ 90 µm "
                    "= 500."},
            {"text": "×500", "correct": True},
            {"text": "×5000", "correct": False,
             "why": "That is ten times too many — check the division. "
                    "45 000 ÷ 90 = 500."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h11",
        "band": "harder",
        "text": "At ×100 a field of view is 1.6 mm across. Determine how "
                "wide the field is at ×400, and what that does to the number "
                "of cells in view.",
        "options": [
            {"text": "6.4 mm, and more cells are in view.", "correct": False,
             "why": "Raising the magnification narrows the field rather than "
                    "widening it: four times the magnification gives a "
                    "quarter of the width."},
            {"text": "0.4 mm, and fewer cells are in view.", "correct": True},
            {"text": "1.2 mm, and about the same number are in view.",
             "correct": False,
             "why": "The field narrows by the same factor the magnification "
                    "rises — four times, from 1.6 mm down to 0.4 mm."},
            {"text": "0.4 mm, and more cells are in view.", "correct": False,
             "why": "The width is right, but a narrower field holds fewer "
                    "cells, each of them looking bigger."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h12",
        "band": "harder",
        "text": "A student measures a cell as 0.08 mm and writes it down as "
                "8 µm. Identify the mistake and give the correct value.",
        "options": [
            {"text": "There is no mistake: 0.08 mm really is 8 µm.",
             "correct": False,
             "why": "There are 1000 µm in a millimetre, so 0.08 mm is "
                    "80 µm."},
            {"text": "They should have written 0.8 µm, since 0.08 mm is "
                     "smaller than one micrometre.", "correct": False,
             "why": "A micrometre is a thousandth of a millimetre, so "
                    "0.08 mm is much larger than one: it is 80 µm."},
            {"text": "They multiplied by 100 instead of 1000; the cell is "
                     "80 µm across.", "correct": True},
            {"text": "They should have written 800 µm, since there are "
                     "10 000 µm in a millimetre.", "correct": False,
             "why": "There are 1000 µm in a millimetre, not 10 000, so "
                    "0.08 mm is 80 µm."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h13",
        "band": "harder",
        "text": "Two animal cells are the same size, but one holds far more "
                "mitochondria than the other. What can you conclude?",
        "options": [
            {"text": "One of them does far more work, so it needs energy "
                     "released far more often.", "correct": True},
            {"text": "One of them is really a plant cell, and plant cells "
                     "hold more of everything.", "correct": False,
             "why": "Both are animal cells here, and mitochondria are not "
                    "one of the plant's extras in any case."},
            {"text": "One of them is older, and mitochondria build up in a "
                     "cell over time.", "correct": False,
             "why": "The number matches the job, not the age. A muscle cell "
                    "is packed with them from the start."},
            {"text": "One of them has lost its nucleus, so there is more "
                     "room inside it.", "correct": False,
             "why": "A nucleus takes up very little of a cell, and a cell "
                    "without one cannot build new parts at all."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h14",
        "band": "harder",
        "text": "A root hair cell and a palisade cell are both plant cells, "
                "and their parts lists differ by exactly one. Name it and "
                "explain the difference.",
        "options": [
            {"text": "The vacuole: only a palisade cell has one, because "
                     "only it stores sugars.", "correct": False,
             "why": "Both have a large vacuole. The part that differs is "
                    "chloroplasts."},
            {"text": "Chloroplasts: a palisade cell gets light and a root "
                     "hair cell never does.", "correct": True},
            {"text": "The cell wall: a root hair cell has none, so it can "
                     "push between soil particles.", "correct": False,
             "why": "A root hair cell has a wall like every plant cell. What "
                    "it has no use for is chloroplasts."},
            {"text": "Mitochondria: only a root hair cell has them, because "
                     "it takes minerals in.", "correct": False,
             "why": "Both have mitochondria — every cell does. The one part "
                    "that differs is chloroplasts."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h15",
        "band": "harder",
        "text": "A plant is kept in total darkness but watered with sugar "
                "solution, and it survives for weeks. Explain how.",
        "options": [
            {"text": "Its chloroplasts can work on sugar when there is no "
                     "light to work on.", "correct": False,
             "why": "Chloroplasts need light and nothing else will do. The "
                    "sugar is used by the mitochondria instead."},
            {"text": "The sugar is turned back into light inside its "
                     "cells.", "correct": False,
             "why": "Nothing turns sugar into light. Sugar is food, and its "
                    "energy is released by respiration."},
            {"text": "Sugar keeps its vacuoles full, and a plant with full "
                     "vacuoles needs nothing else at all to stay alive.",
             "correct": False,
             "why": "Full vacuoles stop it wilting, but a plant needs energy "
                    "as well — released from that sugar in the "
                    "mitochondria."},
            {"text": "It cannot make food in the dark, but its mitochondria "
                     "can still release energy from the sugar it is given.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h16",
        "band": "harder",
        "text": "A chemical stops a cell membrane working while every other "
                "part is left untouched. Predict what happens to the cell.",
        "options": [
            {"text": "Substances move in and out freely, and the cell is "
                     "finished within minutes.", "correct": True},
            {"text": "It carries on as normal, because in a plant cell the "
                     "wall does exactly the same job anyway.", "correct": False,
             "why": "The wall lets everything through and chooses nothing. "
                    "No other part can take the membrane's place."},
            {"text": "It stops dividing, but is otherwise unharmed.",
             "correct": False,
             "why": "Dividing is what is lost when the nucleus goes. Losing "
                    "the membrane loses control of everything crossing."},
            {"text": "It goes limp, because sap can no longer press "
                     "outwards.", "correct": False,
             "why": "That is what a lost vacuole would do, and far more "
                    "slowly. Losing the membrane is immediate."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h17",
        "band": "harder",
        "text": "“The cell wall is a plant's skeleton.” Evaluate that "
                "statement.",
        "options": [
            {"text": "Completely right: the walls hold the whole plant up on "
                     "their own.", "correct": False,
             "why": "A stalk with every wall intact still flops once its "
                    "cells lose water. The push from inside does half the "
                    "work."},
            {"text": "Completely wrong: the wall is only there to keep "
                     "harmful things out.", "correct": False,
             "why": "The wall keeps nothing out — things pass straight "
                    "through it. It does hold each cell's shape."},
            {"text": "Partly right: the walls are stiff, but a plant only "
                     "stands up while its vacuoles are pressing out on "
                     "them.", "correct": True},
            {"text": "Completely wrong: a plant is held up by its "
                     "chloroplasts, which swell in the light and push "
                     "outwards.", "correct": False,
             "why": "Chloroplasts trap light and press on nothing. The "
                    "outward push comes from sap in the vacuoles."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h18",
        "band": "harder",
        "text": "A leaf is treated with a chemical that stops its "
                "mitochondria working, then left in bright sunlight. Predict "
                "what happens to its cells.",
        "options": [
            {"text": "Nothing at all, because a plant cell standing in the "
                     "light has no use for mitochondria.", "correct": False,
             "why": "Making food and releasing the energy from it are two "
                    "jobs. A plant cell needs both, light or no light."},
            {"text": "They die: they can still make food, but nothing can "
                     "release the energy from it.", "correct": True},
            {"text": "They burst, because the water that they take in is "
                     "no longer being used up by anything.", "correct": False,
             "why": "Bursting is about a missing wall. What is lost here is "
                    "the cell's energy supply."},
            {"text": "They lose their green colour as the chloroplasts shut "
                     "down.", "correct": False,
             "why": "The chlorophyll is not removed by this. What stops is "
                    "the release of energy from food."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h19",
        "band": "harder",
        "text": "A plant cell has six of its seven parts, but no vacuole at "
                "all. Predict what a plant made of such cells would look "
                "like.",
        "options": [
            {"text": "Bright green, and standing perfectly upright in the "
                     "full sunshine.", "correct": False,
             "why": "Nothing would be pressing out against the walls, so it "
                    "could not stand up — whatever colour it was."},
            {"text": "Burst wide open, because nothing at all is holding "
                     "the water inside.", "correct": False,
             "why": "Water is held in by the membrane, and the wall stops "
                    "the cell splitting. What a vacuole gives is the push."},
            {"text": "Completely colourless, because a plant keeps all of "
                     "its green in the vacuole.", "correct": False,
             "why": "The green is chlorophyll, inside the chloroplasts. A "
                    "cell with no vacuole would still be green."},
            {"text": "Limp and drooping, because nothing presses out against "
                     "the walls.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h20",
        "band": "harder",
        "text": "A student points at the single line round a cheek cell and "
                "calls it the cell membrane. Why is that not safe to say?",
        "options": [
            {"text": "Because a cheek cell has no membrane at all — only "
                     "plant cells have one.", "correct": False,
             "why": "Every cell here has a membrane. This one is simply far "
                    "too thin to see."},
            {"text": "Because that line is a cell wall, which a cheek cell "
                     "builds around itself once it dries out.",
             "correct": False,
             "why": "No animal cell has a wall, dried out or otherwise."},
            {"text": "Because a membrane is only a few molecules thick; that "
                     "line simply marks where the cell ends.",
             "correct": True},
            {"text": "Because a membrane can only be seen once methylene "
                     "blue has been added.", "correct": False,
             "why": "The stain picks out the nucleus. The membrane stays "
                    "invisible either way."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h21",
        "band": "harder",
        "text": "At night a plant makes no food at all. Explain how its "
                "cells still get the energy they need.",
        "options": [
            {"text": "Its mitochondria release energy from food it made and "
                     "stored during the day.", "correct": True},
            {"text": "Its chloroplasts work more slowly once it is dark, "
                     "but they never stop altogether.", "correct": False,
             "why": "Chloroplasts do nothing without light. The energy comes "
                    "from food that is already stored."},
            {"text": "It takes energy in through its roots overnight, "
                     "along with the water it draws up.", "correct": False,
             "why": "Roots take in water and dissolved minerals, not energy. "
                    "The energy comes from stored food."},
            {"text": "It stops needing energy of any kind until the sun "
                     "comes up again the next morning.", "correct": False,
             "why": "A living cell needs energy constantly, day and night. "
                    "Respiration never stops."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h22",
        "band": "harder",
        "text": "A plant cell wall is about 1 µm thick and a cell membrane "
                "about 0.01 µm. Calculate how many times thicker the wall "
                "is.",
        "options": [
            {"text": "10 times", "correct": False,
             "why": "That is one step of ten only. 1 ÷ 0.01 = 100."},
            {"text": "100 times", "correct": True},
            {"text": "1000 times", "correct": False,
             "why": "That is ten times too many. 1 ÷ 0.01 = 100."},
            {"text": "0.01 times", "correct": False,
             "why": "That divides the wrong way round. The wall is the "
                    "thicker of the two, by 100 times."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h23",
        "band": "harder",
        "text": "A student says plant cells and animal cells each have parts "
                "that the other does not. Evaluate that claim.",
        "options": [
            {"text": "Correct: an animal cell has mitochondria and a plant "
                     "cell does not.", "correct": False,
             "why": "Every plant cell has mitochondria. Nothing on this list "
                    "runs from animals to plants only."},
            {"text": "Correct: an animal cell has a nucleus while a plant "
                     "cell keeps its instructions loose.", "correct": False,
             "why": "Both have a nucleus. In a plant cell the vacuole pushes "
                    "it to one side, but it is there."},
            {"text": "Wrong: the two kinds of cell have exactly the same "
                     "parts as each other.", "correct": False,
             "why": "They do not. A plant cell adds a wall, a vacuole and "
                    "chloroplasts to the shared four."},
            {"text": "Wrong: the difference runs one way only — the plant "
                     "has three extras and the animal has none.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h24",
        "band": "harder",
        "text": "A student prepares a slide of plant tissue and can find no "
                "chloroplasts anywhere on it. Suggest a reason that involves "
                "no mistake on their part.",
        "options": [
            {"text": "The tissue came from a root or a bulb, where no light "
                     "reaches.", "correct": True},
            {"text": "The chloroplasts dissolved in the water used to mount "
                     "the slide.", "correct": False,
             "why": "Water does not dissolve them. The likelier answer is "
                    "that the tissue never had any."},
            {"text": "The magnification was too low, as chloroplasts need "
                     "×1000 before they show.", "correct": False,
             "why": "Chloroplasts are visible at ×400, green and unstained. "
                    "Not every plant cell has them."},
            {"text": "Plant cells only build chloroplasts once they are "
                     "under the microscope lamp.", "correct": False,
             "why": "They are built in cells that grow in the light, not "
                    "made to order under a lamp."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h25",
        "band": "harder",
        "text": "A leaf section is cut too thick, and down the microscope it "
                "looks like solid dark green with no cells visible at all. "
                "Suggest why.",
        "options": [
            {"text": "The chloroplasts have leaked out and coated the whole "
                     "slide.", "correct": False,
             "why": "Chloroplasts stay inside their cells. The trouble is "
                    "that there are too many layers to see through."},
            {"text": "The blade destroyed the cells right through the "
                     "section, leaving only their contents.",
             "correct": False,
             "why": "A blade damages the cut edge only. The rest of the "
                    "section is many cells deep."},
            {"text": "Several layers of cells lie on top of one another, so "
                     "no single cell can be picked out.", "correct": True},
            {"text": "The magnification is too high for a leaf, so only "
                     "colour comes through.", "correct": False,
             "why": "Leaf cells are looked at at ×400 routinely. The "
                    "thickness of the section is the problem here."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h26",
        "band": "harder",
        "text": "A wilted plant is watered. Put these four events into the "
                "order in which they happen.",
        "options": [
            {"text": "The leaves lift · the vacuoles fill · water enters "
                     "the cells · the walls are pushed out.",
             "correct": False,
             "why": "The leaves lift last of all. Nothing can happen until "
                    "water has entered the cells."},
            {"text": "Water enters the cells · the walls are pushed out · "
                     "the vacuoles fill · the leaves lift.", "correct": False,
             "why": "A wall is pushed out by a vacuole that has already "
                    "filled, so those two are the wrong way round."},
            {"text": "Water enters the cells · the vacuoles fill · the walls "
                     "are pushed out · the leaves lift.", "correct": True},
            {"text": "The vacuoles fill · water enters the cells · the "
                     "leaves lift · the walls are pushed out.",
             "correct": False,
             "why": "A vacuole can only fill once water has entered the "
                    "cell, so the first two are reversed."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h27",
        "band": "harder",
        "text": "One part is in every cell, plant or animal, is too small "
                "to be separated at ×400, and is the reason a muscle cell "
                "differs from a cheek cell. Name it.",
        "options": [
            {"text": "The mitochondria", "correct": True},
            {"text": "The cell membrane", "correct": False,
             "why": "It fits the first two clues, but every cell has much "
                    "the same membrane — it is not what sets a muscle cell "
                    "apart."},
            {"text": "The vacuole", "correct": False,
             "why": "A large permanent vacuole is a plant part, and it is "
                    "easy to see. Neither clue fits it."},
            {"text": "The nucleus", "correct": False,
             "why": "The nucleus is in both cells, but it is one of the "
                    "parts you can see, especially once stained."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h28",
        "band": "harder",
        "text": "A student says cells should be measured in millimetres, "
                "because that is what a ruler shows. Evaluate that.",
        "options": [
            {"text": "Right, because a micrometre is too small to be a real "
                     "unit.", "correct": False,
             "why": "A micrometre is a standard unit, a thousandth of a "
                    "millimetre, and cells are exactly the right size "
                    "for it."},
            {"text": "Right, because 1 mm and 1 µm are two names for the "
                     "same length.", "correct": False,
             "why": "They are not the same length. There are 1000 µm in a "
                    "millimetre."},
            {"text": "Wrong, because a typical cell is several millimetres "
                     "across and needs a bigger unit than that.",
             "correct": False,
             "why": "Cells are far smaller than a millimetre — around 50 µm "
                    "— which is why a smaller unit is used."},
            {"text": "Wrong: most cells are around 0.05 mm, so micrometres "
                     "give a whole number instead of a decimal.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h29",
        "band": "harder",
        "text": "Of a cheek cell's four parts, which would kill it fastest "
                "if it were taken away, and why?",
        "options": [
            {"text": "The nucleus, because the cell would have no "
                     "instructions left to follow.", "correct": False,
             "why": "Serious, but not immediate — the cell carries on until "
                    "it needs to build something or divide."},
            {"text": "The mitochondria, because everything would stop within "
                     "a few seconds.", "correct": False,
             "why": "Losing them is fatal, but not in seconds. The cell has "
                    "food in hand and does not empty out."},
            {"text": "The membrane, because everything would leak both ways "
                     "at once.", "correct": True},
            {"text": "The cytoplasm, because the other parts would fall out "
                     "of the cell.", "correct": False,
             "why": "Nothing falls out. Without cytoplasm it was never a "
                    "working cell, but the membrane is the fastest loss."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h30",
        "band": "harder",
        "text": "One student measures ten onion cells spanning 0.6 mm and "
                "divides by ten. Another measures a single cell and gets "
                "70 µm. Compare the two methods.",
        "options": [
            {"text": "The first is better: measuring ten and dividing "
                     "spreads any measuring error across all ten.",
             "correct": True},
            {"text": "The second is better, because one cell can be lined up "
                     "against the scale far more carefully.",
             "correct": False,
             "why": "A single careful measurement still carries the whole of "
                    "any error. Ten cells share it out."},
            {"text": "Neither is any use, because the two answers differ.",
             "correct": False,
             "why": "60 µm and 70 µm are close, and real cells vary. The "
                    "method using ten is the more reliable of the two."},
            {"text": "The first is better, because it proves every onion "
                     "cell is exactly 60 µm wide.", "correct": False,
             "why": "It gives a mean, not a guarantee. Cells vary, which is "
                    "precisely why a mean is taken."},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h31",
        "band": "harder",
        "text": "Put these four in order, from largest to smallest: a "
                "mitochondrion, a leaf cell, the thickness of a cell "
                "membrane, a chloroplast.",
        "options": [
            {"text": "Leaf cell · mitochondrion · chloroplast · membrane "
                     "thickness", "correct": False,
             "why": "A chloroplast is about five times wider than a "
                    "mitochondrion, so those two are the wrong way round."},
            {"text": "Chloroplast · leaf cell · mitochondrion · membrane "
                     "thickness", "correct": False,
             "why": "A leaf cell is about ten times wider than a chloroplast "
                    "and holds many of them, so the cell comes first."},
            {"text": "Leaf cell · chloroplast · membrane thickness · "
                     "mitochondrion", "correct": False,
             "why": "A membrane is a few molecules thick, thinner than "
                    "anything else on the list, so it comes last."},
            {"text": "Leaf cell · chloroplast · mitochondrion · membrane "
                     "thickness", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-03-h32",
        "band": "harder",
        "text": "A cheek cell divides to replace one that has been scraped "
                "away. Which part decides what the new cell will be like, "
                "and why?",
        "options": [
            {"text": "The cytoplasm, because that is where all of the new "
                     "cell's parts are actually assembled.", "correct": False,
             "why": "They are built there, but the cytoplasm holds no "
                    "instructions for what to build."},
            {"text": "The membrane, because it decides what the new cell "
                     "takes in.", "correct": False,
             "why": "It controls what crosses, moment by moment. It says "
                    "nothing about what the new cell will be."},
            {"text": "The mitochondria, because a cell cannot divide at all "
                     "without a steady supply of energy.", "correct": False,
             "why": "Energy is needed, but energy is not information. The "
                    "instructions come from somewhere else."},
            {"text": "The nucleus, because the DNA it holds is the "
                     "instructions the new cell is built from.",
             "correct": True},
        ],
        "figure": None,
    },
]
