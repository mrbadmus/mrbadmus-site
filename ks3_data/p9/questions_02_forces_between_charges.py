"""P9 lesson 02 — Forces between charges: twelve questions (MRB-223).

Written against Design's page. The two balloons, the two spheres on their
stands and the nine-case table are hers.

The discriminations, in the order the lesson builds them:

  · like repels and unlike attracts, with EQUAL AND OPPOSITE forces;
  · the force falls fast with distance — not in step with it (`CHRG-07`);
  · a charged object attracts a NEUTRAL one, and that is a real effect
    with a name (`CHRG-08`);
  · so attraction proves nothing and only repulsion does (`CHRG-05`) —
    the harder band sits here.

⚠️ NO FORCE IN NEWTONS APPEARS IN ANY QUESTION. Ruled 21 Aug 2026 for the
bench, and the bank follows the page: every comparison here is relative
("about a quarter", "much weaker"), because the coefficient behind the
induced case is chosen rather than measured and the equation for the
charged case is beyond this stage.

⚠️ POSITION IS AUTHORED — 1,2,3,0 · 3,0,2,1 · 2,3,0,1, three of each.

⚠️ Neither marked rung is restated: the hanging metal-coated ball and the
5 cm → 10 cm doubling are the ladder's, and nothing here reuses either.
"""

