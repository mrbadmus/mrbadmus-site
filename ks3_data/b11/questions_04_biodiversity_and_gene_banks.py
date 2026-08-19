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
            {"text": "Protected habitat, because the populations are left "
                     "where they are, still breeding and still evolving.",
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
                     "regrown, they die quietly in the dark.",
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
            {"text": "Every tree can be infected, because there is no "
                     "resistant minority for selection to work with.",
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
]
