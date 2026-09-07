"""Biology · Bioenergetics — the seven subtopics of AQA 4.4.

Covers `photosynthesis` through `metabolism`: the photosynthesis equation
and where it happens, limiting factors and RP5, what a plant does with its
glucose, aerobic and anaerobic respiration, the body's response to exercise
and oxygen debt, and metabolism as the sum of anabolic and catabolic
reactions.

Every subtopic here is BASE — a Foundation Combined class sits all of it —
so nothing in these stems or options reaches into the Higher extension
prose (the inverse square law for light intensity, thyroxine and the
factors affecting metabolic rate, ATP yields treated quantitatively beyond
the numbers the base pages themselves teach).

⚠️ `aerobic-respiration` is a slug KS3 also uses. These questions are
deliberately and unmistakably KS4: the balanced symbol equation, the
mitochondrion and its cristae, ATP as the molecule the energy is released
into, and the exothermic transfer that powers metabolic processes — not the
KS3 "we breathe in oxygen". Formulae are written FLAT (CO2, C6H12O6),
because KS4 is not wired to the KS3 subscript pass.

The distractors are built from the misconceptions the pages themselves
declare: plants said to respire only at night or not at all,
photosynthesis and respiration treated as exact opposites, "limiting
factor" applied to whichever factor is largest rather than whichever is in
shortest supply, a plateau explained as "the plant ran out of chlorophyll",
yeast fermentation credited with lactic acid, oxygen debt confused with the
lactic acid itself or with a shortage during the exercise, starch storage
explained by digestibility rather than by insolubility, and metabolism
equated with respiration alone.

Nothing here restates a lesson page's own "Test yourself" question or its
matching block — those are a different pool, printed with their answers on
a page the child can open at will.
"""

TOPIC = "bioenergetics"
SUBJECT = "biology"

