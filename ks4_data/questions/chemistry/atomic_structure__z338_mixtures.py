"""Chemistry · Atomic structure and the periodic table — mixtures and
separation techniques · the MRB-338 expansion.

Fifty-two rows on choosing and running a physical separation: filtration,
evaporation and crystallisation, simple and fractional distillation, and paper
chromatography including the Rf value. The weight falls on the choice itself —
which physical property each technique exploits, and therefore which mixture it
can and cannot touch — and on the errors that spoil a real separation: heating a
solution to dryness, a baseline drawn in ink, a baseline sitting under the
solvent, a thermometer in the wrong place.

The element/compound/mixture classification belongs to the
`atoms-elements-compounds` leaf; this leaf takes the separation angle
throughout.
"""

TOPIC = "atomic-structure"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "ks4-mixtures-e05",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mixture of iron filings and dry sand is to be separated. "
                "State the quickest method.",
        "options": [
            "Draw a magnet through the mixture",
            "Warm the mixture over a flame",
            "Shake the mixture in a stoppered tube",
            "Pour the mixture through a sieve",
        ],
        "correct_index": 0,
        "why": "Iron is magnetic and sand is not, so a magnet removes the "
               "iron and leaves the sand behind.",
    },
    {
        "id": "ks4-mixtures-e06",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is collected at the end of a crystallisation.",
        "options": [
            "The solvent, as a pure liquid",
            "The solid, as crystals",
            "The gas driven off by the heating",
            "Whichever part of the mixture would not dissolve in the solvent "
            "at the start",
        ],
        "correct_index": 1,
        "why": "Crystallisation recovers the dissolved solid as crystals once "
               "enough solvent has gone and the solution cools.",
    },
    {
        "id": "ks4-mixtures-e07",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the liquid that passes through the filter paper during "
                "a filtration.",
        "options": [
            "The residue",
            "The distillate",
            "The filtrate",
            "The solvent front",
        ],
        "correct_index": 2,
        "why": "The liquid that gets through the pores of the paper is the "
               "filtrate; the solid held back is the residue.",
    },
    {
        "id": "ks4-mixtures-e08",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the physical property that distillation makes use of.",
        "options": [
            "The size of the particles",
            "How magnetic each substance is",
            "The density of each substance",
            "The temperature at which each substance boils and turns into a "
            "vapour",
        ],
        "correct_index": 3,
        "why": "Distillation works because one substance boils at a lower "
               "temperature and so leaves as a vapour first.",
    },
    {
        "id": "ks4-mixtures-e09",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the mobile phase in paper chromatography.",
        "options": [
            "The solvent",
            "The paper",
            "The pencil line",
            "The dye spot",
        ],
        "correct_index": 0,
        "why": "The solvent is the mobile phase because it moves up the "
               "paper, carrying the dissolved substances with it.",
    },
    {
        "id": "ks4-mixtures-e10",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which technique gives pure water from sea water?",
        "options": [
            "Filtration",
            "Simple distillation",
            "Chromatography",
            "Crystallisation of the solution in an evaporating basin over a "
            "water bath",
        ],
        "correct_index": 1,
        "why": "The water boils off, travels through the condenser and is "
               "collected pure, leaving the dissolved salts in the flask.",
    },
    {
        "id": "ks4-mixtures-e11",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is left in the flask at the end of a simple "
                "distillation of salt solution.",
        "options": [
            "Pure water",
            "An empty flask",
            "The dissolved salt",
            "A mixture of salt and steam",
        ],
        "correct_index": 2,
        "why": "Only the water boils away, so the salt that was dissolved in "
               "it stays behind in the flask.",
    },
    {
        "id": "ks4-mixtures-e12",
        "subtopic_slug": "mixtures",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the baseline on a chromatography paper is drawn "
                "in pencil.",
        "options": [
            "Pencil is easier to see once the paper is wet, because graphite "
            "darkens",
            "Pencil dries faster than ink does, so the baseline is ready to "
            "use sooner",
            "Pencil marks do not tear the paper when the line is ruled across "
            "it",
            "Pencil graphite does not dissolve in the solvent, so it cannot "
            "travel up the paper and confuse the result",
        ],
        "correct_index": 3,
        "why": "Ink would dissolve and separate into its own spots, whereas "
               "insoluble pencil graphite stays exactly where it was drawn.",
    },
    # ── standard ────────────────────────────────────────────────────
    {
        "id": "ks4-mixtures-s05",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a hot saturated solution is cooled slowly rather "
                "than quickly when crystals are wanted.",
        "options": [
            "Slow cooling lets the solid come out of solution gradually, so "
            "larger regular crystals grow",
            "Slow cooling keeps the solution warm for longer, and warm "
            "crystals are larger than cold ones are",
            "Slow cooling stops the solvent evaporating",
            "Slow cooling makes the solid more soluble",
        ],
        "correct_index": 0,
        "why": "Solubility falls gradually as the temperature falls, so the "
               "solid is deposited slowly and builds well-formed crystals.",
    },
    {
        "id": "ks4-mixtures-s06",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two liquids that mix together boil at 78 degrees C and "
                "118 degrees C. State the technique that separates them.",
        "options": [
            "Filtration through a fine paper",
            "Fractional distillation in a tall column",
            "Crystallisation by slow cooling",
            "Paper chromatography in a covered beaker",
        ],
        "correct_index": 1,
        "why": "Two miscible liquids with different boiling points are "
               "separated in a fractionating column.",
    },
    {
        "id": "ks4-mixtures-s07",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a fractionating column is cooler at the top than "
                "at the bottom.",
        "options": [
            "So that the column does not crack",
            "So that the heat is used up before it can escape the apparatus "
            "and warm the laboratory around it",
            "So that a vapour must be cool enough to reach the top, which "
            "sorts the substances by boiling point",
            "So that the liquid can be poured in at the top",
        ],
        "correct_index": 2,
        "why": "A vapour with a higher boiling point condenses lower down, so "
               "only the lowest-boiling substance reaches the top.",
    },
    {
        "id": "ks4-mixtures-s08",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a lid is placed on the beaker during a paper "
                "chromatography experiment.",
        "options": [
            "To keep the paper from falling over into the solvent below and "
            "spoiling the spots that have been drawn on it",
            "To keep the laboratory air out of the beaker",
            "To hold the paper at the correct height",
            "To stop the solvent evaporating, which would slow the solvent "
            "front and spoil the Rf values",
        ],
        "correct_index": 3,
        "why": "Evaporation from the paper would stop the solvent front "
               "rising evenly, so the distances measured would be wrong.",
    },
    {
        "id": "ks4-mixtures-s09",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the stationary phase in paper "
                "chromatography.",
        "options": [
            "The paper, which does not move while the solvent rises through it",
            "The spot that fails to move",
            "The lid on the beaker",
            "The solvent in the beaker",
        ],
        "correct_index": 0,
        "why": "The paper is the stationary phase: substances are held on it "
               "to differing extents while the solvent travels past.",
    },
    {
        "id": "ks4-mixtures-s10",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A school needs both the pure water and the dissolved solid "
                "recovered from a copper sulfate solution. State the "
                "technique to use.",
        "options": [
            "Filtration, because it keeps the solid and lets the liquid "
            "through the paper into a beaker underneath",
            "Simple distillation, because the water is collected as it "
            "condenses and the solid stays behind",
            "Evaporation over a flame",
            "Chromatography in a tall beaker",
        ],
        "correct_index": 1,
        "why": "Distillation is the only one of these that keeps both parts: "
               "the condensed water and the residue in the flask.",
    },
    {
        "id": "ks4-mixtures-s11",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a chromatography experiment a spot moved 3.6 cm while "
                "the solvent front moved 9.0 cm. Calculate the Rf value of "
                "the spot.",
        "options": [
            "0.25",
            "2.50",
            "0.40",
            "5.40",
        ],
        "correct_index": 2,
        "why": "Rf is the distance moved by the substance divided by the "
               "distance moved by the solvent front, so 3.6 / 9.0 = 0.40.",
    },
    {
        "id": "ks4-mixtures-s12",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an Rf value is written without a unit.",
        "options": [
            "Because the unit is understood to be centimetres, so writing it "
            "out each time would add nothing to the number",
            "Because the value is a percentage",
            "Because the value is too small to need one",
            "Because one distance is divided by another, so the units cancel",
        ],
        "correct_index": 3,
        "why": "Dividing a length in centimetres by another length in "
               "centimetres leaves a pure ratio with no unit attached.",
    },
    {
        "id": "ks4-mixtures-s13",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rock salt is a mixture of salt and sand. State the first "
                "step in separating it.",
        "options": [
            "Stir the rock salt into water",
            "Distil the rock salt",
            "Run a magnet through it",
            "Heat the rock salt strongly",
        ],
        "correct_index": 0,
        "why": "Water dissolves the salt but not the sand, which is what "
               "makes the two separable by filtration afterwards.",
    },
    {
        "id": "ks4-mixtures-s14",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student boils a copper sulfate solution dry over a strong "
                "flame and gets a dull powder rather than crystals. Explain "
                "why.",
        "options": [
            "The solid was driven off with the steam, so what is left in the "
            "basin is a different compound altogether",
            "The solid came out too fast for regular crystals to grow",
            "The solid dissolved again in the steam",
            "The solid needed a seed crystal",
        ],
        "correct_index": 1,
        "why": "Removing the solvent quickly gives the solid no time to build "
               "an ordered lattice, so it is deposited as a fine powder.",
    },
    {
        "id": "ks4-mixtures-s15",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why paper chromatography cannot separate a mixture "
                "of two insoluble powders.",
        "options": [
            "The powders would be too heavy for the paper to hold up while "
            "the solvent was climbing past them",
            "The powders would react with the solvent instead of moving",
            "The solvent cannot carry a substance that will not dissolve in "
            "it",
            "The paper's pores would be blocked by the powders",
        ],
        "correct_index": 2,
        "why": "Chromatography separates dissolved substances, so a substance "
               "that does not dissolve simply stays on the baseline.",
    },
    {
        "id": "ks4-mixtures-s16",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Liquid air is separated into nitrogen, oxygen and argon. "
                "State the technique used.",
        "options": [
            "Simple distillation",
            "Crystallisation",
            "Filtration",
            "Fractional distillation",
        ],
        "correct_index": 3,
        "why": "The three gases have different but fairly close boiling "
               "points, so a fractionating column is needed.",
    },
    {
        "id": "ks4-mixtures-s17",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how filter paper separates an insoluble solid from "
                "a liquid.",
        "options": [
            "The paper's pores let the small liquid particles through but "
            "hold back the larger solid pieces",
            "The paper dissolves the solid, letting the liquid run on into "
            "the beaker placed below the funnel",
            "The paper attracts the liquid and repels any solid that touches "
            "its surface on the way through",
            "The paper holds the denser of the two",
        ],
        "correct_index": 0,
        "why": "Separation is by particle size: the liquid particles fit "
               "through the pores and the solid lumps do not.",
    },
    {
        "id": "ks4-mixtures-s18",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what would be seen if a student drew the "
                "chromatography baseline in blue ballpoint ink.",
        "options": [
            "The ink would stay put and mark the baseline clearly all the "
            "way through the experiment as planned",
            "The ink would separate into its own spots and confuse the "
            "chromatogram",
            "The ink would react with the solvent and give off a gas that "
            "lifted the paper away from the beaker wall",
            "The ink would block the paper's pores",
        ],
        "correct_index": 1,
        "why": "Ballpoint ink is itself a mixture of soluble dyes, so it "
               "would travel up the paper and produce spots of its own.",
    },
    {
        "id": "ks4-mixtures-s19",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Copper sulfate crystals are wanted from a mixture of copper "
                "sulfate and sand. Describe the correct order of techniques.",
        "options": [
            "Filter the dry mixture straight away, then crystallise the sand "
            "that has collected in the filter paper funnel",
            "Distil the mixture, then filter the residue left in the flask",
            "Add water, filter off the sand, then crystallise the filtrate "
            "by gentle heating and slow cooling",
            "Crystallise the whole mixture, then filter out the crystals",
        ],
        "correct_index": 2,
        "why": "Dissolving lets the sand be filtered out, and crystallising "
               "the filtrate then recovers the copper sulfate as crystals.",
    },
    {
        "id": "ks4-mixtures-s20",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a distillation the thermometer bulb is placed level with "
                "the side arm of the flask. Explain why.",
        "options": [
            "So that the bulb is kept out of the boiling liquid, which would "
            "otherwise crack the glass of the thermometer itself",
            "So that the thermometer can be read from across the laboratory "
            "bench without the apparatus being disturbed",
            "So that the bulb stays cool enough to be handled at the end",
            "So that it reads the temperature of the vapour leaving the flask",
        ],
        "correct_index": 3,
        "why": "The useful temperature is that of the vapour on its way to "
               "the condenser, because that is what identifies the fraction.",
    },
    {
        "id": "ks4-mixtures-s21",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which mixture could be separated simply by letting it stand "
                "and then pouring the liquid off?",
        "options": [
            "Sand settled under water",
            "Salt dissolved in water",
            "Ethanol mixed with water",
            "Two dyes dissolved in water",
        ],
        "correct_index": 0,
        "why": "Decanting works when a dense insoluble solid settles out, "
               "leaving a clear liquid that can be poured away.",
    },
    {
        "id": "ks4-mixtures-s22",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the residue in a filtration is rinsed with "
                "distilled water before it is dried.",
        "options": [
            "To cool the solid down before it is weighed",
            "To wash away solution still clinging to the solid, which would "
            "otherwise dry onto it as an impurity",
            "To make the solid heavier so that the balance reading is easier "
            "to take and to record accurately",
            "To dissolve any sand left in the funnel",
        ],
        "correct_index": 1,
        "why": "Trapped solution would leave its dissolved solute behind on "
               "drying, so rinsing is what makes the residue pure.",
    },
    {
        "id": "ks4-mixtures-s23",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ethanol boils at 78 degrees C and water at 100 degrees C. "
                "Explain why simple distillation gives an impure ethanol.",
        "options": [
            "Ethanol is impossible to distil",
            "Ethanol reacts with water on heating and makes a third liquid "
            "that then distils across with it into the receiver",
            "Some water evaporates as well, so water vapour is carried over "
            "with the ethanol",
            "Ethanol condenses before it reaches the condenser",
        ],
        "correct_index": 2,
        "why": "Water evaporates below its boiling point too, so a single "
               "evaporation and condensation cannot separate the two fully.",
    },
    {
        "id": "ks4-mixtures-s24",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the piece of apparatus that turns the vapour back into "
                "a liquid during a distillation.",
        "options": [
            "The funnel",
            "The evaporating basin",
            "The fractionating column",
            "The condenser",
        ],
        "correct_index": 3,
        "why": "The condenser is surrounded by cold water, which cools the "
               "vapour until it condenses and runs into the receiver.",
    },
    {
        "id": "ks4-mixtures-s25",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why two dyes in the same ink travel different "
                "distances up the chromatography paper.",
        "options": [
            "They are held by the paper and carried by the solvent to "
            "different extents",
            "They were placed at slightly different heights on the baseline "
            "when the spot was first drawn onto the paper",
            "They have different colours, and a darker colour marks out the "
            "heavier of any two dyes in a mixture",
            "They have different masses, and the heavier one sinks",
        ],
        "correct_index": 0,
        "why": "A dye that is more strongly attracted to the moving solvent "
               "and less strongly held by the paper travels further.",
    },
    {
        "id": "ks4-mixtures-s26",
        "subtopic_slug": "mixtures",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare evaporation and crystallisation as ways of getting "
                "a dissolved solid back from its solution.",
        "options": [
            "Evaporation gives crystals and crystallisation gives a powder, "
            "because cooling never lets a lattice form properly",
            "Evaporation removes all the solvent and leaves a powder; "
            "crystallisation cools a concentrated solution and gives crystals",
            "Both recover the solvent",
            "Neither can recover the solid",
        ],
        "correct_index": 1,
        "why": "The difference is how fast the solid comes out of solution, "
               "and that is what decides whether crystals can grow.",
    },
    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "ks4-mixtures-h05",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that filtering muddy river water would "
                "make it safe to drink. Evaluate this claim.",
        "options": [
            "Sound, because filtration removes every substance that does not "
            "belong in water and leaves it clean",
            "Sound, because the mud was the only substance in the water",
            "Unsound, because filtration leaves dissolved substances and "
            "microbes in the filtrate",
            "Unsound, because filtration would remove the water as well",
        ],
        "correct_index": 2,
        "why": "Filtration only takes out the insoluble solid, so anything "
               "dissolved in the water passes straight through with it.",
    },
    {
        "id": "ks4-mixtures-h06",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A technician records that a pigment has moved 6.0 cm and "
                "reports its Rf as 0.80. Determine how far the solvent front "
                "had moved.",
        "options": [
            "4.8 cm",
            "6.8 cm",
            "13.3 cm",
            "7.5 cm",
        ],
        "correct_index": 3,
        "why": "Rearranging Rf = substance / front gives front = 6.0 / 0.80.",
    },
    {
        "id": "ks4-mixtures-h07",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mixture contains powdered chalk, which does not dissolve, "
                "and potassium nitrate, which does. Describe how to recover "
                "both solids pure.",
        "options": [
            "Add water, filter off the chalk, then crystallise the filtrate",
            "Heat the mixture strongly until the chalk burns away and only "
            "the potassium nitrate is left behind in the dish",
            "Distil the mixture, then filter the distillate to collect the "
            "chalk that has been carried over with the vapour",
            "Add water and then simply let the two solids settle out",
        ],
        "correct_index": 0,
        "why": "One solid dissolves and the other does not, so filtration "
               "separates them and crystallisation recovers the dissolved one.",
    },
    {
        "id": "ks4-mixtures-h08",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what a high Rf value tells you about a substance in "
                "a given solvent.",
        "options": [
            "It is the densest substance present, so gravity slows it least",
            "It dissolves readily in the solvent and is held only weakly by "
            "the paper, so it travels a long way",
            "It is present in the largest amount, so its spot is carried "
            "furthest up the paper",
            "It has the darkest colour of the spots, and a dark dye travels "
            "faster than a pale one",
        ],
        "correct_index": 1,
        "why": "A high Rf means the substance moved almost as far as the "
               "solvent front, which happens when the solvent carries it "
               "easily.",
    },
    {
        "id": "ks4-mixtures-h09",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to the results if the solvent is left "
                "until it reaches the very top edge of the paper.",
        "options": [
            "The spots would be washed off the top edge of the paper and "
            "into the air above the beaker entirely",
            "Nothing would change, because a spot stops moving on its own "
            "once it has finished separating from the others",
            "The solvent front could no longer be measured, so no Rf value "
            "could be worked out",
            "The Rf values would all come out as zero",
        ],
        "correct_index": 2,
        "why": "An Rf value needs a measurable solvent front, and once the "
               "solvent reaches the edge that distance is no longer known.",
    },
    {
        "id": "ks4-mixtures-h10",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the fraction collected near the top of a crude oil "
                "fractionating column with the one collected near the bottom.",
        "options": [
            "The top fraction has the higher boiling point and the larger "
            "molecules, since heat rises through the column as it works",
            "Both fractions have the same boiling point but different "
            "colours, which is how a refinery tells them apart on sight",
            "The top fraction is a compound while the bottom fraction is "
            "still a mixture of many hydrocarbons",
            "The top fraction has the lower boiling point and the smaller "
            "molecules",
        ],
        "correct_index": 3,
        "why": "Only substances that stay as a vapour in the cooler upper "
               "column reach the top, and those are the smaller molecules.",
    },
    {
        "id": "ks4-mixtures-h11",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two liquids in a mixture boil at 56 degrees C and "
                "57 degrees C. Suggest why even fractional distillation "
                "separates them poorly.",
        "options": [
            "Their boiling points are so close that both are vapours "
            "together at almost every height in the column",
            "Liquids boiling below 60 degrees C cannot be distilled",
            "The column would have to be cooled below room temperature "
            "before either of the two liquids could be made to condense",
            "One of them would decompose",
        ],
        "correct_index": 0,
        "why": "Fractional distillation relies on one vapour condensing "
               "before the other, and a one degree difference barely does "
               "that.",
    },
    {
        "id": "ks4-mixtures-h12",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 60 g sample of rock salt yields 48 g of pure salt after "
                "separation. Calculate the percentage of sand in the sample.",
        "options": [
            "12%",
            "20%",
            "25%",
            "80%",
        ],
        "correct_index": 1,
        "why": "The sand is 60 g - 48 g = 12 g, and 12 / 60 x 100 gives the "
               "percentage.",
    },
    {
        "id": "ks4-mixtures-h13",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cooling water enters a condenser at the end furthest from "
                "the flask. Suggest why it is connected this way round.",
        "options": [
            "Because the water would leak out of the other end if it were "
            "connected the other way round instead",
            "Because warm water cools a vapour faster than cold water does, "
            "so the inlet must be the warmer end of the condenser",
            "So that the coldest water meets the vapour last, giving the "
            "most efficient cooling along the whole tube",
            "So that the water flows downhill",
        ],
        "correct_index": 2,
        "why": "Running the water against the vapour flow keeps a temperature "
               "difference along the whole condenser, so more vapour "
               "condenses.",
    },
    {
        "id": "ks4-mixtures-h14",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'One separation technique will always give "
                "pure substances from any mixture.' Evaluate this statement.",
        "options": [
            "Sound, because a technique is chosen precisely so that it will "
            "finish the whole job in a single step",
            "Sound, because a mixture has only two components",
            "Unsound, because no technique gives anything pure",
            "Unsound, because rock salt needs dissolving, filtering and then "
            "crystallising",
        ],
        "correct_index": 3,
        "why": "A mixture of several components usually needs the techniques "
               "used in sequence, each exploiting a different property.",
    },
    {
        "id": "ks4-mixtures-h15",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a melting point measurement shows whether a "
                "separation has worked.",
        "options": [
            "A pure substance melts sharply at one temperature, while a "
            "mixture softens across a range of temperatures",
            "A pure substance melts at a higher temperature than a mixture "
            "does",
            "A pure substance will not melt until it has been heated well "
            "past its boiling point",
            "A mixture melts more quickly because its particles are packed "
            "less tightly together",
        ],
        "correct_index": 0,
        "why": "A sharp melting point is the standard evidence of purity, so "
               "a range remaining shows the separation is incomplete.",
    },
    {
        "id": "ks4-mixtures-h16",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why rock salt is crushed before water is added to "
                "it.",
        "options": [
            "Crushing makes the sand dissolve as well, so that both parts "
            "end up in the solution together and can be poured off",
            "Crushing gives a larger surface area, so the salt dissolves "
            "faster",
            "Crushing warms the sample up, and a warm solid dissolves in "
            "cold water far more readily than a cold one does",
            "Crushing turns the salt into a liquid",
        ],
        "correct_index": 1,
        "why": "More of the salt is exposed to the water at once, so it "
               "dissolves more quickly and less is trapped inside lumps.",
    },
    {
        "id": "ks4-mixtures-h17",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chromatogram of a food colouring shows one spot. Deduce "
                "what this suggests about the colouring.",
        "options": [
            "That it contains at least two dyes of very similar colour",
            "That it failed to dissolve in the solvent",
            "That it is likely to be a single substance in this solvent",
            "That the solvent was the wrong one to have chosen for this "
            "particular separation of dyes",
        ],
        "correct_index": 2,
        "why": "A single spot means nothing separated out, which is the "
               "expected result for one substance rather than a mixture.",
    },
    {
        "id": "ks4-mixtures-h18",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dye dissolved in water must be removed so that the water "
                "itself is recovered clean. State the technique.",
        "options": [
            "Filtration",
            "Crystallisation",
            "Chromatography",
            "Simple distillation",
        ],
        "correct_index": 3,
        "why": "Boiling the water off and condensing it leaves the dye behind "
               "and delivers the water pure.",
    },
    {
        "id": "ks4-mixtures-h19",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why air must be cooled until it is a liquid before "
                "its gases can be separated by fractional distillation.",
        "options": [
            "Because a gas mixture has no boiling points to exploit until it "
            "is a liquid that can be boiled again in stages",
            "Because a gas has to be made liquid before it can be poured "
            "into the top of the fractionating column in one go",
            "Because cooling changes nitrogen into a compound that then "
            "boils at a quite different temperature from oxygen",
            "Because liquids are easier to store",
        ],
        "correct_index": 0,
        "why": "Fractional distillation works by boiling a liquid mixture, so "
               "the gases must first be condensed into one.",
    },
    {
        "id": "ks4-mixtures-h20",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student filters 50.0 g of a sand and water mixture and "
                "collects 41.0 g of filtrate. Determine the mass of the wet "
                "residue.",
        "options": [
            "4.5 g",
            "9.0 g",
            "41.0 g",
            "91.0 g",
        ],
        "correct_index": 1,
        "why": "Nothing is created or destroyed by filtering, so the residue "
               "is 50.0 g - 41.0 g.",
    },
    {
        "id": "ks4-mixtures-h21",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that chromatography on its own proves "
                "which substance a spot is.",
        "options": [
            "Sound, because an Rf value is unique to one single substance "
            "whichever solvent has been used to run it",
            "Sound, because the colour of the spot identifies the substance",
            "Unsound, because an Rf value must be compared with a known "
            "reference run in the same solvent",
            "Unsound, because Rf values change at random from one run to the "
            "next",
        ],
        "correct_index": 2,
        "why": "An Rf value only means something against a standard measured "
               "under identical conditions, since the solvent changes it.",
    },
    {
        "id": "ks4-mixtures-h22",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates an Rf value of 1.4. Suggest the error "
                "that has been made.",
        "options": [
            "The spot was too concentrated",
            "The paper was left in the solvent for too long a time, so the "
            "spot overtook the solvent that was carrying it up the paper",
            "The solvent front was measured from the wrong edge of the paper "
            "rather than from the pencil baseline that was drawn on it",
            "The two distances were divided the wrong way round",
        ],
        "correct_index": 3,
        "why": "A spot cannot outrun the solvent carrying it, so Rf is never "
               "above 1 and a value of 1.4 means the division was inverted.",
    },
    {
        "id": "ks4-mixtures-h23",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the term used for each separate liquid collected at a "
                "different height of a fractionating column.",
        "options": [
            "A fraction",
            "A filtrate",
            "A residue",
            "A phase",
        ],
        "correct_index": 0,
        "why": "Each liquid collected over a particular temperature range is "
               "called a fraction, which is where the technique's name comes "
               "from.",
    },
    {
        "id": "ks4-mixtures-h24",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why distilled water rather than tap water is used "
                "to make up a solution for an accurate experiment.",
        "options": [
            "Distilled water is denser, so a measured volume of it contains "
            "more water than the same volume of tap water would",
            "Tap water is a mixture containing dissolved solids that would "
            "add to the results",
            "Distilled water boils at a lower temperature, which makes any "
            "later evaporation step run faster than it otherwise would",
            "Tap water is too cold to dissolve a solid",
        ],
        "correct_index": 1,
        "why": "Tap water carries dissolved salts of its own, and those would "
               "be recovered along with whatever the experiment set out to "
               "measure.",
    },
    {
        "id": "ks4-mixtures-h25",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what the thermometer reads while a pure liquid is "
                "distilling steadily.",
        "options": [
            "It climbs steadily throughout, because the flame keeps adding "
            "energy to the liquid the whole time it is distilling",
            "It falls as the liquid level drops, because there is less and "
            "less liquid left in the flask to be heated by the flame",
            "It holds roughly constant at the liquid's boiling point",
            "It swings up and down repeatedly",
        ],
        "correct_index": 2,
        "why": "A pure liquid boils at one temperature, so the vapour leaving "
               "the flask stays at that temperature until the flask is dry.",
    },
    {
        "id": "ks4-mixtures-h26",
        "subtopic_slug": "mixtures",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that getting two spots from a sample proves "
                "the sample was a compound. Evaluate this claim.",
        "options": [
            "Sound, because a compound holds two different elements and each "
            "one of them will travel its own distance up the paper",
            "Sound, because compounds separate on paper",
            "Unsound, because chromatography cannot give two spots from one "
            "baseline spot however many dyes are present in the sample",
            "Unsound, because two spots show two substances were present, "
            "which makes the sample a mixture",
        ],
        "correct_index": 3,
        "why": "Chromatography separates substances, not the elements inside "
               "a compound, so two spots mean two substances were mixed.",
    },
]
