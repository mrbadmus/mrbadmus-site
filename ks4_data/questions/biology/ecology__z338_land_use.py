"""Biology · Ecology — the MRB-338 expansion of `land-use`.

One leaf only: AQA 8461 §4.7.3.3. The original twelve rows in `ecology__a.py`
take waterlogging and decay, peat sold as compost, the thousand-year
timescale, the gas released by drained peat, the two harms together, a quarry
on grassland, why a bog stores carbon, a landfill on farmland, the
'only carbon dioxide' evaluation, re-wetting, brownfield against meadow, and a
garden centre's replanting claim.

This file takes what they leave. The recall band finishes the four named land
uses the baseline never lists in full — building, quarrying, farming and waste
disposal — along with peat-free compost, the bog's own species, and peat as a
fuel. The demand then falls on the two things a pupil actually has to do with
this spec point: weigh one land use against another for the habitat it costs,
and work in hectares and percentages, where a bog accumulating a millimetre a
year and a field measured in hectares are the two numbers the topic supplies.

The weight follows the CONTENT. `easier` stays at eight — the land uses are a
short list and a ninth recall row repeats the eighth. `standard` and `harder`
carry twenty-two each, because every land use generates its own context, its
own trade-off and its own arithmetic.

⚠️ This leaf stays on LAND AREA and on peat. Pollution belongs to
`waste-management`, conservation programmes to `maintaining-biodiversity`, and
forest clearance to `deforestation`; where those subjects touch, the task here
is about the ground being used up.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The four named land uses, peat-free compost, peat as fuel, the bog's
    # own species, and what happens to the species on land that is built on.
    {
        "id": "ks4-land-use-e05",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the four main ways in which humans use up land that "
                "other species could live on.",
        "options": [
            "Breathing, feeding, drinking and sheltering from the weather",
            "Recycling, composting, insulating and generating electricity",
            "Building, quarrying, farming and dumping waste",
            "Walking, cycling and camping in the countryside",
        ],
        "correct_index": 2,
        "why": "Building, quarrying, farming and landfill all take ground that "
               "was habitat, which is why they reduce the space available to "
               "wild species.",
    },
    {
        "id": "ks4-land-use-e06",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a gardener should buy instead of peat compost in "
                "order to protect peat bogs.",
        "options": [
            "Peat-free compost, made from bark, wood fibre or garden waste",
            "Compost dug from the deepest layer of a large undisturbed "
                "peat bog",
            "Compost sold as peat-reduced, which is about half peat by "
                "volume",
            "Compost made from the peat of a bog that has already been "
                "fully drained first",
        ],
        "correct_index": 0,
        "why": "Peat-free compost is made from materials that renew quickly, "
               "so buying it leaves the bog and its stored carbon in place.",
    },
    {
        "id": "ks4-land-use-e07",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one use of dried peat other than as compost.",
        "options": [
            "It is spun into textiles",
            "It is smelted into metal",
            "It is pressed into glass",
            "It is burned as a fuel",
        ],
        "correct_index": 3,
        "why": "Dried peat has been cut and burned as a fuel for centuries, "
               "which releases its stored carbon as carbon dioxide.",
    },
    {
        "id": "ks4-land-use-e08",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the moss that builds up over thousands of years to form "
                "most of a peat bog.",
        "options": [
            "Lichen",
            "Sphagnum moss",
            "Bracken",
            "Seaweed",
        ],
        "correct_index": 1,
        "why": "Sphagnum moss grows in waterlogged ground and its partly "
               "decayed remains accumulate as peat.",
    },
    {
        "id": "ks4-land-use-e09",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the plants and animals living on a "
                "field when a housing estate is built on it.",
        "options": [
            "Their habitat is destroyed, so most of them are lost from "
                "that site",
            "They move into the houses and continue to live exactly as "
                "before",
            "Nothing changes, because building work takes place above the "
                "soil",
            "Their numbers rise, because gardens give them extra food and "
                "shelter all year",
        ],
        "correct_index": 0,
        "why": "The ground is covered by buildings and roads, so the habitat "
               "those species depended on no longer exists there.",
    },
    {
        "id": "ks4-land-use-e10",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by a brownfield site.",
        "options": [
            "An area of moorland where the heather has recently been "
                "burned off",
            "A stretch of farmland whose soil has a very high content of "
                "clay",
            "A field left bare of crops for a whole year so that the soil "
                "can recover",
            "Land that has already been built on or used by industry "
                "before",
        ],
        "correct_index": 3,
        "why": "A brownfield site is previously developed land, so building "
               "there costs far less wildlife habitat than building on an "
               "undisturbed green site.",
    },
    {
        "id": "ks4-land-use-e11",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the land use in which rock and minerals are dug out of "
                "the ground for building materials.",
        "options": [
            "Coppicing",
            "Quarrying",
            "Ploughing",
            "Draining",
        ],
        "correct_index": 1,
        "why": "Quarrying removes rock for building stone, aggregate and "
               "cement, and takes the habitat above it with the rock.",
    },
    {
        "id": "ks4-land-use-e12",
        "subtopic_slug": "land-use",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which single human land use takes up the largest area "
                "of the United Kingdom.",
        "options": [
            "Airports, docks and the land set aside around them",
            "Quarries and open-cast mines dug for building stone and for "
                "coal",
            "Agriculture, which covers most of the country's land",
            "Landfill sites where household waste is buried",
        ],
        "correct_index": 2,
        "why": "Farmland covers about seventy per cent of the UK, so "
               "agriculture is by far the largest single claim on land that "
               "wild species could use.",
    },
    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Each land use in a named context, the bog's mechanism, and the first
    # arithmetic in hectares and percentages.
    {
        "id": "ks4-land-use-s05",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why building a car park on a meadow reduces "
                "biodiversity more than mowing the same meadow does.",
        "options": [
            "Mowing removes the flowers permanently, so the meadow can "
                "never recover from being cut",
            "Mowing kills the roots of the plants, while tarmac leaves "
                "them alive underneath the surface",
            "Tarmac seals the ground, so nothing can grow, while a mown "
                "meadow still supports plants",
            "Cars give off gases that fertilise the soil under the car "
                "park and help plants to grow",
        ],
        "correct_index": 2,
        "why": "A mown meadow is still a habitat, but a sealed surface removes "
               "light, water and rooting space, so the habitat is gone "
               "altogether.",
    },
    {
        "id": "ks4-land-use-s06",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Peat builds up at about 1 mm each year. Calculate the number "
                "of years needed to form a peat layer 2 m deep.",
        "options": [
            "2000 years",
            "20 000 years",
            "20 years",
            "200 years",
        ],
        "correct_index": 0,
        "why": "2 m is 2000 mm, and at 1 mm per year that takes 2000 years to "
               "accumulate.",
    },
    {
        "id": "ks4-land-use-s07",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why draining a peat bog, without digging any peat "
                "out, still releases carbon dioxide.",
        "options": [
            "Draining exposes the peat to sunlight, and light breaks the "
                "carbon compounds apart",
            "The drainage ditches are dug by machines, and their engines "
                "release the gas",
            "Draining lets the water carry dissolved carbon straight up "
                "into the air above the bog",
            "Air enters the drained peat, so decomposers can respire and "
                "break it down",
        ],
        "correct_index": 3,
        "why": "Waterlogging had kept oxygen out and stopped decay; once the "
               "bog is drained, aerobic decomposers respire the stored organic "
               "matter and release carbon dioxide.",
    },
    {
        "id": "ks4-land-use-s08",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a species of wading bird that nests only on open "
                "bog is at particular risk from peat extraction.",
        "options": [
            "Wading birds are unable to fly far enough to reach another "
                "suitable bog site",
            "It has nowhere else to nest, because it will nest only on "
                "open bog",
            "Peat extraction machinery makes a noise that deafens the "
                "nesting birds",
            "The birds eat peat directly, and extraction removes their "
                "food",
        ],
        "correct_index": 1,
        "why": "A specialist species depends on one habitat, so destroying "
               "that habitat removes everywhere it can breed rather than just "
               "one of many options.",
    },
    {
        "id": "ks4-land-use-s09",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farm of 40 hectares has 6 hectares taken for a new road. "
                "Calculate the percentage of the farm that is lost.",
        "options": [
            "15%",
            "24%",
            "40%",
            "6%",
        ],
        "correct_index": 0,
        "why": "6 ÷ 40 × 100 = 15% of the farm's area is taken by the road.",
    },
    {
        "id": "ks4-land-use-s10",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why ploughing permanent grassland to grow wheat "
                "lowers the number of species on that land.",
        "options": [
            "Ploughing turns the soil upside down, and soil cannot support "
                "life once inverted",
            "Wheat grows so tall that no sunlight reaches the ground in "
                "the whole field",
            "Wheat gives off a substance that poisons the soil beneath it "
                "and kills other plants",
            "A ploughed field holds one crop where the grassland held many "
                "plants and the animals using them",
        ],
        "correct_index": 3,
        "why": "Old grassland carries many plant species and the insects, "
               "birds and mammals that depend on them; a wheat field is a "
               "single species and supports very few.",
    },
    {
        "id": "ks4-land-use-s11",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a peat bog holds more carbon per hectare than a "
                "well-drained woodland soil of the same area.",
        "options": [
            "Peat is a rock, and rock holds far more carbon than soil ever "
                "does",
            "Decay is very slow in the waterlogged bog, so remains "
                "accumulate",
            "Bog plants photosynthesise much faster than trees do in every "
                "season",
            "Woodland soil is washed through by the rain, which dissolves "
                "its carbon away",
        ],
        "correct_index": 1,
        "why": "In the bog the lack of oxygen almost stops decomposition, so "
               "dead plant material piles up instead of being respired back "
               "into the air.",
    },
    {
        "id": "ks4-land-use-s12",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe two effects on wildlife of opening a new limestone "
                "quarry on a hillside of rough grassland.",
        "options": [
            "Rainfall in the area rises, and the wetter ground suits a "
                "wider range of plants",
            "The rock shelters the valley from wind, so more insect "
                "species settle nearby",
            "The hillside habitat is removed, and dust and noise disturb "
                "the area around it",
            "The soil becomes richer, and the extra minerals let more "
                "species grow on the hill",
        ],
        "correct_index": 2,
        "why": "Quarrying strips the vegetation and soil from the worked area, "
               "and the noise, traffic and dust reduce the quality of the "
               "habitat that remains beside it.",
    },
    {
        "id": "ks4-land-use-s13",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why converting a garden lawn to a paved driveway "
                "affects the local wildlife.",
        "options": [
            "Paving reflects sunlight upwards, which stops nearby plants "
                "photosynthesising at all",
            "Paving holds rainwater on the surface, which drowns the "
                "animals living in the garden",
            "Paving raises the ground temperature so much that the insects "
                "living there are unable to survive",
            "Paving removes the soil surface, so plants, insects and the "
                "birds feeding on them are lost",
        ],
        "correct_index": 3,
        "why": "A lawn and its soil support plants, invertebrates and the "
               "birds that feed on them; a sealed surface supports none of "
               "them, and many small losses add up across a town.",
    },
    {
        "id": "ks4-land-use-s14",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A drained peat bog releases 20 tonnes of carbon dioxide per "
                "hectare each year. Calculate the mass released by 35 hectares "
                "in one year.",
        "options": [
            "55 tonnes",
            "700 tonnes",
            "7000 tonnes",
            "175 tonnes",
        ],
        "correct_index": 1,
        "why": "20 tonnes per hectare × 35 hectares = 700 tonnes of carbon "
               "dioxide in the year.",
    },
    {
        "id": "ks4-land-use-s15",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a landfill site continues to affect wildlife long "
                "after it stops taking waste.",
        "options": [
            "Buried waste keeps the soil above it so cold that nothing "
                "roots",
            "The site is fenced, and the fence is what stops species "
                "returning",
            "Waste buried there breaks down slowly, and liquids can seep "
                "into soil and water",
            "Lorries keep arriving at the site for decades after it closes",
        ],
        "correct_index": 2,
        "why": "Decomposition in a landfill goes on for decades, producing gas "
               "and a liquid that can contaminate the soil and the water "
               "around the site.",
    },
    {
        "id": "ks4-land-use-s16",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why peat extraction is described as removing a "
                "habitat that cannot simply be put back.",
        "options": [
            "The peat took thousands of years to form, so it cannot be "
                "replaced",
            "The bog's own species become extinct worldwide once the bog "
                "has been cut over",
            "The ground left behind is toxic, so no plant can ever grow "
                "there again",
            "Peat is made in a factory, so a bog cannot be rebuilt by hand",
        ],
        "correct_index": 0,
        "why": "The habitat depends on a depth of peat that accumulated over "
               "millennia, and no management can rebuild that within a human "
               "lifetime.",
    },
    {
        "id": "ks4-land-use-s17",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why building new homes on brownfield land is often "
                "more expensive than building on a green field.",
        "options": [
            "Brownfield sites are much further from any town or city",
            "Old structures and contaminated ground must be cleared first",
            "Brownfield land is owned by the government and cannot be "
                "bought",
            "Building regulations do not apply on a green field",
        ],
        "correct_index": 1,
        "why": "Demolition, and cleaning up contamination left by earlier "
               "industry, both add cost, which is why developers press for "
               "green sites even though those cost more habitat.",
    },
    {
        "id": "ks4-land-use-s18",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how recycling more household waste reduces the amount "
                "of land humans take from other species.",
        "options": [
            "Recycling makes waste lighter, so the same landfill holds "
                "more of it forever",
            "Recycling centres are built on land that wild species cannot "
                "use for anything",
            "Less waste is buried, so fewer new landfill sites need to be "
                "dug",
            "Recycled materials break down faster, so landfill empties "
                "sooner",
        ],
        "correct_index": 2,
        "why": "Landfill takes land, and reducing the volume buried means "
               "fewer and smaller sites, leaving more ground as habitat.",
    },
    {
        "id": "ks4-land-use-s19",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A garden centre labels one compost 'peat-reduced'. Explain "
                "why this is better for bogs than ordinary compost but not as "
                "good as peat-free.",
        "options": [
            "It contains less peat, so less bog is cut, but some is still "
                "cut",
            "It contains no peat but is dug from the very edge of a bog "
                "instead",
            "It contains more peat than usual, but taken from a much "
                "smaller bog area",
            "It contains the same peat but is sold in a much smaller paper "
                "bag",
        ],
        "correct_index": 0,
        "why": "A reduced-peat mix still depends on bog being dug, just less "
               "of it; only a peat-free mix takes none at all.",
    },
    {
        "id": "ks4-land-use-s20",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the loss of a small area of peat bog matters more "
                "than the loss of the same area of arable field.",
        "options": [
            "The bog covers a larger area than an arable field of that "
                "size",
            "Arable fields are owned by farmers, so no wild species is hit",
            "The bog can be rebuilt within a year, so protect it first",
            "The bog is a rare habitat holding specialist species and "
                "stored carbon",
        ],
        "correct_index": 3,
        "why": "An arable field already carries few species and little stored "
               "carbon, while a bog carries specialists found nowhere else and "
               "a very large carbon store.",
    },
    {
        "id": "ks4-land-use-s21",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a worked-out quarry can be made useful to "
                "wildlife again.",
        "options": [
            "Cover the whole quarry floor in concrete so that it is safe "
                "to walk on",
            "Leave it fenced and untouched, since quarries suit no species",
            "Flood it or replant it, so pools and bare rock become new "
                "habitat",
            "Refill it with household waste so that the ground is returned "
                "to its old level",
        ],
        "correct_index": 2,
        "why": "Restored quarries make valuable habitat: flooded pits become "
               "wetlands, and the bare rock faces suit plants and nesting "
               "birds that need open ground.",
    },
    {
        "id": "ks4-land-use-s22",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the amount of land available to wild species "
                "falls as the human population grows.",
        "options": [
            "More people need homes, food and materials, all of which need "
                "land",
            "More people means more noise, and noise on its own removes "
                "habitats",
            "More people means warmer towns, and that warmth kills wild "
                "species",
            "More people breathe out carbon dioxide, and that gas drives "
                "wild species away",
        ],
        "correct_index": 0,
        "why": "Every extra person needs housing, food grown on farmland and "
               "materials quarried from the ground, so the pressure on land "
               "rises with population.",
    },
    {
        "id": "ks4-land-use-s23",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why re-wetting a drained bog is described as "
                "protecting carbon rather than removing it from the air.",
        "options": [
            "Re-wetting turns the released carbon dioxide back into solid "
                "peat within months",
            "It has no effect on carbon, and is done for the bog's wading "
                "birds",
            "The water absorbs carbon dioxide straight out of the air "
                "above it",
            "It stops further decay of the peat that is left, but does not "
                "recapture what has already gone",
        ],
        "correct_index": 3,
        "why": "Flooding excludes oxygen and halts the decay, so the remaining "
               "store is kept — but the carbon already respired into the "
               "atmosphere is not brought back.",
    },
    {
        "id": "ks4-land-use-s24",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A nature reserve of 180 hectares loses 27 hectares to a new "
                "bypass. Calculate the percentage of the reserve remaining.",
        "options": [
            "15%",
            "85%",
            "73%",
            "153%",
        ],
        "correct_index": 1,
        "why": "27 ÷ 180 × 100 = 15% is lost, so 100 − 15 = 85% of the reserve "
               "remains.",
    },
    {
        "id": "ks4-land-use-s25",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a supermarket may choose to sell only peat-free "
                "compost even though peat compost is cheaper to buy in.",
        "options": [
            "Customers increasingly expect the shop to avoid damaging bogs",
            "Peat compost grows plants far worse than any peat-free "
                "mixture",
            "Peat-free compost weighs less, and so it is much cheaper to "
                "transport",
            "Peat compost is illegal to sell anywhere in the United "
                "Kingdom",
        ],
        "correct_index": 0,
        "why": "Public concern about peat bogs makes the choice a commercial "
               "one as well as an environmental one, so shops respond to what "
               "customers want.",
    },
    {
        "id": "ks4-land-use-s26",
        "subtopic_slug": "land-use",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why planting a green roof on a new building does not "
                "fully replace the habitat lost beneath it.",
        "options": [
            "Green roofs have to be watered, and watering washes away all "
                "the soil each year",
            "The roof is set too high for any insect or bird to be able to "
                "reach it from the ground below",
            "Green roofs are on top of the building, so their plants get "
                "no sunlight at all",
            "A thin roof layer suits few species, and nothing can live in "
                "the sealed ground below",
        ],
        "correct_index": 3,
        "why": "A green roof carries a shallow layer of soil and a narrow "
               "range of drought-tolerant plants, which is not the same "
               "habitat as the ground it stands on.",
    },
    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Weighing one land use against another, multi-step area arithmetic, and
    # claims about restoration held up to what peat actually is.
    {
        "id": "ks4-land-use-h05",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A council can put a solar farm on 30 hectares of arable land "
                "or on 30 hectares of old grassland. Evaluate which does less "
                "harm to biodiversity.",
        "options": [
            "The grassland, because arable soil is too poor to support any "
                "panels being built on it",
            "The grassland, because grass regrows quickly under the panels "
                "once they are installed",
            "The arable land, because it already carries very few species",
            "Either, because the same area is covered whichever site is "
                "used",
        ],
        "correct_index": 2,
        "why": "An arable field is close to a monoculture already, while old "
               "grassland has taken decades to develop its range of plants and "
               "invertebrates.",
    },
    {
        "id": "ks4-land-use-h06",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bog is 3 m deep and formed at 1 mm per year. Extraction "
                "removes 1.2 m of it. Determine how many years of accumulation "
                "have been lost.",
        "options": [
            "1200 years",
            "1800 years",
            "3000 years",
            "120 years",
        ],
        "correct_index": 0,
        "why": "1.2 m is 1200 mm, and at 1 mm per year that represents 1200 "
               "years of accumulation removed.",
    },
    {
        "id": "ks4-land-use-h07",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why replacing a hectare of peat bog with a hectare of "
                "newly planted woodland does not make up for the carbon lost.",
        "options": [
            "Woodland absorbs no carbon dioxide until it is a century old",
            "Peat holds no carbon, so nothing was lost from the site",
            "The trees release more carbon dioxide each year than the bog "
                "did",
            "The drained peat keeps releasing carbon for decades as it "
                "decays",
        ],
        "correct_index": 3,
        "why": "Draining the bog starts a long, continuing release from a very "
               "large store, and young trees take decades to absorb even part "
               "of it.",
    },
    {
        "id": "ks4-land-use-h08",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A county has 90 000 hectares of land, of which 63 000 "
                "hectares are farmed. Determine the percentage that is farmed.",
        "options": [
            "63%",
            "70%",
            "27%",
            "143%",
        ],
        "correct_index": 1,
        "why": "63 000 ÷ 90 000 × 100 = 70% of the county's land is farmed.",
    },
    {
        "id": "ks4-land-use-h09",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect on biodiversity of taking 10 hectares in "
                "one block from a wood with taking ten separate hectares from "
                "across the same wood.",
        "options": [
            "Ten scattered hectares do more harm, because the wood is "
                "broken into small pieces",
            "One block does more harm, because a large hole cannot ever "
                "grow back at all",
            "They are identical, because the area of woodland lost is the "
                "same in both cases",
            "Ten scattered hectares do less harm, because each piece is "
                "small enough to be ignored",
        ],
        "correct_index": 0,
        "why": "Scattered clearances break the wood into fragments, so species "
               "that need a large continuous area, or that cannot cross open "
               "ground, are lost as well as the habitat itself.",
    },
    {
        "id": "ks4-land-use-h10",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A company says its peat is 'sustainably harvested because "
                "only the top layer is taken'. Evaluate this claim.",
        "options": [
            "It is sound, because removing the top layer helps the whole "
                "bog to grow back faster",
            "It is weak, because taking away the top layer releases no "
                "carbon dioxide",
            "It is sound, because the layer taken is replaced within a "
                "decade",
            "It is weak, because even the top layer took centuries and the "
                "bog is dried out",
        ],
        "correct_index": 3,
        "why": "The surface metre still represents about a thousand years of "
               "accumulation, and cutting it drains and dries what is left "
               "beneath.",
    },
    {
        "id": "ks4-land-use-h11",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A city needs 600 new homes. Scheme A builds them at 40 homes "
                "per hectare and scheme B at 15 per hectare. Determine the "
                "extra land scheme B needs.",
        "options": [
            "15 hectares",
            "25 hectares",
            "40 hectares",
            "55 hectares",
        ],
        "correct_index": 1,
        "why": "Scheme A needs 600 ÷ 40 = 15 hectares and scheme B needs 600 ÷ "
               "15 = 40 hectares, so B takes 40 − 15 = 25 hectares more.",
    },
    {
        "id": "ks4-land-use-h12",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the effect on the bog's plants if a drainage ditch "
                "lowers the water table by half a metre.",
        "options": [
            "Nothing changes, because bog plants take their water from "
                "rainfall alone",
            "Every plant on the bog dies at once, leaving completely bare "
                "peat behind",
            "Sphagnum, which grows only in wet ground, declines as drier "
                "species spread",
            "Sphagnum spreads faster, because its roots reach deeper into "
                "the drier peat",
        ],
        "correct_index": 2,
        "why": "Bog plants are adapted to permanently waterlogged ground; "
               "drying the surface lets heather, grasses and eventually scrub "
               "outcompete them.",
    },
    {
        "id": "ks4-land-use-h13",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the argument that land use is not a real threat "
                "because species can move to somewhere else.",
        "options": [
            "It is sound, because habitats elsewhere have spare room",
            "It is weak: moving would break the law on protection",
            "It is sound, because every species can simply move to new "
                "ground close by",
            "It is weak: the surrounding land is usually occupied or "
                "unsuitable",
        ],
        "correct_index": 3,
        "why": "Habitat elsewhere is already at its carrying capacity or is "
               "the wrong habitat entirely, and specialists have nowhere "
               "equivalent to go.",
    },
    {
        "id": "ks4-land-use-h14",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bog stores 1400 tonnes of carbon per hectare and a forest "
                "soil stores 200 tonnes per hectare. Determine how many times "
                "more carbon the bog holds.",
        "options": [
            "1200 times",
            "7 times",
            "0.14 times",
            "70 times",
        ],
        "correct_index": 1,
        "why": "1400 ÷ 200 = 7, so the bog holds seven times as much carbon "
               "per hectare as the forest soil.",
    },
    {
        "id": "ks4-land-use-h15",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a planning decision about one field is described "
                "as a balance rather than a simple choice.",
        "options": [
            "Every field in the whole country holds exactly the same set "
                "of wild species",
            "Planners must always refuse, so there is nothing to weigh up",
            "Homes, jobs and food all have real value, and so does the "
                "habitat",
            "The law fixes an answer, so no judgement is involved in any "
                "case here",
        ],
        "correct_index": 2,
        "why": "The land has competing genuine uses, so the decision weighs "
               "human need against habitat rather than choosing between right "
               "and wrong.",
    },
    {
        "id": "ks4-land-use-h16",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to a cut-over peat bog that is simply "
                "abandoned and left to itself.",
        "options": [
            "It dries and is colonised by scrub, and peat rebuilds very "
                "slowly at best",
            "It becomes bare rock, because peat cutting strips away every "
                "bit of the soil beneath it",
            "It floods on its own and returns to being a working bog "
                "within a single season",
            "The original bog reforms to full depth within about ten years",
        ],
        "correct_index": 0,
        "why": "Without deliberate re-wetting the surface stays drained, so "
               "drier species take over and the bog's specialist community and "
               "its carbon store do not return.",
    },
    {
        "id": "ks4-land-use-h17",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare quarrying and landfill in terms of how long the land "
                "is unavailable to wild species.",
        "options": [
            "Both return to habitat within a year, as the subsoil is "
                "undisturbed",
            "A quarry can be restored once worked out; landfill stays "
                "sealed for far longer",
            "Landfill can be restored at once; a quarry stays unusable for "
                "ever",
            "Both make the land unusable for ever, so no comparison is "
                "possible",
        ],
        "correct_index": 1,
        "why": "A finished quarry can be flooded or replanted within years, "
               "while a landfill must be capped and monitored for decades "
               "before anything can be done with it.",
    },
    {
        "id": "ks4-land-use-h18",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a 5 hectare wood surrounded by housing supports "
                "fewer species than a 5 hectare wood in open countryside.",
        "options": [
            "Houses block the wind, and without wind no tree there is able "
                "to reproduce",
            "The surrounded wood receives far less rainfall, because the "
                "houses catch most of it first",
            "It is isolated, so species that die out there cannot be "
                "replaced from elsewhere",
            "The surrounded wood is warmer, and warmth alone drives every "
                "species away",
        ],
        "correct_index": 2,
        "why": "An isolated fragment receives no immigrants, so a local "
               "extinction is permanent and the number of species drifts down "
               "over time.",
    },
    {
        "id": "ks4-land-use-h19",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farm of 120 hectares sets aside 6% of its area as field "
                "margins. Determine the area set aside, in hectares.",
        "options": [
            "7.2 hectares",
            "20 hectares",
            "72 hectares",
            "0.72 hectares",
        ],
        "correct_index": 0,
        "why": "6% of 120 hectares is 0.06 × 120 = 7.2 hectares.",
    },
    {
        "id": "ks4-land-use-h20",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that peat should keep being cut because "
                "gardeners need it and bogs cover a large area.",
        "options": [
            "It is sound, because no other material is able to grow plants "
                "at all",
            "It is weak, because cutting the peat has no effect on the "
                "rest of the bog around it",
            "It is sound, because bogs are very common and they replace "
                "themselves within a few years",
            "It is weak, because alternatives exist and the carbon and "
                "habitat loss are permanent",
        ],
        "correct_index": 3,
        "why": "Peat-free composts already work, and the loss of a store built "
               "over millennia cannot be recovered on any useful timescale.",
    },
    {
        "id": "ks4-land-use-h21",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why building at higher density reduces the total "
                "habitat lost, even though the buildings are taller.",
        "options": [
            "High-density housing has no gardens, so no soil is dug",
            "Taller buildings cast shade, which improves the habitat "
                "around them",
            "The same number of homes covers a smaller ground area",
            "Taller buildings use fewer materials, so less quarrying is "
                "needed",
        ],
        "correct_index": 2,
        "why": "The habitat cost is set by the ground area sealed, so housing "
               "the same population on less ground leaves more land "
               "undeveloped.",
    },
    {
        "id": "ks4-land-use-h22",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the biodiversity value of a 20 hectare block of "
                "restored bog with twenty separate 1 hectare patches of the "
                "same bog.",
        "options": [
            "The single block is worth more, as its wetness is easier to "
                "hold across a large area",
            "The scattered patches are worth more, because they cover "
                "twenty different parts of the county",
            "They are equal, since the total area of restored bog is "
                "identical in the two cases",
            "The scattered patches are worth more, because each dries out "
                "and suits more plant species",
        ],
        "correct_index": 0,
        "why": "A bog depends on a high water table, and a small patch dries "
               "at its edges, so one large block keeps far more of its area "
               "genuinely wet.",
    },
    {
        "id": "ks4-land-use-h23",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a country can lose habitat even while the total "
                "area of its farmland stays exactly the same.",
        "options": [
            "Farmland can only lose habitat if its total area is "
                "increasing",
            "Habitat is measured in hectares, so an unchanged area must "
                "mean no habitat loss",
            "Farmland area is measured wrongly, so the published figure "
                "hides the loss",
            "Farming can intensify, removing hedges and ponds within the "
                "same area",
        ],
        "correct_index": 3,
        "why": "Hedgerows, ponds, margins and rough corners are habitat inside "
               "the farmed area, and removing them to enlarge fields costs "
               "species without changing the farmland total.",
    },
    {
        "id": "ks4-land-use-h24",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bypass takes 12 hectares and the developer replants 12 "
                "hectares of woodland nearby. Evaluate whether the habitat "
                "loss has been made good.",
        "options": [
            "Yes, because the area that was replanted exactly matches the "
                "area that was taken",
            "Not fully, because young planting takes decades to match an "
                "established habitat",
            "Yes, because new woodland holds more species than old "
                "woodland",
            "No, because planting trees removes more habitat than the road",
        ],
        "correct_index": 1,
        "why": "Area is not the same as habitat quality: an old wood's dead "
               "wood, soil fungi and understorey take many decades to develop "
               "in new planting.",
    },
    {
        "id": "ks4-land-use-h25",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 50 hectare bog releases 20 tonnes of carbon dioxide per "
                "hectare per year once drained. Determine how much is released "
                "over 25 years.",
        "options": [
            "25 000 tonnes",
            "2500 tonnes",
            "50 000 tonnes",
            "1000 tonnes",
        ],
        "correct_index": 0,
        "why": "50 × 20 = 1000 tonnes each year, and 1000 × 25 = 25 000 tonnes "
               "over the twenty-five years.",
    },
    {
        "id": "ks4-land-use-h26",
        "subtopic_slug": "land-use",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the suggestion that all new building should be "
                "restricted to brownfield sites.",
        "options": [
            "It would work everywhere, because brownfield land is far more "
                "common than green-field land",
            "It would fail, because brownfield sites hold more wildlife "
                "than any green field does",
            "It would work, because homes can be built far more cheaply on "
                "contaminated land",
            "It would protect habitat, but there are not enough such sites "
                "in the right places",
        ],
        "correct_index": 3,
        "why": "Reusing developed land is the lower-cost option for habitat, "
               "but supply and location limit it, so some green-field building "
               "is hard to avoid.",
    },
]
