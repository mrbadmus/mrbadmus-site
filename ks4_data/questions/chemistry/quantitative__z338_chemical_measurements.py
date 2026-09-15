"""Chemistry · Quantitative chemistry — the MRB-338 expansion for
`chemical-measurements`.

AQA 4.3.1.4 and the practical skills it rests on: accuracy against precision,
random error against systematic error, the resolution and proper use of the
balance, burette, pipette and measuring cylinder, reading from the bottom of
the meniscus at eye level, the volume conversions between cm³ and dm³, and
percentage uncertainty — computed, compared, and used to choose between two
methods.

⚠️ FOUNDATION TIER. No mole appears in any stem, option or `why`; every
calculation is a subtraction, a unit conversion, a mean, or a percentage.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-chemical-measurements-e05",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where a burette reading should be taken from when the "
                "liquid forms a curved surface.",
        "options": [
            "From the highest point of the curve, right at the edge of the "
            "glass",
            "From the bottom of the curve, with the eye level with it",
            "From halfway up the curve, judged by eye from above it",
            "From the top of the curve, looking down into the burette",
        ],
        "correct_index": 1,
        "why": "Water-based liquids curve downwards, so the bottom of the "
               "meniscus is the true level, and eye level avoids a parallax "
               "error.",
    },
    {
        "id": "ks4-chemical-measurements-e06",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the piece of apparatus that delivers one fixed volume of "
                "solution, such as exactly 25.0 cm³, very precisely.",
        "options": [
            "A burette",
            "A pipette",
            "A measuring cylinder",
            "A conical flask",
        ],
        "correct_index": 1,
        "why": "A pipette is manufactured to deliver a single stated volume, "
               "which makes it the most precise choice for that one volume.",
    },
    {
        "id": "ks4-chemical-measurements-e07",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A volume of 1.50 dm³ of solution is prepared. State this "
                "volume in cm³.",
        "options": [
            "0.0015 cm³",
            "150 cm³",
            "1500 cm³",
            "15 000 cm³",
        ],
        "correct_index": 2,
        "why": "There are 1000 cm³ in every dm³, so 1.50 × 1000 = 1500 cm³.",
    },
    {
        "id": "ks4-chemical-measurements-e08",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In practical chemistry, accuracy and precision mean two "
                "different things. Identify the statement that describes "
                "accuracy.",
        "options": [
            "How many decimal places the measuring instrument is able to show",
            "How closely repeated measurements of the same quantity agree with "
            "one another",
            "How close the measurement is to the true value of the quantity",
            "How quickly the measurement can be taken once the reaction starts",
        ],
        "correct_index": 2,
        "why": "Accuracy is about closeness to the true value; how closely "
               "repeats agree with each other is precision instead.",
    },
    {
        "id": "ks4-chemical-measurements-e09",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A digital balance reads to the nearest 0.01 g. State the "
                "resolution of this balance.",
        "options": [
            "0.01 g",
            "0.05 g",
            "0.1 g",
            "1 g",
        ],
        "correct_index": 0,
        "why": "The resolution is the smallest change the instrument can show, "
               "which for this balance is 0.01 g.",
    },
    {
        "id": "ks4-chemical-measurements-e10",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the step that reduces the effect of random error on a "
                "measured result.",
        "options": [
            "Recording every reading to one more decimal place than before",
            "Using a fresh sample of the chemical for the single measurement",
            "Repeating the measurement several times and taking a mean",
            "Writing the readings down as soon as the reaction has finished",
        ],
        "correct_index": 2,
        "why": "Random errors scatter either side of the true value, so "
               "averaging several repeats brings the mean closer to it.",
    },
    {
        "id": "ks4-chemical-measurements-e11",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An acid is delivered from a burette and the volume used "
                "comes to 30 cm³. Convert that volume into dm³.",
        "options": [
            "0.0030 dm³",
            "0.30 dm³",
            "3.0 dm³",
            "0.030 dm³",
        ],
        "correct_index": 3,
        "why": "Dividing by 1000 converts cm³ to dm³, so 30 ÷ 1000 = "
               "0.030 dm³.",
    },
    {
        "id": "ks4-chemical-measurements-e12",
        "subtopic_slug": "chemical-measurements",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the reason a balance is tared before a solid is weighed "
                "out on it.",
        "options": [
            "So that the container's mass is not counted as part of the solid",
            "So that the balance can settle before the solid is added to it",
            "So that the balance records the mass to more decimal places",
            "So that the solid does not stick to the pan while it is weighed",
        ],
        "correct_index": 0,
        "why": "Taring sets the reading to zero with the empty container in "
               "place, so the figure shown afterwards is the solid alone.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-chemical-measurements-s05",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 50 cm³ burette can be read to ±0.05 cm³. A burette reading "
                "of 25.00 cm³ is recorded. Calculate the percentage "
                "uncertainty in this single reading.",
        "options": [
            "0.2%",
            "0.5%",
            "2.0%",
            "5.0%",
        ],
        "correct_index": 0,
        "why": "(0.05 ÷ 25.00) × 100 = 0.2%.",
    },
    {
        "id": "ks4-chemical-measurements-s06",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student needs 20 cm³ of solution and has a 25 cm³ pipette, "
                "a 50 cm³ burette, a 100 cm³ measuring cylinder and a 250 cm³ "
                "beaker. Determine the best choice.",
        "options": [
            "The 50 cm³ burette, because it can deliver exactly 20 cm³",
            "The 25 cm³ pipette, because it is the most precise of the four",
            "The 100 cm³ measuring cylinder, because 20 cm³ fits inside it",
            "The 250 cm³ beaker, because it is marked in tens of cm³",
        ],
        "correct_index": 0,
        "why": "A pipette only delivers its own fixed volume, so for a chosen "
               "20 cm³ the burette is both precise and adjustable.",
    },
    {
        "id": "ks4-chemical-measurements-s07",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A balance has been set 0.05 g too high and is not re-zeroed "
                "between weighings. Describe the effect on a set of repeat "
                "measurements.",
        "options": [
            "They scatter more widely about the true value than before",
            "They are unaffected, because the same balance was used each time",
            "They are all 0.05 g too high, so they agree but are not accurate",
            "They are all 0.05 g too low, because the error works in reverse",
        ],
        "correct_index": 2,
        "why": "A systematic error shifts every reading the same way, so the "
               "repeats stay precise while all of them miss the true value.",
    },
    {
        "id": "ks4-chemical-measurements-s08",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student records titres of 23.45, 23.50, 23.45 and "
                "25.80 cm³. Determine the mean titre that should be quoted.",
        "options": [
            "24.05 cm³",
            "23.60 cm³",
            "23.50 cm³",
            "23.47 cm³",
        ],
        "correct_index": 3,
        "why": "25.80 cm³ is anomalous and is discarded, and the mean of the "
               "three concordant titres is 23.47 cm³.",
    },
    {
        "id": "ks4-chemical-measurements-s09",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In an energy change experiment the temperature climbs by "
                "10.0 °C, and every thermometer reading carries an "
                "uncertainty of ±0.5 °C. Calculate the percentage "
                "uncertainty in the rise.",
        "options": [
            "0.5%",
            "10.0%",
            "20.0%",
            "5.0%",
        ],
        "correct_index": 3,
        "why": "(0.5 ÷ 10.0) × 100 = 5.0%.",
    },
    {
        "id": "ks4-chemical-measurements-s10",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a 100 cm³ measuring cylinder is a poor choice for "
                "measuring out 5 cm³ of liquid.",
        "options": [
            "The liquid would not reach the first marking on the cylinder",
            "Its markings are far apart, so 5 cm³ carries a large uncertainty",
            "The cylinder is far too tall for such a small volume to be poured "
            "into it",
            "A measuring cylinder is meant for solids rather than liquids",
        ],
        "correct_index": 1,
        "why": "The same reading error on a large-scale cylinder is a much "
               "bigger fraction of a small volume, so the percentage "
               "uncertainty is high.",
    },
    {
        "id": "ks4-chemical-measurements-s11",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A burette is filled and read as 0.65 cm³. After the titration "
                "the reading is 24.90 cm³. Calculate the titre.",
        "options": [
            "25.55 cm³",
            "24.90 cm³",
            "23.60 cm³",
            "24.25 cm³",
        ],
        "correct_index": 3,
        "why": "The titre is the difference between the two readings: "
               "24.90 − 0.65 = 24.25 cm³.",
    },
    {
        "id": "ks4-chemical-measurements-s12",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students time the same reaction three times each. Student "
                "A gets 40, 41 and 40 s; student B gets 33, 47 and 41 s. "
                "Compare the precision of their results.",
        "options": [
            "Student A is the more precise, because the repeats agree closely",
            "Student B is the more precise, because a much wider range has been "
            "covered",
            "They are equally precise, because both took three readings each",
            "Neither is precise, because the true reaction time is not given",
        ],
        "correct_index": 0,
        "why": "Precision is about how closely repeats agree with each other, "
               "and A's three times span 1 s against B's 14 s.",
    },
    {
        "id": "ks4-chemical-measurements-s13",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student weighs out 0.50 g of a solid on a balance reading "
                "to ±0.01 g. Calculate the percentage uncertainty in the mass.",
        "options": [
            "0.02%",
            "0.20%",
            "2.0%",
            "5.0%",
        ],
        "correct_index": 2,
        "why": "(0.01 ÷ 0.50) × 100 = 2.0%.",
    },
    {
        "id": "ks4-chemical-measurements-s14",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a student should record 25.00 cm³ rather than "
                "25 cm³ after using a burette.",
        "options": [
            "Because two decimal places make the arithmetic afterwards easier",
            "Because the extra zeros show the reading was taken very carefully",
            "Because the burette's scale can be read to the nearest 0.05 cm³",
            "Because a volume must always be written to two decimal places",
        ],
        "correct_index": 2,
        "why": "A recorded value should show the resolution of the instrument, "
               "and a burette is read to hundredths of a cm³.",
    },
    {
        "id": "ks4-chemical-measurements-s15",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student times a reaction four times and records 62, 65, 63 "
                "and 64 s. Identify the type of error that causes this "
                "spread.",
        "options": [
            "A random error, from judging the end point by eye each time",
            "A systematic error in the stopwatch's internal timing circuit",
            "A zero error, because the stopwatch was not reset to zero",
            "A resolution error, because the stopwatch shows whole seconds",
        ],
        "correct_index": 0,
        "why": "Readings that scatter either side of a central value show "
               "random error, here from the human judgement of when to stop.",
    },
    {
        "id": "ks4-chemical-measurements-s16",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A volumetric flask is used to make a solution up to the "
                "250 cm³ mark. State what that volume refers to.",
        "options": [
            "The volume of water that was added to the flask",
            "The volume of the solid that was dissolved in it",
            "The volume of the solution, solute and solvent together",
            "The volume the solution would occupy once it is warmed",
        ],
        "correct_index": 2,
        "why": "A concentration is always per volume of SOLUTION, which is why "
               "the flask is filled to the mark after the solid has "
               "dissolved.",
    },
    {
        "id": "ks4-chemical-measurements-s17",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student reads a measuring cylinder from above rather than "
                "at eye level. Name the error this introduces.",
        "options": [
            "A zero error",
            "A resolution error",
            "A random error",
            "A parallax error",
        ],
        "correct_index": 3,
        "why": "Looking at the scale from the wrong angle makes the liquid "
               "level appear against the wrong marking, which is a parallax "
               "error.",
    },
    {
        "id": "ks4-chemical-measurements-s18",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 25.0 cm³ pipette is marked as accurate to ±0.06 cm³. "
                "Calculate the percentage uncertainty in the volume it "
                "delivers.",
        "options": [
            "0.06%",
            "0.60%",
            "2.40%",
            "0.24%",
        ],
        "correct_index": 3,
        "why": "(0.06 ÷ 25.0) × 100 = 0.24%.",
    },
    {
        "id": "ks4-chemical-measurements-s19",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a set of measurements can be precise and yet not "
                "accurate.",
        "options": [
            "Because a precise instrument also has a small resolution",
            "Because the repeats can agree closely while all missing the true "
            "value",
            "Because a precise reading is one that has been taken once and not "
            "repeated",
            "Because precision improves as the number of readings taken goes "
            "up",
        ],
        "correct_index": 1,
        "why": "A systematic error shifts every repeat by the same amount, so "
               "the readings cluster tightly around the wrong value.",
    },
    {
        "id": "ks4-chemical-measurements-s20",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 10 cm³ measuring cylinder reads to ±0.2 cm³ and a 50 cm³ "
                "burette to ±0.05 cm³. Determine which gives the smaller "
                "percentage uncertainty on a 10.0 cm³ volume.",
        "options": [
            "The burette, at 0.5% against the cylinder's 2.0%",
            "The cylinder, at 0.2% against the burette's 0.5%",
            "The burette, at 0.05% against the cylinder's 0.2%",
            "They are the same, because the volume measured is the same",
        ],
        "correct_index": 0,
        "why": "(0.05 ÷ 10.0) × 100 = 0.5% for the burette against "
               "(0.2 ÷ 10.0) × 100 = 2.0% for the cylinder.",
    },
    {
        "id": "ks4-chemical-measurements-s21",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what 'concordant titres' means in a titration.",
        "options": [
            "Titres taken by two different students working side by side",
            "Titres that have each been recorded to two decimal places",
            "Titres that lie within 0.10 cm³ of one another",
            "Titres that add up to the volume of the pipette used",
        ],
        "correct_index": 2,
        "why": "Concordant titres agree closely — usually within 0.10 cm³ — and "
               "only those are averaged.",
    },
    {
        "id": "ks4-chemical-measurements-s22",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student leaves a beaker of solution uncovered on the bench "
                "overnight before using it. Explain the effect on its "
                "concentration.",
        "options": [
            "It rises, because water evaporates and leaves the solute behind",
            "It falls, because some of the solute settles out of solution",
            "It stays the same, because no chemical reaction has taken place",
            "It falls, because water vapour from the air joins the solution",
        ],
        "correct_index": 0,
        "why": "Evaporation removes solvent but not solute, so the same mass "
               "of solute is left in a smaller volume of solution.",
    },
    {
        "id": "ks4-chemical-measurements-s23",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student weighs a solid on a watch glass, tips it into a "
                "beaker and reweighs the empty watch glass. Explain why this "
                "method is better than taring and tipping.",
        "options": [
            "It uses fewer pieces of apparatus, so less can go wrong",
            "It means the beaker never has to be placed on the balance at all",
            "It allows for any solid left clinging to the watch glass",
            "It lets the same watch glass be used again straight away",
        ],
        "correct_index": 2,
        "why": "Weighing the watch glass again shows how much solid actually "
               "left it, so any residue does not count as transferred.",
    },
    {
        "id": "ks4-chemical-measurements-s24",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A burette is read as 3.20 cm³ before and 28.55 cm³ after a "
                "titration, and each reading carries an uncertainty of "
                "±0.05 cm³. Determine the titre and its total uncertainty.",
        "options": [
            "25.35 cm³, uncertainty ±0.05 cm³",
            "25.35 cm³, uncertainty ±0.10 cm³",
            "31.75 cm³, uncertainty ±0.10 cm³",
            "25.35 cm³, uncertainty ±0.025 cm³",
        ],
        "correct_index": 1,
        "why": "The titre is 28.55 − 3.20 = 25.35 cm³, and two readings each "
               "±0.05 cm³ give a total uncertainty of ±0.10 cm³.",
    },
    {
        "id": "ks4-chemical-measurements-s25",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the reason a rough titration is carried out before "
                "the accurate ones.",
        "options": [
            "To warm the apparatus up so that each of the later titrations runs "
            "faster",
            "To find roughly where the end point is, so it is not overshot",
            "To rinse the burette out with the solution it will deliver",
            "To check that the indicator chosen changes colour at all",
        ],
        "correct_index": 1,
        "why": "Knowing the approximate titre lets the student add the last "
               "cm³ dropwise, which is what makes the accurate titres "
               "concordant.",
    },
    {
        "id": "ks4-chemical-measurements-s26",
        "subtopic_slug": "chemical-measurements",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction is timed at 30 s using a stopwatch that reads to "
                "the nearest 0.1 s, but the student's reactions add about "
                "0.3 s of uncertainty. Determine the percentage uncertainty "
                "in the time.",
        "options": [
            "0.33%",
            "3.0%",
            "0.1%",
            "1.0%",
        ],
        "correct_index": 3,
        "why": "The human reaction time dominates, so "
               "(0.3 ÷ 30) × 100 = 1.0%.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-chemical-measurements-h05",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A method requires a solid to be weighed to within 0.5%. The "
                "only balance available reads to ±0.01 g. Determine the "
                "smallest mass that can be weighed and still meet this "
                "requirement.",
        "options": [
            "0.20 g",
            "0.50 g",
            "2.00 g",
            "5.00 g",
        ],
        "correct_index": 2,
        "why": "0.5% of a mass m must be at least 0.01 g, so "
               "m = 0.01 ÷ 0.005 = 2.00 g.",
    },
    {
        "id": "ks4-chemical-measurements-h06",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'My burette reads to ±0.05 cm³, my titre "
                "was 20.00 cm³, so my percentage uncertainty is "
                "0.05 ÷ 20.00 = 0.0025%.' Identify the error in this working.",
        "options": [
            "The result was not multiplied by 100 — it is 0.25%, not 0.0025%",
            "The percentage should have been divided by 20.00 again afterwards",
            "The titre should have been divided by the uncertainty instead",
            "The uncertainty of a burette is ±0.5 cm³, not ±0.05 cm³",
        ],
        "correct_index": 0,
        "why": "A percentage needs the fraction multiplied by 100, so "
               "0.05 ÷ 20.00 = 0.0025, which is 0.25%.",
    },
    {
        "id": "ks4-chemical-measurements-h07",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures 250 cm³ of solution with a measuring "
                "cylinder instead of a volumetric flask, then calculates a "
                "concentration. Evaluate the effect on the result.",
        "options": [
            "There is no effect, because both hold 250 cm³ when full",
            "The concentration is too high, because the cylinder overfills",
            "The concentration is less reliable, because the volume is less "
            "certain",
            "The concentration is too low, because the cylinder underfills",
        ],
        "correct_index": 2,
        "why": "A cylinder's volume carries a much larger uncertainty than a "
               "volumetric flask's, and the error could fall on either side, "
               "so the result is less reliable rather than wrong in one "
               "direction.",
    },
    {
        "id": "ks4-chemical-measurements-h08",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thermometer reading to ±0.5 °C is used for a temperature "
                "rise found from two readings. The rise recorded is 8.0 °C. "
                "Determine the percentage uncertainty in the rise.",
        "options": [
            "6.3%",
            "3.1%",
            "0.5%",
            "12.5%",
        ],
        "correct_index": 3,
        "why": "Two readings each ±0.5 °C give ±1.0 °C on the rise, so "
               "(1.0 ÷ 8.0) × 100 = 12.5%.",
    },
    {
        "id": "ks4-chemical-measurements-h09",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Only one burette is available, and the titres a student "
                "obtains carry an unacceptably large percentage uncertainty. "
                "Determine which alteration to the procedure reduces that "
                "uncertainty most.",
        "options": [
            "Dilute the solution in the burette so a larger titre is needed",
            "Take more repeat titrations and average a larger number of them",
            "Read the burette to three decimal places rather than to two",
            "Use a cleaner conical flask for each of the titrations done",
        ],
        "correct_index": 0,
        "why": "The uncertainty is fixed in cm³, so making the measured volume "
               "larger makes that fixed amount a smaller fraction of it.",
    },
    {
        "id": "ks4-chemical-measurements-h10",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A balance shows three decimal places, yet repeat weighings of "
                "one object give 6.241, 6.238, 6.244 and 6.239 g. Determine "
                "what these results show about the balance.",
        "options": [
            "Its resolution is fine but its readings still scatter a little",
            "Its resolution is too coarse for an object of this mass",
            "It carries a systematic error of about 0.003 g on every weighing "
            "made",
            "It should be read to two decimal places rather than three",
        ],
        "correct_index": 0,
        "why": "A high resolution does not remove random variation; the "
               "readings spread over about 0.006 g even though each is shown "
               "to 0.001 g.",
    },
    {
        "id": "ks4-chemical-measurements-h11",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student reports a titre of 22.4 cm³ from a burette that "
                "reads to ±0.05 cm³. Evaluate how the value has been "
                "recorded.",
        "options": [
            "It is fine, because one decimal place is enough for a titre",
            "It is fine, because rounding removes the uncertainty from it",
            "It is wrong, because a titre must be a whole number of cm³",
            "It is poor, because it hides a digit the burette can resolve",
        ],
        "correct_index": 3,
        "why": "Recording to fewer figures than the instrument can resolve "
               "throws away real information and overstates the uncertainty.",
    },
    {
        "id": "ks4-chemical-measurements-h12",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student rinses a burette with water and fills it with acid "
                "without rinsing it with the acid first. Determine the effect "
                "on the titre.",
        "options": [
            "The titre is too small, because the acid has been diluted",
            "The titre is unaffected, because the same volume is delivered",
            "The titre is too large, because water reacts with the indicator",
            "The titre is too large, because the acid has been diluted",
        ],
        "correct_index": 3,
        "why": "Water left in the burette dilutes the acid, so more of the "
               "diluted solution has to be run in to reach the end point.",
    },
    {
        "id": "ks4-chemical-measurements-h13",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Four students weigh the same 5.000 g standard mass and get "
                "5.050, 5.049, 5.051 and 5.050 g. Determine what this shows.",
        "options": [
            "A random error of roughly ±0.050 g in each of the four weighings "
            "taken",
            "A systematic error of about +0.050 g in every weighing taken",
            "That the standard mass itself has gained about 0.050 g",
            "That the balance's resolution is poorer than 0.050 g",
        ],
        "correct_index": 1,
        "why": "The readings agree closely with one another but all sit about "
               "0.050 g above the true value, which is the signature of a "
               "systematic error.",
    },
    {
        "id": "ks4-chemical-measurements-h14",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student must weigh out 1.00 g of solid to within 1%, and "
                "only a balance reading to ±0.02 g is available. Determine "
                "whether it is good enough.",
        "options": [
            "Yes, because 0.02 g is a small mass compared with 1.00 g",
            "No, because the percentage uncertainty is 2%, above the 1% needed",
            "Yes, because the uncertainty can be averaged away by repeating",
            "No, because a balance must read to three decimal places for this",
        ],
        "correct_index": 1,
        "why": "(0.02 ÷ 1.00) × 100 = 2%, which is twice the uncertainty the "
               "method allows.",
    },
    {
        "id": "ks4-chemical-measurements-h15",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student wants the percentage uncertainty in a mass to fall "
                "below 0.1% using a balance reading to ±0.01 g. Determine the "
                "minimum mass that must be weighed.",
        "options": [
            "1.00 g",
            "2.00 g",
            "5.00 g",
            "10.00 g",
        ],
        "correct_index": 3,
        "why": "0.1% of the mass must be at least 0.01 g, so "
               "m = 0.01 ÷ 0.001 = 10.00 g.",
    },
    {
        "id": "ks4-chemical-measurements-h16",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A titration is repeated and the titres are 24.10, 24.15, "
                "24.10 and 24.15 cm³, but the pipette used delivers 24.6 cm³ "
                "rather than the 25.0 cm³ marked on it. Evaluate the results.",
        "options": [
            "Precise and accurate, as the four titres agree closely",
            "Neither precise nor accurate, as the pipette was faulty",
            "Precise but not accurate, because the pipette biases every titre",
            "Accurate but not precise, as the mean is reliable",
        ],
        "correct_index": 2,
        "why": "The titres agree closely with one another, so they are "
               "precise, but a pipette that is wrong by the same amount every "
               "time shifts all of them away from the true value.",
    },
    {
        "id": "ks4-chemical-measurements-h17",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student prepares a solution by weighing the solid into a "
                "beaker, dissolving it, and pouring the solution into a "
                "volumetric flask. Determine what must be done next for the "
                "concentration to be correct.",
        "options": [
            "Rinse the beaker into the flask, then fill to the mark",
            "Fill the flask to the mark and then stir the solution well",
            "Weigh the flask and its contents to check the mass of solid",
            "Warm the flask so that the solid dissolves completely",
        ],
        "correct_index": 0,
        "why": "Solution left in the beaker is solute missing from the flask, "
               "so the beaker is rinsed in before the volume is made up to "
               "the mark.",
    },
    {
        "id": "ks4-chemical-measurements-h18",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas volume is measured as 48.0 cm³ in a syringe reading to "
                "±0.5 cm³, and the time taken is 60.0 s measured to ±0.3 s. "
                "Determine which measurement carries the larger percentage "
                "uncertainty.",
        "options": [
            "The volume, at about 1.0% against about 0.5% for the time",
            "The time, at about 1.8% against about 0.5% for the volume",
            "They are equal, because both uncertainties are under 1 unit",
            "The volume, at about 0.5% against about 1.8% for the time",
        ],
        "correct_index": 0,
        "why": "(0.5 ÷ 48.0) × 100 = 1.0% for the volume and "
               "(0.3 ÷ 60.0) × 100 = 0.5% for the time.",
    },
    {
        "id": "ks4-chemical-measurements-h19",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student quotes a mean titre of 23.4667 cm³ from three "
                "concordant burette readings. Evaluate this way of quoting "
                "the result.",
        "options": [
            "Acceptable, because a mean should keep every digit calculated",
            "Acceptable, because more digits make the mean more accurate",
            "Poor, because the mean cannot be more precise than the readings",
            "Poor, because a mean of three readings should be rounded to "
            "whole cm³",
        ],
        "correct_index": 2,
        "why": "A mean is quoted to the same resolution as the readings it "
               "came from, so 23.47 cm³ is as far as the burette can justify.",
    },
    {
        "id": "ks4-chemical-measurements-h20",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student halves every mass and volume in a method so the "
                "experiment uses less chemical. Determine the effect on the "
                "percentage uncertainties.",
        "options": [
            "They halve as well, because the quantities have all halved",
            "They are unchanged, because the same apparatus is still in use",
            "They roughly double, because the fixed uncertainties stay the same",
            "They fall, because smaller quantities are rather easier to measure "
            "out",
        ],
        "correct_index": 2,
        "why": "The uncertainty of each instrument is a fixed number of units, "
               "so halving the measured quantity doubles that uncertainty as a "
               "fraction of it.",
    },
    {
        "id": "ks4-chemical-measurements-h21",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student records 25 cm³ of solution as 0.25 dm³. Identify "
                "the error and give the correct value.",
        "options": [
            "The student divided by 100 instead of 1000; it is 0.025 dm³",
            "The student multiplied by 1000 instead of dividing; it is 25 000 "
            "dm³",
            "The student divided by 10 instead of 1000; it is 0.0025 dm³",
            "There is no error, because 1 dm³ is equal to 100 cm³ exactly",
        ],
        "correct_index": 0,
        "why": "1 dm³ is 1000 cm³, so 25 ÷ 1000 = 0.025 dm³ — a factor of ten "
               "out.",
    },
    {
        "id": "ks4-chemical-measurements-h22",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two methods give the same answer, but one has a percentage "
                "uncertainty of 0.4% and the other of 4%. Determine what "
                "follows about the two results.",
        "options": [
            "The 4% method must have been carried out incorrectly somewhere",
            "The 0.4% result is closer to the true value than the other one",
            "The 0.4% result is the more reliable, though neither is proven "
            "right",
            "The two results are equally good, since they agree",
        ],
        "correct_index": 2,
        "why": "A smaller percentage uncertainty narrows the range the true "
               "value could lie in, but it cannot rule out a systematic error "
               "in either method.",
    },
    {
        "id": "ks4-chemical-measurements-h23",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student records burette readings of 0.00 and 22.50 cm³, but "
                "an air bubble in the burette tip escaped during the "
                "titration. Determine the effect on the titre.",
        "options": [
            "The titre is too small, because the bubble had taken up some of "
            "the volume",
            "The titre is too large, because the bubble's volume was counted "
            "in",
            "The titre is unchanged, because the bubble held just air",
            "The titre is too large, because the bubble slowed the flow down",
        ],
        "correct_index": 1,
        "why": "The scale recorded the space the bubble had occupied as though "
               "it were solution, so the measured titre is bigger than the "
               "volume actually delivered.",
    },
    {
        "id": "ks4-chemical-measurements-h24",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A method calls for 0.100 dm³ of solution. Determine the "
                "volume in cm³ and the apparatus that measures it most "
                "precisely.",
        "options": [
            "1000 cm³, measured with a 1 dm³ volumetric flask",
            "10.0 cm³, measured with a 10 cm³ pipette",
            "100 cm³, measured with a 250 cm³ beaker",
            "100 cm³, measured with a 100 cm³ volumetric flask",
        ],
        "correct_index": 3,
        "why": "0.100 × 1000 = 100 cm³, and a volumetric flask of that size is "
               "made to hold exactly that volume.",
    },
    {
        "id": "ks4-chemical-measurements-h25",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures a mass difference by weighing 12.46 g and "
                "then 12.02 g on a balance reading to ±0.01 g. Determine the "
                "percentage uncertainty in the difference.",
        "options": [
            "0.08%",
            "0.16%",
            "2.3%",
            "4.5%",
        ],
        "correct_index": 3,
        "why": "The difference is 0.44 g with an uncertainty of ±0.02 g from "
               "two weighings, so (0.02 ÷ 0.44) × 100 = 4.5%.",
    },
    {
        "id": "ks4-chemical-measurements-h26",
        "subtopic_slug": "chemical-measurements",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why finding a small mass change by subtracting two "
                "large masses gives a poor result even on a good balance.",
        "options": [
            "Because a balance is less reliable when the mass on it is large",
            "Because the two uncertainties add while the difference stays tiny",
            "Because subtracting two readings cancels the uncertainty out",
            "Because a large mass takes longer for the balance to settle on",
        ],
        "correct_index": 1,
        "why": "Each weighing contributes its own uncertainty, so a difference "
               "of a few hundredths of a gram can carry a percentage "
               "uncertainty of many per cent.",
    },
]
