"""Chemistry · Energy changes — the MRB-335 extension.

The twelve questions per subtopic in `energy_changes.py` are the AUTOMATIC
weekly assignment's pool and are frozen at bank positions 0-11. This file
holds the rows Set work v2 added on top, because the 7 Sep 2026 availability
table put every one of this topic's four cells below fifty: Combined
Foundation offered twenty-four questions and Combined Higher twenty-eight,
which is not a pool a teacher can pick twenty from.

⚠️ The Foundation cell of a BASE topic can only be fed by base subtopics, and
`energy-changes` has exactly two — `exothermic-endothermic` and
`reaction-profiles`. So most of the weight lands on those two, and most of it
on the first: exothermic/endothermic carries the whole of RP5, the fuel
comparison and every calorimetry rearrangement, while reaction profiles is a
single diagram with four features on it. Loading the two equally would have
meant inventing reaction-profile questions that differ only in their numbers,
which is a worse defect than an uneven split.

Distractors continue the file they extend: the surroundings read backwards
from what the reaction does, the FINAL temperature used where the temperature
CHANGE belongs, activation energy measured to the products instead of to the
peak, and bond energies subtracted the wrong way round. The calorimetry
numbers are all new — none of them reuses the mass, the temperature or the
answer of the worked example printed on the lesson page.
"""

