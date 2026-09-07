"""P11 lesson 02 — Brownian motion: twelve questions (MRB-223).

Written against Design's page. The smoke cell, the four suspensions and
the three bars are hers.

The discriminations, in the order the lesson builds them:

  · what the movement IS — random, never-ending, no direction;
  · what is visible and what is not, and why the speck has to be the
    size it is;
  · why the strikes nearly cancel, which is the whole mechanism;
  · what a visible jiggle is EVIDENCE for (`PART-19` at the easier end,
    and the nature-of-science half in the harder band).

⚠️ POSITION IS AUTHORED — 0,1,2,3 · 1,2,3,0 · 2,3,0,1, three of each.

⚠️ NEITHER MARKED RUNG IS RESTATED: "pushed by other smoke specks" and
"why watch the specks rather than the molecules" are the ladder's, and
nothing here reuses either. The molecule/speck size question here is
about the SPECK's size being chosen, not about why a molecule is
invisible.
"""

UNIT = "P11"
LESSON = "brownian-motion"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p11-02-e01",
        "band": "easier",
        "text": "What is Brownian motion?",
        "options": [
            {"text": "The random jiggling of small specks suspended in a "
                     "fluid", "correct": True},
            {"text": "The steady sinking of specks through a fluid",
             "correct": False,
             "why": "Nothing sinks. The specks never settle, which is the "
                    "first thing anyone notices about them."},
            {"text": "The swirling of a fluid when it is stirred",
             "correct": False,
             "why": "Stirring makes a current, and a current carries "
                    "everything the same way. Brownian motion has no "
                    "direction at all."},
            {"text": "The movement of a fluid from a hot place to a cold one",
             "correct": False,
             "why": "That is a convection current. Brownian motion happens in "
                    "a sealed cell at one steady temperature."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e02",
        "band": "easier",
        "text": "In a smoke cell, what can you actually see through the "
                "microscope?",
        "options": [
            {"text": "The air molecules", "correct": False,
             "why": "A molecule is thousands of times below what any light "
                    "microscope can resolve. You never see one."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "The smoke specks, scattering light",
             "correct": True},
            {"text": "Both the smoke specks and the air molecules",
             "correct": False,
             "why": "Only the specks. The molecules are far too small to see, "
                    "which is why the smoke is put there at all."},
            {"text": "Neither — the movement is measured electrically",
             "correct": False,
             "why": "You look down the microscope and watch. The specks are "
                    "lit from the side against a dark background."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e03",
        "band": "easier",
        "text": "What happens to Brownian motion when the fluid is warmed?",
        "options": [
            {"text": "It stops completely, because the molecules settle",
             "correct": False,
             "why": "Nothing settles at any temperature. Warming makes the "
                    "jiggling wilder, not quieter."},
            {"text": "It slows down and becomes gentler, because warmth calms "
                     "the fluid", "correct": False,
             "why": "Warmth does the opposite of calming. It speeds every "
                    "molecule up, so the strikes are harder and the leftover "
                    "push is bigger."},
            {"text": "It gets faster and more violent", "correct": True},
            {"text": "It stays exactly the same, because heat does not reach "
                     "the speck", "correct": False,
             "why": "The warmth reaches the speck through the very molecules "
                    "that strike it, and their speed changes with it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e04",
        "band": "easier",
        "text": "Why do the strikes on a smoke speck nearly cancel out?",
        "options": [
            {"text": "Because the molecules all move at the same speed, so "
                     "their pushes are equal", "correct": False,
             "why": "They do not all move at the same speed, and it would not "
                    "matter if they did. What cancels them is the number "
                    "arriving from every side at once."},
            {"text": "Because the speck is heavy enough to resist all but the "
                     "hardest strikes", "correct": False,
             "why": "A speck heavy enough to resist the strikes would not "
                    "move at all, and this one plainly does."},
            {"text": "Because half the molecules are moving and half of them "
                     "are standing still", "correct": False,
             "why": "Every molecule in a fluid is moving, all the time. None "
                    "of them is ever standing still."},
            {"text": "Because huge numbers arrive from every direction at the "
                     "same instant", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p11-02-s01",
        "band": "standard",
        "text": "A student says the specks jiggle because there is a draught "
                "in the cell. Which observation shows they are wrong?",
        "options": [
            {"text": "The specks are lit from the side, which is how they "
                     "are made visible", "correct": False,
             "why": "That is how you see them, not why they move. It says "
                    "nothing about draughts."},
            {"text": "A draught would carry every speck the same way at once, "
                     "and they go in every direction", "correct": True},
            {"text": "The specks are made of burnt material, which was never "
                     "alive", "correct": False,
             "why": "True, and it rules out something alive rather than "
                    "something blowing."},
            {"text": "The cell is sealed and kept still, so nothing outside "
                     "it can be moving the air about", "correct": False,
             "why": "A sealed cell can still have a current inside it. What "
                    "settles it is that the specks move independently of one "
                    "another."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s02",
        "band": "standard",
        "text": "Why does the speck have to be a particular size for this to "
                "work?",
        "options": [
            {"text": "Anything works — size makes no difference",
             "correct": False,
             "why": "A molecule would be knocked clean across the cell and a "
                    "grain of sand would not move at all. The size is the "
                    "whole reason smoke is used."},
            {"text": "It has to be as small as a molecule", "correct": False,
             "why": "Then it would be invisible, and it would be flung about "
                    "rather than jiggling."},
            {"text": "Big enough to see, and small enough for the leftover "
                     "push to shift it", "correct": True},
            {"text": "Big enough to be struck evenly on every side, so the "
                     "pushes balance exactly", "correct": False,
             "why": "A speck struck perfectly evenly does not move. The "
                    "imbalance is what you are watching."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s03",
        "band": "standard",
        "text": "What does Brownian motion show about a fluid?",
        "options": [
            {"text": "That it is smooth and continuous all the way down, "
                     "with no gaps", "correct": False,
             "why": "A smooth fluid would push on the speck evenly and it "
                    "would sit still. The jiggle is what rules that out."},
            {"text": "That it is always flowing steadily in one direction",
             "correct": False,
             "why": "The pushes come from every direction, and the speck's "
                    "path changes constantly."},
            {"text": "That it contains something alive that is moving "
                     "itself", "correct": False,
             "why": "Brown found the same jiggling in ground-up rock, which "
                    "had never been alive."},
            {"text": "That it is made of separate particles in constant "
                     "motion", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s04",
        "band": "standard",
        "text": "At 20 °C air molecules move at roughly 500 m/s. Why does a "
                "smoke speck not move at anything like that speed?",
        "options": [
            {"text": "It is struck from all sides at once, so nearly all of "
                     "the pushes cancel", "correct": True},
            {"text": "The molecules slow right down when they hit it",
             "correct": False,
             "why": "They bounce off at similar speeds. What limits the speck "
                    "is that the pushes almost balance."},
            {"text": "The speck is far too heavy to be moved at all by "
                     "something that small", "correct": False,
             "why": "It does move — that is what you are watching. It is "
                    "simply far slower than a molecule."},
            {"text": "Air is too thin to push anything", "correct": False,
             "why": "Air is thin, and there are still enormous numbers of "
                    "molecules arriving every second."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p11-02-h01",
        "band": "harder",
        "text": "A pollen grain in water jiggles less than a smoke speck in "
                "air at the same temperature. Suggest why.",
        "options": [
            {"text": "Water molecules move faster, so each one pushes the "
                     "grain further", "correct": False,
             "why": "Water molecules at 20 °C are quoted at about 590 m/s "
                    "against air's 500, so their speed is not why the grain "
                    "moves less."},
            {"text": "The water must be colder than the air, so its "
                     "molecules are slower", "correct": False,
             "why": "Both are at the same temperature, which is what the "
                    "question says, so neither set of molecules is slower."},
            {"text": "A pollen grain is far bigger, so the leftover push "
                     "shifts it less", "correct": True},
            {"text": "Water molecules are too large to shift a pollen grain "
                     "very far", "correct": False,
             "why": "A water molecule is a fraction of a nanometre across. "
                    "Being small is what makes the pushes cancel so well, not "
                    "what stops them."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h02",
        "band": "harder",
        "text": "Einstein's 1905 work on this mattered because it did "
                "something a description could not. What?",
        "options": [
            {"text": "It showed the specks under a microscope strong enough "
                     "to see molecules", "correct": False,
             "why": "No microscope shows a molecule, and the argument never "
                    "needed one."},
            {"text": "It proved that pollen grains are alive, which explains "
                     "the movement", "correct": False,
             "why": "The opposite: the same jiggling happens in ground-up "
                    "rock, which was never alive."},
            {"text": "It measured the speed of the air molecules directly, "
                     "one at a time", "correct": False,
             "why": "Nothing measured a molecule directly. What was measured "
                    "was how far the speck wandered."},
            {"text": "It predicted a number that could be measured, and the "
                     "measurement agreed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h03",
        "band": "harder",
        "text": "A sealed smoke cell is left overnight at a steady "
                "temperature. What will the specks be doing in the morning?",
        "options": [
            {"text": "Still jiggling, exactly as they were", "correct": True},
            {"text": "Settled on the bottom, because gravity has had time to "
                     "act", "correct": False,
             "why": "The strikes keep shifting them, and nothing is running "
                    "down. It does not stop."},
            {"text": "Stopped, because the energy that was moving them has "
                     "run out", "correct": False,
             "why": "Nothing is being used up. The molecules keep moving for "
                    "as long as the cell has a temperature."},
            {"text": "Gathered in one corner, because the pushes add up over "
                     "time", "correct": False,
             "why": "The pushes are random, so they do not add up in one "
                    "direction — they go on cancelling."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h04",
        "band": "harder",
        "text": "Two identical smoke cells sit at 0 °C and at 80 °C. Which "
                "statement is right?",
        "options": [
            {"text": "The cold cell's specks are still and the warm cell's "
                     "move", "correct": False,
             "why": "The molecules are moving at both temperatures — about "
                    "483 m/s at 0 °C — so the specks jiggle in both."},
            {"text": "Both jiggle, and the warm cell's specks travel further "
                     "each second", "correct": True},
            {"text": "Both jiggle by exactly the same amount, because the "
                     "specks are identical", "correct": False,
             "why": "The specks are identical; the molecules hitting them are "
                    "not. Warmer molecules are faster and push harder."},
            {"text": "Only the cold cell's specks jiggle, because cold air is "
                     "denser", "correct": False,
             "why": "Denser air means more strikes, and colder molecules are "
                    "slower. The jiggling is smaller in the cold, not "
                    "bigger."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p11-02-e05",
        "band": "easier",
        "text": "What causes the jiggling seen in Brownian motion?",
        "options": [
            {"text": "Unbalanced strikes from the fluid's own molecules",
             "correct": True},
            {"text": "The specks pushing each other about", "correct": False,
             "why": "The specks are far too few and far apart to keep hitting "
                    "one another."},
            {"text": "Air currents blowing through the cell", "correct": False,
             "why": "A current would carry them all the same way; these move "
                    "in every direction at once."},
            {"text": "The specks moving under their own power",
             "correct": False,
             "why": "Smoke is not alive and has no way of moving itself."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e06",
        "band": "easier",
        "text": "Does Brownian motion ever stop?",
        "options": [
            {"text": "Yes, once the fluid has settled", "correct": False,
             "why": "The molecules never settle; they are in constant motion "
                    "at any temperature above absolute zero."},
            {"text": "Yes, after a few minutes", "correct": False,
             "why": "It is still going hours or days later, at the same "
                    "temperature."},
            {"text": "No, it carries on indefinitely", "correct": True},
            {"text": "Only if the fluid is cooled to room temperature",
             "correct": False,
             "why": "Room temperature is where it is normally watched, and it "
                    "is going strongly there."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e07",
        "band": "easier",
        "text": "In which materials does Brownian motion happen?",
        "options": [
            {"text": "In solids only", "correct": False,
             "why": "A solid's particles are locked in place, so nothing "
                    "suspended in it can be jostled about."},
            {"text": "In gases only", "correct": False,
             "why": "It was first seen in a liquid — pollen in water — and "
                    "happens in both."},
            {"text": "In liquids and gases", "correct": True},
            {"text": "In any material at all", "correct": False,
             "why": "It needs particles free to move past one another, which "
                    "rules a solid out."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e08",
        "band": "easier",
        "text": "Are the specks watched in a smoke cell alive?",
        "options": [            {"text": "Yes, which is why they move", "correct": False,
             "why": "Smoke is burnt material, and the same motion is seen "
                    "with plastic beads."},
            {"text": "No — nothing is really moving, it only looks that way",
             "correct": False,
             "why": "The movement is real and can be tracked and measured."},
            {"text": "Yes, but only the ones that move fastest",
             "correct": False,
             "why": "None of them is alive; they are all pushed by the "
                    "surrounding molecules."},
            {"text": "No — they are moved by the molecules around them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e09",
        "band": "easier",
        "text": "What can you NOT see through the microscope in a smoke cell?",
        "options": [
            {"text": "The bright points of light from the specks",
             "correct": False,
             "why": "Those are exactly what is watched; they are what the "
                    "experiment shows."},
            {"text": "The paths the specks take", "correct": False,
             "why": "The paths are visible as the specks jiggle and can even "
                    "be traced."},
            {"text": "The air molecules themselves", "correct": True},
            {"text": "The walls of the cell", "correct": False,
             "why": "The cell is easily visible; it is the molecules inside "
                    "that are not."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e10",
        "band": "easier",
        "text": "Cooling the fluid in a smoke cell makes the jiggling…",
        "options": [            {"text": "less violent", "correct": True},
            {"text": "wilder", "correct": False,
             "why": "Warming makes it wilder; cooling does the opposite."},
            {"text": "stop completely", "correct": False,
             "why": "It slows but never stops, because the molecules keep "
                    "moving."},
            {"text": "change direction less often", "correct": False,
             "why": "The direction still changes constantly; it is the size "
                    "of the movement that falls."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e11",
        "band": "easier",
        "text": "What is a fluid?",
        "options": [
            {"text": "A liquid or a gas", "correct": True},
            {"text": "A liquid only", "correct": False,
             "why": "Gases flow too, and Brownian motion happens in both."},
            {"text": "Anything that can be poured", "correct": False,
             "why": "Sand pours and is not a fluid; what matters is that the "
                    "particles move past one another."},
            {"text": "Anything transparent", "correct": False,
             "why": "Glass is transparent and solid; being see-through has "
                    "nothing to do with it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e12",
        "band": "easier",
        "text": "A path made of many small steps, each in a direction nothing "
                "chose, is called…",
        "options": [            {"text": "a straight line", "correct": False,
             "why": "A straight line has one direction throughout, which is "
                    "the opposite of random."},
            {"text": "diffusion", "correct": False,
             "why": "Diffusion is the spreading that results; the path itself "
                    "is a random walk."},
            {"text": "a current", "correct": False,
             "why": "A current carries everything the same way, which is not "
                    "what a speck does."},
            {"text": "a random walk", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e13",
        "band": "easier",
        "text": "Brownian motion is evidence that a fluid is made of…",
        "options": [            {"text": "separate particles that are constantly moving",
             "correct": True},
            {"text": "one continuous substance with no gaps", "correct": False,
             "why": "A continuous substance would push evenly from all sides "
                    "and nothing would jiggle."},
            {"text": "particles that are all the same size as the specks",
             "correct": False,
             "why": "The molecules are far smaller — that is why they cannot "
                    "be seen."},
            {"text": "particles that only move when the fluid is warmed",
             "correct": False,
             "why": "They move at every temperature; warming only makes them "
                    "faster."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p11-02-s05",
        "band": "standard",
        "text": "Why would a large grain of sand be a poor choice for a smoke "
                "cell?",
        "options": [            {"text": "Because it is too heavy to be seen under a microscope",
             "correct": False,
             "why": "It is easy to see; the problem is that it does not "
                    "move."},
            {"text": "Because sand dissolves in the fluid", "correct": False,
             "why": "Sand does not dissolve, and dissolving is not what the "
                    "experiment turns on."},
            {"text": "Because sand is not affected by molecules at all",
             "correct": False,
             "why": "It is struck constantly; the strikes simply balance out "
                    "on something that big."},
            {"text": "Because so many molecules strike it that the pushes "
                     "cancel almost exactly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s06",
        "band": "standard",
        "text": "Why does a speck keep changing direction?",
        "options": [            {"text": "Because the leftover imbalance points a different way "
                     "each instant",
             "correct": True},
            {"text": "Because it bounces off the walls of the cell",
             "correct": False,
             "why": "It changes direction constantly in the middle of the "
                    "cell, far from any wall."},
            {"text": "Because the air current in the cell swirls",
             "correct": False,
             "why": "A swirl would carry neighbouring specks together, and "
                    "they move independently."},
            {"text": "Because it is spinning as it moves", "correct": False,
             "why": "Spinning would not change the direction it travels in."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s07",
        "band": "standard",
        "text": "A student says a draught in the cell is moving the specks. "
                "Which observation rules that out?",
        "options": [
            {"text": "The specks are very small", "correct": False,
             "why": "A draught moves small things most easily, so this "
                    "supports the student rather than refuting them."},
            {"text": "The motion is faster when the cell is warmed",
             "correct": False,
             "why": "A warm cell could have stronger currents, so this does "
                    "not settle it on its own."},
            {"text": "Neighbouring specks move in different directions at the "
                     "same moment",
             "correct": True},
            {"text": "The specks are visible as bright points",
             "correct": False,
             "why": "How they are lit says nothing about what moves them."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s08",
        "band": "standard",
        "text": "Two identical smoke cells are held at 20 °C and 60 °C. Which "
                "shows the wilder motion, and why?",
        "options": [            {"text": "The 20 °C cell, because cool molecules are heavier",
             "correct": False,
             "why": "The molecules are the same; cooling only slows them "
                    "down."},
            {"text": "The 60 °C cell, because warm air rises past the specks",
             "correct": False,
             "why": "Right cell, wrong reason: it is the speed of the "
                    "molecules, not a rising current."},
            {"text": "Neither — temperature does not affect the motion",
             "correct": False,
             "why": "It affects it a great deal, which is one of the "
                    "experiment's main results."},
            {"text": "The 60 °C cell, because its molecules are moving "
                     "faster",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s09",
        "band": "standard",
        "text": "Why is the light shone into a smoke cell from the side?",
        "options": [            {"text": "So the specks show up brightly against a dark "
                     "background",
             "correct": True},
            {"text": "To warm the air and start the motion", "correct": False,
             "why": "The motion is there before the lamp is on; warming would "
                    "only change how wild it is."},
            {"text": "So the molecules can be seen as well", "correct": False,
             "why": "No arrangement of light makes molecules visible in a "
                    "light microscope."},
            {"text": "To stop the smoke escaping from the cell",
             "correct": False,
             "why": "Light does not seal anything; the cell's walls do that."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s10",
        "band": "standard",
        "text": "A fine powder is stirred into water and watched under a "
                "microscope. What would you expect?",
        "options": [
            {"text": "Nothing, because Brownian motion only happens in air",
             "correct": False,
             "why": "It was first seen in water, with pollen, and happens in "
                    "any fluid."},
            {"text": "The grains all drifting slowly the same way",
             "correct": False,
             "why": "That would be a current; Brownian motion sends them in "
                    "different directions."},
            {"text": "The same random jiggling as smoke in air", "correct": True},
            {"text": "The grains settling and then staying perfectly still",
             "correct": False,
             "why": "Small enough grains keep jiggling indefinitely, however "
                    "long you wait."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s11",
        "band": "standard",
        "text": "Why is the motion described as random rather than just "
                "complicated?",
        "options": [            {"text": "Because it is too fast to follow with the eye",
             "correct": False,
             "why": "It is slow enough to watch and to trace; speed is not "
                    "the point."},
            {"text": "Because the specks are all different shapes",
             "correct": False,
             "why": "Identical spheres jiggle randomly too, so shape is not "
                    "what makes it random."},
            {"text": "Because the microscope is not accurate enough to see "
                     "the pattern",
             "correct": False,
             "why": "A better microscope shows the same randomness in more "
                    "detail."},
            {"text": "Because nothing chooses the direction, and each step is "
                     "unrelated to the last",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s12",
        "band": "standard",
        "text": "A student says the bright dots under the microscope ARE the "
                "air molecules. What is right?",
        "options": [            {"text": "They are smoke specks, far larger than the molecules "
                     "that push them",
             "correct": True},
            {"text": "They are the molecules, seen because the light is "
                     "bright enough",
             "correct": False,
             "why": "No amount of light makes them visible; they are far "
                    "below what a light microscope can resolve."},
            {"text": "They are molecules, but only the largest ones in the "
                     "air",
             "correct": False,
             "why": "Even the largest air molecules are thousands of times "
                    "too small to see."},
            {"text": "They are neither — the dots are a fault in the "
                     "microscope",
             "correct": False,
             "why": "The dots are really there and move in a way no fault "
                    "would produce."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s13",
        "band": "standard",
        "text": "What does Brownian motion tell you about the molecules of a "
                "fluid?",
        "options": [            {"text": "That they are large enough to see under a good "
                     "microscope",
             "correct": False,
             "why": "They are never seen; only their effect on the specks "
                    "is."},
            {"text": "That they are joined together into one continuous "
                     "substance",
             "correct": False,
             "why": "A continuous substance could not deliver the uneven "
                    "pushes that make a speck jiggle."},
            {"text": "That they move only when the fluid is stirred",
             "correct": False,
             "why": "The cell is left undisturbed and the jiggling carries "
                    "on."},
            {"text": "That they are separate, moving, and too small to see",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p11-02-h05",
        "band": "harder",
        "text": "Why does a larger speck jiggle less than a smaller one at "
                "the same temperature?",
        "options": [            {"text": "Because more strikes arrive and cancel, and there is "
                     "more mass to shift",
             "correct": True},
            {"text": "Because fewer molecules reach it", "correct": False,
             "why": "Far more reach it; the point is that so many arrive that "
                    "they cancel."},
            {"text": "Because the molecules avoid larger objects",
             "correct": False,
             "why": "Nothing steers the molecules; they arrive from every "
                    "direction whatever is in the way."},
            {"text": "Because larger specks are heavier and sink out of the "
                     "way",
             "correct": False,
             "why": "The comparison is made while both are suspended, and the "
                    "difference is in the jiggling itself."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h06",
        "band": "harder",
        "text": "Why was a jiggling speck taken as evidence that atoms are "
                "real?",
        "options": [            {"text": "Because the atoms could finally be seen directly",
             "correct": False,
             "why": "They still could not be seen; only their effect was "
                    "visible."},
            {"text": "Because the motion stopped when the atoms were removed",
             "correct": False,
             "why": "No experiment removed the atoms; the argument was about "
                    "explaining the movement."},
            {"text": "Because the specks were found to be made of atoms",
             "correct": False,
             "why": "Everything is made of atoms; what mattered was what "
                    "moved the specks."},
            {"text": "Because only separate invisible particles delivering "
                     "uneven pushes could explain it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h07",
        "band": "harder",
        "text": "What would happen to the jiggling if the air were pumped out "
                "of a smoke cell?",
        "options": [            {"text": "It would stop, because nothing would be left to strike "
                     "the specks",
             "correct": True},
            {"text": "It would get wilder, with nothing to slow the specks",
             "correct": False,
             "why": "Nothing slows them now; the molecules are what MOVES "
                    "them."},
            {"text": "It would carry on unchanged, since the specks move "
                     "themselves",
             "correct": False,
             "why": "The specks have no power of their own; they are pushed "
                    "by the molecules."},
            {"text": "It would carry on, driven by the light from the lamp",
             "correct": False,
             "why": "The lamp only makes them visible; turning it brighter "
                    "does not change the motion."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h08",
        "band": "harder",
        "text": "Why does the same experiment work in a liquid and in a gas?",
        "options": [            {"text": "Because both are transparent enough to see through",
             "correct": False,
             "why": "Being see-through lets you watch it; it is not what "
                    "causes the motion."},
            {"text": "Because both are at room temperature", "correct": False,
             "why": "It works at any temperature; being a fluid is what "
                    "matters."},
            {"text": "Because both have the same density", "correct": False,
             "why": "A liquid is about a thousand times denser than a gas, "
                    "and it works in both."},
            {"text": "Because both are fluids, whose particles move past one "
                     "another",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h09",
        "band": "harder",
        "text": "A sealed cell is left for a week at a steady temperature. "
                "Why has the motion not died away?",
        "options": [            {"text": "Because the molecules never stop moving, so the strikes "
                     "never stop",
             "correct": True},
            {"text": "Because the cell has slowly warmed over the week",
             "correct": False,
             "why": "The temperature is stated as steady, and the motion "
                    "would continue even if it were not."},
            {"text": "Because fresh smoke has been produced inside the cell",
             "correct": False,
             "why": "The cell is sealed and nothing new is made; the same "
                    "specks are still jiggling."},
            {"text": "Because the specks store energy from the light",
             "correct": False,
             "why": "It continues in the dark, so the lamp is not driving "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h10",
        "band": "harder",
        "text": "Robert Brown saw this in 1827 and could not explain it. What "
                "was missing at the time?",
        "options": [            {"text": "A microscope good enough to see the specks",
             "correct": False,
             "why": "His microscope showed them perfectly well — that is how "
                    "he saw the motion."},
            {"text": "Anyone who had noticed the effect before him",
             "correct": False,
             "why": "Being first is why it carries his name; it is not what "
                    "stopped him explaining it."},
            {"text": "A way of keeping the sample at a steady temperature",
             "correct": False,
             "why": "Temperature control would have refined the observation, "
                    "not explained it."},
            {"text": "Accepted evidence that matter is made of separate "
                     "moving particles",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h11",
        "band": "harder",
        "text": "Why can a convection current NOT explain what is seen in a "
                "smoke cell?",
        "options": [
            {"text": "Because a current would carry neighbouring specks the "
                     "same way, and they go different ways",
             "correct": True},
            {"text": "Because there is no air in the cell to convect",
             "correct": False,
             "why": "The cell is full of air, which is exactly what does the "
                    "pushing."},
            {"text": "Because convection cannot happen in a container that "
                     "small",
             "correct": False,
             "why": "Small currents certainly can occur, which is why the "
                    "observation has to rule them out."},
            {"text": "Because the specks are too heavy to be carried by a "
                     "current",
             "correct": False,
             "why": "They are light enough for a current to move; the "
                    "directions they take are what settles it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h12",
        "band": "harder",
        "text": "A speck's path is drawn as straight segments joined at "
                "random angles. Why is that a fair picture?",
        "options": [            {"text": "Because each unbalanced strike sends it off in a new "
                     "direction",
             "correct": True},
            {"text": "Because the speck travels in straight lines between "
                     "walls of the cell",
             "correct": False,
             "why": "It changes direction constantly in open fluid, nowhere "
                    "near a wall."},
            {"text": "Because the microscope can only record it at intervals",
             "correct": False,
             "why": "Sampling makes the drawing simpler, but the direction "
                    "really does change."},
            {"text": "Because the angles are always ninety degrees",
             "correct": False,
             "why": "They take every value; nothing picks a right angle."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h13",
        "band": "harder",
        "text": "A smoke cell is built a hundred times larger, with the same "
                "smoke and air. What changes about the jiggling?",
        "options": [
            {"text": "It becomes much wilder, with more air around each "
                     "speck",
             "correct": False,
             "why": "What matters is the molecules immediately around a "
                    "speck, and there are just as many of those."},
            {"text": "It stops, because the specks are too far from the walls",
             "correct": False,
             "why": "The walls play no part; the molecules do the pushing."},
            {"text": "Nothing — the motion depends on the molecules around "
                     "each speck",
             "correct": True},
            {"text": "It becomes slower, because the specks have further to "
                     "travel",
             "correct": False,
             "why": "There is no destination to reach; each speck wanders "
                    "wherever the strikes send it."},
        ],
        "figure": None,
    },
]
