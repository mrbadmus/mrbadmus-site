"""Chemistry · Energy changes — the MRB-338 expansion, subtopic
`exothermic-endothermic`.

The base file and the MRB-335 extension between them already cover the
definitions, the everyday examples, Q = mcΔT in both directions, insulation
and stirring, and the limiting-reactant / rate-versus-amount distinctions.
This file goes wider across the same spec point (5.5.1.1): a specific heat
capacity that is not water's 4.18 J/g°C, the parts of the required practical
not yet touched (housing the cup, reading discipline, comparing fuels
side by side), two named real reactions (thermite; the anhydrous-copper-
sulfate exception to "dissolving is endothermic"), and the multi-step
evaluation work — percentage energy lost, energy per gram from a fuel's
molar value, and ranking several metals' total energy release from Ar and
reactivity together.
"""

TOPIC = "energy-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── standard ─────────────────────────────────────────────────────────
    {
        "id": "ks4-exothermic-endothermic-s13",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction takes place in 40 g of cooking oil, which has a "
                "specific heat capacity of 2.0 J/g°C, and the temperature "
                "rises by 15.0 °C. Calculate the energy released.",
        "options": [
            "1200 J",
            "600 J",
            "2508 J",
            "80 J",
        ],
        "correct_index": 0,
        "why": "Q = mcΔT = 40 × 2.0 × 15.0 = 1200 J, using the oil's own "
               "specific heat capacity rather than water's.",
    },
    {
        "id": "ks4-exothermic-endothermic-s14",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In an energy-change experiment, a polystyrene cup is stood "
                "inside a glass beaker rather than left standing alone on "
                "the bench. State why.",
        "options": [
            "The beaker insulates the cup, cutting down further heat loss "
            "to the surroundings",
            "The beaker holds the thin-walled cup steady and stops it "
            "tipping over during stirring",
            "The beaker reacts with any acid that is spilled, making the "
            "experiment safer",
            "The beaker is needed to measure out the correct volume of "
            "solution before it is carefully poured into the cup",
        ],
        "correct_index": 1,
        "why": "A polystyrene cup is light and thin-walled, so the beaker's "
               "job is purely to support it while it is stirred and read — "
               "it plays no part in the insulation.",
    },
    {
        "id": "ks4-exothermic-endothermic-s15",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a student records the temperature every 30 "
                "seconds during a neutralisation, rather than taking a "
                "single reading once the mixing looks complete.",
        "options": [
            "A single late reading might be taken after the mixture has "
            "already started cooling, missing the true highest temperature",
            "The exam board sets a fixed minimum of five recorded readings "
            "for every practical carried out, whichever quantity happens "
            "to be measured in the experiment",
            "Frequent readings let the student calculate the rate of the "
            "neutralisation reaction directly, rather than its energy "
            "change",
            "A single reading cannot be plotted on a graph, so no useful "
            "result could sensibly be reported from it",
        ],
        "correct_index": 0,
        "why": "The mixture starts losing energy to the surroundings as "
               "soon as the reaction finishes, so only regular readings "
               "reliably catch the actual highest point reached.",
    },
    {
        "id": "ks4-exothermic-endothermic-s16",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reusable hand warmer contains a supersaturated solution "
                "of sodium acetate that releases energy when it "
                "crystallises. Once used up, it is recharged by boiling it "
                "in water. Explain why boiling recharges it.",
        "options": [
            "Boiling replaces the sodium acetate inside the pack with a "
            "fresh supply of the same chemical dissolved out of whichever "
            "water it happens to be placed in",
            "Boiling redissolves the crystals, and this is endothermic — it "
            "reverses the exothermic crystallisation and resets the pack",
            "Boiling sterilises the pack, and it is these sterile "
            "conditions inside that allow the exothermic reaction to "
            "restart",
            "Boiling evaporates away the water inside, concentrating the "
            "sodium acetate until it is ready to crystallise again",
        ],
        "correct_index": 1,
        "why": "Supplying heat dissolves the solid sodium acetate back into "
               "solution, taking energy in and undoing the exothermic "
               "change so the pack is ready to release it again.",
    },
    {
        "id": "ks4-exothermic-endothermic-s17",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the same student, using the same thermometer, "
                "should take every temperature reading in a repeated "
                "energy-change experiment.",
        "options": [
            "It makes the readings more accurate, because school rules say "
            "just one named person is allowed to record any experiment's "
            "results",
            "It makes the readings more reliable, because it removes small "
            "differences between how different people read the same scale",
            "It is required so that the thermometer being used does not "
            "need to be recalibrated in between each of the repeats",
            "It changes the specific heat capacity of the solution being "
            "tested, so exactly the same reader is needed each time for "
            "the calculation to come out right",
        ],
        "correct_index": 1,
        "why": "Reliability is about repeats agreeing with each other; "
               "using one person and one instrument removes a source of "
               "variation between the readings, though it says nothing "
               "about whether any of them is accurate.",
    },
    {
        "id": "ks4-exothermic-endothermic-s18",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants to compare the energy released by two "
                "different fuels fairly. Identify the variables that must "
                "be kept the same between the two tests.",
        "options": [
            "The volume of water heated, its starting temperature, the "
            "type of container and the distance from the flame to the "
            "container",
            "The mass of fuel burned in each of the two tests and the "
            "particular colour that each of the two flames happens to "
            "produce as it burns",
            "The volume of water heated in each test and the brand or "
            "manufacturer that supplied the sample of fuel being tested",
            "The starting temperature of the water and the exact time of "
            "day at which each of the two separate tests is carried out",
        ],
        "correct_index": 0,
        "why": "Everything except the identity of the fuel has to be held "
               "constant, or a difference in the results could be caused by "
               "the set-up rather than by the fuel itself.",
    },
    {
        "id": "ks4-exothermic-endothermic-s19",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student burns a fuel in the open air, with no can or "
                "cup around the flame, and tries to use the temperature "
                "rise of a nearby beaker of water to find its energy "
                "content. Explain why this method is unreliable.",
        "options": [
            "An open flame generally burns at far too low a temperature to "
            "transfer any measurable amount of energy into the nearby "
            "beaker of water",
            "Almost all of the energy released escapes to the surrounding "
            "air rather than reaching the water",
            "A fuel burning freely in the open air undergoes a completely "
            "different, endothermic reaction instead of its usual one",
            "The water in the nearby beaker evaporates away completely "
            "before any useful reading can be taken from it",
        ],
        "correct_index": 1,
        "why": "With nothing to direct the flame's energy towards the "
               "water, almost all of it is lost to the room, so the "
               "temperature rise measured is far smaller than the true "
               "energy released.",
    },
    {
        "id": "ks4-exothermic-endothermic-s20",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neutralisation is carried out on a warm day, starting at "
                "24 °C instead of the usual 18 °C, but releases the same "
                "amount of energy to the same mass of solution. Compare the "
                "maximum temperature reached and the temperature rise with "
                "the usual result.",
        "options": [
            "Both the maximum temperature and the temperature rise are "
            "higher than usual",
            "The maximum temperature is higher than usual, but the "
            "temperature rise is unchanged",
            "The temperature rise is higher than usual, but the maximum "
            "temperature is unchanged",
            "Both the maximum temperature and the temperature rise are "
            "lower than usual, because warm solution absorbs less energy",
        ],
        "correct_index": 1,
        "why": "The maximum temperature simply starts from a higher point, "
               "but the rise depends only on how much energy the same "
               "reaction releases into the same mass of solution.",
    },
    {
        "id": "ks4-exothermic-endothermic-s21",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The thermite reaction, in which powdered aluminium "
                "reduces iron oxide to molten iron, is used to weld railway "
                "tracks together on site. State the type of reaction this "
                "must be, and why it suits this use.",
        "options": [
            "Endothermic, because it needs a blowtorch to supply enough "
            "energy to melt the iron",
            "Exothermic, because it releases enough energy on its own to "
            "melt the iron produced",
            "Endothermic, because the molten iron must absorb energy from "
            "the rail before it will set",
            "Exothermic, but the energy it releases is far too small to "
            "melt any metal without some extra heating from outside",
        ],
        "correct_index": 1,
        "why": "The thermite reaction releases so much energy that the iron "
               "it produces comes out already molten, with no external "
               "heat source needed once it is started.",
    },
    {
        "id": "ks4-exothermic-endothermic-s22",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fixed mass of magnesium reacts completely with an excess "
                "of hydrochloric acid twice: once using acid at room "
                "temperature, once using acid warmed to 40 °C. Compare the "
                "total energy released in the two reactions.",
        "options": [
            "The warmed acid releases more total energy overall, because "
            "warming a liquid generally adds extra chemical energy into "
            "it before the two are even mixed",
            "The warmed acid releases less total energy, because some "
            "energy has already escaped from the acid before mixing",
            "Both reactions release the same total energy, because the "
            "same mass of magnesium reacts completely either way",
            "The room-temperature acid releases more total energy, because "
            "a cooler start allows more energy to be stored",
        ],
        "correct_index": 2,
        "why": "Warming the acid makes the reaction go faster, but the "
               "energy released depends on the amount of magnesium that "
               "reacts, which is unchanged.",
    },
    {
        "id": "ks4-exothermic-endothermic-s23",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical, dilute acid is used in excess "
                "while the amount of alkali is fixed and measured "
                "precisely. Explain why the acid, not the alkali, is the "
                "one added in excess.",
        "options": [
            "It guarantees that every particle of the measured, limited "
            "reactant reacts, so the energy released reflects that fixed "
            "amount exactly",
            "It is done purely for safety reasons, since dilute acids are "
            "considered more hazardous than alkalis and so should ideally "
            "be used up as quickly as possible",
            "It makes the final mixture come out neutral overall, which is "
            "a condition that has to be met before any temperature reading "
            "can be taken from it",
            "It speeds up how quickly the reaction proceeds, so that less "
            "of the released energy has time to escape to the surroundings "
            "before it is measured",
        ],
        "correct_index": 0,
        "why": "Using an excess of one reactant ensures the other, "
               "carefully measured one reacts completely, so the "
               "temperature change can be linked to a known amount of "
               "reaction.",
    },
    {
        "id": "ks4-exothermic-endothermic-s24",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station burns natural gas to heat water into "
                "steam, which then drives a turbine to generate "
                "electricity. State the type of reaction taking place in "
                "the burner, and identify the energy transfer it relies on.",
        "options": [
            "Endothermic — the burning gas absorbs energy from the steam "
            "to keep the flame alight",
            "Exothermic — the burning gas releases energy that transfers "
            "to the water, turning it into steam",
            "Endothermic — energy is absorbed from the turbine and "
            "transferred back into the gas supply",
            "Exothermic, but the energy released plays no real part in "
            "how the steam ends up being produced",
        ],
        "correct_index": 1,
        "why": "Combustion is exothermic, and the whole process depends on "
               "that released energy being transferred to the water to "
               "produce the steam that drives the turbine.",
    },
    {
        "id": "ks4-exothermic-endothermic-s25",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single-use hand warmer works by the oxidation of iron "
                "powder in air, a chemical reaction. A reusable hand "
                "warmer works by the crystallisation of a supersaturated "
                "salt solution, a physical change. Compare the two in "
                "terms of whether they can be reused.",
        "options": [
            "Both can be reused as many times as anybody needs, because "
            "any exothermic process whatsoever can simply be triggered "
            "again once it has finished releasing its stored energy",
            "Neither warmer can be reused, because both kinds of process "
            "use up a fixed store of chemical energy that cannot be "
            "restored once it has gone",
            "The iron warmer cannot be reused, because the iron is "
            "permanently oxidised; the salt warmer can be reset by "
            "redissolving the crystals",
            "The salt warmer cannot be reused, because crystallisation of "
            "a supersaturated solution is essentially an irreversible "
            "chemical reaction, not a physical one",
        ],
        "correct_index": 2,
        "why": "Oxidising iron is a one-way chemical change, while "
               "crystallising a salt solution is a physical change that "
               "can be reversed simply by redissolving it.",
    },
    {
        "id": "ks4-exothermic-endothermic-s26",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the extra piece of data needed to convert an "
                "'energy released per gram of fuel' value into an 'energy "
                "released per mole of fuel' value.",
        "options": [
            "The exact temperature at which the sample of fuel happened to "
            "be stored in the laboratory before it was burned",
            "The relative formula mass of the fuel, so the per-gram value "
            "can be scaled up to a per-mole value",
            "The specific heat capacity of whichever liquid was used in "
            "the calorimeter to absorb the released energy",
            "The total volume of water that was heated by the fuel during "
            "the course of the whole experiment",
        ],
        "correct_index": 1,
        "why": "Multiplying the energy released per gram by the fuel's "
               "relative formula mass converts it into energy released per "
               "mole, since one mole has a mass equal to the Mr in grams.",
    },

    # ── harder ───────────────────────────────────────────────────────────
    {
        "id": "ks4-exothermic-endothermic-h12",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "50 g of cooking oil absorbs 2100 J of energy in a "
                "calorimetry experiment and its temperature rises by "
                "21.0 °C. Determine the specific heat capacity of the oil.",
        "options": [
            "2.0 J/g°C",
            "4.18 J/g°C",
            "100.0 J/g°C",
            "42.0 J/g°C",
        ],
        "correct_index": 0,
        "why": "Rearranging Q = mcΔT gives c = Q ÷ (m × ΔT) = "
               "2100 ÷ (50 × 21.0) = 2.0 J/g°C — much lower than water's "
               "4.18 J/g°C.",
    },
    {
        "id": "ks4-exothermic-endothermic-h13",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The accepted energy released by a reaction is 5000 J, but "
                "a school calorimetry experiment measures only 4200 J. "
                "Calculate the percentage of the energy that was lost to "
                "the surroundings.",
        "options": [
            "16%",
            "84%",
            "8.0%",
            "19%",
        ],
        "correct_index": 0,
        "why": "The energy lost is 5000 − 4200 = 800 J, and "
               "(800 ÷ 5000) × 100 = 16% of the accepted value was lost "
               "before it reached the thermometer.",
    },
    {
        "id": "ks4-exothermic-endothermic-h14",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fuel X releases 640 kJ/mol and has an Mr of 32. Fuel Y "
                "releases 690 kJ/mol and has an Mr of 46. Determine which "
                "fuel releases more energy per gram.",
        "options": [
            "Fuel X, at 20 kJ/g against fuel Y's 15 kJ/g",
            "Fuel Y, at 15 kJ/g against fuel X's 20 kJ/g",
            "Fuel Y, because 690 kJ/mol is the larger of the two molar "
            "values",
            "Both release the same energy per gram, since it is the molar "
            "value that matters most when comparing fuels",
        ],
        "correct_index": 0,
        "why": "Dividing each molar value by its Mr gives energy per gram: "
               "640 ÷ 32 = 20 kJ/g for X and 690 ÷ 46 = 15 kJ/g for Y, so X "
               "is the more energy-dense fuel by mass despite the smaller "
               "molar value.",
    },
    {
        "id": "ks4-exothermic-endothermic-h15",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One student carries out a neutralisation in a polystyrene "
                "cup, another in a large glass beaker of similar volume, "
                "using identical reactants. Compare their measured energy "
                "values with the true value.",
        "options": [
            "The beaker gives the closer value, because glass is a much "
            "better conductor of heat and so it spreads the released "
            "energy more evenly all through the mixture as it forms",
            "Both give equally accurate values in the end, because the "
            "material a container happens to be made from cannot affect "
            "the outcome of a chemical reaction",
            "The cup gives the closer value: the beaker both conducts more "
            "energy away and absorbs some of it warming its own greater "
            "mass of glass",
            "The beaker gives the closer value, because its noticeably "
            "larger volume is able to hold on to more of the energy that "
            "is released during the reaction",
        ],
        "correct_index": 2,
        "why": "An insulating polystyrene cup loses far less energy by "
               "conduction than a glass beaker, and a heavy glass beaker "
               "also takes some of the energy to warm itself, an error the "
               "light cup barely adds.",
    },
    {
        "id": "ks4-exothermic-endothermic-h16",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Equal masses of magnesium (Ar = 24) and zinc (Ar = 65) are "
                "each reacted completely with an excess of dilute "
                "hydrochloric acid. Magnesium is also more reactive than "
                "zinc. Compare the total energy released by the two "
                "reactions.",
        "options": [
            "Zinc releases more overall, because its greater relative "
            "atomic mass means that a correspondingly greater mass of that "
            "metal has evidently reacted with the acid",
            "The two metals release exactly the same total amount of "
            "energy between them, because an identical starting mass of "
            "each metal was carefully weighed out and used in the tests",
            "Magnesium releases more: the same mass gives more moles of "
            "magnesium, and it is also the more reactive of the two metals",
            "Zinc releases more overall, because a metal that is less "
            "reactive is understood to store more chemical energy within "
            "itself in the first place",
        ],
        "correct_index": 2,
        "why": "A lower Ar means the same mass of magnesium supplies more "
               "moles than zinc does, and being the more reactive metal "
               "too, both factors point the same way: more energy from the "
               "magnesium.",
    },
    {
        "id": "ks4-exothermic-endothermic-h17",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student first insulates the sides of a reaction cup with "
                "a polystyrene jacket, then also adds a lid with a small "
                "hole for the thermometer. Explain why adding the lid "
                "further reduces the underestimate of the energy released.",
        "options": [
            "The jacket by itself already stops the whole of the loss, so "
            "adding a lid on top can merely change how quickly the "
            "individual readings happen to be taken",
            "The jacket stops energy escaping through the sides by "
            "conduction, but energy can still rise and escape from the "
            "open top without a lid",
            "The lid noticeably increases the total mass of the whole "
            "apparatus, which in turn raises its overall specific heat "
            "capacity and so traps more of the released energy",
            "The lid evidently reacts chemically with the mixture inside, "
            "releasing extra energy of its own that adds on to the total "
            "amount measured",
        ],
        "correct_index": 1,
        "why": "Side insulation only blocks one escape route; without a "
               "lid, energy can still leave from the open top as the warm "
               "mixture loses heat and vapour upwards.",
    },
    {
        "id": "ks4-exothermic-endothermic-h18",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Reaction P releases energy that warms 50 g of water by "
                "15.0 °C when 2.00 g of fuel is burned. Reaction Q releases "
                "energy that warms the same mass of water by 18.0 °C when "
                "3.00 g of fuel is burned. Using c = 4.18 J/g°C, compare "
                "the energy released per gram of fuel.",
        "options": [
            "P releases about 1568 J/g, more than Q's about 1254 J/g",
            "Q releases about 1568 J/g, more than P's about 1254 J/g",
            "Both release about 1400 J/g, since the temperature rises are "
            "close to each other",
            "P releases about 3135 J/g, more than Q's about 2258 J/g",
        ],
        "correct_index": 0,
        "why": "P: Q = 50 × 4.18 × 15.0 = 3135 J ÷ 2.00 g = 1568 J/g. Q: "
               "Q = 50 × 4.18 × 18.0 = 3762 J ÷ 3.00 g = 1254 J/g. P burned "
               "less fuel for nearly as much water warming, so it releases "
               "more energy per gram.",
    },
    {
        "id": "ks4-exothermic-endothermic-h19",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shop assistant tells a customer that any used hand "
                "warmer can be 'recharged' by boiling it in water, "
                "including both a sodium-acetate crystallisation warmer "
                "and an iron-oxidation warmer. Evaluate this claim.",
        "options": [
            "It is correct for both kinds of warmer, because boiling in "
            "water generally manages to reverse whichever exothermic "
            "process originally took place inside the pack itself",
            "It is correct for neither kind of warmer, because boiling any "
            "hand warmer that has already been used is considered unsafe "
            "and destroys its outer packaging",
            "It is correct only for the sodium-acetate warmer: boiling "
            "redissolves its crystals, but boiling cannot turn iron oxide "
            "back into iron",
            "It is correct for the iron-oxidation warmer specifically, "
            "because iron oxide is known to decompose back into iron and "
            "oxygen gas whenever it is heated in water",
        ],
        "correct_index": 2,
        "why": "Crystallisation is a physical change that boiling can "
               "reverse, but the iron warmer's oxidation is a chemical "
               "change with no way to reverse it just by heating it in "
               "water.",
    },
    {
        "id": "ks4-exothermic-endothermic-h20",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student assumes dissolving a solid in water is always "
                "endothermic. They then dissolve white anhydrous copper "
                "sulfate in water and find the temperature rises sharply "
                "as it turns blue. Identify the error in the assumption.",
        "options": [
            "There is no error in the assumption whatsoever: the rise in "
            "temperature simply shows that this must be a chemical change "
            "rather than a case of one substance dissolving in another",
            "Dissolving anhydrous copper sulfate is an exception: the "
            "energy released bonding water to the ions exceeds the energy "
            "needed to separate the solid",
            "The colour change to blue is what evidently absorbs energy "
            "from the surroundings here, and that is what makes the water "
            "feel warmer by mistake",
            "The thermometer is simply responding to the copper in the "
            "compound conducting the room's background heat faster than "
            "plain water normally does",
        ],
        "correct_index": 1,
        "why": "Most dissolving is endothermic, but this is a real "
               "exception: the energy released as water molecules "
               "surround and bond to the copper and sulfate ions is "
               "greater than the energy needed to break up the solid.",
    },
    {
        "id": "ks4-exothermic-endothermic-h21",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Burning 0.0200 mol of a fuel in a school calorimeter is "
                "measured to release 620 kJ/mol, but the data-book accepted "
                "value is 890 kJ/mol. Suggest the most likely reason for "
                "the difference.",
        "options": [
            "The accepted value must simply be wrong, since a school "
            "measurement made with real apparatus is generally the more "
            "reliable of the two values",
            "The fuel burned amounted to just 0.0200 mol rather than a "
            "whole mole, and this is what lowers the final molar value "
            "that comes out of the calculation",
            "Energy was lost to the surroundings during the school "
            "experiment, so less reached the water than the fuel actually "
            "released",
            "The accepted value must include energy released by some "
            "second reaction that simply does not happen inside a school "
            "calorimeter",
        ],
        "correct_index": 2,
        "why": "A school set-up cannot capture every joule released — some "
               "always escapes to the air and apparatus — so the measured "
               "value comes out lower than the true, accepted one.",
    },
    {
        "id": "ks4-exothermic-endothermic-h22",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that comparing the temperature of two "
                "fuels' flames is the same as comparing how much total "
                "energy each one releases. Evaluate this claim.",
        "options": [
            "The claim is correct, because whichever flame burns hotter "
            "must inevitably contain the greater total amount of energy "
            "overall, regardless of anything else about the two tests",
            "The claim is incorrect: flame temperature depends on how "
            "concentrated the release is, while total energy also depends "
            "on the mass burned",
            "The claim is correct for gas fuels specifically, because "
            "liquid fuels burning in the open air do not produce a "
            "measurable flame temperature of any kind",
            "The claim is incorrect, because a flame's temperature has "
            "nothing whatsoever to do with the fuel's stored chemical "
            "energy in the first place",
        ],
        "correct_index": 1,
        "why": "A very hot, brief flame from a small mass of fuel can "
               "release less total energy than a cooler flame burning for "
               "longer or burning more fuel.",
    },
    {
        "id": "ks4-exothermic-endothermic-h23",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction in an open cup is seen to make a loud crackling "
                "sound and give off a bright flash as well as warming the "
                "solution. Explain why the value calculated from Q = mcΔT "
                "underestimates the total chemical energy released.",
        "options": [
            "Q = mcΔT only measures energy transferred to the solution as "
            "heat, so energy leaving as sound and light is left out of the "
            "calculation entirely",
            "The sound and light must be produced after the reaction has "
            "already finished, so they belong to some entirely separate "
            "process instead",
            "A loud sound generally means that the reaction taking place "
            "must be endothermic, which makes the calculated value come "
            "out too large rather than too small",
            "Sound and light are not able to carry any energy of their "
            "own whatsoever, so neither of them can be the reason for an "
            "underestimate here",
        ],
        "correct_index": 0,
        "why": "The formula only accounts for energy that ends up heating "
               "the solution; any energy that instead leaves as sound or "
               "light is real chemical energy that Q = mcΔT never sees.",
    },
    {
        "id": "ks4-exothermic-endothermic-h24",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Equal masses of magnesium (Ar = 24), zinc (Ar = 65) and "
                "iron (Ar = 56) are each reacted completely with excess "
                "dilute hydrochloric acid. The reactivity order is "
                "magnesium > zinc > iron. Rank the three by the total "
                "energy each releases.",
        "options": [
            "Iron highest, then zinc, then magnesium, since iron evidently "
            "has the smallest Ar of the three and so gives the most moles "
            "per gram reacted",
            "Magnesium highest, then zinc, then iron, since it gives the "
            "most moles per gram and is also the most reactive metal",
            "All three metals release exactly the same total energy "
            "between them, because an identical starting mass of metal "
            "was used in every one of the three separate cases",
            "Zinc highest, then iron, then magnesium, since zinc's "
            "noticeably larger Ar is taken to mean a stronger reaction "
            "with the dilute acid",
        ],
        "correct_index": 1,
        "why": "Magnesium's low Ar gives the most moles for a fixed mass, "
               "and it is also the most reactive of the three, so both "
               "factors place it first; the same reasoning ranks zinc "
               "above iron.",
    },
    {
        "id": "ks4-exothermic-endothermic-h25",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student burns 0.500 g of a fuel and measures a mean rate "
                "of 27.0 kJ of energy released per gram. Determine the mass "
                "of the fuel that must be burned to raise the temperature "
                "of 500 g of water, c = 4.18 J/g°C, by 20.0 °C.",
        "options": [
            "1.55 g",
            "0.155 g",
            "15.5 g",
            "27.0 g",
        ],
        "correct_index": 0,
        "why": "Q = 500 × 4.18 × 20.0 = 41 800 J = 41.8 kJ, and dividing by "
               "27.0 kJ released per gram gives 41.8 ÷ 27.0 = 1.55 g of "
               "fuel needed.",
    },
    {
        "id": "ks4-exothermic-endothermic-h26",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student burns a small mass of fuel under a small volume "
                "of water and calculates 7.2 kJ/g; a second student burns a "
                "much larger mass of the same fuel under a proportionally "
                "larger volume of water and calculates 9.8 kJ/g. Evaluate "
                "which result is likely to be closer to the true value.",
        "options": [
            "The first student's result, because using a smaller mass of "
            "fuel generally keeps the whole reaction under noticeably "
            "better control throughout",
            "The second student's, because the loss of energy to the "
            "surroundings is roughly fixed in size, so it is a smaller "
            "proportion of a larger total release",
            "Neither result is any more trustworthy than the other, "
            "because both students happened to use exactly the same fuel "
            "as one another",
            "The first student's result, because a smaller flame merely "
            "burns for a shorter time, giving the heat far less chance to "
            "escape",
        ],
        "correct_index": 1,
        "why": "Heat losses to the room stay roughly the same size "
               "whatever the scale of the experiment, so they make up a "
               "smaller fraction of a larger energy release, bringing the "
               "second student's result nearer the true value.",
    },
]
