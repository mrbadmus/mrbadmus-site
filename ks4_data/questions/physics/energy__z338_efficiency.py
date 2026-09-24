"""Physics · Energy — the MRB-338 expansion of `efficiency`.

One leaf only: AQA 8463 §4.1.3, efficiency as the fraction of the input that
comes out usefully. The original twelve rows in `energy.py` state the equation,
do four energy substitutions, one power substitution, one rearrangement for the
input, one two-device comparison and one useful-over-wasted correction. This
file takes the ground they leave: the power form as a statement rather than a
sum, the decimal-to-percentage conversion in both directions, what counts as
the useful output in a device where it is not obvious, the rearrangement for the
useful OUTPUT and for the WASTE, a Sankey diagram (drawn — MRB-352), the impossible
answer as a check on your own arithmetic, a two-stage chain worked in joules,
and the evaluations — whether an improvement is worth its price, and whether
heating is always waste.

The weight follows the CONTENT. `easier` stays at eight because recall here is
one equation in two forms, one unit rule, one ceiling and one conversion, and
asking those a ninth way would be the same question. The demand lives in
`standard`, where the ratio has to be run in whichever direction the question
leaves open, and in `harder`, where two devices or two stages compete and the
pupil has to say which figure decides it — so that is where the twenty-two-row
bands sit.

⚠️ Seam with `energy-transfers-in-a-system`: that leaf owns the METHODS —
lubrication, streamlining, insulation, thicker conductors — and where the waste
finishes. This leaf owns the NUMBER. A row here may price an improvement; it
may not explain why oil reduces friction.
⚠️ Seam with `power`: a power ratio is an efficiency and belongs here. Getting
a power from an energy and a time does not, and appears nowhere in this file.
⚠️ Heat pumps are deliberately absent. A heat pump moves energy rather than
transferring it from a store, so its performance figure legitimately exceeds 1
and it is the wrong example for the never-above-100% rule.
"""

