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
        "options": [
            {"text": "Because it would be far too heavy to be seen under the "
                     "microscope",
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
                     "cancel",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s06",
        "band": "standard",
        "text": "Why does a speck keep changing direction?",
        "options": [
            {"text": "Because the leftover imbalance keeps changing direction",
             "correct": True},
            {"text": "Because it keeps bouncing off the walls of the cell as "
                     "it goes",
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
            {"text": "The motion becomes much faster when the cell is warmed "
                     "up",
             "correct": False,
             "why": "A warm cell could have stronger currents, so this does "
                    "not settle it on its own."},
            {"text": "Neighbouring specks move different ways at once",
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
        "options": [
            {"text": "So the specks show up brightly against the dark",
             "correct": True},
            {"text": "To warm the air and start the motion", "correct": False,
             "why": "The motion is there before the lamp is on; warming would "
                    "only change how wild it is."},
            {"text": "So the molecules can be seen as well", "correct": False,
             "why": "No arrangement of light makes molecules visible in a "
                    "light microscope."},
            {"text": "To stop the smoke escaping from the cell while it is "
                     "watched",
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
        "options": [
            {"text": "Because it is too fast to follow with the eye",
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
            {"text": "Because nothing chooses the direction of each fresh "
                     "step",
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
        "options": [
            {"text": "Because more strikes cancel, and there is more mass to "
                     "shift",
             "correct": True},
            {"text": "Because fewer molecules reach it", "correct": False,
             "why": "Far more reach it; the point is that so many arrive that "
                    "they cancel."},
            {"text": "Because the molecules avoid larger objects",
             "correct": False,
             "why": "Nothing steers the molecules; they arrive from every "
                    "direction whatever is in the way."},
            {"text": "Because larger specks are heavier and simply sink out "
                     "of the way faster",
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
        "options": [
            {"text": "Because the atoms could finally be seen directly",
             "correct": False,
             "why": "They still could not be seen; only their effect was "
                    "visible."},
            {"text": "Because the motion stopped when the atoms were taken "
                     "out of the cell",
             "correct": False,
             "why": "No experiment removed the atoms; the argument was about "
                    "explaining the movement."},
            {"text": "Because the specks were found to be made of atoms",
             "correct": False,
             "why": "Everything is made of atoms; what mattered was what "
                    "moved the specks."},
            {"text": "Because only separate invisible particles could push "
                     "unevenly",
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
        "options": [
            {"text": "Because the molecules never stop moving, nor the "
                     "strikes",
             "correct": True},
            {"text": "Because the cell has slowly warmed over the week",
             "correct": False,
             "why": "The temperature is stated as steady, and the motion "
                    "would continue even if it were not."},
            {"text": "Because fresh smoke keeps being produced inside the "
                     "sealed cell",
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
        "options": [
            {"text": "A microscope good enough to see the specks",
             "correct": False,
             "why": "His microscope showed them perfectly well — that is how "
                    "he saw the motion."},
            {"text": "Anyone who had noticed the effect before him",
             "correct": False,
             "why": "Being first is why it carries his name; it is not what "
                    "stopped him explaining it."},
            {"text": "A reliable way of keeping the whole sample at a steady "
                     "temperature",
             "correct": False,
             "why": "Temperature control would have refined the observation, "
                    "not explained it."},
            {"text": "Accepted evidence that matter is made of moving "
                     "particles",
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
                     "same way",
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
            {"text": "Because the specks would be far too heavy to be carried "
                     "by a current",
             "correct": False,
             "why": "They are light enough for a current to move; the "
                    "directions they take are what settles it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h12",
        "band": "harder",
        "text": "Through a microscope, a smoke particle in air jerks a short "
                "way in one direction, then another, again and again. Why "
                "does it keep changing direction?",
        "options": [
            {"text": "Unbalanced hits from air particles push it a new way",
             "correct": True},
            {"text": "It bounces off the walls of the smoke cell each time",
             "correct": False,
             "why": "It changes direction all the time in the middle of the "
                    "air, nowhere near a wall."},
            {"text": "It is alive, and moves about in the air on its own",
             "correct": False,
             "why": "Smoke particles are specks of ash, not living things. "
                    "Pollen grains and dust in water jiggle in just the same "
                    "way."},
            {"text": "Gravity pulls it in a different direction each time",
             "correct": False,
             "why": "Gravity always pulls downwards. It cannot send a "
                    "particle off sideways or upwards."},
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

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p11-02-e14",
        "band": "easier",
        "text": "Who first recorded the constant jiggling of small particles "
                "suspended in a fluid, in 1827?",
        "options": [
            {"text": "Robert Brown", "correct": True},
            {"text": "Albert Einstein", "correct": False,
             "why": "Einstein explained the jiggling mathematically in 1905, "
                    "nearly 80 years after it was first recorded."},
            {"text": "Jean Perrin", "correct": False,
             "why": "Perrin measured the effect precisely years later; he did "
                    "not first record it."},
            {"text": "Isaac Newton", "correct": False,
             "why": "Newton had been dead for a century by the time this "
                    "jiggling was first recorded."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e15",
        "band": "easier",
        "text": "Robert Brown first observed this jiggling using which small "
                "particles?",
        "options": [
            {"text": "Smoke specks in air", "correct": False,
             "why": "Smoke in air is a common classroom version, but Brown's "
                    "original particles were different."},
            {"text": "Pollen grains in water", "correct": True},
            {"text": "Dust in a sunbeam", "correct": False,
             "why": "Dust in a sunbeam is easy to see, but it was not what "
                    "Brown first studied."},
            {"text": "Fat droplets in milk", "correct": False,
             "why": "Milk was not involved in the original 1827 "
                    "observation."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e16",
        "band": "easier",
        "text": "Which suspension has the biggest size difference between the "
                "visible speck and the invisible molecules striking it: smoke "
                "in air, pollen in water, dust in a sunbeam or fat droplets "
                "in milk?",
        "options": [
            {"text": "Smoke in air", "correct": False,
             "why": "A smoke speck is about 5000 times wider than the "
                    "molecules hitting it, far short of a pollen grain's "
                    "ratio."},
            {"text": "Dust in a sunbeam", "correct": False,
             "why": "A dust grain's ratio is around 50 000 times, still well "
                    "below a pollen grain's."},
            {"text": "Pollen in water", "correct": True},
            {"text": "Fat droplets in milk", "correct": False,
             "why": "A fat droplet's ratio is the smallest of the four, at "
                    "about 3000 times."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e17",
        "band": "easier",
        "text": "Which of these speeds is closest to the roughly 500 m/s "
                "quoted for air molecules on this bench?",
        "options": [
            {"text": "A brisk walking pace", "correct": False,
             "why": "Walking pace is only a couple of metres per second, "
                    "thousands of times too slow."},
            {"text": "A car on a motorway", "correct": False,
             "why": "Motorway speed is around 30 m/s, still more than ten "
                    "times too slow."},
            {"text": "A passenger aircraft cruising", "correct": False,
             "why": "A cruising jet is around 250 m/s, still well below the "
                    "figure quoted."},
            {"text": "A bullet fired from a handgun", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e18",
        "band": "easier",
        "text": "Put these three in order of size, smallest first: an air "
                "molecule, a smoke speck, a grain of sand.",
        "options": [
            {"text": "Air molecule, smoke speck, grain of sand",
             "correct": True},
            {"text": "Smoke speck, air molecule, grain of sand",
             "correct": False,
             "why": "An air molecule is thousands of times smaller than a "
                    "smoke speck, which is exactly why the speck is the part "
                    "you can see."},
            {"text": "Air molecule, grain of sand, smoke speck",
             "correct": False,
             "why": "A grain of sand is far larger than a smoke speck, which "
                    "is why sand shows no visible jiggling of its own."},
            {"text": "Grain of sand, air molecule, smoke speck",
             "correct": False,
             "why": "A grain of sand is the largest of the three by a long "
                    "way, not the smallest."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e19",
        "band": "easier",
        "text": "A jiggling smoke speck changes direction very often. About "
                "how many times a second is it being struck by air "
                "molecules?",
        "options": [
            {"text": "About a hundred", "correct": False,
             "why": "The true number is vastly bigger — a speck is struck by "
                    "molecules far more often than that."},
            {"text": "Billions of times", "correct": True},
            {"text": "Once or twice", "correct": False,
             "why": "A single strike each second could not explain constant, "
                    "ever-changing jiggling."},
            {"text": "It cannot be estimated with any confidence", "correct": False,
             "why": "It can be estimated, and the number is enormous — "
                    "billions of strikes every second."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e20",
        "band": "easier",
        "text": "In which of these would you NOT expect to see Brownian "
                "motion?",
        "options": [
            {"text": "Pollen grains suspended in water", "correct": False,
             "why": "This is one of the classic examples, first studied by "
                    "Robert Brown."},
            {"text": "Smoke specks suspended in air", "correct": False,
             "why": "This is a standard classroom demonstration of the "
                    "effect."},
            {"text": "A marble resting on a solid table", "correct": True},
            {"text": "Fat droplets suspended in milk", "correct": False,
             "why": "Fat droplets in milk show the same random jiggling as "
                    "any other fine suspension."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e21",
        "band": "easier",
        "text": "Jean Perrin spent years measuring exactly how far smoke "
                "specks wander in a given time. What was he testing?",
        "options": [
            {"text": "Whether smoke specks are alive", "correct": False,
             "why": "Nobody by this point thought the specks were alive; the "
                    "question had already moved on to what caused the "
                    "motion."},
            {"text": "How hot a smoke cell needs to be before the jiggling "
                     "starts", "correct": False,
             "why": "The jiggling happens at any temperature; his "
                    "measurements were not about a starting threshold."},
            {"text": "Whether a better microscope could show a molecule "
                     "directly", "correct": False,
             "why": "No microscope in his measurements ever showed a "
                    "molecule; he measured the speck's wandering instead."},
            {"text": "Whether Einstein's predicted numbers matched real "
                     "measurements", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e22",
        "band": "easier",
        "text": "A speck's jiggle is measured in micrometres each second. "
                "How big is one micrometre?",
        "options": [
            {"text": "A thousandth of a millimetre", "correct": True},
            {"text": "A thousandth of a metre", "correct": False,
             "why": "A thousandth of a metre is a millimetre, and a "
                    "micrometre is a thousand times smaller again."},
            {"text": "A hundredth of a metre", "correct": False,
             "why": "A hundredth of a metre is a centimetre, ten thousand "
                    "times bigger than a micrometre."},
            {"text": "A thousandth of a kilometre", "correct": False,
             "why": "A thousandth of a kilometre is a whole metre, a million "
                    "times bigger than a micrometre."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e23",
        "band": "easier",
        "text": "What happens to Brownian motion if the temperature of the "
                "fluid is kept exactly steady for a very long time?",
        "options": [
            {"text": "It gradually dies away", "correct": False,
             "why": "It does not fade with time; as long as the temperature "
                    "stays the same, the jiggling carries on at the same "
                    "intensity indefinitely."},
            {"text": "It carries on unchanged, however long you wait",
             "correct": True},
            {"text": "It becomes perfectly regular and predictable",
             "correct": False,
             "why": "It stays random, however long it is watched; nothing "
                    "about waiting removes the randomness."},
            {"text": "It slowly speeds up on its own", "correct": False,
             "why": "Nothing speeds it up without a change in temperature; a "
                    "steady temperature gives a steady amount of jiggling."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e24",
        "band": "easier",
        "text": "Which statement about the molecules striking a smoke speck "
                "is correct?",
        "options": [
            {"text": "A few dozen strike it every second", "correct": False,
             "why": "The true number is vastly bigger — billions of strikes "
                    "happen every second."},
            {"text": "They strike from directly above", "correct": False,
             "why": "They strike from every direction at once, which is "
                    "exactly why most of the pushes cancel out."},
            {"text": "Huge numbers strike it from every direction at once",
             "correct": True},
            {"text": "They strike it just when the lamp is switched on",
             "correct": False,
             "why": "The strikes happen constantly, with or without the "
                    "lamp; the lamp only makes the speck visible."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e25",
        "band": "easier",
        "text": "A dust grain floating in a sunbeam is an everyday example "
                "of…",
        "options": [
            {"text": "Convection", "correct": False,
             "why": "Convection is a current moving one way; the dust "
                    "grain's path has no fixed direction at all."},
            {"text": "Evaporation", "correct": False,
             "why": "Nothing here is changing from a liquid to a gas; the "
                    "grain is simply a solid speck jiggling in air."},
            {"text": "Diffusion", "correct": False,
             "why": "Diffusion is the spreading of a substance through a "
                    "fluid, which is a different, though related, effect."},
            {"text": "Brownian motion", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e26",
        "band": "easier",
        "text": "Which of these words best describes the direction a jiggling "
                "speck takes at each new step?",
        "options": [
            {"text": "Random", "correct": True},
            {"text": "Upward", "correct": False,
             "why": "There is no preferred direction at all; the speck moves "
                    "equally in every direction over time."},
            {"text": "Circular", "correct": False,
             "why": "The path is not a smooth curve; it is a series of short "
                    "straight segments joined at random angles."},
            {"text": "Towards the light", "correct": False,
             "why": "The microscope's lamp only makes the specks visible; it "
                    "does not steer them."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e27",
        "band": "easier",
        "text": "A smoke cell is sealed shut before it goes under the "
                "microscope. What is that mainly to keep out?",
        "options": [
            {"text": "Warmth from the lamp, which would otherwise start the "
                     "jiggling off", "correct": False,
             "why": "The jiggling is already happening before the lamp is "
                    "switched on; warming does not start it."},
            {"text": "Draughts of room air, which would push whole groups of "
                     "specks the same way", "correct": True},
            {"text": "Air molecules, which would otherwise strike the specks "
                     "and move them", "correct": False,
             "why": "The air inside the sealed cell is what strikes the "
                    "specks; sealing it keeps that air in, not out."},
            {"text": "Daylight, which would wash out the specks and stop "
                     "them moving", "correct": False,
             "why": "Light plays no part in the movement; the cell is sealed "
                    "against moving air, not against light."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e28",
        "band": "easier",
        "text": "Which particle is doing the actual pushing in Brownian "
                "motion?",
        "options": [
            {"text": "The visible speck itself", "correct": False,
             "why": "The speck is what is being pushed, not what is doing "
                    "the pushing."},
            {"text": "Nothing — the movement has no physical cause",
             "correct": False,
             "why": "The movement has a clear physical cause: unbalanced "
                    "strikes from surrounding molecules."},
            {"text": "The invisible molecules of the surrounding fluid",
             "correct": True},
            {"text": "Light particles from the microscope's lamp",
             "correct": False,
             "why": "Light plays no part in the pushing; it only makes the "
                    "speck visible."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e29",
        "band": "easier",
        "text": "What is true of the molecules in a fluid at every ordinary "
                "temperature?",
        "options": [
            {"text": "They stay still until something disturbs them",
             "correct": False,
             "why": "They are never still; every molecule in a fluid is in "
                    "constant motion."},
            {"text": "Some of them are moving at any moment",
             "correct": False,
             "why": "Every single one of them is moving, all the time, not "
                    "just some."},
            {"text": "They move just when the fluid is stirred",
             "correct": False,
             "why": "They move on their own, with or without stirring; "
                    "stirring adds a current on top of that motion."},
            {"text": "They are always in constant, random motion",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e30",
        "band": "easier",
        "text": "A student watches a smoke cell and says nothing is happening "
                "because the smoke isn't drifting in any one direction. What "
                "is wrong with that reasoning?",
        "options": [
            {"text": "The specks ARE moving — just randomly, not in one "
                     "direction", "correct": True},
            {"text": "Nothing is wrong; drifting one way is what Brownian "
                     "motion looks like", "correct": False,
             "why": "Drifting steadily one way is what a current looks "
                    "like; Brownian motion has no overall direction at "
                    "all."},
            {"text": "The student is right — nothing at all is happening in "
                     "a still smoke cell", "correct": False,
             "why": "A great deal is happening: billions of molecular "
                    "strikes every second, jiggling every visible speck."},
            {"text": "The smoke would need to be warmed before anything "
                     "could happen", "correct": False,
             "why": "The jiggling is already happening at any ordinary "
                    "temperature, warmed or not."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p11-02-s14",
        "band": "standard",
        "text": "A fat droplet in milk is about 3000 times wider than the "
                "molecules striking it; a pollen grain in water is about "
                "100 000 times wider. Which would you expect to show the "
                "wilder relative jiggling?",
        "options": [
            {"text": "Pollen in water, since more molecules hit it in total",
             "correct": False,
             "why": "More strikes in total also means more cancelling; being "
                    "much bigger than a molecule makes the leftover push "
                    "smaller, not bigger."},
            {"text": "Fat droplets in milk, since they are relatively closer "
                     "in size to the molecules hitting them", "correct": True},
            {"text": "Both jiggle by exactly the same amount", "correct": False,
             "why": "The model's whole point is that size changes how much "
                    "of the imbalance is left over; a smaller ratio leaves "
                    "relatively more."},
            {"text": "Neither — jiggling does not depend on the size of the speck at all", "correct": False,
             "why": "Size is central to the model; that is exactly why a "
                    "grain of sand does not noticeably jiggle at all."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s15",
        "band": "standard",
        "text": "A student claims Brownian motion is just a fancier name for "
                "diffusion. What is the key difference?",
        "options": [
            {"text": "There is no difference; they describe exactly the same "
                     "thing", "correct": False,
             "why": "They are related but distinct — one is a single "
                    "speck's random path, the other is a substance spreading "
                    "out."},
            {"text": "Diffusion happens in gases and Brownian motion only in liquids", "correct": False,
             "why": "Both happen in liquids and in gases; the state of "
                    "matter does not separate them."},
            {"text": "Brownian motion is one speck's random path; diffusion "
                     "is a substance spreading out overall", "correct": True},
            {"text": "Brownian motion needs a microscope and diffusion does "
                     "not", "correct": False,
             "why": "A microscope is only how Brownian motion happens to be "
                    "observed, not part of what defines it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s16",
        "band": "standard",
        "text": "Why did it take until 1905, nearly eighty years after "
                "Brown's first observation, for a full explanation to be "
                "accepted?",
        "options": [
            {"text": "Because nobody looked at the specks again between 1827 and "
                     "1905, so there was nothing new for anyone to explain",
             "correct": False,
             "why": "The jiggling continued to be observed throughout that "
                    "time; what was missing was an accepted explanation, not "
                    "fresh observations."},
            {"text": "Because smoke cells had not yet been invented",
             "correct": False,
             "why": "Pollen grains in water, Brown's original material, "
                    "needed no smoke cell at all."},
            {"text": "Because microscopes only became powerful enough to resolve "
                     "the moving molecules themselves by about 1905, which "
                     "settled the argument at a stroke", "correct": False,
             "why": "The specks were visible with the microscopes of 1827; "
                    "what was missing was a mathematical explanation people "
                    "could test."},
            {"text": "Because nobody had yet made a testable prediction that "
                     "linked the jiggling to moving molecules", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s17",
        "band": "standard",
        "text": "A student records a speck's position every five seconds and "
                "joins the dots with straight lines. Why does that drawing "
                "understate how far the speck has actually travelled?",
        "options": [
            {"text": "Because the speck changes direction many times between "
                     "one reading and the next", "correct": True},
            {"text": "Because the speck speeds up in the gaps between "
                     "readings", "correct": False,
             "why": "Its speed does not rise between readings; what the "
                    "drawing misses is the many direction changes it made in "
                    "the gap."},
            {"text": "Because the microscope shrinks the distances it shows",
             "correct": False,
             "why": "A microscope magnifies evenly and cannot hide part of a "
                    "path; the missing length is real travel between "
                    "readings."},
            {"text": "Because the dots are drawn too close together on the "
                     "page", "correct": False,
             "why": "How the dots are spaced on paper does not change how far "
                    "the speck actually went between them."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s18",
        "band": "standard",
        "text": "A student says warming a smoke cell 'gives the specks more "
                "energy to move with'. What is the more accurate "
                "description?",
        "options": [
            {"text": "The specks gain no energy at all when the cell is "
                     "warmed", "correct": False,
             "why": "The specks do end up moving faster; the description is "
                    "not that nothing changes, but where the extra energy "
                    "first goes."},
            {"text": "Warming speeds up the surrounding molecules, and their "
                     "harder strikes move the specks more", "correct": True},
            {"text": "Warming makes the specks lighter, so they move more "
                     "easily", "correct": False,
             "why": "Warming does not change a speck's mass at all; it "
                    "changes how hard the surrounding molecules strike it."},
            {"text": "Warming removes some of the air from the sealed cell, letting the "
            "remaining specks move about more freely", "correct": False,
             "why": "Nothing is removed by warming; the same air is there, "
                    "its molecules simply moving faster."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s19",
        "band": "standard",
        "text": "Why does a fine powder stirred into water keep moving long "
                "after the stirring has stopped?",
        "options": [
            {"text": "Because stirring adds a fixed amount of energy that slowly runs out "
            "over several hours", "correct": False,
             "why": "However long you wait, the jiggling never runs out on "
                    "its own — it continues for as long as the water has any "
                    "temperature at all."},
            {"text": "Because the container keeps up a very slight vibration of "
                     "its own, and that shaking is passed on to every grain "
                     "suspended in the water", "correct": False,
             "why": "The effect appears even in a container resting on a "
                    "solid, vibration-free surface."},
            {"text": "Because the water's own molecules keep striking the "
                     "grains, stirred or not", "correct": True},
            {"text": "Because fine powders are naturally unstable in water",
             "correct": False,
             "why": "Nothing about the powder itself is unstable; the "
                    "constant motion comes from the water's molecules."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s20",
        "band": "standard",
        "text": "A student argues that since molecules are too small to see, "
                "Brownian motion cannot really be evidence for them. What is "
                "wrong with that argument?",
        "options": [
            {"text": "Nothing — the argument is correct, and molecules were "
                     "only truly confirmed later by other means",
             "correct": False,
             "why": "Brownian motion, once explained and measured, was "
                    "accepted as strong evidence; being unseen is exactly "
                    "why an effect like this mattered so much."},
            {"text": "Evidence must always come from something you can see "
                     "directly", "correct": False,
             "why": "Plenty of accepted evidence in science comes from an "
                    "unseen cause's measurable effect, and this is a clear "
                    "example."},
            {"text": "Molecules can in fact be seen with a strong enough "
                     "light microscope", "correct": False,
             "why": "No light microscope, however strong, can resolve a "
                    "single molecule; that is exactly why an indirect effect "
                    "was needed."},
            {"text": "Seeing an effect caused only by something can be "
                     "strong evidence for that something, even unseen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s21",
        "band": "standard",
        "text": "Very fine dust stays suspended in still indoor air for "
                "hours, while grains of sand dropped into the same air settle "
                "within seconds. Explain the difference.",
        "options": [
            {"text": "Molecular strikes are enough to keep jostling a fine "
                     "speck about, but nowhere near enough to hold a sand "
                     "grain up", "correct": True},
            {"text": "Fine dust is less dense than the air around it while a "
                     "grain of sand is denser, so one is carried upwards and "
                     "the other is pulled straight down", "correct": False,
             "why": "Dust is far denser than air too; what keeps it up is "
                    "the constant jostling from air molecules, not a low "
                    "density."},
            {"text": "Sand grains attract one another and clump together as "
                     "they fall", "correct": False,
             "why": "Clumping is not what brings sand down; a sand grain is "
                    "simply far too big for molecular strikes to matter."},
            {"text": "Still air has no molecules moving about in it to hold "
                     "anything up", "correct": False,
             "why": "The molecules in still air never stop moving, and it is "
                    "exactly that motion that holds the dust up."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s22",
        "band": "standard",
        "text": "Which observation would most convince a sceptic that a "
                "jiggling smoke speck is not alive?",
        "options": [
            {"text": "That it is very small", "correct": False,
             "why": "Being small says nothing about whether something is "
                    "alive; plenty of very small things are."},
            {"text": "That the same jiggling appears in specks of ground-up "
                     "rock, which was never alive", "correct": True},
            {"text": "That it moves constantly without ever resting, and a "
                     "lifeless speck would have no way of keeping itself "
                     "going like that", "correct": False,
             "why": "Plenty of living things also move constantly; "
                    "restlessness alone does not settle it."},
            {"text": "That it is visible only under a microscope, and anything "
                     "needing that much magnification is far too small to be "
                     "a living thing", "correct": False,
             "why": "Needing a microscope to see something has no bearing on "
                    "whether it is alive."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s23",
        "band": "standard",
        "text": "A smoke cell and a cell of pollen in water are both at the "
                "same temperature. Why might the pollen jiggle less "
                "noticeably?",
        "options": [
            {"text": "Because water molecules move more slowly than air molecules "
                     "at the same temperature, so every strike on a pollen "
                     "grain carries a much gentler push", "correct": False,
             "why": "Water molecules are actually quoted as moving slightly "
                    "faster than air molecules at the same temperature."},
            {"text": "Because water is see-through and air is not",
             "correct": False,
             "why": "How transparent the fluid is has no bearing on the "
                    "jiggling it produces."},
            {"text": "Because a pollen grain is much bigger relative to a "
                     "water molecule than a smoke speck is to an air "
                     "molecule", "correct": True},
            {"text": "Because pollen is a solid and smoke is not",
             "correct": False,
             "why": "Both smoke specks and pollen grains are solid particles "
                    "suspended in a fluid."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s24",
        "band": "standard",
        "text": "A container of gas is left completely sealed and "
                "undisturbed for a month. Would Brownian motion still be "
                "observable inside it?",
        "options": [
            {"text": "No, because the motion needs to be freshly started by "
                     "disturbing the gas", "correct": False,
             "why": "Nothing needs to start it fresh; the molecules never "
                    "stop moving on their own."},
            {"text": "No, because a month is long enough for it to wear "
                     "itself out", "correct": False,
             "why": "It never wears out; it continues for as long as the gas "
                    "has any temperature."},
            {"text": "Only if the container is opened first to let in fresh "
                     "air", "correct": False,
             "why": "The sealed gas already has molecules of its own, "
                    "constantly striking anything suspended in it."},
            {"text": "Yes, because the gas's own molecules never stop moving",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s25",
        "band": "standard",
        "text": "Which of these best explains why a very large object, like "
                "a brick, shows no visible Brownian motion?",
        "options": [
            {"text": "So many molecules strike it from every side that the "
                     "imbalance is far too small to notice", "correct": True},
            {"text": "Bricks are not struck by air molecules at all",
             "correct": False,
             "why": "A brick is struck constantly, just as any object is; "
                    "the strikes simply cancel almost perfectly."},
            {"text": "Bricks are far too heavy for a push that small ever to "
                     "move them, however many molecules happen to arrive at "
                     "the same instant", "correct": False,
             "why": "No force is too small to move a brick in principle; it "
                    "is simply that the leftover imbalance is immeasurably "
                    "tiny against its weight."},
            {"text": "Air molecules avoid large surfaces", "correct": False,
             "why": "Nothing steers molecules away from anything; they "
                    "strike every surface from every direction."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s26",
        "band": "standard",
        "text": "A teacher demonstrates the smoke cell in a completely dark "
                "room, lit only by a very brief flash every few seconds. What "
                "would this show about the role of the lamp?",
        "options": [
            {"text": "That the jiggling happens during each flash of light and nowhere "
            "else", "correct": False,
             "why": "The jiggling is continuous; a flash only reveals a "
                    "snapshot of where the specks already were."},
            {"text": "That the specks keep moving between flashes, showing "
                     "the light is not what drives them", "correct": True},
            {"text": "That the microscope needs constant light to focus correctly", "correct": False,
             "why": "Focusing is a separate matter from what is causing the "
                    "movement itself."},
            {"text": "That the jiggling stops completely in the dark",
             "correct": False,
             "why": "It would carry on exactly as before; only the ability "
                    "to see it depends on the light."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s27",
        "band": "standard",
        "text": "Why can a description of Brownian motion not simply say "
                "'invisible things push the specks about', without more "
                "detail?",
        "options": [
            {"text": "Because that description is already completely accurate as it stands", "correct": False,
             "why": "It is too vague to be useful — it does not say what the "
                    "invisible things are or why the pushes leave anything "
                    "unbalanced."},
            {"text": "Because 'invisible' is not a real scientific word",
             "correct": False,
             "why": "The word itself is fine; the problem is that the "
                    "sentence explains nothing about the mechanism."},
            {"text": "Because it does not identify the molecules or explain "
                     "why the pushes do not simply cancel out completely",
             "correct": True},
            {"text": "Because the specks are not actually being pushed by "
                     "anything", "correct": False,
             "why": "They genuinely are being pushed, by huge numbers of "
                    "surrounding molecules."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s28",
        "band": "standard",
        "text": "Suppose a smoke speck were somehow struck completely evenly "
                "from every direction, with no leftover imbalance at all. "
                "What would you see?",
        "options": [
            {"text": "Extremely wild, fast jiggling", "correct": False,
             "why": "A perfectly even set of strikes would cancel out "
                    "entirely, leaving no push in any direction at all."},
            {"text": "The speck drifting steadily in one direction",
             "correct": False,
             "why": "Steady drift in one direction is what an unbalanced "
                    "current looks like, not the result of perfectly even "
                    "strikes."},
            {"text": "The speck spinning rapidly on the spot", "correct": False,
             "why": "Spinning is not what an imbalance of straight-line "
                    "pushes would cause; with no imbalance at all, there is "
                    "no push to move it."},
            {"text": "The speck sitting perfectly still", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s29",
        "band": "standard",
        "text": "A student wants to see Brownian motion for themselves at "
                "home, using cloudy juice viewed under a school microscope. "
                "Which detail matters most for it to work?",
        "options": [
            {"text": "The fine particles must be genuinely suspended and "
                     "small enough to be jiggled", "correct": True},
            {"text": "The juice must be a particular colour", "correct": False,
             "why": "Colour makes no difference to whether fine particles in "
                    "it jiggle."},
            {"text": "The microscope must be far more powerful than any ordinary school "
            "microscope could ever be", "correct": False,
             "why": "An ordinary microscope is exactly what is normally used "
                    "to see this effect; nothing more powerful is "
                    "required."},
            {"text": "The juice must be kept perfectly still, with no vibration "
                     "at all, because the slightest movement of the bench is "
                     "what produces the jiggling", "correct": False,
             "why": "Keeping it still helps rule out other causes, but the "
                    "jiggling itself needs no help from stillness — it comes "
                    "from the molecules."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-s30",
        "band": "standard",
        "text": "A sceptical student says the jiggling could just be caused "
                "by tiny vibrations in the building. Which observation best "
                "rules that out?",
        "options": [
            {"text": "That the specks are very small", "correct": False,
             "why": "Size alone says nothing about whether a building "
                    "vibration or molecular strikes is the cause."},
            {"text": "That neighbouring specks move independently, in "
                     "different directions at once", "correct": True},
            {"text": "That the jiggling can be seen under a microscope",
             "correct": False,
             "why": "Needing a microscope to see it does not tell you what "
                    "is causing it."},
            {"text": "That the cell is sealed", "correct": False,
             "why": "A sealed cell could still be shaken by a nearby "
                    "building vibration; it is the independent motion of "
                    "neighbouring specks that rules that out."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p11-02-h14",
        "band": "harder",
        "text": "A student suggests that a speck made of a much denser "
                "material, but exactly the same size, would jiggle less than "
                "a lighter one. Is that reasonable?",
        "options": [
            {"text": "No, because what a speck is made of has no bearing on "
                     "how it is pushed about", "correct": False,
             "why": "The push is indeed the same, but a heavier speck of the "
                    "same size is harder for that push to shift, so it moves "
                    "less."},
            {"text": "No, because a denser speck is struck harder by the "
                     "molecules around it", "correct": False,
             "why": "The strikes depend on the molecules, not on what the "
                    "speck is made of; a denser speck is struck exactly as "
                    "hard."},
            {"text": "Yes — the same leftover push has more mass to shift, "
                     "so it moves the speck less", "correct": True},
            {"text": "Yes, because a denser speck is struck far less often "
                     "than a lighter one", "correct": False,
             "why": "How often a speck is struck depends on its size, which "
                    "is the same in both cases here."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h15",
        "band": "harder",
        "text": "Jean Perrin's measurements confirmed Einstein's prediction "
                "and were also used to estimate how many molecules there are "
                "in a mole. What made that possible?",
        "options": [
            {"text": "He counted the molecules in his sample directly, one "
                     "at a time", "correct": False,
             "why": "No molecule was ever counted directly; the estimate "
                    "came from the specks' measured wandering instead."},
            {"text": "He weighed a known volume of smoke and divided it by the "
                     "mass of an average molecule, which is how the number in "
                     "a mole was first arrived at", "correct": False,
             "why": "His method used the measured wandering of suspended "
                    "specks, not a direct weighing of smoke."},
            {"text": "He used a microscope powerful enough to resolve "
                     "individual molecules", "correct": False,
             "why": "No microscope of his time, or since, resolves a single "
                    "molecule directly."},
            {"text": "The predicted relationship linking a speck's wandering "
                     "to molecule numbers could be solved once the "
                     "wandering was measured", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h16",
        "band": "harder",
        "text": "A student says that because a smoke speck cannot be pushed "
                "evenly from every side at once, Brownian motion is really "
                "quite unlikely to happen at all. What is wrong with this "
                "reasoning?",
        "options": [
            {"text": "It being unlikely to be pushed evenly is exactly why "
                     "an unbalanced leftover push is expected, not unlikely",
             "correct": True},
            {"text": "Nothing is wrong; Brownian motion genuinely is a very rare, unlikely "
            "event", "correct": False,
             "why": "It is not rare at all — with billions of strikes a "
                    "second, some imbalance is essentially guaranteed at "
                    "every instant."},
            {"text": "The reasoning would be right if the speck were "
                     "smaller", "correct": False,
             "why": "Making the speck smaller makes the same reasoning apply "
                    "even more strongly, not less; it does not change which "
                    "conclusion follows."},
            {"text": "The reasoning is only wrong for liquids, not for "
                     "gases", "correct": False,
             "why": "The same reasoning applies in both — perfectly even "
                    "strikes are never expected in either."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h17",
        "band": "harder",
        "text": "A very large, heavy object and a fine smoke speck are both "
                "bombarded by the same air molecules at the same "
                "temperature. Why does only the speck visibly jiggle?",
        "options": [
            {"text": "Because the heavy object is struck less often",
             "correct": False,
             "why": "Both are struck constantly by molecules from every "
                    "direction; what differs is how big the leftover "
                    "imbalance is compared with each object's own size."},
            {"text": "Because the leftover imbalance is far too small, compared with its "
            "own size, to move the heavy object noticeably at all", "correct": True},
            {"text": "Because heavy objects are made of chemically different "
                     "stuff from smoke specks, and molecules strike some "
                     "materials far harder than they strike others",
             "correct": False,
             "why": "Chemical make-up plays no part here; the difference is "
                    "purely one of relative size against the same kind of "
                    "molecular strikes."},
            {"text": "Because air molecules deliberately avoid heavy "
                     "objects", "correct": False,
             "why": "Nothing steers molecules toward or away from anything; "
                    "they strike every surface from every side."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h18",
        "band": "harder",
        "text": "Two smoke cells are set up identically, except that one has "
                "twice the concentration of smoke in it. Would you expect "
                "the JIGGLING of an individual speck to differ between the "
                "two cells?",
        "options": [
            {"text": "Yes, doubled specks make doubled jiggling",
             "correct": False,
             "why": "The concentration of smoke changes how many specks you "
                    "can see, not how each individual speck is struck by the "
                    "surrounding air molecules."},
            {"text": "Yes, the extra smoke slows the air molecules down",
             "correct": False,
             "why": "Smoke specks are far too few and far too large to "
                    "noticeably slow down the surrounding air molecules."},
            {"text": "No, because each speck's jiggling depends on the air "
                     "molecules around it, not on other specks", "correct": True},
            {"text": "It cannot be predicted without knowing the exact smoke particle size "
            "used in each of the two cells", "correct": False,
             "why": "The reasoning holds regardless of particle size — "
                    "jiggling depends on the surrounding molecules, not on "
                    "how much smoke is present."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h19",
        "band": "harder",
        "text": "Over an hour a jiggling speck ends up only a short distance "
                "from where it started, even though the total length of the "
                "path it travelled is enormous. Explain why.",
        "options": [
            {"text": "The speck slows down as the hour goes on, so the later "
                     "steps carry it barely anywhere", "correct": False,
             "why": "The jiggling does not slow down while the temperature "
                    "holds steady; the steps stay the same size throughout."},
            {"text": "Something pulls the speck back towards the point it "
                     "set out from", "correct": False,
             "why": "Nothing remembers where the speck started, and there is "
                    "no pull of any kind back towards that point."},
            {"text": "The microscope's field of view stops the speck "
                     "travelling any further away", "correct": False,
             "why": "The field of view limits what can be watched, not where "
                    "the speck is free to go."},
            {"text": "Each step's direction is chosen afresh, so the steps "
                     "largely cancel instead of adding up", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h20",
        "band": "harder",
        "text": "A liquid's molecules are quoted as moving at about 590 m/s "
                "at 20 °C, faster than air's quoted 500 m/s at the same "
                "temperature. Does this mean the liquid is hotter than the "
                "air?",
        "options": [
            {"text": "No — both are quoted at the same 20 °C; the different "
                     "speeds come from the two fluids being different "
                     "substances", "correct": True},
            {"text": "Yes, because a higher molecular speed always means a higher "
            "temperature, whatever the two substances happen to be", "correct": False,
             "why": "At the same stated temperature, a higher speed here "
                    "simply reflects a difference between the two "
                    "substances, not a temperature difference."},
            {"text": "Yes, because liquids are always hotter than gases",
             "correct": False,
             "why": "Liquids are not always hotter than gases; a liquid and "
                    "a gas can easily be at the same temperature, as stated "
                    "here."},
            {"text": "It cannot be judged without knowing the pressure of "
                     "each", "correct": False,
             "why": "The question already states both are at 20 °C; "
                    "pressure is not what is being asked about here."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h21",
        "band": "harder",
        "text": "A researcher wants to test whether building vibrations, "
                "rather than molecular strikes, are causing the jiggling "
                "seen in a lab. Suggest an experiment that would settle it.",
        "options": [
            {"text": "Repeat the observation using a much stronger microscope, "
                     "since the higher the magnification the more reliably a "
                     "cause can be identified", "correct": False,
             "why": "A stronger microscope would show the same jiggling in "
                    "more detail, but would not tell you what is causing "
                    "it."},
            {"text": "Move the same sealed cell to a location with far less "
                     "building vibration and see if the jiggling changes",
             "correct": True},
            {"text": "Ask several different people to watch the cell and describe "
                     "what they see, since a cause that several observers "
                     "agree on has been properly tested", "correct": False,
             "why": "Several observers agreeing on what they see does not "
                    "test what is causing the motion."},
            {"text": "Warm the cell and see if the jiggling gets faster",
             "correct": False,
             "why": "Warming would speed up the jiggling either way, whether "
                    "the cause is vibration or molecular strikes, so it "
                    "would not distinguish between them."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h22",
        "band": "harder",
        "text": "Why is it significant that Brownian motion happens "
                "identically in specks taken from completely different, "
                "unrelated materials — smoke, pollen, dust, ground rock?",
        "options": [
            {"text": "It shows that all of those materials are secretly the "
                     "same substance", "correct": False,
             "why": "They remain entirely different materials; what is "
                    "shared is only the effect the surrounding fluid's "
                    "molecules have on them."},
            {"text": "It shows that Brownian motion is a property of the "
                     "specks themselves", "correct": False,
             "why": "The opposite is closer to the truth — the jiggling "
                    "comes from what the surrounding fluid's molecules are "
                    "doing, not from any property unique to the specks."},
            {"text": "It shows the cause must lie in the surrounding fluid, "
                     "since that is the one thing all the cases share",
             "correct": True},
            {"text": "It shows that living things and non-living things behave completely "
            "identically in absolutely every situation", "correct": False,
             "why": "The shared behaviour here is specifically the jiggling "
                    "caused by a fluid's molecules, not a general claim "
                    "about living and non-living things."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h23",
        "band": "harder",
        "text": "A student argues: 'If molecules are too small to ever be "
                "seen, science can never really be sure they exist.' How "
                "would you respond, using the Brownian motion story?",
        "options": [
            {"text": "Agree completely — without seeing something directly, "
                     "nothing can be known about it", "correct": False,
             "why": "The Brownian motion story is a clear historical "
                    "counterexample to that claim."},
            {"text": "Point out that molecules were eventually seen directly, once "
            "microscopes became powerful enough to resolve them", "correct": False,
             "why": "No light microscope, however strong, has directly "
                    "resolved a single molecule; that is not how this case "
                    "was settled."},
            {"text": "Say that Brownian motion is unrelated to the question "
                     "of whether molecules are real", "correct": False,
             "why": "The whole force of the Brownian motion story is that it "
                    "settled exactly this question."},
            {"text": "Explain that a predicted, measurable effect of "
                     "something unseen can be strong, testable evidence for "
                     "it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h24",
        "band": "harder",
        "text": "A cell of smoke in air and a cell of dust in a sunbeam are "
                "both at room temperature. The dust bench value gives a "
                "ratio of about 50 000, and the smoke bench value about "
                "5000. Which speck would you expect to jiggle more, relative "
                "to its own size, if all else is equal?",
        "options": [
            {"text": "The smoke speck, since its ratio to the molecules "
                     "hitting it is smaller", "correct": True},
            {"text": "The dust speck, since a bigger object is struck by "
                     "molecules that are travelling faster, and a faster "
                     "strike shifts it further", "correct": False,
             "why": "Bigger objects generally jiggle less relative to their "
                    "own size, not more, since more of the strikes on them "
                    "cancel out."},
            {"text": "Neither — both jiggle by exactly the same relative amount regardless "
            "of size", "correct": False,
             "why": "The two ratios given are different, and the model "
                    "links a smaller ratio to relatively more jiggling."},
            {"text": "It cannot be judged from the ratios given",
             "correct": False,
             "why": "The ratios given are exactly what the model uses to "
                    "predict which jiggles relatively more."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h25",
        "band": "harder",
        "text": "Why would it be a mistake to say Brownian motion 'proves "
                "atoms exist beyond all possible doubt'?",
        "options": [
            {"text": "Because atoms had already been directly photographed "
                     "by 1905", "correct": False,
             "why": "No photograph of a single atom existed at that time; "
                    "the case rested on prediction and measurement, not on a "
                    "picture."},
            {"text": "Because science treats even strong, repeatedly-tested "
                     "evidence as the best current explanation, not an "
                     "absolute certainty", "correct": True},
            {"text": "Because Einstein's calculation was later shown to be "
                     "wrong", "correct": False,
             "why": "Einstein's prediction was measured and held up; that is "
                    "precisely why it was so influential."},
            {"text": "Because Perrin's measurements disagreed with Einstein's "
                     "prediction, and a claim contradicted once can never be "
                     "called proved afterwards", "correct": False,
             "why": "Perrin's measurements agreed with the prediction, which "
                    "is what made the case so persuasive."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h26",
        "band": "harder",
        "text": "A student proposes testing whether Brownian motion happens "
                "in a solid, by embedding fine specks inside a block of set "
                "jelly. What result would you predict, and why?",
        "options": [
            {"text": "Wild jiggling, because jelly contains a great deal of "
                     "water", "correct": False,
             "why": "Once the jelly has set, its particles are locked in a "
                    "fixed structure and can no longer move past one another "
                    "to strike the specks unevenly and freely."},
            {"text": "The same jiggling as in liquid water, since jelly is mostly water "
            "and water alone is what actually matters here, whatever else has "
            "been added to it", "correct": False,
             "why": "What matters is whether the surrounding particles are "
                    "free to move past each other, and a set jelly's "
                    "particles are locked in place, unlike liquid water's."},
            {"text": "Little or no jiggling, because a solid's particles are "
                     "not free to move past one another", "correct": True},
            {"text": "Faster jiggling than in a liquid, because jelly is far denser than "
            "water and packs more particles in", "correct": False,
             "why": "Density is not the deciding factor here; what matters "
                    "is whether the surrounding particles can move freely "
                    "enough to strike the specks unevenly."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h27",
        "band": "harder",
        "text": "Two students disagree about whether Brownian motion or "
                "diffusion gives stronger direct evidence for moving "
                "particles. What is the strongest argument for Brownian "
                "motion being the more direct of the two?",
        "options": [
            {"text": "Because diffusion happens far more slowly than Brownian "
                     "motion, and the slower a process runs the less "
                     "directly it can show you the particles behind it",
             "correct": False,
             "why": "How fast something happens is not what makes evidence "
                    "more or less direct."},
            {"text": "Because diffusion only happens in gases",
             "correct": False,
             "why": "Diffusion happens in liquids as well as gases, so this "
                    "does not distinguish the two."},
            {"text": "Because Brownian motion was discovered first",
             "correct": False,
             "why": "Which was discovered first says nothing about which "
                    "gives more direct evidence."},
            {"text": "Because Brownian motion shows one particle's "
                     "individual random path, caused directly by molecular "
                     "strikes, rather than an overall spreading pattern",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h28",
        "band": "harder",
        "text": "Why does the historical order — Brown's observation in "
                "1827, then Einstein's prediction in 1905, then Perrin's "
                "measurement afterwards — matter to how convincing the final "
                "case was?",
        "options": [
            {"text": "A prediction made before the confirming measurement "
                     "is stronger evidence than a story fitted to data "
                     "already known", "correct": True},
            {"text": "It does not matter at all; the order events happened "
                     "in is irrelevant to science", "correct": False,
             "why": "The order matters a great deal here — a prediction made "
                    "in advance and then confirmed is more persuasive than "
                    "an explanation invented afterwards to fit known "
                    "results."},
            {"text": "It matters only because Einstein needed Brown's formal permission "
            "before building on his earlier published observation", "correct": False,
             "why": "No such permission was needed or relevant; what "
                    "mattered was the logical and predictive structure of "
                    "the argument."},
            {"text": "It matters only for historical record-keeping, not for "
                     "the science itself", "correct": False,
             "why": "The order genuinely strengthens the scientific case, "
                    "because the prediction came before it was tested rather "
                    "than after."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h29",
        "band": "harder",
        "text": "A smoke cell at 20 °C and an identical one at 100 °C are "
                "compared. Which of these differences would you NOT expect "
                "between them?",
        "options": [
            {"text": "The hotter cell's specks travelling further each "
                     "second", "correct": False,
             "why": "This IS expected — warmer molecules push harder, giving "
                    "a bigger leftover imbalance each second."},
            {"text": "The hotter cell's specks eventually settling to the "
                     "bottom", "correct": True},
            {"text": "The hotter cell's jiggling looking wilder overall to "
                     "anyone watching it through the microscope",
             "correct": False,
             "why": "This IS expected — faster molecules at the higher "
                    "temperature produce a bigger, wilder-looking leftover "
                    "push."},
            {"text": "Both cells continuing to jiggle indefinitely at their "
                     "own temperature", "correct": False,
             "why": "This IS expected in both cells — jiggling never stops "
                    "as long as a temperature, any temperature, is "
                    "maintained."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-h30",
        "band": "harder",
        "text": "A textbook states that Brownian motion 'proves that matter "
                "is made of particles too small to see'. Assess how "
                "carefully worded this claim is.",
        "options": [
            {"text": "It is completely wrong, since matter's particle structure was "
            "already perfectly obvious to everyone well before 1827",
             "correct": False,
             "why": "The particle nature of matter was very much in "
                    "question before this evidence, not already an obvious, "
                    "settled fact."},
            {"text": "It is completely right, and no better wording is "
                     "possible", "correct": False,
             "why": "'Proves' overstates how science actually treats even "
                    "strong evidence; it is more careful to say the "
                    "observation gives strong support for the particle "
                    "model."},
            {"text": "It overstates the case slightly; 'gives strong "
                     "evidence for' would be more careful than 'proves'",
             "correct": True},
            {"text": "It is wrong because Brownian motion has nothing whatsoever to do "
            "with the size of particles, and would be an equally strong argument "
            "either way", "correct": False,
             "why": "The whole argument turns on the relative sizes of the "
                    "speck and the particles striking it, so size is central "
                    "to the claim."},
        ],
        "figure": None,
    },
]
