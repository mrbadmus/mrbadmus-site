"""Physics · Energy — the MRB-338 expansion of `power`.

One leaf only: AQA 8463 §4.1.1, power as the rate of energy transfer, P = E / t
and P = W / t in every direction, and the watt as one joule per second. The
original twelve rows in `energy.py` already own the definition of power, the
watt, one substitution each way, two crane/lift climbs, the minutes trap named
once, t = E / P into minutes, and one two-heater comparison. This file takes
what they leave: the reading of a power RATING, kW and MW as multiples, the
hour conversion, t and m as the unknown, work found from a force and a
distance, several people rather than appliances, and the qualitative set — a
rating is not an energy, two identically-rated devices need not transfer the
same, and "more powerful" means more joules each second and nothing else.

The weight follows the CONTENT, not the arithmetic. `easier` stays at eight
because recall here is one definition, one unit, one multiple and three
one-step substitutions, and a seventh way of asking "what is E / t" would be
the same question wearing a different appliance. The demand in this subtopic
lives in the conversions and in the rearrangements — minutes and hours into
seconds, kW and MW into W, and an energy that has to be found from a force or
from m g h before the division can even start — so `standard` and `harder`
carry twenty-two rows each.

Efficiency appears nowhere: a wasted amount would be quoted in joules, never
as a ratio or a percentage, because "useful power output over total power
input" belongs to `efficiency`. m g h and F d are used only as the step that
produces the energy; every stem asks for the power.
"""

