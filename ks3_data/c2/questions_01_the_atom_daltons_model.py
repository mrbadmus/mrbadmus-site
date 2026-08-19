"""C2 lesson 01 — The atom: Dalton's model: twelve questions (MRB-269).

The lesson's argument is that a model earns its place by what falls over
without it: three claims, four observations that were already known, and a
switch that shows which claim was holding up which. These twelve probe that
argument from the sides the ladder does not — what Dalton added to the particle
model a student already had, which single claim a given observation rests on,
how far a light microscope actually gets, and where the boundary around the
model sits now that two of the claims are known to be wrong.

The distractors are built from the lesson's two declared misconceptions.
ATOM-01 (a copper atom is a tiny bit of copper — orange, shiny, conducting)
drives s03 and h04, where a single atom is given a small share of a bulk
property, or the colour is quietly said to be there but too small to see.
ATOM-02 (a model that is wrong about something has been disproved) drives h02,
where the choices are drop the claim, deny the evidence, or call it a
simplification for beginners — three ways of refusing a boundary. Two further
families run through the bank: transmutation, the belief that a strong enough
reaction or a good enough furnace could change one element into another (e01,
e04, h03); and "any proportion will do", the belief that elements combine in
whatever amounts are available, which is precisely what the whole-number ratio
claim rules out (e01, s02, h01).
"""

