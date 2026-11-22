# -*- coding: utf-8 -*-
"""Natural selection, in the lean shape. Spec table: docs/lessons/wave2/ks3-natural-selection.md.

Rainford 16b (selective breeding) has no page of its own. It is taught here, after natural
selection, with a reveal table comparing the two.
"""

LESSON = {
    "slug": "natural-selection",
    "start": {
        "setup": "A giraffe's neck is about two metres long. Its ancestors had much shorter necks.",
        "question": "If you had to guess, how did giraffes end up with such long necks?",
        "options": [
            ("Long-necked giraffes had more babies",
             "Yes. Giraffes with longer necks reached more food, so more survived to breed."),
            ("Stretching, then passing it on",
             "Long-necked giraffes had more babies. Stretching does not change the genes a giraffe passes on."),
        ],
        "answer": 0,
    },
    "words": ["evolution", "natural selection", "inherited", "selective breeding"],
    "word_defs": {
        "evolution": "The change in a species over many generations.",
        "natural selection": "The best adapted individuals survive and breed more. They pass on their genes.",
        "inherited": "Passed from parents to their young in their genes.",
        "selective breeding": "People choose parents with a feature they want, and breed them.",
    },
    "knowledge": [
        {"kind": "card", "title": "Darwin and evolution",
         "body": ["Evolution is the change in a species over many generations.",
                  "Charles Darwin came up with the theory of evolution by natural selection.",
                  "He published it in 1859, in his book <em>On the Origin of Species</em>.",
                  "Alfred Russel Wallace came up with the same idea at the same time."]},
        {"kind": "card", "title": "What Darwin saw",
         "body": ["Darwin sailed round the world on a ship called HMS Beagle.",
                  "On the Galápagos Islands, he saw mockingbirds that differed from island to island.",
                  "Later, scientists found the finches' beaks suited the food on each island.",
                  "He also bred pigeons, and saw how much breeding could change them."]},
        {"kind": "card", "title": "Natural selection in five steps",
         "body": [{"figure": "b11-selection-steps"},
                  # a bulleted list (lean_blocks draws only <ul>), so no typed numbers: the
                  # figure above numbers the steps, and each line starts with its step's name
                  {"points": ["Variation: individuals in a species are different from each other.",
                              "Competition: more are born than can survive. They compete for food, "
                              "space and mates.",
                              "The best adapted survive: individuals with useful features are more "
                              "likely to survive.",
                              "They reproduce: the survivors breed and pass on their genes.",
                              "Over many generations: the useful feature becomes common. The species "
                              "has changed."]}]},
        {"kind": "card", "title": "The peppered moth",
         "body": ["Peppered moths rest on tree bark in the day. Birds hunt them by sight.",
                  "Most were pale. A few dark ones were born too.",
                  {"figure": "b11-moth-barks"},
                  "In the 1800s, soot from factories blackened the bark in industrial areas.",
                  "Birds saw the pale moths more easily, so they ate more of them.",
                  "More dark moths survived and bred. Their young inherited dark wings.",
                  "Over many generations, most moths in those areas became dark.",
                  "When the air got cleaner, pale moths became common again."]},
        {"kind": "card", "title": "Why stretching is not passed on",
         "body": ["Changes during an animal's life do not change its genes.",
                  "So they are not inherited.",
                  "A giraffe that stretches its neck does not have longer-necked young.",
                  "Jean-Baptiste Lamarck suggested this stretching idea in 1809. Evidence showed it was wrong.",
                  "Long necks spread because giraffes born with longer necks survived and bred more."]},
        {"kind": "card", "title": "Selective breeding",
         "body": ["In selective breeding, people choose which animals or plants breed.",
                  "They choose parents with a feature they want. Examples:",
                  {"points": ["cows that give a lot of milk (a high milk yield)",
                              "chickens that lay many eggs",
                              "wheat with large grains, and crops that resist disease",
                              "dogs with a gentle nature",
                              "large, tasty fruit and vegetables"]}]},
        {"kind": "card", "title": "How selective breeding works",
         "body": [{"points": ["Choose parents that show the wanted feature most.",
                              "Breed them together.",
                              "From their young, choose those that show the feature most.",
                              "Breed these together.",
                              "Repeat for many generations."]},
                  "Over time, more and more of the young show the feature."]},
        {"kind": "card", "title": "Effects of selective breeding",
         "body": ["It gives us more milk, more food and crops that resist disease.",
                  "But the animals in a breed are closely related, so they have little variation.",
                  "A new disease could kill many of them, as none may resist it.",
                  "Some breeds have health problems. Some flat-faced dogs struggle to breathe."]},
        {"kind": "reveal", "title": "Natural selection and selective breeding",
         "cols": ["Natural selection", "Selective breeding"],
         "rows": [
             ("What does the selecting", "The environment: predators, disease, food supply and climate.",
              "People choose which individuals breed."),
             ("Which features win", "Any feature that helps survival and breeding.",
              "Features people want, even ones that do not help survival."),
             ("How long it takes", "Many generations. Moths changed in about 50 years. Bacteria change in days.",
              "Often fewer generations, because people choose every parent."),
             ("Examples", "Peppered moths, giraffes' necks, bacteria that resist antibiotics.",
              "Cows with a high milk yield, wheat with large grains."),
             ("Effect on variation", "Selection narrows the useful feature. A large wild population stays varied overall.",
              "Variation falls, as only a few chosen parents breed."),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Animals change themselves to suit their home, and pass the change on.",
              "Changes during an animal's life are not inherited. Only genes are passed on.",
              "EVOL-03"),
             ("The population needed to change, so it did.",
              "Nothing plans the change. The useful variation was already there.", "EVOL-04"),
             ("The soot turned the moths dark.",
              "Each dark moth was born dark. Soot changed which moths birds could see."),
             ("One animal can evolve during its life.",
              "Species evolve over many generations. One animal keeps the genes it was born with."),
             ("Selective breeding happens in the wild.",
              "People do selective breeding. Natural selection happens in the wild."),
         ]}]},
    ],
    "key_fact": "Individuals vary, and the best adapted survive and reproduce. They pass on their genes, "
                "so over many generations the species changes. This is natural selection, explained by "
                "Charles Darwin.",
    "deeper": [
        {"kind": "card", "title": "Bacteria that resist antibiotics",
         "body": ["A few bacteria may happen to resist an antibiotic.",
                  "The antibiotic kills the rest. The resistant ones survive and divide.",
                  "Bacteria can divide every 20 minutes, so resistance spreads in days.",
                  "Insects become resistant to pesticides in the same way."]},
        {"kind": "card", "title": "Testing the moth idea",
         "body": ["In the 1950s, Bernard Kettlewell released pale and dark moths in two woods.",
                  "In each wood, more of the better hidden moths were caught again later.",
                  "Other scientists said his method was unrealistic.",
                  "Michael Majerus repeated it with a better method. He got the same result."]},
    ],
    "try": None,
    "tutor_body": "Want to check your explanation of natural selection?",
    "ks4_becomes": "The evidence for evolution, and selective breeding and genetic engineering.",
    "figure_caption": {"b11-selection-steps": "Natural selection in peppered moths on sooty bark.",
                       "b11-moth-barks": None},
    "ladder_stem": {
        "explain": "Soot blackened the tree bark. Mainly pale moths became mainly dark moths. Explain "
                   "how, using all five steps. Do not say that any moth changed colour.",
        "produce": "A farmer sprays a pesticide that kills 99% of the insect pests. Within three years it "
                   "barely works. Explain what has happened. Explain why spraying more makes it worse. "
                   "Say what this has in common with the peppered moths.",
    },
    "ladder_ticks": [
        ["Says more dark moths therefore survived to reproduce.",
         "Says more are born than survive, and more dark moths survived to breed."],
        ["Says birds could see the pale moths more easily against the dark bark, so more of them were eaten.",
         "Says birds saw pale moths more easily on dark bark, so ate more of them."],
        ["Says the proportion of dark moths increased over many generations — and does not say that any "
         "moth changed colour.",
         "Says dark moths became more common over many generations. No moth changed colour."],
        ["Says a few insects in the original population happened to be resistant, before the pesticide "
         "was used.",
         "Says a few insects were already resistant before the pesticide was used."],
        ["Says those survivors bred and passed resistance on, so the proportion of resistant insects rose "
         "each generation.",
         "Says survivors bred and passed on resistance, so resistant insects became more common."],
        ["Says spraying more applies the same selection pressure harder and speeds the process up.",
         "Says spraying more kills more of the others, so resistance spreads faster."],
        ["Identifies the shared mechanism: existing variation plus a change in what survives, with no "
         "individual insect becoming resistant during its life.",
         "Says both start with variation already there. No insect became resistant during its life."],
    ],
    "figures": [
        {"id": "b11-selection-steps", "kind": "diagram", "status": "drawn", "art": "b11-selection-steps",
         "title": "Natural selection in five steps",
         "desc": "Five numbered steps, one under another, joined by arrows pointing down. Each step has a "
                 "strip of sooty bark with moths on it. Step 1, Variation: seven moths, five pale and two "
                 "dark. Step 2, Competition: nine moths. Step 3, The best adapted survive: five pale moths "
                 "and one dark moth are crossed out as eaten, leaving one pale and two dark. Step 4, They "
                 "reproduce: the one pale and two dark survivors, an arrow, then five young, one pale and "
                 "four dark. Step 5, Over many generations: nine moths, eight dark and one pale. A key says "
                 "a red cross means eaten by a bird.",
         "caption": "Natural selection in peppered moths on sooty bark.",
         "data": {"steps": [
             {"title": "Variation", "note": "Some moths are pale. Some are dark.", "row": "PPDPPDP"},
             {"title": "Competition", "note": "More are born than can survive.", "row": "PPDPPPDPD"},
             {"title": "The best adapted survive", "note": "Birds spot and eat more pale moths.",
              "row": "ppDpPpdpD"},
             {"title": "They reproduce", "note": "Their young inherit their genes.", "row": "PDD>PDDDD"},
             {"title": "Over many generations", "note": "Dark moths are now the most common.",
              "row": "DDDDPDDDD"},
         ], "legend": "= eaten by a bird"}},
        {"id": "b11-moth-barks", "kind": "diagram", "status": "drawn", "art": "b11-moth-barks",
         "title": "The same two moths on two kinds of bark",
         "desc": "Two panels, one above the other. Top: clean pale bark with patches of lichen. The pale "
                 "moth on it is labelled hard to see and the dark moth easy to see. Bottom: bark "
                 "blackened by soot, with dark streaks. The same pale moth is labelled easy to see and the "
                 "dark moth hard to see. A line underneath says the moths did not change, the bark did.",
         "caption": "The same two moths on two kinds of bark.",
         "data": {"panels": [
             {"bark": "lichen", "label": "Clean bark with lichen",
              "moths": [{"tone": "pale", "label": "Pale moth", "note": "hard to see"},
                        {"tone": "dark", "label": "Dark moth", "note": "easy to see"}]},
             {"bark": "soot", "label": "Bark blackened by soot",
              "moths": [{"tone": "pale", "label": "Pale moth", "note": "easy to see"},
                        {"tone": "dark", "label": "Dark moth", "note": "hard to see"}]},
         ], "key": "The moths did not change. The bark did."}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "No moth changed colour. Each moth keeps the colour it was born with.",
            2: "Soot does not change the colour a moth is born with. Colour is inherited.",
            3: "Learning is not inherited. Fewer pale moths survived to breed.",
        },
        "apply": {
            0: "Giraffes can stretch. Stretching does not change the genes they pass on.",
            1: "Giraffes do feed from tall trees. The idea about inheritance is what is wrong.",
            2: "Giraffe necks did get longer. The question is how that happened.",
        },
    },
}