TOPIC = "energy"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # Reading a rating, the kilowatt, why seconds, what "more powerful"
    # means, and one clean substitution for each of P, E and t.
    {
        "id": "ks4-power-e05",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A microwave oven is labelled 1300 W. State what this tells "
                "you about the energy it transfers.",
        "options": [
            "It transfers 1300 J of energy every second that it is running",
            "It transfers 1300 J of energy in total, and must then be "
            "switched off to be refilled",
            "It holds 1300 J of energy in store inside itself while it is "
            "plugged in",
            "It needs 1300 seconds of running to transfer just one "
            "joule",
        ],
        "correct_index": 0,
        "why": "A watt is one joule per second, so a rating of 1300 W means "
               "1300 J is transferred every second the oven runs.",
    },
    {
        "id": "ks4-power-e06",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The heating element of a toaster transfers 6300 J in 15 s. "
                "Determine the power of the toaster.",
        "options": [
            "94 500 W",
            "0.0024 W",
            "6300 W",
            "420 W",
        ],
        "correct_index": 3,
        "why": "P = E / t = 6300 / 15 = 420 W, which is 420 joules "
               "transferred every second.",
    },
    {
        "id": "ks4-power-e07",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An LED floodlight has a power of 35 W. Determine the energy "
                "it transfers in 60 s.",
        "options": [
            "0.58 J",
            "2100 J",
            "1.7 J",
            "126 000 J",
        ],
        "correct_index": 1,
        "why": "E = P x t = 35 x 60 = 2100 J.",
    },
    {
        "id": "ks4-power-e08",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric drill rated at 500 W transfers 7000 J while a "
                "hole is drilled. Determine how long the drilling took.",
        "options": [
            "0.071 s",
            "3 500 000 s",
            "14 s",
            "140 s",
        ],
        "correct_index": 2,
        "why": "t = E / P = 7000 / 500 = 14 s.",
    },
    {
        "id": "ks4-power-e09",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An immersion heater is rated at 3.0 kW. State its power in "
                "watts.",
        "options": [
            "3000 W",
            "300 W",
            "30 W",
            "3 000 000 W",
        ],
        "correct_index": 0,
        "why": "One kilowatt is 1000 watts, so 3.0 kW is 3.0 x 1000 = "
               "3000 W.",
    },
    {
        "id": "ks4-power-e10",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the quantity whose unit is the watt.",
        "options": [
            "The total energy that the device transfers",
            "The time the device runs for",
            "The work the device does",
            "The power of the device",
        ],
        "correct_index": 3,
        "why": "The watt is the unit of power; energy transferred and work "
               "done are both measured in joules.",
    },
    {
        "id": "ks4-power-e11",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a time given in minutes must be changed into "
                "seconds before power is calculated.",
        "options": [
            "Because the equation stops working altogether whenever the time "
            "given is longer than a single minute",
            "Because a watt means one joule each second, so only a time in "
            "seconds will do",
            "Because energy in joules can be measured over a whole minute "
            "but not over part of one",
            "Because the power of a device falls steadily as the time in the "
            "calculation grows",
        ],
        "correct_index": 1,
        "why": "Power in watts is joules per second, so the t in P = E / t "
               "has to be a number of seconds.",
    },
    {
        "id": "ks4-power-e12",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two motors do the same amount of work, but motor A finishes "
                "sooner than motor B. State which motor is more powerful.",
        "options": [
            "Motor B, because it runs for longer and so transfers more "
            "energy altogether",
            "Neither of them, because two motors doing equal work must have "
            "equal power",
            "Motor A, because it does that work in less time, and power is "
            "always the work done divided by the time taken",
            "Motor B, because a motor that works slowly must be pulling with "
            "a larger force",
        ],
        "correct_index": 2,
        "why": "Power is work done divided by time, so for the same work the "
               "shorter time gives the larger power.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Familiar devices and people, two steps, a conversion each time: minutes
    # and hours into seconds, kW and MW into W, answers in J, kJ, MJ and kW.
    {
        "id": "ks4-power-s05",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A kettle has a power rating of 2200 W and boils water for "
                "4.0 minutes. Determine the energy transferred.",
        "options": [
            "528 000 J",
            "8800 J",
            "9.2 J",
            "31 680 000 J",
        ],
        "correct_index": 0,
        "why": "4.0 minutes is 240 s, so E = P x t = 2200 x 240 = "
               "528 000 J.",
    },
    {
        "id": "ks4-power-s06",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric shower transfers 1 440 000 J of energy during a "
                "4.0 minute shower. Calculate the power of the shower.",
        "options": [
            "360 000 W",
            "6000 W",
            "100 W",
            "1 440 000 W",
        ],
        "correct_index": 1,
        "why": "4.0 minutes is 240 s, so P = E / t = 1 440 000 / 240 = "
               "6000 W.",
    },
    {
        "id": "ks4-power-s07",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A vacuum cleaner rated at 900 W runs for 6.0 minutes. "
                "Determine the energy it transfers, in kJ.",
        "options": [
            "5.4 kJ",
            "0.15 kJ",
            "324 kJ",
            "19 440 kJ",
        ],
        "correct_index": 2,
        "why": "6.0 minutes is 360 s, so E = 900 x 360 = 324 000 J, which is "
               "324 kJ.",
    },
    {
        "id": "ks4-power-s08",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A microwave oven heats a bowl of soup, transferring 96 000 J "
                "in 2.0 minutes. Determine the power of the oven.",
        "options": [
            "48 000 W",
            "1600 W",
            "0.0013 W",
            "800 W",
        ],
        "correct_index": 3,
        "why": "2.0 minutes is 120 s, so P = 96 000 / 120 = 800 W.",
    },
    {
        "id": "ks4-power-s09",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drill rated at 600 W transfers 21 000 J of energy while "
                "making one hole. Calculate the time for which it ran.",
        "options": [
            "35 s",
            "0.029 s",
            "12 600 000 s",
            "350 s",
        ],
        "correct_index": 0,
        "why": "t = E / P = 21 000 / 600 = 35 s.",
    },
    {
        "id": "ks4-power-s10",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hydroelectric power station has a rated power output of "
                "2.5 MW. State this output in watts.",
        "options": [
            "2500 W",
            "2 500 000 W",
            "25 000 W",
            "2 500 000 000 W",
        ],
        "correct_index": 1,
        "why": "One megawatt is 1 000 000 W, so 2.5 MW is 2.5 x 1 000 000 = "
               "2 500 000 W.",
    },
    {
        "id": "ks4-power-s11",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A porter drags a heavy trunk 30 m along a level corridor "
                "with a constant horizontal force of 120 N, taking 20 s. "
                "Determine the power he develops.",
        "options": [
            "180 W",
            "72 000 W",
            "6.0 W",
            "3600 W",
        ],
        "correct_index": 0,
        "why": "The work done is F s = 120 x 30 = 3600 J, so P = 3600 / 20 = "
               "180 W.",
    },
    {
        "id": "ks4-power-s12",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A weightlifter raises an 80 kg barbell through 2.0 m in "
                "1.6 s. Calculate his average useful power output. "
                "(g = 9.8 N/kg)",
        "options": [
            "1568 W",
            "100 W",
            "784 W",
            "980 W",
        ],
        "correct_index": 3,
        "why": "The work done is 80 x 9.8 x 2.0 = 1568 J, so P = 1568 / 1.6 "
               "= 980 W.",
    },
    {
        "id": "ks4-power-s13",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1000 W kettle is switched on for 2.0 minutes and a 1000 W "
                "hairdryer for 30 s. Determine which one transfers more "
                "energy.",
        "options": [
            "The hairdryer, because a hairdryer always transfers energy "
            "faster than a kettle",
            "Neither of them, because two appliances sharing a power rating "
            "transfer equal energy",
            "The kettle, because water must reach a higher temperature and "
            "that raises the rating",
            "The kettle, because both of them transfer 1000 J each second "
            "and the kettle is left running four times as long",
        ],
        "correct_index": 3,
        "why": "Both transfer 1000 J per second, but 120 s against 30 s "
               "gives 120 000 J against 30 000 J.",
    },
    {
        "id": "ks4-power-s14",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the power rating of an appliance does not on its "
                "own tell you how much energy the appliance will transfer.",
        "options": [
            "Because the rating is the total energy the appliance holds, and "
            "a part of that total is always left unused at the end",
            "Because the rating is joules per second, so the energy also "
            "depends on the running time",
            "Because the rating counts only the energy that is wasted rather "
            "than the energy transferred",
            "Because the rating itself alters each time the appliance is "
            "switched on and off at the wall",
        ],
        "correct_index": 1,
        "why": "A rating is a rate, so the energy transferred is that rate "
               "multiplied by the time the appliance runs.",
    },
    {
        "id": "ks4-power-s15",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2000 W heater is left switched on for one hour. Calculate "
                "the energy it transfers, in MJ.",
        "options": [
            "0.12 MJ",
            "0.0020 MJ",
            "7.2 MJ",
            "432 MJ",
        ],
        "correct_index": 2,
        "why": "One hour is 3600 s, so E = 2000 x 3600 = 7 200 000 J, which "
               "is 7.2 MJ.",
    },
    {
        "id": "ks4-power-s16",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist does 24 000 J of useful work in 50 s. Calculate "
                "her average power output.",
        "options": [
            "1 200 000 W",
            "0.0021 W",
            "48 W",
            "480 W",
        ],
        "correct_index": 3,
        "why": "P = W / t = 24 000 / 50 = 480 W.",
    },
    {
        "id": "ks4-power-s17",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 4.5 kW escalator motor operates continuously for 2.0 "
                "minutes. Calculate the energy it transfers, in kJ.",
        "options": [
            "540 kJ",
            "9.0 kJ",
            "0.54 kJ",
            "32 400 kJ",
        ],
        "correct_index": 0,
        "why": "4.5 kW is 4500 W and 2.0 minutes is 120 s, so E = 4500 x 120 "
               "= 540 000 J, or 540 kJ.",
    },
    {
        "id": "ks4-power-s18",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fountain pump raises 200 kg of water through a vertical "
                "height of 9.0 m in 30 s. Calculate its useful power output. "
                "(g = 9.8 N/kg)",
        "options": [
            "17 640 W",
            "588 W",
            "60.0 W",
            "1960 W",
        ],
        "correct_index": 1,
        "why": "The work done is 200 x 9.8 x 9.0 = 17 640 J, so P = 17 640 / "
               "30 = 588 W.",
    },
    {
        "id": "ks4-power-s19",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A toaster rated at 1.2 kW transfers 132 kJ of energy. "
                "Calculate the time for which it was switched on.",
        "options": [
            "0.11 s",
            "158 400 s",
            "110 s",
            "11 s",
        ],
        "correct_index": 2,
        "why": "t = E / P = 132 000 / 1200 = 110 s.",
    },
    {
        "id": "ks4-power-s20",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Motor X does 9000 J of work in 30 s and motor Y does 6000 J "
                "of work in 15 s. Determine which motor has the greater power "
                "output.",
        "options": [
            "Motor X, because it does more work in total",
            "Motor X, because it keeps running for twice as long as motor Y "
            "does",
            "Motor Y, because it does its work at the greater rate",
            "Neither, because both motors end up transferring energy at the "
            "same rate",
        ],
        "correct_index": 2,
        "why": "Power is the work done divided by the time taken, so motor X "
               "gives 9000 / 30 = 300 W and motor Y gives 6000 / 15 = 400 W.",
    },
    {
        "id": "ks4-power-s21",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 50 W filament lamp and a 5.0 W LED lamp are each switched "
                "on for 4.0 minutes. Calculate the difference between the "
                "energies they transfer.",
        "options": [
            "10 800 J",
            "12 000 J",
            "2700 J",
            "180 J",
        ],
        "correct_index": 0,
        "why": "4.0 minutes is 240 s, so the lamps transfer 12 000 J and "
               "1200 J, a difference of 10 800 J.",
    },
    {
        "id": "ks4-power-s22",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station has a power output of 750 MW. Determine the "
                "energy it transfers each second.",
        "options": [
            "750 kJ",
            "750 MJ",
            "750 J",
            "0.75 MJ",
        ],
        "correct_index": 1,
        "why": "One watt is one joule per second, so an output of 750 MW "
               "transfers 750 MJ every second.",
    },
    {
        "id": "ks4-power-s23",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a kilowatt-hour measures.",
        "options": [
            "A power, equal to one kilowatt of energy being supplied for "
            "every single hour of a day that a meter is running",
            "A time, equal to the hour that a 1 kW appliance is able to keep "
            "running",
            "An amount of energy, equal to that transferred by a 1 kW "
            "appliance in one hour",
            "A rate of charging, equal to one extra kilowatt being added to "
            "a battery each hour",
        ],
        "correct_index": 2,
        "why": "A kilowatt-hour is a power multiplied by a time, so it is an "
               "energy: 1000 W x 3600 s = 3 600 000 J.",
    },
    {
        "id": "ks4-power-s24",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A charger delivers 15 000 J of energy to a phone battery "
                "over 25 minutes. Determine its average power.",
        "options": [
            "600 W",
            "0.10 W",
            "375 000 W",
            "10 W",
        ],
        "correct_index": 3,
        "why": "25 minutes is 1500 s, so P = 15 000 / 1500 = 10 W.",
    },
    {
        "id": "ks4-power-s25",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A laptop transfers energy at a rate of 40 W. Determine the "
                "energy it transfers in 2.0 hours, in kJ.",
        "options": [
            "288 kJ",
            "4.8 kJ",
            "0.080 kJ",
            "17 280 kJ",
        ],
        "correct_index": 0,
        "why": "2.0 hours is 7200 s, so E = 40 x 7200 = 288 000 J, which is "
               "288 kJ.",
    },
    {
        "id": "ks4-power-s26",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An appliance transfers 4.0 kJ of energy every 8.0 s. "
                "Calculate its power, in kW.",
        "options": [
            "2.0 kW",
            "0.50 kW",
            "32 kW",
            "500 kW",
        ],
        "correct_index": 1,
        "why": "P = E / t = 4000 / 8.0 = 500 W, and 500 W is 0.50 kW.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Unfamiliar contexts, the unknown moved around the equation, work found
    # from a force or from m g h first, and the comparisons and evaluations.
    {
        "id": "ks4-power-h05",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A forklift truck lifts a crate of mass 250 kg onto a shelf "
                "8.0 m high, taking 5.0 s to do it. Determine its useful "
                "power output, in kW. (g = 9.8 N/kg)",
        "options": [
            "19.6 kW",
            "0.40 kW",
            "3.92 kW",
            "392 kW",
        ],
        "correct_index": 2,
        "why": "The work done is 250 x 9.8 x 8.0 = 19 600 J, so P = 19 600 / "
               "5.0 = 3920 W, which is 3.92 kW.",
    },
    {
        "id": "ks4-power-h06",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crane motor has a useful power output of 4.9 kW. "
                "Determine the largest mass it can raise through 5.0 m in "
                "7.0 s. (g = 9.8 N/kg)",
        "options": [
            "100 kg",
            "3500 kg",
            "6860 kg",
            "700 kg",
        ],
        "correct_index": 3,
        "why": "E = P x t = 4900 x 7.0 = 34 300 J, and m = E / (g h) = "
               "34 300 / (9.8 x 5.0) = 700 kg.",
    },
    {
        "id": "ks4-power-h07",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 3.0 kW kettle and a 2.0 kW kettle each transfer 420 kJ of "
                "energy to the water inside them. Determine how much longer "
                "the 2.0 kW kettle takes.",
        "options": [
            "70 s",
            "140 s",
            "210 s",
            "350 s",
        ],
        "correct_index": 0,
        "why": "t = E / P gives 420 000 / 3000 = 140 s and 420 000 / 2000 = "
               "210 s, a difference of 70 s.",
    },
    {
        "id": "ks4-power-h08",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil says that a 3 kW heater must transfer more energy "
                "than a 1 kW heater. Evaluate this claim.",
        "options": [
            "It is right: a larger rating means more joules are transferred, "
            "whatever the times are",
            "It is wrong: a rating fixes only the rate, so the 1 kW heater "
            "left on three times as long transfers just as much",
            "It is right: a 1 kW heater can never transfer as much as three "
            "thousand joules in total",
            "It is wrong: the 1 kW heater transfers more, because a weaker "
            "heater has to stay on longer",
        ],
        "correct_index": 1,
        "why": "Energy is power multiplied by time, so a smaller rating over "
               "a longer time can transfer just as much.",
    },
    {
        "id": "ks4-power-h09",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hoist lifts a steel beam of mass 1.5 tonnes to a platform "
                "8.0 m above the ground, taking 50 s. Calculate the useful "
                "power output of the hoist, in kW. (1 tonne = 1000 kg, "
                "g = 9.8 N/kg)",
        "options": [
            "118 kW",
            "0.24 kW",
            "2.35 kW",
            "0.0024 kW",
        ],
        "correct_index": 2,
        "why": "1.5 tonnes is 1500 kg, so the work done is 1500 x 9.8 x 8.0 "
               "= 117 600 J and P = 117 600 / 50 = 2352 W, or 2.35 kW.",
    },
    {
        "id": "ks4-power-h10",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A firefighter has a mass of 80 kg and carries 20 kg of "
                "equipment. She reaches a vertical height of 10 m up a "
                "ladder after 20 s. Calculate her average useful power "
                "output. (g = 9.8 N/kg)",
        "options": [
            "392 W",
            "50.0 W",
            "9800 W",
            "490 W",
        ],
        "correct_index": 3,
        "why": "The firefighter and her equipment come to 100 kg, so the "
               "work done is 100 x 9.8 x 10 = 9800 J and P = 9800 / 20 = "
               "490 W.",
    },
    {
        "id": "ks4-power-h11",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Asked for the power of a 2.5 kW appliance used for 2.0 "
                "minutes, a pupil writes 2.5 x 2.0 = 5.0 W. Identify what "
                "has gone wrong.",
        "options": [
            "Multiplying a power by a time gives an energy, not a power, and "
            "that energy is 300 kJ",
            "The two numbers should have been divided instead of multiplied, "
            "which makes the power 1.25 W across the two minutes",
            "The rating had to be halved before it was used, so the power of "
            "the appliance is really 1.25 kW",
            "Only the unit is at fault here, so the answer should have been "
            "written down as 5.0 kW",
        ],
        "correct_index": 0,
        "why": "The pupil has used E = P x t, and done it in the wrong "
               "units: 2500 x 120 = 300 000 J, which is 300 kJ of energy.",
    },
    {
        "id": "ks4-power-h12",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two lifts raise identical loads through the same height, "
                "one in 10 s and the other in 25 s. Predict how the powers "
                "of the two motors compare.",
        "options": [
            "The slower lift's motor has 2.5 times the power, because it "
            "keeps working for longer",
            "The faster lift's motor has 2.5 times the power of the slower "
            "lift's motor",
            "The two motors have equal power, because the power of a lift is "
            "set by its load and its height alone",
            "The faster lift's motor has 15 times the power, taken from the "
            "difference between the two times that are given",
        ],
        "correct_index": 1,
        "why": "The work done is the same, so power is inversely "
               "proportional to time and 25 / 10 = 2.5.",
    },
    {
        "id": "ks4-power-h13",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tumble dryer rated at 2.7 kW is used for 40 minutes. "
                "Determine the energy it transfers, in MJ.",
        "options": [
            "0.11 MJ",
            "0.0065 MJ",
            "6.48 MJ",
            "389 MJ",
        ],
        "correct_index": 2,
        "why": "40 minutes is 2400 s and 2.7 kW is 2700 W, so E = 2700 x "
               "2400 = 6 480 000 J, which is 6.48 MJ.",
    },
    {
        "id": "ks4-power-h14",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An immersion heater rated at 2.0 kW must transfer 5.4 MJ of "
                "energy to a tank of water. Determine how long it must run, "
                "in hours.",
        "options": [
            "2.7 hours",
            "45 hours",
            "0.00075 hours",
            "0.75 hours",
        ],
        "correct_index": 3,
        "why": "t = E / P = 5 400 000 / 2000 = 2700 s, and 2700 / 3600 = "
               "0.75 hours.",
    },
    {
        "id": "ks4-power-h15",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wind turbine is rated at 2.0 MW. Determine how many "
                "500 kW diesel generators would be needed to match its "
                "rated output.",
        "options": [
            "4 generators",
            "40 generators",
            "2.5 generators",
            "250 generators",
        ],
        "correct_index": 0,
        "why": "2.0 MW is 2 000 000 W and 500 kW is 500 000 W, so "
               "2 000 000 / 500 000 = 4 generators.",
    },
    {
        "id": "ks4-power-h16",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil says that an appliance with a higher power rating "
                "always costs more to run than one with a lower rating. "
                "Evaluate this claim.",
        "options": [
            "It is right: a higher rating transfers more joules in each and "
            "every case, so more is always paid out for it",
            "It is wrong: the cost follows the energy transferred, so a high "
            "rating alone never settles it",
            "It is wrong: the rating gives the total energy used up, so the "
            "running time makes no difference",
            "It is right: a higher-rated appliance draws the energy it needs "
            "from the mains far more cheaply",
        ],
        "correct_index": 1,
        "why": "Energy is power multiplied by time, so a 3 kW appliance used "
               "for a minute transfers less than a 1 kW one used all day.",
    },
    {
        "id": "ks4-power-h17",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tug pulls a boat with a steady force of 960 N and moves "
                "it 150 m in 60 s. Calculate the power of the tug, in kW.",
        "options": [
            "144 kW",
            "8640 kW",
            "2.4 kW",
            "0.016 kW",
        ],
        "correct_index": 2,
        "why": "The work done is 960 x 150 = 144 000 J, so P = W / t = "
               "144 000 / 60 = 2400 W, which is 2.4 kW.",
    },
    {
        "id": "ks4-power-h18",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station transfers 900 MJ of energy every 2.0 s. "
                "Determine its power output, in MW.",
        "options": [
            "1800 MW",
            "225 MW",
            "0.0022 MW",
            "450 MW",
        ],
        "correct_index": 3,
        "why": "P = E / t = 900 / 2.0 = 450 MJ each second, and one "
               "megajoule per second is one megawatt.",
    },
    {
        "id": "ks4-power-h19",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 100 W lamp is left on for a whole day and a 2000 W kettle "
                "is used for 5.0 minutes. Determine which of them transfers "
                "more energy.",
        "options": [
            "The lamp, because 8.64 MJ over the day is far more than the "
            "kettle's 0.60 MJ",
            "The kettle, because a larger rating always wins, whatever "
            "the times are",
            "The kettle, because a lamp's light carries hardly any "
            "energy",
            "Neither, because a low power always matches a high one "
            "over time",
        ],
        "correct_index": 0,
        "why": "A day is 86 400 s, so the lamp transfers 100 x 86 400 = "
               "8 640 000 J while the kettle transfers 2000 x 300 = "
               "600 000 J.",
    },
    {
        "id": "ks4-power-h20",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 750 W microwave oven takes 4.0 minutes to heat a meal. "
                "Predict how long a 1000 W microwave oven would take to "
                "transfer the same energy.",
        "options": [
            "5.3 minutes",
            "3.0 minutes",
            "1.3 minutes",
            "4.0 minutes",
        ],
        "correct_index": 1,
        "why": "The energy needed is 750 x 240 = 180 000 J, so t = 180 000 / "
               "1000 = 180 s, which is 3.0 minutes.",
    },
    {
        "id": "ks4-power-h21",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil writes that a 12 W lamp transfers 12 J of energy "
                "every minute. Explain the correction needed.",
        "options": [
            "It transfers 12 J every hour instead, because a watt is one "
            "joule for each hour that a device is used",
            "It transfers 0.20 J every second, by sharing 12 J over the "
            "minute",
            "It transfers 12 J every second, which comes to 720 J in every "
            "minute",
            "The sentence is right, because a watt is defined as one joule "
            "each minute",
        ],
        "correct_index": 2,
        "why": "A watt is a joule per second, so a 12 W lamp transfers 12 J "
               "each second and 12 x 60 = 720 J each minute.",
    },
    {
        "id": "ks4-power-h22",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chair lift raises 20 skiers of average mass 70 kg through "
                "a vertical height of 6.0 m each minute. Calculate the "
                "minimum power of its motor. (g = 9.8 N/kg)",
        "options": [
            "82 320 W",
            "140 W",
            "22.9 W",
            "1372 W",
        ],
        "correct_index": 3,
        "why": "The total mass is 20 x 70 = 1400 kg, so the work done each "
               "minute is 1400 x 9.8 x 6.0 = 82 320 J and P = 82 320 / 60 = "
               "1372 W.",
    },
    {
        "id": "ks4-power-h23",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Crane A raises 600 kg through 10 m in 24 s. Crane B raises "
                "1200 kg through 10 m in 48 s. Determine which crane has "
                "the greater useful power output. (g = 9.8 N/kg)",
        "options": [
            "Neither: both have an output of 2450 W, because crane B does "
            "twice the work in twice the time",
            "Crane B, because a crane that lifts a heavier load must always "
            "turn out to have the greater power output of the two",
            "Crane A, because a shorter lifting time on its own settles "
            "which crane is more powerful",
            "Crane B, because the power of a crane depends only on the work "
            "that the crane does",
        ],
        "correct_index": 0,
        "why": "Crane A gives 58 800 / 24 = 2450 W and crane B gives "
               "117 600 / 48 = 2450 W, so the two outputs are equal.",
    },
    {
        "id": "ks4-power-h24",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.5 kW lawnmower and a 400 W hedge trimmer are both used "
                "for 15 minutes. Calculate the total energy transferred, in "
                "MJ.",
        "options": [
            "2.25 MJ",
            "2.61 MJ",
            "0.36 MJ",
            "0.044 MJ",
        ],
        "correct_index": 1,
        "why": "15 minutes is 900 s and the two ratings come to 2900 W, so "
               "E = 2900 x 900 = 2 610 000 J, which is 2.61 MJ.",
    },
    {
        "id": "ks4-power-h25",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil says that an appliance with a high power rating "
                "must hold a large store of energy inside it. Evaluate this "
                "claim.",
        "options": [
            "It is right: the joules have to be held inside the appliance "
            "before they can be used",
            "It is wrong: a high rating means the appliance holds its store "
            "of energy for a shorter time",
            "It is wrong: the rating is a rate of transfer, and the energy "
            "only arrives from the supply as the appliance uses it",
            "It is right: a bigger rating needs a bigger store, and that is "
            "why such appliances are heavy",
        ],
        "correct_index": 2,
        "why": "A rating says how many joules pass through the appliance "
               "each second, not how many are sitting inside it.",
    },
    {
        "id": "ks4-power-h26",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wind turbine rated at 1.5 MW runs at its rated output for "
                "4.0 hours. Determine the energy it transfers, in MJ.",
        "options": [
            "6.0 MJ",
            "360 MJ",
            "21.6 MJ",
            "21 600 MJ",
        ],
        "correct_index": 3,
        "why": "4.0 hours is 14 400 s and 1.5 MW is 1 500 000 W, so E = "
               "1 500 000 x 14 400 = 21 600 000 000 J, which is 21 600 MJ.",
    },
]
