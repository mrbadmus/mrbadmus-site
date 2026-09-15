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
            {"text": "Yes — anything that hunts down another cell and "
                     "swallows it whole must be an organism in its own "
                     "right.", "correct": False,
             "why": "A white blood cell does exactly that inside you, and it "
                    "is part of an organism. Behaviour is the least reliable "
                    "evidence there is."},
            {"text": "Yes — no cell inside a body ever engulfs anything.",
             "correct": False,
             "why": "Your white blood cells engulf bacteria in precisely this "
                    "way. That is why engulfing settles nothing."},
            {"text": "No — it is far too small a thing for anyone to watch "
                     "it closely enough to judge what it "
                     "is.", "correct": False,
             "why": "It can be watched under a microscope. The reason it "
                    "settles nothing is that cells inside a body do it too."},
            {"text": "No — a white blood cell engulfs bacteria the same way "
                     "and is part of you.", "correct": True},
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
            {"text": "That your own cells are completely watertight in a way "
                     "that the cells of a pond organism simply are "
                     "not.", "correct": False,
             "why": "Water crosses your cell membranes constantly. The "
                    "difference is that the fluid around your cells is held "
                    "steady, so nothing builds up."},
            {"text": "That pond organisms are more advanced at controlling "
                     "their water.", "correct": False,
             "why": "It is not a ranking. It is a job your body does for "
                    "your cells and a free-living cell has to do for itself."},
            {"text": "That having a contractile vacuole is what makes a "
                     "single cell a whole unicellular "
                     "organism.", "correct": False,
             "why": "A bacterium has none and is a complete organism. The "
                    "vacuole is one answer to living in fresh water, not a "
                    "definition."},
            {"text": "That a free-living cell manages its own water, while "
                     "your body does it for you.", "correct": True},
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

    # ── MRB-338 night 3 top-up ──────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-06-e09",
        "band": "easier",
        "text": "A Paramecium beats hundreds of cilia at once. What does that "
                "let it do?",
        "options": [
            {"text": "Digest its food, by breaking it down inside itself.",
             "correct": False,
             "why": "Digesting happens inside a vacuole once the food is in. "
                    "Cilia work on the outside of the cell."},
            {"text": "Squeeze out the water that keeps seeping in through "
                     "its surface.",
             "correct": False,
             "why": "That is the contractile vacuole's job, and it works "
                    "inside the cell rather than on its surface."},
            {"text": "Swim, and reverse when it runs into something.",
             "correct": True},
            {"text": "Stick itself to the slide so that it stays still.",
             "correct": False,
             "why": "Cilia beat, which drives the organism along. Nothing "
                    "about them anchors it to anything."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e10",
        "band": "easier",
        "text": "A Paramecium in pond water has a vacuole that fills up and "
                "empties again, over and over. What is that vacuole doing?",
        "options": [
            {"text": "Collecting the water that keeps seeping in and "
                     "squeezing it back out.",
             "correct": True},
            {"text": "Storing food until the cell has time to digest it "
                     "properly.",
             "correct": False,
             "why": "A food vacuole does that, and it forms around food swept "
                    "in through the oral groove. This one fills with water."},
            {"text": "Holding air so the cell floats near the surface.",
             "correct": False,
             "why": "Nothing on this slide carries air about. The vacuole "
                    "fills with water and then empties that water out."},
            {"text": "Pushing on the cilia from the inside to drive the cell "
                     "forward.",
             "correct": False,
             "why": "The cilia beat under their own power. Filling and "
                    "emptying the vacuole moves the organism nowhere."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e11",
        "band": "easier",
        "text": "A Paramecium sweeps food along a channel in its surface and "
                "digests it once it is inside. What is that channel called?",
        "options": [
            {"text": "A flagellum.",
             "correct": False,
             "why": "A flagellum is one long whip that a cell beats to swim "
                    "with. No food travels along it."},
            {"text": "A cilium.",
             "correct": False,
             "why": "One cilium is a single short hair on the surface. "
                    "Hundreds of them sweep the food along, but the channel "
                    "they sweep it into has its own name."},
            {"text": "A contractile vacuole.",
             "correct": False,
             "why": "That is the sac inside the cell that bails out water. "
                    "Food comes in by a different route."},
            {"text": "An oral groove.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e12",
        "band": "easier",
        "text": "A bacterium has no nucleus. So where does it keep its DNA?",
        "options": [
            {"text": "Loose in the cytoplasm, in a single loop with no "
                     "membrane round it.",
             "correct": True},
            {"text": "Nowhere, because a cell without a nucleus carries no "
                     "DNA whatsoever.",
             "correct": False,
             "why": "Then it could never copy itself, and a bacterium divides "
                    "about every twenty minutes. Its DNA is present."},
            {"text": "Inside the cell wall, which is where a bacterium stores "
                     "its instructions.",
             "correct": False,
             "why": "A wall is a barrier around the outside and stores "
                    "nothing. The DNA sits in the cytoplasm."},
            {"text": "Inside its mitochondria, which do the nucleus's job "
                     "instead.",
             "correct": False,
             "why": "Mitochondria release energy from food. Nothing in a "
                    "bacterium stands in for a nucleus."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e13",
        "band": "easier",
        "text": "What makes a single cell count as a whole organism rather "
                "than part of one?",
        "options": [
            {"text": "It is larger than the cells working inside a body.",
             "correct": False,
             "why": "Size never settles it. A bacterium is smaller than any "
                    "cell of yours and is a whole organism."},
            {"text": "It carries out all seven life processes for itself.",
             "correct": True},
            {"text": "It can move about under its own power.",
             "correct": False,
             "why": "A sperm cell swims and a white blood cell crawls. Both "
                    "of them are parts of a body."},
            {"text": "It has no nucleus inside it.",
             "correct": False,
             "why": "A bacterium has none and is an organism; a red blood "
                    "cell has none and is part of you."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e14",
        "band": "easier",
        "text": "An Amoeba has no cilia and no flagellum. How does it get "
                "about?",
        "options": [
            {"text": "It beats hundreds of short hairs, like a bank of tiny "
                     "oars.",
             "correct": False,
             "why": "Those are cilia, and an Amoeba has none. That is how a "
                    "Paramecium swims."},
            {"text": "It is carried by the currents.",
             "correct": False,
             "why": "It travels under its own power, flowing to wherever it "
                    "is going."},
            {"text": "It changes shape, flowing along as it goes.",
             "correct": True},
            {"text": "It squirts water out behind it and is pushed forwards.",
             "correct": False,
             "why": "Nothing on this slide swims by squirting. Emptying a "
                    "vacuole of water drives the cell nowhere."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e15",
        "band": "easier",
        "text": "An Amoeba comes across a smaller cell in the pond water. How "
                "does it feed on it?",
        "options": [
            {"text": "It sweeps the cell into an oral groove with its cilia.",
             "correct": False,
             "why": "That is how a Paramecium feeds. An Amoeba has no cilia "
                    "and no oral groove."},
            {"text": "It makes its own food from light and leaves it alone.",
             "correct": False,
             "why": "Making food from light is what a Euglena does. An Amoeba "
                    "is not green and cannot do it."},
            {"text": "It anchors itself to the smaller cell and drinks it "
                     "dry.",
             "correct": False,
             "why": "It does not attach to its food. The whole cell is taken "
                    "inside before anything is digested."},
            {"text": "It flows around the smaller cell until that cell is "
                     "inside it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e16",
        "band": "easier",
        "text": "A Euglena is green and traps the light falling on the pond. "
                "What does it use that light for?",
        "options": [
            {"text": "Warming itself, so that it can swim faster in the cold "
                     "water of a pond.",
             "correct": False,
             "why": "Nothing on the slide heats itself with light. The "
                    "trapped light is spent on food instead."},
            {"text": "Making its own food, so that nothing has to feed it.",
             "correct": True},
            {"text": "Beating its flagellum, which will not work in the "
                     "dark.",
             "correct": False,
             "why": "The cell beats its own flagellum, in the dark as readily "
                    "as in the light."},
            {"text": "Killing the bacteria around it before it eats them.",
             "correct": False,
             "why": "Light kills nothing here. A Euglena that is making food "
                    "from light has no need to hunt at all."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e17",
        "band": "easier",
        "text": "How many of the seven life processes does a single "
                "Paramecium carry out for itself?",
        "options": [
            {"text": "All seven.",
             "correct": True},
            {"text": "Six — everything except reproduction.",
             "correct": False,
             "why": "It splits in two and then there are two organisms, so "
                    "reproduction is one of the ones it does."},
            {"text": "Two of the seven.",
             "correct": False,
             "why": "Two would leave five of them being done by something "
                    "else, and there is nothing else to do them."},
            {"text": "One, like any other single cell.",
             "correct": False,
             "why": "One job each is what the cells inside a body do. A "
                    "Paramecium has nobody to do the rest for it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e18",
        "band": "easier",
        "text": "One of your cheek cells stays exactly where it is. What "
                "holds it there?",
        "options": [
            {"text": "Its own cilia, which grip the surface underneath it.",
             "correct": False,
             "why": "A cheek cell has no cilia, and cilia beat rather than "
                    "grip."},
            {"text": "The blood, which presses it against the cells on either "
                     "side of it.",
             "correct": False,
             "why": "Blood delivers glucose and oxygen and carries waste "
                    "away. It holds nothing in position."},
            {"text": "The cells around it, which hold it in a sheet.",
             "correct": True},
            {"text": "A wall around the outside, as a plant cell has.",
             "correct": False,
             "why": "Animal cells have no wall. What keeps a cheek cell in "
                    "place is its neighbours."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e19",
        "band": "easier",
        "text": "One of your cheek cells respires using its own "
                "mitochondria. How does the oxygen get to it?",
        "options": [
            {"text": "It swims up to the surface of your mouth and collects "
                     "some.",
             "correct": False,
             "why": "A cheek cell does not move at all. It is held in a sheet "
                    "by the cells around it."},
            {"text": "Your blood brings it, already dissolved; the cell never "
                     "fetches any.",
             "correct": True},
            {"text": "It takes it from the water around it, as a pond "
                     "organism does.",
             "correct": False,
             "why": "The only fluid around it is the one your body holds "
                    "steady, and the oxygen in that arrived by blood."},
            {"text": "Its mitochondria make their own oxygen out of glucose.",
             "correct": False,
             "why": "Mitochondria use oxygen to release energy from glucose. "
                    "They do not produce any."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e20",
        "band": "easier",
        "text": "A cheek cell does not grow. What happens to it once it has "
                "worn out?",
        "options": [
            {"text": "It stays put and slowly gets bigger, as you get "
                     "bigger.",
             "correct": False,
             "why": "You grow by making more cells, not by swelling the ones "
                    "you already have."},
            {"text": "It floats off into your blood and is used again "
                     "somewhere else.",
             "correct": False,
             "why": "A worn-out cheek cell is not shipped anywhere to be "
                    "reused. Another cell takes its place."},
            {"text": "It simply repairs itself.",
             "correct": False,
             "why": "The lining of your mouth is replaced constantly. No "
                    "cheek cell lasts a lifetime."},
            {"text": "It is replaced by another cell.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e21",
        "band": "easier",
        "text": "Pond water is not sterile. Which precaution does that make "
                "necessary in the laboratory?",
        "options": [
            {"text": "Keeping it away from your mouth and any cuts, and "
                     "washing your hands afterwards.",
             "correct": True},
            {"text": "Boiling every sample before you put it on a slide.",
             "correct": False,
             "why": "Boiling would kill the organisms you collected the water "
                    "in order to look at."},
            {"text": "Working with the laboratory lights switched off.",
             "correct": False,
             "why": "How bright the room is has nothing to do with what is "
                    "living in the water."},
            {"text": "Using a glass slide rather than a plastic one.",
             "correct": False,
             "why": "What the slide is made of changes nothing about what the "
                    "water is carrying."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e22",
        "band": "easier",
        "text": "A Paramecium squeezes water back out of its vacuole. Which "
                "of the seven life processes is that?",
        "options": [
            {"text": "Growth.",
             "correct": False,
             "why": "Growth is getting bigger, which this cell does until "
                    "it is ready to divide."},
            {"text": "Respiration.",
             "correct": False,
             "why": "Respiration is releasing energy from food, and the "
                    "mitochondria do it."},
            {"text": "Excretion.",
             "correct": True},
            {"text": "Sensitivity.",
             "correct": False,
             "why": "Sensitivity is noticing something and responding, as the "
                    "cell does when it meets an obstacle."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e23",
        "band": "easier",
        "text": "A Paramecium splits in two. What is the result?",
        "options": [
            {"text": "One organism that is now twice the size it was.",
             "correct": False,
             "why": "Splitting makes two smaller cells. It never leaves one "
                    "larger one behind."},
            {"text": "Two organisms, each one complete.",
             "correct": True},
            {"text": "One organism made of two cells joined together.",
             "correct": False,
             "why": "The two come apart and live separately. A Paramecium is "
                    "one cell and stays one cell."},
            {"text": "Two halves, both of which soon starve where they lie.",
             "correct": False,
             "why": "Each one carries out all seven life processes from the "
                    "moment they separate."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e24",
        "band": "easier",
        "text": "In warm conditions, how often does a bacterium divide?",
        "options": [
            {"text": "About once a week, after it has grown enough.",
             "correct": False,
             "why": "That is far too slow. A warm bacterium is dividing "
                    "before a lesson is over."},
            {"text": "Only once in its whole life.",
             "correct": False,
             "why": "Each new bacterium divides again, and the ones it makes "
                    "divide as well."},
            {"text": "About once a day.",
             "correct": False,
             "why": "A single warm day would then produce two bacteria. It "
                    "produces a good deal more than that."},
            {"text": "About every twenty minutes.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e25",
        "band": "easier",
        "text": "Put these four in order of length, smallest first: a "
                "bacterium, a cheek cell, a Euglena, a Paramecium.",
        "options": [
            {"text": "Bacterium, Euglena, cheek cell, Paramecium.",
             "correct": True},
            {"text": "Bacterium, cheek cell, Euglena, Paramecium.",
             "correct": False,
             "why": "A Euglena is 0.05 mm and a cheek cell 0.06 mm, so the "
                    "Euglena comes first of those two."},
            {"text": "Euglena, bacterium, cheek cell, Paramecium.",
             "correct": False,
             "why": "A bacterium is 0.002 mm, which is the smallest of the "
                    "four by a long way."},
            {"text": "Paramecium, cheek cell, Euglena, bacterium.",
             "correct": False,
             "why": "That is the order from largest to smallest, the wrong "
                    "way round."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e26",
        "band": "easier",
        "text": "Cilia also line the airways inside your lungs. What is their "
                "job there?",
        "options": [
            {"text": "Moving each airway cell along towards your throat.",
             "correct": False,
             "why": "Airway cells are held in a sheet and stay where they "
                    "are. What travels is the layer lying on top of them."},
            {"text": "Taking oxygen out of the air and passing it to your "
                     "blood.",
             "correct": False,
             "why": "Cilia beat; they carry no gases. Oxygen crosses into the "
                    "blood elsewhere in the lungs."},
            {"text": "Sweeping dust back up out of the lungs.",
             "correct": True},
            {"text": "Sensing dust in the air.",
             "correct": False,
             "why": "Sensing is done for the whole of you by nerve cells. "
                    "Cilia do the sweeping."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e27",
        "band": "easier",
        "text": "A sperm cell never feeds. So where does the energy for its "
                "journey come from?",
        "options": [
            {"text": "It takes in tiny cells as it goes and digests them.",
             "correct": False,
             "why": "That is how an Amoeba feeds. A sperm cell takes in "
                    "nothing from start to finish."},
            {"text": "Everything it will spend was loaded in before it set "
                     "out.",
             "correct": True},
            {"text": "It absorbs dissolved food through its tail as it "
                     "swims.",
             "correct": False,
             "why": "Nothing feeds it on the way. The tail is for swimming "
                    "and takes nothing in."},
            {"text": "It makes its own food from light, as a Euglena does.",
             "correct": False,
             "why": "It is not green and it is nowhere near any light."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e28",
        "band": "easier",
        "text": "A Paramecium sweeps a scrap of food inside itself. What "
                "happens to that food next?",
        "options": [
            {"text": "It is digested inside a vacuole within the cell.",
             "correct": True},
            {"text": "It is shared out among the cells around it in the sheet.",
             "correct": False,
             "why": "There are no cells around it. A Paramecium is one whole "
                    "organism on its own."},
            {"text": "It is stored whole until the cell next divides.",
             "correct": False,
             "why": "It is digested straight away. That is how the cell gets "
                    "the energy it is swimming on."},
            {"text": "It travels to the cell's stomach near the base.",
             "correct": False,
             "why": "A single cell has no stomach. The digesting is done "
                    "inside a vacuole."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e29",
        "band": "easier",
        "text": "Which of these is a job your body does for one of your cheek "
                "cells?",
        "options": [
            {"text": "Beating its cilia so that it can swim about.",
             "correct": False,
             "why": "A cheek cell has no cilia and does not swim anywhere."},
            {"text": "Making food out of light.",
             "correct": False,
             "why": "Nothing in you makes food from light. Your food arrives "
                    "as glucose, already digested."},
            {"text": "Keeping the fluid around it steady.",
             "correct": True},
            {"text": "Respiring for it, so that it does not have to.",
             "correct": False,
             "why": "Every cell respires for itself, using its own "
                    "mitochondria. What your body supplies is the oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-e30",
        "band": "easier",
        "text": "A sperm cell's tail and the long whip a Euglena swims with "
                "share one name. What is that name?",
        "options": [
            {"text": "A cilium.",
             "correct": False,
             "why": "A cilium is one of hundreds of short hairs covering a "
                    "surface, not a single long whip."},
            {"text": "A food vacuole.",
             "correct": False,
             "why": "That is where a Paramecium digests the food it has "
                    "swept in. Nothing swims with one."},
            {"text": "A contractile vacuole.",
             "correct": False,
             "why": "That sits inside the cell and bails out water. It has "
                    "nothing to do with swimming."},
            {"text": "A flagellum.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-06-s09",
        "band": "standard",
        "text": "A Paramecium and one of your cheek cells both respire using "
                "mitochondria. Where does each of them get its oxygen from?",
        "options": [
            {"text": "Both take it straight from the air around them as they "
                     "work.",
             "correct": False,
             "why": "A cheek cell lines the inside of your mouth and a "
                    "Paramecium is under water. Neither one is in contact "
                    "with air."},
            {"text": "The Paramecium takes it from the pond; the cheek cell "
                     "has it brought by blood.",
             "correct": True},
            {"text": "Both of them are supplied by blood, since any cell that "
                     "respires needs a blood supply.",
             "correct": False,
             "why": "A Paramecium has no blood and nothing supplies it. It "
                    "collects its own oxygen from the water it swims in."},
            {"text": "Pond weed delivers it to the Paramecium; the cheek cell "
                     "makes its own.",
             "correct": False,
             "why": "Nothing delivers oxygen to a Paramecium, and no cell of "
                    "yours produces any."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s10",
        "band": "standard",
        "text": "In the side-by-side comparison the Paramecium swims and the "
                "cheek cell does not move at all. Why does that not make the "
                "cheek cell any less alive?",
        "options": [
            {"text": "Cells that stay still are dead cells waiting to be "
                     "cleared away.",
             "correct": False,
             "why": "A cheek cell is alive and working the whole time it is "
                    "there, lining your mouth."},
            {"text": "A cheek cell does move, but far too slowly for anyone "
                     "to see it.",
             "correct": False,
             "why": "It is held in a sheet by the cells around it and travels "
                    "nowhere at all."},
            {"text": "Movement is not one of the seven, so failing it changes "
                     "nothing.",
             "correct": False,
             "why": "Movement is the M of the seven. The cheek cell is not "
                    "the thing being tested against them."},
            {"text": "The seven belong to the whole organism, and you do the "
                     "moving for it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s11",
        "band": "standard",
        "text": "A single cell is fed, positioned and cleaned up after by "
                "something larger. What does that tell you about it?",
        "options": [
            {"text": "It is part of an organism, not an organism itself.",
             "correct": True},
            {"text": "It is an organism that has found itself a very good spot.",
             "correct": False,
             "why": "An organism does those jobs for itself. Having them done "
                    "for you is exactly what being a part means."},
            {"text": "It must be a bacterium, since bacteria live inside "
                     "larger organisms.",
             "correct": False,
             "why": "A bacterium is a whole organism in its own right, and "
                    "most of them live free in soil and water."},
            {"text": "Nothing, because every cell has something larger around "
                     "it somewhere.",
             "correct": False,
             "why": "A Paramecium has nothing around it at all, which is "
                    "precisely why this fact does settle it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s12",
        "band": "standard",
        "text": "A Paramecium gets bigger until it is ready to divide, but "
                "not one of your cheek cells ever gets bigger. So how do you "
                "grow?",
        "options": [
            {"text": "Each of your cells swells a little, and it all adds "
                     "up.",
             "correct": False,
             "why": "Your cells stay the size they are. You grow because "
                    "there are more of them."},
            {"text": "Your cells do swell, but only while you are asleep.",
             "correct": False,
             "why": "No cell swells to make you taller, awake or asleep. The "
                    "number of cells is what rises."},
            {"text": "By making more cells, not by making the ones you have "
                     "bigger.",
             "correct": True},
            {"text": "Your bones stretch, and the cells in them are carried "
                     "along.",
             "correct": False,
             "why": "Bone grows the same way the rest of you does, by adding "
                    "cells rather than stretching the ones there."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s13",
        "band": "standard",
        "text": "A cheek cell senses nothing at all. Explain how you can "
                "still feel it when something touches the inside of your "
                "mouth.",
        "options": [
            {"text": "The cheek cells pass the message along the sheet until "
                     "it reaches your brain.",
             "correct": False,
             "why": "A cheek cell does one job, which is lining your mouth. "
                    "Carrying messages is another cell's work."},
            {"text": "Nerve cells do the sensing for the whole of you.",
             "correct": True},
            {"text": "Your blood carries the feeling from your mouth up to "
                     "your brain.",
             "correct": False,
             "why": "Blood carries glucose, oxygen and waste. It carries no "
                    "sensations anywhere."},
            {"text": "You cannot — a touch inside the mouth is never felt at "
                     "all.",
             "correct": False,
             "why": "It is felt easily, and nerve cells are what make that "
                    "possible."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s14",
        "band": "standard",
        "text": "One of your cheek cells makes waste but has no contractile "
                "vacuole to squeeze anything out with. So where does its "
                "waste go?",
        "options": [
            {"text": "It builds up inside until the cell is finally replaced.",
             "correct": False,
             "why": "Waste leaves the cell as it is made. Nothing is stored "
                    "up waiting for the cell to be replaced."},
            {"text": "It is squeezed out through the cell wall into your "
                     "mouth.",
             "correct": False,
             "why": "An animal cell has no wall, and the waste goes inwards "
                    "to the blood rather than out into your mouth."},
            {"text": "The mitochondria burn it up again to get more energy.",
             "correct": False,
             "why": "Mitochondria release energy from glucose. They do not "
                    "dispose of the cell's waste."},
            {"text": "Into the blood, and your kidneys deal with it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s15",
        "band": "standard",
        "text": "A single cell is watched for an hour. It hunts down food, "
                "backs off a grain of sand, gets bigger, and splits into two "
                "cells that swim away separately. Organism, or part of one?",
        "options": [
            {"text": "An organism — nothing supplied it, and it made two more "
                     "of itself.",
             "correct": True},
            {"text": "Part of one, because a cell that splits is replacing "
                     "itself inside a body.",
             "correct": False,
             "why": "These two swam off and fed separately, which a "
                    "replacement cell inside a body never does."},
            {"text": "Part of one, since only a whole animal is able to hunt "
                     "for its food.",
             "correct": False,
             "why": "A single cell can hunt perfectly well. An Amoeba and a "
                    "Paramecium both do."},
            {"text": "Impossible to say without being told how long the cell "
                     "is.",
             "correct": False,
             "why": "Size never settles it. What the cell does for itself "
                    "does."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s16",
        "band": "standard",
        "text": "A single cell is found to carry only half a set of "
                "chromosomes. What does that show?",
        "options": [
            {"text": "It is young, and it will grow the other half a little "
                     "later on.",
             "correct": False,
             "why": "Nothing that lives on its own carries half its "
                    "instructions and waits for the rest."},
            {"text": "It is a bacterium, since a bacterium keeps its DNA "
                     "loose in a loop.",
             "correct": False,
             "why": "A bacterium's loop is a full set of its own "
                    "instructions, not half of anybody's."},
            {"text": "It is built to join another half, so it is part of a "
                     "larger organism.",
             "correct": True},
            {"text": "It has been damaged, and it will not be able to do its "
                     "job.",
             "correct": False,
             "why": "It works exactly as intended. Carrying half a set is "
                    "what such a cell is for."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s17",
        "band": "standard",
        "text": "Two single cells swim equally well. One feeds as it goes; "
                "the other never feeds at all. Which of them is the organism?",
        "options": [
            {"text": "The one that never feeds, because it is saving all its "
                     "energy for swimming.",
             "correct": False,
             "why": "Taking in nutrition is one of the seven. A cell that "
                    "never feeds is being supplied by something larger."},
            {"text": "The one that feeds, because nothing is doing that job "
                     "for it.",
             "correct": True},
            {"text": "Neither, because swimming shows that both of them are "
                     "parts of something.",
             "correct": False,
             "why": "Swimming settles nothing either way. A Paramecium swims "
                    "and is a whole organism."},
            {"text": "Both, because any cell able to swim is already living "
                     "on its own.",
             "correct": False,
             "why": "A sperm cell swims and belongs to a body."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s18",
        "band": "standard",
        "text": "Explain why a Paramecium needs cilia while one of your cheek "
                "cells has no use for them.",
        "options": [
            {"text": "Cheek cells do have cilia of their own, but very much "
                     "shorter ones than a Paramecium has.",
             "correct": False,
             "why": "They have none. The cells that beat cilia in you are the "
                    "ones lining your airways."},
            {"text": "A cheek cell is too small to carry cilia about with "
                     "it.",
             "correct": False,
             "why": "It is larger than a Euglena, which swims. Size is not "
                    "the reason."},
            {"text": "Cheek cells move using a flagellum instead of cilia.",
             "correct": False,
             "why": "A cheek cell does not move at all, with a flagellum or "
                    "without one."},
            {"text": "The Paramecium must take itself to its food; the cheek "
                     "cell never goes anywhere.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s19",
        "band": "standard",
        "text": "A Paramecium lives in fresh pond water, and water keeps "
                "seeping into it. Why must it pump that water back out again?",
        "options": [
            {"text": "Otherwise the water would build up inside it.",
             "correct": True},
            {"text": "To push itself forward through the pond, the way a jet "
                     "of water would.",
             "correct": False,
             "why": "The cilia drive it along. Emptying the vacuole moves the "
                    "organism nowhere."},
            {"text": "To collect the oxygen dissolved in the water as the "
                     "water passes through.",
             "correct": False,
             "why": "Oxygen crosses into the cell on its own. The vacuole "
                    "handles only the water that has to leave."},
            {"text": "So that it stays heavy enough to sink to the pond floor.",
             "correct": False,
             "why": "It swims wherever it wants to be. Nothing about the "
                    "vacuole is there to weigh it down."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s20",
        "band": "standard",
        "text": "A Euglena is kept in the dark for a week and is still alive "
                "at the end of it. How?",
        "options": [
            {"text": "It stops respiring and waits for the light to come "
                     "back.",
             "correct": False,
             "why": "Nothing survives by stopping respiration. It goes on "
                    "releasing energy the whole week."},
            {"text": "It carries on making food from the light it has stored "
                     "up inside.",
             "correct": False,
             "why": "Light cannot be kept in a store. When it goes, that way "
                    "of feeding stops with it."},
            {"text": "It hunts and feeds like an animal instead.",
             "correct": True},
            {"text": "It turns into a Paramecium.",
             "correct": False,
             "why": "One kind of organism does not become another. A Euglena "
                    "stays a Euglena in the dark."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s21",
        "band": "standard",
        "text": "A warm sample holds 400 bacteria, and the number doubles "
                "every twenty minutes. How many will there be after one hour?",
        "options": [
            {"text": "1200, because it triples in an hour.",
             "correct": False,
             "why": "Doubling three times gives 800, then 1600, then 3200 — "
                    "not three lots of 400."},
            {"text": "3200, because the number doubles three times.",
             "correct": True},
            {"text": "800, because it doubles once an hour.",
             "correct": False,
             "why": "It doubles every twenty minutes, so it doubles three "
                    "times in an hour."},
            {"text": "1600, because there are two doublings in an hour.",
             "correct": False,
             "why": "Sixty minutes divided by twenty is three doublings, not "
                    "two."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s22",
        "band": "standard",
        "text": "Which single fact about a cell would settle that it is part "
                "of a larger organism rather than one in its own right?",
        "options": [
            {"text": "It is smaller than a Paramecium is.",
             "correct": False,
             "why": "Size never settles it. A bacterium is far smaller than "
                    "either and is a whole organism."},
            {"text": "It has no nucleus anywhere inside it.",
             "correct": False,
             "why": "A bacterium has none and is an organism; a red blood "
                    "cell has none and is part of you."},
            {"text": "It cannot move about under its own power.",
             "correct": False,
             "why": "Movement settles nothing. Plenty of organisms stay put, "
                    "and plenty of body cells travel."},
            {"text": "Something else brings it everything it uses.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s23",
        "band": "standard",
        "text": "Ana is certain that nothing lacking a nucleus could be "
                "alive, so she refuses to call a bacterium an organism. "
                "Where does her reasoning break down?",
        "options": [
            {"text": "Its instructions are there in a loop, so it lives and "
                     "divides perfectly well.",
             "correct": True},
            {"text": "Nowhere — without a nucleus a cell cannot carry out the "
                     "seven at all.",
             "correct": False,
             "why": "A bacterium carries out all seven for itself, and "
                    "divides about every twenty minutes while doing it."},
            {"text": "Bacteria do have a nucleus; it is simply far too small "
                     "to make out.",
             "correct": False,
             "why": "They have none whatsoever. Their DNA sits loose in the "
                    "cytoplasm with no membrane round it."},
            {"text": "A bacterium is alive, but only inside a larger "
                     "organism.",
             "correct": False,
             "why": "Most bacteria live free in soil and water, feeding and "
                    "dividing on their own."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s24",
        "band": "standard",
        "text": "A white blood cell and an Amoeba both crawl by changing "
                "shape and both engulf bacteria. What separates them?",
        "options": [
            {"text": "The Amoeba is much the larger of the two, so it is the "
                     "organism.",
             "correct": False,
             "why": "Size never settles it, and a bacterium smaller than "
                    "either of them is a whole organism."},
            {"text": "The white blood cell has a nucleus and the Amoeba has "
                     "none at all.",
             "correct": False,
             "why": "Both of them have a nucleus. The cell with none here is "
                    "the bacterium being engulfed."},
            {"text": "Nothing feeds or replaces the Amoeba; the white blood "
                     "cell is fed and replaced by you.",
             "correct": True},
            {"text": "Nothing separates them at all — engulfing bacteria that "
                     "way means both of them must be organisms.",
             "correct": False,
             "why": "A white blood cell engulfs bacteria inside you and is "
                    "part of you."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s25",
        "band": "standard",
        "text": "A student needs to tell paramecia from amoebae on a pond "
                "slide, but does not need to see inside either of them. Which "
                "magnification is enough?",
        "options": [
            {"text": "×40, which already shows that something in the drop is "
                     "alive.",
             "correct": False,
             "why": "At ×40 they are specks and one or two shapes. You cannot "
                    "tell one kind from another."},
            {"text": "×100, where their shapes and movement can be told "
                     "apart.",
             "correct": True},
            {"text": "×400, the only setting that shows anything of them at "
                     "all.",
             "correct": False,
             "why": "×400 shows the structures inside. The shapes are already "
                    "clear one step lower down."},
            {"text": "None — a school microscope cannot separate one pond "
                     "organism from another.",
             "correct": False,
             "why": "It separates them easily from ×100 upwards. What it "
                    "cannot resolve is a bacterium."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s26",
        "band": "standard",
        "text": "A Paramecium 0.25 mm long swims one millimetre in a second. "
                "How many of its own body lengths is that each second?",
        "options": [
            {"text": "Forty times its own length.",
             "correct": False,
             "why": "Forty lengths would be 10 mm in a second, which is far "
                    "more than it covers."},
            {"text": "A quarter of its own length.",
             "correct": False,
             "why": "That divides the wrong way round. One millimetre shared "
                    "into 0.25 mm lengths is four of them."},
            {"text": "Four times its own length.",
             "correct": True},
            {"text": "One and a quarter times its own length.",
             "correct": False,
             "why": "That comes from adding the two numbers together instead "
                    "of dividing one by the other."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s27",
        "band": "standard",
        "text": "Cilia cover a Paramecium and also line your airways. A "
                "student decides the airway cells must be tiny organisms "
                "living inside you. What is wrong with that?",
        "options": [
            {"text": "Nothing — anything with cilia moves itself, so it is an "
                     "organism.",
             "correct": False,
             "why": "Cilia settle nothing. A Paramecium has them, and so do "
                    "cells that are part of you."},
            {"text": "Airway cells have no cilia; the mucus moves along on "
                     "its own.",
             "correct": False,
             "why": "They do have cilia, and it is their beating that shifts "
                    "the mucus."},
            {"text": "They would be organisms, but they are far too small to "
                     "count as any.",
             "correct": False,
             "why": "Size never settles it. A bacterium is far smaller still "
                    "and is a whole organism."},
            {"text": "Each one does a single job and is fed and held in place "
                     "by the rest of you.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s28",
        "band": "standard",
        "text": "Which would you expect to have a contractile vacuole: a cell "
                "living free in fresh pond water, or a cell sitting in the "
                "fluid your body holds steady?",
        "options": [
            {"text": "The body one, because there is far more water "
                     "surrounding it.",
             "correct": False,
             "why": "The fluid round your cells is held steady, so no water "
                    "builds up inside them."},
            {"text": "The pond one, because water keeps seeping in and "
                     "nothing else removes it.",
             "correct": True},
            {"text": "Both, because every cell has to pump water out all the "
                     "time.",
             "correct": False,
             "why": "Your cells never pump water out. Your body holds the "
                    "fluid around them steady instead."},
            {"text": "Neither, because a vacuole is for storing food rather "
                     "than water.",
             "correct": False,
             "why": "A food vacuole stores food. The contractile one deals "
                    "only with water."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s29",
        "band": "standard",
        "text": "A Paramecium meets a grain of sand and reverses away from "
                "it. Which two of the seven life processes is it showing?",
        "options": [
            {"text": "Nutrition and excretion.",
             "correct": False,
             "why": "Those are taking in food and getting rid of waste. "
                    "Neither is happening here."},
            {"text": "Growth and reproduction.",
             "correct": False,
             "why": "Those are getting bigger and making more of itself, "
                    "which come later."},
            {"text": "Sensitivity and movement.",
             "correct": True},
            {"text": "Respiration and nutrition.",
             "correct": False,
             "why": "Those are releasing energy from food and taking food in. "
                    "It is doing neither at this moment."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-s30",
        "band": "standard",
        "text": "An Amoeba is put into a dish of clean water with nothing "
                "else in it. Predict what will happen to it, and say why.",
        "options": [
            {"text": "It will starve, because nothing else is there to feed "
                     "it.",
             "correct": True},
            {"text": "It will make food from the water, which any single cell "
                     "can do.",
             "correct": False,
             "why": "Only the green ones make their own food, and they need "
                    "light to do it. An Amoeba has to find its food."},
            {"text": "It will be fine, because its neighbours will share what "
                     "they have.",
             "correct": False,
             "why": "It has no neighbours. That is what living as a single "
                    "cell means."},
            {"text": "It will stop respiring until some food eventually turns "
                     "up.",
             "correct": False,
             "why": "Respiration carries on the whole time, which is exactly "
                    "what uses its food up."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-06-h09",
        "band": "harder",
        "text": "A student writes down a rule: a cell that moves under its "
                "own power must be an organism. Name the one cell that breaks "
                "it.",
        "options": [
            {"text": "A Paramecium, which swims and is an organism.",
             "correct": False,
             "why": "It obeys the rule, so it cannot be what breaks it. What "
                    "is needed is a mover that is part of something."},
            {"text": "A sperm cell, which swims and belongs to a body.",
             "correct": True},
            {"text": "A cheek cell, which stays still and is part of you.",
             "correct": False,
             "why": "It does not move, so the rule says nothing about it "
                    "either way."},
            {"text": "A bacterium, which divides about every twenty minutes.",
             "correct": False,
             "why": "Dividing is not moving. This tells you nothing about a "
                    "rule written about movement."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h10",
        "band": "harder",
        "text": "Evaluate this claim: any cell without a nucleus must be a "
                "bacterium.",
        "options": [
            {"text": "Wrong — a red blood cell has no nucleus and is one of "
                     "yours.",
             "correct": True},
            {"text": "Right, because bacteria are the only living things that "
                     "manage without one.",
             "correct": False,
             "why": "A red blood cell manages without one too, having "
                    "destroyed its own and lost its DNA with it."},
            {"text": "Right, because a cell needs a nucleus in order to be "
                     "able to divide.",
             "correct": False,
             "why": "A bacterium divides about every twenty minutes and has "
                    "no nucleus at any stage."},
            {"text": "Wrong, because a bacterium keeps its nucleus hidden in "
                     "the cytoplasm.",
             "correct": False,
             "why": "What sits in a bacterium's cytoplasm is a loose loop of "
                    "DNA, with no membrane round it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h11",
        "band": "harder",
        "text": "A warm dish is started with 50 bacteria, which double every "
                "twenty minutes. How long before there are 800 of them?",
        "options": [
            {"text": "Twenty minutes.",
             "correct": False,
             "why": "That is one doubling, which takes 50 to 100."},
            {"text": "Forty minutes.",
             "correct": False,
             "why": "Two doublings give 200, which is a quarter of the way "
                    "there."},
            {"text": "One hour.",
             "correct": False,
             "why": "Three doublings give 400. One more doubling is needed "
                    "to reach 800."},
            {"text": "Eighty minutes.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h12",
        "band": "harder",
        "text": "At ×400 the field of view is 0.45 mm across, and a "
                "bacterium is 0.002 mm long. Roughly how many bacteria would "
                "lie end to end across the field?",
        "options": [
            {"text": "About 22.",
             "correct": False,
             "why": "There is a zero missing from the divisor. That answer is "
                    "0.45 ÷ 0.02, not 0.45 ÷ 0.002."},
            {"text": "About 2250.",
             "correct": False,
             "why": "That is one zero too many: it divides by 0.0002. A "
                    "bacterium is two thousandths of a millimetre."},
            {"text": "About 450.",
             "correct": False,
             "why": "That comes from dividing by 0.001. The bacterium is "
                    "twice that length, so the answer is half as big."},
            {"text": "About 225.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h13",
        "band": "harder",
        "text": "A Euglena is green and makes food from light, and so does a "
                "cell inside a leaf. Only one of the two is an organism. "
                "Which fact decides it?",
        "options": [
            {"text": "The leaf cell is the larger, so it belongs to something "
                     "bigger than itself.",
             "correct": False,
             "why": "Size never settles it. A bacterium is smaller than "
                    "either of them and is a whole organism."},
            {"text": "The Euglena swims about and the leaf cell stays exactly "
                     "where it is.",
             "correct": False,
             "why": "Movement settles nothing. A sperm cell swims and belongs "
                    "to a body."},
            {"text": "Nothing feeds, moves or protects the Euglena; the leaf "
                     "cell has all three done for it.",
             "correct": True},
            {"text": "Only the Euglena makes its food from light, so only it "
                     "can be an organism.",
             "correct": False,
             "why": "Both of them make food from light. A fact they share "
                    "cannot separate them."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h14",
        "band": "harder",
        "text": "A sperm cell and a Euglena both swim using a single long "
                "flagellum. Which of them is the organism, and what settles "
                "it?",
        "options": [
            {"text": "The Euglena, because it feeds itself and the sperm cell "
                     "never feeds at all.",
             "correct": True},
            {"text": "The sperm cell, because it swims faster and further "
                     "than a Euglena manages.",
             "correct": False,
             "why": "Swimming settles nothing, whichever way round it is put. "
                    "Both of them swim."},
            {"text": "The Euglena, because it is the larger of the two by "
                     "some way.",
             "correct": False,
             "why": "It is the organism, but not for that reason. Size never "
                    "settles this."},
            {"text": "Neither, because a flagellum grows only on part of a "
                     "larger organism.",
             "correct": False,
             "why": "A Euglena has one and is a whole organism on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h15",
        "band": "harder",
        "text": "A cell taken from the gut lining of a snail has a nucleus, "
                "beats cilia, and is supplied with food by the snail's blood. "
                "Organism, or part of one?",
        "options": [
            {"text": "An organism, because a cell that beats cilia is a cell "
                     "that moves itself about.",
             "correct": False,
             "why": "Cilia settle nothing. The cells lining your own airways "
                    "beat them and are part of you."},
            {"text": "Part of one — the cilia and the nucleus settle nothing, "
                     "and it is fed.",
             "correct": True},
            {"text": "An organism, because a cell with a nucleus can live on "
                     "its own.",
             "correct": False,
             "why": "Every cheek cell you own has a nucleus, and not one of "
                    "them lives on its own."},
            {"text": "Impossible to tell without being told how long the cell "
                     "is.",
             "correct": False,
             "why": "Size never settles it. What decides this case is that "
                    "the snail feeds the cell."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h16",
        "band": "harder",
        "text": "A single cell in a compost heap takes in dissolved food from "
                "the rotting leaves around it, grows, and splits into two "
                "cells that go on feeding separately. Is it an organism?",
        "options": [
            {"text": "No, because it depends on the compost heap to feed it.",
             "correct": False,
             "why": "Every organism gets its food from somewhere. What "
                    "matters is that nothing is doing the feeding for it."},
            {"text": "No, because splitting is how cells inside a body "
                     "replace themselves.",
             "correct": False,
             "why": "These two went on feeding separately, which a "
                    "replacement cell inside a body never does."},
            {"text": "Only if it turns out to have a nucleus inside it.",
             "correct": False,
             "why": "A bacterium has none and is a whole organism. The "
                    "nucleus is not what decides this."},
            {"text": "Yes — it feeds, grows and reproduces with nothing "
                     "supplying it at any point.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h17",
        "band": "harder",
        "text": "A drawing shows a Paramecium 100 mm long, and the real one "
                "is 0.25 mm. At that same scale, how long should a 0.002 "
                "mm bacterium be drawn?",
        "options": [
            {"text": "8 mm",
             "correct": False,
             "why": "The scale here is 100 ÷ 0.25, which is ×400, so the "
                    "answer is ten times smaller than that."},
            {"text": "0.08 mm",
             "correct": False,
             "why": "×40 is ten times too small a scale. The drawing is 400 "
                    "times life size."},
            {"text": "0.8 mm",
             "correct": True},
            {"text": "0.002 mm",
             "correct": False,
             "why": "Everything on a scale drawing is scaled, including the "
                    "smallest thing on it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h18",
        "band": "harder",
        "text": "One slide holds a drop of pond water with seven "
                "single-celled organisms in it. The next slide holds a cheek "
                "smear of two hundred cells. Which slide carries more "
                "organisms?",
        "options": [
            {"text": "The pond drop, with seven.",
             "correct": True},
            {"text": "The cheek smear.",
             "correct": False,
             "why": "Those two hundred cells are all part of one person, and "
                    "that person is not on the slide."},
            {"text": "Both hold the same number.",
             "correct": False,
             "why": "A cell doing one job for something larger is part of an "
                    "organism rather than one."},
            {"text": "The smear, because each of those cells is alive and "
                     "getting on with its job.",
             "correct": False,
             "why": "Being alive and doing a job is what a part does. It does "
                    "not make each cell an organism."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h19",
        "band": "harder",
        "text": "An Amoeba is moved out of pond water into a fluid like the "
                "one your body holds steady around its own cells. Predict "
                "what happens to the work its contractile vacuole has to do.",
        "options": [
            {"text": "It goes up, because a fluid like that is heavier than "
                     "pond water.",
             "correct": False,
             "why": "Weight has nothing to do with how much water crosses "
                    "into the cell."},
            {"text": "It goes down — that is exactly why no cell of yours "
                     "needs a vacuole like it.",
             "correct": True},
            {"text": "It stays the same, because the vacuole fills at a fixed "
                     "rate whatever happens.",
             "correct": False,
             "why": "It fills with the water that seeps in, so what is "
                    "outside the cell sets the rate."},
            {"text": "It stops altogether and the Amoeba bursts within "
                     "seconds.",
             "correct": False,
             "why": "Less water arriving means less to pump out, which is "
                    "easier for the cell rather than fatal."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h20",
        "band": "harder",
        "text": "Which single question would sort a Euglena, a sperm cell, a "
                "bacterium and one of your cheek cells correctly, all four at "
                "once?",
        "options": [
            {"text": "Does this cell have a nucleus?",
             "correct": False,
             "why": "That puts the bacterium on one side and the other three "
                    "on the other, which is the wrong split twice over."},
            {"text": "Can this cell move under its own power?",
             "correct": False,
             "why": "The Euglena and the sperm cell both swim, and only one "
                    "of those two is an organism."},
            {"text": "Is this cell bigger than one of the cheek cells lining "
                     "your own mouth?",
             "correct": False,
             "why": "A bacterium is far smaller than a cheek cell and is "
                    "still a whole organism."},
            {"text": "Does this cell carry out all seven life processes for "
                     "itself?",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h21",
        "band": "harder",
        "text": "A cell senses, moves, respires, grows, reproduces and "
                "excretes entirely by itself, but it is fed by the larger "
                "animal it sits inside. Organism, or part of one?",
        "options": [
            {"text": "An organism, because six of the seven carried out alone "
                     "is easily enough to count it as one.",
             "correct": False,
             "why": "The rule is all seven. Being fed is exactly what a part "
                    "has done for it."},
            {"text": "An organism, because no cell that is part of a body "
                     "senses anything.",
             "correct": False,
             "why": "Nerve cells are part of a body and sensing is exactly "
                    "what they do. Sensing settles nothing here."},
            {"text": "Part of one — nutrition is one of the seven, and it is "
                     "the one being done for it.",
             "correct": True},
            {"text": "Part of one, because no single cell can do six things "
                     "at once.",
             "correct": False,
             "why": "A Paramecium does all seven at once, all day long."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h22",
        "band": "harder",
        "text": "A student says a Paramecium must be simpler than one of your "
                "cheek cells, since it is only one cell. Which observation "
                "most clearly shows the opposite?",
        "options": [
            {"text": "It is four times the length of a cheek cell.",
             "correct": False,
             "why": "Size says nothing about how much machinery a cell "
                    "carries."},
            {"text": "It has cilia, an oral groove and a bailing vacuole on "
                     "top of all your cell has.",
             "correct": True},
            {"text": "It lives in pond water rather than inside a body.",
             "correct": False,
             "why": "Where a cell lives settles nothing about how complicated "
                    "it is."},
            {"text": "It has mitochondria, which a cheek cell does not.",
             "correct": False,
             "why": "Both of them have mitochondria. A shared feature cannot "
                    "separate them."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h23",
        "band": "harder",
        "text": "A mystery cell is watched for an hour: it swims, reverses "
                "off an obstacle, gets bigger, and splits into two that swim "
                "away. Which observation settles that it is an organism?",
        "options": [
            {"text": "That it swam about under its own power.",
             "correct": False,
             "why": "A sperm cell swims and a white blood cell crawls. "
                    "Movement settles nothing."},
            {"text": "That it reversed when it met the obstacle.",
             "correct": False,
             "why": "Nerve cells sense for the whole of you, so a cell "
                    "inside a body sits in something just as responsive. "
                    "Sensing settles nothing."},
            {"text": "That it grew and split with nothing supplying it.",
             "correct": True},
            {"text": "That it stayed alive for a whole hour on the slide.",
             "correct": False,
             "why": "Staying alive for an hour says nothing about whether "
                    "something larger was keeping it alive."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h24",
        "band": "harder",
        "text": "A Paramecium's contractile vacuole stops working while the "
                "cell is still in pond water. Predict what happens to the "
                "cell.",
        "options": [
            {"text": "It dries out, because the vacuole was its only supply "
                     "of water.",
             "correct": False,
             "why": "The vacuole removes water from the cell. It brings none "
                    "in."},
            {"text": "Nothing, because a Paramecium gets along perfectly well "
                     "without one.",
             "correct": False,
             "why": "It lives in fresh water, and water crosses into it the "
                    "whole time it is there."},
            {"text": "It stops swimming, because the vacuole is what drives "
                     "the cilia along.",
             "correct": False,
             "why": "The cilia beat under their own power and owe the vacuole "
                    "nothing."},
            {"text": "Water builds up inside it, with nothing left to remove "
                     "it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h25",
        "band": "harder",
        "text": "A slime on a damp wall turns out to be millions of separate "
                "single cells, each one feeding, growing and dividing on its "
                "own. How many organisms is that?",
        "options": [
            {"text": "Millions — one for each cell.",
             "correct": True},
            {"text": "One, because all of them are joined in the same patch "
                     "on the wall.",
             "correct": False,
             "why": "Sitting side by side does not join them into one "
                    "organism. Each is doing all seven for itself."},
            {"text": "None, because a single cell is never a whole organism "
                     "by itself.",
             "correct": False,
             "why": "That is precisely the idea this lesson exists to "
                    "break."},
            {"text": "Two, since the wall and the slime make one living thing "
                     "between them.",
             "correct": False,
             "why": "The wall is not alive at all, and the slime is not one "
                    "thing."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h26",
        "band": "harder",
        "text": "Two students disagree. One says a bacterium is an organism "
                "because it divides on its own; the other says it cannot be, "
                "because it has no nucleus. Who is right?",
        "options": [
            {"text": "The second, because without a nucleus there are no "
                     "instructions to divide with.",
             "correct": False,
             "why": "A bacterium's instructions sit loose in its cytoplasm, "
                    "and it uses them about every twenty minutes."},
            {"text": "The first — what settles it is what a cell does for "
                     "itself, not what it contains.",
             "correct": True},
            {"text": "Both are wrong, because only a cell that makes its own "
                     "food can be an organism.",
             "correct": False,
             "why": "An Amoeba makes none of its own food and is a whole "
                    "organism."},
            {"text": "Both are right, and the two facts cancel each other "
                     "out.",
             "correct": False,
             "why": "Only one of the two facts bears on the question at all. "
                    "The nucleus is beside the point."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h27",
        "band": "harder",
        "text": "At ×400 the field of view is 0.45 mm across. Two paramecia, "
                "each 0.25 mm long, are laid end to end. Would both fit "
                "inside the field?",
        "options": [
            {"text": "Yes, because 0.25 mm is comfortably smaller than 0.45 "
                     "mm.",
             "correct": False,
             "why": "One of them fits. The question is about two of them, "
                    "which come to 0.50 mm."},
            {"text": "Yes, because the field of view grows as you climb the "
                     "magnifications.",
             "correct": False,
             "why": "It shrinks. At ×400 almost all of the slide has gone out "
                    "of view."},
            {"text": "No — together they come to 0.50 mm, which is wider than "
                     "the field.",
             "correct": True},
            {"text": "No, because a Paramecium is too small to see at ×400 "
                     "anyway.",
             "correct": False,
             "why": "At ×400 you can see its cilia, its vacuole and its oral "
                    "groove."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h28",
        "band": "harder",
        "text": "One of your cheek cells is dropped into a drop of pond water "
                "and left there. Explain why it cannot get on with life as an "
                "organism.",
        "options": [
            {"text": "Nothing feeds it, nothing holds the fluid round it "
                     "steady, and it does one job only.",
             "correct": True},
            {"text": "It simply becomes a unicellular organism of its own, now "
                     "that it is on its own in the pond water.",
             "correct": False,
             "why": "Being alone gives it no oral groove, no vacuole and no "
                    "way of finding food."},
            {"text": "It manages, because it has a nucleus and mitochondria "
                     "of its own.",
             "correct": False,
             "why": "So does a cheek cell inside your mouth, and that one is "
                    "still fed and cleaned up after by you."},
            {"text": "It cannot, because pond water has no oxygen dissolved "
                     "in it.",
             "correct": False,
             "why": "Pond water carries dissolved oxygen, and every organism "
                    "on that slide respires in it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h29",
        "band": "harder",
        "text": "A student counts twelve organisms in one field of view at "
                "×400 and reports that the whole drop holds twelve. Evaluate "
                "that report.",
        "options": [
            {"text": "It is right, because one field of view takes in the "
                     "whole slide at once.",
             "correct": False,
             "why": "At ×400 the field is 0.45 mm across, so almost all of "
                    "the slide is outside it."},
            {"text": "Far too low: the field shows 0.45 mm and the rest was "
                     "never looked at.",
             "correct": True},
            {"text": "Too high, because some of the twelve will have been "
                     "counted twice over.",
             "correct": False,
             "why": "They were all in view at the same moment, so none of "
                    "them could be counted twice."},
            {"text": "It cannot be judged, because organisms cannot be "
                     "counted at ×400.",
             "correct": False,
             "why": "They can be counted, and at ×400 you can see which kind "
                    "each one is."},
        ],
        "figure": None,
    },
    {
        "id": "b1-06-h30",
        "band": "harder",
        "text": "Evaluate this statement: a cell inside your body never has "
                "to do anything for itself.",
        "options": [
            {"text": "Correct, because the rest of the body carries out all "
                     "seven of them for it.",
             "correct": False,
             "why": "It respires for itself, using its own mitochondria. What "
                    "your body does is deliver the oxygen."},
            {"text": "Correct, because a cell doing anything for itself would "
                     "be an organism.",
             "correct": False,
             "why": "A cheek cell respires for itself and is still part of "
                    "you."},
            {"text": "Wrong, because your cells go and find their own food in "
                     "the blood.",
             "correct": False,
             "why": "Glucose is delivered to them, dissolved and already "
                    "digested. They fetch nothing."},
            {"text": "Too strong — every one of your cells respires for "
                     "itself, and never stops.",
             "correct": True},
        ],
        "figure": None,
    },
]