QUESTIONS = [
    # ── photosynthesis ──────────────────────────────────────────────────
    {
        "id": "ks4-photosynthesis-e01",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the balanced symbol equation for photosynthesis.",
        "options": [
            "CO2 + H2O -> C6H12O6 + O2",
            "6CO2 + 6H2O -> 6C6H12O6 + 6O2",
            "6CO2 + 6H2O -> C6H12O6 + 6O2",
            "C6H12O6 + 6O2 -> 6CO2 + 6H2O",
        ],
        "correct_index": 2,
        "why": "Six carbon dioxide and six water molecules make one glucose "
               "and six oxygen, which balances all three types of atom.",
    },
    {
        "id": "ks4-photosynthesis-e02",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the structures in a leaf through which carbon dioxide "
                "enters.",
        "options": [
            "Stomata",
            "Xylem vessels",
            "Root hairs",
            "Chloroplasts",
        ],
        "correct_index": 0,
        "why": "Stomata are the pores in the leaf surface that let carbon "
               "dioxide in and oxygen out.",
    },
    {
        "id": "ks4-photosynthesis-e03",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the tissue that carries water from the roots up to the "
                "leaves for photosynthesis.",
        "options": [
            "Phloem",
            "Stomata",
            "The permanent vacuole",
            "Xylem",
        ],
        "correct_index": 3,
        "why": "Xylem carries water and dissolved minerals upwards; phloem "
               "carries dissolved sugars away from the leaves.",
    },
    {
        "id": "ks4-photosynthesis-e04",
        "subtopic_slug": "photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which cells in a leaf carry out the most "
                "photosynthesis.",
        "options": [
            "The guard cells on either side of each stoma",
            "The palisade mesophyll cells near the upper surface",
            "The xylem vessels running through the leaf veins",
            "The epidermal cells covering the lower surface",
        ],
        "correct_index": 1,
        "why": "Palisade cells sit closest to the light and are packed with "
               "chloroplasts, so they do most of the leaf's photosynthesis.",
    },
    {
        "id": "ks4-photosynthesis-s01",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A variegated leaf has white patches that contain no "
                "chlorophyll. Explain why no starch is made in those patches.",
        "options": [
            "The white patches lose their starch to the green parts of the leaf",
            "The white patches have no stomata, so no carbon dioxide can enter",
            "The white patches are cooler, so their enzymes work far too slowly",
            "Without chlorophyll no light is absorbed, so no photosynthesis occurs",
        ],
        "correct_index": 3,
        "why": "Chlorophyll is what absorbs the light energy, so without it "
               "the reaction cannot run and no glucose or starch is made.",
    },
    {
        "id": "ks4-photosynthesis-s02",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "During the night a plant releases carbon dioxide. Explain "
                "why.",
        "options": [
            "The plant reverses photosynthesis in the dark, undoing the day",
            "The plant is respiring, and no photosynthesis is using the CO2",
            "The plant stops respiring at night, so CO2 leaks out of the stomata",
            "The plant breaks down its starch, and CO2 is the waste product",
        ],
        "correct_index": 1,
        "why": "Plants respire all the time; in the dark there is no "
               "photosynthesis taking the CO2 back in, so it is released.",
    },
    {
        "id": "ks4-photosynthesis-s03",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant is given water and bright light, but all the carbon "
                "dioxide is removed from the air around it. Predict what "
                "happens to the amount of glucose it makes, and explain why.",
        "options": [
            "No glucose is made, because carbon dioxide supplies its carbon atoms",
            "Glucose is still made, because the carbon can come from the water",
            "Half as much is made, because only one of the two reactants is gone",
            "More glucose is made, because no energy is spent taking the gas in",
        ],
        "correct_index": 0,
        "why": "Carbon dioxide is the only source of the six carbon atoms in "
               "C6H12O6, so with none available no glucose can be built.",
    },
    {
        "id": "ks4-photosynthesis-s04",
        "subtopic_slug": "photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare photosynthesis and respiration in terms of when "
                "each takes place.",
        "options": [
            "Photosynthesis happens all the time; respiration only in the dark",
            "Both happen only in the light, in cells that contain chloroplasts",
            "Photosynthesis happens only in light; respiration all the time",
            "Both happen all the time, in every living cell of every organism",
        ],
        "correct_index": 2,
        "why": "Photosynthesis needs light and chloroplasts; respiration runs "
               "day and night in every living cell, plants included.",
    },
    {
        "id": "ks4-photosynthesis-h01",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "At one particular light level a plant takes in no oxygen "
                "and releases none. Explain what this shows.",
        "options": [
            "Photosynthesis and respiration are happening at exactly the same rate",
            "Both photosynthesis and respiration have stopped completely in the leaf",
            "Photosynthesis has stopped, so only respiration is taking place now",
            "The stomata have closed, so no gas can enter or leave the leaf at all",
        ],
        "correct_index": 0,
        "why": "The oxygen made by photosynthesis is exactly used up by "
               "respiration, so there is no net gas exchange either way.",
    },
    {
        "id": "ks4-photosynthesis-h02",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant kept in complete darkness for a week dies. Explain "
                "why, in terms of both photosynthesis and respiration.",
        "options": [
            "Respiration stops in the dark, so its cells have no energy at all",
            "Photosynthesis continues, but the glucose made is not enough to live on",
            "Photosynthesis stops but respiration continues, so glucose stores run out",
            "Both stop in the dark, so the plant becomes dormant and then dies",
        ],
        "correct_index": 2,
        "why": "With no light nothing new is made, but respiration keeps "
               "using glucose, so the plant's stores are eventually spent.",
    },
    {
        "id": "ks4-photosynthesis-h03",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Before testing a leaf for starch, it is left in the dark "
                "for 48 hours. Explain why.",
        "options": [
            "So the leaf has time to build up enough starch for the test to find",
            "So any starch already there is used up, giving a fair starting point",
            "So the chlorophyll breaks down and does not interfere with the iodine",
            "So the stomata close and no carbon dioxide can enter during the test",
        ],
        "correct_index": 1,
        "why": "Destarching first means any starch found afterwards must have "
               "been made during the experiment itself.",
    },
    {
        "id": "ks4-photosynthesis-h04",
        "subtopic_slug": "photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student states that photosynthesis is simply respiration "
                "run backwards. Evaluate this statement.",
        "options": [
            "Correct — the two equations are exact reverses, so the processes are",
            "Correct — the same enzymes catalyse both, working in opposite directions",
            "Incorrect — the two use completely different reactants and products",
            "The equations reverse, but the site, energy change and steps all differ",
        ],
        "correct_index": 3,
        "why": "The overall equations do reverse, but one is endothermic in "
               "chloroplasts and the other exothermic in mitochondria.",
    },

    # ── rate-of-photosynthesis ──────────────────────────────────────────
    {
        "id": "ks4-rate-of-photosynthesis-e01",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a limiting factor.",
        "options": [
            "The factor that is present in the largest amount at that moment",
            "The factor that a plant needs least of in order to photosynthesise",
            "Any factor that has no effect at all on the rate of the reaction",
            "The factor in shortest supply, holding back the rate of the reaction",
        ],
        "correct_index": 3,
        "why": "The rate is set by whichever factor is in shortest supply, "
               "not by whichever one is most abundant.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e02",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the three main limiting factors for photosynthesis.",
        "options": [
            "Light intensity, oxygen concentration and the temperature",
            "Light intensity, the water supply and the soil's mineral content",
            "Light intensity, carbon dioxide concentration and temperature",
            "Carbon dioxide concentration, oxygen concentration and the pH",
        ],
        "correct_index": 2,
        "why": "Light supplies the energy, carbon dioxide is the raw "
               "material, and temperature sets how fast the enzymes work.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e03",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the rate of photosynthesis is measured in RP5.",
        "options": [
            "By weighing the aquatic plant before and after the experiment",
            "By counting the oxygen bubbles the aquatic plant gives off per minute",
            "By measuring how far the water in the beaker cools each minute",
            "By measuring the length of new growth on the plant after an hour",
        ],
        "correct_index": 1,
        "why": "Oxygen is a product, so the number of bubbles released per "
               "minute is a direct measure of the rate.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-e04",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the substance added to the water in RP5 to keep the "
                "carbon dioxide concentration constant.",
        "options": [
            "Sodium hydrogencarbonate solution",
            "Iodine solution",
            "Distilled water",
            "Methylene blue solution",
        ],
        "correct_index": 0,
        "why": "Sodium hydrogencarbonate releases carbon dioxide into the "
               "water, keeping that variable controlled.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s01",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower burns a paraffin heater inside a greenhouse in "
                "winter. Explain the two ways this raises the crop yield.",
        "options": [
            "It raises the light intensity and adds water vapour to the air",
            "It raises the temperature and removes oxygen from the greenhouse air",
            "It raises the temperature and adds carbon dioxide to the air",
            "It raises the temperature and adds nitrate ions to the soil",
        ],
        "correct_index": 2,
        "why": "Burning paraffin warms the air and releases carbon dioxide, "
               "relieving two of the three limiting factors at once.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s02",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "At 10 °C a plant photosynthesises slowly even in bright "
                "light with plenty of carbon dioxide. Explain why.",
        "options": [
            "The enzymes have little kinetic energy, so successful collisions are rare",
            "The enzymes have all denatured, so their active sites no longer fit at all",
            "The chlorophyll cannot absorb light at temperatures below 15 °C",
            "The stomata close below 15 °C, so no carbon dioxide can enter",
        ],
        "correct_index": 0,
        "why": "Cold slows enzyme and substrate molecules, so they collide "
               "less often and less successfully — the rate falls.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s03",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In RP5 a student stands the beaker in a large water bath. "
                "Explain why.",
        "options": [
            "To make sure the plant stays fully covered by water all the way through",
            "To keep the carbon dioxide concentration in the water constant",
            "To make the oxygen bubbles rise more slowly so they can be counted",
            "To keep the temperature constant, so only light intensity varies",
        ],
        "correct_index": 3,
        "why": "A lamp warms the water, so without a water bath temperature "
               "would change too and the test would not be fair.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-s04",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a warm, brightly lit day, the rate of photosynthesis in "
                "a field crop stops rising. Suggest the most likely limiting "
                "factor, and why.",
        "options": [
            "Light intensity, because leaves shade one another in a dense crop",
            "Carbon dioxide, because the air holds only about 0.04% of it",
            "Water, because the crop loses it faster than the roots take it up",
            "Oxygen, because the crop cannot release it fast enough through stomata",
        ],
        "correct_index": 1,
        "why": "With light and warmth plentiful, the scarce raw material is "
               "carbon dioxide, which is only about 0.04% of the air.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h01",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "At a low carbon dioxide concentration the rate of "
                "photosynthesis stops rising at a lower light intensity than "
                "it does at a high carbon dioxide concentration. Explain what "
                "this shows.",
        "options": [
            "Carbon dioxide can never limit the rate once the light is bright enough",
            "Carbon dioxide becomes the limiting factor sooner when less is available",
            "Light intensity is the only factor limiting the rate in both conditions",
            "The plant runs out of chlorophyll sooner at the lower CO2 concentration",
        ],
        "correct_index": 1,
        "why": "The rate stops rising where a factor other than light takes "
               "over, and with less carbon dioxide that happens sooner.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h02",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "At 45 °C the rate of photosynthesis is almost zero, and it "
                "does not recover when the plant is cooled again. Explain why "
                "the change is permanent.",
        "options": [
            "The chlorophyll has been bleached and so can no longer absorb any light",
            "The stomata have been sealed shut by the heat and cannot reopen",
            "The plant's glucose store has been used up and cannot be replaced",
            "The enzymes have denatured — the active site shape is changed for good",
        ],
        "correct_index": 3,
        "why": "Denaturing changes the active site shape permanently, so "
               "cooling the plant down cannot restore enzyme activity.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h03",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In one set of results, doubling the light intensity doubles "
                "the rate at low intensities but has no effect at high "
                "intensities. Explain both observations.",
        "options": [
            "Light limits the rate at low intensity; at high intensity another does",
            "Light limits the rate throughout, but the plant tires as the test runs",
            "The chlorophyll saturates with light and then breaks down completely",
            "Carbon dioxide limits at low intensity and light limits at high intensity",
        ],
        "correct_index": 0,
        "why": "While light is the factor in shortest supply the rate tracks "
               "it; once something else is scarcer, extra light does nothing.",
    },
    {
        "id": "ks4-rate-of-photosynthesis-h04",
        "subtopic_slug": "rate-of-photosynthesis",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical plants have the same light and carbon "
                "dioxide, but one is at 20 °C and one at 35 °C, and the "
                "warmer one photosynthesises faster. Predict what would "
                "happen if both were moved to 50 °C.",
        "options": [
            "Both would go faster still, because the rate rises with temperature",
            "The 35 °C plant would speed up and the 20 °C plant would slow down",
            "Both rates would fall sharply, because the enzymes would denature",
            "Both rates would stay the same, because carbon dioxide now limits",
        ],
        "correct_index": 2,
        "why": "50 °C is above the optimum for plant enzymes, so both plants' "
               "enzymes denature and both rates collapse.",
    },

    # ── uses-of-glucose ─────────────────────────────────────────────────
    {
        "id": "ks4-uses-of-glucose-e01",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one plant organ in which starch is stored.",
        "options": [
            "The stomata",
            "The potato tuber",
            "The xylem vessels",
            "The waxy cuticle",
        ],
        "correct_index": 1,
        "why": "A potato tuber is a storage organ packed with starch grains "
               "made from glucose.",
    },
    {
        "id": "ks4-uses-of-glucose-e02",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the ion a plant must absorb from the soil in order to "
                "make amino acids.",
        "options": [
            "Nitrate ions",
            "Chloride ions",
            "Carbonate ions",
            "Sulfate ions",
        ],
        "correct_index": 0,
        "why": "Amino acids contain nitrogen, and nitrate ions from the soil "
               "are the plant's nitrogen supply.",
    },
    {
        "id": "ks4-uses-of-glucose-e03",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the waxy cuticle on a leaf surface is made from.",
        "options": [
            "Cellulose, built up from glucose",
            "Protein, built up from amino acids",
            "Lipids, built up from glucose",
            "Starch, built up from glucose",
        ],
        "correct_index": 2,
        "why": "The cuticle is a lipid layer, and plants make their lipids "
               "from the glucose made in photosynthesis.",
    },
    {
        "id": "ks4-uses-of-glucose-e04",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these a plant does NOT make from glucose.",
        "options": [
            "Starch",
            "Cellulose",
            "Fats and oils",
            "Nitrate ions",
        ],
        "correct_index": 3,
        "why": "Nitrate ions are absorbed from the soil, not manufactured; "
               "starch, cellulose and lipids are all built from glucose.",
    },
    {
        "id": "ks4-uses-of-glucose-s01",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant still needs to respire, even though it "
                "makes its own glucose.",
        "options": [
            "Respiration makes the carbon dioxide the plant needs to photosynthesise",
            "Respiration makes the oxygen the plant releases through its stomata",
            "Glucose holds energy, but only respiration releases it as usable ATP",
            "Respiration converts glucose into starch so that it can be stored",
        ],
        "correct_index": 2,
        "why": "Glucose is a store, not a usable currency: respiration is "
               "what transfers that energy into ATP the cell can spend.",
    },
    {
        "id": "ks4-uses-of-glucose-s02",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant must convert stored starch back into "
                "glucose before it can be used.",
        "options": [
            "Starch becomes toxic to plant cells if it stays in them too long",
            "Starch cannot be turned into cellulose, whereas glucose can be",
            "Starch molecules are too small to hold enough energy to respire",
            "Starch is insoluble, so it cannot be transported or respired as it is",
        ],
        "correct_index": 3,
        "why": "The very insolubility that makes starch a safe store also "
               "means it must be broken back down to glucose to be used.",
    },
    {
        "id": "ks4-uses-of-glucose-s03",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant is kept in the dark for two days. Predict what "
                "happens to the starch in its leaves, and why.",
        "options": [
            "It rises, because starch is made in the dark and used in the light",
            "It falls, because the plant respires stored starch but makes no glucose",
            "It stays the same, because starch can only be used during daylight",
            "It falls, because the starch leaks out through the open stomata",
        ],
        "correct_index": 1,
        "why": "Respiration continues in the dark and draws on the store, "
               "while no photosynthesis is replacing it.",
    },
    {
        "id": "ks4-uses-of-glucose-s04",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sunflower seeds store their energy as oil "
                "rather than as starch.",
        "options": [
            "Oil stores more energy per gram, so a small seed can carry more",
            "Oil is soluble, so the seedling can absorb it faster than starch",
            "Oil is made without glucose, so the parent plant saves its glucose",
            "Oil keeps water out, which would make the seed germinate too early",
        ],
        "correct_index": 0,
        "why": "Lipids are the most energy-dense store, so a seed can pack "
               "more energy into the same small mass.",
    },
    {
        "id": "ks4-uses-of-glucose-h01",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the link between a plant's rate of photosynthesis "
                "and its ability to absorb mineral ions from the soil.",
        "options": [
            "Photosynthesis makes the mineral ions the roots then take in by osmosis",
            "There is no link — mineral ions enter roots by diffusion, needing nothing",
            "Photosynthesis in the root cells provides the energy for absorbing them",
            "Glucose is respired in root cells, giving the ATP for active transport",
        ],
        "correct_index": 3,
        "why": "Mineral ions enter by active transport, which needs ATP from "
               "respiring glucose that photosynthesis supplied.",
    },
    {
        "id": "ks4-uses-of-glucose-h02",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the roles of cellulose and starch in a plant.",
        "options": [
            "Cellulose is the energy store; starch builds the walls of every cell",
            "Both are energy stores; cellulose is used first and starch kept in reserve",
            "Cellulose strengthens the cell wall; starch is an insoluble energy store",
            "Both build cell walls — cellulose in young cells and starch in old ones",
        ],
        "correct_index": 2,
        "why": "Both are polymers of glucose, but cellulose is structural and "
               "starch is the plant's insoluble energy store.",
    },
    {
        "id": "ks4-uses-of-glucose-h03",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farmer spreads a fertiliser containing nitrates on a "
                "field of wheat. Explain how this increases the yield.",
        "options": [
            "Nitrates let the wheat build amino acids and proteins, so it grows more",
            "Nitrates are absorbed and converted into glucose, adding to the sugar",
            "Nitrates raise the rate of photosynthesis by acting as a raw material",
            "Nitrates are stored in the grain as starch, making each grain heavier",
        ],
        "correct_index": 0,
        "why": "Nitrate supplies the nitrogen for amino acids, and without "
               "enough of it a plant cannot make the proteins it needs to grow.",
    },
    {
        "id": "ks4-uses-of-glucose-h04",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant makes 40 g of glucose in a day and uses 25 g of it "
                "in respiration and growth. Suggest what happens to the "
                "remaining 15 g.",
        "options": [
            "It is released back into the air through the open stomata as a vapour",
            "It is converted into starch and stored in the leaves, roots or seeds",
            "It is broken down into carbon dioxide and water and then excreted",
            "It stays as glucose in the cell sap until the plant next needs it",
        ],
        "correct_index": 1,
        "why": "Glucose made faster than it is used is converted to starch, "
               "an insoluble store that does not upset osmosis.",
    },

    # ── aerobic-respiration ─────────────────────────────────────────────
    {
        "id": "ks4-aerobic-respiration-e01",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the balanced symbol equation for aerobic respiration.",
        "options": [
            "6CO2 + 6H2O -> C6H12O6 + 6O2",
            "C6H12O6 + O2 -> CO2 + H2O",
            "C6H12O6 + 6O2 -> 6CO2 + 6H2O + 6ATP",
            "C6H12O6 + 6O2 -> 6CO2 + 6H2O",
        ],
        "correct_index": 3,
        "why": "One glucose reacts with six oxygen to give six carbon dioxide "
               "and six water; ATP is not a substance in the equation.",
    },
    {
        "id": "ks4-aerobic-respiration-e02",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what type of reaction aerobic respiration is, in "
                "terms of energy.",
        "options": [
            "Endothermic, because it takes in energy from its surroundings",
            "Exothermic, because it transfers energy out of the glucose",
            "Endothermic, because it needs oxygen in order to begin at all",
            "Neither, because energy is only stored and never transferred",
        ],
        "correct_index": 1,
        "why": "Respiration releases the energy stored in glucose to the "
               "cell, so it is exothermic; photosynthesis, which stores "
               "energy, is endothermic.",
    },
    {
        "id": "ks4-aerobic-respiration-e03",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State approximately how many ATP molecules aerobic "
                "respiration releases from one molecule of glucose.",
        "options": [
            "About 36 to 38",
            "About 2",
            "About 6",
            "About 100",
        ],
        "correct_index": 0,
        "why": "Complete breakdown with oxygen yields roughly 36–38 ATP, far "
               "more than the 2 from anaerobic respiration.",
    },
    {
        "id": "ks4-aerobic-respiration-e04",
        "subtopic_slug": "aerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the folded inner membranes of a mitochondrion, where "
                "aerobic respiration takes place.",
        "options": [
            "Stomata",
            "Villi",
            "Cristae",
            "Alveoli",
        ],
        "correct_index": 2,
        "why": "The cristae are the folds that give the mitochondrion a large "
               "internal surface area for the reactions.",
    },
    {
        "id": "ks4-aerobic-respiration-s01",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the number 6 appears in front of both CO2 and "
                "H2O in the equation for aerobic respiration.",
        "options": [
            "Glucose has six carbon atoms, so six CO2 and six H2O are formed",
            "Six is used because six oxygen molecules start the reaction off",
            "Six ATP molecules are released, so six of each product is made",
            "The equation would otherwise be endothermic rather than exothermic",
        ],
        "correct_index": 0,
        "why": "C6H12O6 holds six carbons and twelve hydrogens, so the atoms "
               "balance as 6CO2 and 6H2O.",
    },
    {
        "id": "ks4-aerobic-respiration-s02",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cells that carry out a lot of active transport "
                "need a good supply of oxygen.",
        "options": [
            "Oxygen is the carrier protein that moves substances across the membrane",
            "Oxygen makes the membrane more permeable, so substances cross faster",
            "Oxygen is used up directly in pumping ions against the gradient",
            "Aerobic respiration needs oxygen, and it supplies the ATP for pumping",
        ],
        "correct_index": 3,
        "why": "Active transport runs on ATP, and aerobic respiration — which "
               "needs oxygen — is what supplies most of that ATP.",
    },
    {
        "id": "ks4-aerobic-respiration-s03",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A yeast cell and a human liver cell both respire "
                "aerobically. Compare what each one produces.",
        "options": [
            "The yeast makes ethanol and CO2; the liver cell makes CO2 and water",
            "The yeast makes lactic acid; the liver cell makes CO2 and water",
            "Both make carbon dioxide and water, because both are respiring aerobically",
            "The yeast makes only CO2, while the liver cell makes CO2, water and lactic acid",
        ],
        "correct_index": 2,
        "why": "Aerobic respiration gives the same products in every "
               "organism; ethanol and lactic acid are anaerobic products.",
    },
    {
        "id": "ks4-aerobic-respiration-s04",
        "subtopic_slug": "aerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person's body temperature rises during a long "
                "run.",
        "options": [
            "Friction between the muscles and the bones generates heat as the body moves",
            "Respiration is exothermic, and the extra respiration releases more energy",
            "Blood is redirected to the skin, and this raises the core temperature",
            "Oxygen entering the blood carries heat in from the warm air in the lungs",
        ],
        "correct_index": 1,
        "why": "Respiration transfers energy out of glucose, and some of it "
               "always warms the body — more respiration means more warming.",
    },
    {
        "id": "ks4-aerobic-respiration-h01",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug stops the cristae of mitochondria from working. "
                "Predict the effect on a heart muscle cell.",
        "options": [
            "It would still respire aerobically, but in the cytoplasm of the cell instead",
            "It could not release enough ATP, so it would soon stop contracting",
            "It would build more mitochondria, so contraction would carry on",
            "It would switch to photosynthesis to obtain the energy it needs",
        ],
        "correct_index": 1,
        "why": "Heart muscle depends on a constant ATP supply from aerobic "
               "respiration, so blocking the mitochondria stops contraction.",
    },
    {
        "id": "ks4-aerobic-respiration-h02",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In aerobic respiration all six carbon atoms of glucose end "
                "up in carbon dioxide. Explain what this tells you about the "
                "breakdown of glucose.",
        "options": [
            "Glucose is only partly broken down, so some of its carbon stays locked in it",
            "Glucose becomes six carbon dioxide molecules and no water is made",
            "Glucose is broken down completely, so all its stored energy is available",
            "Glucose contains six oxygen atoms, one for each carbon dioxide made",
        ],
        "correct_index": 2,
        "why": "Every carbon leaving as CO2 means nothing is left part-broken, "
               "which is why the aerobic route yields so much more ATP.",
    },
    {
        "id": "ks4-aerobic-respiration-h03",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why aerobic respiration releases roughly eighteen "
                "times as much ATP per glucose molecule as anaerobic "
                "respiration does.",
        "options": [
            "Anaerobic respiration happens in the cytoplasm, which is a smaller space",
            "Anaerobic respiration uses a different sugar that holds much less energy",
            "Aerobic respiration takes far longer, so more ATP builds up over time",
            "Oxygen lets glucose be broken down fully, releasing all of its energy",
        ],
        "correct_index": 3,
        "why": "Without oxygen the glucose is only partly broken down, and "
               "the rest of the energy stays locked in lactic acid or ethanol.",
    },
    {
        "id": "ks4-aerobic-respiration-h04",
        "subtopic_slug": "aerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that the energy released in respiration "
                "'is created in the mitochondria'. Explain why a teacher "
                "would mark this wrong.",
        "options": [
            "Energy is not created — it is transferred from the store in glucose",
            "Energy is created, but in the cytoplasm rather than the mitochondria",
            "Energy is created by the oxygen, not by the mitochondria themselves",
            "Energy is not released at all — respiration stores energy in glucose",
        ],
        "correct_index": 0,
        "why": "Energy cannot be created; respiration transfers energy that "
               "was already stored in the chemical bonds of glucose.",
    },

    # ── anaerobic-respiration ───────────────────────────────────────────
    {
        "id": "ks4-anaerobic-respiration-e01",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the part of the cell in which anaerobic respiration "
                "takes place.",
        "options": [
            "The cytoplasm",
            "The mitochondria",
            "The nucleus",
            "The ribosomes",
        ],
        "correct_index": 0,
        "why": "Anaerobic respiration runs in the cytoplasm; only the aerobic "
               "route needs the mitochondria.",
    },
    {
        "id": "ks4-anaerobic-respiration-e02",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name given to anaerobic respiration in yeast.",
        "options": [
            "Deamination",
            "Fermentation",
            "Denaturation",
            "Germination",
        ],
        "correct_index": 1,
        "why": "Fermentation is anaerobic respiration in yeast, and it is "
               "what makes bread rise and alcoholic drinks ferment.",
    },
    {
        "id": "ks4-anaerobic-respiration-e03",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether anaerobic respiration requires oxygen, and "
                "what it starts from.",
        "options": [
            "It requires oxygen, and it starts from lactic acid",
            "It requires no oxygen, but it starts from ethanol",
            "It requires no oxygen, and it starts from glucose",
            "It requires oxygen, and it starts from carbon dioxide",
        ],
        "correct_index": 2,
        "why": "Anaerobic means without oxygen, but the fuel is still "
               "glucose — it is simply not broken down completely.",
    },
    {
        "id": "ks4-anaerobic-respiration-e04",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which product of yeast fermentation can be used as a "
                "biofuel.",
        "options": [
            "Lactic acid",
            "Carbon dioxide",
            "Glucose",
            "Ethanol",
        ],
        "correct_index": 3,
        "why": "Ethanol from fermentation burns as a renewable fuel; the "
               "carbon dioxide is the gas released alongside it.",
    },
    {
        "id": "ks4-anaerobic-respiration-s01",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why anaerobic respiration cannot supply a marathon "
                "runner for the whole race.",
        "options": [
            "It would use up the runner's store of oxygen far too quickly",
            "It releases too little ATP per glucose, and lactic acid builds up",
            "It can only happen in the first few seconds after exercise begins",
            "It produces ethanol, which would poison the runner's muscle cells",
        ],
        "correct_index": 1,
        "why": "About 2 ATP per glucose cannot sustain long effort, and the "
               "lactic acid that builds up soon causes muscle fatigue.",
    },
    {
        "id": "ks4-anaerobic-respiration-s02",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A brewing vessel is fitted with a valve that lets gas out "
                "but no air in. Explain both features.",
        "options": [
            "It lets ethanol vapour escape and stops water from entering the vessel",
            "It lets oxygen out so that the yeast can respire without any of it",
            "It releases the CO2 made and keeps oxygen out, so fermentation continues",
            "It keeps the pressure high so that more ethanol dissolves in the liquid",
        ],
        "correct_index": 2,
        "why": "Fermentation makes carbon dioxide that must escape, but "
               "letting oxygen in would switch the yeast to aerobic respiration.",
    },
    {
        "id": "ks4-anaerobic-respiration-s03",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why muscles begin to ache and feel weak during a "
                "hard sprint.",
        "options": [
            "Ethanol builds up in the muscle and poisons the muscle enzymes",
            "Oxygen builds up in the muscle faster than it can be used up",
            "Glucose runs out completely, so no respiration of any kind occurs",
            "Lactic acid builds up, lowering the pH and disrupting the enzymes",
        ],
        "correct_index": 3,
        "why": "Lactic acid from anaerobic respiration lowers the pH inside "
               "muscle cells, so their enzymes work less well.",
    },
    {
        "id": "ks4-anaerobic-respiration-s04",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare where in a cell aerobic and anaerobic respiration "
                "take place.",
        "options": [
            "Aerobic in the mitochondria; anaerobic in the cytoplasm",
            "Both in the mitochondria, but anaerobic uses only the outer membrane",
            "Aerobic in the cytoplasm; anaerobic in the mitochondria",
            "Both in the cytoplasm, though aerobic also needs the nucleus",
        ],
        "correct_index": 0,
        "why": "Only the aerobic route uses the mitochondria; anaerobic "
               "respiration is completed in the cytoplasm.",
    },
    {
        "id": "ks4-anaerobic-respiration-h01",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the ethanol yeast produces is not present in a "
                "finished loaf of bread.",
        "options": [
            "The yeast reabsorbs the ethanol as the dough is kneaded and shaped",
            "The ethanol reacts with the flour to make more carbon dioxide gas",
            "The ethanol evaporates in the heat of the oven during baking",
            "The yeast makes only carbon dioxide once it is mixed with flour",
        ],
        "correct_index": 2,
        "why": "Ethanol boils well below oven temperature, so it evaporates "
               "away while the CO2 bubbles leave the risen texture behind.",
    },
    {
        "id": "ks4-anaerobic-respiration-h02",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant's roots sit in waterlogged soil for several days. "
                "Predict what happens in the root cells, and why.",
        "options": [
            "They photosynthesise instead, because there is plenty of water there",
            "They respire aerobically faster, because water carries dissolved oxygen",
            "They stop respiring altogether and the root cells become dormant",
            "They respire anaerobically, since water has driven the air from the soil",
        ],
        "correct_index": 3,
        "why": "Waterlogging fills the air spaces in soil, so root cells lose "
               "their oxygen supply and switch to anaerobic respiration.",
    },
    {
        "id": "ks4-anaerobic-respiration-h03",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aerobic respiration and anaerobic respiration in muscle "
                "both start with glucose. Explain why only one of them makes "
                "carbon dioxide.",
        "options": [
            "Only aerobic respiration breaks glucose down fully into carbon dioxide",
            "Only anaerobic respiration has the energy to split off carbon dioxide",
            "Only aerobic respiration uses glucose; the anaerobic route uses fat",
            "Only anaerobic respiration is fast enough for CO2 to be detected",
        ],
        "correct_index": 0,
        "why": "Without oxygen the glucose is only partly broken down to "
               "lactic acid, so its carbon never reaches carbon dioxide.",
    },
    {
        "id": "ks4-anaerobic-respiration-h04",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company ferments sugar cane to make ethanol for fuel. "
                "Suggest one advantage and one disadvantage of using it.",
        "options": [
            "It is renewable, but it releases lactic acid into the atmosphere",
            "It is renewable, but land used for the crop cannot be used for food",
            "It is non-renewable, but it burns without releasing any carbon dioxide",
            "It is renewable, and it has no disadvantages compared with petrol",
        ],
        "correct_index": 1,
        "why": "The crop can be regrown, so the fuel is renewable, but the "
               "same land could otherwise have grown food.",
    },

    # ── response-to-exercise ────────────────────────────────────────────
    {
        "id": "ks4-response-to-exercise-e01",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the acid that builds up in muscles during very intense "
                "exercise.",
        "options": [
            "Ethanoic acid",
            "Lactic acid",
            "Carbonic acid",
            "Amino acid",
        ],
        "correct_index": 1,
        "why": "Anaerobic respiration in muscle converts glucose into lactic "
               "acid, which accumulates when oxygen runs short.",
    },
    {
        "id": "ks4-response-to-exercise-e02",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the blood flow to the digestive "
                "system during hard exercise.",
        "options": [
            "It increases, so that food is digested faster to supply glucose",
            "It stays the same, because digestion continues at a constant rate",
            "It increases, because the gut needs more oxygen during exercise",
            "It falls, because blood is redirected to the working muscles",
        ],
        "correct_index": 3,
        "why": "Blood is redistributed towards the muscles that need oxygen "
               "and glucose, and away from organs that can wait.",
    },
    {
        "id": "ks4-response-to-exercise-e03",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the two substances that muscles need more of during "
                "exercise.",
        "options": [
            "Glucose and oxygen",
            "Lactic acid and urea",
            "Carbon dioxide and water",
            "Glycogen and nitrate ions",
        ],
        "correct_index": 0,
        "why": "Both are the reactants of aerobic respiration, and exercising "
               "muscle respires much faster than resting muscle.",
    },
    {
        "id": "ks4-response-to-exercise-e04",
        "subtopic_slug": "response-to-exercise",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to a person's resting heart rate after "
                "months of endurance training.",
        "options": [
            "It rises, because the heart has grown larger and beats harder",
            "It stays the same — training changes the rate only during exercise",
            "It falls, because the heart pumps more blood with each beat",
            "It becomes irregular, because the heart muscle has thickened",
        ],
        "correct_index": 2,
        "why": "A stronger heart moves more blood per beat, so fewer beats "
               "per minute are needed at rest.",
    },
    {
        "id": "ks4-response-to-exercise-s01",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why breathing more deeply, as well as more quickly, "
                "helps during exercise.",
        "options": [
            "Deeper breaths use more of the alveoli, so more oxygen enters the blood",
            "Deeper breaths warm the air, so the oxygen dissolves in blood faster",
            "Deeper breaths force carbon dioxide out through the skin as well",
            "Deeper breaths slow the heart, so blood spends longer in the lungs",
        ],
        "correct_index": 0,
        "why": "Depth and rate together raise the volume of air exchanged per "
               "minute, so more oxygen diffuses into the blood.",
    },
    {
        "id": "ks4-response-to-exercise-s02",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete's face becomes red during hard "
                "exercise.",
        "options": [
            "Lactic acid collects in the skin and colours the surface red",
            "The extra red blood cells made during exercise show through the skin",
            "Blood vessels near the skin widen, bringing more blood to the surface",
            "The skin respires anaerobically, and the ethanol made reddens it",
        ],
        "correct_index": 2,
        "why": "Vasodilation near the skin brings warm blood to the surface, "
               "which both cools the body and reddens the face.",
    },
    {
        "id": "ks4-response-to-exercise-s03",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a trained athlete can run further before their "
                "muscles begin to ache.",
        "options": [
            "Their muscles have stopped producing any lactic acid at all",
            "They have more mitochondria, so they respire aerobically for longer",
            "They store more lactic acid in the liver before it causes pain",
            "Their muscles are larger, so the lactic acid is spread more thinly",
        ],
        "correct_index": 1,
        "why": "More mitochondria and better oxygen delivery let a trained "
               "muscle stay aerobic, delaying the switch to anaerobic.",
    },
    {
        "id": "ks4-response-to-exercise-s04",
        "subtopic_slug": "response-to-exercise",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says 'you breathe hard during exercise in order "
                "to repay your oxygen debt'. Correct this statement.",
        "options": [
            "You repay the debt while exercising; afterwards you breathe hard to cool down",
            "There is no oxygen debt — the extra breathing only removes CO2",
            "The debt is repaid by the heart beating faster, not by breathing",
            "During exercise the hard breathing supplies oxygen; the debt is repaid after",
        ],
        "correct_index": 3,
        "why": "Hard breathing during exercise meets the immediate oxygen "
               "demand; the debt is the extra oxygen needed once you stop.",
    },
    {
        "id": "ks4-response-to-exercise-h01",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the harder the exercise, the longer recovery "
                "takes afterwards.",
        "options": [
            "Harder exercise uses more glucose, and glucose takes longer to replace",
            "Harder exercise raises body temperature, which takes hours to fall",
            "Harder exercise damages muscle fibres, which must be rebuilt by mitosis",
            "More lactic acid is made, so there is a larger oxygen debt to repay",
        ],
        "correct_index": 3,
        "why": "Recovery time is set by how much lactic acid has to be "
               "converted back, and that takes extra oxygen.",
    },
    {
        "id": "ks4-response-to-exercise-h02",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "During a 100 m sprint an athlete holds their breath. "
                "Explain how their muscles still obtain energy.",
        "options": [
            "The lungs release oxygen they had stored up before the race began",
            "The muscles respire anaerobically, releasing a small amount of ATP",
            "The muscles use ATP made by photosynthesis during the rest period",
            "The muscles stop respiring, and the movement uses stored elastic energy",
        ],
        "correct_index": 1,
        "why": "Without fresh oxygen the muscles switch to anaerobic "
               "respiration, which yields little ATP but needs no oxygen.",
    },
    {
        "id": "ks4-response-to-exercise-h03",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person's heart rate is 70 beats per minute at rest and "
                "140 beats per minute during exercise. Their heart pumps "
                "70 cm3 of blood with every beat. Calculate the increase in "
                "the volume of blood pumped per minute.",
        "options": [
            "70 cm3 per minute",
            "9800 cm3 per minute",
            "4900 cm3 per minute",
            "140 cm3 per minute",
        ],
        "correct_index": 2,
        "why": "140 x 70 = 9800 cm3 and 70 x 70 = 4900 cm3, so the increase "
               "is 9800 - 4900 = 4900 cm3 per minute.",
    },
    {
        "id": "ks4-response-to-exercise-h04",
        "subtopic_slug": "response-to-exercise",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two people run the same distance, but one has a much larger "
                "oxygen debt afterwards. Suggest what this tells you about "
                "how they ran.",
        "options": [
            "The one with the larger debt relied more on anaerobic respiration",
            "The one with the larger debt took in more oxygen while running",
            "The one with the larger debt has more mitochondria in their muscles",
            "The one with the larger debt ran more slowly and for much longer",
        ],
        "correct_index": 0,
        "why": "Oxygen debt measures the lactic acid left to be dealt with, "
               "so a larger debt means more anaerobic respiration was used.",
    },

    # ── metabolism ──────────────────────────────────────────────────────
    {
        "id": "ks4-metabolism-e01",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what catabolism means.",
        "options": [
            "Breaking large molecules down into smaller ones, releasing energy",
            "Building large molecules from smaller ones, using up energy",
            "Moving molecules across a membrane against a concentration gradient",
            "Copying molecules exactly, so that a cell is able to divide in two",
        ],
        "correct_index": 0,
        "why": "Catabolic reactions break things down and release energy; "
               "anabolic reactions build things up and use it.",
    },
    {
        "id": "ks4-metabolism-e02",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the organ in which deamination takes place.",
        "options": [
            "The kidney",
            "The pancreas",
            "The liver",
            "The small intestine",
        ],
        "correct_index": 2,
        "why": "The liver removes the amino group from excess amino acids and "
               "converts the ammonia produced into urea.",
    },
    {
        "id": "ks4-metabolism-e03",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the storage molecule made when the liver joins glucose "
                "molecules together.",
        "options": [
            "Starch",
            "Cellulose",
            "Urea",
            "Glycogen",
        ],
        "correct_index": 3,
        "why": "Animals store glucose as glycogen in the liver and muscles; "
               "starch and cellulose are the plant polymers.",
    },
    {
        "id": "ks4-metabolism-e04",
        "subtopic_slug": "metabolism",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which organ removes urea from the blood.",
        "options": [
            "The liver",
            "The kidneys",
            "The lungs",
            "The pancreas",
        ],
        "correct_index": 1,
        "why": "Urea is made in the liver but filtered out of the blood by "
               "the kidneys and excreted in urine.",
    },
    {
        "id": "ks4-metabolism-s01",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why every metabolic reaction depends on enzymes.",
        "options": [
            "Enzymes supply the energy that each reaction needs to get started",
            "Enzymes are used up in the reaction, so a fresh supply is needed",
            "Enzymes join onto the products and carry them out of the cell",
            "Enzymes speed the reactions up enough for the cell to stay alive",
        ],
        "correct_index": 3,
        "why": "At body temperature these reactions would be far too slow "
               "without enzymes to catalyse them.",
    },
    {
        "id": "ks4-metabolism-s02",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify the digestion of starch into glucose by amylase, "
                "and give the reason.",
        "options": [
            "Catabolic, because a large molecule is broken into smaller ones",
            "Anabolic, because glucose is a useful product that is then built up",
            "Anabolic, because the reaction needs ATP energy in order to happen",
            "Neither, because digestion happens outside the cells of the body",
        ],
        "correct_index": 0,
        "why": "Digestion breaks a large polymer into small subunits, which "
               "is the definition of a catabolic reaction.",
    },
    {
        "id": "ks4-metabolism-s03",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the body converts ammonia into urea rather than "
                "excreting the ammonia itself.",
        "options": [
            "Ammonia cannot dissolve in blood plasma, so it cannot be carried",
            "Ammonia is highly toxic; urea is far less toxic to carry in the blood",
            "Ammonia is a useful molecule, so the body keeps it and excretes urea",
            "Ammonia would be reabsorbed by the kidneys, but urea passes out",
        ],
        "correct_index": 1,
        "why": "Ammonia is very toxic even in small amounts, so the liver "
               "converts it to the much safer urea for transport.",
    },
    {
        "id": "ks4-metabolism-s04",
        "subtopic_slug": "metabolism",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person eats far more protein than their body needs. "
                "Predict what happens to the excess amino acids.",
        "options": [
            "They are stored in the liver until the body needs protein again",
            "They are converted directly into glucose and stored as glycogen",
            "They are deaminated, and the amino group ends up as urea in urine",
            "They pass out of the body unchanged in the faeces the next day",
        ],
        "correct_index": 2,
        "why": "Amino acids cannot be stored, so the surplus is deaminated "
               "and the nitrogen leaves the body as urea.",
    },
    {
        "id": "ks4-metabolism-h01",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why protein synthesis is described as an anabolic "
                "reaction that needs energy.",
        "options": [
            "It breaks proteins into amino acids, and breaking bonds needs energy",
            "It joins amino acids using energy taken directly from glucose itself",
            "It joins amino acids into a large molecule, and forming bonds needs ATP",
            "It copies DNA into protein, and copying always needs a supply of ATP",
        ],
        "correct_index": 2,
        "why": "Building a large molecule from small subunits is anabolic, "
               "and every peptide bond formed costs ATP.",
    },
    {
        "id": "ks4-metabolism-h02",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare respiration and protein synthesis in terms of "
                "metabolism.",
        "options": [
            "Both are catabolic reactions, but respiration releases far more energy",
            "Respiration is catabolic, releasing ATP; protein synthesis anabolic, using it",
            "Both are anabolic, because both build up the molecules that a cell needs",
            "Respiration is anabolic and stores ATP, whereas protein synthesis is catabolic",
        ],
        "correct_index": 1,
        "why": "Respiration breaks glucose down and supplies ATP; protein "
               "synthesis builds molecules up and spends it.",
    },
    {
        "id": "ks4-metabolism-h03",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person who eats no protein at all can still "
                "become ill, even with plenty of carbohydrate in their diet.",
        "options": [
            "Without amino acids, no enzymes or new proteins can be built at all",
            "Without protein, glucose cannot be broken down during any respiration",
            "Without protein, the liver cannot make urea and so it builds up",
            "Without protein, no glycogen can be stored in the liver or muscles",
        ],
        "correct_index": 0,
        "why": "Carbohydrate supplies energy but no nitrogen, and without "
               "amino acids the body cannot build enzymes or repair tissue.",
    },
    {
        "id": "ks4-metabolism-h04",
        "subtopic_slug": "metabolism",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a rapidly growing cell has a higher rate of "
                "anabolic reactions than a resting cell.",
        "options": [
            "Growing cells break down more molecules to make room for new ones",
            "Growing cells hold more enzymes, so every reaction runs more slowly",
            "Growing cells need less ATP, so more energy is left over for building",
            "Growing cells must build new proteins, membranes and DNA to enlarge",
        ],
        "correct_index": 3,
        "why": "Getting bigger and dividing means constructing new molecules, "
               "and construction is exactly what anabolic reactions do.",
    },
]
