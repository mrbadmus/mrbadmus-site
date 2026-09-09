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

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c2-01-e10",
        "band": "easier",
        "text": "Dalton's model opens with a claim about matter in general. "
                "What does that opening claim say?",
        "options": [
            {"text": "Matter is made of pieces that can be cut in half again "
                     "and again for ever",
             "correct": False,
             "why": "That is the idea Dalton's model replaced. If cutting "
                    "never ran out there would be no smallest particle at "
                    "all."},
            {"text": "Everything is made of atoms", "correct": True},
            {"text": "Matter is made of earth, air, fire and water",
             "correct": False,
             "why": "The old Greek list, dropped long before 1803. Dalton's "
                    "elements are the hundred or so kinds of atom."},
            {"text": "Matter is made of particles that are all identical to "
                     "one another",
             "correct": False,
             "why": "The particle model already said matter is made of "
                    "particles. What Dalton added is that they come in "
                    "kinds."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e11",
        "band": "easier",
        "text": "About how many different kinds of atom are there?",
        "options": [
            {"text": "About a thousand", "correct": False,
             "why": "Ten times too many. The periodic table has a little over "
                    "a hundred entries, and each one is a kind of atom."},
            {"text": "Exactly four, as the Greeks listed", "correct": False,
             "why": "Earth, air, fire and water was dropped long before "
                    "Dalton wrote. Four is nowhere near enough."},
            {"text": "About a hundred, one kind for each element",
             "correct": True},
            {"text": "Too many for anyone to have counted them",
             "correct": False,
             "why": "They have been counted and listed. New ones are still "
                    "added, but only a handful at a time."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e12",
        "band": "easier",
        "text": "In science, what is a model?",
        "options": [
            {"text": "A simplified account of how something works, kept while "
                     "it explains what it was built to explain",
             "correct": True},
            {"text": "An object built to show what something looks like in real "
                     "life, so that anyone can see how it works",
             "correct": False,
             "why": "A kit of plastic balls is a way of showing a model. The "
                    "model itself is the idea behind it."},
            {"text": "A guess that nobody has tested yet", "correct": False,
             "why": "An untested guess is a hypothesis. A model is built to "
                    "fit measurements that have already been made."},
            {"text": "A picture showing exactly what a thing really looks "
                     "like",
             "correct": False,
             "why": "No model shows exactly. A model leaves things out on "
                    "purpose, and that is what makes it usable."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e13",
        "band": "easier",
        "text": "A teacher holds up a kit of plastic balls and sticks. Where "
                "is the model?",
        "options": [
            {"text": "In the plastic, because the kit is the model itself",
             "correct": False,
             "why": "The kit is a way of showing the model. Take the plastic "
                    "away and the ideas it stands for are untouched."},
            {"text": "In the ideas the kit stands for", "correct": True},
            {"text": "Nowhere, because a model has to be an object you can "
                     "hold in your hand",
             "correct": False,
             "why": "Most models in science cannot be held at all. Dalton's "
                    "is a set of sentences."},
            {"text": "In the sticks, which show the joins between the atoms",
             "correct": False,
             "why": "The sticks show one part of what the model says. The "
                    "model is the whole set of ideas, not one piece of the "
                    "kit."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e14",
        "band": "easier",
        "text": "Which of these is the smallest?",
        "options": [
            {"text": "A grain of salt you can see on your hand",
             "correct": False,
             "why": "Visible without any instrument, so it is millions of "
                    "atoms across."},
            {"text": "A bacterium under a school microscope",
             "correct": False,
             "why": "Small, but a light microscope shows one easily. Atoms "
                    "are far below anything light can reach."},
            {"text": "A red blood cell", "correct": False,
             "why": "About 0.007 mm across, which is tens of thousands of "
                    "atoms wide."},
            {"text": "A copper atom", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e15",
        "band": "easier",
        "text": "A student says an atom is the smallest thing that exists. "
                "Why is that wrong?",
        "options": [
            {"text": "Because electrons, which are found inside atoms, are "
                     "smaller still",
             "correct": True},
            {"text": "Because a molecule is smaller than an atom",
             "correct": False,
             "why": "A molecule is two or more atoms joined, so it is bigger "
                    "than an atom rather than smaller."},
            {"text": "Because specks of dust are smaller than atoms",
             "correct": False,
             "why": "A speck of dust holds many millions of atoms. It is "
                    "enormous by comparison."},
            {"text": "Because atoms of different elements are different "
                     "sizes",
             "correct": False,
             "why": "True, and it does not answer the question. Even the "
                    "smallest atom is not the smallest thing there is."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e16",
        "band": "easier",
        "text": "Atoms were first seen in the 1930s. What kind of instrument "
                "showed them?",
        "options": [
            {"text": "A light microscope with a much stronger lens",
             "correct": False,
             "why": "Light is too coarse to show an atom, so no light "
                    "microscope will manage it however strong the lens."},
            {"text": "An electron microscope", "correct": True},
            {"text": "A telescope pointed the other way", "correct": False,
             "why": "A telescope gathers light from far off. It runs into "
                    "exactly the same limit as any other light instrument."},
            {"text": "A magnifying glass ground to a finer curve",
             "correct": False,
             "why": "The lens is not what fails. Once light is too coarse for "
                    "the job, better grinding changes nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e17",
        "band": "easier",
        "text": "Dalton claimed atoms are neither created nor destroyed. What "
                "does that say about the number of oxygen atoms in a "
                "reaction?",
        "options": [
            {"text": "There are exactly as many afterwards as before",
             "correct": True},
            {"text": "There are fewer afterwards, because some are used up",
             "correct": False,
             "why": "Nothing is used up. The oxygen atoms end up inside the "
                    "products instead of where they started."},
            {"text": "There are more afterwards, because the reaction makes "
                     "new ones",
             "correct": False,
             "why": "A reaction cannot make an atom. It joins and separates "
                    "the ones it was given."},
            {"text": "There are fewer, because some become atoms of another "
                     "element",
             "correct": False,
             "why": "No chemical reaction changes an atom's kind. Every "
                    "oxygen atom is still oxygen at the end."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e18",
        "band": "easier",
        "text": "Dalton said the atoms of one element differ from those of "
                "another. State one way they differ.",
        "options": [
            {"text": "In how long they last before they wear out",
             "correct": False,
             "why": "Atoms do not wear out. The atoms in your hand are older "
                    "than the Earth is."},
            {"text": "In their colour, which is different for each element",
             "correct": False,
             "why": "Colour is what a huge crowd of atoms does to light. A "
                    "single atom has no colour at all."},
            {"text": "In their mass", "correct": True},
            {"text": "In how quickly they can be turned into another element",
             "correct": False,
             "why": "No chemical process turns one element into another at "
                    "any speed. That is the whole point of the claim."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e19",
        "band": "easier",
        "text": "What is a molecule?",
        "options": [
            {"text": "A single atom sitting on its own", "correct": False,
             "why": "One atom on its own is just an atom. A molecule needs at "
                    "least two of them joined."},
            {"text": "Two or more atoms joined together", "correct": True},
            {"text": "Any particle that is too small to see", "correct": False,
             "why": "A single atom is too small to see and is not a molecule. "
                    "Size is not what the word means."},
            {"text": "A piece of a substance small enough to fit under a "
                     "microscope",
             "correct": False,
             "why": "Anything a microscope can show holds many millions of "
                    "atoms."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e20",
        "band": "easier",
        "text": "In the particle model, what does the word particle stand "
                "for?",
        "options": [
            {"text": "Any tiny piece of a substance — one atom, or several "
                     "joined together",
             "correct": True},
            {"text": "An atom, and never a group of atoms joined together "
                     "into something bigger", "correct": False,
             "why": "The particles in water are groups of atoms rather than "
                    "single atoms. The word is wider than atom."},
            {"text": "A grain of a substance small enough to need a school "
                     "microscope to see it",
             "correct": False,
             "why": "A grain is millions of particles across. The model's "
                    "particles are far below anything a microscope shows."},
            {"text": "A piece of dust floating in the air", "correct": False,
             "why": "Dust is a visible speck of solid. It is made of "
                    "particles rather than being one."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e21",
        "band": "easier",
        "text": "Dalton's model explains a great deal, but not everything. "
                "Which of these is outside what it can explain?",
        "options": [
            {"text": "Why a reaction sealed in a flask keeps its mass",
             "correct": False,
             "why": "Explained by the claim that atoms are neither created "
                    "nor destroyed."},
            {"text": "Why every sample of water holds the same proportion of "
                     "hydrogen",
             "correct": False,
             "why": "Explained by identical atoms joining in fixed "
                    "whole-number ratios."},
            {"text": "Why no furnace ever turned lead into gold",
             "correct": False,
             "why": "Explained by atoms never changing kind during a chemical "
                    "reaction."},
            {"text": "Why copper is orange and lead is grey", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e22",
        "band": "easier",
        "text": "What makes scientists keep using a model?",
        "options": [
            {"text": "It is true in every last detail", "correct": False,
             "why": "No model is, and Dalton's is wrong about two things. "
                    "Being useful is the test, not being true."},
            {"text": "It was written down by a scientist whose name everybody "
                     "in the subject already knew",
             "correct": False,
             "why": "Fame decides nothing. A model earns its place from the "
                    "observations it accounts for."},
            {"text": "It explains what was known and predicts what turns out "
                     "to be right",
             "correct": True},
            {"text": "It is the simplest idea that anyone has suggested",
             "correct": False,
             "why": "Simple is helpful and it is not the test. A simple model "
                    "that explained nothing would be dropped."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e23",
        "band": "easier",
        "text": "A better model replaces an older one. What does that show "
                "about science?",
        "options": [
            {"text": "That the scientist who wrote the older one had been "
                     "careless",
             "correct": False,
             "why": "Dalton was not careless. He accounted for everything the "
                    "evidence of his day contained."},
            {"text": "That the older model was never really science at all",
             "correct": False,
             "why": "It was science, and good science — tested, used, and "
                    "eventually given a boundary."},
            {"text": "That science is working as it should", "correct": True},
            {"text": "That models cannot be trusted for anything important",
             "correct": False,
             "why": "The opposite. A model that improves when new evidence "
                    "arrives is what makes science trustworthy."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e24",
        "band": "easier",
        "text": "Which of these is a single atom?",
        "options": [
            {"text": "One copper atom in a wire", "correct": True},
            {"text": "A drop of mercury from a thermometer", "correct": False,
             "why": "One drop holds many millions of millions of mercury "
                    "atoms."},
            {"text": "A grain of table salt", "correct": False,
             "why": "A grain is a crowd, and salt's particles are built from "
                    "more than one kind of atom."},
            {"text": "One particle of water", "correct": False,
             "why": "A water particle holds three atoms joined together, so "
                    "it is a molecule rather than an atom."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e25",
        "band": "easier",
        "text": "Some atoms of one element turned out to be heavier than "
                "others. Which of Dalton's claims did that show to be wrong?",
        "options": [
            {"text": "That atoms join in simple whole-number ratios",
             "correct": False,
             "why": "Ratios are about how many atoms combine, not about what "
                    "each one weighs."},
            {"text": "That all the atoms of one element are alike",
             "correct": True},
            {"text": "That atoms are neither created nor destroyed",
             "correct": False,
             "why": "That claim is about totals across a reaction, and an "
                    "atom's mass leaves it untouched."},
            {"text": "That no reaction changes one element into another",
             "correct": False,
             "why": "Still standing, and it is the claim chemistry leans on "
                    "hardest."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e26",
        "band": "easier",
        "text": "Who showed that atoms can be split, about a century after "
                "Dalton?",
        "options": [
            {"text": "Dalton himself, later on in his own life",
             "correct": False,
             "why": "Dalton died in 1844 and denied to the end that an atom "
                    "could be split."},
            {"text": "The alchemists, using furnaces and acids",
             "correct": False,
             "why": "The alchemists split nothing. Their failure is evidence "
                    "in the model's favour."},
            {"text": "Nobody — no atom has ever been split", "correct": False,
             "why": "Atoms have been split, and electrons are real. Chemistry "
                    "is simply not the thing that does it."},
            {"text": "J. J. Thomson, who found electrons", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e27",
        "band": "easier",
        "text": "What were the alchemists trying to do?",
        "options": [
            {"text": "Split an atom into smaller pieces", "correct": False,
             "why": "Nobody knew there was anything inside an atom until "
                    "1897, long after alchemy had ended."},
            {"text": "Measure how small an atom is", "correct": False,
             "why": "No measurement of an atom's size was possible then, and "
                    "it was not what they were after."},
            {"text": "Turn lead into gold", "correct": True},
            {"text": "Count how many kinds of atom there are",
             "correct": False,
             "why": "A list of the elements came much later. What they wanted "
                    "was one substance changed into another."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e28",
        "band": "easier",
        "text": "A view of a copper surface 0.000001 mm across shows the "
                "individual atoms. About how many fit across it?",
        "options": [
            {"text": "About four", "correct": True},
            {"text": "About four hundred", "correct": False,
             "why": "Four hundred atoms would need a view a hundred times "
                    "wider than this one."},
            {"text": "About four million", "correct": False,
             "why": "Four million is roughly what fits across a millimetre of "
                    "the wire, not across this tiny view."},
            {"text": "Just under one, so only part of an atom is in view",
             "correct": False,
             "why": "A whole patch of atoms is in view at this step, stacked "
                    "in a regular pattern."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e29",
        "band": "easier",
        "text": "Which of these could a good light microscope show you?",
        "options": [
            {"text": "A single copper atom", "correct": False,
             "why": "Light is too coarse. No light microscope of any quality "
                    "shows one."},
            {"text": "A plant cell", "correct": True},
            {"text": "An electron", "correct": False,
             "why": "An electron is far smaller than an atom, so it is even "
                    "further out of reach."},
            {"text": "The gaps between the atoms in a metal",
             "correct": False,
             "why": "Those gaps are smaller than the atoms themselves, which "
                    "puts them further out of reach again."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e30",
        "band": "easier",
        "text": "A new model of the atom is put forward. What must it manage "
                "before chemists will accept it?",
        "options": [
            {"text": "Be simpler than the model it is replacing",
             "correct": False,
             "why": "Simpler is welcome and not required. The later models of "
                    "the atom are more complicated than Dalton's, not less."},
            {"text": "Come from a scientist with a bigger reputation",
             "correct": False,
             "why": "Reputation is not evidence. A model is judged by the "
                    "observations it accounts for."},
            {"text": "Agree with the old model in every single detail",
             "correct": False,
             "why": "Then it would say nothing new. A replacement has to "
                    "disagree somewhere or there is no reason to change."},
            {"text": "Explain everything the old model explained, and more",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e31",
        "band": "easier",
        "text": "Dalton's model rests on three claims. Which of these ideas "
                "is not one of them?",
        "options": [
            {"text": "Atoms are far too small to see", "correct": True},
            {"text": "All the atoms of one element are alike",
             "correct": False,
             "why": "That is one of the three, and it holds up the fixed "
                    "proportions in water."},
            {"text": "Atoms cannot be created or destroyed", "correct": False,
             "why": "That is another of the three, and it is what keeps a "
                    "sealed flask's mass steady."},
            {"text": "Elements combine in simple whole-number ratios",
             "correct": False,
             "why": "That is the third, and it is why there is no compound "
                    "in between the two that exist."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-e32",
        "band": "easier",
        "text": "Gold is an element. What is the smallest particle of gold "
                "there can be?",
        "options": [
            {"text": "The smallest grain of gold dust anyone can make",
             "correct": False,
             "why": "The smallest grain you could see still holds many "
                    "millions of atoms."},
            {"text": "A gold molecule, made of two gold atoms joined",
             "correct": False,
             "why": "Gold is not built from pairs. Its smallest particle is "
                    "one atom on its own."},
            {"text": "Half a gold atom", "correct": False,
             "why": "Half an atom of gold would not be gold at all, and "
                    "splitting an atom is outside chemistry anyway."},
            {"text": "One gold atom", "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c2-01-s10",
        "band": "standard",
        "text": "A student says a kit of plastic balls and sticks is a bad "
                "model because atoms are not plastic and not that big. What "
                "is the best reply?",
        "options": [
            {"text": "The student is right, and the kit should not be used "
                     "until somebody makes one that is closer to the "
                     "real thing",
             "correct": False,
             "why": "Nothing in the kit is meant to be a photograph. Judging "
                    "it as one throws away the part that works."},
            {"text": "The kit is fine, because atoms really are coloured "
                     "spheres of about that shape",
             "correct": False,
             "why": "Atoms are not tiny coloured balls. What the kit gets "
                    "right is the arrangement, not the appearance."},
            {"text": "The student is right, because a model has to match "
                     "reality in every way it can",
             "correct": False,
             "why": "No model matches in every way. A map of a city leaves "
                    "out almost everything and still gets you there."},
            {"text": "A model is judged by what it helps you explain, not by "
                     "how closely it resembles the real thing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s11",
        "band": "standard",
        "text": "You want to explain why a reaction sealed in a flask weighs "
                "the same at the end. Which model does the job?",
        "options": [
            {"text": "Dalton's, because whole atoms being rearranged is "
                     "already enough", "correct": True},
            {"text": "A model with a nucleus and electrons, because only that "
                     "one is up to date",
             "correct": False,
             "why": "Up to date is not the test. The later detail adds "
                    "nothing at all to this particular question."},
            {"text": "No model at all, since a balance reading is simply a "
                     "fact",
             "correct": False,
             "why": "The reading is the observation. A model is what tells "
                    "you why it came out that way."},
            {"text": "A model of the flask and its stopper, since the seal is "
                     "what matters",
             "correct": False,
             "why": "The seal is what makes the test fair. What explains the "
                    "result is what happens to the atoms inside."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s12",
        "band": "standard",
        "text": "A student writes that atoms decide which partners they like "
                "best before joining up. What is the problem with that?",
        "options": [
            {"text": "Atoms do decide, but only once they are hot enough to "
                     "move about",
             "correct": False,
             "why": "Heating changes how much energy the particles have, not "
                    "whether they are capable of choosing."},
            {"text": "Atoms are not alive and choose nothing", "correct": True},
            {"text": "Atoms decide, but a chemist has no way of telling which "
                     "choice was made",
             "correct": False,
             "why": "There is no choice to detect. The same elements combine "
                    "in the same ratios every single time."},
            {"text": "Nothing is wrong, because it is only a shorter way of "
                     "saying it",
             "correct": False,
             "why": "It sounds harmless and it teaches a wrong idea, which is "
                    "exactly why chemists avoid it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s13",
        "band": "standard",
        "text": "Iron filings are heated with sulfur and the black solid left "
                "behind is not picked up by a magnet. What has happened to "
                "the iron atoms?",
        "options": [
            {"text": "They have been destroyed, which is why the magnet finds "
                     "nothing",
             "correct": False,
             "why": "Nothing is destroyed. Every iron atom is still there, "
                    "held in a new arrangement."},
            {"text": "They have been split into smaller pieces by the heat of "
                     "the burner",
             "correct": False,
             "why": "A Bunsen burner comes nowhere near splitting an atom, "
                    "and chemistry never does it at all."},
            {"text": "They are still iron atoms, now joined to sulfur atoms",
             "correct": True},
            {"text": "They have turned into atoms of a brand new element",
             "correct": False,
             "why": "No reaction changes an atom's kind. The iron is still "
                    "iron, joined to something else."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s14",
        "band": "standard",
        "text": "An atom is defined as the smallest particle of an element "
                "rather than of a substance. Why does that word matter?",
        "options": [
            {"text": "Because a particle of water holds more than one kind of "
                     "atom", "correct": True},
            {"text": "Because every substance is really a mixture of "
                     "something",
             "correct": False,
             "why": "Plenty of substances are not mixtures. The trouble is "
                    "that some of them are compounds."},
            {"text": "Because the word substance is only ever used about "
                     "solids",
             "correct": False,
             "why": "Gases and liquids are substances too. The wording has "
                    "nothing to do with state."},
            {"text": "Because an element has no particles in it at all, only "
                     "atoms",
             "correct": False,
             "why": "An element's atoms are its particles. The wording is "
                    "there for compounds, whose particles hold two kinds."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s15",
        "band": "standard",
        "text": "Which prediction does Dalton's model make that an experiment "
                "could go and check?",
        "options": [
            {"text": "That every element will one day be seen under a "
                     "microscope",
             "correct": False,
             "why": "The model says nothing about instruments, and seeing an "
                    "atom took another hundred and thirty years."},
            {"text": "That atoms will be found to be built from smaller "
                     "pieces",
             "correct": False,
             "why": "Dalton predicted the opposite. That finding came later "
                    "and came from other people."},
            {"text": "That heating a metal for long enough in a hot enough "
                     "furnace turns it into another metal",
             "correct": False,
             "why": "The model rules that out, and fifteen centuries of "
                    "alchemy had already suggested as much."},
            {"text": "That every sample of a compound holds its elements in "
                     "the same proportion by mass", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s16",
        "band": "standard",
        "text": "Aluminium melts at 660 °C. What is the melting point of one "
                "aluminium atom?",
        "options": [
            {"text": "660 °C, since one atom of aluminium is still aluminium",
             "correct": False,
             "why": "Melting is a crowd coming loose from its arrangement, "
                    "and one atom has no arrangement to lose."},
            {"text": "One atom has no melting point", "correct": True},
            {"text": "Much lower, because a single atom is easier to melt "
                     "than a whole block",
             "correct": False,
             "why": "There is no easier or harder about it. Melting is not "
                    "something a single atom can do at all."},
            {"text": "Much higher, because there are no other atoms helping "
                     "it break away",
             "correct": False,
             "why": "The same mistake in the other direction. A melting point "
                    "belongs to a substance, not to one particle."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s17",
        "band": "standard",
        "text": "Atoms are built from smaller pieces. Explain why chemists "
                "still call the atom the smallest particle of an element.",
        "options": [
            {"text": "Because chemists have not yet caught up with the "
                     "discovery of what is inside every atom",
             "correct": False,
             "why": "They have, and they use it constantly at GCSE. The "
                    "definition is about the range chemistry works in."},
            {"text": "Because the smaller pieces are too small to make any "
                     "difference",
             "correct": False,
             "why": "Electrons matter enormously and explain bonding and "
                    "electricity. Size is not the reason."},
            {"text": "Because splitting an atom leaves you with something "
                     "that is no longer that element", "correct": True},
            {"text": "Because the smaller pieces inside an atom have never "
                     "actually been seen by anybody at all",
             "correct": False,
             "why": "They have been detected in many ways. The reason is what "
                    "splitting does to the element, not what can be seen."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s18",
        "band": "standard",
        "text": "A copper atom is about 0.0000003 mm across. About how many "
                "would fit across a cell 0.003 mm wide?",
        "options": [
            {"text": "About 10 000", "correct": True},
            {"text": "About 100", "correct": False,
             "why": "Out by a factor of a hundred. Dividing 0.003 by "
                    "0.0000003 gives ten thousand."},
            {"text": "About 1 000 000", "correct": False,
             "why": "A hundred times too many. A million copper atoms in a "
                    "row would stretch about a third of a millimetre."},
            {"text": "About 10", "correct": False,
             "why": "Ten atoms span three millionths of a millimetre, a "
                    "thousand times smaller than the cell."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s19",
        "band": "standard",
        "text": "A student argues that Dalton's model must be true because "
                "schools still teach it. What is wrong with that reasoning?",
        "options": [
            {"text": "Nothing — two centuries of being taught in schools "
                     "everywhere is strong evidence all on its own",
             "correct": False,
             "why": "How long an idea has been taught is not evidence for it. "
                    "What counts is what it explains."},
            {"text": "It is taught because it works for chemistry, and two of "
                     "its claims are known to be wrong", "correct": True},
            {"text": "It is wrong, because a model is only a way of talking "
                     "and can never be called true or false",
             "correct": False,
             "why": "A model's claims can be checked, and two of Dalton's "
                    "were checked and failed."},
            {"text": "It is taught only to beginners, so nobody really "
                     "believes it",
             "correct": False,
             "why": "Working chemists use it daily for reactions. It is not a "
                    "beginner's version of something else."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s20",
        "band": "standard",
        "text": "Oxygen gas is made of pairs of oxygen atoms joined together. "
                "What is one of those pairs called?",
        "options": [
            {"text": "An atom, because both halves of it are oxygen",
             "correct": False,
             "why": "An atom is a single one. Two of them joined is something "
                    "bigger than an atom."},
            {"text": "A molecule", "correct": True},
            {"text": "A compound, because two things have been joined",
             "correct": False,
             "why": "A compound needs two different elements. Both of these "
                    "atoms are oxygen."},
            {"text": "A mixture of two separate oxygen atoms",
             "correct": False,
             "why": "A mixture can be separated without a reaction. These two "
                    "atoms are genuinely joined."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s21",
        "band": "standard",
        "text": "Melting, gas pressure and diffusion were all explained "
                "before Dalton wrote. Explain why those explanations needed "
                "no kinds of particle.",
        "options": [
            {"text": "Because the particles involved really are all of one "
                     "kind in those cases",
             "correct": False,
             "why": "Air holds several kinds and still diffuses. Those "
                    "explanations work whatever kinds are present."},
            {"text": "Because those changes are not really changes at all",
             "correct": False,
             "why": "Melting and diffusion are real changes. They are "
                    "physical rather than chemical, which is a different "
                    "point."},
            {"text": "Because nobody had thought to ask about kinds until "
                     "1803",
             "correct": False,
             "why": "The reason is not historical. Those explanations would "
                    "still work today with no mention of kinds."},
            {"text": "Because they depend only on how particles move and how "
                     "far apart they are", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s22",
        "band": "standard",
        "text": "A zoom goes from a view 0.1 mm across to one 0.0001 mm "
                "across. How many times closer is the second view?",
        "options": [
            {"text": "10 times closer", "correct": False,
             "why": "Ten times would take 0.1 mm to 0.01 mm, which is one "
                    "step of the way rather than three."},
            {"text": "100 times closer", "correct": False,
             "why": "A hundred times gives 0.001 mm, still ten times wider "
                    "than the view described."},
            {"text": "1000 times closer", "correct": True},
            {"text": "10 000 times closer", "correct": False,
             "why": "Ten thousand times would give 0.00001 mm, ten times "
                    "smaller than the view described."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s23",
        "band": "standard",
        "text": "A weather forecast comes from a model that gets some days "
                "wrong, and forecasters use it every morning. Which idea "
                "about models does that show?",
        "options": [
            {"text": "A model is kept while it is right often enough to be "
                     "useful", "correct": True},
            {"text": "A model only has to convince the people who are using "
                     "it",
             "correct": False,
             "why": "Belief is not the test. Forecasts are checked against "
                    "what the weather actually did."},
            {"text": "A model that is ever wrong should be abandoned "
                     "immediately",
             "correct": False,
             "why": "Then almost every model in science would go, Dalton's "
                    "included. Being wrong somewhere is normal."},
            {"text": "The weather cannot really be studied scientifically at "
                     "all",
             "correct": False,
             "why": "It is studied with measurements and predictions like "
                    "anything else. Hard to predict is not unscientific."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s24",
        "band": "standard",
        "text": "A student writes that some of the atoms get used up during a "
                "reaction. Which correction should they make?",
        "options": [
            {"text": "None — atoms are used up, which is why fuels run out",
             "correct": False,
             "why": "A fuel runs out because its atoms have been rearranged "
                    "into new substances and carried away as gases."},
            {"text": "The atoms are all still there, rearranged into the "
                     "products", "correct": True},
            {"text": "Atoms are used up only if the reaction is left running "
                     "long enough",
             "correct": False,
             "why": "Time changes nothing here. No length of reaction "
                    "destroys a single atom."},
            {"text": "Atoms are used up but replaced by new ones of the same "
                     "kind",
             "correct": False,
             "why": "Nothing is destroyed and nothing is made. The same atoms "
                    "carry straight through the reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s25",
        "band": "standard",
        "text": "Gold leaf can be beaten until it is only a few hundred atoms "
                "thick, and it is still gold. What does that show?",
        "options": [
            {"text": "Gold atoms are squashed flat by the hammering, which is "
                     "what makes the leaf thin",
             "correct": False,
             "why": "The atoms are not squashed. The layers of them slide "
                    "over one another and spread out."},
            {"text": "Gold is the only element that can be treated in this "
                     "way",
             "correct": False,
             "why": "Gold is unusually easy to beat thin, and other metals "
                    "can be rolled thin too."},
            {"text": "The atoms are still gold atoms, so the substance itself "
                     "has not changed", "correct": True},
            {"text": "The leaf must be a different substance from the block "
                     "it came from",
             "correct": False,
             "why": "Same atoms, same element, same substance. Only the shape "
                    "of the piece has changed."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s26",
        "band": "standard",
        "text": "Mercury is a liquid at room temperature and copper is a "
                "solid. Can Dalton's model explain that difference?",
        "options": [
            {"text": "Yes — mercury atoms must sit further apart than copper "
                     "atoms do",
             "correct": False,
             "why": "The spacing of particles comes from the particle model. "
                    "Dalton's three claims say nothing about it."},
            {"text": "Yes — mercury atoms are lighter, so they flow more "
                     "easily",
             "correct": False,
             "why": "A mercury atom is heavier than a copper atom and mercury "
                    "is still the liquid. Mass does not settle the state."},
            {"text": "No — the difference is too small for any model to "
                     "explain",
             "correct": False,
             "why": "It is a large and obvious difference, and later models "
                    "do explain it. Dalton's was not built for it."},
            {"text": "No — it deals with combining and mass, not with states",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s27",
        "band": "standard",
        "text": "Copper wire conducts electricity. Explain why saying that a "
                "copper atom conducts electricity is not sensible.",
        "options": [
            {"text": "Because conducting means charge travelling through many "
                     "atoms, and one atom is not a path", "correct": True},
            {"text": "Because a copper atom will only conduct once it has "
                     "been warmed up enough to release its charge",
             "correct": False,
             "why": "Temperature is not the issue. One atom is no route for a "
                    "current however warm it is."},
            {"text": "Because copper atoms are far too small to carry a "
                     "current",
             "correct": False,
             "why": "Size is not the problem. Current flows through wires "
                    "made of exactly those atoms."},
            {"text": "Because only wires can conduct, and an atom is not a "
                     "wire",
             "correct": False,
             "why": "Plenty of things conduct without being wires. What "
                    "matters is a path for charge to move along."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s28",
        "band": "standard",
        "text": "Dalton's model is still the right tool for reactions. Which "
                "question would send you to a later model instead?",
        "options": [
            {"text": "Why does a reaction sealed in a flask keep its mass?",
             "correct": False,
             "why": "Dalton answers that one directly: atoms are neither "
                    "created nor destroyed."},
            {"text": "Why does every sample of water hold the same proportion "
                     "of hydrogen?",
             "correct": False,
             "why": "Dalton answers that one too, with identical atoms "
                    "joining in fixed ratios."},
            {"text": "Why do two atoms of one element sometimes have "
                     "different masses?", "correct": True},
            {"text": "Why has no chemist ever made gold out of lead?",
             "correct": False,
             "why": "That is his most famous answer of all — kinds do not "
                    "change in a chemical reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s29",
        "band": "standard",
        "text": "Thomson's model of the atom came after Dalton's, and "
                "Rutherford's came after Thomson's. What does that sequence "
                "show?",
        "options": [
            {"text": "That each scientist proved the one before him had been "
                     "careless",
             "correct": False,
             "why": "None of them was careless. Each explained everything the "
                    "evidence of his own day held."},
            {"text": "That scientists cannot agree, so nothing about the atom "
                     "is settled",
             "correct": False,
             "why": "A great deal is settled. Each model kept what worked and "
                    "added what the last could not explain."},
            {"text": "That the earlier models were never used again by "
                     "anyone",
             "correct": False,
             "why": "Dalton's is used every day for chemical reactions, more "
                    "than two centuries on."},
            {"text": "That a model is replaced when evidence arrives that it "
                     "cannot account for", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s30",
        "band": "standard",
        "text": "Magnesium ribbon is burned in an open crucible and the white "
                "powder weighs more than the ribbon did. Does that break "
                "Dalton's claim that atoms are not created?",
        "options": [
            {"text": "No — oxygen from the air has joined the magnesium, and "
                     "the crucible was open", "correct": True},
            {"text": "Yes — mass has appeared from nowhere, so atoms must "
                     "have been made",
             "correct": False,
             "why": "The extra mass walked in from the air. Nothing was "
                    "created inside the crucible."},
            {"text": "Yes — the heat has gone into the powder, and heat has "
                     "mass",
             "correct": False,
             "why": "The gain is oxygen atoms, and it can be predicted "
                    "exactly. Heating a sealed sample adds no weighable "
                    "mass."},
            {"text": "No — the balance must simply have been read wrongly",
             "correct": False,
             "why": "The gain is real and repeats every time. Calling it an "
                    "error would miss what actually happened."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s31",
        "band": "standard",
        "text": "A metal bar gets slightly longer when it is heated. What has "
                "happened to its atoms?",
        "options": [
            {"text": "Each atom has expanded and become a little bigger",
             "correct": False,
             "why": "An atom does not change size when it is heated. What "
                    "changes is how much it moves."},
            {"text": "They vibrate more and sit slightly further apart",
             "correct": True},
            {"text": "More atoms have been made, so there is more metal than "
                     "before",
             "correct": False,
             "why": "Heating creates no atoms. The bar ends with exactly as "
                    "many as it started with."},
            {"text": "They have begun turning into atoms of a different "
                     "element",
             "correct": False,
             "why": "Heating never changes an atom's kind, which is what "
                    "alchemy tested to destruction."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-s32",
        "band": "standard",
        "text": "A school microscope runs out at about 0.1 mm, and a student "
                "concludes that atoms must be about 0.1 mm across. What has "
                "gone wrong?",
        "options": [
            {"text": "Nothing — it is a fair estimate from the evidence that "
                     "was available",
             "correct": False,
             "why": "It is not an estimate of the atom at all. An "
                    "instrument's limit measures nothing about what it fails "
                    "to show."},
            {"text": "The student should have used a hand lens, which reaches "
                     "further down",
             "correct": False,
             "why": "A hand lens reaches nowhere near as far as a microscope, "
                    "so it would make the same mistake worse."},
            {"text": "The limit of the instrument has been mistaken for the "
                     "size of the thing", "correct": True},
            {"text": "The limit is really 1 mm, so the estimate should have "
                     "been ten times bigger",
             "correct": False,
             "why": "The figure is right and the reasoning is what fails. A "
                    "different limit would only move a wrong number."},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c2-01-h10",
        "band": "harder",
        "text": "Sulfur and oxygen form one compound in which 32 g of sulfur "
                "joins 32 g of oxygen, and a second in which 32 g of sulfur "
                "joins 48 g of oxygen. Determine the ratio of the two oxygen "
                "masses.",
        "options": [
            {"text": "3 : 2", "correct": False,
             "why": "The right pair of numbers the wrong way round. The "
                    "question asks for the first compound first, so it is 32 "
                    "to 48."},
            {"text": "2 : 3, a simple whole-number ratio", "correct": True},
            {"text": "1 : 2", "correct": False,
             "why": "That would need 64 g of oxygen in the second compound "
                    "rather than 48 g."},
            {"text": "32 : 48, which will not simplify any further",
             "correct": False,
             "why": "Both numbers divide by 16, giving 2 : 3 — and a simple "
                    "whole-number ratio is exactly what Dalton predicts."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h11",
        "band": "harder",
        "text": "Gold leaf is about 0.0001 mm thick and a gold atom is about "
                "0.0000003 mm across. Determine roughly how many atoms thick "
                "the leaf is.",
        "options": [
            {"text": "About 30 atoms", "correct": False,
             "why": "Out by a factor of ten. 0.0001 divided by 0.0000003 "
                    "comes to a little over three hundred."},
            {"text": "About 3000 atoms", "correct": False,
             "why": "Ten times too many. Three thousand atoms would make a "
                    "leaf 0.001 mm thick, which a microscope would show."},
            {"text": "About 300 atoms", "correct": True},
            {"text": "About 3 atoms", "correct": False,
             "why": "Three atoms is under a millionth of a millimetre, far "
                    "too thin for anything you could pick up."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h12",
        "band": "harder",
        "text": "Model A explains three known observations and predicts a "
                "fourth result, which is later confirmed. Model B explains "
                "all four and predicts nothing new. Which is the better "
                "scientific model?",
        "options": [
            {"text": "Model A, because a prediction that comes out right is "
                     "the strongest test a model can pass", "correct": True},
            {"text": "Model B, because explaining more observations is what a "
                     "model is for",
             "correct": False,
             "why": "Explaining what is already known is the easier half. Any "
                    "number of models can be built to fit results already "
                    "in."},
            {"text": "Neither, because a model that is wrong about anything "
                     "is no use",
             "correct": False,
             "why": "Neither has been shown wrong here, and every model in "
                    "use has a boundary somewhere."},
            {"text": "Model B, because a prediction is nothing but a guess "
                     "until somebody has gone and checked it properly",
             "correct": False,
             "why": "It was checked and it came out right, which is exactly "
                    "what makes it more than a guess."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h13",
        "band": "harder",
        "text": "Two students test whether a reaction loses mass. One works "
                "in a sealed flask and one in an open beaker. Explain why "
                "only the sealed result tests Dalton's claim.",
        "options": [
            {"text": "Because the open beaker cools faster, and cooling "
                     "lowers the mass",
             "correct": False,
             "why": "Cooling changes the temperature, not the mass. Nothing "
                    "weighable leaves because of it."},
            {"text": "Because the sealed flask weighs more to begin with, so "
                     "the balance can be trusted to read it accurately",
             "correct": False,
             "why": "A heavier container makes a balance no more accurate. "
                    "The seal matters because it keeps the atoms in."},
            {"text": "Because a reaction carried out in an open beaker is not "
                     "a real chemical reaction once its gases escape",
             "correct": False,
             "why": "It is a real reaction. What it is not is a fair test of "
                    "whether the total mass holds still."},
            {"text": "Because gas can leave or enter an open beaker, so the "
                     "balance is not weighing the same atoms twice",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h14",
        "band": "harder",
        "text": "You want to explain why a gas can be squashed into a smaller "
                "volume. Which model does the job, and why?",
        "options": [
            {"text": "Dalton's, because only his model says what the "
                     "particles are made of",
             "correct": False,
             "why": "Knowing the kinds adds nothing here. Squashing a gas is "
                    "about spacing, which the particle model already had."},
            {"text": "The particle model, because gaps between the particles "
                     "are the whole explanation", "correct": True},
            {"text": "Dalton's, because squashing a gas is a chemical change",
             "correct": False,
             "why": "Squashing a gas makes no new substance, so it is not a "
                    "chemical change at all."},
            {"text": "Neither, because a gas is too disorderly to be modelled",
             "correct": False,
             "why": "Gases were one of the particle model's first successes. "
                    "The disorder is part of what it describes."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h15",
        "band": "harder",
        "text": "Copper oxide always holds 4 g of copper for every 1 g of "
                "oxygen. A student heats 5 g of copper in air and weighs 6 g "
                "of black powder. Suggest what went wrong.",
        "options": [
            {"text": "Some of the copper never reacted, because 5 g of copper "
                     "should give 6.25 g", "correct": True},
            {"text": "Some copper was destroyed by the heat, which is why the "
                     "powder is light",
             "correct": False,
             "why": "Nothing is destroyed. Even if it were, losing copper "
                    "would leave far more than 0.25 g missing."},
            {"text": "The proportion is not really fixed, so 6 g is a "
                     "perfectly good result",
             "correct": False,
             "why": "Every sample ever measured gives the same proportion. A "
                    "result that misses it points at the experiment."},
            {"text": "Oxygen escaped from the black powder as it cooled down",
             "correct": False,
             "why": "The oxygen is locked into the compound. It does not "
                    "drift back out of copper oxide on cooling."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h16",
        "band": "harder",
        "text": "A student says a scientific model is just a guess. Using "
                "Dalton, explain the difference.",
        "options": [
            {"text": "A model is written by a scientist, and a guess is not",
             "correct": False,
             "why": "Who says it changes nothing. Scientists guess too; the "
                    "difference is what the idea is built from."},
            {"text": "A model is true, and a guess might turn out to be "
                     "wrong",
             "correct": False,
             "why": "Two of Dalton's claims were wrong and the model is still "
                    "in use. Being true is not what separates them."},
            {"text": "A model accounts for measurements already made and then "
                     "predicts new ones", "correct": True},
            {"text": "A model cannot be tested at all, so it cannot be a "
                     "guess either",
             "correct": False,
             "why": "The opposite is true. A model that could not be tested "
                    "would be of no use to anybody."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h17",
        "band": "harder",
        "text": "Engineers still fly spacecraft using Newton's laws, although "
                "Einstein's theory replaced them. What does that have in "
                "common with chemists keeping Dalton's model?",
        "options": [
            {"text": "Both were never really replaced, only reworded by "
                     "later scientists",
             "correct": False,
             "why": "Both were genuinely replaced by theories that explain "
                    "more. What survives is their usefulness in a range."},
            {"text": "Both are taught only because the newer ideas are too "
                     "hard for school",
             "correct": False,
             "why": "Working engineers and chemists use them, not just "
                    "schools. They are chosen because they fit the job."},
            {"text": "Both are wrong, and both are used because nothing "
                     "better exists yet",
             "correct": False,
             "why": "Something better exists in each case. The older tool is "
                    "chosen for being simpler and accurate enough."},
            {"text": "Both are kept for the range of problems where they "
                     "still give the right answers", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h18",
        "band": "harder",
        "text": "It is true that atoms are far too small to see, and it is "
                "not one of Dalton's three claims. Explain why it is not.",
        "options": [
            {"text": "Because it turned out to be false as soon as the "
                     "electron microscope was built",
             "correct": False,
             "why": "It is still true of light, which is what the statement "
                    "is about. It is left out because it does no work."},
            {"text": "Because it came from the particle model and does none of "
                     "the explaining", "correct": True},
            {"text": "Because Dalton had no idea how small an atom actually "
                     "is",
             "correct": False,
             "why": "He did not, and that is not the reason. A claim earns "
                    "its place by what it explains."},
            {"text": "Because a claim has to be about chemistry, and size "
                     "belongs to physics",
             "correct": False,
             "why": "Chemistry and physics are not divided like that. Size is "
                    "left out because nothing rests on it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h19",
        "band": "harder",
        "text": "Water always holds 1 g of hydrogen for every 8 g of oxygen. "
                "Calculate the mass of oxygen that combines with 3 g of "
                "hydrogen.",
        "options": [
            {"text": "24 g", "correct": True},
            {"text": "8 g", "correct": False,
             "why": "That is the oxygen for 1 g of hydrogen. Three times the "
                    "hydrogen needs three times the oxygen."},
            {"text": "11 g", "correct": False,
             "why": "That adds 3 and 8. The 8 to 1 is a ratio to scale up, "
                    "not an amount to add on."},
            {"text": "2.7 g", "correct": False,
             "why": "That divides 8 by 3. The oxygen goes up with the "
                    "hydrogen, not down."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h20",
        "band": "harder",
        "text": "The photographs of the 1930s are usually said to have "
                "confirmed Dalton's atoms rather than proved them. Explain "
                "the difference.",
        "options": [
            {"text": "A photograph is not evidence at all, because a machine "
                     "produced it",
             "correct": False,
             "why": "It is evidence, and strong evidence. The point is about "
                    "what any one piece of evidence can settle."},
            {"text": "There is no difference, and the two words mean the same "
                     "thing in science",
             "correct": False,
             "why": "Proving would close the question, and the model went on "
                    "to be given a boundary twice over."},
            {"text": "Evidence can support a model and still leave it open to "
                     "being bounded later", "correct": True},
            {"text": "The photographs showed molecules and not atoms, so "
                     "nothing was settled",
             "correct": False,
             "why": "Individual atoms have been imaged. The word is about "
                    "what evidence does, not about the picture."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h21",
        "band": "harder",
        "text": "A student says the atoms in a hundred-year-old iron gate "
                "have worn out, which is why it is rusty. Evaluate that "
                "claim.",
        "options": [
            {"text": "Correct — an atom has a lifetime, and iron's is about a "
                     "century long",
             "correct": False,
             "why": "Atoms do not age. The iron atoms in that gate are older "
                    "than the Earth."},
            {"text": "Correct, but only for metals that are left outdoors",
             "correct": False,
             "why": "Weather speeds up the reaction, not the wearing out of "
                    "atoms. There is no wearing out to speed up."},
            {"text": "Wrong, because rusting destroys the iron atoms instead "
                     "of wearing them down",
             "correct": False,
             "why": "Nothing is destroyed either. Every iron atom is present "
                    "in the rust."},
            {"text": "Wrong — the iron atoms have joined oxygen to make a new "
                     "substance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h22",
        "band": "harder",
        "text": "A student says that a single atom taken from a block of ice "
                "would feel cold. Evaluate that statement.",
        "options": [
            {"text": "Wrong — temperature is the average kinetic energy of "
                     "many particles, so one atom has no temperature",
             "correct": True},
            {"text": "Right, because the atom has come out of a cold block "
                     "and must be carrying some of that cold along with "
                     "it",
             "correct": False,
             "why": "Cold is not a substance an atom can carry about. "
                    "Temperature belongs to a crowd of particles."},
            {"text": "Right, because every single one of the atoms inside a "
                     "cold object has to be just as cold as the object "
                     "is",
             "correct": False,
             "why": "The object has a temperature because of the average "
                    "across all its particles. No one of them has its own."},
            {"text": "Wrong, because a single atom would in fact be extremely "
                     "hot",
             "correct": False,
             "why": "It is not hot either. One atom has kinetic energy, and "
                    "neither hot nor cold applies to it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h23",
        "band": "harder",
        "text": "Which result, if it had turned up in Dalton's own lifetime, "
                "would have forced him to drop the whole-number-ratio claim?",
        "options": [
            {"text": "A compound of two elements that nobody had ever managed "
                     "to make in a laboratory before now",
             "correct": False,
             "why": "New compounds were being made constantly, and each one "
                    "obeyed the claim."},
            {"text": "Two elements combining in every proportion that anyone "
                     "cared to try, with no gaps", "correct": True},
            {"text": "An element that would not combine with anything at all",
             "correct": False,
             "why": "Such an element sits outside the claim, which says how "
                    "elements combine when they do."},
            {"text": "A compound whose two elements had exactly the same mass",
             "correct": False,
             "why": "Equal masses are allowed. The claim is about the counts "
                    "of atoms joining, not about which is heavier."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h24",
        "band": "harder",
        "text": "Dalton's claim that all atoms of one element are alike is "
                "not true. Suggest why it was still a reasonable claim to "
                "make in 1803.",
        "options": [
            {"text": "Nobody had thought to question it, so it was safe to "
                     "assume",
             "correct": False,
             "why": "It was questioned, and tested against every compound "
                    "that could be weighed. It passed every time."},
            {"text": "He admitted at the time that he could not support it",
             "correct": False,
             "why": "He supported it with mass measurements and said so. It "
                    "was never offered as a guess."},
            {"text": "Every measurement available then came out exactly as it "
                     "predicted", "correct": True},
            {"text": "Atoms were too small to see, so anything at all could "
                     "be claimed about them",
             "correct": False,
             "why": "Not anything. A claim had to account for the masses that "
                    "could be measured, and most possible claims did not."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h25",
        "band": "harder",
        "text": "Iron forms two oxides. In the first, 56 g of iron joins 16 g "
                "of oxygen; in the second, 112 g of iron joins 64 g of "
                "oxygen. Is Dalton's ratio claim obeyed?",
        "options": [
            {"text": "No, because 16 g and 64 g are in the ratio 1 : 4",
             "correct": False,
             "why": "The 64 g goes with twice as much iron. Scale the second "
                    "compound to 56 g of iron and it becomes 32 g."},
            {"text": "No, because the second compound holds twice as much "
                     "iron as the first one does",
             "correct": False,
             "why": "Different masses of iron are no obstacle. Scale the "
                    "second compound to 56 g of iron and its oxygen "
                    "becomes 32 g."},
            {"text": "It cannot be decided without knowing the mass of one "
                     "iron atom",
             "correct": False,
             "why": "No atomic mass is needed at all. Scaling both compounds "
                    "to the same mass of iron is enough."},
            {"text": "Yes — scaled to the same 56 g of iron, the oxygen "
                     "masses are 16 g and 32 g", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h26",
        "band": "harder",
        "text": "Electricity splits water into hydrogen and oxygen. Explain "
                "what that shows about the smallest particle of water.",
        "options": [
            {"text": "It is not an atom, because it holds more than one kind "
                     "of atom", "correct": True},
            {"text": "It is an atom, and the electricity has split the atom "
                     "itself",
             "correct": False,
             "why": "Electricity separates atoms from each other. Splitting "
                    "an atom is not something a battery can do."},
            {"text": "It is an atom, because water is a single pure substance",
             "correct": False,
             "why": "Being one substance does not make its particles atoms. "
                    "Water's are built from two kinds."},
            {"text": "It shows that water is a mixture of two gases stirred "
                     "together",
             "correct": False,
             "why": "The gases have to be released by a reaction. A mixture "
                    "could be separated without one."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h27",
        "band": "harder",
        "text": "Two of Dalton's claims are wrong and the model is still "
                "used. Suggest what would have to be true for a wrong model "
                "to be genuinely useless.",
        "options": [
            {"text": "It would have to be wrong about more than half of its "
                     "claims",
             "correct": False,
             "why": "Counting claims settles nothing. What matters is whether "
                    "the wrong ones touch the job it is doing."},
            {"text": "Its errors would have to reach the very things it is "
                     "used to explain", "correct": True},
            {"text": "It would have to have been written down a very long "
                     "time ago",
             "correct": False,
             "why": "Age is not a fault. Dalton's is two centuries old and "
                    "still gives the right answers for reactions."},
            {"text": "It would have to be harder to use than the model that "
                     "replaced it",
             "correct": False,
             "why": "Being awkward would make it unpopular rather than "
                    "useless. Usefulness is about the answers coming out "
                    "right."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h28",
        "band": "harder",
        "text": "24 g of magnesium combines with 16 g of oxygen. Calculate "
                "the mass of magnesium oxide formed, and state which claim "
                "you used.",
        "options": [
            {"text": "24 g, because the oxygen escapes again as a gas "
                     "afterwards",
             "correct": False,
             "why": "The oxygen is part of the compound now. Nothing leaves "
                    "once it has joined."},
            {"text": "8 g, the difference between the two masses",
             "correct": False,
             "why": "Combining adds the masses together. Subtracting would "
                    "mean 32 g of atoms going nowhere."},
            {"text": "40 g, using the claim that atoms are neither created "
                     "nor destroyed", "correct": True},
            {"text": "40 g, using the claim that elements combine in "
                     "whole-number ratios",
             "correct": False,
             "why": "The total is right and the reason is not. What "
                    "guarantees the total is atoms being neither made nor "
                    "destroyed."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h29",
        "band": "harder",
        "text": "Which is the better evidence that the atoms of one element "
                "are alike: the fixed proportion of hydrogen to oxygen in "
                "water, or the failure of alchemy?",
        "options": [
            {"text": "The failure of alchemy, because fifteen centuries is a "
                     "great deal of evidence",
             "correct": False,
             "why": "The amount of evidence is not the issue. It is strong "
                    "evidence for a different claim."},
            {"text": "Neither, because both are observations rather than "
                     "experiments",
             "correct": False,
             "why": "Both were measured and repeated. A careful observation "
                    "is evidence."},
            {"text": "Both equally, because Dalton's three claims cannot be "
                     "separated from each other",
             "correct": False,
             "why": "They were separated in this lesson, one at a time. Each "
                    "observation rests on particular claims."},
            {"text": "The fixed proportion, because alchemy's failure is "
                     "about kinds not changing", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h30",
        "band": "harder",
        "text": "Dalton could weigh substances but never a single atom. "
                "Explain how he could still claim that atoms of different "
                "elements have different masses.",
        "options": [
            {"text": "From the fixed mass proportions in compounds, which "
                     "compare the atoms with each other", "correct": True},
            {"text": "By weighing out the very smallest speck of an element "
                     "that his balance was able to detect",
             "correct": False,
             "why": "The smallest weighable speck still holds more atoms than "
                    "anyone could count. No balance came close."},
            {"text": "By counting all of the atoms in a weighed sample and "
                     "then dividing the mass between them",
             "correct": False,
             "why": "Nobody could count atoms then. The comparison came from "
                    "proportions rather than from counting."},
            {"text": "He could not, so that claim was pure guesswork on his "
                     "part",
             "correct": False,
             "why": "It was supported by measurement. Comparing masses does "
                    "not require weighing one atom."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h31",
        "band": "harder",
        "text": "A student says that dissolving copper in acid destroys the "
                "copper, because the blue solution is not copper. Evaluate "
                "that claim.",
        "options": [
            {"text": "Right, because there is no copper to be seen anywhere in "
                     "the blue solution",
             "correct": False,
             "why": "Not being visible is not being destroyed. The copper can "
                    "be recovered from the solution again."},
            {"text": "Wrong — the copper atoms are all still there, joined to "
                     "something else", "correct": True},
            {"text": "Right, because the acid has turned the copper into a "
                     "different element",
             "correct": False,
             "why": "No reaction changes an element. The blue comes from "
                    "copper inside a new compound."},
            {"text": "Wrong, because the copper is unchanged and simply "
                     "hidden in the liquid",
             "correct": False,
             "why": "It has genuinely reacted and is part of a new substance. "
                    "What it has not done is stop existing."},
        ],
        "figure": None,
    },
    {
        "id": "c2-01-h32",
        "band": "harder",
        "text": "Put these in order from largest to smallest: an electron, a "
                "copper atom, and a grain of copper just visible under a "
                "school microscope.",
        "options": [
            {"text": "Grain, then electron, then atom", "correct": False,
             "why": "The electron came out of the atom, so it is the smaller "
                    "of those two."},
            {"text": "Atom, then grain, then electron", "correct": False,
             "why": "The grain is visible under a microscope, which makes it "
                    "millions of atoms across."},
            {"text": "Grain, then atom, then electron", "correct": True},
            {"text": "Electron, then grain, then atom", "correct": False,
             "why": "The electron is the smallest of the three rather than "
                    "the largest."},
        ],
        "figure": None,
    },
]
