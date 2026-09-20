"""Biology · Ecology — the MRB-338 expansion of `maintaining-biodiversity`.

One leaf only: AQA 8461 §4.7.3.6 — the PROGRAMMES humans run to maintain
biodiversity, and the conflicts those programmes meet. The original twelve rows
in `ecology__a.py` take habitat regeneration, governments cutting deforestation
and emissions, pollination as a service, rewilding, a wildflower strip, habitat
against single-species protection, a logging ban opposed locally, recycling,
one block against narrow margins, conservation as a balance, a fish quota, and
a reserve ringed by farmland.

This file takes what they leave. The recall band finishes the named programmes
the baseline never lists — breeding programmes, seed banks, reintroduction,
legal protection — and the three conflicts AQA names: cost, land, livelihoods.
The demand then falls where the marks are actually lost: a pupil who can list
measures but cannot say why a zoo population alone does not save a species, why
a programme costs something real, or who pays.

The weight follows the CONTENT. `easier` stays at eight — the programmes are a
closed list. `standard` and `harder` carry twenty-two each, because every
measure meets a different objection and every objection has a number attached
to it.

⚠️ This leaf is about the PROGRAMMES and the TRADE-OFFS. What biodiversity is,
and what threatens it, belong to `biodiversity`; peat and land area to
`land-use`; forest clearance to `deforestation`.
"""

