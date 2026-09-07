"""Chemistry · Chemical analysis — the MRB-335 extension.

Four of this topic's eight subtopics are Triple-only (flame tests, metal
hydroxides, the halide and sulfate tests, instrumental methods), so the
Combined pathway sees only `pure-substances`, `formulations`,
`chromatography` and `testing-for-gases` — 48 questions for Foundation and
32 for Higher on the 7 Sep table.

The weight here is deliberately uneven and follows the CONTENT rather than
the arithmetic. `chromatography` carries a required practical, an equation
with two rearrangements and a set of real technique errors, and takes
thirteen rows; `pure-substances` is one idea about melting and boiling
points and takes six. Spreading them evenly would have produced four more
chromatography-shaped questions about purity, which is how a pool grows in
size without growing in coverage.
"""

TOPIC = "analysis"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── pure-substances ───────────────────────── BASE (5.8.1.1) ── +6 ──
    {
        "id": "ks4-pure-substances-e05",
        "subtopic_slug": "pure-substances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a sharp, fixed melting point tells a chemist "
                "about a substance.",
        "options": [
            "That it is a mixture",
            "That it is a pure substance",
            "That it is a formulation",
            "That it is a solid at room temperature",
        ],
        "correct_index": 1,
        "why": "Only a pure substance melts at one exact temperature; "
               "anything mixed in spreads the melting over a range.",
    },
    {
        "id": "ks4-pure-substances-s05",
        "subtopic_slug": "pure-substances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a pure substance boils at a fixed temperature "
                "but a mixture boils over a range.",
        "options": [
            "A pure substance has stronger bonds, so it needs one exact "
            "temperature",
            "A mixture reacts as it is heated, which changes its boiling "
            "point",
            "In a mixture each component has its own boiling point, so they "
            "leave over a spread of temperatures",
            "A pure substance has only one type of particle, so it cannot be "
            "heated any further",
        ],
        "correct_index": 2,
        "why": "A mixture is several substances together, and each boils "
               "away at its own temperature, so the mixture has no single "
               "boiling point.",
    },
    {
        "id": "ks4-pure-substances-s06",
        "subtopic_slug": "pure-substances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A carton of orange juice is labelled 'pure orange juice'. "
                "State whether it is pure in the chemical sense, and explain.",
        "options": [
            "No — it is a mixture of water, sugars, acids and many other "
            "compounds",
            "Yes — nothing at all has been added to it, so it counts as "
            "pure",
            "Yes — it all came from a single source",
            "No — it contains only one element",
        ],
        "correct_index": 0,
        "why": "In everyday use 'pure' means nothing added; in chemistry it "
               "means a single element or compound, and juice is neither.",
    },
    {
        "id": "ks4-pure-substances-s07",
        "subtopic_slug": "pure-substances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sea water is distilled and the distillate's boiling point "
                "is measured. Predict the result and explain it.",
        "options": [
            "It boils over a range above 100 °C, because some salt is "
            "carried over with the vapour",
            "It boils sharply at 100 °C, because sea water always boils at "
            "100 °C",
            "It boils below 100 °C, because distillation removes energy from "
            "the water",
            "It boils sharply at 100 °C, because distillation has separated "
            "pure water from the dissolved salts",
        ],
        "correct_index": 3,
        "why": "The salts do not vaporise, so the distillate is pure water "
               "and behaves like a pure substance with a fixed boiling "
               "point.",
    },
    {
        "id": "ks4-pure-substances-h05",
        "subtopic_slug": "pure-substances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chemist has a colourless liquid that is either pure "
                "ethanol (boiling point 78 °C) or pure propanone (boiling "
                "point 56 °C). Describe how one measurement identifies it, "
                "and what a boiling RANGE would instead show.",
        "options": [
            "Measure the boiling point: a sharp 78 °C means ethanol and 56 "
            "°C means propanone, while a range means a mixture",
            "Measure the melting point instead, because a pure liquid melts "
            "at the same temperature as it boils",
            "Measure the mass of 1 cm3, because ethanol is the heavier of "
            "the two",
            "Measure the colour, because propanone is faintly yellow and "
            "ethanol is not",
        ],
        "correct_index": 0,
        "why": "A pure liquid boils at one temperature that identifies it; "
               "a range means neither, because the sample is not pure.",
    },
    {
        "id": "ks4-pure-substances-h06",
        "subtopic_slug": "pure-substances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Solid A is heated: its temperature rises steadily to 96 °C, "
                "stays at 96 °C for four minutes, then rises again. Solid B "
                "rises steadily throughout with no flat section. Deduce what "
                "each result shows.",
        "options": [
            "Both are pure, but B was heated more quickly",
            "A is pure and melts at a fixed 96 °C; B is a mixture and melts "
            "over a range",
            "A is a mixture and B is pure",
            "Both are mixtures, but A has fewer components than B and so "
            "melts over a narrower range",
        ],
        "correct_index": 1,
        "why": "The flat section is melting at one fixed temperature, which "
               "only a pure substance does; a mixture melts gradually and "
               "the temperature never levels off.",
    },

    # ── formulations ──────────────────────────── BASE (5.8.1.2) ── +7 ──
    {
        "id": "ks4-formulations-e05",
        "subtopic_slug": "formulations",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a formulation is a mixture rather than a compound.",
        "options": [
            "Its components are chemically bonded together in fixed ratios",
            "It contains only one type of particle",
            "Its components are not chemically bonded, and each keeps its "
            "own properties",
            "It cannot be separated by any physical method",
        ],
        "correct_index": 2,
        "why": "The ingredients of a formulation are measured out and mixed, "
               "not reacted together, so each one still does its own job.",
    },
    {
        "id": "ks4-formulations-s05",
        "subtopic_slug": "formulations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Alloys, fuels, cleaning agents, paints, medicines and foods "
                "are all formulations. Identify what they have in common.",
        "options": [
            "Every component is included in a carefully measured quantity "
            "to give the product the properties it needs",
            "Each of them is made of a single compound",
            "Each of them is produced by a chemical reaction between the "
            "components that are mixed together",
            "Each of them contains a solvent, a pigment and a binder mixed "
            "in carefully measured proportions",
        ],
        "correct_index": 0,
        "why": "A formulation is defined by design: someone chose each "
               "quantity so that the mixture does a particular job.",
    },
    {
        "id": "ks4-formulations-s06",
        "subtopic_slug": "formulations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tablet contains an active drug, a binder, a filler and a "
                "coating. Explain why the quantity of the active drug is "
                "controlled far more tightly than the quantity of filler.",
        "options": [
            "Too little drug will not treat the illness and too much could "
            "be toxic; the filler only sets the size",
            "The filler costs far more than the drug does",
            "The binder reacts with the active drug whenever the quantities "
            "are wrong, spoiling the tablet",
            "The coating dissolves at a rate decided by the filler",
        ],
        "correct_index": 0,
        "why": "The dose is what makes the medicine work or makes it "
               "dangerous; the filler is only there to make the tablet a "
               "usable size.",
    },
    {
        "id": "ks4-formulations-s07",
        "subtopic_slug": "formulations",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a shampoo manufacturer tests every new batch to "
                "check the proportions of its ingredients.",
        "options": [
            "Because the proportions of a mixture drift on their own during "
            "storage and have to be corrected",
            "Because a formulation turns into a compound if its proportions "
            "change",
            "Because testing is the only way to find a shampoo's melting "
            "point",
            "Because the properties depend on the proportions, so a batch "
            "off the recipe may not clean or may irritate skin",
        ],
        "correct_index": 3,
        "why": "A formulation only behaves as intended while its quantities "
               "are right, so the proportions are what a quality check "
               "measures.",
    },
    {
        "id": "ks4-formulations-h05",
        "subtopic_slug": "formulations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two antifreeze products contain the same ingredients. Brand "
                "A protects to −20 °C and brand B to −35 °C. Deduce what "
                "must differ between them and explain.",
        "options": [
            "B contains a higher proportion of antifreeze to water, and a "
            "higher concentration lowers the freezing point further",
            "B contains a different compound that is not present in A at "
            "all",
            "B is a compound while A is only a mixture",
            "A has been diluted with water after it was made, so it is no "
            "longer the formulation the maker designed",
        ],
        "correct_index": 0,
        "why": "Same ingredients means the only variable left is how much of "
               "each there is, and more antifreeze depresses the freezing "
               "point further.",
    },
    {
        "id": "ks4-formulations-h06",
        "subtopic_slug": "formulations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A paint sold in an organic solvent is reformulated to use "
                "water instead, with the same pigment. Evaluate this change.",
        "options": [
            "It has no effect at all, because the pigment is unchanged and "
            "the pigment is what gives a paint its properties",
            "It turns the paint into a compound rather than a formulation",
            "It cuts harmful solvent vapours, but the paint may dry more "
            "slowly and cover less well per coat",
            "It removes the need to measure the proportions of any "
            "component",
        ],
        "correct_index": 2,
        "why": "Changing one component of a formulation changes the "
               "properties it was designed around, so a gain in safety can "
               "cost performance.",
    },
    {
        "id": "ks4-formulations-h07",
        "subtopic_slug": "formulations",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Air is a formulation, because it "
                "is a mixture of gases in fixed proportions.'",
        "options": [
            "Correct — any mixture with fixed proportions is a formulation",
            "Incorrect — a formulation is designed, with each quantity "
            "chosen for a purpose, and nobody designed the air",
            "Incorrect — air is a compound rather than a mixture",
            "Correct, because the oxygen content of air is measured and "
            "controlled before the air is used in industry",
        ],
        "correct_index": 1,
        "why": "Fixed proportions are not enough: what makes a mixture a "
               "formulation is that a person chose those proportions to get "
               "particular properties.",
    },

    # ── chromatography ────────────────────────── BASE (5.8.1.3) ── +13 ──
    {
        "id": "ks4-chromatography-e05",
        "subtopic_slug": "chromatography",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In paper chromatography, state what the mobile phase is.",
        "options": [
            "The chromatography paper",
            "The pencil baseline",
            "The solvent that moves up the paper",
            "The spot of the substance being tested",
        ],
        "correct_index": 2,
        "why": "The mobile phase is the one that moves — the solvent — and "
               "it carries the dissolved substances up the stationary paper.",
    },
    {
        "id": "ks4-chromatography-e06",
        "subtopic_slug": "chromatography",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why the baseline must sit ABOVE the level of the "
                "solvent in the tank.",
        "options": [
            "So the spots are not washed straight off the paper into the "
            "solvent",
            "So the paper does not become wet at all",
            "So the solvent front reaches the top of the paper faster",
            "So the pencil line does not dissolve away",
        ],
        "correct_index": 0,
        "why": "If the baseline is below the solvent level the spots dissolve "
               "into the tank instead of travelling up the paper.",
    },
    {
        "id": "ks4-chromatography-s05",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a chromatogram the solvent front reaches 8.0 cm and a "
                "blue spot reaches 4.4 cm. Calculate the Rf value of the "
                "blue spot.",
        "options": [
            "0.44",
            "0.55",
            "1.8",
            "3.6",
        ],
        "correct_index": 1,
        "why": "Rf is the spot's distance divided by the solvent front's "
               "distance: 4.4 ÷ 8.0 = 0.55.",
    },
    {
        "id": "ks4-chromatography-s06",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student's chromatogram shows one ink separating into "
                "three spots. Deduce what this shows about the ink.",
        "options": [
            "It is a pure substance that has reacted with the solvent",
            "The paper was contaminated with three impurities",
            "It contains three chemical elements",
            "It is a mixture of at least three different coloured substances",
        ],
        "correct_index": 3,
        "why": "Each spot is a different substance travelling at its own "
               "rate, so three spots means at least three substances in the "
               "ink.",
    },
    {
        "id": "ks4-chromatography-s07",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe why a lid is placed on the chromatography tank "
                "during a run.",
        "options": [
            "To stop the solvent evaporating, which would change how far "
            "the solvent front travels",
            "To keep the paper warm so that the spots travel faster and the "
            "run is finished sooner",
            "To stop light from fading the coloured spots",
            "To hold the paper upright inside the tank",
        ],
        "correct_index": 0,
        "why": "Evaporation from the paper would slow the solvent front "
               "unevenly, so the distances the Rf values depend on would no "
               "longer be reliable.",
    },
    {
        "id": "ks4-chromatography-s08",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the spot on the baseline should be small and "
                "allowed to dry before the paper goes into the solvent.",
        "options": [
            "A large or wet spot spreads sideways, so the separated spots "
            "overlap and cannot be measured",
            "A large spot uses up too much of the solvent in the tank",
            "A wet spot would dissolve the pencil baseline",
            "A small spot always travels further up the paper, which gives "
            "a larger Rf value to measure",
        ],
        "correct_index": 0,
        "why": "Separation is only visible if each substance starts from a "
               "single narrow point; a broad start gives broad, merging "
               "spots.",
    },
    {
        "id": "ks4-chromatography-s09",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same four dyes are run in two solvents. In solvent 1 "
                "every Rf lies between 0.90 and 0.95; in solvent 2 they lie "
                "between 0.20 and 0.70. Deduce which solvent is the better "
                "choice.",
        "options": [
            "Solvent 1, because a higher Rf means the dyes are more soluble",
            "Solvent 2, because the Rf values are well spread, so the spots "
            "are clearly separated",
            "Solvent 1, because the spots travel further and are easier to "
            "see",
            "Either — the solvent has no effect on how well a mixture "
            "separates",
        ],
        "correct_index": 1,
        "why": "A good solvent spreads the substances out; Rf values bunched "
               "near 1 mean the spots all run together near the front.",
    },
    {
        "id": "ks4-chromatography-s10",
        "subtopic_slug": "chromatography",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student leaves the paper in the tank until the solvent "
                "front reaches the very top edge. Explain why the Rf values "
                "from this run are unreliable.",
        "options": [
            "The run should be stopped before the front reaches the top, "
            "because the front can go no further while the spots keep "
            "moving",
            "The paper absorbs extra solvent once the front reaches the top "
            "edge, and that lowers every Rf value calculated",
            "Rf values calculated from such a run always come out above 1",
            "The pencil baseline dissolves as soon as the front reaches the "
            "top",
        ],
        "correct_index": 0,
        "why": "Rf compares two distances measured at the same moment; once "
               "the front is stuck at the top, that comparison stops being "
               "fair.",
    },
    {
        "id": "ks4-chromatography-h05",
        "subtopic_slug": "chromatography",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Substance E has Rf 0.30 in solvent 1 and 0.75 in solvent 2. "
                "Substance F has Rf 0.30 in solvent 1 and 0.30 in solvent 2. "
                "Deduce whether E and F are the same substance.",
        "options": [
            "They are the same, because both give Rf 0.30 in solvent 1",
            "They are the same, because Rf is a property of the paper alone",
            "They are different, because the same substance would give the "
            "same Rf in both solvents",
            "Nothing can be deduced without knowing the colours of the two "
            "spots",
        ],
        "correct_index": 2,
        "why": "Two substances can share an Rf in one solvent by chance, "
               "which is why a second solvent tells them apart.",
    },
    {
        "id": "ks4-chromatography-h06",
        "subtopic_slug": "chromatography",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures each spot to its TOP edge rather than to "
                "its centre. Describe the effect on the Rf values and "
                "explain.",
        "options": [
            "Every Rf comes out slightly too low, because the top edge is "
            "nearer the baseline",
            "Rf values are unaffected, because the same error is in every "
            "measurement",
            "Every Rf comes out above 1",
            "Every Rf comes out slightly too high, because the measured "
            "distance is longer than the true one",
        ],
        "correct_index": 3,
        "why": "The top edge is further from the baseline than the centre, "
               "so the numerator of every Rf is inflated while the solvent "
               "distance is not.",
    },
    {
        "id": "ks4-chromatography-h07",
        "subtopic_slug": "chromatography",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why chromatography can show that a substance is "
                "impure, but a single spot on its own does not prove that a "
                "substance is pure.",
        "options": [
            "Two different substances can share an Rf value in one solvent, "
            "so one spot may still be two substances",
            "A single spot always means that at least two substances must "
            "be present, whatever the solvent",
            "Chromatography can never separate a mixture into more than one "
            "spot",
            "A pure substance always gives more than one spot",
        ],
        "correct_index": 0,
        "why": "More than one spot proves a mixture; one spot only means "
               "nothing separated in THAT solvent, which is weaker evidence.",
    },
    {
        "id": "ks4-chromatography-h08",
        "subtopic_slug": "chromatography",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a finished chromatogram every spot sits close to the "
                "baseline while the solvent front is near the top. Suggest a "
                "change to the method that would separate them better, and "
                "explain.",
        "options": [
            "Use a shorter piece of paper so the spots are nearer the front",
            "Make the baseline spots much larger so they are easier to see",
            "Leave the paper in the tank far longer under the same "
            "conditions, so the spots have more time to climb",
            "Use a different solvent in which the substances are more "
            "soluble, so it carries them further up the paper",
        ],
        "correct_index": 3,
        "why": "Spots stuck at the baseline are barely dissolving in that "
               "solvent, and only a solvent they dissolve in will move them "
               "apart.",
    },
    {
        "id": "ks4-chromatography-h09",
        "subtopic_slug": "chromatography",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students run identical chromatograms. One marks the "
                "solvent front the moment the paper leaves the tank; the "
                "other waits until the paper has dried. Explain whose Rf "
                "values are trustworthy.",
        "options": [
            "The one who marked it immediately, because the wet front "
            "cannot be seen once the paper has dried",
            "The one who waited, because a dry paper gives a sharper and "
            "more accurate measurement of both distances",
            "Both are equally trustworthy, because Rf does not depend on "
            "the front",
            "Neither, because the front must be marked before the run "
            "begins",
        ],
        "correct_index": 0,
        "why": "The solvent front is only visible while the paper is damp, "
               "so waiting means guessing the distance every Rf is divided "
               "by.",
    },

    # ── testing-for-gases ─────────────────────── BASE (5.8.1.4) ── +7 ──
    {
        "id": "ks4-testing-for-gases-e05",
        "subtopic_slug": "testing-for-gases",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a sample of gas is shown to be oxygen, and "
                "give the positive result.",
        "options": [
            "A lit splint gives a squeaky pop",
            "Damp litmus paper is bleached white",
            "A glowing splint relights",
            "Limewater turns milky",
        ],
        "correct_index": 2,
        "why": "Oxygen supports combustion strongly enough to relight a "
               "splint that is only glowing.",
    },
    {
        "id": "ks4-testing-for-gases-s05",
        "subtopic_slug": "testing-for-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas does not relight a glowing splint, gives no pop with "
                "a lit splint, and turns limewater milky. Identify the gas "
                "and justify the identification.",
        "options": [
            "Oxygen, because it gave no pop",
            "Carbon dioxide, because only carbon dioxide turns limewater "
            "milky",
            "Hydrogen, because it did not relight the splint",
            "Chlorine, because it did not support combustion",
        ],
        "correct_index": 1,
        "why": "The first two results only rule gases out; the limewater is "
               "the positive test that names the gas.",
    },
    {
        "id": "ks4-testing-for-gases-s06",
        "subtopic_slug": "testing-for-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the splint used to test for hydrogen must be "
                "LIT while the splint used to test for oxygen must be "
                "GLOWING.",
        "options": [
            "Hydrogen must be ignited before it will pop, while a glowing "
            "splint shows oxygen relighting a flame",
            "A lit splint would be blown straight out by oxygen",
            "A glowing splint is not hot enough to ignite hydrogen, so the "
            "gas would never pop at all",
            "The two gases have to be tested at different temperatures",
        ],
        "correct_index": 0,
        "why": "The hydrogen test needs a flame to set the gas alight; the "
               "oxygen test needs the flame to be out, so relighting is the "
               "evidence.",
    },
    {
        "id": "ks4-testing-for-gases-s07",
        "subtopic_slug": "testing-for-gases",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium carbonate reacts with dilute hydrochloric acid. "
                "Describe the test that identifies the gas given off and the "
                "positive result.",
        "options": [
            "Hold a lit splint at the mouth of the tube; a squeaky pop is "
            "heard",
            "Hold a glowing splint in the gas; the splint relights",
            "Bubble the gas through limewater; the limewater turns milky",
            "Hold damp litmus paper in the gas; the paper is bleached",
        ],
        "correct_index": 2,
        "why": "An acid and a carbonate always give carbon dioxide, and "
               "limewater turning milky is the test that confirms it.",
    },
    {
        "id": "ks4-testing-for-gases-h05",
        "subtopic_slug": "testing-for-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas bleaches damp litmus paper and also puts out a lit "
                "splint. Deduce which gas it is and explain how the two "
                "results together identify it.",
        "options": [
            "Carbon dioxide, because it puts out a lit splint and turns "
            "damp litmus paper white",
            "Chlorine, because bleaching damp litmus is unique to it and it "
            "does not support combustion",
            "Oxygen, because it does not burn itself",
            "Hydrogen, because it burns rather than supporting burning",
        ],
        "correct_index": 1,
        "why": "Several gases put a splint out, but only chlorine bleaches "
               "damp litmus, so that result is what fixes the "
               "identification.",
    },
    {
        "id": "ks4-testing-for-gases-h06",
        "subtopic_slug": "testing-for-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calcium carbonate is heated strongly and the gas given off "
                "is bubbled through limewater. Predict the observation and "
                "determine the equation for the decomposition.",
        "options": [
            "The limewater turns milky, and CaCO3 → CaO + CO2",
            "The limewater turns milky, and CaCO3 → Ca + CO3",
            "The limewater stays clear, and CaCO3 → CaO + CO2",
            "The limewater turns milky, and CaCO3 + O2 → CaO + CO2",
        ],
        "correct_index": 0,
        "why": "Thermal decomposition of a carbonate gives the metal oxide "
               "and carbon dioxide, and the carbon dioxide is what clouds "
               "the limewater.",
    },
    {
        "id": "ks4-testing-for-gases-h07",
        "subtopic_slug": "testing-for-gases",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium reacts with dilute sulfuric acid and 48 cm3 of "
                "gas is collected in a syringe. Describe the test that "
                "identifies the gas, the result, and name the salt left in "
                "solution.",
        "options": [
            "A glowing splint relights, showing oxygen, and the salt is "
            "magnesium sulfate",
            "A lit splint gives a squeaky pop, showing hydrogen, and the "
            "salt is magnesium sulfide",
            "Limewater turns milky, showing carbon dioxide, and the salt is "
            "magnesium sulfide",
            "A lit splint gives a squeaky pop, showing hydrogen, and the "
            "salt is magnesium sulfate",
        ],
        "correct_index": 3,
        "why": "A metal and an acid give hydrogen plus a salt, and sulfuric "
               "acid always gives a sulfate.",
    },
]
