"""C3 lesson 01 — Pure or mixture?: twelve questions (MRB-269).

The lesson's argument is that one question decides every case — is there one
substance in there, or more than one — and that none of the eight samples on
the bench was settled by looking at it. These twelve probe that argument from
the angles the mastery ladder leaves alone. The ladder asks for the definition,
picks the pure one out of four, and takes the filtered sea water and the
mineral-water label apart; the bank works on the two invisible samples, the
three that look uniform and are not, the composition-can-vary test, and the
word `impurity`.

The distractors are built from the lesson's two declared misconceptions.
MIX-01 (pure means clean, natural or with nothing added) drives the wrong
options in e01, e03, e04, s01, s03, h01, h03 and h04 — every one of them
treats cleanliness, naturalness, or a promise about what was put in as the
test. MIX-02 (if it looks the same all the way through, it is pure) drives
e01, e02, e03, s01, s02, h01, h02 and h03, in each of its three costumes:
uniform-looking, clear, and invisible.

A third strand runs through the bank and is not in the register, because it is
not a wrong idea so much as a missing one: the composition test. A pure
substance's recipe cannot be adjusted and a mixture's can, so s01, s02 and h02
each carry a distractor that treats an adjustable recipe as a fixed one, or
reads a deliberately chosen proportion as evidence of purity.

Two items — e02 and h01 — offer the RIGHT VERDICT with the wrong reason, and
their stems ask for the verdict and the reason together. Getting the right
answer for the wrong reason is the failure this lesson is built to catch: it
survives the gold ring and falls over on the very next sample.
"""

