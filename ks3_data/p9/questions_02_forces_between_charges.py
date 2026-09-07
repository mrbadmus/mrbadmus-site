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
]
