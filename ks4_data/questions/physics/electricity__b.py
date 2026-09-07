"""Physics · Electricity — mains, power, appliances, the grid, static and fields.

The second half of the electricity topic: `mains-electricity`,
`power-electricity`, `energy-transfers-appliances`, `national-grid`,
`static-charge` and `electric-fields`. (`electricity__a.py` holds the first
six subtopics.)

Distractors are built from the brief's declared common mistakes: fuses and
switches belonging in the live wire while the earth wire normally carries
nothing; squaring the resistance instead of the current in P = I²R; mixing
joules-and-seconds with kilowatt-hours-and-hours; believing high transmission
voltage cuts the *power* rather than the *current*; thinking protons move when
an insulator is charged; and running electric field lines from negative to
positive as if they were electron paths.

Every calculation distractor is the answer a named error produces — a dropped
power of ten, an inverted ratio, a time left in minutes, a pence total written
as pounds — never noise. No question needs a figure: every circuit, plate
arrangement and field pattern is described in words.
"""

TOPIC = "electricity"
SUBJECT = "physics"

QUESTIONS = [
    # ── mains-electricity ────────────────────────────────────────────────
    {
        "id": "ks4-mains-electricity-e01",
        "subtopic_slug": "mains-electricity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the colour of the insulation on the neutral wire of a "
                "three-core mains cable.",
        "options": [
            "Blue",
            "Brown",
            "Green with a yellow stripe",
            "Black",
        ],
        "correct_index": 0,
        "why": "The neutral wire is blue; brown is live and green-and-yellow "
               "is earth.",
    },
    {
        "id": "ks4-mains-electricity-e02",
        "subtopic_slug": "mains-electricity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A three-pin plug is being wired. State which pin the brown "
                "wire must be connected to.",
        "options": [
            "The neutral pin",
            "The earth pin",
            "The live pin",
            "Either the live or the neutral pin, provided the earth pin is "
            "connected correctly",
        ],
        "correct_index": 2,
        "why": "Brown is the live wire, which carries the alternating "
               "potential difference of about 230 V, so it goes to the live "
               "pin.",
    },
    {
        "id": "ks4-mains-electricity-e03",
        "subtopic_slug": "mains-electricity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the current in the earth wire of an appliance that is "
                "working normally.",
        "options": [
            "The same current as in the neutral wire",
            "No current at all",
            "Half the current in the live wire",
            "Current only while the switch is open",
        ],
        "correct_index": 1,
        "why": "The earth wire is a safety wire — it carries current only "
               "during a fault, never in normal operation.",
    },
    {
        "id": "ks4-mains-electricity-e04",
        "subtopic_slug": "mains-electricity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hairdryer has a plastic case and is marked with the "
                "double-insulation symbol. Explain why it needs no earth "
                "wire.",
        "options": [
            "Its power rating is low, so any fault current would be far too "
            "small to be felt",
            "Its fuse is fitted in the neutral wire instead of the live wire, "
            "which isolates it",
            "It runs at a lower potential difference than the mains supply, "
            "so a fault cannot be lethal",
            "Two layers of insulation separate the live parts from anything "
            "the user can touch",
        ],
        "correct_index": 3,
        "why": "Double insulation means there is no conducting path from a "
               "live part to the user, so there is nothing for an earth wire "
               "to protect.",
    },
    {
        "id": "ks4-mains-electricity-s01",
        "subtopic_slug": "mains-electricity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the neutral wire is completely safe to touch "
                "because it is at 0 V. Explain why this is wrong.",
        "options": [
            "The neutral wire is at 230 V whenever the appliance is switched "
            "on",
            "The neutral wire carries the full working current of the "
            "appliance, and a fault can raise it above 0 V",
            "The neutral wire carries no current at all, but it is joined to "
            "the earth pin of the plug inside the socket",
            "The neutral wire is only safe once the earth wire has been "
            "disconnected",
        ],
        "correct_index": 1,
        "why": "Neutral sits near 0 V but still carries the whole working "
               "current, and a fault elsewhere can lift its potential — so it "
               "is never safe to treat as dead.",
    },
    {
        "id": "ks4-mains-electricity-s02",
        "subtopic_slug": "mains-electricity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A socket used for an outdoor lawnmower is protected by an "
                "RCD. Describe what the RCD detects.",
        "options": [
            "The total power drawn by the appliance, cutting the supply if "
            "that becomes too large",
            "The temperature of the live wire inside the plug, cutting the "
            "supply if it overheats",
            "The potential difference across the earth wire, which should be "
            "zero in normal use",
            "A difference between the current in the live wire and the "
            "current in the neutral wire",
        ],
        "correct_index": 3,
        "why": "Current leaking to earth — through a person, for example — "
               "makes live and neutral currents unequal, and the RCD cuts the "
               "supply within milliseconds.",
    },
    {
        "id": "ks4-mains-electricity-s03",
        "subtopic_slug": "mains-electricity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A metal-cased heater is NOT connected to an earth wire. A "
                "fault makes the live wire touch the metal case. Describe the "
                "hazard this creates.",
        "options": [
            "The case stays at 230 V and the fuse does not blow, so anyone "
            "touching the case receives a shock",
            "The fuse blows at once anyway, because the metal case has a very "
            "low resistance and draws an enormous current",
            "The current returns through the neutral wire, so the appliance "
            "stays safe",
            "Nothing happens until the appliance is switched on at the socket",
        ],
        "correct_index": 0,
        "why": "With no earth wire there is no low-resistance path for a large "
               "fault current, so the fuse never melts and the case is left "
               "live.",
    },
    {
        "id": "ks4-mains-electricity-s04",
        "subtopic_slug": "mains-electricity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A consumer unit uses circuit breakers rather than fuses. "
                "Give one advantage of a circuit breaker.",
        "options": [
            "It operates at a lower current than a fuse of the same rating",
            "It lets the appliance keep running while the fault is repaired",
            "It can be reset after a fault instead of being replaced",
            "It removes the need for an earth wire on metal-cased appliances",
        ],
        "correct_index": 2,
        "why": "A circuit breaker trips rather than melting, so once the fault "
               "is cleared it is switched back on instead of being replaced.",
    },
    {
        "id": "ks4-mains-electricity-h01",
        "subtopic_slug": "mains-electricity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An extension lead rated at 13 A is used to run a 2.4 kW "
                "heater, a 1.0 kW toaster and a 0.8 kW television at the same "
                "time from the 230 V mains. Determine whether the lead is "
                "overloaded.",
        "options": [
            "No — the total current is 4.2 A, well inside the 13 A rating",
            "No — no single appliance draws more than 13 A, so the lead is "
            "within its rating",
            "Yes — the total current is exactly 13.0 A, right on the rating",
            "Yes — the total current is about 18 A, above the 13 A rating",
        ],
        "correct_index": 3,
        "why": "The powers add to 4200 W, so I = 4200 ÷ 230 ≈ 18 A — the whole "
               "lead carries the total current, not each appliance's share.",
    },
    {
        "id": "ks4-mains-electricity-h02",
        "subtopic_slug": "mains-electricity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A table lamp draws 0.30 A in normal use. Its 3 A fuse is "
                "replaced with a 13 A fuse. Explain the danger this creates.",
        "options": [
            "A fault current of several amperes could flow without melting "
            "the fuse, so the flex overheats and may catch fire",
            "The lamp now draws 13 A instead of 0.30 A, so the bulb becomes "
            "far brighter and its filament quickly burns through",
            "The fuse blows every time the lamp is switched on, because 13 A "
            "is far too large",
            "The earth wire carries the extra current continuously, wasting "
            "energy",
        ],
        "correct_index": 0,
        "why": "A fuse must melt just above the working current — an oversized "
               "fuse allows a dangerous fault current to keep flowing through "
               "thin flex.",
    },
    {
        "id": "ks4-mains-electricity-h03",
        "subtopic_slug": "mains-electricity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a metal-cased drill with an earth wire and a "
                "plastic-cased drill marked as double insulated are each made "
                "safe if the live wire works loose inside.",
        "options": [
            "Both rely on the earth wire carrying the fault current away to "
            "the ground",
            "Neither is made safe — only an RCD protects against a loose live "
            "wire",
            "The metal-cased drill passes a large current to earth so the "
            "fuse blows; the plastic-cased drill has no conducting path to "
            "the user at all",
            "The metal-cased drill has no conducting path to the user at all, "
            "while the plastic-cased drill passes the fault current to earth "
            "and blows its fuse",
        ],
        "correct_index": 2,
        "why": "Earthing works by making the fault current large enough to "
               "blow the fuse; double insulation works by making sure the "
               "fault can never reach the user in the first place.",
    },
    {
        "id": "ks4-mains-electricity-h04",
        "subtopic_slug": "mains-electricity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electrician connects the metal water pipes and the metal "
                "sink in a kitchen to the earth of the supply. Suggest why.",
        "options": [
            "Earthed metalwork raises the resistance of the whole circuit, so "
            "that any fault current is reduced to a level far too small to "
            "give a shock to anyone touching it",
            "If a live wire touched the metalwork it would be held near 0 V "
            "and the fuse or breaker would cut the supply, instead of the "
            "metal becoming live",
            "Earthing stops alternating current flowing along metal pipes, "
            "which would corrode them",
            "Earthed metalwork stores any static charge safely until the next "
            "fault occurs",
        ],
        "correct_index": 1,
        "why": "Anything metal a person might touch is earthed for the same "
               "reason an appliance case is: a fault becomes a blown fuse "
               "rather than a live surface.",
    },

    # ── power-electricity ────────────────────────────────────────────────
    {
        "id": "ks4-power-electricity-e01",
        "subtopic_slug": "power-electricity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the electrical power of an appliance measures.",
        "options": [
            "The total energy the appliance transfers over its lifetime",
            "The charge that flows through the appliance each second",
            "The energy the appliance transfers each second",
            "The potential difference across the appliance each second",
        ],
        "correct_index": 2,
        "why": "Power is the rate of energy transfer — 1 watt is 1 joule "
               "transferred every second.",
    },
    {
        "id": "ks4-power-electricity-e02",
        "subtopic_slug": "power-electricity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The motor in a model crane runs from a 9.0 V supply and the "
                "current in it is 1.5 A. Calculate the power of the motor.",
        "options": [
            "13.5 W",
            "6.0 W",
            "0.17 W",
            "20.3 W",
        ],
        "correct_index": 0,
        "why": "P = V × I = 9.0 × 1.5 = 13.5 W — the current is not squared "
               "when the potential difference is the quantity you have.",
    },
    {
        "id": "ks4-power-electricity-e03",
        "subtopic_slug": "power-electricity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which equation gives the energy transferred when a charge Q "
                "moves through a potential difference V?",
        "options": [
            "E = Q ÷ V",
            "E = V ÷ Q",
            "E = V² × Q",
            "E = V × Q",
        ],
        "correct_index": 3,
        "why": "Potential difference is energy transferred per coulomb, so the "
               "energy is E = V × Q.",
    },
    {
        "id": "ks4-power-electricity-e04",
        "subtopic_slug": "power-electricity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A heater transfers 24 000 J of energy in 60 s. Calculate its "
                "power.",
        "options": [
            "40 W",
            "400 W",
            "1 440 000 W",
            "0.0025 W",
        ],
        "correct_index": 1,
        "why": "E = P × t, so P = 24 000 ÷ 60 = 400 W.",
    },
    {
        "id": "ks4-power-electricity-s01",
        "subtopic_slug": "power-electricity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An immersion heater element has a resistance of 20 Ω "
                "and carries a current of 9.0 A. Calculate the power it "
                "dissipates.",
        "options": [
            "1620 W",
            "180 W",
            "3600 W",
            "2.2 W",
        ],
        "correct_index": 0,
        "why": "P = I² × R = 9.0² × 20 = 81 × 20 = 1620 W — the current "
               "is squared, not the resistance.",
    },
    {
        "id": "ks4-power-electricity-s02",
        "subtopic_slug": "power-electricity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 9.0 V battery drives a current of 0.40 A through a motor "
                "for 2.0 minutes. Calculate the energy transferred.",
        "options": [
            "7.2 J",
            "216 J",
            "432 J",
            "48 J",
        ],
        "correct_index": 2,
        "why": "P = 9.0 × 0.40 = 3.6 W and t = 120 s, so E = 3.6 × 120 = "
               "432 J — the time must be in seconds.",
    },
    {
        "id": "ks4-power-electricity-s03",
        "subtopic_slug": "power-electricity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hairdryer element dissipates 1000 W when the current in it "
                "is 5.0 A. Calculate its resistance.",
        "options": [
            "200 Ω",
            "40 Ω",
            "5000 Ω",
            "0.025 Ω",
        ],
        "correct_index": 1,
        "why": "P = I² × R rearranges to R = P ÷ I² = 1000 ÷ 25 = 40 Ω.",
    },
    {
        "id": "ks4-power-electricity-s04",
        "subtopic_slug": "power-electricity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lamp A has a resistance of 6.0 Ω and lamp B has a resistance "
                "of 24 Ω. Each is connected on its own across the same 12 V "
                "supply. Compare the power each lamp transfers.",
        "options": [
            "Lamp B transfers four times the power of lamp A, because it has "
            "the greater resistance",
            "Lamp A transfers twice the power of lamp B",
            "They transfer the same power, because the potential difference "
            "is the same",
            "Lamp A transfers four times the power of lamp B — 24 W compared "
            "with 6.0 W",
        ],
        "correct_index": 3,
        "why": "Lamp A draws 12 ÷ 6.0 = 2.0 A so P = 24 W, while lamp B draws "
               "0.50 A so P = 6.0 W — at a fixed potential difference, lower "
               "resistance means more power.",
    },
    {
        "id": "ks4-power-electricity-h01",
        "subtopic_slug": "power-electricity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kW electric heater runs from the 230 V mains for 5.0 "
                "minutes. Determine the charge that flows through it.",
        "options": [
            "43 C",
            "2600 C",
            "8.7 C",
            "600 000 C",
        ],
        "correct_index": 1,
        "why": "I = P ÷ V = 2000 ÷ 230 ≈ 8.7 A, then Q = I × t = 8.7 × 300 ≈ "
               "2600 C.",
    },
    {
        "id": "ks4-power-electricity-h02",
        "subtopic_slug": "power-electricity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric shower is marked 8.5 kW, 230 V. Determine "
                "whether it can safely be run from a circuit protected by a "
                "32 A circuit breaker.",
        "options": [
            "Yes — the current is 8.5 A, well below the 32 A limit",
            "Yes — the current is 0.027 A, far below the 32 A limit",
            "No — the current is 370 A, far above the 32 A limit",
            "No — the current is about 37 A, above the 32 A limit",
        ],
        "correct_index": 3,
        "why": "I = P ÷ V = 8500 ÷ 230 ≈ 37 A, which exceeds the 32 A "
               "protection, so the shower needs its own higher-rated circuit.",
    },
    {
        "id": "ks4-power-electricity-h03",
        "subtopic_slug": "power-electricity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates the power dissipated in a 4.0 Ω "
                "resistor carrying 6.0 A as P = 6.0 × 4.0² = 96 W. Identify "
                "the error and give the correct power.",
        "options": [
            "The current is squared, not the resistance: P = 6.0² × 4.0 = "
            "144 W",
            "The resistance should be halved before squaring: P = 6.0² × 2.0 "
            "= 72 W",
            "Both quantities should be squared: P = 6.0² × 4.0² = 576 W",
            "Nothing is wrong — 96 W is correct because P = I × R²",
        ],
        "correct_index": 0,
        "why": "The equation is P = I² × R, so the 6.0 A is squared and the "
               "4.0 Ω is not: 36 × 4.0 = 144 W.",
    },
    {
        "id": "ks4-power-electricity-h04",
        "subtopic_slug": "power-electricity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Heater X runs at 3.0 kW for 8.0 minutes. Heater Y transfers "
                "the same energy in 24 minutes. Calculate the power of heater "
                "Y.",
        "options": [
            "9.0 kW",
            "24 kW",
            "1.0 kW",
            "3.0 kW",
        ],
        "correct_index": 2,
        "why": "The same energy in three times the time needs one third of the "
               "power: 3.0 ÷ 3 = 1.0 kW.",
    },

    # ── energy-transfers-appliances ──────────────────────────────────────
    {
        "id": "ks4-energy-transfers-appliances-e01",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main energy transfer that takes place in an "
                "electric kettle.",
        "options": [
            "Electrical to kinetic",
            "Chemical to electrical",
            "Electrical to sound",
            "Electrical to thermal",
        ],
        "correct_index": 3,
        "why": "The heating element transfers energy electrically to the "
               "thermal store of the water.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e02",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A vacuum cleaner is used to clean a carpet. Identify the "
                "useful energy transfer and the main wasted transfer.",
        "options": [
            "Useful: electrical to thermal. Wasted: electrical to kinetic",
            "Useful: electrical to kinetic. Wasted: electrical to thermal "
            "and sound",
            "Useful: chemical to kinetic. Wasted: chemical to light",
            "Useful: kinetic to electrical. Wasted: kinetic to thermal",
        ],
        "correct_index": 1,
        "why": "The motor's useful output is the kinetic energy of the fan "
               "that moves the air; the heat and noise it also produces are "
               "wasted.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e03",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many joules of energy there are in 1 "
                "kilowatt-hour.",
        "options": [
            "3 600 000 J",
            "1000 J",
            "3600 J",
            "60 000 J",
        ],
        "correct_index": 0,
        "why": "1 kWh = 1000 W × 3600 s = 3 600 000 J.",
    },
    {
        "id": "ks4-energy-transfers-appliances-e04",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 40 W fridge lamp is left on for 90 s. Calculate the "
                "energy transferred.",
        "options": [
            "0.44 J",
            "2.3 J",
            "3600 J",
            "216 000 J",
        ],
        "correct_index": 2,
        "why": "E = P × t = 40 × 90 = 3600 J, with the power in watts "
               "and the time in seconds.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s01",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 9 W LED lamp replaces a 60 W filament lamp. Each is used "
                "for 5 hours a day. Calculate the energy saved in one day, in "
                "kWh.",
        "options": [
            "255 kWh",
            "0.051 kWh",
            "0.255 kWh",
            "0.345 kWh",
        ],
        "correct_index": 2,
        "why": "The saving is 60 − 9 = 51 W = 0.051 kW, so 0.051 × 5 = 0.255 "
               "kWh each day.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s02",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A washing machine transfers 1.8 kWh of energy during a wash "
                "cycle lasting 1.5 hours. Calculate its average power in kW.",
        "options": [
            "1.2 kW",
            "2.7 kW",
            "0.83 kW",
            "1.8 kW",
        ],
        "correct_index": 0,
        "why": "Energy = power × time, so power = 1.8 ÷ 1.5 = 1.2 kW.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s03",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.5 kW tumble dryer runs for 45 minutes. Electricity costs "
                "28p per kWh. Calculate the cost of the cycle.",
        "options": [
            "£31.50",
            "£1.88",
            "£0.70",
            "£0.53",
        ],
        "correct_index": 3,
        "why": "45 minutes is 0.75 h, so 2.5 × 0.75 = 1.875 kWh and 1.875 × "
               "28p ≈ 53p.",
    },
    {
        "id": "ks4-energy-transfers-appliances-s04",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric shower transfers 5 400 000 J of energy in 10 "
                "minutes. Calculate its power output in kW.",
        "options": [
            "540 kW",
            "9.0 kW",
            "9000 kW",
            "90 kW",
        ],
        "correct_index": 1,
        "why": "P = E ÷ t = 5 400 000 ÷ 600 = 9000 W, which is 9.0 kW.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h01",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A household uses a 3.0 kW immersion heater for 40 minutes "
                "each day. Determine the cost of running it for 30 days at "
                "27p per kWh.",
        "options": [
            "£16.20",
            "£0.54",
            "£972.00",
            "£1620.00",
        ],
        "correct_index": 0,
        "why": "3.0 × (40 ÷ 60) = 2.0 kWh a day, so 60 kWh in 30 days, and 60 "
               "× 27p = 1620p = £16.20.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h02",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that a 2.0 kW heater used for 30 minutes "
                "transfers the same energy as a 500 W heater used for 2 "
                "hours. Evaluate this claim.",
        "options": [
            "Wrong — the 2.0 kW heater transfers four times as much energy",
            "Wrong — the 500 W heater transfers four times as much energy",
            "Correct — both transfer 1.0 kWh, because power × time is the "
            "same for each",
            "Correct, but only because the two heaters happen to have the "
            "same resistance value",
        ],
        "correct_index": 2,
        "why": "2.0 × 0.5 = 1.0 kWh and 0.5 × 2 = 1.0 kWh — a large power for "
               "a short time can match a small power for a long time.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h03",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electricity meter reads 42 316 kWh at the start of a "
                "month and 42 598 kWh at the end. The supplier charges a "
                "£9.00 standing charge for the month plus 26p per kWh. "
                "Calculate the total bill.",
        "options": [
            "£73.32",
            "£82.32",
            "£11 084.48",
            "£291.00",
        ],
        "correct_index": 1,
        "why": "The energy used is 42 598 − 42 316 = 282 kWh, costing 282 × "
               "26p = £73.32, plus the £9.00 standing charge.",
    },
    {
        "id": "ks4-energy-transfers-appliances-h04",
        "subtopic_slug": "energy-transfers-appliances",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A family replaces twelve 60 W filament lamps with 8 W LED "
                "lamps. The lamps are on for 4 hours a day. Determine the "
                "energy saved in a year of 365 days, in kWh.",
        "options": [
            "75.9 kWh",
            "1050 kWh",
            "911 040 kWh",
            "911 kWh",
        ],
        "correct_index": 3,
        "why": "Each lamp saves 52 W, so 12 × 0.052 × 4 = 2.496 kWh a day and "
               "2.496 × 365 ≈ 911 kWh a year.",
    },

    # ── national-grid ────────────────────────────────────────────────────
    {
        "id": "ks4-national-grid-e01",
        "subtopic_slug": "national-grid",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the order of the parts of the National Grid between a "
                "power station and a house.",
        "options": [
            "Power station → step-down transformer → high-voltage cables → "
            "step-up transformer → houses",
            "Power station → step-up transformer → high-voltage cables → "
            "step-down transformer → houses",
            "Power station → high-voltage cables → step-up transformer → "
            "step-down transformer → houses",
            "Power station → step-up transformer → step-down transformer → "
            "high-voltage cables → houses",
        ],
        "correct_index": 1,
        "why": "The voltage is stepped up before the long cables and stepped "
               "down again at a local substation before it reaches homes.",
    },
    {
        "id": "ks4-national-grid-e02",
        "subtopic_slug": "national-grid",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A transformer has more turns on its secondary coil than on "
                "its primary coil. State the effect on the potential "
                "difference.",
        "options": [
            "It is unchanged, but the current increases",
            "It is decreased",
            "It is changed from alternating to direct",
            "It is increased",
        ],
        "correct_index": 3,
        "why": "Vp ÷ Vs = np ÷ ns, so more secondary turns than primary turns "
               "gives a larger secondary potential difference — a step-up "
               "transformer.",
    },
    {
        "id": "ks4-national-grid-e03",
        "subtopic_slug": "national-grid",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student connects the primary coil of a transformer to a "
                "battery. Predict the reading on a voltmeter connected across "
                "the secondary coil.",
        "options": [
            "The same as the battery, because the coils share an iron core",
            "Half the battery value, because energy is lost in the core",
            "Zero, because a transformer only works with an alternating "
            "supply",
            "Higher than the battery, because the secondary has more turns",
        ],
        "correct_index": 2,
        "why": "A transformer needs a continually changing supply — a steady "
               "direct current produces no output at all.",
    },
    {
        "id": "ks4-national-grid-e04",
        "subtopic_slug": "national-grid",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the potential difference of the mains supply delivered "
                "to homes in the UK.",
        "options": [
            "230 V",
            "400 000 V",
            "12 V",
            "50 V",
        ],
        "correct_index": 0,
        "why": "UK mains is 230 V; the 400 kV figure belongs to the "
               "transmission cables, before the step-down transformers.",
    },
    {
        "id": "ks4-national-grid-s01",
        "subtopic_slug": "national-grid",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A substation transformer is supplied at 6900 V and has "
                "12 000 turns on its primary coil. Its output is 230 V. "
                "Calculate the number of turns on the secondary coil.",
        "options": [
            "360 000 turns",
            "30 turns",
            "4000 turns",
            "400 turns",
        ],
        "correct_index": 3,
        "why": "Vp ÷ Vs = np ÷ ns, so ns = 12 000 × (230 ÷ 6900) = 400 turns.",
    },
    {
        "id": "ks4-national-grid-s02",
        "subtopic_slug": "national-grid",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a step-down transformer at a substation "
                "increases the current even though it decreases the potential "
                "difference.",
        "options": [
            "The transformer adds energy to the circuit, so both the current "
            "and the power delivered are increased together",
            "The power delivered is almost unchanged, so if the potential "
            "difference falls the current must rise",
            "The lower potential difference lowers the resistance of the "
            "cables, so more current flows",
            "Each extra turn on the secondary coil carries its own separate "
            "current",
        ],
        "correct_index": 1,
        "why": "A transformer transfers power, it does not create it — with "
               "P = VI almost constant, a smaller V means a larger I.",
    },
    {
        "id": "ks4-national-grid-s03",
        "subtopic_slug": "national-grid",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A transmission cable has a resistance of 4.0 Ω and carries a "
                "current of 50 A. Calculate the power wasted as heat in the "
                "cable.",
        "options": [
            "10 000 W",
            "200 W",
            "40 000 W",
            "0.080 W",
        ],
        "correct_index": 0,
        "why": "P = I² × R = 50² × 4.0 = 2500 × 4.0 = 10 000 W.",
    },
    {
        "id": "ks4-national-grid-s04",
        "subtopic_slug": "national-grid",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Transmitting at a higher potential difference reduces the "
                "current in a line from 400 A to 200 A. Determine the "
                "fraction of the original power loss that remains.",
        "options": [
            "One half",
            "One eighth",
            "One quarter",
            "It is unchanged, because the power transmitted is the same",
        ],
        "correct_index": 2,
        "why": "Cable loss is I² × R, and halving the current divides the "
               "square by four.",
    },
    {
        "id": "ks4-national-grid-h01",
        "subtopic_slug": "national-grid",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station delivers 20 MW along a cable of total "
                "resistance 5.0 Ω. Compare the power wasted when the "
                "transmission potential difference is 20 kV with the power "
                "wasted at 400 kV.",
        "options": [
            "5.0 MW at 20 kV and 0.25 MW at 400 kV — the loss falls by a "
            "factor of 20",
            "5.0 MW at 20 kV and 2.5 MW at 400 kV — the loss simply halves",
            "5.0 MW at 20 kV and 0.0125 MW at 400 kV — the loss falls by a "
            "factor of 400",
            "5.0 MW at both values, because a transformer cannot change the "
            "power transmitted",
        ],
        "correct_index": 2,
        "why": "The currents are 1000 A and 50 A, so the losses are 1000² × "
               "5.0 = 5.0 MW and 50² × 5.0 = 12.5 kW — twenty times less "
               "current wastes four hundred times less power.",
    },
    {
        "id": "ks4-national-grid-h02",
        "subtopic_slug": "national-grid",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that transmitting at high potential "
                "difference 'reduces the power that has to be sent along the "
                "cables, so less is wasted'. Identify the error.",
        "options": [
            "High voltage does not reduce the power sent — it reduces the "
            "current, and the wasted power depends on the square of the "
            "current",
            "High voltage does reduce the power sent, but only because the "
            "cables become warmer",
            "High voltage increases the current, and a larger current wastes "
            "less energy",
            "High voltage reduces the resistance of the cables, and it is "
            "that lower resistance which reduces the energy wasted as heat "
            "in them",
        ],
        "correct_index": 0,
        "why": "The power that must be delivered is fixed by the customers; "
               "raising the voltage cuts the current, and the I² in I²R does "
               "the rest.",
    },
    {
        "id": "ks4-national-grid-h03",
        "subtopic_slug": "national-grid",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A transmission line carries a current of 500 A and wastes "
                "2.0 MW as heat. Determine the power wasted if the "
                "transmission potential difference is doubled while the same "
                "total power is transmitted.",
        "options": [
            "4.0 MW",
            "2.0 MW",
            "1.0 MW",
            "0.50 MW",
        ],
        "correct_index": 3,
        "why": "Doubling the potential difference halves the current to 250 A, "
               "and I² × R then gives a quarter of the loss.",
    },
    {
        "id": "ks4-national-grid-h04",
        "subtopic_slug": "national-grid",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A substation transformer steps 33 000 V down to 230 V. Its "
                "secondary coil has 460 turns. Calculate the number of turns "
                "on the primary coil.",
        "options": [
            "3.2 turns",
            "66 000 turns",
            "143 turns",
            "105 800 turns",
        ],
        "correct_index": 1,
        "why": "Vp ÷ Vs = np ÷ ns, so np = 460 × (33 000 ÷ 230) = 460 × 143.5 "
               "≈ 66 000 turns.",
    },

    # ── static-charge (TRIPLE ONLY) ──────────────────────────────────────
    {
        "id": "ks4-static-charge-e01",
        "subtopic_slug": "static-charge",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A negatively charged polythene rod is brought close to a "
                "positively charged perspex rod. State what happens.",
        "options": [
            "They repel, because both of them are charged",
            "Nothing happens, because charge cannot act across a gap",
            "They attract, because opposite charges attract",
            "They repel, because charge always spreads apart",
        ],
        "correct_index": 2,
        "why": "Opposite charges attract — the force acts across the gap "
               "without the rods touching.",
    },
    {
        "id": "ks4-static-charge-e02",
        "subtopic_slug": "static-charge",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a metal rod held in the hand cannot be given a "
                "static charge by rubbing it with a cloth.",
        "options": [
            "Metal conducts, so any charge flows away through the hand and "
            "body to earth",
            "Metal contains no electrons that are free to move",
            "Metal is already positively charged, so no further charge can be "
            "added to it by rubbing",
            "Metal atoms are too heavy for electrons to be rubbed off them",
        ],
        "correct_index": 0,
        "why": "Static charge only builds up on insulators; on a conductor it "
               "flows away as fast as it is produced.",
    },
    {
        "id": "ks4-static-charge-e03",
        "subtopic_slug": "static-charge",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the total charge when two insulating "
                "materials are rubbed together.",
        "options": [
            "It increases, because rubbing creates new charge",
            "It stays the same — the two charges are equal and opposite",
            "It decreases, because some charge is lost as heat",
            "It becomes zero, because the two charges cancel and vanish",
        ],
        "correct_index": 1,
        "why": "Charge is conserved: electrons are moved from one material to "
               "the other, so one gains exactly what the other loses.",
    },
    {
        "id": "ks4-static-charge-e04",
        "subtopic_slug": "static-charge",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which of these everyday hazards is caused by static "
                "electricity?",
        "options": [
            "A fuse blowing when too many appliances share one socket",
            "A metal appliance case becoming live when the earth wire breaks",
            "A cable overheating because its resistance is too high",
            "A spark igniting fuel vapour while a tanker is being emptied",
        ],
        "correct_index": 3,
        "why": "Fuel flowing through a pipe charges the tanker, and the spark "
               "when that charge discharges can ignite the vapour.",
    },
    {
        "id": "ks4-static-charge-s01",
        "subtopic_slug": "static-charge",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A charged plastic comb is held near a thin stream of water "
                "running from a tap, and the stream bends towards the comb. "
                "Explain why.",
        "options": [
            "The comb attracts the opposite charge that it induces on the "
            "near side of the water",
            "The water gains the same charge as the comb, and like charges "
            "attract",
            "Charge flows from the comb into the water, making the stream "
            "heavier",
            "The comb repels the air around the stream, and the moving air "
            "pushes the water sideways with it",
        ],
        "correct_index": 0,
        "why": "The charged comb separates charge within the water, pulling "
               "the nearer, oppositely charged side towards it.",
    },
    {
        "id": "ks4-static-charge-s02",
        "subtopic_slug": "static-charge",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student walks across a nylon carpet and feels a small "
                "shock on reaching for a metal door handle. Explain the "
                "shock.",
        "options": [
            "The metal handle has been storing charge from the house wiring, "
            "and all of it is released the moment a hand comes close to it",
            "The carpet warms the student's shoes, and the heat escapes "
            "through the handle",
            "Charge builds up on the student, and the strong field near the "
            "metal handle ionises the air so charge crosses as a spark",
            "The student becomes a conductor, so mains current flows from the "
            "door frame",
        ],
        "correct_index": 2,
        "why": "Friction with the carpet charges the student, and the charge "
               "discharges through the ionised air as a spark to the earthed "
               "metal.",
    },
    {
        "id": "ks4-static-charge-s03",
        "subtopic_slug": "static-charge",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a car factory the paint droplets leaving a spray gun are "
                "given a negative charge. Explain why the car panel is "
                "connected to a positive supply.",
        "options": [
            "So that the paint dries much faster, because the electric field "
            "warms the droplets while they are still in flight",
            "So that the droplets repel one another and spread out into an "
            "even cloud before landing",
            "So that the paint sticks only to the area of the panel the "
            "operator is pointing at",
            "So that the negative droplets are attracted to the panel, giving "
            "an even coat with less waste",
        ],
        "correct_index": 3,
        "why": "The oppositely charged panel attracts the droplets from every "
               "direction, so even the edges are coated and little paint is "
               "lost.",
    },
    {
        "id": "ks4-static-charge-s04",
        "subtopic_slug": "static-charge",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A positively charged rod is brought near one end of an "
                "insulated metal rod, without touching it. Describe the "
                "charge on the metal rod.",
        "options": [
            "The whole metal rod gains the same charge as the charged rod",
            "The near end becomes negative and the far end positive, but the "
            "rod stays neutral overall",
            "The whole metal rod becomes neutral, because the two kinds of "
            "charge within it cancel each other out completely",
            "Nothing changes, because charge cannot move without contact",
        ],
        "correct_index": 1,
        "why": "Free electrons in the metal are pulled towards the positive "
               "rod, separating the charge without changing the total, which "
               "is still zero.",
    },
    {
        "id": "ks4-static-charge-h01",
        "subtopic_slug": "static-charge",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two identical plastic rods are rubbed with the same cloth "
                "and then hung side by side on nylon threads. Predict what "
                "happens and explain why.",
        "options": [
            "They swing together, because both of them have been charged up "
            "by one and the same cloth",
            "They hang still, because identical objects cannot exert forces "
            "on each other",
            "They swing together first and then apart, once the charge has "
            "spread out",
            "They swing apart, because both gained the same type of charge "
            "and like charges repel",
        ],
        "correct_index": 3,
        "why": "The same cloth transfers electrons the same way to each rod, "
               "so both carry like charge and repel.",
    },
    {
        "id": "ks4-static-charge-h02",
        "subtopic_slug": "static-charge",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The drum of a laser printer is given a positive charge, and "
                "a laser removes the charge from selected parts of it. "
                "Explain how the printed image is then formed.",
        "options": [
            "Toner sticks only to the areas the laser has discharged, because "
            "those are now the only positively charged parts of the drum "
            "surface",
            "Negatively charged toner is attracted to the areas still "
            "positively charged, and is then pressed and heated onto the paper",
            "The laser burns the image straight into the paper, and the toner "
            "only colours it in",
            "Toner is repelled from every charged area and falls onto the "
            "paper in the pattern of the image",
        ],
        "correct_index": 1,
        "why": "Only the still-charged parts of the drum hold the oppositely "
               "charged toner, so those are the parts transferred and fused "
               "onto the paper.",
    },
    {
        "id": "ks4-static-charge-h03",
        "subtopic_slug": "static-charge",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Before an aircraft is refuelled, the fuel bowser and the "
                "aircraft are joined together by a metal bonding cable. "
                "Suggest why.",
        "options": [
            "The cable carries the charge produced by the flowing fuel into "
            "the aircraft's own tank, where the metal skin holds it safely",
            "The cable stops the fuel becoming charged as it flows through "
            "the hose",
            "The cable holds both at the same potential, so charge cannot "
            "build up between them and spark near the fuel vapour",
            "The cable earths the aircraft so that lightning cannot strike it "
            "on the ground",
        ],
        "correct_index": 2,
        "why": "Fuel flowing through a hose charges the metalwork, and bonding "
               "removes the potential difference that a spark would otherwise "
               "jump across.",
    },
    {
        "id": "ks4-static-charge-h04",
        "subtopic_slug": "static-charge",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A negatively charged rod is held near an uncharged aluminium "
                "can lying on its side on a bench, and the can rolls towards "
                "the rod. A student concludes that the can must already have "
                "carried a charge. Evaluate this conclusion.",
        "options": [
            "It is wrong — the rod pushes electrons to the far end of the "
            "can, leaving the near end positive, so the can is attracted "
            "while staying neutral overall",
            "It is right — only an object that already carries a charge of "
            "its own can be attracted by another charged object, so the can "
            "must have been charged before the rod arrived",
            "It is wrong — the charged rod warms the air on one side of the "
            "can, and the moving air is what nudges it along the bench",
            "It is right, but the can must have carried a positive charge "
            "rather than a negative one",
        ],
        "correct_index": 0,
        "why": "Attraction never proves an object is charged: a charged rod "
               "induces a charge separation in any nearby conductor, and the "
               "closer, opposite end is pulled towards it.",
    },

    # ── electric-fields (TRIPLE ONLY) ────────────────────────────────────
    {
        "id": "ks4-electric-fields-e01",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Define an electric field.",
        "options": [
            "A region in which a magnet experiences a turning force",
            "The path an electron follows when it leaves a charged object",
            "The energy stored by a charged object",
            "A region in which a charged object experiences a force",
        ],
        "correct_index": 3,
        "why": "An electric field is the region around a charge where another "
               "charge feels a force, without the two ever touching.",
    },
    {
        "id": "ks4-electric-fields-e02",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what it means when electric field lines are drawn "
                "closer together in one region.",
        "options": [
            "The field is weaker there",
            "Any charge there is moving faster",
            "The field is stronger there",
            "The field changes direction there",
        ],
        "correct_index": 2,
        "why": "Line spacing shows field strength — closer lines mean a "
               "stronger field and a larger force on a given charge.",
    },
    {
        "id": "ks4-electric-fields-e03",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one rule that electric field lines always obey.",
        "options": [
            "Field lines never cross one another",
            "Field lines always form closed loops",
            "Field lines are always the same distance apart",
            "Field lines always point towards the nearest positive charge",
        ],
        "correct_index": 0,
        "why": "Crossing lines would give a charge two different force "
               "directions at the same point, which is impossible.",
    },
    {
        "id": "ks4-electric-fields-e04",
        "subtopic_slug": "electric-fields",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the unit of electric field strength.",
        "options": [
            "newtons per metre, N/m",
            "newtons per coulomb, N/C",
            "coulombs per newton, C/N",
            "joules per coulomb, J/C",
        ],
        "correct_index": 1,
        "why": "Electric field strength is force per unit charge, E = F ÷ q, "
               "so its unit is newtons per coulomb.",
    },
    {
        "id": "ks4-electric-fields-s01",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A small positive charge is moved from a point close to the "
                "positive plate to a point close to the negative plate of a "
                "pair of parallel charged plates. Describe how the force on "
                "the charge changes as it moves.",
        "options": [
            "The force increases steadily as the charge gets nearer to the "
            "negative plate",
            "The force decreases steadily as the charge moves further from "
            "the positive plate",
            "The force stays the same, because the field between parallel "
            "plates is uniform",
            "The force falls to zero halfway across, where the fields of the "
            "two plates cancel",
        ],
        "correct_index": 2,
        "why": "A uniform field has equally spaced field lines, so the force "
               "on a given charge is the same at every point between the "
               "plates.",
    },
    {
        "id": "ks4-electric-fields-s02",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A charge of 0.0020 C experiences a force of 0.30 N in an "
                "electric field. Calculate the electric field strength.",
        "options": [
            "0.0067 N/C",
            "0.00060 N/C",
            "15 N/C",
            "150 N/C",
        ],
        "correct_index": 3,
        "why": "E = F ÷ q = 0.30 ÷ 0.0020 = 150 N/C.",
    },
    {
        "id": "ks4-electric-fields-s03",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An electron is placed in a uniform electric field that "
                "points from left to right. State the direction of the force "
                "on the electron.",
        "options": [
            "From left to right, along the direction of the field",
            "From right to left, opposite to the direction of the field",
            "There is no force, because an electron carries no charge",
            "At right angles to the field",
        ],
        "correct_index": 1,
        "why": "Field lines give the force on a positive charge, so a negative "
               "electron is pushed the opposite way.",
    },
    {
        "id": "ks4-electric-fields-s04",
        "subtopic_slug": "electric-fields",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The electric field strength at a point is 5000 N/C. "
                "Calculate the force on a charge of 3.0 × 10⁻⁶ C placed "
                "there.",
        "options": [
            "0.015 N",
            "1.7 × 10⁹ N",
            "6.0 × 10⁻¹⁰ N",
            "5000 N",
        ],
        "correct_index": 0,
        "why": "E = F ÷ q rearranges to F = E × q = 5000 × 3.0 × 10⁻⁶ = "
               "0.015 N.",
    },
    {
        "id": "ks4-electric-fields-h01",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A highly charged metal dome is brought near an earthed metal "
                "sphere and a spark jumps the gap. Explain how charge crosses "
                "a gap of air, which is normally an insulator.",
        "options": [
            "The charge heats the air until it melts and becomes a conductor",
            "The very strong field ionises the air, and the ions and "
            "electrons released allow it to conduct",
            "The air is pushed out of the gap, and the charge crosses the "
            "vacuum left behind",
            "Air is always a slightly weak conductor, so charge simply leaks "
            "across the gap whenever two objects are close together",
        ],
        "correct_index": 1,
        "why": "A strong enough field strips electrons from air molecules, and "
               "the ionised air conducts until the charge has discharged.",
    },
    {
        "id": "ks4-electric-fields-h02",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student states that the electric field around a point "
                "charge has the same strength at every distance from it, "
                "'because the charge itself does not change'. Identify the "
                "error.",
        "options": [
            "The field lines spread apart as the distance increases, so the "
            "field becomes weaker",
            "The field really is the same strength everywhere, so the student "
            "is correct",
            "The field becomes stronger with distance, because the lines have "
            "further to travel",
            "The field exists only at the surface of the charge, so it has no "
            "strength further away",
        ],
        "correct_index": 0,
        "why": "The same lines are spread over an ever larger area as you move "
               "away, and wider spacing means a weaker field.",
    },
    {
        "id": "ks4-electric-fields-h03",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A positive point charge and an equal negative point charge "
                "are placed a short distance apart. Compare the field at the "
                "midpoint between them with the field a long way from both.",
        "options": [
            "The field is zero at the midpoint, because the field from each "
            "charge exactly cancels the field from the other one there",
            "The field is the same at both places, because the charges are "
            "equal in size",
            "The field is weaker at the midpoint, because the lines are "
            "furthest apart there",
            "The field is much stronger at the midpoint, because lines from "
            "both charges are crowded into that region",
        ],
        "correct_index": 3,
        "why": "Between opposite charges both fields point the same way, so "
               "they add and the lines bunch together — a cancelling "
               "neutral point occurs between LIKE charges, not opposite ones.",
    },
    {
        "id": "ks4-electric-fields-h04",
        "subtopic_slug": "electric-fields",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A charged dust particle of charge 4.0 × 10⁻⁹ C is held "
                "stationary in a uniform electric field. The weight of the "
                "particle is 6.0 × 10⁻⁶ N. Determine the electric field "
                "strength.",
        "options": [
            "2.4 × 10⁻¹⁴ N/C",
            "6.7 × 10⁻⁴ N/C",
            "1500 N/C",
            "150 N/C",
        ],
        "correct_index": 2,
        "why": "The particle is stationary, so the electric force balances the "
               "weight: E = F ÷ q = 6.0 × 10⁻⁶ ÷ 4.0 × 10⁻⁹ = 1500 N/C.",
    },
]
