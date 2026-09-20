"""Physics · Atomic structure — the MRB-338 expansion of `radioactive-decay`.

One leaf only: AQA 8463 §6.4.2.1 — what alpha, beta and gamma each ARE, the
charge and mass each carries, its range in air, what absorbs it, how strongly it
ionises, how a field deflects it, the becquerel and the count rate, the
randomness and spontaneity of decay, and the hazard of each radiation inside
and outside the body. The original twelve rows in `atomic_structure__a.py` take
alpha's composition and range, gamma's charge, the becquerel, the minute-to-
minute variation, the paper-then-aluminium identification, why gamma penetrates,
the sterilisation example, the lead box, the alpha-in-the-hand comparison, count
rate against activity, and the background correction; this file takes what they
leave — beta's composition, charge and range, gamma as an electromagnetic wave,
the ionising and penetrating orders in full, the absorber for each, deflection
in electric and magnetic fields, spontaneity, the three protections, and the
arithmetic of decays per second against counts per minute.

⚠️ **The named APPLICATIONS are deliberately not here.** Smoke detectors,
thickness gauges, tracers, sterilisation and pipeline testing belong to
`uses-of-nuclear-radiation`, a separate leaf of this topic with its own quota.
A row asking which radiation suits which job would be that leaf's question
wearing this leaf's slug, and brief §9.4 measures duplicates across the whole
topic. What this leaf asks instead is the PROPERTY — the charge, the range, the
absorber — from which such a choice would follow.

The weight follows the CONTENT. `easier` stays at eight: recall here is three
compositions, three charges, three absorbers and one unit. The demand lives in
`standard` and `harder`, where a radiation has to be identified from what
absorbs it or from which way a field bends it, or a count corrected and
converted — so that is where the twenty-two-row bands sit.

Every wrong option carries its own FALSE reason at the key's level of detail
(brief §9.2/§9.9). ⚠️ Radiation hazard is stated as AQA states it — ionisation
of cells, damage to DNA, an increased risk of cancer, radiation sickness at
high dose — and never exaggerated to sharpen a distractor.
"""

