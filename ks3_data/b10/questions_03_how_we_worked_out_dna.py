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
    {
        "id": "b10-03-h01",
        "band": "harder",
        "text": "Look at the base-pair diagram. Suppose the pairing rule had "
                "instead been A with G and C with T. What would the "
                "molecule have been like?",
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
    {
        "id": "b10-03-e11",
        "band": "easier",
        "text": "Photo 51 was taken in Franklin's laboratory. Which of her "
                "colleagues took it with her?",
        "options": [
            {"text": "Francis Crick, who was visiting from Cambridge",
             "correct": False,
             "why": "Crick worked in Cambridge and did no X-ray work at all. "
                    "He was shown other people's results rather than "
                    "producing any."},
            {"text": "Erwin Chargaff, on a visit from New York",
             "correct": False,
             "why": "Chargaff measured chemical amounts in New York and never "
                    "worked with X-ray images."},
            {"text": "Raymond Gosling, her research student",
             "correct": True},
            {"text": "Linus Pauling, who was in California",
             "correct": False,
             "why": "Pauling was building models in California. His own "
                    "triple-helix model was published without any such image."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e12",
        "band": "easier",
        "text": "In which year was the structure of DNA published?",
        "options": [
            {"text": "1869",
             "correct": False,
             "why": "1869 is the year the substance itself was first isolated. "
                    "Its structure took another eighty-four years."},
            {"text": "1944",
             "correct": False,
             "why": "1944 is the year DNA was shown to carry inherited "
                    "information. The shape was still unknown."},
            {"text": "1953",
             "correct": True},
            {"text": "1962",
             "correct": False,
             "why": "1962 is the year the Nobel Prize was awarded. The "
                    "structure had been published nine years earlier."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e13",
        "band": "easier",
        "text": "The picture is a drawing of the pattern made when X-rays "
                "were passed through fibres of DNA. What did this pattern "
                "tell scientists about the molecule?",
        "options": [
            {"text": "That the molecule is a helix",
             "correct": True},
            {"text": "That the molecule carries four different bases",
             "correct": False,
             "why": "Which bases are present is chemistry, and it came from "
                    "measuring amounts rather than from any image."},
            {"text": "That the fibres were crossed over one another",
             "correct": False,
             "why": "The pattern is made by X-rays scattering off the atoms in "
                    "the molecule, not by how the fibres were laid out."},
            {"text": "That the sample was damaged by the X-rays",
             "correct": False,
             "why": "The X shape is a real signal, and it is the signal a "
                    "helix gives. Damage would blur the pattern, not shape it."},
        ],
        "figure": "b10-dna-xray-pattern",
    },
    {
        "id": "b10-03-e14",
        "band": "easier",
        "text": "Where did Rosalind Franklin and Maurice Wilkins work?",
        "options": [
            {"text": "Cambridge",
             "correct": False,
             "why": "Cambridge is where Watson and Crick built their models. "
                    "The X-ray work was done in London."},
            {"text": "Columbia University, New York",
             "correct": False,
             "why": "That is where Chargaff measured his base ratios. He never "
                    "worked on X-ray images."},
            {"text": "California",
             "correct": False,
             "why": "Pauling worked in California and published his "
                    "triple-helix model from there."},
            {"text": "King's College London",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e15",
        "band": "easier",
        "text": "Watson and Crick worked in which city?",
        "options": [
            {"text": "New York",
             "correct": False,
             "why": "Chargaff was in New York. His base ratios travelled to "
                    "the model builders, but he did not."},
            {"text": "Cambridge",
             "correct": True},
            {"text": "London",
             "correct": False,
             "why": "London is where the diffraction images were produced, at "
                    "King's College, by Franklin and Wilkins."},
            {"text": "Oxford",
             "correct": False,
             "why": "No part of this story happened in Oxford. The two "
                    "British laboratories in it are in London and Cambridge."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e16",
        "band": "easier",
        "text": "What were Watson and Crick's models physically made of?",
        "options": [
            {"text": "Crystals grown from purified DNA",
             "correct": False,
             "why": "Crystals and fibres were what the X-ray workers prepared "
                    "to shoot X-rays at. A model is a proposal, built by hand."},
            {"text": "Glass tubes filled with the four bases",
             "correct": False,
             "why": "Nothing chemical was needed. The models were shapes, "
                    "built to be measured against other people's figures."},
            {"text": "A computer program written for the purpose",
             "correct": False,
             "why": "No computer available in 1953 could have done this. The "
                    "models were physical objects on a bench."},
            {"text": "Cardboard and bent metal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e17",
        "band": "easier",
        "text": "Which scientist published a triple-helix model of DNA that "
                "turned out to be wrong?",
        "options": [
            {"text": "Erwin Chargaff",
             "correct": False,
             "why": "Chargaff proposed no model at all. He measured the "
                    "amounts of the four bases and left it there."},
            {"text": "Maurice Wilkins",
             "correct": False,
             "why": "Wilkins worked on the X-ray images at King's. The "
                    "triple-helix model came from outside Britain."},
            {"text": "Friedrich Miescher",
             "correct": False,
             "why": "Miescher isolated the substance in the nineteenth "
                    "century, long before anyone could propose a structure."},
            {"text": "Linus Pauling",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e18",
        "band": "easier",
        "text": "In the structure published in 1953, which parts of the "
                "molecule face outwards, in contact with the water?",
        "options": [
            {"text": "The bases",
             "correct": False,
             "why": "The bases face inwards, paired across the middle. Putting "
                    "them outside is exactly the arrangement that failed."},
            {"text": "The phosphate groups",
             "correct": True},
            {"text": "The proteins wound through the molecule",
             "correct": False,
             "why": "Proteins are what a chromosome winds around. They are no "
                    "part of the DNA molecule's own structure."},
            {"text": "Nothing — the molecule is sealed on all sides",
             "correct": False,
             "why": "DNA takes up a great deal of water, which it could only "
                    "do with water-attracting parts on the outside."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e19",
        "band": "easier",
        "text": "In which year was the Nobel Prize for the work on DNA's "
                "structure awarded?",
        "options": [
            {"text": "1950",
             "correct": False,
             "why": "1950 is the year Chargaff's ratios were published, three "
                    "years before the structure itself."},
            {"text": "1953",
             "correct": False,
             "why": "1953 is the year the structure was published. The prize "
                    "came nine years after that."},
            {"text": "1958",
             "correct": False,
             "why": "1958 is the year the copying mechanism was confirmed "
                    "experimentally, and the year Franklin died."},
            {"text": "1962",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e20",
        "band": "easier",
        "text": "What is crystallography?",
        "options": [
            {"text": "Growing crystals in order to study how quickly they form",
             "correct": False,
             "why": "Growing the sample is only a preparation step. The "
                    "science is in what the sample does to a beam of X-rays."},
            {"text": "Working out how atoms are arranged in a solid from the "
                     "way it scatters X-rays",
             "correct": True},
            {"text": "Photographing very small objects using X-rays instead of "
                     "light",
             "correct": False,
             "why": "No photograph of the molecule is produced. What is "
                    "recorded is a pattern that has to be worked backwards."},
            {"text": "Measuring how much water a solid substance takes up when "
                     "it is left in air",
             "correct": False,
             "why": "Franklin did measure that, and it is a separate "
                    "measurement. Crystallography is about scattered X-rays."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e21",
        "band": "easier",
        "text": "In the name double helix, what does the word double refer to?",
        "options": [
            {"text": "Two kinds of base",
             "correct": False,
             "why": "There are four kinds of base, in two pairs. The word "
                    "counts the strands rather than the bases."},
            {"text": "Two turns of the spiral",
             "correct": False,
             "why": "A helix turns over and over along its whole length. Two "
                    "turns would not be worth naming."},
            {"text": "Two strands",
             "correct": True},
            {"text": "Two molecules held side by side",
             "correct": False,
             "why": "It is one molecule with two strands wound round each "
                    "other, not two molecules laid alongside."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e22",
        "band": "easier",
        "text": "Franklin worked out the width of the molecule from the "
                "spacing of the spots. Which feature of the model did that "
                "width settle?",
        "options": [
            {"text": "How many strands there are",
             "correct": True},
            {"text": "Which base pairs with which",
             "correct": False,
             "why": "The pairing rule came from Chargaff's chemical amounts. A "
                    "width cannot tell you which letter goes with which."},
            {"text": "Whether the phosphates face in or out",
             "correct": False,
             "why": "That came from how much water DNA takes up, which is a "
                    "separate measurement of Franklin's."},
            {"text": "How the molecule is copied",
             "correct": False,
             "why": "Copying was a suggestion that followed from the finished "
                    "structure, not something any measurement showed."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e23",
        "band": "easier",
        "text": "Chargaff measured the amounts of the four bases in DNA from "
                "many species. What did he find about A and T?",
        "options": [
            {"text": "A is always about twice as plentiful as T",
             "correct": False,
             "why": "There is no such relationship. The two come out equal, "
                    "which is the finding that mattered."},
            {"text": "The amount of A and the amount of T are equal",
             "correct": True},
            {"text": "A is plentiful in animals and T in plants",
             "correct": False,
             "why": "The equality holds in every organism measured, whatever "
                    "kind it is. Nothing about it splits by kingdom."},
            {"text": "The two amounts vary independently of each other",
             "correct": False,
             "why": "It is the ratio of A to C that varies from species to "
                    "species. A against T does not move at all."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e24",
        "band": "easier",
        "text": "Which base does T pair with across the two strands?",
        "options": [
            {"text": "C",
             "correct": False,
             "why": "C pairs with G. If C took T, the equal amounts Chargaff "
                    "measured would not follow."},
            {"text": "G",
             "correct": False,
             "why": "G is C's partner. Swapping the partners round would break "
                    "the equalities measured in every organism."},
            {"text": "A",
             "correct": True},
            {"text": "T",
             "correct": False,
             "why": "A base never pairs with a copy of itself. Each rung of "
                    "the ladder joins two different bases."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e25",
        "band": "easier",
        "text": "Two of the four bases are the big ones and two are the small "
                "ones. Which two are big?",
        "options": [
            {"text": "C and T",
             "correct": False,
             "why": "C and T are the small ones. Every rung joins one of these "
                    "to one of the big pair, which keeps the width even."},
            {"text": "A and T",
             "correct": False,
             "why": "A and T are a pair, so one of them is big and the other "
                    "small. That is exactly why the rung comes out even."},
            {"text": "C and G",
             "correct": False,
             "why": "C and G are a pair too, one small and one big. A pair is "
                    "never two of the same size."},
            {"text": "A and G",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e26",
        "band": "easier",
        "text": "When DNA was shown in the 1940s to be the material carrying "
                "inherited information, why was that surprising?",
        "options": [
            {"text": "Because nobody had known that DNA existed until then",
             "correct": False,
             "why": "DNA had been known since 1869. What was new was finding "
                    "out what it does."},
            {"text": "Because DNA had already been shown to be a double helix",
             "correct": False,
             "why": "The structure was still unknown and would stay unknown "
                    "for another nine years."},
            {"text": "Because most biochemists had expected the genetic "
                     "material to be protein",
             "correct": True},
            {"text": "Because the result came from a laboratory with no "
                     "reputation at all",
             "correct": False,
             "why": "Where the work was done is not what made it surprising. "
                    "It was surprising because of what everyone expected."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e27",
        "band": "easier",
        "text": "In X-ray diffraction, what is fired at the sample and what is "
                "recorded?",
        "options": [
            {"text": "Light is shone through the sample and a magnified image "
                     "is recorded",
             "correct": False,
             "why": "That describes a light microscope, and no light "
                    "microscope can resolve a molecule."},
            {"text": "X-rays are fired at the sample and the pattern they "
                     "scatter into is recorded",
             "correct": True},
            {"text": "X-rays are fired at the sample and the amount absorbed "
                     "is recorded",
             "correct": False,
             "why": "How much is absorbed says nothing about arrangement. It "
                    "is the geometry of the scattered beam that is read."},
            {"text": "Electrons are fired at the sample and its temperature "
                     "rise is recorded",
             "correct": False,
             "why": "Neither the beam nor the measurement is right. The method "
                    "is X-rays in, a pattern of spots out."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e28",
        "band": "easier",
        "text": "In the 1953 structure, what holds the two strands together?",
        "options": [
            {"text": "The phosphates along the outside of each strand",
             "correct": False,
             "why": "The phosphates face outwards into the water, away from "
                    "the other strand. They are the backbone, not the join."},
            {"text": "Proteins wound around the outside of the molecule",
             "correct": False,
             "why": "Proteins package a chromosome. They are not part of the "
                    "DNA molecule and hold nothing together inside it."},
            {"text": "The pairs of bases meeting in the middle",
             "correct": True},
            {"text": "Nothing — the two strands are simply twisted round one "
                     "another",
             "correct": False,
             "why": "Twisting alone would let them come apart anywhere. The "
                    "paired bases meet across the middle and hold."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e29",
        "band": "easier",
        "text": "About how long was the paper in which the structure was "
                "announced?",
        "options": [
            {"text": "About fifty pages",
             "correct": False,
             "why": "It was famously short. The argument was a structure and "
                    "the evidence it fitted, not a long account of work done."},
            {"text": "About two hundred pages",
             "correct": False,
             "why": "That is the length of a book. The paper ran to roughly a "
                    "single page."},
            {"text": "It was never written down as a paper at all",
             "correct": False,
             "why": "It was published in April 1953, and its closing sentence "
                    "is one of the most quoted in science."},
            {"text": "About a page",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-e30",
        "band": "easier",
        "text": "Of the evidence available in 1952, which piece was an image "
                "rather than a set of measured amounts?",
        "options": [
            {"text": "Chargaff's ratios",
             "correct": False,
             "why": "Those are chemical amounts, measured in a laboratory in "
                    "New York and printed as a table of figures."},
            {"text": "Franklin's water measurements",
             "correct": False,
             "why": "That is a measurement of how much water DNA takes up. It "
                    "is a number, not a picture."},
            {"text": "Pauling's model",
             "correct": False,
             "why": "That is a published model — a proposal about the "
                    "structure rather than evidence gathered from a sample."},
            {"text": "Photo 51",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s11",
        "band": "standard",
        "text": "A model has the bases on the outside of the two strands. "
                "Which single piece of evidence does that choice contradict?",
        "options": [
            {"text": "Franklin's water measurements", "correct": True},
            {"text": "Photo 51", "correct": False,
             "why": "Photo 51 settles the number of strands, not where the "
                    "bases sit. A two-strand model still fits its width."},
            {"text": "Chargaff's base-ratio tables", "correct": False,
             "why": "Chargaff's ratios say how the bases pair up. They say "
                    "nothing about whether the bases face in or out."},
            {"text": "Pauling's triple helix", "correct": False,
             "why": "That is a published proposal rather than a measurement. "
                    "Either way, this model has two strands, so it is not the "
                    "one that proposal rules out."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s12",
        "band": "standard",
        "text": "A proposed model has three strands, the bases on the inside, "
                "and any base able to pair with any other. Tested against "
                "Photo 51, Chargaff's ratios, Franklin's water measurements "
                "and Pauling's published model, how many of the four does it "
                "fail, and which?",
        "options": [
            {"text": "One — only Photo 51, because of the number of strands",
             "correct": False,
             "why": "The pairing has been set to any base with any base, which "
                    "Chargaff's ratios also refuse. Two of the four fail."},
            {"text": "Two — Photo 51 and Chargaff's ratios", "correct": True},
            {"text": "Three — everything except Pauling's model",
             "correct": False,
             "why": "The water measurement passes, because the bases have been "
                    "put on the inside. Only two of the four fail."},
            {"text": "Four — every one of the four fails on a three-stranded "
                     "model",
             "correct": False,
             "why": "Three strands alone does not fail everything. The water "
                    "measurement and Pauling's model both pass this setting."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s13",
        "band": "standard",
        "text": "Why could Chargaff's ratios never have told anyone how many "
                "strands DNA has?",
        "options": [
            {"text": "Because he measured only one species, and a count of "
                     "strands needs many",
             "correct": False,
             "why": "He measured DNA from many species. The trouble is the "
                    "kind of measurement, not how many samples it covered."},
            {"text": "Because his measurements were taken before anyone "
                     "suspected DNA was important",
             "correct": False,
             "why": "They were published in 1950, six years after DNA was "
                    "shown to carry inherited information."},
            {"text": "Because they are amounts of chemicals, and a strand "
                     "count comes from a measured width",
             "correct": True},
            {"text": "Because the number of strands cannot be worked out from "
                     "any evidence at all",
             "correct": False,
             "why": "It was worked out, from the spacing of the spots in the "
                    "diffraction pattern. One kind of evidence could do it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s14",
        "band": "standard",
        "text": "A student says Franklin's images alone established the whole "
                "1953 model. Which feature of the model did they not "
                "establish?",
        "options": [
            {"text": "That the molecule is a helix",
             "correct": False,
             "why": "The cross-shaped pattern of spots is the signature of a "
                    "helix, so this is exactly what the images did show."},
            {"text": "How wide the molecule is",
             "correct": False,
             "why": "The spacing of the spots gave the width, and the width is "
                    "what settled the number of strands."},
            {"text": "That the phosphates lie on the outside",
             "correct": False,
             "why": "Franklin's water measurements settled that, and they are "
                    "hers as well. The images were not her only contribution."},
            {"text": "Which base pairs with which",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s15",
        "band": "standard",
        "text": "What does the spacing of the spots in a diffraction pattern "
                "give you?",
        "options": [
            {"text": "The amount of each of the four bases in the sample",
             "correct": False,
             "why": "Amounts of bases are chemistry, measured by Chargaff in "
                    "New York. A pattern of spots carries no such figure."},
            {"text": "The number of genes carried along the molecule",
             "correct": False,
             "why": "Nobody could count genes in 1952, and a diffraction "
                    "pattern would be no way to try."},
            {"text": "The width of the helix and the distance along it per "
                     "turn",
             "correct": True},
            {"text": "How much water the sample had taken up before the "
                     "exposure",
             "correct": False,
             "why": "The water content was a separate measurement. The spacing "
                    "of the spots is about the geometry of the molecule."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s16",
        "band": "standard",
        "text": "A proposed model fits three of the four pieces of evidence "
                "and fails the fourth. What follows?",
        "options": [
            {"text": "It is ruled out, and one of its decisions has to change",
             "correct": True},
            {"text": "It is accepted, since three out of four is a strong "
                     "majority of the evidence",
             "correct": False,
             "why": "Evidence is not voted on. One measurement a model "
                    "contradicts is enough to send it back."},
            {"text": "The fourth piece of evidence should be set aside as "
                     "unreliable",
             "correct": False,
             "why": "Throwing away the measurement that disagrees with you is "
                    "how a wrong model survives. The model has to change."},
            {"text": "Nothing follows until a better model has been proposed "
                     "to replace it",
             "correct": False,
             "why": "A model that contradicts a measurement is already ruled "
                    "out, whether or not a replacement is ready."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s17",
        "band": "standard",
        "text": "A model of DNA must choose between three strand numbers, two "
                "positions for the bases and two pairing rules. How many "
                "different models is that?",
        "options": [
            {"text": "7", "correct": False,
             "why": "This is 3 added to 2 added to 2. Choices that combine are "
                    "multiplied rather than added."},
            {"text": "12", "correct": True},
            {"text": "3", "correct": False,
             "why": "Three is the number of decisions, not the number of "
                    "models the decisions can produce between them."},
            {"text": "24", "correct": False,
             "why": "This is twice the true figure. Three multiplied by two "
                    "multiplied by two comes to twelve."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s18",
        "band": "standard",
        "text": "Why is a measurement of how much water DNA takes up evidence "
                "about the POSITION of its parts?",
        "options": [
            {"text": "Because water can only reach a molecule that has been "
                     "crystallised first",
             "correct": False,
             "why": "Taking up water is something the substance does in the "
                    "ordinary way. Crystallising is a separate preparation."},
            {"text": "Because the parts that attract water must be the ones "
                     "facing out into it",
             "correct": True},
            {"text": "Because a molecule that holds water must be hollow in "
                     "the middle",
             "correct": False,
             "why": "Nothing about the measurement says the middle is empty. "
                    "It says which parts are in contact with the water."},
            {"text": "Because water reacts with the bases and leaves them "
                     "damaged",
             "correct": False,
             "why": "No reaction is involved. The measurement is simply how "
                    "much water the substance takes up."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s19",
        "band": "standard",
        "text": "What was true of the way Rosalind Franklin and Maurice "
                "Wilkins worked together on DNA?",
        "options": [
            {"text": "They shared every result and published jointly "
                     "throughout",
             "correct": False,
             "why": "Their working relationship was difficult from the start, "
                    "which is part of why the episode is argued about."},
            {"text": "Their working relationship was difficult from the start",
             "correct": True},
            {"text": "They never met, because they worked in different "
                     "buildings",
             "correct": False,
             "why": "They were colleagues in the same laboratory. The "
                    "difficulty was in the working relationship itself."},
            {"text": "Wilkins worked for Franklin as her research student",
             "correct": False,
             "why": "Her research student was Raymond Gosling. Wilkins had "
                    "begun the X-ray work on DNA before Franklin arrived."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s20",
        "band": "standard",
        "text": "Why is it wrong to say that Chargaff discovered base pairing?",
        "options": [
            {"text": "Because his measurements were shown to be wrong when the "
                     "structure was worked out",
             "correct": False,
             "why": "His figures were right and are still right. They are one "
                    "of the three legs the model stands on."},
            {"text": "Because pairing was discovered before he started work on "
                     "the amounts of the bases",
             "correct": False,
             "why": "Nobody had proposed pairing before 1953. His tables came "
                    "first and the rule came out of them afterwards."},
            {"text": "Because he measured the equal amounts without proposing "
                     "what they meant",
             "correct": True},
            {"text": "Because the equal amounts were measured at King's rather "
                     "than in his own laboratory",
             "correct": False,
             "why": "The measurements are his, made in New York. What he did "
                    "not do is say what they implied."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s21",
        "band": "standard",
        "text": "The 1953 paper acknowledged only that its authors had been "
                "\"stimulated by\" unpublished results from King's. What is "
                "the objection to that wording?",
        "options": [
            {"text": "It should not have mentioned King's at all, since the "
                     "results were unpublished",
             "correct": False,
             "why": "Mentioning them is the least it could do. The complaint "
                    "is that it said far too little, not too much."},
            {"text": "It was wrong because the King's results turned out to be "
                     "mistaken",
             "correct": False,
             "why": "The King's measurements were correct, and the model had "
                    "to fit them. That is what makes the wording thin."},
            {"text": "It gave away results that Franklin had wanted to keep "
                     "secret",
             "correct": False,
             "why": "Nothing was published on her behalf. The objection runs "
                    "the other way: her work was used and barely credited."},
            {"text": "It understates work the model could not have been built "
                     "without, and names nobody",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s22",
        "band": "standard",
        "text": "How did Franklin's unpublished measurements reach Crick?",
        "options": [
            {"text": "She sent them to Cambridge herself, as a favour to a "
                     "colleague",
             "correct": False,
             "why": "She was not asked and did not send them. That is the "
                    "heart of the argument about the credit."},
            {"text": "They were published in a journal that Crick happened to "
                     "read",
             "correct": False,
             "why": "They were unpublished. Had they been in a journal there "
                    "would be nothing to argue about."},
            {"text": "Crick repeated her experiments in Cambridge and got the "
                     "same figures",
             "correct": False,
             "why": "Watson and Crick did no experiments on DNA at all. The "
                    "measurements came to them from elsewhere."},
            {"text": "Through a research council committee, without her being "
                     "asked",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s23",
        "band": "standard",
        "text": "Suppose Chargaff had never published his base ratios. Which "
                "part of the 1953 model would have had no evidence behind it?",
        "options": [
            {"text": "That there are two strands rather than one or three",
             "correct": False,
             "why": "The strand count came from the width measured in the "
                    "diffraction pattern, and would have survived."},
            {"text": "That the molecule is a helix",
             "correct": False,
             "why": "The cross-shaped pattern of spots showed that, and it has "
                    "nothing to do with chemical amounts."},
            {"text": "That A pairs with T and C pairs with G",
             "correct": True},
            {"text": "That the phosphates lie on the outside of the molecule",
             "correct": False,
             "why": "That rested on Franklin's water measurements, which are a "
                    "separate piece of evidence altogether."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s24",
        "band": "standard",
        "text": "Why is it wrong to call a diffraction pattern a picture of "
                "the molecule?",
        "options": [
            {"text": "Because the image is far too blurred for anyone to make "
                     "out the details of a molecule anywhere in it",
             "correct": False,
             "why": "Sharpness is not the point. Even a perfect pattern of "
                    "spots is a pattern rather than a likeness."},
            {"text": "Because the picture shows the fibre rather than a single "
                     "molecule inside it",
             "correct": False,
             "why": "The scattering does come from the molecules. What is "
                    "recorded is still not an image of one of them."},
            {"text": "Because the pattern is scattered X-rays whose geometry "
                     "has to be worked backwards to a structure",
             "correct": True},
            {"text": "Because the film records X-rays and the eye cannot see "
                     "X-rays directly",
             "correct": False,
             "why": "What we can or cannot see is beside the point. The "
                    "recording is a pattern, not a magnified likeness."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s25",
        "band": "standard",
        "text": "None of the four pieces of evidence — Photo 51, Chargaff's "
                "ratios, Franklin's water measurements, or Pauling's model — "
                "was gathered specifically to answer the question 'what is "
                "the structure of DNA?'. What does that tell you about how "
                "this discovery actually happened?",
        "options": [
            {"text": "Solving the structure meant bringing together evidence "
                     "that had been gathered for other reasons, not running "
                     "one experiment designed to reveal it directly",
             "correct": True},
            {"text": "It shows the evidence must have been unreliable, since "
                     "none of it was collected with the structure in mind",
             "correct": False,
             "why": "Being gathered for another purpose does not make "
                    "evidence unreliable. Chargaff's ratios and Franklin's "
                    "measurements were both accurate; they simply answered "
                    "narrower questions on their own."},
            {"text": "It means the 1953 model must have been a lucky guess "
                     "rather than a reasoned conclusion",
             "correct": False,
             "why": "Watson and Crick's model had to fit every piece of "
                    "existing evidence at once. A guess that happened to fit "
                    "four independent measurements is not what 'lucky' "
                    "describes."},
            {"text": "It proves that a structure can only be worked out once "
                     "a purpose-built experiment has produced a direct "
                     "picture of it",
             "correct": False,
             "why": "The opposite is closer to what happened here: the "
                    "structure was worked out by combining several indirect "
                    "pieces of evidence, none of which was a direct picture "
                    "of the finished structure on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s26",
        "band": "standard",
        "text": "Franklin calculated the molecule's width from her images. "
                "What would three strands have done to that width?",
        "options": [
            {"text": "Made it too narrow to match the measurement",
             "correct": False,
             "why": "Too narrow is what a single strand gives. Adding a third "
                    "strand pushes the width the other way."},
            {"text": "Left it unchanged, since the width is set by the bases",
             "correct": False,
             "why": "The bases set the width of each rung, but a third strand "
                    "adds a whole extra backbone to the molecule."},
            {"text": "Made it too wide to match the measurement",
             "correct": True},
            {"text": "Made no difference, because the width was measured on a "
                     "fibre rather than a molecule",
             "correct": False,
             "why": "The spacing of the spots gives the width of the molecule "
                    "itself, which is why it could settle the count."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s27",
        "band": "standard",
        "text": "Why did it matter that A equalled T in DNA from every "
                "organism measured, rather than in one species only?",
        "options": [
            {"text": "Because a rule that holds everywhere points to something "
                     "built into the structure itself",
             "correct": True},
            {"text": "Because a result found in one species is always a "
                     "measuring error",
             "correct": False,
             "why": "One species can give a perfectly sound result. What many "
                    "species add is that the rule is not a local accident."},
            {"text": "Because the ratio of A to C is the same in every species "
                     "as well",
             "correct": False,
             "why": "That ratio varies from species to species. It is the A "
                    "against T equality that holds everywhere."},
            {"text": "Because a structure can only be proposed once every "
                     "species has been measured",
             "correct": False,
             "why": "Nobody could measure every species. A rule holding across "
                    "many is enough to need explaining."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s28",
        "band": "standard",
        "text": "A student says the 1953 model was accepted because Watson and "
                "Crick worked at Cambridge. What is the reply?",
        "options": [
            {"text": "It was accepted because it fitted every measurement, and "
                     "Pauling's reputation did not save his model",
             "correct": True},
            {"text": "Cambridge had the only laboratory allowed to publish on "
                     "DNA at the time",
             "correct": False,
             "why": "There was no such restriction. King's, Columbia and "
                    "Pauling's laboratory were all publishing on it."},
            {"text": "The student is right, since the model was not tested "
                     "until years afterwards",
             "correct": False,
             "why": "It was tested against four pieces of evidence "
                    "immediately. That is what a model is built to face."},
            {"text": "Watson and Crick were unknown, so reputation cannot have "
                     "counted for anything at all",
             "correct": False,
             "why": "Their standing is beside the point either way. What "
                    "settled it was the fit to other people's measurements."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s29",
        "band": "standard",
        "text": "Put these in the order they happened: Photo 51, Chargaff's "
                "ratios, Pauling's triple-helix model.",
        "options": [
            {"text": "Photo 51, then Chargaff's ratios, then Pauling's model",
             "correct": False,
             "why": "Chargaff published in 1950, two years before Photo 51 was "
                    "taken. His figures came first of the three."},
            {"text": "Chargaff's ratios, then Photo 51, then Pauling's model",
             "correct": True},
            {"text": "Pauling's model, then Photo 51, then Chargaff's ratios",
             "correct": False,
             "why": "This is the order reversed. Pauling published early in "
                    "1953, last of the three."},
            {"text": "Chargaff's ratios, then Pauling's model, then Photo 51",
             "correct": False,
             "why": "Chargaff is rightly first, but Photo 51 was taken in 1952 "
                    "and Pauling's model came out in 1953."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-s30",
        "band": "standard",
        "text": "Why did the work in Cambridge need physical models at all, "
                "rather than an argument written down on paper?",
        "options": [
            {"text": "Because a model shows at once whether the pieces "
                     "actually fit together at the measured sizes",
             "correct": True},
            {"text": "Because a model can be shown to other scientists, and an "
                     "argument cannot",
             "correct": False,
             "why": "An argument is exactly what scientists send each other in "
                    "print. Building one tests it against real dimensions."},
            {"text": "Because the sizes of the atoms were not known well "
                     "enough to be used in an argument",
             "correct": False,
             "why": "Those sizes were known, and they are what made the models "
                    "worth building to scale in the first place."},
            {"text": "Because a physical model counts as an experiment on DNA",
             "correct": False,
             "why": "It does not. Watson and Crick did no experiments on DNA, "
                    "which is what makes the model building their "
                    "contribution."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h11",
        "band": "harder",
        "text": "In a DNA sample, A makes up 30 per cent of the bases. What "
                "percentage is G?",
        "options": [
            {"text": "30 per cent",
             "correct": False,
             "why": "30 is the share of T, because T is A's partner. G is "
                    "worked out from what is left over."},
            {"text": "20 per cent",
             "correct": True},
            {"text": "40 per cent",
             "correct": False,
             "why": "40 is the share of C and G together. They are equal to "
                    "each other, so each takes half of it."},
            {"text": "70 per cent",
             "correct": False,
             "why": "This is everything that is not A, which lumps T in with C "
                    "and G. T is fixed at 30 by the pairing rule."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h12",
        "band": "harder",
        "text": "DNA was first isolated in 1869 and its structure published in "
                "1953. How long was the gap, and what does it tell you?",
        "options": [
            {"text": "84 years, which shows the 1869 work must have been "
                     "unreliable",
             "correct": False,
             "why": "Miescher's isolation was sound and stood. The delay was "
                    "in finding out what the substance was for."},
            {"text": "94 years, and the gap is explained by the two world wars",
             "correct": False,
             "why": "1953 take away 1869 is 84. The arithmetic matters before "
                    "any explanation of it does."},
            {"text": "74 years, which is roughly how long a scientific "
                     "question of this kind usually takes to answer",
             "correct": False,
             "why": "The subtraction gives 84, and there is no usual length "
                    "for a scientific question."},
            {"text": "84 years, and a substance can be known long before "
                     "anyone knows what it is or does",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h13",
        "band": "harder",
        "text": "Why did the argument need four pieces of evidence rather than "
                "one very good one?",
        "options": [
            {"text": "Because a single measurement is never trusted until "
                     "three others agree with it",
             "correct": False,
             "why": "These four measure different things rather than checking "
                    "each other. Repetition is not what they are doing."},
            {"text": "Because the four pieces came from four laboratories, and "
                     "that is what makes a result official",
             "correct": False,
             "why": "Where evidence comes from is not what gives it force. "
                    "What matters is what each piece eliminates."},
            {"text": "Because the evidence had to cover every base, and there "
                     "are four of those",
             "correct": False,
             "why": "The four pieces of evidence have nothing to do with the "
                    "four bases. One of them covers the pairing of all of "
                    "them."},
            {"text": "Because each piece rules out only some of the possible "
                     "models, and only together do they leave one",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h14",
        "band": "harder",
        "text": "Suppose a new and better measurement had shown the molecule "
                "to be twice as wide as Franklin's figure. Which decision "
                "would have had to be reconsidered?",
        "options": [
            {"text": "How many strands the molecule has",
             "correct": True},
            {"text": "Whether A pairs with T",
             "correct": False,
             "why": "The pairing rule rests on the equal amounts Chargaff "
                    "measured, and a change of width leaves those untouched."},
            {"text": "Whether the molecule is a helix at all",
             "correct": False,
             "why": "The cross-shaped pattern shows a helix whatever its "
                    "width. A wider helix is still a helix."},
            {"text": "Whether DNA carries inherited information",
             "correct": False,
             "why": "That was settled in 1944 by an entirely different kind of "
                    "experiment, and no width measurement touches it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h15",
        "band": "harder",
        "text": "A student says the cross-shaped pattern on Photo 51 proved "
                "DNA is a double helix. How much of that is right?",
        "options": [
            {"text": "All of it, since a cross is the signature of two strands "
                     "crossing over",
             "correct": False,
             "why": "The cross is the signature of a helix, and a helix of one "
                    "or three strands gives one too."},
            {"text": "None of it, since the cross tells you nothing about the "
                     "shape of the molecule",
             "correct": False,
             "why": "It tells you a great deal: the molecule is helical. What "
                    "it does not carry is the number of strands."},
            {"text": "The cross gives the helix; the number of strands came "
                     "from the measured width",
             "correct": True},
            {"text": "The cross gives the number of strands; the helix came "
                     "from the water measurements",
             "correct": False,
             "why": "This has the two the wrong way round, and the water work "
                    "settled a third thing again — where the phosphates sit."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h16",
        "band": "harder",
        "text": "Imagine a model in which A pairs with T but C pairs with "
                "another C. What two things would go wrong with it?",
        "options": [
            {"text": "Nothing would go wrong, because C and C are the same "
                     "size as each other",
             "correct": False,
             "why": "Being the same size is the trouble. Two small bases make "
                    "a rung narrower than the A-with-T rungs beside it."},
            {"text": "The C rungs would come out too wide, and the amount of "
                     "G measured in every organism would have to rise",
             "correct": False,
             "why": "C is a small base, so two of them pinch rather than "
                    "bulge, and G would be left with no partner at all."},
            {"text": "The C rungs would pinch, and there would be no reason "
                     "for C and G to be measured in equal amounts",
             "correct": True},
            {"text": "The molecule could not form a helix at all with that "
                     "pairing rule",
             "correct": False,
             "why": "It could still wind into a helix. What it could not do is "
                    "keep the constant width the diffraction pattern shows."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h17",
        "band": "harder",
        "text": "Chargaff's tables could not have given the molecule's width, "
                "and Photo 51 could not have given the base amounts. What does "
                "that show about evidence?",
        "options": [
            {"text": "That one of the two methods must have been badly chosen "
                     "for the problem",
             "correct": False,
             "why": "Both were well chosen. Each simply answers its own "
                    "question, which is why the model needed both."},
            {"text": "That chemical measurements are always weaker evidence "
                     "than images",
             "correct": False,
             "why": "Chargaff's chemistry carried the pairing rule, which no "
                    "image could have supplied. Neither outranks the other."},
            {"text": "That no measurement can be trusted until a second, "
                     "completely different method has been used to produce "
                     "the same answer",
             "correct": False,
             "why": "These two do not give the same answer, and were never "
                    "meant to. They answer different questions."},
            {"text": "That a measurement answers the question it was designed "
                     "to answer, and different questions need different "
                     "methods",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h18",
        "band": "harder",
        "text": "Meselson and Stahl's 1958 experiment confirmed that DNA is "
                "copied in the way the structure suggested. Suppose it had "
                "come out the other way. What would have followed?",
        "options": [
            {"text": "The structure would have been overturned along with the "
                     "copying idea",
             "correct": False,
             "why": "The structure rests on its own four pieces of evidence. A "
                    "copying result does not reach back and undo them."},
            {"text": "The structure could still stand, but the copying "
                     "suggestion would have needed rethinking",
             "correct": True},
            {"text": "Nothing at all, since the copying idea had never been "
                     "more than a guess",
             "correct": False,
             "why": "It was the paper's most striking claim and the reason the "
                    "structure mattered so much. A result against it would "
                    "have counted."},
            {"text": "The 1962 Nobel Prize would have been awarded to Meselson "
                     "and Stahl instead",
             "correct": False,
             "why": "Prizes are not what the question is about. The scientific "
                    "consequence is what a failed prediction costs."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h19",
        "band": "harder",
        "text": "A student says the 1953 model was a lucky guess that happened "
                "to be right. What is the strongest objection?",
        "options": [
            {"text": "Guessing is never part of science, so the description "
                     "cannot be right",
             "correct": False,
             "why": "Proposing a model always involves a leap. What stops this "
                    "one being a guess is the evidence it had to survive."},
            {"text": "They had seen the answer in Franklin's images before "
                     "they built anything",
             "correct": False,
             "why": "No image shows the answer. The images carried "
                    "measurements, which still had to be reasoned from."},
            {"text": "Every feature of it was forced by somebody's "
                     "measurement, and it was the only combination left "
                     "standing",
             "correct": True},
            {"text": "A guess would have taken a great deal less time than "
                     "the two years of work the model actually took to build",
             "correct": False,
             "why": "How long something takes does not settle what kind of "
                    "reasoning it was. The evidence does."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h20",
        "band": "harder",
        "text": "A team today proposes a shape for a molecule nobody can see. "
                "Which approach follows the method used in 1953?",
        "options": [
            {"text": "Wait until a microscope powerful enough to show the "
                     "molecule has been built",
             "correct": False,
             "why": "No such microscope exists even now for a single molecule. "
                    "Waiting would have meant never answering the question."},
            {"text": "Choose the shape that most other scientists in the field "
                     "already expect",
             "correct": False,
             "why": "The most respected chemist alive expected a triple helix "
                    "and was wrong. Expectation is not evidence."},
            {"text": "Build a model and test it against every existing "
                     "measurement, dropping it if one fails",
             "correct": True},
            {"text": "Repeat every earlier measurement before proposing any "
                     "shape at all",
             "correct": False,
             "why": "Watson and Crick repeated none of them. Using other "
                    "people's measurements is what model building is for."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h21",
        "band": "harder",
        "text": "Given that Photo 51 existed in 1952, why was a three-stranded "
                "model still a serious proposal in early 1953?",
        "options": [
            {"text": "Because a triple helix explains the base ratios better "
                     "than two strands do",
             "correct": False,
             "why": "The ratios point to pairing, which needs two strands. "
                    "They are evidence against a triple helix, not for it."},
            {"text": "Because the image had been published, and its width had "
                     "been read as allowing three",
             "correct": False,
             "why": "The image was not published. That is precisely why "
                    "someone outside King's could still propose three."},
            {"text": "Because Pauling was working without that image, and the "
                     "width measurement it carried",
             "correct": True},
            {"text": "Because three strands were needed to explain how much "
                     "water the molecule takes up",
             "correct": False,
             "why": "The water measurement is about which parts face outwards. "
                    "It says nothing about how many strands there are."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h22",
        "band": "harder",
        "text": "Suppose all four bases had turned out to be present in equal "
                "amounts in every organism. What could Chargaff's data have "
                "shown then?",
        "options": [
            {"text": "That every base pairs with itself, since the amounts all "
                     "match",
             "correct": False,
             "why": "Equal amounts all round are consistent with self-pairing "
                    "and with any other rule, so they would show none of them."},
            {"text": "Nothing about which base pairs with which",
             "correct": True},
            {"text": "That the four bases are really the same substance under "
                     "four names",
             "correct": False,
             "why": "They are four different chemicals whatever their amounts. "
                    "Quantity does not settle identity."},
            {"text": "That the molecule must have four strands rather than two",
             "correct": False,
             "why": "Strand number comes from the measured width. Amounts of "
                    "bases could not reach that question either."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h23",
        "band": "harder",
        "text": "Pauling's published model was wrong in two ways at once. "
                "Which two?",
        "options": [
            {"text": "It had three strands, and it put the bases on the "
                     "outside",
             "correct": True},
            {"text": "It had three strands, and it paired A with G rather than "
                     "with T",
             "correct": False,
             "why": "The strand count is right, but his model's other error "
                    "was about where the parts sat, not about pairing."},
            {"text": "It had one strand, and it put the phosphates on the "
                     "outside",
             "correct": False,
             "why": "Both halves are wrong. His model had three strands, and "
                    "phosphates on the outside is what the real one has."},
            {"text": "It had two strands, and it made the molecule far too "
                     "narrow",
             "correct": False,
             "why": "Two strands is the correct answer, which his model did "
                    "not give. Three strands is too wide, not too narrow."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h24",
        "band": "harder",
        "text": "Watson and Crick did no experiments on DNA. Why does that not "
                "mean they did no work?",
        "options": [
            {"text": "Because they had done experiments on other substances "
                     "earlier in their careers",
             "correct": False,
             "why": "Earlier work elsewhere is not what earned them credit "
                    "here. The work in question is the model building."},
            {"text": "Because they gathered the measurements together from "
                     "all the different laboratories that had produced them",
             "correct": False,
             "why": "Fetching figures is not the work either, and one set "
                    "reached them without being asked for."},
            {"text": "Because they built and rebuilt physical models until one "
                     "fitted every measurement anyone had made",
             "correct": True},
            {"text": "Because writing a paper is itself a form of experiment",
             "correct": False,
             "why": "Writing is not experimenting. What they did that counts "
                    "was to test proposed structures against real numbers."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h25",
        "band": "harder",
        "text": "If DNA had turned out to be single-stranded, what would have "
                "been lost from the closing suggestion of the 1953 paper?",
        "options": [
            {"text": "Nothing, because a single strand carries the same "
                     "sequence of bases",
             "correct": False,
             "why": "The sequence would indeed be there. What would be missing "
                    "is anything to copy it against."},
            {"text": "The helix, because a single strand cannot form one",
             "correct": False,
             "why": "A single strand can perfectly well be helical. The bench "
                    "offers one strand as a live option for that reason."},
            {"text": "The copying mechanism, which needs a partner strand to "
                     "specify what is built",
             "correct": True},
            {"text": "The base pairing rule, because A and T would no longer "
                     "be different sizes",
             "correct": False,
             "why": "The bases keep their sizes whatever the strand count. "
                    "What they would lose is anything to pair with."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h26",
        "band": "harder",
        "text": "A student says the structure was only an opinion until "
                "Meselson and Stahl tested the copying in 1958. What is wrong "
                "with that?",
        "options": [
            {"text": "The 1958 experiment tested the structure itself, so the "
                     "student has the wrong date",
             "correct": False,
             "why": "The 1958 work tested the copying rather than the "
                    "structure. The date is right and the reasoning is not."},
            {"text": "Nothing is wrong: no model counts for anything until a "
                     "separate experiment has confirmed it in the laboratory",
             "correct": False,
             "why": "On that rule the model could never have been published, "
                    "and the four pieces of evidence would count for nothing."},
            {"text": "The structure had been seen directly by then, so no "
                     "confirmation was needed",
             "correct": False,
             "why": "Nobody has ever seen a DNA molecule. Direct observation "
                    "was never available at any point in this story."},
            {"text": "It was already the only model surviving four independent "
                     "pieces of evidence, which is not an opinion",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h27",
        "band": "harder",
        "text": "Suppose Franklin had never measured how much water DNA takes "
                "up. Which feature of the model would then have had no "
                "evidence behind it?",
        "options": [
            {"text": "That the molecule is a helix",
             "correct": False,
             "why": "The cross-shaped pattern of spots carries that, and it is "
                    "a separate piece of evidence from the water work."},
            {"text": "That there are two strands rather than three",
             "correct": False,
             "why": "The strand count came from the width read off the "
                    "spacing of the spots in the diffraction pattern."},
            {"text": "That A pairs with T and C pairs with G",
             "correct": False,
             "why": "That came from Chargaff's base ratios, measured in New "
                    "York years before."},
            {"text": "That the bases are inside and the phosphates outside",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h28",
        "band": "harder",
        "text": "A school poster reads \"In 1953 Rosalind Franklin discovered "
                "the double helix.\" What is the most accurate correction?",
        "options": [
            {"text": "Franklin had no part in the double helix, which was "
                     "worked out from first principles in a laboratory in "
                     "Cambridge",
             "correct": False,
             "why": "That swings too far the other way. Her measurements are "
                    "what the model was built to fit."},
            {"text": "The date is the only error, since the work was actually "
                     "done in 1952",
             "correct": False,
             "why": "Photo 51 was taken in 1952 and the structure published in "
                    "1953. The date is not what the poster gets wrong."},
            {"text": "It should say Wilkins rather than Franklin, since he "
                     "shared the Nobel Prize",
             "correct": False,
             "why": "Swapping one name for another keeps the same mistake. The "
                    "poster confuses producing evidence with building a model."},
            {"text": "Franklin produced the images and measurements the model "
                     "had to fit; Watson and Crick built the model itself",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h29",
        "band": "harder",
        "text": "Pauling's model and the 1953 model were both built rather "
                "than measured. Why did only one of them survive?",
        "options": [
            {"text": "Because only one of them fitted every measurement it was "
                     "tested against",
             "correct": True},
            {"text": "Because only one of them was built by people who had "
                     "done their own experiments",
             "correct": False,
             "why": "Neither team experimented on DNA. Watson and Crick did "
                    "none at all, which makes this no way to tell them apart."},
            {"text": "Because only one of them was published in a scientific "
                     "journal",
             "correct": False,
             "why": "Pauling published his early in 1953, which is how it came "
                    "to narrow the field for everybody else."},
            {"text": "Because only one of them was built to scale out of "
                     "metal and cardboard",
             "correct": False,
             "why": "How a model is made is not what decides it. What decides "
                    "it is whether the measurements agree."},
        ],
        "figure": None,
    },
    {
        "id": "b10-03-h30",
        "band": "harder",
        "text": "Twelve models are possible in all. Photo 51 permits only one "
                "of the three strand numbers. How much of the field does that "
                "one piece of evidence remove?",
        "options": [
            {"text": "One third of it", "correct": False,
             "why": "One of the three strand numbers survives, so two of the "
                    "three are cut. What goes is two thirds."},
            {"text": "One twelfth of it", "correct": False,
             "why": "A single model out of twelve is what survives all four "
                    "pieces of evidence together, not what one of them "
                    "removes."},
            {"text": "All of it except Pauling's model", "correct": False,
             "why": "Pauling's model has three strands, so it is among the "
                    "ones this piece of evidence removes rather than the one "
                    "it leaves."},
            {"text": "Two thirds of it", "correct": True},
        ],
        "figure": None,
    },
]