UNIT = "C2"
LESSON = "the-atom-daltons-model"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c2-01-e01",
        "band": "easier",
        "text": "What did Dalton claim happens when the atoms of two "
                "elements combine?",
        "options": [
            {"text": "They join in whatever proportions happen to be "
                     "available", "correct": False,
             "why": "That is what the world would look like if Dalton were "
                    "wrong. Copper and oxygen make one compound in one ratio "
                    "and a second in another, and never anything in between."},
            {"text": "They join in simple whole-number ratios",
             "correct": True},
            {"text": "They join, and each atom changes into a new kind",
             "correct": False,
             "why": "Combining is not transmutation. No chemical reaction "
                    "turns one kind of atom into another — that is the claim "
                    "that explains why alchemy never worked."},
            {"text": "They break into smaller pieces and share them out",
             "correct": False,
             "why": "Dalton claimed atoms cannot be broken into anything "
                    "smaller. Joining is whole atoms sticking together, not "
                    "atoms being taken apart."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e02",
        "band": "easier",
        "text": "You already had a particle model before this lesson. What "
                "did Dalton add to it?",
        "options": [
            {"text": "That particles come in kinds, one per element",
             "correct": True},
            {"text": "That particles are far too small to see",
             "correct": False,
             "why": "The particle model already said that — it is where it "
                    "started. What it never said was that the particles come "
                    "in kinds."},
            {"text": "That particles are always moving, even in a solid",
             "correct": False,
             "why": "You already had that one, and used it to explain "
                    "diffusion and gas pressure. Dalton's addition was kinds, "
                    "and without kinds nothing in chemistry works."},
            {"text": "That there are gaps between the particles in a gas",
             "correct": False,
             "why": "That was the particle model's explanation for squashing "
                    "a gas, before Dalton wrote anything. It says nothing "
                    "about one element differing from another."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e03",
        "band": "easier",
        "text": "About how many copper atoms would fit across the 1 cm piece "
                "of copper wire?",
        "options": [
            {"text": "About forty", "correct": False,
             "why": "Forty grains is something you could count under a school "
                    "microscope. Atoms are far below anything a light "
                    "microscope reaches — the real number is forty million."},
            {"text": "About a hundred", "correct": False,
             "why": "A hundred is roughly the number of KINDS of atom there "
                    "are, not how many fit across a wire. Those two numbers "
                    "get swapped more than any other pair here."},
            {"text": "About forty million", "correct": True},
            {"text": "About forty thousand", "correct": False,
             "why": "Too few by a factor of a thousand. The last zoom step is "
                    "0.000001 mm across and holds only about four copper "
                    "atoms, so a whole centimetre holds forty million."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e04",
        "band": "easier",
        "text": "Which of these is something a chemical reaction can do to "
                "atoms?",
        "options": [
            {"text": "Change an atom of one element into another element",
             "correct": False,
             "why": "No chemical reaction does. That is exactly what "
                    "alchemists tried for fifteen hundred years with "
                    "furnaces, acids and time, and never once managed."},
            {"text": "Destroy some of them, so the mass drops",
             "correct": False,
             "why": "Seal a reaction in a flask and the mass afterwards is "
                    "exactly the mass before. Nothing was destroyed — the "
                    "same atoms are there in a new arrangement."},
            {"text": "Split them into smaller pieces that join up again",
             "correct": False,
             "why": "Atoms can be split, but never by chemistry. That "
                    "boundary is the one part of Dalton's claim that still "
                    "holds exactly, and it is the range you work in."},
            {"text": "Rearrange them into new combinations", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c2-01-s01",
        "band": "standard",
        "text": "A reaction is sealed in a flask and its mass is exactly the "
                "same afterwards as before. Which of Dalton's claims is "
                "holding that observation up?",
        "options": [
            {"text": "All atoms of one element are the same as each other",
             "correct": False,
             "why": "Identical atoms explain why a compound always has the "
                    "same composition. They do nothing to stop the mass "
                    "drifting up or down during the reaction."},
            {"text": "Atoms join in simple whole-number ratios",
             "correct": False,
             "why": "Whole-number ratios fix what combines with what. The "
                    "balance holding still is about atoms not being made or "
                    "destroyed, which is a different claim."},
            {"text": "Atoms cannot be created or destroyed", "correct": True},
            {"text": "Atoms are far too small to see", "correct": False,
             "why": "True, but it is not one of Dalton's three claims — it "
                    "came from the particle model. Being small would not stop "
                    "mass being lost."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s02",
        "band": "standard",
        "text": "Water from a river, from the sea and from a laboratory "
                "always has the same proportion of hydrogen to oxygen by "
                "mass. If Dalton were wrong that all atoms of one element are "
                "alike, what would you expect instead?",
        "options": [
            {"text": "The proportion would differ from sample to sample",
             "correct": True},
            {"text": "Water would stop forming at all", "correct": False,
             "why": "Nothing in that claim decides whether hydrogen and "
                    "oxygen combine. What it fixes is the proportion they "
                    "combine in, not whether they do it."},
            {"text": "Sea water would hold more oxygen because it is salty",
             "correct": False,
             "why": "The salt is a different substance dissolved in the "
                    "water. The water itself is the same everywhere, which is "
                    "the observation rather than an exception to it."},
            {"text": "The hydrogen would slowly turn into oxygen",
             "correct": False,
             "why": "No chemical process turns one element into another, and "
                    "that is a separate claim anyway. Losing identical atoms "
                    "changes proportions, not kinds."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s03",
        "band": "standard",
        "text": "A single copper atom has almost none of copper's familiar "
                "properties. What does it still have?",
        "options": [
            {"text": "A faint trace of orange, and a little conductivity",
             "correct": False,
             "why": "Not a smaller amount — none at all. Colour is what "
                    "happens when light meets a huge number of atoms, and "
                    "conducting needs somewhere for the charge to go."},
            {"text": "Its bendability, since bending needs no other atoms",
             "correct": False,
             "why": "Bending is the opposite — it needs layers of atoms "
                    "sliding over each other. One atom has no layers, so "
                    "there is nothing there to bend."},
            {"text": "Nothing at all, since properties only exist in a crowd",
             "correct": False,
             "why": "Nearly right, and one step too far. Its kind and its "
                    "mass belong to the single atom; it is everything else "
                    "that belongs to the crowd."},
            {"text": "A kind — copper rather than lead — and a mass",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s04",
        "band": "standard",
        "text": "Dalton wrote his model down in 1803, but nobody saw an atom "
                "until the 1930s. Why the wait?",
        "options": [
            {"text": "Nobody thought to look until the model was accepted",
             "correct": False,
             "why": "People looked, for well over a century. The barrier was "
                    "the instrument, not the idea — and the idea was "
                    "published in 1803."},
            {"text": "Light is too coarse to show an atom, so electrons "
                     "were used", "correct": True},
            {"text": "Lenses could not be ground accurately enough to "
                     "magnify that far", "correct": False,
             "why": "It is not a matter of better lenses or more "
                    "magnification. Once light is too coarse to show a thing, "
                    "no amount of magnifying it will help."},
            {"text": "Atoms move too fast to be photographed", "correct": False,
             "why": "The copper atoms in the last zoom step are held in a "
                    "regular stacked pattern. The problem was that light "
                    "cannot show them at all, not that they blur."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c2-01-h01",
        "band": "harder",
        "text": "Nitrogen and oxygen form one compound in which 14 g of "
                "nitrogen joins 16 g of oxygen, and another in which 14 g "
                "joins 32 g. A student predicts a third with 14 g to 24 g. "
                "What does Dalton's model say?",
        "options": [
            {"text": "It should exist, because any proportion of two elements "
                     "can be put together", "correct": False,
             "why": "Mixing and combining are different. You can mix any "
                    "proportions you like; the ratio claim is about whole "
                    "atoms joining, and half an atom cannot join."},
            {"text": "It should exist, because 24 g sits between two amounts "
                     "that both work", "correct": False,
             "why": "That is the reasoning the ratio claim rules out. Copper "
                    "and oxygen make one compound and then another, and never "
                    "anything in between the two."},
            {"text": "It should not exist — whole-number ratios leave no room "
                     "for anything in between", "correct": True},
            {"text": "It cannot be decided without weighing a nitrogen atom "
                     "first", "correct": False,
             "why": "You need no atomic mass at all. The jump from 16 g "
                    "straight to 32 g, with nothing between, is itself the "
                    "evidence for whole numbers."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h02",
        "band": "harder",
        "text": "Thomson knocked pieces off atoms and found electrons, so "
                "atoms genuinely can be split. Where does that leave Dalton's "
                "claim that they cannot?",
        "options": [
            {"text": "Wrong in general, and still exactly right inside "
                     "chemistry", "correct": True},
            {"text": "Wrong, so the claim has to be taken out of the model",
             "correct": False,
             "why": "Take it out and the sealed flask and the failure of "
                    "alchemy both lose their explanation. The claim did not "
                    "vanish — it gained a boundary."},
            {"text": "Still right, because knocking a piece off is not really "
                     "splitting", "correct": False,
             "why": "It genuinely is, and electrons are genuinely real. "
                    "Dalton was wrong, and he was wrong outside the range he "
                    "was working in."},
            {"text": "Never a real claim, only a simplification for beginners",
             "correct": False,
             "why": "Dalton meant it literally and chemists still use it "
                    "literally. A claim with a known boundary is not the same "
                    "thing as a polite lie."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h03",
        "band": "harder",
        "text": "A nuclear reactor really can turn one element into another. "
                "Does that mean the alchemists were right after all?",
        "options": [
            {"text": "Yes — it shows lead could have been turned into gold "
                     "by chemistry, given enough heat", "correct": False,
             "why": "What a reactor does is not a chemical reaction. The "
                    "claim that no chemical reaction changes an atom's kind is "
                    "left completely untouched by it."},
            {"text": "Yes, but only because modern equipment beats a furnace",
             "correct": False,
             "why": "Fifteen centuries of failure was never a skill problem. "
                    "Heating, dissolving and burning cannot reach what a "
                    "reactor reaches, however well you do them."},
            {"text": "No — a nuclear change is not a chemical reaction, and "
                     "alchemy was chemistry", "correct": True},
            {"text": "No — changing one element into another is impossible by "
                     "any means at all", "correct": False,
             "why": "It is possible, and reactors do it. The boundary Dalton's "
                    "claim has is drawn around chemistry, not around the whole "
                    "universe."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h04",
        "band": "harder",
        "text": "Across the zoom from 1 cm down to 0.000001 mm, at which step "
                "does the copper stop being orange?",
        "options": [
            {"text": "At the very first step, because a magnified view is not "
                     "the real thing", "correct": False,
             "why": "Every step is the same piece of wire, seen closer. What "
                    "changes across the sequence is the scale of the view, "
                    "not the substance in it."},
            {"text": "At no step — even the last view is a crowd, and colour "
                     "needs a crowd", "correct": True},
            {"text": "At 0.1 mm, once the microscope shows scratches and "
                     "grains", "correct": False,
             "why": "Scratches and grains are still copper, and still orange. "
                    "Nothing about the metal changed at that step — only how "
                    "much of it fits in the view."},
            {"text": "At 0.001 mm, where light can no longer reach it",
             "correct": False,
             "why": "Light failing to show you something does not take the "
                    "colour out of it. The wire on the bench stays orange the "
                    "whole way down the sequence."},
        ],
        "figure": None,
    },
]
