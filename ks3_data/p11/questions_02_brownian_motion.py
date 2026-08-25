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
            {"text": "The smoke specks", "correct": True},
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
            {"text": "It stops", "correct": False,
             "why": "It never stops at any temperature. Warming makes it "
                    "wilder, not quieter."},
            {"text": "It slows down", "correct": False,
             "why": "Warming speeds every molecule up, so the strikes are "
                    "harder and the leftover push is bigger."},
            {"text": "It gets faster and more violent", "correct": True},
            {"text": "It stays exactly the same", "correct": False,
             "why": "Temperature is what sets molecular speed, so it changes "
                    "the jiggling directly."},
        ],
        "figure": None,
    },
    {
        "id": "p11-02-e04",
        "band": "easier",
        "text": "Why do the strikes on a smoke speck nearly cancel out?",
        "options": [
            {"text": "Because the molecules are all moving at the same speed",
             "correct": False,
             "why": "They are not, and it would not matter if they were. What "
                    "cancels them is the number arriving from every side at "
                    "once."},
            {"text": "Because the speck is heavy enough to resist them",
             "correct": False,
             "why": "A speck heavy enough to resist them would not move at "
                    "all, and this one does."},
            {"text": "Because half the molecules are moving and half are "
                     "still", "correct": False,
             "why": "Every molecule in a fluid is moving, all the time. None "
                    "of them is still."},
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
            {"text": "The specks are lit from the side", "correct": False,
             "why": "That is how you see them, not why they move. It says "
                    "nothing about draughts."},
            {"text": "A draught would carry every speck the same way at once, "
                     "and they go in every direction", "correct": True},
            {"text": "The specks are made of burnt material", "correct": False,
             "why": "True, and it rules out something alive rather than "
                    "something blowing."},
            {"text": "The cell is sealed and still, so nothing outside it can be "
                     "moving the air about", "correct": False,
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
            {"text": "That it is smooth and continuous all the way down",
             "correct": False,
             "why": "A smooth fluid would push on the speck evenly and it "
                    "would sit still. The jiggle is what rules that out."},
            {"text": "That it is always flowing in one direction",
             "correct": False,
             "why": "The pushes come from every direction, and the speck's "
                    "path changes constantly."},
            {"text": "That it contains something alive", "correct": False,
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
            {"text": "Water molecules move faster, so they push the grain "
                     "further", "correct": False,
             "why": "Water molecules at 20 °C are quoted at about 590 m/s "
                    "against air's 500, so their speed is not why the grain "
                    "moves less."},
            {"text": "The water must be colder than the air", "correct": False,
             "why": "Both are at the same temperature; that is what the "
                    "question says."},
            {"text": "A pollen grain is far bigger, so the leftover push "
                     "shifts it less", "correct": True},
            {"text": "Water molecules are too large to move a pollen grain",
             "correct": False,
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
            {"text": "It showed the specks under a far stronger microscope",
             "correct": False,
             "why": "No microscope shows a molecule, and the argument never "
                    "needed one."},
            {"text": "It proved that pollen is alive", "correct": False,
             "why": "The opposite: the same jiggling happens in ground-up "
                    "rock."},
            {"text": "It measured the speed of the air molecules directly",
             "correct": False,
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
]
