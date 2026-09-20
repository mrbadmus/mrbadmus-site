"""Physics · Atomic structure — the MRB-338 expansion of `uses-of-nuclear-radiation`.

One leaf only: AQA 8463 §6.4.4, physics only — matching alpha, beta and gamma
to a job by their ionising power, their range and the half-life the job needs.

⚠️ The original twelve rows in `atomic_structure__b.py` cover the beta
thickness gauge (four times over), gamma sterilisation, gamma radiotherapy, the
gamma camera, the long-lived industrial source and the buried pipe — and leave
TWO of the specification's named uses completely untouched: the alpha SMOKE
DETECTOR and CARBON DATING. That is where the weight of this file falls, with
the named isotopes the existing rows never mention (americium-241,
technetium-99m, iodine-123, cobalt-60, carbon-14) supplying the recall band.
No row here re-asks a thickness gauge or a rotating radiotherapy beam.

⚠️ Carbon-14's half-life is NOT stated in any stem in this file. The
`half-lives` leaf keys a row on "5730 years", and a stem quoting it would hand
that answer to a pupil who met both in one assignment (brief §9.6) — so the
dating arithmetic here is asked in half-lives rather than in years.

This is a physics-only Triple subtopic, so every row carries
`triple_only=True` at `foundation` tier. Working lives in `why`, never in an
option.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # The smoke detector, the named isotopes, and what a tracer is for.
    {
        "id": "ks4-uses-of-nuclear-radiation-e05",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which type of radiation is used inside a household "
                "smoke detector.",
        "options": [
            "Alpha, because it ionises the air strongly over a very short "
            "distance",
            "Gamma, because it spreads through the whole room to find the "
            "smoke wherever it starts",
            "Beta, because it is absorbed by smoke but not by clean air",
            "X-rays, because they are produced electrically and need no "
            "source",
        ],
        "correct_index": 0,
        "why": "Alpha ionises air very effectively, and its range of a few "
               "centimetres keeps the radiation inside the detector casing.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e06",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the isotope used as the radioactive source in a smoke "
                "detector.",
        "options": [
            "Cobalt-60",
            "Americium-241",
            "Technetium-99m",
            "Strontium-90",
        ],
        "correct_index": 1,
        "why": "Americium-241 is an alpha emitter with a half-life of "
               "hundreds of years, so one tiny source lasts the life of the "
               "detector.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e07",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why the radioactive source in a smoke detector is not a "
                "hazard to a family living in the house.",
        "options": [
            "Its activity is so low that it emits fewer than ten particles "
            "each day",
            "It is switched off whenever the detector is not sensing smoke",
            "Alpha particles travel only a few centimetres, so none of them "
            "leave the casing",
            "The plastic casing converts the alpha particles into visible "
            "light",
        ],
        "correct_index": 2,
        "why": "Alpha is stopped by a few centimetres of air and by any solid "
               "barrier, so the radiation never reaches anyone outside the "
               "unit.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e08",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to the current inside a smoke detector "
                "when smoke enters it.",
        "options": [
            "It rises, because smoke particles carry charge across the gap",
            "It falls, because less of the air between the electrodes is "
            "ionised",
            "It reverses, because the smoke changes which electrode is "
            "positive and which is negative",
            "It stays the same, but an optical sensor detects the smoke "
            "instead",
        ],
        "correct_index": 1,
        "why": "Smoke absorbs the alpha particles, so fewer ions are made, "
               "the current drops and the circuit sounds the alarm.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e09",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the isotope most widely used as a medical tracer.",
        "options": [
            "Americium-241",
            "Uranium-235",
            "Technetium-99m",
            "Carbon-14",
        ],
        "correct_index": 2,
        "why": "Technetium-99m emits gamma, which escapes the body to reach a "
               "camera, and its half-life of a few hours keeps the patient's "
               "dose low.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e10",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one use of gamma radiation in the food industry.",
        "options": [
            "Adding flavour to food by exciting the atoms inside it until they "
            "glow faintly",
            "Killing bacteria on food so that it keeps for longer",
            "Warming food through without using an oven or a hob",
            "Making food heavier so that a portion goes further",
        ],
        "correct_index": 1,
        "why": "Gamma penetrates the packaging and kills the microorganisms "
               "that would spoil the food, which extends its shelf life "
               "without any heating.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e11",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the gland investigated using a tracer containing "
                "iodine-123.",
        "options": [
            "The pancreas",
            "The pituitary gland",
            "The thyroid gland",
            "The adrenal gland",
        ],
        "correct_index": 2,
        "why": "The thyroid takes up iodine from the blood, so a radioactive "
               "iodine tracer collects there and shows whether the gland is "
               "working normally.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e12",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the isotope whose decay is used to find the age of "
                "once-living material.",
        "options": [
            "Carbon-14",
            "Potassium-40",
            "Cobalt-60",
            "Radon-222",
        ],
        "correct_index": 0,
        "why": "Living things take in carbon-14 while they are alive, and it "
               "decays steadily once they die, so the amount left indicates "
               "the age.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e13",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State which of the three types of nuclear radiation ionises "
                "the air most strongly.",
        "options": [
            "Gamma, because it carries the most energy of the three for the "
            "same distance travelled",
            "Beta, because it moves fastest through the air",
            "Alpha, because of its large charge and large mass",
            "They ionise air equally, but over different distances",
        ],
        "correct_index": 2,
        "why": "An alpha particle carries a charge of +2 and is thousands of "
               "times more massive than a beta particle, so it strips "
               "electrons from far more atoms per centimetre travelled.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e14",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one advantage of sterilising equipment with gamma "
                "radiation rather than with steam.",
        "options": [
            "Gamma radiation costs less to produce than hot steam does",
            "No heating is needed, so items damaged by high temperatures can "
            "be treated",
            "Gamma radiation leaves a coating that stops bacteria returning",
            "Gamma radiation works in a few seconds, while steam takes several "
            "days to complete a cycle",
        ],
        "correct_index": 1,
        "why": "Gamma sterilisation is a cold process, so plastic syringes "
               "and other heat-sensitive items survive it unchanged.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e15",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the isotope commonly used as the gamma source in "
                "radiotherapy machines.",
        "options": [
            "Iodine-123",
            "Americium-241",
            "Cobalt-60",
            "Plutonium-239",
        ],
        "correct_index": 2,
        "why": "Cobalt-60 is a strong gamma emitter with a half-life of a few "
               "years, which suits a machine in continuous hospital use.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e16",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the amount of carbon-14 in an old wooden beam is "
                "compared with in order to find its age.",
        "options": [
            "The amount in living wood of the same kind",
            "The amount in the soil the tree grew in",
            "The amount in a sample of coal from the same region of the "
            "country",
            "The amount of carbon dioxide in the air today",
        ],
        "correct_index": 0,
        "why": "Living material holds a known proportion of carbon-14, so the "
               "shortfall in the old beam shows how long it has been "
               "decaying.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e17",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by a medical tracer.",
        "options": [
            "A dye injected into a patient to make an X-ray image clearer",
            "A radioactive substance given to a patient so its movement "
            "through the body can be followed",
            "A device worn by a patient to record the dose received during "
            "treatment and for some weeks afterwards",
            "A metal marker placed on the skin so a beam can be aimed "
            "accurately",
        ],
        "correct_index": 1,
        "why": "A tracer is a radioactive substance whose radiation can be "
               "detected outside the body, revealing where it has travelled "
               "and collected.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-e18",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why a tracer with a half-life of a few seconds would be "
                "unsuitable for a medical scan.",
        "options": [
            "A very short half-life makes the radiation too penetrating to "
            "detect outside the body",
            "Its activity would fall away before it reached the organ and "
            "could be imaged",
            "It would emit alpha particles instead of gamma rays",
            "It would leave the patient contaminated for several years "
            "afterwards",
        ],
        "correct_index": 1,
        "why": "A tracer needs time to be injected, carried in the blood and "
               "imaged, so a half-life of seconds leaves nothing to detect.",
    },

    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # The smoke detector mechanism, the dating method and its limits, and the
    # reasons behind the choices.
    {
        "id": "ks4-uses-of-nuclear-radiation-s05",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how smoke entering a detector causes the alarm to "
                "sound.",
        "options": [
            "Smoke reflects the alpha particles back onto the source, which "
            "then heats up and trips a switch",
            "Smoke makes the air conduct better, so a larger current flows "
            "and the alarm is triggered",
            "Smoke absorbs the alpha particles, so fewer ions are made, the "
            "current falls and the alarm is triggered",
            "Smoke blocks a beam of light between two electrodes, and the "
            "loss of light sounds the alarm",
        ],
        "correct_index": 2,
        "why": "The ionised air between the electrodes normally carries a "
               "small steady current; smoke stops the alpha particles that "
               "produce those ions, and the circuit responds to the drop.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s06",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a current can flow across the air gap inside a "
                "smoke detector even though air is normally an insulator.",
        "options": [
            "The alpha source ionises the air, and the ions and electrons "
            "produced are free to carry charge across the gap",
            "The two electrodes are close enough for electrons to jump "
            "directly between them without any air in the way between them",
            "The alpha particles themselves are the current, travelling from "
            "one electrode to the other and back again many times each second",
            "Warm air from the room conducts electricity, unlike the cold air "
            "outside",
        ],
        "correct_index": 0,
        "why": "Ionisation creates charged particles in the air, and it is "
               "their movement between the electrodes that forms the small "
               "current the circuit watches.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s07",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Americium-241 has a half-life of about 430 years. Explain why "
                "this is an advantage in a smoke detector.",
        "options": [
            "A long half-life makes each alpha particle more strongly ionising "
            "than a short one would, so the current is larger",
            "The source can be made far smaller than a short-lived one, so it "
            "fits inside a ceiling unit",
            "The activity stays almost unchanged, so the detector keeps "
            "working for decades without the source being replaced",
            "A long half-life means the source emits gamma as well as alpha, "
            "which makes the alarm more reliable in a smoky room where the "
            "smoke is thickest",
        ],
        "correct_index": 2,
        "why": "Over the twenty-year life of a detector a 430-year half-life "
               "barely changes the activity, so the current stays at its "
               "designed level.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s08",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a gamma source would not work in place of the "
                "alpha source in a smoke detector.",
        "options": [
            "Gamma rays would pass through the smoke almost unaffected, so "
            "the current would hardly change",
            "Gamma rays would be absorbed by the smoke completely, so the "
            "alarm would sound continuously from the moment it was fitted",
            "Gamma rays are unable to ionise air, so no current would flow in "
            "the first place",
            "Gamma sources are all far too weak to produce a measurable "
            "current",
        ],
        "correct_index": 0,
        "why": "The detector works by a change in absorption, and smoke "
               "absorbs almost no gamma — so there would be nothing for the "
               "circuit to notice.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s09",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a tracer must emit gamma radiation rather than "
                "alpha.",
        "options": [
            "Alpha radiation would be absorbed within the body, so nothing "
            "would reach a detector outside it",
            "Alpha radiation cannot be detected by any instrument a hospital "
            "possesses",
            "Alpha radiation would not be carried in the bloodstream, because "
            "of its positive charge",
            "Alpha radiation decays too quickly to survive the journey to the "
            "organ",
        ],
        "correct_index": 0,
        "why": "A tracer has to be seen from outside, and only gamma "
               "penetrates tissue well enough to leave the body and reach the "
               "camera.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s10",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how technetium-99m's half-life of a few hours keeps a "
                "patient's dose low.",
        "options": [
            "A short half-life means the radiation emitted is less penetrating "
            "and so less harmful, so the patient absorbs less of it",
            "The activity inside the patient falls away quickly once the scan "
            "is finished",
            "The isotope leaves the body faster than one with a long "
            "half-life would",
            "A short half-life means fewer nuclei decay in total, whatever "
            "happens afterwards",
        ],
        "correct_index": 1,
        "why": "Dose builds up for as long as the source is active inside the "
               "patient, and a six-hour half-life has halved the activity "
               "four times by the end of the day.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s11",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how the age of a wooden bowl is estimated from its "
                "carbon-14 content.",
        "options": [
            "The total mass of carbon is measured and compared with the mass "
            "of a new bowl of the same design and timber",
            "The bowl's activity is measured, and every count recorded "
            "represents one year of age, counted over a fixed period of one "
            "minute",
            "The bowl is weighed each year until a measurable change in mass "
            "is detected, since decaying carbon-14 takes mass away from the "
            "object",
            "The proportion of carbon-14 left is measured, and the number of "
            "half-lives that have passed gives the age",
        ],
        "correct_index": 3,
        "why": "The carbon-14 fraction falls by half each half-life, so "
               "measuring what remains tells you how many half-lives have "
               "elapsed since the tree died.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s12",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why carbon dating cannot be used on a stone axe head.",
        "options": [
            "Stone is too dense for the radiation from carbon-14 to escape "
            "and be measured",
            "Stone was never living, so it never took in any carbon-14 to "
            "start with",
            "Stone axe heads are too old, so all the carbon-14 in them has "
            "already decayed",
            "Stone contains carbon-12 but no carbon-14, because the two are "
            "different elements, with different numbers of protons",
        ],
        "correct_index": 1,
        "why": "The method relies on a living thing taking carbon-14 in from "
               "the air; a rock never did, so there is no clock to read.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s13",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why carbon dating gives an unhelpful answer for a "
                "wooden chair made about fifty years ago.",
        "options": [
            "Fifty years is far too long, so almost no carbon-14 would be left "
            "to measure in a sample small enough to test in a laboratory",
            "Carbon-14 only begins to decay once an object is a century old, "
            "so the clock has not yet started running on this wooden chair",
            "Fifty years is a tiny fraction of the half-life, so the "
            "carbon-14 has barely changed and the age cannot be pinned down",
            "The chair would have absorbed fresh carbon-14 from the air "
            "throughout those fifty years, keeping its ratio at the living "
            "value right up to the present day",
        ],
        "correct_index": 2,
        "why": "A dating method only works over times comparable with its "
               "half-life; over fifty years the change in carbon-14 is too "
               "small to measure reliably.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s14",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the cobalt-60 source in a sterilisation plant is "
                "kept inside a thick concrete cell.",
        "options": [
            "Concrete keeps the source at a steady temperature, which holds "
            "its activity constant",
            "Concrete stops radioactive atoms escaping into the factory air",
            "Concrete reflects the gamma rays back onto the products, which "
            "sterilises them faster than a single pass would",
            "Concrete is dense enough to absorb the gamma rays, protecting "
            "the workers outside",
        ],
        "correct_index": 3,
        "why": "A sterilisation source is intensely radioactive and emits "
               "penetrating gamma, so the workers are protected by metres of "
               "dense shielding.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s15",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a tracer is injected into a patient rather than "
                "held against the skin above the organ.",
        "options": [
            "A source held outside would irradiate the skin, but only a "
            "source carried in the blood collects in the organ being studied",
            "A source held outside the body cannot emit gamma radiation "
            "through skin",
            "Injecting the tracer allows a much weaker source to be used, "
            "which removes all risk to the patient and to the hospital staff "
            "alike",
            "A source held against the skin would contaminate the patient, "
            "whereas an injection does not, which is why tracers are given by "
            "needle rather than by hand",
        ],
        "correct_index": 0,
        "why": "The whole point of a tracer is that the body distributes it: "
               "a scan shows where it has gone, which is what reveals how the "
               "organ is functioning.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s16",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why alpha radiation is unsuitable for finding a leak "
                "in a buried pipe.",
        "options": [
            "Alpha is absorbed by a few centimetres of air, so none of it "
            "would reach a detector at the surface",
            "Alpha carries no charge, so it cannot be detected by a Geiger "
            "counter",
            "Alpha is too penetrating, so it would be detected everywhere "
            "along the pipe equally",
            "Alpha would dissolve in the water and be carried away from the "
            "leak",
        ],
        "correct_index": 0,
        "why": "The detector is above ground, so the radiation has to cross "
               "the pipe wall and the soil — a journey alpha cannot make.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s17",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why radiotherapy damages some healthy tissue as well "
                "as the tumour.",
        "options": [
            "Healthy cells absorb gamma radiation more readily than cancer "
            "cells do",
            "The gamma beam has to pass through healthy tissue to reach a "
            "tumour inside the body",
            "The gamma source is placed inside the tumour, so it contaminates "
            "the tissue around it",
            "Gamma radiation spreads sideways once it enters the body and "
            "misses the tumour entirely on its way past",
        ],
        "correct_index": 1,
        "why": "Gamma cannot be switched on only at the tumour, so every "
               "beam ionises the tissue it crosses on the way in and out.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s18",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "An engineer adds a radioactive substance to the water in a "
                "pipe for one afternoon's leak survey. Explain why an isotope "
                "with a half-life of hours is chosen rather than one of years.",
        "options": [
            "A short half-life makes the radiation more penetrating, so the "
            "leak is easier to find from the surface of the ground above",
            "A short half-life means the water supply is not left "
            "radioactive once the survey is over",
            "A short half-life gives a lower activity, which makes the "
            "detector more sensitive to a small leak",
            "A long half-life would make the substance dissolve too slowly "
            "in the water",
        ],
        "correct_index": 1,
        "why": "A one-off survey needs the activity to disappear soon "
               "afterwards; only a permanently installed gauge wants a source "
               "that lasts for years.",
    },

    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # Choosing between four candidate sources, judging a proposal, and the
    # arrangements behind two industrial measurements.
    {
        "id": "ks4-uses-of-nuclear-radiation-h05",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Four sources are offered: W (alpha, 430 years), X (beta, 5 "
                "years), Y (gamma, 6 hours) and Z (alpha, 3 hours). Determine "
                "which is most suitable for a domestic smoke detector.",
        "options": [
            "W, because alpha ionises the air strongly and its activity "
            "lasts for the life of the unit",
            "Z, because alpha is correct and a short half-life keeps the "
            "household dose low year after year for the whole life of the unit",
            "X, because beta is absorbed by smoke and lasts long enough for a "
            "detector",
            "Y, because gamma reaches every corner of the room and is "
            "replaced twice a day",
        ],
        "correct_index": 0,
        "why": "A smoke detector needs alpha for the ionisation and a "
               "half-life of centuries so the current does not drift; Z "
               "would be useless within a day.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h06",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A factory will sterilise sealed packets every day for the "
                "next twenty years. It may buy J (gamma, 30 years), K (alpha, "
                "400 years), L (beta, 12 hours) or M (gamma, 8 hours). "
                "Determine the best purchase.",
        "options": [
            "K, because alpha is the most strongly ionising and so kills "
            "bacteria faster than anything else could on the packet surface",
            "J, because gamma passes through the packets and its activity "
            "holds up over the twenty years",
            "M, because gamma is correct and a short half-life keeps the "
            "factory safer between production runs",
            "L, because beta penetrates packaging easily and is the cheapest "
            "of the four to buy and replace",
        ],
        "correct_index": 1,
        "why": "Sterilising a sealed packet needs gamma, and a plant running "
               "for twenty years needs a half-life measured in decades — only "
               "J has both.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h07",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student proposes replacing the alpha source in a smoke "
                "detector with a gamma source so that it can sense smoke "
                "anywhere in the room. Evaluate the proposal.",
        "options": [
            "It is a good idea, because gamma reaches further and so covers a "
            "larger area of the room than an alpha source ever could from the "
            "same ceiling unit",
            "It is a poor idea, because gamma would escape the casing and "
            "smoke would barely absorb it anyway",
            "It is a good idea, provided the casing is lined with a thin "
            "layer of aluminium",
            "It is a poor idea, because gamma radiation cannot be produced by "
            "any isotope small enough to fit inside a ceiling unit",
        ],
        "correct_index": 1,
        "why": "The proposal fails twice over: it would put a penetrating "
               "source in every home, and the detector's mechanism depends on "
               "smoke absorbing the radiation, which gamma is not.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h08",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wooden sample holds 12.5% of the carbon-14 found in living "
                "wood of the same species. Determine how many half-lives have "
                "passed since the tree died.",
        "options": [
            "3",
            "12",
            "4",
            "6",
        ],
        "correct_index": 0,
        "why": "12.5% is one part in eight, and each half-life leaves half as "
               "much — 50%, then 25%, then 12.5% — so three have passed.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h09",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An archaeologist dating a bone and a hospital preparing a "
                "scan both have to choose an isotope. Determine what governs "
                "the choice of half-life in each case.",
        "options": [
            "Both need the shortest half-life available, so that no "
            "radioactive material is left behind once the measurement has been "
            "made",
            "Both need the longest half-life available, so that the source "
            "does not have to be replaced",
            "The archaeologist needs a half-life comparable with the age "
            "being measured; the hospital needs one comparable with the scan",
            "Neither choice depends on half-life, since both are decided "
            "purely by the type of radiation emitted by the source that has "
            "been selected",
        ],
        "correct_index": 2,
        "why": "A half-life is a clock, and it has to be matched to the "
               "timescale of the job: thousands of years for dating, hours "
               "for a scan.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h10",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that gamma sterilisation should replace "
                "heat sterilisation everywhere in a hospital.",
        "options": [
            "The claim holds, because gamma sterilises anything that heat can, "
            "and does it without raising the temperature, whatever the item is "
            "made of",
            "The claim holds, because heat sterilisation leaves bacteria alive "
            "inside sealed packaging, because the packaging keeps the steam "
            "away from them",
            "The claim fails, because gamma radiation cannot kill bacteria "
            "that are inside a sealed packet, since the plastic wrapping "
            "absorbs it completely",
            "The claim fails, because gamma needs a large shielded source and "
            "a licensed facility, so heat remains practical for everyday use",
        ],
        "correct_index": 3,
        "why": "Gamma's advantages are real for pre-packed and heat-sensitive "
               "items, but an autoclave is cheap and local while a cobalt-60 "
               "cell is neither.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h11",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A company checks the fill level of sealed cans of paint on a "
                "production line. Determine the arrangement that will work.",
        "options": [
            "An alpha source and detector on opposite sides of the can, "
            "counting high where the can is full",
            "A gamma source and detector on the same side of the can, counting "
            "the radiation that bounces back off the paint and returns to it",
            "A gamma source and detector on opposite sides of the can, "
            "counting low where the paint absorbs the beam",
            "A beta source above the can and a detector below it, counting "
            "through the steel base and the paint",
        ],
        "correct_index": 2,
        "why": "Only gamma crosses a steel can, and it is absorbed more by "
               "paint than by the air above it — so a low count marks a full "
               "can and a high count an underfilled one.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h12",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare what a gamma tracer scan and an X-ray photograph tell "
                "a doctor about a kidney that may be failing.",
        "options": [
            "The X-ray shows how well the kidney is working, while the tracer "
            "shows only its outline",
            "The tracer shows how well the kidney is working, while the X-ray "
            "shows mainly its shape and position",
            "Both show function equally well, but the tracer delivers a "
            "smaller dose to the patient",
            "Neither shows function, because a kidney is too deep inside the "
            "body for either method",
        ],
        "correct_index": 1,
        "why": "A tracer is carried by the body, so the image maps activity "
               "over time — function; an X-ray is a shadow picture, so it "
               "maps structure.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h13",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a smoke detector is designed to sound when the "
                "current falls rather than when it rises.",
        "options": [
            "A falling current is easier for a circuit to detect than a "
            "rising one",
            "Smoke particles absorb the alpha radiation, so the number of "
            "ions carrying the current goes down",
            "Smoke particles are charged, so they cancel out part of the "
            "current already flowing across the gap",
            "The battery voltage drops in a fire, which reduces the current "
            "through the gap between the electrodes inside the unit",
        ],
        "correct_index": 1,
        "why": "The alarm is triggered by the loss of ionisation: smoke stops "
               "alpha particles reaching the air gap, so fewer ions are made "
               "and less charge flows.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h14",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that smoke detectors containing "
                "radioactive sources should be banned from homes.",
        "options": [
            "The claim is justified, because any radioactive source in a home "
            "raises the occupants' dose measurably within a year of "
            "installation",
            "The claim is justified, because the alpha source becomes a gamma "
            "source as it ages",
            "The claim is weak, because the alpha cannot leave the casing "
            "while the detector saves lives in a fire",
            "The claim is weak, because the source inside a detector is no "
            "longer radioactive once it has been sealed",
        ],
        "correct_index": 2,
        "why": "This is a benefit-against-risk judgement: the sealed alpha "
               "source delivers essentially no dose to the household, against "
               "a large and well-evidenced benefit.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h15",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "The source in an industrial gauge is replaced with one of the "
                "same type but half the activity. Determine what must be done "
                "before the gauge is used again.",
        "options": [
            "The gauge must be recalibrated, because every count rate it "
            "reads will now be about half what it was",
            "Nothing, because the gauge compares the count with the background "
            "rather than with a fixed value stored in its memory",
            "The detector must be moved twice as close, so the count rate "
            "returns to its old value, which restores the calibration "
            "automatically",
            "The source must be replaced again, because a gauge cannot work at "
            "a reduced activity, however carefully it has been installed",
        ],
        "correct_index": 0,
        "why": "A gauge converts a count rate into a thickness using a fixed "
               "calibration, so halving the source's activity makes every "
               "stored reading wrong until the calibration is redone.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h16",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the same isotope, cobalt-60, can be used both to "
                "treat a tumour and to sterilise equipment, yet is handled "
                "very differently in each case.",
        "options": [
            "Different batches of cobalt-60 emit different types of radiation "
            "depending on how they were made, which is why hospitals and "
            "factories order separately",
            "The treatment source is sealed and the sterilisation source is "
            "not, which changes every precaution, so the hospital source needs "
            "no shielding around it",
            "Cobalt-60 emits gamma in both, but treatment uses a narrow beam "
            "aimed at a patient while sterilisation floods a shielded cell",
            "Cobalt-60 behaves as a beta emitter in a hospital and as a gamma "
            "emitter in a factory, depending on the strength of the magnetic "
            "field applied",
        ],
        "correct_index": 2,
        "why": "The physics is identical; what differs is the dose, the "
               "collimation and who is in the room, so a hospital shapes the "
               "beam while a factory excludes people altogether.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h17",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student says that because gamma is the most penetrating "
                "radiation it must be the most useful for every job. Explain "
                "the error.",
        "options": [
            "Gamma is in fact the least penetrating of the three, so the "
            "statement has the order backwards, with alpha travelling furthest",
            "Gamma is useless outside medicine, because its radiation is too "
            "weak for industrial work, where only X-ray machines are powerful "
            "enough",
            "Gamma is the most penetrating, but a job may need radiation the "
            "material absorbs, and gamma passes through almost unchanged",
            "Gamma is the most penetrating, but it cannot be detected by any "
            "instrument outside a hospital, so its use is confined to "
            "hospitals and research sites",
        ],
        "correct_index": 2,
        "why": "Usefulness comes from matching absorption to the task: a "
               "thickness gauge and a smoke detector both depend on the "
               "radiation being stopped, which is exactly what gamma will not "
               "do.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h18",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A patient's scan shows that a tracer has collected in one "
                "kidney but hardly at all in the other. Suggest what a doctor "
                "would conclude.",
        "options": [
            "The second kidney is not working properly, because it is not "
            "taking up the tracer as it should",
            "The second kidney has absorbed all the radiation, which is why "
            "the camera sees nothing from it on that side",
            "The tracer's half-life expired before it reached the second "
            "kidney",
            "The camera was aimed at one side only, so the result says nothing "
            "about either kidney in this particular patient on the day of the "
            "scan",
        ],
        "correct_index": 0,
        "why": "A tracer image maps function, so an organ that takes up "
               "little of it is an organ that is not doing its normal job.",
    },

    # ══ standard · s19–s26 ═══════════════════════════════════════════════
    # The gamma camera itself, sterilisation dose against a safe human dose,
    # dating's own limits, and two applications the frozen rows never reach.
    {
        "id": "ks4-uses-of-nuclear-radiation-s19",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how a gamma camera positioned outside the body "
                "builds up a picture of where a tracer has collected "
                "inside a patient.",
        "options": [
            "It detects the gamma photons leaving the body from different "
            "points and builds an image from where more of them arrive",
            "It detects the heat released as the tracer decays inside "
            "different organs, and converts that heat map into an image",
            "It measures the small change in the patient's body "
            "temperature caused by the tracer, which differs from organ "
            "to organ",
            "It detects the alpha particles that escape from the tracer "
            "and pass straight through the tissue above wherever it has "
            "collected",
        ],
        "correct_index": 0,
        "why": "Gamma is the only one of the three types that escapes the "
               "body in useful numbers, so the camera maps where the "
               "photons are leaving from most strongly.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s20",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the radiation dose used to sterilise medical "
                "equipment in a gamma facility would be lethal if a "
                "person received it.",
        "options": [
            "The equipment absorbs the gamma rays completely during "
            "sterilisation, but a person's body would reflect most of "
            "them straight back out again, causing far more damage per "
            "photon absorbed",
            "Sterilisation requires killing every microorganism present, "
            "which needs a dose many times larger than any dose "
            "considered safe for living tissue",
            "The equipment is sterilised using a different type of "
            "radiation from the type that would be dangerous to a person "
            "standing nearby",
            "A person absorbs radiation more slowly than a packet of "
            "instruments does, so the same dose takes far longer to "
            "become dangerous to them",
        ],
        "correct_index": 1,
        "why": "Killing resistant microorganisms needs a dose orders of "
               "magnitude above what any safety limit allows a person to "
               "receive, which is why the process is confined to a "
               "shielded cell.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s21",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wooden artefact is later found to have been varnished "
                "with a modern synthetic coating before it was "
                "carbon-dated. Explain why the result is likely to "
                "underestimate its true age.",
        "options": [
            "The varnish blocks some of the radiation the wood emits, so "
            "fewer decays are counted and the wood appears to have "
            "decayed less than it has",
            "The varnish reacts chemically with the carbon-14 in the "
            "wood and destroys some of it, leaving less to measure than "
            "the wood originally held",
            "The varnish adds fresh carbon-14 to the sample, so the "
            "measured ratio looks closer to that of living material than "
            "the wood's own ratio does",
            "The varnish absorbs background radiation that would "
            "otherwise reach the detector, which makes the corrected "
            "count rate too low",
        ],
        "correct_index": 2,
        "why": "Modern carbon carries the full living proportion of "
               "carbon-14, so any of it mixed into an old sample makes "
               "the measured age look younger than the wood's true age.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s22",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A company must find a leak in a buried water pipe and "
                "separately check the wall thickness of an exposed steel "
                "tank standing in the open. Explain why gamma is chosen "
                "for the buried pipe but beta can be used for the tank.",
        "options": [
            "Beta is more expensive to produce than gamma, so it is "
            "reserved for jobs where a lower activity source is "
            "acceptable, such as the exposed tank",
            "Gamma cannot be detected in the open air, so it can only be "
            "used underground where the surrounding soil helps to guide "
            "it to the detector",
            "The buried pipe is checked less often than the tank, so a "
            "source with a shorter half-life is acceptable for the "
            "underground survey",
            "The buried pipe's radiation must cross soil and pipe wall "
            "to reach a surface detector, while the tank's gauge only "
            "has to cross the steel itself",
        ],
        "correct_index": 3,
        "why": "The distance and material the radiation has to cross "
               "decides the choice: gamma for the long underground "
               "journey, beta for the thin steel wall of the tank.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s23",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Testing an ancient linen cloth shows it retains only one "
                "sixteenth of the carbon-14 that a freshly woven length "
                "of the same plant fibre would contain. Work out the "
                "number of half-lives of carbon-14 that have gone by.",
        "options": [
            "4",
            "8",
            "3",
            "16",
        ],
        "correct_index": 0,
        "why": "6.25% is one part in sixteen, and each half-life halves "
               "what remains — 50, 25, 12.5, 6.25 — which is four "
               "halvings.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s24",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A manufacturer proposes replacing the americium-241 in a "
                "smoke detector, whose half-life is about 430 years, with "
                "a different alpha emitter of half-life 30 days, to "
                "reduce cost. Explain why this would be a poor choice "
                "for a detector meant to last ten years.",
        "options": [
            "Alpha from the new isotope would ionise the air more weakly "
            "than americium-241 does, so the detector would fail to "
            "sound even with no smoke present",
            "The new isotope's activity would fall to a negligible level "
            "within a few years, long before the detector's designed "
            "ten-year life is over",
            "A 30-day half-life makes the isotope too radioactive to be "
            "sealed safely inside a plastic casing fitted in a family "
            "home",
            "Alpha particles from a shorter-half-life isotope travel "
            "further than those from americium-241, so they would "
            "escape the detector casing",
        ],
        "correct_index": 1,
        "why": "With a half-life of only 30 days the source has decayed "
               "through more than a hundred half-lives after ten years, "
               "leaving essentially no activity to ionise the air.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s25",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a hospital uses radioactive iodine-123, "
                "rather than the stable, non-radioactive iodine already "
                "present in a patient's diet, to investigate the thyroid "
                "gland.",
        "options": [
            "Stable iodine is not absorbed by the thyroid gland at all, "
            "so it would never collect there in the first place for a "
            "scan to detect",
            "Stable iodine reacts chemically with the thyroid tissue, "
            "which would damage the gland before any useful image could "
            "be taken",
            "Only a radioactive form of iodine emits radiation that a "
            "gamma camera outside the body can detect, so the gland's "
            "uptake can be imaged",
            "Stable iodine has a much larger atomic mass than iodine-123, "
            "so it cannot travel through the bloodstream to reach the "
            "thyroid",
        ],
        "correct_index": 2,
        "why": "The thyroid takes up either form the same way, but only "
               "the radioactive form gives off radiation that reveals "
               "where it has collected.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-s26",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain one advantage of placing a small sealed "
                "radioactive source directly next to a tumour, rather "
                "than aiming an external gamma beam at it from outside "
                "the body.",
        "options": [
            "An implanted source can be left in place for the rest of "
            "the patient's life without ever being removed or replaced",
            "An implanted source needs no shielding of any kind around "
            "it, because its radiation is completely absorbed by the "
            "tumour itself the moment it is put in place inside it",
            "An implanted source treats the tumour using beta radiation "
            "only, which is inherently safer than the gamma used in an "
            "external beam",
            "An implanted source is already at the tumour, so its "
            "radiation does not have to cross as much healthy tissue on "
            "the way in as an external beam does",
        ],
        "correct_index": 3,
        "why": "An external beam irradiates every layer of tissue between "
               "the skin and the tumour, while a source placed at the "
               "tumour delivers most of its dose there directly.",
    },

    # ══ harder · h19–h26 ═════════════════════════════════════════════════
    # The half-life contrast made explicit, proposals to evaluate, dating's
    # two failure limits, and a tracer-logistics calculation of its own.
    {
        "id": "ks4-uses-of-nuclear-radiation-h19",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an industrial thickness gauge and a medical "
                "tracer are chosen with opposite requirements for "
                "half-life.",
        "options": [
            "A gauge must give a steady, unchanging reading for years "
            "without the source being replaced, while a tracer must "
            "clear its own activity from the patient's body within "
            "hours or days",
            "A gauge is used only once a year, so a long half-life saves "
            "money, while a tracer is used many times a day, so a short "
            "half-life is cheaper to produce",
            "A gauge needs a source that emits alpha radiation, which "
            "always has a long half-life, while a tracer needs one that "
            "emits gamma, which always has a short half-life",
            "A gauge is operated only by trained staff who can tolerate "
            "a somewhat higher dose, while a tracer is given to a "
            "patient who must receive as low a dose as possible, "
            "whatever its half-life happens to be",
        ],
        "correct_index": 0,
        "why": "A stable, long-running instrument needs an unchanging "
               "source, while a source left decaying inside a patient "
               "must stop being active again soon — opposite jobs, "
               "opposite half-lives.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h20",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that placing a radioactive implant "
                "directly at a tumour removes all risk of harm to the "
                "patient's healthy tissue.",
        "options": [
            "The claim is sound, because a sealed implant cannot release "
            "any radiation at all once it has been placed inside the "
            "body",
            "The claim is unsound, because tissue immediately next to "
            "the implant still absorbs radiation, even though the total "
            "volume affected is smaller than with an external beam",
            "The claim is sound, because healthy tissue does not absorb "
            "radiation from a source that is touching a tumour rather "
            "than aimed from outside it",
            "The claim is unsound, because an implant delivers a smaller "
            "total dose to the tumour than an external beam ever could, "
            "and so also to the tissue around it",
        ],
        "correct_index": 1,
        "why": "Reducing the volume of healthy tissue crossed is a real "
               "benefit, but the tissue immediately surrounding the "
               "implant is still irradiated — the risk is reduced, not "
               "eliminated.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h21",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A wooden bowl is found to hold between 40% and 45% of "
                "the carbon-14 present in living wood. Given that one "
                "half-life leaves 50% and two half-lives leave 25%, "
                "determine what this tells you about the bowl's age.",
        "options": [
            "The bowl is younger than one half-life old, because 40–45% "
            "is closer to 50% than to any lower value",
            "The bowl is exactly one and a half half-lives old, because "
            "that value always lies exactly halfway between 50% and 25%",
            "The bowl is a little older than one half-life, since its "
            "remaining fraction lies just below the 50% mark left after "
            "one half-life",
            "The bowl's age cannot be estimated at all unless its "
            "carbon-14 fraction is exactly 50%, 25%, 12.5% or another "
            "exact power of a half",
        ],
        "correct_index": 2,
        "why": "40–45% is below the 50% left after one half-life but "
               "well above the 25% left after two, so the bowl's age "
               "sits a little beyond one half-life.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h22",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A designer proposes replacing the alpha source in a "
                "smoke detector with a beta source of similar activity, "
                "arguing that beta is also ionising. Evaluate the "
                "proposal.",
        "options": [
            "The proposal is sound, because beta ionises air far more "
            "strongly than alpha does over the same short distance "
            "inside the casing",
            "The proposal is sound, because beta and alpha ionise air by "
            "exactly the same mechanism and to the same extent, so "
            "either would work equally well",
            "The proposal is unsound, because beta cannot ionise air at "
            "all, whatever its activity, so no current would flow "
            "between the electrodes",
            "The proposal is unsound, because beta ionises air far more "
            "weakly than alpha per particle, so far less current would "
            "flow for the detector to monitor",
        ],
        "correct_index": 3,
        "why": "Alpha's large charge and mass make it a far denser "
               "ioniser than beta over the same short path, which is "
               "exactly why alpha was chosen for the job in the first "
               "place.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h23",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A contractor proposes using an alpha source instead of "
                "a gamma source for an underground pipeline leak survey, "
                "arguing it would give a lower dose to people living "
                "nearby. Evaluate the proposal.",
        "options": [
            "The proposal fails at the first step: alpha cannot reach a "
            "detector at the surface through the pipe wall and the "
            "soil, so no reading would ever be obtained",
            "The proposal is sound, because alpha's shorter range means "
            "people at the surface receive almost no dose, while a "
            "gamma survey exposes the whole neighbourhood",
            "The proposal is sound, because alpha is absorbed harmlessly "
            "by the soil before it can cause any damage to buildings or "
            "people living above the pipe",
            "The proposal fails, because alpha sources cannot be "
            "manufactured with a half-life short enough for a single "
            "afternoon's survey",
        ],
        "correct_index": 0,
        "why": "Whatever the dose argument, alpha loses to a few "
               "centimetres of air, so a source that cannot reach the "
               "detector cannot do the job at all.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h24",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A hospital prepares a batch of a gamma-emitting tracer "
                "at an activity of 800 MBq at 9 a.m., for use in a scan "
                "scheduled for 5 p.m. the same day. The tracer's "
                "half-life is 4 hours. Calculate the activity available "
                "for the scan.",
        "options": [
            "400 MBq",
            "200 MBq",
            "100 MBq",
            "600 MBq",
        ],
        "correct_index": 1,
        "why": "Eight hours have passed, which is two half-lives: "
               "800 → 400 → 200 MBq.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h25",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A laboratory is asked to carbon-date a sample thought to "
                "be around 60,000 years old — roughly ten half-lives of "
                "carbon-14. Evaluate whether the method can give a "
                "reliable result.",
        "options": [
            "It is reliable, because carbon-14 keeps decaying at exactly "
            "the same rate whatever the age of the sample, so accuracy "
            "never changes",
            "It is reliable, provided the laboratory counts for exactly "
            "the same length of time as it would for a much younger "
            "sample",
            "It is unreliable at that age, because after ten half-lives "
            "so little carbon-14 remains that the measurement is "
            "swamped by uncertainty",
            "It is unreliable, because carbon-14 stops decaying "
            "completely once a sample passes about eight half-lives in "
            "age",
        ],
        "correct_index": 2,
        "why": "Ten half-lives leaves roughly one part in a thousand of "
               "the original carbon-14, too little to measure precisely "
               "against the background and other sources of error.",
    },
    {
        "id": "ks4-uses-of-nuclear-radiation-h26",
        "subtopic_slug": "uses-of-nuclear-radiation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A supplier claims that a single isotope with a half-life "
                "of about six months could serve equally well as both an "
                "industrial thickness-gauge source and a medical tracer. "
                "Evaluate the claim.",
        "options": [
            "The claim is sound, because six months is long enough for "
            "a gauge and short enough for a tracer, so the same isotope "
            "suits both jobs equally well",
            "The claim is sound, provided the isotope emits both alpha "
            "and gamma radiation at once, one type for each application",
            "The claim is unsound, because no isotope can be used in "
            "more than one application at all, whatever its half-life "
            "happens to be",
            "The claim is unsound, because six months is far too short "
            "for a gauge needing years of steady output and far too "
            "long for a tracer that must clear a patient within days",
        ],
        "correct_index": 3,
        "why": "A gauge and a tracer sit at opposite ends of the "
               "half-life scale — years for one, hours or days for the "
               "other — and six months serves neither well.",
    },
]
