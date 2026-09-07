"""B11 lesson 04 — Biodiversity and gene banks: twelve questions (MRB-269).

These probe the two halves of the statutory clause the lesson owns whole — why
variation is worth keeping, and what each way of keeping it can and cannot do —
and they are built around the one move the page asks for: stop talking about the
plant and start talking about the population. The distractors come from the
lesson's two declared misconceptions, EVOL-07 (biodiversity is a count of
species) and EVOL-08 (we have gene banks, so a wild loss does not matter),
together with the beliefs the hook, the bench notes and the four bank cards are
drawn to catch: that clones are individually weaker or individually tougher,
that no two living things are ever quite identical so a resistant minority
always exists somewhere, that a monoculture is simply a mistake rather than a
trade-off, that freezing stops time, that stored material adapts to the freezer,
that a studbook holds variation constant, and that a slogan — always choose the
most variation — is a substitute for reading the yield bar. The harder band
works outside the potato field: a grafted apple orchard, the Aleppo withdrawal
from Svalbard read as evidence, forty generations of a captive bird, and a
blight that arrives one year in five. The lesson carries no figures — every
string on the page is drawn by the bench or by a card — so every question is
figure=None.
"""

UNIT = "B11"
LESSON = "biodiversity-and-gene-banks"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b11-04-e01",
        "band": "easier",
        "text": "The first field on the bench is a monoculture. What does "
                "that word mean?",
        "options": [
            {"text": "A crop grown as a single variety across a whole field "
                     "or region.",
             "correct": True},
            {"text": "A crop grown in the same field year after year instead "
                     "of being moved around.",
             "correct": False,
             "why": "The mono counts varieties, not years. Move a single "
                    "variety to a fresh field every season and it is still a "
                    "monoculture — one set of genes, one set of weaknesses."},
            {"text": "A crop grown from seed rather than from cuttings taken "
                     "off one parent plant.",
             "correct": False,
             "why": "Growing from seed is what gives you a landrace, where no "
                    "two plants are genetically identical. That is the other "
                    "end of the bench from a monoculture."},
            {"text": "A crop bred so that every plant carries resistance to "
                     "one named disease.",
             "correct": False,
             "why": "Resistance is something a variety may or may not carry. "
                    "Monoculture describes how little variation is standing "
                    "in the field, not which genes it happens to hold."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e02",
        "band": "easier",
        "text": "The lesson sets out four ways of keeping variation. Which "
                "one keeps the species inside a working ecosystem?",
        "options": [
            {"text": "Seed banks, because seed from a whole habitat is dried "
                     "and stored together.",
             "correct": False,
             "why": "A seed bank stores the species, not the world it lived "
                    "in. The pollinator, the soil fungus and the seed "
                    "disperser are not in the freezer beside it."},
            {"text": "Frozen sperm, eggs and tissue, because thousands of "
                     "species are held at once.",
             "correct": False,
             "why": "Holding thousands of species is not the same as holding "
                    "what they lived in. Frozen material also needs a "
                    "surrogate mother of a close species before it is an "
                    "animal at all."},
            {"text": "Protected habitat: populations stay where they are, "
                     "still breeding and evolving.",
             "correct": True},
            {"text": "Botanic gardens and zoos, because the organisms there "
                     "are alive rather than frozen.",
             "correct": False,
             "why": "Alive is not the same as wild. A captive population is "
                    "fed and bred deliberately, loses variation over "
                    "generations and adapts to captivity."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e03",
        "band": "easier",
        "text": "You plant the field of a thousand identical clones and "
                "release the blight. What is left standing?",
        "options": [
            {"text": "A handful, because a few individuals in any large "
                     "population are always tougher.",
             "correct": False,
             "why": "Tougher normally means genetically different, and these "
                    "thousand plants are the same plant repeated. If the "
                    "blight can kill one of them it can kill all of them."},
            {"text": "Nothing at all — there was only ever one plant, "
                     "repeated a thousand times.",
             "correct": True},
            {"text": "About a quarter, which is the share that comes through "
                     "in the four-variety field.",
             "correct": False,
             "why": "That 25% comes from one of four varieties carrying "
                    "resistance. This field has one variety and none of it "
                    "resists, so there is no quarter to come through."},
            {"text": "Most of them, because this field draws the highest "
                     "yield bar of the four.",
             "correct": False,
             "why": "Yield is what the field gives you in a good year. It "
                    "says nothing about a blight year, and that gap between "
                    "the two bars is the whole point of the bench."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e04",
        "band": "easier",
        "text": "A student writes that biodiversity is the number of "
                "different species in a place. What has been left out?",
        "options": [
            {"text": "The number of individuals belonging to each of those "
                     "species.",
             "correct": False,
             "why": "Counting individuals is still counting bodies. A "
                    "thousand potato clones is a thousand individuals with no "
                    "variation between any of them."},
            {"text": "The number of different habitats those species are "
                     "living across.",
             "correct": False,
             "why": "Habitat count is worth measuring, but it is not the half "
                    "of biodiversity this lesson turns on. The missing half "
                    "is inside each species."},
            {"text": "Nothing — that sentence is the full meaning of the "
                     "word.",
             "correct": False,
             "why": "That is the half most people stop at. A wood with forty "
                    "species in it, each reduced to a few close relatives, is "
                    "in far more trouble than the species count suggests."},
            {"text": "The genetic variation within each species, individual "
                     "to individual.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b11-04-s01",
        "band": "standard",
        "text": "A farmer has read all of this and still plants the "
                "one-variety field. What is the honest reason for that "
                "choice?",
        "options": [
            {"text": "There is no reason — planting one variety is a mistake "
                     "farmers keep repeating.",
             "correct": False,
             "why": "The bench is drawn to stop you saying that. Look at the "
                    "yield bar: the clone field is genuinely best at "
                    "something, which is exactly why the decision is hard."},
            {"text": "It gives the highest yield per plant in a good year, "
                     "and one harvest date rather than four.",
             "correct": True},
            {"text": "Cloned plants are hardier than plants grown from seed, "
                     "so they hold out longer.",
             "correct": False,
             "why": "Cloning copies whatever the original plant was, "
                    "weaknesses included. This is the field that loses "
                    "everything, not the one that holds out."},
            {"text": "The survivors of a blight year can be saved and "
                     "replanted the following spring, so nothing is really "
                     "lost.",
             "correct": False,
             "why": "In this field there are no survivors. Not one plant in a "
                    "thousand comes through, so there is nothing to replant — "
                    "that is what the zero means."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s02",
        "band": "standard",
        "text": "On the bench the four-variety field and the ten-variety "
                "field draw the same yield bar. So what separates them?",
        "options": [
            {"text": "The ten-variety field yields more per plant, which is "
                     "why anyone would plant it.",
             "correct": False,
             "why": "Read the yield bar again — the two are tied there. Ten "
                    "varieties buys you nothing in a good year; it buys you "
                    "more left standing in a bad one."},
            {"text": "The ten-variety field carries less variation, spread "
                     "more thinly across the field.",
             "correct": False,
             "why": "It carries more, not less. Ten varieties draws a taller "
                    "variation bar than four, and the extra survivors are "
                    "what that variation buys."},
            {"text": "Nothing else separates them — the two fields behave the "
                     "same way.",
             "correct": False,
             "why": "They behave the same in a good year only. Release the "
                    "blight and one keeps about a quarter of its plants while "
                    "the other keeps about two fifths."},
            {"text": "More survives the blight in the ten-variety field — "
                     "about 40% against about 25%.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s03",
        "band": "standard",
        "text": "A national seed bank is sealed up and left untouched for "
                "fifty years to save money. What goes wrong?",
        "options": [
            {"text": "Seeds do not keep for ever — never tested, never "
                     "regrown, they die quietly.",
             "correct": True},
            {"text": "The stored seed slowly adapts to the cold and stops "
                     "matching the wild plants.",
             "correct": False,
             "why": "A stored population does not adapt to anything, and that "
                    "is its real limitation: it is frozen in the state it was "
                    "collected in while the world outside carries on "
                    "changing."},
            {"text": "Nothing goes wrong — minus eighteen degrees keeps a "
                     "seed alive indefinitely.",
             "correct": False,
             "why": "Freezing slows a seed's ageing; it does not stop it. "
                    "That is why banks test and regrow samples on a cycle, "
                    "and why Aleppo's withdrawn seed was grown on and sent "
                    "back fresh."},
            {"text": "The record of which sample came from where would be "
                     "lost over that time.",
             "correct": False,
             "why": "Records are the easy part — samples are catalogued and "
                    "duplicated between countries. It is the living seed "
                    "itself that fifty untouched years would cost you."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s04",
        "band": "standard",
        "text": "A frozen zoo holds tissue from a rhino species now extinct "
                "in the wild. What else is needed before a calf could be "
                "born?",
        "options": [
            {"text": "Nothing else — thawing the tissue is enough, because "
                     "the animal is already stored.",
             "correct": False,
             "why": "Tissue is hereditary material, not an animal. It needs a "
                    "surrogate mother of a close species, and even then one "
                    "calf is not a functioning population."},
            {"text": "A second frozen sample, since one sample is never "
                     "enough to work from.",
             "correct": False,
             "why": "Duplicates protect against losing the store, which is "
                    "what Svalbard does for seed. The obstacle here is a "
                    "different one: frozen cells cannot develop without a "
                    "mother."},
            {"text": "A surrogate mother from a closely related species to "
                     "carry the pregnancy.",
             "correct": True},
            {"text": "A spell in a botanic garden or zoo before the animal is "
                     "released.",
             "correct": False,
             "why": "Living collections are a separate method, not a later "
                    "stage of this one — and captive populations lose "
                    "variation and adapt to captivity over generations."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b11-04-h01",
        "band": "harder",
        "text": "An orchard is planted with one grafted apple variety, every "
                "tree a clone. A fungus arrives that this variety cannot "
                "resist. What should you predict?",
        "options": [
            {"text": "The oldest and strongest trees pull through and the "
                     "orchard rebuilds from them.",
             "correct": False,
             "why": "The strength that matters here is genetic, and every "
                    "tree carries the same genes. Age cannot give a tree a "
                    "resistance its own variety does not have."},
            {"text": "A few trees resist anyway, because no two living things "
                     "are ever quite identical.",
             "correct": False,
             "why": "Grafted trees are cuttings of one original, so they are "
                    "identical in exactly the way that decides this. There is "
                    "no resistant minority hiding in the orchard."},
            {"text": "Grafted trees fight off disease better than trees grown "
                     "from apple seed.",
             "correct": False,
             "why": "Grafting is a way of copying a tree you already like, "
                    "not of toughening it. Growing from seed is what would "
                    "have given the orchard variation."},
            {"text": "Every tree can be infected: no resistant minority "
                     "exists for selection to act on.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h02",
        "band": "harder",
        "text": "Syria's seed bank at Aleppo became unreachable, so "
                "researchers withdrew its duplicates from Svalbard, grew them "
                "on in Lebanon and Morocco, and sent fresh seed back. What "
                "does that show?",
        "options": [
            {"text": "That seed can be locked away and left indefinitely, "
                     "provided the store stays cold.",
             "correct": False,
             "why": "The opposite. The reason those samples had to be grown "
                    "on in Lebanon and Morocco is that seed ages in storage "
                    "and has to be replaced with fresh."},
            {"text": "That a gene bank works as insurance, and that its seed "
                     "has to be regrown rather than simply left frozen.",
             "correct": True},
            {"text": "That a seed bank makes it safe to lose a crop "
                     "population from the fields, because the seed can "
                     "always be fetched back.",
             "correct": False,
             "why": "What was replaced was a store, not a landscape. Seed "
                    "came back as seed; the farms, soils and growers it "
                    "belonged to were never in the vault."},
            {"text": "That Svalbard held the only copy of those wheat and "
                     "barley varieties left anywhere.",
             "correct": False,
             "why": "Svalbard is a backup of backups — countries deposit "
                    "duplicates of what their own banks already hold. Aleppo's "
                    "samples were up there because they were copies."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h03",
        "band": "harder",
        "text": "A zoo keeps the last population of a bird for forty "
                "generations, breeding it carefully to a studbook. Released "
                "birds mostly fail. Which explanation fits?",
        "options": [
            {"text": "A studbook holds variation constant, so the losses must "
                     "be down to bad luck.",
             "correct": False,
             "why": "A studbook slows the loss by tracking who is related to "
                    "whom; it cannot add variation the small population never "
                    "had. Forty generations is long enough for that to bite."},
            {"text": "Living organisms cannot lose variation, because they go "
                     "on breeding every generation.",
             "correct": False,
             "why": "Breeding is when a small population loses it — the "
                    "versions of genes carried by the birds that never breed "
                    "are simply gone. Being alive is no protection."},
            {"text": "Captive populations lose variation and adapt to "
                     "captivity, so the released birds suit the zoo.",
             "correct": True},
            {"text": "Freezing tissue instead would have kept the birds ready "
                     "to release at any time.",
             "correct": False,
             "why": "Frozen material stays frozen material. It needs a "
                    "surrogate mother of a close species, and a stored "
                    "population is not a functioning one."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h04",
        "band": "harder",
        "text": "Blight reaches this region roughly one year in five. A "
                "farmer is choosing between the one-variety field and the "
                "ten-variety field. Which argument is soundest?",
        "options": [
            {"text": "Plant ten varieties — a little less yield in the four "
                     "good years, and a bad harvest instead of none in the "
                     "fifth.",
             "correct": True},
            {"text": "Plant one variety, because the highest yield in four "
                     "years out of five more than outweighs whatever the "
                     "fifth year costs.",
             "correct": False,
             "why": "In the bad year that field returns nothing — no crop and "
                    "no seed to plant the next spring. A loss you cannot "
                    "recover from is not traded against four good years."},
            {"text": "Plant the landrace, because the field with the most "
                     "variation is always the right choice.",
             "correct": False,
             "why": "Not always. The landrace draws the lowest yield bar of "
                    "the four, in every year, blight or no blight. Variation "
                    "is a price worth paying here, not a rule that ignores "
                    "the price."},
            {"text": "It makes no difference, because a blight only arrives "
                     "one year in five.",
             "correct": False,
             "why": "One year in five is often enough that a farmer plants "
                    "for it — and the field that returns nothing that year "
                    "also leaves nothing to plant the year after."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ───────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b11-04-e05",
        "band": "easier",
        "text": "What does it mean to say that one plant is a clone of "
                "another?",
        "options": [
            {"text": "It was grown from a seed produced by that plant.",
             "correct": False,
             "why": "A seed carries a new combination of genes, so a seedling "
                    "is not identical to its parent. A clone is made by taking "
                    "a piece of the plant itself."},
            {"text": "It is the same variety, so it is closely related to that "
                     "plant.",
             "correct": False,
             "why": "Members of a variety are closely related and not "
                    "identical. A clone is genetically the same plant, "
                    "copied."},
            {"text": "It was bred from that plant over several generations to "
                     "be very similar to it.",
             "correct": False,
             "why": "Breeding for similarity is how a variety is produced. A "
                    "clone skips the breeding entirely — it is a cutting of "
                    "the original."},
            {"text": "It is genetically identical to it, because it was grown "
                     "or copied from it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e06",
        "band": "easier",
        "text": "What is a landrace?",
        "options": [
            {"text": "A crop population grown from seed in one place over many "
                     "generations, so no two plants are identical.",
             "correct": True},
            {"text": "A crop variety bred by a company to give the highest "
                     "possible yield in a good year on good ground.",
             "correct": False,
             "why": "That describes a modern named variety, bred to be "
                    "uniform. A landrace is the opposite — a mixed population "
                    "nobody has made consistent."},
            {"text": "A wild plant that has never been grown as a crop.",
             "correct": False,
             "why": "A landrace is very much a crop, grown and harvested for "
                    "generations. What it is not is a single uniform variety."},
            {"text": "A field in which several different crop species are "
                     "grown together.",
             "correct": False,
             "why": "That is mixed cropping. A landrace is one crop species in "
                    "which the individual plants differ from one another."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e07",
        "band": "easier",
        "text": "How are seeds kept in a seed bank?",
        "options": [
            {"text": "Damp and just above freezing, so that they stay ready to "
                     "germinate.",
             "correct": False,
             "why": "Damp seeds would germinate or rot. They are dried first, "
                    "which is what allows them to be frozen and kept."},
            {"text": "Sealed in water at room temperature, in a dark store.",
             "correct": False,
             "why": "Water and warmth are what a seed needs in order to grow, "
                    "which is precisely what a store must prevent. Seeds are "
                    "dried and frozen instead."},
            {"text": "Dried, and held at around minus eighteen degrees "
                     "Celsius.",
             "correct": True},
            {"text": "Planted out every year in a garden, so that they are "
                     "never really stored.",
             "correct": False,
             "why": "Regrowing on a cycle is part of running a bank and is not "
                    "how the seeds are held in between. Between regrowings "
                    "they are dried and frozen."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e08",
        "band": "easier",
        "text": "What does a gene bank store?",
        "options": [
            {"text": "Written descriptions of the genes of species that are at "
                     "risk.",
             "correct": False,
             "why": "A written description cannot be planted or bred from. A "
                    "bank holds the living hereditary material itself."},
            {"text": "Hereditary material — seeds, sperm, eggs or tissue — "
                     "kept so that variation can be recovered later.",
             "correct": True},
            {"text": "Whole living animals and plants, kept in enclosures "
                     "until they are needed for release back into the "
                     "wild.",
             "correct": False,
             "why": "That describes a zoo or a botanic garden, which is a "
                    "separate method with its own limits. A gene bank stores "
                    "material, not living populations."},
            {"text": "Soil and water samples from the habitats the species "
                     "came from.",
             "correct": False,
             "why": "Habitat samples are not hereditary material and cannot "
                    "regrow a species. What a bank keeps is seed, sperm, eggs "
                    "or tissue."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e09",
        "band": "easier",
        "text": "What happened to the Gros Michel banana in the 1950s?",
        "options": [
            {"text": "It was replaced because shoppers preferred the taste of "
                     "the Cavendish.",
             "correct": False,
             "why": "Taste is not what ended it. A fungal disease made it "
                    "impossible to grow commercially, and the Cavendish was "
                    "the replacement."},
            {"text": "It was crossed with a wild banana to produce the "
                     "Cavendish.",
             "correct": False,
             "why": "The Cavendish is a separate variety, not a cross made "
                    "from the Gros Michel. The Gros Michel was lost "
                    "commercially to disease."},
            {"text": "A fungus wiped it out commercially, and the Cavendish "
                     "replaced it.",
             "correct": True},
            {"text": "It was banned after a disease was found in the fruit.",
             "correct": False,
             "why": "Nothing was banned. The plants themselves were killed by "
                    "a fungus, so the variety could no longer be grown at "
                    "scale."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e10",
        "band": "easier",
        "text": "Which way of keeping variation holds frozen material from "
                "thousands of animal species, including some already extinct "
                "in the wild?",
        "options": [
            {"text": "Frozen sperm, eggs and tissue.",
             "correct": True},
            {"text": "Seed banks.",
             "correct": False,
             "why": "Seed banks hold plants. There is no seed to store for an "
                    "animal, which is exactly why frozen sperm, eggs and "
                    "tissue exist."},
            {"text": "Botanic gardens and zoos.",
             "correct": False,
             "why": "Those hold living organisms, in small numbers and at "
                    "considerable expense. The frozen stores hold material "
                    "from far more species."},
            {"text": "Protected habitat.",
             "correct": False,
             "why": "Protected habitat keeps populations where they are, alive "
                    "and breeding. Nothing about it is frozen or stored."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e11",
        "band": "easier",
        "text": "A farmer plants four varieties of potato, 250 plants of each. "
                "What does that give the field?",
        "options": [
            {"text": "A thousand genetically different plants, one for every "
                     "plant in the field, since no two potatoes are "
                     "ever quite the same.",
             "correct": False,
             "why": "Plants within one variety are bred to be alike, so four "
                    "varieties is four kinds of plant rather than a thousand "
                    "different ones."},
            {"text": "Four different species of potato growing side by side.",
             "correct": False,
             "why": "They are all one species. A variety is a named type "
                    "within a crop species, not a species of its own."},
            {"text": "Four plants that resist disease, and the rest that do "
                     "not.",
             "correct": False,
             "why": "Resistance is not what the word variety means, and a "
                    "variety may carry none. What four varieties gives you is "
                    "four kinds of plant."},
            {"text": "Four kinds of plant, each bred to be consistent, so "
                     "plants within a kind are closely related.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e12",
        "band": "easier",
        "text": "Seed banks cannot be used for every plant species. Which "
                "plants are the problem?",
        "options": [
            {"text": "Plants whose seeds are too small to be handled and "
                     "catalogued.",
             "correct": False,
             "why": "Very small seeds are stored easily and in enormous "
                    "numbers. The difficulty is biological rather than "
                    "practical."},
            {"text": "Plants whose seeds do not survive being dried and "
                     "frozen.",
             "correct": True},
            {"text": "Plants that produce very few seeds in a season.",
             "correct": False,
             "why": "A small harvest makes collecting slower rather than "
                    "impossible. What rules a species out is seed that cannot "
                    "be dried or frozen at all."},
            {"text": "Plants that are already extinct in the wild.",
             "correct": False,
             "why": "Material from species extinct in the wild is exactly what "
                    "banks are valued for holding. The obstacle is the seed's "
                    "own tolerance of drying and freezing."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e13",
        "band": "easier",
        "text": "What is the Svalbard Global Seed Vault?",
        "options": [
            {"text": "The only seed bank in the world, holding every stored "
                     "crop sample there is.",
             "correct": False,
             "why": "There are many national seed banks. Svalbard is a backup "
                    "of backups, holding duplicates of what those banks "
                    "already keep."},
            {"text": "A greenhouse in the Arctic where rare crops are grown "
                     "and studied.",
             "correct": False,
             "why": "Nothing is grown there. It is a cold store cut into rock, "
                    "holding sealed packets of dried seed."},
            {"text": "A store inside an Arctic mountain holding duplicate seed "
                     "samples sent by banks worldwide.",
             "correct": True},
            {"text": "A laboratory that creates new crop varieties for "
                     "countries to plant.",
             "correct": False,
             "why": "It creates nothing. It keeps copies of what already "
                    "exists, so that a country losing its own bank has "
                    "somewhere to draw from."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b11-04-s05",
        "band": "standard",
        "text": "A mixed landrace of potatoes comes through a blight better "
                "than any named variety does. Why do commercial farms not "
                "simply plant landraces?",
        "options": [
            {"text": "Because a landrace holds too little variation to be "
                     "worth growing.",
             "correct": False,
             "why": "It holds more than any of the alternatives — no two "
                    "plants in it are genetically identical. That is why it "
                    "survives a blight so well."},
            {"text": "Because it yields less per plant and is nearly "
                     "impossible to harvest by machine.",
             "correct": True},
            {"text": "Because a landrace cannot be replanted from its own "
                     "seed.",
             "correct": False,
             "why": "Replanting from its own seed is exactly how a landrace is "
                    "kept going. The obstacles are yield and harvesting."},
            {"text": "Because a landrace is more likely to carry disease into "
                     "the field.",
             "correct": False,
             "why": "It carries no more disease than any other planting. What "
                    "it carries is variation, and its costs are yield and "
                    "convenience."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s06",
        "band": "standard",
        "text": "After a blight passes through a field of several potato "
                "varieties, about a quarter of the plants are still standing. "
                "Why is the seed from those survivors worth more to the farmer "
                "than the crop itself?",
        "options": [
            {"text": "Because seed sells for a higher price than potatoes "
                     "grown for eating.",
             "correct": False,
             "why": "Price is not the point. The value of that seed is what is "
                    "inside it — plants that have already proved they resist "
                    "this blight."},
            {"text": "Because seed can be stored for longer than a harvested "
                     "crop.",
             "correct": False,
             "why": "Storage life is a convenience. What makes this seed "
                    "valuable is that it came from plants the blight could not "
                    "kill."},
            {"text": "Because those plants resisted the blight, so next year's "
                     "field can be planted from them.",
             "correct": True},
            {"text": "Because a quarter of a harvest is not enough food to be "
                     "worth selling.",
             "correct": False,
             "why": "A quarter of a harvest is a bad year and it is still "
                    "food. The seed matters for what it will grow next spring, "
                    "not because the crop is too small."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s07",
        "band": "standard",
        "text": "A grower says that planting four varieties instead of one "
                "makes his field four times safer from disease. What is wrong "
                "with that?",
        "options": [
            {"text": "Safety depends on whether any of the four happens to "
                     "resist this disease, not on the number four.",
             "correct": True},
            {"text": "Nothing is wrong — four varieties really does give four "
                     "times the protection, so the risk of losing the "
                     "crop falls to a quarter.",
             "correct": False,
             "why": "The number of varieties is not a multiplier. If none of "
                    "the four resists the disease that arrives, the field is "
                    "no safer than one variety would have been."},
            {"text": "It is wrong because four varieties is less variation "
                     "than one.",
             "correct": False,
             "why": "Four varieties is far more variation than one. The error "
                    "is in treating the count as a guarantee rather than as a "
                    "better chance."},
            {"text": "It is wrong because varieties always resist different "
                     "diseases from each other.",
             "correct": False,
             "why": "They may resist the same one, or none at all. That "
                    "uncertainty is precisely why the count cannot be turned "
                    "into a figure for safety."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s08",
        "band": "standard",
        "text": "Seed of a wild plant is collected and frozen in 2020 and "
                "grown out again a century later, by which time the climate "
                "where it came from has changed. What problem does that "
                "create?",
        "options": [
            {"text": "The seed will have become adapted to the freezer.",
             "correct": False,
             "why": "Nothing adapts in storage, and that is the point. A "
                    "frozen sample does not change at all, which is a "
                    "different problem from changing wrongly."},
            {"text": "The seed will have lost its ability to germinate over a "
                     "century.",
             "correct": False,
             "why": "That is a risk if the bank never tests or regrows it, and "
                    "it is a matter of management. The deeper problem is what "
                    "the plant meets when it comes out."},
            {"text": "There will be no way to identify which population the "
                     "seed came from.",
             "correct": False,
             "why": "Samples are catalogued carefully, and records are the "
                    "easy part. The difficulty here is biological."},
            {"text": "The stored plants stopped changing in 2020, while the "
                     "place they came from carried on changing.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s09",
        "band": "standard",
        "text": "Two woods each hold forty plant species. In the first, each "
                "species is a large varied population; in the second, each has "
                "been reduced to a handful of close relatives. The species "
                "count is the same. Which wood is in more trouble?",
        "options": [
            {"text": "Neither — the same number of species means the same "
                     "biodiversity, whatever the populations of each "
                     "of them look like.",
             "correct": False,
             "why": "Species count is one half of biodiversity and the other "
                    "half is inside each species. Forty species of close "
                    "relatives is far less variety than forty varied "
                    "populations."},
            {"text": "The first, because large populations attract more "
                     "disease.",
             "correct": False,
             "why": "Large varied populations are the ones most likely to "
                    "contain individuals that survive a disease. Size and "
                    "variety are protection here, not risk."},
            {"text": "The second, because each of its species has almost no "
                     "variation left to survive a change with.",
             "correct": True},
            {"text": "The second, but only because it holds fewer individual "
                     "plants altogether.",
             "correct": False,
             "why": "It may hold plenty of plants. What it does not hold is "
                    "difference between them, and that is what a population "
                    "needs when conditions change."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s10",
        "band": "standard",
        "text": "A zoo breeding programme keeps a studbook recording which "
                "animals are related to which. What is it for?",
        "options": [
            {"text": "To avoid breeding close relatives together, so that as "
                     "much variation as possible is kept.",
             "correct": True},
            {"text": "To record which animals came from which country.",
             "correct": False,
             "why": "Origins are recorded for other reasons. The studbook's "
                    "job is genetic — it tracks relatedness so that pairings "
                    "do not throw variation away."},
            {"text": "To decide which animals are strong enough to be "
                     "released.",
             "correct": False,
             "why": "Release decisions are made on other grounds. A studbook "
                    "is about who is related to whom, and therefore who should "
                    "not be bred together."},
            {"text": "To increase the variation in the captive population with "
                     "each generation of animals bred in the "
                     "collection.",
             "correct": False,
             "why": "It cannot add variation that is not there. The most a "
                    "studbook can do is slow the rate at which a small "
                    "population loses what it has."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s11",
        "band": "standard",
        "text": "A breed of dog descended from a small number of founding "
                "animals has a heart condition that appears in a very high "
                "proportion of individuals. Which idea does that illustrate?",
        "options": [
            {"text": "Clones are always weaker than animals produced by "
                     "ordinary breeding.",
             "correct": False,
             "why": "These dogs are not clones, and they are not weaker in "
                    "general. The trouble is that a version of a gene common "
                    "in the founders is now common in all of them."},
            {"text": "A large population is always safer than a small one, "
                     "whatever its history, because numbers are what "
                     "protect a population.",
             "correct": False,
             "why": "This breed may run to many thousands of dogs. What "
                    "matters is how much variation those thousands hold, and a "
                    "few founders means very little."},
            {"text": "Diseases spread more easily between animals that are "
                     "closely related.",
             "correct": False,
             "why": "This condition is not spreading between dogs at all — it "
                    "is inherited. What is shared is genes, not an infection."},
            {"text": "A population descended from very few individuals holds "
                     "little variation, so a weakness is shared by all.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s12",
        "band": "standard",
        "text": "A country's seed bank holds a single sample of each of its "
                "three hundred crop varieties, all in one building. Name the "
                "weakness in that arrangement.",
        "options": [
            {"text": "Three hundred varieties is too few to be worth "
                     "storing in a building of that size.",
             "correct": False,
             "why": "Three hundred varieties is a great deal of variation to "
                    "hold. The weakness is not in the number but in where it "
                    "all sits."},
            {"text": "One fire, flood or war reaches everything at once, "
                     "because nothing is duplicated elsewhere.",
             "correct": True},
            {"text": "Samples kept together in one building will "
                     "cross-pollinate each other.",
             "correct": False,
             "why": "Dried seed in sealed packets does nothing of the kind. "
                    "The risk is that a single event destroys the whole "
                    "collection."},
            {"text": "A single sample of a variety cannot be regrown.",
             "correct": False,
             "why": "A sample holds many seeds and can be grown on. What it "
                    "cannot do is survive an event that destroys the building "
                    "it is in."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s13",
        "band": "standard",
        "text": "A new blight arrives that none of the ten varieties in a "
                "mixed field happens to resist. What happens, and what does it "
                "show about variation?",
        "options": [
            {"text": "Some plants survive anyway, because a field with ten "
                     "varieties always keeps something.",
             "correct": False,
             "why": "Variation only helps if some of it happens to suit the "
                    "threat. Ten varieties that all fall to this blight leave "
                    "nothing standing."},
            {"text": "Nothing survives, which shows that planting several "
                     "varieties is not worth doing and the effort is "
                     "wasted every time.",
             "correct": False,
             "why": "It is worth doing, and it is not a guarantee. Several "
                    "varieties give a real chance that one resists — this time "
                    "none did."},
            {"text": "Nothing survives — variation helps only when some of it "
                     "happens to suit the threat that arrives.",
             "correct": True},
            {"text": "Nothing survives, because ten varieties is really only "
                     "one variety spread thinly.",
             "correct": False,
             "why": "Ten varieties is ten genuinely different kinds of plant. "
                    "They failed because none of them met this particular "
                    "disease, not because they were secretly the same."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b11-04-h05",
        "band": "harder",
        "text": "A field holds a thousand potato plants, planted as ten "
                "varieties with a hundred plants of each. Four of the ten "
                "varieties resist a blight that sweeps the field, and the rest "
                "are killed. How many plants are left standing, and what share "
                "of the field is that?",
        "options": [
            {"text": "4 plants, which is 0.4% of the field.",
             "correct": False,
             "why": "Four is the number of varieties, not the number of "
                    "plants. Each variety is a hundred plants, so four of them "
                    "is four hundred."},
            {"text": "400 plants, which is 40% of the field.",
             "correct": True},
            {"text": "100 plants, which is 10% of the field.",
             "correct": False,
             "why": "A hundred plants is one variety's worth. Four varieties "
                    "resist, so four hundred plants come through."},
            {"text": "600 plants, which is 60% of the field.",
             "correct": False,
             "why": "Six hundred is the number killed — the six varieties that "
                    "do not resist. The question asks what is left standing."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h06",
        "band": "harder",
        "text": "A farmer keeps seed only from the four hundred plants that "
                "survived a blight, and plants his whole field from them the "
                "following spring. What has he gained, and what has he lost?",
        "options": [
            {"text": "He has gained a resistant crop and lost nothing, since "
                     "the dead plants were of no use.",
             "correct": False,
             "why": "The dead varieties carried versions of genes that might "
                    "have resisted something else. Losing them is a real cost, "
                    "even though they failed this time."},
            {"text": "He has lost his resistance to this blight, because "
                     "resistance is not inherited.",
             "correct": False,
             "why": "Resistance is inherited, which is why keeping the "
                    "survivors' seed works at all. What he has lost is the "
                    "variation the other varieties held."},
            {"text": "He has a field that resists this blight, and much less "
                     "variation to meet the next threat with.",
             "correct": True},
            {"text": "He has gained variation, because the survivors are the "
                     "strongest plants in the field.",
             "correct": False,
             "why": "Survivors are not the strongest, they are the resistant "
                    "ones, and there are fewer kinds of them. The field now "
                    "holds less variation than it did, not more."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h07",
        "band": "harder",
        "text": "Nearly all commercial coffee comes from a small number of "
                "closely related plants, while many wild coffee species still "
                "grow in Ethiopian forest. Why do plant breeders care about "
                "protecting that forest?",
        "options": [
            {"text": "The variation they will need against a future disease "
                     "exists there and almost nowhere else.",
             "correct": True},
            {"text": "Wild coffee produces a better crop than the cultivated "
                     "kind.",
             "correct": False,
             "why": "Wild coffee generally yields poorly and tastes unlike the "
                    "commercial crop. Its value is the variation it holds, not "
                    "what it would produce on a plantation."},
            {"text": "The forest keeps the climate suitable for growing coffee "
                     "elsewhere.",
             "correct": False,
             "why": "Forests do affect local climate, and that is not what "
                    "breeders are protecting here. They are protecting a store "
                    "of versions of genes the crop does not have."},
            {"text": "Growing coffee in a forest is cheaper than growing it on "
                     "a plantation.",
             "correct": False,
             "why": "Cost is not the argument. What the forest holds is "
                    "variation that a crop of closely related plants has lost, "
                    "and which cannot be invented when it is needed."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h08",
        "band": "harder",
        "text": "A seed bank holds ten thousand samples and can afford to test "
                "and regrow two hundred of them each year. On average, how "
                "often is any one sample checked, and why does that matter?",
        "options": [
            {"text": "Every two years, which is often enough to keep every "
                     "sample alive.",
             "correct": False,
             "why": "Two hundred checks a year across ten thousand samples is "
                    "nothing like every two years. Divide the collection by "
                    "the yearly rate: it is one check every fifty years."},
            {"text": "Every twenty years, which is comfortably inside the life "
                     "of a stored seed.",
             "correct": False,
             "why": "That would need five hundred checks a year. Ten thousand "
                    "divided by two hundred gives one check every fifty years, "
                    "which is a very long time for dried seed."},
            {"text": "Every fifty years, and it does not matter because "
                     "freezing stops seeds ageing.",
             "correct": False,
             "why": "The interval is right and the conclusion is not. Freezing "
                    "slows a seed's ageing rather than stopping it, so samples "
                    "can die unnoticed between checks."},
            {"text": "Every fifty years, so some samples will have died before "
                     "anyone looks at them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h09",
        "band": "harder",
        "text": "A new fungus is destroying a wheat crop grown as a handful of "
                "modern varieties. A plant breeder needs wheat that resists "
                "it. Where should she look, and why?",
        "options": [
            {"text": "In the modern varieties themselves, breeding them "
                     "together until resistance appears.",
             "correct": False,
             "why": "Breeding cannot create a version of a gene that none of "
                    "the parents has. Crossing susceptible varieties gives "
                    "more susceptible wheat."},
            {"text": "In gene banks and old landraces, because the resistance "
                     "has to exist somewhere already.",
             "correct": True},
            {"text": "In the fungus, because studying it will show how to make "
                     "the wheat resist.",
             "correct": False,
             "why": "Understanding the fungus helps and does not supply a "
                    "resistant plant. The resistance must already exist in "
                    "some wheat somewhere before it can be bred in."},
            {"text": "Nowhere in particular, because resistance can be "
                     "produced to order once it is needed.",
             "correct": False,
             "why": "Nothing produces a needed characteristic on demand. A "
                    "breeder's whole job here is to find variation that "
                    "already exists and move it into the crop."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h10",
        "band": "harder",
        "text": "The Gros Michel banana was destroyed commercially by a "
                "fungus, and the Cavendish that replaced it is itself grown as "
                "a single clone, now threatened by a similar fungus. What does "
                "that sequence show?",
        "options": [
            {"text": "That the Cavendish was a poor choice of replacement "
                     "variety, and a tougher one should have been "
                     "picked.",
             "correct": False,
             "why": "Any single variety would have been in the same position. "
                    "The problem is not which clone was chosen but that a "
                    "clone was chosen at all."},
            {"text": "That fungal diseases of bananas have become more "
                     "powerful over time.",
             "correct": False,
             "why": "Nothing here says the fungus has become stronger. What "
                    "has stayed the same is a crop with no variation for a "
                    "disease to fail against."},
            {"text": "That the vulnerability lies in growing a crop as one "
                     "clone, not in the particular variety.",
             "correct": True},
            {"text": "That bananas cannot be grown safely at all, whatever is "
                     "planted.",
             "correct": False,
             "why": "Bananas grown from a range of varieties would not be in "
                    "this position. The danger comes from the way they are "
                    "grown, and that is a choice."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h11",
        "band": "harder",
        "text": "A named potato variety is grown from tubers and every plant "
                "of it is closely related. A landrace is grown from seed. Why "
                "does the landrace keep its variation year after year while "
                "the variety does not?",
        "options": [
            {"text": "Seed carries new combinations of genes, so the plants "
                     "differ; a tuber copies one plant.",
             "correct": True},
            {"text": "Landraces are grown in more places, so they pick up more "
                     "variation.",
             "correct": False,
             "why": "Growing somewhere new does not add versions of genes to a "
                    "crop. The variation comes from being grown from seed, "
                    "where each plant is a new combination."},
            {"text": "A named variety loses its variation because farmers "
                     "select the best plants each year.",
             "correct": False,
             "why": "Selecting can reduce variation and is not what makes a "
                    "variety uniform. A variety is uniform because it is bred "
                    "that way and often propagated from pieces of one plant."},
            {"text": "Landraces grow more slowly, which gives their variation "
                     "time to build up.",
             "correct": False,
             "why": "Variation does not build up over a growing season. It is "
                    "present in every generation because every plant is grown "
                    "from seed."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h12",
        "band": "harder",
        "text": "A gene bank holds two hundred seeds of a rare plant, all "
                "collected from one hillside on one day in 1975. In what sense "
                "does the bank not hold the species?",
        "options": [
            {"text": "In no sense — two hundred seeds is plenty to bring a "
                     "species back.",
             "correct": False,
             "why": "It is enough to grow plants and not enough to hold what "
                    "the species was. Those seeds came from one population on "
                    "one day."},
            {"text": "The seeds will not be viable after so long, so nothing "
                     "is really held.",
             "correct": False,
             "why": "Well-managed samples are tested and regrown, so viability "
                    "is a question of management. The deeper limitation is "
                    "what was collected in the first place."},
            {"text": "The bank holds the plant but not its name, so the "
                     "species could not be identified.",
             "correct": False,
             "why": "Records are careful and identification is the easy part. "
                    "What is missing is the variation held by every population "
                    "that was not sampled."},
            {"text": "It holds a sample of one population at one moment, not "
                     "the variation of the whole species.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h13",
        "band": "harder",
        "text": "Two arguments are given for keeping biodiversity: that useful "
                "medicines have come from wild species, and that variation is "
                "what lets populations survive change. Which is the stronger "
                "biological argument?",
        "options": [
            {"text": "The medicines argument, because it can be shown with "
                     "real examples such as penicillin.",
             "correct": False,
             "why": "Real examples make it persuasive rather than fundamental. "
                    "Medicines are a use we happen to have found; variation is "
                    "what decides whether populations survive at all."},
            {"text": "The variation argument, because without variation a "
                     "population cannot survive a change of any kind.",
             "correct": True},
            {"text": "Neither is biological — both are really arguments about "
                     "what species are worth to people.",
             "correct": False,
             "why": "The variation argument is not about worth to people at "
                    "all. It is a statement about how populations survive, and "
                    "it would hold if no human had ever existed."},
            {"text": "The medicines argument, because a species with no known "
                     "use is not worth protecting.",
             "correct": False,
             "why": "That reverses the reasoning. Most species have no use yet "
                    "identified, and their variation is doing exactly the same "
                    "work in their own populations."},
        ],
        "figure": None,
    },
]
