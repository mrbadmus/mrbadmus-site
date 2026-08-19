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
]
