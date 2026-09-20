"""Biology · Bioenergetics — the MRB-338 expansion of `photosynthesis`.

One leaf only: AQA 8461 §4.4.1.1. The original twelve rows in
`bioenergetics.py` take the balanced equation, stomata, xylem, palisade
cells, the variegated-leaf test, night-time CO2 release, removing all CO2,
the timing compare against respiration, the compensation-point instant, a
week in total darkness, destarching before the starch test, and evaluating
"photosynthesis is respiration reversed".

This file takes what they leave: the reaction's endothermic energy
direction, chlorophyll as the named pigment, algae as the other named
photosynthesising group, the fate of the products (phloem, oxygen, the
carbon skeleton of glucose), root and stem cells with and without
chloroplasts, cloudy-day and orange-light photosynthesis, the balanced
equation worked as a ratio calculation in both directions, the dry-mass
and ash evidence that a plant's mass is not mainly drawn from the soil,
the foil-and-iodine test, algae at different depths and obtaining CO2
from water rather than air, a ring-barked tree's phloem failing before
its xylem, and two evaluate items that correct a plant "never needing
oxygen" and "never releasing CO2 in the light" from the same overstretched
reverse-equation idea.

Numbers here come from the equation's own coefficients — 6 CO2 : 6 H2O :
1 C6H12O6 : 6 O2 — worked in both directions, and from a dry-mass and an
ash comparison that are the standard evidence against the soil-mass idea.
No row here reaches into rate-of-photosynthesis's own territory: nothing
names a limiting factor, a light intensity gradient, temperature's effect
on enzymes, or the RP5 apparatus (lamp distance, sodium hydrogencarbonate)
that leaf owns.
"""

