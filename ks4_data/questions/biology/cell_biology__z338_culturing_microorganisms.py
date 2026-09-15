"""Biology · Cell biology — the MRB-338 expansion of `culturing-microorganisms`.

One leaf only: AQA 8461 §4.1.2, Triple-only, and every row here is flagged as
such. The original twelve rows in `cell_biology.py` take agar as the seaweed
gel, the autoclave temperature, the nitrogen source for protein synthesis, the
meaning of no clear zone, the lid lifted briefly, the distilled-water control
disc, the doubling calculation, the flamed bottle neck, the area of a 20 mm
zone, the radius-squared relationship, the 37 °C decision judged, and the
fluffy contaminant growing through a zone.

This file takes what they leave: what culturing IS and why industry and
research do it, the carbon source beside the nitrogen source, the minerals and
vitamins, the autoclave as a piece of apparatus and why it beats boiling, the
red-hot loop before and after use, the rising hot air above a Bunsen, the tape,
the inverted dish, the incubation window, the antibiotic diffusing out of the
disc, what a plateful of differing colonies means, the antiseptic against the
antibiotic, and the arithmetic the zones need — radius from an area, mm² to
cm², a mean diameter carried through to an area, and the diameter-as-radius
error caught and corrected.

The weight is even at eighteen a band, and that is a content judgement rather
than arithmetic: this leaf is a required practical, so its recall is a genuinely
long list of apparatus, temperatures, times and reasons, and eighteen easier
rows are eighteen different things rather than one thing asked eighteen ways.
The demand then rises through the method — which variable, which control, what
a lawn is for — into evaluating a conclusion drawn from one plate, and the area
calculation carries the harder band's arithmetic.

The bacterial growth calculation is deliberately NOT expanded here. It is
Higher-only in AQA and the lesson's own material does not carry it; the single
existing row that uses it stays as it is.
"""

