"""Chemistry · Rates and equilibrium — rate calculations, the four rate
factors, collision theory, catalysts, reversible reactions and Le Chatelier.

The distractors are built from the four misconceptions the brief declares:
that rate is the total amount of product rather than the amount per second;
that concentration or surface area lowers the activation energy (only a
catalyst does); that a catalyst is used up or changes the yield; and that
equilibrium means equal CONCENTRATIONS rather than equal RATES.

⚠️ `catalysts` is byte-identical to a KS3 lesson slug, which is why this pool
has its own table. Every question in that section is pitched at KS4 —
activation energy, the alternative pathway, named industrial catalysts and
catalyst poisoning — never the KS3 "a catalyst makes it go faster".

Le Chatelier appears ONLY under `effect-of-conditions-equilibrium`, which is
higher tier; the five foundation-flagged subtopics stay clear of it.
"""

TOPIC = "rates-equilibrium"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── calculating-rates ───────────────────────────────────────────────
    {
        "id": "ks4-calculating-rates-e01",
        "subtopic_slug": "calculating-rates",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State a suitable unit for the rate of a reaction that is "
                "followed by the mass lost from an open flask.",
        "options": [
            "g/s",
            "s/g",
            "cm3/s",
            "mol/dm3",
        ],
        "correct_index": 0,
        "why": "Rate is the quantity changed divided by the time taken, so a "
               "mass change is measured in grams per second.",
    },
    {
        "id": "ks4-calculating-rates-e02",
        "subtopic_slug": "calculating-rates",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Marble chips react with hydrochloric acid in an open flask "
                "standing on a balance. State why the reading on the balance "
                "falls.",
        "options": [
            "The acid evaporates out of the open flask",
            "The marble chips dissolve and become lighter than the acid",
            "Carbon dioxide gas escapes from the flask",
            "The calcium chloride formed has less mass than the marble",
        ],
        "correct_index": 2,
        "why": "The carbon dioxide produced leaves the open flask, so the "
               "mass on the balance falls as the reaction proceeds.",
    },
    {
        "id": "ks4-calculating-rates-e03",
        "subtopic_slug": "calculating-rates",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the rate of the reaction between "
                "magnesium and a fixed amount of acid as the reaction goes "
                "on.",
        "options": [
            "It increases, because the products speed the reaction up",
            "It decreases, because the reactants are being used up",
            "It stays constant until all the magnesium has gone",
            "It decreases, because the acid becomes more concentrated",
        ],
        "correct_index": 1,
        "why": "Fewer reactant particles remain, so there are fewer "
               "collisions each second and the rate falls until the reaction "
               "stops.",
    },
    {
        "id": "ks4-calculating-rates-e04",
        "subtopic_slug": "calculating-rates",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a flat, horizontal section at the end of a graph "
                "of gas volume against time shows.",
        "options": [
            "The rate of reaction has reached its highest possible value",
            "Gas is leaking out of the apparatus",
            "The reaction has started to run backwards",
            "The reaction has finished — no more gas is being produced",
        ],
        "correct_index": 3,
        "why": "A flat line means the volume is no longer changing, so the "
               "rate is zero and at least one reactant has been used up.",
    },
    {
        "id": "ks4-calculating-rates-s01",
        "subtopic_slug": "calculating-rates",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction mixture loses 1.8 g of mass in 90 seconds. "
                "Calculate the mean rate of reaction in g/s.",
        "options": [
            "0.20 g/s",
            "0.02 g/s",
            "50.00 g/s",
            "162.00 g/s",
        ],
        "correct_index": 1,
        "why": "Mean rate is the total change divided by the total time: "
               "1.8 ÷ 90 = 0.02 g/s.",
    },
    {
        "id": "ks4-calculating-rates-s02",
        "subtopic_slug": "calculating-rates",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction produces 45 cm3 of gas in the first 30 s and a "
                "further 15 cm3 in the next 30 s. Calculate the mean rate "
                "over the whole 60 s.",
        "options": [
            "1.0 cm3/s",
            "1.5 cm3/s",
            "0.5 cm3/s",
            "2.0 cm3/s",
        ],
        "correct_index": 0,
        "why": "The mean rate uses the total gas and the total time: "
               "60 ÷ 60 = 1.0 cm3/s.",
    },
    {
        "id": "ks4-calculating-rates-s03",
        "subtopic_slug": "calculating-rates",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the sodium thiosulfate and hydrochloric acid "
                "experiment, a cross under the flask disappears after 40 s "
                "in one run and after 20 s in another. Compare the rates of "
                "the two runs.",
        "options": [
            "The 40 s run is twice as fast, because it took longer for the "
            "cross to vanish",
            "The rates are the same, because the same cross disappeared in "
            "both runs",
            "The 20 s run is four times as fast, because time and rate are "
            "squared",
            "The 20 s run is twice as fast, because the shorter the time the "
            "greater the rate",
        ],
        "correct_index": 3,
        "why": "Rate is proportional to 1 ÷ time, so halving the time for "
               "the cross to disappear doubles the rate.",
    },
    {
        "id": "ks4-calculating-rates-s04",
        "subtopic_slug": "calculating-rates",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe a suitable method for measuring the rate of a "
                "reaction that produces hydrogen gas.",
        "options": [
            "Weigh the flask at intervals; the mass rises as hydrogen is "
            "made",
            "Measure the temperature at intervals; the rise shows how much "
            "hydrogen has formed",
            "Collect the gas in a gas syringe and record its volume at "
            "regular time intervals",
            "Filter the mixture at intervals and weigh the hydrogen caught "
            "on the filter paper",
        ],
        "correct_index": 2,
        "why": "Hydrogen is a gas, so its volume can be read directly from a "
               "syringe at set times and plotted against time.",
    },
    {
        "id": "ks4-calculating-rates-h01",
        "subtopic_slug": "calculating-rates",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction produces 72 cm3 of gas altogether: 48 cm3 in the "
                "first 20 s and the rest over the following 100 s. Calculate "
                "the mean rate over the first 20 s and the mean rate over "
                "the whole reaction.",
        "options": [
            "2.4 cm3/s and 0.24 cm3/s",
            "3.6 cm3/s and 0.60 cm3/s",
            "2.4 cm3/s and 0.72 cm3/s",
            "2.4 cm3/s and 0.60 cm3/s",
        ],
        "correct_index": 3,
        "why": "48 ÷ 20 = 2.4 cm3/s for the first stage and 72 ÷ 120 = "
               "0.60 cm3/s overall — the mean is lower because the reaction "
               "slows down.",
    },
    {
        "id": "ks4-calculating-rates-h02",
        "subtopic_slug": "calculating-rates",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two runs of the same reaction produce the same final volume "
                "of gas, but run B reaches it in half the time. Explain what "
                "this tells you about the two runs.",
        "options": [
            "Run B used twice as much reactant, so it produced more gas",
            "Run B produced twice as much gas overall, and it did so at "
            "exactly twice the rate",
            "Run B had the faster rate, but the same amount of reactant was "
            "used up in both",
            "Run B had a lower activation energy because its mixture was "
            "warmer",
        ],
        "correct_index": 2,
        "why": "The same final volume means the same quantity of limiting "
               "reactant reacted; only the time taken differed, so run B was "
               "simply faster.",
    },
    {
        "id": "ks4-calculating-rates-h03",
        "subtopic_slug": "calculating-rates",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'The reaction made 100 cm3 of gas, so its "
                "rate is 100 cm3.' Identify the error and state what is "
                "missing.",
        "options": [
            "Rate is an amount per unit time, so the volume must be divided "
            "by the time taken",
            "Rate is the total volume of gas produced, but the unit should "
            "be written as cm3/s",
            "Rate is the volume multiplied by the time, so the time must be "
            "measured as well",
            "Rate is the volume divided by the mass of reactant used, not by "
            "the time",
        ],
        "correct_index": 0,
        "why": "A rate always says how much changes in each second, so it is "
               "the volume of gas divided by the time taken.",
    },
    {
        "id": "ks4-calculating-rates-h04",
        "subtopic_slug": "calculating-rates",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a marble chip and acid reaction the balance reading "
                "falls from 152.40 g to 150.96 g in 4 minutes. Calculate the "
                "mean rate of reaction in g/s.",
        "options": [
            "0.360 g/s",
            "0.006 g/s",
            "0.024 g/s",
            "0.635 g/s",
        ],
        "correct_index": 1,
        "why": "The mass CHANGE is 1.44 g and 4 minutes is 240 s, so the "
               "rate is 1.44 ÷ 240 = 0.006 g/s.",
    },

    # ── factors-affecting-rate ──────────────────────────────────────────
    {
        "id": "ks4-factors-affecting-rate-e01",
        "subtopic_slug": "factors-affecting-rate",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which factor has essentially no effect on the rate of "
                "a reaction between two solutions.",
        "options": [
            "The concentration of the solutions",
            "The pressure of the air above the solutions",
            "The temperature at which the solutions are mixed",
            "The presence of a catalyst",
        ],
        "correct_index": 1,
        "why": "Pressure changes the number of particles per unit volume "
               "only for gases; the particles in a solution are already "
               "close together.",
    },
    {
        "id": "ks4-factors-affecting-rate-e02",
        "subtopic_slug": "factors-affecting-rate",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why food keeps for longer in a refrigerator.",
        "options": [
            "The cold kills the bacteria that spoil food",
            "The cold raises the activation energy of the spoilage reactions",
            "The cold removes the water that the spoilage reactions need",
            "The lower temperature slows down the reactions that spoil food",
        ],
        "correct_index": 3,
        "why": "Cooler particles move more slowly and fewer collisions carry "
               "enough energy, so the reactions that spoil food go more "
               "slowly.",
    },
    {
        "id": "ks4-factors-affecting-rate-e03",
        "subtopic_slug": "factors-affecting-rate",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how crushing a solid reactant into a powder changes "
                "its surface area and the rate of its reaction.",
        "options": [
            "The surface area increases and the rate increases",
            "The surface area increases and the rate decreases",
            "The surface area decreases and the rate increases",
            "The surface area is unchanged, because the mass is unchanged",
        ],
        "correct_index": 0,
        "why": "Powdering exposes far more of the solid's particles to the "
               "other reactant, so more collisions happen each second.",
    },
    {
        "id": "ks4-factors-affecting-rate-e04",
        "subtopic_slug": "factors-affecting-rate",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the effect of increasing the pressure on a reaction "
                "between two gases.",
        "options": [
            "The rate falls, because the particles have less room to move",
            "The rate is unchanged, because pressure is not a rate factor",
            "The rate rises, because the particles are closer together and "
            "collide more often",
            "The rate rises, because the extra pressure gives each of the "
            "particles more energy",
        ],
        "correct_index": 2,
        "why": "Squeezing the gas into a smaller volume puts more particles "
               "into each cubic centimetre, so collisions become more "
               "frequent.",
    },
    {
        "id": "ks4-factors-affecting-rate-s01",
        "subtopic_slug": "factors-affecting-rate",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why doubling the concentration of an acid roughly "
                "doubles the rate of its reaction with magnesium.",
        "options": [
            "The acid particles gain more energy, so more collisions "
            "succeed",
            "The surface area of the magnesium also doubles when the acid "
            "is made twice as concentrated",
            "The activation energy of the reaction is halved by the extra "
            "acid",
            "There are twice as many acid particles in the same volume, so "
            "collisions are twice as frequent",
        ],
        "correct_index": 3,
        "why": "Concentration controls how crowded the particles are, and "
               "twice the crowding gives about twice as many collisions per "
               "second.",
    },
    {
        "id": "ks4-factors-affecting-rate-s02",
        "subtopic_slug": "factors-affecting-rate",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student investigates how surface area affects the rate of "
                "the reaction between marble and acid. Identify the "
                "variables that must be controlled.",
        "options": [
            "The size of the marble pieces and the concentration of the "
            "hydrochloric acid used",
            "The mass of marble used and the size of the marble pieces",
            "The mass of marble, and the volume, concentration and "
            "temperature of the acid",
            "The temperature of the acid and the size of the marble pieces",
        ],
        "correct_index": 2,
        "why": "Only the surface area may change, so the mass of marble and "
               "the volume, concentration and temperature of the acid must "
               "all be held constant.",
    },
    {
        "id": "ks4-factors-affecting-rate-s03",
        "subtopic_slug": "factors-affecting-rate",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction is run at 20 °C and then repeated at 40 °C. "
                "Predict roughly what happens to the time the reaction "
                "takes.",
        "options": [
            "It halves, because the rate doubles for every 20 °C of heating",
            "It falls to about a quarter, because the rate roughly doubles "
            "for each 10 °C rise",
            "It doubles, because the particles spend longer in contact "
            "during each collision",
            "It is unchanged, because temperature does not affect how much "
            "product is formed",
        ],
        "correct_index": 1,
        "why": "Each 10 °C rise roughly doubles the rate, so two such rises "
               "make the reaction about four times faster and it takes about "
               "a quarter of the time.",
    },
    {
        "id": "ks4-factors-affecting-rate-s04",
        "subtopic_slug": "factors-affecting-rate",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why flour dust suspended in the air of a mill can "
                "explode, while a bag of the same flour burns only slowly.",
        "options": [
            "The dust has an enormous surface area, so it reacts with "
            "oxygen extremely quickly",
            "The dust is at a much higher temperature than the flour that "
            "is packed inside the bag",
            "The dust is more concentrated than the flour packed inside the "
            "bag",
            "Grinding the flour releases a catalyst that is trapped inside "
            "the grains",
        ],
        "correct_index": 0,
        "why": "Suspending the flour exposes a vast area to the air, so the "
               "combustion happens all at once instead of only at the "
               "surface of the bag.",
    },
    {
        "id": "ks4-factors-affecting-rate-h01",
        "subtopic_slug": "factors-affecting-rate",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students investigate temperature and rate. Student A "
                "changes the temperature and the concentration together; "
                "student B changes only the temperature. Evaluate whose "
                "results support a conclusion about temperature.",
        "options": [
            "Student A, because changing two variables at the same time "
            "produces twice as much data for the graph",
            "Both of them, because the temperature was changed in each "
            "investigation",
            "Student B, because only one variable changed, so any change in "
            "rate must be due to temperature",
            "Neither, because a rate experiment always needs at least three "
            "variables changed",
        ],
        "correct_index": 2,
        "why": "A conclusion about one variable only holds if everything "
               "else was held constant, so only student B's results isolate "
               "the effect of temperature.",
    },
    {
        "id": "ks4-factors-affecting-rate-h02",
        "subtopic_slug": "factors-affecting-rate",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fixed volume of dilute hydrochloric acid reacts with an "
                "excess of magnesium ribbon. Determine which change speeds "
                "the reaction up WITHOUT changing the total volume of "
                "hydrogen produced.",
        "options": [
            "Warming the acid from 20 °C to 35 °C before adding the "
            "magnesium",
            "Doubling the volume of acid used, at the same concentration",
            "Doubling the concentration of the acid used, in the same volume",
            "Adding water to double the volume of the acid before the "
            "reaction",
        ],
        "correct_index": 0,
        "why": "Heating speeds up the same number of acid particles, whereas "
               "adding more acid produces more hydrogen and diluting the "
               "acid slows the reaction down.",
    },
    {
        "id": "ks4-factors-affecting-rate-h03",
        "subtopic_slug": "factors-affecting-rate",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why raising the pressure has a large effect on a "
                "reaction between two gases but almost none on a reaction "
                "between two solutions.",
        "options": [
            "Solutions are already at high pressure, so extra pressure "
            "makes no difference",
            "Pressure raises the activation energy for reactions in "
            "solution but lowers it for reactions between gases",
            "Gas particles are heavier than particles in solution, so "
            "pressure moves them more",
            "A gas can be compressed into a smaller volume, but the "
            "particles in a liquid are already touching",
        ],
        "correct_index": 3,
        "why": "Compressing a gas puts more particles into each cubic "
               "centimetre and so raises the collision frequency, while a "
               "liquid barely compresses at all.",
    },
    {
        "id": "ks4-factors-affecting-rate-h04",
        "subtopic_slug": "factors-affecting-rate",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Experiment A uses 50 cm3 of 1.0 mol/dm3 acid and "
                "experiment B uses 25 cm3 of 2.0 mol/dm3 acid, both with "
                "excess marble chips at the same temperature. Predict which "
                "starts faster and which produces more gas overall.",
        "options": [
            "A starts faster; both produce the same volume of gas",
            "B starts faster; both produce the same volume of gas",
            "B starts faster and produces twice as much gas",
            "They start at the same rate; A produces twice as much gas",
        ],
        "correct_index": 1,
        "why": "B is twice as concentrated so its particles collide more "
               "often at the start, but both contain the same amount of acid "
               "in total, so the same volume of carbon dioxide is finally "
               "produced.",
    },

    # ── collision-theory ────────────────────────────────────────────────
    {
        "id": "ks4-collision-theory-e01",
        "subtopic_slug": "collision-theory",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two conditions a collision must meet if a "
                "reaction is to occur.",
        "options": [
            "The particles must be the same size and moving at the same "
            "speed",
            "The particles must be electrically charged and must both be "
            "dissolved in water before they meet",
            "The particles must collide with at least the activation energy "
            "and in the correct orientation",
            "The particles must collide head-on and must carry equal "
            "amounts of energy",
        ],
        "correct_index": 2,
        "why": "Energy alone is not enough — the particles must also meet "
               "the right way round for the bonds to break and reform.",
    },
    {
        "id": "ks4-collision-theory-e02",
        "subtopic_slug": "collision-theory",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define activation energy.",
        "options": [
            "The minimum energy that colliding particles must have for a "
            "reaction to occur",
            "The total energy released to the surroundings when a reaction "
            "takes place",
            "The energy stored in the chemical bonds of the reactants",
            "The average energy of all the particles in the reaction mixture",
        ],
        "correct_index": 0,
        "why": "It is the barrier a collision must clear before the existing "
               "bonds can break and the reaction can proceed.",
    },
    {
        "id": "ks4-collision-theory-e03",
        "subtopic_slug": "collision-theory",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the term used for a collision that leads to a "
                "reaction.",
        "options": [
            "A head-on collision",
            "A high-energy elastic collision",
            "A catalysed collision",
            "A successful collision",
        ],
        "correct_index": 3,
        "why": "Only collisions with enough energy and the right "
               "orientation form products, and these are called successful "
               "or effective collisions.",
    },
    {
        "id": "ks4-collision-theory-e04",
        "subtopic_slug": "collision-theory",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which single change lowers the activation energy of a "
                "reaction.",
        "options": [
            "Raising the temperature",
            "Adding a catalyst",
            "Increasing the concentration",
            "Increasing the surface area",
        ],
        "correct_index": 1,
        "why": "Only a catalyst provides a different reaction pathway; the "
               "other changes make collisions more frequent or more "
               "energetic but leave the barrier where it is.",
    },
    {
        "id": "ks4-collision-theory-s01",
        "subtopic_slug": "collision-theory",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, using collision theory, why a reaction between two "
                "gases speeds up when the container is made smaller.",
        "options": [
            "The same number of particles now occupy a smaller volume, so "
            "they collide more frequently",
            "The particles are squeezed closer together, so each one of "
            "them now carries much more energy",
            "The smaller container gives the reaction a lower activation "
            "energy",
            "The container walls force the particles into the correct "
            "orientation",
        ],
        "correct_index": 0,
        "why": "Rate depends on how many collisions happen each second, and "
               "packing the same particles into less space makes collisions "
               "more frequent.",
    },
    {
        "id": "ks4-collision-theory-s02",
        "subtopic_slug": "collision-theory",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Petrol does not react with the oxygen in the air at room "
                "temperature, even though the reaction releases a great deal "
                "of energy. Explain why a spark is needed.",
        "options": [
            "The spark supplies the extra oxygen that the reaction needs",
            "The spark lowers the activation energy of the combustion "
            "reaction",
            "The spark supplies the activation energy, so collisions can "
            "begin to succeed",
            "The reaction is endothermic until it starts, and the spark "
            "supplies the missing energy",
        ],
        "correct_index": 2,
        "why": "Petrol and oxygen collisions at room temperature do not "
               "carry enough energy to clear the activation barrier, and the "
               "spark provides it.",
    },
    {
        "id": "ks4-collision-theory-s03",
        "subtopic_slug": "collision-theory",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why increasing the concentration of a reactant does "
                "not change the activation energy of the reaction.",
        "options": [
            "It does change it — having many more particles present makes "
            "the energy barrier easier to cross",
            "The activation energy depends on the bonds being broken, not "
            "on how many particles are present",
            "The activation energy changes only with pressure, never with "
            "concentration",
            "The activation energy is fixed by the temperature of the "
            "mixture alone",
        ],
        "correct_index": 1,
        "why": "The barrier is a property of the reaction itself; adding "
               "more particles simply produces more collisions against the "
               "same barrier.",
    },
    {
        "id": "ks4-collision-theory-s04",
        "subtopic_slug": "collision-theory",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the reaction A-B + C → A + B-C, explain why some "
                "collisions fail even when the particles have plenty of "
                "energy.",
        "options": [
            "The particles were travelling too fast to be able to stick "
            "together",
            "The A-B bond had already broken before the collision took place",
            "There was not enough C present to react with all of the A-B",
            "C struck the A end of the molecule rather than the B end",
        ],
        "correct_index": 3,
        "why": "Orientation matters as well as energy — C has to arrive at "
               "the end of the molecule where the new bond will form.",
    },
    {
        "id": "ks4-collision-theory-h01",
        "subtopic_slug": "collision-theory",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how adding a catalyst and raising the temperature "
                "each increase the proportion of collisions that succeed.",
        "options": [
            "Both lower the activation energy, but the catalyst lowers it "
            "by more",
            "Both raise the energy of the particles, but the catalyst "
            "manages to do so without any heating at all",
            "Neither changes the proportion — both only make collisions "
            "more frequent",
            "A catalyst lowers the barrier the particles must clear; "
            "heating raises the particles' energies",
        ],
        "correct_index": 3,
        "why": "The two work from opposite sides of the same comparison — "
               "one moves the barrier down, the other moves the particles' "
               "energies up.",
    },
    {
        "id": "ks4-collision-theory-h02",
        "subtopic_slug": "collision-theory",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Increasing the surface area of a solid "
                "lowers the activation energy, which is why the reaction "
                "speeds up.' Identify the error.",
        "options": [
            "Surface area has no effect on the rate of reaction at all, so "
            "the whole statement is wrong",
            "Surface area increases how many collisions happen, but the "
            "activation energy is unchanged",
            "Surface area raises the activation energy, so the reaction "
            "should slow down",
            "Surface area changes only the total mass of product formed, "
            "not the rate",
        ],
        "correct_index": 1,
        "why": "Only a catalyst alters the activation energy; a larger "
               "surface area simply exposes more particles for collisions.",
    },
    {
        "id": "ks4-collision-theory-h03",
        "subtopic_slug": "collision-theory",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Reaction P has Ea = 55 kJ/mol and reaction Q has "
                "Ea = 190 kJ/mol, and both are run at the same temperature "
                "and concentration. Explain why their collision frequencies "
                "are similar but their rates are very different.",
        "options": [
            "The frequencies differ too, because a low-Ea reaction has "
            "faster particles",
            "The rates are the same as each other; only the amount of "
            "product formed differs",
            "Collision frequency is set by temperature and concentration; "
            "far more of P's collisions clear its barrier",
            "Reaction Q contains far fewer particles overall, so its "
            "particles collide less often and it reacts more slowly",
        ],
        "correct_index": 2,
        "why": "How often particles meet is set by temperature and "
               "concentration, but how many of those meetings succeed is set "
               "by the height of the activation energy barrier.",
    },
    {
        "id": "ks4-collision-theory-h04",
        "subtopic_slug": "collision-theory",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas-phase reaction runs in a sealed, rigid container. "
                "Explain what happens to the frequency of successful "
                "collisions as the reaction approaches completion.",
        "options": [
            "It falls, because reactant particles are used up so fewer are "
            "left to collide",
            "It rises, because the product particles are smaller and move "
            "faster",
            "It stays constant, because the volume of the container does not "
            "change",
            "It rises, because the reaction warms the container and speeds "
            "the particles up",
        ],
        "correct_index": 0,
        "why": "Reactant concentration falls as the reaction proceeds, so "
               "there are fewer reactant particles in the same volume and "
               "they meet less often.",
    },

    # ── catalysts ───────────────────────────────────────────────────────
    {
        "id": "ks4-catalysts-e01",
        "subtopic_slug": "catalysts",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how a catalyst increases the rate of a reaction.",
        "options": [
            "By raising the temperature of the reaction mixture",
            "By increasing the concentration of the reactants",
            "By being used up steadily during the reaction, releasing "
            "energy as it goes",
            "By providing an alternative pathway with a lower activation "
            "energy",
        ],
        "correct_index": 3,
        "why": "The alternative route has a lower barrier, so a greater "
               "proportion of collisions carry enough energy to succeed.",
    },
    {
        "id": "ks4-catalysts-e02",
        "subtopic_slug": "catalysts",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the catalyst used in the Haber process, "
                "N2 + 3H2 ⇌ 2NH3.",
        "options": [
            "Platinum",
            "Iron",
            "Vanadium(V) oxide",
            "Nickel",
        ],
        "correct_index": 1,
        "why": "The Haber process uses an iron catalyst, which makes the "
               "reaction fast enough to be economic at about 450 °C.",
    },
    {
        "id": "ks4-catalysts-e03",
        "subtopic_slug": "catalysts",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "2.0 g of catalyst is added at the start of a reaction. "
                "State the mass of catalyst present once the reaction has "
                "finished.",
        "options": [
            "0.0 g, because the catalyst has been used up",
            "1.0 g, because half of the catalyst reacts",
            "2.0 g, because a catalyst is not used up",
            "4.0 g, because the catalyst gains mass from the products",
        ],
        "correct_index": 2,
        "why": "A catalyst takes part in the reaction but is regenerated, so "
               "it is chemically unchanged and its final mass matches its "
               "starting mass.",
    },
    {
        "id": "ks4-catalysts-e04",
        "subtopic_slug": "catalysts",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the catalyst used in the Contact process, "
                "2SO2 + O2 ⇌ 2SO3, in the manufacture of sulfuric acid.",
        "options": [
            "Vanadium(V) oxide, V2O5",
            "Iron, Fe",
            "Platinum and rhodium",
            "Nickel, Ni",
        ],
        "correct_index": 0,
        "why": "The oxidation of sulfur dioxide to sulfur trioxide is "
               "catalysed by vanadium(V) oxide in the Contact process.",
    },
    {
        "id": "ks4-catalysts-s01",
        "subtopic_slug": "catalysts",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what is meant by a heterogeneous catalyst, and give "
                "an example.",
        "options": [
            "One in the same state as the reactants, such as iron in the "
            "Haber process",
            "One in a different state from the reactants, such as solid iron "
            "with gaseous N2 and H2",
            "One that is consumed by the reaction, such as nickel in "
            "margarine production",
            "One that works for any reaction at all, such as platinum in a "
            "catalytic converter",
        ],
        "correct_index": 1,
        "why": "A heterogeneous catalyst is in a different phase from the "
               "reactants, so the reaction takes place on its surface.",
    },
    {
        "id": "ks4-catalysts-s02",
        "subtopic_slug": "catalysts",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a catalytic converter reduces the pollution "
                "produced by a petrol engine.",
        "options": [
            "It filters solid particulates out of the exhaust gases as they "
            "pass through it",
            "It absorbs carbon dioxide onto a platinum surface and stores "
            "it there until the engine is switched off again",
            "It burns the unburnt fuel by injecting extra petrol directly "
            "into the hot exhaust stream",
            "Platinum and rhodium convert carbon monoxide and nitrogen "
            "oxides into carbon dioxide and nitrogen",
        ],
        "correct_index": 3,
        "why": "The catalyst surface speeds up reactions that turn the toxic "
               "gases into less harmful ones before they leave the exhaust.",
    },
    {
        "id": "ks4-catalysts-s03",
        "subtopic_slug": "catalysts",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why only a small mass of catalyst is needed to "
                "catalyse a large mass of reactants.",
        "options": [
            "The catalyst is regenerated after each reaction, so the same "
            "particles work over and over",
            "The catalyst dissolves and spreads through the mixture, "
            "reaching every reactant particle",
            "The catalyst is very dense, so a small mass contains a very "
            "large number of particles",
            "The catalyst reacts with only a tiny fraction of the reactant "
            "particles present",
        ],
        "correct_index": 0,
        "why": "Because the catalyst is not consumed, each catalyst particle "
               "can take part in the reaction again and again.",
    },
    {
        "id": "ks4-catalysts-s04",
        "subtopic_slug": "catalysts",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an enzyme stops working above about 40 °C, even "
                "though a higher temperature normally increases rate.",
        "options": [
            "The reaction it catalyses becomes exothermic above 40 °C",
            "The enzyme dissolves right into the mixture and can no longer "
            "be recovered from it afterwards",
            "The enzyme's protein structure is denatured, so its shape no "
            "longer fits the reactant",
            "The activation energy rises above 40 °C, making the reaction "
            "impossible",
        ],
        "correct_index": 2,
        "why": "Enzymes are proteins, and heating changes the shape of the "
               "active site so the reactant molecule no longer fits.",
    },
    {
        "id": "ks4-catalysts-h01",
        "subtopic_slug": "catalysts",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a catalyst can make an industrial process "
                "cheaper overall even though the catalyst itself is "
                "expensive to buy.",
        "options": [
            "The catalyst is consumed during the process and sold on as a "
            "valuable by-product",
            "The catalyst increases the yield of product obtained from each "
            "batch of reactants",
            "It is not used up, so one charge lasts many batches, and the "
            "lower operating temperature saves energy",
            "The catalyst removes the need for high pressure, so much "
            "smaller and cheaper reaction vessels can be used",
        ],
        "correct_index": 2,
        "why": "A catalyst is not consumed, so a single charge lasts a long "
               "time, while the energy saved by running cooler is repeated "
               "on every batch.",
    },
    {
        "id": "ks4-catalysts-h02",
        "subtopic_slug": "catalysts",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A catalyst becomes poisoned during an industrial process. "
                "Explain what has happened and its effect on the reaction.",
        "options": [
            "Impurities have bonded to the catalyst's surface, blocking the "
            "active sites so the rate falls",
            "The catalyst has reacted with the product, so fresh catalyst "
            "must be added for every batch",
            "The catalyst has been oxidised, which raises the activation "
            "energy above its original value",
            "The catalyst has dissolved into the reactants, so it now "
            "catalyses the reverse reaction",
        ],
        "correct_index": 0,
        "why": "Heterogeneous catalysis happens on the surface, so anything "
               "that sticks to and blocks that surface stops reactant "
               "particles from reaching it.",
    },
    {
        "id": "ks4-catalysts-h03",
        "subtopic_slug": "catalysts",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student adds a catalyst to a reaction and finds it "
                "finishes in half the time, but the mass of product is "
                "exactly the same as before. Explain both observations.",
        "options": [
            "The catalyst halved the activation energy, and the mass of "
            "product formed depends only on the temperature",
            "More collisions succeeded each second because the activation "
            "energy fell, but the amount of reactant was unchanged",
            "The catalyst supplied extra energy to the reaction, but all of "
            "that energy was then released again as heat and light",
            "The catalyst reacted with half of the reactant, so the "
            "reaction only appeared to finish sooner than before",
        ],
        "correct_index": 1,
        "why": "A catalyst changes only how fast the reactants are "
               "converted, never how much product those reactants can make.",
    },
    {
        "id": "ks4-catalysts-h04",
        "subtopic_slug": "catalysts",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A catalyst is a source of energy for "
                "a reaction, because the reaction goes faster once it is "
                "added.'",
        "options": [
            "Correct — the catalyst releases energy that the reactant "
            "particles then absorb",
            "Correct for enzymes, which are made by living cells, but not "
            "for metal catalysts",
            "Wrong — the catalyst absorbs energy, which is why the mixture "
            "cools as it works",
            "Wrong — the catalyst supplies no energy; it lowers the energy "
            "each collision needs",
        ],
        "correct_index": 3,
        "why": "The particles' energies are unchanged; what changes is the "
               "size of the barrier they have to clear.",
    },

    # ── reversible-reactions-equilibrium ────────────────────────────────
    {
        "id": "ks4-reversible-reactions-equilibrium-e01",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the symbol ⇌ shows in a chemical equation.",
        "options": [
            "The reaction requires heating before it will take place",
            "The reaction is reversible — it can go in either direction",
            "The reaction has reached equilibrium and has now stopped",
            "The reaction produces a gas as one of its products",
        ],
        "correct_index": 1,
        "why": "The double arrow shows that the products can react to reform "
               "the original reactants.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-e02",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is observed when blue hydrated copper sulfate "
                "crystals are heated strongly.",
        "options": [
            "They turn black and give off carbon dioxide",
            "They melt to a blue liquid with no change in colour",
            "They turn green and give off hydrogen",
            "They turn white as water is driven off",
        ],
        "correct_index": 3,
        "why": "Heating drives the water out of the crystals, leaving white "
               "anhydrous copper sulfate.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-e03",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the condition a reversible reaction needs if it is to "
                "reach equilibrium.",
        "options": [
            "It must be in a closed system, so that nothing enters or leaves",
            "It must be heated continuously to keep both reactions going",
            "It must start with equal amounts of reactants and products",
            "It must have a catalyst present to allow the reverse reaction",
        ],
        "correct_index": 0,
        "why": "If the products can escape they cannot react back, so the "
               "two rates never become equal.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-e04",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how anhydrous copper sulfate is used as a test for "
                "water.",
        "options": [
            "It fizzes and gives off a gas when water is added to it",
            "It dissolves completely in water but not in any other liquid",
            "It turns from white to blue when water is added to it",
            "It turns from blue to white when water is added to it",
        ],
        "correct_index": 2,
        "why": "Adding water reverses the dehydration, reforming the blue "
               "hydrated crystals.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-s01",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ammonium chloride is heated at one end of a sealed tube: "
                "NH4Cl(s) ⇌ NH3(g) + HCl(g). Describe what happens at the "
                "cool end of the tube.",
        "options": [
            "Nothing happens, because the forward reaction only goes one way",
            "The two gases react to form a new compound different from "
            "ammonium chloride",
            "The ammonia and hydrogen chloride recombine and white solid "
            "ammonium chloride forms",
            "The ammonia condenses to a colourless liquid and the hydrogen "
            "chloride escapes",
        ],
        "correct_index": 2,
        "why": "Cooling favours the reverse reaction, so the two gases join "
               "again and deposit solid ammonium chloride.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-s02",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the test tube feels warm when water is added to "
                "white anhydrous copper sulfate.",
        "options": [
            "Water is being absorbed into the solid, and absorbing any "
            "liquid always releases energy as heat",
            "The reverse of an endothermic dehydration is exothermic, so "
            "energy is released as the crystals form",
            "The reaction is endothermic, and endothermic reactions raise "
            "the temperature",
            "Friction between the powder grains and the water molecules "
            "releases heat",
        ],
        "correct_index": 1,
        "why": "Driving the water out of the crystals takes energy in, so "
               "putting it back gives the same energy out — the reverse "
               "direction is exothermic.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-s03",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why methane burning in an open Bunsen burner cannot "
                "reach equilibrium.",
        "options": [
            "Combustion reactions are never reversible under any conditions",
            "The flame temperature is too high for any reverse reaction to "
            "occur",
            "There is no catalyst present to allow the reverse reaction to "
            "happen",
            "The system is open — the products escape, so they cannot react "
            "back",
        ],
        "correct_index": 3,
        "why": "Equilibrium needs a closed system, and in open air the "
               "carbon dioxide and water vapour are carried away.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-s04",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reversible reaction is started from pure reactants in a "
                "closed flask. Describe how the forward and reverse rates "
                "change as equilibrium is approached.",
        "options": [
            "The forward rate falls and the reverse rate rises until the two "
            "are equal",
            "The forward rate rises and the reverse rate falls until both "
            "reach zero",
            "Both rates fall steadily until both have reached zero at "
            "equilibrium",
            "Both rates stay constant, and equilibrium arrives when the "
            "amounts become equal",
        ],
        "correct_index": 0,
        "why": "Reactants are used up so the forward reaction slows, while "
               "products build up so the reverse reaction speeds up, and "
               "equilibrium is where they meet.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-h01",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "At equilibrium a closed flask contains four times as much "
                "reactant as product, and these amounts do not change. "
                "Explain what this shows.",
        "options": [
            "The forward and reverse reactions run at equal rates, even "
            "though the amounts are unequal",
            "The forward reaction has stopped, because there is still four "
            "times as much reactant left",
            "The mixture is not yet at equilibrium, because the amounts are "
            "not equal",
            "The reverse reaction is running four times faster than the "
            "forward reaction",
        ],
        "correct_index": 0,
        "why": "Equilibrium means equal RATES, not equal amounts — constant "
               "concentrations are the sign that the two reactions are "
               "keeping pace with each other.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-h02",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same reversible reaction is set up in two identical "
                "sealed flasks at the same temperature: one starting from "
                "pure reactants, the other from pure products. Predict the "
                "final composition of each.",
        "options": [
            "Only the first flask reaches equilibrium; the second one "
            "cannot react backwards at all",
            "The second ends up with more product, because it started with "
            "product",
            "Both reach the same equilibrium composition, approached from "
            "opposite directions",
            "Both end with exactly equal amounts of reactant and product",
        ],
        "correct_index": 2,
        "why": "Equilibrium is a balance point fixed by the conditions, not "
               "by which side of the equation you start from.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-h03",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'At equilibrium the reaction has stopped, "
                "because nothing changes any more.' Identify what is wrong "
                "with this.",
        "options": [
            "Nothing is wrong — equilibrium does mean the reaction has "
            "finished",
            "Both reactions are still happening, at equal rates, so no net "
            "change is seen",
            "The forward reaction has stopped but the reverse reaction "
            "continues",
            "The reaction is still going, but only in the warmest region of "
            "the flask",
        ],
        "correct_index": 1,
        "why": "The equilibrium is dynamic — molecules still react in both "
               "directions, and it is only the rates being equal that makes "
               "the concentrations look frozen.",
    },
    {
        "id": "ks4-reversible-reactions-equilibrium-h04",
        "subtopic_slug": "reversible-reactions-equilibrium",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why hydrated and anhydrous copper sulfate can be "
                "converted back and forth repeatedly, while a slice of burnt "
                "toast cannot be turned back into bread.",
        "options": [
            "Because copper sulfate contains no carbon at all, and "
            "reactions involving carbon are always irreversible",
            "Because the toaster raises the temperature past the point at "
            "which any reversal becomes possible",
            "Because toast is a mixture and copper sulfate is a compound, "
            "and only compounds can react",
            "Because the copper sulfate change is reversible, while burning "
            "is irreversible and its products escape",
        ],
        "correct_index": 3,
        "why": "Only some reactions can run backwards, and burning is not "
               "one of them — the gases produced leave and the original "
               "substances cannot reform.",
    },

    # ── effect-of-conditions-equilibrium ────────────────────────────────
    {
        "id": "ks4-effect-of-conditions-equilibrium-e01",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State Le Chatelier's principle.",
        "options": [
            "A system at equilibrium always shifts towards the products",
            "A system at equilibrium keeps equal concentrations of all "
            "species",
            "A system at equilibrium shifts in the direction that opposes "
            "any change made to it",
            "A system at equilibrium reaches its final position faster when "
            "a catalyst is added",
        ],
        "correct_index": 2,
        "why": "The equilibrium moves so as to partly cancel out whatever "
               "change has been imposed on it.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-e02",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the effect of adding a catalyst on the position of an "
                "equilibrium.",
        "options": [
            "No effect on the position; equilibrium is simply reached sooner",
            "The position shifts right, so more product is present at "
            "equilibrium",
            "The position shifts towards whichever side is the exothermic "
            "one",
            "The position shifts left, because the reverse reaction is "
            "speeded up more",
        ],
        "correct_index": 0,
        "why": "A catalyst speeds up the forward and reverse reactions "
               "equally, so the balance point between them is unchanged.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-e03",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "For N2(g) + 3H2(g) ⇌ 2NH3(g), state the number of moles of "
                "gas on each side of the equation.",
        "options": [
            "2 on the left and 4 on the right",
            "1 on the left and 2 on the right",
            "3 on the left and 2 on the right",
            "4 on the left and 2 on the right",
        ],
        "correct_index": 3,
        "why": "One mole of N2 plus three of H2 gives four moles of gas on "
               "the left, against two moles of NH3 on the right.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-e04",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the direction in which an equilibrium shifts when the "
                "temperature is raised.",
        "options": [
            "In the exothermic direction, so as to release the extra heat",
            "In the endothermic direction, so as to absorb the extra heat",
            "Towards whichever side has more moles of gas",
            "It does not shift at all; only pressure moves an equilibrium",
        ],
        "correct_index": 1,
        "why": "Absorbing the added energy opposes the temperature rise, so "
               "the endothermic direction is favoured.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-s01",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "For N2(g) + 3H2(g) ⇌ 2NH3(g), ΔH = −92 kJ/mol. Predict the "
                "effect of raising the temperature on the equilibrium yield "
                "of ammonia.",
        "options": [
            "The yield rises, because a higher temperature always produces "
            "more of the product overall",
            "The yield rises, because the exothermic forward direction is "
            "favoured",
            "The yield is unchanged, because temperature only alters the "
            "rate",
            "The yield falls, because the equilibrium shifts left in the "
            "endothermic direction",
        ],
        "correct_index": 3,
        "why": "The forward reaction is exothermic, so heating favours the "
               "reverse, endothermic direction and less ammonia is present "
               "at equilibrium.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-s02",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "For 2SO2(g) + O2(g) ⇌ 2SO3(g), predict the effect of "
                "removing SO3 from the mixture as it is formed.",
        "options": [
            "The equilibrium shifts left, to replace the SO2 that was used "
            "up",
            "The equilibrium shifts right, forming more SO3 to replace what "
            "was taken",
            "The equilibrium does not move, because SO3 is a product and not "
            "a reactant",
            "The equilibrium shifts right, but only if the pressure is "
            "raised at the same time",
        ],
        "correct_index": 1,
        "why": "Removing a product makes the system act to replace it, so "
               "the forward reaction is favoured.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-s03",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "For H2(g) + I2(g) ⇌ 2HI(g), predict the effect of "
                "increasing the pressure on the position of equilibrium.",
        "options": [
            "It shifts right, because higher pressure always favours the "
            "products",
            "It shifts left, because the reactants are two separate "
            "substances",
            "It does not move, because both sides have the same number of "
            "moles of gas",
            "It shifts right, because HI molecules are smaller than I2 "
            "molecules",
        ],
        "correct_index": 2,
        "why": "Pressure only moves an equilibrium when the two sides differ "
               "in their moles of gas, and here both sides have two.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-s04",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "For CaCO3(s) ⇌ CaO(s) + CO2(g) the forward reaction is "
                "endothermic. Predict the effect of raising the temperature "
                "on the amount of CO2 at equilibrium.",
        "options": [
            "More CO2, because heating favours the endothermic forward "
            "direction",
            "Less CO2, because heating favours the exothermic direction, "
            "which is the forward one",
            "No change, because a solid cannot take part in an equilibrium "
            "at all",
            "Less CO2, because the gas simply escapes faster at higher "
            "temperature",
        ],
        "correct_index": 0,
        "why": "The forward reaction absorbs energy, so raising the "
               "temperature shifts the equilibrium right and more carbon "
               "dioxide is present.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-h01",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "For N2(g) + 3H2(g) ⇌ 2NH3(g), explain why the Haber "
                "process is run at about 200 atmospheres rather than at "
                "atmospheric pressure, and give the drawback.",
        "options": [
            "High pressure shifts the equilibrium left towards fewer moles, "
            "but it makes the plant slower",
            "High pressure shifts the equilibrium right towards two moles "
            "of gas, raising the yield, but costly vessels are needed",
            "High pressure lowers the activation energy and so raises the "
            "yield, but it damages the iron catalyst",
            "High pressure raises the temperature of the gases and so "
            "raises the yield, but it wastes a great deal of energy in "
            "doing so",
        ],
        "correct_index": 1,
        "why": "With four moles of gas on the left and two on the right, "
               "compressing the mixture favours the ammonia side, at the "
               "cost of equipment that can hold the pressure.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-h02",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Predict and explain the effect on the equilibrium yield of "
                "ammonia of replacing the iron catalyst with a more finely "
                "divided one.",
        "options": [
            "The yield rises, because more catalyst surface produces more "
            "ammonia",
            "The yield falls, because the catalyst adsorbs some of the "
            "ammonia onto its surface",
            "The yield rises, because the extra surface shifts the "
            "equilibrium to the right",
            "The yield is unchanged; equilibrium is simply reached more "
            "quickly",
        ],
        "correct_index": 3,
        "why": "A catalyst speeds both directions equally, so it changes how "
               "fast equilibrium arrives, never where it lies.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-h03",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "For 2NO2(g) ⇌ N2O4(g), ΔH = −57 kJ/mol, the mixture is "
                "first cooled and then compressed. Predict the effect of "
                "each change on the amount of N2O4.",
        "options": [
            "Both changes increase the amount of N2O4",
            "Cooling increases it; compressing decreases it",
            "Cooling decreases it; compressing increases it",
            "Both changes decrease the amount of N2O4",
        ],
        "correct_index": 0,
        "why": "The forward reaction is exothermic and goes from two moles "
               "of gas to one, so both cooling and compressing push the "
               "equilibrium to the right.",
    },
    {
        "id": "ks4-effect-of-conditions-equilibrium-h04",
        "subtopic_slug": "effect-of-conditions-equilibrium",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A chemist claims that raising the pressure in the Haber "
                "process increases the equilibrium constant as well as the "
                "yield of ammonia. Evaluate this claim.",
        "options": [
            "Correct — pressure and temperature both change the equilibrium "
            "constant",
            "Correct — the yield and the equilibrium constant always change "
            "together in the same way",
            "Wrong — pressure changes the amounts present, but only "
            "temperature changes the equilibrium constant",
            "Wrong — raising the pressure changes neither the amounts "
            "present nor the value of the equilibrium constant",
        ],
        "correct_index": 2,
        "why": "Raising the pressure moves the position of equilibrium, but "
               "the constant describing the balance at a given temperature "
               "is altered only by temperature.",
    },
]
