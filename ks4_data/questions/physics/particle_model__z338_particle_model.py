"""Physics · Particle model (6.3) — the MRB-338 expansion.

Six BASE subtopics — density of materials, changes of state, internal
energy, temperature changes and specific heat capacity, specific latent
heat, and particle motion and pressure — all foundation, all Combined and
Triple. Coverage widens outward from the curriculum data's own key notes and
common mistakes: named real materials and their densities, the required
practicals (RP17, RP14) and the errors that actually happen in them, the
factors that change a rate (evaporation) or a reading (pressure, density),
comparison and evaluation of everyday scenarios, and rearranged or
multi-step calculations built from clean numbers. Every calculation keeps
its working in the `why` field, never in an option, and every conceptual
option is written to the same level of detail as its neighbours so that
length alone answers nothing.
"""

TOPIC = "particle-model"
SUBJECT = "physics"

QUESTIONS = [
    # ── density-of-materials ────────────────────────────────────────────
    {
        "id": "ks4-density-of-materials-e05",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the equation used to calculate density.",
        "options": [
            "ρ = m ÷ V",
            "ρ = V ÷ m",
            "ρ = m × V",
            "ρ = m + V",
        ],
        "correct_index": 0,
        "why": "Density is mass divided by volume, so ρ = m ÷ V; the other three "
                "options invert or misuse the operation.",
    },
    {
        "id": "ks4-density-of-materials-e06",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the density of pure water, used as a reference value for "
                "many other materials.",
        "options": [
            "100 kg/m³",
            "1000 kg/m³",
            "10 000 kg/m³",
            "1 kg/m³",
        ],
        "correct_index": 1,
        "why": "Water's density is one of the standard reference values in GCSE "
                "Physics: 1000 kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-e07",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rock sample has a mass of 9.0 g and a density of 3.0 g/cm³. "
                "Calculate its volume.",
        "options": [
            "0.33 cm³",
            "27 cm³",
            "3.0 cm³",
            "12 cm³",
        ],
        "correct_index": 2,
        "why": "Rearranging ρ = m ÷ V gives V = m ÷ ρ = 9.0 ÷ 3.0 = 3.0 cm³.",
    },
    {
        "id": "ks4-density-of-materials-e08",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A liquid has a density of 800 kg/m³. Calculate the mass of 0.20 "
                "m³ of the liquid.",
        "options": [
            "4000 kg",
            "800.2 kg",
            "0.00025 kg",
            "160 kg",
        ],
        "correct_index": 3,
        "why": "m = ρ × V = 800 × 0.20 = 160 kg.",
    },
    {
        "id": "ks4-density-of-materials-e09",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the piece of apparatus used to measure the volume of a "
                "liquid in the required practical for density.",
        "options": [
            "A measuring cylinder",
            "A newtonmeter balance",
            "A metre ruler",
            "A set of vernier callipers",
        ],
        "correct_index": 0,
        "why": "A measuring cylinder gives the volume of a liquid directly, in "
                "cm³.",
    },
    {
        "id": "ks4-density-of-materials-e10",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State an instrument that could be used to measure the dimensions "
                "of a regular solid before calculating its density.",
        "options": [
            "A measuring cylinder for liquids",
            "A pair of vernier callipers",
            "A thermometer",
            "A newtonmeter",
        ],
        "correct_index": 1,
        "why": "Vernier callipers (or a ruler or micrometer) measure the length, "
                "width and height needed to calculate volume.",
    },
    {
        "id": "ks4-density-of-materials-e11",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Gold has a density of about 19 300 kg/m³ and aluminium about "
                "2700 kg/m³. State which is the denser material.",
        "options": [
            "Aluminium, because it has the smaller volume",
            "Neither — density cannot be compared between two different "
            "materials",
            "Gold, because it has the greater density",
            "Aluminium, because it has the greater mass",
        ],
        "correct_index": 2,
        "why": "The material with the higher density value, gold, is the denser "
                "one.",
    },
    {
        "id": "ks4-density-of-materials-e12",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Convert a volume of 5 cm³ into m³.",
        "options": [
            "5 × 10⁻³ m³",
            "5 × 10³ m³",
            "5 × 10⁻⁹ m³",
            "5 × 10⁻⁶ m³",
        ],
        "correct_index": 3,
        "why": "1 cm³ = 1 × 10⁻⁶ m³, so 5 cm³ = 5 × 10⁻⁶ m³.",
    },
    {
        "id": "ks4-density-of-materials-s06",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cylindrical rod has a radius of 2.0 cm and a length of 10 cm, "
                "and a mass of 252 g. Using V = πr²h (π ≈ 3.14), calculate its "
                "density in g/cm³.",
        "options": [
            "2.0 g/cm³",
            "6.3 g/cm³",
            "0.50 g/cm³",
            "8.0 g/cm³",
        ],
        "correct_index": 0,
        "why": "V = πr²h = 3.14 × 2.0² × 10 = 126 cm³, so ρ = m ÷ V = 252 ÷ 126 "
                "= 2.0 g/cm³.",
    },
    {
        "id": "ks4-density-of-materials-s07",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three blocks have equal volume: block P has density 700 kg/m³, "
                "block Q has density 2500 kg/m³, and block R has density 1100 "
                "kg/m³. Rank the blocks from lightest to heaviest.",
        "options": [
            "R, P, Q",
            "P, R, Q",
            "Q, R, P",
            "P, Q, R",
        ],
        "correct_index": 1,
        "why": "Equal volume means the block with the lowest density has the "
                "least mass, so the order by mass matches the order by density: "
                "P, then R, then Q.",
    },
    {
        "id": "ks4-density-of-materials-s08",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates the density of an unknown metal block as "
                "8900 kg/m³. Using the values silver = 10 500 kg/m³, copper = "
                "8900 kg/m³, and zinc = 7100 kg/m³, identify the metal.",
        "options": [
            "Silver, because its density is closest to the measured value",
            "Zinc, because all metals round to a similar density",
            "Copper, because its density matches the measured value exactly",
            "None of them, because the measured value must be wrong",
        ],
        "correct_index": 2,
        "why": "8900 kg/m³ matches copper's known density exactly, so the block "
                "is copper.",
    },
    {
        "id": "ks4-density-of-materials-s09",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical, a student reads the water level in a "
                "measuring cylinder from above rather than at eye level with the "
                "meniscus. Explain the effect of this parallax error on the "
                "calculated density.",
        "options": [
            "The reading is unaffected, because parallax error only affects mass "
            "readings, not volumes",
            "The density will definitely come out too high, because reading from "
            "above makes the liquid look as though it fills less of the cylinder than "
            "it really does",
            "The density will definitely come out too low, because reading from above "
            "makes the liquid look as though it fills more of the cylinder than it "
            "really does",
            "The volume reading may be too high or too low, so the calculated "
            "density becomes inaccurate",
        ],
        "correct_index": 3,
        "why": "Parallax error means the meniscus is read from the wrong angle, "
                "so the volume recorded is not the true volume — the density "
                "calculated from it is therefore also inaccurate.",
    },
    {
        "id": "ks4-density-of-materials-s10",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grain of a mineral has a volume of 0.50 cm³ and a density of "
                "5.0 g/cm³. Calculate its mass in milligrams.",
        "options": [
            "2500 mg",
            "250 mg",
            "0.0025 mg",
            "25 mg",
        ],
        "correct_index": 0,
        "why": "m = ρ × V = 5.0 × 0.50 = 2.5 g, and 2.5 g = 2500 mg.",
    },
    {
        "id": "ks4-density-of-materials-s11",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical, a student places an empty measuring "
                "cylinder on a balance and zeroes it before pouring in a liquid. "
                "Explain why this step is necessary.",
        "options": [
            "So the measuring cylinder does not break under the weight of the "
            "liquid",
            "So the cylinder's own mass is not included when the mass of the "
            "liquid is read off",
            "So the density of the liquid can be read directly from the "
            "balance display without any calculation",
            "So the liquid does not evaporate away while it is being weighed on the "
            "balance",
        ],
        "correct_index": 1,
        "why": "Zeroing subtracts the empty cylinder's mass, so the balance then "
                "shows only the mass of the liquid added.",
    },
    {
        "id": "ks4-density-of-materials-s12",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas has a density of 1.2 kg/m³. Determine its density in "
                "g/cm³.",
        "options": [
            "1200 g/cm³",
            "0.12 g/cm³",
            "0.0012 g/cm³",
            "12 g/cm³",
        ],
        "correct_index": 2,
        "why": "1 kg/m³ is 0.001 g/cm³, so dividing by 1000 gives 1.2 ÷ 1000 = "
                "0.0012 g/cm³.",
    },
    {
        "id": "ks4-density-of-materials-s13",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical-sized boxes have the same volume. Box X has a mass "
                "of 4.0 kg and box Y has a mass of 12 kg. Compare their "
                "densities.",
        "options": [
            "Box X has three times the density of box Y",
            "The two boxes have equal density, because they have equal volume",
            "Box Y has one third the density of box X",
            "Box Y has three times the density of box X",
        ],
        "correct_index": 3,
        "why": "Equal volume means density is proportional to mass, and box Y "
                "has three times the mass of box X.",
    },
    {
        "id": "ks4-density-of-materials-s14",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cooking oil has a density of 920 kg/m³. A plastic block has a "
                "density of 950 kg/m³. Predict what happens when the block is "
                "placed in the oil, and separately in water (1000 kg/m³).",
        "options": [
            "It sinks in the oil, because 950 kg/m³ is greater than 920 "
            "kg/m³, but floats in the water, because 950 kg/m³ is less than "
            "1000 kg/m³",
            "It floats in both liquids, because plastic is always less dense "
            "than any liquid",
            "It sinks in both liquids, because its density is greater than "
            "both 920 kg/m³ and 1000 kg/m³, so neither liquid could ever "
            "support it",
            "It floats in the oil but sinks in the water, because oil is less "
            "dense than water",
        ],
        "correct_index": 0,
        "why": "An object sinks when its density is greater than the fluid's and "
                "floats when it is less; 950 kg/m³ sits between the two given "
                "densities.",
    },
    {
        "id": "ks4-density-of-materials-s15",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A small brass key has a mass of 68 g. When lowered into a "
                "measuring cylinder, the water level rises from 60 cm³ to 68 cm³. "
                "Calculate the density of the key.",
        "options": [
            "0.12 g/cm³",
            "8.5 g/cm³",
            "1.0 g/cm³",
            "544 g/cm³",
        ],
        "correct_index": 1,
        "why": "The key's volume is the rise in level, 68 − 60 = 8 cm³, so ρ = m "
                "÷ V = 68 ÷ 8 = 8.5 g/cm³.",
    },
    {
        "id": "ks4-density-of-materials-s16",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Vegetable oil (920 kg/m³), water (1000 kg/m³) and golden syrup "
                "(1400 kg/m³) are poured into the same container and left to "
                "settle. Predict the order of the layers from top to bottom.",
        "options": [
            "Water, oil, syrup",
            "Syrup, water, oil",
            "Oil, water, syrup",
            "Oil, syrup, water",
        ],
        "correct_index": 2,
        "why": "The least dense liquid rises to the top and the most dense sinks "
                "to the bottom, so the order is oil, then water, then syrup.",
    },
    {
        "id": "ks4-density-of-materials-s17",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the displacement method is used to find the volume "
                "of an irregularly shaped stone, rather than measuring its "
                "dimensions with a ruler.",
        "options": [
            "A ruler cannot touch stone, because stone is too hard for a "
            "ruler to measure",
            "The displacement method is always more accurate than a ruler, whatever "
            "shape the object happens to be",
            "A stone has no volume until it is placed in a liquid, so a ruler "
            "could never measure it, not before it touches the water",
            "An irregular shape has no simple formula for volume, so its "
            "dimensions cannot be used in a volume equation",
        ],
        "correct_index": 3,
        "why": "Volume formulae like V = l × w × h only work for regular shapes; "
                "an irregular stone has no such formula, so displacement is used "
                "instead.",
    },
    {
        "id": "ks4-density-of-materials-s18",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates a density using a mass measured in grams "
                "and a volume measured in cm³. State the correct unit for the "
                "answer.",
        "options": [
            "g/cm³",
            "kg/m³",
            "kg/cm³",
            "g/m³",
        ],
        "correct_index": 0,
        "why": "Dividing a mass in grams by a volume in cm³ gives an answer in "
                "grams per cubic centimetre, g/cm³.",
    },
    {
        "id": "ks4-density-of-materials-s19",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Solid candle wax has a density of about 900 kg/m³. When melted, "
                "liquid wax has a density of about 850 kg/m³. Explain why the "
                "density falls on melting.",
        "options": [
            "The wax particles lose mass as they melt, so the same volume has "
            "a lower density during the process",
            "The particles move slightly further apart in the liquid, so the "
            "same mass occupies a greater volume",
            "The number of wax particles decreases as it melts, lowering the "
            "total mass",
            "Melting always increases density, so this measurement must be an "
            "error",
        ],
        "correct_index": 1,
        "why": "Melting usually spreads the particles slightly further apart "
                "without changing their mass or number, so a given mass takes up "
                "more volume and the density falls.",
    },
    {
        "id": "ks4-density-of-materials-s20",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hollow steel boat has an overall volume of 4.0 m³, including "
                "the air inside its hull, and a mass of 3200 kg. Steel itself has "
                "a density of 7800 kg/m³. Determine whether the boat floats in "
                "water (1000 kg/m³), using its average density.",
        "options": [
            "It sinks, because steel's density of 7800 kg/m³ is far greater "
            "than water's",
            "It floats, because all boats are designed to float regardless of "
            "the material",
            "It floats, because its average density, 800 kg/m³, is less than "
            "water's 1000 kg/m³",
            "It sinks, because its average density, 800 kg/m³, still counts "
            "as denser than water",
        ],
        "correct_index": 2,
        "why": "Average density uses the whole hull volume including the "
                "enclosed air: 3200 ÷ 4.0 = 800 kg/m³, less than water's density, "
                "so it floats.",
    },
    {
        "id": "ks4-density-of-materials-s21",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the density of ice, liquid water and steam, all at their "
                "respective transition temperatures.",
        "options": [
            "Steam is the densest, because its particles move the fastest and so "
            "press together most tightly inside a given space",
            "Ice is the densest, followed by steam, then liquid water",
            "All three have the same density, because they are made of exactly the "
            "same substance throughout",
            "Liquid water is the densest, ice is slightly less dense, and "
            "steam is far less dense than both",
        ],
        "correct_index": 3,
        "why": "Water is an unusual solid — it is slightly less dense than its "
                "liquid — but steam's particles are spread so far apart that it "
                "is far less dense than either.",
    },
    {
        "id": "ks4-density-of-materials-s22",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student weighs an empty measuring cylinder, then weighs it "
                "again after adding 40 cm³ of a liquid; the mass reading rises by "
                "36 g. Calculate the density of the liquid.",
        "options": [
            "0.90 g/cm³",
            "1440 g/cm³",
            "4.0 g/cm³",
            "1.1 g/cm³",
        ],
        "correct_index": 0,
        "why": "The rise in the balance reading, 36 g, is the mass of the liquid "
                "alone, so ρ = m ÷ V = 36 ÷ 40 = 0.90 g/cm³.",
    },
    {
        "id": "ks4-density-of-materials-s23",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cube of expanded polystyrene has a density far lower than a "
                "solid block of the plastic it is made from. Explain why, in "
                "terms of the particle model.",
        "options": [
            "The polystyrene particles themselves are far lighter than in the "
            "solid plastic",
            "The foam contains many pockets of trapped air, so the same outer "
            "volume contains far less plastic mass",
            "Foaming the plastic destroys some of its particles, lowering its "
            "total mass",
            "Foamed plastic is a different chemical substance from solid "
            "plastic, with its own lower density, entirely",
        ],
        "correct_index": 1,
        "why": "The trapped air pockets take up space without adding mass, so "
                "the same outer volume of foam has far less plastic in it than a "
                "solid block.",
    },
    {
        "id": "ks4-density-of-materials-s24",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A recipe states a cake tin should hold 1.2 kg of batter with a "
                "density of 1200 kg/m³. Calculate the volume of batter needed, in "
                "m³.",
        "options": [
            "1440 m³",
            "0.0010 m³",
            "1.0 m³",
            "1000 m³",
        ],
        "correct_index": 1,
        "why": "V = m ÷ ρ = 1.2 ÷ 1200 = 0.0010 m³.",
    },
    {
        "id": "ks4-density-of-materials-s25",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A measuring cylinder holds 30 cm³ of water. A metal ball is "
                "lowered in and the level rises to 42 cm³. The ball has a mass of "
                "94.8 g. Determine the metal, given lead = 11.3 g/cm³ and iron = "
                "7.9 g/cm³.",
        "options": [
            "Iron, because 94.8 ÷ 42 = 2.3 g/cm³ is closest to iron",
            "Lead, because a ball heavy enough to read 94.8 g on the balance must be "
            "the denser of the two metals",
            "Iron, because 94.8 ÷ 12 = 7.9 g/cm³ matches iron exactly",
            "Lead, because 94.8 ÷ 12 = 7.9 g/cm³, which is closer to lead "
            "than to iron",
        ],
        "correct_index": 2,
        "why": "The volume is 42 − 30 = 12 cm³, so ρ = 94.8 ÷ 12 = 7.9 g/cm³, "
                "which matches iron.",
    },
    {
        "id": "ks4-density-of-materials-s26",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a scientist trying to identify an unknown pure solid "
                "would find its density more useful than its mass alone.",
        "options": [
            "Mass is not a real physical property of a substance, but density "
            "is",
            "Density is a fixed property of the material, whatever the size "
            "of the sample, while mass changes with the sample size",
            "Density cannot be measured accurately, so mass is always "
            "preferred instead",
            "Mass and density are actually the same quantity, just with "
            "different units, so they always give identical numbers",
        ],
        "correct_index": 1,
        "why": "A bigger sample of the same substance has more mass but the same "
                "density, so density identifies the material while mass alone "
                "does not.",
    },
    {
        "id": "ks4-density-of-materials-h06",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A metal bar measures 25 mm by 40 mm by 300 mm and has a mass of "
                "2.4 kg. Calculate its density in kg/m³.",
        "options": [
            "80 kg/m³",
            "8000 kg/m³",
            "800 kg/m³",
            "8 000 000 kg/m³",
        ],
        "correct_index": 1,
        "why": "Converting mm to m gives 0.025 × 0.040 × 0.300 = 3.0 × 10⁻⁴ m³, "
                "so ρ = 2.4 ÷ 3.0 × 10⁻⁴ = 8000 kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-h07",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Gold has a density of 19 300 kg/m³. A jeweller needs exactly "
                "38.6 g of gold for a ring. Calculate the volume of gold "
                "required, in cm³.",
        "options": [
            "0.20 cm³",
            "20 cm³",
            "2.0 cm³",
            "772 cm³",
        ],
        "correct_index": 2,
        "why": "In g/cm³, gold's density is 19.3 g/cm³, so V = m ÷ ρ = 38.6 ÷ "
                "19.3 = 2.0 cm³.",
    },
    {
        "id": "ks4-density-of-materials-h08",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student uses the displacement method to find the density of a "
                "porous rock that has tiny air pockets throughout it. Evaluate "
                "the effect this has on the calculated density, compared with the "
                "true density of the solid rock material.",
        "options": [
            "The calculated density is too high, because the air pockets add "
            "extra mass to the rock",
            "The calculated density exactly equals the true density, because "
            "air has no effect on volume measurements, in every case, without "
            "exception",
            "The calculated density is too high, because trapped air makes the rock "
            "float higher in the measuring cylinder",
            "The calculated density is too low, because the measured volume "
            "includes the air pockets as well as the solid rock",
        ],
        "correct_index": 3,
        "why": "The displacement measures the total volume the rock pushes out "
                "of the way, including its trapped air, so dividing the true mass "
                "by this larger volume gives too low a density.",
    },
    {
        "id": "ks4-density-of-materials-h09",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student weighs an irregular metal sample as 156 g. When "
                "lowered into a measuring cylinder, the water level rises from 40 "
                "cm³ to 60 cm³. Using the values iron = 7.8 g/cm³ and lead = 11.3 "
                "g/cm³, identify the metal.",
        "options": [
            "Iron, because the calculated density of 7.8 g/cm³ matches iron "
            "exactly",
            "Lead, because the calculated density of 11.3 g/cm³ matches lead "
            "exactly",
            "Neither, because the calculated density, found using the final 40 cm³ "
            "reading as the volume, comes to 3.9 g/cm³ and matches neither metal",
            "Iron, because the calculated density of 15.6 g/cm³ is closest to "
            "iron's value doubled",
        ],
        "correct_index": 0,
        "why": "The volume is 60 − 40 = 20 cm³, so ρ = 156 ÷ 20 = 7.8 g/cm³, "
                "exactly matching iron.",
    },
    {
        "id": "ks4-density-of-materials-h10",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lead ball and an aluminium ball have equal mass. Lead has a "
                "density of 11 300 kg/m³ and aluminium 2700 kg/m³. Compare the "
                "volumes of the two balls, to two significant figures.",
        "options": [
            "The lead ball has about 4.2 times the volume of the aluminium "
            "ball",
            "The aluminium ball has about 4.2 times the volume of the lead "
            "ball",
            "The two balls have equal volume, because their mass is the same",
            "The aluminium ball has about 0.24 times the volume of the lead "
            "ball",
        ],
        "correct_index": 1,
        "why": "For equal mass, volume is inversely proportional to density, so "
                "the less dense aluminium occupies about 11 300 ÷ 2700 ≈ 4.2 "
                "times the volume of the lead.",
    },
    {
        "id": "ks4-density-of-materials-h11",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student tries to find the density of a block of pine wood by "
                "lowering it into a measuring cylinder of water, but the wood "
                "floats and will not fully submerge. Explain the problem this "
                "causes for the displacement method.",
        "options": [
            "There is no problem — the rise in water level still gives the "
            "true volume of the wood, however much of it stays above the "
            "surface",
            "The method fails because a block of pine wood is far too light to "
            "register properly on any laboratory balance at all",
            "The rise in water level gives only the volume of the submerged "
            "part, not the whole block, so the volume is underestimated",
            "The method fails because floating objects have no fixed volume",
        ],
        "correct_index": 2,
        "why": "Only the submerged part of the wood displaces water, so the "
                "level rise underestimates the block's true volume unless it is "
                "pushed fully under.",
    },
    {
        "id": "ks4-density-of-materials-h12",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates: 'mass = 45 g, volume = 15 cm³, so density "
                "= volume ÷ mass = 15 ÷ 45 = 0.33 g/cm³.' Identify the error in "
                "this working.",
        "options": [
            "There is no error — the answer 0.33 g/cm³ is correct",
            "The error is in the mass value, which should have been converted "
            "to kilograms first, not the operation used",
            "The error is in the volume value, which should have been "
            "converted to m³ first",
            "The equation has been inverted — density is mass divided by "
            "volume, ρ = m ÷ V, not volume divided by mass",
        ],
        "correct_index": 3,
        "why": "Density is defined as mass per unit volume, so the calculation "
                "should be 45 ÷ 15 = 3.0 g/cm³, not volume divided by mass.",
    },
    {
        "id": "ks4-density-of-materials-h13",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "200 cm³ of a liquid of density 800 kg/m³ is mixed with 300 cm³ "
                "of a liquid of density 1300 kg/m³, with no change in total "
                "volume. Calculate the density of the mixture.",
        "options": [
            "1100 kg/m³",
            "1050 kg/m³",
            "2100 kg/m³",
            "550 kg/m³",
        ],
        "correct_index": 0,
        "why": "The total mass is (200 × 0.8) + (300 × 1.3) = 160 + 390 = 550 g "
                "in 500 cm³, giving 1.1 g/cm³, which is 1100 kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-h14",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A material has a density of 0.0079 g/mm³. Convert this density "
                "into kg/m³.",
        "options": [
            "0.0079 kg/m³",
            "7900 kg/m³",
            "7 900 000 kg/m³",
            "7.9 kg/m³",
        ],
        "correct_index": 1,
        "why": "1 mm³ = 1 × 10⁻⁹ m³, so 0.0079 g/mm³ = 0.0079 ÷ (1 × 10⁻⁹) g/m³ "
                "= 7.9 × 10⁶ g/m³, which is 7900 kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-h15",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims: 'If I double both the mass and the volume of a "
                "block, its density doubles too.' Evaluate this claim.",
        "options": [
            "The claim is correct, because density depends on both mass and "
            "volume",
            "The claim is correct, because doubling the mass always doubles "
            "the density",
            "The claim is incorrect — doubling both mass and volume leaves "
            "the ratio, and so the density, unchanged",
            "The claim is incorrect — doubling both mass and volume actually "
            "halves the density, not doubles it",
        ],
        "correct_index": 2,
        "why": "Density is mass divided by volume; doubling both the top and "
                "bottom of that ratio leaves the ratio the same, so the density "
                "does not change.",
    },
    {
        "id": "ks4-density-of-materials-h16",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed capsule has a total volume of 0.50 m³. Determine the "
                "greatest mass it can have and still not sink in water (density "
                "1000 kg/m³).",
        "options": [
            "5000 kg",
            "0.50 kg",
            "2000 kg",
            "500 kg",
        ],
        "correct_index": 3,
        "why": "The capsule does not sink as long as its average density does "
                "not exceed water's, so the greatest mass is m = ρ × V = 1000 × "
                "0.50 = 500 kg.",
    },
    {
        "id": "ks4-density-of-materials-h17",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student repeats the density practical on the same regular "
                "block five times and gets very consistent results, but every "
                "value is about 8% higher than the manufacturer's stated density. "
                "Suggest the most likely explanation.",
        "options": [
            "A systematic error, such as a balance that always reads slightly "
            "high, rather than random mistakes in reading the ruler",
            "Random error in reading the ruler, because the results are very "
            "close together",
            "The manufacturer's stated density must be wrong, because the student's "
            "five results agree so closely with each other",
            "The block must have changed density between each of the five repeats, "
            "since handling and warming a metal block alters how tightly its "
            "particles sit together",
        ],
        "correct_index": 0,
        "why": "Consistent results all offset in the same direction point to a "
                "systematic error, such as a balance with a zero error, rather "
                "than random measurement mistakes.",
    },
    {
        "id": "ks4-density-of-materials-h18",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alloy is made by combining 20 cm³ of copper (mass 178 g) with "
                "30 cm³ of tin (mass 219 g), and the volumes simply add together. "
                "Calculate the density of the alloy, to 2 significant figures.",
        "options": [
            "8.9 g/cm³",
            "7.9 g/cm³",
            "8.1 g/cm³",
            "19.9 g/cm³",
        ],
        "correct_index": 1,
        "why": "The total mass is 178 + 219 = 397 g and the total volume is 20 + "
                "30 = 50 cm³, so ρ = 397 ÷ 50 = 7.9 g/cm³ to 2 s.f.",
    },
    {
        "id": "ks4-density-of-materials-h19",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solid aluminium cube and a second aluminium cube of the same outer "
                "size, but with a spherical cavity hollowed out at its centre, are "
                "compared. Explain which cube has the lower average density.",
        "options": [
            "The solid cube, because it contains more aluminium atoms packed into the "
            "same outer volume",
            "Neither — both cubes have the same density, since they are made of the "
            "same metal",
            "The cube with the cavity, because the same outer volume now "
            "contains less mass",
            "The cube with the cavity, because drilling a hole increases the "
            "volume of the aluminium",
        ],
        "correct_index": 2,
        "why": "Average density uses the whole outer volume; removing material "
                "to leave a cavity keeps the volume the same but lowers the mass, "
                "so the average density falls.",
    },
    {
        "id": "ks4-density-of-materials-h20",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A small plastic marble is placed in a beaker of oil. It neither "
                "rises to the surface nor sinks to the bottom, but hovers "
                "motionless in the middle of the liquid. State what this shows "
                "about the marble and the oil.",
        "options": [
            "The marble has a greater density than the oil",
            "The marble has a lower density than the oil",
            "The marble has no measurable density at all",
            "The marble and the oil have equal density",
        ],
        "correct_index": 3,
        "why": "An object sinks if it is denser than the fluid and floats up if "
                "it is less dense; hovering with no net movement means the two "
                "densities are equal.",
    },
    {
        "id": "ks4-density-of-materials-h21",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A metal block has a volume of 200 cm³ at room temperature and a "
                "mass of 1600 g. When heated, its volume expands to 202 cm³ while "
                "its mass stays the same. Calculate the percentage change in its "
                "density.",
        "options": [
            "A decrease of about 1.0%",
            "An increase of about 1.0%",
            "A decrease of about 1.0 g/cm³",
            "No change, because mass is conserved when a solid is heated",
        ],
        "correct_index": 0,
        "why": "The mass stays the same but the volume rises slightly, from 8.0 "
                "g/cm³ to about 7.92 g/cm³, a fall of about 1.0%.",
    },
    {
        "id": "ks4-density-of-materials-h22",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Block A (density 600 kg/m³) and block B (density 900 kg/m³) are "
                "identical in size and both float in water. Compare how much of "
                "each block sits above the water's surface.",
        "options": [
            "Block B floats higher, because its density is closer to the water's, and "
            "the closer those two densities are the less of the block has to sit "
            "below the surface",
            "Block A floats higher, because its lower density means less of "
            "it needs to be underwater to displace enough water to support it",
            "Both float at exactly the same height, because any block with a density "
            "lower than water's floats fully on the surface of it",
            "Block A floats lower, because a lower density means a smaller "
            "floating object",
        ],
        "correct_index": 1,
        "why": "A floating object sinks in only as far as needed to displace its "
                "own weight of water; the less dense block A needs to displace "
                "less water, so more of it stays above the surface.",
    },
    {
        "id": "ks4-density-of-materials-h23",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A container holds 3.5 litres of a liquid with a mass of 3.85 kg. "
                "Calculate the density of the liquid in kg/m³. (1 litre = 1 × "
                "10⁻³ m³)",
        "options": [
            "11 kg/m³",
            "110 kg/m³",
            "1100 kg/m³",
            "11 000 kg/m³",
        ],
        "correct_index": 2,
        "why": "3.5 litres is 3.5 × 10⁻³ m³, so ρ = 3.85 ÷ (3.5 × 10⁻³) = 1100 "
                "kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-h24",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students measure the volume of the same irregularly shaped "
                "pebble: one estimates it using a ruler and an assumed shape, the "
                "other uses the displacement method. Their answers disagree by "
                "40%. Evaluate which result should be trusted more, and why.",
        "options": [
            "The ruler estimate, because ruler measurements are always more "
            "precise than reading a scale on a cylinder, especially for a "
            "smooth, regular shape",
            "Neither, because volume cannot be measured reliably for any "
            "solid object",
            "Both equally, because a 40% disagreement means both methods are "
            "equally unreliable",
            "The displacement result, because a ruler cannot capture the true "
            "shape of an irregular pebble, while displacement measures its "
            "actual volume directly",
        ],
        "correct_index": 3,
        "why": "A ruler-and-formula estimate assumes a regular shape the pebble "
                "does not have, so it is only ever a rough guess; displacement "
                "measures the true volume regardless of shape.",
    },
    {
        "id": "ks4-density-of-materials-h25",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An iceberg has a density of 917 kg/m³ and floats in seawater of "
                "density 1025 kg/m³. Estimate what fraction of the iceberg's "
                "volume is above the surface of the water.",
        "options": [
            "About 10%, because roughly 90% must be submerged to displace "
            "enough seawater to support the iceberg",
            "About 90%, because most of a floating object is usually seen "
            "above the surface",
            "About 50%, because a floating object is always half in and half "
            "out of the water",
            "About 1%, because ice is so close in density to water that "
            "almost none of it can be above the surface",
        ],
        "correct_index": 0,
        "why": "The submerged fraction equals the ratio of the densities, 917 ÷ "
                "1025 ≈ 0.90, so about 90% is submerged and about 10% remains "
                "above the surface.",
    },
    {
        "id": "ks4-density-of-materials-h26",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A balloon is filled with helium (density about 0.18 kg/m³) "
                "surrounded by air (density about 1.2 kg/m³). A student claims "
                "the balloon rises because helium is 'lighter than nothing'. "
                "Evaluate this claim using density.",
        "options": [
            "The claim is correct, because helium genuinely has no mass at all, so "
            "there is nothing at all for gravity to pull downward on",
            "The claim is incorrect — the balloon rises because helium is far "
            "less dense than the surrounding air, not because it has no mass",
            "The claim is correct, because gases always rise regardless of their "
            "density, since a gas has no real weight of its own to hold it down "
            "against the air",
            "The claim is incorrect — the balloon actually rises due to a "
            "chemical reaction between helium and air",
        ],
        "correct_index": 1,
        "why": "Helium does have mass and a measurable density; it rises because "
                "that density is much lower than air's, in the same way that a "
                "less dense object floats in a denser liquid.",
    },
    # ── changes-of-state ────────────────────────────────────────────────
    {
        "id": "ks4-changes-of-state-e05",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the change of state in which a liquid turns into a solid.",
        "options": [
            "Freezing",
            "Melting",
            "Evaporation",
            "Deposition",
        ],
        "correct_index": 0,
        "why": "Liquid to solid is freezing; melting is the reverse change.",
    },
    {
        "id": "ks4-changes-of-state-e06",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the change of state in which a solid turns into a liquid.",
        "options": [
            "Freezing",
            "Melting",
            "Condensation",
            "Sublimation",
        ],
        "correct_index": 1,
        "why": "Solid to liquid is melting, caused by supplying energy to the "
                "substance.",
    },
    {
        "id": "ks4-changes-of-state-e07",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether energy is absorbed from or released to the "
                "surroundings when a gas condenses.",
        "options": [
            "Absorbed from the surroundings",
            "Neither — condensation involves no energy transfer",
            "Released to the surroundings",
            "Both, in equal amounts, so there is no overall change",
        ],
        "correct_index": 2,
        "why": "Condensing particles are pulled together by intermolecular "
                "forces, and forming those bonds releases energy.",
    },
    {
        "id": "ks4-changes-of-state-e08",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether energy is absorbed from or released to the "
                "surroundings when a solid melts.",
        "options": [
            "Released to the surroundings",
            "Neither — melting involves no energy transfer",
            "It depends entirely on the substance being melted",
            "Absorbed from the surroundings",
        ],
        "correct_index": 3,
        "why": "Melting breaks the forces holding particles in a fixed lattice, "
                "and breaking those forces needs energy from the surroundings.",
    },
    {
        "id": "ks4-changes-of-state-e09",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a very cold, clear night, a thin white layer of ice forms "
                "directly on a car windscreen with no liquid water seen forming "
                "first. Name this change of state.",
        "options": [
            "Deposition",
            "Freezing",
            "Evaporation",
            "Condensation",
        ],
        "correct_index": 0,
        "why": "Deposition is the direct gas-to-solid change, which can happen "
                "when water vapour meets a surface cold enough to skip the liquid "
                "stage.",
    },
    {
        "id": "ks4-changes-of-state-e10",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Small droplets of water form on the outside of a cold drinks can "
                "on a warm day. Name this change of state.",
        "options": [
            "Evaporation",
            "Condensation",
            "Sublimation",
            "Melting",
        ],
        "correct_index": 1,
        "why": "Water vapour in the warm air is cooled by the can and condenses "
                "into liquid droplets on its surface.",
    },
    {
        "id": "ks4-changes-of-state-e11",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the general rule for whether a change can be reversed.",
        "options": [
            "Chemical changes can be reversed; physical changes usually "
            "cannot",
            "All changes to a substance can always be reversed",
            "Physical changes can be reversed; chemical changes usually "
            "cannot",
            "No changes to a substance can ever be reversed",
        ],
        "correct_index": 2,
        "why": "A physical change keeps the same substance throughout, so it can "
                "be reversed; a chemical change usually makes a new substance "
                "that cannot easily be turned back.",
    },
    {
        "id": "ks4-changes-of-state-e12",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sugar dissolves completely into water, and the water can later "
                "be evaporated away to leave the sugar behind unchanged. State "
                "whether dissolving sugar is a physical or a chemical change.",
        "options": [
            "Chemical, because the sugar disappears from view",
            "Chemical, because a new liquid, sugar solution, is formed",
            "Physical, but only because sugar is a food, not a chemical",
            "Physical, because the sugar can be recovered unchanged",
        ],
        "correct_index": 3,
        "why": "No new substance is formed and the sugar can be got back "
                "unchanged, so dissolving is a physical change.",
    },
    {
        "id": "ks4-changes-of-state-s06",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An egg is cracked into a hot pan and its clear liquid turns "
                "white and firm. It cannot be turned back into clear liquid egg "
                "by cooling it. Explain whether cooking an egg is a physical or a "
                "chemical change.",
        "options": [
            "Chemical, because the proteins in the egg are permanently "
            "rearranged into a new substance that cannot be reversed",
            "Physical, because no new substance forms — the egg white simply stiffens "
            "as its water is driven off by the heat",
            "Physical, because cooking only involves a change of state, like "
            "melting",
            "Chemical, but only because heat was involved in the change, since any "
            "change brought about by a flame or a hot pan counts as a chemical one",
        ],
        "correct_index": 0,
        "why": "The proteins in the egg white are permanently changed into a new "
                "arrangement — cooking makes a new substance, and the change "
                "cannot be reversed by cooling.",
    },
    {
        "id": "ks4-changes-of-state-s07",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An iron nail left outside develops a flaky orange layer of rust "
                "over several weeks. Explain whether rusting is a physical or a "
                "chemical change.",
        "options": [
            "Physical, because the iron just changes its arrangement of "
            "particles, like freezing, not into a genuinely new substance",
            "Chemical, because iron reacts with oxygen and water to form a "
            "new substance, and cannot turn back into iron by itself",
            "Physical, because rust can be scraped off to reveal iron "
            "underneath, which anyone could check just by looking at the "
            "surface",
            "Chemical, but only because the nail is exposed to the weather",
        ],
        "correct_index": 1,
        "why": "Rust is a new substance, iron oxide, formed by a reaction with "
                "oxygen and water — it will not turn back into iron on its own, "
                "so this is a chemical change.",
    },
    {
        "id": "ks4-changes-of-state-s08",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bar of chocolate is melted in a warm kitchen and then left in "
                "a fridge, where it sets solid again. Explain whether melting the "
                "chocolate is a physical or a chemical change.",
        "options": [
            "Chemical, because the chocolate changes from a solid to a liquid",
            "Chemical, because the melted chocolate looks and tastes completely "
            "different from the solid bar it was cut from",
            "Physical, because the chocolate is still the same substance "
            "throughout, and the change can be reversed by cooling",
            "Physical, but only because chocolate contains sugar, and a substance "
            "made mainly of sugar can never take part in a chemical change",
        ],
        "correct_index": 2,
        "why": "No new substance is formed, and cooling turns the liquid "
                "chocolate back into a solid, so melting it is a physical change.",
    },
    {
        "id": "ks4-changes-of-state-s09",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Water is boiled to steam, the steam is then condensed back to "
                "liquid water, and the water is finally frozen into ice. Explain "
                "whether the substance could, in principle, be taken back through "
                "every step to steam again.",
        "options": [
            "No — once water has been frozen solid into ice it can never be boiled "
            "back into steam again",
            "No — boiling and freezing are chemical changes, so neither can "
            "be reversed, since heating and cooling cannot act on a chemical "
            "change at all",
            "Yes, but only the freezing step can be reversed; boiling and condensing "
            "drive the water permanently into the air",
            "Yes — every step is a physical change, so heating and cooling "
            "can reverse the whole sequence",
        ],
        "correct_index": 3,
        "why": "Boiling, condensing and freezing are all physical changes to the "
                "same substance, so supplying or removing energy can take it back "
                "through every step.",
    },
    {
        "id": "ks4-changes-of-state-s10",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shallow puddle on a playground disappears much faster on a hot "
                "day than on a cool day, even though it never reaches 100 °C. "
                "Explain this difference in terms of particles.",
        "options": [
            "On a hot day, a larger fraction of the surface particles have "
            "enough energy to escape into the air",
            "Hot air pushes down harder on the puddle, squeezing the water out of it "
            "and down into the ground beneath",
            "The puddle must be reaching 100 °C on the hot day without the student "
            "realising it has done so",
            "Heat makes the water particles heavier, so they sink into the "
            "ground faster",
        ],
        "correct_index": 0,
        "why": "Higher temperature gives more surface particles enough energy to "
                "break free as vapour, so evaporation speeds up well below the "
                "boiling point.",
    },
    {
        "id": "ks4-changes-of-state-s11",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The same volume of water is poured into a wide, shallow tray "
                "and, separately, into a tall, narrow glass. Explain which will "
                "evaporate away faster.",
        "options": [
            "The glass, because a taller column of water holds more energy",
            "The tray, because its much larger surface area lets more "
            "particles escape at once",
            "Neither — the same volume always evaporates at the same rate "
            "whatever the container",
            "The glass, because a narrow container traps more heat",
        ],
        "correct_index": 1,
        "why": "Evaporation happens at the surface, so spreading the same water "
                "over a larger surface area lets far more particles escape per "
                "second.",
    },
    {
        "id": "ks4-changes-of-state-s12",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fan is pointed at a wet floor to help it dry. Explain why "
                "moving air over a liquid's surface increases its rate of "
                "evaporation.",
        "options": [
            "The moving air pushes the liquid particles physically off the "
            "floor",
            "Moving air raises the temperature of the floor, so more "
            "particles escape, by transferring its own thermal energy "
            "directly into the water as it blows across",
            "The moving air carries escaped particles away, stopping them "
            "from returning to the liquid and keeping the air above the "
            "surface able to take more",
            "Moving air compresses the liquid, forcing particles out of the "
            "surface, which is really the same thing as blowing the liquid "
            "away as a spray",
        ],
        "correct_index": 2,
        "why": "Without a draught, escaped particles can drift back into the "
                "liquid; a draught sweeps them away, so evaporation can continue "
                "at a higher rate.",
    },
    {
        "id": "ks4-changes-of-state-s13",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Washing on a line dries much more slowly on a damp, humid day "
                "than on a dry day at the same temperature. Explain why.",
        "options": [
            "Humid air is colder than dry air, which slows the evaporation of "
            "the water in the washing, even on an otherwise identical day",
            "Humid air actively pushes water vapour back into the washing faster than "
            "the washing itself can release it",
            "Humidity has no real effect on evaporation, only wind and "
            "temperature do, whatever the humidity happens to be doing on any "
            "given day",
            "Humid air already contains a lot of water vapour, so it can take "
            "up far less extra vapour from the washing",
        ],
        "correct_index": 3,
        "why": "Air already close to saturated with water vapour can absorb far "
                "less more, so particles escaping from the washing have a harder "
                "time getting away into it.",
    },
    {
        "id": "ks4-changes-of-state-s14",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A block of solid carbon dioxide (dry ice) can either be left to "
                "sublime directly into gas, or, under different conditions, made "
                "to melt into liquid and then boil into gas. Compare the total "
                "mass of gas produced by the two different routes, starting from "
                "the same mass of solid.",
        "options": [
            "The two routes produce exactly the same mass of gas, because no "
            "particles are created or destroyed by either route",
            "Sublimation produces less gas, because some mass is lost as it "
            "skips the liquid stage, which simply vanishes into the "
            "surroundings",
            "Melting and boiling produces less gas, because energy is used up in the "
            "extra step and some of the liquid stays behind",
            "The two routes cannot be compared, because they are different "
            "changes of state",
        ],
        "correct_index": 0,
        "why": "Whichever route is taken, no particles are created or destroyed "
                "in a change of state, so the same starting mass of solid ends up "
                "as the same mass of gas.",
    },
    {
        "id": "ks4-changes-of-state-s15",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a cold morning, a garden shows patches of liquid dew on some "
                "leaves and white, crystalline frost on others. Explain the "
                "difference between these two effects.",
        "options": [
            "Dew and frost are the same thing, just given different names depending "
            "on how cold the morning air happens to feel to a gardener outside",
            "Dew forms when water vapour condenses into liquid; frost forms "
            "when water vapour deposits directly as a solid on a surface cold "
            "enough",
            "Dew forms only in the morning and frost only at night, "
            "regardless of temperature, whatever the weather conditions "
            "happen to be doing that day",
            "Frost is simply dew that has been left for longer to dry out",
        ],
        "correct_index": 1,
        "why": "Both start as water vapour in the air; on a surface above 0 °C "
                "it condenses to liquid dew, but on a colder surface it deposits "
                "straight into solid frost.",
    },
    {
        "id": "ks4-changes-of-state-s16",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student looks closely at a boiling kettle and notices there is "
                "a small gap of clear space right at the spout before the visible "
                "white cloud appears. Explain what this shows about the visible "
                "cloud.",
        "options": [
            "The visible cloud is pure steam, and the clear gap is simply the air in "
            "front of the spout being pushed out of the way by the steam first",
            "The visible cloud is smoke from the heating element, not related to the "
            "water at all, since the element burns off a little of its own coating "
            "each time the kettle is switched on",
            "The visible cloud is water vapour cooling and condensing back into tiny "
            "liquid droplets, while the true steam near the spout is invisible",
            "The clear gap shows that the kettle has not reached its boiling "
            "point yet",
        ],
        "correct_index": 2,
        "why": "Water vapour itself is invisible; the white cloud is made of "
                "tiny droplets that form once the hot gas has cooled and "
                "condensed slightly in the air.",
    },
    {
        "id": "ks4-changes-of-state-s17",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed plastic bag containing 250 g of crushed ice is left on a "
                "table until the ice has completely melted. Predict the mass of the "
                "bag and its contents after melting.",
        "options": [
            "Slightly less than before, because some water always evaporates "
            "during melting, even from inside a fully sealed bag",
            "Slightly more than before, because liquid water is denser than ice, and "
            "a denser substance always weighs more",
            "Impossible to predict without knowing the temperature of the room the "
            "bag was left in all day",
            "The same as before, because melting creates and destroys no "
            "particles inside the sealed bag",
        ],
        "correct_index": 3,
        "why": "The bag is sealed, so no particles enter or leave; melting only "
                "rearranges the particles already there, so the total mass is "
                "unchanged.",
    },
    {
        "id": "ks4-changes-of-state-s18",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why energy is transferred to the surroundings whether "
                "water vapour condenses directly into ice (deposition) or first "
                "condenses into liquid water and then freezes.",
        "options": [
            "Both routes end with the particles held more closely together "
            "than they started, in a gas, so both must release energy to the "
            "surroundings",
            "Only the direct deposition route releases energy; the two-step "
            "route absorbs energy overall, taking in energy at every stage "
            "instead of giving it out",
            "Neither route releases energy, because both start and finish with "
            "exactly the same water particles held in exactly the same way at the end",
            "Only the two-step route releases energy; deposition absorbs "
            "energy instead",
        ],
        "correct_index": 0,
        "why": "Whichever path is taken, the particles finish far more ordered "
                "and closely bound than a gas, so energy must leave the substance "
                "either way.",
    },
    {
        "id": "ks4-changes-of-state-s20",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify each of the following as either absorbing energy or "
                "releasing energy: melting, freezing, evaporation, and "
                "condensation.",
        "options": [
            "Melting and freezing absorb energy; evaporation and condensation "
            "release energy",
            "All four absorb energy, because a change of state always needs "
            "energy supplied",
            "Melting and evaporation absorb energy; freezing and condensation "
            "release energy",
            "Melting and condensation absorb energy; freezing and evaporation "
            "release energy",
        ],
        "correct_index": 2,
        "why": "Melting and evaporation move particles further apart against "
                "intermolecular forces, needing energy in; freezing and "
                "condensation pull particles together, releasing energy out.",
    },
    {
        "id": "ks4-changes-of-state-s21",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Burning a piece of toast until it turns black cannot be undone, "
                "but freezing a loaf of bread and then thawing it leaves the "
                "bread unchanged. Compare these two processes.",
        "options": [
            "Both are chemical changes, but burning happens faster than freezing, "
            "since a flame drives the same reaction that a freezer drives very slowly",
            "Both are physical changes, but burning removes water from the bread "
            "while freezing simply locks that water in place",
            "Freezing is the chemical change, because it needs a freezer, "
            "while burning is physical",
            "Burning is a chemical change that forms new substances and "
            "cannot be reversed; freezing is a physical change that can",
        ],
        "correct_index": 3,
        "why": "Burning produces new substances such as carbon, which cannot be "
                "turned back into bread, while freezing only changes the "
                "arrangement of the same particles.",
    },
    {
        "id": "ks4-changes-of-state-s22",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An open bottle of perfume left on a shelf gradually loses liquid "
                "over several weeks at room temperature, well below its boiling "
                "point. Explain how this is possible.",
        "options": [
            "Some of the fastest-moving surface particles have enough energy to "
            "escape into the air at any temperature, not only at the boiling point",
            "The perfume must actually be boiling very slowly at room temperature, "
            "because a liquid that keeps disappearing can only be doing so by boiling "
            "away",
            "The perfume must be soaking into the wooden shelf beneath the bottle "
            "over the weeks, rather than any change of state occurring at all",
            "Room temperature air chemically reacts with the perfume, destroying a "
            "little more of it each day",
        ],
        "correct_index": 0,
        "why": "Evaporation happens whenever the most energetic surface "
                "particles can escape, which occurs at any temperature, not just "
                "at the boiling point.",
    },
    {
        "id": "ks4-changes-of-state-s23",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bowl of soup left on a table for an hour cools down and is "
                "later found to weigh very slightly less, even though it never "
                "boiled. Explain this small loss of mass.",
        "options": [
            "Mass has genuinely been destroyed as the soup cooled down",
            "A small amount of water vapour has evaporated from the open "
            "surface and escaped into the room's air",
            "The bowl itself has lost mass as it cooled, since a cooling solid gives "
            "up some of its material",
            "Cooling a liquid always reduces its total mass slightly, in "
            "every situation, whether or not any surface is exposed to air",
        ],
        "correct_index": 1,
        "why": "In an open container, evaporated particles leave the bowl for "
                "the surrounding air, so the mass measured on the bowl alone "
                "appears to fall — no mass has actually been destroyed.",
    },
    {
        "id": "ks4-changes-of-state-s24",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what happens to the spacing of the particles and to the "
                "forces between them when a solid sublimes directly into a gas.",
        "options": [
            "The spacing decreases and the forces between the particles "
            "strengthen",
            "Neither the spacing nor the forces change during sublimation, "
            "only the particles' speed changes",
            "The spacing increases hugely and the intermolecular forces are "
            "almost completely overcome",
            "The spacing stays the same but the forces between the particles "
            "disappear completely",
        ],
        "correct_index": 2,
        "why": "Sublimation takes particles from a tightly packed lattice "
                "straight to a widely spaced gas, so the spacing grows enormously "
                "and almost all of the intermolecular forces are overcome.",
    },
    {
        "id": "ks4-changes-of-state-s25",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student observes that ice always melts at 0 °C and that liquid "
                "water always freezes at 0 °C. Explain why these are the same "
                "temperature rather than two different values.",
        "options": [
            "It is a coincidence for water, but not true for most other "
            "substances",
            "Melting and freezing are actually different changes with no fixed "
            "relationship between their temperatures, and each substance sets the two "
            "independently",
            "Freezing happens at 0 °C, but melting only happens once the "
            "temperature is above 0 °C",
            "0 °C is simply the temperature at which the energy supplied is "
            "exactly enough to hold the solid and liquid arrangements in "
            "balance, in either direction",
        ],
        "correct_index": 3,
        "why": "The melting point and freezing point of a pure substance are the "
                "same temperature — the point at which the solid and liquid "
                "arrangements are equally balanced.",
    },
    {
        "id": "ks4-changes-of-state-s26",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A used tea bag is squeezed out and left to dry on a plate, and "
                "dries out fully within a day even though the room is never "
                "heated above normal room temperature. Explain what change of "
                "state is occurring, and why no boiling is needed.",
        "options": [
            "Evaporation, because the fastest water particles can always "
            "escape from a wet surface, whatever the temperature",
            "Sublimation, because the water left in the squeezed tea bag turns "
            "directly from a solid into a gas as it dries",
            "Condensation, because water vapour in the room is being drawn "
            "onto the tea bag",
            "Boiling, because all water eventually reaches its boiling point "
            "if left long enough, however cool the room happens to be kept",
        ],
        "correct_index": 0,
        "why": "The water in the tea bag is a liquid, and the most energetic "
                "surface particles can always escape into the air as vapour, "
                "regardless of the room's temperature.",
    },
    {
        "id": "ks4-changes-of-state-h06",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hiker notices that water boils at a lower temperature at the "
                "top of a high mountain than at sea level. Suggest what this "
                "shows about the effect of air pressure on boiling point.",
        "options": [
            "Lower air pressure raises the boiling point, so the water on the "
            "mountain must be boiling away at a temperature well above the usual 100 "
            "°C",
            "Lower air pressure lowers the boiling point, so particles can "
            "escape into the gas phase more easily against less resistance "
            "from the air above",
            "Air pressure has no effect on boiling point; only altitude itself "
            "changes it, because the thinner air high up lets the water's particles "
            "spread out more freely",
            "The water is not really boiling at all, only appearing to "
            "because of the thinner air",
        ],
        "correct_index": 1,
        "why": "At lower pressure there is less resistance from the air above "
                "the liquid's surface, so particles can escape into the gas phase "
                "at a lower temperature.",
    },
    {
        "id": "ks4-changes-of-state-h07",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed pressure cooker allows food to cook faster than an "
                "ordinary open saucepan of boiling water. Explain how raising the "
                "pressure inside the pot helps achieve this.",
        "options": [
            "Higher pressure inside the pot lowers the boiling point, so the water "
            "boils away faster and carries more energy into the food as steam",
            "The sealed lid simply traps more steam, which has no effect on "
            "the temperature reached, regardless of what temperature the "
            "water inside eventually reaches",
            "Higher pressure inside the pot raises the boiling point of "
            "water, so the water can reach a higher temperature before it "
            "boils away",
            "Pressure cookers work by chemically changing the food faster, "
            "not by changing any boiling point",
        ],
        "correct_index": 2,
        "why": "Raising the pressure makes it harder for particles to escape "
                "into the gas phase, so a higher temperature is needed before the "
                "water boils, cooking food faster.",
    },
    {
        "id": "ks4-changes-of-state-h08",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical ice cubes are left in the same warm room, but one "
                "has first been crushed into small chips. Predict which will "
                "finish melting first, and explain why.",
        "options": [
            "The whole cube, because a single large lump holds energy more "
            "efficiently than many small pieces, losing far less of it to the "
            "surrounding air",
            "Both melt in exactly the same time, because they contain the same total "
            "mass of ice at the same starting temperature",
            "The whole cube, because crushing ice raises its melting point "
            "above 0 °C",
            "The crushed ice, because its much greater surface area lets "
            "energy transfer into it from the warm air more quickly",
        ],
        "correct_index": 3,
        "why": "Melting is driven by energy transferred in from the surroundings "
                "across the ice's surface, so the crushed ice, with far more "
                "surface area exposed, melts faster.",
    },
    {
        "id": "ks4-changes-of-state-h09",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that sublimation of a substance always needs "
                "at least as much energy as melting the same mass of that "
                "substance.",
        "options": [
            "The claim is true — sublimation must free the particles from "
            "their lattice and then separate them completely into a gas, both "
            "of which take energy",
            "The claim is false — sublimation always needs less energy, "
            "because it skips the liquid stage entirely, so it should always "
            "be the quicker and cheaper process",
            "The claim is false — melting and sublimation always need exactly "
            "the same amount of energy, since both changes ultimately end "
            "with particles fully separated as a gas",
            "The claim cannot be evaluated without knowing the substance's "
            "temperature and the pressure it is under at the moment that the energy "
            "is supplied to it",
        ],
        "correct_index": 0,
        "why": "Melting only frees particles from fixed positions; sublimation "
                "must do that and then also fully separate them into a gas, so it "
                "needs at least as much energy.",
    },
    {
        "id": "ks4-changes-of-state-h10",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student states: 'Boiling and evaporation are really the same "
                "process, just happening at different speeds.' Evaluate this "
                "statement.",
        "options": [
            "The statement is correct — both happen throughout the liquid and "
            "at any temperature, only the rate differs",
            "The statement is incorrect — evaporation happens at the surface "
            "at any temperature, while boiling happens throughout the liquid "
            "only at its fixed boiling point, producing bubbles of gas",
            "The statement is correct — both only ever happen at exactly 100 "
            "°C, just at different rates of bubbling",
            "The statement is incorrect — evaporation is a chemical change while "
            "boiling is a physical change, because evaporating water splits into new "
            "gases while boiling water stays water throughout",
        ],
        "correct_index": 1,
        "why": "Evaporation is a surface-only process that can occur at any "
                "temperature, while boiling occurs throughout the liquid, only at "
                "a fixed temperature, producing visible bubbles.",
    },
    {
        "id": "ks4-changes-of-state-h11",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Equal puddles of water and of methylated spirit are left side by "
                "side in the same room. The spirit disappears far faster than the "
                "water. Suggest what this shows about the intermolecular forces "
                "in the two liquids.",
        "options": [
            "The spirit has stronger intermolecular forces between its particles, "
            "which is why it evaporates so much faster than the water beside it",
            "Intermolecular forces have no connection to how quickly a liquid "
            "evaporates",
            "The spirit's particles are held together by weaker "
            "intermolecular forces, so more of them can escape into the gas "
            "phase in a given time",
            "The spirit is simply hotter than the water, which is the only "
            "reason it evaporates faster, regardless of anything about their "
            "particles or forces",
        ],
        "correct_index": 2,
        "why": "A liquid with weaker forces between its particles lets more of "
                "them break free at a given temperature, so it evaporates faster "
                "than one with stronger forces.",
    },
    {
        "id": "ks4-changes-of-state-h12",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims: 'A change of state can never be reversed once "
                "the spacing of the particles has changed.' Evaluate this claim, "
                "using freezing liquid water as an example.",
        "options": [
            "The claim is correct, because particle spacing can never be "
            "restored once it has changed, not even by supplying energy back "
            "to the substance",
            "The claim is correct for water specifically, but false for every other "
            "substance, because water's lattice is unusually open",
            "The claim cannot be tested, because particle spacing cannot be "
            "observed directly",
            "The claim is incorrect — freezing changes the spacing, but the "
            "ice can simply be melted again to restore the liquid arrangement",
        ],
        "correct_index": 3,
        "why": "Freezing rearranges the particles into a lattice, but supplying "
                "energy again simply melts the ice back to the same liquid "
                "arrangement — physical changes of state are reversible.",
    },
    {
        "id": "ks4-changes-of-state-h13",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Dry ice used in a fog machine is often described as 'melting "
                "into a puddle of liquid carbon dioxide'. Evaluate this "
                "description at normal atmospheric pressure.",
        "options": [
            "The description is incorrect — at normal atmospheric pressure, "
            "solid carbon dioxide sublimes directly into gas, with no liquid "
            "stage forming at all",
            "The description is correct — solid carbon dioxide always melts "
            "into a liquid before evaporating into fog, just like frozen "
            "carbon dioxide does under any other conditions",
            "The description is correct, because all solids must pass through "
            "a liquid stage before becoming a gas, the same way water itself "
            "must always pass through a liquid stage first",
            "The description is incorrect — dry ice is actually a very cold gas at "
            "room temperature that only looks solid because of the cold fog around it",
        ],
        "correct_index": 0,
        "why": "At normal atmospheric pressure, solid carbon dioxide sublimes "
               "straight into gas — the visible fog is water vapour condensing in the "
               "cold gas, not liquid CO2.",
    },
    {
        "id": "ks4-changes-of-state-h14",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "On some very cold, clear nights, a lawn shows a layer of frost "
                "with no sign of dew having formed first. Suggest why frost can "
                "form directly, without a liquid stage.",
        "options": [
            "Frost always forms from dew that has since frozen solid "
            "overnight",
            "If the grass surface is already below 0 °C when the water vapour "
            "meets it, the vapour deposits directly as ice without becoming "
            "liquid first",
            "Frost is a completely different substance from dew and involves no "
            "change of state at all, forming instead from dust particles in the cold "
            "air",
            "Frost only forms when the air itself freezes into tiny solid "
            "particles",
        ],
        "correct_index": 1,
        "why": "If the surface is already below the freezing point when water "
                "vapour reaches it, the vapour can deposit straight into solid "
                "ice, skipping the liquid stage entirely.",
    },
    {
        "id": "ks4-changes-of-state-h15",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A marshmallow toasted over a fire turns brown and slightly crisp "
                "on the outside, while the inside becomes soft and gooey. "
                "Evaluate what types of change are happening in the marshmallow "
                "at the same time.",
        "options": [
            "Only a physical change is happening — the whole marshmallow is "
            "simply melting throughout",
            "Only a chemical change is happening — the whole marshmallow is "
            "being converted into a new substance, right down to its soft, "
            "gooey centre as well as its crust",
            "The outside undergoes a chemical change as it browns and forms "
            "new substances, while the inside undergoes a physical change as "
            "its sugar melts and softens",
            "Neither change is happening — a marshmallow only changes in "
            "appearance, not in its actual particles",
        ],
        "correct_index": 2,
        "why": "Browning on the outside forms new substances and cannot be "
                "reversed, a chemical change, while the softening inside is just "
                "the sugar mixture melting, a physical change.",
    },
    {
        "id": "ks4-changes-of-state-h16",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ice at −5 °C is warmed steadily until it becomes steam at 110 "
                "°C. Describe, in order, every state the substance passes through "
                "and name the two changes of state involved.",
        "options": [
            "Solid, then gas directly, via a single sublimation",
            "Liquid, then solid, then gas, via freezing and then sublimation",
            "Solid, then liquid, then solid again, via melting and then "
            "freezing",
            "Solid, then liquid, then gas, via melting and then boiling",
        ],
        "correct_index": 3,
        "why": "Warming ice first melts it to liquid water at 0 °C, and further "
                "warming then boils the liquid into steam at 100 °C — solid, "
                "liquid, then gas.",
    },
    {
        "id": "ks4-changes-of-state-h17",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Freeze-dried food is made by removing water from food as a gas "
                "at very low pressure, without the water ever becoming liquid. A "
                "student argues this proves sublimation needs no energy, 'because "
                "low pressure does the work instead'. Evaluate this argument.",
        "options": [
            "The argument is incorrect — energy is still needed to free the "
            "water particles from the food and fully separate them into a "
            "gas; the low pressure only makes this possible at a lower "
            "temperature, however low the pressure inside the chamber is "
            "allowed to fall",
            "The argument is correct — sublimation under low pressure needs no energy "
            "input at all, since removing the air above the food is itself what pulls "
            "its water particles apart and carries them off, leaving the food dry "
            "without anything at all being warmed up",
            "The argument is correct, because the water in the food does not actually "
            "change state at all — at a low enough pressure it is simply drawn out of "
            "the food as a liquid and collected",
            "The argument is incorrect — freeze-drying does not involve sublimation "
            "at all, but ordinary evaporation from the liquid water still inside the "
            "food, which escapes far faster once the pressure around it has been "
            "lowered to near vacuum and nothing is left above the surface to push the "
            "escaping particles back in",
        ],
        "correct_index": 0,
        "why": "Sublimation still requires energy to overcome the forces between "
                "the particles; reducing the pressure simply lets that happen at "
                "a lower temperature, not with no energy at all.",
    },
    {
        "id": "ks4-changes-of-state-h18",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Weather forecasters sometimes give both a 'dew point' and a "
                "lower 'frost point' for the same air on a cold night. Explain "
                "why these are two different temperatures rather than one.",
        "options": [
            "They are always the same temperature; forecasters only use different "
            "names depending on whether the ground beneath the air happens to be "
            "frozen hard at the time that the forecast is issued",
            "The dew point is the temperature at which water vapour condenses "
            "onto a liquid surface, while the frost point, a lower value, is "
            "where it deposits directly onto a surface already below 0 °C",
            "The frost point is always higher than the dew point, because ice "
            "forms more easily than liquid water, which is why frost always "
            "appears well before any dew ever has the chance to form on a "
            "surface",
            "The two points relate to entirely different gases in the air, "
            "not to water vapour at all",
        ],
        "correct_index": 1,
        "why": "Condensation onto a surface above 0 °C forms dew at the dew "
                "point; deposition directly onto a colder surface forms frost, "
                "and that surface must be colder still, at the frost point.",
    },
    {
        "id": "ks4-changes-of-state-h19",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist has a white powder and wants to find out whether it "
                "is a pure substance or a mixture of two different solids. "
                "Explain how heating the powder and observing its melting "
                "behaviour could help answer this.",
        "options": [
            "If it melts at all, it must be a mixture, because pure substances do not "
            "melt but instead break down straight into a gas when they are heated "
            "strongly enough",
            "Melting behaviour reveals nothing about purity — only a density "
            "measurement taken on the solid can separate a pure substance from a "
            "mixture",
            "If it melts gradually over a range of temperatures, it is likely "
            "a mixture; if it melts sharply at one exact temperature, it is "
            "likely pure",
            "If it melts sharply at one exact temperature, it must be a "
            "mixture of two identical substances",
        ],
        "correct_index": 2,
        "why": "A pure solid has a fixed, regular lattice that breaks down at "
                "one precise temperature; a mixture's disrupted structure softens "
                "and melts gradually over a range.",
    },
    {
        "id": "ks4-changes-of-state-h20",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Condensation forms on the OUTSIDE of a cold glass of lemonade on "
                "a warm day, rather than on the inside where the cold liquid "
                "actually is. Explain why.",
        "options": [
            "The cold lemonade itself is leaking slowly out through the wall of the "
            "glass and collecting as visible droplets on its outer surface instead",
            "The glass chemically reacts with the air to produce water on its "
            "outer surface",
            "Condensation always forms on glass regardless of temperature, on "
            "whichever side faces the room, whatever the temperature of the "
            "drink happens to be inside it",
            "Warm, humid air from the room touches the cold outer surface of "
            "the glass, cools below its dew point there, and its water vapour "
            "condenses",
        ],
        "correct_index": 3,
        "why": "It is the room's warm, humid air meeting the cold outside of the "
                "glass that cools below its dew point and condenses — the "
                "lemonade inside never touches that air.",
    },
    {
        "id": "ks4-changes-of-state-h21",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Salt sprinkled on an icy pavement causes the ice to melt, even "
                "though the air temperature stays below 0 °C. Explain how this is "
                "possible.",
        "options": [
            "Dissolved salt lowers the temperature at which the solid-liquid "
            "mixture is balanced, so ice that was stable at that temperature "
            "now melts",
            "The salt chemically reacts with the ice to produce heat, and it is that "
            "heat, rather than the salt itself, which melts the ice on the pavement",
            "Salt physically scrapes a thin layer off the top of the ice, "
            "exposing warmer ice underneath, in exactly the same way that "
            "grit does on an icy road",
            "The salt has no real effect — the ice would have melted at that "
            "temperature anyway",
        ],
        "correct_index": 0,
        "why": "Dissolving salt in the surface water lowers the melting point of "
                "the mixture below 0 °C, so ice that was stable without salt now "
                "melts at the same air temperature.",
    },
    {
        "id": "ks4-changes-of-state-h22",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mothball made of solid naphthalene slowly disappears from a "
                "wardrobe, turning straight into a gas at room temperature. Suggest "
                "whether breaking the mothball into small pieces would make it "
                "sublime faster, using the same reasoning that explains evaporation "
                "rate.",
        "options": [
            "Yes — breaking it up increases the total surface area exposed to the "
            "surroundings, so more particles can escape into the gas phase at once",
            "No — sublimation is a completely different process from evaporation and "
            "is not affected by surface area at all, only by how much of the solid "
            "there is in total",
            "No — a mothball always sublimes at a fixed rate however it is shaped, "
            "since only the total mass of it decides how quickly it disappears",
            "Yes, but only because breaking it up lowers its temperature further, not "
            "because of its surface area",
        ],
        "correct_index": 0,
        "why": "Sublimation, like evaporation, happens at exposed surfaces, so "
               "increasing the surface area lets more particles escape into the "
               "gas phase at once.",
    },
    {
        "id": "ks4-changes-of-state-h23",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Adding salt to water raises its boiling point slightly above "
                "100 °C, while adding it to ice lowers the temperature at which "
                "the ice melts. Suggest what both of these effects have in "
                "common.",
        "options": [
            "In both cases, dissolved salt particles disrupt the regular "
            "arrangement the pure substance would otherwise have, shifting the "
            "temperature at which the change of state balances",
            "The two effects are unrelated: one is caused by a chemical reaction "
            "between the salt and the water, while the other is only a physical "
            "crowding of particles at the surface of the ice",
            "Salt actually lowers both the boiling point and the melting point of "
            "water, so the two effects named in the question are really the same "
            "single effect happening twice over",
            "Only the melting point can be shifted by a dissolved substance; "
            "the boiling point of water can never be changed",
        ],
        "correct_index": 0,
        "why": "A dissolved substance disturbs the regular arrangement pure "
               "water would otherwise settle into, shifting the balance point "
               "of both changes of state.",
    },
    {
        "id": "ks4-changes-of-state-h24",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Frozen food left in a freezer for months sometimes develops "
                "visible ice crystals INSIDE its packaging, even though the bag "
                "was properly sealed. Suggest how this happens.",
        "options": [
            "Ice on the food's surface slowly sublimes into water vapour "
            "inside the sealed bag, which then deposits as ice crystals on the "
            "coldest surfaces it reaches, such as the inside of the packaging",
            "Water must be leaking into the bag from outside the freezer somehow, "
            "because ice cannot form anywhere unless liquid water has first reached "
            "that spot, and a sealed bag holds no liquid on its inner surface",
            "The food's own water content is chemically changing into a new substance "
            "over time, and that new substance settles out of the food as visible "
            "crystals on the inside of the bag over several months",
            "This cannot actually happen if the packaging is properly "
            "sealed, so the seal must have failed",
        ],
        "correct_index": 0,
        "why": "Within the sealed bag, ice can sublime into vapour and then "
               "deposit again on a colder surface, forming visible crystals "
               "without any water entering or leaving the bag.",
    },
    {
        "id": "ks4-changes-of-state-h25",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a very cold day, a person's breath is visible as a small "
                "white cloud when they breathe out. Explain what causes this, "
                "given that their breath is much warmer and more humid than the "
                "surrounding air.",
        "options": [
            "The warm, humid air from their lungs cools rapidly in the cold "
            "outside air, and its water vapour condenses into tiny visible "
            "liquid droplets",
            "The breath itself is made of tiny particles of solid carbon dioxide, "
            "similar to dry ice, which form as the warm breath is suddenly chilled by "
            "the outside air",
            "Breathing out always produces visible smoke, regardless of the outside "
            "temperature, but it only shows up clearly against a cold winter sky",
            "The cold air chemically reacts with the carbon dioxide in the "
            "breath to form a visible gas",
        ],
        "correct_index": 0,
        "why": "Warm, water-vapour-rich breath cools suddenly in the cold "
               "air, and its vapour condenses into the tiny droplets seen as a "
               "visible cloud.",
    },
    {
        "id": "ks4-changes-of-state-h26",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims 'boiling always happens at exactly 100 °C'. "
                "Evaluate this claim, using what happens to the boiling point "
                "at high altitude and when a substance is dissolved in the "
                "water.",
        "options": [
            "The claim is too simple — 100 °C is only the boiling point of "
            "pure water at normal atmospheric pressure; it falls at high "
            "altitude and rises when a substance is dissolved in the water",
            "The claim is entirely correct — 100 °C is a fixed, unchangeable boiling "
            "point for water under every circumstance there is, at any altitude and "
            "with anything at all dissolved in it",
            "The claim is wrong only because of altitude; dissolved substances never "
            "affect the boiling point of water, since they sit down in the liquid and "
            "take no part in what escapes from its surface",
            "The claim is wrong only because of dissolved substances; "
            "altitude never affects the boiling point of water",
        ],
        "correct_index": 0,
        "why": "100 °C is specific to pure water at normal atmospheric "
               "pressure; both altitude and dissolved substances shift it in "
               "opposite directions.",
    },

    # ── internal-energy ─────────────────────────────────────────────────
    {
        "id": "ks4-internal-energy-e05",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State two ways in which the internal energy of a system can be "
                "increased.",
        "options": [
            "By heating it, or by doing work on it",
            "By heating it only — nothing else can increase it",
            "By cooling it, or by doing work on it",
            "By increasing its volume, or its density",
        ],
        "correct_index": 0,
        "why": "Internal energy rises whenever energy is transferred in, whether "
                "by heating or by doing work on the system.",
    },
    {
        "id": "ks4-internal-energy-e06",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A system neither gains nor loses energy to its surroundings. "
                "State what happens to its internal energy.",
        "options": [
            "It gradually falls to zero",
            "It stays exactly the same",
            "It rises slowly over time",
            "It becomes impossible to measure",
        ],
        "correct_index": 1,
        "why": "With no energy transferred in or out by heating or by doing "
                "work, the internal energy cannot change.",
    },
    {
        "id": "ks4-internal-energy-e07",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what decides the direction energy is transferred between "
                "two objects placed in contact.",
        "options": [
            "The difference in their masses",
            "The difference in their colours",
            "The difference in their temperatures",
            "The size of the objects alone",
        ],
        "correct_index": 2,
        "why": "Energy always transfers from the object at the higher "
                "temperature to the one at the lower temperature.",
    },
    {
        "id": "ks4-internal-energy-e08",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A heater warming a metal block is switched off, but the block is "
                "still hotter than the room. State what happens to its internal "
                "energy next.",
        "options": [
            "It increases further, even with the heater switched off",
            "It stays exactly the same until the heater is switched back on",
            "It decreases only if someone touches the block",
            "It decreases, as it transfers energy to the cooler room",
        ],
        "correct_index": 3,
        "why": "The block is still hotter than its surroundings, so it keeps "
                "transferring energy out, and its internal energy keeps falling.",
    },
    {
        "id": "ks4-internal-energy-e09",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of internal energy, why rubbing your hands "
                "together makes them feel warmer.",
        "options": [
            "Friction does work on your hands, transferring energy into them",
            "Your hands heat each other up by direct contact alone",
            "Rubbing lowers the temperature your skin needs to feel warm",
            "Skin always warms up whenever it is touched by anything",
        ],
        "correct_index": 0,
        "why": "Rubbing does work against friction, and that work transfers "
                "energy into your hands, raising their internal energy.",
    },
    {
        "id": "ks4-internal-energy-e10",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist pumps up a tyre quickly, and the barrel of the pump "
                "becomes noticeably warm. State the way its internal energy has "
                "increased.",
        "options": [
            "By heating from the cyclist's warm hands alone",
            "By doing work on the trapped air inside it",
            "By friction between the tyre and the road surface",
            "By energy leaking in from the warm outside air",
        ],
        "correct_index": 1,
        "why": "Compressing the trapped air does work on it, and that work "
                "raises its internal energy without any heating involved.",
    },
    {
        "id": "ks4-internal-energy-e11",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the way internal energy is increased when a Bunsen burner "
                "heats a beaker of water directly.",
        "options": [
            "By doing work",
            "By cooling",
            "By heating",
            "By evaporation",
        ],
        "correct_index": 2,
        "why": "A flame transfers energy in by heating, directly raising the "
                "internal energy of the water.",
    },
    {
        "id": "ks4-internal-energy-e12",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what always happens to the internal energy of a substance when "
                "energy is transferred to it by heating.",
        "options": [
            "It decreases",
            "It stays the same",
            "It becomes negative",
            "It increases",
        ],
        "correct_index": 3,
        "why": "Heating transfers energy into the substance, and that energy raises "
               "its internal energy — during a change of state it is the temperature, "
               "not the internal energy, that stays constant.",
    },
    {
        "id": "ks4-internal-energy-s06",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hot copper block and a cold copper block of the same mass are "
                "pushed together and left. Explain what happens to their "
                "temperatures and their internal energies over time.",
        "options": [
            "Energy transfers from the hot block to the cold block until both "
            "reach the same final temperature",
            "The hot block stays hot forever, because metals do not share "
            "energy with each other, whatever their sizes happen to be",
            "Both blocks warm up together, because pressing two metals into contact "
            "always releases extra energy",
            "The cold block cools further, because contact removes energy "
            "from both blocks",
        ],
        "correct_index": 0,
        "why": "Energy flows from the higher to the lower temperature until the "
                "two blocks reach a shared, equal temperature.",
    },
    {
        "id": "ks4-internal-energy-s07",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An insulated flask and an open cup, both holding the same hot "
                "drink, are left in the same cold room. Compare how their "
                "internal energy changes over the next hour.",
        "options": [
            "Both lose internal energy at the same rate, because insulation "
            "only affects appearance, for both containers, without exception",
            "The open cup loses internal energy faster, because heat escapes "
            "more quickly through its uncovered surface",
            "The insulated flask loses internal energy faster, because "
            "trapped air always heats up more, however good the insulation is "
            "claimed to be",
            "Neither loses any internal energy, because a hot drink holds on to its "
            "energy until it is actually drunk",
        ],
        "correct_index": 1,
        "why": "Insulation slows the rate energy is lost to the surroundings; it "
                "does not stop the loss, so the open cup cools, and empties its "
                "internal energy, faster.",
    },
    {
        "id": "ks4-internal-energy-s08",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A puddle of water is often slightly cooler than the surrounding "
                "air on a hot, dry day. Explain this in terms of the kinetic "
                "energy of its particles.",
        "options": [
            "The ground beneath always absorbs heat directly from the puddle, cooling "
            "it from below faster than the sun above can warm it",
            "Sunlight reflects off the puddle's surface, so it never actually absorbs "
            "any energy from the air above it",
            "The most energetic particles escape as vapour, lowering the "
            "average kinetic energy of those left behind",
            "Water always sits at a lower temperature than the air around it, "
            "whatever the conditions",
        ],
        "correct_index": 2,
        "why": "Evaporation removes the fastest, most energetic particles, so "
                "the average kinetic energy, and so the temperature, of the "
                "remaining water falls slightly.",
    },
    {
        "id": "ks4-internal-energy-s09",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two blocks of the same material and in the same state, but of "
                "different mass, are found to have exactly equal internal energy. "
                "Explain what this tells you about their temperatures.",
        "options": [
            "They must be at exactly the same temperature, because equal "
            "internal energy always means equal temperature",
            "The smaller block must be at a lower temperature, because a smaller mass "
            "always means a lower temperature",
            "Nothing can be said about their temperatures without also knowing their "
            "masses and the materials",
            "The larger block must be at a lower temperature, because its "
            "energy is shared among more particles",
        ],
        "correct_index": 3,
        "why": "The larger block has more particles sharing the same total "
                "energy, so its average kinetic energy per particle, and so its "
                "temperature, is lower.",
    },
    {
        "id": "ks4-internal-energy-s10",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'Object A is at a higher temperature than object "
                "B, but B has ten times the mass of A, so I cannot yet tell which "
                "has more internal energy.' Evaluate this statement.",
        "options": [
            "The student is correct — internal energy depends on both the "
            "temperature and the amount of substance present",
            "The student is wrong — the hotter object always has the greater "
            "internal energy, whatever the two masses are",
            "The student is wrong — mass has no effect at all on the total "
            "internal energy of an object",
            "The student is correct, but only because B is a solid and A is a "
            "liquid, which the question does not state",
        ],
        "correct_index": 0,
        "why": "Internal energy depends on both the average energy per particle "
                "and how many particles there are, so temperature alone cannot "
                "decide which object holds more.",
    },
    {
        "id": "ks4-internal-energy-s11",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to the kinetic energy and to the potential "
                "energy of the particles in a pure liquid as it boils at its "
                "boiling point.",
        "options": [
            "Both the kinetic energy and the potential energy rise steadily "
            "together throughout the boiling, exactly like a solid being "
            "warmed steadily",
            "The kinetic energy stays constant, because the temperature is "
            "fixed, while the potential energy rises sharply",
            "The kinetic energy rises as the particles heat further, while the "
            "potential energy between them stays fixed",
            "Both the kinetic energy and the potential energy fall, because "
            "energy is being used up to form a gas",
        ],
        "correct_index": 1,
        "why": "Temperature is constant during boiling, so average kinetic "
                "energy does not change; the energy supplied goes into potential "
                "energy as the particles fully separate.",
    },
    {
        "id": "ks4-internal-energy-s12",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The gas escaping quickly from an aerosol can feels cold on the "
                "skin. Explain this using the idea of a gas doing work as it "
                "expands.",
        "options": [
            "The gas absorbs energy from the can's own metal casing as it rushes out "
            "through the narrow nozzle, cooling the metal",
            "The gas simply arrives already cold, because it was compressed at a low "
            "temperature originally and has kept that same temperature inside the can "
            "ever since",
            "The rapidly expanding gas does work pushing back the air around "
            "it, and that energy comes from its own internal energy",
            "Expanding gas always warms up first and only cools once it has "
            "spread out completely",
        ],
        "correct_index": 2,
        "why": "Doing work on the surroundings takes energy from the gas's own "
                "internal energy, so its temperature falls as it expands.",
    },
    {
        "id": "ks4-internal-energy-s13",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Steam and liquid water of the same mass are both at 100 °C. "
                "Explain why the steam has the greater internal energy.",
        "options": [
            "The steam particles have a much higher average kinetic energy, "
            "because gas particles always move faster than liquid ones",
            "The two have identical internal energy, because equal "
            "temperature always means equal internal energy",
            "The liquid actually has the greater internal energy, because its "
            "particles are held more tightly together",
            "The steam particles have the same average kinetic energy, but "
            "far more potential energy, since they are fully separated",
        ],
        "correct_index": 3,
        "why": "Equal temperature means equal average kinetic energy, but the "
                "steam's separated particles store far more potential energy, "
                "giving it more internal energy overall.",
    },
    {
        "id": "ks4-internal-energy-s14",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a thermometer reading alone cannot tell you the "
                "total internal energy of an object.",
        "options": [
            "A thermometer only measures average kinetic energy per particle, "
            "not the total energy of every particle present",
            "Thermometers are never accurate enough to be trusted for any energy "
            "measurement, whatever the object being measured",
            "A thermometer measures internal energy directly, but only for "
            "solids, not for liquids or gases, at any temperature above "
            "absolute zero",
            "Internal energy cannot be measured by any instrument, including "
            "a thermometer, under any circumstances, no matter how advanced "
            "the instrument is",
        ],
        "correct_index": 0,
        "why": "Temperature reflects the average energy per particle; finding "
                "the total also needs the mass and the material, which a "
                "thermometer alone cannot give.",
    },
    {
        "id": "ks4-internal-energy-s15",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A block loses 400 J of internal energy, transferring all of it "
                "to a second block with no losses to the surroundings. State what "
                "happens to the internal energy of the second block.",
        "options": [
            "It falls by 400 J, because energy always flows away from "
            "whichever block loses it",
            "It rises by 400 J, since energy is conserved between the two "
            "blocks",
            "It rises by less than 400 J, because some energy always escapes "
            "during a transfer",
            "It stays unchanged, because only the first block's energy was "
            "measured",
        ],
        "correct_index": 1,
        "why": "With no losses, the energy leaving the first block is exactly "
                "the energy arriving at the second, so its internal energy rises "
                "by the same 400 J.",
    },
    {
        "id": "ks4-internal-energy-s16",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says a fridge cools food by 'pumping coldness into "
                "it'. Evaluate this way of describing what a fridge does, in "
                "terms of internal energy.",
        "options": [
            "This is correct — a fridge genuinely creates cold energy and "
            "transfers it into the food, and that cold energy simply appears "
            "from nowhere inside the compressor",
            "This is correct, but only for fridges that use a chemical "
            "coolant rather than an electrical one, as confirmed by every "
            "fridge manufacturer",
            "This is incorrect — a fridge removes energy from the food, "
            "lowering its internal energy, rather than adding coldness",
            "This is incorrect — a fridge does not change the internal energy of the "
            "food at all, only how cold its surface feels",
        ],
        "correct_index": 2,
        "why": "There is no such thing as a store of 'coldness'; a fridge works "
                "by removing energy from the food, lowering its internal energy "
                "so its temperature falls.",
    },
    {
        "id": "ks4-internal-energy-s17",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pan of soup is brought just to a simmer, then the gas supply "
                "is turned off. Explain what happens to the internal energy of "
                "the soup over the following few minutes.",
        "options": [
            "It stays exactly the same, because the soup has already reached "
            "its highest possible temperature",
            "It rises further, because a simmering liquid keeps heating "
            "itself once it has started",
            "It falls to zero almost immediately once the flame is removed "
            "from underneath it",
            "It falls, because the soup is still hotter than the room and "
            "keeps transferring energy out",
        ],
        "correct_index": 3,
        "why": "With the heat source removed but the soup still hotter than the "
                "room, energy keeps transferring out, so its internal energy "
                "keeps falling.",
    },
    {
        "id": "ks4-internal-energy-s18",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Blowing gently across a hot bowl of soup helps it cool faster "
                "than leaving it undisturbed. Suggest why, in terms of "
                "evaporation and internal energy.",
        "options": [
            "Blowing sweeps escaped vapour away, letting more particles "
            "evaporate and carry energy away faster",
            "Blowing physically pushes some of the hot soup out of the bowl, "
            "reducing its total mass",
            "Blowing directly lowers the temperature of the soup by mixing in "
            "cold air from the room",
            "Blowing raises the pressure above the soup, which always slows "
            "down how fast a liquid can cool",
        ],
        "correct_index": 0,
        "why": "Moving air carries evaporated particles away rather than letting "
                "them drift back in, so evaporation, and the energy loss that "
                "goes with it, speeds up.",
    },
    {
        "id": "ks4-internal-energy-s19",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical beakers of water are heated for the same 10 "
                "minutes, one by a 2 kW heater and the other by a 1 kW heater. "
                "Compare the rise in internal energy of the two beakers.",
        "options": [
            "Both beakers gain exactly the same internal energy, because the "
            "heating time was identical for both, since only the total time "
            "spent heating actually matters",
            "The 2 kW heater transfers energy at twice the rate, so it gives "
            "twice the rise in internal energy in the same time",
            "The 1 kW heater actually gives the bigger rise, because lower "
            "power always heats more gently and thoroughly",
            "Neither beaker's internal energy can rise at all without first knowing "
            "the starting temperature of the water in it",
        ],
        "correct_index": 1,
        "why": "Power is the rate of energy transfer, so twice the power for the "
                "same time transfers twice the energy, giving twice the rise in "
                "internal energy.",
    },
    {
        "id": "ks4-internal-energy-s20",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas in a sealed balloon left in bright sunshine on a warm day "
                "slowly warms up, without any flame or heater nearby. Explain how "
                "its internal energy is increasing.",
        "options": [
            "It cannot be increasing, since nothing is touching or heating the "
            "balloon on a day with no flame nearby",
            "The gas is doing work on the balloon's rubber skin, which raises "
            "the gas's own internal energy, exactly as compressing any gas "
            "always does",
            "Energy from sunlight is absorbed by the balloon and its gas, "
            "heating it and raising its internal energy",
            "The balloon must be leaking gas, and losing gas always raises "
            "the internal energy of what remains, however small or large the "
            "leak happens to be",
        ],
        "correct_index": 2,
        "why": "Sunlight transfers energy into the balloon by heating, even with "
                "no flame present, raising the gas's internal energy.",
    },
    {
        "id": "ks4-internal-energy-s21",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An ice cube is dropped into a hot cup of tea. Compare the "
                "internal energy of the tea a few seconds later, right after the "
                "ice is added, with what it was just before.",
        "options": [
            "It is unchanged, because adding a solid to a liquid never "
            "affects the liquid's own internal energy",
            "It is higher, because melting the ice releases extra energy "
            "straight into the tea",
            "It is lower, but only because some tea has been physically "
            "displaced out of the cup",
            "It is lower, because some of the tea's internal energy has been "
            "used to begin melting the ice",
        ],
        "correct_index": 3,
        "why": "Melting the ice takes energy from the surrounding tea, so the "
                "tea's own internal energy falls in that first instant.",
    },
    {
        "id": "ks4-internal-energy-s22",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hot drink is left in an insulated flask instead of an open "
                "mug, both starting at the same temperature. Explain why the "
                "flask keeps its drink hotter for longer, in terms of internal "
                "energy.",
        "options": [
            "The insulation slows the rate energy is lost to the "
            "surroundings, not the total amount that will eventually be lost",
            "The insulation adds extra internal energy to the drink as time "
            "passes",
            "The flask's drink never actually loses any internal energy at "
            "all, however long it is left, for as long as anyone cares to "
            "leave it standing there",
            "The open mug's drink loses internal energy only through evaporation from "
            "its surface, never through the sides of the mug",
        ],
        "correct_index": 0,
        "why": "Insulation does not add energy or stop the eventual loss — it "
                "only reduces how fast that energy escapes to the surroundings.",
    },
    {
        "id": "ks4-internal-energy-h06",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that 'the internal energy of any object can "
                "be measured directly by reading a thermometer'.",
        "options": [
            "The claim is correct, provided the thermometer used is accurate and has "
            "been carefully calibrated against a known standard beforehand each time",
            "The claim is incorrect — a thermometer measures only average "
            "kinetic energy per particle; finding the total also needs the "
            "mass and material",
            "The claim is correct, because temperature and internal energy "
            "are simply two names for the same physical quantity, whatever "
            "units either quantity happens to be measured in",
            "The claim is incorrect — thermometers cannot measure kinetic "
            "energy at all, only potential energy",
        ],
        "correct_index": 1,
        "why": "A thermometer reads temperature, the average kinetic energy per "
                "particle; total internal energy also depends on how much "
                "material is present and what it is made of.",
    },
    {
        "id": "ks4-internal-energy-h07",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 50 g piece of hot metal at 90 °C is dropped into an insulated "
                "container of 200 g of water at 15 °C. Predict whether the final "
                "steady temperature will be closer to 15 °C or to 90 °C, and "
                "explain why.",
        "options": [
            "Closer to 90 °C, because the metal started at the higher "
            "temperature and always dominates the final result, however small "
            "the piece of metal turns out to be",
            "Exactly halfway between the two, because energy is always shared equally "
            "between any two objects placed in contact",
            "Closer to 15 °C, because the much larger mass of water can "
            "absorb the metal's energy with only a small rise of its own",
            "Closer to 90 °C, because metals always release far more energy "
            "than water can ever absorb",
        ],
        "correct_index": 2,
        "why": "The water's far greater mass means it can take in the metal's "
                "energy while its own temperature rises only a little, pulling "
                "the final temperature close to 15 °C.",
    },
    {
        "id": "ks4-internal-energy-h08",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An idealised gas, with no attractive forces between its "
                "particles, expands freely into a large empty, evacuated "
                "container, doing no work and receiving no heat at all. Predict "
                "what happens to its internal energy and its temperature.",
        "options": [
            "Both fall, because a gas always cools whenever its volume increases, "
            "however that increase comes about",
            "The internal energy stays the same, but the temperature falls, "
            "because the particles are now more spread out",
            "Both rise, because free expansion always transfers energy in "
            "from the empty container",
            "Both stay exactly the same, since no energy has entered or left "
            "the gas by heating or by doing work",
        ],
        "correct_index": 3,
        "why": "Internal energy only changes by heating or by doing work; with "
                "neither happening, it, and so the average kinetic energy and "
                "temperature, stays unchanged.",
    },
    {
        "id": "ks4-internal-energy-h09",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed syringe full of air has its nozzle blocked and its "
                "plunger pushed in sharply, too quickly for any energy to escape "
                "as heat. Explain why the air inside becomes measurably hotter.",
        "options": [
            "Pushing the plunger in does work on the trapped air, and that "
            "work raises its internal energy and temperature",
            "The plunger heats the air directly by conduction through the syringe's "
            "plastic casing, which warms under the friction of the plunger sliding "
            "along it",
            "Compressing air chemically reacts with itself, releasing extra energy "
            "each time it is squeezed into a smaller space",
            "The air must be gaining extra particles from outside the syringe as the "
            "plunger is pushed inward along the barrel",
        ],
        "correct_index": 0,
        "why": "With no time for heat to escape, the work done compressing the "
                "gas is transferred straight into its internal energy, raising "
                "its temperature.",
    },
    {
        "id": "ks4-internal-energy-h10",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical, well-insulated flasks each hold 500 g of water at "
                "20 °C. Flask A is heated by a small electric heater for 10 "
                "minutes. Flask B is instead stirred vigorously by a "
                "falling-weight paddle for the same 10 minutes, transferring the "
                "same total energy to the water. Compare the final temperatures "
                "of the two flasks.",
        "options": [
            "Flask A ends hotter, because heating is always a more effective "
            "way of raising internal energy than doing work",
            "The two final temperatures are the same, because the same total "
            "energy has been transferred to the water either way",
            "Flask B ends hotter, because stirring adds extra energy on top "
            "of whatever a heater alone could provide",
            "Neither flask changes temperature, because stirring and heating "
            "are only ways of moving energy, not creating it",
        ],
        "correct_index": 1,
        "why": "Internal energy rises by the same amount whether the energy "
                "arrives by heating or by doing work, so equal energy transferred "
                "gives an equal final temperature.",
    },
    {
        "id": "ks4-internal-energy-h11",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A weather balloon rises into thinner, much colder air and "
                "expands significantly, with essentially no heat transferred to "
                "it from the surrounding air. Predict what happens to the "
                "temperature of the gas inside it as it expands like this, and "
                "explain why.",
        "options": [
            "It rises, because gas expanding into a larger volume always "
            "gains extra internal energy from that extra space, in exactly "
            "the same way a spring gains energy when compressed",
            "It stays exactly the same, because no heat has been transferred to or "
            "from the gas at any point during the balloon's climb",
            "It falls further, because the expanding gas does work pushing "
            "outward on the balloon's skin, using its own internal energy",
            "It falls only because the surrounding air is colder, not because "
            "of anything the gas itself is doing",
        ],
        "correct_index": 2,
        "why": "With no heat entering, the energy the gas uses doing work as it "
                "expands must come from its own internal energy, so it cools "
                "further.",
    },
    {
        "id": "ks4-internal-energy-h12",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A block of ice at 0 °C and an equal mass of liquid water at 0 °C "
                "are each supplied with exactly the same amount of energy from "
                "identical heaters. Compare which block shows the bigger rise in "
                "temperature.",
        "options": [
            "The ice, because solids always warm up faster than liquids for "
            "the same energy input",
            "Both rise by exactly the same amount, because equal energy "
            "always produces an equal temperature change",
            "Neither rises in temperature, because both are already at the "
            "freezing point of water",
            "The water, because some or all of the ice's energy goes into "
            "melting it rather than raising its temperature",
        ],
        "correct_index": 3,
        "why": "The ice's energy is spent breaking its lattice at constant "
                "temperature, while the water's identical energy input goes "
                "straight into raising its temperature.",
    },
    {
        "id": "ks4-internal-energy-h13",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed, rigid metal cylinder of gas falls from a height and "
                "comes to a sudden stop on hitting the ground. A student suggests "
                "some of its kinetic energy while falling is converted into the "
                "internal energy of the gas on impact. Evaluate this suggestion.",
        "options": [
            "This is reasonable — the sudden deceleration does work on the "
            "cylinder and its contents, converting kinetic energy into "
            "internal energy",
            "This is wrong — kinetic energy while falling can only ever become "
            "gravitational energy again, and never internal energy of any kind",
            "This is wrong — a falling object's kinetic energy is always destroyed "
            "completely on impact, rather than converted into anything the cylinder "
            "or its gas could store",
            "This is reasonable, but only if the cylinder is made from a "
            "metal that conducts heat particularly well",
        ],
        "correct_index": 0,
        "why": "Energy is conserved overall, so the sudden stop converts much of "
                "the falling kinetic energy into heat and internal energy through "
                "the violent impact.",
    },
    {
        "id": "ks4-internal-energy-h14",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why it is impossible, according to the particle model, "
                "for the internal energy of a fully isolated system — one with no "
                "heating and doing no work on or by anything — to change over "
                "time.",
        "options": [
            "Because an isolated system's particles are always frozen "
            "completely in place, unable to move at all",
            "Because internal energy can only change by heating or by doing "
            "work, and an isolated system does neither",
            "Because temperature itself is impossible to define for a system "
            "that has no contact with anything else",
            "Because isolated systems are only ever a theoretical idea, and "
            "never actually exist in real experiments",
        ],
        "correct_index": 1,
        "why": "With neither heating nor doing work occurring, there is no route "
                "for energy to enter or leave, so the internal energy cannot "
                "change.",
    },
    {
        "id": "ks4-internal-energy-h15",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students argue about a hot cup of coffee cooling on a table. "
                "Student X says its internal energy 'runs out' as it cools, "
                "becoming zero once it reaches room temperature. Student Y "
                "disagrees. Evaluate which student is correct.",
        "options": [
            "Student X is correct, because internal energy is only ever measured "
            "relative to absolute zero, at −273 °C, and room temperature is the "
            "everyday zero",
            "Student X is correct, because a substance cannot hold any "
            "internal energy once no more energy is being transferred out of "
            "it, regardless of how much time has passed since it was poured",
            "Student Y is correct — at room temperature the coffee still has "
            "internal energy, similar to a cup of water at that same "
            "temperature",
            "Neither student is correct, because internal energy cannot meaningfully "
            "be discussed for a drink as complex a mixture as coffee",
        ],
        "correct_index": 2,
        "why": "The coffee's internal energy at room temperature is not zero — "
                "it is roughly what a cup of water at that temperature would "
                "have; cooling only transfers energy away, it does not use it up.",
    },
    {
        "id": "ks4-internal-energy-h16",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A large, well-insulated tank of water in a solar heating system "
                "gains energy from sunlight every sunny day and loses very little "
                "overnight. Predict what happens to the tank's internal energy "
                "over a week of similar sunny days, assuming nothing is drawn off "
                "to be used.",
        "options": [
            "It stays exactly the same throughout the week, because the gains "
            "and the losses always balance out exactly",
            "It rises during the day and falls back to its starting value "
            "every single night without fail",
            "It cannot be predicted at all without knowing the exact specific "
            "heat capacity of the water",
            "It keeps rising overall, because each day it gains more energy "
            "than the little it loses overnight",
        ],
        "correct_index": 3,
        "why": "With daily gains outweighing the small overnight losses, the "
                "tank's net internal energy climbs a little further with each "
                "sunny day.",
    },
    {
        "id": "ks4-internal-energy-h17",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A metal ball bearing is dropped into a deep container of thick "
                "oil and falls at a slow, constant speed because of resistance "
                "from the oil, rather than speeding up. Suggest what happens to "
                "the internal energy of the oil as a result, and where that "
                "energy has come from.",
        "options": [
            "The oil's internal energy rises slightly, as the ball does work "
            "against its resistance, transferring energy into it",
            "The oil's internal energy is unaffected, because the ball never "
            "actually touches the oil's own particles directly",
            "The oil's internal energy falls slightly, because the ball "
            "absorbs energy from the oil as it pushes through it",
            "The oil's internal energy rises, but only because the ball "
            "itself is releasing chemical energy as it falls",
        ],
        "correct_index": 0,
        "why": "The ball does work against the oil's resistance as it falls at "
                "constant speed, and that work is transferred into the oil's "
                "internal energy.",
    },
    {
        "id": "ks4-internal-energy-h18",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A large concrete apartment block and a small car parked outside "
                "it, both painted a similar dark colour, are left in strong "
                "midday sun for several hours and both feel warm to touch "
                "afterwards. Suggest which is likely to have gained more total "
                "internal energy, and why.",
        "options": [
            "The car, because dark metal always absorbs far more energy per kilogram "
            "of itself than concrete ever can",
            "The apartment block, because its enormously greater mass means "
            "far more total energy has been absorbed for even a modest rise "
            "in temperature",
            "Both gain exactly the same total internal energy, because both "
            "were exposed to identical sunlight for the same time, purely "
            "because both were sitting in the sun for the same number of "
            "hours",
            "Neither gains any real internal energy, because both simply reflect "
            "almost all of the sunlight that reaches their dark painted surfaces",
        ],
        "correct_index": 1,
        "why": "Even a similar temperature rise represents far more total "
                "internal energy for the block, because its far greater mass "
                "means many more particles have been warmed.",
    },
    {
        "id": "ks4-internal-energy-h19",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A well-insulated system is heated, transferring energy in, while "
                "at the same time it expands and does work pushing against its "
                "surroundings. State what happens to its internal energy if the "
                "energy transferred in by heating is greater than the work it "
                "does.",
        "options": [
            "It decreases overall, because doing any work at all always "
            "outweighs the effect of heating",
            "It stays exactly the same, because heating and doing work always "
            "cancel each other out completely",
            "It increases overall, because more energy is being transferred "
            "in than is being transferred out",
            "It cannot change at all, because a system cannot both be heated "
            "and do work at the same time",
        ],
        "correct_index": 2,
        "why": "Internal energy rises by heating and falls by doing work; if "
                "more comes in than goes out, the overall change is a rise.",
    },
    {
        "id": "ks4-internal-energy-h20",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A copper block and an aluminium block of equal mass start at the "
                "same temperature and are both cooled to 0 °C in an ice bath. "
                "Given that copper and aluminium have different specific heat "
                "capacities, state whether the two blocks release the same total "
                "internal energy to the bath.",
        "options": [
            "Yes, because equal mass and an equal temperature change always "
            "mean an equal amount of energy is released, purely because the "
            "numbers given happen to be identical",
            "Yes, because specific heat capacity only affects how quickly a "
            "block cools, not how much energy it releases, however different "
            "their masses might otherwise have been",
            "No, but only because copper and aluminium end up at slightly different "
            "final temperatures once the ice bath has settled down around them",
            "No — even with identical mass and temperature change, the block "
            "with the higher specific heat capacity releases more energy per "
            "degree cooled",
        ],
        "correct_index": 3,
        "why": "Specific heat capacity sets how much energy is released per "
                "degree of temperature drop, so the two blocks release different "
                "total amounts despite the identical mass and temperature change.",
    },
    {
        "id": "ks4-internal-energy-h21",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical, equally sized rooms are kept at the same steady "
                "temperature by heaters, one room completely empty and the other "
                "full of furniture, books and rugs. Both heaters are switched off "
                "at the same time. Predict which room's temperature falls faster "
                "overnight, and explain why, in terms of internal energy.",
        "options": [
            "The empty room, because it stores far less total internal energy "
            "at that temperature, so the same energy loss produces a bigger "
            "temperature drop",
            "The furnished room, because furniture always conducts energy away into "
            "the walls faster than empty air can carry it there, and the more "
            "surfaces touching the walls the quicker the room empties",
            "Both rooms cool at exactly the same rate, because they are the same size "
            "and lose their energy through identical walls, windows and doorways",
            "The furnished room, because more objects always means more "
            "internal energy is generated by friction between them",
        ],
        "correct_index": 0,
        "why": "The furniture gives the second room a much greater total mass "
                "and so a much greater store of internal energy at that "
                "temperature, so it takes longer for a similar energy loss to "
                "lower its temperature by the same amount.",
    },
    {
        "id": "ks4-internal-energy-s23",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A kettle of water and a bath of water are both at exactly the "
                "same temperature. Explain why touching either would feel the "
                "same, even though the bath contains far more internal energy.",
        "options": [
            "Touch senses temperature, the average kinetic energy per "
            "particle, not total internal energy, and the two are at the "
            "same temperature even though the bath holds vastly more total "
            "energy",
            "Touching them cannot feel the same, since the bath holds far more energy "
            "in total and so must feel hotter to the hand than the kettle does, "
            "however similar the two thermometer readings look",
            "They only feel the same because human skin cannot detect temperature "
            "differences smaller than a few degrees, and the kettle and the bath "
            "differ by far less than that however much water each holds",
            "They feel the same because internal energy and what we feel as heat are "
            "actually two names for the same thing, so two samples holding the same "
            "total energy must always feel exactly as warm as one another",
        ],
        "correct_index": 0,
        "why": "What we feel as temperature is the average kinetic energy "
               "per particle, which is the same for both, regardless of how "
               "much total internal energy each holds.",
    },
    {
        "id": "ks4-internal-energy-s24",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cold drink in a can is left on a table in a warm room, and "
                "its can eventually feels the same temperature as the room. "
                "Describe the direction of energy transfer throughout this "
                "process, and state when it stops.",
        "options": [
            "Energy transfers from the warmer room into the colder drink "
            "throughout, and stops once both reach the same temperature",
            "Energy transfers from the drink into the room throughout, since a colder "
            "object always gives up its energy first of all",
            "No net energy transfer occurs, because the drink and the room "
            "start at different temperatures",
            "Energy transfers in both directions equally from the very start, "
            "cancelling out immediately so that neither the drink nor the room ever "
            "changes",
        ],
        "correct_index": 0,
        "why": "Energy always transfers from higher to lower temperature, so "
               "it flows into the drink until both reach the same "
               "temperature, at which point the net transfer stops.",
    },
    {
        "id": "ks4-internal-energy-s25",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A well-insulated flask of coffee and an identical uninsulated "
                "mug of coffee start at the same temperature. Compare the "
                "internal energy each has lost after one hour.",
        "options": [
            "The uninsulated mug has lost more internal energy, because "
            "heat escapes to the room faster without insulation slowing the "
            "loss",
            "The insulated flask has lost more internal energy, because "
            "insulation traps energy inside and increases the pressure "
            "driving it out",
            "Both have lost exactly the same internal energy, because "
            "insulation only changes appearance, not energy loss",
            "Neither has lost any internal energy, because both started at "
            "the same temperature as each other",
        ],
        "correct_index": 0,
        "why": "Insulation only slows the rate energy is lost to the "
               "surroundings, so the uninsulated mug loses more internal "
               "energy over the same hour.",
    },
    {
        "id": "ks4-internal-energy-s26",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why leaving a car with its windows closed in strong "
                "summer sunshine causes the temperature inside to rise well "
                "above the outside air temperature.",
        "options": [
            "Sunlight passes through the windows and is absorbed by the "
            "seats and dashboard, transferring energy in and raising the "
            "internal energy of the trapped air, which cannot easily escape",
            "The glass windows themselves generate heat by reflecting all of the "
            "sunlight back inside the car, where it builds up between the seats and "
            "the roof until the air there is hotter than the air outside",
            "The trapped air chemically reacts with sunlight, releasing extra energy "
            "inside the car without anything at all having to be heated from outside "
            "the windows at any stage of the day",
            "The temperature inside a closed car can never actually exceed "
            "the temperature outside it",
        ],
        "correct_index": 0,
        "why": "Sunlight transfers energy into the car's interior surfaces "
               "and trapped air, and with nowhere for that energy to easily "
               "escape, its internal energy and temperature climb well above "
               "the air outside.",
    },
    {
        "id": "ks4-internal-energy-h22",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A perfectly insulated, sealed flask contains a chemical "
                "hand-warmer packet that reacts and releases energy once "
                "activated. Explain what happens to the internal energy of "
                "the flask's contents, and identify the source of that "
                "energy.",
        "options": [
            "The internal energy of the contents rises, and the energy "
            "comes from the chemical reaction inside the packet, not from "
            "heating or doing work from outside the flask",
            "The internal energy cannot rise at all inside a sealed, insulated flask, "
            "whatever happens inside it, since good insulation blocks every route "
            "that energy could possibly take",
            "The internal energy rises only because the packet does mechanical work "
            "on the air as it swells up inside the sealed flask, pushing outward on "
            "everything around it",
            "The internal energy stays the same, because a chemical "
            "reaction never releases thermal energy",
        ],
        "correct_index": 0,
        "why": "The chemical reaction itself releases energy inside the "
               "sealed flask, raising the internal energy of its contents "
               "without any heating or work crossing the flask's boundary.",
    },
    {
        "id": "ks4-internal-energy-h23",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical metal blocks are each dropped from the same height, "
                "one landing on a soft cushion and the other directly on concrete. "
                "Compare how much the internal energy of each BLOCK ITSELF rises on "
                "impact.",
        "options": [
            "The block hitting the concrete gains more internal energy, because the "
            "cushion deforms and takes up much of the other block's kinetic energy "
            "itself, leaving less to warm that block",
            "The block hitting the cushion gains more internal energy, because "
            "cushions are better at converting motion into heat and pass that heat "
            "straight back into the block resting on them",
            "Both gain exactly the same internal energy, because they fell "
            "from the same height with the same starting energy",
            "Neither block's internal energy changes on impact, since "
            "kinetic energy is destroyed rather than transformed",
        ],
        "correct_index": 0,
        "why": "Both blocks arrive with the same kinetic energy, but the cushion "
               "deforms and takes up much of one block's energy itself, so less of "
               "that energy is left to raise that block's own internal energy.",
    },
    {
        "id": "ks4-internal-energy-h24",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A well-insulated gas cylinder is fitted with a valve that "
                "lets gas escape slowly, doing work as it pushes past the "
                "valve and expands into the atmosphere, with no heat entering "
                "or leaving the cylinder. Predict what happens to the "
                "temperature of the gas remaining inside.",
        "options": [
            "It falls, because the escaping gas does work as it expands, "
            "and with no heat compensating for this, the remaining gas's "
            "internal energy and temperature drop",
            "It rises, because losing mass always concentrates the remaining internal "
            "energy into a higher temperature among the molecules that are left "
            "behind inside the cylinder",
            "It stays exactly the same, because internal energy only changes due to "
            "heating, never due to gas leaving a container through a valve into the "
            "atmosphere outside",
            "It cannot be predicted without knowing the exact chemical "
            "identity of the gas",
        ],
        "correct_index": 0,
        "why": "The escaping gas does work as it expands, and with no heat "
               "entering to replace that energy, the remaining gas's "
               "internal energy, and so its temperature, falls.",
    },
    {
        "id": "ks4-internal-energy-h25",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A go-kart's brakes get noticeably hot after repeated braking "
                "down a long hill, even though no heater or flame is anywhere "
                "near them. Explain the source of this rise in internal "
                "energy.",
        "options": [
            "Friction between the brake pads and the wheel does work, "
            "converting the kart's kinetic energy into internal energy in "
            "the brakes",
            "The brakes must be absorbing heat directly from the hot road "
            "surface below",
            "The rise in internal energy comes entirely from sunlight being focused "
            "onto the brakes by the polished metal of the wheel as it turns",
            "Brakes always warm up slightly over time regardless of "
            "whether they are used",
        ],
        "correct_index": 0,
        "why": "Braking does work against friction, converting the kart's "
               "kinetic energy into internal energy in the brake pads and "
               "wheel.",
    },
    {
        "id": "ks4-internal-energy-h26",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because a bicycle pump gets warm when "
                "compressing air, and a fridge's cooling pipes get cold when "
                "a gas inside them expands, 'doing work on a gas and letting "
                "a gas do work must always have completely opposite effects "
                "on temperature'. Evaluate this general claim.",
        "options": [
            "The claim is broadly reasonable — doing work ON a gas, "
            "compressing it, tends to raise its internal energy and "
            "temperature, while a gas doing work by expanding tends to "
            "lower them, provided little heat is exchanged either way",
            "The claim is wrong, because compressing and expanding a gas always have "
            "exactly the same effect on its temperature, since the same molecules are "
            "moving at the same average speed throughout both of the two changes "
            "described",
            "The claim is wrong, because temperature is completely unrelated to "
            "whether work is done on or by a gas, and depends only on how much heat "
            "reaches it",
            "The claim is correct only for gases, and never applies to "
            "anything solid or liquid in any situation",
        ],
        "correct_index": 0,
        "why": "Doing work on a gas transfers energy into it, raising its "
               "internal energy, while a gas doing work on its surroundings "
               "loses energy, and both effects show up as a temperature "
               "change when little heat is exchanged.",
    },

    # ── temperature-changes-shc ─────────────────────────────────────────
    {
        "id": "ks4-temperature-changes-shc-e06",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State, in words, what specific heat capacity measures.",
        "options": [
            "The energy needed to raise the temperature of 1 kg of a material "
            "by 1 °C",
            "The total energy stored inside a material at room temperature, "
            "whatever the room's temperature happens to be",
            "The energy needed to change the state of 1 kg of a material at its "
            "melting point",
            "The highest temperature a material can reach before it starts to melt",
        ],
        "correct_index": 0,
        "why": "Specific heat capacity is defined as the energy needed per "
                "kilogram per degree Celsius rise in temperature.",
    },
    {
        "id": "ks4-temperature-changes-shc-e07",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.0 kg block of copper has a mass of 1000 g. Calculate the "
                "energy needed to raise its temperature by 10 °C. The specific "
                "heat capacity of copper is 385 J/kg°C.",
        "options": [
            "385 J",
            "3850 J",
            "38.5 J",
            "39 850 J",
        ],
        "correct_index": 1,
        "why": "ΔE = mcΔθ = 1.0 × 385 × 10 = 3850 J.",
    },
    {
        "id": "ks4-temperature-changes-shc-e08",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rearrangement of ΔE = mcΔθ is written as m = ΔE ÷ (c × Δθ). "
                "State which quantity this version finds.",
        "options": [
            "The specific heat capacity",
            "The temperature change",
            "The mass of the substance",
            "The energy transferred",
        ],
        "correct_index": 2,
        "why": "The equation has been rearranged to make m the subject, so it "
                "finds the mass.",
    },
    {
        "id": "ks4-temperature-changes-shc-e09",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "84 000 J of energy raises the temperature of 2.0 kg of a liquid "
                "by 10 °C. Calculate the specific heat capacity of the liquid.",
        "options": [
            "420 J/kg°C",
            "42 J/kg°C",
            "16 800 J/kg°C",
            "4200 J/kg°C",
        ],
        "correct_index": 3,
        "why": "c = ΔE ÷ (m × Δθ) = 84 000 ÷ (2.0 × 10) = 4200 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-e10",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the apparatus used to measure the energy transferred to a "
                "block in the required practical for specific heat capacity.",
        "options": [
            "A joulemeter, or an ammeter, voltmeter and stopwatch",
            "A newtonmeter, or a spring balance and a ruler",
            "A measuring cylinder, or a balance and a stopwatch",
            "A set of vernier callipers, or a micrometer",
        ],
        "correct_index": 0,
        "why": "A joulemeter reads energy directly, or the current, voltage and "
                "time can be used with E = IVt.",
    },
    {
        "id": "ks4-temperature-changes-shc-e11",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sand has a specific heat capacity of about 830 J/kg°C and "
                "seawater about 4000 J/kg°C. State which heats up faster in the "
                "same sunshine, for equal mass and equal energy absorbed.",
        "options": [
            "The seawater, because a higher specific heat capacity heats up "
            "faster",
            "The sand, because a lower specific heat capacity needs less "
            "energy per degree",
            "Both heat up at exactly the same rate, since they receive the "
            "same sunshine",
            "Neither can heat up without first being placed in direct contact "
            "with a flame",
        ],
        "correct_index": 1,
        "why": "A lower specific heat capacity means less energy is needed for "
                "each degree of temperature rise, so the sand warms up faster for "
                "the same energy input.",
    },
    {
        "id": "ks4-temperature-changes-shc-e12",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of these four quantities is NOT needed to calculate "
                "the energy transferred using ΔE = mcΔθ.",
        "options": [
            "The mass of the substance",
            "The specific heat capacity of the substance",
            "The volume of the substance",
            "The temperature change of the substance",
        ],
        "correct_index": 2,
        "why": "ΔE = mcΔθ uses mass, specific heat capacity and temperature "
                "change; volume plays no part in the equation.",
    },
    {
        "id": "ks4-temperature-changes-shc-s07",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.5 kg block absorbs 27 000 J of energy and its temperature "
                "rises by 30 °C. Determine the specific heat capacity of the "
                "material and identify it, given water = 4200 J/kg°C, aluminium = "
                "900 J/kg°C, and copper = 385 J/kg°C.",
        "options": [
            "900 J/kg°C, which matches aluminium, because 27 000 ÷ 30 gives 900 "
            "directly",
            "385 J/kg°C, which matches the value given for copper exactly",
            "4200 J/kg°C, which matches water exactly",
            "600 J/kg°C, which matches none of the three materials given",
        ],
        "correct_index": 3,
        "why": "c = ΔE ÷ (m × Δθ) = 27 000 ÷ (1.5 × 30) = 27 000 ÷ 45 = 600 "
                "J/kg°C, which matches none of the three named materials.",
    },
    {
        "id": "ks4-temperature-changes-shc-s08",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.80 kg block of an unknown metal absorbs 14 400 J of energy "
                "and warms by 20 °C. Identify the metal, given aluminium = 900 "
                "J/kg°C, iron = 450 J/kg°C, and copper = 385 J/kg°C.",
        "options": [
            "Aluminium, since 14 400 ÷ (0.80 × 20) = 900 J/kg°C",
            "Copper, since 14 400 ÷ (0.80 × 20) = 385 J/kg°C",
            "Iron, since 14 400 ÷ (0.80 × 20) = 450 J/kg°C",
            "None of the three, since the value comes out at 720 J/kg°C",
        ],
        "correct_index": 0,
        "why": "c = 14 400 ÷ (0.80 × 20) = 14 400 ÷ 16 = 900 J/kg°C, which "
                "matches aluminium.",
    },
    {
        "id": "ks4-temperature-changes-shc-s09",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kg mass of a liquid is cooled from 60 °C to 35 °C, "
                "releasing 105 000 J of energy. Calculate the specific heat "
                "capacity of the liquid.",
        "options": [
            "1750 J/kg°C",
            "2100 J/kg°C",
            "4200 J/kg°C",
            "52 500 J/kg°C",
        ],
        "correct_index": 1,
        "why": "Δθ = 60 − 35 = 25 °C, so c = 105 000 ÷ (2.0 × 25) = 2100 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-s10",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rearrange ΔE = mcΔθ to make Δθ the subject, and use it to find "
                "the temperature rise when 63 000 J heats 3.0 kg of water (c = "
                "4200 J/kg°C).",
        "options": [
            "Δθ = ΔE × m × c; Δθ = 793 800 000 °C",
            "Δθ = (m × c) ÷ ΔE; Δθ = 0.20 °C",
            "Δθ = ΔE ÷ (m × c); Δθ = 5.0 °C",
            "Δθ = ΔE ÷ (m + c); Δθ = 15 °C",
        ],
        "correct_index": 2,
        "why": "Dividing both sides by mc gives Δθ = ΔE ÷ (mc) = 63 000 ÷ (3.0 × "
                "4200) = 5.0 °C.",
    },
    {
        "id": "ks4-temperature-changes-shc-s11",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical, a student notices the thermometer "
                "bulb is resting against the side of the metal block rather than "
                "sitting inside a hole drilled into the block. Explain the likely "
                "effect on the measured specific heat capacity.",
        "options": [
            "No effect at all, because a thermometer reads the same "
            "temperature wherever it touches the block",
            "The measured value will be too low, because contact with the "
            "surface always reads a higher temperature than the inside",
            "The experiment simply cannot be completed at all without a hole "
            "drilled into the block",
            "The measured value will be too high, because the thermometer "
            "only reads part of the block's true temperature rise",
        ],
        "correct_index": 3,
        "why": "Reading a smaller temperature rise than the true one gives a "
                "smaller Δθ on the bottom of the fraction, which makes the "
                "calculated specific heat capacity come out too high.",
    },
    {
        "id": "ks4-temperature-changes-shc-s12",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cook chooses a copper-bottomed pan (c = 385 J/kg°C) rather "
                "than a stainless steel one (c = 500 J/kg°C) so it responds to "
                "temperature changes quickly. Explain why the lower specific heat "
                "capacity gives this effect.",
        "options": [
            "A lower specific heat capacity needs less energy for each degree "
            "of temperature change, so the pan heats and cools faster",
            "A lower specific heat capacity always means a lighter, thinner pan, and "
            "a thinner base is what makes it respond faster",
            "A lower specific heat capacity means the pan conducts "
            "electricity better, letting the hob heat it directly, which is "
            "why some induction hobs use it directly",
            "A lower specific heat capacity means the copper melts at a lower "
            "temperature, so it warms through sooner",
        ],
        "correct_index": 0,
        "why": "With less energy needed per degree of change, the same burner "
                "supplies enough energy to shift the pan's temperature more "
                "quickly.",
    },
    {
        "id": "ks4-temperature-changes-shc-s13",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A storage heater is designed to hold as much thermal energy as "
                "possible for a given mass and temperature rise. Explain why it "
                "is filled with bricks of a material with a high specific heat "
                "capacity rather than a low one.",
        "options": [
            "A high specific heat capacity makes the bricks heat up much "
            "faster than a low-capacity material would",
            "A high specific heat capacity lets the bricks store far more "
            "energy for the same mass and temperature rise",
            "A high specific heat capacity means the bricks release their "
            "stored energy instantly once the heater switches off",
            "A high specific heat capacity has no real effect on how much "
            "energy the bricks can store, only on their mass",
        ],
        "correct_index": 1,
        "why": "A higher specific heat capacity means more energy is needed, and "
                "so stored, for the same mass and temperature rise, which is "
                "exactly what a storage heater needs.",
    },
    {
        "id": "ks4-temperature-changes-shc-s14",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A desert can swing from very hot in the day to very cold at "
                "night, while a coastal town at a similar latitude stays much "
                "milder throughout. Suggest why the desert's dry sand and rock "
                "produce such large temperature swings.",
        "options": [
            "Dry sand and rock have a much higher specific heat capacity than "
            "seawater, so they store more energy and release it in sudden bursts once "
            "the sun sets",
            "Deserts simply receive far more sunlight overall than coastal regions "
            "do, whatever the ground beneath them there happens to be made from",
            "Dry sand and rock have a much lower specific heat capacity than "
            "seawater, so a given energy change produces a much bigger "
            "temperature change",
            "Sand and rock cannot store any thermal energy at all, unlike the "
            "water found near the coast",
        ],
        "correct_index": 2,
        "why": "A low specific heat capacity means only a small energy change is "
                "needed to swing the temperature a long way, unlike the large, "
                "steady seawater nearby a coastal town.",
    },
    {
        "id": "ks4-temperature-changes-shc-s15",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "500 g of oil (c = 2100 J/kg°C) and 500 g of water (c = 4200 "
                "J/kg°C) are each heated by an identical 1000 J burst of energy. "
                "Compare the resulting temperature rise of each liquid.",
        "options": [
            "The water rises twice as far, because it can hold more energy "
            "overall than the oil",
            "Both rise by exactly the same amount, since they receive exactly "
            "the same amount of energy",
            "The oil rises half as far, because a lower specific heat "
            "capacity always means a smaller temperature change",
            "The oil rises twice as far, because it needs half as much energy "
            "per kilogram per degree",
        ],
        "correct_index": 3,
        "why": "With mass and energy equal, temperature rise is inversely "
                "proportional to specific heat capacity, and the oil's capacity "
                "is half the water's.",
    },
    {
        "id": "ks4-temperature-changes-shc-s16",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 60 W immersion heater runs for 5.0 minutes in 0.30 kg of a "
                "liquid, raising its temperature by 20 °C. Calculate the specific "
                "heat capacity of the liquid, assuming no energy losses.",
        "options": [
            "3000 J/kg°C",
            "18 000 J/kg°C",
            "300 J/kg°C",
            "600 J/kg°C",
        ],
        "correct_index": 0,
        "why": "The energy supplied is E = Pt = 60 × 300 s = 18 000 J, so c = 18 "
                "000 ÷ (0.30 × 20) = 3000 J/kg°C — the time must first be "
                "converted into seconds.",
    },
    {
        "id": "ks4-temperature-changes-shc-s17",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical 100 W heaters each run for 4.0 minutes, one in 1.0 "
                "kg of water (c = 4200 J/kg°C) and the other in 1.0 kg of engine "
                "oil (c = 2100 J/kg°C). Compare the final temperature rise in "
                "each liquid.",
        "options": [
            "The water rises about twice as far as the oil, because its "
            "specific heat capacity is higher",
            "The oil rises about twice as far as the water, for the same "
            "energy transferred to each",
            "Both liquids rise by exactly the same amount, because both "
            "heaters transfer the same energy",
            "Neither liquid changes temperature without also knowing each "
            "container's starting temperature",
        ],
        "correct_index": 1,
        "why": "With equal energy transferred to equal masses, the liquid with "
                "the lower specific heat capacity, the oil, rises further in "
                "temperature.",
    },
    {
        "id": "ks4-temperature-changes-shc-s18",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 40 g sample of a metal is heated with 936 J of energy and its "
                "temperature rises from 18 °C to 78 °C. Calculate its specific "
                "heat capacity.",
        "options": [
            "23.4 J/kg°C",
            "13 J/kg°C",
            "390 J/kg°C",
            "23 400 J/kg°C",
        ],
        "correct_index": 2,
        "why": "The mass must be converted to kilograms, 0.040 kg, and Δθ = 78 − "
                "18 = 60 °C, so c = 936 ÷ (0.040 × 60) = 390 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-s19",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures the specific heat capacity of a metal block "
                "twice, without insulating it either time, and gets a value "
                "noticeably higher than the textbook value on both attempts. "
                "Explain the likely cause.",
        "options": [
            "The thermometer used must have been broken or badly calibrated in the "
            "same way on both of the student's two attempts",
            "The block itself must have been made from an unusually dense "
            "sample of the metal, however carefully the sample was prepared "
            "beforehand",
            "Repeating the experiment twice doubles the total energy supplied, so the "
            "calculated specific heat capacity comes out twice as large as it should",
            "Some of the heater's energy escapes to the surroundings rather "
            "than heating the block, making the measured Δθ too small",
        ],
        "correct_index": 3,
        "why": "Energy lost to the room means less of it reaches the block, so "
                "the measured temperature rise is smaller than it should be, "
                "inflating the calculated specific heat capacity.",
    },
    {
        "id": "ks4-temperature-changes-shc-s20",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two blocks of the same metal have masses in the ratio 1 : 3. "
                "Both are heated by the same energy input. Compare their "
                "temperature rises.",
        "options": [
            "The smaller block rises three times as far, because the same "
            "energy is shared among fewer particles",
            "The larger block rises three times as far, because it has more "
            "particles to share the temperature change between",
            "Both blocks rise by exactly the same amount, since the material "
            "and energy supplied are identical",
            "The temperature rise cannot depend on mass at all, only on the "
            "specific heat capacity of the metal",
        ],
        "correct_index": 0,
        "why": "For the same material and energy input, temperature rise is "
                "inversely proportional to mass, so the smaller block rises three "
                "times as far.",
    },
    {
        "id": "ks4-temperature-changes-shc-s21",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.25 kg block absorbs energy and its temperature rises from 22 "
                "°C to 82 °C, taking in 10 800 J. Calculate its specific heat "
                "capacity.",
        "options": [
            "491 J/kg°C",
            "720 J/kg°C",
            "72 J/kg°C",
            "43 200 J/kg°C",
        ],
        "correct_index": 1,
        "why": "Δθ = 82 − 22 = 60 °C, so c = 10 800 ÷ (0.25 × 60) = 720 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-s22",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A heater supplies 2000 J of energy to a 1.0 kg block, but only "
                "80% of that energy actually reaches the block, the rest being "
                "lost to the air. The block's specific heat capacity is 400 "
                "J/kg°C. Calculate its actual temperature rise.",
        "options": [
            "5.0 °C",
            "6.25 °C",
            "4.0 °C",
            "1.6 °C",
        ],
        "correct_index": 2,
        "why": "Only 80% of 2000 J, which is 1600 J, actually reaches the block, "
                "so Δθ = 1600 ÷ (1.0 × 400) = 4.0 °C.",
    },
    {
        "id": "ks4-temperature-changes-shc-s23",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why walking barefoot on dry beach sand can burn your "
                "feet on a hot day, while wading into the sea a few metres away "
                "feels comfortably cool, even in the same sunshine.",
        "options": [
            "Sand has a much higher specific heat capacity than seawater, so it takes "
            "in far more energy from the sun and ends up at a much higher temperature",
            "The sea only feels cooler because waves are constantly moving colder "
            "water in towards the beach from far offshore",
            "Sand and seawater always reach the same temperature; the sea "
            "only feels cooler because it is wet",
            "Sand has a much lower specific heat capacity than seawater, so "
            "the same sunlight raises its temperature far more",
        ],
        "correct_index": 3,
        "why": "With a much lower specific heat capacity, sand needs far less "
                "energy to reach a high temperature than the same mass of "
                "seawater exposed to the same sunshine.",
    },
    {
        "id": "ks4-temperature-changes-shc-s24",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.2 kg block of an unknown solid releases 21 600 J as it cools "
                "from 95 °C to 35 °C. Calculate its specific heat capacity.",
        "options": [
            "300 J/kg°C",
            "18 000 J/kg°C",
            "6.0 J/kg°C",
            "360 J/kg°C",
        ],
        "correct_index": 0,
        "why": "Δθ = 95 − 35 = 60 °C, so c = 21 600 ÷ (1.2 × 60) = 300 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-s25",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which single change to the required practical setup would "
                "let a student find the specific heat capacity of a liquid rather "
                "than a solid block, using the same underlying method.",
        "options": [
            "Nothing needs to change — the same solid block also gives the "
            "specific heat capacity of any liquid poured near it",
            "Replace the block with a known mass of the liquid in an "
            "insulated container, and heat it with the same heater",
            "Replace the thermometer with a measuring cylinder, since liquids "
            "need their volume measured instead of temperature",
            "The method cannot be adapted for a liquid, since ΔE = mcΔθ only "
            "applies to solids",
        ],
        "correct_index": 1,
        "why": "The same heater, thermometer and equation work for a known mass "
                "of liquid in an insulated container, in place of the solid "
                "block.",
    },
    {
        "id": "ks4-temperature-changes-shc-s26",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A camper's metal mug and a similarly sized ceramic mug both hold "
                "the same hot drink at the same temperature. The metal mug's "
                "outside feels hotter to touch almost immediately. Suggest what "
                "specific heat capacity alone can and cannot explain about this "
                "observation.",
        "options": [
            "Specific heat capacity fully explains it — metal always has a "
            "far higher specific heat capacity than ceramic",
            "Specific heat capacity cannot explain it at all, since both mugs contain "
            "an identical drink at an identical temperature, so nothing about the "
            "mugs themselves can make any difference",
            "Specific heat capacity explains how much energy each mug itself "
            "stores, but not how quickly that energy reaches the outside "
            "surface",
            "Specific heat capacity only applies to liquids, so it says nothing at "
            "all about either of the two solid mugs holding the drink",
        ],
        "correct_index": 2,
        "why": "Specific heat capacity is about energy stored per degree, not "
                "about how quickly energy moves through a material, so it cannot "
                "by itself explain the difference in feel.",
    },
    {
        "id": "ks4-temperature-changes-shc-h06",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 40 W heater runs for 8.0 minutes, transferring energy to 0.50 "
                "kg of a liquid, and its temperature rises from 18 °C to 50 °C. "
                "Calculate the specific heat capacity of the liquid, assuming no "
                "energy losses.",
        "options": [
            "20 J/kg°C",
            "600 J/kg°C",
            "768 J/kg°C",
            "1200 J/kg°C",
        ],
        "correct_index": 3,
        "why": "E = Pt = 40 × 480 s = 19 200 J, and Δθ = 50 − 18 = 32 °C, so c = "
                "19 200 ÷ (0.50 × 32) = 1200 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h07",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.60 kg block at 90 °C (c = 400 J/kg°C) is placed into 1.5 kg "
                "of water at 20 °C (c = 4200 J/kg°C) in an insulated container. "
                "Calculate the energy released by the block as it cools to 30 °C, "
                "and the resulting rise in the water's temperature.",
        "options": [
            "14 400 J released, warming the water by 2.3 °C",
            "21 600 J released, warming the water by 3.4 °C",
            "14 400 J released, warming the water by 9.5 °C",
            "8400 J released, warming the water by 1.3 °C",
        ],
        "correct_index": 0,
        "why": "The block's Δθ is 90 − 30 = 60 °C, giving 0.60 × 400 × 60 = 14 "
                "400 J, which warms the water by 14 400 ÷ (1.5 × 4200) = 2.3 °C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h08",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A storage heater holds 80 kg of a ceramic material (c = 850 "
                "J/kg°C) and a rival design instead holds 80 kg of water (c = "
                "4200 J/kg°C). Both are heated through the same 35 °C rise. "
                "Calculate how much more energy the water design stores than the "
                "ceramic one.",
        "options": [
            "14.0 MJ",
            "9.38 MJ",
            "2.38 MJ",
            "11.76 MJ",
        ],
        "correct_index": 1,
        "why": "The water stores 80 × 4200 × 35 = 11.76 MJ and the ceramic 80 × "
                "850 × 35 = 2.38 MJ, a difference of 9.38 MJ.",
    },
    {
        "id": "ks4-temperature-changes-shc-h09",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car radiator's cooling system carries 63 kJ of energy away "
                "from the engine into the flowing coolant every 6.0 s. The "
                "coolant enters the radiator at 12 °C and leaves at 42 °C. "
                "Determine the mass of coolant flowing through every 6.0 s. "
                "The specific heat capacity of the coolant is 4200 J/kg°C.",
        "options": [
            "0.54 kg",
            "1.25 kg",
            "0.50 kg",
            "2.25 kg",
        ],
        "correct_index": 2,
        "why": "63 kJ is 63 000 J and Δθ = 42 − 12 = 30 °C, so m = 63 000 ÷ "
                "(4200 × 30) = 0.50 kg.",
    },
    {
        "id": "ks4-temperature-changes-shc-h10",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student mixes 300 g of hot water at 80 °C with 300 g of cold "
                "water at 20 °C, of the same substance, in an insulated cup. "
                "Predict the final steady temperature, and explain your "
                "reasoning.",
        "options": [
            "60 °C, because the hotter water always dominates the final outcome, "
            "contributing two thirds of the final temperature to the colder water's "
            "one third",
            "40 °C, because the colder water always pulls the mixture below the "
            "halfway point between the two",
            "80 °C, because mixing two temperatures never lowers the highest one "
            "present, since the cold water simply warms up to join it",
            "50 °C, because equal masses of the same substance simply average "
            "their two starting temperatures",
        ],
        "correct_index": 3,
        "why": "Equal masses of the same liquid mean equal heat capacity "
                "contributions from each side, so the two temperatures simply "
                "average to 50 °C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h11",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 100 g sample of an alloy is heated by 4200 J, and its "
                "temperature rises by 35 °C. Determine which two metals it is "
                "most likely a mixture of, given aluminium = 900 J/kg°C, iron = "
                "450 J/kg°C, and lead = 130 J/kg°C.",
        "options": [
            "None of the pairs, since the alloy's value of 1200 J/kg°C is "
            "higher than any of the three metals",
            "Lead and iron, since 1200 J/kg°C sits comfortably between their two "
            "listed values of 130 and 450 J/kg°C",
            "Aluminium and iron, since 1200 J/kg°C sits between the two values given "
            "for these two metals",
            "Aluminium and lead, since 1200 J/kg°C sits between their two "
            "values",
        ],
        "correct_index": 0,
        "why": "c = 4200 ÷ (0.100 × 35) = 1200 J/kg°C, which is higher than "
                "aluminium's 900 J/kg°C, so it cannot be a mixture of any two of "
                "these three metals alone.",
    },
    {
        "id": "ks4-temperature-changes-shc-h12",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 25 W heater runs continuously in a 0.20 kg block (c = 500 "
                "J/kg°C) that is losing energy to the room at a steady 10 W once "
                "it reaches 40 °C above room temperature. Explain what happens to "
                "the block's temperature once it reaches that point.",
        "options": [
            "It falls back down, because losing any energy at all always "
            "means the block must be cooling overall",
            "It keeps rising steadily, because the heater is still switched "
            "on and supplying energy the whole time",
            "It stays roughly constant, because the 25 W supplied is partly "
            "balanced by the 10 W lost, though not completely",
            "It stays exactly constant, because the heater's power exactly "
            "equals the energy being lost to the room",
        ],
        "correct_index": 1,
        "why": "The heater still supplies more power, 25 W, than the 10 W being "
                "lost, so there is a net energy input and the temperature keeps "
                "climbing, just more slowly than before.",
    },
    {
        "id": "ks4-temperature-changes-shc-h13",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.0 kg block of metal A (c = 900 J/kg°C) and a 2.0 kg block of "
                "metal B (c = 450 J/kg°C) both start at 20 °C and are each "
                "supplied with 9000 J. Compare their final temperatures.",
        "options": [
            "Metal A reaches 30 °C and metal B reaches 20 °C — B does not "
            "change at all",
            "Metal A reaches 25 °C and metal B reaches 25 °C, since both "
            "received identical energy",
            "Metal A reaches 30 °C and metal B reaches 30 °C — both end at "
            "the same final temperature",
            "Metal A reaches 20 °C and metal B reaches 30 °C — the heavier "
            "block always rises further",
        ],
        "correct_index": 2,
        "why": "Metal A rises by 9000 ÷ (1.0 × 900) = 10 °C to 30 °C, and metal "
                "B rises by 9000 ÷ (2.0 × 450) = 10 °C to 30 °C — a coincidence "
                "of these particular numbers, not a general rule.",
    },
    {
        "id": "ks4-temperature-changes-shc-h14",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that 'doubling the specific heat capacity of "
                "a material always doubles how hot it becomes when heated'.",
        "options": [
            "The claim is correct, because specific heat capacity directly "
            "sets the final temperature reached by a material",
            "The claim is correct, provided the mass of the material being heated "
            "stays exactly the same throughout the whole of the heating process",
            "The claim is incorrect, because specific heat capacity has no connection "
            "at all to how a material's temperature changes, only to how much energy "
            "it can hold in total",
            "The claim is incorrect — a higher specific heat capacity means a "
            "SMALLER temperature rise for the same energy input, not a bigger "
            "one",
        ],
        "correct_index": 3,
        "why": "Since Δθ = ΔE ÷ (mc), doubling c halves the temperature rise for "
                "a given energy input, the opposite of what the claim suggests.",
    },
    {
        "id": "ks4-temperature-changes-shc-h15",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 45 W heater supplies energy to a 0.30 kg block for 4.0 "
                "minutes, and its temperature rises from 20 °C to 68 °C. "
                "Calculate the specific heat capacity of the block.",
        "options": [
            "750 J/kg°C",
            "529 J/kg°C",
            "12.5 J/kg°C",
            "0.75 J/kg°C",
        ],
        "correct_index": 0,
        "why": "E = Pt = 45 × 240 s = 10 800 J, and Δθ = 68 − 20 = 48 °C, so c = "
                "10 800 ÷ (0.30 × 48) = 750 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h16",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 250 g sample of an unknown liquid is heated by 6300 J and its "
                "temperature rises by 15 °C. A second, independent trial with a "
                "fresh 500 g sample of the same liquid and 12 600 J gives the "
                "same 15 °C rise. Explain why both trials agree despite the "
                "different masses and energies used.",
        "options": [
            "They only appear to agree; specific heat capacity actually depends on "
            "the mass of the sample tested, and these two masses happen to fall "
            "either side of the same average value",
            "Both trials scale mass and energy by the same factor, leaving "
            "the ratio ΔE ÷ (m × Δθ) — the specific heat capacity — unchanged",
            "The two trials happen to agree purely by chance, and further repeats at "
            "other masses would very likely disagree",
            "Specific heat capacity only stays constant for masses below 300 g, so "
            "the second trial here should be treated with suspicion",
        ],
        "correct_index": 1,
        "why": "Doubling both the mass and the energy leaves ΔE ÷ m unchanged, "
                "so with the same Δθ, the calculated specific heat capacity comes "
                "out the same both times.",
    },
    {
        "id": "ks4-temperature-changes-shc-h17",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kg block of metal at 150 °C is dropped into 4.0 kg of oil "
                "at 25 °C (c = 2100 J/kg°C) in an insulated container, and the "
                "mixture settles at 45 °C. Calculate the specific heat capacity "
                "of the metal.",
        "options": [
            "560 J/kg°C",
            "1600 J/kg°C",
            "800 J/kg°C",
            "400 J/kg°C",
        ],
        "correct_index": 2,
        "why": "The oil gains 4.0 × 2100 × (45 − 25) = 168 000 J, which the "
                "metal must have released cooling from 150 °C to 45 °C, a fall of "
                "105 °C, so c = 168 000 ÷ (2.0 × 105) = 800 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h18",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A school buys two identical-looking storage heaters, one "
                "advertised as 'high capacity' and one as 'standard capacity', "
                "both the same total mass. Suggest what physical difference "
                "between them is most likely responsible for the 'high capacity' "
                "one storing more energy for the same temperature rise.",
        "options": [
            "The 'high capacity' heater almost certainly runs at a higher "
            "electrical voltage than the standard one",
            "The 'high capacity' heater almost certainly has a larger outer "
            "surface area, letting in more energy overall",
            "The 'high capacity' heater almost certainly reaches a higher "
            "maximum temperature before switching off",
            "The 'high capacity' heater is almost certainly filled with a "
            "material of a higher specific heat capacity",
        ],
        "correct_index": 3,
        "why": "For the same mass and temperature rise, only a higher specific "
                "heat capacity of the filling material lets a heater store more "
                "energy.",
    },
    {
        "id": "ks4-temperature-changes-shc-h19",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 30 W heater supplies energy to a 0.40 kg block for 6.0 "
                "minutes, but a faulty connection means only 90% of the "
                "electrical energy actually reaches the block as heat. Given the "
                "block's temperature rises from 15 °C to 42 °C, calculate its "
                "specific heat capacity.",
        "options": [
            "900 J/kg°C",
            "1000 J/kg°C",
            "15 J/kg°C",
            "1111 J/kg°C",
        ],
        "correct_index": 0,
        "why": "The electrical energy is 30 × 360 = 10 800 J, and 90% of that, "
                "9720 J, reaches the block, so c = 9720 ÷ (0.40 × 27) = 900 "
                "J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h20",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 3.0 kg block of metal at 15 °C is placed into 0.30 kg of water "
                "at 80 °C in an insulated cup, and the mixture settles at 35 °C. "
                "The specific heat capacity of water is 4200 J/kg°C. Calculate "
                "the specific heat capacity of the metal.",
        "options": [
            "1680 J/kg°C",
            "945 J/kg°C",
            "540 J/kg°C",
            "2835 J/kg°C",
        ],
        "correct_index": 1,
        "why": "The water releases 0.30 × 4200 × (80 − 35) = 56 700 J, which the "
                "metal absorbs warming from 15 °C to 35 °C, a rise of 20 °C, so c "
                "= 56 700 ÷ (3.0 × 20) = 945 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h21",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a scientist measuring the specific heat capacity of "
                "a brand-new material would repeat the experiment several times "
                "with different masses of the sample, rather than relying on just "
                "one measurement.",
        "options": [
            "Repeating with different masses is required because specific heat "
            "capacity genuinely changes with the amount of sample used, so several "
            "masses are needed to find its true average value",
            "Repeating with different masses is the only way to convert the units of "
            "specific heat capacity into joules per kilogram per degree Celsius "
            "correctly",
            "Repeating checks that the calculated value stays roughly "
            "constant across different masses, giving confidence it is a "
            "genuine property of the material",
            "Repeating is unnecessary scientifically, and is done only to "
            "make the results look more convincing in a report",
        ],
        "correct_index": 2,
        "why": "Specific heat capacity should be a fixed property of the "
                "material, so getting a similar value across different masses "
                "supports that the measurement is reliable.",
    },
    {
        "id": "ks4-temperature-changes-shc-h22",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.80 kg block absorbs 28 800 J and warms from 15 °C to 75 °C. "
                "A second, larger block of the same material absorbs 43 200 J and "
                "warms by the same 60 °C. Calculate the mass of the second block.",
        "options": [
            "1.5 kg",
            "0.60 kg",
            "2.4 kg",
            "1.2 kg",
        ],
        "correct_index": 3,
        "why": "The first block gives c = 28 800 ÷ (0.80 × 60) = 600 J/kg°C, so "
                "the second block's mass is m = 43 200 ÷ (600 × 60) = 1.2 kg.",
    },
    {
        "id": "ks4-temperature-changes-shc-h23",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.0 kg block of metal at 200 °C is dropped into 2.0 kg of "
                "water at 15 °C in an insulated container, and the final "
                "temperature is 25 °C. Calculate the specific heat capacity of "
                "the metal, given water's specific heat capacity is 4200 J/kg°C.",
        "options": [
            "480 J/kg°C",
            "240 J/kg°C",
            "960 J/kg°C",
            "48 J/kg°C",
        ],
        "correct_index": 0,
        "why": "The water gains 2.0 × 4200 × (25 − 15) = 84 000 J, which the "
                "metal released cooling by 200 − 25 = 175 °C, so c = 84 000 ÷ "
                "(1.0 × 175) = 480 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h24",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A factory needs a liquid to carry waste energy away from a furnace "
                "through a pipe loop. Explain why a liquid with a HIGH specific heat "
                "capacity is generally preferred over one with a low value, given "
                "both are otherwise equally suitable.",
        "options": [
            "A high specific heat capacity makes the liquid flow faster through the "
            "pipework, carrying energy away from the furnace much more quickly",
            "A high specific heat capacity lets the liquid absorb a large amount of "
            "the furnace's excess energy without its own temperature rising too far",
            "A high specific heat capacity always means a cheaper liquid, which "
            "matters more to a factory than performance does",
            "A high specific heat capacity means the liquid boils at a much lower "
            "temperature, so it carries energy away as a vapour and protects the "
            "furnace from damage",
        ],
        "correct_index": 1,
        "why": "A liquid with a high specific heat capacity can carry away a great "
               "deal of thermal energy from the furnace while its own temperature "
               "stays relatively controlled.",
    },
    {
        "id": "ks4-temperature-changes-shc-h25",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.50 kg block is heated by a 25 W heater for exactly 10 "
                "minutes, and its temperature rises from 18 °C to 78 °C. "
                "Determine what fraction of the electrical energy supplied "
                "actually reached the block as useful thermal energy, given the "
                "block's true specific heat capacity is 400 J/kg°C.",
        "options": [
            "100%, since every joule that the heater supplies must end up inside the "
            "block itself",
            "60%, since 15 000 J was supplied and 6000 J of it was lost warming the "
            "surrounding air rather than the block",
            "80%, since only 12 000 J of the 15 000 J supplied matches the 12 "
            "000 J actually needed",
            "125%, since the block needed more energy than was supplied",
        ],
        "correct_index": 2,
        "why": "The heater supplies 25 × 600 = 15 000 J, but the block only "
                "needs 0.50 × 400 × 60 = 12 000 J to reach that temperature rise, "
                "so 12 000 ÷ 15 000 = 80% of the supplied energy actually reached "
                "it.",
    },
    {
        "id": "ks4-temperature-changes-shc-h26",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A double-glazed window is filled with a gas of low specific heat "
                "capacity between its two panes, rather than water. Suggest why a "
                "low specific heat capacity is not actually the main property the "
                "manufacturer is relying on for insulation, even though it is "
                "often mentioned.",
        "options": [
            "A low specific heat capacity always means poor insulation, so the "
            "manufacturer's claim about the gas sealed between the two panes must "
            "simply be false, and the window would insulate better with water in the "
            "gap",
            "Specific heat capacity is actually the only property that matters for "
            "insulating a window, so the statement is entirely correct as it stands "
            "and needs no qualification of any kind, since a window's whole job is to "
            "hold energy rather than slow its passage",
            "Gases cannot have a specific heat capacity at all, since the "
            "term only applies to solids and liquids",
            "Specific heat capacity affects how much a material's own "
            "temperature changes for a given energy transfer, not how easily "
            "energy passes through it — the gas's real job is resisting the "
            "flow of energy across the gap",
        ],
        "correct_index": 3,
        "why": "Insulation is about resisting the transfer of energy through a "
                "material, a separate property from specific heat capacity, which "
                "is about how much a material's own temperature changes once "
                "energy has been transferred to it.",
    },

    # ── specific-latent-heat ────────────────────────────────────────────
    {
        "id": "ks4-specific-latent-heat-e06",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which term, fusion or vaporisation, describes the change "
                "between a solid and a liquid.",
        "options": [
            "Fusion",
            "Vaporisation",
            "Sublimation",
            "Condensation",
        ],
        "correct_index": 0,
        "why": "Fusion names the solid-liquid change; vaporisation is the "
                "liquid-gas change.",
    },
    {
        "id": "ks4-specific-latent-heat-e07",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium has a specific latent heat of fusion of 390 000 J/kg. "
                "Calculate the energy needed to melt 2.0 kg of aluminium already "
                "at its melting point.",
        "options": [
            "195 000 J",
            "780 000 J",
            "390 000 J",
            "1 560 000 J",
        ],
        "correct_index": 1,
        "why": "E = mL = 2.0 × 390 000 = 780 000 J.",
    },
    {
        "id": "ks4-specific-latent-heat-e08",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A substance has a specific latent heat of fusion of 150 000 "
                "J/kg. If 60 000 J of energy melts a sample of it at its melting "
                "point, calculate the mass of the sample.",
        "options": [
            "2.5 kg",
            "40 kg",
            "0.40 kg",
            "4.0 kg",
        ],
        "correct_index": 2,
        "why": "Rearranging E = mL gives m = E ÷ L = 60 000 ÷ 150 000 = 0.40 kg.",
    },
    {
        "id": "ks4-specific-latent-heat-e09",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Lead has a specific latent heat of fusion of about 23 000 J/kg "
                "and iron about 247 000 J/kg. State which needs more energy to "
                "melt 1 kg of it.",
        "options": [
            "Lead, because a lower latent heat needs more energy",
            "Iron, but only because it has the higher melting point, not the "
            "higher latent heat",
            "Both need exactly the same energy, since 1 kg is 1 kg whatever "
            "the substance",
            "Iron, because 247 000 J/kg is greater than 23 000 J/kg",
        ],
        "correct_index": 3,
        "why": "A higher specific latent heat of fusion directly means more "
                "energy is needed per kilogram, and iron's value is the greater "
                "of the two.",
    },
    {
        "id": "ks4-specific-latent-heat-e10",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which is true for water: the specific latent heat of "
                "vaporisation is much greater than the specific latent heat of "
                "fusion, or much smaller.",
        "options": [
            "Much greater — vaporisation completely separates the particles, "
            "fusion only frees them from a fixed lattice",
            "Much smaller — vaporisation needs far less energy than melting, because "
            "a gas's particles are already free to move",
            "Exactly equal — both changes need precisely the same amount of energy "
            "for any pure substance you might test",
            "Neither — the two quantities cannot be compared with each other in any "
            "useful way",
        ],
        "correct_index": 0,
        "why": "Boiling must fully separate the particles against all the "
                "intermolecular forces, while melting only frees them from fixed "
                "positions, so vaporisation needs far more energy.",
    },
    {
        "id": "ks4-specific-latent-heat-e11",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wax has a specific latent heat of fusion of 200 000 J/kg. "
                "Calculate the energy released when 0.30 kg of the liquid wax "
                "freezes completely at its freezing point.",
        "options": [
            "600 000 J",
            "60 000 J",
            "6 000 J",
            "200 000 J",
        ],
        "correct_index": 1,
        "why": "E = mL = 0.30 × 200 000 = 60 000 J, released as the wax freezes.",
    },
    {
        "id": "ks4-specific-latent-heat-e12",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the quantity represented by the symbol L in the equation E "
                "= mL.",
        "options": [
            "The length of the container holding the substance",
            "The number of particles in the substance",
            "The specific latent heat of the substance",
            "The temperature at which the substance changes state",
        ],
        "correct_index": 2,
        "why": "L stands for specific latent heat, the energy needed per "
                "kilogram for the change of state.",
    },
    {
        "id": "ks4-specific-latent-heat-s26",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.50 kg sample absorbs 32 000 J of energy as it melts "
                "completely at its melting point. Identify the metal, given "
                "copper = 205 000 J/kg, silver = 105 000 J/kg, and gold = 64 000 "
                "J/kg.",
        "options": [
            "Silver, since 32 000 ÷ 0.50 = 105 000 J/kg",
            "Copper, since 32 000 ÷ 0.50 = 205 000 J/kg",
            "None of the three, since the value comes out at 16 000 J/kg",
            "Gold, since 32 000 ÷ 0.50 = 64 000 J/kg",
        ],
        "correct_index": 3,
        "why": "L = E ÷ m = 32 000 ÷ 0.50 = 64 000 J/kg, matching gold exactly.",
    },
    {
        "id": "ks4-specific-latent-heat-s07",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "0.20 kg of steam at 100 °C condenses completely, then the water "
                "formed cools to 60 °C. Calculate the total energy released. The "
                "specific latent heat of vaporisation of water is 2 260 000 J/kg "
                "and its specific heat capacity is 4200 J/kg°C.",
        "options": [
            "485 600 J",
            "452 000 J",
            "33 600 J",
            "536 000 J",
        ],
        "correct_index": 0,
        "why": "Condensing releases 0.20 × 2 260 000 = 452 000 J, and cooling by "
                "40 °C releases 0.20 × 4200 × 40 = 33 600 J, giving 485 600 J in "
                "total.",
    },
    {
        "id": "ks4-specific-latent-heat-s08",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1000 W heater runs for 334 s, but only 50% of the electrical "
                "energy actually reaches a block of ice at its melting point as "
                "useful thermal energy. The specific latent heat of fusion of ice "
                "is 334 000 J/kg. Calculate the mass of ice melted.",
        "options": [
            "1.0 kg",
            "0.50 kg",
            "0.25 kg",
            "2.0 kg",
        ],
        "correct_index": 1,
        "why": "The electrical energy is 1000 × 334 = 334 000 J, and 50% of "
                "that, 167 000 J, reaches the ice, so m = 167 000 ÷ 334 000 = "
                "0.50 kg.",
    },
    {
        "id": "ks4-specific-latent-heat-s09",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kg block of a material needs 940 000 J to melt completely "
                "at its melting point. Determine its specific latent heat of "
                "fusion, and state whether it could be ice (334 000 J/kg) or lead "
                "(23 000 J/kg).",
        "options": [
            "235 000 J/kg, since the mass is divided out twice",
            "1 880 000 J/kg, since the mass multiplies rather than divides",
            "470 000 J/kg, which matches neither ice nor lead",
            "470 000 J/kg, which happens to match the value for ice exactly",
        ],
        "correct_index": 2,
        "why": "L = E ÷ m = 940 000 ÷ 2.0 = 470 000 J/kg, which is higher than "
                "both of the named substances.",
    },
    {
        "id": "ks4-specific-latent-heat-s10",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "50 kg of water freezes into ice on the surface of a pond "
                "containing 5000 kg of liquid water beneath it. Using the "
                "specific latent heat of fusion of water (334 000 J/kg) and its "
                "specific heat capacity (4200 J/kg°C), estimate the resulting "
                "rise in temperature of the water beneath, assuming all the "
                "released energy warms it.",
        "options": [
            "About 8.0 °C",
            "About 0.080 °C",
            "About 80 °C",
            "About 0.80 °C",
        ],
        "correct_index": 3,
        "why": "Freezing releases 50 × 334 000 = 16 700 000 J, which warms the "
                "5000 kg of water by 16 700 000 ÷ (5000 × 4200) ≈ 0.80 °C.",
    },
    {
        "id": "ks4-specific-latent-heat-s11",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate how much more energy is needed to completely boil away "
                "2.0 kg of water at 100 °C than to melt the same mass of ice at 0 "
                "°C. Use Lf = 334 000 J/kg and Lv = 2 260 000 J/kg.",
        "options": [
            "3 852 000 J",
            "5 188 000 J",
            "1 926 000 J",
            "4 520 000 J",
        ],
        "correct_index": 0,
        "why": "Boiling needs 2.0 × 2 260 000 = 4 520 000 J and melting needs "
                "2.0 × 334 000 = 668 000 J, a difference of 3 852 000 J.",
    },
    {
        "id": "ks4-specific-latent-heat-s12",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An industrial heater rated at 2000 W runs for 167 s to melt a "
                "block of ice that is already at 0 °C. The specific latent heat "
                "of fusion of ice is 334 000 J/kg. Calculate the mass of ice "
                "melted, assuming no energy losses.",
        "options": [
            "0.50 kg",
            "1.0 kg",
            "2.0 kg",
            "334 kg",
        ],
        "correct_index": 1,
        "why": "E = Pt = 2000 × 167 = 334 000 J, so m = E ÷ L = 334 000 ÷ 334 "
                "000 = 1.0 kg.",
    },
    {
        "id": "ks4-specific-latent-heat-s13",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 500 W heater is used to melt 1.0 kg of aluminium already at "
                "its melting point. The specific latent heat of fusion of "
                "aluminium is 390 000 J/kg. Calculate the minimum time needed, "
                "assuming no energy losses.",
        "options": [
            "390 s",
            "1560 s",
            "780 s",
            "0.78 s",
        ],
        "correct_index": 2,
        "why": "E = mL = 1.0 × 390 000 = 390 000 J, so t = E ÷ P = 390 000 ÷ 500 "
                "= 780 s.",
    },
    {
        "id": "ks4-specific-latent-heat-s14",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student uses ΔE = mcΔθ to calculate the energy needed to melt "
                "0.40 kg of ice at 0 °C, reasoning that 'Δθ = 0 during melting, "
                "so no energy is needed'. Identify the error in this reasoning.",
        "options": [
            "There is no error — melting an ice cube at 0 °C genuinely needs no "
            "energy supplied to it at all, since nothing gets hotter",
            "The error is only that Δθ should have been measured in kelvin rather "
            "than in degrees Celsius",
            "The error is that mass should have been left out of the "
            "calculation completely, not about which equation happens to give "
            "a convenient zero answer",
            "ΔE = mcΔθ only applies when temperature changes; melting needs E "
            "= mL instead, which has no Δθ term to make the answer zero",
        ],
        "correct_index": 3,
        "why": "ΔE = mcΔθ measures a temperature change, which is zero during "
                "melting; the right equation, E = mL, has no such term, so it "
                "still gives a real energy value.",
    },
    {
        "id": "ks4-specific-latent-heat-s15",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two ice cubes of the same substance have masses in the ratio 1 : "
                "4. Compare the energy needed to melt each cube completely at 0 "
                "°C.",
        "options": [
            "The larger cube needs four times as much energy as the smaller "
            "one",
            "The larger cube needs a quarter as much energy, since it melts "
            "faster",
            "Both need exactly the same energy, since they are made of the "
            "same substance",
            "The larger cube needs sixteen times as much energy, since volume "
            "scales as the cube of size",
        ],
        "correct_index": 0,
        "why": "E = mL, so with the same latent heat, energy needed is directly "
                "proportional to mass, and the larger cube has four times the "
                "mass.",
    },
    {
        "id": "ks4-specific-latent-heat-s16",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a scientist can identify an unknown pure solid by "
                "melting a sample and measuring the energy needed per kilogram, "
                "in the same way density or specific heat capacity can be used.",
        "options": [
            "Specific latent heat of fusion changes with the size of the sample, so "
            "bigger samples always identify more reliably than small ones do",
            "Specific latent heat of fusion is a fixed property of a pure "
            "substance, so a matching measured value points to a known "
            "material",
            "Specific latent heat of fusion is the same for every solid substance, so "
            "it can never help to identify which one of them a sample is",
            "Specific latent heat of fusion depends only on the starting "
            "temperature of the sample, not on what it is made from",
        ],
        "correct_index": 1,
        "why": "Like density and specific heat capacity, specific latent heat of "
                "fusion is a characteristic value for a given pure substance, so "
                "it can help identify it.",
    },
    {
        "id": "ks4-specific-latent-heat-s17",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Hailstones falling from a storm cloud absorb energy from the air "
                "as they melt on their way down and after landing. Suggest what "
                "effect this has on the air temperature near the ground during a "
                "hailstorm.",
        "options": [
            "It always makes the air warmer, because melting always releases "
            "energy to the surroundings",
            "It has no effect at all, because melting hail is a chemical "
            "change with an energy cost of its own",
            "It can make the air feel colder, because the melting hail "
            "absorbs energy from its surroundings",
            "It only affects the ground itself, and never the air above it",
        ],
        "correct_index": 2,
        "why": "Melting takes in energy from the surroundings, so air near a "
                "large amount of melting hail can lose energy and feel colder.",
    },
    {
        "id": "ks4-specific-latent-heat-s18",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.60 kg block of ice at 0 °C is supplied with 150 000 J of "
                "energy. The specific latent heat of fusion of ice is 334 000 "
                "J/kg. Determine whether the block fully melts.",
        "options": [
            "Yes — 150 000 J is comfortably more than enough energy to melt all 0.60 "
            "kg of the ice",
            "Yes, exactly — the energy supplied and the energy needed match each "
            "other precisely",
            "No — none of the ice melts at all until the full 200 400 J has been "
            "supplied, because a block melts only as a whole",
            "No — 200 400 J would be needed to melt it completely, more than "
            "the 150 000 J supplied",
        ],
        "correct_index": 3,
        "why": "Melting the whole block needs 0.60 × 334 000 = 200 400 J, more "
                "than the 150 000 J supplied, so only part of it melts, "
                "progressively, as energy is added.",
    },
    {
        "id": "ks4-specific-latent-heat-s19",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A defrosting heater rated at 167 W is only 50% efficient at "
                "transferring energy into a 0.50 kg block of frost, treated as "
                "ice, at its melting point. The specific latent heat of fusion of "
                "ice is 334 000 J/kg. Calculate the minimum time needed to melt "
                "the frost completely.",
        "options": [
            "2000 s",
            "1000 s",
            "4000 s",
            "500 s",
        ],
        "correct_index": 0,
        "why": "Melting needs 0.50 × 334 000 = 167 000 J usefully, so 334 000 J "
                "of electrical energy must be supplied at 50% efficiency, taking "
                "334 000 ÷ 167 = 2000 s.",
    },
    {
        "id": "ks4-specific-latent-heat-s20",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 250 g sample of a substance needs 42 000 J to melt completely "
                "at its melting point. Calculate its specific latent heat of "
                "fusion in J/kg.",
        "options": [
            "168 J/kg",
            "168 000 J/kg",
            "1 680 000 J/kg",
            "16 800 J/kg",
        ],
        "correct_index": 1,
        "why": "The mass must be converted to kilograms, 0.250 kg, so L = E ÷ m "
                "= 42 000 ÷ 0.250 = 168 000 J/kg.",
    },
    {
        "id": "ks4-specific-latent-heat-s21",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates a specific latent heat using an energy in "
                "joules and a mass in kilograms. State the correct unit for the "
                "answer.",
        "options": [
            "J/kg°C",
            "kg/J",
            "J/kg",
            "J",
        ],
        "correct_index": 2,
        "why": "Dividing an energy in joules by a mass in kilograms gives an "
                "answer in joules per kilogram, J/kg.",
    },
    {
        "id": "ks4-specific-latent-heat-s22",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Although the air temperature above a frozen lake stays below 0 "
                "°C all day, patches of the ice surface can still absorb enough "
                "energy from direct sunlight to begin melting. Explain how this "
                "is possible.",
        "options": [
            "It is not possible — ice can never begin to melt anywhere while the air "
            "temperature above it stays below 0 °C all day long, whatever else "
            "reaches it",
            "The ice must be receiving energy conducted up through the lake bed from "
            "underground, which is the only route warm enough to melt ice while the "
            "air above stays below 0 °C",
            "The measurement of the air temperature must simply be incorrect",
            "Sunlight can transfer enough energy directly to the ice's "
            "surface to supply the latent heat needed for melting, even while "
            "the surrounding air stays cold",
        ],
        "correct_index": 3,
        "why": "Energy transfer to the ice's surface depends on what reaches it "
                "directly, such as sunlight, not on the surrounding air "
                "temperature alone.",
    },
    {
        "id": "ks4-specific-latent-heat-s23",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 100 W heater and a 400 W heater are each used to melt an "
                "identical block of ice at 0 °C. Compare how long each takes.",
        "options": [
            "The 400 W heater takes a quarter of the time, because it "
            "transfers energy four times as fast",
            "The 400 W heater takes four times as long, because more power "
            "always means a slower process",
            "Both take exactly the same time, because the mass and latent "
            "heat of the ice are unchanged",
            "The 100 W heater takes a quarter of the time, because lower "
            "power heaters are more efficient",
        ],
        "correct_index": 0,
        "why": "The energy needed is fixed by E = mL, so a heater transferring "
                "energy four times as fast takes a quarter of the time.",
    },
    {
        "id": "ks4-specific-latent-heat-s24",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Equal masses of copper (Lf = 205 000 J/kg), tin (Lf = 59 000 "
                "J/kg) and zinc (Lf = 113 000 J/kg) are each melted. Rank them "
                "from least to most energy needed.",
        "options": [
            "Copper, zinc, tin",
            "Tin, zinc, copper",
            "Zinc, tin, copper",
            "Tin, copper, zinc",
        ],
        "correct_index": 1,
        "why": "For equal mass, energy needed increases with specific latent "
                "heat, so the order is tin, then zinc, then copper.",
    },
    {
        "id": "ks4-specific-latent-heat-s25",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A substance has a specific latent heat of fusion of 180 kJ/kg. "
                "Calculate the energy needed to melt 4.0 kg of it at its melting "
                "point, giving your answer in joules.",
        "options": [
            "720 J",
            "45 000 J",
            "720 000 J",
            "7 200 000 J",
        ],
        "correct_index": 2,
        "why": "180 kJ/kg is 180 000 J/kg, so E = mL = 4.0 × 180 000 = 720 000 "
                "J.",
    },
    {
        "id": "ks4-specific-latent-heat-h06",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kg block of aluminium at 20 °C is heated until it "
                "completely melts at its melting point of 660 °C. Aluminium has a "
                "specific heat capacity of 900 J/kg°C and a specific latent heat "
                "of fusion of 390 000 J/kg. Calculate the total energy needed.",
        "options": [
            "1 152 000 J",
            "780 000 J",
            "1 968 000 J",
            "1 932 000 J",
        ],
        "correct_index": 3,
        "why": "Heating to the melting point needs 2.0 × 900 × 640 = 1 152 000 "
                "J, and melting needs 2.0 × 390 000 = 780 000 J, giving 1 932 000 "
                "J in total.",
    },
    {
        "id": "ks4-specific-latent-heat-h07",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "500 g of steam at 100 °C is cooled until it becomes ice at 0 °C. "
                "Calculate the total energy released, using Lv = 2 260 000 J/kg, "
                "c = 4200 J/kg°C, and Lf = 334 000 J/kg for water.",
        "options": [
            "1 507 000 J",
            "1 297 000 J",
            "1 340 000 J",
            "1 130 000 J",
        ],
        "correct_index": 0,
        "why": "Condensing releases 0.50 × 2 260 000 = 1 130 000 J, cooling to 0 "
                "°C releases 0.50 × 4200 × 100 = 210 000 J, and freezing releases "
                "0.50 × 334 000 = 167 000 J, a total of 1 507 000 J.",
    },
    {
        "id": "ks4-specific-latent-heat-h08",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A furnace heats and melts a 2.0 kg block of aluminium: warming "
                "it from 20 °C to its melting point of 660 °C needs 1 152 000 J, "
                "and then melting it needs a further 780 000 J. The furnace is "
                "only 80% efficient at transferring its energy into the block. "
                "Calculate the total electrical energy it must supply.",
        "options": [
            "1 932 000 J",
            "2 415 000 J",
            "1 545 600 J",
            "3 220 000 J",
        ],
        "correct_index": 1,
        "why": "The useful energy needed is 1 152 000 + 780 000 = 1 932 000 J, "
                "so at 80% efficiency the furnace must supply 1 932 000 ÷ 0.80 = "
                "2 415 000 J.",
    },
    {
        "id": "ks4-specific-latent-heat-h09",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample has a measured specific heat capacity of 900 J/kg°C and "
                "a measured specific latent heat of fusion of 390 000 J/kg. "
                "Candidate A has c = 900 J/kg°C and Lf = 390 000 J/kg. Candidate "
                "B has c = 900 J/kg°C and Lf = 234 000 J/kg. Identify the better "
                "match, and explain why.",
        "options": [
            "Candidate B, because a lower latent heat is always the more "
            "likely match for a real substance, regardless of what the "
            "measured sample actually shows",
            "Either candidate is an equally good match, since both of them share "
            "exactly the same specific heat capacity value",
            "Candidate A, because both of its values match the measured "
            "sample exactly, while candidate B's latent heat does not",
            "Neither candidate can be a match, since two substances cannot "
            "share the same specific heat capacity",
        ],
        "correct_index": 2,
        "why": "A genuine match needs both properties to agree; candidate A's "
                "latent heat matches exactly, while candidate B's does not.",
    },
    {
        "id": "ks4-specific-latent-heat-h10",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pond has a surface area of 40 m² and forms a layer of ice 5.0 "
                "cm thick. Ice has a density of 900 kg/m³ and a specific latent "
                "heat of fusion of 334 000 J/kg. Calculate the energy released as "
                "this layer of ice forms from liquid water.",
        "options": [
            "300.6 MJ",
            "1202.4 MJ",
            "0.668 MJ",
            "601.2 MJ",
        ],
        "correct_index": 3,
        "why": "The ice's volume is 40 × 0.05 = 2.0 m³, its mass is 2.0 × 900 = "
                "1800 kg, and the energy released is 1800 × 334 000 = 601 200 000 "
                "J, which is 601.2 MJ.",
    },
    {
        "id": "ks4-specific-latent-heat-h11",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates: 'mass = 0.20 kg, specific latent heat = "
                "334 000 J/kg, so energy = specific latent heat ÷ mass = 334 000 "
                "÷ 0.20 = 1 670 000 J.' Identify the error in this working.",
        "options": [
            "The equation has been inverted — E = mL means multiplying mass "
            "by latent heat, not dividing latent heat by mass",
            "There is no error — 1 670 000 J is the correct answer, since dividing by "
            "a mass smaller than 1 kg must give a larger energy",
            "The error is that the mass should have been converted into grams before "
            "dividing",
            "The error is that the specific latent heat value the student was given "
            "for the ice must itself have been wrong",
        ],
        "correct_index": 0,
        "why": "E = mL requires multiplying the mass by the specific latent "
                "heat, not dividing the latent heat by the mass.",
    },
    {
        "id": "ks4-specific-latent-heat-h12",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 400 W heater runs for 1000 s and is 75% efficient at "
                "transferring its energy into a 0.80 kg sample at its melting "
                "point, which then fully melts. Determine the sample's specific "
                "latent heat of fusion, and state whether it best matches ice "
                "(334 000 J/kg) or lead (23 000 J/kg).",
        "options": [
            "300 000 J/kg, closest to ice, though a little lower",
            "375 000 J/kg, closest to ice, though slightly higher",
            "500 000 J/kg, closest to neither",
            "23 000 J/kg, matches lead",
        ],
        "correct_index": 1,
        "why": "The electrical energy is 400 × 1000 = 400 000 J, and 75% of "
                "that, 300 000 J, is useful, so L = 300 000 ÷ 0.80 = 375 000 "
                "J/kg.",
    },
    {
        "id": "ks4-specific-latent-heat-h13",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student suggests that the energy needed to sublime a solid "
                "directly into a gas should be roughly the sum of its specific "
                "latent heat of fusion and its specific latent heat of "
                "vaporisation, since both bonds must eventually be overcome. "
                "Evaluate this suggestion.",
        "options": [
            "This is wrong, because sublimation involves no melting step, so only the "
            "latent heat of vaporisation is relevant to the energy that the change of "
            "state actually needs",
            "This is wrong, because sublimation always needs far less energy than "
            "either fusion or vaporisation would need alone, since it takes a short "
            "cut past the liquid stage",
            "This is a reasonable estimate, because sublimation must free the "
            "particles from the lattice and then fully separate them, similar "
            "to melting followed by boiling",
            "This is correct, because sublimation and fusion are always "
            "identical processes at any pressure",
        ],
        "correct_index": 2,
        "why": "Sublimation achieves the same end result as melting followed by "
                "boiling, so it needs roughly as much energy as the two combined.",
    },
    {
        "id": "ks4-specific-latent-heat-h14",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A factory needs to melt 5.0 kg of a metal (Lf = 205 000 J/kg) "
                "within 500 s. One available heater delivers 1800 W and a second "
                "delivers 2200 W, both assumed 100% efficient. Determine which "
                "heater, if either, can complete the job in time.",
        "options": [
            "Only the 1800 W heater, since the more powerful 2200 W heater would "
            "overheat and spoil the metal",
            "Both heaters easily complete the job well within the time limit",
            "Neither heater can complete the job, since both would take longer than "
            "the 500 s the factory has available for each batch",
            "Only the 2200 W heater, since the 1800 W heater would take about "
            "569 s, more than the 500 s available",
        ],
        "correct_index": 3,
        "why": "Melting needs 5.0 × 205 000 = 1 025 000 J; the 1800 W heater "
                "takes about 569 s (too slow), but the 2200 W heater takes about "
                "466 s, within the 500 s available.",
    },
    {
        "id": "ks4-specific-latent-heat-h15",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical heaters melt two identical blocks of ice, but "
                "heater A is 100% efficient and heater B is only 50% efficient at "
                "transferring its energy into the ice. Compare how long each "
                "heater takes.",
        "options": [
            "Heater B takes twice as long, because only half of its energy "
            "usefully reaches the ice each second",
            "Heater B takes half as long, because a less efficient heater "
            "always runs hotter",
            "Both take exactly the same time, because efficiency only affects "
            "electricity cost, not melting time",
            "Heater A takes twice as long, because a highly efficient heater "
            "transfers energy more gently",
        ],
        "correct_index": 0,
        "why": "Only half of heater B's power usefully reaches the ice each "
                "second, so it takes twice as long to deliver the same useful "
                "energy.",
    },
    {
        "id": "ks4-specific-latent-heat-h16",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Estimate how much MORE energy 0.020 kg of steam at 100 °C "
                "releases onto skin than the same mass of already-boiled water at "
                "100 °C releases while cooling by just 5 °C, using Lv = 2 260 000 "
                "J/kg and c = 4200 J/kg°C for water.",
        "options": [
            "45 620 J",
            "44 780 J",
            "45 200 J",
            "420 J",
        ],
        "correct_index": 1,
        "why": "The steam releases 0.020 × 2 260 000 = 45 200 J condensing, and "
                "the water releases only 0.020 × 4200 × 5 = 420 J cooling, a "
                "difference of 44 780 J.",
    },
    {
        "id": "ks4-specific-latent-heat-h17",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.0 kg block of a metal at 20 °C is heated until it just melts "
                "at 220 °C, needing 300 000 J in total. Melting it needs 80 000 J "
                "of that total, and its specific latent heat of fusion is 80 000 "
                "J/kg. Calculate the metal's specific heat capacity.",
        "options": [
            "1500 J/kg°C",
            "550 J/kg°C",
            "1100 J/kg°C",
            "1000 J/kg°C",
        ],
        "correct_index": 2,
        "why": "Heating alone needs 300 000 − 80 000 = 220 000 J over a rise of "
                "220 − 20 = 200 °C, so c = 220 000 ÷ (1.0 × 200) = 1100 J/kg°C.",
    },
    {
        "id": "ks4-specific-latent-heat-h18",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates the total energy to heat then melt a solid "
                "by working out ΔE = mcΔθ for the whole temperature range "
                "including the melting point, and completely ignoring E = mL. "
                "Evaluate the size of the error this produces.",
        "options": [
            "The result will be exactly correct, because ΔE = mcΔθ already accounts "
            "for the change of state within the value of c for that material",
            "The result will be too large, because ΔE = mcΔθ always overestimates the "
            "energy needed anywhere near a substance's melting point",
            "There is no error, because E = mL is only relevant for liquids turning "
            "into gases, while ΔE = mcΔθ covers everything a melting solid needs",
            "The result will be too small, because it leaves out the extra "
            "energy needed to actually break the solid's lattice during "
            "melting",
        ],
        "correct_index": 3,
        "why": "ΔE = mcΔθ never includes the extra energy a change of state "
                "needs, so ignoring E = mL always makes the total come out too "
                "small.",
    },
    {
        "id": "ks4-specific-latent-heat-h19",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company wants to design a reusable ice pack that stays at a "
                "very low, steady temperature for as long as possible after being "
                "removed from a freezer. Suggest why a filling with a HIGH "
                "specific latent heat of fusion, rather than a low one, would "
                "help achieve this.",
        "options": [
            "A high specific latent heat of fusion means more energy must be "
            "absorbed from the surroundings before the pack fully melts, "
            "keeping it cold for longer",
            "A high specific latent heat of fusion means the pack freezes solid much "
            "faster in the freezer before it is taken out and used, so it starts its "
            "job sooner",
            "A high specific latent heat of fusion means the pack reaches a lower "
            "starting temperature in the freezer than a low-value filling would, so "
            "it begins colder",
            "Specific latent heat of fusion has no effect on how long a "
            "melting ice pack stays cold",
        ],
        "correct_index": 0,
        "why": "A higher specific latent heat means the pack must draw in more "
                "energy from its surroundings before it finishes melting, so it "
                "stays at its cold melting point for longer.",
    },
    {
        "id": "ks4-specific-latent-heat-h20",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'Since E = mL has no temperature term, the "
                "specific latent heat of a substance must be completely unrelated "
                "to its melting or boiling point.' Evaluate this statement.",
        "options": [
            "The statement is correct — the two properties are entirely unconnected, "
            "because melting point is fixed by the pressure the substance is under, "
            "while latent heat is not affected by pressure in any way at all",
            "The statement is incorrect — latent heat and melting or boiling "
            "point are different properties, but both are still linked to the "
            "strength of the same intermolecular forces holding the substance "
            "together",
            "The statement is correct, because melting point depends on the mass of "
            "the sample while latent heat does not depend on it at all",
            "The statement is incorrect, because E = mL secretly does include "
            "a hidden temperature term",
        ],
        "correct_index": 1,
        "why": "Both properties arise from the same intermolecular forces, even "
                "though they measure different things and neither equation for "
                "them contains the other directly.",
    },
    {
        "id": "ks4-specific-latent-heat-h21",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates the specific latent heat of fusion of a small "
                "candle wax sample and gets an answer of 200 J/kg — roughly a "
                "thousand times SMALLER than a typical textbook value for wax. "
                "Suggest the most likely source of this error.",
        "options": [
            "The energy supplied must have been recorded in kilojoules rather than "
            "joules by mistake, multiplying the calculated value by a thousand",
            "The wax sample must have been unusually pure, giving it a genuinely tiny "
            "latent heat of its own",
            "The mass was probably left in grams rather than converted to kilograms, "
            "dividing by a number a thousand times larger than the true mass",
            "The thermometer used must have been miscalibrated, throwing off "
            "the whole calculation",
        ],
        "correct_index": 2,
        "why": "Leaving the mass in grams means dividing by a number a thousand times "
               "larger than the true mass in kilograms, so the calculated specific "
               "latent heat comes out a thousand times too small.",
    },
    {
        "id": "ks4-specific-latent-heat-h22",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "4000 J is supplied to a 0.030 kg sample of ice at 0 °C. The "
                "specific latent heat of fusion of ice is 334 000 J/kg. Calculate "
                "the mass of ice that melts, and state whether the whole sample "
                "melts.",
        "options": [
            "All 0.030 kg melts, since 4000 J is far more than enough energy for so "
            "small a sample of ice to melt right through",
            "About 0.12 kg melts, since dividing 4000 J by 33 400 J/kg gives the mass "
            "of ice that melts",
            "About 0.0012 kg melts, since 4000 ÷ 3 340 000 gives the mass that melts",
            "About 0.012 kg melts — only part of the sample, since the full "
            "0.030 kg would need 10 020 J",
        ],
        "correct_index": 3,
        "why": "The whole sample would need 0.030 × 334 000 = 10 020 J, more "
                "than the 4000 J supplied, so only m = 4000 ÷ 334 000 ≈ 0.012 kg "
                "melts.",
    },
    {
        "id": "ks4-specific-latent-heat-h23",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thermal store can be built from a large mass of hot water, "
                "using its specific heat capacity, or from a smaller mass of a "
                "wax that changes state, using its specific latent heat of "
                "fusion, to store the same amount of energy. Suggest one "
                "advantage of the latent-heat wax store over the water store.",
        "options": [
            "The wax store can hold the same energy in a much smaller mass, "
            "because latent heat values are often far higher than a "
            "temperature-only store could exploit over a practical range",
            "The wax store is always cheaper, because wax is a cheaper material than "
            "water in every situation, and cost is the only thing that ever separates "
            "two designs storing the same energy",
            "The wax store releases its energy instantly rather than "
            "gradually, unlike a water store",
            "The wax store needs no insulation at all, unlike a water-based "
            "store",
        ],
        "correct_index": 0,
        "why": "A wax's specific latent heat is often much greater than the "
                "energy a realistic temperature range could store using specific "
                "heat capacity, so less mass is needed for the same stored "
                "energy.",
    },
    {
        "id": "ks4-specific-latent-heat-h24",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A furnace operator wants to reduce the total electrical energy "
                "used per batch when melting scrap aluminium. Suggest two "
                "separate strategies, based on the equation E = mL and the "
                "furnace's efficiency, that could reduce the total electrical "
                "energy required for a fixed mass of aluminium.",
        "options": [
            "Increasing the mass melted each time, since larger batches always need "
            "proportionally less total energy per kilogram than small ones do, making "
            "a bigger batch the cheaper way to melt scrap",
            "Raising the furnace's efficiency to cut losses, and pre-heating "
            "the aluminium closer to its melting point beforehand, both "
            "reduce the extra energy needed on top of E = mL",
            "Melting the aluminium faster, since a shorter melting time always means "
            "less total energy is used per batch of scrap, however the furnace itself "
            "happens to be run that day",
            "Using a higher-powered heater, since higher power itself reduces "
            "the total energy needed for the same job",
        ],
        "correct_index": 1,
        "why": "E = mL fixes the minimum useful energy needed; cutting losses "
                "through higher efficiency, and reducing the temperature rise "
                "needed beforehand, both cut the extra energy on top of that "
                "minimum.",
    },
    {
        "id": "ks4-specific-latent-heat-h25",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.50 m³ container of molten wax (density 900 kg/m³, Lf = 200 "
                "000 J/kg) and a separate 0.50 m³ container of molten lead "
                "(density 11 300 kg/m³, Lf = 23 000 J/kg) both freeze completely. "
                "Compare the total energy released by each.",
        "options": [
            "The wax releases more energy overall, because its specific latent heat "
            "is nearly nine times lead's, which outweighs any difference in the "
            "masses the two containers happen to hold",
            "Both release exactly the same total energy, because the two containers "
            "occupy exactly the same volume",
            "The lead releases more energy overall, about 130 MJ against "
            "about 90 MJ for the wax, because its far higher density gives it "
            "much more mass despite its lower latent heat",
            "The lead releases more energy overall, but only because it has the "
            "higher specific latent heat of fusion of the two, and latent heat alone "
            "is what decides the total released",
        ],
        "correct_index": 2,
        "why": "The wax's mass is 0.50 × 900 = 450 kg, releasing 450 × 200 000 = "
                "90 000 000 J; the lead's mass is 0.50 × 11 300 = 5650 kg, "
                "releasing 5650 × 23 000 = 129 950 000 J — lead's far greater "
                "density outweighs its much smaller latent heat.",
    },
    {
        "id": "ks4-specific-latent-heat-h26",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solid at exactly its melting point can either be about to "
                "start melting or already partway through melting, with some "
                "liquid present. Explain why a thermometer alone cannot tell "
                "these two situations apart.",
        "options": [
            "Thermometers cannot measure the temperature of a solid, only of "
            "a liquid",
            "The melting point itself changes depending on how much of the sample has "
            "already melted, so the thermometer reading would drift steadily upward",
            "A thermometer only works correctly above 0 °C, and cannot be relied on "
            "at the melting point of any solid substance that is being tested",
            "Temperature stays at the melting point throughout the whole "
            "melting process, so the thermometer reads the same value in both "
            "situations",
        ],
        "correct_index": 3,
        "why": "Temperature remains constant throughout melting, so a "
                "thermometer reading the melting point cannot show how far "
                "through the process the sample has got.",
    },

    # ── particle-motion-pressure ────────────────────────────────────────
    {
        "id": "ks4-particle-motion-pressure-e05",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the SI unit of pressure.",
        "options": [
            "Pascals (Pa)",
            "Newtons (N)",
            "Joules (J)",
            "Kelvin (K)",
        ],
        "correct_index": 0,
        "why": "Pressure is measured in pascals, Pa, equal to a newton per "
                "square metre.",
    },
    {
        "id": "ks4-particle-motion-pressure-e06",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which quantity is held constant in Boyle's Law (p × V = "
                "constant).",
        "options": [
            "Volume",
            "Temperature",
            "Pressure",
            "Mass",
        ],
        "correct_index": 1,
        "why": "Boyle's Law relates pressure and volume at a constant "
                "temperature.",
    },
    {
        "id": "ks4-particle-motion-pressure-e07",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which quantity is held constant in the pressure law (p ÷ T "
                "= constant).",
        "options": [
            "Temperature",
            "Pressure",
            "Volume",
            "Number of particles",
        ],
        "correct_index": 2,
        "why": "The pressure law relates pressure and temperature at a constant "
                "volume.",
    },
    {
        "id": "ks4-particle-motion-pressure-e08",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas at 100 kPa occupies 4.0 m³. Calculate its pressure when "
                "compressed to 2.0 m³ at constant temperature.",
        "options": [
            "50 kPa",
            "400 kPa",
            "800 kPa",
            "200 kPa",
        ],
        "correct_index": 3,
        "why": "p₁V₁ = p₂V₂, so p₂ = 100 × 4.0 ÷ 2.0 = 200 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-e09",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas at 200 K has a pressure of 100 kPa. Calculate its pressure "
                "when heated to 400 K at constant volume.",
        "options": [
            "200 kPa",
            "50 kPa",
            "400 kPa",
            "300 kPa",
        ],
        "correct_index": 0,
        "why": "p ÷ T stays constant, and 400 K is double 200 K, so the pressure "
                "doubles to 200 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-e10",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Convert a temperature of 77 °C into kelvin.",
        "options": [
            "77 K",
            "350 K",
            "196 K",
            "623 K",
        ],
        "correct_index": 1,
        "why": "T (K) = T (°C) + 273 = 77 + 273 = 350 K.",
    },
    {
        "id": "ks4-particle-motion-pressure-e11",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the volume of a fixed mass of gas if its "
                "pressure is increased at constant temperature.",
        "options": [
            "It increases",
            "It stays the same",
            "It decreases",
            "It depends on the type of gas",
        ],
        "correct_index": 2,
        "why": "Pressure and volume are inversely proportional at constant "
                "temperature, so a pressure increase means a volume decrease.",
    },
    {
        "id": "ks4-particle-motion-pressure-e12",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a gas has no fixed shape or volume of its own.",
        "options": [
            "Its particles are fixed firmly in position but are far too light to settle",
            "Its particles chemically react with the walls of whatever container is "
            "holding them",
            "Its particles have no mass at all, so gravity cannot hold them into any "
            "fixed shape",
            "Its particles move freely and spread out to fill whatever space "
            "is available",
        ],
        "correct_index": 3,
        "why": "Gas particles are in constant, random motion with almost no "
                "forces between them, so they spread out to fill any container.",
    },
    {
        "id": "ks4-particle-motion-pressure-s07",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas syringe holds 500 cm³ of gas at 300 kPa. Calculate the "
                "pressure when the gas is compressed to 200 cm³ at constant "
                "temperature.",
        "options": [
            "750 kPa",
            "120 kPa",
            "500 kPa",
            "1500 kPa",
        ],
        "correct_index": 0,
        "why": "p₁V₁ = p₂V₂, so p₂ = 300 × 500 ÷ 200 = 750 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-s08",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rigid, sealed container of gas is at 7 °C and a pressure of 90 "
                "kPa. Calculate the pressure after it is heated to 287 °C, the "
                "volume staying constant.",
        "options": [
            "45 kPa",
            "180 kPa",
            "3690 kPa",
            "360 kPa",
        ],
        "correct_index": 1,
        "why": "In kelvin the temperature goes from 280 K to 560 K, exactly "
                "doubling, so at constant volume the pressure doubles to 180 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-s09",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas at 400 kPa occupies 3.0 m³. Calculate its volume when the "
                "pressure is increased to 600 kPa at constant temperature.",
        "options": [
            "4.5 m³",
            "1.5 m³",
            "2.0 m³",
            "0.50 m³",
        ],
        "correct_index": 2,
        "why": "p₁V₁ = p₂V₂, so V₂ = 400 × 3.0 ÷ 600 = 2.0 m³.",
    },
    {
        "id": "ks4-particle-motion-pressure-s10",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain both ways in which raising the temperature of a gas at "
                "constant volume increases its pressure.",
        "options": [
            "The molecules move faster, so they collide with the walls more "
            "often, but with exactly the same force each time",
            "The molecules become larger as they warm up, so each collision transfers "
            "more force to the walls",
            "The molecules move faster, so they collide with the walls less "
            "often but much harder",
            "The molecules move faster, so they collide with the walls more "
            "often AND with greater force each time",
        ],
        "correct_index": 3,
        "why": "Faster molecules hit the walls both more frequently and with "
                "more force per collision, both raising the pressure.",
    },
    {
        "id": "ks4-particle-motion-pressure-s11",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why decreasing the volume of a gas at constant "
                "temperature increases its pressure, and state whether the force "
                "of each individual collision also changes.",
        "options": [
            "The molecules travel less distance between collisions, so they "
            "hit the walls more often; the force of each collision stays the "
            "same, since the temperature is unchanged",
            "The molecules hit the walls more often AND harder, because squeezing a "
            "gas at constant temperature always heats it up as well as crowding its "
            "molecules closer together",
            "The molecules hit the walls less often but much harder, because "
            "there is less room to build up speed",
            "The force of each collision increases, even though the temperature and "
            "the molecules' speed stay the same, because a smaller container makes "
            "every single impact that much harder",
        ],
        "correct_index": 0,
        "why": "At constant temperature the molecules keep the same average "
                "speed and force per collision; a smaller volume simply makes the "
                "collisions more frequent.",
    },
    {
        "id": "ks4-particle-motion-pressure-s12",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scuba tank contains compressed air. As a diver breathes from "
                "the tank over time, air leaves but the tank's rigid volume and "
                "the air's temperature stay constant. Explain what happens to the "
                "pressure inside the tank.",
        "options": [
            "The pressure stays the same, because pressure only depends on "
            "temperature and volume, not on the amount of gas",
            "The pressure falls, because there are fewer air molecules left "
            "to collide with the tank's walls each second",
            "The pressure rises, because the remaining molecules have more "
            "room to move around in",
            "The pressure falls to zero the instant any air is used, since "
            "the tank is no longer completely full",
        ],
        "correct_index": 1,
        "why": "Fewer molecules mean fewer collisions with the tank walls each "
                "second, so the pressure falls as air is used.",
    },
    {
        "id": "ks4-particle-motion-pressure-s13",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bicycle pump contains 250 cm³ of air at 100 kPa with the "
                "outlet sealed. The plunger is pushed in until the volume is 50 "
                "cm³, at constant temperature. Calculate the new pressure.",
        "options": [
            "20 kPa",
            "1250 kPa",
            "500 kPa",
            "150 kPa",
        ],
        "correct_index": 2,
        "why": "p₁V₁ = p₂V₂, so p₂ = 100 × 250 ÷ 50 = 500 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-s14",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rigid container of gas is at 250 K and a pressure of 150 kPa. "
                "Calculate the temperature at which the pressure has fallen to 90 "
                "kPa, the volume staying constant.",
        "options": [
            "417 K",
            "90 K",
            "210 K",
            "150 K",
        ],
        "correct_index": 3,
        "why": "p ÷ T stays constant, so T₂ = T₁ × p₂ ÷ p₁ = 250 × 90 ÷ 150 = "
                "150 K.",
    },
    {
        "id": "ks4-particle-motion-pressure-s15",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Garages recommend checking a car's tyre pressure when the tyres "
                "are cold, not immediately after a long drive. Explain why.",
        "options": [
            "Driving heats the air in the tyres, raising its pressure at "
            "constant volume, so a reading taken then would be higher than "
            "the tyre's normal cold pressure",
            "Driving cools the air in the tyres as it rushes past them, lowering its "
            "pressure, so a reading taken straight after a long drive would come out "
            "too low",
            "Tyre pressure never actually changes with temperature, so the timing of "
            "the check makes no real difference at all",
            "Warm tyres are simply too hot to attach a pressure gauge to "
            "safely",
        ],
        "correct_index": 0,
        "why": "Friction and flexing warm the air inside a driven tyre, and at "
                "roughly constant volume that raises its pressure above the "
                "normal cold value.",
    },
    {
        "id": "ks4-particle-motion-pressure-s16",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of particle motion, why the gas inside a "
                "sealed aerosol can is at a much higher pressure than the air "
                "outside it.",
        "options": [
            "The gas inside is at a much higher temperature than the air outside the "
            "can, and a hotter gas always presses harder on whatever is containing it",
            "The gas is compressed into a small volume, so its molecules "
            "collide with the can's walls far more often than the same amount "
            "of gas would in open air",
            "The gas inside has heavier molecules than ordinary air, which "
            "raises its pressure",
            "The can's metal walls chemically react with the gas, generating "
            "extra pressure",
        ],
        "correct_index": 1,
        "why": "Squeezing the same amount of gas into a small can means far more "
                "frequent collisions with its walls, raising the pressure.",
    },
    {
        "id": "ks4-particle-motion-pressure-s17",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed syringe holds 80 cm³ of gas at 120 kPa. The plunger is "
                "pushed until the volume is 20 cm³, at constant temperature. "
                "Calculate the new pressure.",
        "options": [
            "30 kPa",
            "960 kPa",
            "480 kPa",
            "240 kPa",
        ],
        "correct_index": 2,
        "why": "p₁V₁ = p₂V₂, so p₂ = 120 × 80 ÷ 20 = 480 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-s18",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Container A and container B hold the same number of gas "
                "molecules at the same temperature, but container A has half the "
                "volume of container B. Compare their pressures.",
        "options": [
            "Container A has half the pressure of container B, because less "
            "volume means less room for collisions to build up",
            "Both containers have the same pressure, because they hold the "
            "same number of molecules",
            "Container B has four times the pressure of container A, because "
            "larger containers always experience more total force",
            "Container A has twice the pressure of container B, because its "
            "molecules collide with its smaller surface more often",
        ],
        "correct_index": 3,
        "why": "The same number of molecules colliding in half the volume means "
                "twice as many collisions with the walls each second, doubling "
                "the pressure.",
    },
    {
        "id": "ks4-particle-motion-pressure-s19",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pressure cooker seals steam and air inside at 300 K and 100 "
                "kPa. Calculate the pressure once the sealed contents have heated "
                "to 450 K, the volume staying constant.",
        "options": [
            "150 kPa",
            "67 kPa",
            "200 kPa",
            "550 kPa",
        ],
        "correct_index": 0,
        "why": "p ÷ T stays constant, so p₂ = 100 × 450 ÷ 300 = 150 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-s20",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist finds a bicycle pump gets progressively harder to push "
                "as the plunger nears the end of its stroke, with the outlet "
                "still sealed. Explain this in terms of the gas's particles.",
        "options": [
            "The plunger itself becomes heavier as it is pushed further into "
            "the pump",
            "As the volume shrinks, the trapped molecules collide with the "
            "plunger more and more often, so the gas pushes back with greater "
            "pressure",
            "The trapped gas turns into a liquid partway through the stroke, and a "
            "liquid resists being squeezed far more strongly than a gas ever does",
            "Friction between the plunger and the pump barrel is the only "
            "thing that increases",
        ],
        "correct_index": 1,
        "why": "Shrinking the trapped volume raises the collision rate with "
                "every surface, including the plunger, so the gas resists more "
                "strongly.",
    },
    {
        "id": "ks4-particle-motion-pressure-s21",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three identical sealed containers hold the same gas at the same "
                "temperature. Container X is at 100 kPa, container Y at 200 kPa, "
                "and container Z at 300 kPa. Rank them by volume, largest to "
                "smallest, assuming each holds the same number of molecules.",
        "options": [
            "Z, Y, X",
            "X, Z, Y",
            "X, Y, Z",
            "Y, X, Z",
        ],
        "correct_index": 2,
        "why": "At the same temperature and number of molecules, lower pressure "
                "means larger volume, so the order is X, then Y, then Z.",
    },
    {
        "id": "ks4-particle-motion-pressure-s22",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A weather balloon is released at ground level, where the "
                "external air pressure is 100 kPa, and rises to a height where "
                "the external pressure has fallen to 25 kPa, with the internal "
                "gas temperature assumed unchanged. Calculate the factor by which "
                "the balloon's internal volume increases.",
        "options": [
            "0.25 times its original volume",
            "25 times its original volume",
            "100 times its original volume",
            "4 times its original volume",
        ],
        "correct_index": 3,
        "why": "By Boyle's Law, V₂ ÷ V₁ = p₁ ÷ p₂ = 100 ÷ 25 = 4, so the volume "
                "grows to four times its original size.",
    },
    {
        "id": "ks4-particle-motion-pressure-s23",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bubble of gas released by a diver expands as it rises through "
                "water toward the surface, where the surrounding pressure is "
                "lower. Explain why the bubble grows larger, assuming its "
                "temperature stays roughly constant.",
        "options": [
            "As the surrounding pressure falls, the trapped gas needs a "
            "larger volume for its molecules to keep exerting a matching "
            "pressure against it",
            "The bubble absorbs extra gas molecules dissolved in the water as it "
            "rises towards the surface, growing steadily as it takes more of them in",
            "The water pressure has no effect on a gas bubble's size at any "
            "depth",
            "The gas inside the bubble cools as it rises through the colder water, "
            "and cooling always makes a gas expand to fill more space than it did "
            "before",
        ],
        "correct_index": 0,
        "why": "Boyle's Law means a fall in surrounding pressure lets a fixed "
                "amount of trapped gas expand to a larger volume at the same "
                "temperature.",
    },
    {
        "id": "ks4-particle-motion-pressure-s24",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical sealed rigid canisters hold the same gas. Canister "
                "P is at 280 K and canister Q is at 350 K, both starting from the "
                "same pressure when they were at 280 K. Compare their pressures "
                "now.",
        "options": [
            "Canister P has the higher pressure, because cooler gas is denser and "
            "packs its molecules more tightly against the canister walls",
            "Canister Q has the higher pressure, because its higher "
            "temperature means more frequent and more forceful collisions "
            "with the walls",
            "Both canisters have exactly the same pressure, since the "
            "containers are otherwise identical",
            "Canister Q has a lower pressure, because heating a gas always "
            "makes it expand and thin out",
        ],
        "correct_index": 1,
        "why": "At constant volume, a higher temperature always means a higher "
                "pressure, so the warmer canister Q now has the higher pressure.",
    },
    {
        "id": "ks4-particle-motion-pressure-s25",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student records three readings for the same sealed gas sample, "
                "all at the same temperature: 100 kPa at 6.0 m³, 150 kPa at 4.0 "
                "m³, and 200 kPa at 2.5 m³. Identify which reading is "
                "inconsistent with Boyle's Law.",
        "options": [
            "100 kPa at 6.0 m³, since 600 is not a round number",
            "150 kPa at 4.0 m³, since its pV product, 600, lies between the other two "
            "readings",
            "200 kPa at 2.5 m³, since its pV product, 500, does not match the "
            "other two, both 600",
            "None of them — all three readings are perfectly consistent with "
            "each other",
        ],
        "correct_index": 2,
        "why": "For a fixed mass of gas at constant temperature, pV should stay "
                "the same throughout, and only the third reading breaks that "
                "pattern.",
    },
    {
        "id": "ks4-particle-motion-pressure-s26",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas is heated from 200 K to 800 K at constant volume. Compare "
                "the average speed of its molecules before and after.",
        "options": [
            "The molecules move exactly four times as fast at 800 K, since "
            "800 is four times 200",
            "The molecules move at the same average speed, because "
            "temperature does not affect particle speed directly",
            "The molecules move slower at 800 K, because higher temperatures "
            "always spread particles further apart, slowing them down",
            "The molecules move faster at 800 K, because a higher temperature "
            "always means greater average kinetic energy",
        ],
        "correct_index": 3,
        "why": "Higher temperature always means greater average kinetic energy "
                "and so faster molecules, but the exact scaling of speed with "
                "temperature is not this simple direct proportion.",
    },
    {
        "id": "ks4-particle-motion-pressure-h06",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas at 350 kPa occupies 900 cm³. Calculate the volume, in m³, "
                "when the gas is compressed to 1050 kPa at constant temperature.",
        "options": [
            "3.0 × 10⁻⁴ m³",
            "300 m³",
            "3.0 × 10⁻⁶ m³",
            "3.0 × 10⁻³ m³",
        ],
        "correct_index": 0,
        "why": "V₂ = p₁V₁ ÷ p₂ = 350 × 900 ÷ 1050 = 300 cm³, and 300 cm³ = 3.0 × "
                "10⁻⁴ m³.",
    },
    {
        "id": "ks4-particle-motion-pressure-h07",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rigid gas cylinder is at 240 K and 84 kPa. Calculate the "
                "temperature, in kelvin, at which the pressure has fallen to 63 "
                "kPa, the volume remaining constant. State this temperature in "
                "degrees Celsius as well.",
        "options": [
            "320 K, which is 47 °C",
            "180 K, which is −93 °C",
            "63 K, which is −210 °C",
            "300 K, which is 27 °C",
        ],
        "correct_index": 1,
        "why": "T₂ = T₁ × p₂ ÷ p₁ = 240 × 63 ÷ 84 = 180 K, which is 180 − 273 = "
                "−93 °C.",
    },
    {
        "id": "ks4-particle-motion-pressure-h08",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates: 'A gas is at 20 °C and 100 kPa. Heated to "
                "40 °C, the temperature has doubled, so the new pressure is 200 "
                "kPa.' Identify the error in this reasoning.",
        "options": [
            "There is no error — doubling the Celsius temperature really does "
            "double the pressure",
            "The error is that pressure and temperature are not actually related to "
            "each other at all inside a rigid, sealed container",
            "The temperatures must be converted to kelvin first — 20 °C is "
            "293 K and 40 °C is 313 K, which is not a doubling at all",
            "The error is that the volume must have changed as well, which "
            "was not accounted for",
        ],
        "correct_index": 2,
        "why": "The pressure law needs an absolute temperature scale; doubling a "
                "Celsius value is not doubling the true kelvin temperature.",
    },
    {
        "id": "ks4-particle-motion-pressure-h09",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas occupies a 2.0 m³ container at 150 kPa. It is allowed to "
                "expand into a second, previously empty and sealed 3.0 m³ "
                "container connected to the first, so the gas now fills both, a "
                "total of 5.0 m³, at the same temperature. Calculate the new "
                "pressure.",
        "options": [
            "375 kPa",
            "90 kPa",
            "250 kPa",
            "60 kPa",
        ],
        "correct_index": 3,
        "why": "p₂ = p₁V₁ ÷ V₂ = 150 × 2.0 ÷ 5.0 = 60 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-h10",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Container A holds helium gas and container B holds nitrogen gas, "
                "both at the same temperature, the same volume, and containing "
                "the same NUMBER of molecules. Evaluate whether the two "
                "containers must have the same pressure.",
        "options": [
            "Yes — pressure depends on the number of molecules, their average "
            "kinetic energy and the volume, all of which are the same here, "
            "regardless of which gas is used",
            "No — nitrogen molecules are heavier, so container B must have the higher "
            "pressure, since each heavier molecule strikes the wall with more force "
            "behind it each time",
            "No — helium is a lighter gas overall, so container A's molecules move "
            "faster and must give the higher pressure",
            "It cannot be determined without knowing the exact chemical "
            "formula of each gas",
        ],
        "correct_index": 0,
        "why": "The particle model of pressure depends on the number of "
                "molecules, their average kinetic energy and the volume, none of "
                "which favour one gas over another here.",
    },
    {
        "id": "ks4-particle-motion-pressure-h11",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas is compressed from 1.5 m³ to 0.60 m³ at constant "
                "temperature, ending at a pressure of 480 kPa. Calculate its "
                "original pressure.",
        "options": [
            "1200 kPa",
            "192 kPa",
            "288 kPa",
            "96 kPa",
        ],
        "correct_index": 1,
        "why": "p₁ = p₂V₂ ÷ V₁ = 480 × 0.60 ÷ 1.5 = 192 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-h12",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed rigid container of gas is cooled until its pressure has "
                "fallen to 75% of its original value, from an original "
                "temperature of 400 K. Calculate the new temperature.",
        "options": [
            "100 K",
            "533 K",
            "300 K",
            "325 K",
        ],
        "correct_index": 2,
        "why": "Pressure and temperature are directly proportional at constant "
                "volume, so the temperature also falls to 75% of 400 K, which is "
                "300 K.",
    },
    {
        "id": "ks4-particle-motion-pressure-h13",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cylinder holds gas at a pressure of 2.0 × 10⁵ Pa in a volume "
                "of 0.40 m³. If this is squeezed down to 0.16 m³ without changing "
                "its temperature, work out the resulting pressure, in kPa.",
        "options": [
            "80 kPa",
            "1250 kPa",
            "200 kPa",
            "500 kPa",
        ],
        "correct_index": 3,
        "why": "p₂ = p₁V₁ ÷ V₂ = 2.0 × 10⁵ × 0.40 ÷ 0.16 = 5.0 × 10⁵ Pa, which "
                "is 500 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-h14",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student compresses a gas very quickly, without giving it time "
                "to lose the extra heat this generates, and then tries to use "
                "p₁V₁ = p₂V₂ to predict the new pressure. Evaluate whether "
                "Boyle's Law will correctly predict the result.",
        "options": [
            "No — Boyle's Law only holds at constant temperature, and a quick "
            "compression that heats the gas breaks that condition",
            "Yes — Boyle's Law applies to any compression at all, whatever happens to "
            "the temperature of the gas inside the container",
            "Yes, provided the volume change is small enough, whatever "
            "happens to the temperature",
            "No — Boyle's Law only ever applies to gases that are cooling, never to "
            "gases being compressed, because compression always changes the amount of "
            "gas present",
        ],
        "correct_index": 0,
        "why": "Boyle's Law assumes constant temperature; a fast compression "
                "that also heats the gas breaks that assumption, so the simple "
                "prediction will be wrong.",
    },
    {
        "id": "ks4-particle-motion-pressure-h15",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mountaineer's oxygen cylinder shows its pressure gauge reading "
                "has fallen to a third of its original value after some oxygen "
                "has been used, at a constant temperature and the cylinder's "
                "fixed volume. Explain what this tells us about the amount of "
                "oxygen left in the cylinder.",
        "options": [
            "Exactly two-thirds of the oxygen has been used, but the amount remaining "
            "cannot be worked out, because pressure only ever reports how hard the "
            "gas is pushing",
            "About a third of the original amount of oxygen remains, since "
            "pressure at fixed volume and temperature is directly "
            "proportional to the number of molecules present",
            "The volume of the cylinder must have also decreased to a third "
            "of its original size",
            "The temperature inside the cylinder must have risen to explain "
            "the pressure drop",
        ],
        "correct_index": 1,
        "why": "With volume and temperature both fixed, the number of "
                "collisions, and so the pressure, scales directly with how many "
                "molecules remain.",
    },
    {
        "id": "ks4-particle-motion-pressure-h16",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas's volume and pressure are both given at an initial and a "
                "final state, with temperature not mentioned at all. A separate "
                "gas's temperature and pressure are both given at an initial and "
                "a final state, with volume not mentioned at all. State which "
                "law, if either, could be safely applied to each case as it "
                "stands.",
        "options": [
            "Boyle's Law applies to the first gas and the pressure law to the second, "
            "since naming three of the four quantities is always enough to fix which "
            "of the two laws is in use",
            "The pressure law applies to both gases, since pressure appears "
            "in both sets of data",
            "Neither can be safely assumed — Boyle's Law needs constant "
            "temperature confirmed, and the pressure law needs constant "
            "volume confirmed, and neither is stated for either gas",
            "Boyle's Law applies to both gases, since gases always keep a "
            "constant temperature unless directly heated",
        ],
        "correct_index": 2,
        "why": "Each law needs its own held-constant variable confirmed before "
                "it can be applied; simply naming the other two variables is not "
                "enough.",
    },
    {
        "id": "ks4-particle-motion-pressure-h17",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "For a fixed mass of gas at constant temperature, compare the "
                "effect on pressure of doubling the volume with the effect of "
                "halving the volume.",
        "options": [
            "Both changes have exactly the same effect on pressure, since doubling "
            "and halving are opposite operations that simply cancel each other out",
            "Doubling the volume doubles the pressure, and halving the volume halves "
            "it, since a larger container gives the molecules more wall to strike",
            "Neither change affects the pressure of the gas at all, since only a "
            "change in temperature can ever alter the pressure of a trapped gas",
            "Doubling the volume halves the pressure, and halving the volume "
            "doubles the pressure — pressure and volume are inversely "
            "proportional",
        ],
        "correct_index": 3,
        "why": "Boyle's Law makes pressure and volume inversely proportional, so "
                "doubling one halves the other and vice versa.",
    },
    {
        "id": "ks4-particle-motion-pressure-h18",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rearrange p ÷ T = constant to find an expression for T₂, the "
                "final temperature, in terms of p₁, T₁ and p₂.",
        "options": [
            "T₂ = T₁ × p₂ ÷ p₁",
            "T₂ = T₁ × p₁ ÷ p₂",
            "T₂ = p₁ × p₂ ÷ T₁",
            "T₂ = T₁ ÷ (p₁ × p₂)",
        ],
        "correct_index": 0,
        "why": "Since p₁ ÷ T₁ = p₂ ÷ T₂, cross-multiplying and rearranging gives "
                "T₂ = T₁ × p₂ ÷ p₁.",
    },
    {
        "id": "ks4-particle-motion-pressure-h19",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed bicycle pump's plunger is pushed slowly from fully "
                "extended to fully compressed, with the outlet blocked "
                "throughout, at constant temperature. Identify the point in this "
                "stroke at which the trapped gas is at its highest pressure.",
        "options": [
            "At the very start of the stroke, when the volume of the trapped gas "
            "inside the pump barrel is at its largest",
            "At the very end of the stroke, when the volume is smallest, "
            "since pressure and volume are inversely proportional",
            "Exactly halfway through the stroke, since the pressure of a trapped gas "
            "is always greatest in the middle of any compression",
            "The pressure stays the same throughout the whole stroke",
        ],
        "correct_index": 1,
        "why": "Pressure rises continuously as volume falls, so the smallest "
                "volume, at the end of the stroke, gives the highest pressure.",
    },
    {
        "id": "ks4-particle-motion-pressure-h20",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas at 400 K and 120 kPa in a rigid container is cooled at "
                "constant volume until its temperature is 300 K. It is then "
                "transferred, at this new constant temperature, into a smaller "
                "container so its volume becomes half of what it was, with no "
                "further temperature change. Calculate the final pressure.",
        "options": [
            "90 kPa",
            "45 kPa",
            "180 kPa",
            "240 kPa",
        ],
        "correct_index": 2,
        "why": "Cooling to 300 K gives 120 × 300 ÷ 400 = 90 kPa; then halving "
                "the volume at constant temperature doubles the pressure to 180 "
                "kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-h21",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that if a sealed rigid container of gas were "
                "cooled enough, according to p ÷ T = constant, its pressure could "
                "eventually become negative. Evaluate this claim.",
        "options": [
            "The claim is correct — sufficiently extreme cooling can make the "
            "pressure of a gas negative, because the equation p ÷ T = constant "
            "carries on working smoothly through absolute zero into negative values",
            "The claim is flawed, because pressure and temperature are "
            "actually unrelated for a real gas",
            "The claim is correct, and negative pressure has been measured directly "
            "in laboratory experiments on ordinary gases cooled below absolute zero, "
            "where the gas pulls inward on its container instead of pushing outward",
            "The claim is flawed — as the gas approaches absolute zero its "
            "pressure approaches zero, but the model of a gas breaks down "
            "well before that, as a real gas condenses into a liquid or solid "
            "long before then",
        ],
        "correct_index": 3,
        "why": "The simple model predicts pressure falling toward zero near "
                "absolute zero, but real gases condense into a liquid or solid "
                "long before that point is reached.",
    },
    {
        "id": "ks4-particle-motion-pressure-h22",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas starts at 100 kPa, 2.0 m³ and 300 K. Compare the final "
                "pressure if, separately, (a) its volume is halved at constant "
                "temperature, or (b) its temperature is doubled at constant "
                "volume.",
        "options": [
            "Both changes give exactly the same final pressure, 200 kPa",
            "Halving the volume gives the bigger final pressure of the two "
            "changes",
            "Doubling the temperature gives the bigger final pressure of the "
            "two changes",
            "Neither change alters the final pressure of the gas at all",
        ],
        "correct_index": 0,
        "why": "Halving the volume gives p = 100 × 2.0 ÷ 1.0 = 200 kPa, and "
                "doubling the temperature gives p = 100 × 600 ÷ 300 = 200 kPa — "
                "the same result either way.",
    },
    {
        "id": "ks4-particle-motion-pressure-h23",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A submarine's air tank holds 0.50 m³ of compressed air at 2000 "
                "kPa. This air is released into the submarine's ballast tank, "
                "where it expands to fill 5.0 m³ at the same temperature. "
                "Calculate its new pressure.",
        "options": [
            "20 000 kPa",
            "200 kPa",
            "1000 kPa",
            "400 kPa",
        ],
        "correct_index": 1,
        "why": "p₂ = p₁V₁ ÷ V₂ = 2000 × 0.50 ÷ 5.0 = 200 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-h24",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student records these three (pressure, volume) pairs for the "
                "same sealed gas sample at constant temperature: 80 kPa and 12 "
                "m³, 120 kPa and 8.0 m³, and 300 kPa and 3.0 m³. Using pV = "
                "constant, identify which single reading is inconsistent with the "
                "other two.",
        "options": [
            "80 kPa and 12 m³, since 960 is not as round a number as the "
            "others",
            "120 kPa and 8.0 m³, since its pV value lies exactly between the other "
            "two readings",
            "300 kPa and 3.0 m³, since its pV value, 900, does not match the "
            "other two, both 960",
            "None of the readings are inconsistent — all three agree with "
            "each other",
        ],
        "correct_index": 2,
        "why": "80 × 12 = 960 and 120 × 8.0 = 960, but 300 × 3.0 = 900, which "
                "breaks the pattern the other two share.",
    },
    {
        "id": "ks4-particle-motion-pressure-h25",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas-filled syringe has its plunger locked firmly in place so "
                "it cannot move, and is then placed in a warm water bath. "
                "Identify which law describes how its pressure will change as it "
                "warms, and why.",
        "options": [
            "Boyle's Law (p × V = constant), because a syringe is always designed to "
            "change its own volume when it is heated up in water",
            "Neither law applies, because a locked plunger means nothing at all can "
            "change inside the syringe, whatever is done to it from outside",
            "Both laws apply at once, because volume and temperature are "
            "always linked to each other",
            "The pressure law (p ÷ T = constant), because locking the plunger "
            "fixes the volume, not the pressure, as the gas is heated",
        ],
        "correct_index": 3,
        "why": "Locking the plunger fixes the volume, so it is the pressure law, "
                "not Boyle's Law, that describes what happens as the trapped gas "
                "is heated.",
    },
    {
        "id": "ks4-particle-motion-pressure-h26",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student uses p ÷ T = constant to predict the pressure of a gas "
                "as it is cooled steadily toward the temperature at which it will "
                "condense into a liquid. Suggest why the prediction is likely to "
                "become less accurate as that temperature is approached.",
        "options": [
            "As the gas approaches its condensation point, intermolecular "
            "forces start pulling the particles together more strongly, so it "
            "stops behaving like the ideal gas the simple law assumes",
            "The prediction actually becomes more accurate the colder the gas gets, "
            "right down towards absolute zero itself, where the simple gas model "
            "works better than it does anywhere else",
            "The law only ever applies exactly at room temperature, and is "
            "never reliable at any other temperature",
            "The pressure gauge itself becomes less accurate at lower temperatures, "
            "because the cold makes its metal parts contract and stick, which is the "
            "only real source of error in the whole prediction",
        ],
        "correct_index": 0,
        "why": "The simple gas laws assume negligible forces between particles, "
                "an assumption that breaks down as a real gas nears the "
                "temperature at which it condenses.",
    },
]
