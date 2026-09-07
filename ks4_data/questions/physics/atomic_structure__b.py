"""Physics · Atomic structure — the radiation-in-use half of the topic.

Five subtopics: radioactive contamination, background radiation, uses of
nuclear radiation, nuclear fission and nuclear fusion. (`atomic_structure__a.py`
holds the other six, from the structure of the atom through half-lives.)

The distractors are built from four misconceptions the topic produces every
year: contamination read as irradiation (and the belief that being irradiated
leaves an object radioactive); background radiation assumed to be mostly
man-made, and left unsubtracted before a half-life is read off; fission and
fusion swapped, with the moderator credited with the control rods' job; and
"more penetrating" taken to mean "more dangerous" regardless of whether the
source is inside or outside the body.

Only `radioactive-contamination` is BASE — the other four are physics-only
Triple content, so their questions may use the Triple prose but are still
written at foundation tier.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ── radioactive-contamination ───────────────────────────────────────
    # BASE: tier='foundation', triple_only=False
    {
        "id": "ks4-radioactive-contamination-e01",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by radioactive contamination.",
        "options": [
            "Exposure to radiation from a source that is a short distance away",
            "Damage caused to living cells by any form of ionising radiation",
            "Unwanted radioactive material deposited on or inside an object "
            "or person",
            "The gradual increase in an object's activity while it is near a "
            "source",
        ],
        "correct_index": 2,
        "why": "Contamination is radioactive material itself being deposited "
               "on or in something, so the source travels with it and keeps "
               "emitting.",
    },
    {
        "id": "ks4-radioactive-contamination-e02",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A laboratory bench is checked with a detector after a "
                "practical. The count rate above one spot stays high even "
                "though every source has been locked away. State what this "
                "shows.",
        "options": [
            "The bench has been contaminated — radioactive material has been "
            "left on it",
            "The bench has been irradiated, and will now stay radioactive "
            "for ever",
            "The detector is faulty, because a bench cannot read above the "
            "background level",
            "The locked-away sources are still irradiating the bench through "
            "their container",
        ],
        "correct_index": 0,
        "why": "Irradiation stops the moment the source is removed, so a "
               "reading that persists means radioactive material itself has "
               "been left behind — that is contamination.",
    },
    {
        "id": "ks4-radioactive-contamination-e03",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A technician must move an unsealed radioactive powder "
                "between two containers. Which precaution is aimed "
                "specifically at preventing contamination?",
        "options": [
            "Standing as far from the bench as the task allows",
            "Keeping the time spent on the task as short as possible",
            "Reading a dosimeter badge before and after the task",
            "Handling the powder with tongs and wearing gloves",
        ],
        "correct_index": 3,
        "why": "Tongs and gloves stop the radioactive material itself from "
               "touching the skin, which is what contamination is.",
    },
    {
        "id": "ks4-radioactive-contamination-e04",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed source is kept in a rack two metres from where "
                "students work. State which type of radiation from it is the "
                "greatest hazard.",
        "options": [
            "Alpha, because it is the most strongly ionising of the three",
            "Gamma, because it penetrates deeply and reaches the students' "
            "tissue",
            "Beta, because it carries a negative charge and is attracted to "
            "the body",
            "All three equally, because the hazard depends only on the "
            "distance",
        ],
        "correct_index": 1,
        "why": "From outside the body, only gamma penetrates far enough to "
               "reach and damage internal tissue; alpha is stopped by air and "
               "skin.",
    },
    {
        "id": "ks4-radioactive-contamination-s01",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student uses tongs to hold a sealed gamma source at arm's "
                "length for two minutes, then returns it to its lead-lined "
                "box. Describe what has happened to the student.",
        "options": [
            "She has been irradiated, and her exposure ended when the source "
            "was boxed",
            "She has been contaminated, because gamma rays have entered her "
            "body",
            "She has been contaminated, because she was within two metres of "
            "the source",
            "Neither, because a sealed source cannot expose anyone to "
            "radiation",
        ],
        "correct_index": 0,
        "why": "The source stayed sealed and outside her, so this is "
               "irradiation — the exposure stops when the source is shielded "
               "or removed.",
    },
    {
        "id": "ks4-radioactive-contamination-s02",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why staff who work with radioactive sources wear a "
                "dosimeter badge.",
        "options": [
            "It absorbs the radiation before it reaches the wearer's body",
            "It warns the wearer that radioactive material is on their skin",
            "It neutralises any radioactive dust that settles on the clothing",
            "It records the total dose received, so limits can be checked "
            "over time",
        ],
        "correct_index": 3,
        "why": "A dosimeter measures rather than blocks: it records cumulative "
               "dose so a worker's exposure can be kept within annual limits.",
    },
    {
        "id": "ks4-radioactive-contamination-s03",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A trace of an alpha-emitting compound is spilt on the back "
                "of a worker's hand and washed off within a minute. Explain "
                "why this is far less serious than swallowing the same trace.",
        "options": [
            "Washing removes the radioactivity, whereas swallowing it cannot "
            "be undone",
            "Alpha particles cannot penetrate the outer layer of dead skin, "
            "so living tissue is barely reached",
            "Alpha radiation only becomes ionising once it is inside a warm "
            "body",
            "Skin contact is irradiation, and irradiation is always harmless",
        ],
        "correct_index": 1,
        "why": "Alpha has a very short range — outside the body the dead outer "
               "skin absorbs it, but swallowed it deposits all its energy in "
               "living tissue.",
    },
    {
        "id": "ks4-radioactive-contamination-s04",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a school keeps its gamma source in a lead-lined "
                "container when it is not in use.",
        "options": [
            "The lead stops the source decaying, so it lasts more school years",
            "The lead prevents radioactive atoms escaping and settling on the "
            "shelves",
            "The lead absorbs the gamma rays, so the dose to people in the "
            "room is reduced",
            "The lead keeps the source cool, which lowers its activity",
        ],
        "correct_index": 2,
        "why": "Shielding is one of the three ways to cut irradiation, and "
               "lead is dense enough to absorb most of the gamma before it "
               "reaches anyone.",
    },
    {
        "id": "ks4-radioactive-contamination-h01",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Worker A spends one hour two metres from a sealed gamma "
                "source. Worker B swallows a small quantity of an "
                "alpha-emitting powder. Compare the risk to each worker over "
                "the following month.",
        "options": [
            "A is at greater risk all month, because gamma is the most "
            "penetrating radiation",
            "Both are at equal risk, because each received a dose on the same "
            "day",
            "B is at greater risk only on the first day, because alpha has a "
            "very short range",
            "B is at greater risk all month, because the source stays inside "
            "him and keeps ionising nearby tissue",
        ],
        "correct_index": 3,
        "why": "A's exposure ended when he walked away; B is contaminated, so "
               "a highly ionising alpha emitter goes on depositing all its "
               "energy in his tissue.",
    },
    {
        "id": "ks4-radioactive-contamination-h02",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Surgical instruments are sealed in plastic and irradiated "
                "with gamma rays to sterilise them. A student says the "
                "instruments must now be stored as radioactive waste. "
                "Evaluate the student's reasoning.",
        "options": [
            "Correct, because anything that absorbs gamma radiation becomes a "
            "source itself",
            "Incorrect, because irradiation does not deposit any radioactive "
            "material, so the instruments are not contaminated",
            "Correct, because the sealed packaging traps the gamma rays "
            "inside with the instruments",
            "Incorrect, because gamma rays are too weakly ionising to affect "
            "the instruments at all",
        ],
        "correct_index": 1,
        "why": "Being irradiated is not the same as being contaminated — no "
               "radioactive atoms are transferred, so the instruments emit "
               "nothing once the source is removed.",
    },
    {
        "id": "ks4-radioactive-contamination-h03",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nurse says that wearing disposable gloves protects her "
                "from a sealed gamma source she stands beside. Explain the "
                "error in her reasoning.",
        "options": [
            "Gloves are the wrong material — lead-lined gloves would stop the "
            "gamma rays completely",
            "There is no error, because gloves are the standard precaution "
            "against every radiation hazard",
            "Gloves guard against contamination by contact, but a sealed "
            "source irradiates her and thin gloves do not absorb gamma",
            "Gloves increase her risk, because they hold radioactive dust "
            "against the skin for longer",
        ],
        "correct_index": 2,
        "why": "Gloves prevent radioactive material touching the skin; against "
               "penetrating gamma from a sealed source, only distance, time "
               "and dense shielding help.",
    },
    {
        "id": "ks4-radioactive-contamination-h04",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A doctor offers a patient a CT scan, which delivers a "
                "radiation dose far larger than a single chest X-ray. "
                "Evaluate whether the scan should go ahead.",
        "options": [
            "It should go ahead only if the diagnostic benefit outweighs the "
            "increased risk from the dose",
            "It should never go ahead, because all ionising radiation "
            "increases cancer risk",
            "It should always go ahead, because medical radiation is a "
            "natural source and so carries no risk",
            "It should go ahead only if the patient has had no other scan "
            "that year, as the risk resets annually",
        ],
        "correct_index": 0,
        "why": "Medical use of radiation is a benefit-against-risk judgement: "
               "the risk is managed and justified, never eliminated.",
    },

    # ── background-radiation ────────────────────────────────────────────
    # TRIPLE ONLY: tier='foundation', triple_only=True
    {
        "id": "ks4-background-radiation-e01",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by background radiation.",
        "options": [
            "Radiation released only when a radioactive source is opened in a "
            "laboratory",
            "Low-level ionising radiation present in the environment at all "
            "times",
            "Radiation left over in a detector from the previous measurement",
            "Radiation given out by the walls of a building but not by the "
            "ground",
        ],
        "correct_index": 1,
        "why": "Background radiation is the low-level ionising radiation "
               "always present around us, from natural and artificial sources "
               "alike.",
    },
    {
        "id": "ks4-background-radiation-e02",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the largest single contributor to background radiation "
                "in the UK.",
        "options": [
            "Cosmic rays arriving from space",
            "Waste from nuclear power stations",
            "Naturally occurring isotopes in food and drink",
            "Radon gas seeping out of rocks and into buildings",
        ],
        "correct_index": 3,
        "why": "Radon gas accounts for roughly half of the UK's average "
               "background dose — more than every other source combined.",
    },
    {
        "id": "ks4-background-radiation-e03",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the unit in which radiation dose is measured.",
        "options": [
            "The sievert",
            "The becquerel",
            "The count per minute",
            "The joule",
        ],
        "correct_index": 0,
        "why": "Dose is measured in sieverts (often millisieverts), because "
               "the sievert accounts for the biological effect as well as the "
               "amount of radiation.",
    },
    {
        "id": "ks4-background-radiation-e04",
        "subtopic_slug": "background-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which of these contributions to background radiation is an "
                "artificial source?",
        "options": [
            "Gamma rays emitted by granite in building materials",
            "Carbon-14 and potassium-40 present in food",
            "Medical procedures such as CT scans and nuclear medicine",
            "Cosmic rays reaching the ground from space",
        ],
        "correct_index": 2,
        "why": "Medical procedures are the largest artificial contribution; "
               "rocks, food and cosmic rays are all natural sources.",
    },
    {
        "id": "ks4-background-radiation-s01",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a long-haul airline pilot receives a higher "
                "annual radiation dose than an office worker in the same city.",
        "options": [
            "Aircraft fuel contains traces of radioactive isotopes that decay "
            "in flight",
            "The aluminium fuselage of the aircraft emits gamma radiation "
            "when it is cold",
            "At cruising altitude there is less atmosphere above to absorb "
            "cosmic rays, so the pilot receives more of them",
            "Radon gas collects in the pressurised cabin because the air is "
            "recycled",
        ],
        "correct_index": 2,
        "why": "The atmosphere shields us from cosmic rays, so the higher you "
               "fly the less shielding there is and the greater the cosmic "
               "contribution to your dose.",
    },
    {
        "id": "ks4-background-radiation-s02",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two identical houses are built on the same day, one on "
                "granite in Cornwall and one on clay in Essex. Suggest why "
                "the Cornish house records a higher background count rate "
                "indoors.",
        "options": [
            "Cornwall is closer to the sea, and sea water is a strong gamma "
            "emitter",
            "Granite contains more uranium, so more radon gas seeps into the "
            "house from the ground",
            "Clay absorbs cosmic rays before they reach the house, while "
            "granite does not",
            "Houses built on granite are usually older, so their materials "
            "have decayed more",
        ],
        "correct_index": 1,
        "why": "Radon is produced by uranium in the rock beneath a building, "
               "and granite areas hold more uranium — so more radon seeps in.",
    },
    {
        "id": "ks4-background-radiation-s03",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "With no source present a Geiger counter records 46 counts "
                "per minute. A source is then placed nearby and the counter "
                "records 730 counts in 5 minutes. Calculate the corrected "
                "count rate of the source.",
        "options": [
            "100 counts per minute",
            "146 counts per minute",
            "684 counts per minute",
            "192 counts per minute",
        ],
        "correct_index": 0,
        "why": "The measured rate is 730 ÷ 5 = 146 counts per minute, and the "
               "corrected rate is 146 − 46 = 100 counts per minute.",
    },
    {
        "id": "ks4-background-radiation-s04",
        "subtopic_slug": "background-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the background count rate should be measured "
                "over a long period and then averaged.",
        "options": [
            "Because the detector heats up, and a warm detector always counts "
            "faster",
            "Because background radiation slowly decays away while the "
            "experiment runs",
            "Because a long count uses up the background radiation in the "
            "room",
            "Because radioactive decay is random, so a short count gives an "
            "unreliable value",
        ],
        "correct_index": 3,
        "why": "Decay is a random process, so counts fluctuate from minute to "
               "minute; averaging over a long time gives a value close to the "
               "true mean.",
    },
    {
        "id": "ks4-background-radiation-h01",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Background is 30 counts per minute. A source reads 230 "
                "counts per minute at the start and 130 counts per minute two "
                "hours later. A student takes the half-life to be the time "
                "for the reading to fall to 115 counts per minute. Explain "
                "why her half-life will be too long.",
        "options": [
            "She has halved the wrong quantity — the source alone falls from "
            "200 to 100 in two hours, so the true half-life is two hours",
            "She has used minutes rather than hours, so her answer is sixty "
            "times too large",
            "She should have added the background instead, giving 260 counts "
            "per minute as her starting value",
            "Her method is sound — the background is too small to change the "
            "result noticeably",
        ],
        "correct_index": 0,
        "why": "Background must be subtracted first: the source's own rate "
               "goes 200 → 100 in two hours, while the uncorrected reading "
               "never falls below 30 and so takes longer to appear to halve.",
    },
    {
        "id": "ks4-background-radiation-h02",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The average annual dose in the UK is about 2.7 mSv, of which "
                "roughly 50% comes from radon. Calculate the average annual "
                "dose due to radon.",
        "options": [
            "5.4 mSv",
            "1.4 mSv",
            "0.54 mSv",
            "2.2 mSv",
        ],
        "correct_index": 1,
        "why": "50% of 2.7 mSv is 1.35 mSv, which is 1.4 mSv to two "
               "significant figures.",
    },
    {
        "id": "ks4-background-radiation-h03",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A newspaper claims that most of the background radiation a "
                "person in the UK receives comes from the nuclear power "
                "industry. Evaluate this claim.",
        "options": [
            "It is correct, because power stations release radioactive gases "
            "continuously",
            "It cannot be judged, because background radiation cannot be "
            "traced to its sources",
            "It is correct, because fallout from historical weapons testing "
            "is also counted as nuclear industry",
            "It is wrong — about 85% of UK background radiation is natural, "
            "and the nuclear industry is a small part of the remaining 15%",
        ],
        "correct_index": 3,
        "why": "Natural sources — radon, rocks, cosmic rays and food — supply "
               "roughly 85% of the UK dose; the nuclear industry is a small "
               "fraction of the artificial 15%, most of which is medical.",
    },
    {
        "id": "ks4-background-radiation-h04",
        "subtopic_slug": "background-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A weak source gives a measured count rate of 34 counts per "
                "minute where the background is 28 counts per minute. Suggest "
                "why this measurement is unreliable.",
        "options": [
            "A Geiger counter cannot detect any count rate below 50 counts "
            "per minute",
            "Background radiation must be added to weak sources rather than "
            "subtracted from them",
            "The corrected rate of 6 counts per minute is small compared with "
            "the random variation in the background itself",
            "The source must have decayed completely, so the reading is "
            "entirely background",
        ],
        "correct_index": 2,
        "why": "The source's contribution, 34 − 28 = 6 counts per minute, is "
               "no larger than the random fluctuation in the background, so it "
               "cannot be measured with confidence.",
    },

    # ── uses-of-nuclear-radiation ───────────────────────────────────────
    # TRIPLE ONLY: tier='foundation', triple_only=True
    {
        "id": "ks4-uses-of-nuclear-radiation-e01",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which type of radiation is used in a gauge that "
                "monitors the thickness of aluminium foil as it is rolled.",
        "options": [
            "Alpha, because it is absorbed strongly by any thickness of foil",
            "X-rays, because they are the only radiation that passes through "
            "metal",
            "Gamma, because it passes through the foil without any absorption",
            "Beta, because the amount absorbed changes with the thickness of "
            "the foil",
        ],
        "correct_index": 3,
        "why": "Beta is partly absorbed by a thin sheet, so the transmitted "
               "count changes measurably as the thickness changes — alpha is "
               "stopped completely and gamma barely at all.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e02",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Surgical instruments are sealed in plastic packets and then "
                "sterilised. State which radiation is used and why.",
        "options": [
            "Beta, because it is absorbed by plastic and heats the contents",
            "Gamma, because it penetrates the packaging to kill bacteria "
            "inside",
            "Alpha, because it is the most strongly ionising radiation",
            "Beta, because it has a longer range in air than gamma does",
        ],
        "correct_index": 1,
        "why": "Only gamma penetrates the sealed packaging, so the contents "
               "can be sterilised after they have been wrapped, without heat.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e03",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which type of radiation is directed at a tumour deep "
                "inside the body during radiotherapy.",
        "options": [
            "Alpha, because it does the most damage per centimetre travelled",
            "Beta, because it passes through skin but stops in muscle",
            "Gamma, because it penetrates the body far enough to reach the "
            "tumour",
            "Neutrons, because they carry no charge and are not deflected",
        ],
        "correct_index": 2,
        "why": "Gamma is the only one of the three that penetrates deeply "
               "enough to deliver its energy to a tumour inside the body.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e04",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe what a gamma camera shows a doctor after a tracer "
                "has been given to a patient.",
        "options": [
            "Where the tracer has collected, which shows how an organ is "
            "working",
            "The exact shape of the bones, in the same way as an X-ray "
            "photograph",
            "The temperature of each organ, mapped as a colour image",
            "The rate at which the patient's own tissue is becoming "
            "radioactive",
        ],
        "correct_index": 0,
        "why": "A tracer image shows the distribution of the isotope, which "
               "reveals organ function rather than just structure.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s01",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a paper mill a beta source sits above the moving sheet "
                "and a detector below it. Predict what happens to the "
                "detector reading if the sheet becomes too thick.",
        "options": [
            "It stays the same, because beta passes through paper unaffected",
            "It rises, because thicker paper scatters more beta towards the "
            "detector",
            "It falls, because more beta is absorbed by the extra thickness "
            "of paper",
            "It falls to zero, because paper absorbs beta completely",
        ],
        "correct_index": 2,
        "why": "More material means more beta absorbed, so the transmitted "
               "count drops — and that drop is the signal that tells the "
               "rollers to press harder.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s02",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a gamma source would not work in a gauge "
                "measuring the thickness of paper.",
        "options": [
            "Almost all the gamma would pass through whatever the thickness, "
            "so the reading would hardly change",
            "Gamma would be completely absorbed by the paper, so no reading "
            "would reach the detector",
            "Gamma cannot be detected by a Geiger–Müller tube, unlike beta",
            "Gamma would make the paper radioactive, which would ruin the "
            "product",
        ],
        "correct_index": 0,
        "why": "A gauge needs a radiation the material absorbs measurably; "
               "gamma is too penetrating for thin paper to change the count "
               "usefully.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s03",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the source in an industrial thickness gauge is "
                "chosen to have a half-life of many years.",
        "options": [
            "A long half-life makes the source safer to handle than a short "
            "one",
            "A long half-life means the radiation becomes more penetrating "
            "over time",
            "A long half-life increases the activity, giving a larger count "
            "rate",
            "Its activity stays nearly constant, so the gauge does not need "
            "recalibrating or the source replacing",
        ],
        "correct_index": 3,
        "why": "A gauge compares counts against a fixed calibration, so the "
               "source's activity must not fall noticeably during years of "
               "production.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s04",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An engineer passes a radioactive source along the inside of "
                "a buried water pipe while a detector is moved along the "
                "ground above. Explain why a gamma source is used.",
        "options": [
            "Gamma is the least ionising, so it will not damage the pipe wall",
            "Only gamma penetrates the pipe and the soil to reach the "
            "detector at the surface",
            "Gamma is attracted towards cracks by the flow of water",
            "Gamma has the shortest half-life, so the source will not "
            "contaminate the water supply",
        ],
        "correct_index": 1,
        "why": "Alpha and beta would be absorbed by the pipe wall and the "
               "soil; only gamma penetrates far enough to be detected above "
               "ground.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h01",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Four isotopes are available. P emits alpha, half-life 4 "
                "hours. Q emits gamma, half-life 6 hours. R emits beta, "
                "half-life 20 years. S emits gamma, half-life 30 years. "
                "Determine which is most suitable as a medical tracer.",
        "options": [
            "Q, because gamma escapes the body to reach the camera and the "
            "activity falls quickly afterwards",
            "P, because its very short half-life gives the lowest dose of the "
            "four",
            "R, because beta is less penetrating than gamma and so is safer "
            "inside a patient",
            "S, because gamma is detectable outside the body and the source "
            "will not need replacing",
        ],
        "correct_index": 0,
        "why": "A tracer must emit gamma so it can be detected outside the "
               "body, and have a short half-life so the patient's dose falls "
               "quickly after the scan.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h02",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Using the same four isotopes — P (alpha, 4 hours), Q "
                "(gamma, 6 hours), R (beta, 20 years) and S (gamma, 30 "
                "years) — determine which is most suitable for a gauge "
                "monitoring the thickness of thin steel sheet.",
        "options": [
            "Q, because a short half-life keeps the factory dose low",
            "P, because alpha is the most strongly ionising and gives the "
            "clearest signal",
            "S, because gamma passes through steel and lasts for decades",
            "R, because beta is partly absorbed by thin steel and its long "
            "half-life keeps the reading stable",
        ],
        "correct_index": 3,
        "why": "Thickness monitoring needs a radiation the sheet partly "
               "absorbs — beta — together with a half-life long enough that "
               "the calibration holds for years.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h03",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "During radiotherapy the gamma beam is rotated so that it "
                "enters the body from many different directions, always "
                "aimed at the same tumour. Explain the advantage of doing "
                "this.",
        "options": [
            "Rotating the beam increases the ionising power of the gamma rays",
            "Each direction delivers a different type of radiation, killing "
            "more cell types",
            "The tumour receives a high dose from every beam while each path "
            "of healthy tissue receives only a small share",
            "It allows a much weaker source to be used, which removes the "
            "risk to the patient entirely",
        ],
        "correct_index": 2,
        "why": "Only the tumour lies on every beam path, so its dose adds up "
               "while the surrounding healthy tissue is crossed by one beam at "
               "a time.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h04",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student suggests that a tracer with a half-life of "
                "several years would be better, because the hospital could "
                "keep it in stock and would not have to order it repeatedly. "
                "Evaluate this suggestion.",
        "options": [
            "It is a good suggestion, because a longer half-life means the "
            "image is brighter and clearer",
            "It is a poor suggestion, because the isotope would keep "
            "irradiating the patient long after the scan was finished",
            "It is a good suggestion, because the activity of a tracer does "
            "not affect the patient's dose",
            "It is a poor suggestion, because isotopes with long half-lives "
            "cannot emit gamma radiation",
        ],
        "correct_index": 1,
        "why": "A tracer's activity must fall quickly once the scan is done, "
               "or the patient carries an internal source for years for no "
               "diagnostic gain.",
    },

    # ── nuclear-fission ─────────────────────────────────────────────────
    # TRIPLE ONLY: tier='foundation', triple_only=True
    {
        "id": "ks4-nuclear-fission-e01",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to a nucleus during nuclear fission.",
        "options": [
            "A large unstable nucleus splits into two smaller nuclei",
            "Two small nuclei join together to form a larger nucleus",
            "A nucleus emits an alpha particle and becomes slightly smaller",
            "A neutron in the nucleus changes into a proton and an electron",
        ],
        "correct_index": 0,
        "why": "Fission is the splitting of a large, unstable nucleus into two "
               "smaller ones, together with two or three neutrons and energy.",
    },
    {
        "id": "ks4-nuclear-fission-e02",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a uranium-235 nucleus must do before it undergoes "
                "fission.",
        "options": [
            "Emit a gamma ray to lose its excess energy",
            "Be heated until its electrons are stripped away",
            "Absorb a neutron, which makes it unstable",
            "Collide with another uranium-235 nucleus",
        ],
        "correct_index": 2,
        "why": "Fission is induced: the nucleus first absorbs a neutron, "
               "becoming a highly unstable uranium-236 nucleus, and only then "
               "splits.",
    },
    {
        "id": "ks4-nuclear-fission-e03",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Which pair of nuclides is used as fuel in nuclear fission "
                "reactors?",
        "options": [
            "Deuterium and tritium",
            "Uranium-235 and plutonium-239",
            "Carbon-14 and potassium-40",
            "Cobalt-60 and technetium-99m",
        ],
        "correct_index": 1,
        "why": "Uranium-235 and plutonium-239 are the fissile nuclides — they "
               "split when they absorb a slow neutron.",
    },
    {
        "id": "ks4-nuclear-fission-e04",
        "subtopic_slug": "nuclear-fission",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the function of the moderator in a nuclear reactor.",
        "options": [
            "It absorbs surplus neutrons so that the reaction cannot run away",
            "It transfers thermal energy from the core to the steam generator",
            "It shields the operators from gamma radiation leaving the core",
            "It slows the fast neutrons down so they are more likely to cause "
            "fission",
        ],
        "correct_index": 3,
        "why": "Neutrons released by fission are too fast to be captured "
               "efficiently; the moderator slows them by collisions so they "
               "can be absorbed by uranium-235.",
    },
    {
        "id": "ks4-nuclear-fission-s01",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe the products of a single fission event in "
                "uranium-235.",
        "options": [
            "One smaller nucleus, one alpha particle and energy",
            "Two smaller nuclei, two or three neutrons and energy",
            "Two smaller nuclei and one electron, with no energy released",
            "One larger nucleus, one neutron and a gamma ray only",
        ],
        "correct_index": 1,
        "why": "Each fission gives two fission fragments plus two or three "
               "neutrons, and it is those spare neutrons that allow a chain "
               "reaction.",
    },
    {
        "id": "ks4-nuclear-fission-s02",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a chain reaction is able to continue once the "
                "first fission has taken place.",
        "options": [
            "The gamma rays released trigger fission in neighbouring nuclei",
            "The heat produced raises the temperature until further nuclei "
            "split",
            "Each fission releases more than one neutron, and those neutrons "
            "can cause further fissions",
            "The fission fragments are unstable, so each one splits again in "
            "turn",
        ],
        "correct_index": 2,
        "why": "One fission releases two or three neutrons, so more than one "
               "further fission can follow — that is what makes the reaction "
               "self-sustaining.",
    },
    {
        "id": "ks4-nuclear-fission-s03",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In one fission event a uranium-235 nucleus absorbs a neutron "
                "and splits into barium-141 and krypton-92. Determine how "
                "many neutrons are released.",
        "options": [
            "3",
            "1",
            "2",
            "4",
        ],
        "correct_index": 0,
        "why": "Mass number is conserved: 235 + 1 = 236, and 141 + 92 = 233, "
               "so the remaining 3 mass units are three neutrons.",
    },
    {
        "id": "ks4-nuclear-fission-s04",
        "subtopic_slug": "nuclear-fission",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by the critical mass of a fissile "
                "material.",
        "options": [
            "The mass of fuel that a reactor consumes in one day of operation",
            "The mass above which the fuel becomes too hot to cool safely",
            "The mass of uranium needed to make one fission event occur",
            "The smallest mass that will sustain a chain reaction",
        ],
        "correct_index": 3,
        "why": "Below the critical mass too many neutrons escape from the "
               "surface before being absorbed, so the chain reaction dies out.",
    },
    {
        "id": "ks4-nuclear-fission-h01",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare a controlled chain reaction in a power station with "
                "an uncontrolled one in a nuclear weapon.",
        "options": [
            "The reactor uses fission and the weapon uses fusion, which is "
            "why the weapon releases more energy",
            "The reactor splits uranium-235 and the weapon splits "
            "uranium-238, which cannot be controlled",
            "In the reactor, on average one neutron per fission goes on to "
            "cause another, giving a steady rate; in the weapon the number "
            "grows rapidly with each generation",
            "The reactor produces no neutrons at all, whereas the weapon "
            "produces two or three per fission",
        ],
        "correct_index": 2,
        "why": "Control is about how many of the released neutrons go on to "
               "cause the next fission: exactly one keeps the power steady, "
               "more than one makes it grow.",
    },
    {
        "id": "ks4-nuclear-fission-h02",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a lump of uranium-235 smaller than the critical "
                "mass cannot sustain a chain reaction.",
        "options": [
            "Too many neutrons escape from the surface before they are "
            "absorbed by another nucleus",
            "A small lump does not contain any uranium-235, only uranium-238",
            "A small lump cannot reach the temperature at which fission "
            "begins",
            "Fission does not occur at all below the critical mass, so no "
            "neutrons are ever produced",
        ],
        "correct_index": 0,
        "why": "In a small piece the surface is large compared with the "
               "volume, so neutrons leave before finding a nucleus and each "
               "fission fails to trigger a successor.",
    },
    {
        "id": "ks4-nuclear-fission-h03",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'The moderator absorbs neutrons, so "
                "pushing more moderator into the core slows the reaction "
                "down.' Explain the error.",
        "options": [
            "The moderator does absorb neutrons, but it is fixed in place and "
            "cannot be moved",
            "There is no error, as moderator and control rods do the same job "
            "by different means",
            "The moderator releases neutrons rather than absorbing them, so "
            "more moderator speeds the reaction up",
            "The moderator slows neutrons down rather than absorbing them; it "
            "is the control rods that absorb neutrons",
        ],
        "correct_index": 3,
        "why": "Moderator and control rods have opposite effects: slowing "
               "neutrons makes fission more likely, while absorbing them in "
               "boron or cadmium rods makes it less likely.",
    },
    {
        "id": "ks4-nuclear-fission-h04",
        "subtopic_slug": "nuclear-fission",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that nuclear fission is a good way to "
                "generate electricity with a low carbon footprint.",
        "options": [
            "The claim fails entirely, because a reactor releases as much "
            "carbon dioxide as a gas-fired power station",
            "The claim holds for carbon dioxide during operation, but must be "
            "weighed against waste that stays radioactive for thousands of "
            "years and high build and decommissioning costs",
            "The claim holds completely, because fission produces no waste of "
            "any kind",
            "The claim cannot be judged, because the fuel is too energy-dense "
            "to compare with other sources",
        ],
        "correct_index": 1,
        "why": "Fission genuinely emits almost no carbon dioxide while "
               "running, but a fair evaluation also weighs long-lived "
               "radioactive waste, cost and accident risk.",
    },

    # ── nuclear-fusion ──────────────────────────────────────────────────
    # TRIPLE ONLY: tier='foundation', triple_only=True
    {
        "id": "ks4-nuclear-fusion-e01",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by nuclear fusion.",
        "options": [
            "A large nucleus splitting into two smaller nuclei",
            "A nucleus absorbing a neutron and becoming unstable",
            "Two small nuclei joining to form a larger nucleus",
            "A nucleus emitting a beta particle and changing element",
        ],
        "correct_index": 2,
        "why": "Fusion is the joining of two small nuclei into one larger "
               "nucleus, releasing energy — the opposite process to fission.",
    },
    {
        "id": "ks4-nuclear-fusion-e02",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the process that releases the Sun's energy.",
        "options": [
            "The fission of uranium in the Sun's core",
            "The burning of hydrogen gas in oxygen",
            "The radioactive decay of heavy elements",
            "The fusion of hydrogen nuclei to form helium",
        ],
        "correct_index": 3,
        "why": "In the Sun's core hydrogen nuclei fuse to form helium-4, and "
               "the small loss of mass appears as the energy the Sun radiates.",
    },
    {
        "id": "ks4-nuclear-fusion-e03",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Deuterium and tritium fuse together in an experimental "
                "reactor. State the products of this reaction.",
        "options": [
            "A helium-4 nucleus and a neutron",
            "Two helium-3 nuclei and an electron",
            "A hydrogen nucleus and an alpha particle",
            "A helium-4 nucleus and a gamma ray only",
        ],
        "correct_index": 0,
        "why": "²H + ³H → ⁴He + n: the mass numbers 2 + 3 = 5 balance as 4 + "
               "1, so a helium-4 nucleus and one neutron are produced.",
    },
    {
        "id": "ks4-nuclear-fusion-e04",
        "subtopic_slug": "nuclear-fusion",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the name given to the state of matter that the fuel is "
                "in inside a fusion reactor.",
        "options": [
            "A supercooled liquid",
            "A plasma",
            "A saturated vapour",
            "A crystalline solid",
        ],
        "correct_index": 1,
        "why": "At around 100 million °C the atoms are completely ionised, "
               "giving a plasma of free nuclei and electrons.",
    },
    {
        "id": "ks4-nuclear-fusion-s01",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the plasma in a fusion reactor is held in place "
                "by strong magnetic fields rather than by a container wall.",
        "options": [
            "No material could stay solid in contact with plasma at around "
            "100 million °C",
            "A metal wall would react chemically with the hydrogen fuel and "
            "explode",
            "Magnetic fields raise the plasma's temperature, which a wall "
            "cannot do",
            "Plasma has no mass, so it cannot be held by anything except a "
            "field",
        ],
        "correct_index": 0,
        "why": "At fusion temperatures any solid wall would melt or vaporise "
               "on contact, so the charged plasma is steered away from the "
               "walls by magnetic fields instead.",
    },
    {
        "id": "ks4-nuclear-fusion-s02",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State where the deuterium used as fusion fuel is obtained "
                "from.",
        "options": [
            "It is manufactured inside fission reactors as a waste product",
            "It is extracted from sea water, in which it occurs naturally",
            "It is mined from uranium-bearing rocks such as granite",
            "It is separated from the carbon dioxide in the atmosphere",
        ],
        "correct_index": 1,
        "why": "Deuterium is a naturally occurring isotope of hydrogen in "
               "water, so the oceans hold an effectively unlimited supply.",
    },
    {
        "id": "ks4-nuclear-fusion-s03",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why fusion happens in the Sun without any magnetic "
                "confinement.",
        "options": [
            "The Sun's core is much cooler, so the nuclei do not need "
            "confining",
            "The Sun is made of plasma, and plasma confines itself once it is "
            "hot enough",
            "The Sun's own magnetic field is strong enough to act as a "
            "container",
            "The Sun's enormous mass produces gravitational forces that hold "
            "the core together at very high pressure",
        ],
        "correct_index": 3,
        "why": "Gravity does the confining in a star: the weight of the "
               "overlying material keeps the core at the pressure and "
               "temperature fusion needs.",
    },
    {
        "id": "ks4-nuclear-fusion-s04",
        "subtopic_slug": "nuclear-fusion",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "The helium-4 nucleus formed when deuterium and tritium fuse "
                "has slightly less mass than the two nuclei that made it, "
                "even after the neutron is counted. Explain what has become "
                "of the missing mass.",
        "options": [
            "It has been converted into energy, in line with E = mc²",
            "It has been carried away as electrons stripped from the fuel "
            "atoms",
            "It remains in the plasma as unfused fuel that was not measured",
            "It has been lost as heat conducted into the reactor walls",
        ],
        "correct_index": 0,
        "why": "The mass difference is converted into energy through E = mc², "
               "which is why so little fuel releases so much energy.",
    },
    {
        "id": "ks4-nuclear-fusion-h01",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare nuclear fission and nuclear fusion. Which statement "
                "is correct?",
        "options": [
            "Both split large nuclei, but fusion needs a much higher "
            "temperature to start",
            "Fission joins small nuclei and fusion splits large ones, and "
            "only fission releases energy",
            "Fission needs a neutron to start it while fusion needs no energy "
            "input at all",
            "Fission splits a large nucleus and fusion joins small nuclei, "
            "and both release energy from a loss of mass",
        ],
        "correct_index": 3,
        "why": "The two processes are opposites in what happens to the "
               "nuclei, but identical in where the energy comes from — a mass "
               "defect converted by E = mc².",
    },
    {
        "id": "ks4-nuclear-fusion-h02",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Fusion has been demonstrated in laboratories for decades, "
                "yet no fusion power station supplies electricity. Explain "
                "the main reason.",
        "options": [
            "There is not enough deuterium on Earth to fuel a power station",
            "Keeping the plasma hot and confined has so far taken more energy "
            "than the fusion reactions give out",
            "Fusion produces waste that is more radioactive than fission "
            "waste, so it has been banned",
            "The neutrons produced by fusion cannot be used to heat water for "
            "a turbine",
        ],
        "correct_index": 1,
        "why": "The engineering barrier is net energy gain: reaching and "
               "holding 100 million °C currently costs more energy than the "
               "fusion releases.",
    },
    {
        "id": "ks4-nuclear-fusion-h03",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fusion reactor cannot suffer a runaway "
                "reaction in the way a fission reactor can.",
        "options": [
            "Fusion reactors hold only a few atoms of fuel, so nothing could "
            "escape",
            "Fusion releases no neutrons, so there is nothing to trigger "
            "further reactions",
            "If the extreme temperature or confinement is lost the reaction "
            "simply stops, because the conditions it needs disappear",
            "Fusion reactions can only occur one at a time, so the rate can "
            "never build up",
        ],
        "correct_index": 2,
        "why": "Fusion has to be actively maintained: lose the temperature or "
               "the confinement and the reaction ends by itself, so it is "
               "inherently safe.",
    },
    {
        "id": "ks4-nuclear-fusion-h04",
        "subtopic_slug": "nuclear-fusion",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "One deuterium–tritium fusion releases about 17.6 MeV, while "
                "one uranium-235 fission releases about 200 MeV. A student "
                "concludes that fusion must therefore be a poorer source of "
                "energy. Evaluate this conclusion.",
        "options": [
            "It is sound, because the energy released per reaction is the "
            "only fair comparison",
            "It is unsound, because the fission figure includes the energy of "
            "the neutron and the fusion figure does not",
            "It is unsound, because fusion releases far more energy per unit "
            "mass of fuel — 5 nucleons share 17.6 MeV against 236 sharing 200 "
            "MeV — and the fuel is far more abundant",
            "It is sound, because a fusion reactor would need forty times as "
            "much fuel as a fission reactor of the same output",
        ],
        "correct_index": 2,
        "why": "Per nucleon, fusion gives about 3.5 MeV against fission's 0.85 "
               "MeV, so the same mass of fuel yields several times more "
               "energy.",
    },
]
