"""C6 lesson 01 — Acids and alkalis: twelve questions (MRB-269).

The lesson's argument is one shape: acid and alkali are POSITIONS on a scale,
they are read by what a substance does rather than by how it looks, and neither
position is a statement about danger. These twelve probe the angles the mastery
ladder leaves alone.

The distractors are built from the lesson's two declared misconceptions.

`ACID-01` (acids are the dangerous ones; alkalis make things safe) drives the
wrong options in e02, s04, h01 and h03. h01 is the one that matters: it asks
which single observation REFUTES the belief, and three of its four options are
things that are perfectly true and settle nothing — which is the shape of the
mistake, rather than the belief stated flat.

`ACID-02` (a dilute acid is no longer really an acid) drives s01 and h04, where
adding water, or being used up, is treated as ceasing to be an acid. s01 is the
register's own case put as a question about a bottle.

A third strand, everywhere on the page and in neither register entry, is that
NEUTRAL IS A BAND rather than a point. e01 and h02 are built on it: e01 offers
"anything between 6 and 8" as the shape of the wrong idea, and h02 takes clean
rainwater at pH 6 — a number a student expects to be 7 — and asks for the
reason rather than the label.

A fourth strand is that a test is a way of LOOKING. e03 and s02 both offer
weighing, smelling and waiting as alternatives to an indicator, because that is
what a student reaches for when a property has no appearance.

Every question here is new prose, and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape and at its own length, and each is
a mistake a real student actually makes. No correct answer is strictly the
longest in its set by four words or by 1.4x, and the twelve are authored level
across the four answer positions — three apiece — from the start (MRB-278).
"""

