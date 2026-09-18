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
            {"text": "The only seed bank in the world, holding the single "
                     "stored sample of every crop there is.",
             "correct": False,
             "why": "There are many national seed banks. Svalbard is a backup "
                    "of backups, holding duplicates of what those banks "
                    "already keep."},
            {"text": "A greenhouse in the Arctic where rare crops are grown "
                     "and studied.",
             "correct": False,
             "why": "Nothing is grown there. It is a cold store cut into rock, "
                    "holding sealed packets of dried seed."},
            {"text": "An Arctic mountain store holding duplicate seed samples "
                     "from banks worldwide.",
             "correct": True},
            {"text": "A laboratory that creates new crop varieties for "
                     "countries to plant in future.",
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
            {"text": "Because a landrace holds far too little variation to be "
                     "worth a commercial farm's while.",
             "correct": False,
             "why": "It holds more than any of the alternatives — no two "
                    "plants in it are genetically identical. That is why it "
                    "survives a blight so well."},
            {"text": "Because it yields less and cannot easily be harvested "
                     "by machine.",
             "correct": True},
            {"text": "Because a landrace cannot be replanted from its own "
                     "seed.",
             "correct": False,
             "why": "Replanting from its own seed is exactly how a landrace is "
                    "kept going. The obstacles are yield and harvesting."},
            {"text": "Because a landrace is more likely to carry disease into "
                     "the field with it.",
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
            {"text": "Because seed sells for a considerably higher price per "
                     "tonne than potatoes grown for eating.",
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
            {"text": "Because those plants resisted the blight and can seed "
                     "next year's field.",
             "correct": True},
            {"text": "Because a quarter of a harvest is not nearly enough "
                     "food to be worth selling.",
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
            {"text": "The seeds will not still be viable after so long, so "
                     "nothing is really held.",
             "correct": False,
             "why": "Well-managed samples are tested and regrown, so viability "
                    "is a question of management. The deeper limitation is "
                    "what was collected in the first place."},
            {"text": "The bank holds the plant but not its name, so the "
                     "species could not later be identified.",
             "correct": False,
             "why": "Records are careful and identification is the easy part. "
                    "What is missing is the variation held by every population "
                    "that was not sampled."},
            {"text": "It holds one population at one moment, not the whole "
                     "species' variation.",
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

    # ── MRB-338 night 3 top-up (17 easier / 17 standard / 17 harder) ───


    # ===================== EASIER (e14-e30) =====================
    {
        "id": "b11-04-e14",
        "band": "easier",
        "text": "Seed banks and frozen tissue banks are both examples of a "
                "more general kind of store. What is that more general term?",
        "options": [
            {"text": "A biobank: a laboratory that studies genes without "
                     "keeping any living material.",
             "correct": False,
             "why": "A biobank that keeps nothing living could not later "
                    "regrow anything. The stores this lesson describes keep "
                    "material capable of growing into a new organism."},
            {"text": "A gene bank: a store of hereditary material kept to "
                     "preserve variation for later.",
             "correct": True},
            {"text": "A studbook: a written record of which animals happen "
                     "to be related to which.",
             "correct": False,
             "why": "A studbook is a record on paper, kept alongside a "
                    "living captive population. It stores no hereditary "
                    "material of its own."},
            {"text": "A herbarium: a collection of dried, pressed plant "
                     "specimens kept for identification.",
             "correct": False,
             "why": "A pressed specimen is dead and cannot be regrown. The "
                    "term covers stores that keep material capable of "
                    "producing a new organism."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e15",
        "band": "easier",
        "text": "Every wild population of a moss has died out, but its "
                "spores are still kept, dried, in a seed bank. What term "
                "describes its current status?",
        "options": [
            {"text": "Endangered, since its numbers are dangerously low in "
                     "the wild.",
             "correct": False,
             "why": "Endangered species still have living wild populations, "
                    "just at serious risk. This species has none left at "
                    "all."},
            {"text": "Extinct in the wild, since none survive outside "
                     "storage.",
             "correct": True},
            {"text": "Fully extinct, since no individual survives in any "
                     "form.",
             "correct": False,
             "why": "Fully extinct means no living material survives "
                    "anywhere, including in storage. Frozen cells still "
                    "existing is exactly what this term is for."},
            {"text": "Vulnerable, since it faces a real but manageable "
                     "risk.",
             "correct": False,
             "why": "Vulnerable describes a species facing a real but "
                    "smaller risk, usually with a healthy wild population "
                    "still standing."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e16",
        "band": "easier",
        "text": "In which region are potato landraces still grown by small "
                "farms today, the way the lesson describes?",
        "options": [
            {"text": "Northern Europe, close to the main commercial potato "
                     "regions.",
             "correct": False,
             "why": "Northern Europe grows potatoes mainly as named "
                    "commercial varieties. The landrace farming the lesson "
                    "describes is in the crop's region of origin."},
            {"text": "The Andes, the only region where the potato "
                     "originated.",
             "correct": True},
            {"text": "Coastal Australia, a region where blight has never "
                     "been recorded.",
             "correct": False,
             "why": "The lesson does not place landrace farming there, and "
                    "it is blight risk that makes variation worth keeping, "
                    "not its absence."},
            {"text": "The Arctic, near where the Svalbard seed vault is "
                     "built.",
             "correct": False,
             "why": "Svalbard only stores seed samples; nothing is grown "
                    "there. The Arctic is far too cold to farm potatoes at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e17",
        "band": "easier",
        "text": "What practical problem limits protected habitat as a way of "
                "keeping variation, according to the lesson?",
        "options": [
            {"text": "It only ever works for species that produce a seed.",
             "correct": False,
             "why": "That limit belongs to seed banks. Protected habitat "
                    "keeps whole living populations, plants and animals "
                    "alike, where they already are."},
            {"text": "It needs land, and land is wanted for other uses "
                     "too.",
             "correct": True},
            {"text": "It requires every individual to be caught and "
                     "tagged first.",
             "correct": False,
             "why": "Nothing about protecting habitat requires catching "
                    "individuals. The population simply stays where it "
                    "already lives."},
            {"text": "It cannot be duplicated between countries the way a "
                     "sample can.",
             "correct": False,
             "why": "Duplication between countries is a seed-bank practice, "
                    "not something protected habitat is judged against. Its "
                    "limit is competing for the land itself."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e18",
        "band": "easier",
        "text": "Why is an animal's hereditary material kept by freezing "
                "reproductive cells, rather than in a seed bank?",
        "options": [
            {"text": "Because animal cells are too small to see without a "
                     "microscope.",
             "correct": False,
             "why": "Size has nothing to do with it — plant cells and seeds "
                    "are handled at similar scales. Animals simply have no "
                    "seed-shaped stage to store."},
            {"text": "Because animals do not produce a seed to dry and "
                     "freeze at all.",
             "correct": True},
            {"text": "Because freezing kills an animal's cells but not a "
                     "plant's.",
             "correct": False,
             "why": "Freezing is exactly how animal sperm, eggs and tissue "
                    "are kept alive in storage. The difference is what stage "
                    "each kind of organism naturally produces."},
            {"text": "Because animal variation is tracked using a "
                     "studbook, not by freezing anything.",
             "correct": False,
             "why": "A studbook is paper records for a living captive "
                    "population, not a way of storing hereditary material "
                    "itself."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e19",
        "band": "easier",
        "text": "A population has no genetic variation at all between its "
                "individuals. Why can it not evolve resistance to a brand "
                "new disease?",
        "options": [
            {"text": "Because evolution can only happen inside a gene "
                     "bank, never in a living field.",
             "correct": False,
             "why": "Evolution happens in living populations, not in "
                    "storage — a stored sample does not evolve at all. The "
                    "problem here is a lack of variation, not location."},
            {"text": "Because selection needs some individuals to differ "
                     "from others, and here none do.",
             "correct": True},
            {"text": "Because diseases only ever affect populations that "
                     "already carry some resistance.",
             "correct": False,
             "why": "Diseases can affect any population regardless of what "
                    "resistance it carries. The issue is whether any "
                    "individual happens to resist, not whether one must."},
            {"text": "Because a new disease changes an organism's own "
                     "genes the moment it infects it.",
             "correct": False,
             "why": "Infection does not rewrite an organism's genes. "
                    "Selection can only act on variation that was already "
                    "there before the disease arrived."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e20",
        "band": "easier",
        "text": "How do national seed banks reduce the risk of a single "
                "disaster destroying their whole collection?",
        "options": [
            {"text": "By keeping every sample permanently on display so "
                     "staff can watch it.",
             "correct": False,
             "why": "Samples are sealed away in cold, dark storage, not "
                    "displayed. Watching a sample does nothing to protect it "
                    "from a fire or flood."},
            {"text": "By planting the whole collection in one large field "
                     "every year.",
             "correct": False,
             "why": "Planting an entire collection in one field would put "
                    "it all at risk from a single event, which is the "
                    "opposite of what duplication is for."},
            {"text": "By duplicating samples and sending copies to stores "
                     "in other countries.",
             "correct": True},
            {"text": "By insuring the building against fire, flood and "
                     "storm damage.",
             "correct": False,
             "why": "Insurance could replace a building, not the living "
                    "seed inside it. What protects the seed itself is a "
                    "duplicate held somewhere else."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e21",
        "band": "easier",
        "text": "Biodiversity is usually described as having two parts. What "
                "are they?",
        "options": [
            {"text": "The number of different species, and the variation "
                     "between individuals within each species.",
             "correct": True},
            {"text": "The number of different species, and the total number "
                     "of individual organisms alive in the place.",
             "correct": False,
             "why": "A headcount is not the second part. A thousand identical "
                    "plants is a large number and almost no variation."},
            {"text": "The number of different habitats, and how many years "
                     "each of them has existed for.",
             "correct": False,
             "why": "Biodiversity is a measure of living things, not of "
                    "habitats or of how old they are."},
            {"text": "The number of different species, and how useful each of "
                     "those species happens to be to people.",
             "correct": False,
             "why": "Usefulness to people is not part of the measure. A "
                    "species nobody has a use for counts exactly the same."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e22",
        "band": "easier",
        "text": "Which fungal disease is currently moving through Cavendish "
                "banana plantations, echoing what happened to the Gros "
                "Michel?",
        "options": [
            {"text": "Potato blight, the same disease used on the bench.",
             "correct": False,
             "why": "Blight is the potato disease used on the bench. The "
                    "fungus threatening Cavendish bananas is a separate "
                    "disease."},
            {"text": "Panama disease, a fungus that attacks the roots.",
             "correct": True},
            {"text": "Foot rot, a fungus that rots the base of a plant's "
                     "stem.",
             "correct": False,
             "why": "Foot rot is a stem-base rot of other crops. The fungus "
                    "moving through Cavendish plantations is Panama disease."},
            {"text": "Rust, a fungus that attacks cereal crops.",
             "correct": False,
             "why": "Rust attacks cereal crops such as wheat, not bananas. "
                    "Panama disease is the one in the Cavendish plantations."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e23",
        "band": "easier",
        "text": "Which of these keeps variation as living, growing organisms "
                "rather than as stored material?",
        "options": [
            {"text": "A seed bank, holding dried seed cold.",
             "correct": False,
             "why": "A seed bank holds material that is dormant, not growing. "
                    "Nothing in it is alive and developing."},
            {"text": "A frozen store of sperm and eggs.",
             "correct": False,
             "why": "Frozen cells are stored material. They are not organisms "
                    "living and breeding anywhere."},
            {"text": "A botanic garden, growing plants on site.",
             "correct": True},
            {"text": "A studbook of which animals are related.",
             "correct": False,
             "why": "A studbook is a written record. It keeps no organism and "
                    "no material of its own at all."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e24",
        "band": "easier",
        "text": "Which conservation method does the lesson describe as "
                "expensive per individual and able to hold only small "
                "numbers?",
        "options": [
            {"text": "Seed banks, since dried samples take up so little "
                     "room.",
             "correct": False,
             "why": "Seed banks are cheap per sample, which is what lets "
                    "them hold enormous numbers in one building."},
            {"text": "Botanic gardens and zoos, keeping living organisms.",
             "correct": True},
            {"text": "Frozen sperm, eggs and tissue, held from thousands "
                     "of species.",
             "correct": False,
             "why": "Frozen stores hold material from thousands of species "
                    "at once. The costly, small-scale method is a different "
                    "one."},
            {"text": "Protected habitat, limited mainly by land, not "
                     "cost.",
             "correct": False,
             "why": "Protected habitat's limit is competing land use, not "
                    "cost per individual or a small holding capacity."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e25",
        "band": "easier",
        "text": "In the blight bench, how many potato plants make up the "
                "whole field, whichever of the four fields is chosen?",
        "options": [
            {"text": "One hundred, the size of one variety in the ten-"
                     "variety field.",
             "correct": False,
             "why": "A hundred is the size of one variety within the "
                    "ten-variety field, not the size of the whole field."},
            {"text": "Two hundred and fifty, the size of one variety in "
                     "the four-variety field.",
             "correct": False,
             "why": "Two hundred and fifty is the size of one variety "
                    "within the four-variety field, not the whole field."},
            {"text": "One thousand, always the same total whichever field "
                     "is chosen.",
             "correct": True},
            {"text": "Ten thousand, far larger than any single field on "
                     "the bench.",
             "correct": False,
             "why": "Ten thousand is far larger than any field the bench "
                    "describes. Every field on the bench totals a thousand "
                    "plants."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e26",
        "band": "easier",
        "text": "Which three things does the blight bench measure with its "
                "bars?",
        "options": [
            {"text": "Rainfall, soil quality, and the number of "
                     "pollinators visiting the field.",
             "correct": False,
             "why": "None of those appear on the bench. Its three bars are "
                    "survivors, variation and yield."},
            {"text": "The price of seed, the cost of land, and the "
                     "farmer's total profit.",
             "correct": False,
             "why": "The bench is about biology, not farm finances. Its "
                    "three bars track survival, variation and yield."},
            {"text": "Plants surviving the blight, genetic variation, and "
                     "yield per plant.",
             "correct": True},
            {"text": "The species count, the habitat area, and the years "
                     "since the region's last recorded blight.",
             "correct": False,
             "why": "Those figures do not appear on the bench. Its bars are "
                    "survivors, genetic variation, and yield per plant."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e27",
        "band": "easier",
        "text": "Before the blight is released on the bench, what does the "
                "first bar show?",
        "options": [
            {"text": "The percentage of plants expected to resist, worked "
                     "out in advance.",
             "correct": False,
             "why": "That percentage only appears once the blight has "
                    "passed through. Before release the bar simply shows "
                    "what was planted."},
            {"text": "The plants standing in the field, since none have "
                     "died yet.",
             "correct": True},
            {"text": "A blank bar, since nothing shows before a blight has "
                     "been run.",
             "correct": False,
             "why": "The bar is not blank — it reads a full field, since "
                    "every plant is still standing before any blight has "
                    "struck."},
            {"text": "The yield the field produced during the previous "
                     "year.",
             "correct": False,
             "why": "Yield is a separate bar of its own. The first bar, "
                    "before release, is simply the plants standing in the "
                    "field."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e28",
        "band": "easier",
        "text": "According to the lesson, what happens to a seed bank sample "
                "that is never tested or regrown on a cycle?",
        "options": [
            {"text": "It dies quietly, without anyone ever noticing.",
             "correct": True},
            {"text": "It becomes more resistant the longer it is left "
                     "untouched.",
             "correct": False,
             "why": "Being left alone does not add resistance to anything. An "
                    "untested seed is simply ageing towards its own death."},
            {"text": "It slowly turns into a different species over the "
                     "years.",
             "correct": False,
             "why": "Storage does not turn one species into another. A "
                    "neglected sample simply loses viability and dies."},
            {"text": "It stays exactly as viable as the day it was frozen, "
                     "forever.",
             "correct": False,
             "why": "Freezing slows ageing, it does not stop it — which is "
                    "why an untested sample can die without anyone knowing."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e29",
        "band": "easier",
        "text": "Cavendish bananas are grown from cuttings taken off existing "
                "plants rather than from seed. What does that mean for a "
                "plantation of them?",
        "options": [
            {"text": "Every plant is a different variety, since a cutting "
                     "makes new genes.",
             "correct": False,
             "why": "A cutting makes no new genes. It carries the same ones "
                    "as the plant it was cut from."},
            {"text": "Every plant is a clone, so they are all genetically "
                     "identical.",
             "correct": True},
            {"text": "The plants vary as much as seed-grown ones do.",
             "correct": False,
             "why": "Seed comes from two parents and varies. A cutting has "
                    "one parent and copies it exactly."},
            {"text": "The plants are all one age but carry different genes.",
             "correct": False,
             "why": "Age is not what a cutting fixes. What it fixes is the "
                    "genes, which are the same in every plant."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-e30",
        "band": "easier",
        "text": "A pupil says a landrace and a named potato variety must be "
                "different species, since one has far more variation than "
                "the other. What is wrong with that claim?",
        "options": [
            {"text": "Nothing — more variation between plants always means "
                     "a different species is involved.",
             "correct": False,
             "why": "Variation within a species can range hugely without "
                    "creating a new species. A landrace and a variety are "
                    "the same crop, differently bred."},
            {"text": "Both are the same crop species, just bred and grown "
                     "in different ways.",
             "correct": True},
            {"text": "The landrace is a wild ancestor of the domesticated "
                     "variety, not the same species.",
             "correct": False,
             "why": "A landrace is still a farmed crop, not a wild "
                    "ancestor. The two differ in how they are propagated, "
                    "not in species."},
            {"text": "A named variety is one species, and a landrace is "
                     "several species growing mixed together.",
             "correct": False,
             "why": "A landrace is one species with many individually "
                    "different plants, not several species sharing a "
                    "field."},
        ],
        "figure": None,
    },

    # ===================== STANDARD (s14-s30) =====================
    {
        "id": "b11-04-s14",
        "band": "standard",
        "text": "Some Andean farmers still grow a mixed potato landrace "
                "even though a single named variety would yield more in a "
                "good year. What is the reasonable case for their choice?",
        "options": [
            {"text": "There is no reasonable case; the higher-yielding "
                     "variety is always the better choice.",
             "correct": False,
             "why": "The bench itself shows the trade-off is real: the "
                    "landrace trades away yield precisely for a chance at "
                    "surviving a bad year."},
            {"text": "A bad year with a new disease is a bigger threat "
                     "than a smaller harvest most years.",
             "correct": True},
            {"text": "Landraces are simply cheaper to buy as seed than a "
                     "named commercial variety.",
             "correct": False,
             "why": "Cost of seed is not the reasoning given in the lesson. "
                    "The case for the landrace is about surviving a blight "
                    "year, not price."},
            {"text": "A named variety cannot be grown at high altitude, "
                     "unlike a mixed landrace.",
             "correct": False,
             "why": "Altitude tolerance is not the distinction drawn here. "
                    "The genuine trade-off is lower average yield against "
                    "better odds in a bad year."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s15",
        "band": "standard",
        "text": "A country can afford to protect either a small number of "
                "endangered animals in a breeding centre, or a very large "
                "number of plant species in a seed bank. Why does the seed "
                "bank reach so many more species for similar money?",
        "options": [
            {"text": "Plant species are naturally less at risk of "
                     "extinction than animal species are.",
             "correct": False,
             "why": "Risk of extinction is not what decides the cost "
                    "comparison here. The saving comes from how cheaply a "
                    "dried sample can be kept."},
            {"text": "A dried sample costs little to store and takes far "
                     "less space than a living animal.",
             "correct": True},
            {"text": "Seed banks receive far more public funding than any "
                     "breeding centre ever does.",
             "correct": False,
             "why": "Funding levels are not the reason given. The "
                    "difference is the cost of storing a dried seed against "
                    "the cost of keeping a living animal."},
            {"text": "A breeding centre can only ever manage to hold one "
                     "species at a time.",
             "correct": False,
             "why": "A breeding centre can hold several species. What "
                    "limits its scale is the cost and space each living "
                    "individual needs."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s16",
        "band": "standard",
        "text": "The four-variety field holds 1000 plants, and one of its "
                "four varieties resists the blight. How many plants would "
                "you expect to survive?",
        "options": [
            {"text": "One, since only one variety out of the four is "
                     "described as resistant.",
             "correct": False,
             "why": "One is the count of resistant varieties, not of "
                    "surviving plants. Each variety in this field is 250 "
                    "plants, not one."},
            {"text": "500, since half the varieties resisting should mean "
                     "half the plants survive.",
             "correct": False,
             "why": "One resistant variety out of four is a quarter, not a "
                    "half. Half would need two of the four to resist."},
            {"text": "250, since one resistant variety out of four is "
                     "roughly a quarter of the plants.",
             "correct": True},
            {"text": "750, since three failed varieties should be "
                     "subtracted from the total planted.",
             "correct": False,
             "why": "750 is roughly how many plants die, not how many "
                    "survive. The survivors are the quarter that came from "
                    "the resistant variety."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s17",
        "band": "standard",
        "text": "A conservation officer says frozen sperm and eggs in a "
                "gene bank are 'still evolving, just very slowly.' Is that "
                "an accurate description?",
        "options": [
            {"text": "Yes, since freezing simply slows evolution to a "
                     "rate that is too small to notice.",
             "correct": False,
             "why": "Freezing does not slow evolution, it halts it "
                    "entirely. There is no breeding happening inside a "
                    "frozen sample at all."},
            {"text": "No, since only a living, breeding population can "
                     "evolve at all, frozen or not.",
             "correct": True},
            {"text": "Yes, since slow chemical reactions inside a cell "
                     "still count as very slow evolving.",
             "correct": False,
             "why": "Slow chemistry inside a frozen cell is not evolution. "
                    "Evolution needs generations of breeding, which frozen "
                    "storage stops completely."},
            {"text": "It depends on the species, since some organisms "
                     "keep evolving even when frozen.",
             "correct": False,
             "why": "No organism keeps evolving while frozen — storage "
                    "stops the population from breeding at all, whatever "
                    "the species."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s18",
        "band": "standard",
        "text": "The ten-variety field's variation bar reads 90, ten times "
                "the clone field's bar of 9. What does that comparison show?",
        "options": [
            {"text": "The ten-variety field holds ten times the genetic "
                     "variation, on the bench's own scale.",
             "correct": True},
            {"text": "The ten-variety field will survive the blight ten times "
                     "better than the clone field.",
             "correct": False,
             "why": "Survival is read from a separate bar. The variation bar "
                    "reports genetic variety, not the outcome of the blight."},
            {"text": "Ten varieties always yield ten times as much crop as a "
                     "single variety would.",
             "correct": False,
             "why": "Yield is its own bar and is not tied to the variation "
                    "figure this way. The 90 against 9 is a comparison of "
                    "variation alone."},
            {"text": "The clone field secretly holds ten varieties, hidden "
                     "within its one labelled variety.",
             "correct": False,
             "why": "The clone field is genuinely one variety, a thousand "
                    "identical plants. Its low bar reflects that, not a "
                    "hidden variety count."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s19",
        "band": "standard",
        "text": "Two fields of 1000 plants each are hit by the same blight. "
                "One ends with 250 plants standing and the other with 400. "
                "Using the bench's own fields, which is which?",
        "options": [
            {"text": "250 belongs to the four-variety field, 400 to the "
                     "ten-variety field.",
             "correct": True},
            {"text": "250 belongs to the ten-variety field, 400 to the "
                     "four-variety field.",
             "correct": False,
             "why": "That swaps the two. The four-variety field survives at a "
                    "quarter, and the ten-variety field survives at two "
                    "fifths, not the reverse."},
            {"text": "Both counts belong to the landrace, measured across two "
                     "separate years.",
             "correct": False,
             "why": "The landrace survives at a much higher share than either "
                    "of these counts. Neither 250 nor 400 matches its result."},
            {"text": "Neither count matches any field, since all four fields "
                     "survive at the same rate.",
             "correct": False,
             "why": "The four fields survive at clearly different rates. 250 "
                    "and 400 match the four-variety and ten-variety fields "
                    "exactly."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s20",
        "band": "standard",
        "text": "The four-variety field ends a blight year with 250 plants "
                "standing out of the 1000 planted. How many plants died?",
        "options": [
            {"text": "250, matching the number that survived exactly.",
             "correct": False,
             "why": "250 is the number that survived, not the number that "
                    "died. Subtract that from the total planted to find the "
                    "loss."},
            {"text": "500, half of the plants originally planted.",
             "correct": False,
             "why": "500 would be half the field. A quarter surviving "
                    "means three quarters, not a half, were lost."},
            {"text": "750, three quarters of the plants originally "
                     "planted.",
             "correct": True},
            {"text": "850, nearly the whole of the original field.",
             "correct": False,
             "why": "850 overstates the loss. A thousand minus the 250 "
                    "survivors gives 750, not 850."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s21",
        "band": "standard",
        "text": "A country wants to expand protected habitat for an "
                "endangered orchid, but nearly all the surrounding land is "
                "already farmed. What does this illustrate about protected "
                "habitat as a method?",
        "options": [
            {"text": "That protected habitat only ever works for animal "
                     "species, never for plants.",
             "correct": False,
             "why": "Protected habitat is used for plants as much as "
                    "animals. The obstacle here is land use, not the kind "
                    "of species."},
            {"text": "Its main limitation in practice: it competes with "
                     "other uses for the same land.",
             "correct": True},
            {"text": "That a seed bank would face exactly the same "
                     "problem in this situation.",
             "correct": False,
             "why": "A seed bank needs a small building, not farmland, so "
                    "it would not face this particular obstacle at all."},
            {"text": "That the orchid should instead be classed as "
                     "extinct in the wild.",
             "correct": False,
             "why": "A shortage of land to expand a reserve does not make a "
                    "species extinct in the wild. It simply limits this one "
                    "method."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s22",
        "band": "standard",
        "text": "An island wants to preserve variation in both its native "
                "crop plants and its native lizards. Which pairing correctly "
                "matches material to method?",
        "options": [
            {"text": "A seed bank for the crop plants, frozen sperm, eggs or "
                     "tissue for the lizards.",
             "correct": True},
            {"text": "A seed bank for both groups, since seed banks work for "
                     "any organism at all.",
             "correct": False,
             "why": "Lizards produce no seed for a seed bank to dry and "
                    "freeze. Their hereditary material needs frozen sperm, "
                    "eggs or tissue instead."},
            {"text": "Frozen tissue for the crop plants, a seed bank for the "
                     "lizards.",
             "correct": False,
             "why": "That reverses the natural pairing. Crop plants produce "
                    "seed a seed bank can use; lizards do not."},
            {"text": "A studbook for the crop plants, protected habitat for "
                     "the lizards.",
             "correct": False,
             "why": "A studbook only records relatedness in a living captive "
                    "population; it stores no material of its own for either "
                    "group."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s23",
        "band": "standard",
        "text": "Seed banks and zoo breeding programmes each have a real "
                "weakness. Which pairing correctly matches the weakness to "
                "the method?",
        "options": [
            {"text": "Seed banks cannot be duplicated between countries; "
                     "zoos always cost less than a seed bank.",
             "correct": False,
             "why": "Seed banks are routinely duplicated between countries, "
                    "and zoos cost more per individual, not less, than a "
                    "seed bank."},
            {"text": "Seed banks: an untested sample can die quietly; "
                     "zoos: captivity costs variation over time.",
             "correct": True},
            {"text": "Seed banks cannot dry seed without killing it; zoos "
                     "always breed faster than wild animals.",
             "correct": False,
             "why": "Many seeds survive drying perfectly well, which is "
                    "what makes seed banks possible at all. Faster breeding "
                    "is not a stated zoo weakness either."},
            {"text": "Seed banks hold only a handful of samples; zoos "
                     "preserve a whole ecosystem alongside the species.",
             "correct": False,
             "why": "Seed banks hold enormous numbers of samples cheaply. "
                    "A zoo preserves neither the wild population nor its "
                    "ecosystem."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s24",
        "band": "standard",
        "text": "A rhino species survives only as embryos and tissue in a "
                "frozen gene bank, with no living animals anywhere in the "
                "wild. What is the correct term for its wild status?",
        "options": [
            {"text": "Extinct in the wild, since living material still "
                     "survives in storage alone.",
             "correct": True},
            {"text": "Fully extinct, since no rhino of that species is alive "
                     "in any form at all.",
             "correct": False,
             "why": "The frozen material is living hereditary material, not "
                    "nothing. That is exactly why the species is not counted "
                    "as fully extinct."},
            {"text": "Endangered, since the population could still recover on "
                     "its own given time.",
             "correct": False,
             "why": "With no wild population left, there is nothing left to "
                    "recover on its own. Endangered describes a species that "
                    "still has one."},
            {"text": "Reintroduced, since frozen material already counts as a "
                     "functioning wild population.",
             "correct": False,
             "why": "Frozen cells are not a functioning population; a "
                    "surrogate mother and much more would be needed before "
                    "reintroduction could even begin."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s25",
        "band": "standard",
        "text": "The ten-variety field's variation bar reads 90 out of a "
                "possible 100. As a fraction of the maximum reading, what "
                "share is that?",
        "options": [
            {"text": "One tenth of the maximum reading of the bar.",
             "correct": False,
             "why": "One tenth would be a reading of 10, not 90. Ninety out "
                    "of a hundred is nine tenths, not one."},
            {"text": "A quarter of the maximum reading of the bar.",
             "correct": False,
             "why": "A quarter of 100 would be 25. Ninety is far closer to "
                    "the top of the scale than to a quarter of it."},
            {"text": "The full maximum, since 90 is close enough to count "
                     "as 100.",
             "correct": False,
             "why": "Ninety is not one hundred; only the landrace actually "
                    "reaches the top of the scale. Ninety is nine tenths of "
                    "it."},
            {"text": "Nine tenths of the maximum reading of the bar.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s26",
        "band": "standard",
        "text": "Why does keeping seed samples in the Svalbard vault not "
                "remove the need to also protect a crop's growing population "
                "in the field?",
        "options": [
            {"text": "Because stored material still has to be regrown and "
                     "returned to real farms.",
             "correct": True},
            {"text": "Because Svalbard only accepts seed from crops already "
                     "extinct in the wild.",
             "correct": False,
             "why": "Svalbard holds duplicates from banks worldwide, extinct "
                    "or not. Its limit is that it stores material, not a "
                    "growing population."},
            {"text": "Because the vault has already run out of room to accept "
                     "any further new samples this year.",
             "correct": False,
             "why": "Running out of space is not the reason given. The limit "
                    "is that stored seed is not the same thing as a crop "
                    "actually being grown."},
            {"text": "Because seed kept at Svalbard slowly loses its genetic "
                     "identity over the years.",
             "correct": False,
             "why": "Frozen storage does not change a sample's genetic "
                    "identity at all. The limitation is that it is not a "
                    "living, growing population."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s27",
        "band": "standard",
        "text": "A student argues that the four-variety and ten-variety "
                "fields are 'basically identical' because both draw the "
                "same yield bar of 85. What has been left out?",
        "options": [
            {"text": "Nothing; an identical yield bar means the two "
                     "fields behave identically in every way.",
             "correct": False,
             "why": "The two fields behave very differently once a blight "
                    "arrives. A tied yield bar says nothing about how each "
                    "copes with disease."},
            {"text": "The number of plants in each field, which actually "
                     "differs quite a lot between the two fields.",
             "correct": False,
             "why": "Both fields plant the same total of 1000 plants. What "
                    "differs between them is survival in a blight year, not "
                    "field size."},
            {"text": "Which crop species each of the two fields is "
                     "actually growing.",
             "correct": False,
             "why": "Both fields grow the same crop species; only the "
                    "number of varieties within it differs. That is what "
                    "changes their blight survival."},
            {"text": "Their survival in a blight year, which differs "
                     "clearly: about 25% against 40%.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s28",
        "band": "standard",
        "text": "A breeder wants disease resistance a crop's modern "
                "varieties do not currently have. Why might crossing two of "
                "those modern varieties together fail to produce it?",
        "options": [
            {"text": "Crossing two varieties always produces plants "
                     "weaker than either parent variety.",
             "correct": False,
             "why": "Crossing does not automatically weaken offspring. The "
                    "real obstacle is that neither parent carries the "
                    "resistance gene to begin with."},
            {"text": "Modern varieties cannot be crossed with each other "
                     "at all, only with wild relatives.",
             "correct": False,
             "why": "Modern varieties of the same crop can usually be "
                    "crossed with one another. The problem is what genes "
                    "they carry, not whether crossing is possible."},
            {"text": "Crossing combines genes already in the parents; it "
                     "cannot create a gene from nothing.",
             "correct": True},
            {"text": "Crossing removes variation from a crop instead of "
                     "adding any to it.",
             "correct": False,
             "why": "Crossing can combine variation the parents already "
                    "have. It simply cannot invent a gene neither parent "
                    "possesses."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s29",
        "band": "standard",
        "text": "The landrace field's resistant count is 620 out of 1000 "
                "plants. How is that pair of numbers used to derive the 62% "
                "survival figure quoted for it?",
        "options": [
            {"text": "620 is simply written as a percentage sign without any "
                     "calculation at all.",
             "correct": False,
             "why": "The figure genuinely comes from a division. 620 out of "
                    "1000 works out to 62% rather than being read straight "
                    "off."},
            {"text": "1000 is subtracted from 620, leaving a remainder of 62 "
                     "as the answer.",
             "correct": False,
             "why": "Subtracting would give a negative number here, not 62%. "
                    "The figure comes from dividing 620 by 1000, not "
                    "subtracting."},
            {"text": "620 is divided by 1000 and turned into a percentage: "
                     "62%.",
             "correct": True},
            {"text": "620 is multiplied by 1000, and the result is rounded "
                     "down to 62%.",
             "correct": False,
             "why": "Multiplying 620 by 1000 gives a huge number, nothing "
                    "close to 62. Dividing, not multiplying, gives the quoted "
                    "figure."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-s30",
        "band": "standard",
        "text": "A studbook tracks which zoo animals are related to which. "
                "Why can it only slow the loss of variation in a small "
                "captive population, rather than reverse it?",
        "options": [
            {"text": "Because staff rarely follow the studbook's own "
                     "recommendations in practice.",
             "correct": False,
             "why": "The lesson gives no reason to doubt the studbook is "
                    "followed. Its limit is what it can achieve even when "
                    "followed exactly."},
            {"text": "Because studbooks are only kept for a few years "
                     "before being discarded.",
             "correct": False,
             "why": "How long records are kept is not the limitation "
                    "described. The limit is that pairing choices cannot "
                    "invent missing variation."},
            {"text": "It can only avoid breeding relatives; it cannot add "
                     "a gene the population never had.",
             "correct": True},
            {"text": "Because a studbook only works for species that "
                     "breed once a year.",
             "correct": False,
             "why": "Breeding frequency is not what restricts a studbook. "
                    "Its ceiling is that it can only manage the variation "
                    "already present, not create more."},
        ],
        "figure": None,
    },

    # ===================== HARDER (h14-h30) =====================
    {
        "id": "b11-04-h14",
        "band": "harder",
        "text": "The four-variety field survives at 25% and the landrace "
                "at 62%, both out of 1000 plants originally planted. What "
                "is the difference between the two fields' surviving plant "
                "counts?",
        "options": [
            {"text": "37, since the percentage gap can simply be read off "
                     "as a plant count.",
             "correct": False,
             "why": "A gap in percentage points is not a gap in plant "
                    "count. The actual plant totals must be found first, "
                    "then subtracted."},
            {"text": "620, since that is the landrace's whole surviving "
                     "count taken alone.",
             "correct": False,
             "why": "620 is the landrace's survivor count alone, not the "
                    "difference between the two fields. The four-variety "
                    "survivors must still be subtracted."},
            {"text": "370, since 620 landrace survivors minus 250 "
                     "four-variety survivors leaves that gap.",
             "correct": True},
            {"text": "870, since 620 landrace survivors are added to the "
                     "250 from the other field.",
             "correct": False,
             "why": "Adding the two counts together answers a different "
                    "question. The gap between them comes from subtracting, "
                    "not adding."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h15",
        "band": "harder",
        "text": "A fish farm raises one species from a single genetically "
                "uniform broodstock line. A new parasite appears that the "
                "broodstock line cannot resist. Using the bench's own "
                "reasoning, what should you predict for the farmed fish, and "
                "why are wild fish of the same species less at risk?",
        "options": [
            {"text": "The farmed stock could be wiped out entirely, while "
                     "some wild fish likely carry resistance.",
             "correct": True},
            {"text": "Both farmed and wild fish face identical risk, since a "
                     "parasite treats every fish the same.",
             "correct": False,
             "why": "A parasite does not need to recognise farmed fish. What "
                    "matters is whether any resistant genes exist among the "
                    "individuals it meets, and wild fish carry more of them."},
            {"text": "The farmed stock is automatically safer, since a farm "
                     "can medicate sick fish straight away.",
             "correct": False,
             "why": "The question asks what the bench's genetic reasoning "
                    "predicts, and that reasoning says a uniform line has no "
                    "resistant minority, medicine aside."},
            {"text": "Wild fish are at greater risk here, since nobody can "
                     "medicate a wild population at all.",
             "correct": False,
             "why": "Lack of treatment is not what the bench's reasoning "
                    "turns on. Wild fish are the less genetically uniform "
                    "group, which is the real protection."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h16",
        "band": "harder",
        "text": "A coral reef is being damaged by warming seas. A gene "
                "bank can freeze coral sperm and eggs, but cannot freeze "
                "the reef itself. What is lost that frozen coral material "
                "could never replace?",
        "options": [
            {"text": "Nothing important, since coral sperm and eggs are "
                     "the only part of a reef that biologically matters.",
             "correct": False,
             "why": "A reef is far more than its coral's reproductive "
                    "cells. The fish, algae and other species living on it "
                    "are lost the moment the reef itself is gone."},
            {"text": "The coral's own genetic variation, since freezing "
                     "damages DNA that growing coral would not.",
             "correct": False,
             "why": "Freezing preserves genetic material without damaging "
                    "it, which is the whole point of a gene bank. What it "
                    "cannot preserve is the living reef ecosystem."},
            {"text": "The ability to identify which particular coral "
                     "species has been frozen and stored.",
             "correct": False,
             "why": "Samples are catalogued carefully, so identification is "
                    "not the problem. The reef's living ecosystem is what a "
                    "freezer cannot hold."},
            {"text": "The living reef and the fish and algae that depend "
                     "on it, none of which sit in a freezer.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h17",
        "band": "harder",
        "text": "Reading the bench's variation bars — 9, 36, 90 and 100 as "
                "the number of varieties rises from 1 to 4 to 10 to 1000 — "
                "between which two neighbouring fields does the bar rise the "
                "most?",
        "options": [
            {"text": "Between the four-variety and ten-variety fields, a rise "
                     "of 54 points.",
             "correct": True},
            {"text": "Between the clone and four-variety fields, a rise of 27 "
                     "points.",
             "correct": False,
             "why": "27 is a genuine rise, but a smaller one. The larger jump "
                    "of 54 happens between the four-variety and ten-variety "
                    "fields."},
            {"text": "Between the ten-variety field and the landrace, a rise "
                     "of only 10 points.",
             "correct": False,
             "why": "That final step is the smallest rise of the three, only "
                    "10 points, once the bar is close to its ceiling of 100."},
            {"text": "The bar rises by the same amount at every one of the "
                     "three steps shown.",
             "correct": False,
             "why": "The three rises are 27, 54 and 10 — clearly uneven, not "
                    "steady steps of the same size."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h18",
        "band": "harder",
        "text": "After forty years of careful studbook breeding, a "
                "captive bird's genome shows far less variation than wild "
                "museum specimens collected a century earlier. A curator "
                "says 'the birds have adapted well to captivity, which is "
                "good news for the species.' What is wrong with that claim?",
        "options": [
            {"text": "Nothing; any adaptation a captive population makes "
                     "is automatically good for its long-term survival.",
             "correct": False,
             "why": "Adapting to a zoo enclosure is no help in the wild, "
                    "and it comes paired with a genuine loss of variation "
                    "the species will need later."},
            {"text": "It is wrong only because forty years is too short a "
                     "time for any real genetic change to occur.",
             "correct": False,
             "why": "Forty generations, spanning many birds bred and lost "
                    "from the line, is plenty of time for a small "
                    "population to lose real variation."},
            {"text": "It is wrong because captive birds cannot physically "
                     "breed with one another at all.",
             "correct": False,
             "why": "Captive breeding is exactly how the studbook line was "
                    "produced. The flaw is calling lost variation good "
                    "news, not whether breeding happened."},
            {"text": "Adapting to captivity is no help in the wild, and "
                     "the lost variation is a real loss, not good news.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h19",
        "band": "harder",
        "text": "A gene bank holds fifty seeds of a wild plant, all collected "
                "from one hillside on one day. The species grows right across "
                "five hundred miles of country. Why is that sample weaker "
                "insurance than its size suggests?",
        "options": [
            {"text": "Fifty seeds is too few to regrow any plant species at "
                     "all, whatever variation happens to be among them.",
             "correct": False,
             "why": "Fifty seeds is a workable start for many species. The "
                    "weakness is in where they came from, not in how many "
                    "there are."},
            {"text": "Seed collected on one day cannot be dried properly, "
                     "because drying has to be done in stages across a "
                     "season.",
             "correct": False,
             "why": "Seed is dried in the bank, not in the field, and a "
                    "single collecting day is perfectly normal practice."},
            {"text": "It carries only that one hillside's variation, and not "
                     "the variation held by populations across the rest of "
                     "the range.",
             "correct": True},
            {"text": "A wild plant's seed cannot be banked at all, so a "
                     "sample like this would never have been accepted in the "
                     "first place.",
             "correct": False,
             "why": "Wild species are exactly what most seed banks are "
                    "collecting. The sample is real; it is just narrow."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h20",
        "band": "harder",
        "text": "Blight strikes this region one year in five, and in that "
                "year the ten-variety field keeps 400 of its 1000 plants; in "
                "the four good years it keeps all 1000. Roughly how many "
                "plants stand at harvest time in total across the five years?",
        "options": [
            {"text": "4400, from four good years of 1000 plants plus one "
                     "blighted year of 400 plants.",
             "correct": True},
            {"text": "5000, since the field always holds all of its 1000 "
                     "plants whatever the year.",
             "correct": False,
             "why": "That ignores the blighted year entirely. One of the five "
                    "years only reaches 400 plants, not the full 1000."},
            {"text": "2000, treating a blight year as cancelling out two of "
                     "the good years.",
             "correct": False,
             "why": "There is no reason to cancel two good years against one "
                    "bad one. Each of the five years is simply added using "
                    "its own count."},
            {"text": "1400, counting only the blight year alongside one "
                     "single good year.",
             "correct": False,
             "why": "All five years contribute to the total, not just two of "
                    "them. Four good years of 1000 plus one bad year of 400 "
                    "gives 4400."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h21",
        "band": "harder",
        "text": "A city park holds the only population of a rare urban bee "
                "species and is due for redevelopment. A council officer "
                "proposes freezing bee sperm as insurance instead of "
                "stopping the development. Evaluate the proposal using "
                "ideas from this lesson.",
        "options": [
            {"text": "The proposal is a complete solution, since frozen "
                     "sperm preserves everything a live population does.",
             "correct": False,
             "why": "Frozen sperm preserves genetic material alone. It "
                    "does nothing for the standing population or the "
                    "pollination it does today."},
            {"text": "The proposal achieves nothing at all, since "
                     "freezing sperm preserves no genetic material.",
             "correct": False,
             "why": "Freezing genuinely does preserve genetic material — "
                    "that is the whole basis of a gene bank. What it fails "
                    "to preserve is the living population and its role."},
            {"text": "The redevelopment should go ahead unchanged, since "
                     "one park is too small to matter to any bee.",
             "correct": False,
             "why": "The lesson gives no basis for judging the park too "
                    "small to matter. The proposal's flaw is what freezing "
                    "sperm can and cannot preserve, not the park's size."},
            {"text": "Freezing sperm preserves some material, but not the "
                     "population or the pollination it now provides.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h22",
        "band": "harder",
        "text": "A grower plants 500 tomatoes. 98% are clones of one variety, "
                "and 2% grew from seed that had accidentally been crossed "
                "with a wild relative, so those few are genetically different "
                "from the rest. A disease arrives that the clonal variety "
                "cannot resist at all. Roughly how many plants might survive, "
                "and why not zero?",
        "options": [
            {"text": "About 10, since only the 2% that are not clones carry "
                     "any chance of a resistant gene.",
             "correct": True},
            {"text": "0, since a disease that the main variety cannot resist "
                     "always kills the whole field.",
             "correct": False,
             "why": "That would be true if every plant were identical, but 2% "
                    "of this field genuinely are not. Those few plants have a "
                    "chance the clones do not."},
            {"text": "500, since any variation at all guarantees the whole "
                     "field survives together.",
             "correct": False,
             "why": "A small amount of variation gives some plants a chance, "
                    "not the whole field. The 98% of true clones remain just "
                    "as vulnerable as before."},
            {"text": "250, since cross-pollination always affects exactly "
                     "half of whatever field it touches.",
             "correct": False,
             "why": "The cross-pollinated share here is stated as 2%, not "
                    "half. Half the field would be a completely different "
                    "figure."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h23",
        "band": "harder",
        "text": "A student claims 'ten different potato varieties gives "
                "basically the same protection as one mixed landrace, "
                "because both have more than one type of plant.' Use the "
                "bench's own numbers to show this is wrong.",
        "options": [
            {"text": "The claim is correct, since both fields score above "
                     "80 on the same variation bar.",
             "correct": False,
             "why": "Scoring above 80 does not make two readings the same. "
                    "90 against 100, and 40% against 62% survival, are "
                    "clearly different outcomes."},
            {"text": "The claim is correct, since the two fields draw an "
                     "identical yield bar of 85.",
             "correct": False,
             "why": "The two fields do NOT share a yield bar — the "
                    "landrace's is 55, well below the ten-variety field's "
                    "85, which is itself evidence against the claim."},
            {"text": "The claim cannot be tested, since the bench gives no "
                     "numbers for either field.",
             "correct": False,
             "why": "The bench gives clear numbers for every field — "
                    "variation bars, yield bars and survival percentages "
                    "for both the ten-variety field and the landrace."},
            {"text": "The landrace's variation bar and survival rate are "
                     "both clearly higher: 100 against 90, 62% against "
                     "40%.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h24",
        "band": "harder",
        "text": "A seed company markets a new potato variety as "
                "'blight-proof' after lab tests show it resists the current "
                "blight strain completely. Explain why planting this single "
                "variety across a whole country would still be a real risk.",
        "options": [
            {"text": "It would still be a monoculture, so a different disease "
                     "could still wipe the whole crop out.",
             "correct": True},
            {"text": "It would be no risk at all, since resisting the current "
                     "strain removes any danger of this kind.",
             "correct": False,
             "why": "Resisting one strain says nothing about a different "
                    "disease, or a mutated strain, arriving later. The "
                    "monoculture risk remains exactly as before."},
            {"text": "The only risk would be a lower yield than growing "
                     "several varieties together instead.",
             "correct": False,
             "why": "Yield is not the main danger here. A single resistant "
                    "variety planted everywhere still has zero resistance to "
                    "whatever it was not tested against."},
            {"text": "There would be a risk only if the variety were grown "
                     "from seed rather than from cuttings.",
             "correct": False,
             "why": "How the variety is propagated does not change the risk — "
                    "the danger is that every plant shares identical genes, "
                    "seed-grown clone or cutting alike."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h25",
        "band": "harder",
        "text": "A museum keeps pressed, dried specimens of a now-extinct "
                "plant species on public display. A visitor claims this "
                "means the species could be 'brought back' the same way a "
                "gene bank's frozen material could. What is the flaw in "
                "that claim?",
        "options": [
            {"text": "There is no flaw; any preserved plant material, "
                     "pressed or frozen, can be regrown given the right "
                     "conditions.",
             "correct": False,
             "why": "Pressing and drying for display kills the tissue "
                    "completely. A gene bank's material is kept viable on "
                    "purpose, which a museum specimen is not."},
            {"text": "The flaw is only that museums keep poor records of "
                     "where each specimen was originally collected.",
             "correct": False,
             "why": "Museum records are usually careful and detailed. The "
                    "real problem is that the specimen itself is dead, "
                    "record-keeping aside."},
            {"text": "The flaw is that museums are not legally permitted "
                     "to regrow extinct species from their collections.",
             "correct": False,
             "why": "The lesson gives no such legal rule, and it is not "
                    "the real obstacle. A dead, pressed specimen simply "
                    "cannot regrow, permission or not."},
            {"text": "A pressed specimen is dead tissue that cannot grow "
                     "into a plant, unlike a gene bank's living material.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h26",
        "band": "harder",
        "text": "A village keeps its heirloom bean seed alive by having "
                "residents regrow and reshare it every single year, rather "
                "than freezing a sample in a vault. Compare this to a frozen "
                "seed bank: what does the village's method preserve that a "
                "frozen vault does not, and what does it risk that the vault "
                "does not?",
        "options": [
            {"text": "It keeps the beans adapting each year, but depends on "
                     "people continuing the practice, unlike a vault.",
             "correct": True},
            {"text": "It preserves exactly the same things as a vault, since "
                     "both simply keep seed year to year.",
             "correct": False,
             "why": "A frozen sample stops changing the moment it is sealed, "
                    "while regrown seed keeps breeding and adapting — the two "
                    "methods are not equivalent."},
            {"text": "It risks nothing a vault does not, since both depend "
                     "equally on human effort to continue.",
             "correct": False,
             "why": "A sealed, catalogued vault sample does not depend on "
                    "anyone regrowing it every single year the way the "
                    "village's living seed does."},
            {"text": "It preserves nothing a vault does not, since variation "
                     "cannot change from one growing season to the next.",
             "correct": False,
             "why": "A breeding population can and does change across "
                    "generations, which is exactly why the village's living "
                    "seed keeps adapting while a frozen sample does not."},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h27",
        "band": "harder",
        "text": "A scientist proposes directly gene-editing a known "
                "resistance gene into a crop, instead of relying on stored "
                "variation from a gene bank. Applying this lesson's "
                "reasoning, what would the scientist still need before "
                "that was possible?",
        "options": [
            {"text": "Nothing further; gene editing can generate a "
                     "brand-new resistance gene whenever one is needed.",
             "correct": False,
             "why": "Editing copies or moves genes that already exist "
                    "somewhere; it does not invent a resistance gene no "
                    "organism has ever carried."},
            {"text": "Permission to plant the crop as a single variety "
                     "across the whole country at once.",
             "correct": False,
             "why": "How widely the crop is later planted has nothing to "
                    "do with finding the resistance gene the editing needs "
                    "in the first place."},
            {"text": "A frozen zoo holding tissue from a closely related "
                     "animal species instead.",
             "correct": False,
             "why": "A frozen zoo stores animal material and is unrelated "
                    "to editing a crop plant's genes. The gene itself must "
                    "already be known to exist somewhere in a plant."},
            {"text": "A resistance gene that already exists somewhere, "
                     "since editing can only copy a known gene.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h28",
        "band": "harder",
        "text": "For the ten-variety field, the variation bar reads 90 but "
                "only 40% of its plants survive the blight. What does that "
                "gap between the two figures show?",
        "options": [
            {"text": "One figure must be a mistake, since a bar of 90 "
                     "should always mean a survival rate of 90%.",
             "correct": False,
             "why": "Neither figure is a mistake. They are two different "
                    "measures — overall variation, and the fraction that "
                    "happens to resist one specific disease."},
            {"text": "The bench's variation bar must be measured in a "
                     "completely different unit from a percentage.",
             "correct": False,
             "why": "Both are shown on a 0–100 scale. The gap is about what "
                    "each number represents, not a unit mismatch."},
            {"text": "This field must contain some hidden clones among "
                     "its ten labelled varieties.",
             "correct": False,
             "why": "The field genuinely has ten distinct varieties. The "
                    "gap is explained by only some of them resisting this "
                    "blight, not by any hidden clones."},
            {"text": "The two figures genuinely measure different things: "
                     "overall variation against the fraction that resists "
                     "this blight.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h29",
        "band": "harder",
        "text": "The ten-variety field has 4 of its 10 varieties "
                "resistant, a 40% resistant fraction. Suppose a different "
                "field had 20 varieties with 8 of them resistant — the "
                "same 40% fraction. Would you expect the same survival "
                "percentage as the ten-variety field, even though the raw "
                "variety counts differ?",
        "options": [
            {"text": "No, since more varieties overall must always "
                     "produce a higher survival percentage.",
             "correct": False,
             "why": "It is the fraction resistant that decides survival, "
                    "not the raw variety count. Two fields sharing a "
                    "fraction share a survival rate."},
            {"text": "No, since doubling the number of varieties always "
                     "doubles the number of plants that die.",
             "correct": False,
             "why": "Doubling variety count while keeping the resistant "
                    "fraction fixed leaves the survival percentage "
                    "unchanged, not doubled losses."},
            {"text": "Yes, but only because 20 happens to be an even "
                     "number rather than an odd one.",
             "correct": False,
             "why": "Whether the variety count is even or odd makes no "
                    "difference. What matters is the resistant fraction "
                    "being the same in both cases."},
            {"text": "Yes, since survival depends on the fraction "
                     "resistant, not the total varieties planted.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-04-h30",
        "band": "harder",
        "text": "The variation bar equals varieties multiplied by 9 for "
                "the clone, four-variety and ten-variety fields (1×9, 4×9 "
                "and 10×9). The landrace has 1000 varieties, yet its bar "
                "reads only 100, not 9000. Why?",
        "options": [
            {"text": "The landrace must actually have far fewer varieties "
                     "than 1000, despite what the bench states.",
             "correct": False,
             "why": "The landrace genuinely has 1000 varieties, exactly as "
                    "stated. The reason its bar reads 100 is the scale's own "
                    "ceiling, not a hidden lower count."},
            {"text": "Multiplying by 9 only works for fields with fewer "
                     "than a hundred varieties in total.",
             "correct": False,
             "why": "There is no such cutoff rule described. The bar "
                    "simply cannot display a reading above its own maximum "
                    "of 100."},
            {"text": "The landrace's bar must be a rounding error and "
                     "should really read 9000 to match.",
             "correct": False,
             "why": "It is not an error — a bar capped at 100 is a design "
                    "choice, so 1000 varieties correctly reads as the "
                    "maximum rather than an impossible 9000."},
            {"text": "The bar has a maximum reading of 100, so the "
                     "pattern can only be read up to that ceiling.",
             "correct": True},
        ],
        "figure": None,
    },

]
