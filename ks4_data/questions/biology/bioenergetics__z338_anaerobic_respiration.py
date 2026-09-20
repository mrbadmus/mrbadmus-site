"""Biology · Bioenergetics — the MRB-338 expansion of `anaerobic-respiration`.

One leaf only: AQA 8461 §4.4.2.2. The original twelve rows in
`bioenergetics.py` take the cytoplasm location, fermentation as the name
for anaerobic respiration in yeast, glucose as the shared starting point,
ethanol as a biofuel, why anaerobic respiration cannot sustain a marathon,
the brewing valve, lactic acid lowering pH and causing ache, comparing
aerobic and anaerobic locations, ethanol's absence from finished bread,
waterlogged roots switching pathway, why only aerobic respiration makes
CO2, and weighing ethanol as a renewable fuel against the land it takes.

This file takes what they leave: the two word equations recalled directly,
the roughly 2 ATP yield and what that number actually means for an
athlete, what becomes of lactic acid once exercise stops, fermentation's
other named products (beer, wine, cider, the CO2 that makes them fizzy),
brewing temperature as its own limiting factor, agricultural drainage as
the practical fix for waterlogging, and a run of ATP-yield arithmetic
matched in style to the aerobic-respiration leaf but never in wording.

Register: lactic acid and ethanol are treated as ordinary chemical
products, drug-and-alcohol-neutral, exactly as the lesson itself treats
them.
"""

