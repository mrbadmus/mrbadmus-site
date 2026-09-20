"""Biology · Ecology — the MRB-338 expansion of `sustainable-fisheries`.

One leaf only: AQA 8461 §4.7.5.3, Biology-only. The original twelve rows in
`ecology__b.py` take sustainability by definition, aquaculture by definition,
the breeding-season ban, protein dependence, how a quota is set, escaped
farmed salmon, waste beneath a cage, fishmeal from wild fish, a doubled fleet
against a fixed quota, enforcement in international waters, a 30 cm mesh
against a 50 cm maturity, and a closed land system against a sea cage.

This file takes what they leave. The recall band finishes the picture of WHY
stocks fell — sonar, factory ships, the named collapses — and the measures the
baseline does not list: exclusion zones, minimum landing sizes, bycatch. The
demand then falls on the two things pupils most often get wrong here: that a
quota is a scientific estimate rather than a political number, and that a fish
farm shifts pressure rather than removing it, because a carnivorous farmed fish
is still fed on wild-caught fish.

The weight is even at fourteen a band: this is a Triple-only spec point where
the recall is short but every measure carries an argument.

⚠️ Marine protected areas raising the catch on neighbouring grounds belongs to
`biodiversity`, and a supermarket's quota promise to `maintaining-biodiversity`.
This leaf stays on the FISHERY and the farm.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e18 ═════════════════════════════════════════════════
    # Why stocks fell, the named collapses, and the measures the baseline
    # does not name.
    {
        "id": "ks4-sustainable-fisheries-e05",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the technology that lets a modern fishing boat locate a "
                "shoal it cannot see.",
        "options": [
            "A barometer",
            "A thermometer",
            "Sonar",
            "A microscope",
        ],
        "correct_index": 2,
        "why": "Sonar, along with larger nets and factory ships, is why modern "
               "fleets can catch fish faster than the stock can reproduce.",
    },
    {
        "id": "ks4-sustainable-fisheries-e06",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name a North Atlantic fish species whose stock has been "
                "fished to critically low levels.",
        "options": [
            "Cod",
            "Goldfish",
            "Piranha",
            "Guppy",
        ],
        "correct_index": 0,
        "why": "Atlantic cod and North Sea herring are the two collapses the "
               "specification names, and cod has still not fully recovered.",
    },
    {
        "id": "ks4-sustainable-fisheries-e07",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a fishing exclusion zone is.",
        "options": [
            "An area where boats from one country may fish",
            "An area where fish are released after they have been farmed",
            "Water in which nets of any mesh size may be used",
            "An area of sea where no fishing is allowed at all",
        ],
        "correct_index": 3,
        "why": "No-catch zones around breeding grounds, or around a stock that "
               "has collapsed, let the fish reproduce without being caught.",
    },
    {
        "id": "ks4-sustainable-fisheries-e08",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by bycatch.",
        "options": [
            "Fish that escape through the mesh of the net as it is being "
                "hauled in",
            "Animals caught in a net that the boat was not fishing for",
            "Fish caught after a boat's quota has already been filled",
            "The share of a catch that is sold at the quayside market",
        ],
        "correct_index": 1,
        "why": "Dolphins, turtles, seabirds and undersized fish are caught "
               "alongside the target species, and much of it is dead before it "
               "is returned to the sea.",
    },
    {
        "id": "ks4-sustainable-fisheries-e09",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the parasite that spreads rapidly among salmon kept at "
                "high density in a sea cage.",
        "options": [
            "The sea louse",
            "The tapeworm",
            "The head louse",
            "The bed bug",
        ],
        "correct_index": 0,
        "why": "Sea lice multiply in crowded cages and can spread from farmed "
               "salmon to wild salmon passing the farm.",
    },
    {
        "id": "ks4-sustainable-fisheries-e10",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one advantage of fish farming over catching wild fish.",
        "options": [
            "Farmed fish need no feeding, because they live on the sea "
                "water around them",
            "Farmed fish grow without any waste being produced",
            "A fish farm needs no staff once the cages have been built",
            "Supply is steady, because it does not depend on the weather",
        ],
        "correct_index": 3,
        "why": "Controlled production gives a predictable supply, can be sited "
               "near markets, and the fish can be selectively bred for fast "
               "growth.",
    },
    {
        "id": "ks4-sustainable-fisheries-e11",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a minimum landing size rule requires a crew to do.",
        "options": [
            "Weigh each fish before it is taken on board",
            "Return any fish below that length to the sea",
            "Land every fish that it catches, whatever the size of the "
                "fish",
            "Catch the fish that are below that length",
        ],
        "correct_index": 1,
        "why": "The rule protects fish that have not yet bred, which is the "
               "same purpose as the minimum mesh size in the net.",
    },
    {
        "id": "ks4-sustainable-fisheries-e12",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the type of feed that makes farming salmon a pressure on "
                "wild fish stocks.",
        "options": [
            "Wheat straw",
            "Sugar beet",
            "Fishmeal",
            "Grass silage",
        ],
        "correct_index": 2,
        "why": "Fishmeal is made from wild-caught fish, so a carnivorous "
               "farmed species still draws on the ocean's production.",
    },
    {
        "id": "ks4-sustainable-fisheries-e13",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what happens to a fish stock when the catch rate "
                "exceeds the reproduction rate for many years.",
        "options": [
            "The population stays steady",
            "The population grows rapidly",
            "The fish grow larger with each year that passes",
            "The population collapses",
        ],
        "correct_index": 3,
        "why": "Removing adults faster than they are replaced shrinks the "
               "breeding population, and each year's spawning then produces "
               "fewer young than the last.",
    },
    {
        "id": "ks4-sustainable-fisheries-e14",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name one way of farming fish that does not release waste into "
                "open water.",
        "options": [
            "A floating cage towed behind a boat",
            "A closed recirculating system on land",
            "A sea cage moored in a sheltered loch",
            "A net pen anchored beside the mouth of a river",
        ],
        "correct_index": 1,
        "why": "A closed land-based system filters and reuses its water, so "
               "waste, escapes and parasites are all contained.",
    },
    {
        "id": "ks4-sustainable-fisheries-e15",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is used instead of antibiotics on a well-run "
                "modern fish farm.",
        "options": [
            "Warmer water throughout the year",
            "A diet made entirely of wild fish",
            "Vaccination of the young fish",
            "A higher stocking density in each of the cages",
        ],
        "correct_index": 2,
        "why": "Vaccinating the stock prevents disease without the routine "
               "antibiotic use that selects for resistant bacteria.",
    },
    {
        "id": "ks4-sustainable-fisheries-e16",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the kind of survey scientists carry out before a quota "
                "for the coming year is set.",
        "options": [
            "A survey of the stock's size and its breeding rate",
            "A survey of how many boats hold a fishing licence",
            "A survey of the price that fish reached at the market last "
                "year",
            "A survey of how much fuel each fishing boat uses",
        ],
        "correct_index": 0,
        "why": "The quota is calculated from an estimate of the population and "
               "of how fast it replaces itself, which is what makes it a "
               "scientific figure.",
    },
    {
        "id": "ks4-sustainable-fisheries-e17",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the effect on a food web of removing almost all of a "
                "large predatory fish.",
        "options": [
            "The predator's prey also disappears immediately",
            "The species it ate become far more numerous",
            "Every other species in the web dies out at once",
            "The web is unchanged, because the predators eat very little",
        ],
        "correct_index": 1,
        "why": "Taking out a top predator releases its prey from predation, "
               "and the knock-on effects run down through the whole food web.",
    },
    {
        "id": "ks4-sustainable-fisheries-e18",
        "subtopic_slug": "sustainable-fisheries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name a farmed fish that is fed mainly on plant material "
                "rather than on fishmeal.",
        "options": [
            "Tuna",
            "Cod",
            "Carp",
            "Salmon",
        ],
        "correct_index": 2,
        "why": "Carp and tilapia are largely herbivorous, so farming them puts "
               "far less pressure on wild stocks than farming a carnivore "
               "does.",
    },
    # ══ standard · s05–s18 ═══════════════════════════════════════════════
    # Each measure and each cost of aquaculture, worked through in context.
    {
        "id": "ks4-sustainable-fisheries-s05",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a quota is described as a scientific figure "
                "rather than an arbitrary limit.",
        "options": [
            "It is set at the same number every year so that it can be "
                "checked",
            "It is worked out from the total number of boats holding a "
                "licence",
            "It is calculated from the stock's measured size and breeding "
                "rate",
            "It is agreed by a vote among all of the crews who will then "
                "have to keep to it",
        ],
        "correct_index": 2,
        "why": "The figure comes from a population estimate and a replacement "
               "rate, so it is a prediction of what the stock can lose and "
               "still rebuild.",
    },
    {
        "id": "ks4-sustainable-fisheries-s06",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a larger mesh size protects a stock better than "
                "simply catching fewer fish of any size.",
        "options": [
            "The young escape and go on to breed, while the adults caught "
                "have already bred",
            "A larger mesh catches the young fish, and young fish are much "
                "easier to replace than adults",
            "A larger mesh makes the net lighter, so the boat can fish for "
                "longer",
            "The fish that escape become too large for any net to catch "
                "them later",
        ],
        "correct_index": 0,
        "why": "What matters is not only how many are taken but which ones: "
               "removing fish before they have spawned removes the next "
               "generation with them.",
    },
    {
        "id": "ks4-sustainable-fisheries-s07",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A quota of 90 000 tonnes is shared equally between 150 boats. "
                "Calculate each boat's allowance.",
        "options": [
            "60 tonnes",
            "6000 tonnes",
            "1500 tonnes",
            "600 tonnes",
        ],
        "correct_index": 3,
        "why": "90 000 ÷ 150 = 600 tonnes for each boat.",
    },
    {
        "id": "ks4-sustainable-fisheries-s08",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a discard rule that forces crews to land "
                "everything they catch can improve the science behind a quota.",
        "options": [
            "The rule stops the bycatch from being caught in the fishing "
                "nets in the first place",
            "The landed bycatch is recorded, so the real removal from the "
                "sea is known",
            "Landing everything raises the catch, which makes the stock "
                "look healthier",
            "Crews who land everything are given a larger quota the "
                "following year",
        ],
        "correct_index": 1,
        "why": "Fish thrown back dead are invisible in the catch record, so "
               "the stock assessment underestimates what the fishery has "
               "actually removed.",
    },
    {
        "id": "ks4-sustainable-fisheries-s09",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why sea lice from a salmon farm are a problem for "
                "wild salmon in the same loch.",
        "options": [
            "The farm holds so many hosts that lice numbers rise and "
                "spread outwards",
            "Lice from the farm are a different species that the wild "
                "salmon are unable to resist",
            "Farmed salmon are vaccinated, so the lice move to the wild "
                "fish instead",
            "The lice feed on the farm's waste and then follow the wild "
                "fish upstream",
        ],
        "correct_index": 0,
        "why": "A dense host population lets a parasite multiply far beyond "
               "its natural level, and young wild salmon passing the cages "
               "meet a far heavier infestation than they would otherwise.",
    },
    {
        "id": "ks4-sustainable-fisheries-s10",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why farming carp puts less pressure on wild stocks "
                "than farming salmon.",
        "options": [
            "Carp grow far more slowly, so fewer are farmed each year",
            "Carp are farmed in the sea, where feed is not needed",
            "Carp are a wild species, so farming them removes none",
            "Carp are fed on plant material, so no wild fish are caught to "
                "feed them",
        ],
        "correct_index": 3,
        "why": "A herbivorous farmed fish converts plant material directly, "
               "while a carnivore must be fed fishmeal made from wild-caught "
               "fish.",
    },
    {
        "id": "ks4-sustainable-fisheries-s11",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a stock that has collapsed may take decades to "
                "recover even after fishing stops.",
        "options": [
            "Fish stop reproducing altogether once their numbers have "
                "fallen",
            "Few adults are left to breed, and each generation takes years "
                "to mature",
            "The species changes into a different species during the time "
                "it is not being fished",
            "The sea keeps the collapsed stock at its low level "
                "permanently",
        ],
        "correct_index": 1,
        "why": "Recovery depends on the surviving spawning stock, and a "
               "species that takes several years to reach maturity rebuilds "
               "slowly from a small base.",
    },
    {
        "id": "ks4-sustainable-fisheries-s12",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why closing a breeding ground to fishing protects "
                "more fish than closing an area of open sea of the same size.",
        "options": [
            "Fish that spawn cannot swim, so they are easier to protect in "
                "one place",
            "Open sea contains no fish, so closing it protects nothing",
            "Spawning adults are concentrated there, so the same area "
                "shelters far more of them",
            "Breeding grounds hold fish that are too small to be worth "
                "catching anyway",
        ],
        "correct_index": 2,
        "why": "Protection is worth most where the fish are densest and most "
               "vulnerable, and a spawning aggregation is both.",
    },
    {
        "id": "ks4-sustainable-fisheries-s13",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A stock is estimated at 240 000 tonnes and replaces 15% of "
                "itself each year. Calculate a sustainable annual catch.",
        "options": [
            "3600 tonnes",
            "16 000 tonnes",
            "204 000 tonnes",
            "36 000 tonnes",
        ],
        "correct_index": 3,
        "why": "15% of 240 000 tonnes is 0.15 × 240 000 = 36 000 tonnes, which "
               "is what the stock can replace in a year.",
    },
    {
        "id": "ks4-sustainable-fisheries-s14",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why waste from a sea cage affects the seabed beneath "
                "it more than the open water around it.",
        "options": [
            "The cage's netting traps waste against the seabed",
            "Uneaten feed and faeces sink and build up directly below the "
                "cage",
            "The seabed is colder, so waste cannot break down there",
            "Currents carry the waste downwards and not sideways",
        ],
        "correct_index": 1,
        "why": "Solid waste settles under the cage, where decomposers consume "
               "the oxygen and the seabed community beneath is smothered.",
    },
    {
        "id": "ks4-sustainable-fisheries-s15",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a fishing crew may prefer a quota to a total ban "
                "on catching a collapsed species.",
        "options": [
            "A quota applies to other countries' boats but not to their "
                "own",
            "A quota allows them to fish during the breeding season as "
                "well",
            "A quota leaves them some income while the stock is recovering",
            "A quota means that they may catch as many fish as they wish "
                "to catch",
        ],
        "correct_index": 2,
        "why": "A reduced catch keeps a livelihood alive, which is why "
               "management usually tightens a quota rather than closing a "
               "fishery outright.",
    },
    {
        "id": "ks4-sustainable-fisheries-s16",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fishery that lands only the largest fish can "
                "change the population over several generations.",
        "options": [
            "Fish that mature at a smaller size are the ones that survive "
                "and breed",
            "The remaining fish grow larger, because they have more food "
                "each",
            "The large fish are replaced each year by other fish of "
                "exactly the same body size",
            "The stock becomes a different species within a few "
                "generations",
        ],
        "correct_index": 0,
        "why": "Taking the largest is a selection pressure: individuals that "
               "breed young and small leave more offspring, so the stock "
               "shifts towards smaller mature fish.",
    },
    {
        "id": "ks4-sustainable-fisheries-s17",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why replacing fishmeal with plant protein makes a "
                "salmon farm more sustainable.",
        "options": [
            "Salmon fed on plants can be kept at a far higher density",
            "Fewer wild fish are caught to feed the farmed salmon",
            "Plant protein makes the salmon grow to a much greater size",
            "Plant feed dissolves in the water, so none of the waste "
                "reaches the seabed",
        ],
        "correct_index": 1,
        "why": "The wild-caught feed is the largest ocean cost of farming a "
               "carnivore, so cutting it cuts the pressure the farm places on "
               "wild stocks.",
    },
    {
        "id": "ks4-sustainable-fisheries-s18",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "It takes 4 kg of wild fish to produce 1 kg of farmed salmon. "
                "Calculate the wild fish needed for 750 kg of salmon.",
        "options": [
            "754 kg",
            "300 kg",
            "3000 kg",
            "187.5 kg",
        ],
        "correct_index": 2,
        "why": "750 kg × 4 = 3000 kg of wild fish are needed.",
    },
    # ══ harder · h05–h18 ═════════════════════════════════════════════════
    # Management judged against data, and the farm weighed against the sea.
    {
        "id": "ks4-sustainable-fisheries-h05",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A stock's catch stays steady for ten years while the mean "
                "size of fish landed falls. Explain what this suggests.",
        "options": [
            "Nothing has changed, because the total catch has stayed the "
                "same",
            "The fish are growing more slowly because the sea has warmed "
                "up",
            "The stock is being overfished, because more effort is taking "
                "younger fish",
            "The stock is recovering, because smaller fish mean more young "
                "ones present",
        ],
        "correct_index": 2,
        "why": "A steady catch of progressively younger fish means the older "
               "age classes have gone, and the fishery is living on each "
               "year's recruits.",
    },
    {
        "id": "ks4-sustainable-fisheries-h06",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate a quota set from last year's landings rather than "
                "from a survey of the stock.",
        "options": [
            "It is unsound, because landings follow effort, so a falling "
                "stock can still be fished hard",
            "It is sound, because last year's landings are the most "
                "accurate figure that is available",
            "It is sound, because a quota is a target and need not match "
                "the stock",
            "It is unsound, because landings are recorded by the crews and "
                "not by scientists",
        ],
        "correct_index": 0,
        "why": "Catch measures fishing, not fish: a fleet can keep landing the "
               "same tonnage from a shrinking stock by working harder, right "
               "up until it collapses.",
    },
    {
        "id": "ks4-sustainable-fisheries-h07",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A stock falls from 500 000 tonnes to 120 000 tonnes. "
                "Determine the percentage that has been lost.",
        "options": [
            "24%",
            "38%",
            "417%",
            "76%",
        ],
        "correct_index": 3,
        "why": "The loss is 500 000 − 120 000 = 380 000, and 380 000 ÷ 500 000 "
               "× 100 = 76%.",
    },
    {
        "id": "ks4-sustainable-fisheries-h08",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare protecting a fishery with an exclusion zone and "
                "protecting it with a seasonal ban.",
        "options": [
            "Neither protects a stock, because the fish simply swim "
                "outside the limits",
            "A zone protects one place all year; a ban protects the whole "
                "stock at one time",
            "A zone protects the stock while it is spawning; a ban "
                "protects one place all year round",
            "The two are identical, because both stop fishing for part of "
                "the year",
        ],
        "correct_index": 1,
        "why": "They act on different axes: one closes a place permanently, "
               "the other closes the whole fishery at the moment the fish are "
               "breeding.",
    },
    {
        "id": "ks4-sustainable-fisheries-h09",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why raising the minimum mesh size lowers a crew's "
                "income in the first year but can raise it later.",
        "options": [
            "Fewer fish are landed now, but those that escape breed and "
                "are caught when larger",
            "A larger mesh is cheaper to buy, so the saving appears in the "
                "second year",
            "Fewer fish are landed now, and the stock stays at the same "
                "size for ever",
            "A larger mesh catches more fish immediately, but the stock "
                "then falls",
        ],
        "correct_index": 0,
        "why": "The short-term loss buys a larger spawning stock and larger "
               "fish per catch, which is the trade-off every management "
               "measure asks a fishery to accept.",
    },
    {
        "id": "ks4-sustainable-fisheries-h10",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a farmed salmon escaping into a river is a "
                "problem even if it never breeds.",
        "options": [
            "It is a different species altogether, so it cannot survive in "
                "the river's fresh water",
            "It removes the oxygen that the wild salmon in the river need",
            "It is unable to swim upstream, so it blocks the river's flow",
            "It competes with wild fish for food and space, and can carry "
                "parasites",
        ],
        "correct_index": 3,
        "why": "Escapes bring competition and disease as well as the genetic "
               "problem of interbreeding, so all three effects count.",
    },
    {
        "id": "ks4-sustainable-fisheries-h11",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the claim that fish farming removes the need to "
                "manage wild fisheries.",
        "options": [
            "It is weak, because farmed fish are released into the sea "
                "when grown",
            "It is weak, because carnivorous farmed fish are fed on "
                "wild-caught fish",
            "It is sound, because every farmed fish replaces a fish that "
                "is not caught at sea",
            "It is sound, because fish farms produce more than the oceans "
                "do",
        ],
        "correct_index": 1,
        "why": "Farming shifts the pressure rather than removing it, and it "
               "adds pollution, escapes and disease — so the wild fishery "
               "still needs managing.",
    },
    {
        "id": "ks4-sustainable-fisheries-h12",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fleet catches 48 000 tonnes against a quota of 40 000 "
                "tonnes. Determine by what percentage the quota was exceeded.",
        "options": [
            "8%",
            "80%",
            "20%",
            "17%",
        ],
        "correct_index": 2,
        "why": "The excess is 48 000 − 40 000 = 8000, and 8000 ÷ 40 000 × 100 "
               "= 20%.",
    },
    {
        "id": "ks4-sustainable-fisheries-h13",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why removing a predatory fish can reduce the catch of "
                "a completely different species years later.",
        "options": [
            "The other species is unable to breed without the predator "
                "present",
            "Predators create the oxygen the other species needs to "
                "survive",
            "Its removal warms the water, which the other species is "
                "unable to tolerate",
            "Its prey multiply and eat out the food the other species "
                "depends on",
        ],
        "correct_index": 3,
        "why": "A food web is connected: releasing one prey population changes "
               "grazing or predation further down, and the effects reach "
               "species the fishery never targeted.",
    },
    {
        "id": "ks4-sustainable-fisheries-h14",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare the environmental costs of a carp farm in a pond with "
                "those of a tuna farm in a sea cage.",
        "options": [
            "The carp farm costs more, because a pond has to be dug out of "
                "the land first",
            "The carp eats plants and its waste is contained; the tuna is "
                "fed wild fish in open water",
            "The tuna eats plants and the carp eats wild fish, so the tuna "
                "farm costs less",
            "The two are equivalent, because both hold fish at a high "
                "stocking density",
        ],
        "correct_index": 1,
        "why": "Trophic level and containment are the two things that decide "
               "an aquaculture system's cost, and the carp farm is better "
               "placed on both.",
    },
    {
        "id": "ks4-sustainable-fisheries-h15",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a country may set a quota above the level its own "
                "scientists advise.",
        "options": [
            "A higher quota lets the stock recover faster than a lower one "
                "does",
            "Quotas above the advice are set where the stock has already "
                "collapsed",
            "Ministers weigh the immediate cost to fishing communities "
                "against a future gain",
            "Scientific advice has no legal standing anywhere in the world",
        ],
        "correct_index": 2,
        "why": "The scientific advice is about the fish; the decision is also "
               "about jobs, ports and elections, which is why quotas are "
               "routinely set above it.",
    },
    {
        "id": "ks4-sustainable-fisheries-h16",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A closed land system uses 3.2 kWh of electricity per kilogram "
                "of fish and a sea cage 0.4 kWh. Determine how many times more "
                "energy the land system uses.",
        "options": [
            "8 times",
            "2.8 times",
            "1.28 times",
            "0.125 times",
        ],
        "correct_index": 0,
        "why": "3.2 ÷ 0.4 = 8, so the land system uses eight times the energy "
               "per kilogram.",
    },
    {
        "id": "ks4-sustainable-fisheries-h17",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a species that matures at eight years old is "
                "harder to fish sustainably than one that matures at two.",
        "options": [
            "It lives in deeper water, where the nets cannot reach it",
            "It must survive eight years of fishing before it breeds even "
                "once",
            "It grows to a much larger size, so each individual that is "
                "caught weighs more",
            "It produces far fewer eggs each time that it spawns",
        ],
        "correct_index": 1,
        "why": "The longer the time to maturity, the greater the chance an "
               "individual is caught before contributing anything to the next "
               "generation.",
    },
    {
        "id": "ks4-sustainable-fisheries-h18",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate a plan to rebuild a collapsed stock by releasing "
                "hatchery-reared young into the sea.",
        "options": [
            "It cannot help, because hatchery fish cannot survive in the "
                "open sea",
            "It will work, because hatchery fish breed far faster than "
                "wild ones do",
            "It can add numbers, but the overfishing that caused the "
                "collapse must stop as well",
            "It will rebuild the stock in full, whatever the fleet goes on "
                "to catch",
        ],
        "correct_index": 2,
        "why": "Restocking treats the symptom; unless fishing pressure is cut, "
               "the released fish are caught before they spawn and the stock "
               "stays where it is.",
    },

    # ══ standard/harder · s19-s26, h19-h26 (MRB-338 night 3 top-up) ══
    {
        "id": "ks4-sustainable-fisheries-s19",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain one way that selectively breeding farmed salmon for faster "
                "growth can make a fish farm more efficient.",
        "options": [
            "It removes the need to feed the fish, since faster-growing fish are said to need far less food overall",
            "It stops any disease from spreading through the farm, since faster growth outpaces any infection",
            "It reduces how much water a fish farm needs, since fish reach market size in a smaller tank",
            "It lets more fish reach market size sooner, raising the amount of salmon the farm can sell each year",
        ],
        "correct_index": 3,
        "why": "Breeding for faster growth means more fish reach market size sooner, "
               "so the farm can sell more salmon in a given year.",
    },
    {
        "id": "ks4-sustainable-fisheries-s20",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fish farm located close to its market can make a more "
                "sustainable choice than sourcing wild-caught fish from further away.",
        "options": [
            "It removes the need for feeding the fish, since farms near a restaurant can rely on wild food nearby",
            "It cuts the time and distance the fish travel from farm to plate, reducing spoilage and transport cost",
            "It guarantees a lower price for the restaurant, whatever the actual cost of raising the fish has been",
            "It means the fish no longer need to be kept in any sort of enclosure before they are sold",
        ],
        "correct_index": 1,
        "why": "Growing fish close to where they are sold cuts the time and distance "
               "travelled from farm to plate, reducing spoilage and transport costs.",
    },
    {
        "id": "ks4-sustainable-fisheries-s21",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why vaccinating farmed fish, rather than relying on "
                "antibiotics, makes a fish farm more sustainable.",
        "options": [
            "It lowers the risk of antibiotic resistance developing and reduces the amount of chemical residue released",
            "It removes any need to keep the fish at a safe stocking density inside the farm's cages",
            "It guarantees that no fish on the farm will ever catch any disease again for the whole rest of its life",
            "It makes the fish grow noticeably faster than antibiotics alone would ever allow them to",
        ],
        "correct_index": 0,
        "why": "Vaccination lowers the risk of antibiotic resistance developing in "
               "the farm's fish and reduces the amount of chemical residue released "
               "into the water.",
    },
    {
        "id": "ks4-sustainable-fisheries-s22",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fish farm can supply restaurants with a steady weekly "
                "order of salmon in a way that wild-caught fishing cannot always "
                "guarantee.",
        "options": [
            "Wild-caught fishing is banned outright during the exact weeks a farm's contract requires salmon",
            "Farmed salmon typically tastes better than wild salmon, which is why restaurants prefer a steady order",
            "Farm production is not at the mercy of weather, migration patterns or wild population changes each week",
            "A restaurant orders salmon just once a year, so weekly supply is not a genuine concern",
        ],
        "correct_index": 2,
        "why": "A farm's production does not depend on weather, migration patterns "
               "or wild population changes the way wild-caught fishing does, so it "
               "can promise a steady supply.",
    },
    {
        "id": "ks4-sustainable-fisheries-s23",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Trawling for prawns catches large numbers of juvenile fish of other "
                "species as bycatch, which are then discarded dead. Explain the "
                "effect this could have on those other species' populations over "
                "time.",
        "options": [
            "It has little effect, since discarded bycatch is said to survive once it is returned to the sea",
            "Fewer juveniles of the bycatch species survive to reproduce, so their own population may decline too",
            "It affects just the prawns being targeted, since bycatch species are said not to be caught in the net",
            "It raises the bycatch species' population, since discarded fish provide extra food for scavengers nearby",
        ],
        "correct_index": 1,
        "why": "Discarded juveniles rarely survive being caught and thrown back, so "
               "fewer of them reach breeding age, which can reduce their own "
               "species' population over time.",
    },
    {
        "id": "ks4-sustainable-fisheries-s24",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fish stock of 200 000 tonnes reproduces at 12% a year. A fleet "
                "plans to catch 30 000 tonnes next year. Determine whether this catch "
                "is sustainable.",
        "options": [
            "It is sustainable, since 30 000 tonnes is comfortably below the stock's total size of 200 000 tonnes",
            "It is not sustainable, since the stock replaces just 24 000 tonnes a year, less than the proposed catch",
            "It is sustainable, since any catch under 50% of the total stock is considered safe by definition",
            "It cannot be judged, because a 12% reproduction rate would be needed before any catch could be assessed",
        ],
        "correct_index": 1,
        "why": "The stock replaces 12% of 200 000 tonnes, which is 24 000 tonnes a "
               "year, less than the 30 000 tonnes the fleet plans to catch, so the "
               "catch is not sustainable.",
    },
    {
        "id": "ks4-sustainable-fisheries-s25",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "State two things a scientific stock survey needs to measure before a "
                "sustainable quota can be set.",
        "options": [
            "The average size of the fish caught last season, and the price the catch sold for at market",
            "The number of boats currently licensed to fish that species, and their combined engine power",
            "The weather conditions during the survey, and the total distance the survey vessel travelled",
            "The stock's current size or biomass, and the rate at which it grows or reproduces each year",
        ],
        "correct_index": 3,
        "why": "A survey needs the stock's current size or biomass and its rate of "
               "growth or reproduction before a sustainable quota can be worked out.",
    },
    {
        "id": "ks4-sustainable-fisheries-s26",
        "subtopic_slug": "sustainable-fisheries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest one reason a small-scale local fishing crew might find it "
                "harder to comply with a new minimum mesh size rule than a large "
                "industrial fishing company.",
        "options": [
            "It makes no real difference, since every fishing crew is given identical nets by the government",
            "Larger nets are typically cheaper for a small crew to buy than the smaller nets they already own",
            "Replacing nets to meet a new mesh size is a proportionally bigger cost for a crew with less capital",
            "Small crews are automatically exempt from any new mesh size rule that a government introduces",
        ],
        "correct_index": 2,
        "why": "Buying new nets to meet a mesh size rule costs the same in absolute "
               "terms for every crew, but is a much bigger share of a small crew's "
               "limited budget.",
    },
    {
        "id": "ks4-sustainable-fisheries-h19",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fish stock grows at 10% a year with no fishing pressure. A fleet "
                "then begins catching a fixed 50 000 tonnes every year, regardless of "
                "the stock's size. Starting from a stock of 400 000 tonnes, determine "
                "whether the stock grows or shrinks in the first year, and explain "
                "why.",
        "options": [
            "It shrinks at first, since the stock replaces just 40 000 tonnes at 10% while 50 000 tonnes are caught",
            "It grows at first, since a fixed catch is said to fall below the amount a stock happens to reproduce",
            "It stays exactly the same size, since a fixed catch and a percentage growth rate are said to cancel out",
            "It cannot be determined without knowing the exact number of individual fish in the stock",
        ],
        "correct_index": 0,
        "why": "10% of 400 000 tonnes is 40 000 tonnes of new growth, which is less "
               "than the fixed 50 000 tonnes being caught, so the stock shrinks in "
               "the first year.",
    },
    {
        "id": "ks4-sustainable-fisheries-h20",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fish farm switches from feeding its salmon wild-caught fishmeal to "
                "a plant-based feed. A campaigner claims this makes the farm 'fully "
                "sustainable'. Evaluate this claim.",
        "options": [
            "The claim is justified, since switching the feed source removes every possible sustainability concern at once completely",
            "The claim is justified, because wild fish stocks are the only sustainability issue a fish farm ever faces",
            "The claim cannot be assessed, because plant-based feed is said to have no real effect on a fish farm's impact",
            "The claim overstates it; plant-based feed eases pressure on wild stocks, but disease, escapes and pollution remain",
        ],
        "correct_index": 3,
        "why": "Plant-based feed does ease pressure on wild fish stocks, but it does "
               "not remove other concerns such as disease, escapes into the wild or "
               "pollution from the farm.",
    },
    {
        "id": "ks4-sustainable-fisheries-h21",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A fish farm vaccinates its salmon against common diseases rather "
                "than using antibiotics. Evaluate the claim that this removes all "
                "risk of disease spreading rapidly through the farm.",
        "options": [
            "The claim holds completely, since a vaccinated fish is said not to become infected with any disease again",
            "The claim overstates it; density remains high, so an uncovered disease or a vaccine failure could still spread fast",
            "The claim holds completely, since vaccination also lowers the density at which the fish are kept",
            "The claim is meaningless, because vaccination is said to have no measurable effect on how disease spreads through a farm",
        ],
        "correct_index": 1,
        "why": "Vaccination reduces risk but the fish are still kept at high "
               "density, so a disease the vaccine does not cover, or a vaccine "
               "failure, could still spread quickly.",
    },
    {
        "id": "ks4-sustainable-fisheries-h22",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A trawl fleet catches 500 tonnes of target prawns a year, and for "
                "every tonne of prawns caught, 3 tonnes of juvenile fish are "
                "discarded as bycatch. A new bycatch-reduction device cuts this ratio "
                "to 1 tonne of bycatch per tonne of prawns. Determine the reduction "
                "in bycatch achieved by fitting the device across the whole fleet.",
        "options": [
            "500 tonnes, treating the new ratio as though it had already applied to the old bycatch figure directly",
            "1 500 tonnes, the old bycatch figure, mistaken here for the reduction the device achieves",
            "2 000 tonnes, from adding the old and new bycatch figures instead of subtracting them",
            "1 000 tonnes, from 1 500 tonnes of bycatch under the old ratio falling to 500 tonnes under the new one",
        ],
        "correct_index": 3,
        "why": "The old ratio gives 500 tonnes of prawns times 3, or 1 500 tonnes of "
               "bycatch; the new ratio gives 500 tonnes times 1, or 500 tonnes, a "
               "reduction of 1 000 tonnes.",
    },
    {
        "id": "ks4-sustainable-fisheries-h23",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A restaurant chain switches its entire salmon supply from wild- "
                "caught to farmed, citing the need for a reliable weekly order. "
                "Evaluate whether this decision removes every sustainability concern "
                "the chain might have.",
        "options": [
            "Yes, since farmed salmon carries no sustainability concerns of any kind once wild stocks are no longer fished",
            "Yes, since a reliable weekly order is the main sustainability concern a restaurant chain has",
            "No, since wild-caught salmon would have solved the weekly supply problem just as reliably as farmed salmon does",
            "No, since farming introduces its own concerns, such as disease, escapes and pollution, rather than removing every concern",
        ],
        "correct_index": 3,
        "why": "Farming solves the reliable-supply problem and eases pressure on "
               "wild stocks, but introduces its own separate concerns such as "
               "disease, escapes and pollution.",
    },
    {
        "id": "ks4-sustainable-fisheries-h24",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A stock survey measures a fish population at 180 000 tonnes, but the "
                "survey method is known to overestimate the population by around 20%. "
                "Determine the likely true size of the stock, and state the effect "
                "this has on a quota calculated from the survey's raw figure.",
        "options": [
            "150 000 tonnes, so a quota from the raw figure would be set too high and risk overfishing the true stock",
            "150 000 tonnes, so a quota from the raw figure would in fact be set too cautiously low",
            "180 000 tonnes, since the survey's known bias is said to have no effect on the quota eventually calculated from it",
            "216 000 tonnes, from applying the reproduction rate to the survey figure instead of correcting for the bias first",
        ],
        "correct_index": 0,
        "why": "180 000 tonnes divided by 1.2 gives a true stock of about 150 000 "
               "tonnes, so a quota calculated from the raw, inflated figure would be "
               "set too high and risk overfishing.",
    },
    {
        "id": "ks4-sustainable-fisheries-h25",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two fishing fleets both target the same 500 000-tonne stock, which "
                "reproduces at 12% a year. Fleet A catches 8% of the current stock "
                "each year. Fleet B catches a fixed 50 000 tonnes each year "
                "regardless of stock size. Compare which fleet's approach is more "
                "likely to remain sustainable as the stock size changes over time.",
        "options": [
            "Fleet A is more likely to prove unsustainable, since a fixed percentage is said to outpace a stock's reproduction",
            "Fleet B is more likely to prove unsustainable, since its fixed catch does not shrink even as the stock declines",
            "Both fleets are equally sustainable, since 8% of a large stock and a fixed 50 000 tonnes end up identical over time",
            "Neither fleet's approach can be compared without first knowing the exact species of fish being caught",
        ],
        "correct_index": 1,
        "why": "Fleet A's catch falls automatically as the stock shrinks, since 8% "
               "of a smaller number is smaller, while Fleet B's fixed catch stays "
               "the same even as the stock declines.",
    },
    {
        "id": "ks4-sustainable-fisheries-h26",
        "subtopic_slug": "sustainable-fisheries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A country's fishing quota is cut by 40% following a stock survey, "
                "and the fishing industry protests that this will destroy jobs "
                "immediately. Evaluate this claim, considering both the short and the "
                "long term.",
        "options": [
            "The claim is entirely wrong, since a quota cut is said to have no real effect on a fishing crew's income",
            "The claim is entirely right, since a recovering stock is said to take many decades longer to recover than continued fishing would",
            "The claim cannot be assessed, since fishing industry income has no real connection to the size of a fish stock",
            "The claim has some truth short term, but a recovering stock can support a larger, safer catch in the long term",
        ],
        "correct_index": 3,
        "why": "A sudden cut can hit income and jobs in the short term, but letting "
               "the stock recover can support a larger, safer catch in the long term "
               "than continued overfishing would allow.",
    },
]
