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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "It falls to about a ninth, three squared",
             "correct": True},
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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "It is unchanged, because an electric force needs "
                     "no air to carry it", "correct": True},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p9-02-e05",
        "band": "easier",
        "text": "Two objects carry opposite charges. What do they do?",
        "options": [
            {"text": "Attract each other", "correct": True},
            {"text": "Repel each other", "correct": False,
             "why": "Repulsion happens between two charges of the SAME "
                    "sign."},
            {"text": "Do nothing until they touch", "correct": False,
             "why": "The force acts across a gap, with nothing in between."},
            {"text": "Cancel out and become neutral", "correct": False,
             "why": "Their charges stay as they are unless electrons actually "
                    "move between them."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e06",
        "band": "easier",
        "text": "Which observation PROVES that both of two objects are "
                "charged?",
        "options": [            {"text": "They attract each other", "correct": False,
             "why": "A charged object attracts a neutral one too, so "
                    "attraction proves nothing on its own."},
            {"text": "They stick together on contact", "correct": False,
             "why": "Sticking follows attraction, which a neutral object also "
                    "shows."},
            {"text": "One picks the other up", "correct": False,
             "why": "That is attraction again, and a neutral scrap of paper "
                    "behaves the same way."},
            {"text": "They repel each other", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e07",
        "band": "easier",
        "text": "Two charged objects are moved further apart. The force "
                "between them…",
        "options": [
            {"text": "stays the same at any distance", "correct": False,
             "why": "It falls off quickly, which is why the effect is only "
                    "noticeable close up."},
            {"text": "gets stronger", "correct": False,
             "why": "Moving apart weakens it; moving closer is what "
                    "strengthens it."},
            {"text": "gets weaker", "correct": True},
            {"text": "disappears completely beyond a fixed distance",
             "correct": False,
             "why": "It never quite reaches zero; it simply becomes too small "
                    "to notice."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e08",
        "band": "easier",
        "text": "The two forces between a pair of charged objects are…",
        "options": [
            {"text": "equal in size and opposite in direction",
             "correct": True},
            {"text": "larger on the object with more charge", "correct": False,
             "why": "The pair is always equal, whatever the two charges "
                    "are."},
            {"text": "larger on the smaller object", "correct": False,
             "why": "Size makes no difference to the pair; both feel the same "
                    "force."},
            {"text": "in the same direction, so the pair moves off together",
             "correct": False,
             "why": "They act on each other, so the two forces point opposite "
                    "ways."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e09",
        "band": "easier",
        "text": "A charged rod is held near a neutral scrap of foil. What "
                "happens?",
        "options": [            {"text": "The foil is attracted to the rod", "correct": True},
            {"text": "Nothing, because the foil has no charge",
             "correct": False,
             "why": "The rod moves the foil's own electrons, and the foil is "
                    "pulled in."},
            {"text": "The foil is repelled by the rod", "correct": False,
             "why": "Repulsion needs both objects charged with the same "
                    "sign."},
            {"text": "The foil becomes charged with the same sign as the rod",
             "correct": False,
             "why": "Its total charge does not change at all; its own charges "
                    "simply shift within it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e10",
        "band": "easier",
        "text": "Do two charged objects have to touch for a force to act "
                "between them?",
        "options": [
            {"text": "Yes, or the air must carry the force across",
             "correct": False,
             "why": "The force acts in a vacuum too, so the air is not "
                    "carrying it."},
            {"text": "Yes, but only for very small charges", "correct": False,
             "why": "No size of charge requires contact; the force reaches "
                    "across a gap."},
            {"text": "No — the force acts across a gap", "correct": True},
            {"text": "No, but only if one of them is a metal",
             "correct": False,
             "why": "It works between two insulators just as well."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e11",
        "band": "easier",
        "text": "When a charged object moves a neutral object's own electrons "
                "to one side, that is called…",
        "options": [            {"text": "conduction", "correct": False,
             "why": "Conduction is charge travelling through a material to "
                    "somewhere else."},
            {"text": "friction", "correct": False,
             "why": "Friction is the rubbing that separates charge in the "
                    "first place."},
            {"text": "repulsion", "correct": False,
             "why": "Repulsion is a push between two like charges, not a "
                    "shift within one object."},
            {"text": "induction", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e12",
        "band": "easier",
        "text": "Two positively charged spheres are brought close together. "
                "What happens?",
        "options": [            {"text": "They repel", "correct": True},
            {"text": "They attract", "correct": False,
             "why": "Attraction needs opposite signs, and both of these are "
                    "positive."},
            {"text": "Nothing, because positive charges do not act on each "
                     "other",
             "correct": False,
             "why": "They act strongly on each other — that is what a like "
                    "pair does."},
            {"text": "They swap charge until both are neutral",
             "correct": False,
             "why": "Nothing is exchanged across a gap; both keep the charge "
                    "they have."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e13",
        "band": "easier",
        "text": "While a charged rod holds a neutral scrap of paper near it, "
                "what is the paper's TOTAL charge?",
        "options": [
            {"text": "The same sign as the rod", "correct": False,
             "why": "Its charges have shifted within it, but nothing has been "
                    "added or taken away."},
            {"text": "The opposite sign to the rod", "correct": False,
             "why": "The near FACE is opposite, but the paper as a whole is "
                    "still balanced."},
            {"text": "Zero — it is still neutral overall", "correct": True},
            {"text": "Impossible to say without touching it", "correct": False,
             "why": "No charge has crossed the gap, so its total is unchanged "
                    "at zero."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e14",
        "band": "easier",
        "text": "A negatively charged balloon is held near a wall and sticks "
                "to it. What does that tell you about the wall?",
        "options": [
            {"text": "That the wall must be positively charged",
             "correct": False,
             "why": "Attraction does not prove the wall is charged at all; a "
                    "neutral wall behaves this way."},
            {"text": "That the wall must be negatively charged",
             "correct": False,
             "why": "Two negatives would repel, and the balloon clearly "
                    "does not fly away."},
            {"text": "That the wall may be neutral, since attraction proves "
                     "nothing",
             "correct": True},
            {"text": "That the wall must be a good conductor of charge",
             "correct": False,
             "why": "A plaster wall is an insulator, and the effect works "
                    "either way."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e15",
        "band": "easier",
        "text": "Two like charges are brought twice as close together. The "
                "force between them…",
        "options": [
            {"text": "halves", "correct": False,
             "why": "Coming closer strengthens the force, so it cannot fall."},
            {"text": "stays the same", "correct": False,
             "why": "Distance is one of the things the force depends on, so "
                    "it must change."},
            {"text": "gets much stronger", "correct": True},
            {"text": "reverses direction and becomes attraction",
             "correct": False,
             "why": "Like charges repel at every distance; nothing flips the "
                    "sign."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e16",
        "band": "easier",
        "text": "Two neutral objects are brought close together. What force "
                "acts between them because of charge?",
        "options": [
            {"text": "A strong attraction", "correct": False,
             "why": "Attraction between a charged and a neutral object needs "
                    "one of them to be charged."},
            {"text": "A strong repulsion", "correct": False,
             "why": "Repulsion needs both to be charged with the same sign."},
            {"text": "None worth speaking of", "correct": True},
            {"text": "An attraction that grows as they get closer",
             "correct": False,
             "why": "With neither of them charged there is nothing to set an "
                    "attraction going."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e17",
        "band": "easier",
        "text": "A charged rod attracts a hanging ball. Which is still "
                "possible?",
        "options": [            {"text": "The ball is charged the same way as the rod",
             "correct": False,
             "why": "Two like charges repel, so the ball would swing away "
                    "rather than towards."},
            {"text": "The ball must be neutral", "correct": False,
             "why": "An oppositely charged ball is attracted as well, so this "
                    "rules out too much."},
            {"text": "The ball must be charged the opposite way",
             "correct": False,
             "why": "It might be, but a neutral ball is attracted too, so it "
                    "is not the only possibility."},
            {"text": "The ball is neutral, or charged the opposite way",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p9-02-s05",
        "band": "standard",
        "text": "Two charged spheres repel at 3 cm apart and are moved to "
                "6 cm. Roughly what happens to the force?",
        "options": [            {"text": "It falls to about a quarter", "correct": True},
            {"text": "It halves, in step with the distance", "correct": False,
             "why": "The force falls much faster than the distance grows; "
                    "halving would be too gentle."},
            {"text": "It stays the same at any separation", "correct": False,
             "why": "Distance matters a great deal, which is why the effect "
                    "is only noticed close up."},
            {"text": "It doubles as they separate", "correct": False,
             "why": "Moving apart always weakens the force between two "
                    "charges."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s06",
        "band": "standard",
        "text": "A negatively charged balloon is held near a neutral wall. "
                "What do the wall's own charges do?",
        "options": [
            {"text": "The wall's electrons are pushed away, leaving the near "
                     "face positive",
             "correct": True},
            {"text": "The wall's electrons are pulled towards the balloon",
             "correct": False,
             "why": "The balloon is negative, so it PUSHES the wall's "
                    "electrons away rather than pulling them in."},
            {"text": "The wall's protons move to the near face",
             "correct": False,
             "why": "Protons never move; only the electrons shift."},
            {"text": "Nothing moves, because the wall is an insulator",
             "correct": False,
             "why": "Even in an insulator the charges shift slightly within "
                    "each particle, which is enough."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s07",
        "band": "standard",
        "text": "A charged rod attracts a hanging ball. Which single further "
                "test would prove the ball is charged?",
        "options": [
            {"text": "Bring the rod closer and see whether the attraction "
                     "grows",
             "correct": False,
             "why": "It grows for a neutral ball as well, so this separates "
                    "nothing."},
            {"text": "Touch the ball with the rod and see whether it moves",
             "correct": False,
             "why": "Touching CHANGES the ball's charge, so the test destroys "
                    "what it is meant to measure."},
            {"text": "Bring up a rod with the opposite charge and look for "
                     "repulsion",
             "correct": True},
            {"text": "Weigh the ball before and after the rod is brought "
                     "near",
             "correct": False,
             "why": "No measurable mass changes, and mass would not show a "
                    "charge in any case."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s08",
        "band": "standard",
        "text": "A rubbed balloon picks up small scraps of paper that nobody "
                "has charged. Why?",
        "options": [            {"text": "Because the paper was charged by the air around it",
             "correct": False,
             "why": "The paper is neutral, and it does not need to be charged "
                    "for this to work."},
            {"text": "Because the balloon gives the paper some of its charge "
                     "across the gap",
             "correct": False,
             "why": "Nothing crosses the gap; the paper's total charge stays "
                    "at zero."},
            {"text": "Because paper is always slightly positive",
             "correct": False,
             "why": "Untouched paper is neutral; the balloon is what shifts "
                    "its charges."},
            {"text": "Because the balloon moves the paper's own charges, "
                     "leaving the near face opposite",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s09",
        "band": "standard",
        "text": "Two identical spheres repel with a force of 8 units at "
                "10 cm. They are moved to 20 cm apart. About what force is "
                "left?",
        "options": [            {"text": "2 units", "correct": True},
            {"text": "4 units", "correct": False,
             "why": "That halves it in step with the distance, and the force "
                    "falls far faster than that."},
            {"text": "8 units, unchanged", "correct": False,
             "why": "Distance changes the force a great deal, so it cannot "
                    "hold still."},
            {"text": "16 units", "correct": False,
             "why": "Moving apart weakens the force; nothing about separating "
                    "them makes it stronger."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s10",
        "band": "standard",
        "text": "A positively charged sphere and a negatively charged sphere "
                "are held apart. Which statement about the forces is right?",
        "options": [
            {"text": "The positive one pulls harder, because positive is "
                     "stronger",
             "correct": False,
             "why": "Neither sign is stronger; the two forces are always "
                    "equal."},
            {"text": "Only the negative one feels a force", "correct": False,
             "why": "Both feel one — forces between charges always come in "
                    "pairs."},
            {"text": "Each is pulled towards the other with the same size of "
                     "force",
             "correct": True},
            {"text": "The larger sphere feels the larger force",
             "correct": False,
             "why": "Size does not change the pair; both forces match "
                    "exactly."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s11",
        "band": "standard",
        "text": "Two hanging balls both swing apart when brought near each "
                "other. What can you conclude?",
        "options": [
            {"text": "Both are charged, with the same sign", "correct": True},
            {"text": "Both are charged, with opposite signs", "correct": False,
             "why": "Opposite charges would pull them together, not push them "
                    "apart."},
            {"text": "One is charged and one is neutral", "correct": False,
             "why": "A charged ball and a neutral one attract, so they would "
                    "swing towards each other."},
            {"text": "Both are neutral", "correct": False,
             "why": "Two neutral balls do nothing to each other, so nothing "
                    "would swing."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s12",
        "band": "standard",
        "text": "Why does a charged rod pick up a scrap of paper and then "
                "sometimes throw it off again after contact?",
        "options": [            {"text": "Because the paper dries out and becomes lighter",
             "correct": False,
             "why": "Nothing about the paper's mass changes in that "
                    "instant."},
            {"text": "Because the air pushes the paper away once it is "
                     "warmed",
             "correct": False,
             "why": "The air is not involved; the paper is being repelled by "
                    "the rod."},
            {"text": "Because the rod's charge changes sign when it touches "
                     "anything",
             "correct": False,
             "why": "The rod keeps its sign; it is the paper that has "
                    "changed."},
            {"text": "Because on contact the paper takes the rod's sign, and "
                     "like charges repel",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s13",
        "band": "standard",
        "text": "Why is attraction alone not enough to show that an object is "
                "charged?",
        "options": [            {"text": "Because a charged object attracts a neutral one as "
                     "well",
             "correct": True},
            {"text": "Because attraction is always too weak to measure",
             "correct": False,
             "why": "It is easily strong enough to lift paper; strength is "
                    "not the problem."},
            {"text": "Because attraction only happens between two neutral "
                     "objects",
             "correct": False,
             "why": "Two neutral objects do nothing; attraction needs at "
                    "least one charge."},
            {"text": "Because attraction and repulsion look the same from a "
                     "distance",
             "correct": False,
             "why": "They are easy to tell apart — one pulls together and one "
                    "pushes away."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s14",
        "band": "standard",
        "text": "A charged rod is held near a hanging ball and nothing "
                "happens at all. What does that suggest?",
        "options": [
            {"text": "That the ball is charged with the same sign as the rod",
             "correct": False,
             "why": "Like charges repel, so the ball would swing clearly "
                    "away."},
            {"text": "That the ball is charged with the opposite sign",
             "correct": False,
             "why": "Opposite charges attract, so the ball would swing "
                    "towards the rod."},
            {"text": "That the rod has lost its charge", "correct": True},
            {"text": "That the ball is neutral", "correct": False,
             "why": "A neutral ball is still attracted, by induction, so it "
                    "would move."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s15",
        "band": "standard",
        "text": "Two charged spheres are moved from 2 cm apart to 1 cm apart. "
                "Roughly what happens to the force?",
        "options": [
            {"text": "It doubles as they approach", "correct": False,
             "why": "The force grows faster than the distance shrinks, so "
                    "doubling is too little."},
            {"text": "It halves as they approach", "correct": False,
             "why": "Coming closer strengthens the force rather than "
                    "weakening it."},
            {"text": "It becomes about four times as large", "correct": True},
            {"text": "It stays the same at any separation", "correct": False,
             "why": "Distance has a large effect, which is why the spheres "
                    "must be positioned carefully."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s16",
        "band": "standard",
        "text": "Two like-charged balls hang side by side and settle a fixed "
                "distance apart. What is happening?",
        "options": [
            {"text": "The charges have cancelled, so they hang still",
             "correct": False,
             "why": "Cancelling would let them hang vertically, touching; "
                    "they are held apart."},
            {"text": "The repulsion has run out at that distance",
             "correct": False,
             "why": "The force does not run out; it is balanced by the "
                    "threads and their weight."},
            {"text": "The repulsion is balanced by the threads and their "
                     "weight",
             "correct": True},
            {"text": "The air between them is holding them apart",
             "correct": False,
             "why": "It works in a vacuum too, so the air is not what holds "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s17",
        "band": "standard",
        "text": "A charged rod is brought near a can standing on an "
                "insulating mat, and the can rolls towards it. What is the "
                "can's charge?",
        "options": [
            {"text": "The opposite sign to the rod", "correct": False,
             "why": "Its near face is opposite, but the can as a whole may "
                    "well still be neutral."},
            {"text": "The same sign as the rod", "correct": False,
             "why": "Like charges repel, and the can is rolling towards the "
                    "rod."},
            {"text": "Zero, or the opposite sign — attraction cannot tell "
                     "them apart",
             "correct": True},
            {"text": "Zero, because a metal can cannot hold charge",
             "correct": False,
             "why": "On an insulating mat it holds charge perfectly well; "
                    "attraction simply does not prove it has any."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p9-02-h05",
        "band": "harder",
        "text": "A charged rod attracts a neutral ball. A student says the "
                "ball's total charge must have changed. What is right?",
        "options": [
            {"text": "The total is unchanged; the charges have only shifted "
                     "within the ball",
             "correct": True},
            {"text": "The total has changed, because the near face is now "
                     "opposite",
             "correct": False,
             "why": "The far face is equally the same sign, so the two still "
                    "add to zero."},
            {"text": "The total has changed, because charge crossed the gap",
             "correct": False,
             "why": "Nothing crosses the gap while they are apart."},
            {"text": "The total is unchanged, because nothing at all happened "
                     "in the ball",
             "correct": False,
             "why": "Something did happen — the shift is exactly why the ball "
                    "is attracted."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h06",
        "band": "harder",
        "text": "Two charged spheres are sealed in a jar and all the air is "
                "pumped out. What happens to the force between them?",
        "options": [
            {"text": "It disappears, because the air was carrying it",
             "correct": False,
             "why": "The air carries nothing; the force acts across empty "
                    "space."},
            {"text": "It falls, because there is less material to pass it "
                     "through",
             "correct": False,
             "why": "No material is needed at all, so removing it changes "
                    "almost nothing."},
            {"text": "It stays essentially the same as before", "correct": True},
            {"text": "It grows enormously, because nothing is in the way",
             "correct": False,
             "why": "The air was barely in the way to begin with, so removing "
                    "it makes little difference."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h07",
        "band": "harder",
        "text": "A student writes that the rod attracted the foil, so the "
                "foil must have the opposite charge. What is the flaw?",
        "options": [            {"text": "The foil would have to be the same sign to be "
                     "attracted",
             "correct": False,
             "why": "Same signs repel; the student has the rule right and the "
                    "reasoning wrong."},
            {"text": "Attraction cannot happen across a gap, so something "
                     "else moved the foil",
             "correct": False,
             "why": "It certainly happens across a gap; that is how the foil "
                    "is picked up."},
            {"text": "Foil is a conductor, so it cannot be attracted at all",
             "correct": False,
             "why": "Conductors are attracted strongly, because their "
                    "electrons move easily."},
            {"text": "A neutral foil is attracted too, so attraction does not "
                     "settle the sign",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h08",
        "band": "harder",
        "text": "Two spheres carry the same charge and repel with 12 units of "
                "force at 5 cm. What force acts at 15 cm?",
        "options": [            {"text": "About 1.3 units", "correct": True},
            {"text": "4 units", "correct": False,
             "why": "That divides by three, in step with the distance; the "
                    "force falls much faster than that."},
            {"text": "36 units", "correct": False,
             "why": "Moving three times further apart cannot strengthen the "
                    "force."},
            {"text": "12 units, unchanged", "correct": False,
             "why": "Tripling the separation weakens the force to a small "
                    "fraction of what it was."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h09",
        "band": "harder",
        "text": "You have two hanging balls and know one is charged. How do "
                "you find out whether the second is charged too?",
        "options": [            {"text": "Bring them together: attraction proves the second is "
                     "charged",
             "correct": False,
             "why": "Attraction is exactly the result that tells you nothing, "
                    "because a neutral ball is attracted too."},
            {"text": "Compare how far each hangs from vertical",
             "correct": False,
             "why": "Neither hangs off vertical until something acts on it, "
                    "so there is nothing to compare."},
            {"text": "Touch them together and see whether they stick",
             "correct": False,
             "why": "Touching changes both charges, so the test destroys what "
                    "it was measuring."},
            {"text": "Bring them together: repulsion proves it, while "
                     "attraction settles nothing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h10",
        "band": "harder",
        "text": "In electrostatic paint spraying the droplets are charged and "
                "the car body is earthed. Why does paint reach the far side "
                "of an edge?",
        "options": [            {"text": "Because the charged droplets are attracted to the whole "
                     "metal surface",
             "correct": True},
            {"text": "Because the droplets are heavy enough to carry round "
                     "corners",
             "correct": False,
             "why": "Their weight would carry them straight down, not round "
                    "an edge."},
            {"text": "Because the air currents blow them round",
             "correct": False,
             "why": "Air currents are unreliable; the wrap-round works "
                    "because of the attraction."},
            {"text": "Because like charges on the droplets push them round "
                     "the corner",
             "correct": False,
             "why": "Mutual repulsion spreads the spray out; what pulls it to "
                    "the far side is attraction to the body."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h11",
        "band": "harder",
        "text": "Why does a charged rod attract a neutral conductor more "
                "strongly than a neutral insulator of the same size?",
        "options": [            {"text": "Because a conductor has more charge in it to start with",
             "correct": False,
             "why": "Both are neutral and both are full of charge; what "
                    "differs is how freely it moves."},
            {"text": "Because a conductor is repelled rather than attracted",
             "correct": False,
             "why": "It is attracted, and more strongly, which is what the "
                    "question is about."},
            {"text": "Because conductors are always heavier", "correct": False,
             "why": "Mass has nothing to do with the electric force between "
                    "them."},
            {"text": "Because a conductor's electrons are free to move, so "
                     "the shift is larger",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h12",
        "band": "harder",
        "text": "A charged rod is brought near a hanging ball; the ball is "
                "attracted, touches the rod, and springs away. Explain the "
                "whole sequence.",
        "options": [
            {"text": "Neutral ball attracted by induction, takes the rod's "
                     "sign on contact, then repelled",
             "correct": True},
            {"text": "Ball charged the opposite way, attracted, then loses "
                     "its charge and falls back",
             "correct": False,
             "why": "Losing its charge would leave it hanging still, not "
                    "springing away."},
            {"text": "Ball attracted by gravity, then pushed off by the air",
             "correct": False,
             "why": "Gravity pulls straight down, and the air plays no part "
                    "in either movement."},
            {"text": "Ball repelled throughout, and the contact was an "
                     "accident",
             "correct": False,
             "why": "A repelled ball never reaches the rod at all."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h13",
        "band": "harder",
        "text": "Why do the two forces between a large charged sphere and a "
                "tiny one still come out equal?",
        "options": [            {"text": "Because forces between two objects always come in equal "
                     "and opposite pairs",
             "correct": True},
            {"text": "Because the charges are equal, whatever the sizes",
             "correct": False,
             "why": "The charges need not be equal at all; the FORCES are "
                    "equal regardless."},
            {"text": "Because the larger sphere shields the smaller one",
             "correct": False,
             "why": "Nothing is shielded, and shielding would not make the "
                    "pair equal."},
            {"text": "Because the smaller sphere moves more, which evens it "
                     "out",
             "correct": False,
             "why": "It moves more because it is lighter, and that is a "
                    "consequence rather than a cause."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h14",
        "band": "harder",
        "text": "A student says a charged object does nothing at all to an "
                "uncharged one. Which observation refutes it fastest?",
        "options": [            {"text": "Two rubbed rods pushing each other apart",
             "correct": False,
             "why": "Both of those are charged, so it does not test the claim "
                    "at all."},
            {"text": "A spark jumping from a finger to a door handle",
             "correct": False,
             "why": "That shows charge moving to earth rather than a force on "
                    "something neutral."},
            {"text": "A charged rod losing its charge in damp air",
             "correct": False,
             "why": "That is about charge leaking away, not about acting on a "
                    "neutral object."},
            {"text": "A rubbed balloon lifting untouched scraps of paper",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h15",
        "band": "harder",
        "text": "A neutral metal sphere on an insulating stand has a charged "
                "rod held near it, and is then earthed briefly with a finger "
                "before the rod is taken away. What is the sphere?",
        "options": [
            {"text": "Still neutral, because nothing touched it but a finger",
             "correct": False,
             "why": "The finger is exactly what let charge move; earthing is "
                    "a real transfer."},
            {"text": "Charged with the same sign as the rod", "correct": False,
             "why": "That would happen by direct contact with the rod, not by "
                    "earthing while it is near."},
            {"text": "Charged with the opposite sign to the rod",
             "correct": True},
            {"text": "Charged with whichever sign the finger carried",
             "correct": False,
             "why": "The finger is a path to earth, not a source of a "
                    "particular sign."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h16",
        "band": "harder",
        "text": "Why is repulsion, and not attraction, used as the test for "
                "charge in every textbook?",
        "options": [            {"text": "Because only two charged objects can repel, while "
                     "anything can be attracted",
             "correct": True},
            {"text": "Because repulsion is a stronger force than attraction",
             "correct": False,
             "why": "Neither is stronger; for equal charges at equal "
                    "distances they match exactly."},
            {"text": "Because repulsion is easier to see in a school lab",
             "correct": False,
             "why": "Both are easy to see; it is what each one PROVES that "
                    "differs."},
            {"text": "Because attraction happens only between conductors",
             "correct": False,
             "why": "It happens between insulators too — a balloon on a "
                    "plaster wall."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h17",
        "band": "harder",
        "text": "Two spheres 4 cm apart repel with 9 units of force. At what "
                "separation would the force be about 1 unit?",
        "options": [            {"text": "36 cm, nine times as far", "correct": False,
             "why": "That scales the distance with the force directly; the "
                    "fall is much steeper than that."},
            {"text": "1.3 cm, since the force must be brought down",
             "correct": False,
             "why": "Moving closer makes the force larger, not smaller."},
            {"text": "8 cm, twice as far", "correct": False,
             "why": "Doubling the gap leaves about a quarter of the force, "
                    "which is a little over 2 units."},
            {"text": "12 cm, three times as far", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier ────────────────────────────────────────
    {
        "id": "p9-02-e18",
        "band": "easier",
        "text": "Two objects, each of which can be positive, negative or "
                "neutral, are brought close together — nine combinations in "
                "all. In how many of them do the two objects attract?",
        "options": [
            {"text": "Two", "correct": False,
             "why": "Two is the number that repel: positive with positive, "
                    "and negative with negative."},
            {"text": "Six", "correct": True},
            {"text": "Four", "correct": False,
             "why": "Four of them are attraction by induction, but the two "
                    "unlike-charge cases attract as well."},
            {"text": "Eight", "correct": False,
             "why": "Eight would leave only one case out, and three of the "
                    "nine are not attraction."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e19",
        "band": "easier",
        "text": "A charged rod attracts a neutral scrap of foil. Compared "
                "with the pull between two oppositely charged objects the "
                "same distance apart, this pull is…",
        "options": [
            {"text": "much stronger, because a neutral object cannot push "
                     "back at all", "correct": False,
             "why": "Nothing about being neutral strengthens the pull. The "
                    "induced charges are small."},
            {"text": "exactly the same, because the separation is what "
                     "decides the force", "correct": False,
             "why": "Separation is one factor, but the charges involved "
                    "matter too, and the induced ones are tiny."},
            {"text": "the same size but pointing the opposite "
                     "way", "correct": False,
             "why": "Both cases are attraction, so the directions agree. It "
                    "is the sizes that differ."},
            {"text": "much weaker", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e20",
        "band": "easier",
        "text": "There is one thing a charged object can never do to an "
                "uncharged one. What is it?",
        "options": [
            {"text": "Pull it towards itself", "correct": False,
             "why": "That is exactly what it does do — it is the reason a "
                    "rubbed rod picks things up."},
            {"text": "Push it away", "correct": True},
            {"text": "Move the charges about inside it", "correct": False,
             "why": "Moving the other object's own charges to one side is how "
                    "the attraction comes about."},
            {"text": "Act on it across a gap", "correct": False,
             "why": "No contact is needed. The effect happens at a distance, "
                    "as it does between two charges."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e21",
        "band": "easier",
        "text": "Two socks come out of a tumble dryer clinging tightly to "
                "each other. What must be true of their charges?",
        "options": [
            {"text": "They carry the same charge as each "
                     "other", "correct": False,
             "why": "Two like charges would push apart, so the socks would "
                    "fall away rather than cling."},
            {"text": "Neither of them carries any charge", "correct": False,
             "why": "Two uncharged objects do nothing to each other at all, "
                    "so nothing would hold them together."},
            {"text": "One has lost the protons the other "
                     "gained", "correct": False,
             "why": "Protons never move between objects. Only electrons "
                    "change sides."},
            {"text": "They carry opposite charges", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e22",
        "band": "easier",
        "text": "Dust settles onto a charged plastic screen far faster than "
                "onto the wooden frame around it. Does that show the dust is "
                "charged?",
        "options": [
            {"text": "No — an uncharged speck of dust is pulled in just as "
                     "well", "correct": True},
            {"text": "Yes, because only a charged speck could be pulled "
                     "in", "correct": False,
             "why": "An uncharged speck is pulled in as well, which is why "
                    "attraction proves nothing."},
            {"text": "Yes, because the dust has taken charge from the "
                     "air", "correct": False,
             "why": "The dust needs no charge of its own for the screen to "
                    "attract it."},
            {"text": "No, because the dust is blown onto the screen by the "
                     "air", "correct": False,
             "why": "Moving air would land dust on the frame too. The screen "
                    "is picked out because it is charged."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e23",
        "band": "easier",
        "text": "A positively charged rod is held near a neutral ball. What "
                "do the ball's own electrons do?",
        "options": [
            {"text": "They are driven to the side furthest from the "
                     "rod", "correct": False,
             "why": "A positive rod pulls electrons towards it. Driving them "
                    "away is what a negative rod does."},
            {"text": "They are pulled towards the side nearest the "
                     "rod", "correct": True},
            {"text": "They leave the ball and cross over onto the "
                     "rod", "correct": False,
             "why": "Nothing crosses the gap. The ball's total charge is the "
                    "same throughout."},
            {"text": "They stay exactly where they were, as the ball is "
                     "neutral", "correct": False,
             "why": "Neutral means balanced, not fixed. The charges inside "
                    "can still be moved about."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e24",
        "band": "easier",
        "text": "Two positively charged spheres are held near each other. In "
                "which directions do the two forces point?",
        "options": [
            {"text": "Both of them in the same direction along the "
                     "line", "correct": False,
             "why": "The two forces are opposite in direction, so the spheres "
                    "move apart rather than together."},
            {"text": "One sphere is pushed and the other one is "
                     "pulled", "correct": False,
             "why": "Like charges push both ways. Neither sphere is pulled "
                    "towards the other."},
            {"text": "Each sphere is pushed directly away from the "
                     "other", "correct": True},
            {"text": "Each sphere is pulled directly towards the "
                     "other", "correct": False,
             "why": "Pulling together is what unlike charges do. Two "
                    "positives push apart."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e25",
        "band": "easier",
        "text": "Two charged objects are moved further apart. Which of these "
                "does not change?",
        "options": [
            {"text": "The size of the force on each of them", "correct": False,
             "why": "The force falls quickly as the gap grows; that is the "
                    "thing this change is about."},
            {"text": "The charge on each of them", "correct": True},
            {"text": "The distance between their centres", "correct": False,
             "why": "That is precisely what has been changed by moving them "
                    "apart."},
            {"text": "Whether the force is big enough to move "
                     "them", "correct": False,
             "why": "A force that moved them at a small gap may well be too "
                    "weak at a larger one."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e26",
        "band": "easier",
        "text": "What does it mean to say that two objects repel?",
        "options": [
            {"text": "They pull each other together", "correct": False,
             "why": "That is attraction, which is what unlike charges do."},
            {"text": "They swap charge until both are "
                     "neutral", "correct": False,
             "why": "No charge crosses between them; they simply push without "
                    "touching."},
            {"text": "They stay exactly where they are", "correct": False,
             "why": "A force acts on each of them, and if they are free to "
                    "move they do."},
            {"text": "They push each other apart", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e27",
        "band": "easier",
        "text": "A charged rod attracts a neutral scrap of foil. Whose "
                "electrons have moved?",
        "options": [
            {"text": "The rod's, which have crossed onto the "
                     "foil", "correct": False,
             "why": "Nothing crosses the gap. Both objects keep the charge "
                    "they had."},
            {"text": "The foil's, which have crossed onto the "
                     "rod", "correct": False,
             "why": "The foil's total charge does not change, so none of its "
                    "electrons leave it."},
            {"text": "The foil's, which have moved within the "
                     "foil", "correct": True},
            {"text": "Neither object's, since neither has any to "
                     "spare", "correct": False,
             "why": "The foil's own electrons do shift to one side, and that "
                    "is what produces the pull."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e28",
        "band": "easier",
        "text": "Two oppositely charged spheres are held a short way apart. "
                "Two like-charged spheres of the same size are held the "
                "same distance apart. How do the two forces compare in "
                "size?",
        "options": [
            {"text": "The attraction is the bigger of the "
                     "two", "correct": False,
             "why": "Attraction and repulsion between the same charges at the "
                    "same gap come out the same size."},
            {"text": "The two forces are the same size", "correct": True},
            {"text": "The repulsion is the bigger of the "
                     "two", "correct": False,
             "why": "Only the direction changes when the signs change; the "
                    "size does not."},
            {"text": "It depends which of the spheres you look "
                     "at", "correct": False,
             "why": "Both spheres in a pair always feel the same size of "
                    "force as each other."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e29",
        "band": "easier",
        "text": "Which of these would a negatively charged rod push away?",
        "options": [
            {"text": "A positively charged ball", "correct": False,
             "why": "Unlike charges pull together, so a positive ball is "
                    "attracted."},
            {"text": "A neutral scrap of paper", "correct": False,
             "why": "A neutral object is always attracted, never pushed "
                    "away."},
            {"text": "Another negatively charged ball", "correct": True},
            {"text": "Any light object put in front of it", "correct": False,
             "why": "Light objects that carry no charge are pulled in, not "
                    "pushed away."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-e30",
        "band": "easier",
        "text": "A charged balloon stuck to a wall falls off half an hour "
                "later. What has happened?",
        "options": [
            {"text": "The wall has taken on the same charge as the "
                     "balloon", "correct": False,
             "why": "The wall stays neutral throughout. It is the balloon "
                    "that changes."},
            {"text": "Moving air has slowly pushed the balloon off the "
                     "wall", "correct": False,
             "why": "A still room would give the same result. The pull itself "
                    "has faded."},
            {"text": "The balloon's charge has turned into the opposite "
                     "one", "correct": False,
             "why": "A charge does not flip sign on its own; the balloon "
                    "would have been pushed off if it had."},
            {"text": "Its charge has leaked away, so the attraction has "
                     "gone", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ──────────────────────────────────────
    {
        "id": "p9-02-s18",
        "band": "standard",
        "text": "A charged rod lifts small scraps of tissue paper easily but "
                "will not lift a steel paper clip of about the same size. Why "
                "not?",
        "options": [
            {"text": "The clip weighs far more, and the pull is too small to "
                     "lift it", "correct": True},
            {"text": "A metal object cannot be attracted by a charged "
                     "rod", "correct": False,
             "why": "Metals are attracted particularly well, because their "
                    "electrons move so freely."},
            {"text": "The clip carries the same sign of charge as the rod "
                     "does", "correct": False,
             "why": "The clip came out of a box uncharged, and an uncharged "
                    "object is attracted, not repelled."},
            {"text": "The clip conducts, so the rod's charge flows into it "
                     "and stops", "correct": False,
             "why": "No charge crosses the gap, and the clip conducting is "
                    "what makes the pull stronger, not weaker."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s19",
        "band": "standard",
        "text": "In a power-station chimney the ash particles are given a "
                "charge and the collecting plates are given the opposite "
                "charge. Explain how that takes the ash out of the smoke.",
        "options": [
            {"text": "Like charges repel, so the charged ash is pushed on up "
                     "the chimney and straight out into the "
                     "air", "correct": False,
             "why": "Pushing the ash up the chimney would send it into the "
                    "air, which is what the plates are there to stop."},
            {"text": "Unlike charges attract, so the ash is pulled onto the "
                     "plates on the way past", "correct": True},
            {"text": "The charge makes each ash particle heavier, so it falls "
                     "out of the smoke", "correct": False,
             "why": "Charging something does not weigh it down. The plates "
                    "have to pull the ash sideways."},
            {"text": "The charged plates burn the ash away as the smoke "
                     "passes them", "correct": False,
             "why": "Nothing is burned. The ash is collected on the plates "
                    "and cleared off later."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s20",
        "band": "standard",
        "text": "Cling film peeled off a roll sticks firmly to a clean glass "
                "bowl that nobody has charged. Explain what holds it there.",
        "options": [
            {"text": "Peeling leaves the film charged, and a charged object "
                     "attracts an uncharged one", "correct": True},
            {"text": "Peeling leaves the film and the bowl oppositely charged "
                     "as they meet", "correct": False,
             "why": "The bowl takes no charge from being touched by the film; "
                    "it is neutral the whole time."},
            {"text": "The film is sticky, so the force has nothing to do with "
                     "charge", "correct": False,
             "why": "Fresh film will cling before it touches anything, across "
                    "a small gap, which glue cannot do."},
            {"text": "The bowl must have been charged already by being washed "
                     "and dried", "correct": False,
             "why": "The film sticks to a bowl straight out of the cupboard. "
                    "Only the film needs to be charged."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s21",
        "band": "standard",
        "text": "Two identical neutral metal spheres, each on an insulating "
                "stand, are touched in turn by the same charged rod. What do "
                "the two spheres then do to each other?",
        "options": [
            {"text": "Attract, because one of them will have taken more "
                     "charge than the other", "correct": False,
             "why": "Two objects with the same sign of charge repel however "
                    "unequal the amounts are."},
            {"text": "Nothing, because both of them are still neutral "
                     "overall", "correct": False,
             "why": "Touching a charged rod leaves charge behind on each "
                    "sphere, so neither is neutral now."},
            {"text": "Repel, because both now carry the rod's sign of "
                     "charge", "correct": True},
            {"text": "Attract, because touching a rod leaves an object "
                     "oppositely charged", "correct": False,
             "why": "Contact leaves the same sign behind, not the opposite "
                    "one."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s22",
        "band": "standard",
        "text": "A charged rod is held near a light foil ball hanging on a "
                "thread. The ball swings across to the rod, while the rod "
                "does not visibly move. Why not?",
        "options": [
            {"text": "The force acts only on the ball, because the ball is "
                     "much the lighter of the two objects", "correct": False,
             "why": "A force acts on both. Which one moves depends on their "
                    "masses and what is holding them."},
            {"text": "The rod feels a much smaller force, being the one that "
                     "is charged", "correct": False,
             "why": "The two forces are always equal in size, whichever "
                    "object carries the charge."},
            {"text": "The rod feels no force at all, being the one doing the "
                     "attracting", "correct": False,
             "why": "There is no such thing as one object attracting without "
                    "being attracted back."},
            {"text": "The rod feels an equal force, but it is heavier and "
                     "held in the hand", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s23",
        "band": "standard",
        "text": "A positively charged rod is held near one end of a long "
                "neutral metal bar resting on insulating supports. Describe "
                "the charge on the two ends of the bar.",
        "options": [
            {"text": "Near end positive, far end negative, with no charge "
                     "overall", "correct": False,
             "why": "A positive rod pulls the bar's electrons towards it, so "
                    "the near end comes out negative."},
            {"text": "Both ends positive, because charge has come across from "
                     "the rod", "correct": False,
             "why": "No charge crosses the gap. Only the bar's own electrons "
                    "move, and they stay in the bar."},
            {"text": "Both ends neutral, because the bar is a "
                     "conductor", "correct": False,
             "why": "Being a conductor is what lets its electrons gather at "
                    "one end so easily."},
            {"text": "Near end negative, far end positive, with no charge "
                     "overall", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s24",
        "band": "standard",
        "text": "Two objects attract, but far more weakly than two charged "
                "objects the same distance apart would. What must they be?",
        "options": [
            {"text": "Both charged, with opposite signs", "correct": False,
             "why": "Two opposite charges give the full-strength pull, not a "
                    "weak one."},
            {"text": "One charged and one uncharged", "correct": True},
            {"text": "Both charged, with the same sign", "correct": False,
             "why": "Two like charges push apart, so there would be no "
                    "attraction to measure."},
            {"text": "Both of them uncharged", "correct": False,
             "why": "Two uncharged objects give no force at all — the one "
                    "case in the table that does nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s25",
        "band": "standard",
        "text": "A student says an uncharged object has no charges in it at "
                "all, so a charged rod can do nothing to it. Where is the "
                "flaw?",
        "options": [
            {"text": "It has no charges, but the air in the gap carries the "
                     "force across", "correct": False,
             "why": "The air does no carrying, and the object certainly has "
                    "charges of both kinds inside it."},
            {"text": "It holds equal amounts of both charges, and those can "
                     "be moved about", "correct": True},
            {"text": "It really does feel nothing, so the rod has to be "
                     "touching it", "correct": False,
             "why": "A rubbed rod lifts paper without ever touching it, so "
                    "something does act across the gap."},
            {"text": "It takes a little charge from the rod, which is why it "
                     "moves", "correct": False,
             "why": "Nothing crosses the gap, and its total charge is the "
                    "same before and after."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s26",
        "band": "standard",
        "text": "Two charged spheres on insulating stands are repelling each "
                "other. One of them is touched briefly with a finger. What "
                "happens next?",
        "options": [
            {"text": "The repulsion stops, and nothing acts between them at "
                     "all", "correct": False,
             "why": "A charged sphere and an uncharged one still attract "
                    "weakly, by induction."},
            {"text": "The repulsion carries on exactly as it was "
                     "before", "correct": False,
             "why": "The touched sphere loses its charge through you to "
                    "earth, so the like-charge push has gone."},
            {"text": "The repulsion becomes an attraction of exactly the same "
                     "strength as the push had been", "correct": False,
             "why": "Induced attraction is very much weaker than the push "
                    "between two charged spheres."},
            {"text": "The repulsion stops, and the two attract each other "
                     "weakly instead", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s27",
        "band": "standard",
        "text": "A charged rod attracts object X and repels object Y. Which "
                "object's charge do you now know?",
        "options": [
            {"text": "X's, and it is the opposite sign to the "
                     "rod's", "correct": False,
             "why": "X might be oppositely charged, or it might carry no "
                    "charge at all; attraction cannot separate the two."},
            {"text": "Both of their charges", "correct": False,
             "why": "Only one of the two results settles anything, and it is "
                    "not the attraction."},
            {"text": "Neither of their charges", "correct": False,
             "why": "The repulsion is conclusive: nothing but a like charge "
                    "can push."},
            {"text": "Y's, and it is the same sign as the "
                     "rod's", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s28",
        "band": "standard",
        "text": "Why can a charged rod attract almost any light object, while "
                "it can only repel a charged one?",
        "options": [
            {"text": "Attraction between charges is simply a stronger force "
                     "than repulsion is, whatever the distance between "
                     "them", "correct": False,
             "why": "At the same gap with the same charges the two come out "
                    "the same size."},
            {"text": "Everything holds charges that can be pushed to one "
                     "side, but only a like charge pushes "
                     "back", "correct": True},
            {"text": "Light objects are all slightly charged to begin "
                     "with", "correct": False,
             "why": "Paper out of a drawer carries no charge, and it is still "
                    "picked up."},
            {"text": "The rod passes a small charge to whatever it comes "
                     "near", "correct": False,
             "why": "Nothing crosses the gap; the other object's total charge "
                    "is unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s29",
        "band": "standard",
        "text": "How could you show that the two forces between a pair of "
                "charged balls are equal in size?",
        "options": [
            {"text": "Hang the heavier ball on a stronger thread and then "
                     "check that it swings out by a smaller "
                     "angle", "correct": False,
             "why": "Different threads and different masses would tell you "
                    "nothing about the two forces."},
            {"text": "Hang both on identical threads and check that they "
                     "swing out by the same angle", "correct": True},
            {"text": "Move one of them further away and watch the other one "
                     "stop moving", "correct": False,
             "why": "Both forces fall together when the gap grows, so this "
                    "compares nothing."},
            {"text": "Put twice the charge on one of them and compare how far "
                     "each swings", "correct": False,
             "why": "Changing one charge changes both forces by the same "
                    "amount, so the comparison is lost."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-s30",
        "band": "standard",
        "text": "A hanging ball is attracted to a positively charged rod, and "
                "then attracted to a negatively charged one as well. What "
                "does that prove?",
        "options": [
            {"text": "That the ball carries a positive "
                     "charge", "correct": False,
             "why": "A positive ball would have been pushed away by the "
                    "positive rod."},
            {"text": "That the ball carries no charge", "correct": True},
            {"text": "That nothing can be told from those two "
                     "results", "correct": False,
             "why": "Taken together they are conclusive: a charged ball would "
                    "have been repelled by one of the two rods."},
            {"text": "That the ball carries a negative "
                     "charge", "correct": False,
             "why": "A negative ball would have been pushed away by the "
                    "negative rod."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ────────────────────────────────────────
    {
        "id": "p9-02-h18",
        "band": "harder",
        "text": "Ball A repels ball B, and ball B attracts ball C. What can "
                "be said about A and C?",
        "options": [
            {"text": "They will push each other apart, since both of them act "
                     "on B", "correct": False,
             "why": "A and B share a sign, and C is either opposite to B or "
                    "uncharged — so C cannot share A's sign."},
            {"text": "Nothing at all, until C has been tested against a known "
                     "charge", "correct": False,
             "why": "The two results are enough. Both of the possibilities "
                    "left for C give attraction with A."},
            {"text": "They will do nothing to each other, as C's charge is "
                     "unknown", "correct": False,
             "why": "C is either oppositely charged or uncharged, and A "
                    "attracts either of those."},
            {"text": "They will pull towards each other, whether or not C is "
                     "charged", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h19",
        "band": "harder",
        "text": "However carefully you keep your hand uncharged, a charged "
                "rod is still drawn towards it. Explain why.",
        "options": [
            {"text": "A hand is always left slightly charged by the clothes "
                     "you are wearing, and that charge pulls the rod "
                     "across", "correct": False,
             "why": "Even a hand with no charge on it at all is attracted, so "
                    "this cannot be the reason."},
            {"text": "Your hand conducts, so the rod pushes its charges to "
                     "one side and pulls on the near ones", "correct": True},
            {"text": "Your hand is warm, and warm air rises and carries the "
                     "rod with it", "correct": False,
             "why": "Warmth and air currents have nothing to do with it; the "
                    "effect works through a cold hand too."},
            {"text": "The rod takes charge from your hand as soon as it comes "
                     "close", "correct": False,
             "why": "No charge crosses the gap. The hand's own charges simply "
                    "shift within it."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h20",
        "band": "harder",
        "text": "Three objects are each attracted to a negatively charged "
                "rod, and a student concludes that all three carry positive "
                "charge. Describe the test that would settle it.",
        "options": [
            {"text": "Bring a positively charged rod near each: only a "
                     "charged one is pushed away", "correct": True},
            {"text": "Bring the same negative rod nearer: a charged object is "
                     "attracted more strongly", "correct": False,
             "why": "Every one of them is attracted more strongly at a "
                    "smaller gap, charged or not."},
            {"text": "Weigh each object carefully: a charged object comes out "
                     "slightly heavier", "correct": False,
             "why": "There is no weighing that separates them; charge is not "
                    "what a balance measures."},
            {"text": "Touch each object to the rod: a charged one sticks to "
                     "it and stays there", "correct": False,
             "why": "Touching leaves an object with the rod's own sign, so it "
                    "is thrown off whatever it started as."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h21",
        "band": "harder",
        "text": "Light bags on a plastic conveyor belt jump about and cling "
                "to its sides. The engineer replaces one roller with an "
                "earthed metal one. Explain why that helps.",
        "options": [
            {"text": "The metal roller charges the belt the other way and "
                     "cancels it out", "correct": False,
             "why": "An earthed roller does not charge anything. It gives "
                    "charge a route away."},
            {"text": "Charge separated by the belt can now run to earth "
                     "instead of building up on it", "correct": True},
            {"text": "The metal roller stops the belt rubbing against "
                     "anything at all", "correct": False,
             "why": "The belt keeps rubbing against the bags and the rollers. "
                    "What changes is where the charge goes."},
            {"text": "Earthing takes some of the weight off the bags, so they "
                     "are no longer light enough to jump "
                     "about", "correct": False,
             "why": "Earthing changes nothing about weight. The bags jump "
                    "because the belt is charged."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h22",
        "band": "harder",
        "text": "The electric force between two protons is enormously bigger "
                "than the gravitational pull between them. Why do you never "
                "notice electric forces between everyday objects?",
        "options": [
            {"text": "Everyday objects are too heavy for an electric force to "
                     "shift", "correct": False,
             "why": "A rubbed rod lifts paper against the whole Earth's pull, "
                    "so the force is far from feeble."},
            {"text": "Everyday matter has its positive and negative charges "
                     "almost exactly balanced", "correct": True},
            {"text": "The electric force reaches only across distances "
                     "smaller than an atom, so it cannot get from one object "
                     "to another", "correct": False,
             "why": "It reaches across a room. It is simply very much weaker "
                    "by the time it gets there."},
            {"text": "The air between everyday objects cancels the electric "
                     "force out", "correct": False,
             "why": "Air does no cancelling; the force is just as strong with "
                    "the air pumped away."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h23",
        "band": "harder",
        "text": "In electrostatic paint spraying every droplet leaves the gun "
                "carrying the same charge. Besides being pulled onto the car, "
                "what does that do to the spray itself?",
        "options": [
            {"text": "The droplets pull together, so they join into larger "
                     "drops on the way", "correct": False,
             "why": "Like charges push apart. Joining into big drops is what "
                    "a sprayer is trying to avoid."},
            {"text": "The droplets push each other apart, so the spray "
                     "spreads into a fine even mist", "correct": True},
            {"text": "The droplets travel faster, since like charges drive "
                     "them forwards", "correct": False,
             "why": "The push between droplets acts in all directions and "
                    "does not drive the spray along."},
            {"text": "The droplets lose their charge to each other and drop "
                     "out of the air", "correct": False,
             "why": "Charge does not leak between droplets in flight; they "
                    "keep it until they land."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h24",
        "band": "harder",
        "text": "Put these in order of the force on the right-hand object, "
                "largest first: two charged spheres 4 cm apart; the same two "
                "8 cm apart; one charged sphere and one uncharged one 8 cm "
                "apart.",
        "options": [
            {"text": "The uncharged pair, then the pair at 4 cm, then the "
                     "pair at 8 cm", "correct": False,
             "why": "Induced attraction is the weakest of the three, not the "
                    "strongest."},
            {"text": "The pair at 8 cm, then the pair at 4 cm, then the "
                     "uncharged pair", "correct": False,
             "why": "The force falls as the gap grows, so the closer pair "
                    "comes first."},
            {"text": "The pair at 4 cm, then the pair at 8 cm, then the "
                     "uncharged pair", "correct": True},
            {"text": "All three of them the same, as the charges are the same "
                     "size", "correct": False,
             "why": "Separation matters, and so does whether the second "
                    "object carries a charge at all."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h25",
        "band": "harder",
        "text": "A student says induction cannot be real, because an "
                "uncharged object's total charge never changes, so nothing "
                "has happened to it. Refute that.",
        "options": [
            {"text": "Its total charge does change — it takes a little from "
                     "the rod", "correct": False,
             "why": "Nothing crosses the gap. The student is right about the "
                    "total and wrong about what follows."},
            {"text": "Its charges have been moved onto opposite faces, and "
                     "that is what produces the pull", "correct": True},
            {"text": "Nothing does happen to the object; it is the rod that "
                     "moves across towards it instead, because the rod is the "
                     "charged one", "correct": False,
             "why": "Both feel a force, and the light object is the one you "
                    "see move."},
            {"text": "The object was never really uncharged in the first "
                     "place", "correct": False,
             "why": "Paper straight from a drawer is uncharged and is still "
                    "picked up."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h26",
        "band": "harder",
        "text": "The rule that like repels and unlike attracts holds for "
                "magnetic poles as well as for charges. What is a real "
                "difference between the two cases?",
        "options": [
            {"text": "Magnetic forces need contact, while electric forces act "
                     "across a gap", "correct": False,
             "why": "A magnet picks up a pin before touching it. Neither "
                    "force needs contact."},
            {"text": "A magnet attracts only magnetic materials, while a "
                     "charged object attracts almost anything "
                     "light", "correct": True},
            {"text": "Magnetic forces stay exactly the same at any distance "
                     "at all, while electric ones fall away quickly with the "
                     "gap", "correct": False,
             "why": "A magnet's pull weakens sharply with distance too, as "
                    "anyone moving one away from a pin can feel."},
            {"text": "Magnetic poles can be found on their own, while charges "
                     "cannot be", "correct": False,
             "why": "It is the other way round: a single charge is easy to "
                    "make, and a single pole has never been found."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h27",
        "band": "harder",
        "text": "Two charged spheres are held a fixed distance apart. If the "
                "sign of both charges were reversed at the same moment, what "
                "would happen to the force between them?",
        "options": [
            {"text": "It would reverse, so an attraction would become a "
                     "repulsion", "correct": False,
             "why": "Reversing both keeps them like or unlike as they were, "
                    "so the direction is unchanged."},
            {"text": "Nothing at all — it would be the same size and in the "
                     "same direction", "correct": True},
            {"text": "It would double, because both of the charges have "
                     "changed", "correct": False,
             "why": "Neither charge has changed in size, so neither has the "
                    "force."},
            {"text": "It would drop to zero while the two charges swapped "
                     "over", "correct": False,
             "why": "There is no moment with no charge; the pair are reversed "
                    "together."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h28",
        "band": "harder",
        "text": "Two students hold charged rods about 30 cm apart and feel "
                "nothing at all. Does that mean there is no force between the "
                "rods?",
        "options": [
            {"text": "Yes — the force only exists once the objects are close "
                     "enough to touch", "correct": False,
             "why": "The force acts across any gap. Touching has nothing to "
                    "do with whether it is there."},
            {"text": "Yes — over that distance the air between them cancels "
                     "the force out", "correct": False,
             "why": "Air cancels nothing. The force is the same with the air "
                    "pumped away."},
            {"text": "No — the force is there, but it acts on the students "
                     "rather than the rods", "correct": False,
             "why": "The force acts on the charged rods themselves, and their "
                    "hands simply hold them still."},
            {"text": "No — there is a force, but at that gap it is far too "
                     "weak to feel", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h29",
        "band": "harder",
        "text": "Two uncharged objects each hold huge numbers of positive and "
                "negative charges. Why do they not attract each other by "
                "induction?",
        "options": [
            {"text": "Their charges are held in place and none of them can "
                     "move", "correct": False,
             "why": "The charges in each object can move perfectly well; the "
                    "trouble is that nothing is moving them."},
            {"text": "Neither of them has a spare charge to push the other's "
                     "charges to one side", "correct": True},
            {"text": "They push each other apart instead, because their "
                     "charges match", "correct": False,
             "why": "Two uncharged objects neither push nor pull — this is "
                    "the one case that gives no force."},
            {"text": "The air between them blocks any effect that the two of "
                     "them could otherwise have on each "
                     "other", "correct": False,
             "why": "Air blocks nothing, which is why a charged object "
                    "reaches an uncharged one across the same gap."},
        ],
        "figure": None,
    },
    {
        "id": "p9-02-h30",
        "band": "harder",
        "text": "A student argues that in induction the near face is pulled "
                "and the far face is pushed by the same amount, so the two "
                "should cancel and nothing should happen. Where is the flaw?",
        "options": [
            {"text": "The far face is left carrying no charge at all, so "
                     "there is nothing there for the rod to push "
                     "on", "correct": False,
             "why": "The far face does end up charged, with the same sign as "
                    "the rod, and it genuinely is pushed."},
            {"text": "The two faces are at different distances, and the force "
                     "falls off very quickly", "correct": True},
            {"text": "A push between charges is always smaller than a pull "
                     "between them", "correct": False,
             "why": "Push and pull come out the same size for the same "
                    "charges at the same gap."},
            {"text": "The charge on the far face leaks away before it can act "
                     "on anything", "correct": False,
             "why": "It stays there as long as the rod is held nearby, and it "
                    "does push — just from further off."},
        ],
        "figure": None,
    },
]