TOPIC = "bioenergetics"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═══════════════════════════════════════
    {
        "id": "ks4-anaerobic-respiration-e05",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the word equation for anaerobic respiration in muscle.",
        "options": [
            "Glucose -> lactic acid",
            "Glucose + oxygen -> carbon dioxide + water",
            "Glucose -> ethanol + carbon dioxide",
            "Lactic acid -> glucose + oxygen",
        ],
        "correct_index": 0,
        "why": "In muscle, anaerobic respiration converts glucose into lactic acid, with no "
               "oxygen involved.",
    },
    {
        "id": "ks4-anaerobic-respiration-e06",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the word equation for anaerobic respiration in yeast.",
        "options": [
            "Glucose -> lactic acid",
            "Glucose -> ethanol + carbon dioxide",
            "Ethanol + oxygen -> glucose + water",
            "Glucose + oxygen -> ethanol + water",
        ],
        "correct_index": 1,
        "why": "Yeast respiring anaerobically breaks glucose down into ethanol and carbon "
               "dioxide, a process called fermentation.",
    },
    {
        "id": "ks4-anaerobic-respiration-e07",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the ATP yield of anaerobic respiration with the yield of aerobic "
               "respiration, for one glucose molecule.",
        "options": [
            "Anaerobic yields about 36",
            "Anaerobic yields about 100",
            "Anaerobic yields about 2",
            "Anaerobic yields about 18",
        ],
        "correct_index": 2,
        "why": "Anaerobic respiration releases only around 2 ATP per glucose molecule, far "
               "less than the aerobic route.",
    },
    {
        "id": "ks4-anaerobic-respiration-e08",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these drinks is made using yeast fermentation.",
        "options": [
            "Orange squash",
            "Sparkling mineral water",
            "Black tea",
            "Wine",
        ],
        "correct_index": 3,
        "why": "Wine is made by fermenting the sugars in grapes with yeast, producing "
               "ethanol.",
    },
    {
        "id": "ks4-anaerobic-respiration-e09",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the organ to which lactic acid is transported after exercise ends.",
        "options": [
            "The liver",
            "The bladder",
            "The lungs",
            "The pancreas",
        ],
        "correct_index": 0,
        "why": "Lactic acid is carried in the blood to the liver, where it is converted back "
               "into glucose.",
    },
    {
        "id": "ks4-anaerobic-respiration-e10",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what gas makes bread dough rise when yeast is added.",
        "options": [
            "Oxygen",
            "Carbon dioxide",
            "Nitrogen",
            "Hydrogen released from the yeast cell as it ferments",
        ],
        "correct_index": 1,
        "why": "Yeast fermenting sugars in the dough releases carbon dioxide, and the "
               "trapped bubbles make the dough rise.",
    },
    {
        "id": "ks4-anaerobic-respiration-e11",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which gas gives a fizzy fermented drink, such as cider, its "
               "bubbles.",
        "options": [
            "Oxygen",
            "Ethanol vapour",
            "Carbon dioxide",
            "Hydrogen",
        ],
        "correct_index": 2,
        "why": "The carbon dioxide made during fermentation is what gives a fizzy fermented "
               "drink its bubbles.",
    },
    {
        "id": "ks4-anaerobic-respiration-e12",
        "subtopic_slug": "anaerobic-respiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what farmers sometimes add to waterlogged fields to stop plant roots "
               "from respiring anaerobically.",
        "options": [
            "Extra fertiliser",
            "A layer of dark mulch",
            "Extra sodium hydrogencarbonate added to the waterlogged soil around the "
            "roots",
            "Drainage channels to remove the excess water",
        ],
        "correct_index": 3,
        "why": "Draining excess water lets air return to the soil, restoring the oxygen "
               "roots need for aerobic respiration.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════
    {
        "id": "ks4-anaerobic-respiration-s05",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a sprinter's muscles produce lactic acid during a 100 m race, "
               "but a marathon runner's muscles mostly do not.",
        "options": [
            "A sprint demands ATP faster than oxygen can be delivered, forcing anaerobic "
            "respiration",
            "A marathon is run at a temperature too low for lactic acid to form",
            "A sprinter's muscles contain no mitochondria, unlike a marathon runner's, "
            "which is not true of either runner",
            "A marathon runner's blood carries absolutely no oxygen during the entire "
            "race, from start to finish",
        ],
        "correct_index": 0,
        "why": "A sprint's sudden, intense demand for ATP outpaces oxygen delivery, so "
               "muscles switch briefly to anaerobic respiration.",
    },
    {
        "id": "ks4-anaerobic-respiration-s06",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why lactic acid causes a burning, aching feeling in a working "
               "muscle.",
        "options": [
            "Lactic acid dissolves the muscle fibres it comes into contact with",
            "Lactic acid lowers the pH inside the muscle, disrupting its enzymes",
            "Lactic acid blocks blood vessels, stopping oxygen reaching the muscle",
            "Lactic acid reacts with oxygen to release heat directly into the muscle",
        ],
        "correct_index": 1,
        "why": "Lactic acid lowers the pH inside muscle cells, which disrupts enzyme "
               "activity and produces the aching, burning sensation.",
    },
    {
        "id": "ks4-anaerobic-respiration-s07",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what happens to lactic acid once exercise has stopped.",
        "options": [
            "It is excreted from the body unchanged in sweat and urine",
            "It stays in the muscle permanently, causing lasting damage",
            "It is transported to the liver and converted back into glucose",
            "It is converted directly into carbon dioxide gas inside the muscle",
        ],
        "correct_index": 2,
        "why": "Lactic acid is carried to the liver in the blood, where oxygen is used to "
               "convert it back into glucose.",
    },
    {
        "id": "ks4-anaerobic-respiration-s08",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a brewer keeps the fermenting liquid within a narrow temperature "
               "range, rather than as warm as possible.",
        "options": [
            "Warmer liquid produces lactic acid instead of ethanol",
            "Warmer liquid stops carbon dioxide from being released, which is not what "
            "happens in reality as the liquid warms",
            "Warmer liquid converts the ethanol back into glucose",
            "Yeast's enzymes have an optimum temperature, and too much heat denatures "
            "them",
        ],
        "correct_index": 3,
        "why": "Like any enzyme-controlled reaction, fermentation has an optimum "
               "temperature, and too much heat denatures the yeast's enzymes.",
    },
    {
        "id": "ks4-anaerobic-respiration-s09",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student is asked how much less ATP anaerobic respiration releases per "
               "glucose molecule than aerobic respiration does. Suggest the best answer.",
        "options": [
            "Roughly eighteen times less",
            "Roughly twice as much",
            "Exactly the same amount",
            "Roughly eighteen times more, not less",
        ],
        "correct_index": 0,
        "why": "Anaerobic respiration only partly breaks down glucose, releasing roughly "
               "eighteen times less ATP than the complete aerobic route.",
    },
    {
        "id": "ks4-anaerobic-respiration-s10",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a keen home brewer fits an airlock, rather than a fully open "
               "lid, to their fermentation vessel.",
        "options": [
            "A fully open lid would stop any carbon dioxide from being made",
            "A fully open lid would let in oxygen, switching the yeast to aerobic "
            "respiration",
            "A fully open lid would cool the liquid too quickly for fermentation to start",
            "A fully open lid would convert the sugar directly into lactic acid",
        ],
        "correct_index": 1,
        "why": "An airlock lets carbon dioxide escape while keeping oxygen out, so the yeast "
               "keeps respiring anaerobically.",
    },
    {
        "id": "ks4-anaerobic-respiration-s11",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why waterlogged soil forces a plant's root cells to respire "
               "anaerobically.",
        "options": [
            "Waterlogged soil is too cold for aerobic respiration to continue",
            "Water reacts directly with the roots to produce lactic acid",
            "Water displaces the air from the soil, cutting off the roots' oxygen supply",
            "Waterlogged soil stops the roots taking up glucose from the leaves, which is "
            "a separate process from anaerobic respiration entirely",
        ],
        "correct_index": 2,
        "why": "Waterlogging fills the soil's air spaces, so root cells lose their oxygen "
               "supply and switch to anaerobic respiration.",
    },
    {
        "id": "ks4-anaerobic-respiration-s12",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a weightlifter performing one very heavy lift relies almost "
               "entirely on anaerobic respiration.",
        "options": [
            "A weightlifter's muscles contain very few mitochondria, although this is not "
            "the true reason for the switch to anaerobic respiration",
            "Lifting heavy weights stops a muscle needing any ATP",
            "A single lift uses no glucose, just stored lactic acid",
            "The lift is too brief for the heart and lungs to raise oxygen delivery in "
            "time",
        ],
        "correct_index": 3,
        "why": "A single powerful lift is over before the heart and lungs can raise oxygen "
               "delivery, so ATP comes from anaerobic respiration instead.",
    },
    {
        "id": "ks4-anaerobic-respiration-s13",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a loaf of bread contains no measurable ethanol once it is baked, "
               "despite being made using yeast.",
        "options": [
            "Ethanol boils away in the heat of the oven during baking",
            "Yeast converts all of its ethanol back into carbon dioxide while baking",
            "Ethanol is absorbed completely by the flour before baking begins",
            "Bread dough contains no yeast until after it has been baked",
        ],
        "correct_index": 0,
        "why": "Ethanol has a low boiling point, so it evaporates away in the oven's heat, "
               "leaving only the risen texture behind.",
    },
    {
        "id": "ks4-anaerobic-respiration-s14",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the products of anaerobic respiration in a muscle cell with the "
               "products in a yeast cell.",
        "options": [
            "Muscle makes ethanol; yeast makes lactic acid and water",
            "Muscle makes lactic acid; yeast makes ethanol and carbon dioxide",
            "Both make exactly the same two products",
            "Muscle makes just carbon dioxide; yeast makes just lactic acid",
        ],
        "correct_index": 1,
        "why": "Muscle cells produce lactic acid when respiring anaerobically, while yeast "
               "produces ethanol and carbon dioxide instead.",
    },
    {
        "id": "ks4-anaerobic-respiration-s15",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a cyclist sprinting for the finish line feels their legs "
               "suddenly grow heavy and start to ache.",
        "options": [
            "The cyclist's blood has stopped carrying any oxygen",
            "The muscles have completely run out of glucose to respire, which is not what "
            "causes the sudden ache during a sprint",
            "Lactic acid is building up faster than it can be cleared, disrupting the "
            "muscle",
            "The bicycle chain is adding extra resistance to the pedals",
        ],
        "correct_index": 2,
        "why": "A sudden sprint outpaces oxygen delivery, so lactic acid builds up faster "
               "than it can be cleared, causing the aching, heavy feeling.",
    },
    {
        "id": "ks4-anaerobic-respiration-s16",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain one advantage of using ethanol from fermentation as a fuel for "
               "vehicles.",
        "options": [
            "It releases far more energy per litre than any fossil fuel ever could",
            "It is produced without using any land",
            "It releases no carbon dioxide when it is burned",
            "It can be produced repeatedly from crops that are grown again each year",
        ],
        "correct_index": 3,
        "why": "Because it comes from a crop that can be grown again, ethanol from "
               "fermentation is a renewable fuel.",
    },
    {
        "id": "ks4-anaerobic-respiration-s17",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one disadvantage of growing crops specifically to produce ethanol as "
               "a biofuel.",
        "options": [
            "The land used could otherwise have grown food crops",
            "Ethanol biofuel cannot be burned in any engine",
            "Growing the crop destroys the soil permanently",
            "The fermentation process itself needs no energy",
        ],
        "correct_index": 0,
        "why": "Land given over to fuel crops is land not available to grow food, which is "
               "the main trade-off of biofuel crops.",
    },
    {
        "id": "ks4-anaerobic-respiration-s18",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that once a muscle starts respiring anaerobically, it stops "
               "respiring aerobically altogether. Correct this idea.",
        "options": [
            "This is correct; the two pathways cannot run together in the same muscle",
            "Aerobic respiration keeps running wherever oxygen still reaches the muscle",
            "Anaerobic respiration uses up every drop of oxygen immediately",
            "Aerobic respiration restarts just once exercise has completely finished",
        ],
        "correct_index": 1,
        "why": "Anaerobic respiration is a top-up, not a replacement; aerobic respiration "
               "keeps running in the muscle wherever oxygen is still available.",
    },
    {
        "id": "ks4-anaerobic-respiration-s19",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist's legs release about 10 ATP through anaerobic respiration during a "
               "short sprint. Using roughly 2 ATP per glucose molecule, estimate how many "
               "molecules of glucose this used.",
        "options": [
            "About 10 molecules",
            "About 7 molecules",
            "About 5 molecules",
            "About 20 molecules",
        ],
        "correct_index": 2,
        "why": "10 ATP divided by 2 ATP per glucose gives about 5 molecules of glucose "
               "respired.",
    },
    {
        "id": "ks4-anaerobic-respiration-s20",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A muscle cell produces about 40 ATP through anaerobic respiration. Estimate "
               "how many glucose molecules this required, at roughly 2 ATP per molecule.",
        "options": [
            "About 40 molecules",
            "About 2 molecules",
            "About 80 molecules",
            "About 20 molecules",
        ],
        "correct_index": 3,
        "why": "40 ATP divided by 2 ATP per glucose gives about 20 molecules of glucose "
               "respired.",
    },
    {
        "id": "ks4-anaerobic-respiration-s21",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a cheesemaker relies on bacteria or yeast fermentation, rather "
               "than aerobic respiration, to produce some fermented foods.",
        "options": [
            "Excluding oxygen favours the specific products fermentation gives, such as "
            "the right flavour or gas",
            "Aerobic respiration in food produces harmful toxins",
            "Aerobic respiration does not happen in bacteria or yeast",
            "Excluding oxygen speeds up aerobic respiration in the food",
        ],
        "correct_index": 0,
        "why": "Fermentation without oxygen gives the specific flavours and gases that many "
               "traditional fermented foods rely on.",
    },
    {
        "id": "ks4-anaerobic-respiration-s22",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a sports scientist measures how quickly an athlete's blood "
               "lactic acid level falls after a hard sprint.",
        "options": [
            "It shows exactly how much glucose the athlete ate that morning, which a "
            "lactic acid measurement cannot reveal",
            "It shows how efficiently the body is clearing and processing the lactic acid "
            "made",
            "It shows how much oxygen the athlete's blood can ever carry",
            "It has no connection to the athlete's level of fitness",
        ],
        "correct_index": 1,
        "why": "How quickly lactic acid falls reflects how efficiently the body clears and "
               "processes it, which is linked to fitness.",
    },
    {
        "id": "ks4-anaerobic-respiration-s23",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant's root cells, unlike a sprinter's muscle cells, cannot "
               "simply wait for anaerobic respiration to end before returning to normal.",
        "options": [
            "Root cells recover from anaerobic respiration within a single second, which "
            "understates how long a real recovery takes",
            "Root cells produce no lactic acid, so they need no recovery",
            "Root cells stay short of oxygen for as long as the soil remains waterlogged",
            "Root cells do not respire anaerobically under any circumstances",
        ],
        "correct_index": 2,
        "why": "A sprinter's oxygen shortage ends within minutes, but a root's shortage "
               "lasts as long as the soil stays waterlogged.",
    },
    {
        "id": "ks4-anaerobic-respiration-s24",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a food scientist checks that a batch of cider has stopped "
               "producing carbon dioxide before bottling it.",
        "options": [
            "It shows the yeast has switched over to aerobic respiration, which is not "
            "what a falling carbon dioxide rate shows in reality",
            "It shows all of the ethanol has already evaporated away",
            "It has no bearing on how safe the bottle is to seal",
            "It shows fermentation has finished, so the bottle will not build up "
            "dangerous pressure",
        ],
        "correct_index": 3,
        "why": "Bottling before fermentation ends traps carbon dioxide still being made, "
               "which can build dangerous pressure inside a sealed bottle.",
    },
    {
        "id": "ks4-anaerobic-respiration-s25",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an athlete's blood lactic acid level rises much faster during "
               "interval sprints than during a steady jog.",
        "options": [
            "Sprinting repeatedly outpaces oxygen delivery, forcing anaerobic respiration "
            "each time",
            "A steady jog uses far more oxygen overall than any single sprint session "
            "does",
            "Interval sprints stop the muscles needing oxygen",
            "A steady jog produces lactic acid faster than sprinting does",
        ],
        "correct_index": 0,
        "why": "Each sprint repeatedly demands ATP faster than oxygen can be delivered, so "
               "lactic acid builds up much faster than during steady, aerobic jogging.",
    },
    {
        "id": "ks4-anaerobic-respiration-s26",
        "subtopic_slug": "anaerobic-respiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A weightlifter's forearm muscles make roughly 2 ATP for every glucose "
               "molecule respired anaerobically during a lift. Determine the total ATP "
               "released if 12 molecules of glucose are used.",
        "options": [
            "About 14 ATP",
            "About 24 ATP",
            "About 6 ATP",
            "About 48 ATP",
        ],
        "correct_index": 1,
        "why": "12 molecules x 2 ATP each gives roughly 24 ATP in total.",
    },

    # ══ harder · h05–h26 ═══════════════════════════════════════
    {
        "id": "ks4-anaerobic-respiration-h05",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that anaerobic respiration is simply a worse version of "
               "aerobic respiration, with no real purpose of its own.",
        "options": [
            "It is correct; anaerobic respiration serves no purpose aerobic respiration "
            "does not",
            "It is correct, since anaerobic respiration produces less useful ATP than "
            "aerobic respiration",
            "It is wrong; anaerobic respiration lets ATP keep being made when oxygen "
            "delivery cannot keep up",
            "It is wrong; anaerobic respiration is the more efficient of the two pathways",
        ],
        "correct_index": 2,
        "why": "Anaerobic respiration lets a cell keep making some ATP during a brief oxygen "
               "shortfall, which is a genuine purpose of its own.",
    },
    {
        "id": "ks4-anaerobic-respiration-h06",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A runner's blood lactic acid level is measured every minute during a race "
               "that starts fast and then settles to a steady pace. Predict how the level "
               "changes, and explain.",
        "options": [
            "It stays at zero throughout, since running produces no lactic acid",
            "It rises steadily throughout the whole race, without levelling off, which "
            "ignores how the runner's pace settles in reality",
            "It falls throughout the race as the runner gets more tired",
            "It rises sharply at first, then levels off as the pace becomes steady and "
            "aerobic",
        ],
        "correct_index": 3,
        "why": "The fast start outpaces oxygen delivery, but once the pace becomes steady "
               "the runner respires mostly aerobically, so the level levels off.",
    },
    {
        "id": "ks4-anaerobic-respiration-h07",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a bacterium living deep in oxygen-free mud, unlike a human "
               "muscle cell, can respire anaerobically indefinitely without any apparent ill "
               "effect.",
        "options": [
            "Different organisms are adapted to cope with their own anaerobic products "
            "long-term",
            "Anaerobic respiration yields the same ATP in every organism",
            "Human muscle cells cannot make lactic acid, unlike such bacteria",
            "The mud itself constantly supplies the bacterium with extra oxygen",
        ],
        "correct_index": 0,
        "why": "Organisms adapted to permanently low-oxygen conditions can cope with their "
               "own anaerobic products long-term, unlike a human muscle relying on it "
               "briefly.",
    },
    {
        "id": "ks4-anaerobic-respiration-h08",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drug stops lactic acid being transported out of a muscle cell after "
               "exercise. Predict the effect on the muscle's recovery, and explain.",
        "options": [
            "Recovery would be faster, since the lactic acid would be used directly for "
            "more ATP, which is not how a disruptive waste product behaves in reality",
            "Recovery would be slower, since the lactic acid could not be cleared and "
            "converted elsewhere",
            "Recovery would be unaffected, since lactic acid plays no part in recovery",
            "Recovery would happen instantly, since the drug removes the need for oxygen",
        ],
        "correct_index": 1,
        "why": "If lactic acid cannot be transported away, its disruptive effect on the "
               "muscle's enzymes lingers, slowing recovery.",
    },
    {
        "id": "ks4-anaerobic-respiration-h09",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a large batch of fermenting fruit juice can become noticeably "
               "warmer as fermentation proceeds.",
        "options": [
            "Carbon dioxide reacts with the fruit juice to release heat directly",
            "Yeast absorbs heat from the air and stores it in the ethanol produced, "
            "rather than the ethanol simply carrying warmth from elsewhere",
            "Respiration, even the anaerobic kind, is an exothermic reaction that "
            "releases some energy as heat",
            "Fermentation is an endothermic reaction that should cool the juice down",
        ],
        "correct_index": 2,
        "why": "Like aerobic respiration, anaerobic respiration is exothermic, and a large "
               "fermenting batch can release enough heat to be noticeable.",
    },
    {
        "id": "ks4-anaerobic-respiration-h10",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the fate of the carbon atoms in glucose during aerobic respiration "
               "with their fate during anaerobic respiration in muscle.",
        "options": [
            "Both pathways convert every carbon atom into carbon dioxide",
            "Anaerobic respiration converts them all to carbon dioxide; aerobic "
            "respiration locks them in lactic acid, the reverse of what the carbon atoms "
            "do in each pathway",
            "Neither pathway changes what happens to the carbon atoms in glucose",
            "Aerobic respiration converts them all to carbon dioxide; anaerobic "
            "respiration leaves them locked in lactic acid",
        ],
        "correct_index": 3,
        "why": "Aerobic respiration breaks glucose down fully to carbon dioxide, while "
               "anaerobic respiration in muscle leaves the carbon locked inside lactic acid.",
    },
    {
        "id": "ks4-anaerobic-respiration-h11",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist's muscles produce approximately 60 ATP through anaerobic "
               "respiration during a short, hard climb. Estimate the number of glucose "
               "molecules this required, at roughly 2 ATP each.",
        "options": [
            "About 30 molecules",
            "About 60 molecules",
            "About 120 molecules",
            "About 15 molecules",
        ],
        "correct_index": 0,
        "why": "60 ATP divided by 2 ATP per glucose gives about 30 molecules of glucose "
               "respired.",
    },
    {
        "id": "ks4-anaerobic-respiration-h12",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that lactic acid is a harmful waste product the body "
               "simply needs to get rid of.",
        "options": [
            "It is entirely right; lactic acid has no further use to the body once made",
            "It is only partly right; lactic acid is disruptive short-term, but the liver "
            "later converts it back to a useful fuel",
            "It is entirely wrong; lactic acid causes no disruption to the muscle",
            "It is partly right in tone; the body cannot process lactic acid in any way "
            "here, when the liver converts a good deal of it back to glucose",
        ],
        "correct_index": 1,
        "why": "Lactic acid disrupts muscle enzymes in the short term, but the liver later "
               "converts it back into a useful fuel, glucose.",
    },
    {
        "id": "ks4-anaerobic-respiration-h13",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener notices that a waterlogged flower bed smells faintly of alcohol "
               "after several days. Suggest an explanation.",
        "options": [
            "Waterlogged soil converts fertiliser directly into ethanol",
            "The smell has nothing to do with a lack of oxygen in the soil",
            "Some root cells, and microbes in the waterlogged soil, may be respiring "
            "anaerobically and releasing ethanol-like products",
            "Waterlogged roots switch entirely to producing lactic acid instead",
        ],
        "correct_index": 2,
        "why": "Very low oxygen in waterlogged soil can push some plant and microbial cells "
               "towards fermentation-like pathways that release ethanol-like products.",
    },
    {
        "id": "ks4-anaerobic-respiration-h14",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete's ability to tolerate a high blood lactic acid level, "
               "rather than the level itself, is often what improves most with training.",
        "options": [
            "Training reduces the total amount of lactic acid made to zero",
            "Training removes the need for anaerobic respiration in every athlete, when "
            "in reality some anaerobic respiration still remains necessary",
            "Training has no effect on how the body handles lactic acid",
            "Training raises how much lactic acid the muscles and enzymes can withstand "
            "before performance suffers",
        ],
        "correct_index": 3,
        "why": "Training adapts the body to tolerate more lactic acid before it disrupts "
               "performance, rather than eliminating it entirely.",
    },
    {
        "id": "ks4-anaerobic-respiration-h15",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the environmental control needed to brew beer with the environmental "
               "control needed to bake bread, in terms of oxygen.",
        "options": [
            "Brewing excludes oxygen throughout; baking simply lets the yeast respire "
            "until the oven's heat stops it",
            "Both processes exclude oxygen just as strictly as each other",
            "Baking excludes oxygen throughout; brewing lets oxygen in freely",
            "Neither process needs any control over oxygen",
        ],
        "correct_index": 0,
        "why": "Brewing needs oxygen kept out so fermentation continues, while bread dough "
               "is left more openly until baking's heat ends the yeast's activity.",
    },
    {
        "id": "ks4-anaerobic-respiration-h16",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because yeast and muscle cells both start from "
               "glucose, their anaerobic respiration must release the same amount of ATP. "
               "Evaluate this argument.",
        "options": [
            "It is wrong; yeast releases far more ATP anaerobically than muscle does",
            "It is correct; the ATP yield is roughly the same low value in both "
            "organisms, even though the products differ",
            "It is wrong; muscle releases far more ATP anaerobically than yeast does, "
            "which is not supported by how little energy either pathway releases",
            "It is correct, but just because yeast and muscle cells are genetically "
            "identical",
        ],
        "correct_index": 1,
        "why": "Both pathways only partly break down glucose, so both release a similarly "
               "small amount of ATP, even though their end products differ.",
    },
    {
        "id": "ks4-anaerobic-respiration-h17",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fermenting yeast in a small brewing vat releases about 60 ATP by anaerobic "
               "respiration in an hour. Assuming roughly 2 ATP per glucose molecule, find "
               "how many glucose molecules were respired.",
        "options": [
            "About 60 molecules",
            "About 32 molecules",
            "About 30 molecules",
            "About 90 molecules",
        ],
        "correct_index": 2,
        "why": "60 ATP divided by 2 ATP per glucose gives about 30 molecules of glucose "
               "respired.",
    },
    {
        "id": "ks4-anaerobic-respiration-h18",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that switching an entire country's petrol supply to "
               "ethanol biofuel would be an unambiguous environmental improvement.",
        "options": [
            "It is correct; growing fuel crops has no drawback of any kind",
            "It is wrong; ethanol biofuel cannot be burned in any vehicle engine",
            "It is correct, since ethanol releases no carbon dioxide when it is burned, "
            "which ignores the farmland any fuel crop still has to occupy",
            "It is not that simple; the renewable fuel gained has to be weighed against "
            "the farmland lost to growing it",
        ],
        "correct_index": 3,
        "why": "A genuine evaluation weighs the renewable benefit against the real cost of "
               "the farmland the crop takes up.",
    },
    {
        "id": "ks4-anaerobic-respiration-h19",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed jar of fruit is found to have inflated slightly after being left in "
               "a warm room for a week. Suggest an explanation, and predict what a chemical "
               "test on the gas inside would show.",
        "options": [
            "Wild yeast on the fruit is fermenting its sugars; the gas would turn "
            "limewater cloudy, showing carbon dioxide",
            "The fruit is photosynthesising in the dark jar, producing oxygen inside it",
            "The fruit is respiring aerobically, so the gas would relight a splint",
            "The jar has simply warmed up and expanded, with no new gas produced",
        ],
        "correct_index": 0,
        "why": "Fermentation by wild yeast on the fruit produces carbon dioxide, which would "
               "turn limewater cloudy in the standard test.",
    },
    {
        "id": "ks4-anaerobic-respiration-h20",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a doctor treating a patient in severe oxygen shortage (for "
               "example after a heart attack) is concerned about a build-up of lactic acid "
               "in their tissues.",
        "options": [
            "Lactic acid build-up raises the tissues' oxygen supply back to normal",
            "Widespread anaerobic respiration lowers the pH of the tissues, disrupting "
            "enzymes throughout the body",
            "Lactic acid is directly toxic in a way unrelated to pH",
            "A build-up of lactic acid has no medical significance whatsoever",
        ],
        "correct_index": 1,
        "why": "Widespread anaerobic respiration lowers tissue pH, which can disrupt enzyme "
               "function throughout the body, not just in one muscle.",
    },
    {
        "id": "ks4-anaerobic-respiration-h21",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sprinter's calf muscle produces about 90 ATP through anaerobic respiration "
               "during a burst of activity. Estimate the number of glucose molecules this "
               "required, at roughly 2 ATP per molecule.",
        "options": [
            "About 90 molecules",
            "About 180 molecules",
            "About 45 molecules",
            "About 23 molecules",
        ],
        "correct_index": 2,
        "why": "90 ATP divided by 2 ATP per glucose gives about 45 molecules of glucose "
               "respired.",
    },
    {
        "id": "ks4-anaerobic-respiration-h22",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the reliability of anaerobic respiration as a long-term energy "
               "source with its reliability as a short-term one.",
        "options": [
            "It is equally reliable over both the short and long term",
            "It is more reliable long-term, since ATP yield rises the longer it continues",
            "It is unreliable in the short term, but perfectly reliable over a long "
            "period",
            "It is unreliable long-term, since ATP yield is low and lactic acid builds "
            "up; it is useful only for short bursts",
        ],
        "correct_index": 3,
        "why": "The low ATP yield and building lactic acid make anaerobic respiration "
               "workable only for short bursts, not as a long-term energy source.",
    },
    {
        "id": "ks4-anaerobic-respiration-h23",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant breeder develops a rice variety whose roots tolerate long periods of "
               "waterlogging far better than normal rice. Suggest what this variety's root "
               "cells must be better at.",
        "options": [
            "Coping with the effects of anaerobic respiration over an extended period",
            "Photosynthesising underwater without any light reaching them",
            "Absorbing extra oxygen directly from the surrounding floodwater",
            "Converting all of their glucose into cellulose instead of respiring it",
        ],
        "correct_index": 0,
        "why": "A waterlogging-tolerant variety must cope better with the effects of "
               "prolonged anaerobic respiration in its root cells.",
    },
    {
        "id": "ks4-anaerobic-respiration-h24",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an athlete who trains at high intensity develops a greater "
               "tolerance for lactic acid than an untrained person, even though both produce "
               "it in similar circumstances.",
        "options": [
            "Training removes lactic acid production from the muscle completely",
            "Repeated exposure adapts the trained athlete's muscles and enzymes to "
            "function despite a lower pH",
            "An untrained person's muscles produce no lactic acid",
            "Training raises the muscle's pH so high that lactic acid cannot form",
        ],
        "correct_index": 1,
        "why": "Repeated exposure during training adapts a trained athlete's muscles to keep "
               "functioning despite a lower pH than an untrained person could tolerate.",
    },
    {
        "id": "ks4-anaerobic-respiration-h25",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that fermentation is a purely modern invention, made "
               "possible only by scientific understanding of yeast.",
        "options": [
            "It is correct; fermented foods and drinks were unknown before the biology of "
            "yeast was discovered",
            "It is correct, since yeast itself was invented in a laboratory during the "
            "twentieth century",
            "It is wrong; bread, wine and beer have been made by fermentation for "
            "thousands of years, long before yeast's role was understood",
            "It is wrong; fermentation became possible once electricity was available",
        ],
        "correct_index": 2,
        "why": "People have fermented bread, wine and beer for thousands of years, long "
               "before yeast's biological role in the process was understood.",
    },
    {
        "id": "ks4-anaerobic-respiration-h26",
        "subtopic_slug": "anaerobic-respiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scientist compares two identical yeast cultures, one kept at 10°C and one "
               "at 30°C, both sealed away from oxygen. Predict which produces carbon dioxide "
               "faster, and explain.",
        "options": [
            "The 10°C culture, since cold speeds up any enzyme-controlled reaction",
            "Both equally, since temperature has no effect on fermentation",
            "Neither; yeast cannot ferment anything below 35°C",
            "The 30°C culture, since warmer conditions speed up the enzyme-controlled "
            "reactions of fermentation",
        ],
        "correct_index": 3,
        "why": "Warmer conditions, up to an optimum, speed up the enzyme-controlled "
               "reactions of fermentation, so the 30°C culture produces carbon dioxide "
               "faster.",
    },
]