TOPIC = "energy"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The power form, the unit rule, the ceiling as a check, the conversion,
    # and what the useful output actually is in two devices.
    {
        "id": "ks4-efficiency-e05",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the equation for efficiency when powers are given "
                "instead of energies.",
        "options": [
            "efficiency = total power input divided by useful power output",
            "efficiency = useful power output divided by wasted power",
            "efficiency = wasted power divided by useful power output",
            "efficiency = useful power output divided by total power input",
        ],
        "correct_index": 3,
        "why": "Efficiency is the same fraction whether it is worked out from "
               "energies or from powers, so the total input is always the "
               "denominator.",
    },
    {
        "id": "ks4-efficiency-e06",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lamp is supplied with 45 J and gives out 9 J of light. "
                "Calculate its efficiency as a decimal.",
        "options": [
            "5.0",
            "0.20",
            "0.80",
            "36",
        ],
        "correct_index": 1,
        "why": "The useful output divided by the total input is 9 divided by "
               "45, which is 0.20.",
    },
    {
        "id": "ks4-efficiency-e07",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which energy transfer counts as the useful output when "
                "the efficiency of a kettle is worked out.",
        "options": [
            "The energy transferred to the thermal store of the water",
            "The energy transferred from the mains to the heating element",
            "The energy transferred to the thermal store of the kitchen air",
            "The energy transferred to the plastic body of the kettle itself",
        ],
        "correct_index": 0,
        "why": "A kettle is bought to heat water, so only the energy reaching "
               "the water's thermal store is the useful output.",
    },
    {
        "id": "ks4-efficiency-e08",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why an electric room heater is close to 100% "
                "efficient.",
        "options": [
            "Because it is the cheapest appliance in the house to run for an "
            "hour",
            "Because a heater takes in more energy than any other appliance "
            "does",
            "Because the warming it produces is what the heater is wanted "
            "for",
            "Because a heater has no moving parts to rub against each other",
        ],
        "correct_index": 2,
        "why": "Almost everything supplied finishes in the thermal store of "
               "the room, and warming the room is exactly the useful output "
               "wanted.",
    },
    {
        "id": "ks4-efficiency-e09",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A device has an efficiency of 0.25. State this efficiency as "
                "a percentage.",
        "options": [
            "0.25%",
            "2.5%",
            "25%",
            "250%",
        ],
        "correct_index": 2,
        "why": "A decimal efficiency is multiplied by 100 to give a "
               "percentage, so 0.25 becomes 25%.",
    },
    {
        "id": "ks4-efficiency-e10",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of these values cannot be the efficiency of a "
                "device.",
        "options": [
            "0.02",
            "0.35",
            "1.4",
            "0.98",
        ],
        "correct_index": 2,
        "why": "A device cannot transfer more usefully than it is supplied "
               "with, so a decimal efficiency above 1 is impossible.",
    },
    {
        "id": "ks4-efficiency-e11",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit of efficiency.",
        "options": [
            "The joule",
            "The watt",
            "The joule per second",
            "It has no unit",
        ],
        "correct_index": 3,
        "why": "Efficiency is one energy divided by another, so the units "
               "cancel and the answer is a plain number.",
    },
    {
        "id": "ks4-efficiency-e12",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A machine is supplied with 20 kJ and transfers 13 kJ "
                "usefully. Calculate its efficiency as a percentage.",
        "options": [
            "65%",
            "35%",
            "154%",
            "1.54%",
        ],
        "correct_index": 0,
        "why": "13 divided by 20 is 0.65, and 0.65 multiplied by 100 gives "
               "65%.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # The ratio run in every direction it can be run, plus the reasoning
    # about what the numerator and the denominator mean.
    {
        "id": "ks4-efficiency-s05",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A microwave oven is supplied with 1200 J and 840 J reaches "
                "the food. Calculate its efficiency as a percentage.",
        "options": [
            "143%",
            "70%",
            "30%",
            "0.70%",
        ],
        "correct_index": 1,
        "why": "840 divided by 1200 is 0.70, which is 70% once multiplied by "
               "100.",
    },
    {
        "id": "ks4-efficiency-s06",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A motor draws 240 W and delivers 180 W usefully. Calculate "
                "its efficiency as a decimal.",
        "options": [
            "1.33",
            "0.25",
            "0.75",
            "60",
        ],
        "correct_index": 2,
        "why": "The power form works exactly like the energy form: 180 "
               "divided by 240 is 0.75.",
    },
    {
        "id": "ks4-efficiency-s07",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A device with an efficiency of 0.25 is supplied with 800 J. "
                "Calculate the useful energy it transfers.",
        "options": [
            "3200 J",
            "600 J",
            "200 J",
            "775 J",
        ],
        "correct_index": 2,
        "why": "The useful output is the efficiency multiplied by the input, "
               "so 0.25 multiplied by 800 gives 200 J.",
    },
    {
        "id": "ks4-efficiency-s08",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A machine is 40% efficient and transfers 520 J usefully. "
                "Calculate the energy supplied to it.",
        "options": [
            "1300 J",
            "208 J",
            "560 J",
            "2600 J",
        ],
        "correct_index": 0,
        "why": "Rearranging gives input = useful divided by efficiency, so "
               "520 divided by 0.40 is 1300 J.",
    },
    {
        "id": "ks4-efficiency-s09",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A kettle with an efficiency of 0.90 is supplied with 360 kJ. "
                "Calculate the energy wasted.",
        "options": [
            "324 kJ",
            "400 kJ",
            "90 kJ",
            "36 kJ",
        ],
        "correct_index": 3,
        "why": "The useful share is 0.90, so the wasted share is 0.10, and "
               "0.10 multiplied by 360 gives 36 kJ.",
    },
    {
        "id": "ks4-efficiency-s10",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the useful output of a loudspeaker, and hence what "
                "is wasted when one is used.",
        "options": [
            "The warmth of the coil is useful and the sound it makes is the "
            "waste",
            "The current flowing through the coil is useful and the sound "
            "produced is the waste",
            "Both the sound and the warmth are useful, so a loudspeaker "
            "wastes nothing",
            "The sound it produces is useful and the warming of its coil is "
            "the waste",
        ],
        "correct_index": 3,
        "why": "A loudspeaker is bought to make sound, so the energy that "
               "warms its coil instead is the wasted share.",
    },
    {
        "id": "ks4-efficiency-s11",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an LED lamp has a higher efficiency than a "
                "filament lamp of the same brightness.",
        "options": [
            "It draws a larger current, so a greater share of its energy "
            "arrives as light in the room",
            "It gives out light of a brighter colour, and a brighter colour "
            "counts for more in the sum",
            "It needs a smaller supply for the same light, so less is "
            "dissipated by heating",
            "It lasts a great many more hours, so the energy is shared over a "
            "longer life",
        ],
        "correct_index": 2,
        "why": "Efficiency compares the light out with the energy in, and an "
               "LED reaches the same brightness from a much smaller supply.",
    },
    {
        "id": "ks4-efficiency-s12",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "figure": "ks4-fig-sankey-100-65-useful-unlabelled",
        "text": "The Sankey diagram shows the energy transfers for a device. Determine the efficiency of the device.",
        "options": [
            "65%",
            "35%",
            "135%",
            "286%",
        ],
        "correct_index": 1,
        "why": "Energy is conserved, so the useful output is 100 J − 65 J = 35 J. Efficiency = 35 ÷ 100 = 0.35, which is 35%. 65% is the wasted share, not the useful one.",
    },
    {
        "id": "ks4-efficiency-s13",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil calculates the efficiency of a drill as 1.25. "
                "Explain how the pupil can tell the answer is wrong without "
                "being told the numbers.",
        "options": [
            "An efficiency written as a decimal has to be a whole number "
            "rather than a fraction",
            "An efficiency can never exceed 1, because that would mean more "
            "came out than went in",
            "An efficiency has to be written as a percentage, so an answer given "
            "as a decimal is always wrong",
            "An efficiency below 2 is too small for a power tool of that "
            "kind to reach",
        ],
        "correct_index": 1,
        "why": "The useful output is part of the input, so the ratio cannot "
               "exceed 1 and a value above it means the division was the "
               "wrong way round.",
    },
    {
        "id": "ks4-efficiency-s14",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the efficiency of a petrol engine is well below "
                "1.",
        "options": [
            "Much of the fuel's energy is dissipated by heating the engine, "
            "the exhaust gases and the air",
            "Petrol holds little energy in its chemical store compared with what "
            "a car needs",
            "An engine takes in less energy than it delivers, so the ratio "
            "has to come out small",
            "Some of the fuel passes straight through the engine without "
            "being burned inside it",
        ],
        "correct_index": 0,
        "why": "Only a small share of each litre ends up moving the car; the "
               "rest warms the engine, the exhaust and the surrounding air.",
    },
    {
        "id": "ks4-efficiency-s15",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Device P is supplied with 50 J and delivers 20 J usefully. "
                "Device Q is supplied with 80 J and delivers 24 J usefully. "
                "Determine which is more efficient.",
        "options": [
            "Q, because it delivers 24 J against P's 20 J",
            "Q, because it is supplied with more energy in total",
            "P, because 20 out of 50 beats 24 out of 80",
            "Neither, because both of them waste some energy by heating",
        ],
        "correct_index": 2,
        "why": "P is 20 divided by 50, which is 0.40, and Q is 24 divided by "
               "80, which is 0.30, so P uses its supply better.",
    },
    {
        "id": "ks4-efficiency-s16",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fan is left running for twice as long as before. Explain "
                "why its efficiency is unchanged.",
        "options": [
            "Because the useful output and the total input both double, so "
            "the ratio between them is the same",
            "Because efficiency is fixed when a device leaves the factory and "
            "no use can alter it",
            "Because the extra time is spent at a steady speed, when a fan "
            "wastes none of its supply",
            "Because efficiency describes the length of time a device is left "
            "running rather than a share of the energy supplied",
        ],
        "correct_index": 0,
        "why": "Efficiency is a ratio, so multiplying both the useful output "
               "and the input by the same number leaves it where it was.",
    },
    {
        "id": "ks4-efficiency-s17",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hairdryer draws 2000 W and delivers 1700 W as warm moving "
                "air. Calculate its efficiency as a decimal.",
        "options": [
            "1.18",
            "0.85",
            "0.15",
            "300",
        ],
        "correct_index": 1,
        "why": "1700 divided by 2000 is 0.85, and warm moving air is exactly "
               "what a hairdryer is bought to deliver.",
    },
    {
        "id": "ks4-efficiency-s18",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what the width of each arrow in a Sankey diagram "
                "represents.",
        "options": [
            "The amount of energy that arrow carries, so a wider arrow means "
            "more energy",
            "The temperature reached by the part of the device that the arrow "
            "points towards",
            "The length of time for which the energy that arrow carries goes on "
            "being transferred",
            "The distance the energy that arrow carries travels away from the "
            "device",
        ],
        "correct_index": 0,
        "why": "Arrow width is drawn in proportion to the number of joules, "
               "which is what lets a Sankey diagram be read as a "
               "calculation.",
    },
    {
        "id": "ks4-efficiency-s19",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solar cell receives 500 W of sunlight and generates 90 W "
                "of electrical power. Calculate its efficiency as a "
                "percentage.",
        "options": [
            "556%",
            "82%",
            "18%",
            "410%",
        ],
        "correct_index": 2,
        "why": "90 divided by 500 is 0.18, which is 18% once multiplied by "
               "100.",
    },
    {
        "id": "ks4-efficiency-s20",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the gain in the gravitational potential store of "
                "a load is used as the useful output when a crane's "
                "efficiency is worked out.",
        "options": [
            "Because raising the load is the job the crane is there to do",
            "Because a gravitational potential store is the largest store any "
            "crane ever fills",
            "Because the gravitational potential store is the only store that "
            "can be measured on site",
            "Because a crane fills no other store while it is lifting a load "
            "off the ground",
        ],
        "correct_index": 0,
        "why": "The useful output is whatever the device is wanted for, and a "
               "crane is wanted for lifting.",
    },
    {
        "id": "ks4-efficiency-s21",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas boiler releases 40 MJ from its fuel and transfers "
                "34 MJ to the water. Calculate its efficiency as a "
                "percentage.",
        "options": [
            "118%",
            "6%",
            "85%",
            "15%",
        ],
        "correct_index": 2,
        "why": "34 divided by 40 is 0.85, which is 85% once multiplied by "
               "100.",
    },
    {
        "id": "ks4-efficiency-s22",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an efficiency worked out from joules and one "
                "worked out from watts give the same answer for one device.",
        "options": [
            "Because a joule and a watt are two different names for the same "
            "quantity",
            "Because the time taken cancels only when the device is left "
            "running for a whole hour",
            "Because watts are converted into joules before the division is "
            "carried out",
            "Because both are the useful share of the same transfer, over the "
            "same length of time",
        ],
        "correct_index": 3,
        "why": "Dividing both the useful energy and the total energy by the "
               "same time gives the two powers, and a ratio is unchanged when "
               "both parts are divided alike.",
    },
    {
        "id": "ks4-efficiency-s23",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pump with an efficiency of 0.45 receives 20 kJ. Determine "
                "the energy it gives to the water.",
        "options": [
            "44 kJ",
            "11 kJ",
            "9 kJ",
            "20.45 kJ",
        ],
        "correct_index": 2,
        "why": "The useful output is the efficiency multiplied by the input, "
               "so 0.45 multiplied by 20 gives 9 kJ.",
    },
    {
        "id": "ks4-efficiency-s24",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil divides the wasted energy by the total input and "
                "calls the answer the efficiency. Describe what the pupil has "
                "actually worked out.",
        "options": [
            "The share of the supply that is wasted, which is what is left "
            "once the efficiency is taken from 1",
            "The efficiency, because the wasted energy and the useful output of "
            "any device come to exactly the same amount",
            "Nothing that has any meaning, because the waste cannot be "
            "divided by the input at all",
            "The efficiency of the surroundings the device has been "
            "dissipating its energy into",
        ],
        "correct_index": 0,
        "why": "Useful and wasted together make the input, so the wasted "
               "share and the efficiency add to 1.",
    },
    {
        "id": "ks4-efficiency-s25",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A machine is altered so that it needs a larger supply while "
                "its useful output stays the same. Predict the effect on its "
                "efficiency.",
        "options": [
            "It rises, because the machine now handles more energy altogether",
            "It falls, because the same useful output is now a smaller share "
            "of the input",
            "It is unchanged, because the useful output has not been altered",
            "It rises, because the waste is spread across a larger supply",
        ],
        "correct_index": 1,
        "why": "The numerator is fixed and the denominator has grown, so the "
               "fraction is smaller and more of the supply is being wasted.",
    },
    {
        "id": "ks4-efficiency-s26",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A heater with an efficiency of 0.95 draws 1500 W. Calculate "
                "the power it wastes.",
        "options": [
            "1425 W",
            "1579 W",
            "95 W",
            "75 W",
        ],
        "correct_index": 3,
        "why": "The wasted share is 1 minus 0.95, which is 0.05, and 0.05 "
               "multiplied by 1500 gives 75 W.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Two devices or two stages, the rearrangement run twice, and the
    # evaluations — is the improvement worth its price, and is heating waste.
    {
        "id": "ks4-efficiency-h05",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Boiler A releases 30 MJ and transfers 25.5 MJ to the water. "
                "Boiler B releases 45 MJ and transfers 36 MJ. Determine which "
                "is more efficient.",
        "options": [
            "B, because it transfers 36 MJ against A's 25.5 MJ",
            "A, because 25.5 out of 30 is a larger share than 36 out of 45",
            "B, because 9 MJ wasted out of 45 MJ is a smaller share than "
            "4.5 MJ out of 30 MJ",
            "Neither, because both boilers burn gas and so must match",
        ],
        "correct_index": 1,
        "why": "A is 25.5 divided by 30, which is 0.85, and B is 36 divided "
               "by 45, which is 0.80, so A makes better use of its fuel.",
    },
    {
        "id": "ks4-efficiency-h06",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station releases 1000 MJ from fuel and generates "
                "400 MJ of electrical energy. The cables then deliver 360 MJ "
                "of that to homes. Determine the efficiency from fuel to "
                "home.",
        "options": [
            "40%",
            "90%",
            "36%",
            "76%",
        ],
        "correct_index": 2,
        "why": "The useful output at the end of the chain is 360 MJ out of "
               "the 1000 MJ released, and 360 divided by 1000 is 0.36.",
    },
    {
        "id": "ks4-efficiency-h07",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A family is offered a boiler that would raise their heating "
                "efficiency from 0.80 to 0.90 for 3000 pounds, and they spend "
                "600 pounds a year on gas. Evaluate the offer.",
        "options": [
            "Worth it at once, because the gas bill would fall to nothing "
            "after the boiler is fitted",
            "Worth it at once, because a boiler above 0.85 efficient wastes "
            "no energy on heating",
            "Doubtful, because the saving is a small share of the bill and "
            "would take many years to repay",
            "Doubtful, because a boiler of higher efficiency releases less "
            "energy from the same gas",
        ],
        "correct_index": 2,
        "why": "Going from 0.80 to 0.90 saves roughly one ninth of the gas "
               "used, so on a 600 pound bill the yearly saving is well under "
               "100 pounds against a 3000 pound price.",
    },
    {
        "id": "ks4-efficiency-h08",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A device with an efficiency of 0.40 must deliver 1.4 kJ of "
                "useful energy. Calculate the energy that must be supplied, "
                "in joules.",
        "options": [
            "560 J",
            "2333 J",
            "35 J",
            "3500 J",
        ],
        "correct_index": 3,
        "why": "The input is the useful output divided by the efficiency, so "
               "1400 divided by 0.40 gives 3500 J.",
    },
    {
        "id": "ks4-efficiency-h09",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a device described as efficient "
                "wastes no energy.",
        "options": [
            "The claim holds, because an efficient device transfers all of "
            "its supply usefully",
            "The claim fails, because efficient means a large share is "
            "useful, not that none is wasted",
            "The claim holds, because the energy an efficient device wastes is "
            "returned later",
            "The claim fails, because an efficient device wastes more than an "
            "inefficient one",
        ],
        "correct_index": 1,
        "why": "Every real device dissipates something, so even a high "
               "efficiency leaves a wasted share below 1.",
    },
    {
        "id": "ks4-efficiency-h10",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A machine is supplied with 8000 J and transfers 5000 J "
                "usefully. A pupil divides 8000 by 5000 and writes 1.6. "
                "Identify the error and give the correct efficiency.",
        "options": [
            "The division was inverted; the efficiency is 0.625",
            "The wasted energy was left out; the efficiency is 1.6",
            "The units were left out; the efficiency is 1.6 joules",
            "The division was inverted; the efficiency is 0.375",
        ],
        "correct_index": 0,
        "why": "The useful output goes on top, so the efficiency is 5000 "
               "divided by 8000, which is 0.625 and below 1 as it must be.",
    },
    {
        "id": "ks4-efficiency-h11",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric motor is 0.85 efficient and a petrol engine is "
                "0.30 efficient. Each is supplied with 100 MJ. Determine the "
                "useful energy each delivers.",
        "options": [
            "85 MJ from the motor and 30 MJ from the engine",
            "15 MJ from the motor and 70 MJ from the engine",
            "118 MJ from the motor and 333 MJ from the engine",
            "85 MJ from the motor and 70 MJ from the engine",
        ],
        "correct_index": 0,
        "why": "The useful output is the efficiency multiplied by the input, "
               "so 0.85 of 100 MJ is 85 MJ and 0.30 of 100 MJ is 30 MJ.",
    },
    {
        "id": "ks4-efficiency-h12",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a hydroelectric scheme the falling water's gravitational "
                "potential store drops by 2000 kJ and the generator produces "
                "1600 kJ of electrical energy. Determine the efficiency.",
        "options": [
            "125%",
            "20%",
            "400%",
            "80%",
        ],
        "correct_index": 3,
        "why": "1600 divided by 2000 is 0.80, so 80% of the store emptied by "
               "the falling water reaches the grid.",
    },
    {
        "id": "ks4-efficiency-h13",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A machine has an efficiency of 0.70 and wastes 210 J on one "
                "run. Determine the energy supplied to it.",
        "options": [
            "300 J",
            "147 J",
            "700 J",
            "490 J",
        ],
        "correct_index": 2,
        "why": "The wasted share is 1 minus 0.70, which is 0.30, so the input "
               "is 210 divided by 0.30, giving 700 J.",
    },
    {
        "id": "ks4-efficiency-h14",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A workshop lamp is 0.05 efficient and its motor-driven fan "
                "is 0.60 efficient. Determine which offers the larger "
                "possible saving if it is replaced.",
        "options": [
            "The fan, because a device above 0.50 efficient is the easier one "
            "to improve",
            "The lamp, because 95% of its supply is already being wasted",
            "The fan, because it is supplied with more energy than the lamp in "
            "every workshop it is used in",
            "The lamp, because a low efficiency means it is supplied with "
            "very little energy",
        ],
        "correct_index": 1,
        "why": "The lamp wastes 0.95 of everything it is given against the "
               "fan's 0.40, so there is far more to recover by replacing it.",
    },
    {
        "id": "ks4-efficiency-h15",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A motor is 0.60 efficient with a heavy load and 0.75 "
                "efficient with a light one. Determine which load wastes more "
                "energy for each joule supplied.",
        "options": [
            "The heavy load, because 0.40 of each joule is wasted rather than "
            "0.25",
            "The light load, because a smaller load leaves the motor less useful "
            "work to do with its supply",
            "Both waste the same, because the motor itself has not been "
            "altered between the two",
            "The heavy load, because a heavy load makes the motor draw a "
            "smaller current",
        ],
        "correct_index": 0,
        "why": "The wasted share is 1 minus the efficiency, so 0.40 of each "
               "joule is wasted under the heavy load against 0.25 under the "
               "light one.",
    },
    {
        "id": "ks4-efficiency-h16",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A machine needed 1200 J to deliver 800 J usefully. After a "
                "service it needs only 1000 J for the same 800 J. Determine "
                "its new efficiency.",
        "options": [
            "1.25",
            "0.67",
            "0.20",
            "0.80",
        ],
        "correct_index": 3,
        "why": "800 divided by 1000 is 0.80, up from 800 divided by 1200, "
               "which was 0.67.",
    },
    {
        "id": "ks4-efficiency-h17",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that the more powerful of two drills must "
                "be the more efficient one.",
        "options": [
            "It must be, because a larger power rating means a larger useful "
            "output every second",
            "It need not be, because power is how fast energy is supplied and "
            "efficiency is the share used well",
            "It must be, because a powerful drill finishes the job in far less "
            "time and so has less time in which to waste energy",
            "It need not be, because a powerful drill is supplied with less "
            "energy than a weak one",
        ],
        "correct_index": 1,
        "why": "A 1000 W drill delivering 400 W usefully is less efficient "
               "than a 500 W drill delivering 350 W, however much more "
               "powerful it is.",
    },
    {
        "id": "ks4-efficiency-h18",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A generator is supplied with 1000 J and delivers 900 J to a "
                "motor, which then transfers 720 J usefully. Determine the "
                "efficiency of the two working together.",
        "options": [
            "0.90",
            "0.72",
            "0.80",
            "1.70",
        ],
        "correct_index": 1,
        "why": "The useful output at the far end is 720 J and the energy "
               "supplied at the near end is 1000 J, so the efficiency is 720 "
               "divided by 1000.",
    },
    {
        "id": "ks4-efficiency-h19",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Boiling the same water takes 300 kJ in a kettle, of which "
                "255 kJ reaches the water, or 480 kJ on a hob, of which "
                "264 kJ reaches it. Determine which is more efficient.",
        "options": [
            "The hob, because 264 kJ reaches the water against 255 kJ",
            "The hob, because it is supplied with more energy for the same "
            "job",
            "The kettle, because 255 out of 300 is a far larger share than "
            "264 out of 480",
            "Neither, because the water finishes at the same temperature",
        ],
        "correct_index": 2,
        "why": "The kettle is 255 divided by 300, which is 0.85, and the hob "
               "is 264 divided by 480, which is 0.55.",
    },
    {
        "id": "ks4-efficiency-h20",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A motor is advertised as being 110% efficient. Evaluate this "
                "claim.",
        "options": [
            "It is possible for a motor, because its spinning parts add energy "
            "of their own to the supply it is given",
            "It is impossible, because energy is never created, so the output "
            "cannot exceed the supply",
            "It is possible if the motor is supplied with more energy than it "
            "needs to turn",
            "It is impossible, because no motor can be more than 50% "
            "efficient in practice",
        ],
        "correct_index": 1,
        "why": "Energy cannot be created, so the useful output can at most "
               "equal the input and an efficiency above 100% cannot happen.",
    },
    {
        "id": "ks4-efficiency-h21",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A winch with an efficiency of 0.95 delivers 2850 J to a "
                "load. Determine the energy supplied and the energy wasted.",
        "options": [
            "3000 J supplied, with 150 J wasted",
            "2708 J supplied, with 142 J wasted",
            "3000 J supplied, with 2850 J wasted",
            "2850 J supplied, with 143 J wasted",
        ],
        "correct_index": 0,
        "why": "The input is 2850 divided by 0.95, which is 3000 J, and the "
               "waste is 3000 minus 2850, which is 150 J.",
    },
    {
        "id": "ks4-efficiency-h22",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that raising the efficiency of a machine "
                "always saves its owner money.",
        "options": [
            "It always does, because a machine of higher efficiency is the "
            "cheaper one to buy in the first place",
            "It always does, because the energy a machine wastes costs more "
            "than any repair could",
            "Not always, because the change itself has a price that may "
            "exceed what the saving comes to",
            "Not always, because a machine of higher efficiency has to be "
            "supplied with more energy each hour",
        ],
        "correct_index": 2,
        "why": "The saving is worth having only if it repays the cost of the "
               "change within the working life of the machine.",
    },
    {
        "id": "ks4-efficiency-h23",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lamp X draws 60 W for 3 W of light, lamp Y draws 12 W for "
                "3.6 W, and lamp Z draws 20 W for 1 W. Determine which is "
                "most efficient.",
        "options": [
            "X, because a lamp drawing 60 W turns a larger share of its "
            "supply into light",
            "Z, because it draws less power than X does for its light output",
            "Y, because 3.6 out of 12 beats 3 out of 60 and 1 out of 20",
            "All three match, because each of them is a lamp giving out light",
        ],
        "correct_index": 2,
        "why": "The three efficiencies are 0.05, 0.30 and 0.05, so Y turns "
               "much the largest share of its supply into light.",
    },
    {
        "id": "ks4-efficiency-h24",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The bearings of a machine wear out over several years while "
                "the useful work it does stays the same. Predict what happens "
                "to its efficiency, and explain.",
        "options": [
            "It rises, because a worn machine needs a smaller supply to do "
            "the same work",
            "It is unchanged, because the useful work done has not altered",
            "It falls, because a worn machine delivers less useful work than "
            "it was built to",
            "It falls, because a larger supply is now needed for the same "
            "useful output",
        ],
        "correct_index": 3,
        "why": "Worn bearings dissipate more, so the same useful output is "
               "now a smaller share of a larger input.",
    },
    {
        "id": "ks4-efficiency-h25",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lamp is supplied with 400 J and gives out 120 J of light, "
                "240 J by heating and 40 J as sound. Determine its efficiency "
                "and its largest waste.",
        "options": [
            "30% efficient, with heating the largest waste",
            "70% efficient, with heating the largest waste",
            "30% efficient, with sound the largest waste",
            "90% efficient, with the light the largest waste",
        ],
        "correct_index": 0,
        "why": "Light is the useful output, so the efficiency is 120 divided "
               "by 400, and the 240 J that warms the surroundings is the "
               "largest wasted share.",
    },
    {
        "id": "ks4-efficiency-h26",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that any device which warms its "
                "surroundings must have a low efficiency.",
        "options": [
            "The claim holds, because warming the surroundings is a wasted "
            "transfer in every device there is",
            "The claim holds, because a warm device has already dissipated "
            "most of what it was given",
            "The claim fails, because the warmth a device produces returns to "
            "it as it cools again",
            "The claim fails, because warming the surroundings is the useful "
            "output of a room heater",
        ],
        "correct_index": 3,
        "why": "Whether an output is useful depends on the job, and for a "
               "heater the warming of the room is precisely what is wanted.",
    },
]
