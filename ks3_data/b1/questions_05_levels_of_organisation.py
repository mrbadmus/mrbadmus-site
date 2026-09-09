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
                     "different kinds arranged side by side", "correct": False,
             "why": "A tissue is similar cells, not different ones. Several "
                    "unlike tissues together make an organ."},
            {"text": "That a tissue is simply a much larger version of one "
                     "of the cells that make it up", "correct": False,
             "why": "A rung up is a different kind of thing, not a bigger "
                    "one. What the layer adds is arrangement — cells side by "
                    "side with no gaps."},
            {"text": "That similar cells packed together do what none of "
                     "them could do alone", "correct": True},
            {"text": "That each palisade cell catches more light than it "
                     "seems to", "correct": False,
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
            {"text": "An organ system, because it controls the nerves "
                     "running through the body", "correct": False,
             "why": "What it controls does not set the rung. The brain is "
                    "the main organ of the nervous system, not the system "
                    "itself."},
            {"text": "A tissue, because it is nothing but nerve cells, all "
                     "packed together doing one job", "correct": False,
             "why": "It holds more than nerve tissue — blood vessels, "
                    "connective tissue and membranes as well. Several unlike "
                    "tissues together make an organ."},
            {"text": "An organism, because it could survive on its own if it "
                     "were kept supplied with blood and "
                     "oxygen", "correct": False,
             "why": "An organism is a whole living thing. A brain outside a "
                    "body is an organ with nothing bringing it blood."},
            {"text": "An organ, because it is different tissues working "
                     "together", "correct": True},
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
            {"text": "The muscle lifts your arm because each of its cells is "
                     "far bigger than a single cell grown alone in a "
                     "dish", "correct": False,
             "why": "The cells are the same size either way. What the muscle "
                    "adds is thousands of them pulling together in one "
                    "direction."},
            {"text": "The muscle is on the same rung as the cell, since it "
                     "is only more of exactly the same "
                     "thing", "correct": False,
             "why": "A rung up is a different kind of thing. Similar cells "
                    "arranged so their pulls add up is a tissue, and a named "
                    "muscle is an organ."},
            {"text": "The cell must be doing something different from what "
                     "it does alone", "correct": False,
             "why": "It does the same thing either way — it shortens. What "
                    "has changed is that thousands of them are arranged to "
                    "shorten together."},
            {"text": "Thousands of cells pulling the same way is a tissue, "
                     "and the arrangement does it", "correct": True},
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
    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "b1-05-e09",
        "band": "easier",
        "text": "Several whole organs, each doing part of one big job, joined "
                "so that the job gets finished. Which level of organisation "
                "is that?",
        "options": [
            {"text": "A tissue, because all the parts are similar to "
                     "each other", "correct": False,
             "why": "Similar cells on one job make a tissue. Whole organs "
                    "are not similar to each other — a stomach and a liver "
                    "do quite different things."},
            {"text": "An organ, because it is one connected structure",
             "correct": False,
             "why": "An organ is one structure built from several tissues. "
                    "Once you are joining whole organs together you have "
                    "gone a rung higher."},
            {"text": "An organ system", "correct": True},
            {"text": "An organism, because it carries out all seven life "
                     "processes", "correct": False,
             "why": "An organism is the entire living thing. Your "
                    "digestive system is one of several systems inside "
                    "you, not the whole of you."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e10",
        "band": "easier",
        "text": "Which of these best describes an organism?",
        "options": [
            {"text": "A whole living thing, made of organ systems that "
                     "work together", "correct": True},
            {"text": "The largest organ system in a body, such as the "
                     "digestive system", "correct": False,
             "why": "A system is only part of a living thing. Your "
                    "digestive system cannot grow, respond or reproduce on "
                    "its own."},
            {"text": "Any structure made of more than one type of tissue",
             "correct": False,
             "why": "That is the definition of an organ. A stomach is "
                    "several tissues, and a stomach is not an organism."},
            {"text": "A very large group of cells of the same kind",
             "correct": False,
             "why": "Many cells of one kind is a tissue, however many of "
                    "them there are. Size is not what moves you up the "
                    "ladder."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e11",
        "band": "easier",
        "text": "A revision card needs one example of an organ system on it. "
                "What should it say?",
        "options": [
            {"text": "The heart", "correct": False,
             "why": "The heart is an organ — cardiac muscle, valves and "
                    "nerve tissue in one structure. It is the main organ "
                    "of a system, not the system."},
            {"text": "The digestive system", "correct": True},
            {"text": "The lining of your small intestine", "correct": False,
             "why": "That lining is one kind of cell doing one job, so it "
                    "is a tissue. It sits inside an organ rather than "
                    "being a system."},
            {"text": "A red blood cell", "correct": False,
             "why": "A single cell is the bottom rung of the ladder, four "
                    "rungs below a system."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e12",
        "band": "easier",
        "text": "Muscle is called a tissue. What makes it one?",
        "options": [
            {"text": "It is soft and changes shape, which no organ can "
                     "do", "correct": False,
             "why": "Plenty of organs change shape — your stomach and your "
                    "lungs both do. Being soft has nothing to do with "
                    "which rung something is on."},
            {"text": "It is bigger than a cell and smaller than an organ",
             "correct": False,
             "why": "Size is not what the ladder measures. A rung up is a "
                    "different kind of thing, not a bigger one."},
            {"text": "It holds several different kinds of cell in layers",
             "correct": False,
             "why": "Several different tissues arranged together makes an "
                    "organ. A tissue is the opposite: cells of one kind."},
            {"text": "It is many similar cells on one job — shortening",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e13",
        "band": "easier",
        "text": "Your stomach lining holds cells that make acid and enzymes "
                "and do nothing else. What is that layer called?",
        "options": [
            {"text": "Glandular tissue, because the cells are alike and "
                     "share one job", "correct": True},
            {"text": "A gland system, because making acid is a whole job "
                     "on its own", "correct": False,
             "why": "There is no such rung. A group of whole organs on one "
                    "big job is an organ system, and a lining is not a "
                    "group of organs."},
            {"text": "An organ, because the acid is essential to "
                     "digestion", "correct": False,
             "why": "One kind of cell on one job is a tissue, however "
                    "important the job is. An organ needs several unlike "
                    "tissues."},
            {"text": "A specialised cell", "correct": False,
             "why": "One cell is the rung below. This is a whole layer of "
                    "them, and the layer makes far more acid than any "
                    "single cell could."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e14",
        "band": "easier",
        "text": "Epithelial cells line your gut and cover the surface of your "
                "skin. Which statement about epithelium is right?",
        "options": [
            {"text": "It is an organ, because it covers the outside of "
                     "you", "correct": False,
             "why": "Skin is the organ. The epithelium on its outside is "
                    "one of the tissues that skin is built from."},
            {"text": "It is a tissue: similar cells packed into a sheet "
                     "that lines or covers", "correct": True},
            {"text": "It is an organ system, because it turns up in many "
                     "different organs", "correct": False,
             "why": "Turning up in many organs does not promote something. "
                    "Muscle is found all over you too, and muscle is a "
                    "tissue."},
            {"text": "It is not on the ladder, because a lining is only "
                     "a surface", "correct": False,
             "why": "A lining is made of cells doing one job together, "
                    "which is exactly what a tissue is."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e15",
        "band": "easier",
        "text": "Plants have organs, just as animals do. Which of these is "
                "one?",
        "options": [
            {"text": "Xylem", "correct": False,
             "why": "Xylem is a tissue — similar cells on one job, "
                    "carrying water. It sits inside organs rather than "
                    "being one."},
            {"text": "A palisade cell", "correct": False,
             "why": "One cell is the bottom rung, three below the organ."},
            {"text": "The shoot of a plant", "correct": False,
             "why": "The shoot is the stem and every leaf together — "
                    "several organs sharing one job, so it is an organ "
                    "system."},
            {"text": "A leaf", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e16",
        "band": "easier",
        "text": "One root anchors a plant and takes in water. It contains "
                "xylem, phloem and an outer epidermis. Which level is it on?",
        "options": [
            {"text": "A tissue", "correct": False,
             "why": "A tissue is one kind of cell. Three different tissues "
                    "have just been named inside this root."},
            {"text": "A cell", "correct": False,
             "why": "A root is built from millions of cells."},
            {"text": "An organ", "correct": True},
            {"text": "An organ system", "correct": False,
             "why": "One root is an organ. All the roots of a tree "
                    "together are the organ system."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e17",
        "band": "easier",
        "text": "The heart is built from cardiac muscle, valves of connective "
                "tissue and nerve tissue that sets its rhythm. Which level is "
                "it on?",
        "options": [
            {"text": "An organism, because it beats away on its own",
             "correct": False,
             "why": "An organism is a whole living thing. A heart alone "
                    "has nothing feeding it and nothing carrying its waste "
                    "away."},
            {"text": "A tissue, since it is mostly cardiac muscle",
             "correct": False,
             "why": "You have just been told it holds several different "
                    "tissues, and unlike tissues in one structure is "
                    "exactly what an organ means."},
            {"text": "An organ system, because it drives the circulation",
             "correct": False,
             "why": "The heart is the main organ of the circulatory "
                    "system. The system is the heart plus every blood "
                    "vessel and the blood itself."},
            {"text": "An organ", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e18",
        "band": "easier",
        "text": "Your lungs, your windpipe and the muscles that move your "
                "ribs all work on one job: getting oxygen in and carbon "
                "dioxide out. What is that group called?",
        "options": [
            {"text": "The circulatory system", "correct": False,
             "why": "The circulatory system carries oxygen once it is "
                    "already in the blood. Getting it into the blood is a "
                    "different system's job."},
            {"text": "The respiratory system", "correct": True},
            {"text": "Lung tissue", "correct": False,
             "why": "Lung tissue is one kind of cell inside one organ, and "
                    "you have been given several organs working together."},
            {"text": "The digestive system", "correct": False,
             "why": "The digestive system breaks food down. Nothing in "
                    "that list handles food."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e19",
        "band": "easier",
        "text": "Which one of these parts of your circulation sits on the "
                "organ rung?",
        "options": [
            {"text": "Blood", "correct": False,
             "why": "Blood is a tissue — a few kinds of cell in enormous "
                    "numbers, all working on transport."},
            {"text": "Cardiac muscle", "correct": False,
             "why": "Cardiac muscle is one kind of cell doing one job, so "
                    "it is a tissue sitting inside the heart."},
            {"text": "The circulatory system itself", "correct": False,
             "why": "A system is not one of its own organs — it is what "
                    "those organs add up to."},
            {"text": "An artery", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e20",
        "band": "easier",
        "text": "Put the five levels of organisation in order, smallest "
                "first.",
        "options": [
            {"text": "Cell, organ, tissue, organ system, organism",
             "correct": False,
             "why": "A tissue is smaller than an organ — the palisade "
                    "layer sits inside the leaf, not the other way round."},
            {"text": "Cell, tissue, organ system, organ, organism",
             "correct": False,
             "why": "You have swapped the middle two. An organ system "
                    "contains organs, so it comes after them."},
            {"text": "Cell, tissue, organ, organ system, organism",
             "correct": True},
            {"text": "Tissue, cell, organ, organ system, organism",
             "correct": False,
             "why": "The cell is the bottom rung. A tissue is made of "
                    "cells, so it cannot be the smaller of the two."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e21",
        "band": "easier",
        "text": "A student writes the ladder as: cell, tissue, ___, organ "
                "system, organism. What belongs in the gap?",
        "options": [
            {"text": "Organelle", "correct": False,
             "why": "An organelle such as a mitochondrion is part of a "
                    "cell, so it sits below the bottom rung, not in the "
                    "middle."},
            {"text": "Organ", "correct": True},
            {"text": "Population", "correct": False,
             "why": "A population is a group of whole organisms, so it "
                    "comes above the organism rather than inside one."},
            {"text": "Cell membrane", "correct": False,
             "why": "The membrane is part of a single cell, which puts it "
                    "below the ladder altogether."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e22",
        "band": "easier",
        "text": "A student lists the levels as cell, organ, organ system, "
                "organism. Which level have they left out?",
        "options": [
            {"text": "Tissue — cells form tissues before any organ "
                     "exists", "correct": True},
            {"text": "Organelle", "correct": False,
             "why": "An organelle is below the cell, and the ladder starts "
                    "at the cell because that is the smallest living thing "
                    "on it."},
            {"text": "Population", "correct": False,
             "why": "A population sits above the organism, so it is not "
                    "the thing missing from the middle of their list."},
            {"text": "Nothing — cells build an organ directly, so that "
                     "list is already complete", "correct": False,
             "why": "Cells do not build an organ directly. They first form "
                    "tissues, and an organ is several different tissues "
                    "together."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e23",
        "band": "easier",
        "text": "An amoeba is a single cell that feeds, respires, moves and "
                "reproduces by itself. How many of the five levels does it "
                "have?",
        "options": [
            {"text": "All five, because every living thing has all of "
                     "them", "correct": False,
             "why": "The five levels describe bodies built from many "
                    "cells. A one-celled organism never forms tissues, so "
                    "three of the rungs simply do not apply to it."},
            {"text": "Three: cell, tissue and organism", "correct": False,
             "why": "It has no tissue at all — a tissue needs many similar "
                    "cells working together, and there is only one cell."},
            {"text": "None, because one cell cannot be an organism",
             "correct": False,
             "why": "It is an organism: it carries out all seven life "
                    "processes on its own, which is the test."},
            {"text": "Two: it is a cell, and that cell is the whole "
                     "organism", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e24",
        "band": "easier",
        "text": "Which level of organisation is a mitochondrion on?",
        "options": [
            {"text": "Cell, because it is a small working unit in its "
                     "own right", "correct": False,
             "why": "A mitochondrion is inside a cell. It is a part of "
                    "one, not one of its own."},
            {"text": "Tissue, because there are thousands of them in "
                     "every single cell", "correct": False,
             "why": "A tissue is many similar cells, and a mitochondrion "
                    "is far smaller than a single cell."},
            {"text": "Organ, because it has a definite job to do",
             "correct": False,
             "why": "Having a job does not put something on the ladder. An "
                    "organ is several tissues, and a mitochondrion is not "
                    "even one whole cell."},
            {"text": "None — it is part of a cell, below the bottom rung",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e25",
        "band": "easier",
        "text": "Blood carries red cells, white cells and platelets in a "
                "liquid, and all of them are on the transport job. Which "
                "level is blood on?",
        "options": [
            {"text": "Cell, because it is made of blood cells",
             "correct": False,
             "why": "It is made of cells, but so is every rung above the "
                    "cell. The rung names what those cells are arranged "
                    "into."},
            {"text": "Tissue", "correct": True},
            {"text": "Organ, because it holds several kinds of cell",
             "correct": False,
             "why": "An organ is several different tissues, not several "
                    "kinds of cell. Blood's cells all work on one job, so "
                    "blood is one tissue."},
            {"text": "Not on the ladder, because blood is a liquid",
             "correct": False,
             "why": "The ladder measures organisation, not solidity. A "
                    "liquid tissue is still a tissue."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e26",
        "band": "easier",
        "text": "Which pair are both plant tissues?",
        "options": [
            {"text": "A leaf and a root", "correct": False,
             "why": "Both are organs — each is several different tissues "
                    "arranged into one structure with one job."},
            {"text": "Xylem and phloem", "correct": True},
            {"text": "The shoot and the root system", "correct": False,
             "why": "Both are organ systems: several whole organs working "
                    "on one overall job."},
            {"text": "A palisade cell and a chloroplast", "correct": False,
             "why": "A palisade cell is on the cell rung and a chloroplast "
                    "is below the ladder altogether."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e27",
        "band": "easier",
        "text": "A flower holds petals, a stigma, an ovary and the tissue "
                "that makes pollen, all on one job. Which level is a flower "
                "on?",
        "options": [
            {"text": "A tissue, because every part of it belongs to the "
                     "same flower", "correct": False,
             "why": "Several different tissues have just been named inside "
                    "it, and unlike tissues in one structure is what makes "
                    "an organ."},
            {"text": "An organ system", "correct": False,
             "why": "The flower is one organ. The plant's reproductive "
                    "system is the flower together with the fruit and "
                    "seeds that follow it."},
            {"text": "A single specialised cell", "correct": False,
             "why": "A flower is built from millions of cells."},
            {"text": "An organ", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e28",
        "band": "easier",
        "text": "A student thinks the word tissue only ever means muscle. "
                "Which of these is also a tissue?",
        "options": [
            {"text": "The kidney", "correct": False,
             "why": "A kidney is an organ — several different tissues "
                    "built into one structure that cleans the blood."},
            {"text": "The nervous system", "correct": False,
             "why": "That is an organ system: the brain, the spinal cord "
                    "and the nerves, all on one job."},
            {"text": "Bone", "correct": True},
            {"text": "A white blood cell", "correct": False,
             "why": "One cell is the rung below a tissue, however "
                    "specialised it is."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e29",
        "band": "easier",
        "text": "The small intestine has a lining that absorbs food, muscle "
                "that pushes it along and connective tissue holding it "
                "together. What does that make it?",
        "options": [
            {"text": "An organ, because unlike tissues are built into "
                     "one structure with one job", "correct": True},
            {"text": "A tissue, because the whole tube is made of the "
                     "same material from end to end", "correct": False,
             "why": "Three different tissues have just been named in it, "
                    "and a tissue is cells of one kind only."},
            {"text": "An organ system, because food passes right through "
                     "it", "correct": False,
             "why": "The small intestine is one organ of the digestive "
                    "system. The system is the whole chain from mouth to "
                    "intestine."},
            {"text": "An organism, because it is alive", "correct": False,
             "why": "Every rung on the ladder is alive. An organism is the "
                    "whole living thing, not one part inside it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e30",
        "band": "easier",
        "text": "Which of the four things below is a whole organism?",
        "options": [
            {"text": "A daisy plant", "correct": True},
            {"text": "The root system of that daisy", "correct": False,
             "why": "Many roots on one job is an organ system — one rung "
                    "below the whole plant."},
            {"text": "A petal", "correct": False,
             "why": "A petal is part of one organ, the flower, and cannot "
                    "live by itself."},
            {"text": "Palisade tissue from a daisy leaf", "correct": False,
             "why": "Similar cells on one job is a tissue, three rungs "
                    "below the organism."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e31",
        "band": "easier",
        "text": "Which organ system does your brain belong to?",
        "options": [
            {"text": "The circulatory system, because blood reaches it "
                     "constantly", "correct": False,
             "why": "Blood supplies the brain, but supplying an organ does "
                    "not make it part of that system. The brain's job is "
                    "carrying signals."},
            {"text": "The skeletal system, because the skull is built "
                     "around it", "correct": False,
             "why": "The skull protects the brain and the skull is part of "
                    "the skeleton. The brain itself is not bone."},
            {"text": "The nervous system", "correct": True},
            {"text": "None — the brain is an organ system all by itself",
             "correct": False,
             "why": "The brain is one organ. The nervous system is the "
                    "brain, the spinal cord and every nerve, working "
                    "together."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-e32",
        "band": "easier",
        "text": "How do an organ and an organ system fit together?",
        "options": [
            {"text": "A system contains several organs", "correct": True},
            {"text": "An organ contains several systems", "correct": False,
             "why": "It is the other way round. Your stomach sits inside "
                    "the digestive system, not the reverse."},
            {"text": "They are the same rung under two different names",
             "correct": False,
             "why": "Each rung can do something the rung below cannot. One "
                    "leaf photosynthesises; the shoot also delivers what "
                    "the leaf makes."},
            {"text": "A system is one organ that has grown much larger",
             "correct": False,
             "why": "That is the size error. A rung up is a different kind "
                    "of thing, not a bigger version of the same thing."},
        ],
        "figure": None,
    },
    # ── standard · MRB-338 expansion ────────────────────────────────────────
    {
        "id": "b1-05-s09",
        "band": "standard",
        "text": "A student writes: 'The digestive system is the organ that "
                "breaks down your food.' What is wrong with that sentence?",
        "options": [
            {"text": "Nothing is wrong, because breaking food down is "
                     "one single job", "correct": False,
             "why": "One job does not make one organ. The job is shared "
                    "out along a chain of organs, each doing a different "
                    "part of it."},
            {"text": "It is a chain of organs — mouth, stomach, "
                     "intestines, liver — so it is a system", "correct": True},
            {"text": "It should say tissue, because the gut lining is "
                     "where all the digesting really happens",
             "correct": False,
             "why": "The lining is one tissue inside one organ. Naming it "
                    "moves you two rungs down, when the sentence was "
                    "already one rung too low."},
            {"text": "Digestion is chemical, so it belongs on no rung at "
                     "all", "correct": False,
             "why": "The chemistry happens inside structures, and those "
                    "structures are on the ladder like everything else in "
                    "a body."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s10",
        "band": "standard",
        "text": "A student says plants cannot have organs, because organs are "
                "an animal thing. How would you show they are wrong?",
        "options": [
            {"text": "You cannot — plants really do stop at the tissue "
                     "level", "correct": False,
             "why": "A plant has roots, a stem, leaves and flowers, and "
                    "each one is several different tissues on one job."},
            {"text": "Plants have organs only while they are flowering",
             "correct": False,
             "why": "A leaf is an organ in every season. Flowering changes "
                    "what the plant is doing, not how it is built."},
            {"text": "Every plant cell counts as an organ, because it "
                     "works alone", "correct": False,
             "why": "That collapses four rungs into one. A cell is a cell "
                    "whether it belongs to a plant or to you."},
            {"text": "Name a leaf: palisade, spongy, epidermis and vein "
                     "tissue, on one job", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s11",
        "band": "standard",
        "text": "Why is a stomach counted as an organ rather than as a very "
                "large tissue?",
        "options": [
            {"text": "It holds unlike tissues — muscle, glandular, "
                     "connective, nerve — that need each other",
             "correct": True},
            {"text": "It is far too big to count as a tissue, because a "
                     "tissue is always a thin layer of cells",
             "correct": False,
             "why": "This is the size error. A whale's muscle is enormous "
                    "and still a tissue, because every cell in it is on "
                    "the same job."},
            {"text": "It is hollow, and a tissue can never have a space "
                     "inside it", "correct": False,
             "why": "Shape does not decide the rung. What decides it is "
                    "whether the parts are alike or unlike."},
            {"text": "It holds food inside it, and a tissue never comes "
                     "into direct contact with what you eat",
             "correct": False,
             "why": "The gut lining touches food constantly, and that "
                    "lining is a tissue."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s12",
        "band": "standard",
        "text": "The windpipe is a tube with rings of cartilage, a muscle "
                "layer and a lining that traps dust. Which level is it on, "
                "and where does it belong?",
        "options": [
            {"text": "A tissue inside the lungs, since it is only a tube",
             "correct": False,
             "why": "Three different tissues have just been named in it, "
                    "and unlike tissues in one structure is an organ."},
            {"text": "An organ system of its own, because air passes "
                     "through it", "correct": False,
             "why": "Something a substance passes through is not "
                    "automatically a system. The windpipe is one organ of "
                    "a system with several."},
            {"text": "An organ of the respiratory system", "correct": True},
            {"text": "An organ of the digestive system, since it starts "
                     "at the throat", "correct": False,
             "why": "It carries air, not food. The food tube behind it, "
                    "the oesophagus, is the digestive one."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s13",
        "band": "standard",
        "text": "Cardiac muscle is found only in the heart; skeletal muscle "
                "is found all over the body. Which rung is each of them on?",
        "options": [
            {"text": "Cardiac muscle is an organ and skeletal muscle is "
                     "a tissue", "correct": False,
             "why": "The heart is the organ. The cardiac muscle in its "
                    "wall is one of the tissues that heart is built from."},
            {"text": "Both are tissues, because each is similar cells on "
                     "one job", "correct": True},
            {"text": "Skeletal muscle is an organ system, because it "
                     "reaches the whole body", "correct": False,
             "why": "Being spread out does not promote a tissue. The "
                    "muscular system is the named muscles working "
                    "together, not the material itself."},
            {"text": "Cardiac muscle is a tissue and skeletal muscle is "
                     "an organ", "correct": False,
             "why": "Both are similar cells on one job. A named muscle "
                    "such as the biceps is an organ; the muscle tissue in "
                    "it is not."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s14",
        "band": "standard",
        "text": "An eye has a lens, a retina of light-sensitive cells, "
                "muscles that change the lens shape and a nerve at the back. "
                "Which statement fits?",
        "options": [
            {"text": "The eye is a tissue and the retina is one of its "
                     "cells", "correct": False,
             "why": "The retina is a whole layer of similar cells, not one "
                    "cell, and the eye is built from several such layers."},
            {"text": "The eye is an organ system and the retina is one "
                     "of its organs", "correct": False,
             "why": "The eye is a single structure. The nervous system is "
                    "the system it reports to."},
            {"text": "Both the eye and the retina are organs, because "
                     "both have jobs", "correct": False,
             "why": "Having a job does not set the rung. The retina is one "
                    "kind of cell on one job, which makes it a tissue."},
            {"text": "The eye is an organ and the retina is one of the "
                     "tissues inside it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s15",
        "band": "standard",
        "text": "An oak tree is an organism. What is one of its branches?",
        "options": [
            {"text": "Part of an organ system — the shoot — carrying "
                     "leaves and moving water and sugar", "correct": True},
            {"text": "An organism of its own, because a cutting taken "
                     "from it can grow into a whole new tree",
             "correct": False,
             "why": "A cutting becomes an organism only after it grows "
                    "roots. On the tree it is part of one."},
            {"text": "A tissue, because it is mostly wood", "correct": False,
             "why": "The wood in it is xylem tissue, but the branch also "
                    "carries phloem, bark and buds."},
            {"text": "An organelle, because it is one working part "
                     "inside a much bigger living structure",
             "correct": False,
             "why": "An organelle is a part inside a single cell. A branch "
                    "holds billions of cells."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s16",
        "band": "standard",
        "text": "A revision poster reads: 'Cells build organs, and organs "
                "build organisms.' Which rungs has it dropped?",
        "options": [
            {"text": "Only the tissue, and the ladder still works "
                     "without it", "correct": False,
             "why": "Two rungs are gone, and the missing tissue rung is "
                    "the one that explains what an organ actually is."},
            {"text": "Only the organ system, since tissues are optional "
                     "in animals", "correct": False,
             "why": "Tissues are not optional. Every organ you have is "
                    "built from them."},
            {"text": "The tissue and the organ system", "correct": True},
            {"text": "None — the poster has simply used shorter words",
             "correct": False,
             "why": "The words are not shorter, the ladder is. Cells form "
                    "tissues first, and organs work in systems."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s17",
        "band": "standard",
        "text": "Complete this chain: a cardiac muscle cell, then cardiac "
                "muscle, then ___, then the circulatory system.",
        "options": [
            {"text": "The chest, because that is where the muscle sits",
             "correct": False,
             "why": "A body region is not a rung. The ladder names how the "
                    "parts are organised, not where they are."},
            {"text": "Blood, because the muscle pushes blood along",
             "correct": False,
             "why": "Blood is a tissue, so it belongs on the rung you have "
                    "already filled, not the next one up."},
            {"text": "A whole muscular system, then the circulation",
             "correct": False,
             "why": "You would be skipping a rung. Cardiac muscle is built "
                    "into one organ first, and that organ then joins a "
                    "system."},
            {"text": "The heart", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s18",
        "band": "standard",
        "text": "Complete this chain: a palisade cell, then ___, then a leaf, "
                "then the shoot.",
        "options": [
            {"text": "The palisade layer", "correct": True},
            {"text": "A chloroplast, because that is what does the work",
             "correct": False,
             "why": "A chloroplast is inside the cell you started with, so "
                    "this goes down the ladder rather than up."},
            {"text": "The whole plant, because leaves belong to it",
             "correct": False,
             "why": "The whole plant is the organism, and it comes after "
                    "the shoot rather than before the leaf."},
            {"text": "Another palisade cell, because tissues are cells "
                     "added up", "correct": False,
             "why": "Two cells is still the cell rung. What makes the "
                    "tissue is thousands of them packed into one working "
                    "layer."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s19",
        "band": "standard",
        "text": "A heart in perfect condition can beat, but on its own it "
                "cannot move blood around a body. Why not?",
        "options": [
            {"text": "Because a heart is only a tissue, and one tissue "
                     "can never finish a whole job by itself",
             "correct": False,
             "why": "A heart is an organ — several tissues. The reason it "
                    "cannot finish the job lies above it, not below."},
            {"text": "Because its cells stop working the moment it is "
                     "not in a body", "correct": False,
             "why": "Heart muscle keeps contracting for a while outside a "
                    "body. The failure is not that the cells stop."},
            {"text": "Because pumping is only part of the job: the "
                     "vessels and blood complete it", "correct": True},
            {"text": "Because a heart needs a second heart alongside it "
                     "before blood can move anywhere", "correct": False,
             "why": "A system is different organs sharing a job, not more "
                    "copies of the same one."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s20",
        "band": "standard",
        "text": "Yeast is a single-celled organism used to make bread rise. "
                "Which of the five levels are missing from it?",
        "options": [
            {"text": "It has no organism level, because one cell is too "
                     "small to count", "correct": False,
             "why": "Size is not the test. It feeds, respires and "
                    "reproduces on its own, so it is an organism."},
            {"text": "It has no tissue, organ or organ system level",
             "correct": True},
            {"text": "It has no cell level, since the whole thing is the "
                     "organism", "correct": False,
             "why": "It is a cell and an organism at the same time. Being "
                    "one does not cancel the other."},
            {"text": "It has none of the levels, because yeast is a "
                     "fungus rather than a plant", "correct": False,
             "why": "The ladder describes every living thing, whichever "
                    "kingdom it belongs to."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s21",
        "band": "standard",
        "text": "A student writes that bone is a cell. What has gone wrong in "
                "their thinking?",
        "options": [
            {"text": "Nothing — bone cells are the only living part, so "
                     "bone is a cell", "correct": False,
             "why": "Bone cells are living, but the word bone names the "
                    "whole material they build and maintain together."},
            {"text": "Bone should be called an organ system, because the "
                     "skeleton is one", "correct": False,
             "why": "The skeleton is the system and a named bone is an "
                    "organ. The material itself is a rung lower again."},
            {"text": "Bone is not on the ladder at all, because it is "
                     "hard material rather than something living",
             "correct": False,
             "why": "Bone is alive: it has cells, a blood supply and "
                    "nerves, and it repairs itself after a break."},
            {"text": "Bone is many similar cells with the hard material "
                     "they make, so it is a tissue", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s22",
        "band": "standard",
        "text": "The lining of the small intestine is folded into millions of "
                "tiny finger shapes. Why is that lining still only a tissue?",
        "options": [
            {"text": "Because folding is a shape, and only flat layers "
                     "count as tissues", "correct": False,
             "why": "Shape has nothing to do with it. Tissues fold, coil "
                    "and branch all the time."},
            {"text": "Because its cells are alike and share one job, "
                     "absorbing food", "correct": True},
            {"text": "Because it is inside an organ, and nothing inside "
                     "an organ can be a tissue", "correct": False,
             "why": "Tissues are exactly what organs are made of, so being "
                    "inside one is expected."},
            {"text": "Because it does not move, and organs are the parts "
                     "that move", "correct": False,
             "why": "Movement is not the test either — your brain barely "
                    "moves and it is an organ."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s23",
        "band": "standard",
        "text": "The pancreas releases digestive enzymes into the gut and "
                "also releases insulin into the blood. What does that show?",
        "options": [
            {"text": "One organ can belong to more than one organ system",
             "correct": True},
            {"text": "The pancreas must be an organ system of its own, "
                     "since it does two jobs", "correct": False,
             "why": "A system is several organs. Doing two jobs does not "
                    "split one organ into several."},
            {"text": "The pancreas is a tissue, because each job is done "
                     "by one kind of cell", "correct": False,
             "why": "Two different kinds of cell, in different tissues, is "
                    "precisely what makes it an organ."},
            {"text": "Organ systems must overlap completely, sharing all "
                     "of their organs", "correct": False,
             "why": "They overlap only here and there. Your lungs belong "
                    "to the respiratory system alone."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s24",
        "band": "standard",
        "text": "Which pair correctly matches an organ to a system it belongs "
                "to?",
        "options": [
            {"text": "Blood, and the circulatory system", "correct": False,
             "why": "The match is right but the rung is not: blood is a "
                    "tissue, not an organ."},
            {"text": "The stomach, and the respiratory system",
             "correct": False,
             "why": "The stomach is an organ, but it belongs to the "
                    "digestive system. Nothing in it handles air."},
            {"text": "The kidney, and the excretory system", "correct": True},
            {"text": "Xylem, and the plant's shoot", "correct": False,
             "why": "Xylem is a tissue running through the organs of the "
                    "shoot, rather than an organ of it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s25",
        "band": "standard",
        "text": "A leaf traps light, lets carbon dioxide in and keeps water "
                "from escaping too fast. Why does one leaf need several "
                "tissues to manage that?",
        "options": [
            {"text": "It does not — palisade tissue alone could do all "
                     "three if there were enough of it", "correct": False,
             "why": "More of one tissue cannot do a job that tissue is not "
                    "built for. Palisade cells trap light and nothing "
                    "else."},
            {"text": "No single tissue does all three, so palisade, "
                     "epidermis and vein tissue divide the work",
             "correct": True},
            {"text": "Because the tissues take turns, one working while "
                     "the others rest", "correct": False,
             "why": "They work at the same time, not in turns. Trapping "
                    "light is useless without water arriving as it "
                    "happens."},
            {"text": "Because a leaf is thin, and thin structures always "
                     "need several tissues", "correct": False,
             "why": "Thickness decides nothing. What decides it is that "
                    "the job has several unlike parts to it."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s26",
        "band": "standard",
        "text": "A root hair cell, the root's epidermis, one root, and the "
                "root system. Which of those is the organ?",
        "options": [
            {"text": "One root", "correct": True},
            {"text": "The root's epidermis, because it is the root's "
                     "outer boundary", "correct": False,
             "why": "The epidermis is one kind of cell on one job, which "
                    "makes it a tissue inside the root."},
            {"text": "The root system, because it does the whole job of "
                     "taking up water", "correct": False,
             "why": "That is the rung above: many roots, each an organ, "
                    "sharing one overall job."},
            {"text": "The root hair cell, because it is where water "
                     "actually enters", "correct": False,
             "why": "Doing the important step does not move a cell up a "
                    "rung. It is still one cell."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s27",
        "band": "standard",
        "text": "Food is chewed, then churned in acid, then broken down "
                "further, then absorbed. Why is that run by a system rather "
                "than by one long organ?",
        "options": [
            {"text": "Because a single organ is never longer than a few "
                     "centimetres, and the gut is metres long",
             "correct": False,
             "why": "Length is not the point. The small intestine alone is "
                    "several metres long and is one organ."},
            {"text": "Because each organ has to finish before the next "
                     "one is built", "correct": False,
             "why": "All of them exist at once. What passes along the "
                    "chain is the food, not the building work."},
            {"text": "Because the steps need different structures, so "
                     "different organs handle different parts",
             "correct": True},
            {"text": "Because organs cannot touch one another, so a gap "
                     "has to be left between each of them", "correct": False,
             "why": "They are joined end to end. Being connected is what "
                    "lets the food move through in order."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s28",
        "band": "standard",
        "text": "Your femur is one bone; your skeleton is 206 of them, plus "
                "the joints and ligaments that link them. Which rungs are "
                "those two on?",
        "options": [
            {"text": "The femur is a tissue and the skeleton is an organ",
             "correct": False,
             "why": "Bone tissue is the material. A named bone contains "
                    "that tissue plus marrow, vessels and nerves, so it is "
                    "an organ."},
            {"text": "Both are organs, because both are made of bone",
             "correct": False,
             "why": "Being made of the same material does not put two "
                    "things on the same rung — bone tissue and a whole "
                    "femur are both bone, and they are a rung apart."},
            {"text": "The femur is an organ and the skeleton is an organ "
                     "system", "correct": True},
            {"text": "The femur is an organ and the skeleton is an "
                     "organism", "correct": False,
             "why": "An organism is a whole living thing. A skeleton "
                    "cannot feed, respire or reproduce on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s29",
        "band": "standard",
        "text": "An artery wall has a muscle layer, an elastic layer and a "
                "smooth inner lining. What does that make an artery?",
        "options": [
            {"text": "An organ, because unlike tissues are arranged into "
                     "one structure", "correct": True},
            {"text": "A tissue, because its only job is carrying blood",
             "correct": False,
             "why": "One job does not make one tissue. The test is whether "
                    "the parts are alike, and three unlike layers have "
                    "just been named."},
            {"text": "An organ system, because arteries reach every part "
                     "of the body", "correct": False,
             "why": "Reaching far does not promote something. The "
                    "circulatory system is the arteries, veins, heart and "
                    "blood together."},
            {"text": "Not on the ladder, because a vessel is only a "
                     "container", "correct": False,
             "why": "It is living tissue that squeezes and stretches, not "
                    "a pipe laid through you."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s30",
        "band": "standard",
        "text": "Which plant structure sits on the same rung as your stomach?",
        "options": [
            {"text": "A chloroplast, because both hold what does the "
                     "work", "correct": False,
             "why": "A chloroplast is part of one cell, which is below the "
                    "bottom rung altogether."},
            {"text": "A leaf", "correct": True},
            {"text": "Xylem, because both move material through the body",
             "correct": False,
             "why": "Xylem is a tissue — similar cells on one job — so it "
                    "sits two rungs below the stomach."},
            {"text": "The whole shoot, because both handle food for the "
                     "organism", "correct": False,
             "why": "The shoot is several organs together, so it matches "
                    "your digestive system rather than your stomach."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s31",
        "band": "standard",
        "text": "Gut lining cells scattered in a dish absorb a little sugar; "
                "the same number of cells left as an intact lining absorb far "
                "more. Why?",
        "options": [
            {"text": "Because the scattered cells slowly forget how to "
                     "absorb", "correct": False,
             "why": "They keep the same machinery. Nothing about the cells "
                    "themselves has changed."},
            {"text": "Because cells only work while they are touching "
                     "another cell of the same kind", "correct": False,
             "why": "Single cells work perfectly well alone — an amoeba "
                    "spends its whole life doing so."},
            {"text": "Because a lining is a continuous folded sheet with "
                     "food held against it", "correct": True},
            {"text": "Because a dish holds less sugar than a gut does",
             "correct": False,
             "why": "The comparison uses the same cells and the same "
                    "sugar. Only the arrangement is different."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-s32",
        "band": "standard",
        "text": "Put these four in order, smallest first: a human, muscle "
                "tissue, the digestive system, the stomach.",
        "options": [
            {"text": "The stomach, muscle tissue, the digestive system, "
                     "a human", "correct": False,
             "why": "Muscle tissue is one of the tissues inside the "
                    "stomach, so it comes before it and not after."},
            {"text": "Muscle tissue, the digestive system, the stomach, "
                     "a human", "correct": False,
             "why": "The stomach is one organ of the digestive system, so "
                    "the system comes after the stomach."},
            {"text": "The digestive system, the stomach, muscle tissue, "
                     "a human", "correct": False,
             "why": "This is the ladder upside down at the top and right "
                    "at the bottom. Tissue is the smallest of the four."},
            {"text": "Muscle tissue, the stomach, the digestive system, "
                     "a human", "correct": True},
        ],
        "figure": None,
    },
    # ── harder · MRB-338 expansion ──────────────────────────────────────────
    {
        "id": "b1-05-h09",
        "band": "harder",
        "text": "A newspaper reports that a patient has received 'a new "
                "circulatory system' after a heart transplant. What have they "
                "actually received?",
        "options": [
            {"text": "One organ — the patient's own vessels and blood "
                     "are unchanged", "correct": True},
            {"text": "A whole organ system, because the heart drives the "
                     "circulation", "correct": False,
             "why": "Driving a system does not make an organ into one. "
                    "Every artery, vein and drop of blood is unchanged."},
            {"text": "A tissue, because a heart is essentially cardiac "
                     "muscle", "correct": False,
             "why": "Cardiac muscle is one of its tissues. Valves, vessels "
                    "and nerve tissue came with it too."},
            {"text": "Nothing on the ladder, because a donated part is "
                     "no longer alive", "correct": False,
             "why": "A transplanted heart is living tissue throughout, "
                    "which is exactly why it has to be kept cold and moved "
                    "fast."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h10",
        "band": "harder",
        "text": "A jellyfish has nerve tissue and muscle tissue but no heart, "
                "no lungs and no gut wall of layered organs. What does that "
                "tell you about the five levels?",
        "options": [
            {"text": "That the jellyfish is not really an organism, "
                     "since it misses three rungs", "correct": False,
             "why": "It feeds, moves, responds and reproduces, so it is an "
                    "organism whatever it is built from."},
            {"text": "That the five levels must be wrong, because a real "
                     "animal does not fit them", "correct": False,
             "why": "The levels are not a rule every animal has to obey. "
                    "They name ways a body can be organised, and this one "
                    "uses the first three."},
            {"text": "That the rungs describe how a body is built, and "
                     "not every body uses all of them", "correct": True},
            {"text": "That the ladder applies only to animals with bones",
             "correct": False,
             "why": "It applies to every living thing, including plants, "
                    "which have no bones at all."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h11",
        "band": "harder",
        "text": "Xylem is found in a plant's roots and also in its leaves. "
                "Which statement about that is right?",
        "options": [
            {"text": "It is a tissue in the root and becomes part of an "
                     "organ in the leaf", "correct": False,
             "why": "It is a tissue in both. Sitting inside an organ is "
                    "what a tissue does — it does not change rung by "
                    "moving."},
            {"text": "It is really two different tissues that happen to "
                     "share a name", "correct": False,
             "why": "It is one tissue, continuous from root tip to leaf, "
                    "which is why water can travel the whole way."},
            {"text": "It must be an organ system, since it connects "
                     "several organs", "correct": False,
             "why": "Connecting organs does not promote a tissue. Blood "
                    "runs through every organ you have and stays a tissue."},
            {"text": "It is one tissue, appearing inside two different "
                     "organs", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h12",
        "band": "harder",
        "text": "Two students argue. One says the skeleton is an organ; the "
                "other says it is an organ system. Who is right, and why?",
        "options": [
            {"text": "The first, because the skeleton is one connected "
                     "framework", "correct": False,
             "why": "Being connected is not the test. The bones are "
                    "separate organs joined at joints, each with its own "
                    "blood supply and marrow."},
            {"text": "The second: each bone is an organ, and the bones "
                     "together share one job", "correct": True},
            {"text": "Neither, because bone is a tissue and tissues have "
                     "no rung above them", "correct": False,
             "why": "Bone tissue is a tissue, but the ladder carries on "
                    "above it — that is the whole point of the rungs."},
            {"text": "Both, because organ and organ system mean the same "
                     "at this size", "correct": False,
             "why": "They never mean the same. An organ system does "
                    "something no single organ in it can do alone."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h13",
        "band": "harder",
        "text": "Which list runs from smallest to largest and contains "
                "nothing that is off the ladder?",
        "options": [
            {"text": "Chloroplast, palisade cell, palisade layer, leaf, "
                     "shoot", "correct": False,
             "why": "The chloroplast is part of a cell, which puts it "
                    "below the bottom rung, so this list starts off the "
                    "ladder."},
            {"text": "Palisade cell, leaf, palisade layer, shoot, whole "
                     "plant", "correct": False,
             "why": "The palisade layer sits inside the leaf, so it cannot "
                    "come after it."},
            {"text": "Palisade cell, palisade layer, leaf, shoot, whole "
                     "plant", "correct": True},
            {"text": "Palisade cell, palisade layer, leaf, whole plant, "
                     "woodland", "correct": False,
             "why": "A woodland is a community of many organisms, so this "
                    "list runs past the five levels rather than staying "
                    "inside them."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h14",
        "band": "harder",
        "text": "Why do biologists say the respiratory system, rather than "
                "simply saying the lungs?",
        "options": [
            {"text": "Because breathing needs the windpipe and rib "
                     "muscles too, which the lungs do not contain",
             "correct": True},
            {"text": "Because there are two lungs, and any pair of "
                     "matching organs in a body is called a system",
             "correct": False,
             "why": "Two of the same organ is not a system. You have two "
                    "lungs and one windpipe, and the system needs both."},
            {"text": "Because the lungs are really a tissue, so the "
                     "longer name is there to describe the organ",
             "correct": False,
             "why": "A lung is an organ: airways, blood vessels and "
                    "elastic tissue built into one structure."},
            {"text": "Because system and organ mean the same thing in "
                     "medicine", "correct": False,
             "why": "They are two different rungs. A lung alone cannot "
                    "draw air in — nothing would move the ribs."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h15",
        "band": "harder",
        "text": "A student says a plant's xylem and phloem are its "
                "circulatory system. What is right about that, and what is "
                "wrong?",
        "options": [
            {"text": "It is right in every way, since both of them carry "
                     "the substances a living thing needs around it",
             "correct": False,
             "why": "The job is comparable, but the rung is not, and there "
                    "is no pump anywhere in a plant."},
            {"text": "It is wrong in every way, because plants move "
                     "nothing around at all", "correct": False,
             "why": "They move a great deal: water up from the roots and "
                    "sugar out from the leaves, all day."},
            {"text": "It is wrong because xylem and phloem are organs, "
                     "and your blood is a tissue", "correct": False,
             "why": "It is the other way about. Xylem and phloem are "
                    "tissues, and your heart and vessels are the organs."},
            {"text": "The transport job matches, but xylem and phloem "
                     "are tissues, and a plant has no pump", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h16",
        "band": "harder",
        "text": "A burn destroys the epidermis of a patch of skin but leaves "
                "the layers beneath it healthy. What has been lost, in terms "
                "of the levels?",
        "options": [
            {"text": "A whole organ, because skin counts as one organ "
                     "and a patch of it has now been destroyed",
             "correct": False,
             "why": "The organ is damaged, not lost — the tissues "
                    "underneath are intact and can rebuild the surface."},
            {"text": "One tissue of an organ, so the organ still exists "
                     "but cannot keep water in", "correct": True},
            {"text": "An organ system, because the skin covers the whole "
                     "body", "correct": False,
             "why": "Covering a lot of ground does not promote an organ. "
                    "Skin is one organ, however large it is."},
            {"text": "Nothing on the ladder, since the epidermis is only "
                     "dead surface", "correct": False,
             "why": "The epidermis is a living tissue that constantly "
                    "renews itself, and it is what stops water escaping."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h17",
        "band": "harder",
        "text": "An artery is replaced by a rigid plastic tube of exactly the "
                "same width. Blood still flows through it. What is lost?",
        "options": [
            {"text": "Nothing at all, so long as the new tube has "
                     "exactly the same width and length as the artery "
                     "had", "correct": False,
             "why": "Width is only one of the things an artery provides. "
                    "The wall itself does work on every heartbeat."},
            {"text": "The blood stops moving, because plastic cannot "
                     "carry blood", "correct": False,
             "why": "Blood does flow through the tube. The failure is "
                    "subtler than a blockage."},
            {"text": "The muscle and elastic tissues, so the wall no "
                     "longer stretches and recoils to smooth the flow",
             "correct": True},
            {"text": "The circulatory system, because losing any one of "
                     "its organs brings the whole system to a stop",
             "correct": False,
             "why": "A system carries on with one part replaced — that is "
                    "exactly why such operations are done."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h18",
        "band": "harder",
        "text": "Is it fair to say an amoeba is on the cell rung and the "
                "organism rung at the same time?",
        "options": [
            {"text": "Yes: one cell carrying out every life process is "
                     "both at once", "correct": True},
            {"text": "No, because a thing can only ever sit on one rung "
                     "of the ladder", "correct": False,
             "why": "The rungs describe organisation, not membership of a "
                    "club. With one cell doing everything, two "
                    "descriptions fit the same object."},
            {"text": "No, because an amoeba is a cell and nothing more",
             "correct": False,
             "why": "It feeds, respires, responds and reproduces by "
                    "itself, which is what an organism does."},
            {"text": "Yes, and it is also a tissue, since it is doing a "
                     "tissue's job", "correct": False,
             "why": "A tissue needs many similar cells. One cell cannot be "
                    "a tissue however hard it works."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h19",
        "band": "harder",
        "text": "A student defines an organ as 'any named part inside a "
                "body'. Give the strongest objection to that definition.",
        "options": [
            {"text": "It is too narrow, because plants have organs as "
                     "well, and nobody calls a plant a body",
             "correct": False,
             "why": "That is a fair quibble about wording, but the "
                    "definition fails for a much bigger reason than which "
                    "kingdom it covers."},
            {"text": "It is fine, because everything inside a body has a "
                     "name and a job", "correct": False,
             "why": "Then blood, bone, xylem and a mitochondrion would all "
                    "be organs, and they sit on three different rungs."},
            {"text": "It is wrong because organs must be hollow, and "
                     "plenty of named parts are solid all the way "
                     "through", "correct": False,
             "why": "Hollowness is not part of any definition. The brain "
                    "and the liver are solid organs."},
            {"text": "Named parts include tissues and organelles, so it "
                     "collects three rungs into one word", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h20",
        "band": "harder",
        "text": "The definition of a tissue says similar cells, not identical "
                "cells. Why does that single word matter?",
        "options": [
            {"text": "It does not matter, because similar and identical "
                     "mean exactly the same thing in science",
             "correct": False,
             "why": "They do not. Identical would mean no variation at "
                    "all, and no real tissue is like that."},
            {"text": "Blood holds red cells, white cells and platelets, "
                     "and is still one tissue on one job", "correct": True},
            {"text": "It matters because identical cells would be an "
                     "organ instead", "correct": False,
             "why": "An organ is several different tissues. Sameness of "
                    "cells never turns something into an organ."},
            {"text": "It matters because tissues change their cells "
                     "completely every few days", "correct": False,
             "why": "Some tissues do renew fast, but that is about "
                    "replacement over time rather than about what similar "
                    "means."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h21",
        "band": "harder",
        "text": "The liver stores glucose, makes bile for digestion and "
                "breaks down toxins from the blood. What does that show about "
                "organs and systems?",
        "options": [
            {"text": "An organ can serve more than one system, so "
                     "systems are jobs rather than separate boxes",
             "correct": True},
            {"text": "The liver must be an organ system of its own, "
                     "because one organ cannot possibly hold three jobs",
             "correct": False,
             "why": "A system is several organs. Three jobs in one "
                    "structure still leaves it a single organ."},
            {"text": "The liver is an organism, because it can do so "
                     "much without any help from the rest of you",
             "correct": False,
             "why": "It does none of it on its own. Everything it does "
                    "depends on blood arriving and leaving."},
            {"text": "Organ systems must therefore each own exactly one "
                     "organ", "correct": False,
             "why": "The opposite: a system is several organs, and some of "
                    "them are shared between systems."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h22",
        "band": "harder",
        "text": "A plant has no heart, no lungs and no nerves. Does that mean "
                "the levels of organisation do not apply to plants?",
        "options": [
            {"text": "Yes, because plants stop at the tissue rung, and "
                     "nothing above a tissue is ever found inside one",
             "correct": False,
             "why": "A leaf is an organ and a shoot is an organ system, so "
                    "plants use every rung."},
            {"text": "Yes, because the five levels were worked out from "
                     "animal bodies and were never meant for plants",
             "correct": False,
             "why": "They describe organisation itself, which is why the "
                    "same five rungs fit a daisy and a person."},
            {"text": "No: the rungs name levels of organisation, not a "
                     "fixed list of organs every living thing must own",
             "correct": True},
            {"text": "No, because plants have hearts and lungs under "
                     "different names", "correct": False,
             "why": "They genuinely have neither. Water moves without a "
                    "pump and gases move in and out through pores."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h23",
        "band": "harder",
        "text": "How many rungs of the ladder lie between a single palisade "
                "cell and the whole plant it belongs to?",
        "options": [
            {"text": "One, because the cell is simply part of the plant",
             "correct": False,
             "why": "That skips three rungs. The cell is in a layer, the "
                    "layer is in a leaf, and the leaf is on a shoot."},
            {"text": "Three: the palisade layer, the leaf, and the shoot",
             "correct": True},
            {"text": "Two: the leaf and the shoot", "correct": False,
             "why": "You have left out the tissue. Cells form the palisade "
                    "layer before any leaf exists."},
            {"text": "Four, counting the chloroplasts inside the cell",
             "correct": False,
             "why": "Chloroplasts are below the cell, so they cannot be "
                    "between the cell and the plant."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h24",
        "band": "harder",
        "text": "A student writes: 'The heart is made of cardiac muscle, so "
                "the heart is a tissue.' What is the flaw?",
        "options": [
            {"text": "There is no flaw, because cardiac muscle makes up "
                     "nearly all of the mass of a heart", "correct": False,
             "why": "Rung is not decided by what most of the mass is. It "
                    "is decided by whether unlike tissues are working "
                    "together."},
            {"text": "The flaw is that the heart is far too big to be a "
                     "tissue", "correct": False,
             "why": "This is the size error again. A tissue can be huge — "
                    "think of the muscle in an elephant's leg."},
            {"text": "The flaw is that cardiac muscle is an organ, not a "
                     "tissue", "correct": False,
             "why": "Cardiac muscle is similar cells on one job, so it "
                    "really is a tissue. The mistake is in what the heart "
                    "is."},
            {"text": "The heart also has valves, vessels and nerve "
                     "tissue, and needs all of them to pump", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h25",
        "band": "harder",
        "text": "Three of these are on the same rung. Which one is the odd "
                "one out?",
        "options": [
            {"text": "A leaf", "correct": False,
             "why": "A leaf is an organ: palisade, spongy, epidermis and "
                    "vein tissue in one structure."},
            {"text": "The stomach", "correct": False,
             "why": "The stomach is an organ — muscle, glandular, "
                    "connective and nerve tissue together."},
            {"text": "Phloem", "correct": True},
            {"text": "A kidney", "correct": False,
             "why": "A kidney is an organ, built from several tissues to "
                    "clean the blood."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h26",
        "band": "harder",
        "text": "A fish's gill is a stack of thin filaments with a rich blood "
                "supply, held by supporting tissue. How would you classify "
                "it?",
        "options": [
            {"text": "An organ of a gas exchange system", "correct": True},
            {"text": "A tissue, because the filaments are all alike",
             "correct": False,
             "why": "The filaments are alike, but blood vessels and "
                    "supporting tissue are in there with them, and that "
                    "mix is what an organ is."},
            {"text": "An organ system by itself, because gas exchange is "
                     "a whole function", "correct": False,
             "why": "The system is the gills, the mouth and the covers "
                    "that pump water across them, all together."},
            {"text": "Not on the ladder, because a gill is outside the "
                     "fish's body", "correct": False,
             "why": "Gills are part of the fish, sheltered under a cover, "
                    "and everything in a living thing is on the ladder "
                    "somewhere."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h27",
        "band": "harder",
        "text": "A student draws: cell to tissue, tissue to organ, organ to "
                "organism, organism to organ system. Which arrow is wrong?",
        "options": [
            {"text": "Cell to tissue, because one cell on its own cannot "
                     "build anything larger than itself", "correct": False,
             "why": "That arrow is right: many similar cells on one job "
                    "are exactly what a tissue is."},
            {"text": "The last two: an organ joins a system first, and "
                     "systems then make the organism", "correct": True},
            {"text": "Tissue to organ, because tissues make systems and "
                     "never organs", "correct": False,
             "why": "Tissues make organs. Systems are one rung further up "
                    "again."},
            {"text": "None of them — that is the ladder in the usual "
                     "order", "correct": False,
             "why": "The usual order ends organ, organ system, organism, "
                    "so the last two arrows have been swapped."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h28",
        "band": "harder",
        "text": "One student describes a stomach as 'made of cells'; another "
                "describes it as 'made of tissues'. Which description is more "
                "useful, and why?",
        "options": [
            {"text": "The first, because cells are the only things in a "
                     "stomach that are really, physically there",
             "correct": False,
             "why": "Tissues are just as real. The word names cells "
                    "arranged, and the arrangement does most of the work."},
            {"text": "The first, because tissues are only a name "
                     "teachers use for groups of cells", "correct": False,
             "why": "It is not just a label. A tissue does something no "
                    "cell in it can do alone, which is why the rung "
                    "exists."},
            {"text": "Neither is more useful, because both sentences are "
                     "perfectly true of a stomach as it stands",
             "correct": False,
             "why": "Both are true, but only one of them explains why the "
                    "stomach can digest a meal and a dish of its cells "
                    "cannot."},
            {"text": "The second, because it says how the cells are "
                     "grouped, which is what lets the stomach work",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h29",
        "band": "harder",
        "text": "It is said that the stomach digests food and also that the "
                "digestive system digests food. How can both be true?",
        "options": [
            {"text": "The stomach does part of the job; the system does "
                     "the whole job, from mouth to absorption",
             "correct": True},
            {"text": "Only one can be true, and the stomach is the "
                     "correct one", "correct": False,
             "why": "The stomach never finishes digestion and absorbs "
                    "almost nothing. Most of both happens further along."},
            {"text": "They are the same thing said twice, because the "
                     "stomach is really the whole digestive system",
             "correct": False,
             "why": "This is the mistake of treating a system as one "
                    "organ. The system also has a mouth, intestines, liver "
                    "and pancreas."},
            {"text": "Both are wrong, because only enzymes digest food",
             "correct": False,
             "why": "Enzymes do the chemistry, but they are made, released "
                    "and mixed by structures on the ladder."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h30",
        "band": "harder",
        "text": "A patient is given donated blood; another is given a donated "
                "kidney. Which levels have been transplanted?",
        "options": [
            {"text": "Both are organ transplants, since both come from "
                     "another person's body", "correct": False,
             "why": "Where it came from does not set the rung. Blood is "
                    "similar cells on one job, and a kidney is several "
                    "tissues."},
            {"text": "Blood is a cell transplant and the kidney is a "
                     "tissue transplant", "correct": False,
             "why": "Both are one rung too low. Blood is a whole tissue, "
                    "and a kidney is a whole organ."},
            {"text": "A tissue and an organ", "correct": True},
            {"text": "Blood is not on the ladder, so only the kidney "
                     "counts as a transplant", "correct": False,
             "why": "Blood is a tissue. Being a liquid does not keep it "
                    "off the ladder."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h31",
        "band": "harder",
        "text": "Every vein is removed from a leaf. All the other cells stay "
                "alive and in place, and the leaf stays on the plant. Predict "
                "what happens in the light.",
        "options": [
            {"text": "Nothing changes, because the palisade cells still "
                     "have all their chloroplasts", "correct": False,
             "why": "Chloroplasts cannot work without water arriving, and "
                    "water arrives through the xylem in the veins."},
            {"text": "It photosynthesises briefly, then stops: no water "
                     "arrives and no sugar can leave", "correct": True},
            {"text": "It photosynthesises faster, because light no "
                     "longer has veins in the way", "correct": False,
             "why": "Veins block very little light, and the loss of supply "
                    "matters far more than the small gain."},
            {"text": "It becomes a tissue, because only one kind of cell "
                     "is left", "correct": False,
             "why": "Palisade, spongy and epidermis cells are all still "
                    "there, so several tissues remain — a damaged organ, "
                    "not a tissue."},
        ],
        "figure": None,
    },
    {
        "id": "b1-05-h32",
        "band": "harder",
        "text": "Which comparison shows best that organisation, not the "
                "number of cells, is what a rung adds?",
        "options": [
            {"text": "Comparing a young plant with a much larger tree of "
                     "exactly the same species, grown side by side",
             "correct": False,
             "why": "This only changes size. Both are organised the same "
                    "way, so nothing about organisation is being tested."},
            {"text": "Comparing an animal cell with a plant cell under a "
                     "school microscope, side by side", "correct": False,
             "why": "That compares two kinds of cell on one rung, and says "
                    "nothing about the rungs above."},
            {"text": "Comparing a leaf in bright light with the same "
                     "leaf in the dark", "correct": False,
             "why": "That tests what photosynthesis needs, not how the "
                    "leaf is built."},
            {"text": "Comparing scattered gut lining cells with the same "
                     "number of them in an intact lining", "correct": True},
        ],
        "figure": None,
    },
]
