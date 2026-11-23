# -*- coding: utf-8 -*-
"""Biodiversity and gene banks, in the lean shape.
Spec table: docs/lessons/wave2/ks3-biodiversity-and-gene-banks.md."""

LESSON = {
    "slug": "biodiversity-and-gene-banks",
    "start": {
        "setup": "A clone is an exact genetic copy. Cavendish bananas are grown from shoots of a "
                 "parent plant, so every plant is identical.",
        "question": "If you had to guess, why could one disease wipe out a whole field of these bananas?",
        "options": [
            ("Each clone is a weak plant",
             "They all share one weak spot. Each plant is healthy, but every plant is the same."),
            ("They all share one weak spot",
             "Yes. Every plant is the same, so a disease that kills one can kill them all."),
        ],
        "answer": 1,
    },
    "words": ["biodiversity", "clone", "gene bank", "conservation"],
    "word_defs": {
        "biodiversity": "The variety of living things: different species, and the variation within each species.",
        "clone": "An organism that is genetically identical to the one it came from.",
        "gene bank": "A store of seeds, sperm, eggs or tissue, kept to save hereditary material.",
        "conservation": "Protecting species and their habitats so they are not lost.",
    },
    "knowledge": [
        {"kind": "card", "title": "What biodiversity means",
         "body": ["Biodiversity is the variety of living things.",
                  "It includes how many different species there are in an area.",
                  "It also includes the variation within each species."]},
        {"kind": "card", "title": "Why biodiversity matters",
         "body": ["Species depend on each other in food webs. Lose one, and others are affected.",
                  "Variation within a species helps it survive a change, such as a new disease.",
                  "People use many species for food, medicines and materials.",
                  "Each species lost takes genes with it that may have been useful."]},
        {"kind": "reveal", "title": "A field of clones and a mixed field",
         "cols": ["One variety, all clones", "Many varieties"],
         "rows": [
             ("Genetic variation", "None. Every plant is the same.", "Lots. The plants differ."),
             ("Crop in a good year", "The biggest crop.", "A slightly smaller crop."),
             ("When a new disease arrives", "If one plant can be killed, all of them can.",
              "Some plants may resist it and survive."),
             ("Next year", "Nothing may be left to plant.", "The survivors can be planted again."),
         ]},
        {"kind": "card", "title": "When one variety fails",
         "body": ["In the 1840s, most potatoes in Ireland were one variety.",
                  "A disease called potato blight destroyed the crop, year after year.",
                  "About a million people died in the famine that followed.",
                  "In the 1950s, a fungus wiped out the Gros Michel banana on farms.",
                  "The same kind of fungus now attacks the Cavendish banana."]},
        {"kind": "card", "title": "Ways to keep biodiversity",
         "body": [{"points": ["Protect habitats in nature reserves and national parks.",
                              "Breed endangered animals in zoos, and plants in botanic gardens.",
                              "Make laws against hunting and trading endangered species.",
                              "Plant hedgerows and leave field edges wild for other species.",
                              "Store hereditary material in gene banks."]}]},
        {"kind": "card", "title": "Gene banks",
         "body": ["A gene bank stores hereditary material, so variation is not lost.",
                  "Seed banks store dried seeds in freezers at about −18 °C.",
                  "Sperm, eggs and tissue from animals can be frozen too.",
                  "If a wild population is lost, stored material can grow new plants or animals.",
                  "The Svalbard Global Seed Vault holds over a million seed samples."]},
        {"kind": "reveal", "title": "Ways to keep variation",
         "cols": ["What it keeps", "Its limit"],
         "rows": [
             ("Protected habitat", "Living populations that keep breeding and changing.",
              "It needs land, which people want for other uses."),
             ("Seed bank", "Seeds of thousands of plant species, stored cheaply.",
              "Seeds must be grown and replaced every so often, or they die."),
             ("Frozen sperm, eggs and tissue", "Hereditary material from animals.",
              "Bringing an animal back is hard. It needs a living mother of the same or a close species."),
             ("Zoos and botanic gardens", "Living animals and plants, bred with care.",
              "They hold small numbers, so some variation is slowly lost."),
         ]},
        {"kind": "card", "title": "What a gene bank cannot store",
         "body": ["A seed can be stored. Its pollinators, soil fungi and habitat cannot.",
                  "Stored seeds stop changing, while the world outside keeps changing.",
                  "So a gene bank is a backup. Protecting wild habitats still matters."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Biodiversity just means how many species there are.",
              "It also includes the variation within each species.", "EVOL-07"),
             ("We have gene banks, so losing species in the wild does not matter.",
              "A gene bank is a backup. It cannot store a species' habitat or pollinators.",
              "EVOL-08"),
             ("A field of a thousand plants has high biodiversity.",
              "Not if they are clones. Identical plants have no variation."),
             ("Gene banks store whole animals.",
              "They store seeds, sperm, eggs and tissue."),
         ]}]},
    ],
    "key_fact": "Biodiversity is the variety of living things. It includes the number of species and the "
                "variation within each one. Variation helps a species survive change. Gene banks store "
                "seeds, sperm, eggs and tissue, so hereditary material is not lost.",
    "deeper": [
        {"kind": "card", "title": "A seed bank put to use",
         "body": ["A seed bank in Aleppo, Syria, held old varieties of wheat and barley.",
                  "In the civil war, scientists could no longer reach it.",
                  "They took copies of its seeds from the Svalbard vault.",
                  "They grew them in Lebanon and Morocco, then stored fresh seed in Svalbard again."]},
        {"kind": "card", "title": "Medicines from living things",
         "body": ["Aspirin was developed from a substance in willow bark.",
                  "Penicillin came from a mould.",
                  "A cancer drug, vincristine, comes from the Madagascar periwinkle plant.",
                  "A species that dies out may take a future medicine with it."]},
    ],
    "try": None,
    "tutor_body": "Want to argue the case for or against a conservation decision?",
    "ks4_becomes": "Maintaining biodiversity, and the benefits and problems of conservation.",
    "ladder_stem": {
        "explain": "A field of identical crop plants can be wiped out by one disease. A field of many varieties "
                   "usually is not. Explain why. Link your answer to natural selection.",
        "produce": "A government must split its conservation money between protecting habitats and a seed bank. "
                   "Give the argument for each. Say which you would fund more, and why. Name one thing your "
                   "choice would fail to protect.",
    },
    "ladder_ticks": [
        ["Says genetically identical plants all have the same susceptibility, so if one can be infected they "
         "all can.",
         "Says identical plants are all the same, so if one catches it, all can."],
        ["Says a mixed field contains plants with different versions of genes, some of which may resist the "
         "disease.",
         "Says a mixed field has plants with different genes, and some may resist the disease."],
        ["Links this to natural selection: selection can only act on variation that already exists in the "
         "population.",
         "Links to natural selection: it can only act on variation that already exists."],
        ["Concludes that a clone population has no variation for selection to act on, so there is no "
         "possibility of a resistant survivor.",
         "Concludes clones have no variation to select from, so no resistant plant survives."],
        ["States what habitat protection achieves: living populations that keep varying and evolving, with "
         "their ecosystem intact.",
         "Says protecting habitat keeps living populations evolving, with their food web intact."],
        ["States what a seed bank achieves: many species stored cheaply and safely, including some already "
         "lost from the wild.",
         "Says a seed bank stores many species cheaply, even some lost from the wild."],
        ["Identifies a real limitation of the chosen option — land use conflict, or the fact that stored "
         "material stops evolving.",
         "Names a limit of the choice, such as land needed or stored seeds not evolving."],
        ["Recognises the two are complementary rather than alternatives, or explains why a split would still "
         "involve a trade-off.",
         "Says the two work together, or explains why any split is a trade-off."],
    ],
    "figures": [],
    "ladder_feedback": {
        "recall": {
            1: "Fifty species is a lot of variety. Look for the least variation.",
            2: "Ten varieties have far more variation than one clone variety.",
            3: "Each grass plant differs a little. Clones have no variation at all.",
        },
        "apply": {
            0: "Many seeds survive drying and freezing. That is why seed banks work.",
            1: "Seed banks are cheap for what they protect. Cost is not the main objection.",
            2: "Stored seeds can be grown. The problem is the habitat they return to.",
        },
    },
}
