"""B1 lesson 05 — Levels of organisation: twelve questions (MRB-269).

The lesson's one claim is that a rung up is a different KIND of thing, not a
bigger one, and that the only thing added between rungs is organisation. These
twelve probe exactly that: the five stops of the plant zoom in order, the
tissue/organ/organ-system definitions applied to the awkward cases the lesson
sorts (blood, skin, xylem, a chloroplast, a tree's root system), the removal
cases (a stomach with no muscle layer, a leaf whose cells are shuffled), and —
in the harder band — the same rule carried into contexts the lesson does not
draw: why the ladder starts at the cell, why extinction belongs to a
population, and why a healthy donated organ in a box can do nothing.

The distractors are built from the lesson's two declared misconceptions —
CELL-06 "an organ is just a bigger tissue" (the size error, which reappears as
"more cells", "a larger version", "bigger than the tree above ground" and "a
population is a very large organism") and CELL-07 "blood can't be a tissue —
it's a liquid" (the solidity error) — plus the hook's own wrong options:
quantity fixes it, and different kinds of cell are what is missing.
"""

UNIT = "B1"
LESSON = "levels-of-organisation"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-05-e01",
        "band": "easier",
        "text": "A group of similar cells, all doing the same job, packed "
                "together so their effect adds up. What is that called?",
        "options": [
            {"text": "A tissue", "correct": True},
            {"text": "An organ", "correct": False,
             "why": "An organ is several different tissues arranged together "
                    "— a leaf needs palisade cells, veins and an epidermis. "
                    "Similar cells on one job is the rung below."},
            {"text": "An organ system", "correct": False,
             "why": "An organ system is a group of whole organs on one big "
                    "job, like the shoot: the stem and every leaf together. "
                    "You are two rungs too high."},
            {"text": "An organism", "correct": False,
             "why": "An organism is the whole living thing — the entire "
                    "plant, or you. One kind of cell doing one job is a long "
                    "way below that."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e02",
        "band": "easier",
        "text": "The zoom went from the whole plant down to one palisade cell "
                "in five stops. Which order is that, largest first?",
        "options": [
            {"text": "Organism, organ, organ system, tissue, cell",
             "correct": False,
             "why": "You have swapped the middle two. The shoot (an organ "
                    "system) contains the leaf (an organ), not the other way "
                    "round."},
            {"text": "Organism, organ system, tissue, organ, cell",
             "correct": False,
             "why": "A tissue sits inside an organ, not above it — the "
                    "palisade layer is one of the layers that make up the "
                    "leaf."},
            {"text": "Organism, organ system, organ, tissue, cell",
             "correct": True},
            {"text": "Organism, organ system, organ, cell, tissue",
             "correct": False,
             "why": "Cells come below tissues. A tissue is many similar cells "
                    "together, so the cell is always the bottom rung of the "
                    "five."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e03",
        "band": "easier",
        "text": "Climbing one rung of the ladder always adds one thing. What "
                "is it?",
        "options": [
            {"text": "More cells than the rung below has", "correct": False,
             "why": "Quantity is not what the ladder measures. A dish can "
                    "hold more stomach cells than your stomach does and still "
                    "digest nothing."},
            {"text": "Organisation — the parts arranged to work together",
             "correct": True},
            {"text": "A larger version of the same structure", "correct": False,
             "why": "That is the size error this lesson exists to kill. A "
                    "rung up is a different kind of thing, not a bigger one."},
            {"text": "New kinds of cell that the rung below lacks",
             "correct": False,
             "why": "Sometimes there are new cell types and sometimes there "
                    "are not — the shoot has no cell type the leaf lacks. "
                    "What is added every time is the arrangement."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e04",
        "band": "easier",
        "text": "Which one of these is an organ?",
        "options": [
            {"text": "Xylem", "correct": False,
             "why": "Xylem is a tissue — similar cells doing one job, "
                    "carrying water up the plant. It sits inside organs like "
                    "the stem, the root and the leaf."},
            {"text": "Blood", "correct": False,
             "why": "Blood is a tissue: a few kinds of cell in huge numbers, "
                    "all working on transport. Being a liquid does not move "
                    "it up a rung."},
            {"text": "The digestive system", "correct": False,
             "why": "That is a chain of organs — mouth, stomach, intestines "
                    "and more — working on one big job, so it is an organ "
                    "system."},
            {"text": "The skin", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-05-s01",
        "band": "standard",
        "text": "A stomach is left whole but its muscle tissue is removed. "
                "The lining still makes acid and enzymes and the nerves are "
                "untouched. What happens to a sandwich in it?",
        "options": [
            {"text": "Acid and enzymes stop being made, so nothing is broken "
                     "down at all", "correct": False,
             "why": "The muscle layer never made the acid — the lining does, "
                    "and the lining is still there. The chemistry is fine; it "
                    "is the mixing that has gone."},
            {"text": "The chemistry works but nothing churns, so digestion is "
                     "patchy and never finishes",
             "correct": True},
            {"text": "Nothing changes, because the enzymes do all the real "
                     "work and they are still there", "correct": False,
             "why": "Enzymes only work where they meet the food, and a "
                    "sandwich is not a liquid. With no churning they reach "
                    "the outside of the lump and never the middle."},
            {"text": "The stomach bursts, because nothing is holding it in "
                     "shape any more", "correct": False,
             "why": "The connective tissue still holds the shape. Losing one "
                    "tissue does not destroy the organ — it stops the organ "
                    "doing its job properly."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s02",
        "band": "standard",
        "text": "A leaf's cells are shuffled so that palisade, spongy and "
                "epidermis cells are mixed evenly through a blob of the same "
                "size. Every cell is alive, with all its chloroplasts. What "
                "happens in the light?",
        "options": [
            {"text": "It photosynthesises exactly as well, since not one "
                     "chloroplast has been lost", "correct": False,
             "why": "Counting chloroplasts is the quantity error. Most of "
                    "them now sit in shade behind other cells instead of in a "
                    "dense layer at the top."},
            {"text": "It photosynthesises faster, because light now reaches "
                     "cells all through the blob", "correct": False,
             "why": "Light is absorbed by whatever it meets first, so the "
                    "deeper cells are shaded either way. Spreading the "
                    "chloroplasts out wastes the layer that caught almost all "
                    "of it."},
            {"text": "It stops at once, because cells only work while they "
                     "are joined to each other", "correct": False,
             "why": "Every cell stays alive and keeps working — that is the "
                    "whole point of the case. What was taken away is the "
                    "arrangement, not the cells."},
            {"text": "It photosynthesises poorly and soon dries out, with no "
                     "epidermis, air spaces or veins", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s03",
        "band": "standard",
        "text": "A student writes: 'Skin must be a tissue, because it is one "
                "continuous covering made of skin cells.' What is wrong with "
                "that?",
        "options": [
            {"text": "Skin is several unlike tissues — epidermis, glands, "
                     "nerves — so it is an organ",
             "correct": True},
            {"text": "Skin is an organ system, because it covers and protects "
                     "the whole body", "correct": False,
             "why": "An organ system is a group of whole organs, like the "
                    "digestive system. Skin is one organ, however much of you "
                    "it covers."},
            {"text": "Nothing is wrong — every cell in skin really is doing "
                     "the same job", "correct": False,
             "why": "They are not. A gland cell, a nerve ending and an "
                    "epidermis cell are unlike each other, and unlike tissues "
                    "working together make an organ."},
            {"text": "Skin is a tissue, but only because it is thin — "
                     "thickness is what sets the rung", "correct": False,
             "why": "Thickness sets nothing. The palisade layer is 0.2 mm "
                    "thick and is a tissue; a leaf is thinner than skin and "
                    "is an organ."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s04",
        "band": "standard",
        "text": "A tree's root system: hundreds of roots that anchor it and "
                "take up water and minerals. Which rung is it on?",
        "options": [
            {"text": "A tissue, because the roots are all similar to one "
                     "another", "correct": False,
             "why": "Similar organs is not the same as similar cells. A "
                    "tissue is one kind of cell on one job, and a single root "
                    "is already several tissues."},
            {"text": "An organ, because it is one connected structure doing "
                     "one job", "correct": False,
             "why": "Each single root is the organ. Many organs working on "
                    "one overall job is the rung above that — an organ "
                    "system."},
            {"text": "An organ system, because many roots, each an organ, "
                     "share one overall job", "correct": True},
            {"text": "An organism, because it can be larger than the tree "
                     "above ground", "correct": False,
             "why": "Size again. The organism is the whole tree; the root "
                    "system is one part of it, however large that part "
                    "grows."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-05-h01",
        "band": "harder",
        "text": "A chloroplast is smaller than a cell and does a definite "
                "job. So why do biologists put the bottom rung of the ladder "
                "at the cell, and not lower?",
        "options": [
            {"text": "Because a chloroplast is too small to see with a school "
                     "microscope", "correct": False,
             "why": "Size and visibility settle nothing here — a palisade "
                    "cell is only 0.05 mm across and it is on the ladder. "
                    "What matters is what the thing can do."},
            {"text": "Because only plant cells have chloroplasts, so that "
                     "rung would not work for animals", "correct": False,
             "why": "A ladder could simply name a different organelle for "
                    "animals. The real reason is that no organelle is alive "
                    "on its own."},
            {"text": "Because a cell is the smallest living thing that does "
                     "all seven life processes",
             "correct": True},
            {"text": "Because a chloroplast is a chemical rather than a "
                     "structure built from cells", "correct": False,
             "why": "A chloroplast is a real structure, not a chemical. It is "
                    "a part of a cell — machinery inside a living thing, not "
                    "a living thing."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h02",
        "band": "harder",
        "text": "A conservationist says a single rabbit cannot go extinct — "
                "only a population can. How does that fit the ladder of "
                "organisation?",
        "options": [
            {"text": "It follows the same rule above the organism: a "
                     "population does something no single organism can",
             "correct": True},
            {"text": "It breaks the rule, because the ladder stops at the "
                     "organism and nothing sits above it", "correct": False,
             "why": "The ladder carries on upwards — populations, "
                    "communities, ecosystems — and the same rule holds at "
                    "every one of those levels."},
            {"text": "A population is just a very large organism, so it is "
                     "the same rung with more members", "correct": False,
             "why": "That is the size error, one rung higher up. A population "
                    "is a different kind of thing, not a bigger rabbit."},
            {"text": "It has nothing to do with the ladder, which only "
                     "describes what is inside one body", "correct": False,
             "why": "The ladder is about levels of organisation wherever they "
                    "happen, and each level doing something the level below "
                    "cannot runs above the organism too."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h03",
        "band": "harder",
        "text": "A donated kidney is carried to a hospital in a cold box. "
                "Every cell and every tissue in it is healthy. Why can it not "
                "clean anybody's blood while it sits there?",
        "options": [
            {"text": "Because a kidney is only a tissue, and a single tissue "
                     "cannot do a whole job by itself", "correct": False,
             "why": "A kidney is an organ — several unlike tissues arranged "
                    "together. Which rung it is on is not the problem here."},
            {"text": "Because its cells stop working the moment the organ "
                     "leaves a body", "correct": False,
             "why": "The cells are alive and still working, which is why the "
                    "box is worth using at all. What has been cut is the "
                    "connection, not the cell."},
            {"text": "Because it has to be joined to more kidneys before it "
                     "can filter anything", "correct": False,
             "why": "One kidney is plenty — people live with one. What it "
                    "needs is to be plumbed into a system, not to be "
                    "duplicated."},
            {"text": "Because an organ is not self-sufficient — nothing brings "
                     "it blood or takes waste away",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h04",
        "band": "harder",
        "text": "Which pair of things sits on the same rung of the ladder?",
        "options": [
            {"text": "A leaf and the shoot it grows on", "correct": False,
             "why": "The leaf is an organ and the shoot is the organ system "
                    "it belongs to — one rung apart, not the same rung."},
            {"text": "The palisade layer of a leaf and blood", "correct": True},
            {"text": "Xylem and the stomach", "correct": False,
             "why": "Xylem is a tissue and the stomach is an organ. Sitting "
                    "inside an organ is exactly what a tissue does."},
            {"text": "A chloroplast and a palisade cell", "correct": False,
             "why": "A palisade cell is on the bottom rung. A chloroplast is "
                    "a part of that cell, and is not on the ladder at all."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b1-05-e05",
        "band": "easier",
        "text": "What is an organ?",
        "options": [
            {"text": "A group of similar cells all doing the same job",
             "correct": False,
             "why": "That is a tissue. An organ is built from several "
                    "different tissues working together."},
            {"text": "A group of different tissues working together to do one "
                     "job", "correct": True},
            {"text": "A group of organs working together to do one big job",
             "correct": False,
             "why": "That is an organ system — your digestive system, or a "
                    "tree's root system. An organ is one rung below it."},
            {"text": "Any part of the body that is larger than a tissue",
             "correct": False,
             "why": "Size does not set a rung. An organ is a different kind "
                    "of thing: several unlike tissues arranged to do one "
                    "job."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e06",
        "band": "easier",
        "text": "Which one of these is a tissue?",
        "options": [
            {"text": "The brain", "correct": False,
             "why": "The brain is an organ: nerve tissue of more than one "
                    "kind, with blood vessels, connective tissue and "
                    "membranes."},
            {"text": "The stomach", "correct": False,
             "why": "The stomach is an organ — muscle, lining, connective "
                    "tissue and nerves arranged so that they work together."},
            {"text": "Xylem", "correct": True},
            {"text": "The root system of a tree", "correct": False,
             "why": "That is an organ system: many roots, each of them an "
                    "organ, sharing one overall job."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e07",
        "band": "easier",
        "text": "The levels of organisation start at the cell rather than "
                "at anything smaller. Why?",
        "options": [
            {"text": "A cell is the smallest thing in that series that is "
                     "alive", "correct": True},
            {"text": "It is the smallest thing a school microscope can show "
                     "you", "correct": False,
             "why": "A nucleus and a chloroplast are both smaller and both "
                    "visible. The bottom level is set there because a cell is "
                    "the smallest living thing."},
            {"text": "It is the smallest part of a body that has a job to do",
             "correct": False,
             "why": "A chloroplast has a definite job and is smaller than a "
                    "cell. What a chloroplast is not is alive."},
            {"text": "Nothing smaller than a cell exists inside a living "
                     "thing", "correct": False,
             "why": "A great deal does — a nucleus, a vacuole, a chloroplast. "
                    "They sit below the bottom level because they are parts, "
                    "not living things."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e08",
        "band": "easier",
        "text": "The mouth, oesophagus, stomach, intestines, liver and "
                "pancreas all work on one big job. What is that group called?",
        "options": [
            {"text": "A tissue", "correct": False,
             "why": "A tissue is similar cells doing one job. Each of these "
                    "is a whole organ in its own right."},
            {"text": "An organ", "correct": False,
             "why": "Each one of them is an organ. Several organs sharing one "
                    "overall job make the rung above."},
            {"text": "An organism", "correct": False,
             "why": "The organism is the whole living thing. These organs are "
                    "one system inside it."},
            {"text": "An organ system", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b1-05-s05",
        "band": "standard",
        "text": "One palisade cell catches a speck of the light landing on a "
                "leaf, but the palisade layer catches nearly all of it. What "
                "does that show about a tissue?",
        "options": [
            {"text": "That a tissue works only when its cells are of several "
                     "different kinds", "correct": False,
             "why": "A tissue is similar cells, not different ones. Several "
                    "unlike tissues together make an organ."},
            {"text": "That a tissue is simply a larger version of one of its "
                     "cells", "correct": False,
             "why": "A rung up is a different kind of thing, not a bigger "
                    "one. What the layer adds is arrangement — cells side by "
                    "side with no gaps."},
            {"text": "That similar cells packed together can do something "
                     "none of them could do alone", "correct": True},
            {"text": "That each palisade cell must catch far more light than "
                     "it appears to", "correct": False,
             "why": "Each one still catches a speck. The layer works because "
                    "thousands of them stand shoulder to shoulder, leaving "
                    "nothing to get past."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s06",
        "band": "standard",
        "text": "People argue about whether a bone such as your femur is a "
                "tissue or an organ. Why does the argument happen?",
        "options": [
            {"text": "The named bone is an organ; the hard material inside "
                     "it is a tissue, so the wording decides", "correct": True},
            {"text": "Because a femur is far too large to count as a tissue "
                     "and far too simple to count as an organ",
             "correct": False,
             "why": "Size and simplicity set no rungs. The argument is about "
                    "which thing the word bone is naming."},
            {"text": "Because bone is living in a child and not living in an "
                     "adult", "correct": False,
             "why": "Bone contains living cells, blood vessels and nerves "
                    "throughout life. Age has nothing to do with the rung."},
            {"text": "Because nobody has decided which rung bones belong on",
             "correct": False,
             "why": "It has been decided, and both sides are right about "
                    "different things: the femur is an organ, and bone is a "
                    "tissue inside it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s07",
        "band": "standard",
        "text": "Which rung is the brain on, and why?",
        "options": [
            {"text": "An organ system, because it controls the whole body",
             "correct": False,
             "why": "What it controls does not set the rung. The brain is the "
                    "main organ of the nervous system, not the system "
                    "itself."},
            {"text": "A tissue, because it is nerve cells all doing one job",
             "correct": False,
             "why": "It holds more than nerve tissue — blood vessels, "
                    "connective tissue and membranes as well. Several unlike "
                    "tissues together make an organ."},
            {"text": "An organism, because it could survive alone if it were "
                     "kept supplied", "correct": False,
             "why": "An organism is a whole living thing. A brain outside a "
                    "body is an organ with nothing bringing it blood."},
            {"text": "An organ, because it is several different tissues "
                     "working together on one job", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s08",
        "band": "standard",
        "text": "A leaf can make sugar but cannot deliver it anywhere; a stem "
                "can move sugar but cannot make any. What does that tell you "
                "about the rung above the organ?",
        "options": [
            {"text": "That an organ system is several copies of the same "
                     "organ joined together", "correct": False,
             "why": "The shoot is a stem and leaves — different organs doing "
                    "different things. Copies of one organ would add "
                    "nothing."},
            {"text": "That an organ system runs a whole function end to end, "
                     "which no single organ can", "correct": True},
            {"text": "That an organ system is where the real work happens, "
                     "and organs are only its parts", "correct": False,
             "why": "The organs do the work — the leaf really does make the "
                    "sugar. What the system adds is that the separate jobs "
                    "join into one complete function."},
            {"text": "That a leaf and a stem must be tissues, since neither "
                     "can finish the job alone", "correct": False,
             "why": "Both are organs, each built from several tissues. Not "
                    "being self-sufficient is true of every organ, and it is "
                    "why the rung above exists."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b1-05-h05",
        "band": "harder",
        "text": "A student says blood cannot be a tissue, because a tissue is "
                "one kind of cell and blood holds several. What is the best "
                "reply?",
        "options": [
            {"text": "Blood is an organ, because it holds several different "
                     "kinds of cell all working together in one place",
             "correct": False,
             "why": "An organ is several unlike tissues arranged into one "
                    "structure. Blood is one tissue, and it travels through "
                    "organs rather than being one."},
            {"text": "Blood is on none of the levels at all, because a "
                     "liquid cannot be organised", "correct": False,
             "why": "What sets a level is organisation, not solidity. Blood "
                    "is a tissue like any other."},
            {"text": "A tissue is similar cells working on one job, and every "
                     "cell in blood is working on transport", "correct": True},
            {"text": "The student is right, so blood has to be counted as an "
                     "organ system instead", "correct": False,
             "why": "That puts it two rungs above where it belongs. Similar "
                    "cells on one job is a tissue, and blood is one."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h06",
        "band": "harder",
        "text": "The epidermis of a leaf and your skin both cover and "
                "protect. Why are they on different rungs?",
        "options": [
            {"text": "The leaf epidermis is one tissue — one kind of cell, "
                     "one job — and skin is several tissues", "correct": True},
            {"text": "Skin is thicker, and thickness is what moves something "
                     "up a rung", "correct": False,
             "why": "Thickness never sets a rung. Skin is an organ because it "
                    "contains several different tissues — epidermis, "
                    "connective tissue, glands and nerve endings."},
            {"text": "They are on the same rung as each other, because they "
                     "are doing the same protective job", "correct": False,
             "why": "The job does not set the rung; the organisation does. "
                    "One is a single tissue and the other holds several."},
            {"text": "The leaf epidermis is on no rung, because a plant's "
                     "outer layer is not made of cells", "correct": False,
             "why": "It is made of cells, like every other living structure. "
                    "It is a tissue: similar cells, one job."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h07",
        "band": "harder",
        "text": "A single muscle cell shortens by a tiny amount. A whole "
                "muscle lifts your arm. Which statement about that is right?",
        "options": [
            {"text": "The muscle lifts your arm because its cells are far "
                     "bigger than the ones grown in a dish", "correct": False,
             "why": "The cells are the same size either way. What the muscle "
                    "adds is thousands of them pulling together in one "
                    "direction."},
            {"text": "The muscle is on the same rung as the cell, since it is "
                     "only more of the same thing", "correct": False,
             "why": "A rung up is a different kind of thing. Similar cells "
                    "arranged so their pulls add up is a tissue, and a named "
                    "muscle is an organ."},
            {"text": "The cell must be doing something different from what it "
                     "does on its own", "correct": False,
             "why": "It does the same thing either way — it shortens. What "
                    "has changed is that thousands of them are arranged to "
                    "shorten together."},
            {"text": "Thousands of cells arranged to pull the same way is a "
                     "tissue, and the arrangement is what does it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h08",
        "band": "harder",
        "text": "Xylem runs through a plant's roots, its stem and its leaves. "
                "A student says that makes it an organ system, because it "
                "links several organs. What is wrong?",
        "options": [
            {"text": "Nothing is wrong — anything that runs through several "
                     "different organs counts as a system", "correct": False,
             "why": "Running through organs does not make something a system. "
                    "Xylem is similar cells doing one job, which is a "
                    "tissue."},
            {"text": "Xylem is similar cells on one job, so it is a tissue "
                     "sitting inside organs, as muscle does", "correct": True},
            {"text": "Xylem is an organ, because it is one structure running "
                     "the whole length of the plant", "correct": False,
             "why": "Length does not make an organ. An organ is several "
                    "different tissues together, and xylem is one tissue on "
                    "its own."},
            {"text": "Xylem is a tissue in the stem, but becomes part of an "
                     "organ once it reaches the leaf", "correct": False,
             "why": "It is the same tissue wherever it runs. A tissue sitting "
                    "inside an organ is still a tissue — muscle inside your "
                    "stomach is exactly the same."},
        ],
        "figure": None,
    },
]
