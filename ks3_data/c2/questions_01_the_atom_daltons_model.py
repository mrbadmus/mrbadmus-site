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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-01-e05",
        "band": "easier",
        "text": "This lesson uses the word property. What is a property of a "
                "substance?",
        "options": [
            {"text": "Something it is like or does — its colour, whether it "
                     "bends, whether it conducts",
             "correct": True},
            {"text": "The name of the element the substance was originally "
                     "made from",
             "correct": False,
             "why": "A property is about behaviour, not about origin. Iron "
                    "sulfide's properties belong to iron sulfide"},
            {"text": "The number of atoms that one particle of it contains",
             "correct": False,
             "why": "That is what a formula gives you. A property is what the "
                    "substance is like"},
            {"text": "The place on the periodic table where it is listed",
             "correct": False,
             "why": "Only elements have an entry, and its position is not a "
                    "property of the substance"},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e06",
        "band": "easier",
        "text": "What is a chemical reaction?",
        "options": [
            {"text": "A change in which the particles of a substance are "
                     "spread further apart than they were before",
             "correct": False,
             "why": "That is a change of state. No atom joins anything new, "
                    "and the substance is the one you started with"},
            {"text": "A change in which atoms are rearranged into different "
                     "substances",
             "correct": True},
            {"text": "A change in which one kind of atom is turned into "
                     "another kind",
             "correct": False,
             "why": "That is the one thing a chemical reaction never does. It "
                    "is why alchemy failed for fifteen hundred years"},
            {"text": "Any change that cannot be reversed once it has "
                     "happened",
             "correct": False,
             "why": "Plenty of reactions can be reversed, and plenty of "
                    "changes that cannot are not reactions at all"},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e07",
        "band": "easier",
        "text": "One of Dalton's three claims is about the atoms of a single "
                "element. What does it say?",
        "options": [
            {"text": "That they can be broken into smaller pieces if enough "
                     "energy is put into them somehow",
             "correct": False,
             "why": "Dalton said the opposite — that they cannot be broken at "
                    "all. That is the claim Thomson later overturned"},
            {"text": "That they combine with other elements in simple "
                     "whole-number ratios",
             "correct": False,
             "why": "That is a different one of the three, and it is about "
                    "elements combining rather than about one element's own "
                    "atoms"},
            {"text": "That they are all the same as each other, and different "
                     "from every other element's",
             "correct": True},
            {"text": "That they are all the same size, whichever element they "
                     "belong to",
             "correct": False,
             "why": "Dalton never claimed that, and it is not true. Atoms of "
                    "different elements differ in size and in mass"},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e08",
        "band": "easier",
        "text": "Which observation had been known for fifteen hundred years "
                "before Dalton wrote his model down?",
        "options": [
            {"text": "That an atom is made of a nucleus with electrons "
                     "outside it",
             "correct": False,
             "why": "That is Rutherford, a hundred years AFTER Dalton. Nobody "
                    "in 1803 knew an atom had any parts"},
            {"text": "That about forty million copper atoms fit across a "
                     "centimetre",
             "correct": False,
             "why": "Nothing could measure that until long after Dalton. He "
                    "worked from masses, not sizes"},
            {"text": "That electricity can split water into two gases",
             "correct": False,
             "why": "Electrolysis arrived at almost exactly Dalton's own "
                    "time, not fifteen centuries before it"},
            {"text": "That no amount of heating, dissolving or burning ever "
                     "turned lead into gold",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e09",
        "band": "easier",
        "text": "On the zoom, at which point does light stop being any use "
                "and electrons have to be used instead?",
        "options": [
            {"text": "At 0.0001 mm, past the reach of any light microscope",
             "correct": True},
            {"text": "At 1 mm, under an ordinary hand lens",
             "correct": False,
             "why": "A hand lens works perfectly well there. Nothing has run "
                    "out at a millimetre"},
            {"text": "At 0.1 mm, about as far as a school microscope reaches",
             "correct": False,
             "why": "That is where the SCHOOL microscope runs out, not where "
                    "light itself does. Better light microscopes go further"},
            {"text": "At 0.000001 mm, where the individual atoms finally come "
                     "into view",
             "correct": False,
             "why": "By then you are already using electrons. Light gave out "
                    "two steps earlier"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c2-01-s05",
        "band": "standard",
        "text": "Switch off Dalton's claim that elements combine in simple "
                "whole-number ratios. Which observation stops being "
                "explained?",
        "options": [
            {"text": "That water from a river, the sea and a laboratory "
                     "always holds the same proportion of hydrogen to oxygen",
             "correct": True},
            {"text": "That a reaction sealed in a flask weighs exactly the "
                     "same afterwards as it did before it was started",
             "correct": False,
             "why": "That rests on atoms not being created or destroyed, "
                    "which is a different claim and is still switched on"},
            {"text": "That no amount of chemistry has ever turned lead into "
                     "gold",
             "correct": False,
             "why": "That rests on atoms not changing kind. Ratios have "
                    "nothing to do with it"},
            {"text": "That copper is orange and lead is grey",
             "correct": False,
             "why": "Dalton's model does not explain colours at all. "
                    "Switching a claim off cannot take down something it "
                    "never held up"},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s06",
        "band": "standard",
        "text": "A student says Dalton could not have had evidence for atoms, "
                "because nobody could see one until the 1930s. What is the "
                "best reply?",
        "options": [
            {"text": "He did see them, using the best microscopes that were "
                     "available to a chemist working in 1803",
             "correct": False,
             "why": "No microscope of any kind could show an atom then. His "
                    "case never depended on seeing one"},
            {"text": "His evidence was measurement — fixed proportions, "
                     "balanced masses and whole-number ratios",
             "correct": True},
            {"text": "He had no evidence, so the model was a lucky guess that "
                     "later turned out to be right",
             "correct": False,
             "why": "A guess would not have predicted the ratios he "
                    "predicted. The numbers came first"},
            {"text": "Seeing something is the only evidence that counts, so "
                     "the model was not science until 1930",
             "correct": False,
             "why": "Chemistry had been using and testing the model for a "
                    "century by then. Measurement is evidence"},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s07",
        "band": "standard",
        "text": "Dalton's model says a reaction rearranges atoms into new "
                "substances. Which of these is therefore NOT a chemical "
                "reaction?",
        "options": [
            {"text": "Magnesium burning in air to leave a white powder behind "
                     "in the crucible",
             "correct": False,
             "why": "A new substance has been made from two others, so atoms "
                    "have been rearranged. That is a reaction"},
            {"text": "Iron rusting slowly over a month in a damp shed",
             "correct": False,
             "why": "Rust is a new substance made from iron and oxygen. Being "
                    "slow does not stop it being a reaction"},
            {"text": "Ice melting into water in a warm room",
             "correct": True},
            {"text": "Marble chips fizzing when dilute acid is poured onto "
                     "them",
             "correct": False,
             "why": "The fizzing is a new gas being made. Atoms have been "
                    "rearranged"},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s08",
        "band": "standard",
        "text": "Suppose Dalton's claim that all atoms of one element are "
                "alike were dropped, and the other two kept. Which "
                "observation would still be explained?",
        "options": [
            {"text": "That water everywhere holds hydrogen and oxygen in the "
                     "same proportion by mass",
             "correct": False,
             "why": "That needs atoms of one element to be alike. Mixed "
                    "masses would give a proportion that drifted"},
            {"text": "That every sample of copper oxide holds the same "
                     "proportion of copper to oxygen",
             "correct": False,
             "why": "Same problem as water. A fixed proportion by mass needs "
                    "the atoms to have a fixed mass"},
            {"text": "That elements combine in whole-number ratios of fixed "
                     "masses",
             "correct": False,
             "why": "The ratios are ratios of masses, so they need identical "
                    "atoms to come out the same every time"},
            {"text": "That a sealed reaction weighs the same before and after "
                     "it has finished",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s09",
        "band": "standard",
        "text": "Iron rusts, wood burns and copper roofs turn green. What has "
                "happened to the atoms in every one of those changes?",
        "options": [
            {"text": "They have been rearranged into new substances, and none "
                     "has changed kind",
             "correct": True},
            {"text": "Some of them have been destroyed, which is why the wood "
                     "is lighter",
             "correct": False,
             "why": "Nothing is destroyed. The wood's atoms have left as "
                    "gases, and those gases have mass"},
            {"text": "Some of them have been turned into atoms of a different "
                     "element",
             "correct": False,
             "why": "No chemical change does that. It is the one thing "
                    "fifteen hundred years of alchemy could never manage"},
            {"text": "They have all been split into the smaller pieces that "
                     "Thomson found",
             "correct": False,
             "why": "Chemistry never splits an atom. Rusting and burning "
                    "rearrange whole atoms"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-01-h05",
        "band": "harder",
        "text": "Every sample of water ever measured holds 1 g of hydrogen "
                "for every 8 g of oxygen. Which of Dalton's claims does that "
                "measurement support most directly?",
        "options": [
            {"text": "That all atoms of one element are alike, so a fixed "
                     "count gives a fixed mass",
             "correct": True},
            {"text": "That atoms cannot be created or destroyed in a reaction",
             "correct": False,
             "why": "That claim is about totals before and after a reaction. "
                    "It says nothing about the proportion inside a "
                    "compound"},
            {"text": "That atoms are far too small to be seen with any "
                     "microscope",
             "correct": False,
             "why": "Their size is not one of Dalton's three claims, and no "
                    "mass measurement could establish it"},
            {"text": "That one kind of atom can never be turned into "
                     "another",
             "correct": False,
             "why": "That claim is what alchemy's failure supports. Fixed "
                    "proportions are a different piece of evidence"},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h06",
        "band": "harder",
        "text": "About forty million copper atoms fit across the 1 cm of "
                "wire. Roughly how wide is one copper atom?",
        "options": [
            {"text": "About 0.3 mm — small, but a good hand lens would show "
                     "you one if you looked carefully",
             "correct": False,
             "why": "That is thicker than a hair. Dividing 10 mm by forty "
                    "million gives something ten million times smaller"},
            {"text": "About 0.0000003 mm",
             "correct": True},
            {"text": "About 0.003 mm",
             "correct": False,
             "why": "That is around the size of a small cell. You are still "
                    "several thousand times too big"},
            {"text": "About 0.03 mm",
             "correct": False,
             "why": "That is about half the width of a hair, and a school "
                    "microscope would show it easily. An atom would not"},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h07",
        "band": "harder",
        "text": "A reaction is sealed in a flask and weighed before and "
                "after. Which of Dalton's claims is that experiment actually "
                "testing?",
        "options": [
            {"text": "That all the atoms of one element are alike, since "
                     "otherwise the masses would not agree so neatly",
             "correct": False,
             "why": "A balance reads a total. It would read the same total "
                    "whether the atoms in it were alike or not"},
            {"text": "That elements combine in simple whole-number ratios",
             "correct": False,
             "why": "The balance never sees the ratio. It only sees the "
                    "total, before and after"},
            {"text": "That atoms are neither created nor destroyed",
             "correct": True},
            {"text": "That atoms cannot be split into anything smaller",
             "correct": False,
             "why": "Splitting an atom would not change the total mass on the "
                    "balance by anything you could weigh"},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h08",
        "band": "harder",
        "text": "Which result, if anyone ever obtained it, would break "
                "Dalton's model as chemists actually use it today?",
        "options": [
            {"text": "A machine that splits an atom into smaller pieces than "
                     "anyone had managed to produce before",
             "correct": False,
             "why": "That has already been done, and the model survived it. "
                    "Splitting an atom is not a chemical change"},
            {"text": "A finding that atoms of one element can have different "
                     "masses from each other",
             "correct": False,
             "why": "Also already found, and also outside chemistry's range. "
                    "The model was given a boundary rather than dropped"},
            {"text": "The discovery of a new element that nobody had listed "
                     "before",
             "correct": False,
             "why": "New elements have been added for two centuries without "
                    "troubling the model at all"},
            {"text": "A chemical reaction that turned copper into gold",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h09",
        "band": "harder",
        "text": "Atoms of one element really can have different masses, which "
                "Dalton denied. Why does that not wreck the chemistry he used "
                "the claim for?",
        "options": [
            {"text": "Because those atoms still cannot change kind, so "
                     "reactions still balance and proportions still hold",
             "correct": True},
            {"text": "Because the difference is far too small for any balance "
                     "in any laboratory anywhere to detect it",
             "correct": False,
             "why": "The difference is easily measurable. It survives for a "
                    "better reason than being invisible"},
            {"text": "Because chemists agreed to ignore it so that the older "
                     "model would not have to be rewritten",
             "correct": False,
             "why": "Nothing was ignored. The model was given a boundary, "
                    "which is a different thing from looking away"},
            {"text": "Because the atoms with the odd masses are all "
                     "radioactive and are never met in a school laboratory",
             "correct": False,
             "why": "Most are perfectly ordinary. Chlorine in the lab is a "
                    "mixture of two masses and behaves exactly as expected"},
        ],
        "figure": None,
    },
]