TOPIC = "energy-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── exothermic-endothermic ─────────────────── BASE (5.5.1.1) ── +23 ──
    {
        "id": "ks4-exothermic-endothermic-e05",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Magnesium ribbon is added to dilute hydrochloric acid and "
                "the mixture becomes noticeably warmer. State the type of "
                "reaction.",
        "options": [
            "Endothermic, because the acid loses energy to the magnesium",
            "Exothermic, because energy is released to the surroundings",
            "Endothermic, because a gas is given off and gases take energy in",
            "Neither, because a temperature change is a physical change",
        ],
        "correct_index": 1,
        "why": "A rise in the temperature of the surroundings means energy "
               "has been released by the reaction, which is what exothermic "
               "means.",
    },
    {
        "id": "ks4-exothermic-endothermic-e06",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the quantity that ΔT represents in Q = m × c × ΔT, "
                "and its unit.",
        "options": [
            "The temperature change of the solution, in °C",
            "The final temperature of the solution, in °C",
            "The thermal energy transferred, in J",
            "The time the reaction takes, in s",
        ],
        "correct_index": 0,
        "why": "ΔT is the CHANGE in temperature — the highest reading minus "
               "the starting reading — not the final temperature itself.",
    },
    {
        "id": "ks4-exothermic-endothermic-e07",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the total amount of energy during a "
                "chemical reaction.",
        "options": [
            "It increases in an exothermic reaction, because energy is "
            "created",
            "It decreases in an endothermic reaction, because energy is "
            "destroyed",
            "It stays the same — energy is transferred between the chemicals "
            "and the surroundings",
            "It stays the same only in reactions that are neither exothermic "
            "nor endothermic",
        ],
        "correct_index": 2,
        "why": "Energy is conserved: a reaction moves energy between the "
               "chemicals and their surroundings, it never makes or destroys "
               "any.",
    },
    {
        "id": "ks4-exothermic-endothermic-e08",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student records the temperature of a reaction mixture "
                "every 30 s. State which readings are used to find the "
                "temperature change of an exothermic reaction.",
        "options": [
            "The final temperature at the end, minus the starting temperature",
            "The highest temperature reached, on its own",
            "The mean of all the temperatures recorded",
            "The highest temperature reached, minus the starting temperature",
        ],
        "correct_index": 3,
        "why": "The mixture starts cooling once the reaction finishes, so the "
               "largest change is from the starting temperature to the "
               "highest reading, not to the last one.",
    },
    {
        "id": "ks4-exothermic-endothermic-e09",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student investigates how the volume of sodium hydroxide "
                "solution affects the temperature rise when it is "
                "neutralised by acid. State the independent variable.",
        "options": [
            "The volume of sodium hydroxide solution added",
            "The temperature rise of the mixture",
            "The concentration of the hydrochloric acid",
            "The type of cup the reaction is carried out in",
        ],
        "correct_index": 0,
        "why": "The independent variable is the one deliberately changed — "
               "here the volume of alkali; the temperature rise is what is "
               "measured in response.",
    },
    {
        "id": "ks4-exothermic-endothermic-e10",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State an everyday use of an ENDOTHERMIC process.",
        "options": [
            "A disposable hand warmer",
            "A self-heating can of coffee",
            "An instant cold pack for a sports injury",
            "A camping stove burning butane",
        ],
        "correct_index": 2,
        "why": "A cold pack works because the salt inside takes energy in "
               "from its surroundings as it dissolves; the other three all "
               "release energy.",
    },
    {
        "id": "ks4-exothermic-endothermic-e11",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit of c in Q = m × c × ΔT when the mass of "
                "solution is measured in grams.",
        "options": [
            "J/kg",
            "J/g°C",
            "J/°C",
            "°C/g",
        ],
        "correct_index": 1,
        "why": "c is the energy in joules needed to raise one gram of the "
               "solution by one degree Celsius, so its unit is J/g°C.",
    },
    {
        "id": "ks4-exothermic-endothermic-e12",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the change that releases energy to its "
                "surroundings.",
        "options": [
            "Water vapour condensing on a cold window",
            "Ice melting in a drink",
            "Water boiling in a kettle",
            "A puddle evaporating in the sun",
        ],
        "correct_index": 0,
        "why": "Condensing releases energy to the surroundings; melting, "
               "boiling and evaporating all take energy in.",
    },
    {
        "id": "ks4-exothermic-endothermic-s05",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction warms 75 g of solution from 18.5 °C to 27.5 °C. "
                "Using c = 4.18 J/g°C, calculate the energy released.",
        "options": [
            "282 J",
            "2820 J",
            "5800 J",
            "8620 J",
        ],
        "correct_index": 1,
        "why": "ΔT is 27.5 − 18.5 = 9.0 °C, so Q = 75 × 4.18 × 9.0 = 2820 J "
               "to 3 significant figures.",
    },
    {
        "id": "ks4-exothermic-endothermic-s06",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student investigates how the concentration of "
                "hydrochloric acid affects the temperature rise when it "
                "neutralises sodium hydroxide solution. Describe the control "
                "variables needed.",
        "options": [
            "The volume of acid, the volume and concentration of the "
            "alkali, and the type of cup",
            "The concentration of the acid and the temperature rise of the "
            "mixture",
            "The volume of acid and the concentration of the acid",
            "The temperature rise and the highest temperature reached",
        ],
        "correct_index": 0,
        "why": "Control variables are everything held constant so that only "
               "the acid concentration can explain a change in the "
               "temperature rise.",
    },
    {
        "id": "ks4-exothermic-endothermic-s07",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two fuels are burned in identical burners to heat 100 g of "
                "water in the same copper can, and each burner loses the "
                "same mass of fuel. Fuel A raises the water by 24 °C and "
                "fuel B by 15 °C. Compare the energy released per gram.",
        "options": [
            "Fuel B releases more per gram, because a smaller rise means the "
            "energy was stored rather than released",
            "They release the same per gram, because the same mass of fuel "
            "burned",
            "Nothing can be compared unless the two fuels have the same "
            "formula",
            "Fuel A releases more per gram, because the same mass of fuel "
            "warmed the same mass of water further",
        ],
        "correct_index": 3,
        "why": "The same mass of water and the same mass of fuel were used, "
               "so the larger temperature rise means more energy released "
               "per gram.",
    },
    {
        "id": "ks4-exothermic-endothermic-s08",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same mass of magnesium reacts completely with an excess "
                "of hydrochloric acid in a polystyrene cup. Predict which "
                "change would increase the temperature rise recorded.",
        "options": [
            "Using a larger volume of acid of the same concentration",
            "Stirring the mixture more slowly",
            "Using a smaller volume of acid, so the same energy warms less "
            "solution",
            "Using a thermometer with a finer scale",
        ],
        "correct_index": 2,
        "why": "The magnesium is the limiting reactant, so the energy "
               "released is fixed; sharing it between a smaller mass of "
               "solution gives a bigger rise.",
    },
    {
        "id": "ks4-exothermic-endothermic-s09",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student repeats a neutralisation four times and records "
                "temperature rises of 6.4 °C, 6.6 °C, 6.5 °C and 9.1 °C. "
                "Describe how the mean temperature rise should be found.",
        "options": [
            "Discard 9.1 °C as an anomaly and take the mean of the other "
            "three, giving 6.5 °C",
            "Take the mean of all four values, giving 7.15 °C, since every "
            "reading was recorded",
            "Take the largest value, 9.1 °C, because it lost the least "
            "energy",
            "Take the smallest value, 6.4 °C, because the others were "
            "warmed by the hand",
        ],
        "correct_index": 0,
        "why": "9.1 °C sits far outside the other three, so it is an anomaly "
               "and is left out of the mean rather than allowed to drag it "
               "up.",
    },
    {
        "id": "ks4-exothermic-endothermic-s10",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a reaction mixture is stirred before the "
                "temperature is read.",
        "options": [
            "So the energy spreads evenly and the thermometer reads the "
            "whole mixture",
            "So the reaction happens faster and releases more of its energy "
            "overall",
            "So the reactants do not settle out and stop reacting",
            "So the thermometer bulb does not touch the bottom of the cup",
        ],
        "correct_index": 0,
        "why": "Without stirring the liquid nearest the reaction is hotter "
               "than the rest, so the thermometer reads one part of the "
               "mixture rather than all of it.",
    },
    {
        "id": "ks4-exothermic-endothermic-s11",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two separate 50 g portions of the same solution are used. "
                "One reaction raises the temperature by 8.0 °C and another "
                "raises it by 2.0 °C. Compare the energy released by the two "
                "reactions.",
        "options": [
            "The first releases twice as much energy",
            "The first releases four times as much energy, because the mass "
            "and c are the same",
            "They release the same energy, because the mass of solution is "
            "the same",
            "The second releases four times as much, because a smaller rise "
            "means slower release",
        ],
        "correct_index": 1,
        "why": "Q = mcΔT, and with m and c identical the energy is "
               "proportional to ΔT, so 8.0 °C means four times the energy of "
               "2.0 °C.",
    },
    {
        "id": "ks4-exothermic-endothermic-s12",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants to compare the energy released when one "
                "gram of each of three fuels is burned. Describe the "
                "measurements that must be taken.",
        "options": [
            "The volume of each fuel and the time it burns for",
            "The temperature of each flame and the mass of the water that "
            "is heated",
            "The mass of fuel burned, the mass of water heated and the "
            "temperature rise of the water",
            "The mass of fuel burned and the time taken for it to burn",
        ],
        "correct_index": 2,
        "why": "Q = mcΔT gives the energy transferred to the water, and "
               "dividing by the mass of fuel burned turns it into energy per "
               "gram.",
    },
    {
        "id": "ks4-exothermic-endothermic-h05",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Burning 0.50 g of ethanol raises the temperature of 150 g "
                "of water by 12.0 °C. Using c = 4.18 J/g°C, calculate the "
                "energy released per gram of ethanol.",
        "options": [
            "3760 J/g",
            "1200 J/g",
            "15 000 J/g",
            "7520 J/g",
        ],
        "correct_index": 2,
        "why": "Q = 150 × 4.18 × 12.0 = 7520 J, and dividing by the 0.50 g "
               "burned gives about 15 000 J per gram.",
    },
    {
        "id": "ks4-exothermic-endothermic-h06",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two reactions release exactly the same amount of energy. "
                "In one the energy warms 100 g of solution and in the other "
                "it warms 250 g. Compare the temperature rises.",
        "options": [
            "The 250 g mixture rises further, because more solution can "
            "store more energy",
            "The 100 g mixture rises further, because the same energy is "
            "shared between less solution",
            "Both rise by the same amount, because the same energy was "
            "released",
            "The 250 g mixture rises further, because specific heat capacity "
            "increases with mass",
        ],
        "correct_index": 1,
        "why": "ΔT = Q ÷ (m × c), so with Q and c fixed a smaller mass gives "
               "a larger temperature rise.",
    },
    {
        "id": "ks4-exothermic-endothermic-h07",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sodium hydroxide solution is neutralised by an excess of "
                "hydrochloric acid. A student claims that using acid of "
                "double the concentration, at the same volume, must give a "
                "higher maximum temperature. Evaluate the claim.",
        "options": [
            "It is right, because more concentrated acid releases more "
            "energy per cubic centimetre",
            "It is right, because a higher concentration raises the specific "
            "heat capacity of the mixture",
            "It is wrong, because more concentrated acid makes the reaction "
            "endothermic",
            "It is wrong, because the alkali is limiting, so the same amount "
            "of reaction warms the same mass of solution",
        ],
        "correct_index": 3,
        "why": "The alkali decides how much reaction happens, so adding "
               "spare acid changes nothing about the energy released or the "
               "mass warmed.",
    },
    {
        "id": "ks4-exothermic-endothermic-h08",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction transfers 4180 J to a solution and the "
                "temperature rises by 8.0 °C. Using c = 4.18 J/g°C, "
                "determine the mass of the solution.",
        "options": [
            "125 g",
            "523 g",
            "1000 g",
            "140 000 g",
        ],
        "correct_index": 0,
        "why": "Rearranging Q = mcΔT gives m = 4180 ÷ (4.18 × 8.0) = 125 g.",
    },
    {
        "id": "ks4-exothermic-endothermic-h09",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One student adds 1.0 g of zinc powder to 50 cm3 of copper "
                "sulfate solution; another adds 1.0 g of zinc granules to "
                "the same volume and concentration. Both react completely "
                "and no energy is lost to the surroundings. Compare the "
                "maximum temperatures reached.",
        "options": [
            "The powder gives a higher maximum, because powder releases more "
            "energy per gram",
            "The granules give a higher maximum, because they react for "
            "longer",
            "Both reach the same maximum, because the same amount of "
            "reaction warms the same mass of solution",
            "The powder gives a higher maximum, because a larger surface "
            "area increases the energy released",
        ],
        "correct_index": 2,
        "why": "Surface area changes how FAST the energy comes out, not how "
               "MUCH: the same mass of zinc reacting completely releases the "
               "same energy either way.",
    },
    {
        "id": "ks4-exothermic-endothermic-h10",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student burns a candle under a copper can of water and "
                "gets an energy-per-gram value far below the accepted one. "
                "Moving the can from 10 cm above the flame to 2 cm above it "
                "raises the value. Explain the improvement.",
        "options": [
            "Less of the flame's energy is transferred to the surrounding "
            "air before reaching the can",
            "The candle wax burns hotter when the can is closer, so more "
            "energy is released",
            "The wax stores more energy per gram when it is closer to the "
            "can",
            "Copper conducts energy better over short distances",
        ],
        "correct_index": 0,
        "why": "The gap between flame and can is where the energy escapes to "
               "the air, so closing the gap means more of it reaches the "
               "water.",
    },
    {
        "id": "ks4-exothermic-endothermic-h11",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thermometer reads 1.0 °C too high at every temperature. "
                "Predict the effect on the temperature RISE measured for a "
                "neutralisation.",
        "options": [
            "The rise is measured 1.0 °C too high, because the thermometer "
            "over-reads",
            "The rise is measured 2.0 °C too high",
            "The rise is measured 1.0 °C too low",
            "No effect — the same error is in both readings and cancels in "
            "the subtraction",
        ],
        "correct_index": 3,
        "why": "A rise is a difference between two readings, and adding the "
               "same 1.0 °C to both leaves the difference unchanged.",
    },

    # ── reaction-profiles ──────────────────────── BASE (5.5.1.2) ── +11 ──
    {
        "id": "ks4-reaction-profiles-e05",
        "subtopic_slug": "reaction-profiles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the quantity plotted on the vertical axis of a "
                "reaction profile, and the unit it usually carries.",
        "options": [
            "Energy, usually in kJ/mol",
            "Time, in seconds",
            "Temperature, in °C",
            "Concentration, in mol/dm3",
        ],
        "correct_index": 0,
        "why": "A reaction profile plots the energy of the chemicals against "
               "how far the reaction has progressed.",
    },
    {
        "id": "ks4-reaction-profiles-e06",
        "subtopic_slug": "reaction-profiles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where the products of an EXOTHERMIC reaction are "
                "drawn on a reaction profile.",
        "options": [
            "At the same level as the reactants",
            "Below the reactant level",
            "Above the reactant level",
            "At the same level as the peak",
        ],
        "correct_index": 1,
        "why": "Exothermic means energy has left the chemicals, so the "
               "products end up storing less energy than the reactants did.",
    },
    {
        "id": "ks4-reaction-profiles-e07",
        "subtopic_slug": "reaction-profiles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the meaning of activation energy.",
        "options": [
            "The energy released when the products form",
            "The total energy stored in the reactants",
            "The average energy of all the particles in the mixture",
            "The minimum energy colliding particles must have for a reaction "
            "to happen",
        ],
        "correct_index": 3,
        "why": "Colliding particles with less than the activation energy "
               "simply bounce apart, so it is the minimum a successful "
               "collision needs.",
    },
    {
        "id": "ks4-reaction-profiles-e08",
        "subtopic_slug": "reaction-profiles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction profile shows the peak 90 kJ/mol above the "
                "reactants and the products 30 kJ/mol below the reactants. "
                "State the activation energy.",
        "options": [
            "30 kJ/mol",
            "60 kJ/mol",
            "90 kJ/mol",
            "120 kJ/mol",
        ],
        "correct_index": 2,
        "why": "Activation energy is measured from the reactant level up to "
               "the peak, so it is the 90 kJ/mol given, not anything "
               "involving the products.",
    },
    {
        "id": "ks4-reaction-profiles-s05",
        "subtopic_slug": "reaction-profiles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction profile shows the reactants at 180 kJ/mol, the "
                "peak at 295 kJ/mol and the products at 240 kJ/mol. "
                "Calculate ΔH and state the type of reaction.",
        "options": [
            "−60 kJ/mol, exothermic",
            "+115 kJ/mol, endothermic",
            "+55 kJ/mol, endothermic",
            "+60 kJ/mol, endothermic",
        ],
        "correct_index": 3,
        "why": "ΔH is products minus reactants, 240 − 180 = +60 kJ/mol, and a "
               "positive ΔH means energy has been taken in.",
    },
    {
        "id": "ks4-reaction-profiles-s06",
        "subtopic_slug": "reaction-profiles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why heating a mixture makes an endothermic reaction "
                "go faster.",
        "options": [
            "More colliding particles have at least the activation energy, "
            "so more collisions succeed",
            "Heating lowers the activation energy of the reaction",
            "Heating turns the reaction into an exothermic one",
            "Heating raises the product energy level, so less energy is "
            "needed overall",
        ],
        "correct_index": 0,
        "why": "Heating raises the energy of the particles, so a bigger "
               "fraction of collisions clears the same barrier — the barrier "
               "itself does not move.",
    },
    {
        "id": "ks4-reaction-profiles-s07",
        "subtopic_slug": "reaction-profiles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Reactions M and N have the same activation energy, but M is "
                "exothermic and N is endothermic. Compare their reaction "
                "profiles.",
        "options": [
            "M's peak is lower, because energy is released",
            "The peaks are the same height above the reactants; M's "
            "products lie below the reactants and N's above",
            "N has no peak, because energy is absorbed rather than released",
            "The peaks are the same height; M's products lie above the "
            "reactants and N's below them",
        ],
        "correct_index": 1,
        "why": "Equal activation energies mean equally high peaks above the "
               "reactants; the exothermic and endothermic difference shows "
               "only in where the products finish.",
    },
    {
        "id": "ks4-reaction-profiles-s08",
        "subtopic_slug": "reaction-profiles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction profile has its peak at 410 kJ/mol and an "
                "activation energy of 160 kJ/mol. Determine the energy level "
                "of the reactants.",
        "options": [
            "160 kJ/mol",
            "410 kJ/mol",
            "250 kJ/mol",
            "570 kJ/mol",
        ],
        "correct_index": 2,
        "why": "The peak sits one activation energy above the reactants, so "
               "the reactants are at 410 − 160 = 250 kJ/mol.",
    },
    {
        "id": "ks4-reaction-profiles-h05",
        "subtopic_slug": "reaction-profiles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student sketches an endothermic profile in which the peak "
                "is drawn LOWER than the product level. Identify why the "
                "sketch must be wrong.",
        "options": [
            "An endothermic reaction has no peak at all",
            "The product level must be drawn below the reactant level",
            "The peak must lie below the reactant level whenever a reaction "
            "is endothermic",
            "The peak must lie above both levels, because the barrier is "
            "climbed before the products form",
        ],
        "correct_index": 3,
        "why": "The curve has to rise over the activation energy barrier "
               "before it can settle at the product level, so the peak is "
               "always the highest point.",
    },
    {
        "id": "ks4-reaction-profiles-h06",
        "subtopic_slug": "reaction-profiles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Reactions R and S both have ΔH = −85 kJ/mol. R has an "
                "activation energy of 40 kJ/mol and S has one of 190 kJ/mol. "
                "Compare the energy released and the rate at room "
                "temperature.",
        "options": [
            "Both release 85 kJ/mol, but R is faster because more collisions "
            "clear its lower barrier",
            "R releases more energy and is faster, because its activation "
            "energy is lower",
            "S releases more energy, because its peak is higher",
            "Both release 85 kJ/mol and react at the same rate, because ΔH "
            "is the same",
        ],
        "correct_index": 0,
        "why": "ΔH fixes how much energy comes out; the activation energy "
               "fixes how many collisions are successful, and so how fast it "
               "comes out.",
    },
    {
        "id": "ks4-reaction-profiles-h07",
        "subtopic_slug": "reaction-profiles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction profile shows reactants at 95 kJ/mol and "
                "products at 260 kJ/mol, and the reverse reaction has an "
                "activation energy of 45 kJ/mol. Determine the activation "
                "energy of the forward reaction.",
        "options": [
            "120 kJ/mol",
            "165 kJ/mol",
            "210 kJ/mol",
            "350 kJ/mol",
        ],
        "correct_index": 2,
        "why": "The peak is 45 kJ/mol above the products, at 305 kJ/mol, and "
               "that is 305 − 95 = 210 kJ/mol above the reactants.",
    },

    # ── bond-energy-calculations ──────────────── HIGHER (5.5.1.3) ── +9 ──
    {
        "id": "ks4-bond-energy-calculations-e05",
        "subtopic_slug": "bond-energy-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State what happens to energy when a new chemical bond is "
                "formed.",
        "options": [
            "Energy must be supplied; bond forming is endothermic",
            "Energy is released; bond forming is exothermic",
            "There is no energy change when a bond forms",
            "Energy is released only when the bond formed is a double bond",
        ],
        "correct_index": 1,
        "why": "Atoms are attracted to one another, so energy is given out "
               "as they come together and a new bond forms.",
    },
    {
        "id": "ks4-bond-energy-calculations-e06",
        "subtopic_slug": "bond-energy-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the bonds that must be broken in 1 mol of methane, "
                "CH4.",
        "options": [
            "1 mol of C-H bonds",
            "2 mol of C-H bonds and 2 mol of C-C bonds",
            "3 mol of C-H bonds and 1 mol of C-C bonds",
            "4 mol of C-H bonds",
        ],
        "correct_index": 3,
        "why": "Methane is one carbon joined to four hydrogens, so there are "
               "four C-H bonds per molecule and no C-C bond at all.",
    },
    {
        "id": "ks4-bond-energy-calculations-e07",
        "subtopic_slug": "bond-energy-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "A reaction absorbs 890 kJ/mol breaking bonds and releases "
                "1240 kJ/mol forming bonds. State ΔH.",
        "options": [
            "−350 kJ/mol",
            "+350 kJ/mol",
            "+2130 kJ/mol",
            "−2130 kJ/mol",
        ],
        "correct_index": 0,
        "why": "ΔH is energy in minus energy out, 890 − 1240 = −350 kJ/mol, "
               "and the negative sign means exothermic.",
    },
    {
        "id": "ks4-bond-energy-calculations-s05",
        "subtopic_slug": "bond-energy-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate ΔH for CH4 + 2O2 → CO2 + 2H2O. Bond energies in "
                "kJ/mol: C-H 413, O=O 498, C=O 805, O-H 464.",
        "options": [
            "+818 kJ/mol",
            "−818 kJ/mol",
            "−1644 kJ/mol",
            "−6114 kJ/mol",
        ],
        "correct_index": 1,
        "why": "Breaking costs 4(413) + 2(498) = 2648 kJ and forming gives "
               "2(805) + 4(464) = 3466 kJ, so ΔH = 2648 − 3466 = −818 "
               "kJ/mol.",
    },
    {
        "id": "ks4-bond-energy-calculations-s06",
        "subtopic_slug": "bond-energy-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate ΔH for C2H4 + H2 → C2H6. Bond energies in kJ/mol: "
                "C=C 614, C-H 413, C-C 347, H-H 436.",
        "options": [
            "+123 kJ/mol",
            "−559 kJ/mol",
            "−123 kJ/mol",
            "−2825 kJ/mol",
        ],
        "correct_index": 2,
        "why": "Breaking costs 614 + 4(413) + 436 = 2702 kJ and forming "
               "gives 347 + 6(413) = 2825 kJ, so ΔH = 2702 − 2825 = −123 "
               "kJ/mol.",
    },
    {
        "id": "ks4-bond-energy-calculations-s07",
        "subtopic_slug": "bond-energy-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate ΔH for 2HI → H2 + I2. Bond energies in kJ/mol: "
                "H-I 299, H-H 436, I-I 151.",
        "options": [
            "−288 kJ/mol",
            "−11 kJ/mol",
            "+1185 kJ/mol",
            "+11 kJ/mol",
        ],
        "correct_index": 3,
        "why": "Breaking two H-I bonds costs 598 kJ and forming H-H and I-I "
               "gives 587 kJ, so ΔH = 598 − 587 = +11 kJ/mol, slightly "
               "endothermic.",
    },
    {
        "id": "ks4-bond-energy-calculations-h05",
        "subtopic_slug": "bond-energy-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate ΔH for C2H4 + Br2 → C2H4Br2. Bond energies in "
                "kJ/mol: C=C 614, C-H 413, Br-Br 193, C-C 347, C-Br 285.",
        "options": [
            "−110 kJ/mol",
            "+110 kJ/mol",
            "+175 kJ/mol",
            "−2569 kJ/mol",
        ],
        "correct_index": 0,
        "why": "Breaking costs 614 + 4(413) + 193 = 2459 kJ and forming "
               "gives 347 + 4(413) + 2(285) = 2569 kJ, so ΔH = −110 kJ/mol.",
    },
    {
        "id": "ks4-bond-energy-calculations-h06",
        "subtopic_slug": "bond-energy-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student calculating ΔH from bond energies forgets to "
                "break the bonds in one of the two reactants. State the "
                "effect on the calculated value.",
        "options": [
            "ΔH is unchanged, because bond breaking and bond making cancel "
            "out",
            "ΔH comes out too positive, because the energy taken in has been "
            "under-counted",
            "ΔH comes out too negative, because the energy taken in has been "
            "under-counted",
            "ΔH comes out too negative, because the energy given out has "
            "been over-counted",
        ],
        "correct_index": 2,
        "why": "Bonds broken are the positive term in ΔH = in − out, so "
               "leaving some out makes the total too small and pushes ΔH "
               "downwards.",
    },
    {
        "id": "ks4-bond-energy-calculations-h07",
        "subtopic_slug": "bond-energy-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "For a reaction, breaking the bonds in the reactants needs "
                "1850 kJ/mol and ΔH is +95 kJ/mol. Determine the energy "
                "released as the product bonds form.",
        "options": [
            "1945 kJ/mol, and more energy is given out than taken in",
            "1755 kJ/mol, and more energy is given out than taken in",
            "1945 kJ/mol, and more energy is taken in than given out",
            "1755 kJ/mol, and more energy is taken in than given out",
        ],
        "correct_index": 3,
        "why": "ΔH = in − out, so out = 1850 − 95 = 1755 kJ/mol; a positive "
               "ΔH means the breaking cost more than the making returned.",
    },
]