TOPIC = "cell-biology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # What culturing is, the carbon source, the autoclave as apparatus, the
    # red-hot loop, the school incubation temperature, what a zone is and
    # what its size means, the area equation, a food, the tape, the meaning
    # of contamination, the Bunsen's rising air, the incubation window, and
    # the process that carries the antibiotic out of the disc.
    {
        "id": "ks4-culturing-microorganisms-e05",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by culturing microorganisms.",
        "options": [
            "Growing them in controlled laboratory conditions so that they can be studied",
            "Killing them off with an antibiotic so that they can then be counted under a microscope",
            "Staining them so that the structures inside each cell can be seen clearly",
            "Sorting them into groups according to the shape of the colony each forms",
        ],
        "correct_index": 0,
        "why": "Culturing means growing a population of microorganisms under "
               "controlled conditions in the laboratory.",
    },
    {
        "id": "ks4-culturing-microorganisms-e06",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the nutrient that a culture medium supplies as an "
                "energy source for bacteria.",
        "options": [
            "Agar, the gel the nutrients are dissolved in",
            "A carbon source, such as glucose",
            "Oxygen, drawn in from the air above the plate",
            "Vitamin C, added in very small amounts",
        ],
        "correct_index": 1,
        "why": "A sugar such as glucose is the carbon source, and respiring it "
               "releases the energy a bacterium needs in order to grow.",
    },
    {
        "id": "ks4-culturing-microorganisms-e07",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the piece of equipment that sterilises Petri dishes "
                "using steam under pressure.",
        "options": [
            "A centrifuge",
            "A water bath",
            "An autoclave",
            "An incubator",
        ],
        "correct_index": 2,
        "why": "An autoclave holds equipment in pressurised steam, which kills "
               "every microorganism on it, including bacterial spores.",
    },
    {
        "id": "ks4-culturing-microorganisms-e08",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how an inoculating loop is sterilised before it is "
                "used.",
        "options": [
            "It is rinsed in cold distilled water and then dried off",
            "It is wiped clean using a piece of dry filter paper",
            "It is dipped into the agar to coat it with nutrients",
            "It is held in a Bunsen flame until it glows red hot",
        ],
        "correct_index": 3,
        "why": "Heating the wire loop to red heat in a Bunsen flame destroys "
               "every microorganism on it.",
    },
    {
        "id": "ks4-culturing-microorganisms-e09",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the highest temperature at which bacteria are "
                "incubated in a school laboratory.",
        "options": [
            "25 °C",
            "37 °C",
            "45 °C",
            "30 °C",
        ],
        "correct_index": 0,
        "why": "School cultures are kept at no more than 25 °C, which "
               "discourages the growth of organisms suited to the human body.",
    },
    {
        "id": "ks4-culturing-microorganisms-e10",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what an inhibition zone on an agar plate is.",
        "options": [
            "A patch of mould that has landed on the plate out of the air",
            "A clear area around a disc in which the bacteria have not grown",
            "A cloudy ring around a disc in which the bacteria grew thickest",
            "The whole plate, once the antibiotic has spread right across it",
        ],
        "correct_index": 1,
        "why": "The antibiotic diffuses out of the disc and stops bacteria "
               "growing near it, leaving a clear zone with no colonies in it.",
    },
    {
        "id": "ks4-culturing-microorganisms-e11",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student compares two antibiotics on the same bacterial "
                "culture. Antibiotic X gives a 30 mm inhibition zone and "
                "antibiotic Y gives a 12 mm inhibition zone. State which "
                "antibiotic is more effective against this bacterium.",
        "options": [
            "Antibiotic Y, because a smaller zone means the antibiotic is more concentrated",
            "Neither can be judged, because zone size depends only on disc size",
            "Antibiotic X, because it stopped growth over a wider area",
            "Both are equally effective, because a zone formed around each disc",
        ],
        "correct_index": 2,
        "why": "A bigger clear zone means bacteria were stopped across a wider "
               "area, so antibiotic X is the more effective one against this "
               "bacterium.",
    },
    {
        "id": "ks4-culturing-microorganisms-e12",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the equation used to calculate the area of a circular "
                "inhibition zone.",
        "options": [
            "area = 2 × π × r",
            "area = π × d²",
            "area = π × r³",
            "area = π × r²",
        ],
        "correct_index": 3,
        "why": "An inhibition zone is a circle, so its area is π "
               "multiplied by the radius squared.",
    },
    {
        "id": "ks4-culturing-microorganisms-e13",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name one food that is produced using cultured "
                "microorganisms.",
        "options": [
            "Yoghurt",
            "Boiled rice",
            "Tinned peas",
            "Roast potatoes",
        ],
        "correct_index": 0,
        "why": "Bacteria are cultured on a large scale to turn milk into "
               "yoghurt, and other microorganisms are used to make bread and "
               "cheese.",
    },
    {
        "id": "ks4-culturing-microorganisms-e14",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why a Petri dish is sealed with tape once it has been "
                "inoculated.",
        "options": [
            "To stop the antibiotic discs floating off the agar surface",
            "To stop microorganisms in the air from getting in from outside",
            "To hold the agar down so that it cannot slide out of the dish",
            "To keep the dish warm enough for the bacteria inside to grow",
        ],
        "correct_index": 1,
        "why": "Tape keeps airborne microorganisms out, so any growth on the "
               "plate came from the culture that was deliberately added.",
    },
    {
        "id": "ks4-culturing-microorganisms-e15",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what it means to say that a culture has become "
                "contaminated.",
        "options": [
            "The antibiotic in it has spread out across the whole of the agar plate",
            "The agar has set too firmly for any bacteria to grow on it",
            "Unwanted microorganisms have got into it from outside",
            "The bacteria in it grew so well that the agar has run out",
        ],
        "correct_index": 2,
        "why": "Contamination is the arrival of microorganisms nobody put "
               "there, and it makes the result of the investigation "
               "unreliable.",
    },
    {
        "id": "ks4-culturing-microorganisms-e16",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why aseptic work is carried out close to a lit Bunsen "
                "burner.",
        "options": [
            "The light from the flame makes the colonies much easier to see",
            "The heat keeps the agar liquid so bacteria can be stirred in",
            "The flame uses up the oxygen, so no bacteria nearby can respire",
            "Rising hot air carries airborne microorganisms away from the work",
        ],
        "correct_index": 3,
        "why": "Hot air rises from the flame, so airborne contaminants are "
               "carried upwards and away from the open dish.",
    },
    {
        "id": "ks4-culturing-microorganisms-e17",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how long an inoculated agar plate is usually "
                "incubated for.",
        "options": [
            "24 to 48 hours",
            "5 to 10 minutes",
            "about three weeks",
            "exactly two hours",
        ],
        "correct_index": 0,
        "why": "A day or two at 25 °C is long enough for visible colonies and "
               "clear zones to develop.",
    },
    {
        "id": "ks4-culturing-microorganisms-e18",
        "subtopic_slug": "culturing-microorganisms",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the process by which an antibiotic spreads out of a "
                "paper disc into the agar around it.",
        "options": [
            "Active transport",
            "Diffusion",
            "Osmosis",
            "Respiration",
        ],
        "correct_index": 1,
        "why": "The antibiotic moves out of the disc, where it is "
               "concentrated, into the agar, where it is not, and that is "
               "diffusion.",
    },

    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # The method and its reasons: why sterilise, why flame the loop
    # afterwards, why a research laboratory may use a temperature a school
    # may not, why an even lawn, antiseptic against antibiotic, the area of a
    # 14 mm zone, why a contaminated plate is useless, why the zone is round,
    # why a gel rather than a broth, the inverted dish, two antiseptics
    # compared, industrial culturing, the minerals and vitamins, and why two
    # classes' plates cannot be compared.
    {
        "id": "ks4-culturing-microorganisms-s05",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why culture media and Petri dishes are sterilised "
                "before they are used.",
        "options": [
            "So that the only microorganism that can grow is the one deliberately added",
            "So that the agar sets into a firm gel in the dish instead of staying a warm runny liquid",
            "So that the nutrients in the agar are broken down into a usable form",
            "So that the bacteria added later are killed off as soon as they land on the agar",
        ],
        "correct_index": 0,
        "why": "Sterilising removes every microorganism already present, so "
               "growth on the plate can only have come from the culture that "
               "was added.",
    },
    {
        "id": "ks4-culturing-microorganisms-s06",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student flames their inoculating loop before transferring "
                "bacteria to a plate, but sets it straight down on the bench "
                "afterwards without flaming it again. Explain the risk this "
                "creates.",
        "options": [
            "The loop is still carrying live bacteria, so the bench is now contaminated",
            "The agar on the plate that was just inoculated will dry out",
            "The colony on the plate will grow more slowly because the loop cooled unevenly",
            "None — the bacteria on the loop die within a few seconds in open air",
        ],
        "correct_index": 0,
        "why": "Flaming afterwards is what kills the culture left on the wire; "
               "skipping it leaves live bacteria on a surface other people and "
               "equipment then touch.",
    },
    {
        "id": "ks4-culturing-microorganisms-s07",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a research laboratory may incubate cultures at "
                "human body temperature when a school laboratory may not.",
        "options": [
            "Its agar contains an antibiotic, so no pathogen there is able to grow",
            "It uses bacteria of a kind that cannot grow at human body temperature",
            "It has containment facilities and trained staff that a school does not have",
            "Its incubators can be set to that exact temperature, whereas a school incubator cannot",
        ],
        "correct_index": 2,
        "why": "Body temperature favours organisms suited to the human body, "
               "so it is used only where strict containment controls that "
               "risk.",
    },
    {
        "id": "ks4-culturing-microorganisms-s08",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the bacteria must be spread evenly over the agar "
                "before the discs are placed on it.",
        "options": [
            "So that the bacteria do not use up all of the nutrients in just one part of the plate",
            "So that the colonies stay small enough to be counted one at a time afterwards",
            "So that the antibiotic does not have to diffuse so far before it reaches the far edge of the agar",
            "So that a clear zone is due to the antibiotic and not to a thin patch of bacteria",
        ],
        "correct_index": 3,
        "why": "An even lawn means every disc sits in the same density of "
               "bacteria, so a difference in zone size can only be due to the "
               "substances.",
    },
    {
        "id": "ks4-culturing-microorganisms-s09",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an antiseptic rather than an antibiotic is used "
                "to clean a laboratory bench.",
        "options": [
            "An antiseptic kills microorganisms outside the body, which is what a bench needs",
            "An antibiotic cannot be made strong enough to work anywhere outside a living body",
            "An antiseptic kills bacteria, whereas an antibiotic kills only fungi and viruses",
            "An antibiotic evaporates within seconds, so none of it would be left on the bench",
        ],
        "correct_index": 0,
        "why": "Antiseptics are used on skin and on surfaces to kill "
               "microorganisms outside the body; antibiotics treat infections "
               "inside it.",
    },
    {
        "id": "ks4-culturing-microorganisms-s10",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A clear inhibition zone measures 14 mm across. Calculate "
                "its area, to 2 significant figures.",
        "options": [
            "620 mm²",
            "150 mm²",
            "44 mm²",
            "88 mm²",
        ],
        "correct_index": 1,
        "why": "The radius is 7 mm, so the area is π × 7² = "
               "154 mm², which is 150 mm² to 2 significant figures.",
    },
    {
        "id": "ks4-culturing-microorganisms-s11",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a result taken from a contaminated plate cannot "
                "be used.",
        "options": [
            "The tape used to seal it will no longer stick once contamination has begun",
            "The antibiotic on the discs is all used up by the contaminant long before it can work",
            "The growth on it may be from an organism nobody added, so it proves nothing",
            "The extra organisms use up the agar, so the plate simply dries out too fast",
        ],
        "correct_index": 2,
        "why": "If unknown microorganisms are present, any zone — or the "
               "absence of one — may be caused by them rather than by the "
               "substance being tested.",
    },
    {
        "id": "ks4-culturing-microorganisms-s12",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the zone around an antibiotic disc is circular.",
        "options": [
            "The bacteria grow in circles, so the gaps they leave are circular",
            "The disc is pressed into the agar, and its shape is stamped there",
            "The agar sets in rings, so an antibiotic spreads along one ring",
            "The antibiotic diffuses outwards from the disc equally in all directions",
        ],
        "correct_index": 3,
        "why": "The antibiotic spreads out of the disc by diffusion at the "
               "same rate in every direction, so the area it inhibits is a "
               "circle.",
    },
    {
        "id": "ks4-culturing-microorganisms-s13",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a solid agar gel, rather than a liquid nutrient "
                "broth, is used when antibiotic discs are being compared.",
        "options": [
            "A gel holds each disc in place and lets separate clear zones be seen",
            "A gel contains far more nutrients than a broth of the same volume",
            "A gel keeps the bacteria alive, whereas a broth kills them in an hour",
            "A gel needs no sterilising, so the work can be set up much faster",
        ],
        "correct_index": 0,
        "why": "In a solid gel the bacteria and the antibiotic stay where "
               "they are put, so each disc produces its own measurable zone.",
    },
    {
        "id": "ks4-culturing-microorganisms-s14",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an agar plate is incubated with its lid "
                "downwards.",
        "options": [
            "So that the colonies are pressed flat, which makes the zones easier to see",
            "So that water condensing on the lid cannot drip onto the growing colonies",
            "So that the bacteria are pulled down into the agar by gravity as they start to grow",
            "So that the agar cannot slide out of the dish while it is being warmed",
        ],
        "correct_index": 1,
        "why": "Condensation collects on the cooler lid, and inverting the "
               "dish keeps those drops off the agar, where they would smear "
               "the colonies.",
    },
    {
        "id": "ks4-culturing-microorganisms-s15",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "On one plate, antiseptic X gives a zone 18 mm across and "
                "antiseptic Y a zone 9 mm across. Explain which is more "
                "effective at that concentration.",
        "options": [
            "X, but only because a wider zone shows it diffused faster, not that it works",
            "Neither, because zone size shows how far a substance spread and nothing else",
            "X, because it stopped the bacteria growing across a wider area of the plate",
            "Y, because a smaller zone shows the antiseptic stayed where it was needed",
        ],
        "correct_index": 2,
        "why": "A larger inhibition zone means bacteria were stopped further "
               "from the disc, so at that concentration X is the more "
               "effective of the two.",
    },
    {
        "id": "ks4-culturing-microorganisms-s16",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a pharmaceutical company cultures "
                "microorganisms on a large scale.",
        "options": [
            "To use up the nutrients in the agar before that agar has to be thrown out",
            "To keep the microorganisms alive so that the species does not die out",
            "To raise the temperature of the fermenter, which then needs no heating",
            "To produce medicines such as antibiotics in the quantities that are needed",
        ],
        "correct_index": 3,
        "why": "Microorganisms are cultured in bulk to make medicines, foods "
               "and industrial chemicals.",
    },
    {
        "id": "ks4-culturing-microorganisms-s17",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a culture medium has to contain minerals and "
                "vitamins as well as a sugar.",
        "options": [
            "Bacteria need them in small amounts for reactions a sugar cannot supply",
            "They are what makes the agar set firmly, which a sugar on its own cannot do",
            "They kill off any contaminant that happens to land on the agar out of the air nearby",
            "They give the colonies their colour, which is the one way they can be counted",
        ],
        "correct_index": 0,
        "why": "A culture medium has to supply everything the microorganism "
               "needs, so minerals and vitamins are added alongside the "
               "carbon and nitrogen sources.",
    },
    {
        "id": "ks4-culturing-microorganisms-s18",
        "subtopic_slug": "culturing-microorganisms",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the zones on one plate can be compared with each "
                "other but not with the zones on a plate set up by another "
                "class.",
        "options": [
            "Zones shrink as soon as a plate is moved, so a second plate cannot be compared",
            "The other plate may carry a different density of bacteria or have been kept warmer",
            "The other plate will contain a different antibiotic, no matter which discs were used",
            "Zones can be compared if both plates were poured from the very same bottle of agar",
        ],
        "correct_index": 1,
        "why": "A fair comparison needs the same bacteria, the same lawn "
               "density and the same incubation conditions, which only one "
               "plate can guarantee.",
    },

    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # The arithmetic worked backwards and converted, an unfamiliar plate to
    # diagnose, an unfair test to identify, a conclusion to weigh, the
    # autoclave against boiling, aseptic technique justified for a harmless
    # organism, antibiotic against antiseptic compared, mixed colonies from a
    # doorknob, an unsterilised fermenter, the measurement through the
    # centre, the uninoculated control plate, and an error found and put
    # right.
    {
        "id": "ks4-culturing-microorganisms-h05",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A circular inhibition zone has an area of 78.5 mm². "
                "Determine its radius.",
        "options": [
            "5 mm",
            "10 mm",
            "25 mm",
            "12.5 mm",
        ],
        "correct_index": 0,
        "why": "Dividing the area by π gives r² = 25 mm², so "
               "the radius is the square root of that, 5 mm.",
    },
    {
        "id": "ks4-culturing-microorganisms-h06",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "An inhibition zone has an area of 250 mm². Determine "
                "this area in cm².",
        "options": [
            "2500 cm²",
            "2.5 cm²",
            "25 cm²",
            "0.25 cm²",
        ],
        "correct_index": 1,
        "why": "There are 100 mm² in 1 cm², so 250 mm² divided "
               "by 100 is 2.5 cm².",
    },
    {
        "id": "ks4-culturing-microorganisms-h07",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Three measurements of one inhibition zone give diameters of "
                "11 mm, 12 mm and 13 mm. Determine the area of the zone from "
                "the mean diameter, to 2 significant figures.",
        "options": [
            "450 mm²",
            "1000 mm²",
            "110 mm²",
            "38 mm²",
        ],
        "correct_index": 2,
        "why": "The mean diameter is 12 mm, so the radius is 6 mm and the "
               "area is π × 6² = 113 mm², which is "
               "110 mm² to 2 significant figures.",
    },
    {
        "id": "ks4-culturing-microorganisms-h08",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A plate shows a thick lawn of bacteria everywhere and no "
                "clear zone around any of its four antibiotic discs. Suggest "
                "two possible explanations.",
        "options": [
            "The plate was incubated for too long, or else the agar was poured far too thickly",
            "The bacteria were spread too evenly, or the lid was sealed with too much tape",
            "The antibiotics diffused too far, or the plate was kept at too low a temperature",
            "The bacteria resist all four antibiotics, or the discs were never soaked in any",
        ],
        "correct_index": 3,
        "why": "No zone anywhere means nothing inhibited the bacteria, so "
               "either they resist all four antibiotics or no antibiotic was "
               "on the discs.",
    },
    {
        "id": "ks4-culturing-microorganisms-h09",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student soaks one disc in an antiseptic and a second disc "
                "in a different antiseptic made up twice as concentrated. "
                "Explain why the two zones cannot show which antiseptic is "
                "stronger.",
        "options": [
            "Concentration was not kept the same, so it could be the cause of any difference",
            "Volume is the one variable that can change a zone, so neither result means much",
            "Two antiseptics cannot be compared on a single plate, whatever their concentrations may be",
            "A zone shows how far a liquid soaked into the agar, not how strong that liquid is",
        ],
        "correct_index": 0,
        "why": "A fair test changes one variable at a time; with two "
               "concentrations, a bigger zone may be due to the "
               "concentration rather than to the substance.",
    },
    {
        "id": "ks4-culturing-microorganisms-h10",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student concludes that because one antibiotic gave the "
                "largest zone on a plate, it is the best antibiotic to treat "
                "any infection. Evaluate this conclusion.",
        "options": [
            "Sound, provided the plate was incubated at body temperature",
            "Unsafe — it worked best on this one species of bacterium, at this one concentration",
            "Sound — the largest zone identifies the best antibiotic for an infection",
            "Unsafe — zone size shows how far the antibiotic diffused, and nothing more",
        ],
        "correct_index": 1,
        "why": "The test compares those substances against one bacterium at "
               "one concentration, so it says nothing about other species or "
               "about use in a patient.",
    },
    {
        "id": "ks4-culturing-microorganisms-h11",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why an autoclave sterilises equipment more reliably "
                "than a pan of boiling water does.",
        "options": [
            "Boiling water dissolves the nutrients out of the agar before the gel can set",
            "Boiling water cannot reach inside a Petri dish once its lid has been put on",
            "Steam under pressure reaches a higher temperature, so bacterial spores never survive",
            "Steam carries no water, so nothing is left behind for bacteria to grow in later",
        ],
        "correct_index": 2,
        "why": "Boiling water reaches only 100 °C and some bacterial spores "
               "survive that, whereas pressurised steam is hotter and kills "
               "them.",
    },
    {
        "id": "ks4-culturing-microorganisms-h12",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why aseptic technique still matters when the "
                "microorganism being cultured is a harmless one.",
        "options": [
            "A harmless microorganism turns harmful as soon as it has been grown on a plate of nutrient agar",
            "Aseptic technique is the thing that makes the nutrients in the agar available to it",
            "Without it the agar would not set properly, so no colonies could grow on the plate",
            "A contaminant may itself be harmful, and it also makes the result unreliable",
        ],
        "correct_index": 3,
        "why": "Contamination both invalidates the investigation and may "
               "introduce an organism that is a genuine hazard to the people "
               "handling it.",
    },
    {
        "id": "ks4-culturing-microorganisms-h13",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare how an antibiotic and an antiseptic are used, and "
                "suggest why both are tested on agar plates.",
        "options": [
            "Antibiotics treat infection inside the body and antiseptics clean skin and surfaces; a plate compares how well each stops bacteria",
            "Antibiotics clean skin and surfaces and antiseptics treat infection inside the body; a plate shows how far each one diffuses",
            "Both are taken into the body, but antiseptics act faster; a plate shows which of the two dissolves in agar more readily",
            "Both are used on surfaces only, but antibiotics are stronger; a plate shows which keeps the agar sterile for longer",
        ],
        "correct_index": 0,
        "why": "Both are tested by measuring inhibition zones, but an "
               "antibiotic is a medicine used inside the body while an "
               "antiseptic is used on skin and surfaces.",
    },
    {
        "id": "ks4-culturing-microorganisms-h14",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Bacteria wiped from an unwashed door handle are cultured, "
                "and every colony that appears is a different shape and "
                "colour. Explain what this shows.",
        "options": [
            "The plate was incubated too warm, and warmth changes a colony's colour",
            "Several different species were present on the handle, not just one",
            "One species was present, and each colony mutated into a new species",
            "The agar was not mixed evenly, so the colonies set at different depths",
        ],
        "correct_index": 1,
        "why": "Each colony grows from one original cell, so colonies that "
               "look different must have come from different species of "
               "microorganism.",
    },
    {
        "id": "ks4-culturing-microorganisms-h15",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fermenter used to make an antibiotic is sterilised with "
                "steam before each batch. Suggest what would happen if it "
                "were not.",
        "options": [
            "The antibiotic would be made too quickly for the tank to be emptied safely",
            "The temperature inside would fall, because steam is what warms a fermenter",
            "Other microorganisms would compete for the nutrients and spoil the product",
            "The nutrients would set into a gel, so nothing could be stirred through them",
        ],
        "correct_index": 2,
        "why": "Unwanted microorganisms would use up the nutrients and "
               "contaminate the product, so the whole batch could not be "
               "used.",
    },
    {
        "id": "ks4-culturing-microorganisms-h16",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the diameter of a clear zone is measured along a "
                "line that passes through the disc.",
        "options": [
            "The disc absorbs light, and a ruler must be read against something dark",
            "The antibiotic is strongest at the edge of a zone, where it stopped spreading",
            "A line that misses the disc measures the radius instead, which cannot be used",
            "Only a line through the disc at its centre gives the true diameter of a zone",
        ],
        "correct_index": 3,
        "why": "A line that misses the centre is shorter than the diameter, so "
               "the measurement has to pass through the disc at the centre of "
               "the zone.",
    },
    {
        "id": "ks4-culturing-microorganisms-h17",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "One plate is inoculated with bacteria and sealed, and a "
                "second identical plate is sealed with nothing added to it. "
                "Explain the purpose of the second plate.",
        "options": [
            "It shows whether the agar and the dish were sterile before the culture was added",
            "It shows how much of the agar the bacteria on the first plate have used up",
            "It shows how long the bacteria on the first plate take to form a colony",
            "It shows the colour the agar turns once the bacteria have finished growing",
        ],
        "correct_index": 0,
        "why": "Growth on a plate nobody inoculated would mean the equipment "
               "or the medium was contaminated, so the first plate's result "
               "could not be trusted.",
    },
    {
        "id": "ks4-culturing-microorganisms-h18",
        "subtopic_slug": "culturing-microorganisms",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student measures a zone 24 mm across and calculates its "
                "area as 1810 mm². Identify the error and give the "
                "correct area to 2 significant figures.",
        "options": [
            "The answer was simply not rounded; the correct area is 1800 mm²",
            "The diameter was used as the radius; the correct area is 450 mm²",
            "The radius was used as the diameter; the correct area is 7200 mm²",
            "The radius was not squared; the correct area is 38 mm²",
        ],
        "correct_index": 1,
        "why": "The radius is half of 24 mm, so the area is π × "
               "12² = 452 mm², which is 450 mm² to 2 "
               "significant figures.",
    },
]
