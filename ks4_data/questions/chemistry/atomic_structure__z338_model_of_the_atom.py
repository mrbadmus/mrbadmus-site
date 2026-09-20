"""Chemistry · Atomic structure and the periodic table — the development of the
model of the atom · the MRB-338 expansion.

Fifty-two rows on how the model changed and on the evidence that changed it:
Dalton's indivisible sphere, Thomson's electron and his plum pudding, the
alpha-scattering experiment Geiger and Marsden ran for Rutherford, Bohr's fixed
shells, and Chadwick's neutron. The weight falls on reading an OBSERVATION into
a CONCLUSION — most particles straight through means empty space, a very few
turned back means a tiny dense nucleus — and on the apparatus decisions that
make the experiment work at all: a foil only atoms thick, a vacuum, a detector
that can be moved to any angle.

Radioactivity is the physics half of this topic id and appears nowhere here:
alpha particles are the projectile in one experiment, nothing more.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-model-of-the-atom-e05",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the observation made by most of the alpha particles "
                "fired at the thin gold foil.",
        "options": [
            "They passed straight through the foil",
            "They bounced back towards the source",
            "They were absorbed and stopped inside the foil",
            "They were deflected sideways through large angles",
        ],
        "correct_index": 0,
        "why": "The great majority went straight through, which is what "
               "showed an atom to be mostly empty space.",
    },
    {
        "id": "ks4-model-of-the-atom-e06",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the charge carried by an alpha particle.",
        "options": [
            "Negative",
            "Positive",
            "Neutral",
            "It changes as the particle travels",
        ],
        "correct_index": 1,
        "why": "Alpha particles are positively charged, which is why they are "
               "repelled by the positive nucleus of an atom.",
    },
    {
        "id": "ks4-model-of-the-atom-e07",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the scientist who discovered the neutron in 1932.",
        "options": [
            "John Dalton",
            "J J Thomson",
            "James Chadwick",
            "Ernest Rutherford",
        ],
        "correct_index": 2,
        "why": "Chadwick identified the neutron about twenty years after the "
               "nucleus itself had been proposed.",
    },
    {
        "id": "ks4-model-of-the-atom-e08",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the central part of the atom in Rutherford's model.",
        "options": [
            "The inner shell",
            "The outer shell",
            "The electron cloud",
            "The nucleus",
        ],
        "correct_index": 3,
        "why": "Rutherford placed the positive charge and nearly all of the "
               "mass into a tiny central nucleus.",
    },
    {
        "id": "ks4-model-of-the-atom-e09",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what Dalton believed about whether an atom could be "
                "split.",
        "options": [
            "That it could not be split at all",
            "That it could be split only by a very strong electric current",
            "That it could be split into a nucleus and some electrons",
            "That it could be split by heating it strongly enough",
        ],
        "correct_index": 0,
        "why": "Dalton's atoms were indivisible: the idea of anything smaller "
               "inside an atom came only with the electron.",
    },
    {
        "id": "ks4-model-of-the-atom-e10",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the approximate radius of an atom in nanometres.",
        "options": [
            "0.001 nm",
            "0.1 nm",
            "1 nm",
            "10 nm",
        ],
        "correct_index": 1,
        "why": "An atomic radius of about a ten-thousand-millionth of a metre "
               "is a tenth of a nanometre.",
    },
    {
        "id": "ks4-model-of-the-atom-e11",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two scientists who carried out the alpha-scattering "
                "experiment for Rutherford.",
        "options": [
            "Dalton and Thomson",
            "Bohr and Chadwick",
            "Geiger and Marsden",
            "Moseley and Newlands",
        ],
        "correct_index": 2,
        "why": "Hans Geiger and Ernest Marsden ran the scattering experiment "
               "whose results Rutherford then interpreted.",
    },
    {
        "id": "ks4-model-of-the-atom-e12",
        "subtopic_slug": "model-of-the-atom",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where almost all of an atom's mass is found according "
                "to the nuclear model.",
        "options": [
            "Spread evenly through the whole atom",
            "In the empty space between the shells",
            "In the electron shells",
            "In the nucleus",
        ],
        "correct_index": 3,
        "why": "The protons and neutrons of the nucleus carry nearly all the "
               "mass, since an electron's mass is negligible.",
    },
    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-model-of-the-atom-s05",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what the very small number of alpha particles that "
                "came almost straight back showed.",
        "options": [
            "That the atom contains a tiny region of concentrated positive "
            "charge and mass",
            "That the foil as a whole carried a strong negative charge, "
            "which pulled the positive particles round and sent them "
            "back the way they came",
            "That alpha particles lose energy in a metal",
            "That the electrons are heavy enough to turn a particle",
        ],
        "correct_index": 0,
        "why": "Only a dense concentration of positive charge could repel a "
               "fast positive particle through nearly 180 degrees.",
    },
    {
        "id": "ks4-model-of-the-atom-s06",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the discovery of the electron meant Dalton's "
                "model had to be replaced.",
        "options": [
            "It showed that the atoms of one element differ in size from "
            "one another, which is something Dalton had denied outright "
            "in his own work",
            "It showed the atom has parts inside it, so it cannot be an "
            "indivisible sphere",
            "It showed that atoms can be destroyed in a reaction",
            "It showed the atom is larger than Dalton drew",
        ],
        "correct_index": 1,
        "why": "A particle found inside the atom proves the atom has internal "
               "structure, which an indivisible sphere cannot have.",
    },
    {
        "id": "ks4-model-of-the-atom-s07",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the alpha-scattering apparatus had to be "
                "evacuated of air.",
        "options": [
            "Because air would cool the foil and rearrange its atoms",
            "Because air would tarnish the gold surface",
            "Because air molecules would scatter the alpha particles before "
            "they reached the foil",
            "Because air would carry the particles and speed them up",
        ],
        "correct_index": 2,
        "why": "Any scattering by air would be mixed in with the scattering "
               "by the foil, so the results could not be interpreted.",
    },
    {
        "id": "ks4-model-of-the-atom-s08",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what Thomson's model said an atom was made of.",
        "options": [
            "A tiny nucleus with electrons in fixed shells",
            "A cloud of electrons with all of the positive charge "
            "gathered into a single point at the very centre of that "
            "cloud",
            "A solid sphere of one material that could not be broken into "
            "anything smaller at all",
            "A ball of positive charge with electrons spread through it",
        ],
        "correct_index": 3,
        "why": "The plum pudding model had the positive charge spread across "
               "the whole atom with the electrons embedded in it.",
    },
    {
        "id": "ks4-model-of-the-atom-s09",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why gold was chosen for the foil in the scattering "
                "experiment.",
        "options": [
            "Gold is so malleable that it can be beaten into a sheet only a "
            "few atoms thick",
            "Gold is the densest metal, so it stops most",
            "Gold is so unreactive that the alpha particles cannot bond "
            "to any of its atoms as they travel through the sheet of "
            "foil",
            "Gold conducts, so it carries the charge away",
        ],
        "correct_index": 0,
        "why": "An extremely thin sheet means most particles meet only one "
               "layer of atoms, so each deflection can be interpreted.",
    },
    {
        "id": "ks4-model-of-the-atom-s10",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the detector in the scattering experiment could "
                "be moved to different angles.",
        "options": [
            "So that the detector stayed out of the direct beam",
            "So that the number of particles arriving at each angle could be "
            "counted",
            "So that the foil could be lit from several directions while the "
            "readings were being taken",
            "So that the whole experiment could be repeated with the "
            "particle source set at a different distance from the foil "
            "each time",
        ],
        "correct_index": 1,
        "why": "The pattern of counts against angle is the actual result: it "
               "is what shows most go through and very few come back.",
    },
    {
        "id": "ks4-model-of-the-atom-s11",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why Chadwick's neutron accounted for the existence "
                "of isotopes.",
        "options": [
            "Neutrons move between atoms of a sample, so the mass of any one "
            "atom keeps changing over time",
            "Atoms of one element can hold different numbers of protons, so "
            "their masses come out different from each other",
            "Atoms of one element can hold different numbers of neutrons, "
            "which changes the mass but not the element",
            "Neutrons carry a charge that cancels part of the proton charge "
            "and so alters the measured mass",
        ],
        "correct_index": 2,
        "why": "A neutral particle in the nucleus can vary in number without "
               "changing the element, which is exactly what an isotope is.",
    },
    {
        "id": "ks4-model-of-the-atom-s12",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what Bohr's model added to Rutherford's nuclear model.",
        "options": [
            "A neutral particle sharing the nucleus with the protons",
            "The idea that an atom cannot be divided into smaller pieces by "
            "any means at all",
            "A positive charge spread across the whole of the atom instead of "
            "gathered at its centre",
            "Electrons in fixed shells at set distances from the nucleus",
        ],
        "correct_index": 3,
        "why": "Rutherford's model placed electrons somewhere outside the "
               "nucleus; Bohr fixed them into definite energy levels.",
    },
    {
        "id": "ks4-model-of-the-atom-s13",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate how many atoms of radius 1 x 10^-10 m would fit "
                "side by side across a 1 mm gap.",
        "options": [
            "5 x 10^6 atoms",
            "1 x 10^7 atoms",
            "5 x 10^7 atoms",
            "1 x 10^10 atoms",
        ],
        "correct_index": 0,
        "why": "An atom of radius 1 x 10^-10 m is 2 x 10^-10 m across, and "
               "1 x 10^-3 m divided by 2 x 10^-10 m gives 5 x 10^6.",
    },
    {
        "id": "ks4-model-of-the-atom-s14",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the nucleus must carry a positive charge rather "
                "than a negative one.",
        "options": [
            "Because a positive charge is needed to hold the neutrons in "
            "place beside the protons in the nucleus",
            "Because positive alpha particles were repelled by it as they "
            "approached",
            "Because the electrons around the nucleus are negative, and "
            "any two charges of the same kind must attract one another "
            "strongly",
            "Because a negative nucleus would charge the atom",
        ],
        "correct_index": 1,
        "why": "Like charges repel, so a positive particle turned back by the "
               "centre of an atom shows that centre to be positive.",
    },
    {
        "id": "ks4-model-of-the-atom-s15",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what is meant by saying that a scientific model is "
                "the current best explanation.",
        "options": [
            "It has been proved correct beyond any possibility of change",
            "It is the explanation that the largest number of scientists "
            "happen to find easiest to teach",
            "It fits the evidence available now and may be revised if new "
            "evidence contradicts it",
            "It is a simplified picture that was never meant to match any "
            "real measurement at all",
        ],
        "correct_index": 2,
        "why": "A model earns its place by explaining the evidence, and it "
               "gives way when an experiment produces evidence it cannot "
               "explain.",
    },
    {
        "id": "ks4-model-of-the-atom-s16",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Place these in the order in which they were proposed: "
                "nuclear model, plum pudding model, solid sphere, shell "
                "model.",
        "options": [
            "Shell, solid sphere, plum pudding, nuclear",
            "Plum pudding, solid sphere, shell, nuclear",
            "Solid sphere, nuclear, plum pudding, shell",
            "Solid sphere, plum pudding, nuclear, shell",
        ],
        "correct_index": 3,
        "why": "Dalton came first, then Thomson's plum pudding, then "
               "Rutherford's nucleus, then Bohr's shells.",
    },
    {
        "id": "ks4-model-of-the-atom-s17",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the electrons in the foil could not have caused "
                "the large deflections that were seen.",
        "options": [
            "Electrons have far too little mass to turn a much heavier alpha "
            "particle aside",
            "Electrons carry no charge of their own, so they cannot push "
            "a charged particle off its path in any direction whatever",
            "Electrons sit inside the nucleus, out of reach",
            "Electrons move too quickly to be in the way",
        ],
        "correct_index": 0,
        "why": "An alpha particle is thousands of times more massive than an "
               "electron, so a collision with one barely changes its path.",
    },
    {
        "id": "ks4-model-of-the-atom-s18",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what Dalton said about the atoms of two different "
                "elements.",
        "options": [
            "That they were identical to each other in every way",
            "That they were spheres of different sizes and masses",
            "That they held different numbers of electrons inside them",
            "That they could be changed into one another by a chemical "
            "reaction",
        ],
        "correct_index": 1,
        "why": "Dalton distinguished elements by the size and mass of their "
               "spheres, having no knowledge of anything inside an atom.",
    },
    {
        "id": "ks4-model-of-the-atom-s19",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nucleus is drawn 2 mm across in a scale diagram. "
                "Determine how wide the whole atom should be drawn.",
        "options": [
            "2 cm",
            "20 cm",
            "20 m",
            "2 m",
        ],
        "correct_index": 2,
        "why": "The atom is about ten thousand times wider than the nucleus, "
               "so 2 mm scales up to 20 000 mm.",
    },
    {
        "id": "ks4-model-of-the-atom-s20",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why Thomson's model could not account for particles "
                "being turned back by a foil.",
        "options": [
            "Its charge sits at the centre and repels all",
            "Its electrons are fixed, so nothing can move",
            "Its atoms are packed too tightly to be entered",
            "Its positive charge is spread thinly, so nowhere in the atom "
            "repels strongly enough",
        ],
        "correct_index": 3,
        "why": "A concentrated charge is needed for a strong repulsion, and "
               "the plum pudding model has none anywhere.",
    },
    {
        "id": "ks4-model-of-the-atom-s21",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which discovery showed that an atom is not the "
                "smallest particle of matter.",
        "options": [
            "The electron",
            "The neutron",
            "The nucleus",
            "The noble gases",
        ],
        "correct_index": 0,
        "why": "The electron was the first particle found to be smaller than "
               "an atom and present inside one.",
    },
    {
        "id": "ks4-model-of-the-atom-s22",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the mass of an atom was found to be greater than "
                "the mass of its protons alone.",
        "options": [
            "The electrons in the shells make up the missing part of the "
            "total mass",
            "The nucleus also contains neutrons, and each has about the same "
            "mass as a proton",
            "A proton gains mass when it is packed together with others in a "
            "nucleus of an atom",
            "The empty space inside the atom has a small mass of its own that "
            "adds to the total",
        ],
        "correct_index": 1,
        "why": "Neutrons each have a relative mass of 1, so they account for "
               "the mass a proton count leaves unexplained.",
    },
    {
        "id": "ks4-model-of-the-atom-s23",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the nuclear model accounts for most alpha "
                "particles passing straight through a metal foil.",
        "options": [
            "Most atoms in a metal foil hold no nucleus",
            "Most alpha particles travel too fast to be affected",
            "Most of each atom is empty space, so most particles meet nothing "
            "on the way through",
            "Most alpha particles lose charge on entering",
        ],
        "correct_index": 2,
        "why": "A tiny nucleus in a large atom means a particle aimed at "
               "random will almost always miss it.",
    },
    {
        "id": "ks4-model-of-the-atom-s24",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a single atom cannot be seen using a light "
                "microscope.",
        "options": [
            "An atom is colourless, so no light is reflected from it at all",
            "An atom moves far too quickly to be brought into focus",
            "An atom is destroyed by the light shone onto it",
            "An atom is far smaller than the wavelength of visible light",
        ],
        "correct_index": 3,
        "why": "Light cannot resolve anything much smaller than its own "
               "wavelength, and an atom is thousands of times smaller than "
               "that.",
    },
    {
        "id": "ks4-model-of-the-atom-s25",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a new model of the atom was accepted only after "
                "other scientists had examined the work.",
        "options": [
            "Because a result has to be checked and repeated by others before "
            "it is relied on",
            "Because the scientist who first proposed a model was not "
            "permitted to publish any part of the work until others had",
            "Because a model has to be agreed by a vote",
            "Because a model waits on every scientist",
        ],
        "correct_index": 0,
        "why": "Evidence is only trusted once independent workers can "
               "reproduce it, which is what scrutiny by others provides.",
    },
    {
        "id": "ks4-model-of-the-atom-s26",
        "subtopic_slug": "model-of-the-atom",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare where Thomson and Rutherford each placed the "
                "positive charge in an atom.",
        "options": [
            "Thomson used a nucleus; Rutherford spread it",
            "Thomson spread it through the atom; Rutherford concentrated it "
            "in a tiny nucleus",
            "Both of them placed the charge in a nucleus, but Rutherford "
            "made that nucleus a good deal larger than Thomson had done",
            "Neither of them gave the atom a positive charge",
        ],
        "correct_index": 1,
        "why": "The move from spread-out to concentrated positive charge is "
               "exactly what the scattering results forced.",
    },
    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-model-of-the-atom-h05",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest what would have been concluded if every alpha "
                "particle had passed straight through the foil undeflected.",
        "options": [
            "That the alpha particles carried no charge and so could not be "
            "affected by anything in the foil",
            "That the atom has a nucleus much larger than the one Rutherford "
            "went on to propose from the results",
            "That the atom holds no concentrated charge anywhere inside it",
            "That the foil used in the experiment had been made from a "
            "material containing no atoms at all",
        ],
        "correct_index": 2,
        "why": "Deflection is the evidence for a concentrated charge, so its "
               "complete absence would be evidence against one.",
    },
    {
        "id": "ks4-model-of-the-atom-h06",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the number of particles deflected through large "
                "angles was a more useful result than the number passing "
                "straight through.",
        "options": [
            "Because a large count is always easier to measure accurately "
            "than a small count is in any experiment",
            "Because the deflected particles were the only ones that the "
            "movable detector was able to register at all",
            "Because particles going straight through had not entered any of "
            "the atoms of the foil and so carried no information",
            "Because the plum pudding model predicted the straight-through "
            "result too, and only the deflections told the models apart",
        ],
        "correct_index": 3,
        "why": "A result both models predict cannot decide between them; the "
               "large deflections were predicted by only one.",
    },
    {
        "id": "ks4-model-of-the-atom-h07",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the nucleus was discovered because the alpha "
                "particles hit it. Explain why this is not accurate.",
        "options": [
            "The particles were repelled by the nucleus without touching it",
            "The particles were attracted into the nucleus and absorbed there "
            "before they could reach any detector",
            "The particles struck the electrons rather than the nucleus "
            "itself, and it was those collisions that the movable "
            "detector counted",
            "The particles passed through the nucleus and slowed",
        ],
        "correct_index": 0,
        "why": "Two positive charges repel at a distance, so the deflection "
               "happens as the particle approaches rather than on contact.",
    },
    {
        "id": "ks4-model-of-the-atom-h08",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict how the results would change if the foil were "
                "replaced by one of the same thickness made from a metal of "
                "much lower atomic number.",
        "options": [
            "No particle would be deflected, because only heavy atoms have a "
            "nucleus able to repel one",
            "Fewer particles would be deflected through large angles, because "
            "each nucleus carries less positive charge",
            "Every particle would be turned back, because a smaller atom "
            "presents a more crowded target to the beam",
            "The particles would arrive at the detector more slowly, because "
            "a lighter metal slows them as they pass",
        ],
        "correct_index": 1,
        "why": "A smaller positive charge on the nucleus gives a weaker "
               "repulsion, so fewer particles are turned through large "
               "angles.",
    },
    {
        "id": "ks4-model-of-the-atom-h09",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what Dalton and Bohr each said about the inside of "
                "an atom.",
        "options": [
            "Both described a nucleus and gave it a charge",
            "Dalton placed the electrons in shells, while Bohr said the "
            "atom had no internal structure that was worth describing",
            "Dalton said there was nothing inside; Bohr placed electrons in "
            "fixed energy levels",
            "Both called the atom a solid positive sphere",
        ],
        "correct_index": 2,
        "why": "A century of evidence separates an atom with no interior from "
               "one with electrons in defined energy levels.",
    },
    {
        "id": "ks4-model-of-the-atom-h10",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a model that has been replaced can still be "
                "described as good science.",
        "options": [
            "Because a replaced model is still used today in any case "
            "where the newer one turns out to be too complicated to "
            "apply",
            "Because its author was right about later things",
            "Because every model is equally true, and the choice between two "
            "of them is only a matter of taste",
            "Because it explained the evidence that existed when it was made",
        ],
        "correct_index": 3,
        "why": "Science judges a model by how well it accounts for the "
               "available evidence, not by whether it lasted for ever.",
    },
    {
        "id": "ks4-model-of-the-atom-h11",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how many times larger an atomic radius of "
                "1 x 10^-10 m is than a nuclear radius of 2 x 10^-15 m.",
        "options": [
            "5 x 10^4 times",
            "2 x 10^4 times",
            "2 x 10^5 times",
            "5 x 10^5 times",
        ],
        "correct_index": 0,
        "why": "Dividing 1 x 10^-10 by 2 x 10^-15 gives 0.5 x 10^5, which is "
               "5 x 10^4.",
    },
    {
        "id": "ks4-model-of-the-atom-h12",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the neutron was found about twenty years after "
                "the nucleus itself.",
        "options": [
            "Because a neutron is far smaller than a proton",
            "Because a neutron has no charge, so it is not deflected by "
            "electric or magnetic fields",
            "Because the early metals held no neutrons",
            "Because a neutron forms only once struck",
        ],
        "correct_index": 1,
        "why": "The techniques of the day detected particles by how fields "
               "bent their paths, and a neutral particle is not bent at all.",
    },
    {
        "id": "ks4-model-of-the-atom-h13",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims the plum pudding model was abandoned "
                "because nobody could picture it. Evaluate this claim.",
        "options": [
            "Sound, because a model hard to draw falls out of use",
            "Sound, because Thomson described it poorly",
            "Unsound, because it was abandoned when an experiment gave a "
            "result it could not explain",
            "Unsound, because the model was never abandoned",
        ],
        "correct_index": 2,
        "why": "Models are replaced by evidence, and the large-angle "
               "deflections are the evidence that replaced this one.",
    },
    {
        "id": "ks4-model-of-the-atom-h14",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce what would be observed if a thick block of gold "
                "replaced the foil.",
        "options": [
            "The particles would pass through more easily",
            "Exactly the same pattern would be seen again",
            "All the particles would come straight back out",
            "Almost no particles would reach the detector, because each would "
            "meet many atoms in turn",
        ],
        "correct_index": 3,
        "why": "Repeated deflections in a thick sample scatter the beam in "
               "all directions, so no interpretable pattern survives.",
    },
    {
        "id": "ks4-model-of-the-atom-h15",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the nuclear model places nearly all the mass in "
                "a region that occupies almost none of the volume.",
        "options": [
            "Because protons and neutrons are dense and are packed into a "
            "very small space",
            "Because the electrons are spread so widely that their own mass "
            "cancels out across the atom",
            "Because the empty space in an atom has a negative mass which is "
            "subtracted from the total",
            "Because mass and volume are the same quantity measured in two "
            "different sets of units",
        ],
        "correct_index": 0,
        "why": "Mass and volume are independent: a small region can hold "
               "nearly all of an atom's mass if what is in it is dense "
               "enough.",
    },
    {
        "id": "ks4-model-of-the-atom-h16",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why Rutherford's team counted particles at many "
                "angles rather than at one.",
        "options": [
            "Because their detector faced one direction",
            "Because a full pattern of counts against angle is needed to test "
            "a prediction properly",
            "Because the foil scattered to a new angle each time",
            "Because the particle source drifted as time passed",
        ],
        "correct_index": 1,
        "why": "The models differ in the shape of the angle distribution, so "
               "only readings across the whole range can distinguish them.",
    },
    {
        "id": "ks4-model-of-the-atom-h17",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce which model is supported by the observation that an "
                "atom emits light at only certain fixed energies.",
        "options": [
            "Dalton's solid sphere",
            "Thomson's plum pudding",
            "Bohr's shell model",
            "Rutherford's nuclear model",
        ],
        "correct_index": 2,
        "why": "Fixed emission energies mean electrons can occupy only "
               "certain energy levels, which is what Bohr's shells provide.",
    },
    {
        "id": "ks4-model-of-the-atom-h18",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that Rutherford discovered the electron. "
                "Explain the error.",
        "options": [
            "The electron was found by Dalton; Rutherford's work revealed the "
            "sizes of different atoms",
            "The electron was found by Chadwick; Rutherford's work revealed "
            "the neutron inside the nucleus",
            "The electron was found by Bohr; Rutherford's work revealed the "
            "shells the electrons occupy",
            "The electron was found by Thomson; Rutherford's work revealed "
            "the nucleus",
        ],
        "correct_index": 3,
        "why": "Thomson's cathode-ray work identified the electron, and "
               "Rutherford's scattering results identified the nucleus.",
    },
    {
        "id": "ks4-model-of-the-atom-h19",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an alpha particle aimed directly at a nucleus "
                "slows down before it turns back.",
        "options": [
            "The repulsion between two positive charges opposes its motion as "
            "it closes in",
            "The nucleus grips the particle briefly and then releases it "
            "again in the opposite direction",
            "The electrons it has passed pull it backwards",
            "The particle loses its charge steadily as it travels "
            "through the foil, so less and less force is left available "
            "to it",
        ],
        "correct_index": 0,
        "why": "A repulsive force acting against the direction of travel "
               "slows the particle until it stops and is pushed back out.",
    },
    {
        "id": "ks4-model-of-the-atom-h20",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that Dalton's model is of no value now "
                "that the nuclear model exists.",
        "options": [
            "Sound, because a superseded model has no remaining use in any "
            "part of chemistry as it is taught now",
            "Unsound, because treating atoms as indivisible spheres still "
            "works for balancing equations and counting atoms",
            "Sound, because Dalton's model was shown by experiment to have "
            "been wrong about every claim that it made",
            "Unsound, because Dalton's model is still the most accurate "
            "description of an atom's internal structure",
        ],
        "correct_index": 1,
        "why": "A simpler model remains useful where its simplification does "
               "not matter, as in the conservation of atoms in a reaction.",
    },
    {
        "id": "ks4-model-of-the-atom-h21",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the fraction of an atom's radius taken up by a "
                "nucleus whose radius is one ten-thousandth of it.",
        "options": [
            "1%",
            "0.1%",
            "0.01%",
            "10%",
        ],
        "correct_index": 2,
        "why": "One ten-thousandth expressed as a percentage is "
               "1 / 10 000 x 100, which is 0.01%.",
    },
    {
        "id": "ks4-model-of-the-atom-h22",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the scattering experiment could not have been "
                "performed in 1803.",
        "options": [
            "Scientists then could not experiment on metals",
            "The idea that matter is built out of atoms had not yet been "
            "put forward by anybody working in science at that time",
            "Gold could not be beaten into a thin sheet until machinery of a "
            "much later century was invented",
            "No source of fast positive particles and no way of detecting "
            "them existed then",
        ],
        "correct_index": 3,
        "why": "The experiment depends on apparatus that came only after the "
               "discoveries of the end of that century.",
    },
    {
        "id": "ks4-model-of-the-atom-h23",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of particles deflected slightly with the "
                "number turned back through nearly 180 degrees.",
        "options": [
            "Far more were deflected slightly than were turned right back",
            "Far more were turned right back, because a head-on approach is "
            "the most likely one for a particle to make",
            "The two numbers were about equal, since a particle is as likely "
            "to pass a nucleus closely as distantly",
            "Neither happened in any measurable number during the course of "
            "the whole experiment",
        ],
        "correct_index": 0,
        "why": "A near-miss is far more likely than a head-on approach to "
               "something as small as a nucleus.",
    },
    {
        "id": "ks4-model-of-the-atom-h24",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce what the scattering results showed about how much of "
                "an atom is occupied by matter.",
        "options": [
            "All of it, since a particle was deflected wherever it happened "
            "to enter the foil at the front",
            "Almost none of it, since almost nothing obstructed the beam",
            "About half of it, since roughly half of the particles were "
            "deflected away from their original path",
            "None of it, since the beam passed through the foil without any "
            "particle being affected at all",
        ],
        "correct_index": 1,
        "why": "An unobstructed beam means the matter in an atom occupies a "
               "tiny fraction of its volume.",
    },
    {
        "id": "ks4-model-of-the-atom-h25",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the modern model still describes the electron "
                "arrangement using shells even though better descriptions "
                "exist.",
        "options": [
            "Because shells are the only arrangement that a nucleus of "
            "protons and neutrons is able to hold in place",
            "Because no better description has been proposed",
            "Because shells predict bonding and group behaviour well enough "
            "for this course",
            "Because every one of the more detailed descriptions was "
            "shown by experiment to be wrong soon after it was published",
        ],
        "correct_index": 2,
        "why": "A model is chosen to fit its purpose, and shells account for "
               "groups, ion charges and bonding correctly.",
    },
    {
        "id": "ks4-model-of-the-atom-h26",
        "subtopic_slug": "model-of-the-atom",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Deduce which of Dalton's claims survives in the modern "
                "model of chemical reactions.",
        "options": [
            "That an atom of one element can be turned into an atom of "
            "another by a chemical reaction",
            "That an atom cannot be divided into anything smaller than itself",
            "That the atoms of one element are spheres of a single fixed mass "
            "shared by every one of them",
            "That atoms are neither created nor destroyed when substances "
            "react",
        ],
        "correct_index": 3,
        "why": "Conservation of atoms is why equations balance, and it is the "
               "part of Dalton's work that the modern model keeps.",
    },
]
