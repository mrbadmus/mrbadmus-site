# -*- coding: utf-8 -*-
"""When the environment changes: extinction, in the lean shape.
Spec table: docs/lessons/wave2/ks3-when-the-environment-changes-extinction.md."""

LESSON = {
    "slug": "when-the-environment-changes-extinction",
    "start": {
        "setup": "Half of a wood is cut down. Brown rats and hazel dormice both live there.",
        "question": "If you had to guess, what helps an animal most when its home changes?",
        "options": [
            ("Breeding fast, eating anything",
             "Yes. Fast breeders soon replace the animals they lose. Unfussy eaters still find food."),
            ("Being big, strong and fierce",
             "Breeding fast and eating anything helps most. Strength does not bring back lost food or "
             "habitat."),
        ],
        "answer": 0,
    },
    "words": ["extinction", "endangered", "habitat", "genetic variation"],
    "word_defs": {
        "extinction": "When a species dies out completely. No individuals are left alive anywhere.",
        "endangered": "At risk of becoming extinct.",
        "habitat": "The place where an organism lives.",
        "genetic variation": "Differences in genes between individuals of the same species.",
    },
    "knowledge": [
        {"kind": "card", "title": "What extinction means",
         "body": ["A species is extinct when no individuals of it are left alive anywhere.",
                  "Extinction is permanent. The species cannot come back.",
                  "The dodo and the dinosaurs are extinct.",
                  "A species at risk of extinction is endangered, such as the tiger."]},
        {"kind": "card", "title": "When the environment changes",
         "body": ["Each species is adapted to its environment.",
                  "When the environment changes, some individuals may no longer be well adapted.",
                  "They cannot compete well, so fewer of them survive and reproduce.",
                  "If some have variations that suit the new conditions, the species may survive.",
                  "If none can survive and reproduce, the species becomes extinct."]},
        {"kind": "reveal", "title": "Ways a species can become extinct",
         "cols": ["What happens", "Example"],
         "rows": [
             ("New predators", "A predator arrives that the species has no defence against.",
              "Stoats brought to New Zealand kill kakapo, a parrot that cannot fly."),
             ("New diseases", "A disease spreads that none of the species can resist.",
              "A fungus disease has wiped out many species of frog."),
             ("More successful competitors", "A new species takes the food or space it needs.",
              "Grey squirrels have replaced red squirrels in most of England."),
             ("Habitat destruction", "Its habitat is cut down, built on or polluted.",
              "Orangutans are endangered as their rainforest is cleared."),
             ("Climate change", "The climate changes faster than the species can adapt over many generations.",
              "Dinosaurs died out after an asteroid strike changed the climate."),
             ("Hunting by people", "People kill too many for food or trade.",
              "Sailors hunted the dodo. Their rats and pigs ate its eggs. It died out within 100 years."),
         ]},
        {"kind": "card", "title": "Which species are most at risk",
         "body": [{"points": ["Species that eat one kind of food or live in one kind of habitat.",
                              "Species that breed slowly, so they replace losses slowly.",
                              "Species that live only in a small area.",
                              "Small populations with little genetic variation."]},
                  "A giant panda eats almost only bamboo. It raises one cub every two years at most."]},
        {"kind": "reveal", "title": "Two species, one change",
         "cols": ["Brown rat", "Hazel dormouse"],
         "rows": [
             ("Food", "Eats almost anything.", "Eats a few foods, in order through the year."),
             ("Breeding", "Up to five litters a year.", "Usually one small litter a year."),
             ("Moving", "Crosses open ground and moves into towns.", "Will not cross open ground."),
             ("Genetic variation", "High.", "Low, as small groups get cut off from each other."),
             ("After half the wood is cleared", "Recovers within a few years.", "May not recover."),
         ]},
        {"kind": "card", "title": "Extinction has always happened",
         "body": ["Most species that have ever lived are now extinct.",
                  "Most of them died out long before there were humans.",
                  "There have been five mass extinctions, when most species died out in a short time.",
                  "Today species are dying out much faster than the natural rate.",
                  "Habitat destruction, hunting, introduced species and climate change are the main causes."]},
        {"kind": "card", "title": "A lost species is not quickly replaced",
         "body": ["After a mass extinction, the number of species took millions of years to recover.",
                  "Meanwhile, the food web has lost a link, so other species are affected.",
                  "Each species also has its own mix of genes. Once lost, that mix is gone."]},
        {"kind": "card", "title": "Helping a species survive",
         "body": [{"points": ["Protect its habitat, or make its reserve bigger.",
                              "Link cut-off habitats, for example with hedgerows. Then groups can meet and "
                              "breed, which keeps genetic variation.",
                              "Breed it in zoos and release the young into the wild.",
                              "Ban hunting and trade in the species."]},
                  "Captive breeding raises numbers. The animals still need a habitat to return to."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Extinction only happens because of humans.",
              "Most extinct species died out before humans existed. Humans are speeding it up now.",
              "EVOL-05"),
             ("If a species goes extinct, another one just takes its place.",
              "Replacement can take millions of years. Meanwhile the food web loses a link.",
              "EVOL-06"),
             ("Big, strong animals are safe from extinction.",
              "Size does not protect a species. Tigers and elephants are both endangered."),
             ("Endangered means extinct.",
              "Endangered means at risk. Extinct means none are left alive."),
         ]}]},
    ],
    "key_fact": "A species becomes extinct when no individuals are left alive. This happens when the "
                "environment changes and too few individuals can survive and reproduce. Causes include new "
                "predators, new diseases, competitors, habitat destruction and climate change.",
    "deeper": [
        {"kind": "card", "title": "The kakapo",
         "body": ["The kakapo is a large parrot from New Zealand that cannot fly.",
                  "New Zealand had no land mammals except bats. Birds that could not fly still survived.",
                  "When threatened, it freezes. That fools an eagle, but not a stoat that hunts by smell.",
                  "It breeds only in years when certain trees fruit heavily.",
                  "People brought rats, cats and stoats. The kakapo fell to 51 birds.",
                  "Every kakapo is now named and tracked. Numbers are slowly rising."]},
    ],
    "try": None,
    "tutor_body": "Want to work out the risks for a species you know?",
    "ks4_becomes": "Causes of extinction, and the fossil record as evidence for evolution.",
    "ladder_stem": {
        "explain": "A brown rat and a hazel dormouse live in the same wood. Half of the wood is cleared. "
                   "Explain why the rats recover and the dormice may not. Use at least three of the four "
                   "risk factors.",
        "produce": "A team can do one thing to save an endangered woodland species. They can make its reserve "
                   "bigger. They can plant hedgerows linking it to another group. Or they can breed it in a "
                   "zoo. Argue for one, using the risk factors. Say what the other two would and would not fix.",
    },
    "ladder_ticks": [
        ["Says the rat is a generalist and the dormouse a specialist, and explains why that matters when "
         "habitat changes.",
         "Says rats eat almost anything but dormice need a few foods, and why that matters."],
        ["Says the rat breeds several times a year and the dormouse once, so the rat replaces losses far "
         "faster.",
         "Says rats breed several times a year and dormice once, so rats replace losses faster."],
        ["Says the dormouse will not cross open ground, so the remaining wood is fragmented into isolated "
         "populations.",
         "Says dormice will not cross open ground, so they are cut off in small groups."],
        ["Concludes that the rat population recovers while the dormouse population may decline to nothing "
         "even though the event was identical.",
         "Concludes the rats recover but the dormice may die out, after the same change."],
        ["Identifies which risk factor each option addresses — range, fragmentation and genetic variation, "
         "or numbers.",
         "Says which risk factor each option helps: range, cut-off groups and variation, or numbers."],
        ["Makes a clear choice and gives a reason grounded in the risk factors rather than in preference.",
         "Makes a clear choice, with a reason based on the risk factors."],
        ["Recognises that linking populations addresses genetic variation as well as space, which the other "
         "two do not.",
         "Says linking groups lets them breed together, which keeps genetic variation."],
        ["Notes a limitation of captive breeding — that it does not fix the habitat the animals would return "
         "to, or that captive populations lose variation too.",
         "Says captive breeding does not fix the habitat the animals return to."],
        ["Acknowledges that the options are not equally cheap or equally quick, and that a real decision "
         "involves a trade-off.",
         "Says the options differ in cost and speed, so choosing means a trade-off."],
    ],
    "figures": [],
    "ladder_feedback": {
        "recall": {
            1: "Small size does not decide it. Rats are small and very hard to wipe out.",
            2: "A large, widespread population is one of the safest things to have.",
            3: "Species live alongside their usual predators. A new predator is the danger.",
        },
        "apply": {
            0: "Species died out long before humans. Five mass extinctions happened without us.",
            2: "Extinction is natural, but humans have made it much faster. That is a worry.",
            3: "Well adapted species die out too, when their conditions change.",
        },
    },
}