TOPIC = "atomic-structure"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # Beta and gamma as the first twelve never ask them, plus the two orders
    # and the one unit.
    {
        "id": "ks4-radioactive-decay-e05",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a beta particle is.",
        "options": [
            "A helium nucleus made of two protons and two neutrons",
            "A fast-moving electron emitted from the nucleus",
            "A high-energy electromagnetic wave with no mass at all",
            "A neutron travelling at close to the speed of light",
        ],
        "correct_index": 1,
        "why": "A beta particle is an electron thrown out of the nucleus when "
               "a neutron there turns into a proton.",
    },
    {
        "id": "ks4-radioactive-decay-e06",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the charge carried by a beta particle.",
        "options": [
            "−2",
            "0",
            "+1",
            "−1",
        ],
        "correct_index": 3,
        "why": "A beta particle is an electron, so it carries a charge of −1.",
    },
    {
        "id": "ks4-radioactive-decay-e07",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what gamma radiation is made of.",
        "options": [
            "A high-energy electromagnetic wave",
            "Two protons together with two neutrons",
            "A stream of fast-moving electrons from the nucleus",
            "A stream of uncharged neutrons from the nucleus",
        ],
        "correct_index": 0,
        "why": "Gamma is not a particle at all but electromagnetic radiation "
               "of very short wavelength, carrying no charge and no mass.",
    },
    {
        "id": "ks4-radioactive-decay-e08",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which of the three nuclear radiations is the most "
                "strongly ionising.",
        "options": [
            "Gamma, because it travels the furthest of the three through the "
                "air around it",
            "Beta, because it sits between the other two in every one of its "
                "other properties",
            "Alpha",
            "All three of them ionise equally strongly",
        ],
        "correct_index": 2,
        "why": "Alpha carries a charge of +2 and a large mass, so it "
               "produces far more ion pairs per centimetre than the others.",
    },
    {
        "id": "ks4-radioactive-decay-e09",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Of alpha, beta and gamma, state which needs the thickest "
                "absorber to stop it.",
        "options": [
            "Alpha, because it is the heaviest of the three and so drives "
                "furthest into a material",
            "Beta, because a light particle slips between the atoms of a "
                "material more easily than a wave",
            "All three penetrate to the same depth in a given material",
            "Gamma",
        ],
        "correct_index": 3,
        "why": "Gamma has no charge and no mass, so it ionises only rarely "
               "and gives up its energy slowly, reaching much further in.",
    },
    {
        "id": "ks4-radioactive-decay-e10",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what thickness of which material is needed to stop "
                "beta radiation.",
        "options": [
            "A single sheet of paper",
            "A few millimetres of aluminium",
            "Several centimetres of lead",
            "Several metres of concrete",
        ],
        "correct_index": 1,
        "why": "Beta passes through paper but is absorbed by a few "
               "millimetres of aluminium.",
    },
    {
        "id": "ks4-radioactive-decay-e11",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the number of decays per second that an activity of "
                "1 Bq represents.",
        "options": [
            "60",
            "100",
            "1000",
            "1",
        ],
        "correct_index": 3,
        "why": "One becquerel is defined as one decay per second.",
    },
    {
        "id": "ks4-radioactive-decay-e12",
        "subtopic_slug": "radioactive-decay",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the instrument commonly used in a school laboratory to "
                "detect nuclear radiation.",
        "options": [
            "A Geiger–Müller tube",
            "An ammeter",
            "A thermistor",
            "An oscilloscope",
        ],
        "correct_index": 0,
        "why": "A Geiger–Müller tube connected to a counter registers each "
               "ionising particle or photon that enters it.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Identify a radiation from its absorber or its deflection; convert and
    # correct a count.
    {
        "id": "ks4-radioactive-decay-s05",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the range of beta radiation in air with the range of "
                "alpha radiation in air.",
        "options": [
            "Beta a few centimetres against alpha a few metres, since the "
                "heavier particle carries further through the air",
            "Beta a few metres against alpha a few centimetres",
            "Both of them travel a few centimetres, because both are "
                "particles rather than waves",
            "Both of them travel effectively without limit, because neither "
                "is absorbed by air at all",
        ],
        "correct_index": 1,
        "why": "Beta ionises less strongly than alpha, so it loses its energy "
               "more slowly and reaches metres rather than centimetres.",
    },
    {
        "id": "ks4-radioactive-decay-s06",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what is meant by saying that radioactive decay is "
                "spontaneous.",
        "options": [
            "That it happens at the same steady rate in every source, "
                "whatever isotope that source happens to be made of",
            "That it happens only once a nucleus has been heated enough for "
                "its particles to break apart",
            "That it happens the instant a nucleus is formed, so no unstable "
                "nucleus lasts any length of time",
            "That it happens without being triggered, and is unaffected by "
                "temperature, pressure or chemical state",
        ],
        "correct_index": 3,
        "why": "Nothing outside the nucleus starts a decay, and no change of "
               "temperature, pressure or chemistry alters its rate.",
    },
    {
        "id": "ks4-radioactive-decay-s07",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is needed to reduce the intensity of gamma "
                "radiation substantially.",
        "options": [
            "A sheet of paper, or a few centimetres of air",
            "A few millimetres of aluminium foil",
            "Several centimetres of lead, or metres of concrete",
            "A thin plastic sheet held close to the source",
        ],
        "correct_index": 2,
        "why": "Gamma is only weakly absorbed, so a thick, dense absorber "
               "such as lead or concrete is needed to cut it down.",
    },
    {
        "id": "ks4-radioactive-decay-s08",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the relative mass and the charge of an alpha "
                "particle.",
        "options": [
            "A mass of about 4 units and a charge of +2",
            "A mass of about 2 units and a charge of +4, one unit of charge "
                "for each of the particles in it",
            "A negligible mass and a charge of −1, in the same way as the "
                "electron it resembles",
            "A mass of about 4 units and no charge at all, its protons being "
                "cancelled by its neutrons",
        ],
        "correct_index": 0,
        "why": "Two protons and two neutrons give a mass of about 4 atomic "
               "mass units, and the two protons give a charge of +2.",
    },
    {
        "id": "ks4-radioactive-decay-s09",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why alpha radiation ionises far more strongly than "
                "gamma radiation does.",
        "options": [
            "Because an alpha particle travels much faster than gamma "
                "radiation and so meets more atoms in a second",
            "Because an alpha particle carries a charge of +2 and a large "
                "mass, so it interacts strongly with the atoms it passes",
            "Because gamma radiation is absorbed long before it can reach "
                "the atoms that it would otherwise have ionised along the way",
            "Because an alpha particle is small enough to enter a nucleus, "
                "which is where ionisation actually happens",
        ],
        "correct_index": 1,
        "why": "A large charge and a large mass mean strong interaction over "
               "a short path, so alpha strips electrons from many atoms "
               "quickly.",
    },
    {
        "id": "ks4-radioactive-decay-s10",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a magnetic field, a beam of radiation from a source is "
                "deflected in the opposite direction to a beam of beta "
                "particles. Determine which radiation the source emits.",
        "options": [
            "Gamma, because a wave is deflected the other way from a particle",
            "Beta as well, because two beta beams always repel one another "
                "and so separate as they travel",
            "Alpha, because its charge is positive while beta's is negative",
            "Neutrons, because an uncharged particle is pushed sideways by a "
                "magnetic field",
        ],
        "correct_index": 2,
        "why": "A magnetic field deflects opposite charges in opposite "
               "directions, and alpha is the positively charged radiation.",
    },
    {
        "id": "ks4-radioactive-decay-s11",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why gamma radiation passes through a magnetic field "
                "without being deflected.",
        "options": [
            "Because it travels too quickly for a magnetic field to be able "
                "to act on it during the crossing",
            "Because it is absorbed by the magnet itself before it can be "
                "deflected by the field around it",
            "Because its positive and negative parts are deflected equally "
                "and in opposite directions, cancelling out",
            "Because it carries no charge, and a magnetic field exerts a "
                "force only on moving charge",
        ],
        "correct_index": 3,
        "why": "Magnetic deflection acts on moving charges, and gamma "
               "radiation carries none.",
    },
    {
        "id": "ks4-radioactive-decay-s12",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Place the three nuclear radiations in order of ionising "
                "power, strongest first.",
        "options": [
            "Gamma, beta, alpha, in order of how far each one travels through "
                "the air before it stops",
            "Beta, alpha, gamma, with the middling radiation the strongest "
                "ioniser of the three",
            "Alpha, beta, gamma",
            "All three ionise equally, since each carries the same energy "
                "away from the nucleus",
        ],
        "correct_index": 2,
        "why": "Ionising power falls as charge and mass fall, so the order is "
               "alpha, then beta, then gamma.",
    },
    {
        "id": "ks4-radioactive-decay-s13",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the order of alpha, beta and gamma by how deeply "
                "each travels into matter, deepest first.",
        "options": [
            "Gamma, beta, alpha",
            "Alpha, beta, gamma, in the same order as their ionising power "
                "runs",
            "Beta, gamma, alpha, since a light particle gets furthest of the "
                "three into a solid",
            "All three penetrate equally, the absorber used making the only "
                "difference between them",
        ],
        "correct_index": 0,
        "why": "Penetration runs opposite to ionisation: the weakest ioniser, "
               "gamma, travels furthest before its energy is absorbed.",
    },
    {
        "id": "ks4-radioactive-decay-s14",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A detector's count rate near a source drops to the "
                "background level as soon as a single sheet of paper is put "
                "in the way. Determine which radiation the source emits.",
        "options": [
            "Gamma only, since paper absorbs an electromagnetic wave far "
                "more readily than it absorbs a particle",
            "Alpha only",
            "Beta only, since a few millimetres of any solid material is "
                "enough to stop it completely",
            "A mixture of beta and gamma, because two radiations are needed "
                "before paper has any effect",
        ],
        "correct_index": 1,
        "why": "Only alpha is stopped by something as thin as paper; beta "
               "needs millimetres of aluminium and gamma much more.",
    },
    {
        "id": "ks4-radioactive-decay-s15",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why alpha radiation is a far greater hazard inside "
                "the body than outside it.",
        "options": [
            "Because alpha radiation is only produced once a source has been "
                "swallowed and has reached the warmth of the body",
            "Because inside the body there is no skin in the way, so the "
                "strongly ionising alpha gives all its energy to living "
                "cells nearby",
            "Because alpha radiation becomes very much more penetrating once "
                "it finds itself surrounded by tissue rather than by air",
            "Because outside the body alpha radiation is deflected away by "
                "the body's own electric charge",
        ],
        "correct_index": 1,
        "why": "Outside, dead skin absorbs alpha; inside, its very short "
               "range means every ionisation happens in living tissue.",
    },
    {
        "id": "ks4-radioactive-decay-s16",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why gamma radiation from a source across the room is "
                "a greater hazard than alpha radiation from the same "
                "distance.",
        "options": [
            "Because gamma ionises very much more strongly than alpha does "
                "at any distance at all from the source",
            "Because gamma is attracted towards a person's body, whereas "
                "alpha is repelled away from it",
            "Because alpha radiation is emitted only in short bursts and "
                "gamma radiation is emitted steadily",
            "Because gamma penetrates skin and reaches internal organs, "
                "while alpha does not even cross the air between",
        ],
        "correct_index": 3,
        "why": "Alpha's range in air is a few centimetres and skin stops what "
               "reaches it, whereas gamma travels across a room and into "
               "tissue.",
    },
    {
        "id": "ks4-radioactive-decay-s17",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the count rate recorded by a detector falls as "
                "the detector is moved further from a gamma source.",
        "options": [
            "Because the source decays more slowly once the detector has "
                "been moved away from it",
            "Because the radiation spreads out over a larger area, so less "
                "of it enters the detector's window",
            "Because gamma radiation loses its charge steadily as it travels "
                "further from the source",
            "Because the air between absorbs almost all of the gamma "
                "radiation within the first few centimetres",
        ],
        "correct_index": 1,
        "why": "The same emitted radiation is spread over an ever larger "
               "area, so a fixed detector window intercepts a smaller share "
               "of it.",
    },
    {
        "id": "ks4-radioactive-decay-s18",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the activity of a radioactive source falls as "
                "time passes.",
        "options": [
            "Because the nuclei that are left become steadily more stable "
                "and so decay more slowly than they did",
            "Because the radiation already emitted is reabsorbed by the "
                "source and slows the remaining decays down",
            "Because fewer undecayed nuclei are left, so fewer decays happen "
                "in each second",
            "Because the source cools as it decays, and a cooler source "
                "always decays at a lower rate",
        ],
        "correct_index": 2,
        "why": "Activity depends on how many unstable nuclei remain, and that "
               "number falls with every decay.",
    },
    {
        "id": "ks4-radioactive-decay-s19",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the three ways in which a worker can reduce the dose "
                "received from an external radioactive source.",
        "options": [
            "Increase the distance, reduce the time, and use shielding",
            "Increase the time, reduce the distance, and remove all "
                "shielding so that the radiation can escape",
            "Cool the source, seal the source, and reduce its activity by "
                "handling it as little as possible",
            "Wear gloves, work quickly, and keep the source in a "
                "well-ventilated part of the room",
        ],
        "correct_index": 0,
        "why": "Dose from an external source falls with greater distance, "
               "less exposure time and suitable absorbing material in "
               "between.",
    },
    {
        "id": "ks4-radioactive-decay-s20",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source has an activity of 240 Bq. Calculate the number of "
                "nuclei in it that decay in one minute.",
        "options": [
            "240",
            "4",
            "14 400",
            "240 000",
        ],
        "correct_index": 2,
        "why": "240 decays per second × 60 seconds = 14 400 decays in a "
               "minute.",
    },
    {
        "id": "ks4-radioactive-decay-s21",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A detector records 900 counts in 5.0 minutes. Calculate the "
                "count rate in counts per minute.",
        "options": [
            "4500 counts per minute",
            "15 counts per minute",
            "900 counts per minute",
            "180 counts per minute",
        ],
        "correct_index": 3,
        "why": "900 ÷ 5.0 = 180 counts per minute.",
    },
    {
        "id": "ks4-radioactive-decay-s22",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a student who measures the count rate from one "
                "source five times gets five slightly different answers.",
        "options": [
            "Because the detector becomes steadily less sensitive each time "
                "it is switched on and used again",
            "Because the activity of the source rises and falls in a regular "
                "cycle through the course of a lesson",
            "Because decay is random, so the number of nuclei decaying in "
                "any given interval varies by chance",
            "Because each reading includes a different amount of background, "
                "which the tube adds on at random",
        ],
        "correct_index": 2,
        "why": "Which nucleus decays next is a matter of chance, so equal "
               "intervals do not contain equal numbers of decays.",
    },
    {
        "id": "ks4-radioactive-decay-s23",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to an unstable nucleus when it emits "
                "radiation.",
        "options": [
            "It gains extra particles from its surroundings and grows "
                "heavier than it was",
            "It becomes more stable than it was before",
            "It stays exactly as it was, the radiation having come from the "
                "electron shells instead",
            "It breaks apart completely, leaving nothing behind but the "
                "radiation it emitted",
        ],
        "correct_index": 1,
        "why": "A nucleus emits radiation precisely in order to reach a more "
               "stable arrangement of its particles.",
    },
    {
        "id": "ks4-radioactive-decay-s24",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a sheet of paper protects a worker from alpha "
                "radiation but gives almost no protection from beta.",
        "options": [
            "Alpha ionises so strongly that it gives up all its energy "
                "within the paper, while beta ionises weakly and passes "
                "through",
            "Alpha is attracted to the paper and sticks fast to its surface, "
                "while beta is repelled away from it and carries straight on",
            "Alpha is an electromagnetic wave, which paper reflects, while "
                "beta is a particle and cannot be reflected",
            "Alpha travels much faster than beta, so the paper has more "
                "time in which to absorb it as it crosses",
        ],
        "correct_index": 0,
        "why": "The strongly ionising alpha loses its energy over a very "
               "short path, so even paper absorbs it, whereas beta needs "
               "millimetres of aluminium.",
    },
    {
        "id": "ks4-radioactive-decay-s25",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the activity of a source can be quoted as a "
                "definite number even though nobody can say when any one "
                "nucleus will decay.",
        "options": [
            "Because the activity quoted is only ever a rough guess, with no "
                "measurement behind it at all",
            "Because the nuclei of the sample take it in turn to decay, in "
                "an order that was fixed at the moment the source was made",
            "Because the first nucleus to decay sets the rate that all the "
                "others afterwards follow",
            "Because a large sample contains so many nuclei that the average "
                "rate of decay is predictable even though each decay is not",
        ],
        "correct_index": 3,
        "why": "Randomness in individual events averages out over very large "
               "numbers, in the same way as the proportion of heads in many "
               "coin tosses.",
    },
    {
        "id": "ks4-radioactive-decay-s26",
        "subtopic_slug": "radioactive-decay",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why alpha radiation has a much shorter range in air "
                "than gamma radiation.",
        "options": [
            "Alpha is absorbed by the oxygen of the air, while gamma is "
                "absorbed only by the nitrogen in it",
            "Alpha is slower than gamma, so the air has very much longer in "
                "which to bring it to a stop as it travels",
            "Alpha ionises the air strongly, losing its energy over a few "
                "centimetres, while gamma ionises only rarely",
            "Alpha is pulled downwards by gravity, so its path through the "
                "air is much the shorter of the two",
        ],
        "correct_index": 2,
        "why": "Every ionisation costs the alpha particle energy, and it "
               "makes so many per centimetre that it stops within a few of "
               "them.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Identification from combined evidence, corrected counts, and the hazard
    # comparisons that turn on WHERE the source is.
    {
        "id": "ks4-radioactive-decay-h05",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A beam of radiation crosses an electric field without being "
                "deflected at all, and is then stopped only by a thick lead "
                "block. Determine which radiation it is and justify your "
                "answer.",
        "options": [
            "Alpha, because its two charges cancel each other out and lead "
                "is the only absorber strong enough to hold it",
            "Beta, because an electron is far too light to be deflected "
                "measurably and lead is what stops it",
            "Gamma, because it carries no charge to be deflected and it is "
                "the only radiation needing lead",
            "A mixture of alpha and beta, whose opposite deflections cancel, "
                "and both are absorbed by the lead",
        ],
        "correct_index": 2,
        "why": "No deflection means no charge, and needing thick lead means "
               "high penetration; only gamma has both properties.",
    },
    {
        "id": "ks4-radioactive-decay-h06",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two sealed sources sit 50 cm from a detector. One gives a "
                "reading no higher than background and the other gives a "
                "high count rate. Determine which radiation each emits.",
        "options": [
            "The background one emits alpha, whose range in air is only a "
                "few centimetres; the other emits gamma",
            "The background one emits gamma, which is absorbed completely by "
                "50 cm of air; the other emits alpha",
            "Both of them emit gamma, and the first source has simply run "
                "out of nuclei left to decay",
            "The background one emits beta, which cannot travel more than a "
                "few centimetres through air at all",
        ],
        "correct_index": 0,
        "why": "Alpha cannot cross 50 cm of air, so it reads as background at "
               "that distance, whereas gamma crosses it easily.",
    },
    {
        "id": "ks4-radioactive-decay-h07",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the radiation that ionises most strongly is also "
                "the radiation that penetrates least.",
        "options": [
            "Because a strongly ionising radiation is always emitted with "
                "much less energy than a weakly ionising one is",
            "Because each ionisation takes energy from the radiation, so the "
                "more it ionises the sooner it runs out of energy",
            "Because a strongly ionising radiation is pulled back towards "
                "the source by the ions it has just created",
            "Because ionisation and penetration are unrelated, and the "
                "pattern is no more than a coincidence",
        ],
        "correct_index": 1,
        "why": "Ionising costs energy, so heavy ionisation empties the "
               "radiation's energy over a short path and stops it sooner.",
    },
    {
        "id": "ks4-radioactive-decay-h08",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alpha particle has about 7300 times the mass of a beta "
                "particle. Predict how the deflections of the two compare in "
                "the same magnetic field.",
        "options": [
            "Alpha is deflected far more, because a charge of +2 is twice as "
                "large as a charge of −1",
            "Both of them are deflected by the same amount, because the "
                "field acting on each is the same",
            "Neither of them is deflected, because a magnetic field can only "
                "act on radiation that is a wave",
            "Beta is deflected far more, because the same size of force acts "
                "on a very much smaller mass",
        ],
        "correct_index": 3,
        "why": "A similar magnetic force acting on a mass thousands of times "
               "smaller produces a very much larger change of direction.",
    },
    {
        "id": "ks4-radioactive-decay-h09",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A detector records 1200 counts in 4.0 minutes with a source "
                "in place and 60 counts in 4.0 minutes with the source "
                "removed. Calculate the corrected count rate of the source in "
                "counts per minute.",
        "options": [
            "285 counts per minute",
            "1140 counts per minute",
            "315 counts per minute",
            "300 counts per minute",
        ],
        "correct_index": 0,
        "why": "1200 ÷ 4.0 = 300 and 60 ÷ 4.0 = 15, so the corrected rate is "
               "300 − 15 = 285 counts per minute.",
    },
    {
        "id": "ks4-radioactive-decay-h10",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'A source kept in a lead-lined box "
                "for a year will have stopped decaying by the time it is "
                "taken out.'",
        "options": [
            "Sound — lead absorbs the radiation, and a source that is unable "
                "to emit anything at all is no longer decaying either",
            "Sound — a year is long enough for any school source to have "
                "used up every unstable nucleus it held",
            "Unsound — the lead absorbs the radiation once it has left the "
                "source, but the nuclei inside go on decaying as before",
            "Unsound — being shut in lead in fact makes a source decay "
                "faster than it would in the open",
        ],
        "correct_index": 2,
        "why": "Decay is spontaneous and nothing outside the nucleus alters "
               "it; the shielding changes only what escapes the box.",
    },
    {
        "id": "ks4-radioactive-decay-h11",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a sealed alpha source may be stored on an open "
                "shelf while an unsealed alpha powder may not.",
        "options": [
            "A sealed source keeps the material where it is, whereas loose "
                "powder can be inhaled or swallowed and then irradiates tissue "
                "from inside",
            "A sealed source emits no radiation at all, whereas an unsealed "
                "powder emits it continuously into the room",
            "A sealed source has a very much shorter half-life than a loose "
                "powder, so it becomes safe within a few days of being sealed up",
            "A sealed source emits gamma instead of alpha, and gamma is the "
                "safer of the two at a distance",
        ],
        "correct_index": 0,
        "why": "The hazard from alpha is internal, so the precaution that "
               "matters is preventing the material itself from entering the "
               "body.",
    },
    {
        "id": "ks4-radioactive-decay-h12",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which of the three nuclear radiations could still "
                "be detected after passing through a 2 cm steel plate, and "
                "explain why.",
        "options": [
            "Alpha, because its large mass carries it through a solid more "
                "easily than a lighter radiation",
            "Beta, because a few millimetres of metal slow it without "
                "absorbing it completely",
            "Gamma, because it is only weakly absorbed and needs a thick, "
                "dense absorber to cut it down",
            "None of the three, because steel of that thickness absorbs "
                "every kind of nuclear radiation",
        ],
        "correct_index": 2,
        "why": "Alpha stops at paper and beta at a few millimetres of "
               "aluminium, so only gamma survives 2 cm of steel.",
    },
    {
        "id": "ks4-radioactive-decay-h13",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a detector in a laboratory never reads zero, "
                "even with every source locked away.",
        "options": [
            "Because the tube keeps counting the last source it was used "
                "with for some while afterwards",
            "Because ionising radiation from rocks, the air, food and space "
                "is present everywhere at all times",
            "Because a Geiger–Müller tube produces a steady count of its own "
                "whether or not any radiation enters it",
            "Because the locked sources continue to irradiate the room right "
                "through the walls of their container",
        ],
        "correct_index": 1,
        "why": "Background radiation from natural and artificial sources is "
               "always present, so some counts are always recorded.",
    },
    {
        "id": "ks4-radioactive-decay-h14",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source emits both beta and gamma radiation. Predict what "
                "happens to the count rate when a 5 mm aluminium sheet is "
                "placed between the source and the detector.",
        "options": [
            "It falls but stays well above background, because the beta is "
                "absorbed and the gamma passes through",
            "It falls to the background level, because aluminium absorbs "
                "both of the radiations completely",
            "It stays exactly the same, because aluminium absorbs neither "
                "beta nor gamma to any degree",
            "It rises, because the aluminium becomes a source of its own "
                "once the beta has been absorbed in it",
        ],
        "correct_index": 0,
        "why": "5 mm of aluminium stops beta but hardly touches gamma, so the "
               "reading drops by the beta contribution only.",
    },
    {
        "id": "ks4-radioactive-decay-h15",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two sealed sources of equal activity are held 1 m away, one "
                "emitting alpha and one emitting gamma. Compare the hazard "
                "each presents at that distance.",
        "options": [
            "The alpha source is the greater hazard, because alpha is the "
                "most strongly ionising of the radiations",
            "Both present exactly the same hazard, because their activities "
                "are equal and activity is the only thing dose depends on",
            "The gamma source is the greater hazard, because alpha cannot "
                "cross a metre of air while gamma reaches the body",
            "Neither presents any hazard, because a sealed source cannot "
                "emit radiation through its own container",
        ],
        "correct_index": 2,
        "why": "Alpha's few-centimetre range in air means none of it arrives, "
               "while gamma crosses the metre and penetrates tissue.",
    },
    {
        "id": "ks4-radioactive-decay-h16",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why counting for ten minutes gives a better estimate "
                "of a source's count rate than counting for ten seconds.",
        "options": [
            "Because the detector needs several minutes of use before it "
                "begins to register any radiation at all",
            "Because the source's activity settles to a steady value only "
                "after it has been near a detector for some minutes",
            "Because a longer count records many more decays, so the random "
                "variation matters less as a proportion of the total",
            "Because a ten-second count misses the decays that happen "
                "between one second and the next",
        ],
        "correct_index": 2,
        "why": "Chance variation is a smaller fraction of a large total, so a "
               "longer count gives a more reliable average rate.",
    },
    {
        "id": "ks4-radioactive-decay-h17",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A radioactive sample is decaying at 8000 Bq. Determine how "
                "many of its nuclei break down over 2.0 minutes.",
        "options": [
            "16 000",
            "960 000",
            "480 000",
            "133",
        ],
        "correct_index": 1,
        "why": "8000 decays per second × 120 s = 960 000 decays.",
    },
    {
        "id": "ks4-radioactive-decay-h18",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'Alpha radiation is harmless, "
                "because a sheet of paper is enough to stop it.'",
        "options": [
            "Unsound — paper and skin do stop it from outside, but an alpha "
                "emitter taken into the body damages cells severely",
            "Sound — a radiation that paper can stop cannot reach anything "
                "living and so does no damage",
            "Unsound — paper does not in fact stop alpha radiation, which "
                "needs several centimetres of lead",
            "Sound — alpha radiation does not ionise anything at all, so "
                "even where it is absorbed there is nothing to be harmed by it",
        ],
        "correct_index": 0,
        "why": "The short range that makes alpha harmless outside the body is "
               "exactly what makes it dangerous inside it, where all its "
               "energy is given to nearby living cells.",
    },
    {
        "id": "ks4-radioactive-decay-h19",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why moving twice as far from a gamma source reduces "
                "the dose received in a given time.",
        "options": [
            "The radiation emitted is spread over a much larger area, so far "
                "less of it passes through the body",
            "The source emits less radiation altogether once nobody is "
                "standing close beside it",
            "The gamma radiation loses half of its own energy for every "
                "metre of air that it has to cross on the way",
            "The radiation is bent away from the body by the air, and more "
                "air means more bending",
        ],
        "correct_index": 0,
        "why": "The same emitted radiation spreads over a larger area with "
               "distance, so a body at that distance intercepts a smaller "
               "share of it.",
    },
    {
        "id": "ks4-radioactive-decay-h20",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source's count rate is reduced but not removed by a sheet "
                "of paper, and falls to background behind 3 mm of aluminium. "
                "Determine which radiations it emits.",
        "options": [
            "Gamma only, since gamma is the only radiation able to pass "
                "through a sheet of paper at all",
            "Beta and gamma, since the aluminium removed the beta and the "
                "paper removed the gamma",
            "Alpha and beta",
            "Alpha only, since alpha is partly absorbed by paper and "
                "completely absorbed by aluminium",
        ],
        "correct_index": 2,
        "why": "The paper removing part of the count means alpha is present, "
               "and nothing surviving 3 mm of aluminium rules gamma out, so "
               "the rest is beta.",
    },
    {
        "id": "ks4-radioactive-decay-h21",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a technician uses long-handled tongs to move a "
                "gamma source even though a lead screen is already in place.",
        "options": [
            "Because the tongs absorb the gamma radiation before it can "
                "reach the technician's hand at all",
            "Because the lead screen only works while the source is not "
                "being moved from one place to another",
            "Because distance reduces the dose, and tongs keep the source "
                "much further from the body than a hand would",
            "Because handling a source directly would leave the technician's "
                "own hand radioactive from that point onwards",
        ],
        "correct_index": 2,
        "why": "Intensity falls with distance, so holding the source at "
               "arm's length through tongs cuts the dose to the hands and "
               "body.",
    },
    {
        "id": "ks4-radioactive-decay-h22",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the energy an alpha particle gives up per centimetre "
                "of its path with the energy a gamma photon gives up per "
                "centimetre.",
        "options": [
            "Alpha gives up much more per centimetre, which is why its whole "
                "path is only a few centimetres long",
            "Gamma gives up much more per centimetre, which is why it needs "
                "lead to absorb it in the end",
            "Both give up the same amount per centimetre, the difference "
                "being only in how much energy each started with",
            "Neither gives up any energy until the very end of its path, "
                "where both stop abruptly",
        ],
        "correct_index": 0,
        "why": "Alpha ionises heavily and so spends its energy over a very "
               "short distance; gamma ionises rarely and travels much "
               "further.",
    },
    {
        "id": "ks4-radioactive-decay-h23",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why some nuclei emit radiation while others never do.",
        "options": [
            "Some nuclei have an unstable combination of protons and "
                "neutrons, and emitting radiation takes them to a more stable "
                "one",
            "Only nuclei that have already been struck by radiation from "
                "elsewhere are able to emit any of their own",
            "Only the nuclei of the heaviest elements are able to emit "
                "radiation, and the light ones never can",
            "Every nucleus emits some radiation, but in most of them the "
                "rate is far too low for any detector at all to register it",
        ],
        "correct_index": 0,
        "why": "Radioactivity comes from an unstable balance of protons and "
               "neutrons, and a stable nucleus has no reason to change.",
    },
    {
        "id": "ks4-radioactive-decay-h24",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'The more penetrating a radiation is, "
                "the more dangerous it must be.'",
        "options": [
            "Sound — penetration is the only property that decides how much "
                "harm a radiation can do",
            "Unsound — it depends where the source is: gamma is the worse "
                "outside the body and alpha the worse inside it",
            "Sound — a radiation that penetrates further reaches a greater "
                "number of cells and so ionises more of them",
            "Unsound — the most penetrating radiation is in fact always the "
                "safest, whatever the circumstances",
        ],
        "correct_index": 1,
        "why": "Hazard depends on whether the radiation can reach living "
               "tissue and how strongly it ionises once there, so the answer "
               "changes with the source's position.",
    },
    {
        "id": "ks4-radioactive-decay-h25",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how ionising radiation causes harm to living cells.",
        "options": [
            "It heats the cells until the water inside them boils and the "
                "cells burst open",
            "It adds extra protons to the nucleus of every cell it passes "
                "through on its way",
            "It dissolves the membrane around each of the cells, letting the "
                "contents of the cell leak away",
            "It removes electrons from molecules in the cell, damaging DNA "
                "and raising the risk of cancer",
        ],
        "correct_index": 3,
        "why": "Ionisation damages molecules including DNA, which can cause "
               "mutations and an increased risk of cancer, and at high doses "
               "kills cells outright.",
    },
    {
        "id": "ks4-radioactive-decay-h26",
        "subtopic_slug": "radioactive-decay",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students measure the same gamma source with identical "
                "detectors but record different count rates. Suggest the most "
                "likely reason.",
        "options": [
            "One of the two sources has a different activity from the other "
                "one, even though it is the same source",
            "Gamma radiation cannot be measured with a Geiger–Müller tube, "
                "so both readings are meaningless",
            "One detector was held further from the source than the other, "
                "so less radiation entered its window",
            "One student measured for a longer time, and a longer count "
                "always gives a higher rate per minute",
        ],
        "correct_index": 2,
        "why": "Count rate depends on what fraction of the emitted radiation "
               "enters the detector, which falls off as the detector is "
               "moved away.",
    },
]
