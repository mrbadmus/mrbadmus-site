"""Biology · Ecology — the MRB-338 expansion of `deforestation`.

One leaf only: AQA 8461 §4.7.3.4. The original twelve rows in `ecology__a.py`
take biofuel by name, the rainforest as the richest habitat, biodiversity
falling, photosynthesis by name, the two carbon routes together, a
single-species replanting, rising demand for rice land, the medicine argument,
a carbon-neutral biofuel claim, one 500 km² calculation, regrowth against
cattle, and a ten-million-tree promise.

This file takes what they leave. The recall band finishes the named drivers —
cattle ranching, soya, palm oil — and the method, slash and burn. The demand
then falls on the two things that separate a strong answer here from a weak
one: naming which of the two carbon effects is which, and understanding why
cleared rainforest land fails as farmland within a few years, because the
nutrients in a rainforest are in the biomass and not in the soil. Around that
sit the edge effects, selective logging against clear-felling, certification,
and arithmetic on hectares, rates and percentages.

The weight follows the CONTENT. `easier` stays at eight because the drivers
and consequences are a short closed list. `standard` and `harder` carry
twenty-two each, because each driver brings its own context, its own
trade-off and its own numbers.

⚠️ This leaf stays on FOREST CLEARANCE. The carbon cycle's own arrows belong
to `carbon-cycle`, peat and quarrying to `land-use`, and conservation
programmes to `maintaining-biodiversity`.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The named drivers, the method, the organisms that release the carbon
    # from felled wood, and what happens to a species that loses its forest.
    {
        "id": "ks4-deforestation-e05",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the farm animal most often grazed on land cleared from "
                "tropical forest.",
        "options": [
            "Goats",
            "Sheep",
            "Cattle",
            "Chickens",
        ],
        "correct_index": 2,
        "why": "Cattle ranching is one of the three reasons AQA names for "
               "large-scale tropical deforestation, alongside rice fields and "
               "biofuel crops.",
    },
    {
        "id": "ks4-deforestation-e06",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the method by which tropical forest is most often "
                "cleared quickly.",
        "options": [
            "Cutting the trees down and then burning what is left",
            "Flooding the forest floor until the trees drown slowly",
            "Spraying every tree with a fertiliser that stops its growth",
            "Removing all of the leaves and leaving the trunks standing in "
                "place",
        ],
        "correct_index": 0,
        "why": "Slash and burn fells the trees and burns the remains, which "
               "clears the ground in weeks and releases the stored carbon at "
               "the same time.",
    },
    {
        "id": "ks4-deforestation-e07",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the group of organisms that releases carbon dioxide as "
                "felled wood rots on the forest floor.",
        "options": [
            "Grasses, which take carbon from the timber through their "
                "roots",
            "Earthworms, which swallow the wood and change it into carbon "
                "dioxide",
            "Insects and spiders, which chew the wood into powder",
            "Microorganisms, which respire as they decay the wood",
        ],
        "correct_index": 3,
        "why": "Decay is a biological process: bacteria and fungi break the "
               "wood down and release carbon dioxide during their own "
               "respiration.",
    },
    {
        "id": "ks4-deforestation-e08",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a species becoming locally extinct.",
        "options": [
            "It has become so rare that only one individual is left "
                "worldwide",
            "It has died out in that area but survives somewhere else",
            "It has died out everywhere on Earth and cannot return",
            "It has moved to a new area and taken over from the species "
                "there",
        ],
        "correct_index": 1,
        "why": "Local extinction means the species is gone from that place; "
               "enough local extinctions, and the species is gone altogether.",
    },
    {
        "id": "ks4-deforestation-e09",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the oil crop grown on huge areas of cleared tropical "
                "forest in south-east Asia.",
        "options": [
            "Oil palm",
            "Linseed",
            "Sunflower",
            "Olive",
        ],
        "correct_index": 0,
        "why": "Oil palm plantations have replaced very large areas of "
               "tropical forest, and palm oil is used in food, cosmetics and "
               "fuel.",
    },
    {
        "id": "ks4-deforestation-e10",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the carbon that had been stored in a "
                "tree when that tree is burned.",
        "options": [
            "It sinks into the soil and stays there as solid carbon",
            "It is destroyed by the heat of the fire and ceases to exist",
            "It is taken up by each of the neighbouring trees through "
                "their roots",
            "It is released into the atmosphere as carbon dioxide",
        ],
        "correct_index": 3,
        "why": "Combustion oxidises the carbon in the wood, so it leaves the "
               "tree's biomass and enters the air as carbon dioxide.",
    },
    {
        "id": "ks4-deforestation-e11",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the crop, grown widely on cleared South American forest, "
                "that is used mainly to feed farm animals.",
        "options": [
            "Tea",
            "Soya",
            "Barley",
            "Cotton",
        ],
        "correct_index": 1,
        "why": "Soya grown on cleared land is exported as animal feed, so meat "
               "eaten far away drives forest clearance.",
    },
    {
        "id": "ks4-deforestation-e12",
        "subtopic_slug": "deforestation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by reforestation.",
        "options": [
            "Fencing a forest so that no person is allowed to enter it",
            "Clearing a forest completely so that crops can be planted on "
                "the land",
            "Planting trees again on land where forest used to grow",
            "Cutting selected mature trees and leaving the rest standing",
        ],
        "correct_index": 2,
        "why": "Reforestation restores tree cover to land that was forest, "
               "which begins to rebuild both the carbon store and the habitat.",
    },
    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Each driver and each consequence in a named context, with the first
    # arithmetic in hectares, rates and percentages.
    {
        "id": "ks4-deforestation-s05",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cleared rainforest land often gives good crops "
                "for two or three years and poor crops after that.",
        "options": [
            "Crops grown on cleared forest release a poison into the soil "
                "that builds up over several seasons",
            "The soil slowly cools each year until it is too cold for a "
                "tropical crop",
            "The nutrients were in the trees, and the ash from burning "
                "them is quickly used up",
            "The rainfall falls sharply as soon as the first crop is "
                "harvested",
        ],
        "correct_index": 2,
        "why": "In a rainforest most of the nutrients are held in the living "
               "biomass, not the soil, so once the ash is washed out or taken "
               "up the thin soil has little left.",
    },
    {
        "id": "ks4-deforestation-s06",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why removing trees from a steep slope leads to soil "
                "being washed away.",
        "options": [
            "Tree roots had bound the soil together and their leaves broke "
                "the force of the rain",
            "Trees had absorbed every drop of rain on the slope, so none "
                "reached the soil",
            "Trees had made the soil heavier by dropping leaves on it each "
                "wet season",
            "Trees had kept the slope frozen at night, which held the soil "
                "in place",
        ],
        "correct_index": 0,
        "why": "Roots hold the soil and the canopy shields it, so bare ground "
               "on a slope is exposed to rain that then carries the topsoil "
               "downhill.",
    },
    {
        "id": "ks4-deforestation-s07",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A region loses 4500 hectares of forest a year. Calculate the "
                "area lost over 12 years.",
        "options": [
            "5400 hectares",
            "540 000 hectares",
            "375 hectares",
            "54 000 hectares",
        ],
        "correct_index": 3,
        "why": "4500 hectares per year × 12 years = 54 000 hectares of forest "
               "lost.",
    },
    {
        "id": "ks4-deforestation-s08",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why clearing forest reduces the carbon dioxide "
                "removed from the atmosphere, even before anything is burned.",
        "options": [
            "The remaining trees close their stomata once their neighbours "
                "have been cut down beside them",
            "The felled trees can no longer photosynthesise, so they take "
                "in no more carbon dioxide",
            "The felled trees begin to respire much faster than they did "
                "while they were growing",
            "The bare soil left behind gives off carbon dioxide at a "
                "greater rate than the trees did",
        ],
        "correct_index": 1,
        "why": "A living tree removes carbon dioxide continuously; felling "
               "stops that uptake whatever is then done with the timber.",
    },
    {
        "id": "ks4-deforestation-s09",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare selective logging with clear-felling in terms of the "
                "habitat left behind.",
        "options": [
            "Selective logging leaves most of the forest standing; "
                "clear-felling removes it",
            "Selective logging removes more trees in total than "
                "clear-felling does",
            "Clear-felling leaves the canopy intact, so its species carry "
                "on",
            "The two leave the same habitat, as the same number of trees "
                "is taken",
        ],
        "correct_index": 0,
        "why": "Taking scattered mature trees keeps a functioning forest with "
               "its canopy and its species, while clear-felling replaces the "
               "habitat with open ground.",
    },
    {
        "id": "ks4-deforestation-s10",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a supermarket might pay more for timber carrying "
                "a sustainable forestry certificate.",
        "options": [
            "Certified timber is lighter, which saves the shop fuel money",
            "Certified timber must be sold within one year of felling",
            "Certified timber is stronger, because the trees are grown "
                "more slowly in a managed forest",
            "Customers want assurance the wood did not come from destroyed "
                "forest",
        ],
        "correct_index": 3,
        "why": "Certification is a market signal: it tells buyers the forest "
               "is being managed so that it continues to exist, and shoppers "
               "increasingly ask for it.",
    },
    {
        "id": "ks4-deforestation-s11",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a country far from the tropics can be responsible "
                "for tropical deforestation.",
        "options": [
            "Its weather systems dry the tropical forest each year",
            "It imports beef, soya and palm oil grown on the cleared land",
            "Its own forests are cleared first, which forces tropical "
                "countries to clear theirs as well",
            "Its carbon dioxide emissions travel south and kill the "
                "tropical trees directly",
        ],
        "correct_index": 1,
        "why": "Demand, not distance, drives clearance: the land is cleared to "
               "grow what distant markets buy.",
    },
    {
        "id": "ks4-deforestation-s12",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the edges of a cleared forest lose species even "
                "though the trees there are still standing.",
        "options": [
            "Species at the edge are eaten by the clearing machinery",
            "The edge receives far more rainfall than the interior, which "
                "drowns the roots of the trees",
            "The edge is drier, brighter and windier, so deep-forest "
                "species cannot live there",
            "The edge trees are felled first and then replanted in place",
        ],
        "correct_index": 2,
        "why": "An exposed edge has a different microclimate from the forest "
               "interior, so species adapted to deep shade and humidity are "
               "lost well inside the remaining trees.",
    },
    {
        "id": "ks4-deforestation-s13",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A forest of 80 000 hectares loses 12 000 hectares. Calculate "
                "the percentage of the forest that remains.",
        "options": [
            "15%",
            "68%",
            "12%",
            "85%",
        ],
        "correct_index": 3,
        "why": "12 000 ÷ 80 000 × 100 = 15% is lost, so 100 − 15 = 85% of the "
               "forest remains.",
    },
    {
        "id": "ks4-deforestation-s14",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why deforestation is described as having a double "
                "effect on atmospheric carbon dioxide.",
        "options": [
            "Both carbon dioxide and oxygen are released, and the two "
                "together warm the atmosphere",
            "Less is absorbed because the trees are gone, and more is "
                "released as they burn or rot",
            "Carbon dioxide is released twice over: once when the tree "
                "falls and once when the timber is sawn up",
            "The gas is released by the trees and again by the machinery "
                "brought in to clear the forest",
        ],
        "correct_index": 1,
        "why": "Felling removes a sink and creates a source at the same time, "
               "which is why the effect on the atmosphere is larger than "
               "either change alone.",
    },
    {
        "id": "ks4-deforestation-s15",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why people living in a forest may oppose a total ban "
                "on cutting any trees there.",
        "options": [
            "They are unable to grow food while the forest is still "
                "standing there",
            "They believe standing trees make the local climate colder",
            "They depend on the forest for timber, fuel and their income",
            "They want the forest cleared so more roads can be built",
        ],
        "correct_index": 2,
        "why": "Forest communities take building timber, firewood and cash "
               "crops from the forest, so a blanket ban removes their "
               "livelihood as well as the clearance.",
    },
    {
        "id": "ks4-deforestation-s16",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a hectare of tropical rainforest holds more "
                "species than a hectare of UK woodland.",
        "options": [
            "The tropical climate is warm and wet all year, so more niches "
                "exist and growth never stops",
            "The rainforest is much older than the woodland, and age "
                "decides its species count",
            "Tropical soils are far richer, so every plant grows much "
                "larger",
            "UK woodland is managed, and management removes half of the "
                "species",
        ],
        "correct_index": 0,
        "why": "Constant warmth and rainfall mean year-round productivity and "
               "a complex layered structure, which supports many more "
               "specialised species.",
    },
    {
        "id": "ks4-deforestation-s17",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why burning cleared forest on peat soil releases far "
                "more carbon dioxide than burning the trees alone.",
        "options": [
            "Peat contains oxygen, which allows a fire to spread right "
                "across the whole area",
            "The peat beneath also burns, and it holds a very large carbon "
                "store",
            "Peat soil makes the trees burn at a higher temperature",
            "Peat reflects heat upwards, so the trees burn for longer",
        ],
        "correct_index": 1,
        "why": "Peat is thousands of years of undecayed plant material; once "
               "alight it smoulders for months and releases carbon that the "
               "trees above never held.",
    },
    {
        "id": "ks4-deforestation-s18",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Forest is being cleared at 3 hectares per minute. Calculate "
                "the area cleared in one hour.",
        "options": [
            "60 hectares",
            "18 hectares",
            "180 hectares",
            "1800 hectares",
        ],
        "correct_index": 2,
        "why": "3 hectares per minute × 60 minutes = 180 hectares cleared in "
               "an hour.",
    },
    {
        "id": "ks4-deforestation-s19",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why replanting a cleared area restores the carbon "
                "store more quickly than it restores the biodiversity.",
        "options": [
            "Trees grow and take in carbon within years, while a forest "
                "community takes far longer",
            "Carbon is returned by the machinery used for planting, so the "
                "store is refilled immediately",
            "Biodiversity is measured only once a century, so any recovery "
                "is invisible until then",
            "Young trees hold more carbon than mature trees, so the store "
                "recovers before planting ends",
        ],
        "correct_index": 0,
        "why": "Biomass rebuilds as the trees grow, but the fungi, soil "
               "animals, understorey plants and specialist species of an old "
               "forest take many decades to return, if they return at all.",
    },
    {
        "id": "ks4-deforestation-s20",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how growing a biofuel crop on cleared forest can "
                "raise carbon dioxide levels rather than lowering them.",
        "options": [
            "Biofuel crops give off carbon dioxide during the day as well "
                "as at night",
            "Biofuel does not burn cleanly, so it releases twice the gas "
                "that petrol does",
            "The crop takes carbon dioxide from the soil instead of taking "
                "it from the air",
            "Clearing the forest released more carbon than the crop will "
                "save for many years",
        ],
        "correct_index": 3,
        "why": "The carbon released by felling and burning the forest is a "
               "large one-off debt, and the yearly saving from the fuel takes "
               "decades to pay it back.",
    },
    {
        "id": "ks4-deforestation-s21",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a road cut through a forest causes more clearance "
                "than the road itself removes.",
        "options": [
            "The road carries rainwater away, so the forest either side of "
                "it dies of drought",
            "The road is repainted each year, and the paint used damages "
                "the nearby canopy",
            "The road gives access, so logging and farming spread along it "
                "into the forest",
            "The road surface gives off a chemical that kills the trees "
                "for miles on either side of it",
        ],
        "correct_index": 2,
        "why": "Access is the limiting factor for clearance; once a road "
               "exists, timber can be taken out and produce brought back, so "
               "clearance follows the road.",
    },
    {
        "id": "ks4-deforestation-s22",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how deforestation can push a species towards "
                "extinction even when some forest is left.",
        "options": [
            "The remaining patches may be too small or too separate to "
                "hold a breeding population",
            "The remaining trees produce a scent that drives away every "
                "animal living among them",
            "Species that survive clearance become sterile within one "
                "generation of the felling",
            "The remaining forest is colder, and cold alone removes every "
                "species from a habitat",
        ],
        "correct_index": 0,
        "why": "A small isolated population loses individuals to chance events "
               "and cannot be topped up from elsewhere, so it can die out even "
               "though habitat remains.",
    },
    {
        "id": "ks4-deforestation-s23",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why satellite images are used to monitor tropical "
                "deforestation.",
        "options": [
            "They show the species present in each part of the forest, one "
                "individual at a time",
            "They record the temperature of each tree, which reveals which "
                "ones are about to be felled soon",
            "They are the one record a government is legally allowed to "
                "use in a forest dispute",
            "They cover vast, remote areas repeatedly, so change can be "
                "measured over time",
        ],
        "correct_index": 3,
        "why": "Much cleared forest is far from any road, and repeated imaging "
               "gives a consistent measure of how much cover has been lost and "
               "where.",
    },
    {
        "id": "ks4-deforestation-s24",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One hectare of rainforest holds 200 tonnes of carbon. "
                "Calculate the carbon released if 350 hectares are cleared and "
                "burned.",
        "options": [
            "550 tonnes",
            "70 000 tonnes",
            "7000 tonnes",
            "1750 tonnes",
        ],
        "correct_index": 1,
        "why": "200 tonnes per hectare × 350 hectares = 70 000 tonnes of "
               "carbon released.",
    },
    {
        "id": "ks4-deforestation-s25",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why replacing rainforest with cattle pasture reduces "
                "the number of species far more than replacing it with "
                "regrowing forest.",
        "options": [
            "Pasture is a single grass species kept short, so almost "
                "nothing else can live there",
            "Cattle eat every species of animal they come across when "
                "grazing",
            "Regrowing forest is planted with each original species, "
                "returned by hand",
            "Pasture soil is acidic, and acid soil supports no organism",
        ],
        "correct_index": 0,
        "why": "Grazed pasture is close to a monoculture with no structure "
               "above the grass, while even young regrowth offers shelter, "
               "food and layers for many species.",
    },
    {
        "id": "ks4-deforestation-s26",
        "subtopic_slug": "deforestation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why reducing food waste in wealthy countries can slow "
                "tropical deforestation.",
        "options": [
            "Wasted food is shipped to the tropics and dumped on the "
                "forest floor",
            "Rotting food waste gives off a gas that kills tropical trees",
            "Food waste is burned in power stations built on cleared "
                "rainforest",
            "Less food needs to be grown, so less land has to be cleared "
                "for crops and grazing",
        ],
        "correct_index": 3,
        "why": "Clearance is driven by demand for land to grow food; if less "
               "of what is grown is thrown away, the same diet needs less "
               "land.",
    },
    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Weighing the drivers against each other, multi-step arithmetic on
    # areas and rates, and claims about offsetting held up to what a forest
    # actually is.
    {
        "id": "ks4-deforestation-h05",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country's forest fell from 25 million hectares to 19 "
                "million hectares in 30 years. Determine the mean rate of loss "
                "per year.",
        "options": [
            "2 000 000 hectares per year",
            "20 000 hectares per year",
            "200 000 hectares per year",
            "600 000 hectares per year",
        ],
        "correct_index": 2,
        "why": "The loss is 25 − 19 = 6 million hectares, and 6 000 000 ÷ 30 = "
               "200 000 hectares per year.",
    },
    {
        "id": "ks4-deforestation-h06",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a palm oil plantation replaces the "
                "rainforest it was cleared from, because both are covered in "
                "trees.",
        "options": [
            "It is weak, because one planted species supports a tiny "
                "fraction of the forest's life",
            "It is sound, because a plantation holds more carbon than old "
                "forest",
            "It is weak, because oil palms cannot photosynthesise in the "
                "tropical sunlight they grow in",
            "It is sound, because tree cover decides how many species live "
                "there",
        ],
        "correct_index": 0,
        "why": "A rainforest is a layered community of thousands of species; "
               "an even-aged single-species plantation supports very few of "
               "them and stores less carbon.",
    },
    {
        "id": "ks4-deforestation-h07",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a country can report that its total forest area "
                "is stable while its biodiversity is still falling.",
        "options": [
            "Biodiversity is counted in a different unit from area, so the "
                "two figures cannot both be right",
            "Forest area is measured from the ground and biodiversity from "
                "the air, so they disagree",
            "Trees are counted twice in the total, which makes the "
                "reported area seem to stay the same",
            "Old natural forest is being replaced by plantation of the "
                "same area but far fewer species",
        ],
        "correct_index": 3,
        "why": "Area counts hectares of trees; it does not distinguish ancient "
               "rainforest from a young plantation, so the total can hold "
               "while what lives there collapses.",
    },
    {
        "id": "ks4-deforestation-h08",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect on carbon dioxide of felling a forest and "
                "leaving the wood to rot with felling it and burning the wood.",
        "options": [
            "Burning releases less overall, because the carbon that "
                "remains is locked into the ash on the ground below",
            "Burning releases it quickly; rotting releases a similar "
                "amount over years",
            "Rotting releases far more in total, because the decomposers "
                "add carbon of their own to the wood",
            "Rotting releases nothing, because wood left alone simply "
                "returns to the soil beneath it",
        ],
        "correct_index": 1,
        "why": "Both routes oxidise the same carbon back to carbon dioxide; "
               "the difference is the rate, not the total.",
    },
    {
        "id": "ks4-deforestation-h09",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cleared hectare yields 1.5 tonnes of beef over its whole "
                "productive life, and 40 hectares are cleared. Determine the "
                "total beef yield.",
        "options": [
            "60 tonnes",
            "600 tonnes",
            "41.5 tonnes",
            "26.7 tonnes",
        ],
        "correct_index": 0,
        "why": "1.5 tonnes per hectare × 40 hectares = 60 tonnes of beef in "
               "total.",
    },
    {
        "id": "ks4-deforestation-h10",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the argument that tropical countries should not be "
                "asked to stop clearing forest while wealthy countries cleared "
                "their own long ago.",
        "options": [
            "It has no force, because forests cleared in the past have all "
                "since been replanted in full",
            "It settles the matter, because no country may comment on what "
                "another country does with its land",
            "It has no force, because temperate forest and tropical forest "
                "hold exactly the same species",
            "It has real force, but the loss is global, so the answer is "
                "support rather than a demand",
        ],
        "correct_index": 3,
        "why": "The historical point is fair, which is why the practical "
               "answer is payment and technology transfer for conservation "
               "rather than a simple instruction.",
    },
    {
        "id": "ks4-deforestation-h11",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to the species in a forest reserve of "
                "200 hectares that is completely surrounded by soya fields.",
        "options": [
            "Numbers rise, because the fields keep every predator out",
            "Numbers fall over time, as losses cannot be replaced from "
                "other forest",
            "Numbers rise, because the soya crop gives the forest species "
                "an extra source of food all year",
            "Numbers stay the same, because the reserve was not cleared",
        ],
        "correct_index": 1,
        "why": "Isolation stops immigration, so each chance local extinction "
               "is permanent and the species list shortens even though the "
               "habitat is intact.",
    },
    {
        "id": "ks4-deforestation-h12",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why clearing forest for cattle produces far less "
                "human food per hectare than clearing it for crops.",
        "options": [
            "Crops are harvested several times a day, while cattle can be "
                "harvested only once",
            "Cattle take in no energy from their food, so their meat "
                "contains none of the crop's energy",
            "Most of the energy the cattle eat is lost in respiration and "
                "movement, not stored as meat",
            "Cattle refuse to eat any plant that has been grown on cleared "
                "tropical forest land",
        ],
        "correct_index": 2,
        "why": "Adding a trophic level costs most of the energy, so feeding "
               "people directly on crops needs a small fraction of the land "
               "that beef does.",
    },
    {
        "id": "ks4-deforestation-h13",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A forest absorbs 12 tonnes of carbon dioxide per hectare per "
                "year. Determine the annual absorption lost when 2500 hectares "
                "are cleared.",
        "options": [
            "3000 tonnes per year",
            "300 000 tonnes per year",
            "208 tonnes per year",
            "30 000 tonnes per year",
        ],
        "correct_index": 3,
        "why": "12 tonnes per hectare × 2500 hectares = 30 000 tonnes of "
               "carbon dioxide no longer absorbed each year.",
    },
    {
        "id": "ks4-deforestation-h14",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate a scheme that pays a landowner each year to leave "
                "forest standing, rather than buying the land outright.",
        "options": [
            "It protects the forest better than purchase, since a bought "
                "forest may be cleared by its owner",
            "It costs less at the start, but protection lasts only while "
                "the payments continue",
            "It protects the forest for ever, because a single payment "
                "settles the matter permanently",
            "It is worthless, because no landowner anywhere would accept "
                "money to leave land unused",
        ],
        "correct_index": 1,
        "why": "Annual payments are affordable and quick to start, but they "
               "create no permanent protection: the incentive ends the moment "
               "the funding does.",
    },
    {
        "id": "ks4-deforestation-h15",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the loss of a pollinating insect species can "
                "damage a forest that is otherwise left standing.",
        "options": [
            "Pollinators supply the trees with mineral ions, which they "
                "cannot take up from the soil",
            "The insect had produced the carbon dioxide that the forest "
                "trees were using to photosynthesise",
            "Plants that depended on it set no seed, so those tree species "
                "fail to regenerate",
            "The insect had been feeding on the leaves, and without it the "
                "trees grow too large",
        ],
        "correct_index": 2,
        "why": "Many rainforest trees are pollinated by one or a few "
               "specialist species, so losing the pollinator ends reproduction "
               "for those trees even where the adults survive.",
    },
    {
        "id": "ks4-deforestation-h16",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Of 30 million hectares of original forest, 40% has been "
                "cleared. Determine the area remaining.",
        "options": [
            "18 million hectares",
            "40 million hectares",
            "7.5 million hectares",
            "12 million hectares",
        ],
        "correct_index": 0,
        "why": "40% of 30 million is 12 million cleared, so 30 − 12 = 18 "
               "million hectares remain.",
    },
    {
        "id": "ks4-deforestation-h17",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare planting one large 1000 hectare block of new forest "
                "with planting ten separate 100 hectare blocks.",
        "options": [
            "The ten blocks support more species, because each is small "
                "enough to be managed closely",
            "The large block supports more deep-forest species, as it has "
                "proportionally less edge",
            "The ten blocks support more species, because ten habitats are "
                "always richer than one",
            "The two are equal, because exactly 1000 hectares in total is "
                "planted in each one of the two cases",
        ],
        "correct_index": 1,
        "why": "Edge conditions penetrate a fixed distance, so small blocks "
               "are almost all edge, while one large block has a genuine "
               "interior that deep-forest species need.",
    },
    {
        "id": "ks4-deforestation-h18",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a ban on clearing forest in one country can lead "
                "to more clearing in a neighbouring country.",
        "options": [
            "The banned country exports its cleared soil to its neighbour, "
                "which then has to clear more",
            "A ban makes timber cheaper worldwide, so far less of it is "
                "needed anywhere",
            "The demand for the land's produce has not changed, so "
                "production moves across the border",
            "Forests grow across borders, so banning clearance on one side "
                "makes the other side grow faster",
        ],
        "correct_index": 2,
        "why": "Unless demand falls, a restriction in one place simply shifts "
               "the clearance somewhere with weaker rules, which is why action "
               "on the demand side matters.",
    },
    {
        "id": "ks4-deforestation-h19",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why regrowth on abandoned cleared land does not "
                "always return to rainforest.",
        "options": [
            "Thin soil, distant seed sources and repeated fires can hold "
                "it as scrub or grassland",
            "Rainforest seeds cannot germinate on ground that people have "
                "farmed",
            "The region's climate changes permanently once the first "
                "hectare goes",
            "Regrowth is cut again within a year, so nothing has returned",
        ],
        "correct_index": 0,
        "why": "Recovery needs seed, soil and time; degraded soil, no nearby "
               "parent trees and recurring fire can lock the land into a "
               "different, poorer community.",
    },
    {
        "id": "ks4-deforestation-h20",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the suggestion that biofuel from cleared forest is "
                "still better than petrol because it comes from plants.",
        "options": [
            "It is sound, because any fuel made from a plant is carbon "
                "neutral from the moment it is first burned",
            "It is sound: plants absorb carbon dioxide and petrol does not",
            "It is weak, because burning biofuel releases far more carbon "
                "dioxide per litre than petrol releases",
            "It is weak: the clearance debt can outweigh the saving for "
                "decades",
        ],
        "correct_index": 3,
        "why": "The carbon released in clearing is counted against the fuel, "
               "and on newly cleared forest that debt can take decades of "
               "yearly savings to repay.",
    },
    {
        "id": "ks4-deforestation-h21",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the number of species lost to deforestation "
                "cannot be counted exactly.",
        "options": [
            "Counting species is banned in tropical forests, so no figure "
                "is collected for any of them",
            "Every species lost from one forest survives in another one, "
                "so the true figure is zero each time",
            "Many rainforest species have never been described, so losses "
                "cannot be recorded",
            "Species are counted once a century, so most of the losses "
                "fall between the counts",
        ],
        "correct_index": 2,
        "why": "A large share of tropical species are unknown to science, so "
               "some are lost before they are ever named and no count can "
               "include them.",
    },
    {
        "id": "ks4-deforestation-h22",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Clearing 1 hectare releases 500 tonnes of carbon dioxide, and "
                "replanting absorbs 10 tonnes per hectare per year. Determine "
                "the years needed to repay one hectare.",
        "options": [
            "50 years",
            "500 years",
            "5000 years",
            "5 years",
        ],
        "correct_index": 0,
        "why": "500 tonnes ÷ 10 tonnes per year = 50 years of regrowth to "
               "absorb what clearing one hectare released.",
    },
    {
        "id": "ks4-deforestation-h23",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the biodiversity value of protecting 100 hectares of "
                "untouched rainforest with replanting 100 hectares of cleared "
                "land.",
        "options": [
            "Replanting is worth more, as new trees grow faster",
            "The two are equal, because the same area of forest exists at "
                "the end in both of the cases",
            "Replanting is worth more, because the species can be chosen "
                "to suit the local conditions there",
            "Protection keeps a community that replanting would take "
                "centuries to rebuild",
        ],
        "correct_index": 3,
        "why": "An intact forest's soil fungi, dead wood, understorey and "
               "specialist species cannot be planted; protecting what exists "
               "is the cheaper and surer option.",
    },
    {
        "id": "ks4-deforestation-h24",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why clearance rates often rise when the world price "
                "of beef or soya rises.",
        "options": [
            "A price rise forces governments to sell forest land",
            "Clearing land becomes more profitable, so more of it is "
                "cleared",
            "High prices mean cattle eat more, so more pasture is needed",
            "Expensive crops grow larger, so each one needs a greater area "
                "of cleared ground to itself",
        ],
        "correct_index": 1,
        "why": "Clearance is an economic decision, so anything that raises the "
               "return on the cleared land raises the rate at which it is "
               "cleared.",
    },
    {
        "id": "ks4-deforestation-h25",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why felling an old tree and planting a sapling in its "
                "place does not keep the carbon store unchanged.",
        "options": [
            "The sapling holds a tiny fraction of the carbon, and the "
                "felled tree's carbon is released",
            "The sapling holds more carbon than the old tree did, so the "
                "store grows larger",
            "Saplings take in no carbon dioxide until they are fully grown",
            "The old tree's carbon passes into the sapling through the "
                "soil",
        ],
        "correct_index": 0,
        "why": "Carbon storage depends on biomass; a young tree holds almost "
               "none of what a mature tree held, and the felled tree's carbon "
               "is released as its timber is burned or rots.",
    },
    {
        "id": "ks4-deforestation-h26",
        "subtopic_slug": "deforestation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that deforestation is a problem only for "
                "the countries where the forests grow.",
        "options": [
            "It is sound, because carbon dioxide released in the tropics "
                "stays above the tropics and goes no further",
            "It is sound: species in one country are of no value to "
                "another",
            "It is weak, because the countries with forests are the ones "
                "that buy the products grown there",
            "It is weak: the carbon released and the species lost affect "
                "everyone",
        ],
        "correct_index": 3,
        "why": "The atmosphere is shared, the species lost are part of global "
               "biodiversity, and the demand driving clearance comes largely "
               "from elsewhere.",
    },
]
