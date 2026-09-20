"""Physics · Atomic structure — the MRB-338 expansion of `radioactive-contamination`.

One leaf only: AQA 8463 §6.4.2.4 — contamination against irradiation, which
radiation is the hazard from outside the body and which from inside it, the
biological effect (DNA damage, mutation, raised cancer risk, acute sickness at
high dose), the two separate lists of precautions (tongs, gloves, ventilation,
no eating, sealed containers against contamination; time, distance, shielding,
dosimeters against irradiation), decontamination, and the half-life reasoning
that decides how long a contaminated place stays a problem.

The original four rows of each band in `atomic_structure__b.py` take the
definition of contamination, the persistent bench count, tongs-and-gloves, the
sealed source at two metres, the arm's-length gamma source, the dosimeter
badge, alpha on skin against alpha swallowed, the lead-lined box, the
gamma-outside/alpha-inside comparison, the sterilised instruments, the nurse's
gloves and the CT-scan judgement. Nothing here repeats one of those frames:
this file works the OTHER definition (irradiation), the named decontamination
methods, beta as its own case rather than as the option nobody picks, the
inverse-square arithmetic behind "stand further back", dose-rate × time
budgets, and the half-life-of-the-contaminant question that decides when an
area reopens.

This is a BASE subtopic — `tier='foundation'`, `triple_only=False` — so every
row is answerable by a Combined Science pupil. The weight follows the AQA
command words: `easier` is eight rows of definition and one-step recall, and
the demand sits in the two twenty-two-row bands, where a precaution has to be
matched to the hazard it actually addresses, or two exposures compared.

Working lives in `why` and never in an option (brief §9.2). Doses are in
microsieverts or millisieverts throughout and every calculation comes out
exactly.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The second definition, the named examples on each side of it, the
    # shielding materials, and the biological effect.
    {
        "id": "ks4-radioactive-contamination-e05",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed source is held near a person for a few seconds and "
                "then taken away again. State what the person has received.",
        "options": [
            "Contamination, because radioactive atoms have crossed onto their "
            "skin",
            "Irradiation, because they were exposed to radiation from an "
            "outside source",
            "Nothing measurable, because a few seconds is too short for any "
            "radiation to arrive through the air",
            "Both, because every exposure leaves some radioactive material "
            "behind",
        ],
        "correct_index": 1,
        "why": "Irradiation is exposure to radiation from a source that is not "
               "on or in you, so it ends the moment the source is taken away.",
    },
    {
        "id": "ks4-radioactive-contamination-e06",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these is an example of radioactive contamination?",
        "options": [
            "Having a chest X-ray taken at a hospital",
            "Breathing in radon gas inside a house",
            "Standing beside a cobalt-60 source in a store room",
            "Receiving radiotherapy from a rotating gamma beam",
        ],
        "correct_index": 1,
        "why": "Breathed-in radon is radioactive material taken inside the "
               "body, where it stays and goes on emitting — the other three "
               "are external sources that stop affecting you when you leave.",
    },
    {
        "id": "ks4-radioactive-contamination-e07",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which type of radiation does the most damage when the "
                "source has been swallowed.",
        "options": [
            "Gamma, because it passes right through the body and out the "
            "other side",
            "Beta, because it is the only one that can travel through soft "
            "tissue",
            "Alpha, because it is strongly ionising and gives up all its "
            "energy in nearby cells",
            "All three do equal damage inside, because the body absorbs every "
            "kind fully",
        ],
        "correct_index": 2,
        "why": "Alpha has a very short range, so inside the body it deposits "
               "all of its energy into a small volume of living tissue.",
    },
    {
        "id": "ks4-radioactive-contamination-e08",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the material normally used to shield a beta source.",
        "options": [
            "A sheet of paper a fraction of a millimetre thick",
            "A few millimetres of aluminium",
            "Several centimetres of lead or concrete",
            "A layer of dry air about ten centimetres deep",
        ],
        "correct_index": 1,
        "why": "Beta passes through paper and air but is absorbed by a few "
               "millimetres of aluminium; paper stops alpha and lead is "
               "needed for gamma.",
    },
    {
        "id": "ks4-radioactive-contamination-e09",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what ionising radiation does to a living cell it "
                "passes through.",
        "options": [
            "It heats the cell until the water inside it boils away, which is "
            "what people call a radiation burn",
            "It can damage the DNA, which may cause a mutation and raise "
            "cancer risk",
            "It adds extra neutrons to the nuclei of the atoms in the cell, "
            "leaving that cell radioactive for the rest of its life",
            "It turns the cell into a radioactive source of the same kind",
        ],
        "correct_index": 1,
        "why": "Ionising radiation knocks electrons from atoms in the cell, "
               "and damage to DNA can lead to mutations and an increased risk "
               "of cancer.",
    },
    {
        "id": "ks4-radioactive-contamination-e10",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Apart from shielding and limiting time, state the third way "
                "of reducing the dose received from a source outside the body.",
        "options": [
            "Working at a greater distance from the source",
            "Wearing two pairs of gloves rather than one, so that twice as "
            "much radiation is absorbed",
            "Keeping the room as cool as the work allows, since a cool source "
            "decays more slowly",
            "Choosing a source with a longer half-life, whose radiation is "
            "given out more gently",
        ],
        "correct_index": 0,
        "why": "Time, distance and shielding are the three controls on "
               "irradiation, and moving further away cuts the dose rate "
               "sharply.",
    },
    {
        "id": "ks4-radioactive-contamination-e11",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why eating and drinking are forbidden in a laboratory "
                "where unsealed radioactive materials are used.",
        "options": [
            "Food absorbs radiation and then emits it again for several hours",
            "Chewing slows a worker down, so more time is spent near a source",
            "Radioactive material could be swallowed, contaminating the "
            "inside of the body",
            "Warm drinks raise the room temperature and speed up the decay "
            "rate of any source left open on the bench",
        ],
        "correct_index": 2,
        "why": "The rule prevents ingestion: swallowed material becomes an "
               "internal source that keeps emitting inside the body.",
    },
    {
        "id": "ks4-radioactive-contamination-e12",
        "subtopic_slug": "radioactive-contamination",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why unsealed radioactive powders are handled in a "
                "well-ventilated area.",
        "options": [
            "Moving air carries the radiation away before it reaches anybody "
            "standing at the bench",
            "Fresh air keeps the powder cool, which lowers its activity",
            "Ventilation dilutes the emitted gamma rays across a larger "
            "volume, which brings the dose rate down to a safe level",
            "It stops radioactive dust and gas building up where it could be "
            "breathed in",
        ],
        "correct_index": 3,
        "why": "Ventilation is a contamination control: it clears airborne "
               "dust and gas so they are not inhaled and taken into the body.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Precautions matched to the hazard they actually address, the two-way
    # comparison of external and internal sources, dose-rate arithmetic, and
    # the half-life of a contaminant.
    {
        "id": "ks4-radioactive-contamination-s05",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A worker finds radioactive dust on their overalls. Explain "
                "why removing and bagging the overalls reduces their risk.",
        "options": [
            "It takes the radioactive material itself away from the body, so "
            "it stops emitting close to their tissue",
            "It cools the dust down, and cool material has a much lower "
            "activity than warm material",
            "The plastic bag absorbs all three types of radiation, so the "
            "dust becomes harmless once sealed",
            "It converts the contamination into irradiation, which cannot do "
            "any damage to living cells",
        ],
        "correct_index": 0,
        "why": "Contamination is the source travelling with you, so removing "
               "the contaminated clothing removes the source.",
    },
    {
        "id": "ks4-radioactive-contamination-s06",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an alpha emitter breathed into the lungs is more "
                "damaging than a gamma emitter of the same activity in the "
                "same place.",
        "options": [
            "Gamma is uncharged, so it passes through lung tissue without "
            "interacting",
            "Alpha is strongly ionising over a very short range, so all of "
            "its energy goes into a small patch of lung tissue",
            "Alpha particles are attracted to lung tissue because the lungs "
            "carry a negative charge",
            "Gamma rays are heavier than alpha particles, so they settle out "
            "of the lungs more quickly and are cleared from the lungs before "
            "they can do harm",
        ],
        "correct_index": 1,
        "why": "Alpha's short range means every alpha particle stops within a "
               "millimetre or so of where it started, concentrating the "
               "ionisation; much of the gamma escapes the body entirely.",
    },
    {
        "id": "ks4-radioactive-contamination-s07",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gamma source gives a dose rate of 80 microsieverts per hour "
                "at a distance of 1.0 m. Calculate the dose rate at 2.0 m.",
        "options": [
            "40 microsieverts per hour",
            "20 microsieverts per hour",
            "160 microsieverts per hour",
            "8 microsieverts per hour",
        ],
        "correct_index": 1,
        "why": "Doubling the distance spreads the radiation over four times "
               "the area, so the dose rate falls to a quarter: 80 ÷ 4 = 20 "
               "microsieverts per hour.",
    },
    {
        "id": "ks4-radioactive-contamination-s08",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A technician works for 5.0 hours where the dose rate is 12 "
                "microsieverts per hour. Calculate the dose received.",
        "options": [
            "2.4 microsieverts",
            "17 microsieverts",
            "60 microsieverts",
            "0.6 microsieverts",
        ],
        "correct_index": 2,
        "why": "Dose is dose rate multiplied by time: 12 × 5.0 = 60 "
               "microsieverts.",
    },
    {
        "id": "ks4-radioactive-contamination-s09",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a radiographer steps behind a lead screen while "
                "an X-ray is being taken rather than putting on thicker gloves.",
        "options": [
            "Gloves would make her hands too clumsy to operate the machine "
            "safely",
            "The hazard is contamination, and a screen catches dust that "
            "gloves would miss",
            "The screen absorbs the X-rays, whereas gloves leave the rest of "
            "her body exposed to them",
            "X-rays travel only downwards, so a vertical screen is the only "
            "shield that works",
        ],
        "correct_index": 2,
        "why": "The hazard is irradiation of her whole body by penetrating "
               "X-rays, so dense shielding between her and the beam is what "
               "protects her.",
    },
    {
        "id": "ks4-radioactive-contamination-s10",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two spills contaminate a store room floor. One isotope has a "
                "half-life of 6 hours and the other 30 years. Explain which "
                "spill is the greater long-term problem.",
        "options": [
            "The 30-year isotope, because its activity will still be close to "
            "its starting value for decades",
            "The 6-hour isotope, because a short half-life means it emits "
            "radiation for longer in total",
            "The 30-year isotope, because a longer half-life makes each "
            "emitted particle more ionising",
            "Neither, because half-life describes the decay rate and has no "
            "bearing on how long a hazard lasts in a store room",
        ],
        "correct_index": 0,
        "why": "A long half-life means the activity falls only slowly, so the "
               "contaminated floor stays a hazard for many years rather than "
               "clearing itself in a day.",
    },
    {
        "id": "ks4-radioactive-contamination-s11",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why bone marrow is one of the tissues most easily "
                "harmed by a radiation dose.",
        "options": [
            "Marrow lies deep in the bone, where radiation is trapped and "
            "cannot escape again",
            "Marrow contains no DNA, so damage there cannot be repaired by "
            "the body",
            "Marrow cells divide rapidly, so DNA damage is copied into many "
            "new cells",
            "Marrow is the densest tissue in the body, so it absorbs more "
            "gamma radiation than the bone surrounding it",
        ],
        "correct_index": 2,
        "why": "Rapidly dividing tissue is the most radiosensitive, because a "
               "damaged DNA strand is replicated into the daughter cells "
               "before it can be repaired.",
    },
    {
        "id": "ks4-radioactive-contamination-s12",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a small liquid spill of a radioactive solution "
                "should be dealt with on a laboratory bench.",
        "options": [
            "Wipe it up with absorbent pads and dispose of them as "
            "radioactive waste",
            "Cover the wet patch with a lead sheet and leave the bench in use, "
            "since lead absorbs radiation of every kind",
            "Rinse it into the sink with plenty of cold tap water",
            "Warm the bench with a hot plate so the liquid evaporates away, "
            "carrying the radioactivity away with the vapour from the surface",
        ],
        "correct_index": 0,
        "why": "Decontamination means physically removing the radioactive "
               "material and containing it, so it is absorbed, bagged and "
               "handled as radioactive waste.",
    },
    {
        "id": "ks4-radioactive-contamination-s13",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a sheet of paper is enough to shield an alpha "
                "source but not a beta source.",
        "options": [
            "Paper carries no charge, and only charged shields can stop beta "
            "particles",
            "Beta particles are far more strongly ionising than alpha, so they "
            "burn through paper, leaving a small hole wherever one of them "
            "strikes it",
            "Alpha particles are much heavier than beta particles, so gravity "
            "pulls them onto the paper, where a single sheet is enough to "
            "catch every one of them",
            "Alpha has a range of only a few centimetres in air and is "
            "absorbed by paper, while beta penetrates several millimetres of "
            "solid material",
        ],
        "correct_index": 3,
        "why": "Penetrating power runs alpha < beta < gamma, so beta passes "
               "straight through paper and needs a few millimetres of "
               "aluminium.",
    },
    {
        "id": "ks4-radioactive-contamination-s14",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient is injected with a gamma-emitting tracer. A student "
                "says the patient has only been irradiated. Explain why the "
                "student is wrong.",
        "options": [
            "The tracer is inside the patient, so radioactive material has "
            "been taken into the body — that is contamination",
            "An injection is a medical procedure, and medical procedures "
            "count as neither term",
            "Gamma radiation cannot irradiate anybody, because it is a wave "
            "rather than a particle",
            "The patient is contaminated only once the gamma camera has been "
            "switched on above them",
        ],
        "correct_index": 0,
        "why": "The source has been placed inside the body and travels with "
               "the patient, which is exactly what contamination means — "
               "deliberate and useful contamination, but contamination.",
    },
    {
        "id": "ks4-radioactive-contamination-s15",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a worker's dosimeter reading is added up over a "
                "whole year rather than judged one day at a time.",
        "options": [
            "A badge can be read once a year at most, because the film inside "
            "it is damaged by more frequent reading",
            "The risk depends on the total dose built up over time, so annual "
            "limits are what the readings are checked against",
            "Radiation received on one day is cancelled out by a day spent "
            "away from any source, so the yearly total comes back close to "
            "zero anyway",
            "Daily readings are too large to record, so a yearly average is "
            "used to keep the numbers small, which keeps the recorded numbers "
            "small and easy to file",
        ],
        "correct_index": 1,
        "why": "Dose accumulates: the raised cancer risk depends on the total "
               "received, so exposure is managed against an annual limit.",
    },
    {
        "id": "ks4-radioactive-contamination-s16",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a laboratory coat protects a worker from "
                "contamination but not from a nearby gamma source.",
        "options": [
            "A coat is loose-fitting, so gamma rays pass round it through the "
            "gaps at the sleeves and collar rather than through the cloth "
            "itself",
            "A coat becomes contaminated itself, which draws the gamma rays "
            "towards the wearer",
            "A coat is made of cotton, and cotton reflects alpha but focuses "
            "gamma onto the skin",
            "A coat catches radioactive material before it reaches the skin, "
            "but thin cloth absorbs almost no gamma",
        ],
        "correct_index": 3,
        "why": "Clothing is a barrier against material, not against "
               "penetrating radiation — gamma needs dense shielding such as "
               "lead or concrete.",
    },
    {
        "id": "ks4-radioactive-contamination-s17",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a technician transferring a source works as "
                "quickly as the task safely allows.",
        "options": [
            "A fast transfer lowers the source's activity by giving it less "
            "time to warm up",
            "Dose is dose rate multiplied by time, so less time near the "
            "source means a smaller dose",
            "Radiation takes several minutes to build up to full intensity "
            "after a container is opened and left standing on the bench",
            "Hurrying reduces the chance of the source being dropped, which "
            "is the only real hazard",
        ],
        "correct_index": 1,
        "why": "Time is one of the three irradiation controls: the dose "
               "received is the dose rate multiplied by the time spent in it.",
    },
    {
        "id": "ks4-radioactive-contamination-s18",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why alpha contamination on unbroken skin is much less "
                "serious than the same contamination on an open cut.",
        "options": [
            "A cut bleeds, and blood attracts alpha particles towards the "
            "damaged tissue, which is why a cut near a source feels hot",
            "Unbroken skin neutralises alpha particles by adding electrons to "
            "them",
            "The dead outer layer of skin absorbs alpha, but through a cut it "
            "reaches living tissue directly",
            "Skin is a good conductor, so the charge on the alpha particles "
            "runs away harmlessly, leaving nothing behind for the tissue to "
            "absorb",
        ],
        "correct_index": 2,
        "why": "Alpha is stopped by the dead outer skin layer; a cut removes "
               "that barrier and lets the alpha deposit its energy in living "
               "cells.",
    },
    {
        "id": "ks4-radioactive-contamination-s19",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a patient who has had a dental X-ray does not "
                "need to be kept away from other people afterwards.",
        "options": [
            "The dose from a dental X-ray is too small to have any effect on "
            "living tissue",
            "The X-rays leave the patient's jaw slowly, over about half an "
            "hour",
            "Dental X-rays are aimed downwards, so nothing reaches anyone "
            "standing nearby",
            "No radioactive material was put into the patient, so nothing is "
            "emitted once the machine is off",
        ],
        "correct_index": 3,
        "why": "An X-ray machine irradiates the patient while it is switched "
               "on; it transfers no radioactive material, so the patient "
               "emits nothing afterwards.",
    },
    {
        "id": "ks4-radioactive-contamination-s20",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a fire in a store holding unsealed radioactive "
                "material is treated as a contamination emergency.",
        "options": [
            "Heat raises the activity of every source in the building by "
            "several times, so the store becomes far more radioactive than it "
            "was",
            "Smoke and hot gases can carry radioactive particles out of the "
            "building to be breathed in",
            "Flames convert stable atoms in the building into radioactive "
            "ones",
            "Water from the fire hoses turns radioactive as soon as it is "
            "sprayed",
        ],
        "correct_index": 1,
        "why": "A fire lifts the material into the air as smoke and dust, "
               "which can be inhaled or settle on people and ground far from "
               "the store.",
    },
    {
        "id": "ks4-radioactive-contamination-s21",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why workers in a radon-affected house are advised to "
                "improve the ventilation rather than to line the walls with "
                "lead.",
        "options": [
            "Lead reacts chemically with radon and produces a more dangerous "
            "gas, which is far more dangerous to breathe than the radon itself",
            "Radon emits gamma rays alone, which pass through lead without "
            "being absorbed, so a lead lining would make no difference to the "
            "dose it delivers",
            "Ventilation clears the gas out before it can be breathed in, "
            "while shielding does nothing about a gas already indoors",
            "Lead is porous to gases, so radon would seep through it within a "
            "few days",
        ],
        "correct_index": 2,
        "why": "The radon hazard is inhalation — internal contamination — so "
               "the control is removing the gas, not shielding against a beam "
               "that is not the problem.",
    },
    {
        "id": "ks4-radioactive-contamination-s22",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A radiation worker's annual limit is 20 millisieverts. She "
                "has already received 14 millisieverts this year. Calculate "
                "the dose she may still receive.",
        "options": [
            "6 millisieverts",
            "34 millisieverts",
            "14 millisieverts",
            "0.7 millisieverts",
        ],
        "correct_index": 0,
        "why": "The remaining allowance is the limit minus the dose already "
               "recorded: 20 − 14 = 6 millisieverts.",
    },
    {
        "id": "ks4-radioactive-contamination-s23",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a very large dose received in a few minutes "
                "causes different effects from the same total dose spread "
                "over forty years.",
        "options": [
            "A slow dose is absorbed by the skeleton, where it can do no "
            "damage to soft tissue",
            "A large sudden dose kills many cells at once, causing radiation "
            "sickness, while a slow dose mainly raises the long-term cancer "
            "risk",
            "A slow dose is cancelled out by the body's own background "
            "radiation over the same period, so the two come to nothing over "
            "the course of a lifetime of ordinary living",
            "A large sudden dose is less harmful, because the body repairs "
            "everything it notices immediately, however large that sudden dose "
            "happens to be",
        ],
        "correct_index": 1,
        "why": "Acute high doses destroy enough cells at once to make a "
               "person ill; the same energy delivered slowly leaves the body "
               "time to repair, and the main remaining effect is raised "
               "cancer risk.",
    },
    {
        "id": "ks4-radioactive-contamination-s24",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a school still uses long-handled tongs for a "
                "source that is completely sealed.",
        "options": [
            "The seal can be broken by the warmth of a hand holding the "
            "source",
            "Tongs are the safest way of gripping a source without making it "
            "spin",
            "Sealed sources leak slowly, so gloves alone are never enough for "
            "them, however carefully the seal was made",
            "The seal prevents contamination, but the tongs add distance and "
            "so cut the dose to the hands",
        ],
        "correct_index": 3,
        "why": "A seal deals with the material; the remaining hazard is "
               "irradiation, and distance is the cheapest way to reduce it.",
    },
    {
        "id": "ks4-radioactive-contamination-s25",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a worker washes their hands immediately after "
                "handling an unsealed source, even with no visible spill.",
        "options": [
            "Washing removes any radioactive material that has settled there, "
            "before it is transferred to the mouth",
            "Water cools the skin, which slows down any decay taking place at "
            "the surface, so the count rate at the fingertips falls away "
            "within a minute",
            "Soap reacts with radioactive atoms and turns them into stable "
            "ones",
            "Wet skin absorbs less radiation from the surroundings than dry "
            "skin does, which is why a damp cloth is used to clear a spill",
        ],
        "correct_index": 0,
        "why": "Invisible traces of material are exactly what contamination "
               "is, and hands are the usual route from a bench into the body.",
    },
    {
        "id": "ks4-radioactive-contamination-s26",
        "subtopic_slug": "radioactive-contamination",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why lead is chosen to shield a gamma source while "
                "aluminium would be chosen for a beta source.",
        "options": [
            "Lead is heavier, so gravity pulls the gamma rays downwards into "
            "the floor",
            "Aluminium is shiny, so it reflects beta particles back towards "
            "the source, so none of them ever reach the person behind the "
            "screen",
            "Lead is much denser, so it absorbs the far more penetrating "
            "gamma, which thin aluminium would not",
            "Lead conducts electricity better, so it drains the charge from "
            "the gamma rays, leaving them with no energy to carry through the "
            "shield and no ability to ionise",
        ],
        "correct_index": 2,
        "why": "Shielding is matched to penetrating power: a few millimetres "
               "of aluminium stops beta, but gamma needs centimetres of a "
               "dense material such as lead.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Two exposures compared, a precaution judged against the hazard it does
    # not address, rearranged inverse-square and dose-budget arithmetic, and
    # the decisions a half-life forces.
    {
        "id": "ks4-radioactive-contamination-h05",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A dose rate of 360 microsieverts per hour is measured 0.50 m "
                "from a gamma source. Determine the distance at which the "
                "dose rate would be 40 microsieverts per hour.",
        "options": [
            "1.5 m",
            "4.5 m",
            "2.0 m",
            "0.17 m",
        ],
        "correct_index": 0,
        "why": "The dose rate falls by a factor of 9, and because it follows "
               "an inverse square the distance must rise by a factor of 3: "
               "0.50 × 3 = 1.5 m.",
    },
    {
        "id": "ks4-radioactive-contamination-h06",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A worker's annual dose limit is 20 millisieverts. In one part "
                "of the plant the dose rate is 50 microsieverts per hour. "
                "Calculate the greatest number of hours she may work there in "
                "a year.",
        "options": [
            "400 hours",
            "1000 hours",
            "40 hours",
            "4000 hours",
        ],
        "correct_index": 0,
        "why": "20 millisieverts is 20 000 microsieverts, and 20 000 ÷ 50 = "
               "400 hours.",
    },
    {
        "id": "ks4-radioactive-contamination-h07",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Worker P stands 1.0 m from a gamma source for 4.0 hours. "
                "Worker Q stands 2.0 m from the same source for 8.0 hours. "
                "Compare the doses they receive.",
        "options": [
            "Q receives twice the dose of P, because he spends twice as long "
            "near the source",
            "P receives twice the dose of Q, because quartering the dose rate "
            "outweighs doubling the time",
            "They receive the same dose, because distance and time change by "
            "the same factor",
            "Q receives four times the dose of P, because dose depends on the "
            "total time spent and nothing else",
        ],
        "correct_index": 1,
        "why": "Doubling the distance cuts the dose rate to a quarter, so Q's "
               "rate is one quarter of P's while his time is only doubled — "
               "Q receives half what P does.",
    },
    {
        "id": "ks4-radioactive-contamination-h08",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A technician proposes decontaminating a spill by laying a "
                "lead sheet over it and leaving the bench in service. "
                "Evaluate this proposal.",
        "options": [
            "It is sound, because lead absorbs radiation and so removes the "
            "hazard completely",
            "It is sound, because covered material decays far faster than "
            "material left open to the air, so the spill will clear itself "
            "within a week",
            "It is unsound, because lead sheet is too thin to absorb alpha "
            "particles from a spill",
            "It is unsound, because the radioactive material is still there "
            "and can be spread further the moment the sheet is moved",
        ],
        "correct_index": 3,
        "why": "Shielding reduces irradiation but does nothing about "
               "contamination: decontamination means removing and containing "
               "the material itself.",
    },
    {
        "id": "ks4-radioactive-contamination-h09",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Strawberries are irradiated with gamma rays to make them keep "
                "longer. A shopper refuses to buy them, saying they must now "
                "be radioactive. Evaluate the shopper's reasoning.",
        "options": [
            "She is right, because gamma rays add energy to the fruit and "
            "energy is what makes a nucleus radioactive inside each strawberry",
            "She is wrong, because no radioactive material is transferred, so "
            "the fruit emits nothing once it leaves the beam",
            "She is right, because the packaging traps some of the gamma rays "
            "with the fruit inside, so the fruit goes on emitting long after "
            "it leaves the plant",
            "She is wrong, because gamma rays are too weakly ionising to have "
            "any effect whatever on the fruit, so the bacteria growing on it "
            "survive the treatment completely unharmed by it",
        ],
        "correct_index": 1,
        "why": "Irradiation kills the microorganisms on the fruit but leaves "
               "no radioactive atoms behind, so the fruit is not "
               "contaminated.",
    },
    {
        "id": "ks4-radioactive-contamination-h10",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alpha emitter and a gamma emitter have equal activities. "
                "Determine which is the greater hazard held in a sealed tube "
                "in the hand, and which is the greater hazard if swallowed.",
        "options": [
            "The gamma emitter in both situations, because it is the more "
            "penetrating of the two",
            "The alpha emitter in both situations, because it is the more "
            "strongly ionising of the two",
            "The gamma emitter in the hand, and the alpha emitter if "
            "swallowed",
            "The alpha emitter in the hand, and the gamma emitter if "
            "swallowed",
        ],
        "correct_index": 2,
        "why": "From outside, only gamma penetrates to reach organs; inside, "
               "alpha's short range means all of its energy is absorbed by "
               "surrounding tissue while much of the gamma escapes the body.",
    },
    {
        "id": "ks4-radioactive-contamination-h11",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient treated with radioactive iodine is asked to avoid "
                "prolonged close contact with young children for several "
                "days. Explain why the advice is temporary.",
        "options": [
            "The iodine is excreted and decays, so the activity inside the "
            "patient falls to a negligible level within days",
            "Children grow more resistant to radiation as they get older, so "
            "waiting removes the risk to them entirely within a few days of "
            "the treatment",
            "The iodine stops emitting once it has reached the thyroid gland "
            "and settled there",
            "The hospital removes the iodine during a follow-up appointment a "
            "few days later",
        ],
        "correct_index": 0,
        "why": "A treatment isotope is chosen with a short half-life, so the "
               "patient is briefly a source of radiation to those nearby and "
               "then ceases to be.",
    },
    {
        "id": "ks4-radioactive-contamination-h12",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "After a spill of an isotope with a half-life of 8.0 hours, a "
                "room is sealed off. Determine how long it must stay sealed "
                "for the activity to fall to one sixteenth of its starting "
                "value.",
        "options": [
            "32 hours",
            "128 hours",
            "16 hours",
            "8.0 hours",
        ],
        "correct_index": 0,
        "why": "One sixteenth is four halvings, so the time needed is 4 × 8.0 "
               "= 32 hours.",
    },
    {
        "id": "ks4-radioactive-contamination-h13",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hospital keeps its used tracer waste in a locked store for "
                "a few weeks and then disposes of it as ordinary waste. "
                "Explain why this is acceptable.",
        "options": [
            "Sealed storage stops radioactive atoms decaying, so the waste "
            "cannot become more dangerous",
            "The tracers used have half-lives of hours, so after weeks the "
            "activity has fallen to around the background level",
            "Radioactive waste becomes harmless as soon as it is no longer "
            "inside a patient's body",
            "A few weeks is long enough for the lead lining of the store to "
            "absorb all the radioactivity",
        ],
        "correct_index": 1,
        "why": "Decay storage works because a short-half-life isotope halves "
               "many times over in weeks, leaving an activity no greater than "
               "the background.",
    },
    {
        "id": "ks4-radioactive-contamination-h14",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A worker argues that because the same total dose can be "
                "received from natural sources anyway, no precautions are "
                "needed at work. Evaluate the argument.",
        "options": [
            "It is sound, because the body cannot tell one source of a dose "
            "from another, so the two may safely be traded off",
            "It is sound, because doses that occur naturally carry no risk at "
            "all",
            "It is unsound, because occupational dose is added on top of the "
            "unavoidable dose, raising the total and so the risk",
            "It is unsound, because doses received at work are of a different "
            "radiation type from natural ones, so the two cannot sensibly be "
            "added together as one figure",
        ],
        "correct_index": 2,
        "why": "Risk rises with total dose, so an avoidable extra exposure "
               "adds to an unavoidable one rather than replacing it.",
    },
    {
        "id": "ks4-radioactive-contamination-h15",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A worker wears gloves, a coat and a dosimeter, and stands "
                "well back from an unsealed beta source on an open bench. "
                "Determine which hazard is still poorly controlled.",
        "options": [
            "Irradiation of the whole body, because no shielding stands "
            "between the worker and the source",
            "Contamination of the hands, because gloves let beta particles "
            "through, which is why lead-lined gloves are issued for beta work "
            "of this kind",
            "Internal contamination, because the dosimeter cannot record an "
            "internal dose, so any material taken in would go unnoticed",
            "Contamination of the coat, because cloth cannot catch "
            "radioactive dust",
        ],
        "correct_index": 0,
        "why": "The clothing handles contamination and distance helps, but "
               "with no aluminium screen between worker and source the beta "
               "irradiation itself is uncontrolled.",
    },
    {
        "id": "ks4-radioactive-contamination-h16",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two spills of the same isotope are found. Spill X is a fine "
                "dry powder and spill Y is a sticky paste of the same "
                "activity. Compare the contamination risk they present.",
        "options": [
            "Y is more dangerous, because a paste stays in one place and so "
            "concentrates the dose, so the whole of the dose is delivered to "
            "one small area of the worker's skin",
            "X is more dangerous, because a dry powder can be disturbed into "
            "the air and breathed in",
            "They are equally dangerous, because the risk depends only on the "
            "activity of the spill, whatever form the spilt material happens "
            "to take",
            "Y is more dangerous, because a liquid carries radiation further "
            "than a solid can, which is why liquids are kept away from an open "
            "bench",
        ],
        "correct_index": 1,
        "why": "Contamination is about the material getting onto or into "
               "people, and an airborne powder has a route into the lungs "
               "that a paste does not.",
    },
    {
        "id": "ks4-radioactive-contamination-h17",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A monitor over a contaminated patch reads 950 counts per "
                "minute. After cleaning it reads 34 counts per minute, and "
                "the background in that room is 30 counts per minute. "
                "Evaluate whether the decontamination has worked.",
        "options": [
            "It has failed, because a reading of 34 counts per minute is "
            "still well above zero",
            "It cannot be judged, because the background was not measured "
            "before the cleaning began, so neither reading can be trusted on "
            "its own",
            "It has worked, because the patch now reads only a few counts per "
            "minute above the background of the room",
            "It has worked, because any count rate below 50 counts per minute "
            "is defined as clean, which is the figure written into the safety "
            "regulations for laboratories",
        ],
        "correct_index": 2,
        "why": "The patch's own contribution has fallen from about 920 to "
               "about 4 counts per minute, which is no more than the random "
               "variation in the background itself.",
    },
    {
        "id": "ks4-radioactive-contamination-h18",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why radiotherapy deliberately gives a patient a dose "
                "of radiation that would be unacceptable in a workplace.",
        "options": [
            "The dose is aimed at a tumour, and the benefit of destroying it "
            "is judged to outweigh the risk from the dose",
            "Radiation used in hospitals is a different kind that cannot "
            "damage healthy DNA, so no healthy tissue anywhere is put at risk "
            "by it",
            "Patients receive their dose slowly, so no cells are killed by it "
            "at any stage, which is why a course of treatment is spread over "
            "weeks",
            "A patient's cells repair themselves faster than a worker's cells "
            "do, because of the drugs given alongside the treatment",
        ],
        "correct_index": 0,
        "why": "Medical use of radiation is always a benefit-against-risk "
               "judgement: here the benefit is destroying cancer cells, and "
               "the risk is managed rather than removed.",
    },
    {
        "id": "ks4-radioactive-contamination-h19",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A worker inhales a quantity of an alpha emitter that the body "
                "clears within two days. A colleague inhales the same "
                "quantity of an alpha emitter the body retains for years. "
                "Compare the total doses they receive.",
        "options": [
            "They receive the same dose, because the same quantity was inhaled "
            "in each case, however long each of them keeps the material inside",
            "The first receives more, because material still in the lungs is "
            "shielded by the surrounding tissue in the first place",
            "The second receives more, because the source stays in his tissue "
            "and keeps depositing energy there",
            "Neither receives a dose, because alpha particles cannot travel "
            "far enough to leave the lungs, however long the material stays "
            "where it settled",
        ],
        "correct_index": 2,
        "why": "An internal source delivers dose for as long as it stays in "
               "the body, so a contaminant that is retained is far worse than "
               "an identical one that is cleared.",
    },
    {
        "id": "ks4-radioactive-contamination-h20",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why holding a sealed beta source in the hand for a "
                "minute is less serious than swallowing the same source's "
                "contents.",
        "options": [
            "Beta particles cannot pass through skin, so nothing reaches the "
            "body from outside",
            "The stomach concentrates beta particles, which makes them more "
            "ionising than they were",
            "Swallowing places the source inside, where it irradiates soft "
            "organs continuously until it is cleared or decays",
            "Holding a source is irradiation, and irradiation cannot damage "
            "cells at any dose",
        ],
        "correct_index": 2,
        "why": "Held in the hand the exposure is brief and mostly to skin; "
               "swallowed, the source travels with the person and delivers "
               "its energy straight into soft tissue.",
    },
    {
        "id": "ks4-radioactive-contamination-h21",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a worker who has been irradiated needs no "
                "decontamination while one who has been contaminated does.",
        "options": [
            "Decontamination works only on people, and irradiation is a "
            "property of the room rather than the person, not of anything "
            "carried on the worker's body",
            "Irradiation leaves nothing on or in the worker to be removed, "
            "whereas contamination leaves material that must be washed off",
            "An irradiated worker has already lost all the energy they "
            "absorbed, so washing them afterwards would only add to the dose "
            "already recorded on their badge",
            "Contamination passes into the bloodstream within the first "
            "minute, so washing the skin afterwards makes almost no "
            "difference to the dose received",
        ],
        "correct_index": 1,
        "why": "Decontamination removes radioactive material, and only the "
               "contaminated worker has any on or in them.",
    },
    {
        "id": "ks4-radioactive-contamination-h22",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Three precautions are used in a laboratory: a lead screen, a "
                "fume cupboard and a pair of tongs. Determine which of them "
                "reduces the dose from irradiation without reducing "
                "contamination risk.",
        "options": [
            "The fume cupboard, because moving air carries radiation away from "
            "the bench before it can reach the worker standing at it",
            "The tongs, because they remove radioactive dust from the "
            "worker's fingers",
            "None of them, because each of the three reduces both hazards "
            "equally",
            "The lead screen, because it absorbs radiation but does nothing "
            "about radioactive material",
        ],
        "correct_index": 3,
        "why": "Shielding is purely an irradiation control; the fume cupboard "
               "prevents inhalation and the tongs prevent contact, so both of "
               "those work on contamination as well.",
    },
    {
        "id": "ks4-radioactive-contamination-h23",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a radiation worker who has never "
                "exceeded the annual dose limit has taken on no extra risk at "
                "all.",
        "options": [
            "It is correct, because the limit is set at the level below which "
            "radiation does nothing to cells",
            "It is correct, because dose received below a legal limit is not "
            "recorded on the dosimeter",
            "It is wrong, because a limit keeps the additional risk small and "
            "acceptable rather than reducing it to nothing",
            "It is wrong, because the annual limit applies to contamination "
            "only and not to irradiation",
        ],
        "correct_index": 2,
        "why": "Dose limits manage risk to a level judged acceptable; any "
               "extra dose carries some extra probability of DNA damage.",
    },
    {
        "id": "ks4-radioactive-contamination-h24",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plan for handling an unsealed gamma emitter lists gloves, a "
                "laboratory coat and a ventilated cabinet. Suggest the "
                "important control that is missing.",
        "options": [
            "Dense shielding between the worker and the open source",
            "A second pair of gloves worn over the first",
            "A cooling system to keep the cabinet below room temperature",
            "A change from a gamma emitter to an alpha emitter of the same "
            "activity",
        ],
        "correct_index": 0,
        "why": "Every listed control guards against contamination; nothing on "
               "the list reduces the irradiation from a penetrating gamma "
               "emitter, which needs lead or concrete.",
    },
    {
        "id": "ks4-radioactive-contamination-h25",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two houses stand on the same contaminated ground. In one the "
                "topsoil is dug out and taken away; in the other a concrete "
                "slab is poured over it. Compare the two approaches.",
        "options": [
            "The concrete is better, because it shields the house and leaves "
            "the ground undisturbed, so the dose rate indoors drops away to "
            "nothing",
            "The two are equivalent, because both leave the family's dose rate "
            "unchanged",
            "Digging out the soil is better, because it removes the source, "
            "while concrete only shields material that is still there",
            "Digging out the soil is worse, because disturbed soil becomes "
            "more radioactive than settled soil, releasing far more radiation "
            "than it held before",
        ],
        "correct_index": 2,
        "why": "Removing the contaminated soil is decontamination and ends "
               "the hazard; a slab reduces the dose while the material and "
               "its future risks remain beneath it.",
    },
    {
        "id": "ks4-radioactive-contamination-h26",
        "subtopic_slug": "radioactive-contamination",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A school stores its alpha, beta and gamma sources together in "
                "one lead-lined box. Explain why the box is designed around "
                "the gamma source rather than the other two.",
        "options": [
            "Gamma sources have the highest activity of the three, whatever "
            "material is used",
            "Alpha and beta sources lose their activity while in storage, so "
            "they need no shielding",
            "Gamma is the most penetrating, so shielding thick enough for it "
            "is more than enough for the others",
            "Lead reacts with alpha and beta sources, so the box must be "
            "sized to keep them apart",
        ],
        "correct_index": 2,
        "why": "Shielding is designed for the worst case: lead thick enough "
               "to absorb most gamma stops alpha and beta many times over.",
    },
]
