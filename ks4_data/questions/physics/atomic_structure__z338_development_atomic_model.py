"""Physics · Atomic structure — the MRB-338 expansion of
`development-atomic-model`.

One leaf only: AQA 8463 §6.4.1.3 — the solid sphere model, Thomson's cathode
rays and the electron, the plum pudding model, the Geiger–Marsden alpha
scattering experiment and the three observations it produced, Rutherford's
nuclear model, Bohr's energy levels and Chadwick's neutron, and the way a model
changes when the evidence changes. The original twelve rows in
`atomic_structure__a.py` take the pre-electron model, who found the electron,
the ordering of the four models, Chadwick's particle, the one feature the two
models agree on, the lower-atomic-number prediction, the +2 charge, the need
for many observations, the thin foil, the Thomson evaluation, size against
charge, and the fame-versus-evidence error; this file takes what they leave —
what the cathode-ray evidence actually showed, what each of the three
scattering observations separately establishes, the vacuum, the choice of gold,
the discrete line spectra behind Bohr, the alpha-to-electron mass ratio, what
the neutron explained, and the nature-of-science reasoning that a model fitting
today's evidence may still be replaced tomorrow.

The weight follows the CONTENT. `easier` stays at eight: recall here is four
models, four names and two pieces of apparatus, and a ninth recall question is
the same question wearing a different verb. The demand lives in `standard` and
`harder`, where one observation has to be turned into one conclusion and no
more than that, or two models compared on a single feature — so that is where
the twenty-two-row bands sit.

⚠️ The original `s02` already predicts the effect of a SMALLER atomic number on
the deflected fraction, so no row here asks the same prediction for a larger
one: that is the same task with the sign flipped (brief §3). Every wrong option
carries its own FALSE reason at the key's level of detail (§9.2/§9.9).
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The evidence and the apparatus, not just the names.
    {
        "id": "ks4-development-atomic-model-e05",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what Thomson was working with when he discovered the "
                "electron.",
        "options": [
            "Alpha particles fired at a thin sheet of gold foil inside a "
                "vacuum",
            "Cathode rays deflected by electric and magnetic fields",
            "The light given out by a heated gas",
            "The tracks left in a cloud chamber",
        ],
        "correct_index": 1,
        "why": "Thomson studied cathode rays, beams that electric and "
               "magnetic fields deflected, and identified their particles as "
               "electrons.",
    },
    {
        "id": "ks4-development-atomic-model-e06",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what the plum pudding model said an atom was like.",
        "options": [
            "A tiny solid ball that could not be divided into anything "
                "smaller at all",
            "A dense positive nucleus with electrons in orbit far outside it",
            "Electrons held in fixed energy levels around a central "
                "positive core",
            "A ball of positive charge with negative electrons set into it",
        ],
        "correct_index": 3,
        "why": "Thomson pictured the positive charge spread through the whole "
               "atom with the electrons embedded in it, like plums in a "
               "pudding.",
    },
    {
        "id": "ks4-development-atomic-model-e07",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the scientist who proposed the nuclear model of the "
                "atom.",
        "options": [
            "Ernest Rutherford",
            "J. J. Thomson",
            "Niels Bohr",
            "John Dalton",
        ],
        "correct_index": 0,
        "why": "Rutherford put forward the nuclear model in 1911, after the "
               "alpha scattering results.",
    },
    {
        "id": "ks4-development-atomic-model-e08",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the scientist who proposed that electrons orbit the "
                "nucleus in fixed energy levels.",
        "options": [
            "James Chadwick",
            "John Dalton",
            "Ernest Rutherford",
            "Niels Bohr",
        ],
        "correct_index": 3,
        "why": "Bohr's 1913 model placed the electrons in fixed shells, or "
               "energy levels, at set distances from the nucleus.",
    },
    {
        "id": "ks4-development-atomic-model-e09",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which particles were fired at the gold foil in the "
                "scattering experiment.",
        "options": [
            "Neutrons",
            "Alpha particles",
            "Electrons",
            "Beta particles",
        ],
        "correct_index": 1,
        "why": "The beam was made of alpha particles, each carrying a charge "
               "of +2.",
    },
    {
        "id": "ks4-development-atomic-model-e10",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happened to most of the alpha particles fired at "
                "the gold foil.",
        "options": [
            "They were absorbed by the foil and did not emerge from it at "
                "all",
            "They bounced back towards the source they had come from",
            "They were deflected through large angles as they passed",
            "They passed straight through with little or no deflection",
        ],
        "correct_index": 3,
        "why": "The great majority went straight through, which is what "
               "showed the atom to be mostly empty space.",
    },
    {
        "id": "ks4-development-atomic-model-e11",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the discovery of the neutron explained.",
        "options": [
            "Why an atom has no overall electric charge",
            "Why the electrons of an atom stay in their fixed shells instead "
                "of falling inwards",
            "Why a nucleus is heavier than its protons alone can account for",
            "Why alpha particles are deflected by a nucleus",
        ],
        "correct_index": 2,
        "why": "Nuclei are heavier than the mass of their protons, and the "
               "uncharged neutron accounts for the difference.",
    },
    {
        "id": "ks4-development-atomic-model-e12",
        "subtopic_slug": "development-atomic-model",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two scientists who carried out the alpha scattering "
                "experiment in Rutherford's laboratory.",
        "options": [
            "Geiger and Marsden",
            "Thomson and Bohr",
            "Chadwick and Bohr",
            "Geiger and Chadwick",
        ],
        "correct_index": 0,
        "why": "Hans Geiger and Ernest Marsden did the counting from which "
               "Rutherford drew the nuclear model.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # One observation turned into one conclusion, and the apparatus choices.
    {
        "id": "ks4-development-atomic-model-s05",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what the fact that most alpha particles passed "
                "straight through the foil showed about the atom.",
        "options": [
            "That the atom is mostly empty space",
            "That the positive charge of the atom is spread thinly right "
                "through it, exactly as the plum pudding model had said",
            "That the nucleus of a gold atom carries no charge, so nothing "
                "was there to push the particles aside",
            "That alpha particles are too fast for any atom to deflect them "
                "however they are aimed",
        ],
        "correct_index": 0,
        "why": "If almost every particle passes through undeflected, almost "
               "none of the atom can be occupied by matter.",
    },
    {
        "id": "ks4-development-atomic-model-s06",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what the very small number of alpha particles that "
                "bounced almost straight back showed about the atom.",
        "options": [
            "That the atom holds a great many separate small positive "
                "regions rather than only one of them",
            "That the positive charge is concentrated in something very "
                "small and very dense",
            "That the electrons of the atom are massive enough to turn an "
                "alpha particle right around",
            "That the foil had been beaten too thin for the experiment to "
                "give a reliable result",
        ],
        "correct_index": 1,
        "why": "Only a tiny, massive, strongly repelling target could turn "
               "back an alpha particle, and only very rarely.",
    },
    {
        "id": "ks4-development-atomic-model-s07",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what the deflection of some alpha particles through "
                "large angles showed about the atom.",
        "options": [
            "That the atom contains loose electrons able to knock a heavy "
                "particle well off its line of travel",
            "That the atom contains a concentrated region of positive charge",
            "That the atom is a solid sphere throughout, which is why a "
                "particle striking it rebounds at an angle",
            "That alpha particles repel one another strongly enough to "
                "scatter the beam as it travels",
        ],
        "correct_index": 1,
        "why": "A large deflection needs a strong repulsion, which means the "
               "positive charge is gathered together rather than spread out.",
    },
    {
        "id": "ks4-development-atomic-model-s08",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the solid sphere model of the atom had to be "
                "abandoned.",
        "options": [
            "Because alpha particles were found to pass straight through a "
                "sheet of gold, which a solid sphere would have stopped",
            "Because the neutron was discovered, and a solid sphere has no "
                "room inside it for a particle of that kind",
            "Because the electron was discovered, so an atom must have parts "
                "inside it and can be divided",
            "Because atoms were found to be far smaller than the model had "
                "supposed them to be",
        ],
        "correct_index": 2,
        "why": "The solid sphere model said the atom could not be divided, "
               "and finding a particle inside it showed that it could.",
    },
    {
        "id": "ks4-development-atomic-model-s09",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Thomson found that the particles in a cathode ray were the "
                "same whatever metal the cathode was made from. State what "
                "he concluded from this.",
        "options": [
            "That every metal conducts electricity in exactly the same way "
                "as every other metal does",
            "That the cathode metal plays no part at all in producing a "
                "cathode ray in the first place",
            "That the particle must come from the air inside the tube rather "
                "than from the metal",
            "That the particle is a part of all atoms, not only of one "
                "particular element",
        ],
        "correct_index": 3,
        "why": "A particle that appears whatever the source material is a "
               "component of matter generally, so electrons are in every "
               "atom.",
    },
    {
        "id": "ks4-development-atomic-model-s10",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the plum pudding model predicted would happen to "
                "a beam of alpha particles crossing a thin metal foil.",
        "options": [
            "Every particle would be stopped dead inside the foil, because "
                "the positive charge fills the whole of each atom",
            "Half of the particles would pass and half would bounce back, "
                "since each atom is half charge and half space",
            "All of them would pass through, or be deflected only very "
                "slightly by the spread-out charge",
            "Most would bounce straight back, because the charge is "
                "gathered at the centre of every atom",
        ],
        "correct_index": 2,
        "why": "A positive charge spread thinly through the whole atom could "
               "never exert a large enough force to turn a particle sharply.",
    },
    {
        "id": "ks4-development-atomic-model-s11",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the alpha scattering experiment had to be "
                "carried out in a vacuum.",
        "options": [
            "Because alpha particles have a range of only a few centimetres "
                "in air and would be absorbed before reaching the foil",
            "Because the gold foil would tarnish in air and stop deflecting "
                "the particles reliably",
            "Because air molecules would have made the beam travel too "
                "quickly",
            "Because the detector cannot be made to work at ordinary "
                "atmospheric pressure",
        ],
        "correct_index": 0,
        "why": "Air stops alpha radiation within a few centimetres, so in "
               "air very few particles would ever reach the foil or the "
               "detector.",
    },
    {
        "id": "ks4-development-atomic-model-s12",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why gold was chosen as the metal for the foil.",
        "options": [
            "Because gold has the largest atomic number of all the metals "
                "and so deflects a particle most strongly",
            "Because gold is so malleable that it can be beaten into a sheet "
                "only a few atoms thick",
            "Because gold does not react with the alpha particles in the way "
                "that a cheaper metal would have done",
            "Because gold conducts the charge carried by the beam safely "
                "away to earth as the beam arrives",
        ],
        "correct_index": 1,
        "why": "Gold can be hammered into an extremely thin foil, so most "
               "alpha particles meet at most one nucleus on the way through.",
    },
    {
        "id": "ks4-development-atomic-model-s13",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what Bohr's model added to Rutherford's nuclear "
                "model.",
        "options": [
            "A second, uncharged particle sitting in the nucleus beside the "
                "protons already there",
            "A positive charge spread through the atom outside the nucleus "
                "to balance the electrons",
            "Electrons held at fixed distances from the nucleus, in "
                "separate energy levels",
            "A nucleus far smaller than Rutherford had first supposed it to "
                "be",
        ],
        "correct_index": 2,
        "why": "Bohr kept the nucleus and placed the electrons in fixed "
               "energy levels rather than at any distance at all.",
    },
    {
        "id": "ks4-development-atomic-model-s14",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the observation that supported Bohr's idea of fixed "
                "electron energy levels.",
        "options": [
            "The continuous rainbow of colours given out by a hot solid",
            "The deflection of a beam of electrons by a magnetic field",
            "The mass of a nucleus being greater than its protons alone",
            "Light emitted by atoms appearing as separate sharp lines",
        ],
        "correct_index": 3,
        "why": "Discrete spectral lines mean electrons can only lose fixed "
               "amounts of energy, which is what fixed energy levels "
               "predict.",
    },
    {
        "id": "ks4-development-atomic-model-s15",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare where the plum pudding model and the nuclear model "
                "each place the positive charge of an atom.",
        "options": [
            "Plum pudding spreads it through the whole atom; the nuclear "
                "model concentrates it in a tiny centre",
            "Plum pudding concentrates it at the centre; the nuclear model "
                "spreads it evenly through the atom instead",
            "Both place it in a small central nucleus",
            "Both of them spread it through the atom, differing only over "
                "how many electrons there are",
        ],
        "correct_index": 0,
        "why": "The two models disagree precisely over whether the positive "
               "charge is spread out or gathered into a nucleus.",
    },
    {
        "id": "ks4-development-atomic-model-s16",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the electrons in the gold atoms barely deflected "
                "the alpha particles.",
        "options": [
            "Because electrons and alpha particles both carry a negative "
                "charge and so cannot interact with one another at all",
            "Because the electrons had all been stripped away from the gold "
                "before the beam was switched on",
            "Because electrons sit inside the nucleus, where the alpha "
                "particles never reach them",
            "Because an electron is thousands of times lighter than an alpha "
                "particle, so it cannot push one off course",
        ],
        "correct_index": 3,
        "why": "An alpha particle has thousands of times an electron's mass, "
               "so a collision with one changes its path hardly at all.",
    },
    {
        "id": "ks4-development-atomic-model-s17",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how the nuclear model accounts for an atom having "
                "no overall charge.",
        "options": [
            "The neutrons of the nucleus cancel out the charge that its "
                "protons carry",
            "The nucleus carries no charge of its own, so there is nothing "
                "at all left for the electrons of the atom to have to balance",
            "The positive charge of the nucleus is balanced by an equal "
                "total negative charge on the orbiting electrons",
            "The charge of the atom leaks away to its neighbours until "
                "nothing at all is left of it",
        ],
        "correct_index": 2,
        "why": "The model has a positive nucleus and enough orbiting "
               "electrons to match its charge exactly.",
    },
    {
        "id": "ks4-development-atomic-model-s18",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rutherford said the result was as surprising as firing a "
                "large shell at tissue paper and having it come back. "
                "Explain which observation he was describing.",
        "options": [
            "That a very few alpha particles were turned almost completely "
                "around by the foil",
            "That most of the alpha particles went straight through the foil "
                "without being deflected",
            "That the number of alpha particles arriving each minute varied "
                "from one minute to the next",
            "That the foil itself was left undamaged after hours of being "
                "struck by the beam",
        ],
        "correct_index": 0,
        "why": "Nothing in the plum pudding model could reverse a heavy fast "
               "particle, so the few that came back were the shock.",
    },
    {
        "id": "ks4-development-atomic-model-s19",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would happen to the results if the gold foil "
                "were made many times thicker.",
        "options": [
            "Nothing would change, because each alpha particle meets only "
                "one atom whatever the thickness of the foil",
            "Every alpha particle would come straight back, since a thicker "
                "foil reflects the whole of the beam",
            "Many particles would meet several nuclei, so the pattern would "
                "be harder to interpret",
            "The particles would speed up as they crossed, because a "
                "thicker foil gives them a longer push",
        ],
        "correct_index": 2,
        "why": "Multiple deflections inside a thick foil confuse the simple "
               "one-encounter picture the experiment depends on.",
    },
    {
        "id": "ks4-development-atomic-model-s20",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the neutron was discovered so much later than "
                "the electron.",
        "options": [
            "Because it carries no charge, so electric and magnetic fields "
                "do not deflect it and it is hard to detect",
            "Because it is very much smaller than an electron and so escapes "
                "every one of the detectors that were available at the time",
            "Because neutrons were not present in atoms until the 1930s, "
                "when the first ones formed",
            "Because it sits outside the atom, where nobody had thought to "
                "look for a new particle",
        ],
        "correct_index": 0,
        "why": "Detection methods of the time relied on deflecting charged "
               "particles, and an uncharged particle is not deflected at "
               "all.",
    },
    {
        "id": "ks4-development-atomic-model-s21",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The electron was discovered in 1897 and the neutron in 1932. "
                "Determine the approximate interval between the two "
                "discoveries.",
        "options": [
            "About 15 years",
            "About 35 years",
            "About 55 years",
            "About 100 years",
        ],
        "correct_index": 1,
        "why": "1932 − 1897 = 35 years.",
    },
    {
        "id": "ks4-development-atomic-model-s22",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a scientific model of the atom is for.",
        "options": [
            "To record which scientists made which discovery and in what "
                "order the discoveries came",
            "To explain the observations already made and to predict the "
                "results of new experiments",
            "To provide a picture of the atom that will never afterwards "
                "need to be altered in any way",
            "To show the true appearance of an atom as it would look under a "
                "sufficiently powerful microscope",
        ],
        "correct_index": 1,
        "why": "A model earns its place by accounting for the evidence and "
               "by predicting what has not yet been measured.",
    },
    {
        "id": "ks4-development-atomic-model-s23",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the accepted model of the atom changed four "
                "times in less than half a century.",
        "options": [
            "Because each scientist preferred a picture of his own to the "
                "one his predecessor had drawn",
            "Because the atom itself was changing over that period as new "
                "particles formed inside it",
            "Because the earlier models had been proposed without any "
                "evidence behind them at all",
            "Because new experimental evidence appeared that the model then "
                "in use could not account for",
        ],
        "correct_index": 3,
        "why": "Cathode rays, alpha scattering, line spectra and nuclear "
               "masses each arrived as evidence the current model could not "
               "explain.",
    },
    {
        "id": "ks4-development-atomic-model-s24",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why Rutherford concluded that the nucleus carries a "
                "positive charge rather than a negative one.",
        "options": [
            "Because the foil became positively charged as the beam kept "
                "striking it over several months",
            "Because a nucleus must be positive if the electrons around it "
                "are to stay in their shells at all",
            "Because the positive alpha particles were pushed away from it, "
                "and like charges repel",
            "Because the alpha particles were pulled towards it, and "
                "opposite charges attract each other",
        ],
        "correct_index": 2,
        "why": "The alpha particles carry +2 and were repelled, so whatever "
               "repelled them must also be positive.",
    },
    {
        "id": "ks4-development-atomic-model-s25",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to an alpha particle that approaches a "
                "gold nucleus head-on.",
        "options": [
            "It is slowed and pushed back along its own path by the "
                "repulsion of the nucleus",
            "It is absorbed by the nucleus and becomes part of it",
            "It passes through the nucleus and out of the far side of it",
            "It is captured into an orbit around the nucleus and stays there "
                "from that moment onwards",
        ],
        "correct_index": 0,
        "why": "Two positive charges repel, so a head-on approach is slowed, "
               "stopped and sent back the way it came.",
    },
    {
        "id": "ks4-development-atomic-model-s26",
        "subtopic_slug": "development-atomic-model",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the discovery of the electron on its own did not "
                "tell scientists where the positive charge of an atom was.",
        "options": [
            "Because an atom's neutrality only shows that positive charge is "
                "present, not how it is arranged",
            "Because the electron had not yet been shown to carry any charge "
                "of its own when it was found",
            "Because the positive charge of an atom had not been discovered "
                "until many years afterwards",
            "Because Thomson's apparatus was able to detect a negative "
                "charge but never a positive one",
        ],
        "correct_index": 0,
        "why": "Knowing an atom is neutral fixes the total positive charge "
               "but says nothing about whether it is spread out or gathered "
               "into a nucleus.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Evidence read against conclusion, and the nature-of-science reasoning.
    {
        "id": "ks4-development-atomic-model-h05",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'The alpha scattering experiment showed "
                "that a nucleus contains neutrons as well as protons.'",
        "options": [
            "Sound — the deflections that were recorded could only have been "
                "produced by a nucleus holding both kinds of particle at once",
            "Sound — the neutrons were what stopped the particles that "
                "failed to emerge from the foil",
            "Unsound — the experiment showed the nucleus is small, dense and "
                "positive; the neutron was found two decades later",
            "Unsound — the experiment in fact showed that a nucleus contains "
                "no neutrons whatsoever",
        ],
        "correct_index": 2,
        "why": "Scattering reveals a small dense positive nucleus and "
               "nothing about uncharged particles; Chadwick found the "
               "neutron in 1932.",
    },
    {
        "id": "ks4-development-atomic-model-h06",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an experiment that measured only the total "
                "charge of an atom could never have decided between the plum "
                "pudding model and the nuclear model.",
        "options": [
            "Because both models describe a neutral atom, so both predict "
                "the same total charge",
            "Because the total charge of an atom cannot be measured by any "
                "experiment at all",
            "Because the plum pudding model says an atom carries a small "
                "positive charge overall",
            "Because the nuclear model says the charge of an atom changes "
                "from moment to moment",
        ],
        "correct_index": 0,
        "why": "Two models that agree on a prediction cannot be told apart "
               "by measuring it; the experiment has to probe where the "
               "charge sits.",
    },
    {
        "id": "ks4-development-atomic-model-h07",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that Rutherford discovered the electron. "
                "Correct the statement and state what his work did establish.",
        "options": [
            "Rutherford found the neutron; the electron came from Bohr's "
                "work on the spectra of hot gases",
            "Rutherford found the electron and the nucleus together, in the "
                "one series of scattering measurements",
            "Thomson found the electron; Rutherford's team established the "
                "small dense positive nucleus",
            "Chadwick found the electron; Rutherford established that the "
                "atom is a solid indivisible sphere",
        ],
        "correct_index": 2,
        "why": "Thomson identified the electron in 1897; the scattering work "
               "under Rutherford established the nucleus in 1911.",
    },
    {
        "id": "ks4-development-atomic-model-h08",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a model that fits every piece of evidence "
                "available today may still be replaced in the future.",
        "options": [
            "Because scientists change their models on a regular timetable "
                "whether the evidence has moved or not",
            "Because no model is ever tested against evidence in the first "
                "place, so any of them may fall",
            "Because the thing being modelled is itself changing steadily as "
                "the years pass",
            "Because new apparatus can produce observations the present "
                "model was never built to explain",
        ],
        "correct_index": 3,
        "why": "A model is only as secure as the evidence it has met, and "
               "better instruments keep producing evidence it has not.",
    },
    {
        "id": "ks4-development-atomic-model-h09",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what the plum pudding model and the nuclear model "
                "each predict for a beam of alpha particles crossing a thin "
                "foil.",
        "options": [
            "Plum pudding: small deflections only. Nuclear: mostly straight "
                "through, with a few turned through large angles",
            "Plum pudding: mostly straight through with a few large "
                "deflections. Nuclear: small deflections only",
            "Both predict that most particles pass through and a few are "
                "turned back, which is why the test settled nothing",
            "Both predict that the whole beam is absorbed, so the experiment "
                "could distinguish the two only by counting",
        ],
        "correct_index": 0,
        "why": "A thinly spread charge can only nudge a particle, whereas a "
               "concentrated nucleus leaves most paths untouched and turns a "
               "few sharply.",
    },
    {
        "id": "ks4-development-atomic-model-h10",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rutherford's model left it unexplained why a negative "
                "electron orbiting a positive nucleus does not simply fall "
                "into it. State which later model addressed that problem.",
        "options": [
            "Thomson's plum pudding model",
            "Bohr's model of fixed energy levels",
            "Chadwick's discovery of the neutron",
            "The solid sphere model",
        ],
        "correct_index": 1,
        "why": "Bohr's fixed energy levels gave the electrons stable orbits "
               "they could not spiral out of.",
    },
    {
        "id": "ks4-development-atomic-model-h11",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Nuclei were measured to be heavier than the total mass of "
                "their protons. Explain how Chadwick's work resolved this.",
        "options": [
            "He showed that a proton is heavier than had been thought, which "
                "accounted for the whole difference",
            "He showed that the electrons of an atom are drawn into the "
                "nucleus and add their mass to it",
            "He found the neutron — an uncharged nuclear particle of about a "
                "proton's mass",
            "He showed that the mass measurements had been wrong and that no "
                "difference existed",
        ],
        "correct_index": 2,
        "why": "A neutral particle of roughly a proton's mass adds mass "
               "without adding charge, which is exactly the discrepancy "
               "observed.",
    },
    {
        "id": "ks4-development-atomic-model-h12",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that one alpha particle seen to bounce "
                "back would have been enough to establish the nuclear model.",
        "options": [
            "Sound — a single observation of that kind rules the plum "
                "pudding model out completely",
            "Unsound — a single particle bouncing back off the foil would in "
                "fact have been support for the plum pudding model instead",
            "Sound — provided that the one particle was observed by two "
                "different scientists at once",
            "Unsound — the counts have to be large before the proportion "
                "turned back means anything, since one event could be a stray",
        ],
        "correct_index": 3,
        "why": "The conclusion rests on how RARE a large deflection is, and "
               "a proportion cannot be measured from a single event.",
    },
    {
        "id": "ks4-development-atomic-model-h13",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alpha particle has roughly 7300 times the mass of an "
                "electron. Determine what this means for the scattering "
                "results.",
        "options": [
            "The electrons of the foil cannot account for the large "
                "deflections, so a massive target must be responsible",
            "The electrons of the foil are what turned the particles back, "
                "since a light target deflects a heavy one most",
            "The alpha particles must have been slowed to a stop by the "
                "electrons before they reached any nucleus",
            "The mass ratio makes no difference, because deflection depends "
                "on charge alone and never on mass",
        ],
        "correct_index": 0,
        "why": "A heavy particle is barely deflected by a much lighter one, "
               "so the large-angle scattering points to something as massive "
               "as a nucleus.",
    },
    {
        "id": "ks4-development-atomic-model-h14",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the scattering experiment revealed almost "
                "nothing about the electrons of the gold atoms.",
        "options": [
            "Because gold atoms hold no electrons for the experiment to "
                "have revealed anything about",
            "Because the electrons are too light to deflect an alpha "
                "particle measurably, so they leave no mark on the results",
            "Because the electrons of the foil had all been driven out of it "
                "by the beam well before the counting began",
            "Because electrons and alpha particles carry the same charge and "
                "so pass each other untouched",
        ],
        "correct_index": 1,
        "why": "An experiment only measures what changes the thing it is "
               "measuring, and the electrons change an alpha particle's path "
               "hardly at all.",
    },
    {
        "id": "ks4-development-atomic-model-h15",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the plum pudding model was accepted for more "
                "than a decade even though it was wrong.",
        "options": [
            "Because no scientist of the period was willing to disagree "
                "with Thomson in public",
            "Because it explained the evidence then available — atoms hold "
                "electrons and are neutral overall",
            "Because the experiment that disproved it could not be "
                "performed until the vacuum pump was invented",
            "Because it made no predictions at all, so there was nothing in "
                "it that an experiment could test",
        ],
        "correct_index": 1,
        "why": "A model stands while it fits the evidence, and Thomson's fit "
               "everything known until the scattering results arrived.",
    },
    {
        "id": "ks4-development-atomic-model-h16",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the kind of evidence Thomson used with the kind "
                "Rutherford's team used.",
        "options": [
            "Thomson deflected a beam of particles with fields; Rutherford's "
                "team counted particles scattered by a foil",
            "Both of them counted particles scattered by a metal foil, "
                "differing only in which metal they chose",
            "Thomson counted scattered particles; Rutherford's team "
                "deflected a beam of them with electric fields",
            "Thomson measured the light emitted by atoms; Rutherford's team "
                "measured the mass of a nucleus directly",
        ],
        "correct_index": 0,
        "why": "Thomson's evidence came from deflecting cathode rays in "
               "fields; the nuclear model came from counting how alpha "
               "particles scattered.",
    },
    {
        "id": "ks4-development-atomic-model-h17",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the picture of the atom is called a model "
                "rather than a photograph.",
        "options": [
            "Because photographs of atoms had not been invented at the time "
                "the picture was first drawn",
            "Because the word model is simply the term physicists prefer for "
                "any diagram they draw",
            "Because a photograph would show the atom in colour, and the "
                "model is drawn in black and white",
            "Because it is a representation built to explain measurements, "
                "not a direct image of the thing itself",
        ],
        "correct_index": 3,
        "why": "Nobody has seen an atom directly; the model is an account "
               "constructed to fit what experiments measure.",
    },
    {
        "id": "ks4-development-atomic-model-h18",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine what the very small proportion of alpha particles "
                "deflected through large angles implies about the size of a "
                "nucleus compared with the size of an atom.",
        "options": [
            "That a nucleus is about a tenth of the width of its atom",
            "That a nucleus and its atom are of much the same size as one "
                "another",
            "That a nucleus is a minute fraction of the width of its atom",
            "That a nucleus is wider than its atom, which is why a particle "
                "can strike it",
        ],
        "correct_index": 2,
        "why": "A target that is almost never hit must occupy almost none of "
               "the area presented to the beam.",
    },
    {
        "id": "ks4-development-atomic-model-h19",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Because the nuclear model replaced "
                "the plum pudding model, scientific models cannot be "
                "trusted.'",
        "options": [
            "Unsound — replacing a model when better evidence arrives is "
                "exactly how science is meant to work",
            "Sound — any model that may later be replaced is of no use to "
                "anybody while it stands",
            "Sound — the replacement shows that the scientists of the period "
                "were working without evidence",
            "Unsound — the plum pudding model was never actually replaced, "
                "only extended",
        ],
        "correct_index": 0,
        "why": "Being open to revision on new evidence is a strength of the "
               "method, not a reason to distrust its current best model.",
    },
    {
        "id": "ks4-development-atomic-model-h20",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why Rutherford's team used a source of alpha "
                "particles rather than a source of beta particles.",
        "options": [
            "Because beta particles carry no charge and so would not have "
                "been deflected by a nucleus at all",
            "Because alpha particles are massive and positively charged, so "
                "a positive nucleus deflects them strongly and measurably",
            "Because beta particles are too heavy to be turned aside by "
                "anything as small as a nucleus",
            "Because alpha particles travel very much faster than beta "
                "particles do, which is what makes them the easier of the two to "
                "count",
        ],
        "correct_index": 1,
        "why": "A heavy positive projectile is repelled sharply by a "
               "positive nucleus, and a light one would scatter off the "
               "electrons instead.",
    },
    {
        "id": "ks4-development-atomic-model-h21",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A modern repeat of the scattering experiment uses an "
                "electronic detector in place of a human observer. Suggest "
                "one advantage of this.",
        "options": [
            "The detector changes the model the results support",
            "The detector makes the vacuum unnecessary, so the experiment "
                "can be run in ordinary air",
            "The detector removes the randomness from radioactive decay, so "
                "each count is now predictable",
            "The detector records far more counts reliably in a given time, "
                "so the proportions are more precise",
        ],
        "correct_index": 3,
        "why": "Counting a rare event well needs a great many trials, and an "
               "electronic detector gathers them faster and without "
               "observer error.",
    },
    {
        "id": "ks4-development-atomic-model-h22",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the solid sphere model with the plum pudding model.",
        "options": [
            "Solid sphere: an indivisible ball. Plum pudding: positive "
                "charge with electrons set into it",
            "Solid sphere: positive charge with electrons set into it. Plum "
                "pudding: an indivisible ball",
            "Both of them have a small dense nucleus, differing only over "
                "where the electrons sit",
            "Both of them have electrons in fixed shells, differing only "
                "over the charge of the centre",
        ],
        "correct_index": 0,
        "why": "The solid sphere had no internal structure at all, while the "
               "plum pudding gave the atom separate positive and negative "
               "parts.",
    },
    {
        "id": "ks4-development-atomic-model-h23",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the nuclear model is still taught even though "
                "Bohr later refined it.",
        "options": [
            "Because Bohr's refinement was afterwards shown to have been "
                "mistaken, and the nuclear model was restored in its place",
            "Because Bohr's work changed only where the electrons go, "
                "leaving the small dense positive nucleus intact",
            "Because the nuclear model is simpler to draw, even though it is "
                "known to be wrong throughout",
            "Because the two models describe different kinds of atom, one "
                "light and the other heavy",
        ],
        "correct_index": 1,
        "why": "Bohr kept Rutherford's nucleus and added fixed energy levels "
               "for the electrons, so the nuclear picture still holds.",
    },
    {
        "id": "ks4-development-atomic-model-h24",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the plum pudding model had no evidence behind "
                "it at all. Evaluate that judgement.",
        "options": [
            "Sound — Thomson proposed it with nothing in its support",
            "Sound — the alpha scattering results were already known when he "
                "proposed it and he ignored them",
            "Unsound — it rested on the alpha scattering results, which is "
                "why it lasted as long as it did",
            "Unsound — it was built on the discovery of the electron and on "
                "the fact that atoms are electrically neutral",
        ],
        "correct_index": 3,
        "why": "Thomson had found a negative particle inside neutral atoms, "
               "and his model was a reasonable account of exactly that.",
    },
    {
        "id": "ks4-development-atomic-model-h25",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine what the three scattering observations, taken "
                "together, establish about the atom.",
        "options": [
            "That it holds protons, neutrons and electrons in fixed numbers "
                "which can be counted from the deflections",
            "That it is mostly empty space, with a small, dense, positively "
                "charged centre",
            "That it is a solid sphere of positive charge with electrons "
                "spread evenly all the way through it",
            "That its electrons sit in fixed energy levels at set distances "
                "from a central nucleus",
        ],
        "correct_index": 1,
        "why": "Most through means empty space, some deflected means "
               "concentrated positive charge, a few reversed means that "
               "charge is small and dense.",
    },
    {
        "id": "ks4-development-atomic-model-h26",
        "subtopic_slug": "development-atomic-model",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why Rutherford's conclusions were published so that "
                "other scientists could repeat the measurements.",
        "options": [
            "So that the credit for the discovery could be shared out among "
                "the laboratories that took part in it",
            "So that other laboratories could check the results "
                "independently before the new model was accepted",
            "So that the experiment would not need to be performed a second "
                "time anywhere else",
            "So that the plum pudding model could be removed from the "
                "textbooks without any further argument",
        ],
        "correct_index": 1,
        "why": "A claim becomes accepted science once others have repeated "
               "the measurement and found the same thing.",
    },
]