UNIT = "P9"
LESSON = "forces-between-charges"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p9-02-e01",
        "band": "easier",
        "text": "Two objects both carry a negative charge. What do they do?",
        "options": [
            {"text": "Attract", "correct": False,
             "why": "Attraction needs the two charges to be opposite. Two "
                    "negatives are alike, so they push."},
            {"text": "Repel", "correct": True},
            {"text": "Nothing", "correct": False,
             "why": "Nothing happens only when both objects are neutral. "
                    "Two charged objects always act on each other."},
            {"text": "It depends which of the two is carrying the larger "
                     "charge", "correct": False,
             "why": "The size changes how strong the push is, never whether "
                    "it is a push or a pull. That is set by the signs."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e02",
        "band": "easier",
        "text": "A positively charged sphere and a negatively charged "
                "sphere are held near each other. Which statement about the "
                "forces is right?",
        "options": [
            {"text": "Only the lighter one feels a force", "correct": False,
             "why": "Both feel one. Mass decides how much each one MOVES, "
                    "not whether a force acts on it."},
            {"text": "The one with more charge feels the larger force",
             "correct": False,
             "why": "Both forces are always the same size, however "
                    "different the two charges are."},
            {"text": "They are equal in size and opposite in direction",
             "correct": True},
            {"text": "The positive one feels a push and the negative one "
                     "feels a pull", "correct": False,
             "why": "Both are pulled, towards each other. Unlike charges "
                    "attract, and they attract each other."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e03",
        "band": "easier",
        "text": "Two spheres are both left completely neutral and brought "
                "close together. What happens?",
        "options": [
            {"text": "They attract weakly, by induction", "correct": False,
             "why": "Induction needs one of them to be charged. With no "
                    "charge anywhere there is nothing to push the other "
                    "one's charges aside."},
            {"text": "They repel weakly, because both hold electrons",
             "correct": False,
             "why": "Every object holds electrons, and every object holds "
                    "matching protons. Neutral means the two balance."},
            {"text": "They attract strongly, because neutral objects share "
                     "their charge", "correct": False,
             "why": "There is no charge to share. Neutral is not a store of "
                    "charge waiting to be handed over."},
            {"text": "Nothing at all", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e04",
        "band": "easier",
        "text": "A charged rod is brought near a scrap of paper that nobody "
                "has touched. What is the paper's total charge while it is "
                "being lifted?",
        "options": [
            {"text": "Zero — it is neutral throughout", "correct": True},
            {"text": "Opposite to the rod", "correct": False,
             "why": "Its NEAR FACE becomes opposite. The paper as a whole "
                    "has gained and lost nothing."},
            {"text": "The same as the rod", "correct": False,
             "why": "If it were, the rod would push it away rather than "
                    "pick it up."},
            {"text": "Opposite to the rod on the near side and larger "
                     "overall, because the rod has added charge to it",
             "correct": False,
             "why": "Nothing was added. The paper's own charges just moved "
                    "within it, and the two faces still add to zero."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p9-02-s01",
        "band": "standard",
        "text": "A charged rod attracts a small hanging ball. Which single "
                "further observation would prove the ball is charged?",
        "options": [
            {"text": "Bringing the rod closer and finding that the pull "
                     "on the ball gets much stronger", "correct": False,
             "why": "It gets stronger for a neutral ball too — induction "
                    "falls off with distance even faster."},
            {"text": "Weighing the ball before and after to see whether "
                     "it has gained any mass", "correct": False,
             "why": "The electrons involved weigh nothing you could "
                    "measure, and a neutral ball would weigh the same "
                    "either way."},
            {"text": "Watching whether the ball swings towards the rod from "
                     "further away than before", "correct": False,
             "why": "Distance changes the size of the pull, not what causes "
                    "it. A neutral ball behaves the same way."},
            {"text": "Bringing up a second rod with the opposite charge and "
                     "finding the ball is pushed away", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s02",
        "band": "standard",
        "text": "A negatively charged balloon is held near a neutral wall. "
                "What happens to the wall's own charges?",
        "options": [
            {"text": "Electrons in the wall are pushed away from the "
                     "surface, leaving the near face positive",
             "correct": True},
            {"text": "Electrons in the wall are pulled towards the "
                     "surface, leaving the near face negative",
             "correct": False,
             "why": "The balloon is negative, so it PUSHES the wall's "
                    "electrons away rather than pulling them in."},
            {"text": "Protons in the wall move towards the surface, "
                     "leaving the far face negative",
             "correct": False,
             "why": "Protons never move. Everything that happens here is "
                    "electrons shifting."},
            {"text": "Electrons cross from the balloon onto the wall, "
                     "sharing the charge between them", "correct": False,
             "why": "Nothing crosses the gap. The wall's total charge is "
                    "unchanged throughout — that is what makes this "
                    "induction rather than a transfer."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s03",
        "band": "standard",
        "text": "Two charged spheres are moved from 4 cm apart to 12 cm "
                "apart. Roughly what happens to the force?",
        "options": [
            {"text": "It falls to about a third", "correct": False,
             "why": "That would be the answer if the force tracked the "
                    "distance. It falls much faster than that."},
            {"text": "It stays the same, because the charges have not "
                     "changed", "correct": False,
             "why": "The force depends on the separation as well as on the "
                    "charges."},
            {"text": "It falls to about a ninth", "correct": True},
            {"text": "It falls to about a sixth, because the distance "
                     "tripled and the pair shares the drop between them",
             "correct": False,
             "why": "There is nothing to share. Both spheres feel the same "
                    "force, and it falls to about a ninth for both."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s04",
        "band": "standard",
        "text": "In the nine-case table of every charge combination, how "
                "many of the nine give no force at all?",
        "options": [
            {"text": "Two", "correct": False,
             "why": "The two cases where both objects carry the same sign "
                    "repel, which is very much a force. The no-force case is "
                    "the one with no charge anywhere."},
            {"text": "One", "correct": True},
            {"text": "None", "correct": False,
             "why": "Two neutral objects genuinely do nothing to each "
                    "other, and that is the one case in the table that "
                    "gives no force."},
            {"text": "Four", "correct": False,
             "why": "Four of the nine are the induction case, and those all "
                    "attract weakly. Only one gives nothing."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p9-02-h01",
        "band": "harder",
        "text": "A student writes: \"The rod attracted the foil, so the "
                "foil must have the opposite charge.\" What is wrong with "
                "the reasoning?",
        "options": [
            {"text": "Nothing — attraction between unlike charges is the "
                     "standard rule", "correct": False,
             "why": "The rule is right and the inference is not. Attraction "
                    "has two possible causes and this observation cannot "
                    "tell them apart."},
            {"text": "The rod would have to be neutral for the foil to be "
                     "attracted to it", "correct": False,
             "why": "A neutral rod would do nothing at all. The rod is "
                    "certainly charged; it is the foil that is undecided."},
            {"text": "A neutral foil would be attracted too, so the "
                     "observation cannot decide", "correct": True},
            {"text": "Foil is a conductor, so it can never be charged and "
                     "the conclusion is impossible", "correct": False,
             "why": "A conductor can certainly be charged — it just has to "
                    "be insulated from earth. The flaw is in the inference, "
                    "not in the foil."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h02",
        "band": "harder",
        "text": "Electrostatic paint spraying charges the droplets and "
                "earths the car body. Why does the paint wrap round the "
                "edges instead of drifting past?",
        "options": [
            {"text": "The charged droplets repel each other so hard that "
                     "some of them are pushed round to the far side",
             "correct": False,
             "why": "They do repel each other, which spreads the spray — "
                    "but what pulls paint onto the far side is the metal "
                    "attracting it."},
            {"text": "Earthing turns the body into a magnet, and the "
                     "paint has iron powder mixed into it", "correct": False,
             "why": "Nothing here is magnetic. It is charge and induction "
                    "throughout."},
            {"text": "The droplets are heavier than air, so they settle "
                     "onto whatever surface is beneath them", "correct": False,
             "why": "Gravity would drop them straight down. The paint goes "
                    "sideways and round corners, towards the metal."},
            {"text": "The charged droplets induce the opposite charge in "
                     "the metal, so every part of the body pulls on them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h03",
        "band": "harder",
        "text": "Two charged objects are sealed in a jar and all the air is "
                "pumped out. What happens to the force between them?",
        "options": [
            {"text": "It is unchanged", "correct": True},
            {"text": "It disappears, because there is nothing left to carry "
                     "it across the gap", "correct": False,
             "why": "Nothing was carrying it in the first place. Air is not "
                    "the messenger, and taking it away changes nothing."},
            {"text": "It gets weaker, because thinner air passes the force "
                     "on less well", "correct": False,
             "why": "Air was never passing it on, so removing air cannot "
                    "weaken it."},
            {"text": "It gets stronger, because the air was in the way and "
                     "was absorbing part of the push", "correct": False,
             "why": "The air was not absorbing anything. The force in a "
                    "vacuum is the same force it was in the jar."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h04",
        "band": "harder",
        "text": "One sphere is charged and one is neutral. The gap between "
                "them is doubled. Compared with two CHARGED spheres over "
                "the same change of gap, the attraction falls…",
        "options": [
            {"text": "by the same amount, because distance affects every "
                     "case in the same way", "correct": False,
             "why": "Induction depends on the separation twice over — once "
                    "to shift the neutral object's charges, once to pull on "
                    "them — so it falls faster."},
            {"text": "faster, because the induced charges also get smaller "
                     "as the gap grows", "correct": True},
            {"text": "more slowly, because an induced charge takes time to "
                     "settle back", "correct": False,
             "why": "The charges rearrange instantly, and nothing here "
                    "depends on time."},
            {"text": "not at all, because a neutral object is either "
                     "attracted or it is not", "correct": False,
             "why": "The pull is real and it varies. Move the charged "
                    "sphere far enough away and the attraction becomes far "
                    "too weak to see."},
        ],
        "figure": None,
    },
]