UNIT = "C3"
LESSON = "pure-or-mixture"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c3-01-e01",
        "band": "easier",
        "text": "What does a chemist mean by a mixture?",
        "options": [
            {"text": "Any substance that has had something unwanted or dirty "
                     "put into it", "correct": False,
             "why": "That is the everyday meaning and it is not the test. An "
                    "impurity can be perfectly clean, and milk has had "
                    "nothing put into it at all."},
            {"text": "Any substance you can see two or more different things "
                     "in", "correct": False,
             "why": "The gold ring, the milk and the juice all look "
                    "completely uniform and all three are mixtures. Looking "
                    "settles nothing either way."},
            {"text": "Two or more substances together that are not chemically "
                     "joined", "correct": True},
            {"text": "Any substance that has been made in a factory rather "
                     "than found in nature", "correct": False,
             "why": "Sea water is natural and is a mixture; sugar is refined "
                    "in a factory and is pure. Where it came from is not the "
                    "test."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e02",
        "band": "easier",
        "text": "A 9-carat gold ring is uniform, shiny and gold-coloured all "
                "the way through. Which verdict and reason are BOTH right?",
        "options": [
            {"text": "A mixture — only 37.5% of it is gold and the rest is "
                     "copper and silver", "correct": True},
            {"text": "A mixture — you can see the copper in it if you look "
                     "closely enough", "correct": False,
             "why": "Right verdict, wrong reason, and the reason is the one "
                    "that matters: you cannot see the copper. The ring looks "
                    "completely uniform, which is exactly why looking cannot "
                    "decide it."},
            {"text": "Pure — it is the same all the way through, with no bits "
                     "you can pick out", "correct": False,
             "why": "Milk and orange juice are uniform too, and both are "
                    "mixtures. Looking the same throughout is no evidence of "
                    "purity."},
            {"text": "Pure — nothing has been put into it that should not be "
                     "there", "correct": False,
             "why": "The copper and silver are meant to be there — that is "
                    "why the ring lasts. Meaning to add something does not "
                    "stop the result being a mixture."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e03",
        "band": "easier",
        "text": "Oxygen from a cylinder and the air in the room are both "
                "completely invisible. Which one is pure?",
        "options": [
            {"text": "Both of them — there is nothing to see in either, so "
                     "there is nothing else in there", "correct": False,
             "why": "Being invisible tells you nothing about purity. Two "
                    "invisible samples, two different answers — that is the "
                    "whole reason both are on the bench."},
            {"text": "The oxygen — the cylinder holds one substance and the "
                     "air holds several", "correct": True},
            {"text": "The air — it is natural, and nothing has been put into "
                     "it by anybody", "correct": False,
             "why": "Air is nitrogen, oxygen, argon, carbon dioxide and water "
                    "vapour, and the proportions change with where you are "
                    "standing. Natural is not the test."},
            {"text": "Neither of them — a gas is too spread out to count as "
                     "pure", "correct": False,
             "why": "How spread out the particles are has nothing to do with "
                    "it. A cylinder of oxygen holds one substance, and that "
                    "is what pure means."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e04",
        "band": "easier",
        "text": "What does a chemist mean by an impurity?",
        "options": [
            {"text": "Dirt, or anything in the sample that would make it "
                     "unsafe", "correct": False,
             "why": "An impurity is not the same as dirt and can be perfectly "
                    "clean. Water in a bottle of ethanol is an impurity and "
                    "there is nothing dirty about it."},
            {"text": "Something added to the sample on purpose while it was "
                     "being made", "correct": False,
             "why": "An impurity may have been there all along. Orange juice "
                    "has had nothing added to it and is full of substances "
                    "that are not orange juice."},
            {"text": "A part of the sample that looks different from the rest "
                     "of it", "correct": False,
             "why": "The copper in a gold ring cannot be picked out by eye "
                    "and it is still not gold. What an impurity looks like is "
                    "not what makes it one."},
            {"text": "Anything present that is not the substance you wanted",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c3-01-s01",
        "band": "standard",
        "text": "The Dead Sea is about nine times saltier than the Atlantic, "
                "and both of them are sea water. What does that establish?",
        "options": [
            {"text": "Sea water is a mixture — its composition can be varied "
                     "and a pure substance's cannot", "correct": True},
            {"text": "Nothing either way — both samples are clear and "
                     "colourless, so there is nothing to go on",
             "correct": False,
             "why": "Being clear settles nothing, but the saltiness is not "
                    "about looking. A composition that varies from place to "
                    "place is the evidence, and it is decisive."},
            {"text": "Dead Sea water is impure and Atlantic water is pure, "
                     "because there is far less in it", "correct": False,
             "why": "Both are mixtures. How much of the other substance there "
                    "is does not decide it — one substance or more than one "
                    "does, and both of these hold several."},
            {"text": "Dead Sea water has had extra salt put into it, which is "
                     "what makes it a mixture", "correct": False,
             "why": "Nobody put anything in; the Dead Sea is saltier because "
                    "of where it sits and how it evaporates. Both samples "
                    "were mixtures before anyone touched them."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s02",
        "band": "standard",
        "text": "Milk is uniform white with no bits you can pick out. Left "
                "standing in a jug overnight, the cream rises to the top. "
                "What does the cream rising tell you?",
        "options": [
            {"text": "Nothing about purity — it looked uniform to start with, "
                     "and that is the test", "correct": False,
             "why": "Looking uniform was never the test. The cream separating "
                    "out is the evidence, and it is evidence no pure "
                    "substance could ever give."},
            {"text": "It was pure in the jug and became a mixture once the "
                     "cream rose", "correct": False,
             "why": "Nothing changed in the jug overnight. The fats were "
                    "there the whole time — standing still only made them "
                    "easy to see."},
            {"text": "It is pure, because nothing was added — the cream was "
                     "in there all along", "correct": False,
             "why": "The cream being in there all along is exactly what makes "
                    "milk a mixture. Nothing needed adding for there to be "
                    "more than one substance."},
            {"text": "It is a mixture — no pure substance ever separates out "
                     "on standing", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s03",
        "band": "standard",
        "text": "Granulated sugar is refined in a factory until nothing but "
                "sucrose is left. Sea water comes straight out of the sea. "
                "Which of the two is pure?",
        "options": [
            {"text": "The sea water — it is natural, and the sugar has been "
                     "through a factory", "correct": False,
             "why": "Being natural is not the test. Sea water holds sodium "
                    "chloride and several other salts, and a factory is "
                    "exactly the place something gets refined down to one "
                    "substance."},
            {"text": "The sugar — it is one substance, and where it was made "
                     "is not the test", "correct": True},
            {"text": "Both of them — nothing has been added to either one",
             "correct": False,
             "why": "Nothing has to be added for a sample to hold more than "
                    "one substance. The salts in sea water were there before "
                    "anybody arrived."},
            {"text": "Neither of them — nothing is ever completely pure",
             "correct": False,
             "why": "Distilled water, oxygen from a cylinder and this sugar "
                    "are all one substance. Saying nothing is ever pure gives "
                    "up on a question that has an answer."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s04",
        "band": "standard",
        "text": "Pure sodium will set fire to your hand. Distilled water is "
                "pure and tastes of nothing at all. What do those two facts "
                "together show about the word pure?",
        "options": [
            {"text": "It says how many substances are in the sample, and "
                     "nothing about whether it is good for you",
             "correct": True},
            {"text": "It says the sample is clean, which is not quite the "
                     "same thing as saying it is safe", "correct": False,
             "why": "Purity is not about cleanliness either. Sea water can be "
                    "crystal clear and is a mixture; a lump of pure sodium "
                    "kept under oil is filthy and is pure."},
            {"text": "It shows that pure substances are usually more "
                     "dangerous than the mixtures they came from",
             "correct": False,
             "why": "There is no such rule. Distilled water is pure and "
                    "harmless; petrol is a mixture and will burn your house "
                    "down."},
            {"text": "It shows that the word means something different every "
                     "time a chemist happens to use it", "correct": False,
             "why": "In chemistry it means one thing every time — one "
                    "substance and nothing else. It is the food label that "
                    "uses it for something else."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c3-01-h01",
        "band": "harder",
        "text": "Two silver-coloured spoons look identical. One is pure "
                "silver; the other is sterling silver, which is 92.5% silver "
                "and 7.5% copper. Which statement gets both the verdict and "
                "the reason right?",
        "options": [
            {"text": "Both spoons are pure — each is uniform silver-coloured "
                     "metal the whole way through", "correct": False,
             "why": "Uniform is what the gold ring looked like as well. Being "
                    "the same all through is not evidence of one substance, "
                    "however convincing it is."},
            {"text": "The sterling spoon is a mixture, and you would know by "
                     "spotting the copper in it", "correct": False,
             "why": "Right verdict, and a reason that would fail on the next "
                    "sample. The copper cannot be spotted — that is precisely "
                    "why the two spoons look identical."},
            {"text": "One spoon is pure, and no amount of looking will say "
                     "which — the test is how many substances are in it",
             "correct": True},
            {"text": "The sterling spoon is pure too, because the copper is "
                     "meant to be there and nothing unwanted was added",
             "correct": False,
             "why": "Meaning to add the copper does not un-add it. Sterling "
                    "silver is a mixture on purpose, in the same way and for "
                    "the same reason as a 9-carat gold ring."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h02",
        "band": "harder",
        "text": "A diver's cylinder holds a breathing gas of 32% oxygen and "
                "68% nitrogen. A second cylinder holds nitrogen only. Both "
                "were filled in the same factory and both are invisible. "
                "Which is pure?",
        "options": [
            {"text": "Neither can be decided — you cannot see inside either "
                     "cylinder, so there is nothing to go on", "correct": False,
             "why": "Invisible samples are decided the same way as every "
                    "other one: by how many substances are in there. Oxygen "
                    "is invisible and pure, and air is invisible and is not."},
            {"text": "The nitrogen cylinder — it holds one substance, and the "
                     "breathing gas holds two", "correct": True},
            {"text": "The breathing gas — it was made to an exact recipe, so "
                     "its composition is fixed", "correct": False,
             "why": "The recipe was chosen, and a diver can order 36% oxygen "
                    "instead. A proportion somebody can change is the "
                    "signature of a mixture, not of a pure substance."},
            {"text": "Both of them — a gas straight from a cylinder has had "
                     "nothing added to it", "correct": False,
             "why": "The breathing gas is two gases put together on purpose. "
                    "Nothing needing to be added afterwards does not make a "
                    "sample one substance."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h03",
        "band": "harder",
        "text": "A tanker of drinking water is treated until every bacterium "
                "and every speck of dirt has gone. A chemist tests it and "
                "calls it a mixture. Is the chemist wrong?",
        "options": [
            {"text": "Yes — nothing unwanted is left in it, so there is "
                     "nothing there to make it a mixture", "correct": False,
             "why": "Wanted and unwanted is the label's question, not the "
                    "chemist's. The dissolved minerals are wanted, and they "
                    "are still two or more substances."},
            {"text": "Yes — the water is completely clear, so there is only "
                     "one substance left in it", "correct": False,
             "why": "Clear means no undissolved bits. Sea water is clear "
                    "too, and everything dissolved in it is still there."},
            {"text": "No — but only because water can never be got "
                     "completely pure", "correct": False,
             "why": "Water can be got pure: the distilled water on the bench "
                    "is one substance. What makes this tanker a mixture is "
                    "what is dissolved in it, not an impossibility."},
            {"text": "No — the dissolved minerals are still in it, and "
                     "cleanliness was never the test", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h04",
        "band": "harder",
        "text": "A painkiller is sold at 99.9% purity, with the missing 0.1% "
                "named and limited on the packet. A carton of juice is sold "
                "as 100% pure and names nothing. Which is a claim about "
                "composition?",
        "options": [
            {"text": "The painkiller's — it says what fraction of the sample "
                     "is the substance itself", "correct": True},
            {"text": "The juice's — 100% is a larger figure than 99.9%, so it "
                     "is the stronger claim", "correct": False,
             "why": "The two figures are not measuring the same thing. The "
                    "juice's 100% is about how much was added, which is none, "
                    "and it says nothing at all about what is in there."},
            {"text": "Both of them — pure means the same thing wherever it is "
                     "written down", "correct": False,
             "why": "One word, two meanings, and only one of them is "
                    "chemistry. On food, pure means nothing was added; in a "
                    "laboratory it means one substance is there."},
            {"text": "Neither of them — a purity figure is advertising rather "
                     "than chemistry", "correct": False,
             "why": "The painkiller's figure is measured, checked and legally "
                    "limited, because a tablet is swallowed by somebody who "
                    "cannot inspect it. That one is chemistry."},
        ],
        "figure": None,
    },
]
