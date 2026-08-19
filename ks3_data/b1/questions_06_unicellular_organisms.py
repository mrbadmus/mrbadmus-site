"""B1 lesson 06 — Unicellular organisms: twelve questions (MRB-269).

These probe the one thing the lesson exists to teach: which facts about a
single cell discriminate between a whole organism and a part of one, and which
vivid facts settle nothing. The distractors are built from the lesson's three
declared misconceptions — LIFE-03 (a single cell must be part of something
bigger), CELL-13 (no nucleus means no instructions, so a bacterium cannot
divide) and CELL-08 (a unicellular organism is just a simpler version of one of
our cells) — plus the two habits of reasoning the settles-it activity is aimed
at: treating movement as evidence, and treating size as evidence. The lesson
carries no figures, so every question is figure=None.
"""

UNIT = "B1"
LESSON = "unicellular-organisms"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-06-e01",
        "band": "easier",
        "text": "A pond sample is described as full of unicellular organisms. "
                "What does unicellular tell you about them?",
        "options": [
            {"text": "Each one is a single cell that is itself the whole "
                     "organism.",
             "correct": True},
            {"text": "Each one is a single cell taken from a larger living "
                     "thing.",
             "correct": False,
             "why": "This is the idea the lesson exists to break. A single "
                    "cell can be a whole living thing — a bacterium, an "
                    "amoeba and a Euglena are each an entire organism, not a "
                    "piece of one."},
            {"text": "Each one is built from cells that are all of one single "
                     "type.",
             "correct": False,
             "why": "That describes a sheet of identical cells inside a "
                    "multicellular body, like your cheek lining. Unicellular "
                    "counts the cells — one — not the number of types."},
            {"text": "Each one is far too small to be seen without a "
                     "microscope.",
             "correct": False,
             "why": "Size is not what the word means. A Paramecium is 0.25 mm "
                    "and your cheek cell is 0.06 mm, so the organism here is "
                    "the bigger one."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e02",
        "band": "easier",
        "text": "A cell's surface is covered in short hairs that beat "
                "together like tiny oars. What are they called?",
        "options": [
            {"text": "Flagella",
             "correct": False,
             "why": "A flagellum is one long whip, not a covering of short "
                    "hairs. You have already met one: the tail of a sperm "
                    "cell."},
            {"text": "Oral grooves",
             "correct": False,
             "why": "The oral groove is the channel food is swept into. It is "
                    "what the hairs sweep towards, not the hairs themselves."},
            {"text": "Cilia",
             "correct": True},
            {"text": "Contractile vacuoles",
             "correct": False,
             "why": "Those sit inside the cell, collecting the water that "
                    "keeps seeping in and squeezing it back out. They are not "
                    "on the surface."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e03",
        "band": "easier",
        "text": "In the side-by-side comparison, how does a Paramecium get "
                "its food?",
        "options": [
            {"text": "Glucose arrives dissolved in the blood, already "
                     "digested for it.",
             "correct": False,
             "why": "That is the cheek cell's side of the table. Nothing "
                    "delivers food to a Paramecium — it has to go and find "
                    "it."},
            {"text": "It sweeps food into an oral groove and digests it "
                     "inside itself.",
             "correct": True},
            {"text": "It is green, so it makes all its own food out of light.",
             "correct": False,
             "why": "That is Euglena, the green one. A Paramecium cannot make "
                    "food from light and has to hunt for it."},
            {"text": "It absorbs digested food straight through its cilia "
                     "while it swims.",
             "correct": False,
             "why": "Cilia beat to swim, and to sweep food towards the oral "
                    "groove. Absorbing food is not what they do."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e04",
        "band": "easier",
        "text": "At the bench, at which total magnification does the pond "
                "slide first show structures — cilia, an eyespot, a vacuole "
                "filling and emptying?",
        "options": [
            {"text": "×40",
             "correct": False,
             "why": "At ×40 you get specks and one or two shapes. You can see "
                    "that something in there is alive; you cannot see what it "
                    "is."},
            {"text": "×100",
             "correct": False,
             "why": "×100 gives you outlines. You can tell one kind from "
                    "another by shape and by how it moves, but the insides "
                    "are still a blur."},
            {"text": "×400",
             "correct": True},
            {"text": "You never can with a school microscope",
             "correct": False,
             "why": "You can, at ×400 — that is what the bench shows you. "
                    "What a school microscope cannot resolve is a bacterium, "
                    "which stays a dot at every setting."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-06-s01",
        "band": "standard",
        "text": "On the pond slide at ×400 the paramecia show their cilia "
                "clearly, but the bacteria are still only dots. Why?",
        "options": [
            {"text": "The bacteria lie at a different depth, so they are out "
                     "of focus.",
             "correct": False,
             "why": "Racking the focus does bring a different depth sharp — "
                    "and even perfectly in focus a 0.002 mm dot is still a "
                    "dot. Depth is not the limit here."},
            {"text": "The bacteria are swimming too fast for the microscope "
                     "to show them.",
             "correct": False,
             "why": "On this mount the organisms are held still for you and "
                    "the slide is what moves. Speed is not what is hiding "
                    "them."},
            {"text": "Bacteria have no structures inside them at all, because "
                     "they are not really organisms.",
             "correct": False,
             "why": "A bacterium is a whole organism, doing all seven life "
                    "processes for itself. It is small, not empty."},
            {"text": "A bacterium is 0.002 mm long and a Paramecium 0.25 mm — "
                     "too small even at ×400.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s02",
        "band": "standard",
        "text": "A student says: “this mystery cell swims with a long "
                "tail, so it must be a unicellular organism.” What is "
                "wrong with that reasoning?",
        "options": [
            {"text": "Swimming settles nothing — a sperm cell has a tail and "
                     "is part of a body.",
             "correct": True},
            {"text": "Nothing is wrong — moving about on its own is exactly "
                     "what makes a cell an organism.",
             "correct": False,
             "why": "Moving on your own is the most misleading fact in this "
                    "lesson. A white blood cell crawls through tissue, and it "
                    "is a part of you."},
            {"text": "Unicellular organisms never have tails; they all swim "
                     "using cilia instead.",
             "correct": False,
             "why": "Euglena is a whole organism and swims with one long "
                    "flagellum, exactly as a sperm cell does. The whip is not "
                    "the giveaway either way."},
            {"text": "A tail is only ever found on a cell that is part of a "
                     "larger organism.",
             "correct": False,
             "why": "That is the same mistake turned around. Euglena has a "
                    "flagellum and is nobody's part, so the tail decides "
                    "nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s03",
        "band": "standard",
        "text": "A cell has no nucleus, so a student decides its "
                "instructions must be gone. Then they see a loose loop of DNA "
                "in its cytoplasm. What does that show?",
        "options": [
            {"text": "The DNA is leaking out of a nucleus that has broken "
                     "open.",
             "correct": False,
             "why": "There was never a nucleus for it to leak from. This "
                    "cell's DNA has always sat loose in the cytoplasm, with "
                    "no membrane around it."},
            {"text": "The instructions are there and only the container is "
                     "missing, so it can divide.",
             "correct": True},
            {"text": "The cell must be a red blood cell, since that has no "
                     "nucleus either.",
             "correct": False,
             "why": "A red blood cell had a nucleus and destroyed it, and the "
                    "DNA went with it. There would be no loop left to find."},
            {"text": "DNA sitting outside a nucleus can never be read, so this "
                     "cell must already be dead.",
             "correct": False,
             "why": "A bacterium reads that loop every twenty minutes when it "
                    "divides. A membrane around DNA is not what makes it "
                    "work."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s04",
        "band": "standard",
        "text": "A Paramecium has a vacuole that keeps filling with water and "
                "squeezing it back out. Your cheek cell has nothing like it. "
                "Why not?",
        "options": [
            {"text": "A cheek cell is smaller, so far less water seeps into "
                     "it.",
             "correct": False,
             "why": "Size is not the reason, and this lesson never lets size "
                    "settle anything. What differs is what surrounds the "
                    "cell."},
            {"text": "Cheek cells make no waste of any kind, so they have "
                     "nothing at all to get rid of.",
             "correct": False,
             "why": "They do make waste — it passes into the blood and your "
                    "kidneys deal with it. What a cheek cell does not need is "
                    "its own water pump."},
            {"text": "Your kidneys pump the water straight back out of each "
                     "cheek cell.",
             "correct": False,
             "why": "Kidneys work on waste that has already passed into the "
                    "blood. Nothing reaches inside a cell to empty it."},
            {"text": "Your body holds the fluid around that cell steady, so "
                     "it never has to bail out.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-06-h01",
        "band": "harder",
        "text": "Euglena is green and makes food from light, and it also "
                "swims after food and can feed like an animal in the dark. "
                "Biologists argued for a century over which kingdom it "
                "belonged in. What did they settle on?",
        "options": [
            {"text": "It is a plant, because making its own food from light "
                     "is the stronger clue.",
             "correct": False,
             "why": "Euglena also hunts and feeds like an animal. Choosing "
                    "whichever clue you prefer is not classifying — it is "
                    "ignoring half the evidence."},
            {"text": "It is part plant and part animal, so it belongs half in "
                     "each of the two kingdoms.",
             "correct": False,
             "why": "It is one whole organism, not two halves stuck together. "
                    "The trouble is with the two boxes, not with the cell."},
            {"text": "The question was wrong — single-celled life does not "
                     "sort into plant or animal.",
             "correct": True},
            {"text": "It switches from plant to animal depending on how much "
                     "light there is.",
             "correct": False,
             "why": "It holds both abilities all the time and uses whichever "
                    "the conditions allow. Nothing about what it is changes "
                    "in the dark."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h02",
        "band": "harder",
        "text": "Cilia beat on a Paramecium, and cilia also beat on the cells "
                "lining your airways. What do they achieve in each case?",
        "options": [
            {"text": "In both cases they move the cell itself — airway cells "
                     "crawl up towards your throat.",
             "correct": False,
             "why": "An airway cell is held in a sheet by the cells around "
                    "it and does not move. What travels is the mucus and dust "
                    "over its surface."},
            {"text": "They move the whole Paramecium; in your airways they "
                     "move dust past still cells.",
             "correct": True},
            {"text": "Airway cilia sense dust rather than move it; only a "
                     "Paramecium's cilia move anything.",
             "correct": False,
             "why": "Sensing is done for the whole of you by nerve cells. "
                    "Airway cilia sweep dust back up out of your lungs — that "
                    "is work, not sensing."},
            {"text": "A Paramecium's are really flagella, since they are what "
                     "moves the whole cell along.",
             "correct": False,
             "why": "A flagellum is one long whip; a Paramecium beats "
                    "hundreds of short cilia. What they move does not change "
                    "what they are called."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h03",
        "band": "harder",
        "text": "A single cell divides in two. In one case there are now two "
                "organisms; in the other there is still only one organism. "
                "What decides which has happened?",
        "options": [
            {"text": "Whether the two new cells drift apart afterwards or stay "
                     "stuck together in a clump.",
             "correct": False,
             "why": "Sticking together is not the test. Ask instead whether "
                    "each new cell feeds, senses and excretes for itself, or "
                    "is fed and positioned by something larger."},
            {"text": "Whether the cell had a nucleus before it divided.",
             "correct": False,
             "why": "A bacterium has no nucleus and dividing makes two "
                    "organisms; a cheek cell has one and dividing still "
                    "leaves only one of you."},
            {"text": "Whether the new cells are as big as the cell they came "
                     "from.",
             "correct": False,
             "why": "Size never settles anything here. A 0.002 mm bacterium "
                    "is a whole organism and a 0.06 mm cheek cell is part of "
                    "one."},
            {"text": "Whether each new cell does all seven life processes for "
                     "itself, or just one job.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h04",
        "band": "harder",
        "text": "A unicellular organism's adaptations do for it what a whole "
                "organ system does for one of your cells. Which pairing "
                "follows that idea correctly?",
        "options": [
            {"text": "An oral groove and food vacuole do what your digestive "
                     "system does for a cheek cell.",
             "correct": True},
            {"text": "Mitochondria do for a Paramecium what your lungs and "
                     "blood together do for a cheek cell.",
             "correct": False,
             "why": "Both cells have their own mitochondria — that is a "
                    "shared feature, not an adaptation. What your body "
                    "supplies to a cheek cell is the oxygen, delivered by "
                    "blood."},
            {"text": "Beating cilia do for a Paramecium what your nerve cells "
                     "do for a cheek cell.",
             "correct": False,
             "why": "Cilia move the organism, so what they stand in for is "
                    "whatever moves you. Nerve cells are what sense for the "
                    "whole of you instead."},
            {"text": "A contractile vacuole does for a Paramecium what your "
                     "skin does for a cheek cell.",
             "correct": False,
             "why": "The vacuole bails out water. What matches it in you is "
                    "your blood and kidneys, holding the fluid around your "
                    "cells steady."},
        ],
        "figure": None,
    },
]
