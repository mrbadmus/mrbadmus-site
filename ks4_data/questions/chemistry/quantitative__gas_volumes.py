"""Chemistry · Quantitative chemistry — the assignment pool for `gas-volumes`.

AQA 8462 4.3.5, Chemistry only, Higher only: equal amounts in moles of gases
occupy the same volume at the same temperature and pressure; one mole of any
gas at room temperature and pressure (20 °C, 1 atmosphere) occupies 24 dm³;
gas volumes from a balanced equation; a volume from a mass and Mr; changing
the subject of the equation.

The distractors are built from the errors: dividing by 24 where the amount
should be multiplied (and the other way round), 24 divided by the amount,
cm³ used where dm³ is needed, a volume in dm³ labelled cm³, a mole ratio
missed or turned upside down, a liquid product counted as a gas, the
balancing number of the wrong substance, Ar used where Mr is needed.

Filed as ks4_data/questions/chemistry/quantitative__gas_volumes.py. The first
four of each band are bank positions 0-11 (load_pool assigns them; the
comment on each row says which). correct_index is three each of 0, 1, 2, 3,
and no credited option is the longest of its four.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {   # bank_position 0
        "id": "ks4-gas-volumes-e01",
        "subtopic_slug": "gas-volumes",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Two sealed flasks at room temperature and pressure each hold "
                "0.5 mol of gas. One holds argon (Ar 40) and the other holds "
                "ammonia (Mr 17). Compare the volumes of the two gases.",
        "options": [
            "The argon has the larger volume, as its atoms are heavier",
            "The ammonia has the larger volume, as its molecules are lighter",
            "The two gases occupy the same volume as each other",
            "The ammonia has the larger volume, as each molecule has 4 atoms",
        ],
        "correct_index": 2,
        "why": "Equal amounts in moles of gases occupy the same volume at the "
               "same temperature and pressure, whatever the gas.",
    },
    {   # bank_position 1
        "id": "ks4-gas-volumes-e02",
        "subtopic_slug": "gas-volumes",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Give the volume, in cm³, of one mole of any gas at room "
                "temperature and pressure.",
        "options": [
            "24 cm³",
            "24 000 cm³",
            "2400 cm³",
            "240 000 cm³",
        ],
        "correct_index": 1,
        "why": "One mole occupies 24 dm³, and 1 dm³ = 1000 cm³, so "
               "24 × 1000 = 24 000 cm³.",
    },
    {   # bank_position 2
        "id": "ks4-gas-volumes-e03",
        "subtopic_slug": "gas-volumes",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A sample of gas at room temperature and pressure has a volume "
                "of 6 dm³. The amount of gas in moles is tripled, at the same "
                "temperature and pressure. State the new volume.",
        "options": [
            "2 dm³",
            "6 dm³",
            "0.25 dm³",
            "18 dm³",
        ],
        "correct_index": 3,
        "why": "Volume is proportional to the amount in moles, so three times "
               "the moles takes up three times the volume: 6 × 3 = 18 dm³.",
    },
    {   # bank_position 3
        "id": "ks4-gas-volumes-e04",
        "subtopic_slug": "gas-volumes",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A weather balloon is filled with 30 dm³ of helium at room "
                "temperature and pressure. Calculate the amount of helium in "
                "moles.",
        "options": [
            "1.25 mol",
            "720 mol",
            "0.800 mol",
            "1.34 mol",
        ],
        "correct_index": 0,
        "why": "Amount = volume ÷ 24 = 30 ÷ 24 = 1.25 mol.",
    },
    # ── standard ────────────────────────────────────────────────────────
    {   # bank_position 4
        "id": "ks4-gas-volumes-s01",
        "subtopic_slug": "gas-volumes",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Calculate the mass of nitrogen gas, N2, that occupies 1.8 dm³ "
                "at room temperature and pressure. Mr of N2 = 28.",
        "options": [
            "50.4 g",
            "2.1 g",
            "0.075 g",
            "1.05 g",
        ],
        "correct_index": 1,
        "why": "Amount = 1.8 ÷ 24 = 0.075 mol. Mass = amount × Mr = "
               "0.075 × 28 = 2.1 g.",
    },
    {   # bank_position 5
        "id": "ks4-gas-volumes-s02",
        "subtopic_slug": "gas-volumes",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Hydrogen burns in chlorine: H2(g) + Cl2(g) → 2HCl(g). "
                "Calculate the volume of hydrogen chloride made when 75 cm³ of "
                "hydrogen reacts completely. All volumes are measured at room "
                "temperature and pressure.",
        "options": [
            "75 cm³",
            "37.5 cm³",
            "1800 cm³",
            "150 cm³",
        ],
        "correct_index": 3,
        "why": "The ratio H2 : HCl is 1 : 2, and gas volumes are in the same "
               "ratio as moles: 75 × 2 ÷ 1 = 150 cm³.",
    },
    {   # bank_position 6
        "id": "ks4-gas-volumes-s03",
        "subtopic_slug": "gas-volumes",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Ammonia is made from its elements: N2(g) + 3H2(g) → 2NH3(g). "
                "Calculate the volume of nitrogen needed to make 0.6 dm³ of "
                "ammonia. Give your answer in cm³. All volumes are measured "
                "at room temperature and pressure.",
        "options": [
            "300 cm³",
            "0.3 cm³",
            "1200 cm³",
            "200 cm³",
        ],
        "correct_index": 0,
        "why": "N2 : NH3 is 1 : 2, and gas volumes are in the same ratio as "
               "moles: 0.6 × 1 ÷ 2 = 0.3 dm³. Multiply by 1000: 300 cm³.",
    },
    {   # bank_position 7
        "id": "ks4-gas-volumes-s04",
        "subtopic_slug": "gas-volumes",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "At room temperature and pressure, 1 dm³ of sulfur dioxide, "
                "SO2 (Mr 64), and 1 dm³ of oxygen, O2 (Mr 32), are weighed. "
                "Explain how their masses compare.",
        "options": [
            "Equal masses, as the two volumes are the same",
            "The oxygen is heavier, as it holds twice the moles",
            "The SO2 is twice as heavy, as both hold equal moles",
            "The SO2 is heavier, as its molecules take more space",
        ],
        "correct_index": 2,
        "why": "Equal volumes of gases at the same temperature and pressure "
               "hold equal amounts in moles, so the gas with the larger Mr "
               "has the larger mass: 64 ÷ 32 = 2 times.",
    },
    # ── harder ──────────────────────────────────────────────────────────
    {   # bank_position 8
        "id": "ks4-gas-volumes-h01",
        "subtopic_slug": "gas-volumes",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Calcium reacts with water: Ca + 2H2O → Ca(OH)2 + H2. "
                "Calculate the volume of hydrogen, at room temperature and "
                "pressure, made when 1.2 g of calcium reacts. Ar of Ca = 40.",
        "options": [
            "1.44 dm³",
            "0.030 dm³",
            "0.0013 dm³",
            "0.72 dm³",
        ],
        "correct_index": 3,
        "why": "Amount of Ca = 1.2 ÷ 40 = 0.030 mol. Ca : H2 is 1 : 1, so "
               "0.030 mol of H2. Volume = 0.030 × 24 = 0.72 dm³.",
    },
    {   # bank_position 9
        "id": "ks4-gas-volumes-h02",
        "subtopic_slug": "gas-volumes",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "10 cm³ of propane is burned completely in 100 cm³ of oxygen: "
                "C3H8(g) + 5O2(g) → 3CO2(g) + 4H2O(l). All volumes are measured "
                "at room temperature and pressure. Determine the total volume "
                "of gas left at the end.",
        "options": [
            "30 cm³",
            "80 cm³",
            "120 cm³",
            "110 cm³",
        ],
        "correct_index": 1,
        "why": "The propane uses 10 × 5 = 50 cm³ of oxygen, leaving 50 cm³. "
               "It makes 10 × 3 = 30 cm³ of CO2. Water is a liquid at room "
               "temperature, so the gas left is 50 + 30 = 80 cm³.",
    },
    {   # bank_position 10
        "id": "ks4-gas-volumes-h03",
        "subtopic_slug": "gas-volumes",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A 0.80 g sample of a gas occupies 600 cm³ at room "
                "temperature and pressure. Calculate the relative formula mass "
                "(Mr) of the gas.",
        "options": [
            "19.2",
            "3.2",
            "32",
            "750",
        ],
        "correct_index": 2,
        "why": "600 cm³ = 0.600 dm³, so the amount is 0.600 ÷ 24 = 0.025 mol. "
               "Mr = mass ÷ amount = 0.80 ÷ 0.025 = 32.",
    },
    {   # bank_position 11
        "id": "ks4-gas-volumes-h04",
        "subtopic_slug": "gas-volumes",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Aluminium reacts with acid: 2Al + 6HCl → 2AlCl3 + 3H2. A "
                "student finds the volume of hydrogen made from 0.10 mol of "
                "aluminium at room temperature and pressure by writing "
                "0.10 × 24 = 2.4 dm³. Identify the student's error.",
        "options": [
            "The 2 : 3 ratio is missed, so it is 3.6 dm³",
            "It should divide by 24, so it is 0.0042 dm³",
            "It should use the 6 for HCl, so it is 14.4 dm³",
            "There is no error, so 2.4 dm³ is the right answer",
        ],
        "correct_index": 0,
        "why": "Al : H2 is 2 : 3, so 0.10 mol of Al makes 0.10 × 3 ÷ 2 = "
               "0.15 mol of H2. Volume = 0.15 × 24 = 3.6 dm³.",
    },
]
