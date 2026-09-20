"""Chemistry · Using resources — the MRB-338 expansion for `haber-process`.

The shipped rows state the temperature, the catalyst and the raw materials and
ask once why a colder reactor would be too slow. The weight here therefore falls
on the half of the compromise those rows leave out — the pressure, why 200 atm
and not 400, and why an exothermic forward reaction makes yield and rate pull
against each other in the first place.

Round that sit the things a plant operator deals with: steam reforming methane
and removing the carbon monoxide, why the ammonia condenses out while nitrogen
and hydrogen do not, why a catalyst can change the rate without touching the
yield, and why the vessel is thick steel. Four rows carry arithmetic on the
equation N2 + 3H2 in both directions, plus a percentage yield and a percentage
by mass.
"""

TOPIC = "resources"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": "ks4-haber-process-e05",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the pressure used in the Haber process.",
        "options": [
            "About 200 atmospheres",
            "About 2 atmospheres",
            "About 20 atmospheres",
            "About 20 000 atmospheres",
        ],
        "correct_index": 0,
        "why": "The process runs at roughly 200 atmospheres, high enough to "
               "improve the yield without the cost of a stronger vessel.",
    },
    {
        "id": "ks4-haber-process-e06",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give the chemical formula of ammonia.",
        "options": [
            "NH4",
            "NH3",
            "N2H4",
            "N3H",
        ],
        "correct_index": 1,
        "why": "Ammonia is NH3: one nitrogen atom joined to three hydrogen "
               "atoms.",
    },
    {
        "id": "ks4-haber-process-e07",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "What does the symbol used in place of an arrow in the Haber "
                "equation tell you about the reaction?",
        "options": [
            "It needs a catalyst to be added before it can start reacting",
            "It gives out heat energy to its surroundings",
            "It happens in both directions at the same time",
            "It takes in heat energy from its surroundings",
        ],
        "correct_index": 2,
        "why": "The double arrow marks a reversible reaction: products turn "
               "back into reactants at the same time as reactants turn into "
               "products.",
    },
    {
        "id": "ks4-haber-process-e08",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Most of the ammonia made in industry is used to make which "
                "kind of product?",
        "options": [
            "Fuels for aircraft engines",
            "Glass for bottles and windows",
            "Paints for outside woodwork",
            "Fertilisers for growing crops",
        ],
        "correct_index": 3,
        "why": "Ammonia is the starting point for the ammonium salts that "
               "make up nitrogen fertilisers, which take the large majority "
               "of world production.",
    },
    {
        "id": "ks4-haber-process-e09",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which gas is reacted with steam to make the hydrogen for the "
                "Haber process?",
        "options": [
            "Chlorine",
            "Methane",
            "Oxygen",
            "Argon",
        ],
        "correct_index": 1,
        "why": "Methane from natural gas is reformed with steam, which gives "
               "hydrogen together with carbon monoxide.",
    },
    {
        "id": "ks4-haber-process-e10",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Roughly what percentage of the air is nitrogen?",
        "options": [
            "About 21%",
            "About 50%",
            "About 78%",
            "About 96%",
        ],
        "correct_index": 2,
        "why": "Nitrogen makes up about 78% of dry air, which is why air is "
               "the cheapest source of it.",
    },
    {
        "id": "ks4-haber-process-e11",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "The forward reaction that makes ammonia gives out energy. "
                "What name is given to a reaction like this?",
        "options": [
            "Endothermic",
            "Neutralisation",
            "Electrolytic",
            "Exothermic",
        ],
        "correct_index": 3,
        "why": "A reaction that transfers energy out to the surroundings is "
               "exothermic; for this one the value is about 92 kJ per mole.",
    },
    {
        "id": "ks4-haber-process-e12",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In the Haber equation, how many molecules of hydrogen react "
                "with one molecule of nitrogen?",
        "options": [
            "Three",
            "One",
            "Two",
            "Six",
        ],
        "correct_index": 0,
        "why": "The balanced equation is N2 + 3H2, so nitrogen and hydrogen "
               "react in a 1 : 3 ratio.",
    },
    {
        "id": "ks4-haber-process-e13",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "What effect does the iron catalyst have inside the reactor?",
        "options": [
            "It lets the mixture reach equilibrium sooner",
            "It removes the ammonia as soon as it forms",
            "It stops the reverse reaction taking place",
            "It raises the temperature of the gas inside the reactor",
        ],
        "correct_index": 0,
        "why": "A catalyst gives the reaction a faster route, so equilibrium "
               "is reached in far less time.",
    },
    {
        "id": "ks4-haber-process-e14",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Ammonia can gain a hydrogen ion to form NH4+. What is this "
                "ion called?",
        "options": [
            "The nitrate ion",
            "The ammonium ion",
            "The nitride ion",
            "The amide ion",
        ],
        "correct_index": 1,
        "why": "NH4+ is the ammonium ion, and it is the ion in every "
               "ammonium salt made from the ammonia this process produces.",
    },
    {
        "id": "ks4-haber-process-e15",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give one environmental drawback of getting the hydrogen for "
                "the Haber process from natural gas.",
        "options": [
            "It uses up the last of the world's fresh water",
            "It releases carbon dioxide into the atmosphere",
            "It makes the ammonia produced slightly acidic",
            "It releases chlorine gas into the atmosphere",
        ],
        "correct_index": 1,
        "why": "Reforming methane turns the carbon in the fuel into carbon "
               "dioxide, which is released rather than being built into the "
               "product.",
    },
    {
        "id": "ks4-haber-process-e16",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Give one reason why iron is a good industrial choice of "
                "catalyst.",
        "options": [
            "It reacts with nitrogen to form ammonia",
            "It dissolves in the ammonia that the reactor produces",
            "It is cheap and there is plenty of it",
            "It is used up in the reaction, so none is wasted",
        ],
        "correct_index": 2,
        "why": "Iron is abundant and inexpensive, so the catalyst adds little "
               "to the running cost of the plant.",
    },
    {
        "id": "ks4-haber-process-e17",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Steam reforming of methane makes hydrogen together with one "
                "other gas, which has to be removed. Name that gas.",
        "options": [
            "Sulfur dioxide",
            "Nitrogen dioxide",
            "Ammonia",
            "Carbon monoxide",
        ],
        "correct_index": 3,
        "why": "Methane and steam give carbon monoxide and hydrogen, and the "
               "carbon monoxide is taken out before the hydrogen reaches the "
               "reactor.",
    },
    {
        "id": "ks4-haber-process-e18",
        "subtopic_slug": "haber-process",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one safety hazard of running the Haber process.",
        "options": [
            "The gas mixture is at a very high pressure",
            "The iron catalyst gives off a poisonous gas",
            "The reaction takes in heat and freezes the pipes solid",
            "The nitrogen used is highly flammable in air",
        ],
        "correct_index": 0,
        "why": "Containing gas at around 200 atmospheres needs thick vessels "
               "and careful maintenance, because a failure would release the "
               "contents violently.",
    },
    # -------------------------------------------------------------- standard
    {
        "id": "ks4-haber-process-s05",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a high pressure increases the amount of ammonia "
                "present at equilibrium.",
        "options": [
            "There are fewer gas molecules on the ammonia side",
            "There are more gas molecules on the ammonia side",
            "Pressure makes the iron catalyst work far better",
            "Pressure lowers the temperature inside the reactor vessel",
        ],
        "correct_index": 0,
        "why": "Four molecules of gas react to give two, so squeezing the "
               "mixture favours the side that takes up less volume.",
    },
    {
        "id": "ks4-haber-process-s06",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In the Haber process, nitrogen and hydrogen form ammonia and "
                "nothing else. State the atom economy of the reaction.",
        "options": [
            "About 15%, the share of the gas converted each pass",
            "About 50%, since two gases combine to give one",
            "100%, because every atom ends up in the ammonia",
            "About 98%, which is the plant's overall yield",
        ],
        "correct_index": 2,
        "why": "Ammonia is the only product, so the whole mass of the nitrogen "
               "and the hydrogen ends up in it. The conversion per pass and "
               "the overall yield are a different measure.",
    },
    {
        "id": "ks4-haber-process-s07",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student expects that using twice as much iron catalyst "
                "will give twice as much ammonia at equilibrium. Identify the "
                "error.",
        "options": [
            "A catalyst is used up, so doubling it will double the reaction "
            "time",
            "A catalyst changes the rate and never the equilibrium amount",
            "A catalyst works only on the reverse reaction, not both",
            "A catalyst has to be heated before it has any effect",
        ],
        "correct_index": 1,
        "why": "Catalysts change how quickly equilibrium is reached and "
               "nothing about where it lies, so the amount of ammonia at "
               "equilibrium is the same.",
    },
    {
        "id": "ks4-haber-process-s08",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain what chemists mean when they call the conditions in "
                "an ammonia plant a compromise.",
        "options": [
            "Every condition is set to the cheapest possible value",
            "Each condition trades yield against rate or against cost",
            "The conditions are changed from one hour to the next",
            "Two companies agreed the same conditions between them",
        ],
        "correct_index": 1,
        "why": "No single set of conditions gives the best yield, the fastest "
               "rate and the lowest cost at once, so each is set where the "
               "overall gain is greatest.",
    },
    {
        "id": "ks4-haber-process-s09",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the maximum mass of ammonia that could be made "
                "from 28 tonnes of nitrogen with excess hydrogen. Relative "
                "formula masses: N2 = 28, NH3 = 17.",
        "options": [
            "17 tonnes",
            "56 tonnes",
            "68 tonnes",
            "34 tonnes",
        ],
        "correct_index": 3,
        "why": "28 tonnes of N2 is one relative formula mass in tonnes, and "
               "each N2 gives 2NH3, so the maximum is 2 x 17 = 34 tonnes.",
    },
    {
        "id": "ks4-haber-process-s10",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the mass of hydrogen needed to react completely "
                "with 28 tonnes of nitrogen. Relative formula masses: N2 = "
                "28, H2 = 2.",
        "options": [
            "6 tonnes",
            "2 tonnes",
            "3 tonnes",
            "84 tonnes",
        ],
        "correct_index": 0,
        "why": "One N2 needs 3H2, so 28 tonnes of nitrogen needs 3 x 2 = 6 "
               "tonnes of hydrogen.",
    },
    {
        "id": "ks4-haber-process-s11",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why ammonia turns to a liquid as the mixture is "
                "cooled while the other two gases stay as gases.",
        "options": [
            "Ammonia is the only one of the three that is a mixture",
            "Ammonia has a much higher boiling point than they have",
            "Ammonia is denser, so it sinks to the base of the vessel",
            "Ammonia reacts with the cold metal walls of the condenser pipes",
        ],
        "correct_index": 1,
        "why": "Ammonia boils at about -33 degrees C while nitrogen and "
               "hydrogen boil far lower, so cooling condenses ammonia alone.",
    },
    {
        "id": "ks4-haber-process-s12",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why an ammonia plant is usually built beside a "
                "natural gas supply.",
        "options": [
            "Natural gas is the raw material the hydrogen comes from",
            "Natural gas is needed to cool the reactor down again",
            "Natural gas reacts with the nitrogen taken from the air",
            "Natural gas is a by-product the plant has to get rid of",
        ],
        "correct_index": 0,
        "why": "Hydrogen is made on site by reforming methane, so putting the "
               "plant at the gas supply removes the cost of moving either.",
    },
    {
        "id": "ks4-haber-process-s13",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the gas leaving the reactor always contains "
                "nitrogen and hydrogen as well as ammonia.",
        "options": [
            "The catalyst holds some of the gas back inside its own pores",
            "The gases are pumped in faster than they can react",
            "The reaction is reversible, so it reaches a balance",
            "The reactor is not hot enough for the gases to react",
        ],
        "correct_index": 2,
        "why": "In a reversible reaction ammonia breaks down as fast as it "
               "forms once equilibrium is reached, so some reactant is always "
               "left.",
    },
    {
        "id": "ks4-haber-process-s14",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how using a catalyst allows an ammonia plant to run "
                "at a lower temperature than it otherwise could.",
        "options": [
            "It raises the yield, so less heating is needed to reach it",
            "It gives an acceptable rate at a cooler temperature",
            "It cools the reactor down by taking in heat",
            "It burns methane, which warms the incoming gases up",
        ],
        "correct_index": 1,
        "why": "Without a catalyst an acceptable rate would need a much "
               "hotter reactor, and a hotter reactor would give a poorer "
               "yield of ammonia.",
    },
    {
        "id": "ks4-haber-process-s15",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why taking the ammonia out of the mixture as a "
                "liquid helps the plant make more of it.",
        "options": [
            "Removing it stops the reverse reaction using it up",
            "Removing it raises the temperature of the mixture",
            "Removing it makes the catalyst last a great deal longer",
            "Removing it raises the pressure inside the reactor",
        ],
        "correct_index": 0,
        "why": "Ammonia taken out of the system cannot break down again, so "
               "more nitrogen and hydrogen go on to react when the gas is "
               "returned.",
    },
    {
        "id": "ks4-haber-process-s16",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Calculate the percentage by mass of nitrogen in ammonia. "
                "Relative atomic masses: H = 1, N = 14.",
        "options": [
            "17.6%",
            "25.0%",
            "82.4%",
            "46.7%",
        ],
        "correct_index": 2,
        "why": "The formula mass is 17, of which nitrogen is 14, so 14 / 17 = "
               "0.824, which is 82.4%.",
    },
    {
        "id": "ks4-haber-process-s17",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why oxygen must be taken out of the air before the "
                "nitrogen is fed into the reactor.",
        "options": [
            "Oxygen would react with the hydrogen instead of nitrogen",
            "Oxygen would turn the ammonia into a solid",
            "Oxygen would lower the pressure inside the reactor",
            "Oxygen would react with nitrogen to make ammonia",
        ],
        "correct_index": 0,
        "why": "Hydrogen burns readily in oxygen, so oxygen in the feed would "
               "consume hydrogen and make water rather than ammonia.",
    },
    {
        "id": "ks4-haber-process-s18",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why the nitrogen is taken from the air rather than "
                "from a nitrogen compound dug out of the ground.",
        "options": [
            "The air is an unlimited supply that costs nothing to obtain",
            "The air is the only place nitrogen is found on this planet",
            "Nitrogen from a compound would already be joined to hydrogen "
            "atoms",
            "Nitrogen from a mine would be a liquid and hard to pump in",
        ],
        "correct_index": 0,
        "why": "Air is free, everywhere and effectively endless, so only the "
               "cost of separating the nitrogen out has to be paid.",
    },
    # ---------------------------------------------------------------- harder
    {
        "id": "ks4-haber-process-h05",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Predict the effect on the yield of ammonia of raising the "
                "pressure from 200 to 400 atmospheres, and give the main "
                "drawback.",
        "options": [
            "The yield falls, and the plant would also cost a lot more",
            "The yield rises, but the vessel and pumps cost far more",
            "The yield is unchanged, so the extra pressure buys no more "
            "ammonia",
            "The yield rises, and the plant would be cheaper to build",
        ],
        "correct_index": 1,
        "why": "More pressure pushes the equilibrium towards the smaller "
               "volume, so more ammonia forms, but the cost of building for "
               "400 atmospheres outweighs the gain.",
    },
    {
        "id": "ks4-haber-process-h06",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A chemist suggests leaving out the iron and running the "
                "reactor at 700 degrees C to get the same rate. Evaluate the "
                "suggestion.",
        "options": [
            "Good, because heating is cheaper than buying a catalyst",
            "Good, because a higher temperature raises the yield too",
            "Poor, because the rate at 700 degrees C is far too slow",
            "Poor, because the yield would fall and the fuel bill would rise",
        ],
        "correct_index": 3,
        "why": "The rate could indeed be matched by heating, but the forward "
               "reaction is exothermic, so a hotter reactor gives less "
               "ammonia and costs more to heat.",
    },
    {
        "id": "ks4-haber-process-h07",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A plant obtains 1360 tonnes of ammonia in a day, against a "
                "theoretical maximum of 1700 tonnes. Calculate the percentage "
                "yield.",
        "options": [
            "125%",
            "80%",
            "20%",
            "76%",
        ],
        "correct_index": 1,
        "why": "Percentage yield is 1360 / 1700 x 100, which comes to 80%.",
    },
    {
        "id": "ks4-haber-process-h08",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Making ammonia uses about 2% of the world's energy supply. "
                "Evaluate whether that cost is justified.",
        "options": [
            "No, because the ammonia is used mainly in explosives",
            "No, because there is no other use for that energy",
            "Yes, because the fertilisers made from it feed much of the world",
            "Yes, because the energy is all returned when ammonia forms",
        ],
        "correct_index": 2,
        "why": "Nitrogen fertilisers made from this ammonia raise crop yields "
               "enough to feed roughly half the world's population, which is "
               "a return few other uses of energy can match.",
    },
    {
        "id": "ks4-haber-process-h09",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the amount of ammonia present at equilibrium "
                "falls as the reactor is run hotter.",
        "options": [
            "Heating destroys the catalyst, so less ammonia can form",
            "Heating favours the reaction that takes energy in",
            "Heating makes the gases expand, so they cannot meet",
            "Heating favours the reaction that gives energy out",
        ],
        "correct_index": 1,
        "why": "Making ammonia is exothermic, so the endothermic direction "
               "back to nitrogen and hydrogen is the one favoured as the "
               "temperature rises.",
    },
    {
        "id": "ks4-haber-process-h10",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A plant must produce 170 tonnes of ammonia in a day. Work "
                "out the mass of nitrogen it has to be fed. Relative formula "
                "masses: N2 = 28, NH3 = 17.",
        "options": [
            "70 tonnes",
            "85 tonnes",
            "140 tonnes",
            "280 tonnes",
        ],
        "correct_index": 2,
        "why": "170 tonnes of ammonia is 5 lots of 2NH3 (2 x 17 = 34), and "
               "each lot needs one N2, so 5 x 28 = 140 tonnes of nitrogen.",
    },
    {
        "id": "ks4-haber-process-h11",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the reaction vessel in an ammonia plant is built "
                "from thick steel.",
        "options": [
            "It must hold a gas mixture squeezed to 200 atmospheres",
            "It must conduct heat away from the iron catalyst inside",
            "It must react with the nitrogen to start the reaction off",
            "It must stop light reaching the mixture during the whole "
            "reaction",
        ],
        "correct_index": 0,
        "why": "A vessel holding gas at around 200 atmospheres has to resist "
               "an enormous outward force, which needs thick walls of a "
               "strong material.",
    },
    {
        "id": "ks4-haber-process-h12",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The iron in an ammonia reactor is packed as small pellets "
                "rather than as one solid block. Explain why.",
        "options": [
            "The pellets give a far greater surface area, so more gas meets "
            "the iron",
            "The pellets take part in the reaction and are slowly used up as "
            "it runs",
            "The pellets lower the pressure inside the reactor, which "
            "protects the vessel",
            "The pellets raise the amount of ammonia present once the "
            "balance is reached",
        ],
        "correct_index": 0,
        "why": "A catalyst works at its surface, so breaking the same mass "
               "into pellets exposes far more of it to the gas mixture and "
               "the mixture reaches equilibrium sooner.",
    },
    {
        "id": "ks4-haber-process-h13",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "100 mol of nitrogen and 300 mol of hydrogen are fed into a "
                "reactor, and 30 mol of the nitrogen reacts. Calculate the "
                "amount of ammonia formed, in mol.",
        "options": [
            "15 mol",
            "30 mol",
            "60 mol",
            "90 mol",
        ],
        "correct_index": 2,
        "why": "Each mole of nitrogen that reacts gives two moles of ammonia, "
               "so 30 mol of N2 gives 60 mol of NH3.",
    },
    {
        "id": "ks4-haber-process-h14",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The forward reaction gives out energy, yet an ammonia plant "
                "still needs a large energy supply. Explain why.",
        "options": [
            "The catalyst has to be melted down before it will work properly",
            "The ammonia has to be boiled before it can be stored",
            "Energy is needed to compress the gases and to heat them",
            "Energy is needed to split nitrogen out of its compounds",
        ],
        "correct_index": 2,
        "why": "Squeezing the feed gases to 200 atmospheres and bringing them "
               "to 450 degrees C both take large amounts of energy, far more "
               "than the reaction itself releases.",
    },
    {
        "id": "ks4-haber-process-h15",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why ammonia is moved around the country as a liquid "
                "under pressure rather than as a gas.",
        "options": [
            "The liquid takes up far less space than the gas does",
            "The liquid is a different compound from the gas is",
            "The liquid cannot react with anything it is stored in",
            "The liquid weighs much less than the same gas would",
        ],
        "correct_index": 0,
        "why": "Liquefying the ammonia cuts its volume by a factor of "
               "hundreds, so a single tanker carries far more of it.",
    },
    {
        "id": "ks4-haber-process-h16",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain, in terms of particles, why the reaction goes faster "
                "as the reactor is made hotter.",
        "options": [
            "The particles grow larger, so they are easier to hit",
            "The particles collide more often and with more energy",
            "The particles break apart into single atoms before they can mix",
            "The particles are pushed closer together by the heating",
        ],
        "correct_index": 1,
        "why": "Heating raises the average speed of the molecules, so there "
               "are more collisions each second and a greater share of them "
               "have enough energy to react.",
    },
    {
        "id": "ks4-haber-process-h17",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why an ammonia plant is run day and night rather "
                "than being shut down each evening.",
        "options": [
            "The equilibrium takes several days to be reached at all",
            "The catalyst would dissolve if the gas flow ever stopped",
            "Bringing the plant back to pressure and heat wastes energy",
            "The ammonia already made would decompose once it was cool",
        ],
        "correct_index": 2,
        "why": "Reheating and repressurising a cold plant costs a great deal "
               "of energy and time, so running continuously is far cheaper "
               "per tonne of ammonia.",
    },
    {
        "id": "ks4-haber-process-h18",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that leaving the gases in the reactor for "
                "long enough would turn all of them into ammonia.",
        "options": [
            "Correct, because a slow reaction still finishes in the end",
            "Correct, because the catalyst keeps working indefinitely",
            "Wrong, because the iron catalyst stops working after an hour",
            "Wrong, because at equilibrium ammonia breaks down as fast as "
            "it forms",
        ],
        "correct_index": 3,
        "why": "Once equilibrium is reached the composition stops changing, "
               "however long the mixture is left, so some nitrogen and "
               "hydrogen always remain.",
    },

    # ---------------------------------------------------------- standard (top-up)
    {
        "id": "ks4-haber-process-s19",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the two chemists whose work in the early twentieth "
                "century gives the process its name.",
        "options": [
            "Fritz Haber and Carl Bosch",
            "John Dalton and Amedeo Avogadro",
            "Robert Boyle and Jacques Charles",
            "Humphry Davy and Michael Faraday",
        ],
        "correct_index": 0,
        "why": "Fritz Haber developed the reaction and Carl Bosch scaled it "
               "up for industry, which is why it is often called the "
               "Haber-Bosch process.",
    },
    {
        "id": "ks4-haber-process-s20",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The industrial iron catalyst is used together with small "
                "amounts of aluminium oxide and potassium oxide. State what "
                "these additional substances are called.",
        "options": [
            "Promoters, which make the catalyst more effective",
            "Reactants, which are converted into ammonia alongside nitrogen "
            "and hydrogen",
            "Inhibitors, which slow the reaction down deliberately",
            "Indicators, which show when equilibrium has been reached",
        ],
        "correct_index": 0,
        "why": "Promoters are added in small amounts to boost a catalyst's "
               "activity beyond what the iron alone would achieve.",
    },
    {
        "id": "ks4-haber-process-s21",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the process used to separate nitrogen from the other "
                "gases in the air.",
        "options": [
            "Filtration of the air through a fine membrane",
            "Fractional distillation of liquid air",
            "Electrolysis of air that has been dissolved in water",
            "Cracking the air over a hot catalyst",
        ],
        "correct_index": 1,
        "why": "Air is cooled until it liquefies and is then fractionally "
               "distilled, separating nitrogen from oxygen and the other "
               "gases by their different boiling points.",
    },
    {
        "id": "ks4-haber-process-s22",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest an alternative source of hydrogen for the Haber "
                "process that would not release carbon dioxide, unlike "
                "reforming methane.",
        "options": [
            "Hydrogen obtained by the electrolysis of water, using "
            "electricity from a renewable source",
            "Hydrogen extracted directly from the nitrogen already taken "
            "from the air",
            "Hydrogen obtained by cooling ammonia until it separates into "
            "its elements",
            "Hydrogen taken from carbon dioxide already present in the "
            "atmosphere",
        ],
        "correct_index": 0,
        "why": "Splitting water by electrolysis, powered by renewable "
               "electricity, would supply hydrogen without burning a fossil "
               "fuel or releasing carbon dioxide.",
    },
    {
        "id": "ks4-haber-process-s23",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the nitrogen and hydrogen that leave "
                "the reactor without having reacted.",
        "options": [
            "They are released into the atmosphere as waste gases",
            "They are recycled and fed back into the reactor",
            "They are burned to help heat the incoming feed gases",
            "They are dissolved in water and disposed of safely",
        ],
        "correct_index": 1,
        "why": "Unreacted nitrogen and hydrogen are not thrown away; they "
               "are separated from the ammonia and returned to the reactor "
               "to react again.",
    },
    {
        "id": "ks4-haber-process-s24",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State approximately what percentage of the nitrogen and "
                "hydrogen is converted to ammonia in a single pass through "
                "the reactor, before any recycling.",
        "options": [
            "About 15%",
            "About 50%",
            "About 80%",
            "About 98%",
        ],
        "correct_index": 0,
        "why": "Only around 15% converts on one pass; it is the recycling "
               "of the rest that raises the overall yield to about 98%.",
    },
    {
        "id": "ks4-haber-process-s25",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is true of the rates of the forward and reverse "
                "reactions once the mixture has reached equilibrium.",
        "options": [
            "Both rates have fallen to zero",
            "The forward rate is faster than the reverse rate",
            "The forward and reverse rates are equal to one another",
            "The reverse rate is faster than the forward rate",
        ],
        "correct_index": 2,
        "why": "Equilibrium is reached when ammonia forms exactly as "
               "quickly as it breaks down, not when the reaction has "
               "stopped.",
    },
    {
        "id": "ks4-haber-process-s26",
        "subtopic_slug": "haber-process",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the nitrogen and hydrogen leaving the reactor "
                "unreacted are better described as recycled material than as "
                "waste.",
        "options": [
            "They are compressed until they turn into a completely "
            "different substance",
            "They are returned to the reactor and go on to form more "
            "ammonia, rather than being discarded",
            "They are sold separately to other factories once they leave "
            "the plant",
            "They are chemically identical to ammonia once they have left "
            "the reactor",
        ],
        "correct_index": 1,
        "why": "Waste is material with no further use; this gas still "
               "reacts perfectly well and is fed straight back in, which is "
               "why it is recycled rather than wasted.",
    },

    # ------------------------------------------------------------- harder (top-up)
    {
        "id": "ks4-haber-process-h19",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Using the fact that only about 15% of the gas converts on "
                "one pass through the reactor, and the plant's overall yield "
                "is about 98%, explain why recycling is essential to the "
                "process's economics.",
        "options": [
            "Without recycling, most of the costly purified nitrogen and "
            "hydrogen would leave the plant unused rather than becoming "
            "ammonia",
            "Without recycling, the reactor would need to be run at a far "
            "lower pressure than 200 atmospheres",
            "Without recycling, the iron catalyst would have to be replaced "
            "after every single pass through the reactor",
            "Without recycling, ammonia would decompose back into nitrogen "
            "and hydrogen as soon as it left the reactor",
        ],
        "correct_index": 0,
        "why": "At only 15% conversion per pass, throwing away the "
               "unreacted gas would waste the great majority of the "
               "nitrogen and hydrogen that had already been purified and "
               "compressed at real cost.",
    },
    {
        "id": "ks4-haber-process-h20",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The catalyst promoters aluminium oxide and potassium oxide "
                "add to the cost of preparing the iron catalyst. Suggest why "
                "manufacturers include them anyway.",
        "options": [
            "They lower the pressure the reactor has to be built to "
            "withstand",
            "They significantly raise the catalyst's activity, so the plant "
            "runs faster and more cheaply overall",
            "They react with the nitrogen to make a small extra amount of "
            "ammonia directly",
            "They are required by law in every country that manufactures "
            "ammonia",
        ],
        "correct_index": 1,
        "why": "A more active catalyst reaches equilibrium faster, which "
               "raises the plant's output and more than repays the small "
               "extra cost of including the promoters.",
    },
    {
        "id": "ks4-haber-process-h21",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how fractional distillation is able to separate "
                "nitrogen from the other gases in liquid air.",
        "options": [
            "Nitrogen has a different boiling point from the other gases, "
            "so it evaporates off separately as the liquid air is warmed",
            "Nitrogen is denser than the other gases and sinks to the "
            "bottom of the column",
            "Nitrogen reacts with the column packing while the other gases "
            "pass straight through",
            "Nitrogen is magnetic and can be pulled out of the mixture as "
            "it flows through the column",
        ],
        "correct_index": 0,
        "why": "Each gas in liquid air boils off at its own temperature, so "
               "warming the mixture gradually lets nitrogen be collected "
               "separately from oxygen and the rest.",
    },
    {
        "id": "ks4-haber-process-h22",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that switching entirely to hydrogen made "
                "by electrolysis with renewable electricity would solve the "
                "environmental problems of the Haber process immediately.",
        "options": [
            "Sound: electrolysis needs no electricity at all once it is "
            "built, so the change would cost nothing further to run",
            "Sound, because ammonia made this way is a chemically different "
            "and cleaner substance",
            "Unsound: enormous amounts of renewable electricity and new "
            "infrastructure would be needed, so the change could only "
            "happen gradually",
            "Unsound, because electrolysis cannot produce hydrogen in "
            "large enough quantities under any circumstances",
        ],
        "correct_index": 2,
        "why": "Electrolysis would remove the carbon dioxide released by "
               "reforming methane, but replacing the whole world's supply "
               "would need a huge, gradual build-up of renewable "
               "electricity and plant.",
    },
    {
        "id": "ks4-haber-process-h23",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Gas leaving the reactor is cooled to condense out the "
                "ammonia before the leftover nitrogen and hydrogen are "
                "recycled. Explain why the ammonia is removed first, rather "
                "than recycling the whole mixture as it is.",
        "options": [
            "Recycling the whole mixture would send the ammonia already "
            "made straight back into the reactor instead of collecting it "
            "as product",
            "Ammonia would corrode the compressor used to recycle the "
            "unreacted gases",
            "Ammonia cannot pass through the same pipework as nitrogen and "
            "hydrogen do",
            "Ammonia would react with the iron catalyst if it were "
            "recycled through the reactor again",
        ],
        "correct_index": 0,
        "why": "Cooling and condensing takes the ammonia out of the loop so "
               "it can be collected, leaving only the unreacted gases to be "
               "sent round again.",
    },
    {
        "id": "ks4-haber-process-h24",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that, because the forward reaction is "
                "exothermic, running the reactor as cold as possible would "
                "always give the best result.",
        "options": [
            "Sound, because a lower temperature always raises both the "
            "yield and the rate together",
            "Unsound: a very low temperature would raise the yield but make "
            "the rate impractically slow",
            "Sound, because temperature has no effect on the rate of this "
            "particular reaction",
            "Unsound, because a lower temperature would in fact lower the "
            "equilibrium yield of ammonia",
        ],
        "correct_index": 1,
        "why": "A colder reactor would shift equilibrium further towards "
               "ammonia, but the reaction would then be too slow to be "
               "worth running, which is exactly why 450 °C is chosen as a "
               "compromise.",
    },
    {
        "id": "ks4-haber-process-h25",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "50 tonnes of nitrogen is fed into a reactor, but only 80% "
                "of it reacts before the gas is drawn off. Calculate the "
                "mass of ammonia formed. Relative formula masses: N2 = 28, "
                "NH3 = 17.",
        "options": [
            "24.3 tonnes",
            "34.0 tonnes",
            "48.6 tonnes",
            "60.7 tonnes",
        ],
        "correct_index": 2,
        "why": "80% of 50 tonnes is 40 tonnes of nitrogen reacted; each "
               "28 tonnes of N2 gives 34 tonnes of NH3, so "
               "40 × (34 ÷ 28) = 48.6 tonnes.",
    },
    {
        "id": "ks4-haber-process-h26",
        "subtopic_slug": "haber-process",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the process conditions of 450 °C, 200 "
                "atmospheres and an iron catalyst are described as optimum "
                "rather than as the conditions that give the highest "
                "possible yield of ammonia.",
        "options": [
            "They balance yield, rate and cost together, rather than "
            "chasing the highest yield alone regardless of price or speed",
            "They are simply the conditions that happen to be easiest for "
            "an engineer to measure accurately",
            "They give the highest yield possible, and the word optimum "
            "means exactly the same thing as maximum in this context",
            "They were fixed by international law once the process was "
            "first invented and cannot be changed since",
        ],
        "correct_index": 0,
        "why": "A lower temperature or a higher pressure would each raise "
               "the equilibrium yield further, but only at a cost in rate "
               "or in engineering that outweighs the extra ammonia gained, "
               "which is what makes the chosen conditions optimum rather "
               "than maximal.",
    },
]
