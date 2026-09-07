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
            {"text": "She took the X-ray diffraction images and the "
                     "measurements from them", "correct": True},
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
            {"text": "Model building is a method — a model still has to fit "
                     "everyone's measurements", "correct": True},
            {"text": "It only counts as science once the model turns out to "
                     "match the real structure", "correct": False,
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
            {"text": "Five laboratories over two decades produced what the "
                     "model had to fit", "correct": True},
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

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-03-e05",
        "band": "easier",
        "text": "The two strands of DNA are joined by pairs of bases. Which "
                "of these is one of the pairs?",
        "options": [
            {"text": "A with C",
             "correct": False,
             "why": "A and C never pair. A goes with T, and C goes with G — "
                    "which is what Chargaff's equal amounts pointed to"},
            {"text": "A with A",
             "correct": False,
             "why": "A base never pairs with a copy of itself. Each rung joins "
                    "one base on one strand to a different base on the other"},
            {"text": "C with G",
             "correct": True},
            {"text": "T with G",
             "correct": False,
             "why": "T pairs with A, and G pairs with C. Swapping the partners "
                    "round would give unequal amounts, and every organism ever "
                    "measured gives equal ones"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e06",
        "band": "easier",
        "text": "The structure published in 1953 is called a double helix. "
                "What shape is that?",
        "options": [
            {"text": "Two strands wound round each other in a spiral",
             "correct": True},
            {"text": "One strand folded back on itself to make two halves",
             "correct": False,
             "why": "There are two separate strands, not one folded in half. "
                    "The measured width in the diffraction pattern is what "
                    "settled the number"},
            {"text": "Two flat ribbons lying side by side without twisting",
             "correct": False,
             "why": "Flat ribbons would not give the cross-shaped pattern of "
                    "spots that Photo 51 shows. The cross is the signature of "
                    "a helix"},
            {"text": "Three strands twisted together, with the bases facing "
                     "outwards",
             "correct": False,
             "why": "That is Pauling's model, which was published early in "
                    "1953 and was wrong. The measured width says two strands"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e07",
        "band": "easier",
        "text": "DNA itself was found long before its structure was worked "
                "out. Who found it, and roughly when?",
        "options": [
            {"text": "Chargaff, in 1950, while measuring the amounts of the "
                     "four bases",
             "correct": False,
             "why": "Chargaff measured the base amounts in DNA that was "
                    "already well known. He was working on a substance "
                    "discovered eighty years earlier"},
            {"text": "Watson and Crick, in 1953, in Cambridge",
             "correct": False,
             "why": "This is the commonest mistake in the whole story. They "
                    "worked out the structure; the substance itself had been "
                    "known since 1869"},
            {"text": "Franklin and Wilkins, in 1952, at King's College London",
             "correct": False,
             "why": "They produced the X-ray images of a substance already "
                    "known for over eighty years. Their work was on its shape"},
            {"text": "Friedrich Miescher, in 1869",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e08",
        "band": "easier",
        "text": "Erwin Chargaff worked in New York with chemical amounts "
                "rather than images. What did he measure?",
        "options": [
            {"text": "The width of the DNA molecule and the distance along "
                     "it taken up by a single full turn of the helix",
             "correct": False,
             "why": "Those came from the X-ray diffraction images taken at "
                    "King's. Chargaff never worked with images at all"},
            {"text": "How much of each of the four bases DNA from different "
                     "organisms contains",
             "correct": True},
            {"text": "How much water DNA takes up",
             "correct": False,
             "why": "That was Franklin's measurement, and it is what put the "
                    "phosphates on the outside. Chargaff was counting bases"},
            {"text": "How many genes each chromosome carries in the "
                     "organisms he collected his samples from",
             "correct": False,
             "why": "Nobody could count genes in 1950. What Chargaff could "
                    "measure was the proportion of each base in a sample"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e09",
        "band": "easier",
        "text": "In the story of how DNA's structure was worked out, what "
                "is meant by a model?",
        "options": [
            {"text": "A drawing made once the answer is already known, in "
                     "order to explain that answer to other people",
             "correct": False,
             "why": "That is an illustration, made afterwards. A model is "
                    "built while the answer is still unknown, so that it can "
                    "be tested"},
            {"text": "A smaller copy of something real, built to the right "
                     "proportions in every dimension",
             "correct": False,
             "why": "That is a scale model. Here a model is a proposal about "
                    "what the structure might be, kept only while it fits the "
                    "evidence"},
            {"text": "A representation built to be tested against evidence "
                     "and dropped if wrong",
             "correct": True},
            {"text": "An idea that has been proved correct and can now be "
                     "relied on",
             "correct": False,
             "why": "Pauling's model was a model and it was wrong. Being "
                    "testable, not being right, is what makes something a "
                    "model"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e10",
        "band": "easier",
        "text": "The 1953 paper closed by noting that the structure it "
                "proposed immediately suggested something. What?",
        "options": [
            {"text": "A way the molecule could be copied",
             "correct": True},
            {"text": "A way of curing inherited disease",
             "correct": False,
             "why": "That was decades away and the paper claimed nothing of "
                    "the kind. What the geometry suggested was how the "
                    "material could be copied"},
            {"text": "A way of counting the genes in a chromosome",
             "correct": False,
             "why": "Counting genes was far beyond anything available then. "
                    "The structure's own shape pointed at copying"},
            {"text": "A way of photographing a single molecule directly",
             "correct": False,
             "why": "No microscope can do that even now. The structure had "
                    "been deduced precisely because it could not be "
                    "photographed"},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-03-s05",
        "band": "standard",
        "text": "Chargaff found that A always equals T in every organism, but "
                "that the ratio of A to C changes from one species to "
                "another. What does the changing ratio show?",
        "options": [
            {"text": "That some species must have more strands of DNA in "
                     "each of their chromosomes than other species do",
             "correct": False,
             "why": "Every species has the same two-stranded molecule. What "
                    "differs is what is written along it"},
            {"text": "That what is written along the molecule differs "
                     "between species, unlike the pairing rule",
             "correct": True},
            {"text": "That his measurements were less reliable for some "
                     "species",
             "correct": False,
             "why": "The variation is real and repeatable. A rule that holds "
                    "everywhere, alongside a proportion that varies, is "
                    "exactly what a shared structure carrying different "
                    "information looks like"},
            {"text": "That the pairing rule holds in some species and "
                     "breaks down in others, depending on the sample he "
                     "happened to test",
             "correct": False,
             "why": "The pairing rule held in every sample he tested — that is "
                    "the half that never changed. Only the proportion of A to "
                    "C moved"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s06",
        "band": "standard",
        "text": "One argument against putting the phosphate groups in the "
                "centre of the molecule was about the phosphates themselves. "
                "What was it?",
        "options": [
            {"text": "Phosphates are far too large to fit into the middle "
                     "of a molecule as narrow as DNA had already been "
                     "measured to be",
             "correct": False,
             "why": "Size was not the objection. The problem was electrical — "
                    "the phosphates carry negative charges"},
            {"text": "Phosphates are not part of DNA at all, so the "
                     "question of where they sit inside it does not even "
                     "arise",
             "correct": False,
             "why": "They are part of it, and they run along the two "
                    "backbones. The question was whether those backbones face "
                    "in or out"},
            {"text": "Phosphates in the middle would block the bases from "
                     "being read",
             "correct": False,
             "why": "Reading was not what was being argued about in 1952. The "
                    "objection was that negative charges crowded together "
                    "repel each other"},
            {"text": "They carry negative charges, so crowding them into "
                     "the centre would push the molecule apart",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s07",
        "band": "standard",
        "text": "In 1944 Avery, MacLeod and McCarty showed that DNA is the "
                "material carrying inherited information. Why did that result "
                "make the structure worth chasing?",
        "options": [
            {"text": "Because once DNA was known to be the material, how it is "
                     "built became the question",
             "correct": True},
            {"text": "Because it showed that the structure of DNA must be a "
                     "helix",
             "correct": False,
             "why": "It said nothing about shape. The helix came from the "
                    "diffraction images taken eight years later"},
            {"text": "Because it proved that proteins carry no information at "
                     "all",
             "correct": False,
             "why": "It showed DNA carries it, which surprised biochemists who "
                    "had expected protein. That is not the same as ruling "
                    "proteins out of everything"},
            {"text": "Because it gave Watson and Crick the measurements they "
                     "later built their model from",
             "correct": False,
             "why": "The measurements came from Franklin, Wilkins and "
                    "Chargaff. The 1944 result supplied the reason to care, "
                    "not the numbers"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s08",
        "band": "standard",
        "text": "A student says the four pieces of evidence available in 1952 "
                "showed Watson and Crick what the answer was. What is a "
                "better description of what the evidence did?",
        "options": [
            {"text": "It confirmed the model they had already built, one piece "
                     "at a time",
             "correct": False,
             "why": "They built several models and threw them away. Evidence "
                    "that only ever confirms is not being used as a test"},
            {"text": "It suggested the answer to anyone clever enough to see "
                     "it",
             "correct": False,
             "why": "Chargaff had his own ratios for years without seeing what "
                    "they meant, and Pauling was the most respected chemist "
                    "alive and got it wrong. Cleverness was not the mechanism"},
            {"text": "It ruled possibilities out until only one combination "
                     "was left standing",
             "correct": True},
            {"text": "It measured the structure directly, so the model only "
                     "had to be drawn from the measurements",
             "correct": False,
             "why": "Nothing measured the structure directly — that is the "
                    "whole difficulty. Each piece of evidence eliminated "
                    "something rather than displaying the answer"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s09",
        "band": "standard",
        "text": "Maurice Wilkins shared the 1962 Nobel Prize with Watson and "
                "Crick. What was his part in the work?",
        "options": [
            {"text": "He measured the base ratios in New York that gave the "
                     "pairing rule its evidence, working quite separately from "
                     "the London team",
             "correct": False,
             "why": "Those were Chargaff's, measured in New York. Wilkins "
                    "worked on X-ray images at King's"},
            {"text": "He worked on DNA's X-ray images at King's, and it was he "
                     "who showed Franklin's image to Watson",
             "correct": True},
            {"text": "He built the metal models in Cambridge alongside Watson "
                     "and Crick",
             "correct": False,
             "why": "The model building was done in Cambridge by Watson and "
                    "Crick. Wilkins was at King's, working on the images"},
            {"text": "He published the triple-helix model that had to be ruled "
                     "out",
             "correct": False,
             "why": "That was Linus Pauling, in California. Wilkins was one of "
                    "the two people producing the King's diffraction work"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s10",
        "band": "standard",
        "text": "Five years after 1953, Meselson and Stahl showed "
                "experimentally that DNA really is copied in the way the "
                "structure suggested. What did their result change?",
        "options": [
            {"text": "It showed that the 1953 structure had been wrong in "
                     "at least one important detail",
             "correct": False,
             "why": "It confirmed the structure's most striking implication "
                    "rather than correcting it. The model survived the test"},
            {"text": "It replaced the model with a photograph of DNA "
                     "copying",
             "correct": False,
             "why": "No photograph of that exists, then or now. What they "
                    "produced was an experiment whose result the model had "
                    "predicted"},
            {"text": "It meant the credit for working out the structure "
                     "had to be shared much more widely than before",
             "correct": False,
             "why": "The question of credit is a separate one, and it turns on "
                    "whose data was used in 1953. Meselson and Stahl were "
                    "testing the model, not auditing it"},
            {"text": "The copying idea stopped being a proposal and became "
                     "a tested result",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-03-h05",
        "band": "harder",
        "text": "A student asks why the scientists did not simply look at DNA "
                "down a microscope in 1952 and settle the argument. What is "
                "the reply, and what follows from it?",
        "options": [
            {"text": "DNA is far too thin for any microscope to resolve, "
                     "so its structure had to be deduced indirectly",
             "correct": True},
            {"text": "Microscopes of the 1950s were not good enough, but a "
                     "modern electron microscope would be able to show the "
                     "double helix directly",
             "correct": False,
             "why": "No microscope today can show the shape of a single DNA "
                    "molecule either. It is not a matter of the equipment "
                    "catching up"},
            {"text": "DNA can be seen, but only while a cell is dividing, "
                     "and none were available",
             "correct": False,
             "why": "What becomes visible then is a whole chromosome, packed "
                    "from a great many turns of the molecule. The molecule "
                    "itself stays far below what can be resolved"},
            {"text": "They could have looked, but X-ray diffraction gave a "
                     "much sharper picture of the molecule, so they used "
                     "that",
             "correct": False,
             "why": "Diffraction gives no picture at all — Photo 51 is a "
                    "pattern of spots. It was used because looking was "
                    "impossible, not because it was better looking"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h06",
        "band": "harder",
        "text": "Chargaff published his base ratios years before 1953 without "
                "seeing what they implied. What does that episode show about "
                "how evidence works?",
        "options": [
            {"text": "That a measurement is only worth publishing once its "
                     "meaning is understood",
             "correct": False,
             "why": "Exactly backwards. His numbers were correct and useful "
                    "precisely because he published them before anyone knew "
                    "what to do with them"},
            {"text": "That his ratios cannot have been the real reason for the "
                     "pairing rule, since he did not see it himself",
             "correct": False,
             "why": "Who noticed what a result means does not change what the "
                    "result establishes. The equal amounts are the evidence "
                    "either way"},
            {"text": "That data can be correct and its meaning stay unnoticed "
                     "until someone has a model to fit it to",
             "correct": True},
            {"text": "That measurements taken without a hypothesis are of "
                     "little use to anybody",
             "correct": False,
             "why": "His measurements became one of the three legs of the "
                    "1953 model. Waiting for a use is not the same as being "
                    "useless"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h07",
        "band": "harder",
        "text": "Explain why a structure in which A always pairs with T and C "
                "always with G immediately suggests how DNA could be copied.",
        "options": [
            {"text": "Because the two strands are identical, so one can simply "
                     "be used twice",
             "correct": False,
             "why": "They are not identical — they are partners. Wherever one "
                    "reads A the other reads T, which is a different sequence "
                    "carrying the same information"},
            {"text": "Because separating the strands leaves each one "
                     "specifying exactly what must be built alongside it",
             "correct": True},
            {"text": "Because a molecule with a repeating pattern can grow "
                     "longer by adding more of the same pattern",
             "correct": False,
             "why": "The order of bases is not a repeating pattern — it is the "
                    "information, and it must be reproduced exactly rather "
                    "than extended"},
            {"text": "Because the bases sit on the inside, where they are "
                     "protected from damage during copying",
             "correct": False,
             "why": "Protection is a real advantage of the arrangement and is "
                    "not what suggests copying. What does is that each base "
                    "has exactly one possible partner"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h08",
        "band": "harder",
        "text": "A newspaper article says simply that Franklin's data was "
                "stolen. Historians say the episode is more complicated than "
                "that. What is a fair summary?",
        "options": [
            {"text": "The complications mean that no fair criticism can "
                     "now be made of the way her data was used by Watson "
                     "and Crick in 1953",
             "correct": False,
             "why": "One thing is not in dispute: the data were used without "
                    "her knowledge and the acknowledgement understated what "
                    "was owed. Complication is not the same as exoneration"},
            {"text": "Nothing was owed, because unpublished results are "
                     "open to anyone",
             "correct": False,
             "why": "The rule people have since drawn from this episode is the "
                    "opposite: data belongs to whoever produced it and should "
                    "be used with their knowledge"},
            {"text": "The whole argument is really about the Nobel rules, "
                     "since the prize cannot be given after a person's "
                     "death",
             "correct": False,
             "why": "That explains the 1962 prize and nothing else. The use of "
                    "her measurements in 1953 is a separate question, and it "
                    "is the one being asked"},
            {"text": "Her data was used without her knowledge and "
                     "under-acknowledged; how much else counted is argued",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h09",
        "band": "harder",
        "text": "A chemist measures a new sample and finds A 31 per cent, T "
                "31 per cent, C 19 per cent and G 19 per cent. Does the "
                "sample fit Chargaff's rule, and what does that suggest?",
        "options": [
            {"text": "Yes — A equals T and C equals G, which is what paired "
                     "strands would give",
             "correct": True},
            {"text": "No — the rule requires all four bases to be present in "
                     "equal amounts",
             "correct": False,
             "why": "The rule is that A equals T and C equals G, not that all "
                    "four match. The A-to-C ratio varies from species to "
                    "species, and here it is 31 to 19"},
            {"text": "No — A does not equal C, so the pairing rule is broken",
             "correct": False,
             "why": "A and C are not partners, so there is no reason for them "
                    "to match. The partners here, A with T and C with G, do "
                    "match exactly"},
            {"text": "It cannot be judged, because the four percentages do not "
                     "add up to a hundred",
             "correct": False,
             "why": "31 and 31 and 19 and 19 come to exactly 100, so nothing "
                    "is missing. The check is worth doing, and here it passes"},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h10",
        "band": "harder",
        "text": "A student builds a paper model of DNA with the bases on the "
                "outside, and shows that it fits Chargaff's ratios perfectly. "
                "Why is her model still ruled out?",
        "options": [
            {"text": "Because Chargaff's ratios were only about chemical "
                     "amounts and say nothing at all about any model",
             "correct": False,
             "why": "They say a great deal about a model — they are what "
                    "forces A to pair with T. Her model passes that test; the "
                    "trouble is the tests it fails"},
            {"text": "Because a paper model cannot be tested against evidence "
                     "at all",
             "correct": False,
             "why": "Watson and Crick's were metal and cardboard. What matters "
                    "is what a model claims, not what it is cut out of"},
            {"text": "Because a model must fit all the evidence, and the "
                     "water data puts phosphates outside",
             "correct": True},
            {"text": "Because putting the bases on the outside would make "
                     "the molecule far too narrow for the width actually "
                     "measured",
             "correct": False,
             "why": "Width is decided by the number of strands, and Photo 51 "
                    "settled that separately. What rules out bases on the "
                    "outside is where the phosphates then have to go"},
        ],
        "figure": None,
    },
]
