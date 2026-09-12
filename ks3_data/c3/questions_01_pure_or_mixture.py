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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-01-e05",
        "band": "easier",
        "text": "What does a chemist mean by the composition of a sample?",
        "options": [
            {
             "text": "What it is made of, and how much of each",
             "correct": True,
            },
            {
             "text": "How much of it there is, in grams",
             "correct": False,
             "why": "That is a mass. A litre of sea water and a spoonful of it have the same composition",
            },
            {
             "text": "Whether it has anything dirty or harmful in it",
             "correct": False,
             "why": "That is a safety judgement. Pure sodium is clean and will set fire to your hand",
            },
            {
             "text": "Where the sample came from originally",
             "correct": False,
             "why": "Origin is never the test. Factory sugar is pure and natural sea water is not",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e06",
        "band": "easier",
        "text": "Road salt is deliberately not pure sodium chloride. What "
                "does that tell you about the word pure?",
        "options": [
            {"text": "That a mixture is never as good as the pure substance "
                     "would be if you could afford to buy enough of it",
             "correct": False,
             "why": "Road salt is a mixture BECAUSE the mixture works better. "
                    "Pure is not a quality rating"},
            {"text": "That being pure is not always what you want",
             "correct": True},
            {"text": "That road salt has been contaminated on the way to the "
                     "depot",
             "correct": False,
             "why": "Nothing went wrong. What is in it was put there on "
                    "purpose"},
            {"text": "That sodium chloride cannot be made pure",
             "correct": False,
             "why": "It can, and the salt in a laboratory is. It is not worth "
                    "the cost for a road"},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e07",
        "band": "easier",
        "text": "Pure gold is soft enough to mark with a fingernail. What is "
                "done about that when a ring is made?",
        "options": [
            {"text": "It is hammered for a long time, which is what hardens a "
                     "soft metal without anything having to be added to it",
             "correct": False,
             "why": "Hammering helps a little and wears off. A ring is hard "
                    "because other metals were added to the gold"},
            {"text": "It is cooled to make it harder",
             "correct": False,
             "why": "A ring is worn at room temperature and would be soft "
                    "again at once. The hardness comes from the mixture"},
            {"text": "Other metals are added on purpose",
             "correct": True},
            {"text": "It is purified further, since a purer gold is harder",
             "correct": False,
             "why": "The opposite. The purer the gold, the softer it is"},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e08",
        "band": "easier",
        "text": "A carton says 100% pure orange juice. What is that "
                "sentence claiming?",
        "options": [
            {"text": "That the juice contains only one substance",
             "correct": False,
             "why": "Juice holds water, sugars, acids and dozens of other "
                    "substances. No drink you can buy is one substance"},
            {"text": "That it is safe to drink and has been tested",
             "correct": False,
             "why": "Safety is a different claim, made in a different place "
                    "on the packaging"},
            {"text": "That it is safe to drink",
             "correct": False,
             "why": "Juice varies with the fruit. A fixed composition is what "
                    "a PURE substance has"},
            {"text": "That nothing has been added to it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c3-01-s05",
        "band": "standard",
        "text": "Steel is iron with a little carbon added, and the amount of "
                "carbon is chosen by the steelmaker. Pure or mixture?",
        "options": [
            {"text": "Mixture, and deliberately so",
             "correct": True},
            {"text": "Pure, because both iron and carbon are elements and "
                     "nothing else has been allowed into it",
             "correct": False,
             "why": "Two substances in one sample is a mixture, whether or "
                    "not each of them is an element"},
            {"text": "Pure, because it is uniform all the way through",
             "correct": False,
             "why": "Uniform appearance is the evidence that has failed in "
                    "every lesson of this unit"},
            {"text": "Mixture, because the carbon was an accident of "
                     "smelting",
             "correct": False,
             "why": "The verdict is right and the reason is not. The carbon "
                    "is put in on purpose, to a chosen amount"},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s06",
        "band": "standard",
        "text": "Two bottles of clear colourless liquid: one is distilled "
                "water, the other is tap water filtered until nothing can be "
                "seen in it. Which is pure?",
        "options": [
            {"text": "The filtered tap water, because filtering removes "
                     "everything that was in it and leaves only the water "
                     "behind",
             "correct": False,
             "why": "Filtering removes what is not dissolved. Everything "
                    "dissolved goes straight through the paper"},
            {"text": "The distilled water",
             "correct": True},
            {"text": "Both, because both are clear",
             "correct": False,
             "why": "Clear is not pure. Sea water can be made perfectly "
                    "clear"},
            {"text": "Neither, because no liquid is ever completely pure",
             "correct": False,
             "why": "Distilled water is treated as pure for this purpose. "
                    "This sort of answer refuses a question that has one"},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s07",
        "band": "standard",
        "text": "A painkiller is sold at 99.9% pure, and the missing 0.1% is "
                "named and limited on the packet. Why does naming it matter?",
        "options": [
            {"text": "Because a substance cannot legally be called pure "
                     "unless every other substance in it is listed",
             "correct": False,
             "why": "The law is looser than that, which is exactly why a "
                    "juice carton can say 100% pure and name nothing"},
            {"text": "Because naming it makes the tablet more pure",
             "correct": False,
             "why": "Naming changes nothing about the composition. It changes "
                    "what the buyer can check"},
            {"text": "Because the tablet is swallowed by someone who cannot "
                     "inspect it, so what else is in it has to be known and "
                     "controlled",
             "correct": True},
            {"text": "Because 0.1% is a large enough share to change how the "
                     "painkiller works",
             "correct": False,
             "why": "It is a tiny share, and that is not the point. The point "
                    "is that it is known rather than unknown"},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s08",
        "band": "standard",
        "text": "Which single result would show that a clear colourless "
                "liquid is a mixture rather than a pure substance?",
        "options": [
            {"text": "It has no smell at all, which a pure substance almost "
                     "always has and a mixture almost never does",
             "correct": False,
             "why": "There is no such rule. Distilled water is pure and has "
                    "no smell"},
            {"text": "It pours easily and leaves no film on the glass",
             "correct": False,
             "why": "That describes how it behaves as a liquid. It says "
                    "nothing about how many substances are in it"},
            {"text": "It is completely clear with nothing floating in it",
             "correct": False,
             "why": "Clear rules out undissolved bits and nothing more. Sea "
                    "water is clear"},
            {"text": "Boiling it dry leaves a solid residue behind",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-01-h05",
        "band": "harder",
        "text": "Air and oxygen are both invisible. Brass and copper both "
                "look like metal. Sea water and distilled water both look like "
                "water. What one point do the three pairs make?",
        "options": [
            {"text": "That appearance never decides purity",
             "correct": True},
            {"text": "That every mixture has a pure substance that looks "
                     "exactly like it, so purity always comes in pairs",
             "correct": False,
             "why": "Neat, and not a rule. The three pairs were chosen to "
                    "make a point, not because pairing always happens"},
            {"text": "That mixtures are always harder to identify than pure "
                     "substances",
             "correct": False,
             "why": "Neither is identified by eye. The difficulty is the same "
                    "in both directions"},
            {"text": "That a pure substance is always the more useful of the "
                     "two",
             "correct": False,
             "why": "Brass, sea water and air are all more useful than their "
                    "partners for most jobs"},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h06",
        "band": "harder",
        "text": "9-carat gold is only 37.5% gold and a ring made of it lasts "
                "for decades. What does that show about the word pure?",
        "options": [
            {"text": "That a jeweller uses the word differently from a "
                     "chemist",
             "correct": False,
             "why": "The carat number is an honest statement of composition. "
                    "Nobody is using the word loosely here"},
            {"text": "That purity is a statement about composition, not about "
                     "how good something is",
             "correct": True},
            {"text": "That the ring would be better if it were purer",
             "correct": False,
             "why": "A pure gold ring would mark with a fingernail. Purer is "
                    "worse for this job"},
            {"text": "That 9-carat gold is a compound of gold with copper and "
                     "silver",
             "correct": False,
             "why": "Nothing is chemically joined, and the proportions can be "
                    "chosen. That is a mixture"},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h07",
        "band": "harder",
        "text": "Which change would turn a mixture into a pure substance?",
        "options": [
            {"text": "Filtering out everything you can see in it",
             "correct": False,
             "why": "That removes the undissolved solids only. Anything "
                    "dissolved goes through with the liquid"},
            {"text": "Stirring it until it is uniform all the way through",
             "correct": False,
             "why": "Stirring makes a mixture look more convincing and "
                    "changes nothing about what is in it"},
            {"text": "Separating out everything except one substance",
             "correct": True},
            {"text": "Sterilising it until nothing living is left in it "
                     "anywhere, so that it is completely safe to drink or to "
                     "handle",
             "correct": False,
             "why": "Purity is a count of substances, not a safety rating. "
                    "Everything dissolved survives"},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h08",
        "band": "harder",
        "text": "A student says a pure substance must have been made in a "
                "factory, because nature always mixes things up. What is the "
                "best reply?",
        "options": [
            {"text": "They are right in practice — no natural sample is pure "
                     "enough",
             "correct": False,
             "why": "Plenty have. A diamond is one, and so is a quartz "
                    "crystal"},
            {"text": "They are right, because purifying is something only a "
                     "chemist can do",
             "correct": False,
             "why": "Purity is about what is in the sample, not about who "
                    "handled it. Nature makes pure substances too"},
            {"text": "Factory substances are usually less pure, because "
                     "things get added",
             "correct": False,
             "why": "This disagrees with the student for the wrong reason. "
                    "The test is composition, not origin"},
            {"text": "A natural diamond is almost pure carbon, and where a "
                     "sample came from is never the test",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ────────────────────────────────────────
    {
        "id": "c3-01-e09",
        "band": "easier",
        "text": "Bronze is made by melting copper and tin together on "
                "purpose. Is bronze a pure substance?",
        "options": [
            {"text": "No — two substances mixed together on purpose is "
                     "still a mixture", "correct": True},
            {"text": "Yes — melting the two metals together joins them permanently into one brand new substance", "correct": False,
             "why": "Melting mixes them without joining them chemically. "
                    "Both copper and tin are still there, unchanged, once "
                    "it cools."},
            {"text": "Yes — nothing was added afterwards to spoil it",
             "correct": False,
             "why": "Nothing being added afterwards is not the test. Two "
                    "substances were combined at the start, which is "
                    "enough to make it a mixture."},
            {"text": "No, but only because it was made in a furnace rather "
                     "than found naturally", "correct": False,
             "why": "Where it was made is not the test. It is a mixture "
                    "because it holds two substances, whether that "
                    "happened in a furnace or anywhere else."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e10",
        "band": "easier",
        "text": "Rock salt, dug straight from the ground, is salt mixed with grit and clay. Table salt has been refined until only sodium chloride is left. Which of the two is pure?",
        "options": [
            {
             "text": "Rock salt — it comes straight from the ground with nothing added by anyone",
             "correct": False,
             "why": "Nothing added is not the test, and rock salt still has grit and clay mixed all through it.",
            },
            {
             "text": "Table salt — it has been refined until only one substance is left",
             "correct": True,
            },
            {
             "text": "Neither — both of them have been through some kind of industrial processing",
             "correct": False,
             "why": "Processing does not decide it. Refining rock salt down to one substance is exactly what makes table salt pure.",
            },
            {
             "text": "Both — they are both called salt",
             "correct": False,
             "why": "Sharing a name does not make two things the same. Rock salt is salt mixed with other substances.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e11",
        "band": "easier",
        "text": "Solid carbon dioxide (dry ice), used in a fog machine, is "
                "one substance frozen solid, with nothing else in it. Is "
                "it pure?",
        "options": [
            {"text": "No — a solid substance can never truly be pure, only a liquid or a gas ever can", "correct": False,
             "why": "Purity is about how many substances are present, not "
                    "what state something is in."},
            {"text": "Yes — one substance, frozen solid, is still just "
                     "one substance", "correct": True},
            {"text": "No — fog is a mixture of gases and water droplets, "
                     "so the ice that makes it must be too", "correct": False,
             "why": "The fog it produces afterwards is a different thing "
                    "from the block of dry ice itself, which is one "
                    "substance on its own."},
            {"text": "It cannot be decided without seeing inside it",
             "correct": False,
             "why": "You cannot see individual particles in anything, "
                    "solid or gas. That never decides purity either way."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e12",
        "band": "easier",
        "text": "A bottle labelled \"pure malt vinegar\" actually contains "
                "acetic acid dissolved in water, plus flavour compounds "
                "from the malt. Is the vinegar a pure substance?",
        "options": [
            {"text": "No — several substances dissolved together, "
                     "whatever the label says", "correct": True},
            {"text": "Yes — the label promises nothing has been added",
             "correct": False,
             "why": "The label's \"pure\" means nothing added, not that "
                    "only one substance is present."},
            {"text": "Yes — it is a liquid you can see straight through "
                     "with your own eyes, from any angle",
             "correct": False,
             "why": "Clear tells you there are no undissolved solids, and "
                    "nothing about how many dissolved substances are "
                    "present."},
            {"text": "It cannot be a mixture, since vinegar is a single "
                     "well-known substance", "correct": False,
             "why": "Being well-known and having one common name does not "
                    "mean it is chemically one substance."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e13",
        "band": "easier",
        "text": "A gold bar is stamped 999.9, meaning 99.99% gold. A ring is stamped 375, meaning 37.5% gold. Which is closer to a pure substance?",
        "options": [
            {
             "text": "The bar — 99.99% is far closer to one substance than 37.5% is",
             "correct": True,
            },
            {
             "text": "The ring, because a ring is the more valuable of the two objects",
             "correct": False,
             "why": "Value has nothing to do with it. The stamped numbers say how much of each object is actually gold.",
            },
            {
             "text": "Both equally, since both are described as gold",
             "correct": False,
             "why": "The two numbers are very different, and one is far closer to 100% than the other.",
            },
            {
             "text": "Neither — a stamped number tells you an object's weight rather than what it is made of",
             "correct": False,
             "why": "The stamps 999.9 and 375 state how much of each object is gold, not what the object weighs.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e14",
        "band": "easier",
        "text": "A welder uses argon gas from a cylinder to protect hot "
                "metal from the air. The cylinder holds one gas and "
                "nothing else. Is the argon pure?",
        "options": [
            {"text": "No — a gas you cannot see can never be checked for "
                     "purity", "correct": False,
             "why": "Invisibility never decides it, for argon any more "
                    "than for oxygen or air."},
            {"text": "Yes — one gas and nothing else in the cylinder",
             "correct": True},
            {"text": "No — welding gases are always mixtures of several "
                     "shielding gases", "correct": False,
             "why": "Some welding jobs do use gas mixtures, but this "
                    "cylinder is stated to hold one gas only."},
            {"text": "It depends on what metal is being welded",
             "correct": False,
             "why": "What the gas is used on has nothing to do with what "
                    "is inside the cylinder."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e15",
        "band": "easier",
        "text": "A jar of honey is labelled \"100% pure, raw honey, "
                "nothing added\". Honey actually contains several natural "
                "sugars, water, enzymes and pollen grains. Is honey a "
                "pure substance?",
        "options": [
            {"text": "Yes — nothing has been added to it", "correct": False,
             "why": "Nothing added is the label's claim, not a claim "
                    "about how many substances are inside."},
            {"text": "Yes — it is a completely natural product, gathered from the hive by bees with nothing else involved",
             "correct": False,
             "why": "Natural is not the test. Sea water and rainwater are "
                    "natural too, and both are mixtures."},
            {"text": "No — several different sugars and other substances "
                     "are already mixed through it", "correct": True},
            {"text": "It cannot be decided without tasting it",
             "correct": False,
             "why": "Tasting tells you about flavour, not about how many "
                    "substances are present."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e16",
        "band": "easier",
        "text": "Petrol is a mixture of many different hydrocarbon "
                "substances, and it is highly flammable. What does that "
                "show about mixtures?",
        "options": [
            {"text": "That mixtures are never used as fuels",
             "correct": False,
             "why": "Petrol itself is a fuel and a mixture. The two are "
                    "not exclusive."},
            {"text": "That petrol must actually be a pure substance, "
                     "since pure things are usually the dangerous ones",
             "correct": False,
             "why": "Petrol holds many different hydrocarbon substances. "
                    "It is a mixture, dangerous or not."},
            {"text": "That anything at all that is flammable is therefore automatically and always impure",
             "correct": False,
             "why": "Pure substances can be flammable too — pure sodium "
                    "bursts into flame in water. Being flammable does not "
                    "decide purity either way."},
            {"text": "That being a mixture does not make something safer "
                     "than a pure substance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e17",
        "band": "easier",
        "text": "Crisp packets are often filled with pure nitrogen gas "
                "instead of air, to stop the crisps going stale. Is the "
                "gas inside pure?",
        "options": [
            {"text": "Yes — nitrogen from a cylinder is one substance, "
                     "sealed packet or not", "correct": True},
            {"text": "No — a gas sealed tightly inside a crisp packet can never really be checked at all", "correct": False,
             "why": "Sealing something away does not make it a mixture. "
                    "Nitrogen from a cylinder is one substance whichever "
                    "container it ends up in."},
            {"text": "No — the crisps themselves are a mixture, so the "
                     "gas around them must be too", "correct": False,
             "why": "The crisps and the gas are two separate things. The "
                    "crisps being a mixture says nothing about what is in "
                    "the gas."},
            {"text": "It depends on the flavour of crisp inside the "
                     "packet", "correct": False,
             "why": "The flavour of the food has no bearing on what gas "
                    "surrounds it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e18",
        "band": "easier",
        "text": "A bottle of sparkling mineral water contains dissolved "
                "carbon dioxide as well as several dissolved minerals. Is "
                "it a pure substance?",
        "options": [
            {"text": "Yes — mineral water is marketed as pure and "
                     "natural", "correct": False,
             "why": "A marketing claim about naturalness is not a claim "
                    "about how many substances are present."},
            {"text": "No — carbon dioxide and several minerals are all "
                     "dissolved in it together", "correct": True},
            {"text": "Yes — carbon dioxide bubbles are not really part of "
                     "the water", "correct": False,
             "why": "While dissolved, the carbon dioxide is one more "
                    "substance present in the liquid, exactly like the "
                    "minerals."},
            {"text": "It cannot be decided until the bubbles have gone "
                     "flat", "correct": False,
             "why": "Whether the gas has escaped yet does not change how "
                    "many substances were originally dissolved."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e19",
        "band": "easier",
        "text": "Silicon used to make computer chips is refined to 99.9999999% purity. Sand, which silicon is refined from, is a mixture of many different minerals. Which is closer to a pure substance?",
        "options": [
            {
             "text": "The sand — it is completely natural",
             "correct": False,
             "why": "Natural is not the test. Sand holds several different minerals mixed together.",
            },
            {
             "text": "Both equally pure — the refined silicon originally came from that very same sand",
             "correct": False,
             "why": "Sharing an origin does not make the starting material and the refined product equally pure.",
            },
            {
             "text": "The refined silicon — 99.9999999% is about as close to one substance as it gets",
             "correct": True,
            },
            {
             "text": "Neither — no material anywhere can be measured to a purity as high as 99.9999999%",
             "correct": False,
             "why": "That figure is a real, measured purity used in the electronics industry. Refusing to accept it settles nothing.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e20",
        "band": "easier",
        "text": "Car coolant is a mixture of ethylene glycol and water, mixed on purpose so it does not freeze in winter. Is the coolant pure?",
        "options": [
            {
             "text": "Yes — it was mixed carefully by a chemist, not carelessly",
             "correct": False,
             "why": "Care taken in mixing something does not change how many substances are present. Two substances mixed carefully are still a mixture.",
            },
            {
             "text": "Yes — it is sold and labelled under a single well-known product name, antifreeze",
             "correct": False,
             "why": "Having one name for a product does not make it one substance.",
            },
            {
             "text": "It depends on which car it is used in",
             "correct": False,
             "why": "What the coolant is used in has no bearing on what it is made of.",
            },
            {
             "text": "No — ethylene glycol and water mixed together on purpose",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e21",
        "band": "easier",
        "text": "Pure ethanol, sold to a laboratory, is one substance. A can of beer contains ethanol along with water, flavour compounds and dissolved carbon dioxide. Which is pure?",
        "options": [
            {
             "text": "The laboratory ethanol — one substance, with nothing else dissolved in it",
             "correct": True,
            },
            {
             "text": "The beer — it is a natural product of fermentation, and a natural product has nothing else mixed into it",
             "correct": False,
             "why": "Fermentation being a natural process does not reduce how many substances end up in the drink.",
            },
            {
             "text": "Both — they both contain the same substance, ethanol",
             "correct": False,
             "why": "Containing some of the same substance does not make two different samples equally pure. One holds several others besides.",
            },
            {
             "text": "Neither — alcohol can never be pure",
             "correct": False,
             "why": "Ethanol can be produced and sold as a pure substance. A laboratory bottle of it is exactly that.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e22",
        "band": "easier",
        "text": "A bar of chocolate is labelled \"100% cocoa\". It still "
                "contains cocoa solids and cocoa butter, at least two "
                "different substances. Is the chocolate a pure substance?",
        "options": [
            {"text": "Yes — the label says 100%", "correct": False,
             "why": "A food label's percentage is about how much of an "
                    "ingredient was used, not how many substances the "
                    "bar contains."},
            {"text": "No — cocoa solids and cocoa butter are already two "
                     "different substances", "correct": True},
            {"text": "Yes — nothing artificial has been added to it at any stage of the manufacturing process",
             "correct": False,
             "why": "Nothing artificial being added is a different claim "
                    "from being made of one substance."},
            {"text": "It cannot possibly be decided without first melting the whole bar of chocolate completely down",
             "correct": False,
             "why": "Melting changes the chocolate's state, not how many "
                    "substances are already mixed through it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e23",
        "band": "easier",
        "text": "A canister of pure carbon dioxide is used to carbonate a drink. A separate canister of compressed air is used to inflate a bicycle tyre. Which canister holds a pure substance?",
        "options": [
            {
             "text": "The air canister — air is what bicycle tyres are normally filled with",
             "correct": False,
             "why": "Being the normal choice for a job does not make air one substance. It is still a mixture of several gases.",
            },
            {
             "text": "Both — both are compressed tightly into a metal canister under high pressure",
             "correct": False,
             "why": "Being compressed changes nothing about how many substances are inside. Air stays a mixture under any pressure.",
            },
            {
             "text": "The carbon dioxide canister — one gas, with nothing else mixed in",
             "correct": True,
            },
            {
             "text": "Neither — gases cannot be classified as pure or mixture",
             "correct": False,
             "why": "Gases can absolutely be pure substances — the carbon dioxide in this canister is exactly that.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e24",
        "band": "easier",
        "text": "Caster sugar is almost pure sucrose. Icing sugar looks identical — a fine white powder — but has a small amount of cornflour mixed in to stop it clumping. Which is pure?",
        "options": [
            {
             "text": "Icing sugar — it looks even finer and whiter, and a finer powder has fewer substances in it",
             "correct": False,
             "why": "Appearance never decides it, and the two look essentially identical anyway. How fine a powder is says nothing about how many substances are in it.",
            },
            {
             "text": "Both — they are both kinds of sugar",
             "correct": False,
             "why": "Sharing the word sugar in their name does not make icing sugar free of the cornflour that is genuinely mixed through it.",
            },
            {
             "text": "Neither — both have been through a factory",
             "correct": False,
             "why": "Going through a factory is not the test. Caster sugar comes out as one substance; icing sugar comes out with cornflour added.",
            },
            {
             "text": "Caster sugar — the icing sugar has cornflour mixed through it as well",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e25",
        "band": "easier",
        "text": "Car battery manufacturers recommend topping up with distilled water rather than tap water. Which of the two is closer to a pure substance?",
        "options": [
            {
             "text": "Distilled water — the dissolved minerals have been taken out of it",
             "correct": True,
            },
            {
             "text": "Tap water — it comes straight from the mains and has not been processed",
             "correct": False,
             "why": "Not being processed does not remove the dissolved minerals tap water already carries. Distilled water has had them taken out.",
            },
            {
             "text": "Both equally — both are described as water",
             "correct": False,
             "why": "Sharing the name water does not mean sharing a composition. Tap water carries dissolved minerals that distilled water does not.",
            },
            {
             "text": "Neither — boiling a liquid and condensing it again cannot change what is dissolved in it",
             "correct": False,
             "why": "Distilling does exactly that: the water evaporates and condenses while the dissolved minerals are left behind.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e26",
        "band": "easier",
        "text": "Sulfur mined from a volcanic vent can be nearly one substance, bright yellow and crystalline. The surrounding volcanic rock is a mixture of many different minerals. Which is closer to pure?",
        "options": [
            {
             "text": "The volcanic rock — it formed naturally from the volcano, and nothing formed naturally is a mixture",
             "correct": False,
             "why": "Forming naturally does not reduce how many minerals are mixed into a rock.",
            },
            {
             "text": "The mined sulfur — the surrounding rock is a mixture of many minerals",
             "correct": True,
            },
            {
             "text": "Both — both came out of the same volcano",
             "correct": False,
             "why": "Sharing an origin does not make two very different materials equally pure.",
            },
            {
             "text": "Neither — nothing that comes from a volcano can be pure",
             "correct": False,
             "why": "Sulfur deposits from volcanic vents can genuinely be very close to one substance. The source does not rule that out.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e27",
        "band": "easier",
        "text": "A bar of soap labelled \"pure glycerine soap\" is "
                "actually a mixture of oils, glycerine, fragrance and "
                "colouring. Is the soap a pure substance?",
        "options": [
            {"text": "Yes — the label uses the word pure", "correct": False,
             "why": "A product's own name for itself is a marketing "
                    "claim, not a chemistry claim."},
            {"text": "Yes — glycerine really is one of the ingredients",
             "correct": False,
             "why": "Containing some glycerine among several other "
                    "ingredients does not make the whole bar one "
                    "substance."},
            {"text": "No — oils, fragrance and colouring are all mixed in "
                     "alongside the glycerine", "correct": True},
            {"text": "It cannot be decided without first dissolving the entire bar completely in a beaker of water", "correct": False,
             "why": "Dissolving would tell you about solubility, not "
                    "directly settle how many substances the solid bar "
                    "already contains."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e28",
        "band": "easier",
        "text": "A galvanised steel pipe is made of steel coated in a "
                "layer of zinc, to stop it rusting. Is the whole pipe a "
                "pure substance?",
        "options": [
            {"text": "Yes — the zinc coating is only on the surface, not "
                     "inside the pipe", "correct": False,
             "why": "The object as a whole is being asked about, and it "
                    "holds at least two different substances even if one "
                    "only coats the surface."},
            {"text": "Yes — zinc and steel are both metals",
             "correct": False,
             "why": "Being the same broad category does not make two "
                    "different substances one substance."},
            {"text": "It depends entirely on exactly how thick the zinc coating happens to be applied to the pipe",
             "correct": False,
             "why": "Even a thin coating is a second substance present. "
                    "Thickness changes the proportion, not the verdict."},
            {"text": "No — the pipe is made of at least two substances, "
                     "steel and zinc", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e29",
        "band": "easier",
        "text": "Natural gas piped into homes is mostly methane, but a "
                "smelly sulfur-containing substance is deliberately added "
                "so people can detect a gas leak. Is the gas that reaches "
                "your home pure methane?",
        "options": [
            {"text": "No — the smelly substance is mixed in on top of "
                     "the methane", "correct": True},
            {"text": "Yes — the added substance is only there for smell, "
                     "not chemistry", "correct": False,
             "why": "Whatever it is added for, the smelly substance is a "
                    "second substance now mixed in. That is what a "
                    "mixture is."},
            {"text": "Yes — natural gas is naturally occurring, so "
                     "nothing counts as being \"added\" to it",
             "correct": False,
             "why": "The odorant genuinely is added by the supplier, on "
                    "top of whatever methane came out of the ground."},
            {"text": "It depends on whether you can smell it in a "
                     "particular room", "correct": False,
             "why": "Whether a person notices the smell has nothing to "
                    "do with whether the substance is actually present."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e30",
        "band": "easier",
        "text": "Surgical spirit is mostly ethanol, with methanol and a bitter-tasting substance added on purpose so that it cannot be drunk. Is surgical spirit a pure substance?",
        "options": [
            {
             "text": "Yes — ethanol is by far the largest and most important substance dissolved in it",
             "correct": False,
             "why": "Being the main ingredient does not remove the other substances mixed in alongside it.",
            },
            {
             "text": "Yes — the added substances are only there to change the taste, not the chemistry",
             "correct": False,
             "why": "Whatever they are added for, the extra substances genuinely are mixed into the liquid. That is enough to make it a mixture.",
            },
            {
             "text": "It cannot be decided, since the bottle does not state how much of each substance is present",
             "correct": False,
             "why": "Knowing the amounts is not needed. More than one substance being present is already enough to make it a mixture.",
            },
            {
             "text": "No — methanol and a bitter substance are mixed in on purpose",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e31",
        "band": "easier",
        "text": "A diamond and a lump of graphite can both be almost pure carbon, and nothing else, even though they look completely different from each other. What does that show?",
        "options": [
            {
             "text": "That one of the two must actually be a mixture, since pure substances all look alike",
             "correct": False,
             "why": "Pure substances do not all have to look alike. The two look different because the carbon particles are arranged differently in each.",
            },
            {
             "text": "That diamond and graphite are not really made of the same thing",
             "correct": False,
             "why": "Both can be almost entirely carbon. The arrangement of the particles differs, not the substance.",
            },
            {
             "text": "That two things can look totally different and still both be pure substances of the same element",
             "correct": True,
            },
            {
             "text": "That looking different always means one sample is impure",
             "correct": False,
             "why": "Looking different is not evidence of a mixture, any more than looking the same is evidence of purity. Appearance never decides it, in either direction.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-e32",
        "band": "easier",
        "text": "Blood is made of plasma, red and white blood cells, "
                "platelets and many dissolved substances. Is blood a pure "
                "substance?",
        "options": [
            {"text": "Yes — it is a single body fluid with one name",
             "correct": False,
             "why": "Having one everyday name for something does not "
                    "make it chemically one substance."},
            {"text": "Yes — it looks completely uniform, one red liquid",
             "correct": False,
             "why": "The gold ring, the milk and the juice all look "
                    "uniform too, and appearance never decides it."},
            {"text": "It cannot be decided without knowing whose blood it "
                     "is", "correct": False,
             "why": "Whose blood it is does not change the answer. "
                    "Every person's blood is a mixture of the same kinds "
                    "of components."},
            {"text": "No — plasma, blood cells and many dissolved "
                     "substances, all together", "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-01-s09",
        "band": "standard",
        "text": "A sculptor could use pure copper or bronze (copper and "
                "tin) for a statue. Pure copper is soft and dents easily; "
                "bronze is much harder. Why might the mixture be chosen "
                "over the pure metal?",
        "options": [
            {"text": "Because the tin reacts with the copper to make the "
                     "statue lighter", "correct": False,
             "why": "Nothing reacts, and lightness is not the point. The "
                    "tin and copper stay themselves, mixed together."},
            {"text": "Because mixing in tin makes the metal harder and "
                     "more durable, even though it is no longer pure",
             "correct": True},
            {"text": "Because bronze is technically still pure, since "
                     "both metals came from the ground", "correct": False,
             "why": "Where the metals came from is not the test. Two "
                    "substances mixed together is a mixture, wherever "
                    "each one started."},
            {"text": "Because pure metals cannot be cast into a statue "
                     "shape at all", "correct": False,
             "why": "Pure copper can be cast perfectly well. It is simply "
                    "softer once it has been."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s10",
        "band": "standard",
        "text": "A shopper says rock salt cannot be impure, because "
                "nothing has been added to it since it was dug up. What "
                "is wrong with the claim?",
        "options": [
            {"text": "Rock salt actually has extra salt added to it "
                     "during mining", "correct": False,
             "why": "Nothing is added during mining. The grit and clay "
                    "were mixed in naturally, long before that."},
            {"text": "Impurities do not have to be added — they can be "
                     "there in the ground already", "correct": True},
            {"text": "Nothing is wrong — dug-up substances are always "
                     "pure until something is done to them", "correct": False,
             "why": "This is the exact idea the claim is making, and it "
                    "is false. Plenty of dug-up materials are mixtures "
                    "from the start."},
            {"text": "The claim is right, because purity is about what "
                     "has been added, not what is naturally there",
             "correct": False,
             "why": "Purity is about how many substances are present, "
                    "whatever their origin."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s11",
        "band": "standard",
        "text": "Dry ice (solid carbon dioxide) is one substance. Oxygen "
                "from a cylinder is also one substance, but it is a gas "
                "rather than a solid. Does the different state of matter "
                "change whether either one is pure?",
        "options": [
            {"text": "Yes — only a gas can truly be pure, because a "
                     "solid is always packed with impurities",
             "correct": False,
             "why": "Nothing about being a solid adds other substances. "
                    "A pure solid is exactly as possible as a pure gas."},
            {"text": "Yes — a solid pure substance is technically a "
                     "mixture of very small crystals", "correct": False,
             "why": "Many identical crystals of the same substance are "
                    "still one substance. Being made of separate crystals "
                    "does not create a second one."},
            {"text": "No — both are pure, and the state they are in "
                     "makes no difference", "correct": True},
            {"text": "It cannot be decided, because dry ice and gas "
                     "cylinders are never compared", "correct": False,
             "why": "Comparability is not the test. How many substances "
                    "each one contains is, and that can be answered for "
                    "both."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s12",
        "band": "standard",
        "text": "Why does a bottle labelled \"pure vinegar\" not settle "
                "whether the liquid inside is a pure substance in the "
                "chemist's sense?",
        "options": [
            {"text": "Because food labels are not allowed to use "
                     "scientific words at all", "correct": False,
             "why": "Nothing stops a label using the word. The trouble "
                    "is that the word means something different there."},
            {"text": "Because vinegar's composition genuinely changes a little every single time the bottle is opened, used and closed again", "correct": False,
             "why": "Opening the bottle changes nothing about what is "
                    "dissolved in it."},
            {"text": "Because \"pure\" only applies to solids, never to "
                     "liquids", "correct": False,
             "why": "Liquids can be pure substances too — distilled "
                    "water is one."},
            {"text": "Because \"pure\" on food labelling means nothing "
                     "was added, which is a different claim from one "
                     "substance only", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s13",
        "band": "standard",
        "text": "Investment-grade gold bars are sold as 999.9 fine gold, "
                "while wedding rings of the same metal are typically only "
                "37.5% to 75% gold. Why is the bar allowed to be so much "
                "purer?",
        "options": [
            {"text": "Because a bar only has to be stored, while a ring "
                     "has to survive being worn every day and needs the "
                     "strength a mixture gives it", "correct": True},
            {"text": "Because pure gold is cheaper to produce than an "
                     "alloy", "correct": False,
             "why": "Refining gold to 999.9 costs more, not less, than "
                    "leaving other metals mixed in."},
            {"text": "Because wedding rings are traditionally always made from whatever scrap metal happens to be left over once the investment bars have been cast", "correct": False,
             "why": "Rings are alloyed on purpose for hardness, not "
                    "because of leftover metal."},
            {"text": "Because a bar's purity is only a marketing claim, "
                     "not really measured", "correct": False,
             "why": "Bar purity is assayed and stamped precisely. It is "
                    "a real, checked figure."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s14",
        "band": "standard",
        "text": "A welder chooses pure argon from a cylinder rather than "
                "ordinary air to shield a hot weld, even though both are "
                "invisible. Why does the choice matter?",
        "options": [
            {"text": "Because pure gases are always cheaper to buy in a "
                     "cylinder than air is", "correct": False,
             "why": "Air is free; a cylinder of pure argon costs money "
                    "precisely because it has been separated out."},
            {"text": "Because air is a mixture that includes oxygen, "
                     "which would react with the hot metal and spoil the "
                     "weld", "correct": True},
            {"text": "Because argon gas is faintly coloured, which lets the welder see exactly where the hot weld is forming as they work", "correct": False,
             "why": "Argon is just as invisible as air. Colour is not "
                    "why it is chosen."},
            {"text": "Because a mixture like air cannot be compressed "
                     "into a cylinder", "correct": False,
             "why": "Air is compressed into cylinders all the time. That "
                    "is not the reason argon is chosen here."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s15",
        "band": "standard",
        "text": "Explain why raw honey being natural and having \"nothing "
                "added\" does not make it a pure substance.",
        "options": [
            {"text": "Because raw honey has never once been heated by anybody, and heating a mixture up is generally what eventually makes a substance become pure", "correct": False,
             "why": "Heating a mixture does not remove the other "
                    "substances in it. It can even drive off some of the "
                    "water."},
            {"text": "Because bees add pollen to the honey on purpose to "
                     "make it a mixture", "correct": False,
             "why": "Whether the pollen was added on purpose or fell in "
                    "by chance makes no difference to the verdict."},
            {"text": "Because several different sugars, water and other "
                     "substances are already there, whether or not "
                     "anything was added afterwards", "correct": True},
            {"text": "Because the jar itself contaminates the honey once "
                     "it is sealed", "correct": False,
             "why": "The jar contributes nothing. The sugars, water and "
                    "enzymes were already there before it was ever put in "
                    "a jar."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s16",
        "band": "standard",
        "text": "A petrol station carries hazard warnings everywhere, but "
                "a bottle of distilled water carries none. Does this mean "
                "pure substances are always safer than mixtures?",
        "options": [
            {"text": "Yes — a pure substance can never catch fire",
             "correct": False,
             "why": "Pure sodium catches fire on contact with water. "
                    "Purity is no guarantee of safety."},
            {"text": "Yes — mixtures are always more dangerous than any pure substance, because they contain several more substances mixed in", "correct": False,
             "why": "Plenty of mixtures, such as milk or sea water, "
                    "carry no hazard warnings at all."},
            {"text": "It cannot be answered, because petrol has never "
                     "been tested for purity", "correct": False,
             "why": "It does not need testing — a fuel deliberately "
                    "blended from many hydrocarbons is a mixture by "
                    "definition."},
            {"text": "No — petrol is a mixture and is hazardous, while "
                     "pure sodium is a pure substance and is also "
                     "hazardous", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s17",
        "band": "standard",
        "text": "A crisp manufacturer chooses pure nitrogen rather than ordinary air to fill the packet. Why does the choice matter, given both are invisible?",
        "options": [
            {
             "text": "Air is a mixture containing oxygen, which would react with the crisps and make them stale; nitrogen does not",
             "correct": True,
            },
            {
             "text": "Nitrogen is heavier than air, so it sinks into the packet and cushions the crisps against being crushed in transit",
             "correct": False,
             "why": "Nitrogen is slightly lighter than air, and cushioning is not why it is chosen. It is about what the gas does to the food chemically.",
            },
            {
             "text": "Air cannot be pumped into a sealed packet",
             "correct": False,
             "why": "Air is used to fill all sorts of sealed containers. That is not the reason nitrogen is chosen here.",
            },
            {
             "text": "Nitrogen is cheaper to produce than air",
             "correct": False,
             "why": "Air is free — nitrogen costs money precisely because it has been separated out of it.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s18",
        "band": "standard",
        "text": "Still bottled water and sparkling bottled water are drawn from the same spring. The sparkling version has extra carbon dioxide added. Which change made it MORE of a mixture?",
        "options": [
            {
             "text": "Drawing it from the spring, since spring water starts out as pure water and only picks up its minerals once it is in the bottle",
             "correct": False,
             "why": "The minerals dissolve into the water underground, long before bottling. That is not the change the question is asking about.",
            },
            {
             "text": "Adding the carbon dioxide, on top of the minerals already dissolved from the spring",
             "correct": True,
            },
            {
             "text": "Bottling it, since bottling always adds substances to a liquid",
             "correct": False,
             "why": "Bottling adds nothing by itself. It is the deliberate addition of carbon dioxide that changes the composition here.",
            },
            {
             "text": "Nothing changed — the carbon dioxide dissolves without ever becoming part of the water",
             "correct": False,
             "why": "A dissolved substance is part of the mixture, whatever it is. That is what dissolving means.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s19",
        "band": "standard",
        "text": "Why does a computer chip need silicon refined to such an extreme purity, when a window pane made of glass (also mostly silicon compounds) does not?",
        "options": [
            {
             "text": "Because computer chips are always far more expensive products to manufacture than a simple pane of glass, so naturally they deserve to be made from better, more carefully chosen materials",
             "correct": False,
             "why": "Cost does not decide the science. The purity is needed because of how the chip works.",
            },
            {
             "text": "Because glass contains no silicon compounds at all",
             "correct": False,
             "why": "Glass is largely made from silica, a silicon compound. The two do share their key raw material.",
            },
            {
             "text": "Because tiny amounts of another substance would disrupt how electricity moves through the chip, in a way that does not matter for a pane of glass",
             "correct": True,
            },
            {
             "text": "Because sand naturally becomes purer the longer it is heated in a furnace",
             "correct": False,
             "why": "Heating alone does not remove other minerals. A chip's silicon is chemically separated out, not just melted.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s20",
        "band": "standard",
        "text": "Pure water freezes at 0 °C. The mixed coolant does not "
                "freeze until far below that. Why does mixing it with "
                "ethylene glycol change the freezing point?",
        "options": [
            {"text": "Because ethylene glycol is warmer than water and "
                     "heats it up", "correct": False,
             "why": "Nothing here is about temperature of the "
                    "ingredients. It is about how a mixture behaves "
                    "compared with a pure substance."},
            {"text": "Because the mixture is less dense than pure water",
             "correct": False,
             "why": "Density is not the reason a mixture's freezing "
                    "point shifts. Being a mixture at all is."},
            {"text": "Because the ethylene glycol reacts chemically with the water molecules to make an entirely new substance that simply cannot freeze at any temperature at all", "correct": False,
             "why": "Nothing reacts. The two substances stay themselves, "
                    "mixed together, and that mixing is what shifts the "
                    "freezing point."},
            {"text": "Because mixing something else in disrupts the "
                     "regular arrangement water's particles need to "
                     "freeze, in the same way that mixing salt into "
                     "water does", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s21",
        "band": "standard",
        "text": "A can of beer and a bottle of laboratory ethanol both contain the same substance, ethanol. Explain why one is a mixture and the other is close to pure.",
        "options": [
            {
             "text": "Because the beer also has water, flavour compounds and dissolved gas mixed in, while the laboratory ethanol has had all of that removed or never added",
             "correct": True,
            },
            {
             "text": "Because beer has been fermented and laboratory ethanol has not",
             "correct": False,
             "why": "How ethanol was made — by fermenting or by another method — does not decide whether other substances are still mixed with it afterwards.",
            },
            {
             "text": "Because laboratory ethanol is stronger than the ethanol in beer",
             "correct": False,
             "why": "Strength, how much ethanol there is, is not the test. Whether OTHER substances are present alongside it is.",
            },
            {
             "text": "Because beer is sold as a drink and laboratory ethanol is sold as a chemical, and that difference is what decides it, since anything sold as a drink is counted as a single substance",
             "correct": False,
             "why": "How a liquid is sold and labelled has nothing to do with how many substances it is made of.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s22",
        "band": "standard",
        "text": "Explain what the \"100%\" on a bar of \"100% cocoa\" "
                "chocolate is actually claiming, and why it is not a "
                "claim about purity in the chemist's sense.",
        "options": [
            {"text": "It claims the chocolate has been formally tested inside an independent laboratory and then officially certified by government regulators as being entirely chemically pure", "correct": False,
             "why": "No such testing or certification is implied by the "
                    "percentage on a food label."},
            {"text": "It claims the bar contains only cocoa, with none of "
                     "another ingredient such as milk or added sugar — "
                     "not that cocoa itself is a single substance",
             "correct": True},
            {"text": "It claims the bar weighs exactly 100 g",
             "correct": False,
             "why": "The percentage is about the recipe, not the mass of "
                    "the finished bar."},
            {"text": "It claims every cocoa bean used came from the same "
                     "farm", "correct": False,
             "why": "Nothing about the source farm is stated by that "
                    "figure. It is about the ingredients mixed in, not "
                    "where they grew."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s23",
        "band": "standard",
        "text": "Why can a drinks manufacturer truthfully call its carbon "
                "dioxide canister \"pure\", while nobody would call a "
                "canister of compressed air pure?",
        "options": [
            {"text": "Because carbon dioxide is a gas that is widely used across the food and drinks industry, and food ingredients are conventionally always described on the packaging as being pure",
             "correct": False,
             "why": "Plenty of food ingredients, such as orange juice, "
                    "are mixtures and are not called pure."},
            {"text": "Because air has to be filtered before it can go in "
                     "a canister, which introduces impurities",
             "correct": False,
             "why": "Filtering removes dust; it does not add substances. "
                    "Air was already a mixture of gases before any "
                    "filtering."},
            {"text": "Because the carbon dioxide canister genuinely "
                     "holds one substance, while the air canister holds a "
                     "mixture of nitrogen, oxygen and other gases",
             "correct": True},
            {"text": "Because compressed gases are never really at 100% "
                     "of anything", "correct": False,
             "why": "The carbon dioxide canister genuinely can be very "
                    "close to 100% carbon dioxide. That is a real, "
                    "achievable figure."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s24",
        "band": "standard",
        "text": "Caster sugar and icing sugar look identical to the eye. Explain what test, other than looking, would tell them apart.",
        "options": [
            {
             "text": "Taste each one, since cornflour tastes noticeably different from sugar",
             "correct": False,
             "why": "Cornflour is added in a small enough amount that it is not meant to be tasted. That is not a reliable or safe test.",
            },
            {
             "text": "Weigh equal spoonfuls of each, since icing sugar is heavier",
             "correct": False,
             "why": "Mass per spoonful depends on how finely packed the powder is, not on what it is made of.",
            },
            {
             "text": "Leave both out in damp weather and see which clumps first, since the cornflour in icing sugar draws in moisture and makes it clump sooner than caster sugar, which stays a free-flowing powder however damp the air gets",
             "correct": False,
             "why": "It is the other way round — the cornflour is there precisely to stop icing sugar clumping in damp weather, so this test would point the wrong way.",
            },
            {
             "text": "Dissolve a sample in water — the cornflour in icing sugar does not dissolve and leaves the mixture cloudy, while pure caster sugar dissolves completely and stays clear",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s25",
        "band": "standard",
        "text": "Explain why a car battery is topped up with distilled "
                "water rather than the tap water that comes out of a "
                "kitchen sink.",
        "options": [
            {"text": "Because the dissolved minerals in tap water would "
                     "interfere with the battery's chemistry, and "
                     "distilled water has had them removed",
             "correct": True},
            {"text": "Because tap water is not wet enough for a battery "
                     "to work properly", "correct": False,
             "why": "Wetness is not the issue. Both liquids are water; "
                    "the difference is what else is dissolved in them."},
            {"text": "Because distilled water conducts electricity far better than ordinary tap water does, which is exactly what a working car battery genuinely needs inside it", "correct": False,
             "why": "It is the other way round — dissolved minerals "
                    "actually make tap water conduct better, which is "
                    "exactly the problem inside a battery."},
            {"text": "Because tap water evaporates faster than distilled "
                     "water", "correct": False,
             "why": "The two evaporate at similar rates. Evaporation "
                    "speed is not why one is chosen over the other here."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s26",
        "band": "standard",
        "text": "A geologist finds a bright yellow crystal at a volcanic "
                "vent and a dull grey rock nearby. Which observation "
                "would actually help decide which is closer to a pure "
                "substance, and which would not?",
        "options": [
            {"text": "The brighter colour is the useful evidence, since "
                     "pure substances are usually more strikingly "
                     "coloured", "correct": False,
             "why": "Colour brightness is not a rule for purity — plenty "
                    "of pure substances, such as distilled water, are "
                    "colourless."},
            {"text": "Testing what each one is made of would help; "
                     "noticing that one is a brighter, more striking "
                     "colour would not", "correct": True},
            {"text": "Neither observation is any use, since geology and "
                     "chemistry are unrelated", "correct": False,
             "why": "They are closely related. A geologist testing a "
                    "mineral's composition is doing exactly this kind of "
                    "chemistry."},
            {"text": "Only the crystal's shape matters, since regular "
                     "crystals are always pure", "correct": False,
             "why": "Shape is closer evidence than colour, but shape "
                    "alone is still not the test. You can only be sure by "
                    "finding out what is actually in it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s27",
        "band": "standard",
        "text": "Explain what \"pure glycerine soap\" most likely means on "
                "a label, given that the bar also contains oils, "
                "fragrance and colouring.",
        "options": [
            {"text": "It means the soap has been through a purifying "
                     "process that removes fragrance and colour",
             "correct": False,
             "why": "The fragrance and colour are still present in the "
                    "finished bar, so nothing has been removed by "
                    "whatever \"pure\" is claiming."},
            {"text": "It means the bar contains no oils at all",
             "correct": False,
             "why": "Soap is generally made from oils reacted with other "
                    "ingredients; oils or their products are typically "
                    "still part of the bar."},
            {"text": "It most likely means glycerine is the main or a "
                     "notable ingredient, not that the bar is one "
                     "substance", "correct": True},
            {"text": "It means the same as \"organic\", which is a "
                     "different label altogether", "correct": False,
             "why": "Organic and pure are two different claims on a "
                    "label, and neither one is a chemistry claim about "
                    "substance count."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s28",
        "band": "standard",
        "text": "A plumber has a choice between pure copper pipe and "
                "galvanised steel pipe (steel coated in zinc). Which one "
                "is closer to being made of a pure substance, and does "
                "that make it the better choice for every job?",
        "options": [
            {"text": "The copper pipe is closer to pure, and being the purer material automatically makes it the better choice for absolutely every single plumbing job in the whole house", "correct": False,
             "why": "Being closer to pure is a fact about composition, "
                    "not a guarantee of being the right choice for a "
                    "particular job."},
            {"text": "The galvanised pipe is closer to pure, since the protective zinc coating stops the steel underneath from ever becoming a rusty mixture with the air and rain around it", "correct": False,
             "why": "The pipe already holds two substances, steel and "
                    "zinc, whatever the zinc goes on to protect it from."},
            {"text": "Neither is closer to pure, since both are "
                     "manufactured products", "correct": False,
             "why": "Being manufactured does not equalise them. Copper "
                    "pipe can be very close to one substance, and "
                    "galvanised pipe deliberately combines two."},
            {"text": "The copper pipe is closer to pure, but that alone "
                     "does not make it better for every job — cost, "
                     "weight and the water it will carry all matter too",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s29",
        "band": "standard",
        "text": "Explain why a gas company deliberately makes its natural "
                "gas supply LESS pure by adding a smelly substance to "
                "it.",
        "options": [
            {"text": "Because pure methane is odourless, so a leak could "
                     "go undetected; the added substance makes a leak "
                     "obvious by smell, which is a safety benefit worth "
                     "the loss of purity", "correct": True},
            {"text": "Because pure methane on its own is not flammable "
                     "enough to use as a fuel", "correct": False,
             "why": "Pure methane burns perfectly well as a fuel. The "
                    "additive is there for detection, not to help it "
                    "burn."},
            {"text": "Because the added substance makes the gas burn "
                     "with a cleaner flame", "correct": False,
             "why": "The odorant is present in far too small an amount "
                    "to affect the flame. It is there purely to be "
                    "smelled."},
            {"text": "Because methane straight out of the ground is already mixed together with several other natural gases anyway, so nothing significant is really lost by adding one more substance into it", "correct": False,
             "why": "Methane from the ground is close to pure before "
                    "the odorant is added. The addition is a real, "
                    "deliberate step away from purity."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s30",
        "band": "standard",
        "text": "Explain why methanol and a bitter substance are "
                "deliberately mixed into ethanol to make surgical "
                "spirit.",
        "options": [
            {"text": "So that the ethanol dissolves other substances "
                     "more easily on the skin", "correct": False,
             "why": "The additives are there to discourage drinking it, "
                    "not to change how it dissolves things."},
            {"text": "So that the ethanol cannot legally or safely be "
                     "drunk as an alcoholic drink, while it can still be "
                     "sold cheaply for cleaning and antiseptic use",
             "correct": True},
            {"text": "So that the finished mixture becomes a noticeably stronger, more effective disinfectant than pure ethanol on its own could ever hope to be against household germs", "correct": False,
             "why": "Pure ethanol is already an effective disinfectant. "
                    "The additives are not added to boost that effect."},
            {"text": "So that the mixture is classed as a medicine "
                     "rather than a chemical", "correct": False,
             "why": "What it is legally classed as is not why the "
                    "additives are put in. They are there to stop it "
                    "being drunk."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s31",
        "band": "standard",
        "text": "Explain why it would be a mistake to assume graphite must be a mixture, just because it looks so unlike a diamond.",
        "options": [
            {
             "text": "Because graphite is actually just as shiny and reflective as a well-polished diamond is, so the two genuinely look far more alike than most people would ever first think",
             "correct": False,
             "why": "They genuinely look very different — a dull grey solid against a clear, faceted crystal. The point is that this difference still says nothing about purity.",
            },
            {
             "text": "Because graphite has never been tested for purity",
             "correct": False,
             "why": "Graphite has been tested and can be very close to pure carbon. The mistake is assuming a test based on looks alone.",
            },
            {
             "text": "Because the mistake assumes appearance decides purity, when the real test is what substances are present — and both can be almost entirely carbon",
             "correct": True,
            },
            {
             "text": "Because graphite is soft enough to rub off on paper and diamond is the hardest thing there is, and only a mixture could ever be that soft rather than a pure substance",
             "correct": False,
             "why": "Hardness is a property, not a count of substances. A pure substance can be soft or hard — the arrangement of the carbon differs, not the number of substances.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-s32",
        "band": "standard",
        "text": "A doctor separates a blood sample into plasma and blood "
                "cells using a centrifuge. Does that separation prove "
                "blood was a mixture to begin with?",
        "options": [
            {"text": "No — the act of separating it might well have created two entirely new substances out of one", "correct": False,
             "why": "Nothing new is made by spinning a sample in a "
                    "centrifuge. It only separates components that were "
                    "already different, already present."},
            {"text": "No — a centrifuge only separates solids from "
                     "liquids, so this proves nothing about purity",
             "correct": False,
             "why": "Whatever the centrifuge sorts by, successfully "
                    "splitting blood into different components shows "
                    "there was more than one thing there to split."},
            {"text": "It cannot be decided without chemically testing "
                     "what comes out", "correct": False,
             "why": "The very fact that separation is possible is itself "
                    "the evidence a mixture was there."},
            {"text": "Yes — you can only separate substances that were "
                     "mixed together in the first place", "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ────────────────────────────────────────
    {
        "id": "c3-01-h09",
        "band": "harder",
        "text": "A supplier offers a block of pure copper and a block of "
                "bronze (copper and tin) at the same price. A sculptor "
                "wants a statue that will survive outdoors for centuries. "
                "Which is the pure one, and is it the better choice?",
        "options": [
            {"text": "The copper is pure, and being pure makes it the "
                     "better choice for durability", "correct": False,
             "why": "Purity says nothing about hardness or durability, "
                    "and pure copper is soft and dents easily."},
            {"text": "The bronze is pure, because tin has been added on "
                     "purpose to strengthen it", "correct": False,
             "why": "Adding on purpose still makes a mixture. Bronze is "
                    "the mixture here, not the pure one."},
            {"text": "The copper is pure, but the bronze mixture is the "
                     "better choice for a statue that must last",
             "correct": True},
            {"text": "Neither is pure, because both have been melted and "
                     "cast in a foundry", "correct": False,
             "why": "Melting and casting does not decide purity. Copper "
                    "is unmixed and pure regardless of how it was "
                    "shaped."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h10",
        "band": "harder",
        "text": "Table salt is refined until it is almost entirely sodium chloride. Sea salt is marketed as \"natural and unrefined\" and contains several other minerals as well as sodium chloride. Which is closer to being a pure substance, and does \"natural\" decide it?",
        "options": [
            {
             "text": "Sea salt is closer to pure — natural products contain fewer substances than processed ones",
             "correct": False,
             "why": "The opposite is shown here — the natural product holds MORE substances, not fewer.",
            },
            {
             "text": "Table salt is closer to pure, and \"natural\" has nothing to do with it",
             "correct": True,
            },
            {
             "text": "Both are equally pure — salt is salt whichever way it has been produced",
             "correct": False,
             "why": "One has been refined down to one substance and the other has several other minerals besides sodium chloride. They are not equally pure.",
            },
            {
             "text": "Table salt is closer to pure — refining is a natural process",
             "correct": False,
             "why": "Refining is not natural, and that is not why it matters. It matters because refining removes the other substances.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h11",
        "band": "harder",
        "text": "A block of dry ice slowly turns entirely into carbon "
                "dioxide gas and vanishes, leaving nothing behind. A "
                "block of ice made by freezing a tray of tap water melts "
                "into a puddle. Which of the two starting blocks was the "
                "pure one?",
        "options": [
            {"text": "The tap water ice — it left a visible puddle, "
                     "which proves it was one substance all along",
             "correct": False,
             "why": "Leaving a visible liquid behind says nothing about "
                    "purity. A mixture leaves a puddle just as easily as "
                    "a pure substance does."},
            {"text": "The dry ice — because it disappeared completely "
                     "rather than leaving a mess", "correct": False,
             "why": "Right verdict, wrong reason — vanishing without "
                    "residue is not the test. How many substances are "
                    "present is."},
            {"text": "The dry ice — carbon dioxide is one substance, "
                     "while tap water has dissolved minerals mixed "
                     "through it", "correct": True},
            {"text": "Neither — both are frozen water in one form or "
                     "another", "correct": False,
             "why": "Dry ice is frozen carbon dioxide, not water in any "
                    "form. The two are entirely different substances."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h12",
        "band": "harder",
        "text": "Distilled vinegar is around 5% acetic acid in water. A bottle of concentrated acetic acid sold to a school laboratory is almost entirely one substance. Which is closer to a pure substance?",
        "options": [
            {
             "text": "The distilled vinegar",
             "correct": False,
             "why": "Distilling here separates the vinegar from a fermented liquid; the result is still mostly water with acetic acid dissolved in it.",
            },
            {
             "text": "Both, equally",
             "correct": False,
             "why": "Sharing a substance's name in the description does not mean the two liquids have the same composition.",
            },
            {
             "text": "Neither of the two liquids",
             "correct": False,
             "why": "A laboratory chemical can be very close to one substance. Assuming otherwise is not a real test.",
            },
            {
             "text": "The concentrated acetic acid",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h13",
        "band": "harder",
        "text": "A collector buys a coin stamped 999.9 fine gold. A "
                "jeweller buys a disc of 9-carat gold (37.5%) at the same "
                "price per gram. Which purchase is closer to a pure "
                "substance, and is that purchase the better one for "
                "making a ring?",
        "options": [
            {"text": "The fine gold coin is closer to pure, but the "
                     "9-carat disc is the better choice for a ring",
             "correct": True},
            {"text": "The fine gold coin is closer to pure, and that "
                     "also makes it the better choice for a ring",
             "correct": False,
             "why": "Purity and suitability are different questions. "
                    "Pure gold is too soft for a ring that has to "
                    "survive daily wear."},
            {"text": "The 9-carat disc is closer to pure, since it has "
                     "been alloyed on purpose by a professional",
             "correct": False,
             "why": "Alloying on purpose still makes a mixture. The "
                    "coin, not the disc, is closer to one substance."},
            {"text": "Neither is closer to pure, because both have been "
                     "through a refinery", "correct": False,
             "why": "Going through a refinery does not equalise them. "
                    "One comes out at 99.99% gold, the other at 37.5%."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h14",
        "band": "harder",
        "text": "Oxygen from a cylinder, air, and argon from a welding cylinder are all invisible. Two of the three are pure. Which two, and what is the one reason that decides it in every case?",
        "options": [
            {
             "text": "Air and argon — both are used for jobs that need a carefully controlled gas supply",
             "correct": False,
             "why": "What a gas is used for has no bearing on how many substances are in it.",
            },
            {
             "text": "Oxygen and argon — each cylinder holds one substance, while air holds several",
             "correct": True,
            },
            {
             "text": "Oxygen and air — both are essential for a flame or a weld to work",
             "correct": False,
             "why": "Air is not pure. It is a mixture of nitrogen, oxygen and other gases, whatever it is used for.",
            },
            {
             "text": "Oxygen and argon — because both are kept under pressure in a cylinder, while the air in a room is not",
             "correct": False,
             "why": "Being stored under pressure is not the test. A cylinder of compressed air is under pressure too and is still a mixture.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h15",
        "band": "harder",
        "text": "Honey contains several natural sugars mixed together. A chemist extracts and purifies just the glucose from it into white glucose powder. Which of the two is closer to a pure substance, and has anything been added to make it that way?",
        "options": [
            {
             "text": "The glucose powder is closer to pure — glucose was added to the honey during the extraction",
             "correct": False,
             "why": "Nothing is added during extraction. The glucose was already there, and the other substances are what get taken away.",
            },
            {
             "text": "The honey is closer to pure — it has not been processed at all",
             "correct": False,
             "why": "Being unprocessed is not the test. The honey still holds several sugars and other substances together.",
            },
            {
             "text": "The glucose powder is closer to pure, and nothing was added — the other substances were removed",
             "correct": True,
            },
            {
             "text": "Both are equally pure — both come from the same jar of raw honey",
             "correct": False,
             "why": "Sharing an origin does not make two samples equally pure. One has been separated down to a single sugar and the other has not.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h16",
        "band": "harder",
        "text": "Pure sodium sets fire to your hand on contact with "
                "water. Petrol, a mixture of hydrocarbons, is also "
                "highly flammable. Distilled water and milk are both "
                "harmless to touch, and one is pure while the other is a "
                "mixture. What do all four together show?",
        "options": [
            {"text": "That mixtures are hazardous only when they are "
                     "liquids", "correct": False,
             "why": "Sea water and air are liquid or gas mixtures and "
                    "neither is hazardous. Hazard has nothing to do with "
                    "the state a mixture is in."},
            {"text": "That pure substances are hazardous only when they "
                     "are metals", "correct": False,
             "why": "Distilled water is a pure substance and is "
                    "harmless. Being a metal is not what makes sodium "
                    "dangerous."},
            {"text": "That two of the four must have been wrongly "
                     "classified", "correct": False,
             "why": "All four verdicts are correct as they stand. The "
                    "four together simply show that hazard and purity "
                    "are unrelated questions."},
            {"text": "That purity says nothing at all about how "
                     "hazardous a substance is", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h17",
        "band": "harder",
        "text": "A packet is filled with pure nitrogen; a second "
                "identical packet is filled with ordinary air. Months "
                "later, the nitrogen packet's crisps are still crisp and "
                "the air packet's are stale. What does the difference "
                "show?",
        "options": [
            {"text": "That the air's mixture of gases included something "
                     "reactive that the pure nitrogen did not",
             "correct": True},
            {"text": "That nitrogen preserves food chemically, turning it "
                     "fresher over time", "correct": False,
             "why": "Nitrogen preserves by NOT reacting, not by making "
                    "anything fresher. It simply avoids the change air "
                    "would have caused."},
            {"text": "That air is heavier than nitrogen and crushed the "
                     "crisps", "correct": False,
             "why": "Nothing here is about weight or crushing. Staleness "
                    "is a chemical change, not physical damage."},
            {"text": "That the two packets must have been stored "
                     "differently", "correct": False,
             "why": "The gas inside is the stated difference, and it is "
                    "enough on its own to explain the result."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h18",
        "band": "harder",
        "text": "A spring produces naturally still water containing several dissolved minerals. A factory adds carbon dioxide to make a sparkling version, and separately distils the spring water to remove almost all the minerals before carbonating it, making a \"purified\" sparkling water. Rank the three from closest to pure to furthest from pure.",
        "options": [
            {
             "text": "Still spring water, then sparkling spring water, then purified sparkling",
             "correct": False,
             "why": "The still spring water still carries every one of its original minerals. Removing them, as the purified version does, moves it closer to pure, not further.",
            },
            {
             "text": "Purified sparkling, then still spring water, then sparkling spring water",
             "correct": True,
            },
            {
             "text": "All three are equally pure, because they all started from the same spring",
             "correct": False,
             "why": "Sharing an origin does not make three different processed products equally pure. Substances were added to one and removed from another.",
            },
            {
             "text": "Sparkling spring water, then purified sparkling, then still spring water",
             "correct": False,
             "why": "The sparkling spring water has BOTH the original minerals and the added gas, which is the most substances of the three, not the fewest.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h19",
        "band": "harder",
        "text": "A furnace melts sand into glass for a window. A refinery "
                "processes the same raw sand into 99.9999999% pure "
                "silicon for a computer chip. Both start from the same "
                "mixture. What decided how pure each final product "
                "needed to be?",
        "options": [
            {"text": "The temperature each was heated to, since higher "
                     "heat always removes more impurities", "correct": False,
             "why": "Melting sand into glass does not remove other "
                    "minerals from it. Heat alone is not what refines "
                    "silicon."},
            {"text": "How much of the raw sand each process used",
             "correct": False,
             "why": "Quantity used has nothing to do with how pure the "
                    "final product is."},
            {"text": "What the product was for — the job it had to do, "
                     "not the material it started from", "correct": True},
            {"text": "Which factory did the processing, since some "
                     "factories are simply better than others",
             "correct": False,
             "why": "This is not about the quality of a factory. It is "
                    "about the purity a particular use actually demands."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h20",
        "band": "harder",
        "text": "Road salt lowers the freezing point of water on an icy "
                "pavement, and car coolant lowers the freezing point of "
                "water in an engine. What do the two have in common, and "
                "is either one \"wrong\" for being a mixture rather than "
                "pure water?",
        "options": [
            {"text": "Both work because salt and ethylene glycol are themselves pure substances that naturally resist freezing on their own, whatever liquid they happen to be mixed into afterwards, whether that liquid is water, oil or anything else entirely",
             "correct": False,
             "why": "What matters is that each is MIXED into water. "
                    "Neither would do this job sitting on its own, "
                    "unmixed with the water it is protecting."},
            {"text": "Coolant is a better mixture than salt water because "
                     "it is man-made", "correct": False,
             "why": "How a mixture is made does not decide how well it "
                    "does its job or whether it is \"better\"."},
            {"text": "Only one of the two is really a mixture — the other "
                     "is a solution and something different",
             "correct": False,
             "why": "A solution is one kind of mixture, not a separate "
                    "category from it. Both examples here are mixtures."},
            {"text": "Both work because a mixture freezes at a lower "
                     "temperature than the pure substance would, and "
                     "neither is \"wrong\" — being a mixture is exactly "
                     "what makes each one useful for its job",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h21",
        "band": "harder",
        "text": "A brewery could, in principle, distil all the water and "
                "flavour compounds out of a batch of beer, leaving close "
                "to pure ethanol behind. What would that show about the "
                "relationship between the beer and the ethanol in it?",
        "options": [
            {"text": "That the same substance can exist inside a mixture "
                     "or on its own, and separating it out does not "
                     "create it — it was already there", "correct": True},
            {"text": "That the whole process of distilling actually changes the ethanol itself into a completely different, chemically purer substance altogether",
             "correct": False,
             "why": "Distilling does not change the ethanol chemically. "
                    "It removes everything else and leaves the same "
                    "substance behind."},
            {"text": "That beer only becomes ethanol once it has been "
                     "distilled", "correct": False,
             "why": "The ethanol is present in the beer from the moment "
                    "fermentation finishes. Distilling only separates it "
                    "out."},
            {"text": "That the flavour compounds and water were never "
                     "really part of the beer", "correct": False,
             "why": "They were genuinely part of the mixture. Removing "
                    "them is what distilling does, not proof they were "
                    "never there."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h22",
        "band": "harder",
        "text": "\"100% cocoa\" chocolate and \"70% cocoa\" chocolate are both sold as bars. Which one, if either, is closer to being a pure substance, and does the percentage on the front decide it?",
        "options": [
            {
             "text": "The 100% bar is pure, and the 70% bar is a mixture",
             "correct": False,
             "why": "Cocoa itself is already at least two substances (solids and butter) mixed together. The 100% bar is a mixture too.",
            },
            {
             "text": "Neither is close to pure — both are mixtures of cocoa solids and cocoa butter, and the 70% bar has added sugar as well — and the percentage names an ingredient, not a substance count",
             "correct": True,
            },
            {
             "text": "The 70% bar is pure, because the remaining 30% is a single added substance",
             "correct": False,
             "why": "The remaining 30% is mostly sugar, usually with an emulsifier or flavouring as well — more substances again, on top of the cocoa's own mixture.",
            },
            {
             "text": "Both bars are equally pure, since chocolate as a whole food product is always officially classed by food scientists as being one single substance, whatever percentage happens to be printed on the wrapper",
             "correct": False,
             "why": "Being one type of food does not make something chemically one substance. Both bars hold several.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h23",
        "band": "harder",
        "text": "A gas supplier sells cylinders of pure oxygen, cylinders of ordinary compressed air, and cylinders of a nitrogen–oxygen blend made up to a customer's order. Which of the three, if any, is a pure substance?",
        "options": [
            {
             "text": "None of the three, because every gas sold in a cylinder has been blended to the customer's requirements",
             "correct": False,
             "why": "The supplier also sells cylinders of pure oxygen, which hold one substance rather than a blend.",
            },
            {
             "text": "The custom blend, because it has been mixed precisely rather than left as it naturally occurs",
             "correct": False,
             "why": "Precise, deliberate mixing still makes a mixture. How carefully something is mixed does not reduce how many substances it contains.",
            },
            {
             "text": "Pure oxygen only — both air and the custom blend mix two or more gases together",
             "correct": True,
            },
            {
             "text": "All three, because all are described using the word \"gas\"",
             "correct": False,
             "why": "Sharing the word gas does not mean sharing a substance count. Oxygen is one gas; air and the blend are each several.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h24",
        "band": "harder",
        "text": "Icing sugar is deliberately mixed with a little cornflour to stop it clumping in damp weather. Why would a baker choose the mixture over pure caster sugar for dusting a cake, even though the caster sugar is the purer of the two?",
        "options": [
            {
             "text": "Because icing sugar is actually purer than ordinary caster sugar once it has been finely sieved and ground down several times over through an increasingly fine mesh",
             "correct": False,
             "why": "Sieving separates lumps; it does not remove the cornflour that is mixed all the way through the powder.",
            },
            {
             "text": "Because cornflour makes the sugar taste sweeter",
             "correct": False,
             "why": "Cornflour is not sweet and is not added for flavour. It is added purely to stop clumping.",
            },
            {
             "text": "Because caster sugar cannot be used for dusting a cake at all",
             "correct": False,
             "why": "Caster sugar can be used for dusting. It is simply more prone to clumping in damp conditions than the mixture is.",
            },
            {
             "text": "Because the practical job — staying a free-flowing powder — is done better by the mixture; \"pure\" does not mean \"better for every job\"",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h25",
        "band": "harder",
        "text": "A car battery needs distilled (pure) water, while a car "
                "radiator needs a mixture of water and antifreeze. What "
                "does the pair show about when purity, and when mixing, "
                "is the right choice?",
        "options": [
            {"text": "That neither purity nor mixing is automatically "
                     "\"better\" — each job decides which one is needed",
             "correct": True},
            {"text": "That a battery is a more advanced piece of "
                     "engineering than a radiator, so it needs the purer "
                     "liquid", "correct": False,
             "why": "How advanced a device is does not decide this. It "
                    "is about what would go wrong with the wrong liquid "
                    "in each case."},
            {"text": "That water should always be kept as completely pure as possible wherever it is used anywhere in a car engine",
             "correct": False,
             "why": "The radiator is the clear counter-example — mixing "
                    "something in is exactly what makes it work properly "
                    "there."},
            {"text": "That distilled water and antifreeze mixture are "
                     "actually the same thing", "correct": False,
             "why": "They are different liquids doing different jobs. "
                    "One is a pure substance and the other is a "
                    "deliberate mixture."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h26",
        "band": "harder",
        "text": "Both a diamond (nearly pure carbon) and a lump of coal (a "
                "mixture of carbon and many other substances) come from "
                "carbon-rich deposits underground, but they look "
                "completely different. What does that pair show about "
                "judging purity by appearance?",
        "options": [
            {"text": "That coal must actually be purer, because it looks "
                     "more like ordinary rock", "correct": False,
             "why": "Ordinary appearance is no more informative than a "
                    "striking one. Coal genuinely does hold several "
                    "substances mixed together."},
            {"text": "That looking completely different does not prove "
                     "two things are made of different substances, or of "
                     "different numbers of substances, either way",
             "correct": True},
            {"text": "That diamond and coal cannot possibly both come from the same element, carbon, since the two materials look absolutely nothing alike to the naked eye, ever",
             "correct": False,
             "why": "They can, and do — the same element can form very "
                    "different-looking materials depending on how it is "
                    "arranged and what else is present."},
            {"text": "That appearance decides purity as long as you look "
                     "closely enough", "correct": False,
             "why": "No amount of close looking told you the ring, the "
                    "milk or the juice were mixtures either. Appearance "
                    "is not the test at any distance."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h27",
        "band": "harder",
        "text": "A cosmetics company sells \"pure\" soap, \"pure\" "
                "shampoo and \"pure\" moisturiser, none of which are pure "
                "substances by the chemist's definition. Is the company "
                "lying?",
        "options": [
            {"text": "Yes — using the word pure on a mixture is always "
                     "false advertising", "correct": False,
             "why": "The everyday meaning of pure (gentle, natural, few "
                    "harsh chemicals) is a real and different use of the "
                    "word, not automatically a lie."},
            {"text": "No, because cosmetics are never checked for purity "
                     "by anybody", "correct": False,
             "why": "Whether or not they are checked has no bearing on "
                    "whether the word is being used honestly in its "
                    "everyday sense."},
            {"text": "Not necessarily — \"pure\" is being used in its "
                     "everyday sense, about gentleness or lack of harsh "
                     "additives, which is a legitimate but different "
                     "claim from the chemist's", "correct": True},
            {"text": "Yes, because only substances that have actually been tested and formally certified inside a proper chemistry laboratory can ever honestly be described as pure, on a label or anywhere else at all", "correct": False,
             "why": "That is the chemist's meaning specifically. The "
                    "everyday meaning does not require laboratory "
                    "testing at all."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h28",
        "band": "harder",
        "text": "Zinc is deliberately coated onto steel to stop it rusting. In a gold ring, copper and silver are deliberately mixed with the gold. Is the reasoning behind the two the same?",
        "options": [
            {
             "text": "No — zinc on its own is a pure metal, so coating steel with it makes the object purer rather than less pure, and a coating of a pure metal always raises the purity of whatever it is put onto",
             "correct": False,
             "why": "Adding a second substance to an object never makes the object purer. The coated steel now holds both steel and zinc.",
            },
            {
             "text": "No — galvanising is done to stop a reaction, and the ring's mixing is done to change appearance",
             "correct": False,
             "why": "The ring's mixing is done for hardness and durability, not appearance — both examples are about a physical property, not looks.",
            },
            {
             "text": "Yes, but only because both examples happen to involve metals",
             "correct": False,
             "why": "The shared reasoning is about choosing a mixture on purpose for a property. It is not specific to metals as a category.",
            },
            {
             "text": "Yes — in both cases a second substance is added on purpose to give the object a property (rust resistance, or hardness) that the single substance did not have alone",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h29",
        "band": "harder",
        "text": "Road salt, sterling silver and odourised natural gas are "
                "all made deliberately less pure than they could be. "
                "What is the one thing all three examples show about the "
                "word \"pure\"?",
        "options": [
            {"text": "That being pure is not automatically the goal — "
                     "sometimes a mixture is chosen on purpose because it "
                     "does the job better or more safely", "correct": True},
            {"text": "That none of the three examples was ever truly a pure substance in the first place, so nothing about any of them has really changed at all, then or now",
             "correct": False,
             "why": "Methane from the ground and silver refined to high "
                    "purity both start close to one substance. Something "
                    "genuinely is mixed in afterwards in each case."},
            {"text": "That mixtures are always safer than pure "
                     "substances", "correct": False,
             "why": "Petrol is a flammable mixture and pure water is "
                    "harmless. Safety and purity are not linked in that "
                    "simple way."},
            {"text": "That all three examples are really about strength, "
                     "not purity", "correct": False,
             "why": "Strength explains the silver, but not the gas (a "
                    "safety smell) or the salt (a lower freezing point) "
                    "— the shared idea is broader than strength alone."},
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h30",
        "band": "harder",
        "text": "A student says: \"surgical spirit being deliberately made undrinkable proves it must be more dangerous than pure ethanol.\" Is that right?",
        "options": [
            {
             "text": "Yes — anything deliberately made impure is being made more dangerous",
             "correct": False,
             "why": "Road salt, sterling silver and odourised gas are all deliberately made impure and none of them is being made more dangerous by it.",
            },
            {
             "text": "No — it is made undrinkable for a legal and safety reason (to stop it being drunk as alcohol), not because the mixture itself is more hazardous to handle than pure ethanol",
             "correct": True,
            },
            {
             "text": "Yes — mixing two liquids together always produces something more hazardous than either liquid was on its own, so any blend of two chemicals has to be handled more carefully than the pure liquids that went into it",
             "correct": False,
             "why": "Mixing does not automatically raise hazard. Road salt and sterling silver are both deliberate mixtures and neither is more dangerous than what went into it.",
            },
            {
             "text": "It cannot be answered, since ethanol and methanol are the same substance",
             "correct": False,
             "why": "They are two different substances. That is exactly why mixing them together makes surgical spirit a mixture rather than a pure substance.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h31",
        "band": "harder",
        "text": "A 9-carat gold ring looks completely uniform all the way through, yet it is a mixture of gold, copper and silver. Diamond and graphite look nothing like each other, yet both can be almost pure carbon. What single idea explains both results?",
        "options": [
            {
             "text": "That metals cannot be judged by appearance, but other materials can",
             "correct": False,
             "why": "The diamond and graphite example shows the same failure of appearance for a non-metal. It is not limited to metals.",
            },
            {
             "text": "That uniform-looking objects are mixtures and different-looking objects are pure",
             "correct": False,
             "why": "That would be a new rule based on looks, and this unit's whole argument is that no such rule exists.",
            },
            {
             "text": "That appearance carries no information about purity at all, in either direction",
             "correct": True,
            },
            {
             "text": "That the gold ring and the two forms of carbon are simply unrelated coincidences that happen to point in opposite directions",
             "correct": False,
             "why": "They are the same underlying point, made twice from opposite directions — looking the same, and looking different — and neither settles it.",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-01-h32",
        "band": "harder",
        "text": "A chemist argues that blood cannot be classified as a "
                "mixture in the same way as sea water, because blood "
                "contains living cells rather than dissolved chemicals. "
                "Evaluate that argument.",
        "options": [
            {"text": "The argument is right, because only non-living "
                     "substances can form real mixtures", "correct": False,
             "why": "Nothing in the definition of a mixture excludes "
                    "living components. Several substances together, "
                    "chemically unjoined, is enough."},
            {"text": "The argument is right, because living blood cells are able to change their own internal composition over time as they grow, divide and eventually die, which no dissolved chemical in sea water could ever do", "correct": False,
             "why": "Whether a component can change over time is a "
                    "different question from whether more than one "
                    "substance is present right now."},
            {"text": "It cannot be evaluated, since blood has never been "
                     "formally tested for purity", "correct": False,
             "why": "The argument can be judged directly against the "
                    "definition of a mixture, without needing a new "
                    "laboratory test."},
            {"text": "The argument is wrong — a mixture is defined by "
                     "having more than one substance present, not by "
                     "whether those substances are dissolved chemicals "
                     "or cells; blood qualifies either way",
             "correct": True},
        ],
        "figure": None,
    },
]
