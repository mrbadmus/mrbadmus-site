"""B10 lesson 03 — How we worked out DNA's structure: twelve questions (MRB-269).

The lesson's argument is that a structure nobody could see was reached by
elimination: four pieces of evidence, each ruling something out, until one
combination was left. These twelve probe that argument from the sides the
ladder does not — what Photo 51 actually is, which card goes red for a given
setting of the bench, why equal amounts of two bases imply pairing, and why a
model that was wrong still counted for something.

The distractors are built from the lesson's two declared misconceptions.
GENE-05 (Watson and Crick discovered DNA) drives the who-did-what confusions in
e04, h02 and h04 — every one of them hands a contribution to the wrong person or
makes assembling other people's measurements sound like doing nothing. NOS-03 (a
great discovery is one person's flash of insight) drives s03, h02 and h03, where
a ruled-out rival is treated as worthless and twenty years of work in five
laboratories collapses into one moment. A third family, everywhere in the lesson
and named in its own vocabulary note, treats Photo 51 as a photograph of a
molecule: e01 and h01 both carry a distractor that does exactly that. h04 holds
the lesson's most carefully drawn line — Franklin was ineligible for the 1962
Nobel because she had died, not denied it over the credit dispute — and its
three wrong options are the three stories students build instead.
"""

UNIT = "B10"
LESSON = "how-we-worked-out-dna"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-03-e01",
        "band": "easier",
        "text": "Photo 51 is the most famous image in this story. What is it "
                "actually an image of?",
        "options": [
            {"text": "A photograph of a DNA molecule taken with a very "
                     "powerful microscope", "correct": False,
             "why": "No microscope can show you the shape of a single "
                    "molecule — that is the whole problem the lesson opens "
                    "with. Photo 51 is not a picture of DNA at all."},
            {"text": "A pattern of spots made by X-rays scattering off "
                     "fibres of DNA", "correct": True},
            {"text": "A drawing of the helix, made once the structure had "
                     "been worked out", "correct": False,
             "why": "You have the order backwards. The image came first, in "
                    "1952, and the helix was worked backwards out of it — the "
                    "drawings came after."},
            {"text": "A chemical test that changed colour to reveal the "
                     "molecule's shape", "correct": False,
             "why": "A colour change tells you what something is made of, "
                    "never how its atoms are arranged. The arrangement came "
                    "from the geometry of scattered X-rays."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e02",
        "band": "easier",
        "text": "In the structure published in April 1953, where do the bases "
                "sit?",
        "options": [
            {"text": "On the inside, paired with each other across the two "
                     "strands", "correct": True},
            {"text": "On the outside, facing the water, with the phosphates "
                     "in the centre", "correct": False,
             "why": "That is Pauling's arrangement, and it fails twice: DNA "
                    "takes up far too much water for the phosphates to be "
                    "hidden inside, and crowded negative phosphates would "
                    "push the molecule apart."},
            {"text": "Along one strand only, with the other strand carrying "
                     "the phosphates", "correct": False,
             "why": "Both strands are the same kind of thing — each has a "
                    "phosphate backbone on the outside and bases pointing "
                    "inwards. The pairing happens between them."},
            {"text": "Wound round the outside of the two strands, holding "
                     "them together", "correct": False,
             "why": "You have the job right and the position wrong. The base "
                    "pairs are what hold the two strands together, and they "
                    "do it from the inside."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e03",
        "band": "easier",
        "text": "Franklin found that DNA takes up a great deal of water. What "
                "did that tell her about the molecule?",
        "options": [
            {"text": "The bases must be on the outside, since they are what "
                     "attracts the water", "correct": False,
             "why": "The water-attracting parts are the phosphate groups, not "
                    "the bases. Put the bases outside and the phosphates end "
                    "up crowded in the centre, where they would repel each "
                    "other."},
            {"text": "There must be three strands, because that many can hold "
                     "more water", "correct": False,
             "why": "The number of strands came from the measured width in "
                    "the diffraction pattern, not from the water. This "
                    "measurement is about which parts face outwards."},
            {"text": "The phosphate groups must be on the outside, in contact "
                     "with the water", "correct": True},
            {"text": "It must be a helix, because a spiral holds more water "
                     "than a straight chain", "correct": False,
             "why": "The helix came from the cross-shaped pattern of spots in "
                    "Photo 51. Each piece of evidence settles one thing, and "
                    "the water settles where the phosphates sit."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e04",
        "band": "easier",
        "text": "Rosalind Franklin worked at King's College London. What was "
                "her contribution?",
        "options": [
            {"text": "She measured how much A, T, C and G each species "
                     "contains", "correct": False,
             "why": "Those were Chargaff's measurements, made at Columbia in "
                    "New York. Franklin's work was X-ray crystallography, not "
                    "chemical analysis."},
            {"text": "She built the metal models that were tested against the "
                     "measurements", "correct": False,
             "why": "The model building was Watson and Crick's, in Cambridge. "
                    "Franklin produced the evidence their models had to fit."},
            {"text": "She published the triple-helix model that had to be "
                     "ruled out", "correct": False,
             "why": "That was Pauling, in California. Franklin's measurements "
                    "are part of what ruled his model out."},
            {"text": "She produced the X-ray diffraction images and the "
                     "measurements taken from them", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-03-s01",
        "band": "standard",
        "text": "At the bench a student chooses one strand, bases on the "
                "inside, A with T and C with G. One card goes red. Which, and "
                "why?",
        "options": [
            {"text": "Chargaff's ratios — a single strand has no second "
                     "strand to pair with", "correct": False,
             "why": "Chargaff's card asks only how the bases pair, and this "
                    "student has already chosen A with T and C with G, so it "
                    "passes. The objection you are making is a real one, but "
                    "it is not what this card tests."},
            {"text": "Franklin's water measurements — one strand cannot take "
                     "up that much water", "correct": False,
             "why": "The water measurements are about which parts face "
                    "outwards, not how many strands there are. The bases are "
                    "already on the inside here, so this card passes."},
            {"text": "Photo 51 — a single strand is too narrow for the "
                     "measured width", "correct": True},
            {"text": "Pauling's model — his published model had a single "
                     "strand too", "correct": False,
             "why": "Pauling's model had three strands with the bases facing "
                    "outwards. That card only rules out that one combination, "
                    "and this is not it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s02",
        "band": "standard",
        "text": "In DNA from every species ever measured, the amount of A "
                "equals the amount of T. Why does that point to A pairing "
                "with T?",
        "options": [
            {"text": "If each A is joined to a T across the strands, their "
                     "amounts must come out equal", "correct": True},
            {"text": "Equal amounts must mean that A and T are really the "
                     "same chemical unit", "correct": False,
             "why": "A and T are two different bases. Equal amounts tell you "
                    "how they are arranged with respect to each other, not "
                    "that they are the same substance."},
            {"text": "Every species has the same DNA, so all four base "
                     "amounts come out equal", "correct": False,
             "why": "The four amounts are not all equal. A equals T and C "
                    "equals G, but the ratio of A to C varies from species to "
                    "species — which is exactly why species differ."},
            {"text": "Nothing on its own, because Chargaff never said what "
                     "his own ratios meant", "correct": False,
             "why": "He did not draw the conclusion, and the pattern sat in "
                    "his tables for three years waiting for someone to. "
                    "Evidence does not stop being evidence because the person "
                    "who collected it missed what it implied."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s03",
        "band": "standard",
        "text": "Pauling's triple-helix model was wrong. Why is it on the "
                "bench as a piece of evidence at all?",
        "options": [
            {"text": "It is there to show that even the most famous "
                     "scientists make mistakes", "correct": False,
             "why": "True, but that is a moral, not evidence. It earns its "
                    "place because ruling it out removed a combination "
                    "everybody else then no longer had to consider."},
            {"text": "It had to be tested first, because Pauling was the most "
                     "respected chemist alive", "correct": False,
             "why": "Reputation is not what makes something evidence. His "
                    "model counts because of what its failure eliminated, and "
                    "it would count the same if an unknown had published it."},
            {"text": "It was nearly right, and only needed one of its three "
                     "strands taking away", "correct": False,
             "why": "Two things were wrong, not one. It had three strands and "
                    "the bases facing outwards, which crowded the negative "
                    "phosphates into the centre where they would push the "
                    "molecule apart."},
            {"text": "Ruling out a serious rival narrowed the field of "
                     "possible structures", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s04",
        "band": "standard",
        "text": "A student sets the bench to three strands, bases on the "
                "outside, A with T and C with G. Three cards go red. Which "
                "one still passes?",
        "options": [
            {"text": "Photo 51", "correct": False,
             "why": "Three strands is too wide for the width the spacing of "
                    "the spots gives, so Photo 51 is one of the red ones."},
            {"text": "Chargaff's ratios", "correct": True},
            {"text": "Franklin's water measurements", "correct": False,
             "why": "Bases on the outside puts the phosphates in the centre, "
                    "which contradicts how much water DNA takes up. Red."},
            {"text": "Pauling's triple helix", "correct": False,
             "why": "Three strands with the bases outward is Pauling's model "
                    "exactly, and it had already been ruled out. Red."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-03-h01",
        "band": "harder",
        "text": "The diagram draws A and G wide and C and T narrow. Suppose "
                "the rule had instead been A with G and C with T. What would "
                "the molecule have been like?",
        "options": [
            {"text": "Its width would stay constant, because the backbones "
                     "are a fixed distance apart", "correct": False,
             "why": "That is the cause running backwards. Nothing holds the "
                    "backbones apart except the rungs between them — the "
                    "pairs set the width, not the other way round."},
            {"text": "It would be wider all along, since A and G are both big "
                     "bases", "correct": False,
             "why": "If A took G, then C would be left with T — small with "
                    "small. You would get wide rungs and narrow rungs "
                    "alternating, not a uniformly wide molecule."},
            {"text": "It would look the same, because the pattern shows the "
                     "shape and not the bases", "correct": False,
             "why": "The pattern is what gave the width, and the width is set "
                    "by the bases. A molecule that bulged and pinched could "
                    "not have produced the single constant spacing Franklin "
                    "measured."},
            {"text": "Its width would vary — bulging at big-with-big and "
                     "pinching at small-with-small", "correct": True},
        ],
        "figure": "b10-base-pairs",
    },
    {
        "id": "b10-03-h02",
        "band": "harder",
        "text": "A team publishes a model of a virus protein built entirely "
                "from other laboratories' measurements. A classmate says that "
                "is not real science. What is the best reply?",
        "options": [
            {"text": "They are right — a result only counts if you measured "
                     "it yourself", "correct": False,
             "why": "That would throw out the 1953 structure. Watson and "
                    "Crick did no experiments on DNA at all; what made their "
                    "work science was that the model had to survive "
                    "everyone else's numbers."},
            {"text": "They are right, unless the team is given a prize for "
                     "the work", "correct": False,
             "why": "Prizes follow work, they do not make it science. "
                    "Pauling's model won nothing and still narrowed the field "
                    "for everyone."},
            {"text": "Model building is a method in itself — a model still "
                     "has to fit everyone's measurements", "correct": True},
            {"text": "It only counts as science if the model turns out to be "
                     "correct", "correct": False,
             "why": "Pauling's triple helix was wrong and still mattered, "
                    "because seeing why it failed ruled a whole combination "
                    "out. Being testable is what counts, not being right."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h03",
        "band": "harder",
        "text": "A textbook says: \"In 1953 Watson and Crick had a flash of "
                "insight, and the double helix was born.\" What is the "
                "strongest objection to that sentence?",
        "options": [
            {"text": "It should say 1952, which is the year Photo 51 was "
                     "actually taken", "correct": False,
             "why": "The date of publication is right. What is wrong is the "
                    "picture of a single moment standing in for twenty years "
                    "of work in several laboratories."},
            {"text": "Five laboratories in three countries over two decades "
                     "produced what the model had to fit", "correct": True},
            {"text": "It should name Wilkins as well, since he shared the "
                     "1962 Nobel Prize", "correct": False,
             "why": "Adding a name does not repair it. The sentence would "
                    "still describe a flash of insight rather than an "
                    "argument assembled from images, ratios and a ruled-out "
                    "rival."},
            {"text": "Nothing — they did have the key idea and only needed "
                     "data to confirm it", "correct": False,
             "why": "This is the flash-of-insight story itself. The data was "
                    "not confirmation added at the end: every feature of the "
                    "model was forced by a measurement somebody else had "
                    "already made."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h04",
        "band": "harder",
        "text": "The 1962 Nobel Prize went to Watson, Crick and Wilkins. "
                "Franklin was not among them. Why not?",
        "options": [
            {"text": "She had died in 1958, and a Nobel cannot be given after "
                     "death", "correct": True},
            {"text": "The committee judged that her images had not "
                     "contributed to the model", "correct": False,
             "why": "Her images and the measurements taken from them are what "
                    "the model had to fit. She was not on the 1962 list "
                    "because she had died four years earlier and the rules "
                    "do not allow a posthumous award."},
            {"text": "She had refused permission for her measurements to be "
                     "used by others", "correct": False,
             "why": "She was never asked — the report reached Crick without "
                    "her knowledge. That is a real part of the story, but it "
                    "is not the reason she was left off the prize."},
            {"text": "Her name was left out of the 1953 paper's "
                     "acknowledgement", "correct": False,
             "why": "The acknowledgement did understate what was owed, and "
                    "that is worth knowing. It is a separate matter from the "
                    "Nobel, which she was not eligible for because she had "
                    "died in 1958."},
        ],
        "figure": None,
    },
]