UNIT = "C6"
LESSON = "acids-and-alkalis"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c6-01-e01",
        "band": "easier",
        "text": "What is the pH of a neutral substance?",
        "options": [
            {"text": "Exactly 7, which is what pure water reads",
             "correct": True},
            {"text": "Anything between 6 and 8, near the middle",
             "correct": False,
             "why": "Neutral is a single point, not a band. pH 6 is acidic "
                    "and pH 8 is alkaline, however close to the middle they "
                    "look."},
            {"text": "Below 7, which is where lemon juice sits",
             "correct": False,
             "why": "That is the acid half of the scale. Neutral is the "
                    "middle of it, not the acid end."},
            {"text": "Above 7, which is where oven cleaner sits",
             "correct": False,
             "why": "That is the alkali half. Neutral sits between the two "
                    "halves, at 7 exactly."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e02",
        "band": "easier",
        "text": "Four bottles are on the bench. Which is the most dangerous "
                "to get on your skin?",
        "options": [
            {"text": "Lemon juice, because it is an acid", "correct": False,
             "why": "Citric acid at about pH 2, and people drink it. Being an "
                    "acid says which side of 7 it sits on, not how hard it "
                    "hits."},
            {"text": "Oven cleaner, because it is a strong alkali",
             "correct": True},
            {"text": "Salt solution, because it was made from acid",
             "correct": False,
             "why": "It reads pH 7. What it was made from does not survive "
                    "the reaction — a salt is a new substance."},
            {"text": "Pure water, because it has no pH at all",
             "correct": False,
             "why": "Pure water has a pH and it is 7, the definition of "
                    "neutral. Nothing is without one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e03",
        "band": "easier",
        "text": "A drop of vinegar turns litmus red. What does that tell you?",
        "options": [
            {"text": "It is neutral, because red is the middle colour",
             "correct": False,
             "why": "Litmus has two colours and no middle one. It reports a "
                    "side of the scale rather than a position on it."},
            {"text": "It is an alkali, because alkalis turn litmus red",
             "correct": False,
             "why": "The other way round. Alkalis turn litmus blue; red is "
                    "the acid answer."},
            {"text": "It is an acid, because acids turn litmus red",
             "correct": True},
            {"text": "Nothing, because litmus goes red in every liquid",
             "correct": False,
             "why": "Litmus stays its own colour in a neutral solution and "
                    "goes blue in an alkali. It is a test, not a detector."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e04",
        "band": "easier",
        "text": "Garden lime is spread on soil that has turned too acidic for "
                "a crop. Why does that help?",
        "options": [
            {"text": "It washes the acid down out of the topsoil",
             "correct": False,
             "why": "Nothing is washed anywhere. The lime reacts with the "
                    "acid and both are used up where they meet."},
            {"text": "It adds more acid, so the two cancel each other",
             "correct": False,
             "why": "Two acids do not cancel. It takes something from the "
                    "other side of 7 to cancel an acid."},
            {"text": "It dries the soil out so the acid cannot work",
             "correct": False,
             "why": "Acid in dry soil is still acid. The lime changes the "
                    "chemistry rather than the water."},
            {"text": "It is an alkali, so it cancels the acid out",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c6-01-s01",
        "band": "standard",
        "text": "A bottle of concentrated acid is diluted with a very large "
                "amount of water. What is in the bottle now?",
        "options": [
            {"text": "Water, because the acid stopped being acid when it was "
                     "diluted", "correct": False,
             "why": "Diluting makes an acid weaker in effect and leaves it "
                    "unchanged in kind. Every drop of acid in there is still "
                    "acid."},
            {"text": "Acid, weaker in effect, with a pH still below 7",
             "correct": True},
            {"text": "An alkali, because so much neutral water pushed it past "
                     "7", "correct": False,
             "why": "Water is neutral and cannot push anything past 7. It can "
                    "only bring a reading closer to it."},
            {"text": "Acid, with a pH now further below 7 than it was",
             "correct": False,
             "why": "Diluting moves the pH towards 7, not away from it. There "
                    "is less acid in each cm³ afterwards, not more."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s02",
        "band": "standard",
        "text": "Two unlabelled colourless liquids are on the bench: one acid, "
                "one alkali. Which test would tell them apart?",
        "options": [
            {"text": "Weigh equal volumes of each and compare the readings",
             "correct": False,
             "why": "Both are mostly water and both weigh about the same. "
                    "Mass says nothing about which side of 7 a liquid is on."},
            {"text": "Smell each one carefully from a safe distance",
             "correct": False,
             "why": "Neither has to smell of anything, and sodium hydroxide "
                    "does not. Smell is not a test for pH."},
            {"text": "Add a few drops of an indicator to a sample of each",
             "correct": True},
            {"text": "Leave both out and see which one evaporates first",
             "correct": False,
             "why": "Both are water solutions and both evaporate. Waiting "
                    "tells you nothing about which is which."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s03",
        "band": "standard",
        "text": "Copper oxide neutralises acid perfectly well but barely "
                "dissolves in water. What is it?",
        "options": [
            {"text": "An alkali, because neutralising an acid is what alkalis "
                     "do", "correct": False,
             "why": "Every alkali neutralises acid, but not everything that "
                    "neutralises acid is an alkali. An alkali has to dissolve."},
            {"text": "An acid, because it reacts strongly with another acid",
             "correct": False,
             "why": "A substance that reacts WITH acid is the opposite of an "
                    "acid. Two acids do nothing at all to each other."},
            {"text": "Neutral, because it is neither an acid nor an alkali",
             "correct": False,
             "why": "Neutral means it does nothing to an acid. This one does "
                    "— it cancels it out completely."},
            {"text": "A base but not an alkali, because it does not dissolve",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s04",
        "band": "standard",
        "text": "An indigestion tablet dissolved in water reads pH 9. Why is "
                "something like that sold as a medicine?",
        "options": [
            {"text": "It is a mild alkali, so it cancels out excess stomach "
                     "acid", "correct": True},
            {"text": "It is a strong alkali, so it destroys the acid on "
                     "contact", "correct": False,
             "why": "A strong alkali swallowed would do more damage than the "
                    "acid it was sent to deal with. pH 9 is mild on purpose."},
            {"text": "It is an acid, so it makes the stomach less acidic "
                     "overall", "correct": False,
             "why": "Adding acid to acid does not help. Cancelling an acid "
                    "takes something on the other side of 7."},
            {"text": "It is neutral, so it dilutes the stomach acid "
                     "harmlessly", "correct": False,
             "why": "Diluting would take a great deal of water. pH 9 means it "
                    "reacts with the acid rather than watering it down."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c6-01-h01",
        "band": "harder",
        "text": "A student says anything corrosive must be an acid. Which "
                "single observation shows that is wrong?",
        "options": [
            {"text": "Battery acid burns cloth and skin the moment it touches "
                     "them", "correct": False,
             "why": "That is an acid being corrosive, which is what the "
                    "student already believes. It supports the claim instead "
                    "of testing it."},
            {"text": "Lemon juice is an acid and is safe enough to drink",
             "correct": False,
             "why": "That shows some acids are harmless, which is a different "
                    "claim. The student said corrosive things are acids."},
            {"text": "Oven cleaner burns skin badly and reads pH 13",
             "correct": True},
            {"text": "Pure water reads pH 7 and is harmless to touch",
             "correct": False,
             "why": "A harmless neutral liquid tests nothing here. The claim "
                    "is about corrosive things, and water is not one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h02",
        "band": "harder",
        "text": "Rainwater collected cleanly, far from any road, reads pH 6 "
                "rather than 7. What is the best explanation?",
        "options": [
            {"text": "The sample was contaminated by the bottle it was "
                     "collected in", "correct": False,
             "why": "Clean glass changes nothing. A reading of 6 in clean "
                    "rain is normal rather than an error to explain away."},
            {"text": "Rain always picks up acid from the exhausts of passing "
                     "cars", "correct": False,
             "why": "This sample was taken well away from a road, and rain in "
                    "genuinely clean air still reads about 6."},
            {"text": "Pure water is really pH 6 and the figure of 7 is a "
                     "rounding", "correct": False,
             "why": "Pure water is 7 by definition. What has changed here is "
                    "that this water is not pure."},
            {"text": "Carbon dioxide from the air dissolves in it and makes "
                     "it slightly acidic", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h03",
        "band": "harder",
        "text": "Sodium hydroxide splashes onto a hand and the person feels "
                "almost nothing. Why is that more dangerous, not less?",
        "options": [
            {"text": "There is no pain to warn them, so it is left on the "
                     "skin for longer", "correct": True},
            {"text": "It only turns corrosive after a few minutes on warm "
                     "skin", "correct": False,
             "why": "It starts attacking straight away. What is delayed is "
                    "the pain, not the damage."},
            {"text": "Feeling nothing means the alkali is too weak to do any "
                     "harm", "correct": False,
             "why": "Strength and sting are two different things. Sodium "
                    "hydroxide is one of the strongest alkalis in any school "
                    "lab."},
            {"text": "It has to be washed off with a weak acid rather than "
                     "water", "correct": False,
             "why": "Water, under a running tap, for a long time. Adding acid "
                    "to a burn releases heat and makes it worse."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h04",
        "band": "harder",
        "text": "Sodium chloride solution is made by reacting a strong acid "
                "with a strong alkali. Why does it read pH 7?",
        "options": [
            {"text": "The salt holds a little acid and a little alkali, which "
                     "cancel", "correct": False,
             "why": "Neither survives the reaction. What is left is one new "
                    "compound dissolved in water, and it is not acidic at "
                    "all."},
            {"text": "Both were used up making new substances, and neither "
                     "product is acidic", "correct": True},
            {"text": "The salt formed is neutral and it dilutes both of the "
                     "originals", "correct": False,
             "why": "The salt dilutes nothing — it is what the acid and the "
                    "alkali became."},
            {"text": "The acid and the alkali destroyed each other and left "
                     "only water", "correct": False,
             "why": "The salt is dissolved in that water. Boil the water off "
                    "and the crystals are sitting in the dish."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-01-e05",
        "band": "easier",
        "text": "What is a base?",
        "options": [
            {"text": "Any substance that cancels an acid out",
             "correct": True},
            {"text": "Any substance with a pH above 7 that will dissolve "
                     "readily in water and can be poured out of a bottle",
             "correct": False,
             "why": "That describes an alkali, which is one kind of base. "
                    "Copper oxide is a base and barely dissolves at all"},
            {"text": "Any substance that is safe to handle",
             "correct": False,
             "why": "Oven cleaner is a base and will burn skin. Safety is not "
                    "what the word means"},
            {"text": "The liquid at the bottom of a mixture",
             "correct": False,
             "why": "Nothing here is about position. A base is defined by "
                    "what it does to an acid"},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e06",
        "band": "easier",
        "text": "A bottle is labelled corrosive. What does that mean?",
        "options": [
            {"text": "That it is an acid, since corrosive is the warning word "
                     "the law requires on every acid sold in a bottle",
             "correct": False,
             "why": "Strong alkalis are corrosive too. Oven cleaner is the "
                    "most dangerous bottle on the bench"},
            {"text": "That it will attack and destroy materials it touches, "
                     "including skin",
             "correct": True},
            {"text": "That it gives off a gas you should not breathe",
             "correct": False,
             "why": "That is a different hazard with a different label. "
                    "Corrosive is about attacking materials"},
            {"text": "That it must not be mixed with water",
             "correct": False,
             "why": "Many corrosive substances are supplied already dissolved "
                    "in water. The word is about what they attack"},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e07",
        "band": "easier",
        "text": "Two clear colourless liquids sit on the bench and nothing "
                "about them can be seen to differ. What tells them apart?",
        "options": [
            {"text": "Their smell, breathed in over the neck of the bottle",
             "correct": False,
             "why": "Never smell a bottle like that, and it would settle "
                    "nothing anyway. An indicator is the tool"},
            {"text": "Their taste",
             "correct": False,
             "why": "Nothing on a laboratory bench is ever tasted. One of "
                    "these could strip the skin off your hand"},
            {"text": "An indicator, which changes colour depending on which "
                     "one it is in",
             "correct": True},
            {"text": "How thick and syrupy each one is when it is poured",
             "correct": False,
             "why": "How a liquid pours has nothing to do with whether it is "
                    "an acid. Both may pour like water"},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e08",
        "band": "easier",
        "text": "Where in your own body is there acid at about pH 2?",
        "options": [
            {"text": "In the blood",
             "correct": False,
             "why": "Blood is held very close to neutral, a little above 7. "
                    "Acid at pH 2 there would be fatal"},
            {"text": "In the lungs",
             "correct": False,
             "why": "There is no pool of acid in the lungs. The organ that "
                    "runs on acid is lower down"},
            {"text": "In the mouth, which is why teeth have hard enamel on "
                     "the outside of them to stand up to it all day",
             "correct": False,
             "why": "Saliva sits close to neutral. Enamel is attacked by what "
                    "you eat and drink, not by the mouth itself"},
            {"text": "In the stomach",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c6-01-s05",
        "band": "standard",
        "text": "Which of these is an alkali?",
        "options": [
            {"text": "Sodium hydroxide",
             "correct": True},
            {"text": "Copper oxide, which neutralises an acid completely and "
                     "leaves a blue salt behind in the beaker",
             "correct": False,
             "why": "It is a base and not an alkali, because it barely "
                    "dissolves in water"},
            {"text": "Hydrochloric acid",
             "correct": False,
             "why": "An acid is the opposite kind of substance. Its pH is "
                    "below 7"},
            {"text": "Pure water",
             "correct": False,
             "why": "Pure water is neutral at exactly pH 7 — neither one nor "
                    "the other"},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s06",
        "band": "standard",
        "text": "A household cleaner containing ammonia reads pH 11. What is "
                "it, and what would it do to a spill of acid?",
        "options": [
            {"text": "An acid, and it would make an acid spill worse by "
                     "adding more acid to what is already on the floor",
             "correct": False,
             "why": "pH 11 is above 7, so it is an alkali. Acids read below "
                    "7"},
            {"text": "An alkali, and it would cancel the acid out",
             "correct": True},
            {"text": "Neutral, and it would dilute the acid without changing "
                     "its pH",
             "correct": False,
             "why": "Neutral is pH 7 exactly. 11 is a long way above it"},
            {"text": "An alkali, and it would have no effect on an acid",
             "correct": False,
             "why": "Right about what it is and wrong about what it does. "
                    "Cancelling acids out is the definition of an alkali"},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s07",
        "band": "standard",
        "text": "Your stomach runs at about pH 2 — strong enough to dissolve "
                "the meat you eat. Why is the stomach itself not dissolved?",
        "options": [
            {"text": "Because the acid is only made at mealtimes, so the "
                     "stomach spends most of the day at a safe pH",
             "correct": False,
             "why": "Acid is present far more of the time than that, and the "
                    "lining would still need protecting"},
            {"text": "Because stomach lining is made of a material that acid "
                     "cannot attack",
             "correct": False,
             "why": "Acid attacks it perfectly well. Where the protection "
                    "fails, the result is an ulcer"},
            {"text": "Because the lining is coated in mucus and replaced "
                     "constantly",
             "correct": True},
            {"text": "Because the food neutralises the acid as soon as it "
                     "arrives",
             "correct": False,
             "why": "Food is broken down BY the acid rather than cancelling "
                    "it. The stomach stays acidic while it works"},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s08",
        "band": "standard",
        "text": "A gardener treats acidic soil with lime, adds far too much, "
                "and the soil now reads pH 9. What is the problem?",
        "options": [
            {"text": "No problem — pH 9 is above 7, and the crop wanted soil "
                     "that was not acidic",
             "correct": False,
             "why": "The crop needs soil near 7, not above it. pH 9 is two "
                    "steps the wrong way"},
            {"text": "The lime has made the soil more acidic than it was",
             "correct": False,
             "why": "Lime is an alkali and raises the pH. It has gone too far "
                    "in the right direction, not the wrong one"},
            {"text": "The lime will wash away, so nothing has changed",
             "correct": False,
             "why": "It washes out over months. The soil is alkaline now, and "
                    "the crop is planted now"},
            {"text": "The soil has been pushed past neutral and is now "
                     "alkaline, which is just as wrong for the crop",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-01-h05",
        "band": "harder",
        "text": "A concentrated acid is diluted a thousandfold and its pH "
                "rises from 1 to 4. Is it still an acid, and is it still "
                "corrosive?",
        "options": [
            {"text": "Still an acid, and far less corrosive",
             "correct": True},
            {"text": "No longer an acid, and no longer corrosive, because "
                     "adding that much water turns it into something much "
                     "closer to water than to acid",
             "correct": False,
             "why": "pH 4 is still below 7, so every drop of it is still "
                    "acid. Weaker in effect is not the same as changed in "
                    "kind"},
            {"text": "Still an acid, and just as corrosive as before",
             "correct": False,
             "why": "Right about the kind and wrong about the effect. There "
                    "is a thousandth as much acid in each cubic centimetre"},
            {"text": "No longer an acid, but still corrosive",
             "correct": False,
             "why": "Exactly the wrong way round. What changes on diluting is "
                    "how fiercely it acts, not which side of 7 it is on"},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h06",
        "band": "harder",
        "text": "In 1984 an Australian doctor drank a flask of bacteria, gave "
                "himself gastritis, and eventually won a Nobel Prize. What did "
                "that settle?",
        "options": [
            {"text": "That stomach acid is strong enough to dissolve iron "
                     "filings, which nobody had been willing to believe until "
                     "somebody was prepared to swallow some",
             "correct": False,
             "why": "The acid's strength was already known. What was in "
                    "dispute was the cause of ulcers"},
            {"text": "That ulcers are caused by an infection rather than by "
                     "stress",
             "correct": True},
            {"text": "That the stomach lining is replaced constantly",
             "correct": False,
             "why": "True, and not what the experiment was about. It was "
                    "about what damages that lining"},
            {"text": "That drinking bacteria is safe",
             "correct": False,
             "why": "It made him ill, which was the point. Nothing about the "
                    "episode shows it was safe"},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h07",
        "band": "harder",
        "text": "A student proposes emptying the pH 1 bottle and the pH 13 "
                "bottle into the same sink at the same time, so that each "
                "makes the other safe. What is wrong with the plan?",
        "options": [
            {"text": "Nothing at all — an acid and an alkali always cancel "
                     "each other out exactly, whatever amounts of each of them "
                     "happen to be poured in",
             "correct": False,
             "why": "They cancel only if the amounts match. Any excess is "
                    "left in the sink at nearly its original strength"},
            {"text": "An acid and an alkali cannot react with each other at "
                     "all when both are that strong",
             "correct": False,
             "why": "They react extremely readily. That is the trouble — the "
                    "reaction is violent"},
            {"text": "The amounts have to match, and a reaction that "
                     "vigorous gives out a great deal of heat",
             "correct": True},
            {"text": "The two would make a substance more dangerous than "
                     "either",
             "correct": False,
             "why": "The products are a salt and water. The danger is the "
                    "heat and whatever is left over, not a new poison"},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h08",
        "band": "harder",
        "text": "A cleaning bottle is labelled CORROSIVE and gives no pH. "
                "What can you conclude, and what can you not?",
        "options": [
            {"text": "That it is a strong acid, but not how strong, since "
                     "corrosive is a word used only of acids and never of "
                     "anything else",
             "correct": False,
             "why": "Alkalis are corrosive too, and the most dangerous bottle "
                    "on the bench is one of them"},
            {"text": "That it is dangerous, and that its pH must therefore be "
                     "below 7",
             "correct": False,
             "why": "Danger says nothing about which side of 7 a substance "
                    "sits on. That is this lesson's whole point"},
            {"text": "Nothing at all, because a hazard label is not chemical "
                     "information",
             "correct": False,
             "why": "It is real information — it tells you the substance "
                    "attacks materials. It just does not tell you the pH"},
            {"text": "That it will attack materials, but not whether it is an "
                     "acid or an alkali",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 expansion ───────────
    {
        "id": "c6-01-e09",
        "band": "easier",
        "text": "An acid dissolves in water. What does it release into the solution?",
        "options": [
            {"text": "Oxygen", "correct": False,
             "why": "Oxygen is dissolved in ordinary river water and in the air. "
                    "Releasing it has nothing to do with being an acid."},
            {"text": "Hydrogen", "correct": True},
            {"text": "Carbon", "correct": False,
             "why": "Carbon is locked into carbonates and into every food you eat, "
                    "and it is not what an acid puts into solution."},
            {"text": "Chlorine", "correct": False,
             "why": "Chlorine is in hydrochloric acid but not in sulfuric or citric "
                    "acid, so it cannot be the thing they share."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e10",
        "band": "easier",
        "text": "Oven cleaner and drain unblocker both contain the same strong "
                "alkali. Which is it?",
        "options": [
            {"text": "Sodium chloride", "correct": False,
             "why": "Sodium chloride is table salt. It reads pH 7 and would not "
                    "shift a trace of baked-on fat."},
            {"text": "Calcium carbonate", "correct": False,
             "why": "Calcium carbonate is chalk. It is a base, but it barely "
                    "dissolves and is not what is in those bottles."},
            {"text": "Sodium hydroxide", "correct": True},
            {"text": "Citric acid", "correct": False,
             "why": "Citric acid is what makes a lemon sharp. It sits on the acid "
                    "side of the scale, not the alkali side."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e11",
        "band": "easier",
        "text": "Garden lime is spread on fields that have turned too acidic. Which "
                "compound is it?",
        "options": [
            {"text": "Calcium chloride", "correct": False,
             "why": "Calcium chloride is a salt and already neutral, so it has "
                    "nothing to give an acidic soil."},
            {"text": "Sulfuric acid", "correct": False,
             "why": "That would drive the soil further down the scale. Lime has to "
                    "be on the alkali side to do its job."},
            {"text": "Sodium hydroxide", "correct": False,
             "why": "A strong alkali, but far too fierce for a field — it would "
                    "destroy the crop and the life in the soil."},
            {"text": "Calcium hydroxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e12",
        "band": "easier",
        "text": "Which acid gives lemon juice its sharp taste?",
        "options": [
            {"text": "Citric acid", "correct": True},
            {"text": "Ethanoic acid", "correct": False,
             "why": "Ethanoic acid is the acid in vinegar. Lemons contain a "
                    "different one."},
            {"text": "Nitric acid", "correct": False,
             "why": "Nitric acid is a laboratory acid used to make nitrates. No "
                    "fruit contains it."},
            {"text": "Hydrochloric acid", "correct": False,
             "why": "Hydrochloric acid is the acid your own stomach makes. Fruit "
                    "does not contain it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e13",
        "band": "easier",
        "text": "Ethanoic acid is the acid in which everyday liquid?",
        "options": [
            {"text": "Household bleach", "correct": False,
             "why": "Bleach sits on the alkaline side of the scale and contains no "
                    "ethanoic acid at all."},
            {"text": "Washing-up liquid", "correct": False,
             "why": "Washing-up liquid is close to neutral and is not sold as an "
                    "acid of any kind."},
            {"text": "Milk", "correct": False,
             "why": "Milk is very slightly acidic, but the acid in it is lactic acid"
                    " rather than ethanoic acid."},
            {"text": "Vinegar", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e14",
        "band": "easier",
        "text": "Which of these substances is neutral?",
        "options": [
            {"text": "Vinegar", "correct": False,
             "why": "Vinegar is an acid at about pH 3 — sharp to taste and strong "
                    "enough to strip limescale."},
            {"text": "Oven cleaner", "correct": False,
             "why": "Oven cleaner is a strong alkali at about pH 13, as far from "
                    "neutral as battery acid is."},
            {"text": "Lemon juice", "correct": False,
             "why": "Lemon juice is an acid at about pH 2, the same reading as the "
                    "acid in your stomach."},
            {"text": "Pure water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e15",
        "band": "easier",
        "text": "A substance is known to be an alkali. What must be true of its pH?",
        "options": [
            {"text": "It is below 7", "correct": False,
             "why": "Below 7 is the acid half of the scale, so an alkali cannot sit "
                    "there."},
            {"text": "It is above 7", "correct": True},
            {"text": "It is exactly 7", "correct": False,
             "why": "Exactly 7 is neutral, which is neither acidic nor alkaline."},
            {"text": "It could be any value", "correct": False,
             "why": "The pH is what puts a substance on one side or the other, so "
                    "being an alkali fixes it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e16",
        "band": "easier",
        "text": "What does an alkali do to an acid?",
        "options": [
            {"text": "It makes it more acidic", "correct": False,
             "why": "Adding alkali moves a solution up the scale towards 7, never "
                    "further down it."},
            {"text": "It dilutes it without changing it", "correct": False,
             "why": "Adding water dilutes an acid. An alkali reacts with it, which "
                    "is a different thing entirely."},
            {"text": "It cancels it out", "correct": True},
            {"text": "It has no effect on it at all", "correct": False,
             "why": "The two react with each other, which is the reason an "
                    "indigestion tablet works at all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e17",
        "band": "easier",
        "text": "Which statement about bases and alkalis is correct?",
        "options": [
            {"text": "Base and alkali are simply two words for exactly the same thing", "correct": False,
             "why": "They overlap but they are not the same set. The alkalis are "
                    "only the bases that dissolve in water."},
            {"text": "Every base is an alkali, and every alkali is a base as well", "correct": False,
             "why": "Plenty of bases neutralise acid without dissolving in water, "
                    "and those are bases that are not alkalis."},
            {"text": "A base is whatever is left over once an acid has been "
                      "neutralised", "correct": False,
             "why": "A neutralised acid leaves a salt and water. A base is what did "
                    "the neutralising, not what is left afterwards."},
            {"text": "Every alkali is a base, but many bases are not alkalis", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e18",
        "band": "easier",
        "text": "What is the pH of oven cleaner, roughly?",
        "options": [
            {"text": "About 2", "correct": False,
             "why": "About 2 is lemon juice, on the acid side of the scale — the "
                    "opposite of what oven cleaner is."},
            {"text": "About 7", "correct": False,
             "why": "About 7 is pure water. Something reading 7 would not shift "
                    "baked-on fat."},
            {"text": "About 13", "correct": True},
            {"text": "About 0", "correct": False,
             "why": "About 0 is battery acid. Oven cleaner is as far from neutral as"
                    " that, but the other way."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e19",
        "band": "easier",
        "text": "Four bottles read pH 0, pH 3, pH 7 and pH 12. Which is the most "
                "acidic?",
        "options": [
            {"text": "The pH 12 one", "correct": False,
             "why": "12 is the most alkaline of the four, at the opposite end of the"
                    " scale from the acids."},
            {"text": "The pH 3 one", "correct": False,
             "why": "3 is acidic, but 0 is further down the scale and so is more "
                    "acidic still."},
            {"text": "The pH 7 one", "correct": False,
             "why": "7 is neutral, so that bottle is neither acidic nor alkaline."},
            {"text": "The pH 0 one", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e20",
        "band": "easier",
        "text": "Which of these acids is produced inside the human body?",
        "options": [
            {"text": "Citric acid", "correct": False,
             "why": "Citric acid is in lemons and oranges. It arrives with food "
                    "rather than being made by you."},
            {"text": "Sulfuric acid", "correct": False,
             "why": "Sulfuric acid is the acid in a car battery, and nothing in your"
                    " body makes it."},
            {"text": "Hydrochloric acid", "correct": True},
            {"text": "Ethanoic acid", "correct": False,
             "why": "Ethanoic acid is the acid in vinegar, and any you swallow "
                    "arrives on your chips."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e21",
        "band": "easier",
        "text": "A solution is tested and reads pH 9. What is it?",
        "options": [
            {"text": "Alkaline", "correct": True},
            {"text": "Acidic", "correct": False,
             "why": "Acidic means below 7. A reading of 9 is on the other side of "
                    "neutral."},
            {"text": "Neutral", "correct": False,
             "why": "Neutral is 7 exactly. A reading of 9 is above it, and so is "
                    "alkaline."},
            {"text": "Corrosive", "correct": False,
             "why": "Corrosive says what a substance does to materials. It is not a "
                    "position on the pH scale."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e22",
        "band": "easier",
        "text": "Four alkaline products sit on a shelf. Which one is sold to be "
                "swallowed?",
        "options": [
            {"text": "Oven cleaner, for baked-on fat", "correct": False,
             "why": "Sodium hydroxide at about pH 13. It takes fat apart, and it "
                    "would do the same to a throat."},
            {"text": "Drain unblocker, for a blocked pipe", "correct": False,
             "why": "Another strong alkali, sold precisely because it destroys what "
                    "is stuck in the pipe."},
            {"text": "An indigestion tablet, for stomach acid", "correct": True},
            {"text": "Garden lime, for soil that is too acidic", "correct": False,
             "why": "Calcium hydroxide at about pH 12. It is spread on fields by the"
                    " sackful and is not a food."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e23",
        "band": "easier",
        "text": "What goes on before any acid or alkali is opened in a laboratory?",
        "options": [
            {"text": "Eye protection", "correct": True},
            {"text": "A face shield for the strong acids", "correct": False,
             "why": "Dilute acid and dilute alkali both sting badly in the eyes, so "
                    "protection goes on for all of them."},
            {"text": "Nothing, for dilute solutions", "correct": False,
             "why": "Dilute does not mean harmless. A dilute splash still damages an"
                    " unprotected eye."},
            {"text": "Gloves instead of goggles", "correct": False,
             "why": "Gloves protect hands and do nothing for eyes, which are what a "
                    "splash damages most."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e24",
        "band": "easier",
        "text": "Dilute acid splashes onto a student's hand. What should they do?",
        "options": [
            {"text": "Wipe it off with a paper towel and carry on working as before", "correct": False,
             "why": "Wiping spreads it and leaves acid on the skin. It has to be "
                    "washed off with water."},
            {"text": "Rinse it with plenty of cold water and tell the teacher", "correct": True},
            {"text": "Put alkali on it so that the two cancel each other out "
                      "completely", "correct": False,
             "why": "That adds a second corrosive substance, and gives out heat onto"
                    " skin that is already damaged."},
            {"text": "Wait and see whether it starts to hurt at all", "correct": False,
             "why": "Waiting lets the damage go on. A splash is washed off at once, "
                    "whether or not it stings yet."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e25",
        "band": "easier",
        "text": "Sodium hydroxide on the skin feels soapy rather than stinging. What "
                "is it doing?",
        "options": [
            {"text": "Turning the fat in the skin into soap", "correct": True},
            {"text": "Coating the skin in a harmless film", "correct": False,
             "why": "Nothing protective is forming. The skin is being taken apart "
                    "while it feels like nothing at all."},
            {"text": "Drying the skin out, as cold weather does", "correct": False,
             "why": "This is a chemical attack rather than dryness, and it gets "
                    "worse for as long as the alkali is there."},
            {"text": "Nothing at all, because it does not hurt", "correct": False,
             "why": "The absence of pain is the hazard. A strong alkali does real "
                    "damage with no warning signal."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s09",
        "band": "standard",
        "text": "A cleaning bottle carries the corrosive hazard symbol. What does "
                "that tell the person using it?",
        "options": [
            {"text": "Keep it off skin and eyes, whether it is acid or alkali", "correct": True},
            {"text": "Keep it off skin, since only acids carry it", "correct": False,
             "why": "Strong alkalis carry it too. Oven cleaner is corrosive and is "
                    "not an acid."},
            {"text": "Dilute it before use, since that takes the hazard away", "correct": False,
             "why": "Diluting makes it act less fiercely, but it does not turn a "
                    "corrosive product into a safe one."},
            {"text": "Store it away from food, and nothing more", "correct": False,
             "why": "Sensible, but the symbol is about what the contents do to "
                    "whatever they touch, including skin."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s10",
        "band": "standard",
        "text": "Pure water reads pH 7 exactly, but tap water usually reads slightly "
                "either side of it. Suggest why.",
        "options": [
            {"text": "Tap water is not really water but a different substance", "correct": False,
             "why": "It is water with small amounts of other things dissolved in it,"
                    " which is not the same claim."},
            {"text": "Tap water carries substances dissolved from the rock it "
                      "travelled through", "correct": True},
            {"text": "Tap water has been heated on its way to the tap, and heating "
                      "moves the pH upwards", "correct": False,
             "why": "Warming a solution does not shift it across the scale. What is "
                    "dissolved in it does."},
            {"text": "Tap water is older, and a pH reading drifts with time on its "
                      "own", "correct": False,
             "why": "Age changes nothing by itself. A reading moves when something "
                    "dissolves into the water."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s11",
        "band": "standard",
        "text": "Indigestion tablets contain magnesium hydroxide rather than sodium "
                "hydroxide, though both cancel acids out. Explain the choice.",
        "options": [
            {"text": "Sodium hydroxide costs a great deal more per kilogram than "
                      "magnesium hydroxide does", "correct": False,
             "why": "Cost is not the reason. Sodium hydroxide is cheap, and it is "
                    "still never put in a medicine."},
            {"text": "Sodium hydroxide will not neutralise stomach acid at all", "correct": False,
             "why": "It neutralises acid perfectly well. That is the problem — it "
                    "would not stop at the acid."},
            {"text": "Magnesium hydroxide is a mild base and sodium hydroxide is a "
                      "strong alkali", "correct": True},
            {"text": "Magnesium hydroxide dissolves in water, while sodium hydroxide "
                      "will not dissolve at all", "correct": False,
             "why": "Sodium hydroxide dissolves readily. It is one of the most "
                    "soluble alkalis there is."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s12",
        "band": "standard",
        "text": "An alkali is defined as a base that dissolves in water. Why does the"
                " definition need the word dissolves?",
        "options": [
            {"text": "Because a base only works on an acid once it has dissolved", "correct": False,
             "why": "An insoluble base neutralises acid perfectly well while sitting"
                    " on the bottom of the beaker."},
            {"text": "Because plenty of bases neutralise acid without ever dissolving"
                      " in water", "correct": True},
            {"text": "Because a base that dissolves is stronger than one that does "
                      "not", "correct": False,
             "why": "Dissolving says nothing about strength. It decides whether the "
                    "base is called an alkali."},
            {"text": "Because water is needed before a pH can be read at all", "correct": False,
             "why": "That is true of measuring a pH, but it is not why the word "
                    "alkali is narrower than the word base."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s13",
        "band": "standard",
        "text": "Most of the acids in a house are in the food cupboard and most of "
                "the alkalis are in the cleaning cupboard. Suggest why.",
        "options": [
            {"text": "Acids are always safe to eat and alkalis never are", "correct": False,
             "why": "Battery acid is an acid nobody could eat, and an indigestion "
                    "tablet is an alkali sold to be swallowed."},
            {"text": "Many foods taste sharp because of weak acids, and grease is "
                      "stripped by strong alkalis", "correct": True},
            {"text": "Alkalis have to be kept cool and dark, so they are always "
                      "stored well away from a warm kitchen", "correct": False,
             "why": "Storage temperature has nothing to do with it. The split "
                    "follows what each is for."},
            {"text": "Acids react with food, so food is kept beside them on purpose", "correct": False,
             "why": "The acids are already in the food rather than reacting with it "
                    "from the next shelf."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s14",
        "band": "standard",
        "text": "Two colourless liquids are the same temperature, pour the same and "
                "smell of nothing. What does that rule out?",
        "options": [
            {"text": "Nothing useful, because a careful enough look will always "
                      "separate any two liquids in the end", "correct": False,
             "why": "Every physical observation has already been made here, and none"
                    " of them separated the two."},
            {"text": "Only touch, so one careful drop on the skin would still be the "
                      "quickest way to decide", "correct": False,
             "why": "Both are corrosive, and one of them gives no warning sting at "
                    "all while it damages skin."},
            {"text": "Only smell, so weighing equal volumes would still settle which "
                      "is which", "correct": False,
             "why": "Equal volumes of dilute acid and dilute alkali weigh almost "
                    "exactly the same."},
            {"text": "Every physical observation, leaving only a test that makes them"
                      " react with something", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s15",
        "band": "standard",
        "text": "Sodium hydroxide takes fat apart chemically. What does that single "
                "fact explain?",
        "options": [
            {"text": "Why it clears a greasy drain, and why it destroys skin", "correct": True},
            {"text": "Why it clears a drain, but not why it is dangerous to touch", "correct": False,
             "why": "Skin contains fat too, so the same action that clears the pipe "
                    "is the one that does the damage."},
            {"text": "Why it is dangerous to touch, but not why it clears a drain", "correct": False,
             "why": "What blocks a drain is largely fat, so this is exactly how the "
                    "product does its job."},
            {"text": "Neither, since dissolving fat is a physical change rather than "
                      "a reaction", "correct": False,
             "why": "The fat is not simply dissolved. It is turned into something "
                    "else, which is why the change cannot be undone."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s16",
        "band": "standard",
        "text": "A chemist sells a tablet that cancels out stomach acid. What "
                "property must the alkali in it have?",
        "options": [
            {"text": "It must be the strongest alkali available, so that little of it"
                      " is needed", "correct": False,
             "why": "A strong alkali would attack the stomach lining the way the "
                    "acid does. Strength is the wrong target."},
            {"text": "It must be an acid as well, so that it can work in either "
                      "direction", "correct": False,
             "why": "Nothing is both at once, and only the alkali side can cancel "
                    "out an excess of acid."},
            {"text": "It must be mild — enough to cancel the acid, gentle enough to "
                      "swallow", "correct": True},
            {"text": "It must be insoluble, so that it passes through without "
                      "reacting", "correct": False,
             "why": "Something that never reacts would do nothing about the acid it "
                    "was taken for."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s17",
        "band": "standard",
        "text": "Eye protection is required for dilute acid and dilute alkali, not "
                "only for the concentrated bottles. Why?",
        "options": [
            {"text": "Because a dilute solution is really a concentrated one that has"
                      " separated out", "correct": False,
             "why": "Diluting spreads the acid evenly through the water. It does not"
                    " leave concentrated pockets behind."},
            {"text": "Because the eye is damaged by even a dilute splash, long before"
                      " it would mark skin", "correct": True},
            {"text": "Because dilute solutions turn back into concentrated ones as "
                      "the water evaporates off", "correct": False,
             "why": "Nothing evaporates fast enough to matter in the second a splash"
                    " takes to reach an eye."},
            {"text": "Because goggles are needed for every laboratory task, whatever "
                      "is on the bench", "correct": False,
             "why": "The rule here is not a blanket one. It exists because of what "
                    "these particular solutions do to an eye."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s18",
        "band": "standard",
        "text": "Alkali splashes on a hand. Why is it washed off with a great deal of"
                " water rather than treated with dilute acid?",
        "options": [
            {"text": "Because acid would simply not react with an alkali once it was "
                      "sitting on skin", "correct": False,
             "why": "The two would react. The trouble is what the reaction does "
                    "where it is happening."},
            {"text": "Because acid is a second corrosive substance, and the reaction "
                      "gives out heat", "correct": True},
            {"text": "Because water is the only liquid in the room that will lift an "
                      "alkali off skin", "correct": False,
             "why": "Water works by carrying the alkali away. It is the quantity "
                    "that matters, not a special property."},
            {"text": "Because acid would drive the skin below pH 7, and that is "
                      "always harmful to it", "correct": False,
             "why": "Skin is slightly acidic already. The objection is the corrosive"
                    " acid and the heat, not the number."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s19",
        "band": "standard",
        "text": "The same vinegar strips limescale off a kettle and goes on chips. "
                "What does that show about acids?",
        "options": [
            {"text": "That vinegar is a special case, and other acids are only ever "
                      "one or the other", "correct": False,
             "why": "Citric acid does both as well — it cleans and it is eaten. "
                    "Vinegar is not unusual."},
            {"text": "That limescale is a food, since the same liquid deals with both", "correct": False,
             "why": "Limescale is a carbonate deposit. Acting on it and being edible"
                    " are unrelated facts about the acid."},
            {"text": "That being an acid says which side of 7 it sits on, not how "
                      "fiercely it acts", "correct": True},
            {"text": "That an acid becomes weaker once it has been used for cleaning", "correct": False,
             "why": "The bottle on the chip shop counter has never cleaned anything,"
                    " and it is the same acid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s20",
        "band": "standard",
        "text": "Put these in order from most acidic to most alkaline: pure water, "
                "oven cleaner, battery acid, vinegar.",
        "options": [
            {"text": "Battery acid, vinegar, pure water, oven cleaner", "correct": True},
            {"text": "Vinegar, battery acid, pure water, oven cleaner", "correct": False,
             "why": "Battery acid is about pH 0 and vinegar about pH 3, so the "
                    "battery acid comes first."},
            {"text": "Oven cleaner, battery acid, vinegar, pure water", "correct": False,
             "why": "Oven cleaner is the most alkaline of the four, so it belongs at"
                    " the far end rather than the near one."},
            {"text": "Battery acid, vinegar, oven cleaner, pure water", "correct": False,
             "why": "Pure water at 7 sits between the acids and the alkali, not "
                    "beyond the alkali."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s21",
        "band": "standard",
        "text": "A student says lemon juice cannot be a real acid, because you can "
                "drink it. Where does the reasoning go wrong?",
        "options": [
            {"text": "It assumes every acid is a laboratory chemical", "correct": False,
             "why": "Acids are all through the food cupboard and in your own "
                    "stomach, not only on a bench."},
            {"text": "It assumes citric acid is far too corrosive to drink", "correct": False,
             "why": "People drink it by the glass. The juice really is safe to "
                    "swallow."},
            {"text": "It assumes the sharp taste of lemon juice comes from its sugar", "correct": False,
             "why": "Citric acid is genuinely in the fruit, at about pH 2, and it is"
                    " what makes it sharp."},
            {"text": "It assumes being an acid and being dangerous are the same "
                      "question", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h09",
        "band": "harder",
        "text": "The definition of an acid says it releases hydrogen into solution "
                "when it dissolves in water. Why does water appear in it at all?",
        "options": [
            {"text": "Because water is itself a weak acid, and it is what supplies "
                      "the hydrogen", "correct": False,
             "why": "The hydrogen comes out of the acid. Water reads pH 7 and "
                    "supplies nothing."},
            {"text": "Because the acid cannot release anything until it is in "
                      "solution, so a dry acid does nothing", "correct": True},
            {"text": "Because only a solution can ever be corrosive, so a dry solid "
                      "acid is completely harmless to handle", "correct": False,
             "why": "Solid acids can do serious damage, particularly once they meet "
                    "the moisture on skin."},
            {"text": "Because water dilutes the acid, and a pH can only be measured "
                      "on a dilute solution", "correct": False,
             "why": "Concentrated solutions have a pH as well. The point is about "
                    "releasing hydrogen, not about measuring."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h10",
        "band": "harder",
        "text": "A student treats the words strong and concentrated as meaning the "
                "same thing about an acid. What are they missing?",
        "options": [
            {"text": "Nothing — the two words describe the same property and can be "
                      "swapped freely", "correct": False,
             "why": "They answer different questions, and a bottle can be "
                    "concentrated without being a strong acid."},
            {"text": "That concentrated means fiercer, while strong only means there "
                      "is a great deal of the acid there", "correct": False,
             "why": "This has the two the wrong way round. Concentration is the how-"
                    "much question."},
            {"text": "That concentrated says how much acid is in each cm³, while "
                      "strong says how fiercely it acts", "correct": True},
            {"text": "That strong describes a solid acid, while concentrated "
                      "describes the same acid once it is in solution", "correct": False,
             "why": "Neither word is about the state it is in. Both describe "
                    "solutions on a bench."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h11",
        "band": "harder",
        "text": "A student argues that since an indigestion tablet works by being "
                "alkaline, a stronger alkali would work better. Evaluate that.",
        "options": [
            {"text": "Correct, because a stronger alkali cancels more acid for the "
                      "same mass swallowed", "correct": False,
             "why": "It would cancel the acid and then keep going, attacking the "
                    "stomach itself."},
            {"text": "Correct, because the extra alkali is simply carried out of the "
                      "body unused", "correct": False,
             "why": "Nothing is simply carried through unchanged. A strong alkali "
                    "reacts with whatever it touches."},
            {"text": "Wrong, because a strong alkali cannot neutralise hydrochloric "
                      "acid the way a mild one can", "correct": False,
             "why": "It neutralises it very effectively. The objection is what else "
                    "it does on the way past."},
            {"text": "Wrong, because a strong alkali would attack the stomach as "
                      "badly as excess acid does", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h12",
        "band": "harder",
        "text": "A student proposes tasting an unlabelled dilute solution, arguing "
                "that lemon juice is an acid and is safe to drink. Evaluate the "
                "argument.",
        "options": [
            {"text": "Sound, because any acid dilute enough to be tasted is dilute "
                      "enough to be safe", "correct": False,
             "why": "Dilute sodium hydroxide is not an acid at all, and a dilute "
                    "strong acid still attacks tooth enamel."},
            {"text": "Unsound, because the bottle is unidentified and only known "
                      "substances can be judged safe", "correct": True},
            {"text": "Sound, because a pH reading anywhere above 2 means a solution "
                      "can safely be tasted without harm", "correct": False,
             "why": "Oven cleaner reads 13, which is above 2 and would burn a mouth "
                    "badly."},
            {"text": "Unsound, because lemon juice is not really an acid and so "
                      "proves nothing", "correct": False,
             "why": "Lemon juice genuinely is an acid. The flaw is in arguing from a"
                    " known bottle to an unknown one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h13",
        "band": "harder",
        "text": "Why is neutral a more useful word to a chemist than safe?",
        "options": [
            {"text": "Because neutral is a measured position on a scale, while safe "
                      "depends on how much and on what it touches", "correct": True},
            {"text": "Because every neutral substance is safe by definition, so the "
                      "second word adds nothing at all to the description", "correct": False,
             "why": "A neutral solution can still be scalding hot or poisonous. "
                    "Neutral is only about pH."},
            {"text": "Because safe is the measured quantity here, and neutral is only"
                      " an impression taken off a printed colour chart", "correct": False,
             "why": "This is the wrong way round. Neutral is the number; safe is the"
                    " judgement."},
            {"text": "Because every substance is neutral somewhere, so the word "
                      "applies to all of them", "correct": False,
             "why": "Neutral names one point on the scale, and most substances do "
                    "not sit on it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h14",
        "band": "harder",
        "text": "A technician is told only the pH of two spills and asked which to "
                "deal with first. Why can that not be decided?",
        "options": [
            {"text": "Because a pH reading is unreliable unless the same meter "
                      "measured both spills", "correct": False,
             "why": "Assume both readings are good. The gap is in what pH reports, "
                    "not in how it was taken."},
            {"text": "Because pH only applies to laboratory solutions and not to a "
                      "spill on a floor", "correct": False,
             "why": "A spilled solution has a pH like any other. The problem is what"
                    " that number leaves out."},
            {"text": "Because the two readings would have to be on opposite sides of "
                      "7 before they could sensibly be compared", "correct": False,
             "why": "Two acids can be compared perfectly well. Which side of 7 they "
                    "sit on is not the missing information."},
            {"text": "Because pH says how far from neutral each is, not how much "
                      "there is or what it is spreading across", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h15",
        "band": "harder",
        "text": "Calcium hydroxide is spread on acidic farmland but sodium hydroxide "
                "never is, although both cancel acids out. Suggest why.",
        "options": [
            {"text": "Sodium hydroxide on its own is not alkaline enough to shift the"
                      " pH of a whole field of crops", "correct": False,
             "why": "It is one of the strongest alkalis there is. Being too weak is "
                    "not the objection."},
            {"text": "Calcium hydroxide is an acid, which is what an acidic soil "
                      "actually needs", "correct": False,
             "why": "Calcium hydroxide is an alkali at about pH 12. Adding acid "
                    "would make an acidic field worse."},
            {"text": "Sodium hydroxide reacts with water, so it would all be gone "
                      "long before it ever reached the soil", "correct": False,
             "why": "It dissolves in water rather than being destroyed by it, and "
                    "would arrive in the ground fully active."},
            {"text": "Sodium hydroxide is a strong alkali that would damage the crop "
                      "and the life in the soil", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h16",
        "band": "harder",
        "text": "Laboratory dilute hydrochloric acid and kitchen vinegar both remove "
                "limescale. Compare them as a way of doing it.",
        "options": [
            {"text": "The vinegar works and the acid does not, because only food "
                      "acids attack limescale", "correct": False,
             "why": "Both attack it. Limescale does not care whether the acid came "
                    "from a kitchen."},
            {"text": "They are identical in every way, since both are acids and "
                      "limescale is limescale", "correct": False,
             "why": "Being on the same side of 7 does not make two bottles equally "
                    "fierce or equally safe to keep."},
            {"text": "The laboratory acid works faster, but the vinegar is the one "
                      "that can be kept in a kitchen", "correct": True},
            {"text": "The laboratory acid is safer, because it is sold labelled as a "
                      "chemical", "correct": False,
             "why": "A label describes a hazard rather than removing it. Dilute "
                    "hydrochloric acid is the more dangerous bottle."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e26",
        "band": "easier",
        "text": "Which acid is inside a car battery?",
        "options": [
            {"text": "Sulfuric acid", "correct": True},
            {"text": "Citric acid", "correct": False,
             "why": "Citric acid is the mild acid in fruit, and it would not "
                    "attack metal the way battery acid does."},
            {"text": "Ethanoic acid", "correct": False,
             "why": "Ethanoic acid is the acid in vinegar, weak enough to put on "
                    "food."},
            {"text": "Carbonic acid", "correct": False,
             "why": "Carbonic acid is the very weak acid made when carbon dioxide "
                    "dissolves in water."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e27",
        "band": "easier",
        "text": "Sugar is stirred into water and the solution has no effect on an"
                " indicator at all. What is the solution?",
        "options": [
            {"text": "Alkaline, because sugar dissolves so easily in water",
             "correct": False,
             "why": "Dissolving easily has nothing to do with which side of 7 a "
                    "solution sits on."},
            {"text": "Neutral", "correct": True},
            {"text": "Acidic, because sugar is a food and most foods are acids",
             "correct": False,
             "why": "Many foods are acidic, but sugar solution is not one of "
                    "them."},
            {"text": "Both acidic and alkaline at the same time", "correct": False,
             "why": "Nothing is both; a solution sits on one side of 7 or exactly "
                    "on it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e28",
        "band": "easier",
        "text": "Eight bottles are sorted into acid, alkali and neutral. Three are"
                " acids and three are alkalis. How many are neutral?",
        "options": [
            {"text": "None of them", "correct": False,
             "why": "Three and three leave two bottles unaccounted for."},
            {"text": "One", "correct": False,
             "why": "That leaves one of the eight bottles in no group at all."},
            {"text": "Four", "correct": False,
             "why": "That would make ten bottles altogether, which is more than "
                    "were on the bench."},
            {"text": "Two", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e29",
        "band": "easier",
        "text": "A jar of dry acid crystals does nothing at all to an indicator. What"
                " has to happen before the acid can act?",
        "options": [
            {"text": "It has to be warmed until it melts", "correct": False,
             "why": "Melting an acid does not let it release hydrogen; it has to "
                    "be in solution."},
            {"text": "It has to dissolve in water", "correct": True},
            {"text": "It has to be crushed into a fine powder", "correct": False,
             "why": "A fine powder is still dry, and still does nothing to an "
                    "indicator."},
            {"text": "It has to be mixed with an alkali", "correct": False,
             "why": "An alkali would cancel it out rather than letting it behave "
                    "as an acid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e30",
        "band": "easier",
        "text": "A label says the acid in the bottle is dilute. What does dilute mean?",
        "options": [
            {"text": "It has been mixed with a large amount of water",
             "correct": True},
            {"text": "It has been made from a weaker kind of acid",
             "correct": False,
             "why": "Dilute says how much water has been added, not which acid "
                    "was used."},
            {"text": "It has stopped being an acid altogether", "correct": False,
             "why": "Every drop of a dilute acid is still acid, with a pH below "
                    "7."},
            {"text": "It has been left open so some has evaporated",
             "correct": False,
             "why": "Evaporating water away would make it less dilute rather than "
                    "more."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e31",
        "band": "easier",
        "text": "Most of the drinks in a supermarket read a little below pH 7. What"
                " does that make them?",
        "options": [
            {"text": "Strongly alkaline", "correct": False,
             "why": "Anything alkaline reads above 7, not below it."},
            {"text": "Slightly acidic", "correct": True},
            {"text": "Exactly neutral", "correct": False,
             "why": "Neutral is 7 exactly, and these readings are below that."},
            {"text": "Slightly alkaline", "correct": False,
             "why": "Below 7 is the acid side of the scale, whichever way the "
                    "reading leans."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e32",
        "band": "easier",
        "text": "What is the pH of lemon juice, roughly?",
        "options": [
            {"text": "About 7, the same as pure water", "correct": False,
             "why": "Lemon juice is sharply acidic, which puts it well below 7."},
            {"text": "About 9, a little above neutral", "correct": False,
             "why": "A reading above 7 would make it an alkali, which lemon juice "
                    "is not."},
            {"text": "About 2", "correct": True},
            {"text": "About 13, the same as oven cleaner", "correct": False,
             "why": "That is the far alkaline end of the scale, and nothing "
                    "edible sits there."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s22",
        "band": "standard",
        "text": "A student is told only that a substance is a base. State what that"
                " does not tell them.",
        "options": [
            {"text": "Whether it cancels an acid out", "correct": False,
             "why": "Cancelling an acid out is what the word base means, so that "
                    "much is settled."},
            {"text": "Whether it will dissolve in water", "correct": True},
            {"text": "Whether its pH is below 7", "correct": False,
             "why": "A base is never on the acid side of the scale, so that is "
                    "settled too."},
            {"text": "Whether it is a substance at all", "correct": False,
             "why": "Calling something a base already says it is a substance."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s23",
        "band": "standard",
        "text": "A bottle of sodium hydroxide solution reading pH 13 is diluted with a"
                " very large amount of water. Predict the new reading.",
        "options": [
            {"text": "Below 7, because adding water pushes a solution past neutral",
             "correct": False,
             "why": "Water cannot push a solution to the other side of the scale; "
                    "it only moves it towards the middle."},
            {"text": "Still 13, because the substance in the bottle has not "
                      "changed", "correct": False,
             "why": "The substance is the same, but there is far less of it in "
                    "each cm³, which is what pH reads."},
            {"text": "Above 7 but closer to it, such as 9", "correct": True},
            {"text": "Exactly 7, because water is neutral and there is a lot of "
                      "it", "correct": False,
             "why": "Diluting moves a reading towards 7 without ever quite "
                    "arriving there."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s24",
        "band": "standard",
        "text": "A colourless liquid in an unlabelled bottle is found at the back of a"
                " cupboard. Explain why it is treated as dangerous.",
        "options": [
            {"text": "Because an unlabelled liquid is always an acid",
             "correct": False,
             "why": "It could be anything at all, which is the reason for the "
                    "caution rather than an argument that it is acid."},
            {"text": "Because liquids become dangerous if they are stored a long "
                      "time", "correct": False,
             "why": "Age is not the problem; not knowing what is in the bottle "
                    "is."},
            {"text": "Because colourless liquids are the hazardous ones",
             "correct": False,
             "why": "Water is colourless and harmless; colour says nothing about "
                    "hazard."},
            {"text": "Because nothing about its appearance can show what it is",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s25",
        "band": "standard",
        "text": "A field reads pH 5. Lime is spread and it reads pH 6.5 a month later."
                " Has the soil become alkaline?",
        "options": [
            {"text": "No — it is less acidic, but it is still below 7",
             "correct": True},
            {"text": "Yes, because lime is an alkali and lime was added to it",
             "correct": False,
             "why": "Adding an alkali moves the reading up; it does not make the "
                    "soil alkaline until it passes 7."},
            {"text": "Yes, because the pH went up and any rise means alkaline",
             "correct": False,
             "why": "A rise says the reading moved, and alkaline means it moved "
                    "past 7."},
            {"text": "No, because lime cannot change the pH of soil at all",
             "correct": False,
             "why": "It plainly did change it, which is why fields are limed in "
                    "the first place."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s26",
        "band": "standard",
        "text": "The stomach lining is coated in mucus that is replaced constantly."
                " Suggest what would happen if that coating stopped being made.",
        "options": [
            {"text": "The stomach would stop producing any acid of its own",
             "correct": False,
             "why": "The acid is made by the stomach whether the coating is there "
                    "or not."},
            {"text": "The acid would start to attack the stomach wall itself",
             "correct": True},
            {"text": "The food would no longer be broken down by the acid",
             "correct": False,
             "why": "The acid would go on working on food; it is the wall that "
                    "loses its protection."},
            {"text": "The acid in the stomach would be neutralised by the food",
             "correct": False,
             "why": "Food does not neutralise stomach acid, and the coating has "
                    "nothing to do with food."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s27",
        "band": "standard",
        "text": "A dilute acid spill is mopped up with a cloth, and the cloth is"
                " dropped straight into an open bin. Explain why that is unsafe.",
        "options": [
            {"text": "The cloth will set alight once the acid dries out",
             "correct": False,
             "why": "Dilute acid does not set cloth alight; the danger is what it "
                    "still attacks."},
            {"text": "The acid turns into a gas in the bin and fills the room",
             "correct": False,
             "why": "The acid stays in the cloth as a liquid rather than becoming "
                    "a gas."},
            {"text": "The acid is still acid, and will attack whatever it touches",
             "correct": True},
            {"text": "The cloth becomes neutral, so nobody knows it was used",
             "correct": False,
             "why": "Nothing has neutralised it; soaking an acid up does not "
                    "cancel it out."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s28",
        "band": "standard",
        "text": "Two solutions are on the shelf: one reads pH 6 and one reads pH 8."
                " Which would you use on a spill of acid, and why?",
        "options": [
            {"text": "The pH 6 one, because it is closer to neutral than the "
                      "other", "correct": False,
             "why": "It is itself on the acid side, so it adds to the spill "
                    "rather than cancelling it."},
            {"text": "The pH 8 one, because it is on the alkaline side of 7",
             "correct": True},
            {"text": "Either, because both are close enough to neutral to work",
             "correct": False,
             "why": "Only a substance above 7 can cancel an acid out, however "
                    "close to 7 the other is."},
            {"text": "Neither, because a spill of acid can only be dealt with by "
                      "an acid", "correct": False,
             "why": "Acid does not cancel acid; the opposite kind of substance is "
                    "what is needed."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s29",
        "band": "standard",
        "text": "A technician pours a little of a solution into a test tube and tests"
                " that, rather than dropping indicator into the stock bottle. Explain"
                " why.",
        "options": [
            {"text": "Because indicator does not work in a large volume of liquid",
             "correct": False,
             "why": "A few drops work in any volume; the trouble is what is left "
                    "behind afterwards."},
            {"text": "Because the rest of the bottle is left clean enough to use",
             "correct": True},
            {"text": "Because a test tube gives a more accurate pH than a bottle "
                      "does", "correct": False,
             "why": "The container does not change the reading; the same solution "
                    "reads the same in both."},
            {"text": "Because indicator reacts with glass bottles and spoils the "
                      "colour", "correct": False,
             "why": "Indicator does not attack glass, and stock bottles are glass "
                    "in any case."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s30",
        "band": "standard",
        "text": "Two unlabelled colourless liquids are weighed, and equal volumes come"
                " out at almost exactly the same mass. Explain why that settles"
                " nothing.",
        "options": [
            {"text": "Because a balance is never accurate enough for liquids",
             "correct": False,
             "why": "Balances weigh liquids perfectly well; the trouble is that "
                    "mass is the wrong question here."},
            {"text": "Because both liquids would have to be dried out first",
             "correct": False,
             "why": "Drying them out destroys the solutions without answering "
                    "which was which."},
            {"text": "Because being acid or alkali is not something a mass can "
                      "show", "correct": True},
            {"text": "Because the acid always weighs more, so equal masses mean "
                      "neither is acid", "correct": False,
             "why": "There is no rule that an acid weighs more, and neither "
                    "liquid stopped being what it is."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s31",
        "band": "standard",
        "text": "A pupil writes that oven cleaner must be safe on the hands because it"
                " is not an acid. Explain the error.",
        "options": [
            {"text": "Oven cleaner is in fact a weak acid rather than an alkali",
             "correct": False,
             "why": "It is a strong alkali, which is precisely why it strips baked-"
                    "on fat."},
            {"text": "Being an alkali rather than an acid does not make something "
                      "safe", "correct": True},
            {"text": "Oven cleaner is safe on the hands, so the reasoning reaches "
                      "the right end", "correct": False,
             "why": "It attacks skin badly, so the conclusion is wrong as well as "
                    "the reasoning."},
            {"text": "Only concentrated substances are hazardous, and this one is "
                      "dilute", "correct": False,
             "why": "Oven cleaner is sold ready to use and is hazardous as it "
                    "comes."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s32",
        "band": "standard",
        "text": "A grower limes an acidic field, overshoots, and ends with soil at pH"
                " 9 that the crop will not grow in. Describe what should have been"
                " done differently.",
        "options": [
            {"text": "Spread the lime in stages, testing the pH as they went",
             "correct": True},
            {"text": "Spread all the lime at once but water the field afterwards",
             "correct": False,
             "why": "Watering does not remove the alkali that has already been "
                    "spread across the soil."},
            {"text": "Used a stronger alkali so that less of it was needed",
             "correct": False,
             "why": "A stronger alkali overshoots more easily, not less, and would "
                    "damage the soil as well."},
            {"text": "Waited for rain to make the field acidic again before "
                      "liming", "correct": False,
             "why": "Rain is very close to neutral and cannot be relied on to "
                    "acidify a field."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h17",
        "band": "harder",
        "text": "A bottle with no label is found in the cleaning cupboard. A student"
                " records it as an alkali. Evaluate that.",
        "options": [
            {"text": "Sound, because everything kept in a cleaning cupboard is "
                      "alkaline", "correct": False,
             "why": "Descalers and toilet cleaners are acids and live in the same "
                    "cupboard."},
            {"text": "Unsound, because where a bottle is kept is a guess and not "
                      "a test", "correct": True},
            {"text": "Sound, because an alkali is the only thing that shifts "
                      "grease", "correct": False,
             "why": "Alkalis are good at grease, but that does not make every "
                    "cleaner one."},
            {"text": "Unsound, because cleaning products are always neutral to "
                      "protect the user", "correct": False,
             "why": "Cleaning products sit right across the scale, and some of "
                    "them are the harshest substances in a house."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h18",
        "band": "harder",
        "text": "To identify two unlabelled colourless liquids, a student proposes"
                " leaving both out in open dishes and seeing which disappears first."
                " Evaluate the plan.",
        "options": [
            {"text": "Sound, because an acid evaporates faster than an alkali does",
             "correct": False,
             "why": "There is no such rule, and both bottles here are mostly "
                    "water."},
            {"text": "Sound, because whatever is left behind will be the alkali",
             "correct": False,
             "why": "Both would leave something behind, so the residue names "
                    "neither of them."},
            {"text": "Unsound, because it tests a physical property and not what "
                      "each does", "correct": True},
            {"text": "Unsound, because nothing dissolved in water can ever be "
                      "left behind", "correct": False,
             "why": "Evaporating a solution does leave the dissolved substance "
                    "behind; that is not the flaw."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h19",
        "band": "harder",
        "text": "A student argues that an indigestion medicine should keep being taken"
                " until the stomach reads pH 9, so that no acid at all is left."
                " Evaluate.",
        "options": [
            {"text": "Sound, because an alkaline stomach cannot give indigestion",
             "correct": False,
             "why": "A stomach pushed past 7 is a new problem rather than a cure "
                    "for the old one."},
            {"text": "Unsound, because only the excess acid needs cancelling",
             "correct": True},
            {"text": "Sound, because a medicine works better the more of it is "
                      "taken", "correct": False,
             "why": "Overshooting a target is not the same as working better."},
            {"text": "Unsound, because a mild alkali cannot change the pH of a "
                      "stomach", "correct": False,
             "why": "It can and does; that is what the tablet is sold to do."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h20",
        "band": "harder",
        "text": "A liquid has no effect at all on an indicator, and a student concludes"
                " it must be pure water. Evaluate.",
        "options": [
            {"text": "Sound, because only water gives no colour change at all",
             "correct": False,
             "why": "Any neutral solution leaves an indicator where it started."},
            {"text": "Sound, because an indicator identifies every substance it "
                      "meets", "correct": False,
             "why": "An indicator reports which side of 7 a solution is on and "
                    "nothing more."},
            {"text": "Unsound, because salt solution is neutral as well",
             "correct": True},
            {"text": "Unsound, because pure water turns an indicator green rather "
                      "than leaving it", "correct": False,
             "why": "The point is that a neutral liquid gives a neutral reading, "
                    "whatever colour that is."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h21",
        "band": "harder",
        "text": "A student writes that an alkali is just an acid with a higher pH."
                " Evaluate that statement.",
        "options": [
            {"text": "Sound, because both are measured on one scale from 0 to 14",
             "correct": False,
             "why": "Sharing a scale does not make two opposite kinds of "
                    "substance the same thing."},
            {"text": "Sound, because adding water to an acid raises its pH until "
                      "it is alkaline", "correct": False,
             "why": "Water moves a reading towards 7 and never takes it past."},
            {"text": "Unsound, because an alkali is a different kind of substance "
                      "altogether", "correct": True},
            {"text": "Unsound, because an alkali has a lower pH than an acid does",
             "correct": False,
             "why": "That has the scale the wrong way round: alkalis read above "
                    "7."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h22",
        "band": "harder",
        "text": "A technician is told to store bottles so that a single dropped bottle"
                " cannot cause a second accident. Suggest a rule, with a reason.",
        "options": [
            {"text": "Keep acids and alkalis on separate shelves, since a mixed "
                      "spill reacts", "correct": True},
            {"text": "Keep every bottle in one place, so that a spill is always "
                      "found quickly", "correct": False,
             "why": "Putting everything together is what allows one spill to "
                    "reach the next bottle."},
            {"text": "Keep the acids above the alkalis, since acid is the heavier "
                      "of the two", "correct": False,
             "why": "Weight is not the issue, and a bottle falling from a high "
                    "shelf is worse rather than better."},
            {"text": "Keep the dilute bottles apart from each other, as those are "
                      "the reactive ones", "correct": False,
             "why": "Dilute bottles are the mild ones; it is the pairing of "
                    "opposites that matters."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h23",
        "band": "harder",
        "text": "Milk of magnesia is a cloudy mixture in which most of the magnesium"
                " hydroxide never dissolves. Explain how it can still cancel stomach"
                " acid.",
        "options": [
            {"text": "The cloudiness dissolves as soon as it is swallowed",
             "correct": False,
             "why": "It stays a suspension in the stomach; it does not become a "
                    "solution on the way down."},
            {"text": "A base cancels acid whether or not it dissolves first",
             "correct": True},
            {"text": "The stomach acid dissolves it, so it is an alkali after all",
             "correct": False,
             "why": "It reacts with the acid rather than dissolving in water, "
                    "which is what the word alkali asks for."},
            {"text": "Only the dissolved part does anything, so the rest is added "
                      "for taste", "correct": False,
             "why": "The undissolved solid is the part doing most of the work as "
                    "the acid meets it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h24",
        "band": "harder",
        "text": "A student says the pH of a solution depends on how much of it you"
                " have. Evaluate.",
        "options": [
            {"text": "Sound, because a bigger volume of the same acid reads further "
                      "away from 7", "correct": False,
             "why": "A larger volume of the same acid reads exactly what a small "
                    "sample of it reads."},
            {"text": "Sound, because a small sample always reads closer to 7",
             "correct": False,
             "why": "A sample reads what the solution reads, whatever its size."},
            {"text": "Unsound, because pH describes each cm³ rather than the whole "
                      "amount", "correct": True},
            {"text": "Unsound, because pH depends only on which acid was used",
             "correct": False,
             "why": "How much water it has been mixed with matters as well, which "
                    "is what diluting changes."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h25",
        "band": "harder",
        "text": "A bottle is advertised as containing no acid and therefore being"
                " gentle on the hands. Evaluate the claim.",
        "options": [
            {"text": "Sound, because acids are the substances that attack skin",
             "correct": False,
             "why": "Strong alkalis attack skin as badly, and often without "
                    "warning."},
            {"text": "Sound, because anything that is not an acid is neutral",
             "correct": False,
             "why": "A substance that is not an acid may be alkaline, which is a "
                    "third possibility."},
            {"text": "Unsound, because a strong alkali is at least as harsh",
             "correct": True},
            {"text": "Unsound, because every cleaning product contains an acid "
                      "somewhere", "correct": False,
             "why": "Many contain no acid at all; that is not what is wrong with "
                    "the claim."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h26",
        "band": "harder",
        "text": "Battery acid and lemon juice are both acids. Compare them: state one"
                " thing that is true of both and one thing that separates them.",
        "options": [
            {"text": "Both sit below 7, but only one attacks skin and metal on "
                      "contact", "correct": True},
            {"text": "Both attack metal, but only one of them sits below 7",
             "correct": False,
             "why": "Lemon juice is well below 7, and it does not eat through "
                    "metal the way battery acid does."},
            {"text": "Both are safe to drink, but only one is used in a car",
             "correct": False,
             "why": "Battery acid would do terrible damage to anyone who "
                    "swallowed it."},
            {"text": "Both sit above 7, but only one of them tastes sharp",
             "correct": False,
             "why": "No acid sits above 7; that side of the scale belongs to the "
                    "alkalis."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h27",
        "band": "harder",
        "text": "First-aid instructions for an alkali splash say to keep rinsing for a"
                " long time, even once it feels fine. Explain why.",
        "options": [
            {"text": "Because rinsing turns the alkali into a neutral substance",
             "correct": False,
             "why": "Water washes the alkali away rather than cancelling it out."},
            {"text": "Because an alkali gives no pain to say it is still there",
             "correct": True},
            {"text": "Because an alkali only starts to act several hours after it "
                      "lands", "correct": False,
             "why": "It begins attacking straight away; what is missing is the "
                    "warning."},
            {"text": "Because cold water stops any chemical reaction on the skin "
                      "completely", "correct": False,
             "why": "Cooling slows a reaction down; it does not stop what has not "
                    "been washed off."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h28",
        "band": "harder",
        "text": "One student spills 1 cm³ of pH 1 acid and another spills 100 cm³ of"
                " pH 4 acid. Explain why the second spill may be the bigger job.",
        "options": [
            {"text": "Because a pH 4 acid attacks a bench faster than a pH 1 acid",
             "correct": False,
             "why": "A pH 1 acid is the fiercer of the two by a long way."},
            {"text": "Because a large volume spreads further and there is far "
                      "more of it", "correct": True},
            {"text": "Because pH 4 is on the alkaline side and mixes with the "
                      "bench", "correct": False,
             "why": "pH 4 is acidic; alkaline means a reading above 7."},
            {"text": "Because only volume matters when an acid is spilled",
             "correct": False,
             "why": "How fierce the acid is matters too, which is why the small "
                    "spill is not harmless."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h29",
        "band": "harder",
        "text": "Four of the eight bottles sorted on the bench are things a person"
                " eats, drinks or already has inside them. Explain what that"
                " arrangement is there to show.",
        "options": [
            {"text": "That everything a person eats is on the acid side of 7",
             "correct": False,
             "why": "One of the four is an indigestion tablet, which is alkaline."},
            {"text": "That the pH scale only applies to substances in a "
                      "laboratory", "correct": False,
             "why": "The whole point of the bench is that the scale describes "
                    "ordinary things."},
            {"text": "That being acidic and being dangerous are separate "
                      "questions", "correct": True},
            {"text": "That anything safe to eat must be close to neutral",
             "correct": False,
             "why": "Lemon juice is about pH 2 and is drunk every day."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h30",
        "band": "harder",
        "text": "Explain why chemists define an alkali as a base that dissolves in"
                " water rather than as a base that is dangerous.",
        "options": [
            {"text": "Because dissolving is what decides whether it can be tested "
                      "and used in solution", "correct": True},
            {"text": "Because every base that dissolves in water is dangerous to "
                      "handle", "correct": False,
             "why": "An indigestion tablet dissolves and is mild enough to "
                    "swallow."},
            {"text": "Because a base that does not dissolve cannot cancel an acid "
                      "out", "correct": False,
             "why": "An insoluble base neutralises acid perfectly well, which is "
                    "why the word base exists."},
            {"text": "Because how dangerous a base is can be read off the pH scale "
                      "and its solubility cannot", "correct": False,
             "why": "pH measures how acidic or alkaline something is, not how "
                    "dangerous it is."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h31",
        "band": "harder",
        "text": "One field reads pH 4.5 and another reads pH 6.5. Explain why the"
                " first needs more lime than the second.",
        "options": [
            {"text": "Because it is further from neutral, so more acid has to be "
                      "cancelled", "correct": True},
            {"text": "Because lime works more slowly on a soil that is strongly "
                      "acidic", "correct": False,
             "why": "Speed is not what sets the amount; how far the soil has to "
                    "be moved is."},
            {"text": "Because a lower pH means the soil holds less water for the "
                      "lime", "correct": False,
             "why": "Water content is a separate matter and is not what the "
                    "reading reports."},
            {"text": "Because lime is only able to raise a pH by one step at a "
                      "time", "correct": False,
             "why": "There is no such limit; enough lime moves a soil as far as "
                    "you like."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h32",
        "band": "harder",
        "text": "A drink at pH 2 is defended on the grounds that the stomach is at pH 2"
                " anyway, so it can do no harm anywhere. Evaluate.",
        "options": [
            {"text": "Sound, because a liquid cannot harm what already matches it",
             "correct": False,
             "why": "Matching one part of the body says nothing about the parts "
                    "it passes on the way."},
            {"text": "Sound, because the stomach neutralises the drink before it "
                      "is swallowed", "correct": False,
             "why": "The stomach comes after the mouth and throat, not before "
                    "them."},
            {"text": "Unsound, because the stomach is lined for acid and the "
                      "mouth is not", "correct": True},
            {"text": "Unsound, because a drink at pH 2 is more acidic than "
                      "stomach acid", "correct": False,
             "why": "The two readings are the same, so that is not where the "
                    "argument fails."},
        ],
        "figure": None,
    },
]
