"""Physics · Electricity — the MRB-338 expansion of `energy-transfers-appliances`.

The weight falls where the spec point actually splits in two. One half is
named recall — which store a particular appliance fills, and the fact that
every appliance dissipates some energy to the thermal store of its
surroundings — so the easier rows and six standard rows walk a fresh set of
devices (toaster, charger, loudspeaker, hairdryer, food mixer, cordless
drill, torch) that the baseline never named. The other half is arithmetic,
and the arithmetic is where pupils lose marks, so the remaining rows rotate
the unknown through E, P and t, and rotate the units through joules,
kilowatt-hours and money, keeping the seconds-versus-hours trap in the
distractors rather than in the stem.
"""

TOPIC = "electricity"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ───────────────────────────────────────────────────────────
    {
        "id": "ks4-energy-transfers-appliances-e05",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric toaster is switched on to brown two slices of "
                "bread. Name the main energy transfer taking place.",
        "options": [
            "Electrical to thermal",
            "Electrical to kinetic",
            "Electrical to sound",
            "Chemical to thermal",
        ],
        "correct_index": 0,
        "why": "The heating elements transfer energy electrically to the "
               "thermal store of the bread and the air around it.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e06",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A phone is plugged into a mains charger and is charging. "
                "State the main energy transfer taking place.",
        "options": [
            "Electrical to kinetic",
            "Chemical to electrical",
            "Electrical to chemical",
            "Electrical to sound",
        ],
        "correct_index": 2,
        "why": "A charger fills the chemical store of the battery; the "
               "reverse transfer happens later, when the phone is used.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e07",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the useful energy transfer that takes place in a "
                "loudspeaker.",
        "options": [
            "Electrical to light",
            "Electrical to sound",
            "Sound to electrical",
            "Electrical to chemical",
        ],
        "correct_index": 1,
        "why": "The coil makes the cone vibrate, so energy is transferred "
               "electrically and carried away as sound.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e08",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hairdryer blows warm air. Identify its useful energy "
                "transfers and the main wasted transfer.",
        "options": [
            "Useful: electrical to sound and light. Wasted: electrical to "
            "thermal",
            "Useful: electrical to chemical in the element. Wasted: electrical "
            "to thermal and sound",
            "Useful: thermal to electrical. Wasted: electrical to kinetic "
            "and sound",
            "Useful: electrical to thermal and kinetic. Wasted: electrical "
            "to sound",
        ],
        "correct_index": 3,
        "why": "The element heats the air and the motor drives the fan, so "
               "both transfers are useful; the noise it makes is wasted.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e09",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement about the energy supplied to an electrical "
                "appliance is correct?",
        "options": [
            "Some energy is always dissipated to the thermal store of the "
            "surroundings",
            "The energy supplied is destroyed inside the appliance as it "
            "does its job",
            "The wasted energy stays stored inside the appliance until it is "
            "switched off again",
            "The whole of the energy supplied is transferred to the useful "
            "store",
        ],
        "correct_index": 0,
        "why": "No appliance is 100% efficient — every one of them "
               "dissipates some energy to the surroundings as thermal "
               "energy.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e10",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fan heater carries the label 1400 W. State what this "
                "power rating tells you about the heater.",
        "options": [
            "It transfers a total of 1400 joules before it switches itself "
            "off",
            "It transfers 1400 joules of energy in each hour it is switched "
            "on",
            "It transfers 1400 joules of energy in each second it is "
            "switched on",
            "It draws a steady current of 1400 amperes from the mains supply "
            "while it is running",
        ],
        "correct_index": 2,
        "why": "Power is the energy transferred each second, so a 1400 W "
               "rating means 1400 J every second.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e11",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An appliance is labelled 850 W. Calculate its power in "
                "kilowatts.",
        "options": [
            "8.5 kW",
            "0.85 kW",
            "85 kW",
            "850 000 kW",
        ],
        "correct_index": 1,
        "why": "There are 1000 W in 1 kW, so 850 ÷ 1000 = 0.85 kW.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e12",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An appliance transfers 3.0 kWh of energy. Electricity is "
                "charged at 24p per kWh. Calculate the cost.",
        "options": [
            "8p",
            "24p",
            "27p",
            "72p",
        ],
        "correct_index": 3,
        "why": "Cost = energy × price per unit = 3.0 × 24 = 72p.",
    },

    # ── standard ─────────────────────────────────────────────────────────
    {
        "id": "ks4-energy-transfers-appliances-s05",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A food mixer is used to beat a cake mixture. Identify the "
                "useful energy transfer and the main wasted transfers.",
        "options": [
            "Useful: electrical to thermal in the beaters. Wasted: electrical "
            "to kinetic and sound",
            "Useful: electrical to kinetic. Wasted: electrical to thermal "
            "and sound",
            "Useful: electrical to sound. Wasted: electrical to kinetic "
            "and thermal",
            "Useful: kinetic to electrical. Wasted: kinetic to thermal "
            "and sound",
        ],
        "correct_index": 1,
        "why": "The motor's useful output is the kinetic store of the "
               "turning beaters; the warmth of the motor and the noise it "
               "makes are both wasted.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s06",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A filament lamp and an LED lamp give out the same amount of "
                "light. Compare the energy each one wastes.",
        "options": [
            "The filament lamp wastes far more energy as thermal energy "
            "than the LED does",
            "The LED wastes far more thermal energy than the filament lamp",
            "Both waste the same energy, because both run from the mains",
            "The filament lamp wastes energy as sound, not as heat",
        ],
        "correct_index": 0,
        "why": "A filament has to reach white heat to glow, so most of the "
               "energy supplied to it is dissipated as thermal energy; an "
               "LED needs far less.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s07",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A television transfers energy from the mains while a film "
                "is playing. State its two useful outputs and the store the "
                "wasted energy ends up in.",
        "options": [
            "Useful: light and kinetic energy, because the moving picture "
            "carries energy. Wasted: the thermal store of the surroundings",
            "Useful: sound and chemical energy. Wasted: the kinetic store "
            "of the moving air",
            "Useful: light and thermal energy. Wasted: the chemical store "
            "of the mains supply",
            "Useful: light and sound energy. Wasted: the thermal store of "
            "the surroundings",
        ],
        "correct_index": 3,
        "why": "A television is built to give out light and sound; the "
               "energy it does not transfer usefully warms the set and then "
               "the room.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s08",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cordless drill is charged from the mains and then used to "
                "drill a hole. Describe the energy transfers, in order.",
        "options": [
            "Chemical to electrical while the drill charges, then electrical "
            "to kinetic and thermal while drilling",
            "Electrical to kinetic while charging, then kinetic to chemical "
            "and thermal while drilling",
            "Electrical to chemical while charging, then chemical to "
            "kinetic and thermal while drilling",
            "Electrical to thermal while charging, then thermal to kinetic "
            "and chemical while drilling",
        ],
        "correct_index": 2,
        "why": "Charging fills the battery's chemical store; the motor then "
               "empties it into the kinetic store of the bit, warming the "
               "drill as it goes.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s09",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the energy transfers that take place in a "
                "battery-powered torch while it is switched on.",
        "options": [
            "Chemical to light and thermal",
            "Electrical to chemical and then to light",
            "Light to chemical and thermal",
            "Thermal to light and electrical",
        ],
        "correct_index": 0,
        "why": "The cells' chemical store empties, the bulb gives out light, "
               "and the bulb and cells also warm up, so some is wasted as "
               "thermal energy.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s10",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A household wants to reduce the energy its heating system "
                "transfers each winter. Suggest the most effective change.",
        "options": [
            "Run the heating at night, when the price per kWh is lower",
            "Fit better loft and wall insulation, so less energy is needed "
            "to keep the rooms warm",
            "Fit a heater with a higher power rating, so the rooms warm up "
            "more quickly",
            "Replace the filament lamps with LED lamps, which lowers the "
            "heating energy",
        ],
        "correct_index": 1,
        "why": "Insulation slows the energy escaping through the roof and "
               "walls, so the heating has to replace less of it.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s11",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A microwave oven rated 750 W heats a bowl of soup for 2.0 "
                "minutes. Calculate the energy transferred, in joules.",
        "options": [
            "375 J",
            "1500 J",
            "90 000 J",
            "45 000 J",
        ],
        "correct_index": 2,
        "why": "The time must be in seconds: E = P × t = 750 × 120 = "
               "90 000 J.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s12",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A laptop charger rated 72 W transfers 108 000 J of energy. "
                "Calculate how long it was switched on, in minutes.",
        "options": [
            "1500 minutes",
            "1.5 minutes",
            "150 minutes",
            "25 minutes",
        ],
        "correct_index": 3,
        "why": "t = E ÷ P = 108 000 ÷ 72 = 1500 s, and 1500 ÷ 60 = 25 "
               "minutes.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s13",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric blanket transfers 45 000 J of energy in 15 "
                "minutes. Calculate its power.",
        "options": [
            "50 W",
            "3000 W",
            "750 W",
            "675 000 W",
        ],
        "correct_index": 0,
        "why": "P = E ÷ t = 45 000 ÷ (15 × 60) = 45 000 ÷ 900 = 50 W.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s14",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dishwasher rated 2.4 kW runs a cycle lasting 1 hour 30 "
                "minutes. Calculate the energy transferred, in kWh.",
        "options": [
            "1.6 kWh",
            "3.6 kWh",
            "3.9 kWh",
            "216 kWh",
        ],
        "correct_index": 1,
        "why": "1 hour 30 minutes is 1.5 h, so energy = 2.4 × 1.5 = 3.6 "
               "kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s15",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A television rated 250 W is left on for 6.0 hours. "
                "Calculate the energy transferred, in kWh.",
        "options": [
            "0.042 kWh",
            "150 kWh",
            "1.5 kWh",
            "1500 kWh",
        ],
        "correct_index": 2,
        "why": "250 W is 0.25 kW, so energy = 0.25 × 6.0 = 1.5 kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s16",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pair of hair straighteners rated 1.2 kW is used for 20 "
                "minutes. Calculate the energy transferred, in kWh.",
        "options": [
            "24 kWh",
            "0.060 kWh",
            "4.0 kWh",
            "0.40 kWh",
        ],
        "correct_index": 3,
        "why": "20 minutes is 20 ÷ 60 = 0.333 h, so energy = 1.2 × 0.333 = "
               "0.40 kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s17",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An appliance transfers 0.50 kWh of energy. Calculate this "
                "energy in joules.",
        "options": [
            "1 800 000 J",
            "1800 J",
            "500 J",
            "7 200 000 J",
        ],
        "correct_index": 0,
        "why": "1 kWh = 3 600 000 J, so 0.50 kWh = 0.50 × 3 600 000 = "
               "1 800 000 J.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s18",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A storage heater transfers 7 200 000 J of energy overnight. "
                "Calculate this energy in kilowatt-hours.",
        "options": [
            "20 kWh",
            "2.0 kWh",
            "0.50 kWh",
            "7200 kWh",
        ],
        "correct_index": 1,
        "why": "1 kWh = 3 600 000 J, so 7 200 000 ÷ 3 600 000 = 2.0 kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s19",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dishwasher transfers 1.4 kWh each cycle and is run 5 "
                "times a week. Electricity costs 24p per kWh. Calculate the "
                "cost for one week.",
        "options": [
            "£0.29",
            "£0.34",
            "£1.68",
            "£16.80",
        ],
        "correct_index": 2,
        "why": "The week's energy is 1.4 × 5 = 7.0 kWh, costing 7.0 × 24 = "
               "168p = £1.68.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s20",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A games console rated 500 W is used for 3.0 hours one "
                "evening. Electricity costs 32p per kWh. Calculate the cost "
                "of that evening's use.",
        "options": [
            "16p",
            "96p",
            "480p",
            "48p",
        ],
        "correct_index": 3,
        "why": "500 W is 0.50 kW, so 0.50 × 3.0 = 1.5 kWh, costing 1.5 × 32 "
               "= 48p.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s21",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A household is charged £4.50 for the electricity a heater "
                "used, at 30p per kWh. Calculate the energy the heater "
                "transferred.",
        "options": [
            "0.067 kWh",
            "15 kWh",
            "1.5 kWh",
            "135 kWh",
        ],
        "correct_index": 1,
        "why": "Energy = cost ÷ price per unit = 450p ÷ 30p = 15 kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s22",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Running an appliance rated 0.80 kW for 5.0 hours costs "
                "£1.08. Calculate the price charged per kWh.",
        "options": [
            "27p",
            "22p",
            "3.7p",
            "216p",
        ],
        "correct_index": 0,
        "why": "The energy used is 0.80 × 5.0 = 4.0 kWh, so the price is "
               "108p ÷ 4.0 = 27p per kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s23",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pressure washer rated 2.0 kW and a vacuum cleaner rated "
                "1.4 kW are each used for 30 minutes. Calculate how much "
                "more energy the pressure washer transfers.",
        "options": [
            "1.7 kWh",
            "18 kWh",
            "0.30 kWh",
            "0.60 kWh",
        ],
        "correct_index": 2,
        "why": "Each runs for 0.5 h, so 2.0 × 0.5 = 1.0 kWh and 1.4 × 0.5 = "
               "0.70 kWh, a difference of 0.30 kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s24",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric oven rated 3.0 kW is used for 20 minutes on "
                "Monday and for 45 minutes on Tuesday. Calculate the extra "
                "energy transferred on Tuesday, in kWh.",
        "options": [
            "1.0 kWh",
            "2.25 kWh",
            "75 kWh",
            "1.25 kWh",
        ],
        "correct_index": 3,
        "why": "Tuesday is 25 minutes longer, which is 25 ÷ 60 = 0.4167 h, "
               "so the extra energy is 3.0 × 0.4167 = 1.25 kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s25",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An old chest freezer transfers 1.2 kWh each day and a new "
                "model transfers 0.75 kWh each day. Calculate the energy "
                "saved in 30 days.",
        "options": [
            "13.5 kWh",
            "0.45 kWh",
            "22.5 kWh",
            "58.5 kWh",
        ],
        "correct_index": 0,
        "why": "The daily saving is 1.2 − 0.75 = 0.45 kWh, so over 30 days "
               "it is 0.45 × 30 = 13.5 kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s26",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A broadband router rated 60 W is left switched on all day "
                "and all night. Calculate the energy it transfers in 24 "
                "hours, in kWh.",
        "options": [
            "0.144 kWh",
            "1.44 kWh",
            "2.5 kWh",
            "1440 kWh",
        ],
        "correct_index": 1,
        "why": "60 W is 0.060 kW, so the energy is 0.060 × 24 = 1.44 kWh.",
    },

    # ── harder ───────────────────────────────────────────────────────────
    {
        "id": "ks4-energy-transfers-appliances-h05",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shower rated 7.5 kW is used for 6 minutes by each of four "
                "people every day. Determine the cost of a week's showers at "
                "30p per kWh.",
        "options": [
            "£0.90",
            "£1.58",
            "£6.30",
            "£378.00",
        ],
        "correct_index": 2,
        "why": "The shower runs 24 minutes a day, which is 0.40 h, so 7.5 × "
               "0.40 = 3.0 kWh a day, 21 kWh a week, and 21 × 30p = £6.30.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h06",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student works out the energy transferred by an iron rated "
                "1200 W used for 30 minutes as 36 000 J, by multiplying 1200 "
                "by 30. Determine the correct energy transferred.",
        "options": [
            "36 000 J",
            "72 000 J",
            "216 000 J",
            "2 160 000 J",
        ],
        "correct_index": 3,
        "why": "For an answer in joules the time must be in seconds: 30 "
               "minutes is 1800 s, so E = 1200 × 1800 = 2 160 000 J.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h07",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A heater transfers 6.3 MJ of energy in 35 minutes. "
                "Determine its power, in kW.",
        "options": [
            "3.0 kW",
            "180 kW",
            "0.18 kW",
            "3000 kW",
        ],
        "correct_index": 0,
        "why": "6.3 MJ is 6 300 000 J and 35 minutes is 2100 s, so P = "
               "6 300 000 ÷ 2100 = 3000 W = 3.0 kW.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h08",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An appliance rated 1.6 kW transfers 6.4 kWh of energy. "
                "Determine for how long it was used.",
        "options": [
            "0.25 hours",
            "4.0 hours",
            "4.0 minutes",
            "10.2 hours",
        ],
        "correct_index": 1,
        "why": "Time = energy ÷ power = 6.4 ÷ 1.6 = 4.0 hours, because the "
               "energy is in kWh and the power is in kW.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h09",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wallpaper steamer rated 2.0 kW is used for 12 minutes. A "
                "desktop computer rated 150 W is used for 3.0 hours. "
                "Determine which transfers more energy, and by how much.",
        "options": [
            "The steamer, by 1.60 kWh",
            "The steamer, by 0.050 kWh",
            "The computer, by 0.050 kWh",
            "The computer, by 0.85 kWh",
        ],
        "correct_index": 2,
        "why": "The steamer transfers 2.0 × 0.20 = 0.40 kWh and the computer "
               "0.15 × 3.0 = 0.45 kWh, so the computer transfers 0.050 kWh "
               "more.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h10",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A supplier charges 26p per kWh for the first 300 kWh of a "
                "quarter and 22p per kWh for every kWh after that. Determine "
                "the bill for a household that used 540 kWh.",
        "options": [
            "£13.08",
            "£118.80",
            "£140.40",
            "£130.80",
        ],
        "correct_index": 3,
        "why": "300 × 26p = £78.00 and the remaining 240 kWh cost 240 × 22p "
               "= £52.80, giving £130.80 altogether.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h11",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Running an appliance for 5.0 hours costs £1.35 when "
                "electricity is charged at 27p per kWh. Determine the power "
                "rating of the appliance.",
        "options": [
            "1.0 kW",
            "5.0 kW",
            "0.20 kW",
            "6.8 kW",
        ],
        "correct_index": 0,
        "why": "The energy used is 135p ÷ 27p = 5.0 kWh, so the power is "
               "5.0 ÷ 5.0 = 1.0 kW.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h12",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An old washing machine transfers 1.4 kWh per wash and a new "
                "one transfers 0.75 kWh per wash. A family does 6 washes a "
                "week. Determine the money saved in 52 weeks at 25p per kWh.",
        "options": [
            "£0.98",
            "£50.70",
            "£8.45",
            "£202.80",
        ],
        "correct_index": 1,
        "why": "Each wash saves 0.65 kWh, so 0.65 × 6 × 52 = 202.8 kWh a "
               "year, and 202.8 × 25p = £50.70.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h13",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An iron rated 1.5 kW is used for 20 minutes, three times a "
                "week. Determine the energy transferred in 4 weeks, in kWh.",
        "options": [
            "0.50 kWh",
            "1.5 kWh",
            "6.0 kWh",
            "360 kWh",
        ],
        "correct_index": 2,
        "why": "Each use is 1.5 × (20 ÷ 60) = 0.50 kWh, and there are 12 "
               "uses in 4 weeks, so 0.50 × 12 = 6.0 kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h14",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Appliance A transfers 2.5 kWh of energy and appliance B "
                "transfers 8 000 000 J. Determine which transfers more "
                "energy.",
        "options": [
            "B, because 8 000 000 J is the same as about 8 kWh",
            "B, because an energy given in joules is always the larger one",
            "They transfer the same, because 8 000 000 J converts exactly to "
            "2.5 kWh",
            "A, because 8 000 000 J is the same as about 2.2 kWh",
        ],
        "correct_index": 3,
        "why": "8 000 000 ÷ 3 600 000 = 2.2 kWh, which is less than the 2.5 "
               "kWh transferred by A.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h15",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One use of a microwave oven rated 1.2 kW costs 9.0p when "
                "electricity is charged at 30p per kWh. Determine how long "
                "the oven was used, in minutes.",
        "options": [
            "15 minutes",
            "18 minutes",
            "135 minutes",
            "0.25 minutes",
        ],
        "correct_index": 0,
        "why": "The energy used is 9.0p ÷ 30p = 0.30 kWh, so the time is "
               "0.30 ÷ 1.2 = 0.25 h = 15 minutes.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h16",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that because a microwave oven rated 700 W "
                "has a lower power rating than an oven rated 2.0 kW, "
                "reheating a meal in the microwave must cost less. Evaluate "
                "this statement.",
        "options": [
            "It is justified, because a lower power rating gives a lower "
            "cost whatever the times are",
            "It is not justified, because the cost depends on the power and "
            "on the time each is used",
            "It is not justified, because it is the oven that has the lower "
            "power rating of the two",
            "It is justified, because the cost of running any appliance "
            "depends only on its power rating, not on the time",
        ],
        "correct_index": 1,
        "why": "Cost comes from energy, and energy is power × time, so the "
               "two running times are needed before the comparison can be "
               "made.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h17",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In one evening a household uses an oven rated 2.0 kW for 45 "
                "minutes, a dishwasher rated 0.50 kW for 2.0 hours and an "
                "iron rated 1.0 kW for 30 minutes. Determine the total cost "
                "at 28p per kWh.",
        "options": [
            "8.4p",
            "70p",
            "84p",
            "112p",
        ],
        "correct_index": 2,
        "why": "The three appliances transfer 1.5, 1.0 and 0.50 kWh, a total "
               "of 3.0 kWh, costing 3.0 × 28p = 84p.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h18",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A freezer transfers 1.68 kWh of energy in 24 hours. "
                "Determine its average power, in watts.",
        "options": [
            "14 W",
            "40 W",
            "0.070 W",
            "70 W",
        ],
        "correct_index": 3,
        "why": "Power = 1.68 ÷ 24 = 0.070 kW, and 0.070 × 1000 = 70 W.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h19",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A security light rated 15 W is left on for 12 hours each "
                "night. Determine the energy it transfers in one night, in "
                "joules.",
        "options": [
            "648 000 J",
            "180 J",
            "10 800 J",
            "64 800 J",
        ],
        "correct_index": 0,
        "why": "12 hours is 12 × 3600 = 43 200 s, so E = 15 × 43 200 = "
               "648 000 J.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h20",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A household cuts the time its storage heater rated 2.4 kW "
                "runs each day from 60 minutes to 40 minutes. Determine the "
                "percentage reduction in the energy it transfers each day.",
        "options": [
            "20%",
            "33%",
            "50%",
            "67%",
        ],
        "correct_index": 1,
        "why": "The energy falls from 2.4 kWh to 1.6 kWh, a drop of 0.80 "
               "kWh, and 0.80 ÷ 2.4 = 0.33, which is 33%.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h21",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Tariff A charges 30p per kWh and no standing charge. Tariff "
                "B charges 22p per kWh plus a standing charge of 40p a day. "
                "A household uses 6.0 kWh a day. Determine which tariff is "
                "cheaper, and by how much a day.",
        "options": [
            "Tariff A, by 8p a day",
            "Tariff A, by 48p a day",
            "Tariff B, by 8p a day",
            "Tariff B, by 88p a day",
        ],
        "correct_index": 2,
        "why": "Tariff A costs 6.0 × 30p = 180p and tariff B costs 6.0 × 22p "
               "+ 40p = 172p, so B is 8p cheaper each day.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h22",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A circuit transfers 7.2 kWh of energy in 6.0 hours. "
                "Determine the greatest number of identical lamps rated 300 "
                "W each that it could supply for that time.",
        "options": [
            "24 lamps",
            "40 lamps",
            "1200 lamps",
            "4 lamps",
        ],
        "correct_index": 3,
        "why": "The circuit supplies 7.2 ÷ 6.0 = 1.2 kW, which is 1200 W, "
               "and 1200 ÷ 300 = 4 lamps.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h23",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A phone battery stores 43 200 J of energy when it is fully "
                "charged. A charger transfers energy to it at 8.0 W. "
                "Determine the time needed for a full charge, in minutes.",
        "options": [
            "90 minutes",
            "1.5 minutes",
            "5400 minutes",
            "345 600 minutes",
        ],
        "correct_index": 0,
        "why": "t = E ÷ P = 43 200 ÷ 8.0 = 5400 s, and 5400 ÷ 60 = 90 "
               "minutes.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h24",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shop claims that switching a heater rated 1.6 kW off for "
                "15 minutes in every hour saves a quarter of the energy it "
                "would otherwise transfer. Evaluate this claim.",
        "options": [
            "Wrong — the saving is 15%, because it is off for 15 minutes",
            "Correct — the heater transfers 1.2 kWh an hour instead of 1.6 "
            "kWh, a saving of 25%",
            "Wrong — the saving is 75%, because the heater runs for only 45 "
            "minutes",
            "Wrong — there is no saving, because restarting the heater uses "
            "extra energy",
        ],
        "correct_index": 1,
        "why": "In 45 minutes the heater transfers 1.6 × 0.75 = 1.2 kWh "
               "instead of 1.6 kWh, and 0.40 ÷ 1.6 = 0.25, so a quarter is "
               "saved.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h25",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A television left on standby draws 3.0 W without stopping. "
                "Determine the energy it wastes in a year of 365 days, in "
                "kWh.",
        "options": [
            "1095 kWh",
            "2.628 kWh",
            "26.28 kWh",
            "26 280 kWh",
        ],
        "correct_index": 2,
        "why": "3.0 W is 0.0030 kW, and it runs 24 × 365 = 8760 hours, so "
               "0.0030 × 8760 = 26.28 kWh.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h26",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "After better loft insulation is fitted, a home's heating "
                "system rated 5.0 kW runs for 4.5 hours a day instead of 6.0 "
                "hours a day. Determine the energy saved in 30 days, in kWh.",
        "options": [
            "7.5 kWh",
            "675 kWh",
            "900 kWh",
            "225 kWh",
        ],
        "correct_index": 3,
        "why": "The heating runs 1.5 hours less each day, saving 5.0 × 1.5 = "
               "7.5 kWh a day, so 7.5 × 30 = 225 kWh in 30 days.",
    },
]