TOPIC = "ecology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The named programmes the baseline leaves out, and the three conflicts.
    {
        "id": "ks4-maintaining-biodiversity-e05",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the programme in which a zoo breeds an endangered "
                "species to increase its numbers.",
        "options": [
            "A recycling scheme",
            "A drainage programme",
            "A breeding programme",
            "A quota scheme",
        ],
        "correct_index": 2,
        "why": "Captive breeding programmes raise the number of individuals of "
               "a species that has become too rare to recover on its own.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e06",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is stored in a seed bank.",
        "options": [
            "Seeds of many plant species, kept dry and cold for the future",
            "Money raised by charities to buy land for new nature reserves "
                "everywhere in the world",
            "Records of every plant species that has ever been discovered "
                "anywhere",
            "Soil samples taken from each of the world's rare habitats",
        ],
        "correct_index": 0,
        "why": "A seed bank keeps viable seed from many species in cold "
               "storage, so a plant can be grown again even if it is lost from "
               "the wild.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e07",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name one thing, other than money, that a conservation "
                "programme competes with human needs for.",
        "options": [
            "Oxygen",
            "Sunlight",
            "Rainfall",
            "Land",
        ],
        "correct_index": 3,
        "why": "Land set aside for habitat is land not used for farming or "
               "housing, which is why conservation decisions are trade-offs.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e08",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by reintroducing a species.",
        "options": [
            "Removing it from an area where it has become too common",
            "Releasing it back into an area where it used to live",
            "Moving it into a country where it has not lived before",
            "Breeding it with a related species in order to make a "
                "stronger one",
        ],
        "correct_index": 1,
        "why": "Reintroduction returns a species to part of its former range, "
               "usually from a captive-bred or translocated population.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e09",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the kind of protected area set aside so that wildlife "
                "can live undisturbed.",
        "options": [
            "A nature reserve",
            "An industrial estate",
            "A landfill site",
            "A quarry",
        ],
        "correct_index": 0,
        "why": "A nature reserve protects habitat from development and manages "
               "it for the species that live there.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e10",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name one service, besides pollination, that humans get from a "
                "healthy ecosystem.",
        "options": [
            "Mains electricity",
            "Mobile phone signal",
            "Tarmac for roads",
            "Clean water",
        ],
        "correct_index": 3,
        "why": "Wetlands and soils filter water, and healthy ecosystems also "
               "supply food, timber, fibre and flood protection.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e11",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a law that protects a rare species usually "
                "forbids.",
        "options": [
            "Feeding it during the coldest months of the winter",
            "Killing it, or damaging the place where it breeds",
            "Photographing it from anywhere in the countryside",
            "Naming it in a scientific paper before it has been counted",
        ],
        "correct_index": 1,
        "why": "Legal protection typically bans killing, capturing or "
               "disturbing a species and damaging its breeding or resting "
               "places.",
    },
    {
        "id": "ks4-maintaining-biodiversity-e12",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why conservation programmes are described as costing "
                "money that could be spent elsewhere.",
        "options": [
            "The money must be paid directly to the species being "
                "protected",
            "The money is taken from the wages of local farmers",
            "The money could have gone to hospitals, schools or housing",
            "The money is simply destroyed once a conservation project has "
                "finally ended",
        ],
        "correct_index": 2,
        "why": "Conservation competes with every other public spending "
               "priority, which is one of the three conflicts AQA names.",
    },
    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Each programme in a named context, each conflict from the side of the
    # person who holds it, and the first arithmetic on cost and numbers.
    {
        "id": "ks4-maintaining-biodiversity-s05",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why breeding an animal in a zoo does not on its own "
                "save the species.",
        "options": [
            "Animals bred in a zoo are sterile, so their numbers are "
                "unable to increase",
            "A zoo can hold one individual of any species at a time",
            "There must still be habitat in the wild for the animals to be "
                "returned to",
            "Zoo animals are a different species altogether from the wild "
                "ones of the same kind",
        ],
        "correct_index": 2,
        "why": "Captive breeding raises numbers, but unless the habitat the "
               "species needs still exists and the original threat has been "
               "removed there is nowhere for them to go.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s06",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why zoos exchange animals between one another as part "
                "of a breeding programme.",
        "options": [
            "It keeps the genetic variety high and avoids breeding close "
                "relatives",
            "It gives visitors something new to look at in every season",
            "It spreads the cost of feeding all of the animals out between "
                "all of the zoos involved",
            "It allows each zoo to keep exactly the same number of animals "
                "as the others",
        ],
        "correct_index": 0,
        "why": "A small captive population quickly becomes inbred; moving "
               "animals between collections keeps enough genetic variety for "
               "the population to stay healthy.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s07",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reserve costs 240 000 pounds a year and protects 400 "
                "hectares. Calculate the cost per hectare per year.",
        "options": [
            "60 pounds",
            "6000 pounds",
            "1667 pounds",
            "600 pounds",
        ],
        "correct_index": 3,
        "why": "240 000 ÷ 400 = 600 pounds per hectare each year.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s08",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a government might pay farmers to leave uncropped "
                "margins around their fields.",
        "options": [
            "The land is bought outright by the state, so the farmer no "
                "longer owns any part of it",
            "The farmer loses income from that land, so payment makes it "
                "worthwhile",
            "The margins grow a crop that the government buys at a "
                "guaranteed fixed price",
            "Payment is a fine imposed on farms that are too large to "
                "manage",
        ],
        "correct_index": 1,
        "why": "Land in margins grows no crop, so without a payment the farmer "
               "carries the whole cost of a benefit the public receives.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s09",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a seed bank is a cheaper way to protect plant "
                "species than a nature reserve.",
        "options": [
            "Seeds take little space and need no land to be set aside",
            "Seeds do not have to be kept cold, so no electricity is used",
            "Seeds can be sold to gardeners, which pays for the whole bank",
            "A seed bank needs no member of staff, because seeds look "
                "after themselves",
        ],
        "correct_index": 0,
        "why": "A freezer holds thousands of species in a few rooms, while a "
               "reserve needs land bought and then managed year after year.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s10",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain one thing a seed bank cannot protect that a nature "
                "reserve can.",
        "options": [
            "The seeds of plants that produce very small seeds indeed",
            "The genetic variation within a single plant species",
            "Plants that reproduce by making seeds rather than by cuttings",
            "The habitat itself, and the animals and fungi living in it",
        ],
        "correct_index": 3,
        "why": "A seed bank stores plants alone; the insects, fungi, birds and "
               "soil community of the habitat are not in it, and they cannot "
               "be replanted from a freezer.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s11",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a reintroduction can fail even when the animals "
                "released are healthy.",
        "options": [
            "A species lives in the place where it was born and nowhere "
                "else",
            "The threat that removed the species may still be present",
            "Healthy animals are unable to breed once they are released",
            "Released animals lose the ability to feed within just a few "
                "days of release",
        ],
        "correct_index": 1,
        "why": "If the habitat is still degraded, or the hunting or "
               "persecution that caused the loss continues, the released "
               "animals meet the same conditions that removed the original "
               "population.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s12",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a conservation charity monitors a species for "
                "years after a programme begins.",
        "options": [
            "Counting the animals is what causes their numbers to rise",
            "Monitoring keeps the charity's own staff in employment "
                "between its projects",
            "Only repeated counts show whether numbers are really "
                "recovering",
            "The law requires a count to be taken once in every decade",
        ],
        "correct_index": 2,
        "why": "Populations fluctuate for many reasons, so a single count "
               "after the work proves nothing; a trend over years is what "
               "shows whether the programme worked.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s13",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A population of 45 rare birds rises to 63 after a programme. "
                "Calculate the percentage increase.",
        "options": [
            "18%",
            "29%",
            "71%",
            "40%",
        ],
        "correct_index": 3,
        "why": "The rise is 63 − 45 = 18, and 18 ÷ 45 × 100 = 40%.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s14",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why local people are usually involved in planning a "
                "new reserve.",
        "options": [
            "They know which animals should be removed from the area first",
            "They live with the consequences, and a scheme they reject "
                "rarely works",
            "They are the people who are legally allowed to count species",
            "They can be made to pay for the reserve out of their own "
                "income",
        ],
        "correct_index": 1,
        "why": "Protection depends on the rules being kept day to day, and a "
               "scheme imposed on people whose livelihoods it damages is "
               "rarely kept.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s15",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how wildlife tourism can help maintain biodiversity "
                "in a poorer region.",
        "options": [
            "It replaces the species lost with the species brought in by "
                "visitors",
            "It means the animals are fed by visitors and need no habitat",
            "It gives local people an income from keeping the wildlife "
                "alive",
            "It removes the need for any protected area to be created "
                "anywhere in the region",
        ],
        "correct_index": 2,
        "why": "When wildlife is worth more alive than the land is worth "
               "cleared, the incentive that drives habitat loss is reversed.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s16",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why protecting a species that people have never heard "
                "of can still matter to those people.",
        "options": [
            "It may support a service such as pollination, decay or clean "
                "water",
            "Unknown species are the ones that governments will protect",
            "Every species is worth the same amount of money to a "
                "country's economy",
            "A species that nobody has ever heard of is far easier and "
                "cheaper to protect",
        ],
        "correct_index": 0,
        "why": "Ecosystem services come from whole communities, and the "
               "unglamorous species — decomposers, soil invertebrates, wild "
               "pollinators — do much of that work.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s17",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why regenerating a rare habitat can take decades "
                "rather than a single season.",
        "options": [
            "The species have to be bred in a zoo first, which takes "
                "decades",
            "Soil, plants and the species depending on them all develop "
                "slowly",
            "The law forbids any habitat work from being finished in under "
                "ten years",
            "Rare habitats can be worked on for one week in each year",
        ],
        "correct_index": 1,
        "why": "Structure builds up over years — soil, dead wood, the "
               "slow-colonising plants — and the specialist species arrive "
               "only once it has.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s18",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why recycling aluminium helps maintain biodiversity "
                "more than recycling the same mass of paper.",
        "options": [
            "Paper is made from trees that are planted rather than felled",
            "Aluminium is heavier, so more fits into each recycling lorry",
            "Aluminium comes from mining, which destroys habitat where the "
                "ore is dug",
            "Aluminium cannot be buried in landfill, unlike paper, which "
                "can",
        ],
        "correct_index": 2,
        "why": "Bauxite mining clears and excavates large areas, so recycling "
               "the metal avoids habitat destruction as well as the energy "
               "used in extraction.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s19",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a conservation programme protects a whole wetland "
                "rather than only its rarest bird.",
        "options": [
            "The bird needs the wetland's plants, invertebrates and water "
                "to live",
            "Protecting one bird is illegal unless the site is bought",
            "Wetlands are cheaper to protect than one bird species is",
            "The rarest bird is the sole species living in the wetland",
        ],
        "correct_index": 0,
        "why": "A species is held up by everything it eats, nests in and "
               "depends on, so the habitat is the unit that has to be kept.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s20",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an international agreement is needed to protect a "
                "migratory bird.",
        "options": [
            "Migratory birds are owned jointly by all of the countries "
                "that they cross over",
            "An international body must count the bird population each "
                "year",
            "The bird changes species each time it crosses a national "
                "border",
            "It uses several countries in a year, so one country cannot "
                "protect it",
        ],
        "correct_index": 3,
        "why": "Breeding grounds, stopover sites and wintering grounds may lie "
               "in different countries, and losing any one of them loses the "
               "population.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s21",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why reducing carbon dioxide emissions is counted as a "
                "measure that maintains biodiversity.",
        "options": [
            "Emissions cuts free up money that is then spent on reserves",
            "Lower emissions make plants grow larger and feed more animals",
            "Slower warming means fewer species pushed out of their range",
            "Carbon dioxide is toxic to life, so less of it lets many more "
                "species live",
        ],
        "correct_index": 2,
        "why": "Climate change is one of the named threats to biodiversity, so "
               "limiting it protects species that could not shift their range "
               "fast enough.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s22",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A charity has 90 000 pounds. A reserve costs 30 000 pounds a "
                "year to run. Calculate how many years it can be funded.",
        "options": [
            "3 years",
            "30 years",
            "2.7 years",
            "60 years",
        ],
        "correct_index": 0,
        "why": "90 000 ÷ 30 000 = 3 years of running costs.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s23",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a fishing community may accept a no-catch zone "
                "more readily if it is told the zone will be reviewed in five "
                "years.",
        "options": [
            "A review means the rule does not have to be obeyed until five "
                "years have passed",
            "Reviews are decided in favour of whoever objected the loudest",
            "Fish populations recover fully within exactly five years of "
                "any closure",
            "A reviewable rule feels reversible, so it is less of a threat "
                "to their future",
        ],
        "correct_index": 3,
        "why": "People accept restrictions more readily when they keep a voice "
               "in them, and a review date also lets the measure be judged "
               "against real data.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s24",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a captive population of only twelve individuals "
                "is a difficult starting point for a breeding programme.",
        "options": [
            "Small populations produce male offspring after a few years",
            "So few individuals carry little genetic variation, so "
                "inbreeding follows",
            "Twelve animals are too heavy for a zoo enclosure to hold",
            "A population must reach one hundred before any will breed",
        ],
        "correct_index": 1,
        "why": "A tiny founder group carries only a fraction of the species' "
               "genetic variation, and the inbreeding that follows lowers "
               "fertility and disease resistance.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s25",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why protecting biodiversity is sometimes described as "
                "protecting future medicines.",
        "options": [
            "Useful chemicals are still being found in wild species",
            "Medicines are stored inside the bodies of the animals being "
                "protected",
            "Doctors must use drugs taken from protected species",
            "Rare species produce more chemicals than common ones do",
        ],
        "correct_index": 0,
        "why": "Many drugs began as compounds found in plants, fungi or "
               "microorganisms, and a species lost before it is studied takes "
               "whatever it held with it.",
    },
    {
        "id": "ks4-maintaining-biodiversity-s26",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a government may find reducing deforestation "
                "abroad cheaper than protecting habitat at home.",
        "options": [
            "Habitat abroad does not need any management once it has been "
                "protected",
            "Foreign habitat holds no species, so it is cheaper to look "
                "after",
            "Protecting habitat at home is forbidden under the terms of an "
                "international agreement",
            "Land and labour cost less there, so each pound protects more "
                "habitat",
        ],
        "correct_index": 3,
        "why": "Cost per hectare varies enormously, so the same money can "
               "protect far more habitat where land is cheaper — though it "
               "protects different species.",
    },
    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Weighing measures against each other, weighing them against the three
    # conflicts, and judging what a programme has actually achieved.
    {
        "id": "ks4-maintaining-biodiversity-h05",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare spending one million pounds on a captive breeding "
                "programme with spending it on buying and protecting habitat.",
        "options": [
            "The two achieve exactly the same result, because both raise "
                "the number of individuals",
            "Habitat protection saves fewer species, because reserves hold "
                "the commonest ones",
            "Breeding saves one species; habitat protects a whole "
                "community for the same money",
            "Breeding protects more species, because a zoo can hold many "
                "species in one building",
        ],
        "correct_index": 2,
        "why": "Captive breeding is expensive per species and does not address "
               "the habitat loss, while a protected site keeps many species, "
               "and the conditions they need, at once.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h06",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reserve costs 90 000 pounds a year and holds 45 species. A "
                "second costs 150 000 pounds and holds 100 species. Determine "
                "which costs less per species.",
        "options": [
            "The second, at 1500 pounds per species",
            "The first, at 2000 pounds per species",
            "The first, at 1500 pounds per species",
            "The second, at 2000 pounds per species",
        ],
        "correct_index": 0,
        "why": "90 000 ÷ 45 = 2000 pounds per species and 150 000 ÷ 100 = 1500 "
               "pounds, so the second reserve is cheaper per species.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h07",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the argument that money spent on conservation should "
                "go to hospitals instead.",
        "options": [
            "It is not a conflict, because conservation costs almost "
                "nothing to run",
            "It settles the matter, because human health outweighs every "
                "other consideration",
            "It is not a conflict, because hospitals are funded from a "
                "completely separate source",
            "It is a real conflict, but ecosystems supply food, water and "
                "medicines people need",
        ],
        "correct_index": 3,
        "why": "The competing claim on the money is genuine, which is why the "
               "case for conservation is argued on the services and resources "
               "that people themselves depend on.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h08",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict what happens to a reintroduced population if only the "
                "captive-bred animals are released and the original threat "
                "remains.",
        "options": [
            "It moves to a new habitat, where the original threat cannot "
                "follow it",
            "It declines again, because the cause of the first loss is "
                "still acting",
            "It grows steadily, because captive-bred animals are stronger "
                "than wild ones",
            "It stays at the released number for ever, neither rising nor "
                "falling",
        ],
        "correct_index": 1,
        "why": "Reintroduction replaces individuals but not conditions; if the "
               "habitat loss, pollution or persecution continues, the new "
               "population meets the same fate.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h09",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a programme judged on the number of individuals "
                "alone can hide a real problem.",
        "options": [
            "Numbers can rise while genetic variation keeps falling",
            "Numbers cannot be counted accurately in any wild population",
            "The number of individuals is not related to whether a species "
                "survives",
            "Counting individuals disturbs them, so the count is wrong",
        ],
        "correct_index": 0,
        "why": "A population rebuilt from a few founders may be numerous and "
               "still carry too little variation to resist a new disease or "
               "adapt to change.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h10",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a species is safe once its numbers "
                "have doubled.",
        "options": [
            "It is sound, because a doubled population is no longer "
                "endangered by definition",
            "It is weak, because the number of individuals has nothing to "
                "do with extinction risk",
            "It is sound, because a species that can double its numbers "
                "will keep on doubling them",
            "It is weak, because doubling from a tiny base can still be a "
                "very small population",
        ],
        "correct_index": 3,
        "why": "Twice twenty is forty, which is still far below the size at "
               "which a population can absorb a bad year or a disease "
               "outbreak.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h11",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare protecting one 500 hectare site with protecting five "
                "100 hectare sites in different parts of a county.",
        "options": [
            "The two are identical, because the total protected area is "
                "500 hectares either way",
            "One site holds species needing large areas; five spread the "
                "risk of a local disaster",
            "One site is better in every respect, because a single large "
                "area holds more species",
            "Five sites are better in every respect, because five habitats "
                "are richer than one",
        ],
        "correct_index": 1,
        "why": "The answer depends on the species: area-demanding ones need "
               "the single block, while several sites survive a fire, flood or "
               "disease that would take out one.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h12",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why removing a grazing animal from a chalk grassland "
                "reserve can reduce its biodiversity.",
        "options": [
            "Grazing animals eat the seeds of scrub, and without them no "
                "grass can germinate",
            "Removing an animal raises biodiversity, because the plants "
                "are no longer eaten",
            "Without grazing, coarse grasses and scrub shade out the small "
                "flowering plants",
            "The grazing animal had been adding minerals that the soil "
                "needs to support plants",
        ],
        "correct_index": 2,
        "why": "Chalk grassland is a grazed habitat: without grazing it moves "
               "towards scrub and woodland, and the specialists of the open "
               "sward are lost.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h13",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country protects 8% of its 60 million hectares and aims for "
                "30%. Determine the extra area it must protect.",
        "options": [
            "18.0 million hectares",
            "22.0 million hectares",
            "4.8 million hectares",
            "13.2 million hectares",
        ],
        "correct_index": 3,
        "why": "8% of 60 million is 4.8 million and 30% is 18.0 million, so "
               "18.0 − 4.8 = 13.2 million hectares more.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h14",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a wealthy country may find it easier to protect "
                "habitat than a country where many people are poor.",
        "options": [
            "Habitat in a poorer country recovers on its own, so "
                "protection is not needed",
            "Where people depend on the land for food and fuel, setting it "
                "aside costs them directly",
            "Poorer countries hold no habitat that would be worth the "
                "trouble of protecting",
            "Wealthy countries have laws, and poorer countries are not "
                "allowed to make any",
        ],
        "correct_index": 1,
        "why": "Conservation competes with immediate need; where an income "
               "depends on the land, protection must come with an alternative, "
               "not only a rule.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h15",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate reintroducing a top predator to a landscape where "
                "farmers keep livestock.",
        "options": [
            "It cannot work, because a predator released into farmland "
                "will starve within weeks",
            "It is purely a scientific decision, so the views of farmers "
                "carry no weight in it",
            "It can restore the ecosystem, but the losses fall on farmers, "
                "so compensation is needed",
            "It is certain to succeed, because a predator restores the "
                "natural balance wherever it is released",
        ],
        "correct_index": 2,
        "why": "The ecological case can be strong while the cost falls on a "
               "few people, which is why such schemes carry compensation and "
               "local agreement or they fail.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h16",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why protecting an area on a map does not always "
                "protect the species inside it.",
        "options": [
            "A designation still needs funding, management and enforcement "
                "to mean anything",
            "Species leave any area once it is marked as protected on a "
                "map",
            "A map cannot be drawn accurately enough to include a whole "
                "habitat",
            "Protected areas attract more visitors, and visitors count as "
                "a threat",
        ],
        "correct_index": 0,
        "why": "A line on a map with no warden, no budget and no penalty is a "
               "paper park; the habitat can still be grazed, drained or "
               "poached.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h17",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wild population falls 8% a year from 5000. Determine the "
                "number after two years, to the nearest ten.",
        "options": [
            "3400",
            "4230",
            "4200",
            "4600",
        ],
        "correct_index": 1,
        "why": "After one year 5000 × 0.92 = 4600, and after two 4600 × 0.92 = "
               "4232, which is 4230 to the nearest ten.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h18",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a species protected by law can still decline "
                "sharply.",
        "options": [
            "The law applies to species that are already extinct in the "
                "wild",
            "Protected species are counted differently, which makes the "
                "figures fall",
            "A law protects the animals but not always the habitat they "
                "depend on",
            "Legal protection makes a species stop breeding while it is "
                "protected",
        ],
        "correct_index": 2,
        "why": "Killing may be banned while the meadow, wetland or hedgerow "
               "the species needs is drained or ploughed perfectly legally.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h19",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a ban on selling a rare species with a programme that "
                "gives local people an income from protecting it.",
        "options": [
            "A ban removes the trade; an income removes the reason to take "
                "it in the first place",
            "A ban is stronger in every case, because breaking it carries "
                "a legal penalty",
            "An income scheme is worse, because paying people just "
                "encourages them to take even more",
            "The two are identical, because each of them reduces the "
                "number of animals that are being taken",
        ],
        "correct_index": 0,
        "why": "A ban alone can push a trade underground where poverty drives "
               "it; giving the species a living value aligns the local "
               "interest with protecting it.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h20",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a conservation plan written for one species may "
                "damage another in the same reserve.",
        "options": [
            "Two species cannot live in the same reserve at the same time",
            "A plan may legally name one species and must ignore all "
                "others",
            "The second species is removed before the plan begins",
            "Managing for one species changes the habitat away from what "
                "another needs",
        ],
        "correct_index": 3,
        "why": "Cutting scrub for a butterfly removes nesting cover for birds; "
               "flooding for waders drowns a dry-ground plant — the management "
               "is a choice between communities.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h21",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that seed banks make nature reserves "
                "unnecessary for plants.",
        "options": [
            "It is weak, because seeds stored in a bank lose the ability "
                "to germinate within a year",
            "It is sound, because a seed bank holds the animals of the "
                "habitat as well as its plants",
            "It is weak, because a seed cannot be returned to a habitat "
                "that no longer exists",
            "It is sound, because every plant species can be stored as "
                "seed indefinitely",
        ],
        "correct_index": 2,
        "why": "Storage preserves the genetic material, but restoring a "
               "species needs somewhere with the right soil, climate, "
               "pollinators and fungi to plant it back into.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h22",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a target expressed as a percentage of land "
                "protected can be met without much benefit to biodiversity.",
        "options": [
            "Cheap, species-poor land can be designated to reach the "
                "figure",
            "Percentages cannot be measured accurately across the area of "
                "a whole country",
            "A percentage target ignores any land that is newly protected",
            "Any land that is protected holds the same number of species",
        ],
        "correct_index": 0,
        "why": "A target counts hectares, not value, so the cheapest land — "
               "mountain, moorland already unfarmed — can be designated while "
               "the richest lowland sites are still lost.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h23",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A programme costs 2.4 million pounds and saves 30 species. "
                "Determine the cost per species, and one limit of judging it "
                "that way.",
        "options": [
            "800 000 pounds each; it ignores how long the work will take",
            "80 000 pounds each; it counts the species that were lost",
            "8000 pounds each; it assumes the money is spent in a single "
                "year",
            "80 000 pounds each; it treats every species as equally "
                "valuable",
        ],
        "correct_index": 3,
        "why": "2 400 000 ÷ 30 = 80 000 pounds per species, but a cost per "
               "species treats a keystone predator and an obscure moss as "
               "worth the same.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h24",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a conservation measure that works in one country "
                "may fail in another.",
        "options": [
            "Species behave differently on each side of a national border",
            "The threat, the habitat and the way people use the land all "
                "differ",
            "Conservation measures are patented, so each one of them can "
                "be used a single time",
            "A measure is effective just in the country where it was first "
                "invented",
        ],
        "correct_index": 1,
        "why": "A measure has to match the threat it meets; a grazing regime, "
               "a quota or a payment scheme depends on local ecology, economy "
               "and enforcement.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h25",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the long-term effect on a reserve of protecting it "
                "perfectly while the climate around it warms.",
        "options": [
            "Its species change, as some can no longer live there and "
                "others move in",
            "Its species stay exactly the same, because the boundary "
                "excludes any kind of change",
            "It loses every species it holds, because a reserve cannot "
                "warm up",
            "Its species double in number, because warming suits every "
                "protected species",
        ],
        "correct_index": 0,
        "why": "A reserve protects a place, not a climate, so the community "
               "inside it shifts as conditions move outside the tolerance of "
               "its original species.",
    },
    {
        "id": "ks4-maintaining-biodiversity-h26",
        "subtopic_slug": "maintaining-biodiversity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the suggestion that conservation should protect the "
                "species people find most appealing.",
        "options": [
            "It is the right rule, because public support is the thing "
                "that matters",
            "It is wrong, because appealing species are not the ones that "
                "are under threat here",
            "It is the right rule, because appealing species support all "
                "of the others living in a habitat",
            "Appealing species raise money, but the ecosystem depends on "
                "unappealing ones too",
        ],
        "correct_index": 3,
        "why": "Charismatic species do attract funding and can act as "
               "umbrellas for a whole habitat, but a programme steered only by "
               "appeal leaves out most of what an ecosystem runs on.",
    },
]
