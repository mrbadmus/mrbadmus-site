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

    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-06-e05",
        "band": "easier",
        "text": "What does multicellular mean?",
        "options": [
            {"text": "Made of one cell that carries out all seven life "
                     "processes.", "correct": False,
             "why": "That is unicellular — one cell that is the whole "
                    "organism. Multicellular means many cells."},
            {"text": "Made of cells that are all exactly the same as each "
                     "other.", "correct": False,
             "why": "The cells of a multicellular organism are usually "
                    "specialised, so they differ. What the word means is that "
                    "there are many of them."},
            {"text": "Made of cells that could each survive alone if they "
                     "were separated.", "correct": False,
             "why": "Most of them could not. A cheek cell is fed, positioned "
                    "and supplied by the rest of you."},
            {"text": "Made of many cells, which are usually specialised for "
                     "different jobs.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e06",
        "band": "easier",
        "text": "What is a flagellum?",
        "options": [
            {"text": "A long whip that a cell beats in order to swim.",
             "correct": True},
            {"text": "A short hair, one of hundreds covering a cell's "
                     "surface.", "correct": False,
             "why": "Those are cilia, and they beat together like tiny oars. "
                    "A flagellum is a single long whip."},
            {"text": "A groove that sweeps food into the cell.",
             "correct": False,
             "why": "That is an oral groove, which is how a Paramecium feeds. "
                    "A flagellum is used for swimming."},
            {"text": "A vacuole that collects water and squeezes it out "
                     "again.", "correct": False,
             "why": "That is a contractile vacuole. A flagellum is the long "
                    "whip a cell beats to move itself along."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e07",
        "band": "easier",
        "text": "Which single-celled organism is green, makes its own food "
                "from light, and swims using one long whip?",
        "options": [
            {"text": "Amoeba", "correct": False,
             "why": "An Amoeba changes shape to move and engulfs other cells "
                    "for food. It is not green and it makes nothing."},
            {"text": "Paramecium", "correct": False,
             "why": "A Paramecium swims with hundreds of cilia and sweeps "
                    "food into an oral groove. The green one with a single "
                    "whip is Euglena."},
            {"text": "Euglena", "correct": True},
            {"text": "A bacterium", "correct": False,
             "why": "A bacterium has no nucleus and is not green. Euglena "
                    "is the one that makes its own food from light and swims "
                    "with a single whip."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e08",
        "band": "easier",
        "text": "Which one of these single cells is a whole organism rather "
                "than part of one?",
        "options": [
            {"text": "A red blood cell", "correct": False,
             "why": "It is one of your cells, made in your marrow and carried "
                    "round by your blood. Everything it needs is supplied to "
                    "it."},
            {"text": "An Amoeba", "correct": True},
            {"text": "A sperm cell", "correct": False,
             "why": "It carries half a set of chromosomes and never feeds — "
                    "both signs that something larger made it and stocked "
                    "it."},
            {"text": "A cheek cell", "correct": False,
             "why": "It lines your mouth, is held in place by the cells "
                    "around it and is fed by your blood. It does one job "
                    "while the rest of you does the others."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-06-s05",
        "band": "standard",
        "text": "A single cell flows around a smaller cell and takes it "
                "inside itself. Does that settle whether it is a whole "
                "organism?",
        "options": [
            {"text": "Yes — anything that hunts and eats another cell must be "
                     "an organism.", "correct": False,
             "why": "A white blood cell does exactly that inside you, and it "
                    "is part of an organism. Behaviour is the least reliable "
                    "evidence there is."},
            {"text": "Yes — no cell inside a body ever engulfs anything.",
             "correct": False,
             "why": "Your white blood cells engulf bacteria in precisely this "
                    "way. That is why engulfing settles nothing."},
            {"text": "No — it is far too small a thing for anyone to watch "
                     "and judge.", "correct": False,
             "why": "It can be watched under a microscope. The reason it "
                    "settles nothing is that cells inside a body do it too."},
            {"text": "No — a white blood cell engulfs bacteria the same way, "
                     "and it is part of you.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s06",
        "band": "standard",
        "text": "A single cell in a rain barrel is green, has mitochondria, "
                "is 0.05 mm long and can swim. Which of those facts settles "
                "that it is a whole organism?",
        "options": [
            {"text": "That it can swim under its own power.",
             "correct": False,
             "why": "A sperm cell swims and a white blood cell crawls through "
                    "tissue. Moving under your own power tells you nothing."},
            {"text": "That it is green, and so makes its own food.",
             "correct": True},
            {"text": "That it has mitochondria inside it.",
             "correct": False,
             "why": "A Paramecium has mitochondria, and so does your cheek "
                    "cell. A fact that is true of everything separates "
                    "nothing."},
            {"text": "That it is only 0.05 mm long.", "correct": False,
             "why": "Size never settles it. Your cheek cell is 0.06 mm and a "
                    "Paramecium is 0.25 mm, and the larger of those is the "
                    "organism."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s07",
        "band": "standard",
        "text": "A Paramecium is 0.25 mm long and one of your cheek cells is "
                "0.06 mm. A student says the larger one must be the organism. "
                "What is wrong with that?",
        "options": [
            {"text": "Nothing — a whole organism does have to be larger than "
                     "one of its own cells.", "correct": False,
             "why": "An organism made of one cell is exactly the size of that "
                    "cell. Euglena is smaller than your cheek cell and is a "
                    "whole organism."},
            {"text": "The Paramecium is not really larger; it only looks it "
                     "because it sits nearer the lens.", "correct": False,
             "why": "It genuinely is four times longer. The mistake is "
                    "treating size as evidence at all."},
            {"text": "Size never settles it — Euglena is smaller than a cheek "
                     "cell and is still an organism.", "correct": True},
            {"text": "Cheek cells are the largest cells you have, so the "
                     "comparison was unfair.", "correct": False,
             "why": "A nerve cell can be a metre long. The reasoning fails "
                    "whichever pair of cells you pick, because size does not "
                    "decide this."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s08",
        "band": "standard",
        "text": "A student says a unicellular organism must be a simpler cell "
                "than one of yours, since it is only one cell. What is wrong "
                "with that?",
        "options": [
            {"text": "It is the other way round: it does all seven itself, "
                     "so it needs structures your cells do not.",
             "correct": True},
            {"text": "Nothing is wrong — a single cell does have fewer parts "
                     "than a cell working inside a body.", "correct": False,
             "why": "A Paramecium has cilia, an oral groove and a contractile "
                    "vacuole on top of the parts your cells have. It is doing "
                    "more, not less."},
            {"text": "It is simpler, but only because it is smaller than one "
                     "of your cells.", "correct": False,
             "why": "A Paramecium is four times longer than a cheek cell. And "
                    "size does not decide how much a cell has to do for "
                    "itself."},
            {"text": "They are equally complex, because both are built from "
                     "the same seven parts.", "correct": False,
             "why": "The seven parts are not the whole story. A cell that "
                    "feeds, moves and manages its own water needs structures "
                    "a cheek cell never builds."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-06-h05",
        "band": "harder",
        "text": "One bacterium divides into two every twenty minutes, and "
                "every new cell divides at the same rate. Starting from a "
                "single bacterium, how many are there after two hours?",
        "options": [
            {"text": "6, because there are six divisions in two hours.",
             "correct": False,
             "why": "Six is the number of divisions, not the number of cells. "
                    "Each division doubles the whole population."},
            {"text": "12, because six divisions each make two cells.",
             "correct": False,
             "why": "Six twos added together is 12; the number doubles "
                    "instead. One becomes 2, 4, 8, 16, 32, 64."},
            {"text": "64, because the number doubles six times.",
             "correct": True},
            {"text": "128, because the number doubles seven times.",
             "correct": False,
             "why": "Two hours is 120 minutes, and 120 ÷ 20 = 6 divisions, "
                    "not seven. Six doublings give 64."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h06",
        "band": "harder",
        "text": "A cell is found held in a sheet with thousands of identical "
                "cells beside it, all sweeping their cilia the same way. "
                "Organism, or part of one?",
        "options": [
            {"text": "An organism, because it is moving under its own "
                     "power.", "correct": False,
             "why": "Movement is the most misleading evidence there is. A "
                    "sperm cell swims and a Paramecium swims, and only one of "
                    "them is an organism."},
            {"text": "Part of one — it does a single job while something else "
                     "feeds it and holds it in place.", "correct": True},
            {"text": "An organism, because thousands of identical cells means "
                     "thousands of identical organisms.", "correct": False,
             "why": "Being held in a sheet of identical neighbours is what a "
                    "tissue looks like. Each of these cells does one job for "
                    "something larger."},
            {"text": "Part of one, because any cell that is covered in cilia "
                     "is always part of a larger organism.", "correct": False,
             "why": "A Paramecium is covered in cilia and is a complete "
                    "organism. What settles this case is that the cell does "
                    "one job and is supplied by something else."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h07",
        "band": "harder",
        "text": "A Paramecium in pond water has a vacuole that keeps filling "
                "with water and squeezing it out, and so does an Amoeba. No "
                "cell in your body has one. What does that tell you?",
        "options": [
            {"text": "That your own cells are watertight in a way a pond "
                     "organism's cells simply are not.", "correct": False,
             "why": "Water crosses your cell membranes constantly. The "
                    "difference is that the fluid around your cells is held "
                    "steady, so nothing builds up."},
            {"text": "That pond organisms are more advanced, because they "
                     "control their own water.", "correct": False,
             "why": "It is not a ranking. It is a job your body does for your "
                    "cells and a free-living cell has to do for itself."},
            {"text": "That a contractile vacuole is what makes something a "
                     "unicellular organism.", "correct": False,
             "why": "A bacterium has none and is a complete organism. The "
                    "vacuole is one answer to living in fresh water, not a "
                    "definition."},
            {"text": "That a free-living cell manages its own water, while "
                     "your body does that job for your cells.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h08",
        "band": "harder",
        "text": "A bacterium is about 0.002 mm long and a Paramecium about "
                "0.25 mm. How many times longer is the Paramecium?",
        "options": [
            {"text": "125 times, because 0.25 ÷ 0.002 = 125.",
             "correct": True},
            {"text": "0.248 times, because 0.25 − 0.002 = 0.248.",
             "correct": False,
             "why": "Subtracting gives the difference in length in "
                    "millimetres, not how many times longer. For “how many "
                    "times”, divide."},
            {"text": "12.5 times, because 0.25 ÷ 0.02 = 12.5.",
             "correct": False,
             "why": "There is a zero missing from the divisor. The bacterium "
                    "is 0.002 mm, so it is 0.25 ÷ 0.002 = 125."},
            {"text": "1250 times, because 0.25 ÷ 0.0002 = 1250.",
             "correct": False,
             "why": "That is one zero too many. 0.002 mm is two thousandths "
                    "of a millimetre, and 0.25 ÷ 0.002 = 125."},
        ],
        "figure": None,
    },
]