TOPIC = "bioenergetics"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    {
        "id": "ks4-photosynthesis-e05",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether photosynthesis is an endothermic or an "
                "exothermic reaction, and why.",
        "options": [
            "Endothermic, because light energy is absorbed and stored in "
            "glucose",
            "Exothermic, because energy is released from the glucose that "
            "is made",
            "Exothermic, because it takes place while the plant is in "
            "bright light",
            "Neither, because no energy is transferred during the "
            "reaction",
        ],
        "correct_index": 0,
        "why": "Photosynthesis absorbs light energy and stores it as "
               "chemical energy in glucose, which makes it endothermic.",
    },
    {
        "id": "ks4-photosynthesis-e06",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the pigment in a chloroplast that absorbs light "
                "energy for photosynthesis.",
        "options": [
            "Cellulose",
            "Chlorophyll",
            "Haemoglobin",
            "Cytoplasm",
        ],
        "correct_index": 1,
        "why": "Chlorophyll is the light-absorbing pigment held inside a "
               "chloroplast.",
    },
    {
        "id": "ks4-photosynthesis-e07",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name a group of organisms, besides green plants, that can "
                "carry out photosynthesis.",
        "options": [
            "Fungi",
            "Viruses",
            "Algae",
            "Yeast",
        ],
        "correct_index": 2,
        "why": "Algae contain chlorophyll in chloroplasts and photosynthesise "
               "just as green plants do.",
    },
    {
        "id": "ks4-photosynthesis-e08",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the tissue that carries the glucose made in "
                "photosynthesis away from the leaf.",
        "options": [
            "Xylem",
            "The waxy cuticle",
            "Stomata",
            "Phloem",
        ],
        "correct_index": 3,
        "why": "Phloem transports the sugars made in photosynthesis away to "
               "the rest of the plant.",
    },
    {
        "id": "ks4-photosynthesis-e09",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these is a reactant of photosynthesis "
                "rather than a product.",
        "options": [
            "Water",
            "Oxygen",
            "Starch",
            "Glucose",
        ],
        "correct_index": 0,
        "why": "Water is taken in as a reactant; glucose, oxygen and starch "
               "are all made from it.",
    },
    {
        "id": "ks4-photosynthesis-e10",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether a plant's root cells contain chloroplasts, "
                "and why.",
        "options": [
            "Yes, because roots absorb the carbon dioxide a plant needs",
            "No — roots are always underground and never receive light",
            "Yes, but just during the plant's first year of growth",
            "No, because roots store starch rather than sugar",
        ],
        "correct_index": 1,
        "why": "Chloroplasts would be useless underground, where no light "
               "reaches the root cells.",
    },
    {
        "id": "ks4-photosynthesis-e11",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas released as a waste product of photosynthesis.",
        "options": [
            "Nitrogen",
            "Carbon dioxide",
            "Oxygen",
            "Water vapour",
        ],
        "correct_index": 2,
        "why": "Oxygen is released through the stomata as photosynthesis "
               "makes glucose from carbon dioxide and water.",
    },
    {
        "id": "ks4-photosynthesis-e12",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the raw material that supplies the carbon atoms built "
                "into glucose during photosynthesis.",
        "options": [
            "Water",
            "Oxygen",
            "Nitrate ions",
            "Carbon dioxide",
        ],
        "correct_index": 3,
        "why": "Carbon dioxide is the only reactant that supplies carbon, "
               "which becomes part of every glucose molecule made.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    {
        "id": "ks4-photosynthesis-s05",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why algae can carry out photosynthesis but fungi "
                "cannot.",
        "options": [
            "Algae contain chloroplasts with chlorophyll; fungi do not",
            "Algae live in water, which is what lets aquatic organisms "
            "photosynthesise",
            "Algae have cell walls, and having a cell wall is what allows "
            "photosynthesis",
            "Algae respire aerobically, and this aerobic respiration is "
            "what allows photosynthesis",
        ],
        "correct_index": 0,
        "why": "Photosynthesis needs chlorophyll inside a chloroplast, which "
               "algae have and fungi lack.",
    },
    {
        "id": "ks4-photosynthesis-s06",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower fits red and blue LED lamps above seedlings "
                "rather than plain white lamps. Explain the advantage.",
        "options": [
            "Red and blue light contains no heat, so the seedlings cannot "
            "be scorched",
            "Red and blue are the wavelengths chlorophyll absorbs best for "
            "photosynthesis",
            "Red and blue LEDs are simply far cheaper to run than a white "
            "lamp",
            "Red and blue light makes the leaves grow larger, regardless "
            "of which pigment is present",
        ],
        "correct_index": 1,
        "why": "Chlorophyll absorbs red and blue light most strongly, so "
               "those wavelengths drive photosynthesis most efficiently.",
    },
    {
        "id": "ks4-photosynthesis-s07",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A leaf cutting, kept moist and warm, grows into a new "
                "plant, but a root cutting given the same care dies. "
                "Suggest why, referring to chloroplasts.",
        "options": [
            "A leaf cutting needs very little oxygen; a root cutting needs "
            "a constant supply",
            "A leaf cutting absorbs water directly; a root cutting cannot "
            "take in water",
            "A leaf cutting can photosynthesise its own glucose; a root "
            "cutting cannot",
            "A leaf cutting is simply larger, so it stores more of the "
            "parent's glucose",
        ],
        "correct_index": 2,
        "why": "Leaf cells contain chloroplasts and can make their own "
               "glucose once rooted; root cells cannot photosynthesise.",
    },
    {
        "id": "ks4-photosynthesis-s08",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener removes every leaf from a plant with a green "
                "stem, leaving the stem intact. Predict whether the plant "
                "can still photosynthesise, and explain.",
        "options": [
            "No, because photosynthesis can take place in a leaf alone",
            "Yes, because the stem absorbs light through its xylem "
            "vessels",
            "No, because without leaves there are no stomata left anywhere "
            "on the plant",
            "Yes — green stem cells always contain chlorophyll in their "
            "chloroplasts",
        ],
        "correct_index": 3,
        "why": "Any cell containing chlorophyll in a chloroplast can "
               "photosynthesise, including the cells of a green stem.",
    },
    {
        "id": "ks4-photosynthesis-s09",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the role of xylem with the role of phloem in "
                "photosynthesis.",
        "options": [
            "Xylem carries water to the leaf; phloem carries the glucose "
            "made away from it",
            "Xylem carries glucose to the leaf; phloem carries water away "
            "from it",
            "Both carry water; xylem to the leaf and phloem away from the "
            "roots",
            "Both carry glucose; xylem around the leaf and phloem around "
            "the stem",
        ],
        "correct_index": 0,
        "why": "Xylem supplies one reactant, water; phloem then distributes "
               "the sugar product to the rest of the plant.",
    },
    {
        "id": "ks4-photosynthesis-s10",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas collected from an aquatic plant in bright light "
                "relights a glowing splint. Identify the gas, and explain "
                "what the test shows.",
        "options": [
            "Carbon dioxide, because a glowing splint relights in a raised "
            "concentration of that gas",
            "Oxygen, because a glowing splint relights in a raised oxygen "
            "concentration",
            "Hydrogen, because a glowing splint pops rather than relights "
            "in that gas",
            "Water vapour, because a glowing splint relights in any moist "
            "gas",
        ],
        "correct_index": 1,
        "why": "A relit glowing splint is the standard test for oxygen, the "
               "gas photosynthesis releases.",
    },
    {
        "id": "ks4-photosynthesis-s11",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant kept outdoors on a cloudy day can "
                "still photosynthesise, though more slowly than on a "
                "bright day.",
        "options": [
            "Clouds keep the leaf temperature high enough for the enzymes "
            "to work",
            "Clouds raise the carbon dioxide concentration near the "
            "ground",
            "Some light energy still reaches the leaves through the cloud "
            "cover",
            "Cloud cover has no effect on how much light a leaf receives",
        ],
        "correct_index": 2,
        "why": "Cloud reduces light intensity but does not remove it "
               "completely, so some photosynthesis can still occur.",
    },
    {
        "id": "ks4-photosynthesis-s12",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant's uptake of water continues after "
                "dark, while its production of glucose does not.",
        "options": [
            "Glucose production continues in the dark, but water uptake "
            "stops",
            "Water uptake speeds up in the dark, while glucose production "
            "simply pauses",
            "Neither continues in the dark; both depend on light equally",
            "Water uptake never depends on light, but glucose production "
            "always does",
        ],
        "correct_index": 3,
        "why": "Roots can take up water at any time, but making glucose "
               "needs the light energy photosynthesis depends on.",
    },
    {
        "id": "ks4-photosynthesis-s13",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A variegated leaf has white patches with no chlorophyll. "
                "Explain why the whole leaf can still survive.",
        "options": [
            "The green patches make enough glucose to supply the whole "
            "leaf",
            "The white patches absorb glucose directly from the air "
            "around them",
            "The white patches carry out photosynthesis more efficiently "
            "instead",
            "The whole leaf survives on starch stored before it was ever "
            "green",
        ],
        "correct_index": 0,
        "why": "Glucose made in the chlorophyll-containing patches is "
               "transported through the leaf, supporting the parts that "
               "cannot photosynthesise.",
    },
    {
        "id": "ks4-photosynthesis-s14",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that photosynthesis happens in every cell "
                "of a green plant. Explain why this is incorrect.",
        "options": [
            "Every plant cell can photosynthesise, given bright direct "
            "sunlight",
            "Only cells containing chloroplasts, such as palisade cells, "
            "can photosynthesise",
            "Photosynthesis happens in every cell, during the day",
            "Cells with a cell wall are the ones able to carry out "
            "photosynthesis",
        ],
        "correct_index": 1,
        "why": "Cells such as root cells and xylem vessels have no "
               "chloroplasts, so they cannot photosynthesise at all.",
    },
    {
        "id": "ks4-photosynthesis-s15",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant's dry mass increases by 12 g over a week, while "
                "the mass of the soil it grows in falls by only 0.3 g. "
                "Explain where most of the extra 12 g came from.",
        "options": [
            "From minerals absorbed through the roots, which have a very "
            "high mass",
            "From the small loss of mass in the soil, concentrated into "
            "the plant",
            "From carbon dioxide and water built into glucose and other "
            "molecules",
            "From oxygen absorbed directly from the air into the plant's "
            "tissues",
        ],
        "correct_index": 2,
        "why": "Photosynthesis builds new dry mass from carbon dioxide and "
               "water, not mainly from the soil.",
    },
    {
        "id": "ks4-photosynthesis-s16",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why seedlings grown under green-tinted glass grow "
                "more slowly than seedlings grown under clear glass.",
        "options": [
            "Green glass lets through extra carbon dioxide, slowing "
            "photosynthesis",
            "Green glass blocks out all light, so no photosynthesis can "
            "occur",
            "Green glass raises the temperature too high for the enzymes "
            "to work",
            "Green glass mostly transmits the light chlorophyll absorbs "
            "least well",
        ],
        "correct_index": 3,
        "why": "Chlorophyll reflects green light rather than absorbing it, "
               "so light filtered to mostly green drives less "
               "photosynthesis.",
    },
    {
        "id": "ks4-photosynthesis-s17",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Using the balanced symbol equation, calculate how many "
                "molecules of water are needed to make 3 molecules of "
                "glucose.",
        "options": [
            "18 molecules",
            "6 molecules",
            "3 molecules",
            "36 molecules",
        ],
        "correct_index": 0,
        "why": "The equation needs 6 water molecules per glucose molecule, "
               "so 3 glucose needs 3 x 6 = 18 water.",
    },
    {
        "id": "ks4-photosynthesis-s18",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant absorbs 24 molecules of carbon dioxide during "
                "photosynthesis. Work out how many molecules of oxygen "
                "this produces.",
        "options": [
            "4 molecules",
            "24 molecules",
            "48 molecules",
            "144 molecules",
        ],
        "correct_index": 1,
        "why": "Carbon dioxide and oxygen appear in equal amounts in the "
               "equation, so 24 CO2 releases 24 O2.",
    },
    {
        "id": "ks4-photosynthesis-s19",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A leaf's dry mass is measured before and after six hours in "
                "bright light. Predict the change, and explain.",
        "options": [
            "It stays the same, because photosynthesis and respiration "
            "exactly cancel out",
            "It falls, because water evaporates from the leaf faster than "
            "it enters",
            "It rises, because photosynthesis adds more mass than "
            "respiration removes",
            "It falls, because glucose is used up faster than it can be "
            "replaced",
        ],
        "correct_index": 2,
        "why": "In good light, glucose is made faster than respiration uses "
               "it up, so the leaf's dry mass rises over the six hours.",
    },
    {
        "id": "ks4-photosynthesis-s20",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a fish-only aquarium needs a pump to add "
                "oxygen, while a balanced aquarium with aquatic plants "
                "does not.",
        "options": [
            "The plants filter the water, letting more air dissolve into "
            "it",
            "The plants use up the fish's waste, which frees oxygen "
            "automatically",
            "The plants raise the water temperature, which holds more "
            "oxygen",
            "The plants photosynthesise and release oxygen into the water",
        ],
        "correct_index": 3,
        "why": "Aquatic plants photosynthesising in the light are a natural "
               "oxygen source that a fish-only tank lacks.",
    },
    {
        "id": "ks4-photosynthesis-s21",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why seedlings grown under a lamp giving only a "
                "narrow band of orange light grow poorly.",
        "options": [
            "Orange light is not the red or blue light chlorophyll "
            "absorbs best",
            "Orange light contains too much ultraviolet energy for the "
            "leaves",
            "Orange light is simply too dim for any plant to use "
            "effectively",
            "Orange light raises the leaf temperature above the enzymes' "
            "optimum",
        ],
        "correct_index": 0,
        "why": "Chlorophyll absorbs red and blue light most strongly, so a "
               "narrow orange band supplies little usable energy.",
    },
    {
        "id": "ks4-photosynthesis-s22",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant has all the carbon dioxide removed from the air "
                "around it, yet starch is still found in its leaves a day "
                "later. Explain where this starch came from.",
        "options": [
            "It was made from the water alone, without any carbon dioxide",
            "It was made and stored before the carbon dioxide was removed",
            "It was absorbed directly from the soil through the roots",
            "It was converted from the oxygen released earlier that day",
        ],
        "correct_index": 1,
        "why": "Starch already stored from earlier photosynthesis remains "
               "in the leaf; no new starch can be made once carbon dioxide "
               "is removed.",
    },
    {
        "id": "ks4-photosynthesis-s23",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cutting down a large area of forest reduces "
                "the amount of oxygen released into the atmosphere.",
        "options": [
            "Fewer trees means less carbon dioxide is available in the "
            "air",
            "The cleared soil respires faster, using up more oxygen than "
            "before",
            "Fewer trees means less photosynthesis taking place overall",
            "The remaining trees photosynthesise more slowly once the "
            "canopy opens",
        ],
        "correct_index": 2,
        "why": "Photosynthesis by trees is a major source of atmospheric "
               "oxygen, so removing trees reduces how much is released.",
    },
    {
        "id": "ks4-photosynthesis-s24",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the direction of energy transfer in photosynthesis "
                "with the direction of energy transfer in respiration.",
        "options": [
            "Both store energy in glucose, and both need light in order "
            "to do so",
            "Both transfer energy out of glucose, but respiration does so "
            "more slowly",
            "Photosynthesis releases energy from light; respiration "
            "stores it in glucose",
            "Photosynthesis transfers energy in and stores it; "
            "respiration releases it",
        ],
        "correct_index": 3,
        "why": "Photosynthesis is endothermic, absorbing and storing "
               "energy; respiration is exothermic, releasing that stored "
               "energy.",
    },
    {
        "id": "ks4-photosynthesis-s25",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant takes in 36 molecules of carbon dioxide. Find the "
                "number of glucose molecules this makes.",
        "options": [
            "6 molecules",
            "36 molecules",
            "216 molecules",
            "3 molecules",
        ],
        "correct_index": 0,
        "why": "Six carbon dioxide molecules make one glucose molecule, so "
               "36 CO2 gives 36 / 6 = 6 glucose.",
    },
    {
        "id": "ks4-photosynthesis-s26",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Using the balanced symbol equation, work out how many "
                "molecules of glucose are made from 66 molecules of "
                "water.",
        "options": [
            "6 molecules",
            "11 molecules",
            "60 molecules",
            "396 molecules",
        ],
        "correct_index": 1,
        "why": "Six water molecules are needed per glucose molecule, so 66 "
               "water gives 66 / 6 = 11 glucose.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    {
        "id": "ks4-photosynthesis-h05",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a plant's dry mass comes mainly "
                "from the soil in which it grows.",
        "options": [
            "It is correct, because roots visibly shrink the volume of "
            "soil over time",
            "It is correct; minerals absorbed from soil make up almost all "
            "dry mass",
            "It is wrong; most dry mass is built from carbon dioxide and "
            "water",
            "It is wrong; dry mass comes entirely from the oxygen released "
            "each day",
        ],
        "correct_index": 2,
        "why": "Photosynthesis builds the great majority of a plant's dry "
               "mass from carbon dioxide and water, not from the soil.",
    },
    {
        "id": "ks4-photosynthesis-h06",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed, illuminated aquarium containing both fish and "
                "aquatic plants keeps a stable oxygen level for weeks with "
                "no pump. Explain the balance that maintains this.",
        "options": [
            "The glass tank itself slowly releases stored oxygen into the "
            "water",
            "The fish gradually stop respiring as their bodies adapt to "
            "the water's fixed oxygen level",
            "The plants stop respiring completely once enough light is "
            "available",
            "In the light, the plants' photosynthesis replaces the oxygen "
            "that respiration in the tank uses up",
        ],
        "correct_index": 3,
        "why": "While lit, the plants' photosynthesis produces roughly as "
               "much oxygen as the fish and plants together use up in "
               "respiration.",
    },
    {
        "id": "ks4-photosynthesis-h07",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement 'a green plant gets its energy from "
                "the soil.'",
        "options": [
            "It is wrong; the plant's energy comes from light absorbed by "
            "chlorophyll",
            "It is correct; the soil supplies the chemical energy stored "
            "in glucose",
            "It is correct, because minerals in soil are themselves a "
            "store of energy",
            "It is wrong; the plant's energy comes from the oxygen it "
            "releases",
        ],
        "correct_index": 0,
        "why": "Soil supplies water and minerals, but the energy stored in "
               "glucose comes from light absorbed during photosynthesis.",
    },
    {
        "id": "ks4-photosynthesis-h08",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant absorbs 1,200 molecules of carbon dioxide. "
                "Determine how many molecules of both glucose and oxygen "
                "are produced.",
        "options": [
            "1,200 molecules of glucose and 200 molecules of oxygen",
            "200 molecules of glucose and 1,200 molecules of oxygen",
            "7,200 molecules of glucose and 7,200 molecules of oxygen",
            "200 molecules of glucose and 7,200 molecules of oxygen",
        ],
        "correct_index": 1,
        "why": "Glucose is 1,200 / 6 = 200 molecules, and oxygen matches "
               "carbon dioxide at 1,200 molecules.",
    },
    {
        "id": "ks4-photosynthesis-h09",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine how many molecules of oxygen are released when a "
                "plant makes 45 molecules of glucose.",
        "options": [
            "45 molecules",
            "7.5 molecules",
            "270 molecules",
            "540 molecules",
        ],
        "correct_index": 2,
        "why": "Six oxygen molecules are released per glucose molecule "
               "made, so 45 glucose gives 45 x 6 = 270 oxygen.",
    },
    {
        "id": "ks4-photosynthesis-h10",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of dried plant material is burned, and the ash "
                "left over has a far smaller mass than the original "
                "sample. Explain why.",
        "options": [
            "Water evaporating during drying already removed most of the "
            "mass",
            "Burning destroys roughly half of any sample's original mass",
            "The ash contains no minerals, unlike the original plant "
            "material",
            "Most of the dry mass is organic matter that burns off as "
            "gases",
        ],
        "correct_index": 3,
        "why": "The dry mass is mostly carbon-based compounds built by "
               "photosynthesis, which burn away as carbon dioxide and water "
               "vapour, leaving only the mineral ash.",
    },
    {
        "id": "ks4-photosynthesis-h11",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Part of a leaf is covered with foil for 24 hours while the "
                "rest is left exposed to light, then the whole leaf is "
                "tested with iodine solution. Predict and explain the "
                "result.",
        "options": [
            "The exposed part turns blue-black; the covered part stays "
            "orange-brown",
            "The covered part turns blue-black; the exposed part stays "
            "orange-brown",
            "The whole leaf turns blue-black, because starch is made "
            "throughout it",
            "The whole leaf stays orange-brown, because foil blocks all "
            "photosynthesis",
        ],
        "correct_index": 0,
        "why": "Only the exposed part received light and could "
               "photosynthesise, so only it made the starch that turns "
               "iodine blue-black.",
    },
    {
        "id": "ks4-photosynthesis-h12",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a scientist tests one destarched leaf "
                "immediately and a second destarched leaf after a further "
                "six hours in light, rather than testing only one leaf.",
        "options": [
            "It shows the first leaf's result was measured incorrectly",
            "It shows any starch found afterwards was made during those "
            "six hours",
            "It removes the need to destarch the leaf beforehand",
            "It shows that iodine solution needs two separate leaves to "
            "work",
        ],
        "correct_index": 1,
        "why": "Testing the destarched leaf straight away confirms the "
               "starting point, so any starch in the second leaf must have "
               "been made in the six hours between.",
    },
    {
        "id": "ks4-photosynthesis-h13",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant's leaves give off 90 molecules of oxygen during "
                "photosynthesis. Work out how many molecules of glucose "
                "were made.",
        "options": [
            "90 molecules",
            "540 molecules",
            "15 molecules",
            "9 molecules",
        ],
        "correct_index": 2,
        "why": "Six oxygen molecules are released per glucose molecule, so "
               "90 oxygen comes from 90 / 6 = 15 glucose.",
    },
    {
        "id": "ks4-photosynthesis-h14",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare why an alga one metre below a lake's clear surface "
                "can photosynthesise well, while one fifty metres down in "
                "the same lake cannot.",
        "options": [
            "The alga at fifty metres has access to more dissolved oxygen",
            "Carbon dioxide is plentiful at one metre but absent at fifty "
            "metres",
            "The water is far warmer at one metre than at fifty metres "
            "down",
            "Enough light reaches one metre down; almost none reaches "
            "fifty metres",
        ],
        "correct_index": 3,
        "why": "Light is absorbed as it passes through water, so enough "
               "reaches one metre down for photosynthesis but almost none "
               "reaches fifty metres.",
    },
    {
        "id": "ks4-photosynthesis-h15",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why testing for oxygen bubbles is a simpler way to "
                "show photosynthesis is occurring than testing for a fall "
                "in dissolved carbon dioxide concentration.",
        "options": [
            "Bubbles of a gas can be seen and counted directly, unlike a "
            "small dissolved change",
            "Carbon dioxide concentration rises during photosynthesis, "
            "rather than falling",
            "Oxygen bubbles form once all the carbon dioxide has been "
            "used up",
            "Dissolved carbon dioxide is far too difficult to measure by "
            "any method",
        ],
        "correct_index": 0,
        "why": "A visible gas collecting as bubbles is far easier to "
               "observe and count than a small change in a dissolved gas's "
               "concentration.",
    },
    {
        "id": "ks4-photosynthesis-h16",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how an aquatic alga and a land plant each obtain "
                "the carbon dioxide they need for photosynthesis.",
        "options": [
            "Both absorb CO2 through stomata, since both carry out "
            "photosynthesis",
            "The alga absorbs dissolved CO2 across its surface; the land "
            "plant takes CO2 in through stomata",
            "The alga manufactures its own CO2 internally by respiration; "
            "the land plant absorbs it from the soil through its roots",
            "Both absorb dissolved CO2 directly through their roots from "
            "the water or soil",
        ],
        "correct_index": 1,
        "why": "An alga takes in carbon dioxide already dissolved in the "
               "surrounding water, while a land plant relies on stomata to "
               "let the gas diffuse in from the air.",
    },
    {
        "id": "ks4-photosynthesis-h17",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tree has a strip of bark and phloem removed all the way "
                "round its trunk. Its leaves stay healthy for several "
                "weeks before the whole tree eventually dies. Explain this "
                "pattern.",
        "options": [
            "The roots die first, because the bark carried the water "
            "supply to them",
            "The leaves die first, because the xylem is inevitably "
            "destroyed at the same time as the phloem",
            "The leaves keep photosynthesising, but glucose can never "
            "reach the roots, which then starve",
            "Nothing changes until the wound around the trunk finally "
            "heals",
        ],
        "correct_index": 2,
        "why": "Water still reaches the leaves through the undamaged "
               "xylem, so photosynthesis continues, but with the phloem "
               "destroyed the glucose cannot travel down to feed the "
               "roots.",
    },
    {
        "id": "ks4-photosynthesis-h18",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant's photosynthesis produces 5,400 molecules of "
                "oxygen in a day. Calculate how many molecules of glucose "
                "were made alongside it.",
        "options": [
            "5,400 molecules",
            "32,400 molecules",
            "90 molecules",
            "900 molecules",
        ],
        "correct_index": 3,
        "why": "Glucose is made at one sixth the rate of oxygen released, "
               "so 5,400 / 6 = 900 glucose molecules.",
    },
    {
        "id": "ks4-photosynthesis-h19",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A green organism is found in a pond sample. Suggest a "
                "test that would confirm it is photosynthesising, rather "
                "than simply being green in colour.",
        "options": [
            "Keep it in bright light and test any gas it releases for "
            "oxygen",
            "Check its colour again under a microscope at higher "
            "magnification",
            "Weigh the organism before and after leaving it in complete "
            "darkness",
            "Add iodine solution directly to the organism and look for a "
            "colour change",
        ],
        "correct_index": 0,
        "why": "Collecting gas the organism gives off in the light and "
               "showing it relights a glowing splint confirms oxygen is "
               "being produced, which colour alone cannot.",
    },
    {
        "id": "ks4-photosynthesis-h20",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A thick layer of algae covers a pond's surface, blocking "
                "light from the plants submerged beneath it. Predict the "
                "effect on those submerged plants over several weeks, and "
                "explain.",
        "options": [
            "They are unaffected, because respiration alone supplies all "
            "the energy a plant needs",
            "They photosynthesise far less, and may eventually die from a "
            "lack of glucose",
            "They photosynthesise more, because the algae raise the "
            "carbon dioxide concentration",
            "They switch permanently to making their glucose from the "
            "pond mud instead",
        ],
        "correct_index": 1,
        "why": "Without enough light reaching them, the submerged plants "
               "cannot photosynthesise enough to meet their energy needs, "
               "and may eventually die.",
    },
    {
        "id": "ks4-photosynthesis-h21",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant releases 10,800 molecules of oxygen. Determine how "
                "many molecules of both carbon dioxide and glucose were "
                "needed.",
        "options": [
            "64,800 molecules of carbon dioxide and 64,800 molecules of "
            "glucose",
            "1,800 molecules of carbon dioxide and 10,800 molecules of "
            "glucose",
            "10,800 molecules of carbon dioxide and 1,800 molecules of "
            "glucose",
            "10,800 molecules of carbon dioxide and 64,800 molecules of "
            "glucose",
        ],
        "correct_index": 2,
        "why": "Carbon dioxide matches oxygen at 10,800 molecules, and "
               "glucose is one sixth of that, 10,800 / 6 = 1,800.",
    },
    {
        "id": "ks4-photosynthesis-h22",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A field of crops uses up 3,000 molecules of carbon dioxide "
                "during photosynthesis. Calculate how many molecules of "
                "glucose this makes.",
        "options": [
            "3,000 molecules",
            "18,000 molecules",
            "250 molecules",
            "500 molecules",
        ],
        "correct_index": 3,
        "why": "Six carbon dioxide molecules are used for every glucose "
               "molecule made, so 3,000 / 6 = 500 glucose.",
    },
    {
        "id": "ks4-photosynthesis-h23",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that because photosynthesis and "
                "respiration have equations that are exact reverses of "
                "each other, a plant photosynthesising rapidly in bright "
                "light must be releasing no carbon dioxide at all at that "
                "moment.",
        "options": [
            "It is wrong; respiration continues too, so some carbon "
            "dioxide is still released",
            "It is correct; photosynthesis stops respiration completely "
            "in bright light",
            "It is correct, because the two reactions cannot ever occur "
            "at the same time",
            "It is wrong; photosynthesis itself directly releases carbon "
            "dioxide as well as oxygen",
        ],
        "correct_index": 0,
        "why": "Respiration keeps running in every living cell regardless "
               "of light, so the plant still produces some carbon dioxide "
               "even while photosynthesising rapidly.",
    },
    {
        "id": "ks4-photosynthesis-h24",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A greenhouse crop makes 25 molecules of glucose in an "
                "experiment. Find how many molecules of water this "
                "required.",
        "options": [
            "25 molecules",
            "150 molecules",
            "4.2 molecules",
            "300 molecules",
        ],
        "correct_index": 1,
        "why": "Six water molecules are needed for every glucose molecule "
               "made, so 25 glucose needs 25 x 6 = 150 water.",
    },
    {
        "id": "ks4-photosynthesis-h25",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because oxygen is released during "
                "photosynthesis, a plant does not need to take in any "
                "oxygen of its own. Evaluate this argument.",
        "options": [
            "It is correct, because any oxygen the plant needs is made "
            "internally by its roots",
            "It is correct; a photosynthesising plant does not respire",
            "It is wrong; the plant's own cells still need oxygen for "
            "respiration",
            "It is wrong; no oxygen is produced during photosynthesis",
        ],
        "correct_index": 2,
        "why": "Every living plant cell still respires and needs oxygen, "
               "regardless of how much extra oxygen photosynthesis happens "
               "to release.",
    },
    {
        "id": "ks4-photosynthesis-h26",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crop plant makes 500 molecules of glucose over the "
                "course of a day. Calculate the number of oxygen molecules "
                "it must have released to do so.",
        "options": [
            "500 molecules",
            "6,000 molecules",
            "83.3 molecules",
            "3,000 molecules",
        ],
        "correct_index": 3,
        "why": "Six oxygen molecules are released per glucose molecule "
               "made, so 500 glucose gives 500 x 6 = 3,000 oxygen.",
    },
]
