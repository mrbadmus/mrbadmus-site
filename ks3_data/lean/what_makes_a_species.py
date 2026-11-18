# -*- coding: utf-8 -*-
"""What makes a species, in the lean shape. Spec table: docs/lessons/wave2/ks3-what-makes-a-species.md.

The Rainford scheme (15b) asks for the process of speciation, which the old page never taught.
The speciation card and its figure are new teaching.
"""

LESSON = {
    "slug": "what-makes-a-species",
    "start": {
        "setup": "A mule's mother is a horse and its father is a donkey.",
        "question": "If you had to guess, are a horse and a donkey the same species?",
        "options": [
            ("No, two different species",
             "Yes, two species. Their mule is healthy, but it almost never has young of its own."),
            ("Yes, the same species",
             "They are two species. Their mule is healthy, but it almost never has young of its own."),
        ],
        "answer": 0,
    },
    "words": ["species", "fertile", "hybrid", "speciation"],
    "word_defs": {
        "species": "A group of organisms that can breed together to produce fertile offspring.",
        "fertile": "Able to reproduce and have offspring of its own.",
        "hybrid": "The offspring of two different species, such as a mule.",
        "speciation": "The process by which new species form.",
    },
    "knowledge": [
        {"kind": "card", "title": "What a species is",
         "body": ["A species is a group of organisms that can breed together.",
                  "Their offspring must be fertile. That means able to have young of their own.",
                  "Both parts matter: they can breed, and their offspring are fertile."]},
        {"kind": "card", "title": "The mule",
         "body": ["A horse and a donkey can mate. Their offspring is a mule.",
                  "A mule is a hybrid: the offspring of two different species.",
                  "A horse has 64 chromosomes. A donkey has 62.",
                  "A mule gets 32 from its horse parent and 31 from its donkey parent. That makes 63.",
                  "An odd number of chromosomes cannot all sort into matching pairs to make gametes.",
                  "So a mule almost never has young. Horses and donkeys are two species."]},
        {"kind": "reveal", "title": "Same species or not",
         "cols": ["Same species", "Why"],
         "rows": [
             ("Great dane and chihuahua", "Yes", "Their puppies can grow up and have puppies."),
             ("Horse and donkey", "No", "Their offspring, the mule, is almost always infertile."),
             ("Lion and tiger", "No", "Male ligers are infertile. Lions and tigers do not breed in the wild."),
             ("Two kinds of pipistrelle bat", "No", "They look the same, but they do not breed together."),
         ]},
        {"kind": "card", "title": "Looks can mislead",
         "body": ["Members of one species can look very different. Dog breeds are an example.",
                  "Two species can look almost the same, like the two pipistrelle bats.",
                  "So appearance is only a clue. The breeding test decides."]},
        {"kind": "card", "title": "Where the test runs out",
         "body": ["Bacteria do not breed with each other. Each one splits in two.",
                  "Fossils cannot be bred either.",
                  "For these, scientists compare their DNA or their features instead.",
                  "DNA is also compared when two groups cannot be brought together."]},
        {"kind": "card", "title": "How a new species forms",
         "body": [{"figure": "b10-speciation"},
                  {"points": ["One population of a species lives in one area.",
                              "A barrier, such as a sea or mountains, splits it into two groups.",
                              "The two groups cannot meet, so they cannot breed together.",
                              "Conditions on each side are different, such as food, climate or predators.",
                              "On each side, individuals best suited to the conditions survive and breed more.",
                              "Over many generations, changes build up. The two groups become more and more different.",
                              "In the end, they can no longer breed to make fertile offspring.",
                              "They are now two separate species. This is speciation."]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Organisms that look alike are the same species.",
              "Two species can look the same. The breeding test decides.", "GENE-09"),
             ("If two animals can have a baby together, they are the same species.",
              "The baby must also be fertile. A mule is not.", "GENE-10"),
             ("Two separated groups become new species straight away.",
              "It takes many generations for enough changes to build up."),
             ("Animals change on purpose to suit their surroundings.",
              "Individuals that happen to suit them survive and breed more."),
         ]}]},
    ],
    "key_fact": "A species is a group of organisms that can breed together to produce fertile offspring. "
                "Speciation happens when two separated groups change so much that they can no longer interbreed.",
    "deeper": [
        {"kind": "card", "title": "Partway there",
         "body": ["Groups that split only recently may be partway to becoming two species.",
                  "They may still breed together sometimes.",
                  "For them, there may be no clear answer yet."]},
        {"kind": "card", "title": "Darwin's finches",
         "body": ["Finches reached the Galápagos Islands long ago.",
                  "Different islands had different foods.",
                  "Birds with beaks suited to the local food survived and bred more.",
                  "Over many generations, each island's finches became different.",
                  "Today there are more than a dozen species of finch there."]},
    ],
    "try": None,
    "tutor_body": "Want to test the species rule on a pair of animals or plants?",
    "ks4_becomes": "Evolution by natural selection, speciation, and classifying living things.",
    "figures": [
        {"id": "b10-speciation", "kind": "diagram", "status": "drawn", "art": "b10-speciation",
         "title": "How one species becomes two",
         "desc": "Four panels, one under another. Panel 1, one population: beetles of one shade spread "
                 "across one area. Panel 2, a barrier splits it: a ridge of mountains runs down the middle, "
                 "with beetles on both sides, all still the same shade. Panel 3, each side changes over time: the beetles on the cold, dry side are now dark and those on the warm, wet side "
                 "are pale. Panel 4, the barrier is gone and the two kinds meet: a dark beetle and a pale "
                 "beetle face each other with a cross between them, labelled no fertile offspring.",
         "caption": "Split, change on each side, and the two groups can no longer interbreed.",
         "data": {"stages": ["One population", "A barrier splits it",
                             "Each side changes over time", "They meet: two species"],
                  "barrier": "mountains", "sides": ["cold, dry side", "warm, wet side"]}},
    ],
    "figure_caption": {"b10-speciation": None},
    "ladder_stem": {
        "explain": "Horses and donkeys readily produce mules, yet they are two species. "
                   "Explain why. Use the chromosome numbers in your answer.",
        "produce": "A biologist finds two groups of beetles on either side of a mountain range. They look "
                   "identical. Describe how she could test whether they are one species. Say what she could "
                   "do if they cannot be brought together. Explain why the answer might be \"not yet decided\".",
    },
    "ladder_ticks": [
        ["Concludes that horses and donkeys are therefore two species, and notes that producing offspring alone is not enough.",
         "Concludes they are two species, as offspring alone are not enough."],
        ["Proposes bringing them together and observing whether they mate and whether the offspring can then reproduce.",
         "Proposes bringing them together to see if they mate and the young are fertile."],
        ["Notes that looking identical proves nothing, referring to cryptic species or giving an equivalent reason.",
         "Says looking identical proves nothing, as two species can look the same."],
        ["Explains that populations separated recently may be partway to becoming separate species, so a clear answer may not exist yet.",
         "Says recently split groups may be partway to becoming two species."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Having offspring is only half the test. The offspring must be fertile.",
            2: "Looks do not decide a species. A mule looks like both its parents.",
            3: "Healthy but infertile offspring is the sign of two species.",
        },
        "apply": {
            0: "A name is something people chose. The test is fertile offspring.",
            2: "Dogs do not have identical DNA. That is why breeds look so different.",
            3: "Food has nothing to do with the species test.",
        },
    },
}
