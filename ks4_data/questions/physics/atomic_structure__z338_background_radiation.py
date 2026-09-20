"""Physics · Atomic structure — the MRB-338 expansion of `background-radiation`.

One leaf only: AQA 8463 §6.4.3, physics only — what background radiation is,
the named natural sources (radon from uranium in the rocks, gamma from ground
and building materials, cosmic rays, carbon-14 and potassium-40 in food) and
the named artificial ones (medical procedures, the nuclear industry, fallout
still present from weapons testing), the fact that it varies with place and
with time, the sievert as the unit of dose, the becquerel as the unit of
activity, and the correction that has to be made before any source measurement
means anything.

The original four rows of each band in `atomic_structure__b.py` take the
definition, radon as the largest single contributor, the sievert, medical
procedures as an artificial source, the airline pilot, granite against clay,
one corrected-count-rate sum, the randomness argument for a long count, the
unsubtracted half-life, half of 2.7 mSv, the newspaper's nuclear-industry
claim and the weak source that cannot be distinguished from background.

Nothing here repeats one of those. ⚠️ Two numbers are deliberately avoided:
the existing `h02` STATES 2.7 mSv and the 50% radon share in its own stem, so
no row here may be keyed on either (brief §9.6) — the dose arithmetic in this
file runs on a 2.4 mSv budget and a 15% food-and-drink share instead. The
corrected-count-rate sums run BACKWARDS (given the corrected rate, find the
reading) or across two different rooms, so that no stem shares a frame with
the existing `s03`.

This is a physics-only Triple subtopic, so every row carries
`triple_only=True`, but the tier stays `foundation` — the demand is in the
band, never in the tier. Working lives in `why` and never in an option.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # The named sources one at a time, the two units, the correction rule and
    # the fact that background can never be switched off.
    {
        "id": "ks4-background-radiation-e05",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the contribution to background radiation that arrives "
                "from space.",
        "options": [
            "Cosmic rays",
            "Radon gas",
            "Fallout from weapons testing",
            "Potassium-40 in food",
        ],
        "correct_index": 0,
        "why": "Cosmic rays are high-energy particles reaching the Earth from "
               "space; the other three all originate on Earth.",
    },
    {
        "id": "ks4-background-radiation-e06",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the two radioactive isotopes found naturally in the food "
                "and drink we take in.",
        "options": [
            "Uranium-235 and plutonium-239",
            "Cobalt-60 and technetium-99m",
            "Carbon-14 and potassium-40",
            "Radon-222 and radium-226",
        ],
        "correct_index": 2,
        "why": "Carbon-14 and potassium-40 occur naturally in living material, "
               "so everything we eat and drink carries a trace of them.",
    },
    {
        "id": "ks4-background-radiation-e07",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a radiation detector records in a laboratory where "
                "no radioactive source has been taken out.",
        "options": [
            "Nothing, because it responds when a source is placed in front of "
            "it and at no other time",
            "A small count rate caused by the background radiation around it",
            "A steadily rising count as the instrument warms up during the "
            "lesson",
            "A count left over from the last source the instrument was used "
            "with",
        ],
        "correct_index": 1,
        "why": "Background radiation is present everywhere at all times, so a "
               "detector always registers a small count rate.",
    },
    {
        "id": "ks4-background-radiation-e08",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how the corrected count rate of a source is worked out.",
        "options": [
            "Add the background count rate to the measured count rate",
            "Divide the measured count rate by the background count rate and "
            "round the answer",
            "Subtract the background count rate from the measured count rate",
            "Multiply the measured count rate by the background count rate",
        ],
        "correct_index": 2,
        "why": "The detector records the source and the background together, "
               "so the background has to be taken away to leave the source's "
               "own count rate.",
    },
    {
        "id": "ks4-background-radiation-e09",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why radon gas is a health hazard once it has been "
                "breathed in.",
        "options": [
            "It reacts with the lining of the lungs and burns the tissue "
            "chemically on contact and leaves a permanent scar",
            "It blocks the alveoli, so less oxygen reaches the blood",
            "It decays in the lungs, emitting alpha particles that ionise "
            "nearby cells",
            "It carries cosmic rays that were absorbed while it was "
            "underground",
        ],
        "correct_index": 2,
        "why": "Radon decaying inside the lungs puts a strongly ionising "
               "alpha emitter in direct contact with living tissue, which "
               "raises the risk of lung cancer.",
    },
    {
        "id": "ks4-background-radiation-e10",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State a simple measure that lowers the amount of radon gas "
                "inside a home.",
        "options": [
            "Improving the ventilation so the gas is carried outside",
            "Painting the inside walls with a thick coat of gloss paint",
            "Keeping the heating on so the gas is destroyed by the warmth",
            "Storing food in sealed containers rather than open bowls",
        ],
        "correct_index": 0,
        "why": "Radon seeps in from the ground, so replacing indoor air with "
               "outdoor air keeps its concentration low.",
    },
    {
        "id": "ks4-background-radiation-e11",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what a measurement of radiation dose takes into "
                "account.",
        "options": [
            "Only the number of nuclei that decayed during the measurement",
            "The amount of radiation absorbed and the biological effect it has",
            "The distance from the source and nothing else about the exposure "
            "that took place",
            "The half-life of the source that produced the radiation",
        ],
        "correct_index": 1,
        "why": "Dose combines how much radiation the body absorbed with how "
               "much harm that type of radiation does, which is why it is "
               "given in sieverts.",
    },
    {
        "id": "ks4-background-radiation-e12",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State whether the background count rate is the same "
                "everywhere in the United Kingdom.",
        "options": [
            "Yes, because it is fixed by the amount of cosmic radiation "
            "reaching the Earth at the top of the atmosphere",
            "Yes, because the atmosphere spreads it evenly over the whole "
            "country",
            "No, but it changes only in places where nuclear work is carried "
            "out",
            "No, because it depends on the local rocks and on the altitude of "
            "the place",
        ],
        "correct_index": 3,
        "why": "Geology and altitude both vary across the country, so the "
               "background differs from one town to the next.",
    },
    {
        "id": "ks4-background-radiation-e13",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State when the background count rate should be measured "
                "during a radioactivity experiment.",
        "options": [
            "Before any source is brought out of its container",
            "At the same moment as the source reading is taken",
            "After the source has been returned, once the room has settled",
            "Halfway through, so the detector has reached its working "
            "temperature, which takes about twenty minutes",
        ],
        "correct_index": 0,
        "why": "Measuring first gives a background value that is free of any "
               "contribution from the source.",
    },
    {
        "id": "ks4-background-radiation-e14",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the artificial contribution to today's background "
                "radiation that was created by activity in the twentieth "
                "century and is still present.",
        "options": [
            "Fallout left in the soil by nuclear weapons testing",
            "Ultraviolet light released by early electric lighting",
            "Carbon dioxide released by coal-fired power stations",
            "Helium released by early hot-air balloon flights",
        ],
        "correct_index": 0,
        "why": "Atmospheric weapons tests scattered radioactive material that "
               "settled worldwide, and some of it is long-lived enough to "
               "remain in the soil.",
    },
    {
        "id": "ks4-background-radiation-e15",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the unit used for the activity of a radioactive source.",
        "options": [
            "The millisievert",
            "The becquerel",
            "The watt",
            "The gram per second",
        ],
        "correct_index": 1,
        "why": "Activity is the number of decays each second, and one "
               "becquerel is one decay per second.",
    },
    {
        "id": "ks4-background-radiation-e16",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why the walls and floor of a granite building add to "
                "the background radiation inside it.",
        "options": [
            "Granite reflects cosmic rays back into the room from outside",
            "Granite is cut with tools that leave radioactive dust in the "
            "surface when the blocks are shaped",
            "Granite contains radioactive isotopes that emit gamma rays",
            "Granite is denser than brick, so it stores radiation for longer",
        ],
        "correct_index": 2,
        "why": "Rocks such as granite contain naturally occurring radioactive "
               "isotopes, and the gamma rays they emit pass out into the "
               "rooms around them.",
    },
    {
        "id": "ks4-background-radiation-e17",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one factor that makes one person's annual radiation "
                "dose larger than another's.",
        "options": [
            "The colour of the clothing they usually wear",
            "The number of hours of daylight where they live",
            "The part of the country they live in, and its local rocks",
            "Whether they keep their windows open or closed at night during "
            "the summer months",
        ],
        "correct_index": 2,
        "why": "Local geology changes the radon and gamma contributions, so "
               "where a person lives is one of the biggest influences on "
               "their annual dose.",
    },
    {
        "id": "ks4-background-radiation-e18",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State whether background radiation in a laboratory can be "
                "switched off before an experiment begins.",
        "options": [
            "Yes, by earthing the bench so the charge drains away",
            "No, it is always present, so it has to be measured and allowed "
            "for",
            "Yes, by locking every radioactive source in a lead-lined cupboard "
            "on the far side of the building",
            "No, but it falls to zero once the room has been empty overnight",
        ],
        "correct_index": 1,
        "why": "Background comes from rocks, the air, food and space, so it "
               "cannot be removed — the way to deal with it is to subtract it.",
    },

    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # The correction run backwards, the mean of repeated readings, the
    # place-to-place and season-to-season variation, and dose arithmetic on a
    # 2.4 mSv budget.
    {
        "id": "ks4-background-radiation-s05",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The corrected count rate of a source is 260 counts per "
                "minute. The background in the room is 24 counts per minute. "
                "Calculate the reading the detector will show.",
        "options": [
            "236 counts per minute",
            "284 counts per minute",
            "260 counts per minute",
            "6240 counts per minute",
        ],
        "correct_index": 1,
        "why": "The detector records source and background together, so the "
               "reading is 260 + 24 = 284 counts per minute.",
    },
    {
        "id": "ks4-background-radiation-s06",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the background is measured before the source is "
                "taken out of its container.",
        "options": [
            "The detector is more sensitive at the start of a lesson than "
            "later on",
            "The source would otherwise contribute to the reading, making the "
            "background value too high",
            "Handling the source charges the detector, which then counts "
            "faster for an hour",
            "The container absorbs background radiation, so the reading would "
            "be too low with it in the room during the measurement",
        ],
        "correct_index": 1,
        "why": "A background value must come from the room alone; if the "
               "source is out, part of its own count is subtracted from "
               "itself later.",
    },
    {
        "id": "ks4-background-radiation-s07",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two schools using identical detectors record background count "
                "rates of 18 and 47 counts per minute. Suggest why the values "
                "differ.",
        "options": [
            "One detector has been used more often, which wears down its "
            "response",
            "One school took its reading in the morning, when cosmic rays are "
            "strongest",
            "The two schools stand on different rocks and at different "
            "altitudes, so the local background differs",
            "One school measured in counts per minute and the other in "
            "becquerels by mistake",
        ],
        "correct_index": 2,
        "why": "Background depends on local geology and on height above sea "
               "level, so two places can legitimately differ by a factor of "
               "two or more.",
    },
    {
        "id": "ks4-background-radiation-s08",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a well-sealed modern house can hold more radon "
                "than a draughty older one standing on the same ground.",
        "options": [
            "Modern building materials contain far more uranium than older "
            "ones do",
            "Modern houses are warmer, and warm rock releases radon at a much "
            "greater rate",
            "Older houses have thicker walls, which absorb the radon before "
            "it enters a room",
            "Less air is exchanged with outside, so the radon seeping in "
            "builds up instead of being cleared",
        ],
        "correct_index": 3,
        "why": "Radon enters from the ground in both houses; what differs is "
               "how quickly the indoor air is replaced, and sealing a house "
               "slows that down.",
    },
    {
        "id": "ks4-background-radiation-s09",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In one year a person receives 1.2 mSv from radon, 0.3 mSv "
                "from cosmic rays, 0.3 mSv from food and drink and 0.6 mSv "
                "from medical procedures. Calculate their total annual dose.",
        "options": [
            "2.4 mSv",
            "1.8 mSv",
            "0.6 mSv",
            "2.1 mSv",
        ],
        "correct_index": 0,
        "why": "Doses from separate sources add: 1.2 + 0.3 + 0.3 + 0.6 = 2.4 "
               "mSv.",
    },
    {
        "id": "ks4-background-radiation-s10",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a doctor discussing the risk of a scan uses "
                "millisieverts rather than becquerels.",
        "options": [
            "The becquerel is too large a unit to describe anything that "
            "happens to a patient",
            "The millisievert measures the harm done to the body, while the "
            "becquerel only counts decays in a source",
            "The becquerel applies to gamma radiation only, and scans use "
            "X-rays instead",
            "The millisievert is the older unit, and hospitals have not yet "
            "changed over",
        ],
        "correct_index": 1,
        "why": "Activity in becquerels says nothing about how much radiation "
               "a person absorbed or how damaging it was; the sievert is "
               "built to express exactly that.",
    },
    {
        "id": "ks4-background-radiation-s11",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a chest X-ray adds to a person's annual dose but "
                "is counted as an artificial rather than a natural source.",
        "options": [
            "X-rays are produced by a machine built by people, not by "
            "radioactive rocks or by space",
            "X-rays carry more energy than any radiation that occurs "
            "naturally on Earth",
            "X-rays are absorbed by bone, and only radiation absorbed by soft "
            "tissue counts as natural background radiation",
            "X-rays do not add to the annual dose, because the machine is "
            "switched off afterwards",
        ],
        "correct_index": 0,
        "why": "The natural and artificial split is about where the radiation "
               "comes from; an X-ray set is a human-made source, so its dose "
               "is counted as artificial.",
    },
    {
        "id": "ks4-background-radiation-s12",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a radon measurement in the same house is often "
                "higher in January than in July.",
        "options": [
            "Cosmic rays reach the ground more easily in winter, when the air "
            "is colder and thinner",
            "Uranium in the rock decays faster in winter, producing more "
            "radon",
            "Windows and doors are kept shut in winter, so less radon is "
            "cleared from the rooms",
            "Radon is denser when cold, so more of it can fit into the same "
            "room before it escapes again through a gap in the floor",
        ],
        "correct_index": 2,
        "why": "The rock's output barely changes; the indoor concentration "
               "depends on ventilation, and a house is ventilated far less in "
               "winter.",
    },
    {
        "id": "ks4-background-radiation-s13",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Four one-minute background readings are taken in a "
                "laboratory: 22, 26, 24 and 28 counts. Calculate the mean "
                "background count rate.",
        "options": [
            "25 counts per minute",
            "24 counts per minute",
            "100 counts per minute",
            "26 counts per minute",
        ],
        "correct_index": 0,
        "why": "The total is 22 + 26 + 24 + 28 = 100 counts, and 100 ÷ 4 = 25 "
               "counts per minute.",
    },
    {
        "id": "ks4-background-radiation-s14",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why radon is treated as a serious hazard even though "
                "alpha radiation cannot pass through skin.",
        "options": [
            "Radon emits gamma rays as well, and it is the gamma that reaches "
            "the lungs from outside the body entirely",
            "Radon is breathed in, so the alpha is released inside the body "
            "where there is no skin to stop it",
            "Radon is absorbed through the skin of the hands before it is "
            "breathed in, which is why gloves are worn indoors in "
            "radon-affected areas",
            "Radon changes into a beta emitter as soon as it enters a warm "
            "room",
        ],
        "correct_index": 1,
        "why": "The skin argument only applies to a source outside the body; "
               "a gas that is inhaled puts the alpha emitter directly against "
               "living lung tissue.",
    },
    {
        "id": "ks4-background-radiation-s15",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why living a few miles from a nuclear power station "
                "adds very little to a person's annual dose.",
        "options": [
            "The station's radiation is directed upwards, so it passes over "
            "nearby houses without reaching anybody living in them",
            "A working reactor emits no radiation of any kind while it is "
            "sealed",
            "Routine releases are tightly controlled and small compared with "
            "radon, rocks, food and cosmic rays",
            "Radiation from a reactor has a very short half-life and decays "
            "before it leaves the site boundary fence",
        ],
        "correct_index": 2,
        "why": "The nuclear industry is a small part of the artificial "
               "contribution, which is itself far smaller than the natural "
               "sources everyone lives with.",
    },
    {
        "id": "ks4-background-radiation-s16",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pupil suggests carrying the detector into the corridor to "
                "take a reading with no background in it. Explain why this "
                "will not work.",
        "options": [
            "The corridor has its own background, because rocks, air, food "
            "and space contribute everywhere",
            "The corridor has a higher background than the laboratory, "
            "because more people pass through it",
            "The detector needs several hours to settle after being moved, so "
            "the reading would be wrong",
            "Moving a detector while it is switched on resets its count to "
            "zero automatically",
        ],
        "correct_index": 0,
        "why": "There is nowhere on Earth with no background radiation, so "
               "moving the detector changes the value slightly but never "
               "removes it.",
    },
    {
        "id": "ks4-background-radiation-s17",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the published UK annual dose figure is described "
                "as an average.",
        "options": [
            "It is the dose measured in the middle month of the year and "
            "multiplied by twelve, which is the simplest way of estimating a "
            "yearly figure",
            "Individual doses differ with home, job, altitude and medical "
            "treatment, so one figure has to stand for a wide range",
            "It is the mean of the highest and the lowest dose recorded "
            "anywhere in the country, so most people receive something between "
            "the two",
            "It is an estimate, because dose cannot be measured for any one "
            "individual person, since no instrument is sensitive enough to "
            "follow one person",
        ],
        "correct_index": 1,
        "why": "The figure summarises a population in which some people "
               "receive several times what others do, so no individual should "
               "assume it is their own dose.",
    },
    {
        "id": "ks4-background-radiation-s18",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A person's annual dose is 2.4 mSv, of which 0.36 mSv comes "
                "from food and drink. Calculate the percentage of their dose "
                "that comes from food and drink.",
        "options": [
            "15%",
            "6.7%",
            "36%",
            "0.15%",
        ],
        "correct_index": 0,
        "why": "The fraction is 0.36 ÷ 2.4 = 0.15, which as a percentage is "
               "15%.",
    },

    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # Two-stage corrections, comparisons in which the background cancels, and
    # judgements about what a measurement can and cannot show.
    {
        "id": "ks4-background-radiation-h05",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "With no source present a detector records 260 counts in 10 "
                "minutes. With a source in place it records 1160 counts in 4 "
                "minutes. Calculate the corrected count rate of the source.",
        "options": [
            "264 counts per minute",
            "290 counts per minute",
            "900 counts per minute",
            "234 counts per minute",
        ],
        "correct_index": 0,
        "why": "Background is 260 ÷ 10 = 26 counts per minute and the "
               "measured rate is 1160 ÷ 4 = 290, so the corrected rate is 290 "
               "− 26 = 264 counts per minute.",
    },
    {
        "id": "ks4-background-radiation-h06",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two sources are measured one after the other on the same "
                "detector in the same room, and one reads higher than the "
                "other. Determine whether subtracting the background could "
                "change which of them is the more active.",
        "options": [
            "Yes, because the background affects a weak source more than a "
            "strong one",
            "No, because the same background is included in both readings, so "
            "the order is unchanged",
            "Yes, because background radiation varies too much between two "
            "successive measurements",
            "No, because background radiation does not reach a detector while "
            "a source is in front of it, however weak that source may be",
        ],
        "correct_index": 1,
        "why": "Taking the same number from both readings leaves the "
               "difference between them unchanged, so the ranking survives — "
               "though each source's own activity is still overstated until "
               "the correction is made.",
    },
    {
        "id": "ks4-background-radiation-h07",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A source reads 148 counts per minute in a laboratory where "
                "the background is 48, and 118 counts per minute in another "
                "where the background is 18. Determine whether the two "
                "readings are consistent with it being the same source.",
        "options": [
            "No, because a source cannot give two different readings if it is "
            "unchanged",
            "No, because the second laboratory must be shielding part of the "
            "radiation",
            "Yes, because both corrected rates come to 100 counts per minute",
            "Yes, because the two readings differ by less than a third of the "
            "larger one, which is well within experimental error",
        ],
        "correct_index": 2,
        "why": "Correcting each reading gives 148 − 48 = 100 and 118 − 18 = "
               "100, so the source itself is behaving identically in both "
               "rooms.",
    },
    {
        "id": "ks4-background-radiation-h08",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that background radiation makes accurate "
                "radioactivity measurements impossible in a school "
                "laboratory.",
        "options": [
            "It is correct, because the background cannot be measured to any "
            "useful accuracy",
            "It is correct, because school detectors are not sensitive enough "
            "to separate a source from the background, even in a well-equipped "
            "laboratory",
            "It is wrong, because background radiation stops at the walls of a "
            "building and so cannot get inside a laboratory building",
            "It is wrong, because the background can be measured and "
            "subtracted, and school sources give count rates well above it",
        ],
        "correct_index": 3,
        "why": "A known, measurable background is a correction rather than an "
               "obstacle; it only limits the work when the source's own count "
               "rate is comparable with it.",
    },
    {
        "id": "ks4-background-radiation-h09",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Four people live in the same city. Determine which of them is "
                "likely to receive the largest annual radiation dose.",
        "options": [
            "A gardener who works outdoors for most of the year, handling soil "
            "that carries natural radioactivity on his hands and boots",
            "A long-haul pilot living in a granite-built house who has had "
            "two CT scans this year",
            "A swimmer who trains in an indoor pool every morning",
            "A night-shift worker who sleeps during the day with the curtains "
            "closed in a poorly ventilated room",
        ],
        "correct_index": 1,
        "why": "The pilot gathers three raised contributions at once — extra "
               "cosmic rays at altitude, extra radon and gamma from granite, "
               "and a large medical dose.",
    },
    {
        "id": "ks4-background-radiation-h10",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pupil doubles the counting time and finds that the total "
                "number of counts roughly doubles while the count rate stays "
                "about the same. Explain this result.",
        "options": [
            "The detector becomes less sensitive as it runs, which cancels out "
            "the extra counts gained in the second half of the measurement as "
            "the tube tires",
            "Count rate is counts divided by time, so doubling both leaves "
            "the rate unchanged while the longer count is more reliable",
            "Radioactive decay speeds up slightly while a detector is left "
            "switched on nearby, which is why longer counts give larger totals",
            "Doubling the time halves the count rate, which is why the total "
            "appears to stay the same from one measurement to the next",
        ],
        "correct_index": 1,
        "why": "Rate is a quantity per unit time, so a longer count changes "
               "the total but not the rate — it simply averages out more of "
               "the randomness.",
    },
    {
        "id": "ks4-background-radiation-h11",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that background radiation must be "
                "harmless, because humans have lived with it throughout their "
                "history.",
        "options": [
            "It is sound, because the body has evolved a mechanism that "
            "repairs every kind of radiation damage, whatever the type of "
            "radiation and whatever the dose",
            "It is sound, because radiation that occurs naturally is a "
            "different type from the radiation used in laboratories, so the "
            "two cannot be compared on the same scale",
            "It is unsound, because the ionising radiation in the background "
            "carries the same small risk as any other, and radon is a known "
            "cause of lung cancer",
            "It is unsound, because background radiation has become far "
            "stronger than it was in the past, chiefly because of the granite "
            "used in modern building work",
        ],
        "correct_index": 2,
        "why": "Being unavoidable is not the same as being harmless: "
               "background radiation carries a real if small risk, which is "
               "why radon levels in homes are managed.",
    },
    {
        "id": "ks4-background-radiation-h12",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A CT scan gives a dose of 7.2 mSv. A person's average annual "
                "background dose is 2.4 mSv. Calculate how many years of "
                "background the scan is equivalent to.",
        "options": [
            "3 years",
            "4.8 years",
            "9.6 years",
            "0.33 years",
        ],
        "correct_index": 0,
        "why": "Dividing the scan dose by the annual dose gives 7.2 ÷ 2.4 = 3 "
               "years.",
    },
    {
        "id": "ks4-background-radiation-h13",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a count rate in counts per minute cannot on its "
                "own tell a doctor how dangerous a source is to a patient.",
        "options": [
            "A count rate is measured at one place and says nothing about how "
            "much energy the tissue absorbs or how damaging that type is",
            "A count rate is only valid for gamma sources, and patients are "
            "given beta emitters",
            "A count rate changes with the time of day, so a single value is "
            "meaningless",
            "A count rate cannot be converted into any other quantity, "
            "because it has no unit",
        ],
        "correct_index": 0,
        "why": "Harm depends on absorbed energy and on the type of radiation, "
               "which is what the sievert expresses; a count rate is just how "
               "often a particular detector clicks.",
    },
    {
        "id": "ks4-background-radiation-h14",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A class measures the background on Monday as 24 counts per "
                "minute and on Friday as 29 counts per minute in the same "
                "room. Suggest how the class should proceed.",
        "options": [
            "Use Monday's value for everything, because the first measurement "
            "is the reliable one, and later readings only add uncertainty to "
            "it",
            "Abandon the experiment, because an inconsistent background makes "
            "the work invalid, since no correction can be made without a fixed "
            "value to correct against",
            "Use the higher value throughout, so that every corrected result "
            "is a safe underestimate, which is the safer way to report any "
            "result",
            "Measure the background again on each day of the experiment and "
            "correct that day's readings with that day's value",
        ],
        "correct_index": 3,
        "why": "The difference is ordinary random variation, and the "
               "correction is most accurate when the background used is the "
               "one measured alongside the source readings.",
    },
    {
        "id": "ks4-background-radiation-h15",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A householder tests for radon over a single weekend and "
                "concludes the house is safe. Evaluate the conclusion.",
        "options": [
            "It is reliable, because radon enters a house at a steady rate "
            "all year round",
            "It is unreliable, because radon levels change with ventilation "
            "and season, so a short test may miss the highest levels",
            "It is unreliable, because radon cannot be detected in under a "
            "month of continuous testing",
            "It is reliable, because a weekend covers both a working day and "
            "a rest day",
        ],
        "correct_index": 1,
        "why": "Indoor radon varies with how the house is ventilated and with "
               "the weather, so a representative figure needs a measurement "
               "spanning months.",
    },
    {
        "id": "ks4-background-radiation-h16",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A pupil argues that because the background is only 26 counts "
                "per minute and her source reads 900, correcting for the "
                "background is a waste of time. Evaluate the argument.",
        "options": [
            "She is right, because a background below 50 counts per minute is "
            "ignored by convention",
            "She is wrong, because the background must be added to a strong "
            "source rather than subtracted",
            "She is right, because background radiation does not reach a "
            "detector once a strong source is in front of it on the laboratory "
            "bench where the tube is standing",
            "She has a fair point for this reading, but the same correction "
            "becomes essential once the source has decayed to a low count rate",
        ],
        "correct_index": 3,
        "why": "26 in 900 is a 3% effect, but the same 26 counts per minute "
               "dominate a reading of 40 — so the correction is always made, "
               "because the point at which it matters arrives without warning.",
    },
    {
        "id": "ks4-background-radiation-h17",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A laboratory whose background is normally about 30 counts "
                "per minute records 300 counts per minute with no source out "
                "on the bench. Suggest the most likely explanation.",
        "options": [
            "Background radiation rose tenfold across the country that "
            "morning",
            "A radioactive source has been left unshielded somewhere in the "
            "room",
            "The detector has become radioactive through long use near "
            "sources",
            "Cosmic rays were unusually intense because the laboratory is on "
            "an upper floor",
        ],
        "correct_index": 1,
        "why": "A tenfold jump in one room is far too large for natural "
               "variation, so the sensible first check is whether a source is "
               "out of its container.",
    },
    {
        "id": "ks4-background-radiation-h18",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why absorbing a given amount of energy from alpha "
                "radiation is recorded as a larger dose in sieverts than "
                "absorbing the same energy from gamma radiation.",
        "options": [
            "Alpha radiation carries a positive charge, and charged radiation "
            "is measured on a scale of its own rather than in sieverts",
            "Alpha radiation travels more slowly, so the body is exposed to it "
            "for a longer time, giving the cells around it longer to absorb "
            "the energy",
            "Alpha radiation ionises far more densely along its path, so the "
            "same energy does more biological damage",
            "Alpha radiation has a shorter half-life, so more of it is "
            "absorbed in the same period, so a larger share of it arrives "
            "during the measurement",
        ],
        "correct_index": 2,
        "why": "The sievert weights absorbed energy by how harmful that type "
               "of radiation is, and alpha's dense ionisation over a short "
               "track damages far more molecules in the cells it crosses.",
    },

    # ══ standard · s19–s26 ═══════════════════════════════════════════════
    # The natural/artificial split, altitude and occupation carried further,
    # and fresh dose arithmetic on numbers not used above.
    {
        "id": "ks4-background-radiation-s19",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the artificial contribution to a person's "
                "annual dose is normally much smaller than the natural "
                "contribution.",
        "options": [
            "Medical and industrial sources reach only some people for "
            "part of the year, while rocks, air, food and space add to "
            "everyone's dose all year round",
            "Every artificial source is switched off long before its "
            "radiation can reach a person, unlike a natural source, which "
            "is never switched off",
            "Hospitals and factories are required to shield every "
            "artificial source so completely that almost none of its "
            "radiation escapes to reach anybody",
            "Artificial sources emit only alpha radiation, which adds very "
            "little to a dose measured in sieverts once it has passed "
            "through the surrounding air",
        ],
        "correct_index": 0,
        "why": "Natural sources act on the whole population continuously, "
               "whereas artificial exposure is occasional and reaches a "
               "smaller share of people at any one time.",
    },
    {
        "id": "ks4-background-radiation-s20",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an astronaut receives a far higher cosmic-ray "
                "dose than an airline pilot flying the same number of "
                "hours.",
        "options": [
            "An astronaut's spacecraft is made of a lighter material than "
            "an aircraft's hull, so it shields much less of the cosmic "
            "radiation arriving from space",
            "An astronaut works far above the atmosphere, which absorbs "
            "most cosmic radiation before it reaches even a cruising "
            "aircraft, let alone the ground",
            "An astronaut is exposed to the same cosmic-ray intensity as a "
            "pilot, but for many more hours at a time during one mission",
            "An astronaut's body is not shielded by clothing in the way a "
            "pilot's is, since a spacesuit is built to hold pressure "
            "rather than to absorb radiation",
        ],
        "correct_index": 1,
        "why": "The atmosphere absorbs cosmic radiation with height; an "
               "aircraft still sits within a thinning atmosphere, while a "
               "spacecraft has left almost all of it behind.",
    },
    {
        "id": "ks4-background-radiation-s21",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a cellar dug into the ground typically shows a "
                "higher radon reading than a bedroom on the floor above it "
                "in the same house.",
        "options": [
            "Cellars are built from different materials than the rest of "
            "the house, and those materials release far more radon than "
            "ordinary bricks or plaster do",
            "The cellar walls are usually thicker than upstairs walls, so "
            "more of the gamma radiation from the rock outside is "
            "absorbed and released as radon",
            "Radon seeps in directly from the ground, so the room in "
            "closest contact with the soil receives it first and at the "
            "highest concentration",
            "A cellar is colder than an upstairs room, and radioactive "
            "decay in the surrounding rock runs faster at lower "
            "temperatures, producing more radon",
        ],
        "correct_index": 2,
        "why": "Radon's source is the ground itself, so the room nearest "
               "the soil — usually a cellar — meets it before it has been "
               "diluted by mixing through the rest of the house.",
    },
    {
        "id": "ks4-background-radiation-s22",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A person's estimated dose from natural background is 4.8 "
                "mSv over one year, delivered at a steady rate throughout "
                "the year. Calculate their average monthly dose.",
        "options": [
            "57.6 mSv",
            "0.04 mSv",
            "1.2 mSv",
            "0.4 mSv",
        ],
        "correct_index": 3,
        "why": "Dividing the annual dose evenly across the year: "
               "4.8 ÷ 12 = 0.4 mSv per month.",
    },
    {
        "id": "ks4-background-radiation-s23",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A CT scan gives a patient a dose of about 8 mSv, and a "
                "plain chest X-ray gives about 0.02 mSv. Calculate roughly "
                "how many chest X-rays would be needed to match the dose "
                "of one CT scan.",
        "options": [
            "400",
            "40",
            "4000",
            "16",
        ],
        "correct_index": 0,
        "why": "Dividing one dose by the other: 8 ÷ 0.02 = 400.",
    },
    {
        "id": "ks4-background-radiation-s24",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a worker who quarries granite for a living "
                "typically receives a higher occupational radiation dose "
                "than an office worker in the same town.",
        "options": [
            "Granite quarrying uses heavy diesel machinery that generates "
            "its own ionising radiation as a by-product of the engines "
            "and hydraulic systems running throughout each long shift on "
            "site",
            "The worker spends the working day close to freshly broken "
            "granite, which releases more radon and gamma radiation than "
            "granite left undisturbed for years",
            "Granite quarry workers are legally required to carry a "
            "personal source of radiation for monitoring, which itself "
            "adds to their measured dose",
            "The office worker's building is built from materials that "
            "actively absorb background radiation before it can reach "
            "anyone working inside it",
        ],
        "correct_index": 1,
        "why": "Freshly exposed and broken rock releases radon more "
               "readily than intact rock, and the quarry worker spends the "
               "day close to it and to the dust it produces.",
    },
    {
        "id": "ks4-background-radiation-s25",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why doctors describe the dose from a single "
                "routine X-ray as very small when set against a lifetime "
                "of natural background exposure.",
        "options": [
            "A single X-ray delivers no measurable dose at all, so any "
            "comparison with background exposure is really only a "
            "formality for the patient's records",
            "Natural background stops contributing to a person's dose "
            "once they reach adulthood, so only childhood background is "
            "ever compared with a medical dose",
            "A lifetime of natural background adds up to many times the "
            "dose of one X-ray, because it is received continuously over "
            "many decades rather than once",
            "An X-ray uses a different type of radiation from natural "
            "background, so the two doses cannot be compared on the same "
            "numerical scale at all",
        ],
        "correct_index": 2,
        "why": "Background accumulates for a lifetime, so even a dose that "
               "seems large next to one X-ray is small next to the total "
               "received over many decades.",
    },
    {
        "id": "ks4-background-radiation-s26",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest one change to a person's lifestyle that would "
                "reduce the cosmic-ray dose they receive over a year.",
        "options": [
            "Eating less meat and more vegetables, since meat carries a "
            "higher concentration of naturally radioactive isotopes",
            "Spending more time outdoors during the day rather than "
            "remaining indoors under a roof",
            "Sleeping with the bedroom window closed rather than open "
            "throughout the year",
            "Taking fewer long-haul flights, since cosmic-ray dose rises "
            "with the time spent at cruising altitude",
        ],
        "correct_index": 3,
        "why": "Cosmic-ray intensity is much greater at aircraft cruising "
               "altitude than at ground level, so time spent flying is a "
               "lifestyle factor within a person's control.",
    },

    # ══ harder · h19–h26 ═════════════════════════════════════════════════
    # Multi-source arithmetic across named people and years, and judgements
    # that turn on the natural/artificial split and on detector behaviour.
    {
        "id": "ks4-background-radiation-h19",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that banning all non-essential medical "
                "X-rays would remove most of a typical person's annual "
                "radiation dose.",
        "options": [
            "The claim is unsound: artificial sources make up only a "
            "small share of the average dose, so removing every X-ray "
            "would leave the far larger natural contribution untouched",
            "The claim is sound: medical procedures are the single "
            "largest contributor to the average annual dose figure, well "
            "ahead of radon and every other natural source combined once "
            "the whole population is counted",
            "The claim is sound, because banning X-rays would also stop "
            "the background radiation released by hospital equipment when "
            "it is not in use",
            "The claim is unsound, because an X-ray uses a different type "
            "of radiation from the kind counted in the average annual "
            "dose figure",
        ],
        "correct_index": 0,
        "why": "Natural sources such as radon, rocks and cosmic rays make "
               "up most of the average dose, so removing artificial "
               "sources alone leaves most of it unchanged.",
    },
    {
        "id": "ks4-background-radiation-h20",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two Geiger counters of different sensitivity are both "
                "correctly calibrated and both have their own background "
                "subtracted. Evaluate the claim that they must then read "
                "the same corrected count rate for one source.",
        "options": [
            "The claim is sound, because subtracting each detector's own "
            "measured background removes any difference caused by the "
            "design or the sensitivity of either instrument",
            "The claim is unsound, because a more sensitive detector "
            "registers a larger share of the decays reaching it, so its "
            "corrected reading is naturally higher",
            "The claim is sound, because two correctly calibrated "
            "detectors always have identical sensitivity by definition, "
            "whatever their design",
            "The claim is unsound, because background radiation cannot be "
            "measured accurately enough for any two detectors to be "
            "compared fairly",
        ],
        "correct_index": 1,
        "why": "Correcting for background removes the detector's own "
               "baseline, but it does not equalise how efficiently two "
               "different detectors register the decays that do reach "
               "them.",
    },
    {
        "id": "ks4-background-radiation-h21",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Person A's annual dose is made up of 1.5 mSv from radon, "
                "0.2 mSv from cosmic rays, 0.3 mSv from food and 0.1 mSv "
                "from medical procedures. Person B's is 0.4 mSv from "
                "radon, 0.3 mSv from cosmic rays, 0.3 mSv from food and "
                "1.8 mSv from medical procedures. Determine who receives "
                "the higher total dose, and why.",
        "options": [
            "Person A, because radon is always the largest contributor to "
            "anybody's annual dose, whoever they are and wherever they "
            "live",
            "Neither, because the two totals must be equal once every "
            "contribution has been added up correctly on both sides",
            "Person B, because their large medical contribution outweighs "
            "person A's larger radon contribution once every source is "
            "added up",
            "Person A, because natural sources are always larger overall "
            "than artificial ones for any person, in any year, without "
            "exception",
        ],
        "correct_index": 2,
        "why": "Person A totals 2.1 mSv and person B totals 2.8 mSv, so "
               "B's unusually high medical dose that year makes their "
               "total the larger of the two.",
    },
    {
        "id": "ks4-background-radiation-h22",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A person's annual dose is 2.7 mSv from natural sources "
                "plus 1.3 mSv from a course of medical treatment in one "
                "year. The following year they receive no medical "
                "treatment. Calculate the percentage decrease in their "
                "annual dose between the two years.",
        "options": [
            "13%",
            "48%",
            "68%",
            "32.5%",
        ],
        "correct_index": 3,
        "why": "The first year totals 4.0 mSv and the second totals 2.7 "
               "mSv, a fall of 1.3 mSv; 1.3 ÷ 4.0 × 100 = 32.5%.",
    },
    {
        "id": "ks4-background-radiation-h23",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that quoting a single average annual "
                "dose figure means nobody needs to know how their own "
                "dose splits between natural and artificial sources.",
        "options": [
            "The claim is unsound, because a person can only reduce the "
            "artificial part of their dose through choices such as "
            "flights or scans, so the split matters to anyone managing "
            "their own exposure",
            "The claim is sound, because the published average figure "
            "already accounts for every individual person's own split "
            "between their natural and artificial sources of exposure",
            "The claim is sound, because natural and artificial radiation "
            "affect the body in identical ways, so distinguishing between "
            "them serves no purpose",
            "The claim is unsound, because the average figure is measured "
            "incorrectly whenever natural and artificial sources are not "
            "reported separately",
        ],
        "correct_index": 0,
        "why": "The natural part of a dose is largely outside anyone's "
               "control, while flights, scans and other artificial "
               "exposures are choices a person can influence.",
    },
    {
        "id": "ks4-background-radiation-h24",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Radon supplies about half of the natural background, and "
                "natural sources make up about 85% of a person's total "
                "average annual dose. Calculate the approximate "
                "percentage of the TOTAL annual dose that radon alone "
                "provides.",
        "options": [
            "85%",
            "42.5%",
            "50%",
            "17%",
        ],
        "correct_index": 1,
        "why": "Radon is half of the natural share: 0.5 × 85% = 42.5% of "
               "the total dose.",
    },
    {
        "id": "ks4-background-radiation-h25",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A homeowner in a high-radon area is advised to have a "
                "sump fitted beneath the floor to vent the gas outside, "
                "rather than simply opening a window when they remember "
                "to. Evaluate why the sump is judged the more effective "
                "long-term solution.",
        "options": [
            "A sump works by absorbing the radon chemically before it "
            "can enter the house, whereas an open window only dilutes "
            "gas that has already got in",
            "A sump increases the air pressure inside the house, which "
            "stops radon rising through the floor from the ground below "
            "at any time of year",
            "A sump removes radon continuously at its entry point "
            "regardless of habit or season, while a window depends on "
            "someone remembering to open it",
            "A sump and an open window achieve exactly the same "
            "reduction, so the advice to install one is really a matter "
            "of the homeowner's own preference",
        ],
        "correct_index": 2,
        "why": "Ventilation only helps while a window is actually open, "
               "but a sump works automatically and continuously at the "
               "point where the gas enters.",
    },
    {
        "id": "ks4-background-radiation-h26",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A long-haul airline pilot flies for about 900 hours a "
                "year and receives roughly 5 microsieverts of cosmic-ray "
                "dose for each hour spent at cruising altitude. Calculate "
                "their approximate annual dose from flying alone, and "
                "compare it with a UK average annual dose of 2.7 mSv from "
                "all sources combined.",
        "options": [
            "0.45 mSv, which is well below the UK average from all "
            "sources",
            "45 mSv, more than fifteen times the UK average from all "
            "sources",
            "0.9 mSv, about a third of the UK average from all sources",
            "4.5 mSv, more than the UK average from all sources combined",
        ],
        "correct_index": 3,
        "why": "900 × 5 microsieverts = 4500 microsieverts = 4.5 mSv, "
               "which by itself already exceeds the average 2.7 mSv most "
               "people receive from every source together.",
    },
]
